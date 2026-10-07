# -*- coding: utf-8 -*-
"""生成物品页（docs/items/<分类>/<ID>_<名称>.md）+ 物品总览页。

只读 note_log/wiki_data/*.json 与 note_log/index/*.tsv，写 wiki/docs/items/。
可选读取 note_log/wiki_data/item_sources.json（获取方式，由子智能体产出）；
文件不存在时该节标「待考证」，不编造。
"""
from __future__ import annotations

import json
import os
import re
import sys
import collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wiki_common import (  # noqa: E402
    DOCS, WIKI_DATA, INDEX_DIR, WIKI_DIR, MAP_VERSION, MAP_NAME, MEMBER_SHA,
    RECON_DIR,
    utf8, load_json, load_tsv, clean_text, clean_inline, esc, code, safe_name,
    write_page, table, source_footer, blank, obj_code,
)

utf8()

ITEMS_JSON = os.path.join(WIKI_DATA, "items.json")
ABIL_JSON = os.path.join(WIKI_DATA, "abilities.json")
UNITS_JSON = os.path.join(WIKI_DATA, "units.json")
EXCL_JSON = os.path.join(RECON_DIR, "hero_exclusive.json")
ITEM_SRC = os.path.join(WIKI_DATA, "item_sources.json")
ABIL_FIELDS = os.path.join(INDEX_DIR, "field_dict_abilities.tsv")
ITEM_OUT = os.path.join(DOCS, "items")

CATEGORY_ORDER = [
    "武器", "装甲", "副武器", "头部道具", "灵魂装备", "觉醒装备",
    "消耗品", "素材", "任务物品", "传送与关卡", "NPC功能物品", "不归类",
]

# 说明里第一个染色片段 → 分类（排除单字母热键标签）
TAG_MAP = {
    "武器": "武器",
    "装甲": "装甲",
    "-副武器": "副武器",
    "副武器": "副武器",
    "头部道具": "头部道具",
    "灵魂武器": "灵魂装备",
    "灵魂道具": "灵魂装备",
    "灵魂宝具": "灵魂装备",
    "觉醒": "觉醒装备",
    "不归类": "不归类",
    "野性熊套-爪": "装甲",
    "掉落物品": "传送与关卡",
    "特殊物品": "传送与关卡",
}

COLOR_TAG = re.compile(r"\|c[0-9a-fA-F]{8}([^|\r\n]{1,14})\|r")
CONSUMABLE_RE = re.compile(r"之书|药水|卷轴|药剂|丹药|药膏|符咒|蛋糕|面包|奶酪|料理|食物")
NPC_RE = re.compile(r"打造|制造|交换|交易|提交|兑换|分解|重铸|解锁器|抽奖")
TELEPORT_RE = re.compile(r"传送|迷宫|挑战|回城|时空")
QUEST_RE = re.compile(r"任务|信封|调查|笔记本|钥匙|剧情|日记|请托")
MATERIAL_RE = re.compile(r"片$|碎片|牙齿|之骨|骨头|羽毛|狼皮|皮革|矿石|结晶|宝石|之石|角$|鳞|木材|布料|丝线")
QUALITY_RE = re.compile(r"品质\s*[:：]\s*([^\n|]+)")
SINGLE_LETTER = re.compile(r"^[A-Za-z]$")


def v(x) -> str:
    if x is None:
        return ""
    if isinstance(x, bool):
        return "是" if x else "否"
    if isinstance(x, float):
        if abs(x - round(x)) < 1e-9:
            return str(int(round(x)))
        return ("%g" % x)
    return str(x)


def first(fields: dict, key: str):
    rows = fields.get(key)
    if not rows:
        return None
    return rows[0].get("value")


def first_row(fields: dict, key: str):
    rows = fields.get(key)
    return rows[0] if rows else None


