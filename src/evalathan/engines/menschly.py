"""G8. A timer in the source passes this row. A README sentence does not. FUSS is optional."""

from evalathan.findings import read_text, text_files
from evalathan.model import Cell, deferred, provisional, scored
from evalathan.subject import Subject

GATE = "G8"
QUESTION = "Does a sitting ask the person to stop?"
STOP_PHRASES = ("take a break", "session limit", "time budget")
TIMER_MARKS = ("def bind_fuss", "def bindfuss", "function bindfuss", "session_limit_minutes", "sessionlimit")


def _timer_files(subject: Subject) -> list[str]:
    found = []
    for path in text_files(subject, {".py", ".js", ".mjs", ".ts"}, cap=400):
        if path.stem.lower() in {"fuss", "bind_fuss", "bindfuss"}:
            found.append(subject.rel(path))
            continue
        blob = read_text(path, 80_000).lower()
        if any(mark in blob for mark in TIMER_MARKS):
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
