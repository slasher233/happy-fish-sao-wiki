"""生成英雄图鉴页面（docs/heroes/*.md）。

数据来源（全部来自本图，非参考站）：
  note_log/recon/heroes.tsv        —— 英雄名单与 Q/W/E/R/F/D 技能绑定（子智能体取证）
  note_log/wiki_data/units.json    —— 英雄单位对象字段
  note_log/wiki_data/abilities.json—— 技能对象字段
  note_log/wiki_data/items.json    —— 反查专属装备
  note_log/index/field_dict_*.tsv  —— 字段中文化
  patch_plan/data/hero_skill_text.csv  —— 私有需求单里的技能说明原文（按 ability_code 索引）
  patch_plan/data/hero_ability_data.csv—— 私有需求单里的可改数值项（按 ability_code 索引）

只读脚本：不修改地图，只写 wiki/docs。
"""
from __future__ import annotations

import csv
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wiki_common import (  # noqa: E402
    DOCS, INDEX_DIR, MAP_SHA256, MAP_VERSION, MEMBER_SHA, RECON_DIR, W, WIKI_DATA,
    blank, clean_inline, clean_text, code, esc, link, load_json, obj_code, safe_name,
    source_footer, table, write_page,
)

HERO_OUT = os.path.join(DOCS, "heroes")
HERO_TSV = os.path.join(RECON_DIR, "heroes.tsv")
UNITS_JSON = os.path.join(WIKI_DATA, "units.json")
ABIL_JSON = os.path.join(WIKI_DATA, "abilities.json")
ITEMS_JSON = os.path.join(WIKI_DATA, "items.json")
ABIL_FIELDS = os.path.join(INDEX_DIR, "field_dict_abilities.tsv")
EXCL_JSON = os.path.join(RECON_DIR, "hero_exclusive.json")
# 私有需求单仓库（只读引用；wiki 不写这里）
PATCH_DATA = os.path.join(W, "patch_plan", "data")
SKILL_TEXT_CSV = os.path.join(PATCH_DATA, "hero_skill_text.csv")
ABILITY_DATA_CSV = os.path.join(PATCH_DATA, "hero_ability_data.csv")

SLOTS = ["Q", "W", "E", "R", "F", "D", "T"]
ATTR_ZH = {"STR": "筋力（力量）", "AGI": "敏捷", "INT": "体力（智力）"}
ATTR_SHORT = {"STR": "筋力", "AGI": "敏捷", "INT": "体力"}
SKILL_FIELDS = {
    "Cool": "冷却",
    "Cost": "魔法消耗",
    "Rng": "施法距离",
    "Area": "作用范围",
    "Dur": "持续时间",
    "HeroDur": "英雄持续时间",
    "Cast": "施法前摇",
    "levels": "等级数",
    "reqLevel": "学习需求等级",
}


