"""生成站点骨架页面：首页、技能总览、info 页、更新日志首页。

数据来源：note_log/wiki_data/*.json、note_log/recon/*.tsv、note_log/index/*.tsv
只读脚本：不修改地图。
"""
from __future__ import annotations

import collections
import csv
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wiki_common import (  # noqa: E402
    DOCS, INDEX_DIR, MAP_NAME, MAP_SHA256, MAP_VERSION, MEMBER_SHA, RECON_DIR,
    WIKI_DATA, blank, clean_inline, clean_text, code, esc, load_json, obj_code,
    source_footer, table, write_page,
)

HERO_TSV = os.path.join(RECON_DIR, "heroes.tsv")
UNBOUND_TSV = os.path.join(RECON_DIR, "abilities_not_on_heroes.tsv")
ITEMS_JSON = os.path.join(WIKI_DATA, "items.json")
ABIL_JSON = os.path.join(WIKI_DATA, "abilities.json")
UNITS_JSON = os.path.join(WIKI_DATA, "units.json")


def load_tsv(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def first(fields, key):
    rows = fields.get(key)
    if not rows:
        return None
    return rows[0].get("value")


def build_index() -> None:
    heroes = load_tsv(HERO_TSV)
    items = load_json(ITEMS_JSON)
    abils = load_json(ABIL_JSON)
    units = load_json(UNITS_JSON)
    reachable = [h for h in heroes if (h.get("reachable") or "").lower() != "no"]
    lines = [
        "# happy丶FISH SAO Wiki",
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
            ["英雄", str(len(heroes)), f"{len(reachable)} 个确认可选中"],
            ["物品", str(len(items)), "全部生成独立页面"],
            ["技能", f"{len(abils):,}", "英雄技能逐条展开；未绑定技能见技能总览"],
            ["单位", f"{len(units):,}", "英雄单位已收录，其余单位暂未展开"],
        ]),
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
        "> 说明：本 Wiki 的数值来自**发布图本身**的对象数据与触发器取证，**未经过实机验证**；"
        "技能说明文字（`Ubertip`）可能与实际效果不一致，以触发器与数据字段为准。",
        "",
        source_footer(),
    ]
    write_page(os.path.join(DOCS, "index.md"), "\n".join(lines))


def build_skills() -> None:
    abils = load_json(ABIL_JSON)
    heroes = load_tsv(HERO_TSV)
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
    rows = []
    for a in sorted(abils, key=lambda x: x["code"]):
        c = a["code"]
        name = clean_inline(a.get("name"))
        owner = bound.get(c, "")
        rows.append([code(c), esc(name) or "—", esc(owner) or "_未绑定英雄_",
                     code(a.get("base", "")), esc(clean_inline(a.get("base_name"))) or "—"])
    lines = [
        "# 技能总览",
        "",
        f"共 **{len(abils):,}** 个技能对象；其中 **{len(bound)}** 个通过 `PH_BindUnit` / "
        "`P2SV_FillAbilities` 绑定到英雄键位（Q/W/E/R/F/D/T），其余为物品技能、单位技能或系统技能。",
        "",
        "> 技能对象在本图里通常只有 1 级（`alev=1`），等级成长由触发器控制。",
        "",
        table(["技能 ID", "名称", "绑定", "原型", "原型名称"], rows),
        "",
        source_footer([
            f"技能对象来自 `war3map.w3a`（SHA256 `{MEMBER_SHA['war3map.w3a']}`）。"
        ]),
    ]
    out = os.path.join(DOCS, "skills")
    os.makedirs(out, exist_ok=True)
    write_page(os.path.join(out, "index.md"), "\n".join(lines))
    write_page(os.path.join(out, ".pages"), "title: 技能总览\n")


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

    write_page(os.path.join(out, "楼层信息.md"), "\n".join([
        "# 迷宫楼层线索",
        "",
        f"下表由物品名里的「传送迷宫 N 层」与说明文本**自动提取**，共 {len(floors)} 条。"
        "说明文本是作者手写的，可能不完整。",
        "",
        table(["物品 ID", "物品名", "说明首行"], frows) if frows else "_（未提取到楼层物品）_",
        "",
        source_footer(),
    ]))

    write_page(os.path.join(out, "存档与读档.md"), "\n".join([
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
        "!!! warning \"待补充\"",
        "    存档格式、对象编码、分卷与读取入口**尚未解析**，本页目前只有模块指纹。",
        "    改图涉及存档字段前，必须先读懂现有格式，不要拿真实玩家存档做破坏性测试。",
        "",
        source_footer(),
    ]))


def build_changelogs() -> None:
    out = os.path.join(DOCS, "changelogs")
    posts = os.path.join(out, "posts")
    os.makedirs(posts, exist_ok=True)
    write_page(os.path.join(out, ".pages"), "title: 更新日志\n")
    # blog 插件的作者表必须放在 blog_dir 根（docs/changelogs/.authors.yml）
    # mkdocs-material 9.7 的 schema 是 `authors:` → {id: {name, description}}
    write_page(os.path.join(out, ".authors.yml"), "\n".join([
        "authors:",
        "  wiki:",
        "    name: happy丶FISH SAO Wiki",
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
        "| 英雄条目 | 60（58 个确认可选中） |",
        "| 物品条目 | 551 |",
        "| 技能对象 | 2,199 |",
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
    build_changelogs()
    print("站点骨架页已生成：index / skills / info / changelogs")


if __name__ == "__main__":
    main()
