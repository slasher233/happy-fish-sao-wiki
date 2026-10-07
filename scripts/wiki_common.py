# -*- coding: utf-8 -*-
"""wiki 生成器共用工具。

所有生成器都只读 `note_log\\` 下的解析产物，把 markdown 写进 `wiki\\docs\\`。
不接触地图文件本身。
"""
from __future__ import annotations

import json
import os
import re
import sys

# ── 路径 ────────────────────────────────────────────────────────────────
# 本文件在 <W>\\wiki\\scripts\\ 下，W 是干活目录（含 note_log 与 wiki）
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_DIR = os.path.dirname(SCRIPTS_DIR)
W = os.path.dirname(WIKI_DIR)

NOTE_LOG = os.path.join(W, "note_log")
WIKI_DATA = os.path.join(NOTE_LOG, "wiki_data")
INDEX_DIR = os.path.join(NOTE_LOG, "index")
RECON_DIR = os.path.join(NOTE_LOG, "recon")
EXTRACT_DIR = os.path.join(NOTE_LOG, "extract")
DOCS = os.path.join(WIKI_DIR, "docs")

MAP_NAME = "刀剑物语 happy丶FISH v1.0 正式版"
MAP_SHA256 = "62A1122ACEDA220B746DF730B1625C2AF8E3C149048E26FDC2AF5C37BDA6BD6D"
MAP_VERSION = "v1.0 正式版"

MEMBER_SHA = {
    "war3map.j": "13bafcf0c1e91848fbf8ee72cbc48017e711cae7b6198e69cb01136c7064a4a2",
    "war3map.w3i": "e5ff90f74a533be08ded10e529348317335f3ad4a0c4385882e2df81cea2b455",
    "war3map.w3u": "e8612c55afc5219e30c45c19dcff26b63cd8966a94d740853c5ef39085804294",
    "war3map.w3a": "80675c0549e25604b5b97bb05cd7f6594f92dfec95639cbdf6a6480ba2ffa9d3",
    "war3map.w3t": "98164862404eee98a28c5b5ba01f88fceb7fca896b3b06457f1853d75bac896d",
    "war3map.w3e": "9134500588e81df8fcc2e9756b18355e3ffaff40e9ae838e9f8c228a262e89ac",
    "war3map.doo": "c4242d9fd37fdfbb4789674599ca50d412036955bff32ac18c445ea78dfb81e5",
    "hf16_save_core.lua": "39b04631e80502a126ac9d70a892dbf018d45265674cf2503efe9faa7048ff21",
    "hf16_save_runtime.lua": "4739914ca91c9eec3e36acf4e3f35089dfaa56207df9eddbbd8db655029f33d3",
    "hf16_save_step.lua": "ec5c1eae4ceb542ee0642788cc224cc7770665ed74e8eb8f7842751fffa189e8",
    "hf22_stability.lua": "0f79764b742951f06b8bec4feb6ab64d6be6eb7fe380e491b1047e9fa3ea0c95",
}


def utf8() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


# ── 载入 ────────────────────────────────────────────────────────────────
def load_json(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_tsv(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8-sig") as f:
        lines = [ln.rstrip("\n") for ln in f if ln.strip()]
    if not lines:
        return []
    head = lines[0].split("\t")
    out = []
    for ln in lines[1:]:
        cells = ln.split("\t")
        cells += [""] * (len(head) - len(cells))
        out.append(dict(zip(head, cells)))
    return out


# ── 文本清理 ─────────────────────────────────────────────────────────────
_COLOR = re.compile(r"\|c[0-9a-fA-F]{8}|\|r|\|c")
_NEWLINE = re.compile(r"\|n", re.IGNORECASE)


def clean_text(s) -> str:
    """去掉 WC3 颜色代码、把 |n 换成真换行。"""
    if s is None:
        return ""
    t = str(s)
    t = _NEWLINE.sub("\n", t)
    t = _COLOR.sub("", t)
    return t.replace("\r\n", "\n").strip()


def clean_inline(s) -> str:
    """把说明压成单行（用于表格单元格）。"""
    return re.sub(r"\s*\n+\s*", " / ", clean_text(s)).strip()


def strip_color_keep_nl(s) -> str:
    return _COLOR.sub("", str(s or "")).replace("\r\n", "\n")


_MD_ESCAPE = re.compile(r"([\\`*_{}\[\]()#+\-.!|>])")


def esc(s) -> str:
    """表格单元格里的 markdown 转义（并把换行压成空格）。"""
    t = clean_inline(s)
    return t.replace("|", "\\|")


def code(s) -> str:
    return f"`{s}`" if s not in (None, "") else "—"


def blank(v, dash: str = "—") -> str:
    if v is None or v == "":
        return dash
    return str(v)


def obj_code(o: dict) -> str:
    """对象数据的唯一 4 字符 ID。

    `extract_wiki_data.py` 产出的 `code` 取自 new_id；**被修改的原版对象**在 w3u/w3a/w3t 里
    new_id 是四个 NUL，此时真正的 ID 是原型 `base`（例如原版物品 `gcel` 被改了数据但没换 ID）。
    """
    c = str(o.get("code") or "").replace("\x00", "")
    if len(c) == 4:
        return c
    b = str(o.get("base") or "").replace("\x00", "")
    if len(b) == 4:
        return b
    return c or b or "????"


# ── 文件名 ───────────────────────────────────────────────────────────────
_BAD = re.compile(r'[<>:"/\\|?*\x00-\x1f]')


def safe_name(s: str, limit: int = 60) -> str:
    t = clean_inline(s)
    t = _BAD.sub(" ", t)
    t = re.sub(r"\s+", " ", t).strip(" .")
    if len(t) > limit:
        t = t[:limit].rstrip(" .")
    return t or "未命名"


def write_page(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


# ── markdown 片段 ────────────────────────────────────────────────────────
def table(headers: list[str], rows: list[list], align: list[str] | None = None) -> str:
    if not rows:
        return "_（无）_\n"
    align = align or ["---"] * len(headers)
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(align) + " |"]
    for r in rows:
        cells = ["" if c is None else str(c) for c in r]
        cells += [""] * (len(headers) - len(cells))
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out) + "\n"


def source_footer(extra: list[str] | None = None) -> str:
    lines = ["", "---", ""]
    lines.append('<div class="wiki-source-note" markdown="1">')
    lines.append("")
    lines.append(f"**数据来源**：`{MAP_NAME}`（母图 SHA256 `{MAP_SHA256}`）")
    lines.append("")
    lines.append(
        "本页数值由该图的 `war3map.w3u` / `war3map.w3a` / `war3map.w3t` 与 `war3map.j` 解析生成；"
        "**未经过实机验证**——「数据来自哪个成员」不等于「游戏里就是这个表现」。"
    )
    for e in extra or []:
        lines.append("")
        lines.append(e)
    lines.append("")
    lines.append("</div>")
    lines.append("")
    return "\n".join(lines)
