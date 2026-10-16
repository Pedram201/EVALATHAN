"""Shared readers. Engines measure files. They do not invent a grade."""

from __future__ import annotations

import json
from pathlib import Path

from evalathan.subject import Subject

TEXT_SUFFIXES = {".py", ".js", ".mjs", ".ts", ".tsx", ".md", ".json", ".jsonl", ".txt", ".log", ".yml", ".yaml"}


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except (OSError, json.JSONDecodeError, UnicodeError):
        return None


def read_text(path: Path, limit: int = 200_000) -> str:
    try:
        if path.stat().st_size > limit:
            return ""
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def text_files(subject: Subject, suffixes: set[str] | None = None, cap: int = 500) -> list[Path]:
    allowed = suffixes or TEXT_SUFFIXES
    found = []
    for path in subject.files:
        if path.suffix.lower() not in allowed:
            continue
        found.append(path)
        if len(found) >= cap:
            break
    return found
