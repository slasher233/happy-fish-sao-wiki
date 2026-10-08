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
# 本版新增物品（issue #2）：物品字段 + 新建技能副本
PLAN_ITEMS_CSV = os.path.join(PLAN_DATA, "items.csv")
PLAN_ISSUE2_JSON = os.path.join(PLAN_DATA, "issue2_plan.json")
# 只有这两个需求单的 new_value 才是「本版计划值」
PLAN_CHANGE_REQS = ("issue2", "issue3")
NEW_ITEM_BANNER = "🆕 **本版本新增物品**"
# 需求单（2.61 源）里的类别用词 → 站内已有分类；不新增目录，避免无关页面跟着变
EXTRA_CLASS_CAT = {"装备道具": "灵魂装备"}
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


def type_zh(icla) -> str:
    """`class`（字段 `icla`）枚举 → 中文；缺失/未收录时写清依据（审计问题 W002）。"""
    s = (icla or "").strip()
    if not s:
        return "未设置（对象数据 `icla` 字段为空）"
    zh = CLASS_ZH.get(s)
    if zh:
        return f"{zh}（原始枚举 `{s}`）"
    return f"`{s}`（未收录的枚举值，站内暂未译）"


def who_zh(t) -> str:
    """把 unclassified 的「给谁」表达式翻成人话。

    认得出函数名就只写人话（审计问题 W012：`GetTriggerUnit(` 这种没写完的函数残片
    不能印给用户；行尾已有 `j 行号` 可回溯）；认不出的也只保留函数名 + 省略号。
    """
    s = clean_inline(str(t or ""))
    if not s or s in ("None", "—"):
        return "（无法确定目标）"
    m = _UNIT_EXPR_RE.match(s)
    if not m:
        return s
    who = _UNIT_EXPR_ZH.get(m.group(1))
    if who:
        return who
    fn = m.group(1).replace("`", "'")
    return f"（无法确定目标：触发器片段 `{fn}(...)`）"


# 同一属性在站内有两套叫法（审计问题 W016）：**客户端/编辑器的标准中文名**写「力量」「智力」，
# **本图说明原文与策划习惯**写「筋力」「体力」。每页首次出现写成「筋力（力量）」，
# 其后统一用图内叫法；原文引用块保留作者原文，另用 ATTR_NOTE 在页内说明一次。
ATTR_PAIRS = (("力量", "筋力"), ("智力", "体力"))
_ATTR_WORD_PAIR = {w: pair for pair in ATTR_PAIRS for w in pair}
_ATTR_REGEX = re.compile("|".join(w for pair in ATTR_PAIRS for w in pair))
_ATTR_ALIASED = tuple(f"{g}（{f}）" for f, g in ATTR_PAIRS)
ATTR_NOTE = ("用词说明：**客户端/编辑器**里这两个字段的标准中文名是「力量」「智力」，"
             "**本图说明原文**写「筋力」「体力」，说的是同一组属性；"
             "本站正文统一用图内叫法，必要时在括号里补标准名。")


def attr_unify(text, seen=None) -> str:
    """按 `seen`（每页一个 set）统一属性的两套叫法（审计问题 W016）。"""
    if seen is None:
        return str(text or "")

    def rep(m):
        pair = _ATTR_WORD_PAIR[m.group(0)]
        if pair[0] in seen:
            return pair[1]
        seen.add(pair[0])
        return f"{pair[1]}（{pair[0]}）"

    return _ATTR_REGEX.sub(rep, str(text or ""))


def attr_needs_note(lines) -> bool:
    """页面上（除「筋力（力量）」这种对照写法外）还出现过属性词时，加一行用词说明。"""
    body = "\n".join(lines)
    for alias in _ATTR_ALIASED:
        body = body.replace(alias, "")
    return any(w in body for pair in ATTR_PAIRS for w in pair)


