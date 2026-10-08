"""生成站点骨架页面：首页、技能总览、info 页、更新日志首页。

数据来源：note_log/wiki_data/*.json、note_log/recon/*.tsv、note_log/index/*.tsv
只读脚本：不修改地图。
"""
from __future__ import annotations

import collections
import csv
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wiki_common import (  # noqa: E402
    DOCS, INDEX_DIR, MAP_NAME, MAP_SHA256, MAP_VERSION, MEMBER_SHA, RECON_DIR, W,
    WIKI_DATA, blank, clean_inline, clean_text, code, esc, field_zh_map, load_json,
    obj_code, source_footer, table, write_page,
)

HERO_TSV = os.path.join(RECON_DIR, "heroes.tsv")
UNBOUND_TSV = os.path.join(RECON_DIR, "abilities_not_on_heroes.tsv")
ITEMS_JSON = os.path.join(WIKI_DATA, "items.json")
ABIL_JSON = os.path.join(WIKI_DATA, "abilities.json")
UNITS_JSON = os.path.join(WIKI_DATA, "units.json")
# 私有需求单仓库（只读引用）
PATCH_DATA = os.path.join(W, "patch_plan", "data")
SKILL_TEXT_CSV = os.path.join(PATCH_DATA, "hero_skill_text.csv")
ABILITY_DATA_CSV = os.path.join(PATCH_DATA, "hero_ability_data.csv")