def load_field_dict(path: str) -> dict:
    out = {}
    if not os.path.exists(path):
        return out
    with open(path, encoding="utf-8-sig") as f:
        head = f.readline().rstrip("\n").split("\t")
        for ln in f:
            c = ln.rstrip("\n").split("\t")
            if len(c) < len(head):
                continue
            d = dict(zip(head, c))
            out[d.get("field_id", "")] = d
    return out


def classify(name: str, tip: str, ubertip: str, icla: str) -> str:
    """按「说明里第一个染色片段」→ 名称规则 → 能力名的顺序推断分类。

    分类是**自动推断**，页面里会标明；拿不准的一律进「不归类」。
    """
    body = f"{ubertip}\n{tip}"
    m = COLOR_TAG.search(ubertip) or COLOR_TAG.search(tip)
    if m:
        tag = m.group(1).strip()
        if tag and not SINGLE_LETTER.match(tag) and not tag.startswith(("如下", "提示", "无法理解")):
            for key, cat in TAG_MAP.items():
                if tag == key or tag.startswith(key):
                    return cat
            if "灵魂" in tag:
                return "灵魂装备"
            if tag.startswith("迷宫"):
                return "传送与关卡"
            if tag in ("觉醒",):
                return "觉醒装备"
            if tag.startswith("比较好的") or tag.endswith("的牙齿"):
                return "素材"
    if TELEPORT_RE.search(name):
        return "传送与关卡"
    if NPC_RE.search(name):
        return "NPC功能物品"
    if CONSUMABLE_RE.search(name):
        return "消耗品"
    if QUEST_RE.search(name):
        return "任务物品"
    if MATERIAL_RE.search(name):
        return "素材"
    if "掉落物品" in body or "特殊物品" in body:
        return "传送与关卡"
    return "不归类"


def quality_of(ubertip: str) -> str:
    m = QUALITY_RE.search(ubertip)
    if not m:
        return ""
    return clean_inline(m.group(1)).strip("　 ")


def load_base_names() -> dict:
    """原型 code → 客户端官方中文名（备被修改的原版物体没有 Name 字段时用）。"""
    out = {}
    p = os.path.join(INDEX_DIR, "base_names_items.tsv")
    if not os.path.exists(p):
        return out
    for r in load_tsv(p):
        out[r["code"].lower()] = r.get("name", "")
        out[r["code"].upper()] = r.get("name", "")
    return out


