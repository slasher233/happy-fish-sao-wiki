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
import csv
import glob

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wiki_common import (  # noqa: E402
    DOCS, WIKI_DATA, INDEX_DIR, WIKI_DIR, MAP_VERSION, MAP_NAME, MEMBER_SHA,
    RECON_DIR,
    utf8, load_json, load_tsv, clean_text, clean_inline, esc, code, safe_name,
    write_page, table, source_footer, blank, obj_code,
    CLASS_ZH, field_zh, val_or, fmt_num, link,
)

utf8()

W_ROOT = os.path.dirname(WIKI_DIR)
PLAN_DATA = os.path.join(W_ROOT, "patch_plan", "data")
ANCHORS_JSON = os.path.join(RECON_DIR, "item_text_anchors.json")

ITEMS_JSON = os.path.join(WIKI_DATA, "items.json")
ABIL_JSON = os.path.join(WIKI_DATA, "abilities.json")
UNITS_JSON = os.path.join(WIKI_DATA, "units.json")
EXCL_JSON = os.path.join(RECON_DIR, "hero_exclusive.json")
ITEM_SRC = os.path.join(WIKI_DATA, "item_sources.json")
ABIL_FIELDS = os.path.join(INDEX_DIR, "field_dict_abilities.tsv")
ITEM_OUT = os.path.join(DOCS, "items")

# 需求单仓库里的成品表（用户看的那份）；只用它们补充「人话」字段，不写回
PLAN_ITEM_TEXT = os.path.join(PLAN_DATA, "item_text.csv")
PLAN_ITEM_SOURCE = os.path.join(PLAN_DATA, "items_source.csv")
PLAN_DROPS_BY_BOSS = os.path.join(PLAN_DATA, "drops_by_boss.csv")
PLAN_ITEM_ABILITY = os.path.join(PLAN_DATA, "item_ability_data.csv")
# 本版本无法获得的物品清单（由 note_log/tools/make_removed_manifest.py 生成）；
# 这些物品已从数据层与图鉴删除，生成器读它过滤，避免重新生成时又冒出来。
REMOVED_JSON = os.path.join(PLAN_DATA, "removed_items.json")

# 技能「表头字段」在 AbilityData.slk 里的列名（slk_col）：冷却/耗魔/距离/范围/持续/等级数。
# 它们不是 `Data` 每级数值，但同样是玩家能感知、说明里常出现的数（以前完全没进需求单）。
HDR_SLK = {"Cool", "Cost", "Rng", "Area", "Dur", "HeroDur", "levels"}


def load_item_hdr_rows(path: str) -> dict:
    """`item_code` → [表头字段行]（冷却/耗魔/距离/范围/持续/等级数），保持 CSV 行序。"""
    out: dict[str, list] = {}
    if not os.path.exists(path):
        return out
    for r in load_csv(path):
        if (r.get("slk_col") or "").strip() not in HDR_SLK:
            continue
        c = (r.get("item_code") or "").strip()
        if c:
            out.setdefault(c, []).append(r)
    return out

# 内部枚举 → 中文（审计问题 W012：不能把 unclassified_give / GetTriggerUnit( 直接印给用户）
KIND_ZH = {
    "npc_gift": "NPC 赠送", "unclassified_give": "触发时赠予（无法归类）",
    "event_spawn": "事件生成", "static_preplaced": "地图预置",
    "recipe_scroll_used": "配方卷轴被使用", "menu_item_used": "菜单物品被使用",
    "auto_combine": "自动合成", "recipe_scroll": "配方卷轴", "craft_station": "合成台",
    "gacha": "抽奖机", "single_weight": "单条权重掉落", "weighted_table": "权重掉落表",
    "consumed_only": "被收走后消失",
}
_UNIT_EXPR_ZH = {
    "GetTriggerUnit": "触发事件的单位（击杀者或进入区域的单位）",
    "GetKillingUnit": "击杀者",
    "GetManipulatingUnit": "操作该物品的单位",
    "GetSpellAbilityUnit": "施法单位",
}
_UNIT_EXPR_RE = re.compile(r"^(Get[A-Za-z]+)\s*\(")


def kind_zh(k) -> str:
    s = (k or "").strip()
    return KIND_ZH.get(s, s or "未知方式")


