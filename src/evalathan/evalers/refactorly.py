"""G11. Identical bytes, unreferenced Python names, and git churn."""

from __future__ import annotations

import ast
import hashlib
import subprocess
from collections import defaultdict

from evalathan.model import Cell, deferred, scored
from evalathan.subject import Subject

GATE = "G11"
QUESTION = "Is change localized: duplication, dead code, churn?"


def _dead_python(subject: Subject) -> list[str]:
    defined: dict[str, str] = {}
    used: set[str] = set()
    for path in subject.files:
        if path.suffix.lower() != ".py":
            continue
        try:
            tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
        except (OSError, SyntaxError):
            continue
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                if isinstance(getattr(node, "parent_scope", None), type(None)) or True:
                    defined.setdefault(node.name, subject.rel(path))
            if isinstance(node, ast.Name):
                used.add(node.id)
            if isinstance(node, ast.Attribute):
                used.add(node.attr)
    dead = []
    for name, rel in defined.items():
        if name.startswith("_") or name.startswith("test"):
            continue
        if name not in used:
            dead.append(f"{name} in {rel}")
    return dead


def _churn(subject: Subject) -> str:
    if not (subject.root / ".git").exists():
        return "Churn needs a git history, and this tree has none."
    try:
        out = subprocess.run(
            ["git", "log", "--numstat", "--pretty=format:", "-n", "40"],
            cwd=subject.root,
            capture_output=True,
            text=True,
            timeout=8,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return "Git churn command did not finish."
    if out.returncode != 0:
        return "Git churn command did not finish."
    totals: dict[str, int] = defaultdict(int)
    for line in out.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) != 3:
            continue
        added, deleted, name = parts
        try:
            totals[name] += int(added) + int(deleted)
        except ValueError:
            continue
    if not totals:
        return "Git history has no line churn in the last 40 commits."
    top = sorted(totals.items(), key=lambda item: item[1], reverse=True)[:3]
    shown = ", ".join(f"{name} {count}" for name, count in top)
    return f"Churn over the last 40 commits, top files: {shown}."


def run(subject: Subject) -> Cell:
    groups: dict[str, list[str]] = defaultdict(list)
    hashed = 0
    for path in subject.files:
        try:
            size = path.stat().st_size
        except OSError:
            continue
        if size == 0 or size > 200_000:
            continue
        try:
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
        except OSError:
            continue
        hashed += 1
        groups[digest].append(subject.rel(path))
    dupes = [paths for paths in groups.values() if len(paths) > 1]
    dead = _dead_python(subject)
    if hashed == 0:
        return deferred("Refactorly", GATE, QUESTION, "No files small enough to hash.")
    shown = [", ".join(group[:4]) for group in dupes[:8]]
    return scored(
        "Refactorly",
        GATE,
        QUESTION,
        (
            f"{len(dupes)} identical-byte groups among {hashed} hashed files. "
            f"Unreferenced Python names: {len(dead)}. {_churn(subject)}"
        ),
        (shown or ["no identical-byte groups"]) + dead[:8],
        passed=None,
    )