def load_tsv(path: str) -> list[dict]:
    with open(path, encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def load_field_dict(path: str) -> dict:
    out = {}
    for r in load_tsv(path):
        out[r["field_id"]] = r
    return out


def load_csv(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def load_skill_text(path: str) -> dict:
    """`ability_code` → 需求单行（说明原文）。

    **必须按 `ability_code` 索引**：两张需求单表按 `(hero, slot)` 并不一一对应
    （存在同一 (hero, slot) 换过技能 code、以及同一 code 挂在不同键位的情况），
    按位置对应会串行。
    """
    out = {}
    for r in load_csv(path):
        c = (r.get("ability_code") or "").strip()
        if c:
            out.setdefault(c, r)
    return out


def load_ability_data(path: str) -> dict:
    """`ability_code` → [可改数值行]（保持 CSV 行序，只取 `slk_col == "Data"`）。"""
    out: dict[str, list] = {}
    for r in load_csv(path):
        if (r.get("slk_col") or "").strip() != "Data":
            continue
        c = (r.get("ability_code") or "").strip()
        if c:
            out.setdefault(c, []).append(r)
    return out


def first(fields: dict, key: str):
    rows = fields.get(key)
    if not rows:
        return None
    for r in rows:
        if r.get("level") in (0, None, 1, "0", "1"):
            return r.get("value")
    return rows[0].get("value")


def v(x) -> str:
    if x is None:
        return ""
    if isinstance(x, float):
        if abs(x - round(x)) < 1e-6:
            return str(int(round(x)))
        return f"{x:.4g}"
    return str(x)


# 主动信号字段：**必须含 Area**——只靠 Area 就能认出 5 条纯范围技能
# （例如 优库里伍德 的 D 技能 `Z0EK` 是 Area=600、Cost/Cool/Rng 全 0）。
ACTIVE_SIGNALS = ("Cost", "Cool", "Rng", "Area")


def _num(x):
    s = "" if x is None else str(x).strip()
    if s == "":
        return None
    try:
        return float(s)
    except ValueError:
        return None


def has_active_signal(fields: dict) -> bool:
    return any((_num(first(fields, k)) or 0) > 0 for k in ACTIVE_SIGNALS)


def skill_kind(fields: dict) -> str:
    """技能类型三态：主动 / 被动 / 未判定（证据不足）。

    - 任一主动信号 > 0（`Cost` / `Cool` / `Rng` / `Area`）→ 主动
    - 无主动信号但对象带 `Order` 字段 → 被动
    - 四种信号全 0/缺失且 `Order` 也缺 → 未判定（对象数据里没有可用证据，
      **不等于**游戏里一定是被动）
    """
    if has_active_signal(fields):
        return "主动"
    if first(fields, "Order") not in (None, ""):
        return "被动"
    return "未判定"


def is_unreachable(h: dict) -> bool:
    """`heroes.tsv` 的 `reachable` 实际取值是 `NO(地图上无此单位)` / `yes(legacy，…)`，
    所以必须 `startswith("no")`，不能拿 `== "no"` 比大小写（审计问题 W010）。"""
    return str(h.get("reachable") or "").lower().startswith("no")


def hero_scope(heroes: list[dict]) -> tuple[int, int, int]:
    """(可选, 地图上无此单位, 英雄数据条数)。

    口径必须与 `docs/index.md`、`docs/heroes/index.md`、`docs/skills/index.md` 三处一致
    （审计问题 W010）；`build_site.py` 里有一份等价实现（wiki_common.py 不许改）。
    """
    n_no = sum(1 for h in heroes if is_unreachable(h))
    return len(heroes) - n_no, n_no, len(heroes)


def scope_text(heroes: list[dict]) -> str:
    ok, no, total = hero_scope(heroes)
    return (f"**{total}** 条英雄数据 = **{ok}** 个可选 + **{no}** 个地图上无此单位"
            f"（`note_log/recon/heroes.tsv` 共 {total} 行）")


def parse_slot(raw: str) -> tuple[str, str]:
    """'Z1US(绯雪-Q1)' → ('Z1US', '绯雪-Q1')"""
    raw = (raw or "").strip()
    if not raw:
        return "", ""
    m = re.match(r"^([0-9A-Za-z]{4})\s*\(([^)]*)\)", raw)
    if m:
        return m.group(1), m.group(2).strip()
    return raw.split()[0], ""


def iter_bindings(h: dict):
    """英雄的 (键位, 技能 code, 技能名) —— 按 Q/W/E/R/F/D/T 顺序。"""
    for slot in SLOTS:
        raw = h.get(slot)
        if not raw:
            continue
        scode, sbind = parse_slot(str(raw))
        if scode:
            yield slot, scode, sbind


def item_page_map() -> dict:
    """物品 code → (分类, docs/items 下的相对路径)"""
    out = {}
    root = os.path.join(DOCS, "items")
    if not os.path.isdir(root):
        return out
    for cat in os.listdir(root):
        d = os.path.join(root, cat)
        if not os.path.isdir(d):
            continue
        for fn in os.listdir(d):
            if not fn.endswith(".md"):
                continue
            c = fn.split("_")[0]
            if len(c) == 4:
                out.setdefault(c, (cat, f"{cat}/{fn}"))
    return out


def item_link(icode: str, item_pages: dict) -> tuple[str, str]:
    """物品 code → (分类, markdown 链接)。

    `docs/items` 下的文件名可能含空格与括号，裸拼 `[label](path)` 会被
    Python-Markdown 在空格处截断（审计问题 W024）→ 统一走 `wiki_common.link()`
    （尖括号包住目标 + 百分号编码；MkDocs 解析时会 `unquote`，所以仍能命中真实文件）。
    """
    cat, rel = item_pages.get(icode, ("?", ""))
    return cat, (link(f"../items/{rel}", code(icode)) if rel else code(icode))


def render_skill(slot: str, scode: str, sbind: str, abils: dict, fdict: dict,
                 stext: dict, adata: dict) -> list[str]:
    a = abils.get(scode)
    # 折叠块标题的 sbind 直接取自 heroes.tsv 的括号文本，里面带 WC3 颜色码
    # （`|cffffcc99碎骨拳|r`）→ 必须走 clean_inline，否则 |c/|r 原样落进 markdown
    # （审计问题 W004）。
    sbind_clean = clean_inline(sbind)
    head = f"{slot} · {sbind_clean or scode}"
    if not a:
        return [f'??? note "{head}"', "", "    （技能对象不存在）", "",
                "    #### 说明（原文）", "", "    原图该技能对象没有说明文字", "",
                "    #### 可改数值项", "", "    _（技能对象不存在）_", ""]
    f = a["fields"]
    anam = clean_inline(first(f, "Name"))
    tip = clean_text(first(f, "Tip"))
    ubertip = clean_text(first(f, "Ubertip"))
    hot = clean_inline(first(f, "Hotkey"))
    bcode = str(a.get("base") or "").replace("\x00", "")
    meta = [f"**技能 ID**：`{scode}`"]
    if a.get("base_name"):
        # 原型名同样可能带颜色码（如 `黑雪姬/|cffff00ff模仿数据|r`）
        meta.append(f"**原型**：`{bcode}`（{clean_inline(a['base_name'])}）")
    else:
        meta.append(f"**原型**：`{bcode}`")
    if hot:
        meta.append(f"**热键**：`{hot}`")
    for k, zh in SKILL_FIELDS.items():
        val = first(f, k)
        if val not in (None, ""):
            meta.append(f"**{zh}**：{v(val)}")
    lines = [f'??? note "{head}"', "", "    " + "　·　".join(meta), ""]
    if anam and anam != sbind_clean:
        lines.append(f"    对象名：{esc(anam)}")
        lines.append("")
    if tip:
        lines.append(f"    **提示**：{esc(tip)}")
        lines.append("")
    if ubertip:
        for part in ubertip.split("\n"):
            lines.append(f"    {esc(part)}" if part.strip() else "")
        lines.append("")
    # Data 字段（技能真值数值）
    drows = []
    for ini_key, rows in f.items():
        for r in rows:
            fid = r.get("field", "")
            d = fdict.get(fid, {})
            if d.get("ini_key") == "Data":
                drows.append([
                    code(fid),
                    esc(d.get("zh_label") or ""),
                    esc(v(r.get("value"))),
                    blank(r.get("level"), ""),
                ])
    if drows:
        lines.append("    #### 数据字段（技能真值）")
        lines.append("")
        for ln in table(["字段", "含义", "值", "等级"], drows).split("\n"):
            lines.append(f"    {ln}" if ln.strip() else "")
        lines.append("")

    # ── 说明（原文）：patch_plan\data\hero_skill_text.csv 的 cur_ubertip ──
    st = stext.get(scode) or {}
    raw_ub = st.get("cur_ubertip") or ""
    lines.append("    #### 说明（原文）")
    lines.append("")
    if raw_ub.strip():
        # clean_text 把 `|n` 换成真换行、清掉 `|c…|r`（需求单里目前没有颜色码，防御性处理）
        for part in clean_text(raw_ub).split("\n"):
            lines.append(f"    {esc(part)}" if part.strip() else "")
    else:
        lines.append("    原图该技能对象没有说明文字")
    lines.append("")

    # ── 可改数值项：patch_plan\data\hero_ability_data.csv（按 ability_code 索引）──
    arows = []
    for r in adata.get(scode, []):
        arows.append([
            blank((r.get("level") or "").strip(), ""),
            code((r.get("field") or "").strip()),
            esc(r.get("zh") or "") or "—",
            esc(r.get("cur_value") or "") or "—",
            esc(r.get("note") or "") or "—",
        ])
    lines.append("    #### 可改数值项")
    lines.append("")
    if arows:
        for ln in table(["等级", "字段", "中文名", "现值", "说明"], arows).split("\n"):
            lines.append(f"    {ln}" if ln.strip() else "")
    else:
        lines.append("    _（需求单里没有本技能的可改数值项）_")
    lines.append("")
    lines.append("    改数值请到私有需求单仓库 `patch_plan\\data\\hero_ability_data.csv` 填 `new_value`，"
                 "或用「口语需求」Issue 写人话（我会用 `note_log\\tools\\nl_request.py` 定位）。")
    lines.append("")
    return lines


def render_hero(h: dict, unit: dict, abils: dict, fdict: dict, item_pages: dict,
                item_ub: dict, excl: dict, stext: dict, adata: dict) -> str:
    hcode = h["code"]
    hname = clean_inline(h.get("name")) or hcode
    proper = clean_inline(h.get("proper_name"))
    title = f"{hname}（{proper}）" if proper and proper != hname else hname
    uf = (unit or {}).get("fields", {})
    name_in_table = f"# {hcode} · {title}"
    lines = [name_in_table, ""]
    reach = str(h.get("reachable") or "")
    meta = [
        # 主属性为空时要说清「是数据里没有」，不能只留一个横杠（审计问题 W022）
        f"**主属性**：{ATTR_SHORT.get((h.get('primary') or '').upper()) or '未在对象数据中设置（`heroes.tsv` 的 `primary` 为空）'}",
        f"**英雄 ID**：`{hcode}`",
        f"**原型**：`{clean_inline(h.get('base'))}`",
    ]
    if is_unreachable(h):
        # `reachable` 是 `NO(地图上无此单位)`，拿 `== "no"` 比会漏判（审计问题 W010）
        meta.append(f"**可选性**：❌ 地图上无此单位（`reachable={reach}`）")
    elif reach and not reach.strip().lower() == "yes":
        meta.append(f"**可选性**：✅ 可选（`reachable={reach}`）")
    lines.append("> " + "\u3000·\u3000".join(meta))
    lines.append("")
    if is_unreachable(h):
        lines += [
            '!!! warning "本英雄在地图上不可选"',
            "",
            f"    `note_log/recon/heroes.tsv` 的 `reachable` 字段为 `{reach}`"
            f"（该行 `portinit_line={h.get('portinit_line') or '—'}`），"
            f"且选人注册表 `PH_PortInit`（`war3map.j`）**不包含** `{hcode}`。",
            "",
            "    本页数据全部来自对象文件（`war3map.w3u`）：**对象存在 ≠ 游戏里能选到**，"
            "这个英雄在选人区不会出现。",
            "",
        ]

    lines += ["## 基础属性", ""]
    # heroes.tsv 的列名与对象字段名不同，这里做映射（对象字段优先，名单列兜底）
    COL2TSV = {
        "ustr": "str", "ustp": "str_per_lv",
        "uagi": "agi", "uagp": "agi_per_lv",
        "uint": "int", "uinp": "int_per_lv",
        "uhpm": "hp_base", "umpm": "mana_base", "umpi": "mana_init",
        "udef": "armor", "uarm": "armor_type", "umvs": "move_speed",
        "ulev": "init_level", "uhab": "uhab",
    }

    def ufield(key):
        val = first(uf, key)
        if val in (None, ""):
            val = h.get(COL2TSV.get(key, key))
        return val

    _EMPTY_MARKS = ("", "(空)", "空", "NULL", "None", "null", "—")

    def vcell(key) -> str:
        """空值统一写「—（对象数据中此字段为空）」，不留白也不泄漏 `(空)` 这类抽取占位符
        （审计问题 W021 / W023）。"""
        s = v(ufield(key))
        return "—（对象数据中此字段为空）" if s in _EMPTY_MARKS else s

    rows = [
        [f"初始{ATTR_ZH.get('STR', '筋力')}", vcell("ustr"), f"+{vcell('ustp')} / 级"],
        ["初始敏捷", vcell("uagi"), f"+{vcell('uagp')} / 级"],
        [f"初始{ATTR_ZH.get('INT', '体力')}", vcell("uint"), f"+{vcell('uinp')} / 级"],
        ["最大生命值", vcell("uhpm"), "—"],
        ["最大魔法值", vcell("umpm"), "—"],
        ["初始魔法值", vcell("umpi"), "—"],
        ["护甲", vcell("udef"), "—"],
        ["护甲类型", blank(clean_inline(ufield("uarm"))) if clean_inline(ufield("uarm")) not in _EMPTY_MARKS else "—（对象数据中此字段为空）", "—"],
        ["移动速度", vcell("umvs"), "—"],
        ["初始等级", vcell("ulev"), "—"],
        ["英雄属性成长技能", code(clean_inline(ufield("uhab"))) if clean_inline(ufield("uhab")) not in _EMPTY_MARKS else "—（对象数据中此字段为空）", "—"],
    ]
    lines.append(table(["属性", "初始值", "成长"], rows))
    lines.append("")
    # 这句原来硬编码断言「59 个英雄的 uhab 统一为 Z063/Z064/Z065」，对 uhab 不同的英雄是错的
    # （审计问题 W009）→ 改为按本页实际取值分别说明。
    uhab = clean_inline(ufield("uhab")).strip("`").strip()
    lines.append("> 本图把「力量」写作**筋力**、把「智力」写作**体力**（依据：对象数据里 `ustr`/`uint` 的中文标注与说明文本用语）。")
    if uhab and uhab not in _EMPTY_MARKS:
        if uhab in ("Z063", "Z064", "Z065"):
            lines.append(f"> 本页「英雄属性成长技能」= `{uhab}`（本图多数英雄用的 `Z063`/`Z064`/`Z065` 三件套之一）。")
        else:
            lines.append(f"> ⚠️ 本页「英雄属性成长技能」= `{uhab}`，**不是**多数英雄用的 `Z063`/`Z064`/`Z065` 三件套，"
                         "该英雄的属性成长走的是别的技能对象。")
    else:
        lines.append("> 本页 `uhab`（英雄属性成长技能）在对象数据里为空，属性成长技能未在对象数据中体现。")
    lines.append("")

    lines += ["## 技能取得", ""]
    lines.append("_本图技能对象全部只有 1 级（`alev=1`，`arlv` 多为 1），**解锁与升级由触发器控制**："
                 "对象数据里没有「解锁等级」字段（`reqLevel` 多为 0），所以下表不写等级，"
                 "只写「解锁等级由 `war3map.j` 触发器决定」。要考证某个技能，可在 `war3map.j` 里搜技能 ID "
                 "（例如 `Z1UR`）与 `SetUnitAbilityLevel` / `SelectHeroSkill` 附近的判断。_")
    lines.append("")
    srows = []
    bindings = list(iter_bindings(h))
    for slot, scode, sbind in bindings:
        a = abils.get(scode)
        aub = clean_text(first(a["fields"], "Ubertip")) if a else ""
        kind = skill_kind(a["fields"]) if a else "未判定"
        # 摘要在 60 字处截断时要补省略号，否则读者以为原文就断在半句（审计问题 W015）
        summary = aub[:60] + ("…（完整说明见下面技能数据块）" if len(aub) > 60 else "")
        if not summary.strip():
            # 空摘要要给出路，不能留白（审计问题 W031）
            summary = "（对象数据没有说明文字；数值与字段见下面技能数据块）"
        srows.append([f"**{slot}**", code(scode), esc(sbind) or "—", kind,
                      "由触发器控制（对象无此字段）", esc(summary)])
    if srows:
        lines.append(table(["键位", "技能 ID", "技能名", "类型", "解锁等级", "说明摘要"], srows))
        lines.append("")
        lines.append("> **「说明摘要」列是 `Ubertip` 的前 60 字**（截断处有 `…`）；完整原文与可改数值见下面每个技能的折叠块。")
        lines.append("")
        lines.append("> **类型判定（三态）**：`Cost` / `Cool` / `Rng` / `Area` 任一 > 0 → **主动**；"
                     "无主动信号但对象带 `Order` 字段 → **被动**；"
                     "四种信号全 0/缺失且 `Order` 也缺 → **未判定（证据不足）**，"
                     "只说明对象数据里没有可用证据，**不等于**游戏里一定是被动。")
    else:
        lines.append("_（未在名单里绑定技能）_")
    lines.append("")

    lines += [f"## {MAP_VERSION} 技能数据", ""]
    if bindings:
        for slot, scode, sbind in bindings:
            lines += render_skill(slot, scode, sbind, abils, fdict, stext, adata)
    else:
        lines.append("_（本英雄在 `heroes.tsv` 里没有绑定任何技能键位；"
                     "判定依据是 `heroes.tsv` 的 Q/W/E/R/F/D/T 列，见页脚数据来源。）_")
        lines.append("")

    # 专属装备：以触发器白名单函数 EXEQ_Allowed 的证据为准
    ex = (excl.get("heroes") or {}).get(hcode) if excl else None
    ex_items = (ex or {}).get("items") or []
    lines += ["## 专属装备（触发器证据）", ""]
    if ex_items:
        lines.append("本图**不存在**哈希表形式的「英雄→物品」配对；「专属」由唯一白名单函数 "
                     "`EXEQ_Allowed(unit, integer)`（`war3map.j:87157-87312`）判定，拾取时由 "
                     "`EXEQ_InventoryEvent`（`war3map.j:88094-88112`）强制移除不合规物品。"
                     "下表直接来自该函数的返回值：")
        lines.append("")
        irows = []
        for it in ex_items:
            ic = it.get("item_code") or ""
            cat, label = item_link(ic, item_pages)
            gate = it.get("gate")
            gate_txt = {
                "unit_type": "英雄类型",
                "legacy_unit_var": "英雄类型（旧版硬编码触发器）",
                "player_nickname": "⚠️ 玩家昵称",
            }.get(gate, gate or "—")
            ev = it.get("evidence") or {}
            irows.append([label, blank(clean_inline(it.get("item_name"))), gate_txt,
                          f"L{ev.get('line')}" if ev.get("line") else "—"])
        lines.append(table(["物品", "名称", "判定方式", "触发器行号（`war3map.j`）"], irows))
        lines.append("")
    else:
        n_types = (excl or {}).get("_n_types")
        n_tot = (excl or {}).get("_n_total")
        n_items = (excl or {}).get("_n_items")
        lines.append("_`EXEQ_Allowed` 的白名单里**没有本英雄**的条目，也没有对应的旧版硬编码触发器。_")
        lines.append("")
        lines.append(f"> 统计口径（自动生成，随数据变化）：本图 **{n_tot if n_tot else 60}** 条英雄数据里，"
                     f"能解析出专属装备证据的有 **{n_types if n_types is not None else 34}** 个英雄类型、"
                     f"共 **{n_items if n_items is not None else 41}** 件专属物品；"
                     "判定依据是 `war3map.j` 里 `EXEQ_Allowed` 的返回值与旧版硬编码触发器。")
        lines.append("")
    lines.append("> ⚠️ 按玩家昵称判定专属的物品（`J0H6`/`J0L4`/`K001`/`K002`/`K004`）无法从脚本归属到某个英雄类型，"
                 "本页不会把它们算作本英雄的专属。")
    lines.append("")

    # 说明文本里提到英雄名的物品（弱证据，仅作线索）
    hits = []
    for icode, text in item_ub.items():
        if hname and len(hname) >= 2 and hname in text:
            hits.append(icode)
    if hits:
        lines += ["## 相关物品（说明文本提到本英雄）", "",
                  "下面这些物品的游戏内说明里出现了本英雄的名字。**这只是文本匹配，不等于专属绑定**，"
                  "仅供参考；真实专属关系以上一节的触发器证据为准。", ""]
        irows = []
        for ic in sorted(hits):
            cat, label = item_link(ic, item_pages)
            irows.append([label, cat])
        lines.append(table(["物品", "分类"], irows))
        lines.append("")

    if h.get("evidence"):
        lines += ['??? quote "取证记录（子智能体只读勘查）"', "", f"    {esc(h['evidence'])}", ""]

    lines.append(source_footer([
        f"英雄单位对象来自 `war3map.w3u`（SHA256 `{MEMBER_SHA['war3map.w3u']}`），"
        f"技能对象来自 `war3map.w3a`（SHA256 `{MEMBER_SHA['war3map.w3a']}`）。"
        "技能绑定关系由 `war3map.j` 的 `PH_BindUnit` / `P2SV_FillAbilities` 取证得出。"
    ]))
    return "\n".join(lines)


def main() -> None:
    heroes = load_tsv(HERO_TSV)
    units = {obj_code(u): u for u in load_json(UNITS_JSON)}
    abils = {a["code"]: a for a in load_json(ABIL_JSON)}
    fdict = load_field_dict(ABIL_FIELDS)
    item_pages = item_page_map()
    item_ub = {}
    for it in load_json(ITEMS_JSON):
        item_ub[obj_code(it)] = clean_text(first(it["fields"], "Ubertip"))

    excl = {}
    if os.path.exists(EXCL_JSON):
        try:
            excl = load_json(EXCL_JSON)
        except Exception as e:  # noqa: BLE001
            print(f"  ! hero_exclusive.json 解析失败：{e}")
    else:
        print("  · hero_exclusive.json 尚不存在 → 专属装备章节只写「无证据」")
    n_ex = len((excl.get("heroes") or {}))
    # 供 render_hero 引用真实统计，避免页面里硬编码「34 / 60」这类会过期的断言（审计问题 W033/W031）
    excl["_n_types"] = n_ex
    excl["_n_total"] = len(heroes)
    n_ex_items = sum(len((v or {}).get("items") or []) for v in (excl.get("heroes") or {}).values())
    excl["_n_items"] = n_ex_items

    # 私有需求单（只读）：说明原文 + 可改数值项，两张表都按 ability_code 索引
    stext = load_skill_text(SKILL_TEXT_CSV)
    adata = load_ability_data(ABILITY_DATA_CSV)
    if not stext:
        print(f"  · 未找到 {SKILL_TEXT_CSV} → 「说明（原文）」写「没有说明文字」")
    if not adata:
        print(f"  · 未找到 {ABILITY_DATA_CSV} → 「可改数值项」全为空")
    print(f"  · 需求单：说明原文 {len(stext)} 条 ability_code；"
          f"可改数值项 {sum(len(x) for x in adata.values())} 行 / {len(adata)} 个 ability_code")

    os.makedirs(HERO_OUT, exist_ok=True)
    # 该目录完全由本脚本生成：先清掉旧 md，避免改名后留下陈旧页面（连同旧的 index.md 一起重建）
    import glob as _glob
    for stale in _glob.glob(os.path.join(HERO_OUT, "*.md")):
        try:
            os.remove(stale)
        except OSError:
            pass
    # 文件名去重：本图存在同名英雄（含未改色的重复名，如 H01J/H01K 同为「公会:命运之夜(four*king)」，
    # 以及 莉莉丝忒拉 / 雷电·忘川守·芽衣 各有一个不可达条目）。重名的加 _<code> 后缀，避免互相覆盖。
    base_counts = {}
    for h in heroes:
        base = safe_name(clean_inline(h.get("name")) or h["code"])
        base_counts[base] = base_counts.get(base, 0) + 1
    for h in heroes:
        hcode = h["code"]
        hname = clean_inline(h.get("name")) or hcode
        base = safe_name(hname)
        fn = f"{base}_{hcode}.md" if base_counts.get(base, 0) > 1 else base + ".md"
        h["file"] = fn
        write_page(os.path.join(HERO_OUT, fn),
                   render_hero(h, units.get(hcode), abils, fdict, item_pages, item_ub, excl,
                               stext, adata))

    # 英雄总览
    rows = []
    for h in sorted(heroes, key=lambda x: x["code"]):
        hname = clean_inline(h.get("name")) or h["code"]
        sk = []
        for slot in ("Q", "W", "E", "R", "F", "D"):
            c, _ = parse_slot(h.get(slot))
            sk.append(f"{slot}:{c}" if c else f"{slot}:—")
        rows.append([
            link(h["file"], code(h["code"])),
            esc(hname),
            esc(clean_inline(h.get("proper_name"))) or "—",
            ATTR_SHORT.get((h.get("primary") or "").upper()) or "未设置",
            # 单列标出可选性，不把 ⚠️ 塞在名称后面（审计问题 W030）
            "❌ 不可选" if is_unreachable(h) else "✅ 可选",
            "　".join(sk),
        ])
    n_ok, n_no, n_total = hero_scope(heroes)
    no_list = "、".join(f"`{h['code']}`"
                       for h in sorted(heroes, key=lambda x: x["code"]) if is_unreachable(h))
    legacy_list = "、".join(f"`{h['code']}`" for h in heroes
                          if str(h.get("reachable") or "").lower().startswith("yes")
                          and str(h.get("reachable") or "").strip().lower() != "yes")
    idx = ["# 英雄图鉴", "",
           f"共 {scope_text(heroes)}。"
           "开局在选人区把单位**双击**即可选中（触发器 `Lz` / `iy4`）。", "",
           "| 说明 | 内容 |", "| --- | --- |",
           f"| 可选英雄 | {n_ok}（另有 {n_no} 个地图上无此单位 → 合计 {n_total} 条数据） |",
           "| 选人方式 | 双击 `Player(15)` 所属的选人单位 |",
           "| 技能键位 | Q/W/E/R/F/D（对象数据 `abpx/abpy` 判定） |",
           f"| 地图上无此单位 | {no_list or '—'}（`PH_PortInit` 注册表不含这些 code，两页页内有 ⚠️ 警告） |",
           f"| `reachable` 带 legacy 备注但可选 | {legacy_list or '—'}（不在 `PH_PortInit` 注册表，计入上面 {n_ok} 个可选里） |",
           f"| 技能类型口径 | 主动 / 被动 / 未判定（证据不足）三态，见各页「技能取得」表下说明 |",
           f"| 有专属装备证据的英雄 | {n_ex} / {n_total}（判定函数 `EXEQ_Allowed`，`war3map.j:87157-87312`） |", "",
           table(["ID", "名称", "称号", "主属性", "可选", "技能绑定"], rows), ""]
    idx.append(source_footer())
    write_page(os.path.join(HERO_OUT, "index.md"), "\n".join(idx))
    write_page(os.path.join(HERO_OUT, ".pages"),
               "title: 英雄图鉴\nnav:\n  - index.md\n  - ...\n")
    print(f"英雄页：{len(heroes)} 个 → {HERO_OUT}")

    # ── 自检：三态分布与「标被动却带主动信号」的矛盾数（矛盾必须为 0）──
    dist = {"主动": 0, "被动": 0, "未判定": 0}
    contra = 0
    n_block = n_block_empty = n_note = n_note_empty = 0
    for h in heroes:
        for slot, scode, _ in iter_bindings(h):
            a = abils.get(scode)
            kind = skill_kind(a["fields"]) if a else "未判定"
            dist[kind] = dist.get(kind, 0) + 1
            if kind == "被动" and a and has_active_signal(a["fields"]):
                contra += 1
            if a:
                n_block += 1
                if not adata.get(scode):
                    n_block_empty += 1
            st = stext.get(scode) or {}
            n_note += 1
            if not (st.get("cur_ubertip") or "").strip():
                n_note_empty += 1
    print(f"技能类型三态：主动 {dist['主动']} / 被动 {dist['被动']} / 未判定 {dist['未判定']}"
          f" = {sum(dist.values())}；矛盾（标被动却带主动信号）{contra}")
    print(f"可改数值项技能块：{n_block} 个，其中表行为 0 的 {n_block_empty} 个")
    print(f"说明（原文）：{n_note} 块，其中写「没有说明文字」的 {n_note_empty} 块")
    print(f"英雄口径：{n_ok} 个可选 + {n_no} 个地图上无此单位 = {n_total} 条英雄数据")


if __name__ == "__main__":
    main()