def load_tsv(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def load_csv(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def load_skill_text(path: str) -> dict:
    """`ability_code` → 需求单行（说明原文）。两张需求单表必须按 ability_code 索引。"""
    out = {}
    for r in load_csv(path):
        c = (r.get("ability_code") or "").strip()
        if c:
            out.setdefault(c, r)
    return out


def load_ability_data(path: str) -> dict:
    """`ability_code` → [可改数值行]（只取 `slk_col == "Data"` 的平衡数值行）。"""
    out: dict[str, list] = {}
    for r in load_csv(path):
        if (r.get("slk_col") or "").strip() != "Data":
            continue
        c = (r.get("ability_code") or "").strip()
        if c:
            out.setdefault(c, []).append(r)
    return out


def is_unreachable(h: dict) -> bool:
    """`heroes.tsv` 的 `reachable` 实际取值是 `NO(地图上无此单位)` / `yes(legacy，…)`，
    必须 `startswith("no")`，`== "no"` 会漏判（审计问题 W010）。"""
    return str(h.get("reachable") or "").lower().startswith("no")


def hero_scope(heroes: list[dict]) -> tuple[int, int, int]:
    """(可选, 地图上无此单位, 英雄数据条数)——口径与 `docs/heroes/index.md` 一致。"""
    n_no = sum(1 for h in heroes if is_unreachable(h))
    return len(heroes) - n_no, n_no, len(heroes)


def scope_text(heroes: list[dict]) -> str:
    ok, no, total = hero_scope(heroes)
    return (f"**{total}** 条英雄数据 = **{ok}** 个可选 + **{no}** 个地图上无此单位"
            f"（`note_log/recon/heroes.tsv` 共 {total} 行）")


def first(fields, key):
    rows = fields.get(key)
    if not rows:
        return None
    return rows[0].get("value")


def count_item_pages() -> int:
    """docs/items 下实际生成的物品页数（不含 index.md）。"""
    n = 0
    for _root, _dirs, files in os.walk(os.path.join(DOCS, "items")):
        for f in files:
            if f.endswith(".md") and f != "index.md":
                n += 1
    return n


def build_index() -> None:
    heroes = load_tsv(HERO_TSV)
    items = load_json(ITEMS_JSON)
    abils = load_json(ABIL_JSON)
    units = load_json(UNITS_JSON)
    n_ok, n_no, n_total = hero_scope(heroes)
    n_item_pages = count_item_pages()
    lines = [
        "# happy丶FISH Wiki",
        "",
        "本 Wiki 由 **本图对象数据与触发器取证自动生成**，用于改图/平衡时快速查阅英雄、技能、物品与数值。",
        "",
        "## 地图身份",
        "",
        "| 项目 | 值 |",
        "| --- | --- |",
        f"| 地图文件名 | `{MAP_NAME}` |",
        f"| 版本标签 | {MAP_VERSION} |",
        f"| SHA256 | `{MAP_SHA256}` |",
        "| 目标客户端 | 魔兽争霸 III 1.27a（1.27.0.52240） |",
        "| 归档成员数 | 3,192（`.blp` 2044 / `.mdx` 1016 / `.mp3` 107 / `.lua` 4 / 其它） |",
        "| 触发器形态 | 无 GUI 触发器（无 `war3map.wtg/.wct/.wts`），逻辑全部在 4.4 MB 的 `war3map.j` |",
        "",
        "> 身份以 SHA256 为准，不看文件名——同名的图可能是不同构建。",
        "",
        "## 数据规模",
        "",
        table(["类别", "对象数", "本 Wiki 覆盖"], [
            ["英雄", f"{n_total} 条数据", f"{n_ok} 个可选 + {n_no} 个地图上无此单位"],
            ["物品", f"{n_item_pages} 页（母图 {len(items)} 件对象）", "已生成独立页面"],
            ["技能", f"{len(abils):,}", "英雄技能逐条展开；未绑定技能见技能总览"],
            ["单位", f"{len(units):,}", "英雄单位已收录，其余单位暂未展开"],
        ]),
        "",
        f"> 英雄口径（与 [英雄图鉴](heroes/index.md)、[技能总览](skills/index.md) 一致）：{scope_text(heroes)}。",
        "",
        "## 快速导航",
        "",
        table(["入口", "内容"], [
            ["[英雄图鉴](heroes/index.md)", "英雄基础属性、技能绑定与技能真值数值"],
            ["[物品图鉴](items/index.md)", "物品属性、来源能力、游戏内说明原文"],
            ["[技能总览](skills/index.md)", "技能对象全量索引与英雄绑定情况"],
            ["[资料与说明](info/index.md)", "地图身份、数据来源、验证状态、迷宫楼层"],
            ["[更新日志](changelogs/index.md)", "版本改动记录"],
        ]),
        "",
        "## 验证状态（分层，互不替代）",
        "",
        table(["层级", "状态", "依据"], [
            ["① 源码改动", "不适用（本 Wiki 未改图）", "—"],
            ["② 静态检查", "PASS", "`pjass common.j Blizzard.j war3map.j` → exit 0（112,226 行）"],
            ["③ 封包与成员读回", "PASS", "3,192 个成员全部读回、逐个 SHA256 比对一致"],
            ["④ 实际载入", "**未验证**", "本轮没有启动魔兽/KK 客户端"],
            ["⑤ 功能测试", "**未验证**", "本轮没有进入游戏逐项测试"],
        ]),
        "",
        "!!! warning \"数值未实机验证\"",
        "",
        "    本 Wiki 的数值来自**发布图本身**的对象数据与触发器取证，**没有经过实机验证**；"
        "技能/物品的说明文字（`Ubertip`）是策划手写的，可能与实际效果不一致，**以触发器与对象数据字段为准**。",
        "    页面里出现的 `待考证`、`未判定（证据不足）`、`—` 都表示 Wiki **没有下结论**，"
        "不等于「值为 0」或「该功能不存在」；符号与用语含义见 [术语与用语](info/术语与用语.md)。",
        "",
        source_footer(),
    ]
    write_page(os.path.join(DOCS, "index.md"), "\n".join(lines))


def build_skills() -> None:
    abils = load_json(ABIL_JSON)
    heroes = load_tsv(HERO_TSV)
    stext = load_skill_text(SKILL_TEXT_CSV)
    adata = load_ability_data(ABILITY_DATA_CSV)
    bound = {}
    for h in heroes:
        hname = clean_inline(h.get("name")) or h["code"]
        for slot in ("Q", "W", "E", "R", "F", "D", "T"):
            raw = (h.get(slot) or "").strip()
            if not raw:
                continue
            m = re.match(r"^([0-9A-Za-z]{4})", raw)
            if m:
                bound[m.group(1)] = f"{hname} · {slot}"
    # 2199 个技能对象里有 73 个 code 是四个 NUL（被改名的原版对象，真实身份在 `base`）——
    # 直接用 a["code"] 会把 292 个 NUL 字符写进 markdown（审计问题 W018）→ 统一走 obj_code()。
    rows = []
    for a in sorted(abils, key=obj_code):
        c = obj_code(a)
        name = esc(clean_inline(a.get("name")))
        bname = esc(clean_inline(a.get("base_name")))
        owner = bound.get(c, "")
        st = stext.get(c)
        n_ad = len(adata.get(c, []))
        if st is None:
            note_flag = "未收录"
        else:
            note_flag = "有" if (st.get("cur_ubertip") or "").strip() else "无"
        # 名称空的分三种措辞（审计问题 W019）：只有名称空 → 指到同一行的「原型名称」；
        # 名称与原型名都空 → 整行没有可读信息，必须提示读者改按「技能 ID」检索。
        if name:
            name_cell = name
        elif bname:
            name_cell = "（未设置名称）"
        else:
            name_cell = "该技能对象未设置名称与原型名，请用 ID 检索"
        rows.append([code(c), name_cell, esc(owner) or "（没有英雄引用）",
                     code(str(a.get("base") or "").replace("\x00", "")) or "（无原型字段）",
                     bname or "（未设置名称）",
                     str(n_ad), note_flag])
    lines = [
        "# 技能总览",
        "",
        f"共 **{len(abils):,}** 个技能对象；其中 **{len(bound)}** 个通过 `PH_BindUnit` / "
        "`P2SV_FillAbilities` 绑定到英雄键位（Q/W/E/R/F/D/T），其余为物品技能、单位技能或系统技能。",
        "",
        f"> 英雄口径（与 [英雄图鉴](../heroes/index.md)、[首页](../index.md) 一致）：{scope_text(heroes)}；"
        "「绑定」列只对这些英雄的键位成立。",
        "",
        "> 技能对象在本图里通常只有 1 级（`alev=1`），等级成长由触发器控制。"
        "「可改数值项数」= 私有需求单 `patch_plan/data/hero_ability_data.csv` 里该 `ability_code` 的行数；"
        "「说明（原文）」= `patch_plan/data/hero_skill_text.csv` 里 `cur_ubertip` 的状态"
        "（`有` / `无` = 该技能有行但原文为空 / `未收录` = 该表没有这行）。",
        "",
        "> 表里的「（未设置名称）」= 对象数据里**这个字段真的是空值**，不是抓取失败；"
        "「（无原型字段）」= 连原型对象都没有，无法回退取 ID。"
        "名称为「该技能对象未设置名称与原型名，请用 ID 检索」的行请按第一列「技能 ID」检索。"
        "「（没有英雄引用）」= 本站英雄数据里**没有任何一个英雄**在这 7 个键位（Q/W/E/R/F/D/T）上"
        "引用这个技能 code（判定依据：本页「绑定」列由英雄表逐英雄逐键位解析而来，不是从 `war3map.w3a` 反推），"
        "这类技能多为魔兽原版遗留、本图没有使用的对象。"
        "符号 `—` 表示对象数据里该字段为空字符串（不是 0，也不是未知），"
        "全站口径见 [术语与用语](../info/术语与用语.md)。",
        "",
        table(["技能 ID", "名称", "绑定", "原型", "原型名称", "可改数值项数", "说明（原文）"], rows),
        "",
        source_footer([
            f"技能对象来自 `war3map.w3a`（SHA256 `{MEMBER_SHA['war3map.w3a']}`）。"
        ]),
    ]
    out = os.path.join(DOCS, "skills")
    os.makedirs(out, exist_ok=True)
    write_page(os.path.join(out, "index.md"), "\n".join(lines))
    write_page(os.path.join(out, ".pages"), "title: 技能总览\n")


def fmt_evidence(ev) -> str:
    """把 {line,snippet} / {file,line,snippet} 之类的取证对象渲染成一行。"""
    if not isinstance(ev, dict):
        return esc(str(ev))
    bits = []
    f = ev.get("file")
    ln = ev.get("line") or ev.get("line_ref")
    if f:
        bits.append(f"`{f}`")
    if ln:
        bits.append(f"`L{ln}`")
    if bits:
        s = ev.get("snippet") or ev.get("role") or ""
        return " ".join(bits) + (f" {esc(str(s)[:160])}" if s else "")
    return esc(str(ev)[:200])


def md_from_json(obj, depth: int = 2, max_list: int = 40) -> list[str]:
    """把任意 JSON 结构渲染成朴素 markdown（用于子智能体产出的取证数据）。"""
    lines: list[str] = []
    pad = "#" * depth
    if isinstance(obj, dict):
        for k, val in obj.items():
            if isinstance(val, (dict, list)):
                n = len(val)
                lines += [f"{pad} {k}（{n}）", ""]
                lines += md_from_json(val, min(depth + 1, 6), max_list)
            else:
                lines.append(f"- **{k}**：{esc(str(val))}")
        if lines and lines[-1].startswith("- "):
            lines.append("")
    elif isinstance(obj, list):
        if all(isinstance(x, (str, int, float)) for x in obj):
            lines += ["、".join(f"`{esc(str(x))}`" for x in obj[:max_list]) or "—", ""]
        else:
            for i, x in enumerate(obj[:max_list]):
                if isinstance(x, dict):
                    head = (x.get("name") or x.get("code") or x.get("item_code")
                            or x.get("function") or x.get("id") or f"#{i + 1}")
                    lines.append(f"- **{esc(str(head))}**")
                    for k, val in x.items():
                        if k in ("name", "code", "item_code", "function", "id"):
                            continue
                        if isinstance(val, (dict, list)):
                            lines.append(f"    - {k}：{esc(json.dumps(val, ensure_ascii=False)[:400])}")
                        else:
                            lines.append(f"    - {k}：{esc(str(val))}")
                else:
                    lines.append(f"- {esc(str(x))}")
            if len(obj) > max_list:
                lines.append(f"- _（另有 {len(obj) - max_list} 条未显示）_")
            lines.append("")
    else:
        lines.append(esc(str(obj)))
    return lines


def build_info() -> None:
    items = load_json(ITEMS_JSON)
    out = os.path.join(DOCS, "info")
    os.makedirs(out, exist_ok=True)

    # 迷宫/传送物品 → 楼层线索（说明文本自动提取）
    floor_re = re.compile(r"(?:传送)?迷宫\s*([0-9０-９一二三四五六七八九十百]+)\s*层")
    floors = []
    for it in items:
        nm = clean_inline(first(it["fields"], "Name"))
        ub = clean_text(first(it["fields"], "Ubertip"))
        m = floor_re.search(nm)
        if m:
            floors.append((m.group(1), obj_code(it), nm, ub))
    floors.sort(key=lambda x: (len(x[0]), x[0]))
    frows = []
    for num, c, nm, ub in floors:
        first_line = next((ln.strip() for ln in ub.split("\n") if ln.strip()), "")
        frows.append([code(c), esc(nm), esc(first_line[:120])])

    write_page(os.path.join(out, "index.md"), "\n".join([
        "# 资料与说明",
        "",
        table(["页面", "内容"], [
            ["[地图身份与技术说明](地图身份.md)", "母图指纹、成员构成、数据来源与验证分层"],
            ["[术语与用语](术语与用语.md)", "筋力/体力/敏捷、本站符号含义、字段名对应（审计问题 W016）"],
            ["[对象字段对照表](对象字段对照表.md)", "`war3map.w3t` 物品字段与 `war3map.w3a` 技能数值字段的中文名对照"],
            ["[迷宫楼层线索](楼层信息.md)", "从「传送迷宫N层」物品的说明文本自动提取"],
            ["[存档与读档](存档与读档.md)", "存档相关 Lua 模块与已知事实（待补充）"],
        ]),
        "",
        source_footer(),
    ]))

    write_page(os.path.join(out, "地图身份.md"), "\n".join([
        "# 地图身份与技术说明",
        "",
        table(["项目", "值"], [
            ["文件名", f"`{MAP_NAME}`"],
            ["版本标签", MAP_VERSION],
            ["SHA256", f"`{MAP_SHA256}`"],
            ["war3map.j", f"`{MEMBER_SHA['war3map.j']}`"],
            ["war3map.w3u", f"`{MEMBER_SHA['war3map.w3u']}`"],
            ["war3map.w3a", f"`{MEMBER_SHA['war3map.w3a']}`"],
            ["war3map.w3t", f"`{MEMBER_SHA['war3map.w3t']}`"],
            ["war3map.w3i", f"`{MEMBER_SHA['war3map.w3i']}`"],
            ["hf16_save_core.lua", f"`{MEMBER_SHA['hf16_save_core.lua']}`"],
            ["hf22_stability.lua", f"`{MEMBER_SHA['hf22_stability.lua']}`"],
        ]),
        "",
        "## 数据来源",
        "",
        "| Wiki 内容 | 来源 |",
        "| --- | --- |",
        "| 英雄基础属性、技能绑定 | `war3map.w3u` 对象字段 + `war3map.j` 的 `PH_BindUnit` / `P2SV_FillAbilities` |",
        "| 技能数值 | `war3map.w3a` 对象字段（`Data` 字段为真值） |",
        "| 物品属性 | `war3map.w3t` + 物品技能（`war3map.w3a`） |",
        "| 物品/技能说明原文 | 对象字段 `Tip` / `Ubertip`（**可能与实际效果不符**） |",
        "| 字段中文化 | 客户端 `War3Patch.mpq` 的 `Units\\UnitMetaData.slk` / `AbilityMetaData.slk` + `UI\\WorldEditStrings.txt` |",
        "",
        "## 已知限制",
        "",
        "- 技能解锁等级、专属装备绑定、掉落配方写在触发器里，Wiki 目前只做了有限取证，未覆盖处标注「待考证」。",
        "- 物品分类与品质由游戏内说明文本**自动推断**，可能有误。",
        "- 所有内容都**没有经过实机验证**。",
        "",
        source_footer(),
    ]))

    floor_lines = [
        "# 迷宫楼层线索",
        "",
        f"下表由物品名里的「传送迷宫 N 层」与说明文本**自动提取**，共 {len(floors)} 条。"
        "说明文本是作者手写的，可能不完整。",
        "",
        table(["物品 ID", "物品名", "说明首行"], frows) if frows else "_（未提取到楼层物品）_",
        "",
    ]
    fb_path = os.path.join(RECON_DIR, "floors_bosses.json")
    if os.path.exists(fb_path):
        try:
            fb = load_json(fb_path)
            floor_lines += ["## 触发器取证：楼层、传送与 BOSS", "",
                            "以下数据由只读静态分析从 `war3map.j` 提取，**每条都带行号**；"
                            "行号见各项的 `evidence` 字段。"
                            "完整报告（含方法、覆盖率、不确定项逐条说明）："
                            "`note_log/recon/floors_bosses_报告.md`；机器可读数据："
                            "`note_log/recon/floors_bosses.json`（schema `floors_bosses/v1`）。", ""]
            floor_lines += md_from_json(fb, depth=3, max_list=200)
        except Exception as e:  # noqa: BLE001
            floor_lines.append(f"!!! warning \"取证数据解析失败\"\n    {esc(str(e))}\n")
    else:
        floor_lines += ["> 楼层/传送/BOSS 的触发器取证数据仍在生成中。", ""]
    floor_lines.append(source_footer())
    write_page(os.path.join(out, "楼层信息.md"), "\n".join(floor_lines))

    save_lines = [
        "# 存档与读档",
        "",
        "本图包含 3 个存档相关 Lua 模块（`hf16_save_core.lua`、`hf16_save_runtime.lua`、"
        "`hf16_save_step.lua`）与 1 个稳定性模块（`hf22_stability.lua`），"
        "由 `war3map.j` 的 `main` 通过 `Cheat(\"exec-lua: hf22_stability\")` 载入。",
        "",
        table(["成员", "字节数", "SHA256"], [
            ["`hf16_save_core.lua`", "20,579", f"`{MEMBER_SHA['hf16_save_core.lua']}`"],
            ["`hf16_save_runtime.lua`", "5,542", f"`{MEMBER_SHA['hf16_save_runtime.lua']}`"],
            ["`hf16_save_step.lua`", "247", f"`{MEMBER_SHA['hf16_save_step.lua']}`"],
            ["`hf22_stability.lua`", "775", f"`{MEMBER_SHA['hf22_stability.lua']}`"],
        ]),
        "",
    ]
    ss_path = os.path.join(RECON_DIR, "save_schema.json")
    if os.path.exists(ss_path):
        try:
            ss = load_json(ss_path)
            save_lines += ["## 取证的存档结构", "",
                           "以下内容由只读静态分析得出，**每条断言都带 `war3map.j` 行号或 Lua 文件行号**。", ""]
            if ss.get("entry_points"):
                save_lines += ["### 入口函数", "",
                               table(["类型", "函数", "位置", "证据"],
                                     [[esc(str(e.get("kind", "—"))), code(e.get("function") or "—"),
                                       f"`L{e.get('line')}`" if e.get("line") else "—",
                                       fmt_evidence(e.get("evidence"))]
                                      for e in ss["entry_points"]]), ""]
            if (ss.get("format") or {}).get("sections"):
                save_lines += ["### 数据结构", "",
                               table(["字段", "序号", "编码", "说明", "证据"],
                                     [[esc(str(s.get("name", "—"))), esc(str(s.get("index", "—"))),
                                       esc(str(s.get("encoding", "—"))), esc(str(s.get("description", ""))[:200]),
                                       fmt_evidence(s.get("evidence"))]
                                      for s in ss["format"]["sections"]]), ""]
            if (ss.get("load") or {}).get("steps"):
                save_lines += ["### 读档步骤", ""]
                for i, st in enumerate(ss["load"]["steps"], 1):
                    save_lines.append(f"{i}. {esc(str(st))}")
                save_lines.append("")
            save_lines += ["### 其余取证字段", ""]
            rest = {k: v for k, v in ss.items()
                    if k not in ("entry_points", "format", "load", "schema", "map_sha256")}
            save_lines += md_from_json(rest, depth=4, max_list=40)
        except Exception as e:  # noqa: BLE001
            save_lines.append(f"!!! warning \"存档取证数据解析失败\"\n    {esc(str(e))}\n")
    else:
        save_lines += ['!!! warning "待补充"',
                       "    存档格式、对象编码、分卷与读取入口的取证**仍在进行中**，本页目前只有模块指纹。",
                       "    改图涉及存档字段前，必须先读懂现有格式，不要拿真实玩家存档做破坏性测试。",
                       ""]
    save_lines.append(source_footer())
    write_page(os.path.join(out, "存档与读档.md"), "\n".join(save_lines))

    # 术语与用语（审计问题 W016）：把全站反复出现的自造词/符号固定解释一遍
    write_page(os.path.join(out, "术语与用语.md"), "\n".join([
        "# 术语与用语",
        "",
        "本 Wiki 的词汇多半直接来自地图对象数据（`war3map.w3u` / `war3map.w3a` / `war3map.w3t`），"
        "与玩家口头叫法、其他版本的习惯叫法可能不同。下表是本站统一口径。",
        "",
        "## 属性三围",
        "",
        table(["本图用语", "本图字段", "常见叫法", "说明"], [
            ["筋力", "`ustr` / `ustp` / `Istr`", "力量 / Strength", "地图说明原文（Tip/Ubertip）写「筋力」；**客户端/编辑器**里这个字段的标准中文名是「力量」"],
            ["敏捷", "`uagi` / `uagp` / `Iagi`", "敏捷 / Agility", "与常见叫法一致"],
            ["体力", "`uint` / `uinp` / `Iint`", "智力 / Intelligence", "地图说明原文写「体力」；**客户端/编辑器**里的标准中文名是「智力」，**不是生命值上限**（生命值上限是 `uhpm`）"],
        ]),
        "",
        "## 本站符号",
        "",
        table(["符号", "含义"], [
            ["`—`", "对象数据里该字段为空（不是 0，也不是未知）"],
            ["「（对象数据中此字段为空字符串）」", "字段存在但值为空串，常见于原版改名的对象"],
            ["`—（对象数据中此字段为空）`", "英雄页对空值的写法，与上一条同义（只是句式更短，避免整表被长句撑开）"],
            ["「（未设置名称）」", "对象数据里**名称字段真的是空值**（不是抓取失败）；技能总览、物品页都会这样标"],
            ["「（无原型字段）」", "该对象连「原型」都没有，无法回退取名字或 ID，只能用 ID 检索"],
            ["「（没有英雄引用）」", "技能总览「绑定」列为空时的写法：本站英雄数据里没有任何一个英雄在 "
                                "Q/W/E/R/F/D/T 键位上引用这个技能 code（多为魔兽原版遗留、本图未使用的技能对象）"],
            ["✔", "该数值在游戏内说明文本里出现过（说明与数值能对上）"],
            ["`未判定（证据不足）`", "对象数据既没有主动施法信号（耗魔/冷却/施法距离/范围），也没有 `Order`，无法判断主动还是被动"],
            ["`⚠️ 不可选`", "该英雄存在于对象数据，但不在 `PH_PortInit` 注册表里，游戏里选不到"],
            ["`待考证`", "需要读 `war3map.j` 触发器才能确定（Wiki 目前只写了线索，没有下结论）"],
        ]),
        "",
        "## 与地图对象字段的对应",
        "",
        "各页「可改数值项」块里的字段名就是地图对象里的字段 id（例如 `Ocr1`、`isr2`、`Iagi`）。"
        "它们与 `patch_plan/data/` 下 CSV 的 `field` 列一一对应；改数值请改 CSV 的 `new_value` 列，"
        "不要直接改 Markdown。字段的中文名取自客户端的 `UnitMetaData.slk` / `AbilityMetaData.slk`。",
        "",
        source_footer(),
    ]))

    # info 目录导航（审计问题 W028：原来没有 .pages，导航顺序靠文件名）
    write_page(os.path.join(out, ".pages"), "\n".join([
        "title: 资料与说明",
        "nav:",
        "  - index.md",
        "  - 地图身份.md",
        "  - 术语与用语.md",
        "  - 对象字段对照表.md",
        "  - 楼层信息.md",
        "  - 存档与读档.md",
        "",
    ]))


# ── 对象字段对照表（审计问题 W005）───────────────────────────────────────
# 字段字典（客户端本地化）就在 `wiki_common.INDEX_DIR` = `<W>\note_log\index`；
# 该目录缺文件时退回 `patch_plan\index\` 的同名文件（两处都实测存在，按先存在的用）。
FIELD_DICT_FILES = ("field_dict_units.tsv", "field_dict_abilities.tsv")
# 物品页折叠块「全部对象字段（原始值）」里实测出现过的字段 id（39 个，按 id 排序）。
ITEM_FIELD_IDS = (
    "iabi", "iarm", "icid", "icla", "iclb", "iclg", "iclr", "ides", "idro", "idrp",
    "ifil", "igol", "ihtp", "iicd", "iico", "ilev", "ilum", "ilvo", "imor", "ipaw",
    "iper", "ipow", "ipri", "iprn", "isca", "isel", "issc", "isst", "isto", "istr",
    "iusa", "iuse", "ubpx", "ubpy", "uhot", "unam", "ureq", "utip", "utub",
)
# 物品页折叠块的行形状（build_items.py:924）：`    - \`ides\` **描述**（Profile） = \`…\``
ITEM_FIELD_LINE_RE = re.compile(r"^[ \t]*- `([0-9A-Za-z_]{1,12})` \*\*", re.M)
# 「基础属性」表表头（build_items.py:853：属性 / 数值 / 来源能力 / 字段 / 等级）
BASE_ATTR_HEADER = "| 属性 | 数值 | 来源能力 | 字段 | 等级 |"
BASE_ATTR_FIELD_RE = re.compile(r"^\|\s*[^|]*\|\s*[^|]*\|\s*[^|]*\|\s*`([^`|]+)`\s*\|")
FIELD_ZH_MISSING = "（客户端未收录，见下方说明）"


def field_dict_path(name: str) -> str:
    p = os.path.join(INDEX_DIR, name)
    if os.path.exists(p):
        return p
    return os.path.join(W, "patch_plan", "index", name)


def load_field_dict() -> dict[str, dict]:
    """`field_id` → 客户端字段字典行（units 优先、abilities 补充，先见者胜）。

    `wiki_common` 只有 `field_zh_map()`（只留中文名），本页还要 `ini_key` / `type` /
    取值范围，所以按同一顺序、同一份 tsv 再读一遍；不改动 `wiki_common` 的行为。
    """
    out: dict[str, dict] = {}
    for name in FIELD_DICT_FILES:
        for r in load_tsv(field_dict_path(name)):
            fid = (r.get("field_id") or "").strip()
            if fid and fid not in out:
                out[fid] = r
    return out


def scan_item_pages() -> tuple[int, dict[str, int], dict[str, int]]:
    """现算 `docs/items/**/*.md` 里的字段覆盖度（不改 docs，只读）。

    返回 `(物品页数, 字段 id → 出现页数（页内去重）, 技能数值字段 id → 出现次数)`。
    """
    n_pages = 0
    pages: dict[str, int] = {}
    base: dict[str, int] = {}
    for root, _dirs, files in os.walk(os.path.join(DOCS, "items")):
        for fn in files:
            if not fn.endswith(".md") or fn == "index.md":
                continue
            n_pages += 1
            with open(os.path.join(root, fn), "r", encoding="utf-8") as fh:
                text = fh.read()
            for fid in {m.group(1) for m in ITEM_FIELD_LINE_RE.finditer(text)}:
                pages[fid] = pages.get(fid, 0) + 1
            state = False  # True = 正在读「基础属性」表格
            pending = False
            for ln in text.split("\n"):
                if ln.strip() == "### 基础属性":
                    pending, state = True, False
                    continue
                if pending:
                    if not ln.strip():
                        continue
                    pending = False
                    state = ln.startswith(BASE_ATTR_HEADER)
                    continue
                if state:
                    if not ln.startswith("|"):
                        state = False
                        continue
                    m = BASE_ATTR_FIELD_RE.match(ln)
                    if m:
                        fid = m.group(1).strip()
                        base[fid] = base.get(fid, 0) + 1
    return n_pages, pages, base


def build_field_reference() -> None:
    """生成 `docs/info/对象字段对照表.md`（审计问题 W005）。

    两张表都从现有产物现算：表 1 = 物品页折叠块里的字段 id（固定 39 个）+ 页数覆盖度；
    表 2 = 物品页「基础属性」表第 4 列的字段 id 去重。中文名/类型/取值范围查客户端字段字典。
    """
    out = os.path.join(DOCS, "info")
    os.makedirs(out, exist_ok=True)
    fdict = load_field_dict()
    zhmap = field_zh_map()
    n_pages, page_hits, base_hits = scan_item_pages()

    def zh_of(fid: str) -> str:
        # 按 units → abilities 的顺序取（与 field_zh_map() 同序），再用合并表兜底
        return ((fdict.get(fid) or {}).get("zh_label") or zhmap.get(fid) or "").strip()

    rows_items = []
    n_miss_items = 0
    for fid in ITEM_FIELD_IDS:
        d = fdict.get(fid) or {}
        zh = zh_of(fid)
        if not zh:
            n_miss_items += 1
        rows_items.append([code(fid), esc(zh) if zh else FIELD_ZH_MISSING,
                           code((d.get("ini_key") or "").strip()), str(page_hits.get(fid, 0))])

    rows_abils = []
    n_miss_abils = 0
    for fid in sorted(base_hits):
        d = fdict.get(fid) or {}
        zh = zh_of(fid)
        if not zh:
            n_miss_abils += 1
        # 类型/取值范围逐行现算；原来每行都重复的「`war3map.w3a` 的 `Data` 数值字段（类型 …），取值 …」
        # 样板句只在表 2 上方的段落里说一次（噪音太大）。
        ty = (d.get("type") or "").strip()
        lo, hi = (d.get("minVal") or "").strip(), (d.get("maxVal") or "").strip()
        if lo and hi:
            rng = "%s–%s" % (lo, hi)
        elif hi:
            rng = "≤ %s" % hi
        elif lo:
            rng = "≥ %s" % lo
        else:
            rng = "—"
        rows_abils.append([code(fid), esc(zh) if zh else FIELD_ZH_MISSING,
                           code(ty) if ty else "—", rng])

    lines = [
        "# 对象字段对照表",
        "",
        "本页把本站正文里出现的**字段**（如 `ides`、`utub`、`iabi`、`Ilif`）集中成一张可检索的对照表："
        "它们是地图对象数据里的**原始字段名（WC3 内部 id）**。改了图以后要按这些 id 去找数据"
        "（写回 `war3map.w3t` / `war3map.w3a` / `war3map.w3u`）；游戏内与编辑器里显示的中文名只是"
        "**客户端本地化**标签，不能用来检索对象数据。下表的中文名取自这份本地化字典"
        f"（`note_log/index/{FIELD_DICT_FILES[0]}` / `{FIELD_DICT_FILES[1]}`，源头是客户端 "
        "`War3Patch.mpq` 的 `UnitMetaData.slk` / `AbilityMetaData.slk` 与 `WorldEditStrings.txt`）；"
        f"字典里没有的字段写「{FIELD_ZH_MISSING}」，本站不臆造译名。",
        "",
        "## 表 1：物品字段（`war3map.w3t`）",
        "",
        f"下表是物品页折叠块「全部对象字段（原始值）」里出现过的全部 **{len(ITEM_FIELD_IDS)}** 个字段 id（按 id 排序）。"
        f"「出现物品页数」现算自 `docs/items/**/*.md`（不含 `index.md`，共 {n_pages} 页）——"
        "某个字段只在少数物品里被写过，数字就小，可以拿它判断这个字段值不值得改。"
        "字段在某个对象里没有值时，物品页写的是「（对象数据中此字段为空字符串）」，那是**空值**，不是抓取失败。",
        "",
        table(["字段 id", "中文名", "所属分组(ini_key)", "出现物品页数"], rows_items),
        "",
        "## 表 2：技能数值字段（`war3map.w3a`）",
        "",
        "物品页「当前数据 → 基础属性」表格第 4 列写的就是下表的字段 id——它们全部是物品绑定技能对象里 "
        "`ini_key = Data` 的数值字段，也就是**改技能数值时真正要写的字段名**。"
        f"本表从上面那 {n_pages} 个物品页现算去重，共 **{len(rows_abils)}** 个，按字段 id 排序；"
        "它只覆盖**物品技能**用到过的字段，英雄技能页里出现、但没绑到任何物品的字段不在本表内。"
        "「类型」列是客户端字典给的字段类型（`unreal` = 浮点数、`int` = 整数、`bool` = 0/1 开关，"
        "其余为枚举或字符串）；「取值范围」列是字典里的 `minVal` / `maxVal`，字典没写的写 `—`。",
        "",
        table(["字段 id", "中文名", "类型", "取值范围"], rows_abils),
        "",
        "## 正文里的「字段」指什么",
        "",
        "本站正文里出现**字段**一词时，一律指地图对象数据的**原始字段名（WC3 内部 id）**，例如 `ides`、`Ilif`；"
        "它既不等于游戏内显示的属性名，也不等于需求单 CSV 的列名。"
        "**玩家要改数值请看各页的「可改数值项」小节**——那里列的才是可以直接改的项，"
        "改动落在私有需求单仓库 `patch_plan/data/*.csv` 的 `new_value` 列，不要直接改 Markdown；"
        "站点符号与用语口径见 [术语与用语](/info/术语与用语/)，数据来源与验证分层见 [地图身份](/info/地图身份/)。",
        "",
        source_footer([
            f"物品字段来自 `war3map.w3t`（SHA256 `{MEMBER_SHA['war3map.w3t']}`）；"
            f"技能数值字段来自 `war3map.w3a`（SHA256 `{MEMBER_SHA['war3map.w3a']}`）；"
            "字段中文名、类型与取值范围来自客户端 `War3Patch.mpq` 的 `UnitMetaData.slk` / "
            "`AbilityMetaData.slk` 与 `WorldEditStrings.txt`。",
            f"字典覆盖率：表 1 {len(ITEM_FIELD_IDS) - n_miss_items}/{len(ITEM_FIELD_IDS)}、"
            f"表 2 {len(rows_abils) - n_miss_abils}/{len(rows_abils)}，其余为客户端未收录。",
        ]),
    ]
    write_page(os.path.join(out, "对象字段对照表.md"), "\n".join(lines))


def build_changelogs() -> None:
    out = os.path.join(DOCS, "changelogs")
    posts = os.path.join(out, "posts")
    os.makedirs(posts, exist_ok=True)
    # 口径与 docs/index.md、docs/heroes/index.md、docs/skills/index.md 保持一致（审计问题 W010）：
    # 三处数字都从同一份数据现算，不在正文里写死，避免下次数据变了又对不上。
    c_ok, c_no, c_total = hero_scope(load_tsv(HERO_TSV))
    n_items = len(load_json(ITEMS_JSON))
    n_abils = len(load_json(ABIL_JSON))
    write_page(os.path.join(out, ".pages"), "title: 更新日志\n")
    # blog 插件的作者表必须放在 blog_dir 根（docs/changelogs/.authors.yml）
    # mkdocs-material 9.7 的 schema 是 `authors:` → {id: {name, description}}
    write_page(os.path.join(out, ".authors.yml"), "\n".join([
        "authors:",
        "  wiki:",
        "    name: happy丶FISH Wiki",
        "    description: Wiki 自动生成与维护",
        "    avatar: https://github.com/slasher233.png",
        "",
    ]))
    stale = os.path.join(posts, ".authors.yml")
    if os.path.exists(stale):
        os.remove(stale)
    write_page(os.path.join(out, "index.md"), "\n".join([
        "# 更新日志",
        "",
        "记录本 Wiki 与地图版本的对应关系。地图改动记录写到 `posts/` 下。",
        "",
        source_footer(),
    ]))
    write_page(os.path.join(posts, "2026-10-08-v1.0-baseline.md"), "\n".join([
        "---",
        "map_version: \"v1.0 正式版\"",
        "date:",
        "  created: 2026-10-08",
        "authors: [wiki]",
        "categories: [版本更新]",
        "---",
        "",
        "# v1.0 正式版（基线）",
        "",
        "本 Wiki 的初始基线。地图文件身份：",
        "",
        f"- 文件名：`{MAP_NAME}`",
        f"- SHA256：`{MAP_SHA256}`",
        "",
        "<!-- more -->",
        "",
        "## 本次记录",
        "",
        "| 项目 | 内容 |",
        "| --- | --- |",
        f"| 英雄条目 | {c_total} 条数据（{c_ok} 个可选 + {c_no} 个地图上无此单位） |",
        f"| 物品条目 | {n_items} 件对象 |",
        f"| 技能对象 | {n_abils:,} |",
        "",
        "## 已知问题",
        "",
        "- 技能解锁等级、专属装备绑定未取证，标注「待考证」。",
        "- Wiki 内容未经过实机验证。",
        "",
        source_footer(),
    ]))


def main() -> None:
    build_index()
    build_skills()
    build_info()
    build_field_reference()
    build_changelogs()
    print("站点骨架页已生成：index / skills / info（含对象字段对照表） / changelogs")


if __name__ == "__main__":
    main()