def load_csv(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8-sig", newline="") as fh:
        return [row for row in csv.DictReader(fh)]

CATEGORY_ORDER = [
    "武器", "装甲", "副武器", "头部道具", "灵魂装备", "觉醒装备",
    "消耗品", "素材", "任务物品", "传送与关卡", "NPC功能物品", "不归类",
]

# 新物品的字段 id → 母图快照里的字段分组（`fields` 按 ini_key 存）
NEW_ITEM_FIELDS = (
    ("unam", "Name"), ("utip", "Tip"), ("utub", "Ubertip"), ("ides", "Description"),
    ("iico", "Art"), ("iabi", "abilList"), ("icla", "class"), ("igol", "goldcost"),
)


def load_plan_change_rows(path: str) -> dict:
    """`item_code` → [本版计划改动行]（`req_id` ∈ issue2/issue3 且 `new_value` 非空）。

    需求单里 `new_value` 就是「这一版要改成多少」；没有计划行的物品页不会出现任何计划内容。
    """
    out: dict[str, list] = {}
    for r in load_csv(path):
        if (r.get("req_id") or "").strip() not in PLAN_CHANGE_REQS:
            continue
        if not (r.get("new_value") or "").strip():
            continue
        c = (r.get("item_code") or "").strip()
        if c:
            out.setdefault(c, []).append(r)
    return out


def load_plan_items_csv(path: str) -> dict:
    """`item_code` → `items.csv` 行（本版本带 `new_*` 计划值的那些，用来读 `new_iabi`）。"""
    out: dict[str, dict] = {}
    for r in load_csv(path):
        c = (r.get("item_code") or "").strip()
        if c and (r.get("req_id") or "").strip() in PLAN_CHANGE_REQS:
            out[c] = r
    return out


def _plan_key(ability, field, level) -> tuple:
    """计划行与现值行的对应键：`(ability_code, field, level)`（等级统一成字符串再比）。"""
    return ((ability or "").strip(), (field or "").strip(),
            str("" if level is None else level).strip())


def _plan_new_value(row: dict, scale: str = "") -> str:
    """计划值的显示文本。

    百分比类字段（`x100`）的 `new_value` 存的是**原始小数**（0.2 = 20%），
    现值列用的是换算后的百分数，所以这里也要换算，否则会印成 `50 → 0.2`。
    """
    raw = (row.get("new_value") or "").strip()
    if not raw:
        return ""
    if scale == "x100":
        try:
            return fmt_num(str(float(raw) * 100))
        except (TypeError, ValueError):
            return raw
    return fmt_num(raw)


def _plan_cell(cur_text: str, new_text: str) -> str:
    """「本版计划值」单元格：能对上现值就写 `现值 → 计划值`，对不上（新增字段）只写计划值。"""
    if not new_text:
        return "—"
    if cur_text in ("", "—"):
        return f"**{esc(new_text)}**"
    return f"**{esc(cur_text)} → {esc(new_text)}**"


def plan_infer_scale(raw, text: str) -> str:
    """需求单行没有现成 `scale` 时（计划新增的字段 / 新物品），按物品说明里的数字反推是不是 ×100。

    说明里出现的数才是玩家看到的数：`0.5` 不在说明里、`50` 在 → 这是百分比字段（×100）。
    `100.0` 这种说明里写的是 `100`，那就不换算。说明里两个都找不到就按原样显示。
    """
    raw = str(raw or "").strip()
    text = text or ""
    if not raw or not text:
        return ""
    try:
        n = float(raw)
    except (TypeError, ValueError):
        return ""
    if fmt_num(str(n)) in text:
        return ""
    if fmt_num(str(n * 100)) in text:
        return "x100"
    return ""


def _synthetic_row(fid: str, val, fdict: dict, level) -> dict:
    """按母图快照的字段行形状造一行（`field`/`ini_key`/`zh`/`type`/`level`/`value`）。"""
    d = fdict.get(fid) or {}
    return {"field": fid, "ini_key": d.get("ini_key") or "", "zh": d.get("zh_label") or fid,
            "type": d.get("type"), "level": level, "value": v(val)}


def build_issue2_new_items(plan_path: str, plan_csv: dict, base_names: dict, fdict: dict):
    """把 `issue2_plan.json` 里 issue #2 的 10 件新物品造成 `parsed` 记录 + 它们的新建技能。

    母图快照（`items.json` / `abilities.json`）里**没有**这些对象（applier 会用模板深拷贝新建），
    所以这里按快照的逻辑形状手工合成物品字段 `fields`、技能列表 `abilList` 和 30 个新建技能对象，
    `render_item` 才能正常渲染。返回 `(记录列表, code → 技能对象)`。
    """
    if not os.path.exists(plan_path):
        print(f"  ! {os.path.basename(plan_path)} 不存在 → 本版新增物品不会进图鉴")
        return [], {}
    try:
        plan = load_json(plan_path)
    except Exception as e:  # noqa: BLE001
        print(f"  ! {os.path.basename(plan_path)} 解析失败（本版新增物品将缺失）：{e}")
        return [], {}

    new_abils: dict[str, dict] = {}
    for a in plan.get("abilities") or []:
        ac = str(a.get("new") or "").strip()
        if not ac:
            continue
        fields: dict[str, list] = {}
        for fid, val in (a.get("overrides") or {}).items():
            ini = (fdict.get(fid) or {}).get("ini_key") or "Other"
            fields.setdefault(ini, []).append(
                _synthetic_row(fid, val, fdict, 1 if ini == "Data" else None))
        new_abils[ac] = {"code": ac, "base": str(a.get("template") or ""), "fields": fields}

    out = []
    for it in plan.get("items") or []:
        c = str(it.get("new") or "").strip()
        if not c:
            continue
        crow = plan_csv.get(c) or {}
        mods = it.get("mods") or {}
        name = clean_inline(mods.get("unam") or crow.get("name") or it.get("name") or "")
        tip_raw = str(mods.get("utip") or "")
        ub_raw = str(mods.get("utub") or mods.get("ides") or "")
        iabi = str(mods.get("iabi") or crow.get("new_iabi") or "")
        fields: dict[str, list] = {}
        for fid, ini in NEW_ITEM_FIELDS:
            val = mods.get(fid)
            if val in (None, ""):
                continue
            fields.setdefault(ini, []).append(_synthetic_row(fid, val, fdict, None))
        if (crow.get("new_ilev") or "").strip():
            fields.setdefault("Level", []).append(_synthetic_row("ilev", crow["new_ilev"], fdict, None))
        cls_zh = str(it.get("cls") or "").strip()
        cls_zh = EXTRA_CLASS_CAT.get(cls_zh, cls_zh)
        origin = str(it.get("old") or "").strip()
        tpl = str(it.get("template") or crow.get("base") or "").strip()
        obname = base_names.get(origin, "") or base_names.get(origin.lower(), "")
        abil_list = [x.strip() for x in iabi.split(",") if x.strip()]
        # 母图里没有这件物品，所以 recon 的 anchors 也没有它：手工造一份，让「功能描述（人话版）」
        # 不至于印成「说明文字为空 / 没有可机械改写的数值项」。计划值走 render_changeable 的计划表。
        nvals = []
        for ac in abil_list:
            for rr in ((new_abils.get(ac) or {}).get("fields") or {}).get("Data") or []:
                nvals.append(f"{(rr.get('zh') or rr.get('field') or '').strip()}={rr.get('value')}")
        nl_desc = "本版新增物品（母图 v1.0 正式版里还没有，随下一版补丁上线）"
        nl_desc += ("：" + "、".join(nvals) + "。") if nvals else "。"
        out.append({
            "code": c,
            "base": tpl,
            "base_name": obname,
            "name": name,
            "display": name or f"未设置名称（新增 {c}）",
            "tip": clean_text(tip_raw),
            "ubertip": clean_text(ub_raw),
            "icla": clean_inline(mods.get("icla")),
            "cat": cls_zh if cls_zh in CATEGORY_ORDER else classify(
                name, tip_raw, ub_raw, clean_inline(mods.get("icla"))),
            "quality": clean_inline(it.get("quality") or "") or quality_of(clean_text(ub_raw)),
            "fields": fields,
            "abil": abil_list,
            "anchor": {
                "code": c,
                "name": name,
                "item_name": name,
                "item_class": clean_inline(mods.get("icla")),
                "has_abil": bool(abil_list),
                "abil_list": abil_list,
                "tip_raw": tip_raw,
                "ubertip_raw": ub_raw,
                "ubertip_clean": clean_text(ub_raw),
                "nl_desc": nl_desc,
                "values": [],
                "mismatches": [],
                "confidence": None,
            },
            "new_item": True,
            "template": tpl,
            "origin": origin,
            "origin_name": obname,
            "issue_code": str(it.get("issue_code") or "").strip(),
        })
    return out, new_abils


def render_new_item_banner(p, plan_csv_row=None) -> list:
    """新增物品页顶部的醒目提示：母图 v1.0 正式版里还没有这件物品。"""
    tpl = p.get("template") or p.get("base") or ""
    origin = p.get("origin") or ""
    iv = str((plan_csv_row or {}).get("new_iabi") or "")
    src = f"由母图模板 `{tpl}` 深拷贝新建" if tpl else "按需求单新建"
    if origin:
        src += f"（原始原型 `{origin}`{(' ' + p.get('origin_name')) if p.get('origin_name') else ''}）"
    out = [f"> {NEW_ITEM_BANNER}（**随下一版补丁上线**，母图 v1.0 正式版里还没有这件物品）：{src}。", ""]
    abilities = [x.strip() for x in iv.split(",") if x.strip()]
    if abilities:
        out += [f"> 本版新建的技能对象：{'、'.join(code(x) for x in abilities)}。"
                "页内数值取自需求单 `patch_plan/data/issue2_plan.json` 与 "
                "`patch_plan/data/item_ability_data.csv`（`req_id=issue2`），"
                "掉落取自 `patch_plan/data/drops_by_boss.csv`；本页**未经实机验证**。", ""]
    return out

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
            "new_item": False,
        })

    # ── 本版需求单：计划改动行（issue2/issue3）+ issue #2 的 10 件新物品 ──
    # 计划行：item_ability_data.csv 里 new_value 非空的行，页面显示「现值 → 本版计划值」
    plan_rows = load_plan_change_rows(PLAN_ITEM_ABILITY)
    plan_csv = load_plan_items_csv(PLAN_ITEMS_CSV)
    # 新物品：母图快照里不存在，用 issue2_plan.json 合成记录 + 新建技能对象
    new_items, new_abils = build_issue2_new_items(PLAN_ISSUE2_JSON, plan_csv, base_names, fdict)
    _have = {x["code"] for x in parsed}
    _dup = [x["code"] for x in new_items if x["code"] in _have]
    if _dup:
        print(f"  ! 新增物品 {'、'.join(_dup)} 已存在于母图快照 → 跳过，避免重复页面")
        new_items = [x for x in new_items if x["code"] not in _have]
    for _c, _a in new_abils.items():
        if _c in abils:
            print(f"  ! 新建技能 {_c} 与母图 abilities.json 里的对象同名 → 保留母图对象")
        else:
            abils[_c] = _a
    parsed += new_items
    print(f"  · 本版计划改动行：{sum(len(x) for x in plan_rows.values())} 行 / {len(plan_rows)} 件物品"
          "（item_ability_data.csv，req_id ∈ issue2/issue3 且 new_value 非空）")
    print(f"  · 本版新增物品：{len(new_items)} 件（issue #2，母图快照里不存在）；"
          f"新建技能对象 {len(new_abils)} 个")

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
                               anchors.get(p["code"]) or anchors.get("#" + p["name"]) or anchors.get("#" + p["display"]) or p.get("anchor"),
                               text_rows.get(p["code"]), src_rows.get(p["code"]),
                               boss_rows.get(p["code"]) or [], zh_to_fid,
                               hdr_rows.get(p["code"]) or [],
                               plan_rows.get(p["code"]) or [], plan_csv.get(p["code"])))

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
           f"共 **{len(parsed)}** 个物品对象（没有自定义名称的 {len(no_name)} 个显示为「未设置名称（原型 …）」："
           f"{'、'.join(no_name) or '无'}）。", ""]
    _new_items = [p for p in parsed if p.get("new_item")]
    if _new_items:
        idx += [f"其中 **{len(_new_items)}** 件是**本版本新增**物品"
                "（随下一版补丁上线，母图 v1.0 正式版里还没有）："
                + "、".join(f"{link(p['file'], '`%s`' % p['code'])} {esc(p['display'])}"
                            for p in sorted(_new_items, key=lambda x: x["code"])) + "。", ""]
    idx += ["分类由游戏内说明里的类型标签与名称规则**自动推断**，推断结果可能有误——以每页的说明原文为准。", "",
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
                boss_rows=None, zh_to_fid=None, hdr_rows=None,
                plan_rows=None, plan_csv_row=None) -> str:
    f = p["fields"]
    icla = (p["icla"] or "").strip()
    attr_seen: set = set()  # 属性用词对照（W016）：每页一份，首次出现写「筋力（力量）」
    lines = [f"# {p['code']} · {p['display']}", ""]
    if p.get("new_item"):
        lines += render_new_item_banner(p, plan_csv_row)

    price = clean_inline(first(f, "goldcost"))
    meta = [
        f"**分类**：{p['cat']}",
        f"**品质**：{val_or(p['quality'], '无数据（说明里没写品质）')}",
        f"**类型**：{type_zh(icla)}",
        f"**物品等级**：{val_or(clean_inline(first(f, 'Level')), '未设置（对象数据里没有这一项）')}",
        f"**价格**：{val_or(price, '未设置（对象数据里没有这一项）')}" + (" 金" if price else ""),
    ]
    lines.append("> " + "\u3000".join(meta))
    lines.append("")
    proto = f"`{p['base']}`"
    if p["base_name"]:
        proto += f"（{p['base_name']}）"
    ver = MAP_VERSION + ("（本版新增，母图 v1.0 正式版中尚无此对象）" if p.get("new_item") else "")
    lines.append(f"**物品 ID**：`{p['code']}`　·　**原型**：{proto}　·　**版本**：{ver}")
    lines.append("")

    lines += render_natural_language(p, anchor, text_row, src_row, attr_seen)
    lines += render_changeable(p, anchor, zh_to_fid or {}, hdr_rows, plan_rows, plan_csv_row,
                               attr_seen)
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
                    zh = attr_unify(d.get("zh_label") or fid, attr_seen)
                    stat_rows.append([
                        esc(zh),
                        esc(v(r.get("value"))),
                        f"`{ac}`",
                        code(fid),
                        blank(r.get("level"), ""),
                    ])
                    keybits.append(f"{zh}={v(r.get('value'))}")
                elif d.get("ini_key") in ("Cost", "Cool") and r.get("level") in (1, "1", None):
                    keybits.append(f"{attr_unify(d.get('zh_label') or fid, attr_seen)}={v(r.get('value'))}")
        ability_rows.append([code(ac), esc(anam) or "—", esc(", ".join(keybits)) or "—", esc(aub) or "—"])

    if stat_rows:
        lines.append(table(["属性", "数值", "来源能力", "字段", "等级"], stat_rows))
    else:
        lines.append("_（本节无内容：本物品的 `abilList`（字段 `iabi`）里没有带 `Data` 数值字段的物品技能，"
                     "对象数据里确实没有属性数值可列。）_")
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
        lines.append("_（本节无内容：对象数据的 `abilList`（字段 `iabi`）为空，本物品没有绑定任何能力对象。）_")
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
              "    这是 `war3map.w3t` 里这件物品的**全部字段原始值**，字段名保留魔兽内部 id（**加粗**的是中文名）——"
              "字段 id 与中文名的完整对照见 [对象字段对照表](/info/对象字段对照表/)。",
              "    正常阅读不用看这里；要改数值请看上面的「可改数值项」。", ""]
    for ini_key in sorted(f.keys()):
        for r in f[ini_key]:
            fid = r.get("field", "")
            zh = attr_unify(field_zh(fid) if fid else clean_inline(r.get("zh") or ""), attr_seen)
            lv = f" (Lv{r['level']})" if r.get("level") not in (None, "") else ""
            val = detoken(clean_inline(v(r.get("value"))))
            if val == "":
                val = "（对象数据中此字段为空字符串）"
            lines.append(f"    - `{fid}` **{esc(zh)}**（{ini_key}）{lv} = `{val}`")
    lines.append("")

    # 属性用词说明放在页首（审计问题 W016：同一页里两套叫法都出现时说明一次）
    if attr_needs_note(lines):
        i = next((k for k, s in enumerate(lines) if s.startswith("**物品 ID**：")), None)
        if i is not None:
            lines[i + 2:i + 2] = [f"> {ATTR_NOTE}", ""]

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