def who_zh(t) -> str:
    """把 unclassified 的「给谁」表达式翻成人话。"""
    s = clean_inline(str(t or ""))
    if not s or s in ("None", "—"):
        return "（无法确定目标）"
    m = _UNIT_EXPR_RE.match(s)
    if not m:
        return s
    who = _UNIT_EXPR_ZH.get(m.group(1))
    raw = s.replace("`", "'")
    if who:
        return f"{who}（原表达式 `{raw}`）"
    return f"（无法确定目标；原表达式 `{raw}`）"


def load_csv(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8-sig", newline="") as fh:
        return [row for row in csv.DictReader(fh)]

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
# 未解析的模板占位符：<AIim,DataB1>（原版技能 + 其数值字段）
DETOKEN_RE = re.compile(r"<([A-Za-z0-9]{4}),([A-Za-z0-9]{2,8})>")


def detoken(s) -> str:
    """把 <AIim,DataB1> 这种未解析占位符翻成人话，正文里不留尖括号 token。"""
    return DETOKEN_RE.sub(
        lambda m: f"〔原版技能 {m.group(1)} 的数值字段 {m.group(2)}（本图未解析）〕", str(s or ""))

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
    removed_items = {}
    if os.path.exists(REMOVED_JSON):
        try:
            for _r in (load_json(REMOVED_JSON).get("removed") or []):
                if _r.get("code"):
                    removed_items[str(_r["code"])] = _r
        except Exception as e:  # noqa: BLE001
            print(f"  ! removed_items.json 解析失败：{e}")
    if removed_items:
        _before = len(items)
        items = [it for it in items if obj_code(it) not in removed_items]
        print(f"  · 本版本无法获得的物品：剔除 {_before - len(items)} 件"
              f"（清单 patch_plan/data/removed_items.json，共 {len(removed_items)} 条）")
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
            # 名称缺失时不要写「原名（原版）」这种双重括号表达（审计问题 W029）
            "display": name or (f"未设置名称（原型 {bname}）" if bname else f"未设置名称（原型 {base}）"),
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
    # docs/items 完全由本脚本生成：先清空，避免物品改名/换分类后留下陈旧页面
    for old in glob.glob(os.path.join(ITEM_OUT, "**", "*.md"), recursive=True):
        try:
            os.remove(old)
        except OSError:
            pass
    cat_count = collections.Counter()
    no_name = []

    item_names = {p["code"]: p["display"] for p in parsed}
    # 交叉引用里若出现已删除的物品（例如某装备的说明里写着「奶酪」），
    # 不要只留一个裸 code —— 明确标出它本版本不可获得、已从图鉴删除。
    for _c, _r in removed_items.items():
        item_names.setdefault(_c, "%s（本版本不可获得，已从图鉴删除）" % (_r.get("name") or _c))
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

    # 自然语言描述 / 可改数值项（子智能体产出的 anchors）
    anchors = {}
    try:
        if os.path.exists(ANCHORS_JSON):
            _a = load_json(ANCHORS_JSON)
            _items = _a.get("items", _a) if isinstance(_a, dict) else _a
            _seq = _items.values() if isinstance(_items, dict) else _items
            for rec in _seq:
                if not isinstance(rec, dict):
                    continue
                if rec.get("code"):
                    anchors[rec["code"]] = rec
                if rec.get("item_name"):
                    anchors.setdefault("#" + rec["item_name"], rec)
        else:
            print("  · item_text_anchors.json 尚不存在 → 功能描述退化为「只有说明原文」")
    except Exception as e:  # noqa: BLE001
        print(f"  ! item_text_anchors.json 解析失败（功能描述将退化）：{e}")

    # 需求单仓库成品表：人话版获取方式 + 按 BOSS 聚合的掉落
    text_rows = {r["item_code"]: r for r in load_csv(PLAN_ITEM_TEXT) if r.get("item_code")}
    src_rows = {r["item_code"]: r for r in load_csv(PLAN_ITEM_SOURCE) if r.get("item_code")}
    boss_rows = collections.defaultdict(list)
    for r in load_csv(PLAN_DROPS_BY_BOSS):
        if r.get("item_code"):
            boss_rows[r["item_code"]].append(r)
    hdr_rows = load_item_hdr_rows(PLAN_ITEM_ABILITY)
    zh_to_fid = {}
    for fid, d in fdict.items():
        z = (d.get("zh_label") or "").strip()
        if z:
            zh_to_fid.setdefault(z, fid)
    print(f"  · anchors {len(anchors)} 条 / item_text {len(text_rows)} 行 / items_source {len(src_rows)} 行 / "
          f"按BOSS聚合掉落 {len(boss_rows)} 件物品 / 技能表头字段 {len(hdr_rows)} 件物品")

    for p in parsed:
        cat_count[p["cat"]] += 1
        if not p["name"]:
            no_name.append(p["code"])
        d = os.path.join(ITEM_OUT, p["cat"])
        fn = f"{p['code']}_{safe_name(p['display'])}.md"
        p["file"] = f"{p['cat']}/{fn}"
        write_page(os.path.join(d, fn),
                   render_item(p, abils, fdict, sources, used_in, item_names, unit_names, excl_items,
                               anchors.get(p["code"]) or anchors.get("#" + p["name"]) or anchors.get("#" + p["display"]),
                               text_rows.get(p["code"]), src_rows.get(p["code"]),
                               boss_rows.get(p["code"]) or [], zh_to_fid,
                               hdr_rows.get(p["code"]) or []))

    for c in CATEGORY_ORDER:
        os.makedirs(os.path.join(ITEM_OUT, c), exist_ok=True)

    # 物品总览
    rows = []
    for p in sorted(parsed, key=lambda x: (x["cat"], x["code"])):
        rows.append([
            link(p["file"], f"`{p['code']}`"),
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
        n_rm = len(removed_items)
        idx += ["## 获取途径证据覆盖", "",
                f"- 图鉴收录的物品对象：**{len(parsed)}**"
                + (f"（地图数据里另有 {n_rm} 件本版本完全无法获得，已从图鉴删除）" if n_rm else ""),
                "",
                "下面几行是**删除前**整张 `war3map.w3t` 的静态统计（来自 `note_log/wiki_data/item_sources.json`，未随删除重算）：",
                f"- 对象总数：**{cov.get('items_total', '—')}**",
                f"- 拿到至少一条获取途径证据：**{cov.get('items_with_acquisition_evidence', '—')}**",
                f"- 只有上下文证据（作为材料/触发物被消耗）：**{cov.get('items_with_context_only_evidence', '—')}**",
                f"- 完全没有获取证据：**{cov.get('items_without_any_evidence', '—')}**", "",
                "每条获取方式都带 `war3map.j` 行号；证据来自静态分析，**不代表游戏内一定如此**（例如合成还需要 NPC 菜单配合）。",
                f"被删除的 {n_rm} 件物品（含 code、名称与原文判定理由）保留在 `patch_plan/data/removed_items.json`，"
                "需要恢复时从该清单删掉条目、重跑生成器即可。", ""]
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
                excl_items=None, anchor=None, text_row=None, src_row=None,
                boss_rows=None, zh_to_fid=None, hdr_rows=None) -> str:
    f = p["fields"]
    icla = (p["icla"] or "").strip()
    lines = [f"# {p['code']} · {p['display']}", ""]

    price = clean_inline(first(f, "goldcost"))
    meta = [
        f"**分类**：{p['cat']}",
        f"**品质**：{val_or(p['quality'], '无数据（说明里没写品质）')}",
        f"**类型**：{(CLASS_ZH.get(icla, icla) if icla else '未设置')}"
        + (f"（原始枚举 `{icla}`）" if icla and CLASS_ZH.get(icla) else ""),
        f"**物品等级**：{val_or(clean_inline(first(f, 'Level')), '未设置')}",
        f"**价格**：{val_or(price, '未设置')}" + (" 金" if price else ""),
    ]
    lines.append("> " + "\u3000".join(meta))
    lines.append("")
    proto = f"`{p['base']}`"
    if p["base_name"]:
        proto += f"（{p['base_name']}）"
    lines.append(f"**物品 ID**：`{p['code']}`　·　**原型**：{proto}　·　**版本**：{MAP_VERSION}")
    lines.append("")

    lines += render_natural_language(p, anchor, text_row, src_row)
    lines += render_changeable(p, anchor, zh_to_fid or {}, hdr_rows)
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
    missing_abils = []
    for ac in p["abil"]:
        a = abils.get(ac)
        if not a:
            missing_abils.append(ac)
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
        # 能力说明整列都取不到时不要留一个空列（审计问题 W032）
        if all((r[3] in ("—", "", "（对象不存在）")) for r in ability_rows):
            for r in ability_rows:
                r.pop(3)
            lines.append(table(["能力 ID", "能力名称", "关键数值"], ability_rows))
            lines.append("")
            lines.append("> 对象数据没有给出这些能力的说明文字（`Ubertip` 为空），所以只列绑定关系与关键数值。")
        else:
            lines.append(table(["能力 ID", "能力名称", "关键数值", "能力说明"], ability_rows))
        lines.append("")
    else:
        lines.append("_（无 `iabi` 绑定）_")
        lines.append("")
    if missing_abils:
        lines += ["!!! warning \"数据异常：引用了本图不存在的能力对象\"",
                  "",
                  "    本物品的 `abilList`（字段 `iabi`）引用了本图 `war3map.w3a` 里**不存在**的能力："
                  + "、".join(f"`{c}`" for c in missing_abils) + "。",
                  "    这些多半是**魔兽原版技能**（本图没有把它们复制成自定义对象），wiki 无法展开其数值；"
                  "游戏里是否生效取决于客户端原版技能数据，本页不把它当作本图自定义能力。",
                  ""]

    lines += ["### 游戏内说明（原文）", ""]
    if p["ubertip"]:
        for ln in detoken(p["ubertip"]).split("\n"):
            lines.append(f"> {ln}" if ln.strip() else ">")
    else:
        lines.append("> _（对象数据的 `Ubertip` 字段为空：这件物品没有游戏内说明文本。）_")
    lines.append("")
    if p["tip"] and clean_inline(p["tip"]) != clean_inline(p["ubertip"]):
        # Tip 就是物品名/原名时没有信息量，别占一大块（审计问题 W026）
        if clean_inline(p["tip"]) in (p["display"], p["name"], p["base"]):
            lines += ["_（提示工具（Tip）与物品名相同，没有额外说明。）_", ""]
        else:
            lines += ["**提示工具（Tip）**：", "", "```text", detoken(p["tip"]), "```", ""]

    lines += ["## 获取方式", ""]
    lines += render_acquisition_human(p, src_row, boss_rows or [])
    src = sources.get(p["code"]) if sources else None
    if src:
        lines += ["### 全部证据明细", "", render_sources(src, item_names, unit_names)]
    else:
        lines.append("**待考证**——尚未在本图 `war3map.j` 中找到该物品的获取证据。")
        lines.append("")
        lines.append("> `war3map.j` 中的获取入口只有 `AddItemToStock`（进货）、`CreateItem`（生成）、"
                     "`UnitAddItemByIdSwapped`（掉给单位）、`ChooseRandomItemExBJ`（随机掉落）几类；"
                     "没有命中的物品不等于无法获得，可能由商店菜单、NPC 对话或外部触发器间接给出。")
        lines.append("")

    lines += ["## 合成与材料用途", ""]
    lines.append(render_materials(src, used_in.get(p["code"]) or [], item_names))

    lines += ['??? note "全部对象字段（原始值）"', "",
              "    这是 `war3map.w3t` 里这件物品的**全部字段原始值**，字段名保留魔兽内部 id（**加粗**的是中文名）。",
              "    正常阅读不用看这里；要改数值请看上面的「可改数值项」。", ""]
    for ini_key in sorted(f.keys()):
        for r in f[ini_key]:
            fid = r.get("field", "")
            zh = field_zh(fid) if fid else clean_inline(r.get("zh") or "")
            lv = f" (Lv{r['level']})" if r.get("level") not in (None, "") else ""
            val = detoken(clean_inline(v(r.get("value"))))
            if val == "":
                val = "（对象数据中此字段为空字符串）"
            lines.append(f"    - `{fid}` **{esc(zh)}**（{ini_key}）{lv} = `{val}`")
    lines.append("")

    lines.append(source_footer([
        f"物品字段：`war3map.w3t`（SHA256 `{MEMBER_SHA['war3map.w3t']}`）；"
        f"物品技能：`war3map.w3a`（SHA256 `{MEMBER_SHA['war3map.w3a']}`）；"
        f"物品技能字段中文名来自客户端 `War3Patch.mpq` 的 `Units\\AbilityMetaData.slk` + `UI\\WorldEditStrings.txt`。",
        "**说明文字（Tip/Ubertip）是策划手写的，可能与实际触发器数值不一致**；本页数值列取自对象数据的真实字段。",
    ]))
    return "\n".join(lines)


_MISMATCH_TAG = re.compile(r"^\[([^\]]+)\]")


def _mismatch_summary(anchor) -> str:
    cnt = collections.Counter()
    for m in ((anchor or {}).get("mismatches") or []):
        mm = _MISMATCH_TAG.match(str(m).strip())
        cnt[mm.group(1) if mm else "其它"] += 1
    return "、".join(f"{k} {n} 处" for k, n in cnt.most_common())


def render_natural_language(p, anchor, text_row, src_row=None) -> list:
    """## 功能描述（人话版）——把物品技能数值转写成一句自然语言。

    没有数值可转写时（本图 220 件物品没有绑定物品技能），**不写占位符**，而是改成
    「说明原文 + 分类推断 + 获取方式 + 要改怎么办」的证据合成句：全部来自游戏内说明文字
    （`Tip`/`Ubertip`）与 `items_source.csv` 的获取证据，不臆造效果。
    """
    out = ["## 功能描述（人话版）", ""]
    desc = clean_inline((anchor or {}).get("nl_desc") or "")
    if not desc:
        auto = clean_inline((text_row or {}).get("功能描述(由数值生成)") or "")
        desc = auto.replace("✔", "（说明里出现过）") if auto else ""
    synthesized = not desc
    if desc:
        out += [desc, ""]
    else:
        out += _synth_desc(p, anchor, src_row)

    if synthesized:
        out += ["> 上面的描述**由游戏内说明原文 + 获取/用途数据合成**"
                "（这件物品没有可转写的数值字段，所以没有数值转写）；"
                "凡标了「**按本站分类推断**」的行都是推断，不是对象数据里的字段。", ""]
        return out

    bits = []
    conf = (anchor or {}).get("confidence")
    if conf:
        bits.append(f"自动转写置信度 **{conf}**")
    ms = _mismatch_summary(anchor)
    if ms:
        bits.append("与说明原文的差异：" + ms)
    if bits:
        out += ["> " + "；".join(bits) + "。",
                "> 描述由**物品技能的对象数值**（`war3map.w3a`）自动转写；"
                "游戏内说明是策划手写的，**两者不一致时以对象数值为准**（真实生效的是对象数值）。", ""]
    return out


# 分类 → 「它是做什么的」的推断句（用于没有数值可转写的物品；一律标明是推断）
_CAT_ROLE = {
    "传送与关卡": "传送/关卡类道具：用掉之后把人送到某个地点或开启关卡流程",
    "NPC功能物品": "NPC 功能道具：拿去和 NPC 交互（打造、兑换、提交、抽奖之类）",
    "任务物品": "任务/剧情道具：交给指定 NPC 或满足任务条件，本身不加属性",
    "素材": "合成材料：主要用来作为打造/合成的材料消耗掉",
    "消耗品": "消耗品：使用后生效（具体效果看下面说明原文）",
    "武器": "武器：属性写在对象数据里，见下面「可改数值项」",
    "装甲": "护甲：属性写在对象数据里，见下面「可改数值项」",
    "灵魂装备": "灵魂装备：属性写在对象数据里，见下面「可改数值项」",
}


def _synth_desc(p, anchor, src_row) -> list:
    """没有物品技能时的人话版描述：说明原文 + 分类推断 + 获取方式 + 改动入口。"""
    out = []
    ub = clean_text((anchor or {}).get("ubertip_clean")
                    or (anchor or {}).get("ubertip_raw") or "")
    tip = clean_text((anchor or {}).get("tip_raw") or "")
    shown = ub or tip
    abil = p.get("abil") or []
    if not abil:
        if shown:
            out.append("这件物品**没有绑定物品技能**（对象数据里 `iabi` 是空的），所以它本身**不加任何数值** —— "
                       "它的作用完全写在游戏内说明文字里：")
        else:
            out.append("这件物品**没有绑定物品技能**（对象数据里 `iabi` 是空的），"
                       "而且对象数据里**连 `Tip`/`Ubertip` 都是空的** —— 站内没有任何可读的效果描述：")
    else:
        out.append("它的说明文字如下（对象数据里的技能字段没有可机械转写的数值）：")
    out.append("")
    if shown:
        for ln in [x.strip() for x in shown.splitlines() if x.strip()]:
            # 正文不能出现未解析的 <AIxx,DataYy> 占位符（审计问题 W001/W004）
            out.append("> " + esc(detoken(clean_inline(ln))))
    else:
        out.append("> _（说明文字为空：只能从名字、分类与获取方式判断它的用途。）_")
    out.append("")

    role = _CAT_ROLE.get(p.get("cat") or "")
    bullets = []
    if "<AI" in (shown or ""):
        bullets.append("- **数值为什么改不了**：说明里的尖括号是**原版（暴雪）技能**的数值占位符，"
                       "本图 `war3map.w3a` 里没有对应对象 —— 数值由魔兽原版决定，"
                       "要改必须先把那个技能复制成自定义技能对象，再挂到这件物品上（见下面的「可改数值项」）。")
    if role:
        bullets.append(f"- **它大概是做什么的**：{role}（**按本站分类推断**，不是对象数据里的字段）")
    else:
        bullets.append("- **它大概是做什么的**：分类是「不归类」，站内无法从数据判断用途——"
                       + ("请看上面的说明原文" if shown else "连说明文字都没有，只能按名字与出现位置判断")
                       + "，或按获取方式定位它出现在哪段流程里（**推断，非字段**）")
    if src_row:
        avail = (src_row.get("可获得性") or "").strip()
        main = (src_row.get("主要获取方式") or "").strip()
        use = (src_row.get("用途") or "").strip()
        if avail:
            bullets.append(f"- **能不能拿到**：{avail}（见下面「获取方式」一节的依据）")
        if main:
            bullets.append(f"- **怎么拿到**：{main}")
        if use:
            bullets.append(f"- **用途**：{use}")
    bullets.append("- **要改它怎么办**：它没有可机械改写的数值项 —— 改动只能落在**说明文字**"
                   "（`war3map.w3t` 的 `Tip`/`Ubertip`）或**触发器逻辑**（`war3map.j`）上。"
                   "在需求单仓库 `happy-fish-patch-plan` 用「口语需求」Issue 说人话即可（例如"
                   "「XX 物品的说明改成…」或「XX 传送物品改成传到第 N 层」）。")
    out += bullets + [""]
    return out


def render_changeable(p, anchor, zh_to_fid, hdr_rows=None) -> list:
    """## 可改数值项——玩家/策划说要改哪个数，就改这里列的哪个字段。"""
    out = ["## 可改数值项（改这些值会写进地图对象）", ""]
    vals = [v for v in ((anchor or {}).get("values") or []) if isinstance(v, dict)]
    hdr_rows = [r for r in (hdr_rows or []) if isinstance(r, dict)]
    if not vals and not hdr_rows:
        out += ["_（这件物品没有可机械修改的数值项。）_", "",
                "> 常见原因：它没绑定物品技能，或只挂标准暴雪技能（`AIxx`）——"
                "这类数值由魔兽原版决定，要改必须先把技能对象复制成自定义技能再改。", ""]
        return out

    rows = []
    for v in vals:
        fid = (v.get("field") or zh_to_fid.get((v.get("field_zh") or "").strip(), "") or "").strip()
        zh = (v.get("field_zh") or "").strip() or field_zh(fid) or fid
        extra = []
        if v.get("scale") == "x100" and v.get("raw_value") is not None:
            extra.append(f"原始值 {fmt_num(v.get('raw_value'))}（= {fmt_num(v.get('value'))}%）")
        unit = (v.get("unit") or "").strip()
        if unit and unit != "%":
            extra.append(f"单位：{unit}")
        rows.append([
            ("✔ " if v.get("in_desc") else "") + esc(zh),
            esc(fmt_num(v.get("value"))),
            code(fid),
            blank(v.get("level"), ""),
            "每级数值",
            esc("；".join(extra)) or "—",
        ])
    # 表头字段（冷却/耗魔/距离/范围/持续）来自需求单长表，与等级无关 → 等级列留空
    for r in hdr_rows:
        rows.append([
            esc(r.get("zh") or ""),
            esc(r.get("cur_value") or "") or "—",
            code((r.get("field") or "").strip()),
            blank((r.get("level") or "").strip(), ""),
            "表头字段",
            esc(r.get("note") or "") or "—",
        ])
    out += ["**类别**列里「每级数值」是技能对象 `Data` 里的分级数值，"
            "「表头字段」是技能级的冷却/耗魔/距离/范围/持续（与等级无关）。", "",
            table(["数值项", "当前值", "字段 id", "等级", "类别", "备注"], rows), "",
            "**怎么改**：到需求单仓库 `happy-fish-patch-plan` 打开 `data/item_ability_data.csv`，"
            "按 `item_code` + `ability_code` + `field` + `level` 找到对应行，把目标值写进 `new_value`，"
            "同行补 `req_id` 与 `note`；或者直接在「口语需求（自然语言）」Issue 里说人话，由我落表。", "",
            "> ✔ = 该数值在游戏内说明里出现过（说明与对象数值对得上）。"
            "标 `x100` 的百分比项：CSV 里的 `cur_value` 存的是**原始小数**（0.1 = 10%），`new_value` 也要填小数。", ""]
    return out


def render_acquisition_human(p, src_row, boss_rows) -> list:
    """获取方式的人话摘要 + 按来源（BOSS/宝箱/抽奖机）聚合的掉落表。"""
    out = []
    if src_row:
        avail = (src_row.get("可获得性") or "").strip()
        main = (src_row.get("主要获取方式") or "").strip()
        allw = (src_row.get("全部获取方式") or "").strip()
        floor = (src_row.get("掉落层") or "").strip()
        boss = (src_row.get("掉落BOSS") or "").strip()
        use = (src_row.get("用途") or "").strip()
        judged = (src_row.get("判定来源") or "").strip()
        out.append(f"- **能不能拿到**：{avail or '未判定'}")
        if main or allw:
            out.append(f"- **怎么拿**：{main or allw}")
        if floor:
            out.append(f"- **掉落层**：{floor}")
        if boss:
            out.append(f"- **掉落 BOSS**：{boss}")
        if use:
            out.append(f"- **用途**：{use}")
        if judged:
            out.append(f"- 判定依据：`{judged}`（明细见 `note_log/recon/item_source_gaps.json`）")
        out.append("")

    if boss_rows:
        groups = collections.OrderedDict()
        for r in boss_rows:
            groups.setdefault((r.get("组号") or "").strip(), []).append(r)
        rows = []
        for gid, rs in groups.items():
            head = {}
            for r in rs:
                for k in ("来源类型", "来源ID", "来源名称", "层", "层名"):
                    if not head.get(k) and (r.get(k) or "").strip():
                        head[k] = (r.get(k) or "").strip()
            label = "·".join(x for x in (head.get("来源类型"), head.get("来源名称")) if x)
            if head.get("来源ID"):
                label += f"（`{head['来源ID']}`）"
            where = " ".join(x for x in (head.get("层"), head.get("层名")) if x)
            first = True
            for r in rs:
                rows.append([
                    (f"**{gid}** {esc(label)}" if first else ""),
                    (esc(where) if first else ""),
                    code(r.get("item_code")),
                    esc(r.get("item_name") or ""),
                    blank(r.get("cur_chance_pct"), ""),
                    blank(r.get("cur_weight"), ""),
                    blank(r.get("cur_amount"), ""),
                    esc(clean_inline(r.get("证据") or "")),
                ])
                first = False
        out += ["### 按来源聚合的掉落（同一 BOSS/宝箱的多件掉落并排列出）", "",
                table(["来源（组号）", "所在层", "物品 ID", "物品名", "概率%", "权重", "数量", "证据"], rows), "",
                "> 组号 = `drops_by_boss.csv` 里的一格来源；同一组的继续行留空，表示它们来自同一个来源。", ""]
    elif (src_row or {}).get("可获得性", "").startswith("可获得"):
        out += ["_（这件物品的获取方式没有按来源聚合成组，见下方证据明细。）_", ""]
    return out


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
            rows.append([esc(kind_zh(e.get("kind"))), _nm(cond.split(", ") if cond else [], unit_names), code(e.get("line"))])
        section("事件生成（`CreateItemLoc`）", rows, ["方式", "触发单位", "j 行号"])

    # 10) 赠送
    if src.get("gift"):
        rows = [[esc(kind_zh(e.get("kind"))), esc(who_zh(e.get("to"))), code(e.get("line"))] for e in src["gift"]]
        section("触发时赠予", rows, ["方式", "给谁", "j 行号"])

    # 11) 拾取 / 使用触发
    if src.get("trigger_use"):
        rows = []
        for e in src["trigger_use"]:
            rows.append([esc(kind_zh(e.get("kind"))), _nm(e.get("produces") or [], item_names), code(e.get("used_at_line"))])
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
        parts += ["**作为材料参与合成**：明细与证据见上面「获取方式 → 作为材料被消耗」一节"
                  "（同一份 `item_sources.used_as_material` 数据，这里不再重复列表）。", ""]
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
