"""生成英雄图鉴页面（docs/heroes/*.md）。

数据来源（全部来自本图，非参考站）：
  note_log/recon/heroes.tsv        —— 英雄名单与 Q/W/E/R/F/D 技能绑定（子智能体取证）
  note_log/wiki_data/units.json    —— 英雄单位对象字段
  note_log/wiki_data/abilities.json—— 技能对象字段
  note_log/wiki_data/items.json    —— 反查专属装备
  note_log/index/field_dict_*.tsv  —— 字段中文化

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
    DOCS, INDEX_DIR, MAP_SHA256, MAP_VERSION, MEMBER_SHA, RECON_DIR, WIKI_DATA,
    blank, clean_inline, clean_text, code, esc, load_json, obj_code, safe_name,
    source_footer, table, write_page,
)

HERO_OUT = os.path.join(DOCS, "heroes")
HERO_TSV = os.path.join(RECON_DIR, "heroes.tsv")
UNITS_JSON = os.path.join(WIKI_DATA, "units.json")
ABIL_JSON = os.path.join(WIKI_DATA, "abilities.json")
ITEMS_JSON = os.path.join(WIKI_DATA, "items.json")
ABIL_FIELDS = os.path.join(INDEX_DIR, "field_dict_abilities.tsv")

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


def parse_slot(raw: str) -> tuple[str, str]:
    """'Z1US(绯雪-Q1)' → ('Z1US', '绯雪-Q1')"""
    raw = (raw or "").strip()
    if not raw:
        return "", ""
    m = re.match(r"^([0-9A-Za-z]{4})\s*\(([^)]*)\)", raw)
    if m:
        return m.group(1), m.group(2).strip()
    return raw.split()[0], ""


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


def render_skill(slot: str, scode: str, sbind: str, abils: dict, fdict: dict) -> list[str]:
    a = abils.get(scode)
    head = f"{slot} · {sbind or scode}"
    if not a:
        return [f'??? note "{head}"', "", "    （技能对象不存在）", ""]
    f = a["fields"]
    anam = clean_inline(first(f, "Name"))
    tip = clean_text(first(f, "Tip"))
    ubertip = clean_text(first(f, "Ubertip"))
    hot = clean_inline(first(f, "Hotkey"))
    meta = [f"**技能 ID**：`{scode}`"]
    if a.get("base_name"):
        meta.append(f"**原型**：`{a['base']}`（{a['base_name']}）")
    else:
        meta.append(f"**原型**：`{a['base']}`")
    if hot:
        meta.append(f"**热键**：`{hot}`")
    for k, zh in SKILL_FIELDS.items():
        val = first(f, k)
        if val not in (None, ""):
            meta.append(f"**{zh}**：{v(val)}")
    lines = [f'??? note "{head}"', "", "    " + "　·　".join(meta), ""]
    if anam and anam != sbind:
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
    return lines


def render_hero(h: dict, unit: dict, abils: dict, fdict: dict, item_pages: dict,
                item_ub: dict) -> str:
    hcode = h["code"]
    hname = clean_inline(h.get("name")) or hcode
    proper = clean_inline(h.get("proper_name"))
    title = f"{hname}（{proper}）" if proper and proper != hname else hname
    uf = (unit or {}).get("fields", {})
    name_in_table = f"# {hcode} · {title}"
    lines = [name_in_table, ""]
    meta = [
        f"**主属性**：{ATTR_SHORT.get((h.get('primary') or '').upper(), h.get('primary') or '—')}",
        f"**英雄 ID**：`{hcode}`",
        f"**原型**：`{clean_inline(h.get('base'))}`",
    ]
    if h.get("reachable") == "no":
        meta.append("**可选性**：⚠️ 未确认可选中")
    lines.append("> " + "\u3000·\u3000".join(meta))
    lines.append("")

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
    rows = [
        [f"初始{ATTR_ZH.get('STR', '筋力')}", v(ufield("ustr")), f"+{v(ufield('ustp'))} / 级"],
        ["初始敏捷", v(ufield("uagi")), f"+{v(ufield('uagp'))} / 级"],
        [f"初始{ATTR_ZH.get('INT', '体力')}", v(ufield("uint")), f"+{v(ufield('uinp'))} / 级"],
        ["最大生命值", v(ufield("uhpm")), "—"],
        ["最大魔法值", v(ufield("umpm")), "—"],
        ["初始魔法值", v(ufield("umpi")), "—"],
        ["护甲", v(ufield("udef")), "—"],
        ["护甲类型", blank(clean_inline(ufield("uarm"))), "—"],
        ["移动速度", v(ufield("umvs")), "—"],
        ["初始等级", v(ufield("ulev")), "—"],
        ["英雄属性成长技能", code(clean_inline(ufield("uhab"))) or "—", "—"],
    ]
    lines.append(table(["属性", "初始值", "成长"], rows))
    lines.append("")
    lines.append("> 本图把「力量」写作**筋力**、把「智力」写作**体力**（依据：59 个英雄的 `uhab` 统一为 "
                 "`Z063/Z064/Z065` 三个属性成长技能）。")
    lines.append("")

    lines += ["## 技能取得", ""]
    lines.append("_本图技能对象全部只有 1 级（`alev=1`，`arlv` 多为 1），**解锁与升级由触发器控制**，"
                 "对象数据里没有可读的解锁等级 → 本表只列技能绑定，解锁等级标注为「待考证」。_")
    lines.append("")
    srows = []
    bindings = []
    for slot in SLOTS:
        raw = h.get(slot)
        if not raw:
            continue
        scode, sbind = parse_slot(raw)
        bindings.append((slot, scode, sbind))
        a = abils.get(scode)
        aub = clean_text(first(a["fields"], "Ubertip")) if a else ""
        kind = "被动" if (a and first(a["fields"], "Order") in (None, "")) else "主动"
        srows.append([f"**{slot}**", code(scode), esc(sbind) or "—", kind, "待考证", esc(aub[:60])])
    if srows:
        lines.append(table(["键位", "技能 ID", "技能名", "类型", "解锁等级", "说明摘要"], srows))
    else:
        lines.append("_（未在名单里绑定技能）_")
    lines.append("")

    lines += [f"## {MAP_VERSION} 技能数据", ""]
    if bindings:
        for slot, scode, sbind in bindings:
            lines += render_skill(slot, scode, sbind, abils, fdict)
    else:
        lines.append("_（无）_")
        lines.append("")

    # 专属装备（文本匹配，明确标注为推断）
    hits = []
    for icode, text in item_ub.items():
        if hname and len(hname) >= 2 and hname in text:
            hits.append(icode)
    lines += ["## 专属装备（自动推断）", ""]
    if hits:
        lines.append("下面这些物品的游戏内说明里出现了本英雄的名字。**这只是文本匹配，不等于专属绑定**，"
                     "真实专属关系要看触发器。")
        lines.append("")
        irows = []
        for ic in sorted(hits):
            cat, rel = item_pages.get(ic, ("?", ""))
            label = f"[`{ic}`](../items/{rel})" if rel else code(ic)
            irows.append([label, cat])
        lines.append(table(["物品", "分类"], irows))
    else:
        lines.append("_（没有任何物品说明提到本英雄——可能确实没有专属装备，也可能专属写死在触发器里。）_")
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

    os.makedirs(HERO_OUT, exist_ok=True)
    for h in heroes:
        hcode = h["code"]
        hname = clean_inline(h.get("name")) or hcode
        fn = safe_name(hname) + ".md"
        h["file"] = fn
        write_page(os.path.join(HERO_OUT, fn),
                   render_hero(h, units.get(hcode), abils, fdict, item_pages, item_ub))

    # 英雄总览
    rows = []
    for h in sorted(heroes, key=lambda x: x["code"]):
        hname = clean_inline(h.get("name")) or h["code"]
        sk = []
        for slot in ("Q", "W", "E", "R", "F", "D"):
            c, _ = parse_slot(h.get(slot))
            sk.append(f"{slot}:{c}" if c else f"{slot}:—")
        rows.append([
            f"[`{h['code']}`]({h['file']})",
            esc(hname),
            esc(clean_inline(h.get("proper_name"))) or "—",
            ATTR_SHORT.get((h.get("primary") or "").upper(), h.get("primary") or "—"),
            "　".join(sk),
        ])
    idx = ["# 英雄图鉴", "",
           f"共 **{len(heroes)}** 个英雄条目（其中 `reachable=no` 的未确认可选中）。"
           "开局在选人区把单位**双击**即可选中（触发器 `Lz` / `iy4`）。", "",
           "| 说明 | 内容 |", "| --- | --- |",
           "| 可选中英雄 | 58 |", "| 选人方式 | 双击 `Player(15)` 所属的选人单位 |",
           "| 技能键位 | Q/W/E/R/F/D（对象数据 `abpx/abpy` 判定） |", "",
           table(["ID", "名称", "称号", "主属性", "技能绑定"], rows), ""]
    idx.append(source_footer())
    write_page(os.path.join(HERO_OUT, "index.md"), "\n".join(idx))
    write_page(os.path.join(HERO_OUT, ".pages"),
               "title: 英雄图鉴\nnav:\n  - index.md\n  - ...\n")
    print(f"英雄页：{len(heroes)} 个 → {HERO_OUT}")


if __name__ == "__main__":
    main()
