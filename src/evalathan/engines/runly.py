"""G7. A local loop always times. SPEC, LLVM, and pyperformance count only from their own files."""

from __future__ import annotations

import time

from evalathan.findings import load_json, text_files
from evalathan.model import Cell, deferred, scored
from evalathan.subject import Subject

GATE = "G7"
QUESTION = "How fast is this compiler, interpreter, or runtime on a suite that was run?"


def _suite_numbers(subject: Subject) -> list[str]:
    found = []
    for path in text_files(subject, {".json", ".txt", ".log"}, cap=200):
        name = path.name.lower()
        if "pyperformance" not in name and "spec2017" not in name and "llvm" not in name:
            continue
        payload = load_json(path) if path.suffix.lower() == ".json" else None
        if isinstance(payload, dict) and ("benchmarks" in payload or "results" in payload):
            found.append(f"{subject.rel(path)} has a result object")
        elif path.suffix.lower() != ".json":
            found.append(subject.rel(path))
    return found


def _microbench() -> float:
    started = time.perf_counter()
    total = 0
    for i in range(200_000):
        total += i
    elapsed = time.perf_counter() - started
    if total < 0:
        raise RuntimeError("unreachable")
    return elapsed * 1000.0


def run(subject: Subject) -> Cell:
    suites = _suite_numbers(subject)
    has_code = any(path.suffix.lower() == ".py" for path in subject.files)
    if not suites and not has_code:
        return deferred(
            "Runly",
            GATE,
            QUESTION,
            "No Python source and no SPEC, LLVM test-suite, or pyperformance result file.",
        )
    parts = []
    if has_code:
        parts.append(f"Evalathan microbench: {_microbench():.1f} ms for 200000 integer steps on this machine.")
    if suites:
        parts.append("Suite files: " + "; ".join(suites[:6]) + ".")
    else:
        parts.append("SPEC, LLVM test-suite, and pyperformance files are absent, so those suites are not the source of this time.")
    return scored("Runly", GATE, QUESTION, " ".join(parts), suites or ["evalathan-microbench"], passed=None)
