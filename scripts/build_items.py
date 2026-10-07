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
    utf8, load_json, load_tsv, clean_text, clean_inline, esc, code, safe_name,
    write_page, table, source_footer, blank, obj_code,
)

utf8()

ITEMS_JSON = os.path.join(WIKI_DATA, "items.json")
ABIL_JSON = os.path.join(WIKI_DATA, "abilities.json")
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
    if os.path.exists(ITEM_SRC):
        try:
            sources = load_json(ITEM_SRC).get("items", {})
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

    for p in parsed:
        cat_count[p["cat"]] += 1
        if not p["name"]:
            no_name.append(p["code"])
        d = os.path.join(ITEM_OUT, p["cat"])
        fn = f"{p['code']}_{safe_name(p['display'])}.md"
        p["file"] = f"{p['cat']}/{fn}"
        write_page(os.path.join(d, fn), render_item(p, abils, fdict, sources, used_in))
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
    idx.append(source_footer([
        f"物品对象来自 `war3map.w3t`（SHA256 `{MEMBER_SHA['war3map.w3t']}`），"
        f"物品技能数值来自 `war3map.w3a`（SHA256 `{MEMBER_SHA['war3map.w3a']}`）。"
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


def render_item(p, abils, fdict, sources, used_in) -> str:
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
        lines.append(render_sources(src))
    else:
        lines.append("**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。")
        lines.append("")
        lines.append("> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、"
                     "`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；"
                     "没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。")
        lines.append("")

    lines += ["## 合成与材料用途", ""]
    uses = used_in.get(p["code"]) or []
    if uses:
        rows = [[code(c), esc(n)] for c, n in sorted(set(uses))]
        lines.append("这些物品的游戏内说明里提到了本物品（**文本匹配，不等于真实的合成配方**）：")
        lines.append("")
        lines.append(table(["物品 ID", "物品名称"], rows))
    else:
        lines.append("_（没有其它物品的说明提到本物品）_")
        lines.append("")

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


def render_sources(src: dict) -> str:
    out = []
    kinds = [("vendor", "商店出售"), ("craft", "打造/合成"), ("drop", "掉落"), ("shop_menu", "NPC菜单")]
    for key, label in kinds:
        entries = src.get(key)
        if not entries:
            continue
        out.append(f"**{label}**")
        out.append("")
        rows = []
        for e in entries:
            if isinstance(e, dict):
                rows.append([
                    esc(e.get("what") or e.get("snippet") or ""),
                    code(e.get("line")) if e.get("line") else "—",
                    "`" + clean_inline(e.get("snippet") or "")[:120].replace("`", "'") + "`",
                ])
            else:
                rows.append([esc(e), "—", "—"])
        out.append(table(["说明", "j 行号", "原始片段"], rows))
    if not out:
        out.append("**待考证**——`item_sources.json` 中没有该物品的记录。")
        out.append("")
    extra = src.get("note")
    if extra:
        out += [f"> {clean_inline(extra)}", ""]
    return "\n".join(out)


if __name__ == "__main__":
    main()
