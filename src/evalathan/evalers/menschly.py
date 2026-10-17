"""G8. A timer in the source passes this row. A README sentence does not. FUSS is optional."""

import ast

from evalathan.model import Cell, deferred, provisional, scored
from evalathan.subject import Subject

GATE = "G8"
QUESTION = "Does a sitting ask the person to stop?"
STOP_PHRASES = ("take a break", "session limit", "time budget")
TIMER_NAMES = {"bind_fuss", "bindfuss"}
LIMIT_NAMES = {"session_limit_minutes", "sessionlimit"}


def _python_timer(path) -> bool:
    try:
        if path.stat().st_size > 2_000_000:
            return False
        tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
    except (OSError, SyntaxError):
        return False
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name.lower() in TIMER_NAMES:
            return True
        targets = []
        if isinstance(node, ast.Assign):
            targets = node.targets
        elif isinstance(node, ast.AnnAssign):
            targets = [node.target]
        for target in targets:
            if isinstance(target, ast.Name) and target.id.lower() in LIMIT_NAMES:
                return True
    return False


def _script_timer(path) -> bool:
    try:
        if path.stat().st_size > 5_000_000:
            return False
        blob = path.read_text(encoding="utf-8", errors="replace").lower()
    except OSError:
        return False
    return "function bindfuss" in blob or "function bind_fuss" in blob or "session_limit_minutes" in blob


def _timer_files(subject: Subject) -> list[str]:
    found = []
    candidates = [
        path for path in subject.files
        if path.suffix.lower() in {".py", ".js", ".mjs", ".ts", ".tsx"}
    ]
    candidates.sort(key=lambda path: (0 if "fuss" in path.stem.lower() else 1, subject.rel(path)))
    for path in candidates:
        if path.stem.lower() in {"fuss", "bind_fuss", "bindfuss"}:
            found.append(subject.rel(path))
        elif path.suffix.lower() == ".py" and _python_timer(path):
            found.append(subject.rel(path))
        elif path.suffix.lower() != ".py" and _script_timer(path):
            found.append(subject.rel(path))
        if len(found) >= 8:
            break
    return found


def run(subject: Subject) -> Cell:
    timers = _timer_files(subject)
    if timers:
        return scored(
            "Menschly",
            GATE,
            QUESTION,
            "A stop timer is in the source. Any real stop passes this row. "
            "FUSS (For-User Session Switch) is one optional timer, not the only one.",
            timers,
            passed=True,
        )
    hits = subject.text_hits(*STOP_PHRASES)
    if hits:
        return provisional(
            "Menschly",
            GATE,
            QUESTION,
            "Stop language is in the README. That is a claim, not a timer running in the source.",
            hits,
        )
    return deferred(
        "Menschly",
        GATE,
        QUESTION,
        "No timer in the source and no sitting record. A batch tool or compiler stays deferred.",
    )