def render_natural_language(p, anchor, text_row, src_row=None, attr_seen=None) -> list:
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
        out += [attr_unify(desc, attr_seen), ""]
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


def render_changeable(p, anchor, zh_to_fid, hdr_rows=None, plan_rows=None, plan_csv_row=None,
                      attr_seen=None) -> list:
    """## 可改数值项——玩家/策划说要改哪个数，就改这里列的哪个字段。

    `plan_rows` 是本版需求单（`patch_plan/data/item_ability_data.csv`）里 `new_value` 非空的行。
    有计划值的物品会多一列**本版计划值**：能按 `(ability_code, field, level)` 对上现有行的就地写
    「现值 → 计划值」；对不上的（计划新增的字段/技能）单独列在下面，不丢。
    没有计划行的物品页与改动前**逐字节一致**。
    """
    out = ["## 可改数值项（改这些值会写进地图对象）", ""]
    vals = [v for v in ((anchor or {}).get("values") or []) if isinstance(v, dict)]
    hdr_rows = [r for r in (hdr_rows or []) if isinstance(r, dict)]
    plan_rows = [r for r in (plan_rows or []) if isinstance(r, dict)]
    if not vals and not hdr_rows and not plan_rows:
        lack = ("对象数据的 `abilList`（字段 `iabi`）为空" if not (p.get("abil") or "")
                else "它绑定的技能里没有 `Data` 数值字段")
        out += [f"_（本节无内容：{lack} —— 对象数据里没有可机械修改的数值项。）_", "",
                "> 常见原因：它没绑定物品技能，或只挂标准暴雪技能（`AIxx`）——"
                "这类数值由魔兽原版决定，要改必须先把技能对象复制成自定义技能再改。", ""]
        return out

    show_plan = bool(plan_rows)
    plan_index = collections.defaultdict(list)
    for i, r in enumerate(plan_rows):
        plan_index[_plan_key(r.get("ability_code"), r.get("field"), r.get("level"))].append(i)
    claimed: set = set()

    def take_plan(ability, field, level):
        """取一条还没被其它行认领的计划行（同一 (技能,字段,等级) 有多条时按顺序取）。"""
        for i in plan_index.get(_plan_key(ability, field, level), []):
            if i not in claimed:
                claimed.add(i)
                return plan_rows[i]
        return None

    def cell(cur_text: str, pr, scale: str = "") -> list:
        """有计划的物品才多这一格「本版计划值」。"""
        if not show_plan:
            return []
        return [_plan_cell(cur_text, _plan_new_value(pr, scale)) if pr else "—"]

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
        cur = esc(fmt_num(v.get("value")))
        rows.append([
            ("✔ " if v.get("in_desc") else "") + esc(attr_unify(zh, attr_seen)),
            cur,
        ] + cell(cur, take_plan(v.get("ability"), fid, v.get("level")), v.get("scale") or "") + [
            code(fid),
            blank(v.get("level"), ""),
            "每级数值",
            esc("；".join(extra)) or "—",
        ])
    # 表头字段（冷却/耗魔/距离/范围/持续）来自需求单长表，与等级无关 → 等级列留空
    for r in hdr_rows:
        cur = esc(r.get("cur_value") or "") or "—"
        rows.append([
            esc(attr_unify(r.get("zh") or "", attr_seen)),
            cur,
        ] + cell(cur, take_plan(r.get("ability_code"), (r.get("field") or "").strip(),
                                 (r.get("level") or "").strip())) + [
            code((r.get("field") or "").strip()),
            blank((r.get("level") or "").strip(), ""),
            "表头字段",
            esc(r.get("note") or "") or "—",
        ])

    # 计划里有、但上面现值表里没有对应行的（本版新增的字段/技能）单独列出，不丢
    _ptext = (p.get("ubertip") or "") + "\n" + (p.get("tip") or "")
    plan_extra = []
    for i, r in enumerate(plan_rows):
        if i in claimed:
            continue
        fid = (r.get("field") or "").strip()
        if fid == "anam":
            continue  # 技能显示名（如「增加最大生命值12000」），不是玩家可改的数值
        plan_extra.append([
            esc(attr_unify((r.get("zh") or "").strip() or field_zh(fid) or fid, attr_seen)),
            _plan_cell("", _plan_new_value(r, plan_infer_scale(r.get("new_value"), _ptext))),
            code(fid),
            blank((r.get("level") or "").strip(), ""),
            code((r.get("ability_code") or "").strip())
            + ((" " + esc(r.get("ability_name"))) if (r.get("ability_name") or "").strip() else ""),
            esc(r.get("note") or "") or "—",
        ])

    out += ["**类别**列里「每级数值」是技能对象 `Data` 里的分级数值，"
            "「表头字段」是技能级的冷却/耗魔/距离/范围/持续（与等级无关）。", ""]
    if show_plan:
        reqs = sorted({(r.get("req_id") or "").strip() for r in plan_rows if (r.get("req_id") or "").strip()})
        out += ["**本版计划改动**：「本版计划值」列来自需求单 `patch_plan/data/item_ability_data.csv`"
                + (f"（本页改动行 `req_id` = {'、'.join('`%s`' % x for x in reqs)}）" if reqs else "")
                + "；把目标值写进 `new_value` **即生效，随下一版补丁上线**。"
                "单元格 `50 → 20` 读作「现值 50，本版上线后为 20」。", ""]
        nb = str((plan_csv_row or {}).get("new_iabi") or "").strip()
        ob = str((plan_csv_row or {}).get("cur_iabi") or "").strip()
        if nb and nb != ob:
            out += [f"> 本版还会把技能列表从 `{ob or '（空）'}` 换成 `{nb}`"
                    "（换上的技能是母图技能的副本，见 `patch_plan/data/items.csv` 的 `new_iabi`）。", ""]
    if rows:
        head = ["数值项", "当前值", "本版计划值", "字段 id", "等级", "类别", "备注"] if show_plan else \
               ["数值项", "当前值", "字段 id", "等级", "类别", "备注"]
        out += [table(head, rows), ""]
    if plan_extra:
        out += ["### 本版计划新增的数值（上面现值表里没有对应行）", "",
                table(["数值项", "本版计划值", "字段 id", "等级", "来源技能", "备注"], plan_extra), "",
                "> 这些是需求单里**新增**的字段/技能（母图现在还没有这一行）；"
                "写 `new_value` 即生效，随下一版补丁上线。", ""]
    out += ["**怎么改**：到需求单仓库 `happy-fish-patch-plan` 打开 `data/item_ability_data.csv`，"
            "按 `item_code` + `ability_code` + `field` + `level` 找到对应行，把目标值写进 `new_value`，"
            "同行补 `req_id` 与 `note`；或者直接在「口语需求（自然语言）」Issue 里说人话，由我落表。", "",
            "> ✔ = 该数值在游戏内说明里出现过（说明与对象数值对得上）。"
            "标 `x100` 的百分比项：CSV 里的 `cur_value` 存的是**原始小数**（0.1 = 10%），`new_value` 也要填小数。", ""]
    return out


