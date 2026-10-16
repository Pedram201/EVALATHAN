"""G7. Python branch counts are a measurement. They are not radon and not ISO 5055."""

from __future__ import annotations

import ast
from pathlib import Path

from evalathan.model import Cell, deferred, scored
from evalathan.subject import Subject

GATE = "G7"
QUESTION = "Do tests, coverage, complexity, and diagnostics hold on this tree?"
PACKS = ("Python", "JavaScript", "TypeScript", "C", "C++", "Rust", "Go", "Java")
BRANCH_NODES = (ast.If, ast.For, ast.While, ast.ExceptHandler, ast.With, ast.Assert)


def _python_complexity(paths: list[Path]) -> tuple[int, int]:
    functions = 0
    branches = 0
    for path in paths:
        if path.suffix.lower() != ".py":
            continue
        try:
            tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
        except (OSError, SyntaxError):
            continue
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                functions += 1
                branches += sum(1 for child in ast.walk(node) if isinstance(child, BRANCH_NODES))
    return functions, branches


def run(subject: Subject) -> Cell:
    langs = [name for name in subject.by_lang if name in PACKS]
    if not langs:
        present = ", ".join(subject.by_lang) or "none"
        return deferred(
            "Codely",
            GATE,
            QUESTION,
            f"No language pack for this tree ({present}). That is not a pass.",
        )
    if "Python" not in subject.by_lang:
        return deferred(
            "Codely",
            GATE,
            QUESTION,
            "Language pack for "
            + ", ".join(langs)
            + " is named and not executed in v0.1. Python is the only pack that measures.",
        )
    functions, branches = _python_complexity(subject.files)
    tests = [
        subject.rel(p)
        for p in subject.files
        if p.suffix.lower() == ".py" and (p.name.startswith("test_") or p.name.endswith("_test.py"))
    ]
    mean = (branches / functions) if functions else 0.0
    return scored(
        "Codely",
        GATE,
        QUESTION,
        (
            f"Python pack measured {functions} functions, {branches} branch nodes, "
            f"mean {mean:.2f} branch nodes per function. "
            f"Test modules seen: {len(tests)}. "
            "pytest, coverage, radon, and ISO/IEC 5055 were not run."
        ),
        tests[:12] or ["no test_*.py modules"],
        passed=None,
    )
