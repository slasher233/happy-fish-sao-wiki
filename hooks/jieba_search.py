# -*- coding: utf-8 -*-
"""MkDocs hook：给中文内容做词粒度索引。

Material 的搜索把整段文本按 separator 切开。中文没有空格，默认会切成很长的
片段，导致「只记得一半关键词」搜不到。这里在**行内文本**（不动 HTML 标签、
不动 code/pre/script/style）里用 jieba 分词，并在词与词之间插入零宽空格
U+200B；mkdocs.yml 的 search.separator 已包含 \\u200b，于是索引粒度变成词。

设计原则：**任何异常都不影响构建**（hook 出错只会让搜索退化，不能让站点构建失败）。
"""
from __future__ import annotations

import re

try:
    import jieba

    jieba.initialize()
    _HAS_JIEBA = True
except Exception:  # pragma: no cover - 环境缺 jieba 时静默降级
    _HAS_JIEBA = False

ZWSP = "\u200b"

# 需要跳过的块级元素（整段不处理）
_SKIP_BLOCK = re.compile(
    r"<(code|pre|script|style|kbd|samp|var)\b.*?</\1>",
    re.IGNORECASE | re.DOTALL,
)
# 需要跳过的自闭合/单标签
_SKIP_TAG = re.compile(r"<[^>]+>")
# 含 CJK 的片段才需要分词
_CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")


def _tokenize_text(text: str) -> str:
    """只在含中文的文本片段里插零宽空格。"""
    if not text.strip() or not _CJK.search(text):
        return text
    try:
        words = [w for w in jieba.lcut(text) if w.strip()]
    except Exception:
        return text
    if len(words) <= 1:
        return text
    return ZWSP.join(words)


def _process_html(html: str) -> str:
    """跳过 code/pre/script/style 后，对纯文本片段分词。"""
    placeholders: list[str] = []

    def _stash(match: re.Match) -> str:
        placeholders.append(match.group(0))
        return f"\x00{len(placeholders) - 1}\x00"

    masked = _SKIP_BLOCK.sub(_stash, html)

    # 按标签切开，只处理标签之间的文本
    parts = re.split(r"(<[^>]+>)", masked)
    for i, part in enumerate(parts):
        if part.startswith("<") and part.endswith(">"):
            continue
        if "\x00" in part:  # 占位符片段，整段跳过
            continue
        parts[i] = _tokenize_text(part)
    out = "".join(parts)

    def _restore(match: re.Match) -> str:
        return placeholders[int(match.group(1))]

    return re.sub(r"\x00(\d+)\x00", _restore, out)


def on_page_content(html: str, page, config, files):  # noqa: ARG001
    if not _HAS_JIEBA:
        return html
    try:
        return _process_html(html)
    except Exception:
        return html
