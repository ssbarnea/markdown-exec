"""Formatter for literate Markdown."""

from __future__ import annotations

from markdown_exec.formatters.base import base_format


def _format_markdown(**kwargs) -> str:
    return base_format(language="md", run=lambda code, **_: code, **kwargs)