def _cur_or_plan(r: dict, name: str) -> str:
    """掉落表的现值格：母图里没有现值（本版新增的掉落行）时回落到计划值 `new_*`，其余原样输出。"""
    cur = r.get("cur_" + name)
    if cur not in (None, ""):
        return blank(cur, "")
    return blank(r.get("new_" + name), "")


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
                    _cur_or_plan(r, "chance_pct"),
                    _cur_or_plan(r, "weight"),
                    _cur_or_plan(r, "amount"),
                    esc(clean_inline(r.get("证据") or "")),
                ])
                first = False
        out += ["### 按来源聚合的掉落（同一 BOSS/宝箱的多件掉落并排列出）", "",
                table(["来源（组号）", "所在层", "物品 ID", "物品名", "概率%", "权重", "数量", "证据"], rows), "",
                "> 组号 = `drops_by_boss.csv` 里的一格来源；同一组的继续行留空，表示它们来自同一个来源。", ""]
        if p.get("new_item"):
            out += ["> 本物品是**本版新增**：上面的掉落行来自 `patch_plan/data/drops_by_boss.csv`"
                    "（`req_id=issue2`，概率% 列是**本版计划值**，母图里还没有这条掉落），随下一版补丁上线。", ""]
    elif (src_row or {}).get("可获得性", "").startswith("可获得"):
        out += ["_（本节无内容：`item_sources.json` 里这件物品的来源没有记到具体 BOSS/宝箱/店，"
                "只有「可获得」这一条笼统记录；逐条证据见下方「全部证据明细」。）_", ""]
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
        section("商店出售（`AddItemToStock` 进货）", rows, ["商店", "接口", "当前库存", "最大库存", "触发器行号（`war3map.j`）"])

    # 2) 商店货架（对象数据）
    if src.get("vendor_object_data"):
        rows = []
        for e in src["vendor_object_data"]:
            shop = e.get("shop_name") or unit_names.get(e.get("shop_unit") or "", "") or e.get("shop_unit") or "—"
            rows.append([esc(shop), code(e.get("shop_unit")), code(e.get("field")), esc(e.get("field_name") or ""), esc(e.get("line_ref") or "")])
        section("商店货架（对象数据 `usei`/`umki`）", rows, ["商店", "商店单位", "字段", "字段名", "证据位置"])

    if src.get("vendor_removed"):
        rows = [[code(e.get("shop_unit")), code(e.get("line")), "`" + clean_inline(e.get("snippet") or "")[:110].replace("`", "'") + "`"] for e in src["vendor_removed"]]
        section("该物品被从商店移除（`RemoveItemFromStock`）", rows, ["商店单位", "触发器行号（`war3map.j`）", "原始片段"])

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
        section("抽奖 / 扭蛋", rows, ["触发物", "产出", "消耗", "触发器行号（`war3map.j`）"])

    # 4) 打造 / 合成
    if src.get("craft"):
        rows = []
        for e in src["craft"]:
            trig = (esc(e.get("trigger_item_name") or "") + " " + code(e.get("trigger_item"))) if e.get("trigger_item") else "（自动合成）"
            mats = e.get("consumed_materials") or e.get("checked_materials") or []
            rows.append([trig, _nm(mats, item_names), code(e.get("cond_line") or e.get("line")),
                         "⚠️ 材料不符" if e.get("material_mismatch") else "—"])
        section("打造 / 合成", rows, ["触发物", "消耗材料", "触发器行号（`war3map.j`）", "备注"])

    # 5) 掉落
    if src.get("drop"):
        rows = []
        for e in src["drop"]:
            su = e.get("source_unit") or ""
            sun = e.get("source_unit_name") or unit_names.get(su, "")
            chance = e.get("chance_pct")
            rows.append([
                (f"`{su}`" + (f" {esc(sun)}" if sun else "")) if su else "（未标注来源单位）",
                esc(kind_zh(e.get("method") or e.get("kind")) if (e.get("method") or e.get("kind")) else ""),
                (f"{chance}%" if chance is not None else "—"),
                code(e.get("line") or e.get("choose_line")),
            ])
        section("掉落（掉落表 / 权重表）", rows, ["来源单位", "方式", "概率", "触发器行号（`war3map.j`）"])

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
        section(label, rows, ["另一形态", "击杀阈值", "触发器行号（`war3map.j`）"])

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
        section("事件生成（`CreateItemLoc`）", rows, ["方式", "触发单位", "触发器行号（`war3map.j`）"])

    # 10) 赠送
    if src.get("gift"):
        rows = [[esc(kind_zh(e.get("kind"))), esc(who_zh(e.get("to"))), code(e.get("line"))] for e in src["gift"]]
        section("触发时赠予", rows, ["方式", "给谁", "触发器行号（`war3map.j`）"])

    # 11) 拾取 / 使用触发
    if src.get("trigger_use"):
        rows = []
        for e in src["trigger_use"]:
            rows.append([esc(kind_zh(e.get("kind"))), _nm(e.get("produces") or [], item_names), code(e.get("used_at_line"))])
        section("拾取 / 使用触发", rows, ["方式", "产出", "触发器行号（`war3map.j`）"])

    # 12) 作为材料被消耗
    if src.get("used_as_material"):
        rows = []
        for e in src["used_as_material"]:
            rows.append([esc(e.get("trigger_item_name") or "") + " " + code(e.get("trigger_item")),
                         _nm([e.get("result")], item_names), code(e.get("line"))])
        section("作为材料被消耗", rows, ["触发卷轴/菜单", "合成结果", "触发器行号（`war3map.j`）"])

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
        # 审计问题 W014：空章节要写清「查了什么、所以为空」，不能只丢一句「没有证据」
        parts.append("_（本节无内容：`item_sources.json` 里这件物品既没有 `used_as_material`、"
                     "也没有 `consumed_only` 记录，全物品的说明文本（Tip/Ubertip）里也没有任何物品"
                     "提到它（文本匹配，不等于真实配方）；逐条证据见下方「全部证据明细」。）_")
        parts.append("")
    return "\n".join(parts)


if __name__ == "__main__":
    main()