def main() -> None:
    items = load_json(ITEMS_JSON)
    abils = {a["code"]: a for a in load_json(ABIL_JSON)}
    fdict = load_field_dict(ABIL_FIELDS)
    base_names = load_base_names()
    sources = {}
    cov = {}
    if os.path.exists(ITEM_SRC):
        try:
            _src = load_json(ITEM_SRC)
            sources = _src.get("items", {})
            cov = _src.get("coverage", {}) or {}
        except Exception as e:  # noqa: BLE001
            print(f"  ! item_sources.json 解析失败：{e}")
    else:
        print("  · item_sources.json 尚不存在 → 获取方式一律标「待考证」")

    parsed = []
    for it in items:
        f = it["fields"]
        name = clean_inline(first(f, "Name"))
        raw_tip = str(first(f, "Tip") or "")
        raw_ub = str(first(f, "Ubertip") or "")
        tip = clean_text(raw_tip)
        ubertip = clean_text(raw_ub)
        icla = clean_inline(first(f, "class"))
        cat = classify(name, raw_tip, raw_ub, icla)
        base = it["base"]
        bname = base_names.get(base, "") or base_names.get(base.lower(), "")
        parsed.append({
            "code": obj_code(it),
            "base": base,
            "base_name": bname,
            "name": name,
            "display": name or (f"{bname}（原版）" if bname else base),
            "tip": tip,
            "ubertip": ubertip,
            "icla": icla,
            "cat": cat,
            "quality": quality_of(ubertip),
            "fields": f,
            "abil": [x.strip() for x in str(first(f, "abilList") or "").split(",") if x.strip()],
        })

    # 材料用途反查：其它物品的说明里出现了本物品的名字
    used_in = collections.defaultdict(list)
    for p in parsed:
        if not p["ubertip"]:
            continue
        text = p["ubertip"]
        for other in parsed:
            onm = other["name"]
            if len(onm) < 2 or onm == p["name"]:
                continue
            if onm in text:
                used_in[other["code"]].append((p["code"], onm))

    os.makedirs(ITEM_OUT, exist_ok=True)
    cat_count = collections.Counter()
    no_name = []

    item_names = {p["code"]: p["display"] for p in parsed}
    unit_names = {}
    try:
        for u in load_json(UNITS_JSON):
            c = str(u.get("code") or "").replace("\x00", "")
            if len(c) != 4:
                c = u.get("base") or ""
            nm = clean_inline((u.get("fields") or {}).get("Name", [{}])[0].get("value") if (u.get("fields") or {}).get("Name") else "")
            if len(c) == 4 and nm:
                unit_names[c] = nm
    except Exception as e:  # noqa: BLE001
        print(f"  ! units.json 读取失败（掉落来源单位名将留空）：{e}")

    excl_items = {}
    if os.path.exists(EXCL_JSON):
        try:
            excl_items = load_json(EXCL_JSON).get("exclusive_items", {}) or {}
        except Exception as e:  # noqa: BLE001
            print(f"  ! hero_exclusive.json 解析失败（专属标记将缺失）：{e}")

    for p in parsed:
        cat_count[p["cat"]] += 1
        if not p["name"]:
            no_name.append(p["code"])
        d = os.path.join(ITEM_OUT, p["cat"])
        fn = f"{p['code']}_{safe_name(p['display'])}.md"
        p["file"] = f"{p['cat']}/{fn}"
        write_page(os.path.join(d, fn),
                   render_item(p, abils, fdict, sources, used_in, item_names, unit_names, excl_items))
    for c in CATEGORY_ORDER:
        os.makedirs(os.path.join(ITEM_OUT, c), exist_ok=True)

    # 物品总览
    rows = []
    for p in sorted(parsed, key=lambda x: (x["cat"], x["code"])):
        rows.append([
            f"[`{p['code']}`]({p['file']})",
            esc(p["display"]) or "—",
            p["cat"],
            p["quality"] or "—",
            blank(clean_inline(first(p["fields"], "goldcost"))),
            blank(clean_inline(first(p["fields"], "Level"))),
            code(p["base"]),
        ])
    head = ["ID", "名称", "分类", "品质", "价格", "物品等级", "原型"]
    idx = [f"# 物品总览", "",
           f"共 **{len(parsed)}** 个物品对象（没有自定义名称的 {len(no_name)} 个显示为「原版名（原版）」："
           f"{'、'.join(no_name) or '无'}）。", "",
           "分类由游戏内说明里的类型标签与名称规则**自动推断**，推断结果可能有误——以每页的说明原文为准。", "",
           table(head, rows), ""]
    for c in CATEGORY_ORDER:
        if cat_count.get(c):
            idx.append(f"- **{c}**：{cat_count[c]} 个")
    idx.append("")

    # 获取途径统计（来自 item_sources.json）
    if cov:
        idx += ["## 获取途径证据覆盖", "",
                f"- 物品对象总数：**{cov.get('items_total', '—')}**",
                f"- 拿到至少一条获取途径证据：**{cov.get('items_with_acquisition_evidence', '—')}**",
                f"- 只有上下文证据（作为材料/触发物被消耗）：**{cov.get('items_with_context_only_evidence', '—')}**",
                f"- 完全没有获取证据：**{cov.get('items_without_any_evidence', '—')}**", "",
                "每条获取方式都带 `war3map.j` 行号；证据来自静态分析，**不代表游戏内一定如此**（例如合成还需要 NPC 菜单配合）。", ""]
        kinds = cov.get("acquisition_kinds") or []
        if kinds:
            idx.append("识别的获取途径类型：" + "、".join(f"`{k}`" for k in kinds))
            idx.append("")

    idx.append(source_footer([
        f"物品对象来自 `war3map.w3t`（SHA256 `{MEMBER_SHA['war3map.w3t']}`），"
        f"物品技能数值来自 `war3map.w3a`（SHA256 `{MEMBER_SHA['war3map.w3a']}`）。",
        "获取方式来自 `war3map.j`（SHA256 `13bafcf0c1e91848fbf8ee72cbc48017e711cae7b6198e69cb01136c7064a4a2`）"
        "的静态数据流分析，断言都带行号。",
    ]))
    write_page(os.path.join(ITEM_OUT, "index.md"), "\n".join(idx))

    with open(os.path.join(ITEM_OUT, ".pages"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("title: 物品图鉴\nnav:\n  - index.md\n")
        for c in CATEGORY_ORDER:
            if cat_count.get(c):
                fh.write(f"  - {c}\n")

    print(f"物品页：{len(parsed)} 个 → {ITEM_OUT}")
    for c in CATEGORY_ORDER:
        print(f"   {c}: {cat_count.get(c, 0)}")
    print(f"   无名称: {len(no_name)} {no_name}")


def render_item(p, abils, fdict, sources, used_in, item_names, unit_names,
                excl_items=None) -> str:
    f = p["fields"]
    icla = p["icla"] or "—"
    lines = [f"# {p['code']} · {p['display']}", ""]

    meta = [
        f"**分类**：{p['cat']}",
        f"**品质**：{p['quality'] or '—'}",
        f"**类型**：{icla}",
        f"**物品等级**：{blank(clean_inline(first(f, 'Level')))}",
        f"**价格**：{blank(clean_inline(first(f, 'goldcost')))} 金",
    ]
    lines.append("> " + "\u3000".join(meta))
    lines.append("")
    proto = f"`{p['base']}`"
    if p["base_name"]:
        proto += f"（{p['base_name']}）"
    lines.append(f"**物品 ID**：`{p['code']}`　·　**原型**：{proto}　·　**版本**：{MAP_VERSION}")
    lines.append("")
    if first(f, "Hotkey"):
        lines.append(f"**热键**：`{clean_inline(first(f, 'Hotkey'))}`")
        lines.append("")

    ex = (excl_items or {}).get(p["code"])
    if ex:
        allowed = ex.get("allowed_unit_types") or []
        nicks = ex.get("allowed_nicknames") or []
        ev = (ex.get("evidence") or {}).get("line")
        at = f"（`war3map.j:{ev}`）" if ev else ""
        if nicks and not allowed:
            lines.append("> ⚠️ **限定使用（按玩家昵称）**：仅玩家昵称 "
                         + "、".join(f"`{n}`" for n in nicks) + f" 可以使用{at}。")
        elif allowed:
            who = "、".join(f"{unit_names.get(u) or ''}(`{u}`)".strip() for u in allowed)
            lines.append(f"> 🔒 **英雄专属**：仅 {who} 可以拾取，其他英雄拾取会被立即移除{at}。")
        if nicks and allowed:
            lines.append("> 另有按玩家昵称的判定：" + "、".join(f"`{n}`" for n in nicks) + "。")
        if ex.get("drop_pool_index") is not None:
            lines.append(f"> 同时属于 `EXEQ_DropPool[{ex['drop_pool_index']}]`（英雄专属掉落池，"
                         "`war3map.j:88781-88814`）。")
        lines.append("")

    lines += [f"## {MAP_VERSION} 当前数据", "", "### 基础属性", ""]

    # 数值来自物品技能（iabi）
    stat_rows = []
    ability_rows = []
    for ac in p["abil"]:
        a = abils.get(ac)
        if not a:
            ability_rows.append([code(ac), "（对象不存在）", "—", "—"])
            continue
        anam = clean_inline(first(a["fields"], "Name"))
        aub = clean_inline(first(a["fields"], "Ubertip"))
        keybits = []
        for ini_key, rows in a["fields"].items():
            for r in rows:
                fid = r.get("field", "")
                d = fdict.get(fid, {})
                if d.get("ini_key") == "Data":
                    zh = d.get("zh_label") or fid
                    stat_rows.append([
                        esc(zh),
                        esc(v(r.get("value"))),
                        f"`{ac}`",
                        code(fid),
                        blank(r.get("level"), ""),
                    ])
                    keybits.append(f"{zh}={v(r.get('value'))}")
                elif d.get("ini_key") in ("Cost", "Cool") and r.get("level") in (1, "1", None):
                    keybits.append(f"{d.get('zh_label') or fid}={v(r.get('value'))}")
        ability_rows.append([code(ac), esc(anam) or "—", esc(", ".join(keybits)) or "—", esc(aub) or "—"])

    if stat_rows:
        lines.append(table(["属性", "数值", "来源能力", "字段", "等级"], stat_rows))
    else:
        lines.append("_（该物品没有属性类物品技能）_")
        lines.append("")

    lines += ["### 物品能力", ""]
    if ability_rows:
        lines.append(table(["能力 ID", "能力名称", "关键数值", "能力说明"], ability_rows))
    else:
        lines.append("_（无 `iabi` 绑定）_")
        lines.append("")

    lines += ["### 游戏内说明（原文）", ""]
    if p["ubertip"]:
        for ln in p["ubertip"].split("\n"):
            lines.append(f"> {ln}" if ln.strip() else ">")
    else:
        lines.append("> _（无）_")
    lines.append("")
    if p["tip"] and clean_inline(p["tip"]) != clean_inline(p["ubertip"]):
        lines += ["**提示工具（Tip）**：", "", "```text", p["tip"], "```", ""]

    lines += ["## 获取方式", ""]
    src = sources.get(p["code"]) if sources else None
    if src:
        lines.append(render_sources(src, item_names, unit_names))
    else:
        lines.append("**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。")
        lines.append("")
        lines.append("> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、"
                     "`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；"
                     "没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。")
        lines.append("")

    lines += ["## 合成与材料用途", ""]
    lines.append(render_materials(src, used_in.get(p["code"]) or [], item_names))

    lines += ['??? note "全部对象字段（原始值）"', ""]
    for ini_key in sorted(f.keys()):
        for r in f[ini_key]:
            zh = r.get("zh") or fdict.get(r.get("field", ""), {}).get("zh_label") or ""
            lv = f" (Lv{r['level']})" if r.get("level") not in (None, "") else ""
            lines.append(f"    - `{r.get('field','')}` {ini_key}{lv} = `{v(r.get('value'))}`"
                         + (f"　*({clean_inline(zh)})*" if zh else ""))
    lines.append("")

    lines.append(source_footer([
        f"物品字段：`war3map.w3t`（SHA256 `{MEMBER_SHA['war3map.w3t']}`）；"
        f"物品技能：`war3map.w3a`（SHA256 `{MEMBER_SHA['war3map.w3a']}`）；"
        f"物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\\AbilityMetaData.slk` + `UI\\WorldEditStrings.txt`。",
        "**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。",
    ]))
    return "\n".join(lines)


def _nm(codes, names, limit=12) -> str:
    """把 code 列表渲染成「`ID` 名称」形式。"""
    out = []
    for c in codes if isinstance(codes, list) else [codes]:
        if not c:
            continue
        n = names.get(c) or ""
        out.append(f"`{c}`" + (f" {esc(n)}" if n else ""))
    if len(out) > limit:
        out = out[:limit] + [f"…等 {len(out)} 项"]
    return "、".join(out)


def render_sources(src: dict, item_names: dict, unit_names: dict) -> str:
    out = []

    def section(title, rows, head):
        out.append(f"**{title}**")
        out.append("")
        out.append(table(head, rows))
        out.append("")

    # 1) 商店出售（触发器进货）
    if src.get("vendor"):
        rows = []
        for e in src["vendor"]:
            shop = e.get("shop_name") or unit_names.get(e.get("shop_unit") or "", "") or e.get("shop_unit") or "—"
            rows.append([esc(shop), code(e.get("api")), blank(e.get("stock_cur")), blank(e.get("stock_max")), code(e.get("line"))])
        section("商店出售（`AddItemToStock` 进货）", rows, ["商店", "接口", "当前库存", "最大库存", "j 行号"])

    # 2) 商店货架（对象数据）
    if src.get("vendor_object_data"):
        rows = []
        for e in src["vendor_object_data"]:
            shop = e.get("shop_name") or unit_names.get(e.get("shop_unit") or "", "") or e.get("shop_unit") or "—"
            rows.append([esc(shop), code(e.get("shop_unit")), code(e.get("field")), esc(e.get("field_name") or ""), esc(e.get("line_ref") or "")])
        section("商店货架（对象数据 `usei`/`umki`）", rows, ["商店", "商店单位", "字段", "字段名", "证据位置"])

    if src.get("vendor_removed"):
        rows = [[code(e.get("shop_unit")), code(e.get("line")), "`" + clean_inline(e.get("snippet") or "")[:110].replace("`", "'") + "`"] for e in src["vendor_removed"]]
        section("该物品被从商店移除（`RemoveItemFromStock`）", rows, ["商店单位", "j 行号", "原始片段"])

    # 3) 抽奖机
    if src.get("gacha"):
        rows = []
        for e in src["gacha"]:
            mat = e.get("consumed_material_names") or e.get("consumed_materials") or []
            rows.append([
                esc(e.get("trigger_item_name") or "") + " " + code(e.get("trigger_item")),
                esc(_nm([e.get("result")], item_names)),
                esc(f"{len(mat)} × " + (mat[0] if mat and isinstance(mat[0], str) else "")),
                code(e.get("line")),
            ])
        section("抽奖 / 扭蛋", rows, ["触发物", "产出", "消耗", "j 行号"])

    # 4) 打造 / 合成
    if src.get("craft"):
        rows = []
        for e in src["craft"]:
            trig = (esc(e.get("trigger_item_name") or "") + " " + code(e.get("trigger_item"))) if e.get("trigger_item") else "（自动合成）"
            mats = e.get("consumed_materials") or e.get("checked_materials") or []
            rows.append([trig, _nm(mats, item_names), code(e.get("cond_line") or e.get("line")),
                         "⚠️ 材料不符" if e.get("material_mismatch") else "—"])
        section("打造 / 合成", rows, ["触发物", "消耗材料", "j 行号", "备注"])

    # 5) 掉落
    if src.get("drop"):
        rows = []
        for e in src["drop"]:
            su = e.get("source_unit") or ""
            sun = e.get("source_unit_name") or unit_names.get(su, "")
            chance = e.get("chance_pct")
            rows.append([
                (f"`{su}`" + (f" {esc(sun)}" if sun else "")) if su else "（未标注来源单位）",
                esc(e.get("method") or e.get("kind") or ""),
                (f"{chance}%" if chance is not None else "—"),
                code(e.get("line") or e.get("choose_line")),
            ])
        section("掉落（掉落表 / 权重表）", rows, ["来源单位", "方式", "概率", "j 行号"])

    # 6) BOSS 掉落池
    if src.get("boss_pool"):
        rows = []
        for e in src["boss_pool"]:
            bu = e.get("boss_unit") or ""
            bn = e.get("boss_name") or unit_names.get(bu, "")
            rows.append([esc(e.get("pool") or ""), blank(e.get("index")),
                         (f"`{bu}`" + (f" {esc(bn)}" if bn else "")) if bu else "—",
                         code(e.get("pool_line")), code(e.get("drop_line"))])
        section("BOSS 专属掉落池（`HF22SD_Pool`）", rows, ["池", "序号", "来源 BOSS", "池定义行", "掉落行"])

    # 7) 击杀成长
    for key, label in (("grow", "击杀成长（本物品是**升级后**的形态）"), ("grow_into", "击杀成长（本物品会**升级为**下一形态）")):
        if not src.get(key):
            continue
        rows = []
        for e in src[key]:
            th = e.get("kill_threshold") or {}
            rows.append([
                _nm([e.get("from_item")], item_names) if key == "grow" else _nm([e.get("to_item")], item_names),
                code(th.get("var")) + f" ≥ {blank(th.get('value'))}",
                code(th.get("line")),
            ])
        section(label, rows, ["另一形态", "击杀阈值", "j 行号"])

    # 8) 塔层奖励
    if src.get("tower_reward"):
        rows = [[blank(e.get("tower_stage")), code(e.get("line")), code(e.get("grant_line"))] for e in src["tower_reward"]]
        section("通天塔层奖励", rows, ["层数", "定义行", "发奖行"])

    # 9) 事件生成
    if src.get("spawn"):
        rows = []
        for e in src["spawn"]:
            cond = ", ".join(e.get("cond_rawcodes") or [])
            rows.append([esc(e.get("kind") or ""), _nm(cond.split(", ") if cond else [], unit_names), code(e.get("line"))])
        section("事件生成（`CreateItemLoc`）", rows, ["方式", "触发单位", "j 行号"])

    # 10) 赠送
    if src.get("gift"):
        rows = [[esc(e.get("kind") or ""), esc(clean_inline(str(e.get("to") or ""))), code(e.get("line"))] for e in src["gift"]]
        section("触发时赠予", rows, ["方式", "给谁", "j 行号"])

    # 11) 拾取 / 使用触发
    if src.get("trigger_use"):
        rows = []
        for e in src["trigger_use"]:
            rows.append([esc(e.get("kind") or ""), _nm(e.get("produces") or [], item_names), code(e.get("used_at_line"))])
        section("拾取 / 使用触发", rows, ["方式", "产出", "j 行号"])

    # 12) 作为材料被消耗
    if src.get("used_as_material"):
        rows = []
        for e in src["used_as_material"]:
            rows.append([esc(e.get("trigger_item_name") or "") + " " + code(e.get("trigger_item")),
                         _nm([e.get("result")], item_names), code(e.get("line"))])
        section("作为材料被消耗", rows, ["触发卷轴/菜单", "合成结果", "j 行号"])

    if not out:
        out.append("**待考证**——`item_sources.json` 中没有该物品的获取途径记录（它可能只作为材料被消耗）。")
        out.append("")
    return "\n".join(out)


def render_materials(src, text_uses, item_names) -> str:
    parts = []
    if src and src.get("used_as_material"):
        rows = []
        for e in src["used_as_material"]:
            rows.append([esc(e.get("trigger_item_name") or "") + " " + code(e.get("trigger_item")),
                         _nm([e.get("result")], item_names), code(e.get("line"))])
        parts += ["**作为材料参与合成（触发器证据）**：", "", table(["触发卷轴/菜单", "合成结果", "j 行号"], rows), ""]
    if src and src.get("consumed_only"):
        parts += ["**被收走后消失（`RemoveItem`）**：", ""]
        for e in src["consumed_only"]:
            parts.append(f"- j 行 {e.get('line')}：`{clean_inline(e.get('snippet') or '')[:130]}`")
        parts.append("")
    if text_uses:
        rows = [[code(c), esc(n)] for c, n in sorted(set(text_uses))]
        parts += ["**说明文本中提到本物品的物品**（文本匹配，不等于真实配方）：", "",
                  table(["物品 ID", "物品名称"], rows), ""]
    if not parts:
        parts.append("_（没有找到本物品参与合成或作为材料的证据）_")
        parts.append("")
    return "\n".join(parts)


if __name__ == "__main__":
    main()
