"""G10. TOKEX (Token Expenditure) counts only from a before and an after."""

from evalathan.findings import load_json, text_files
from evalathan.model import Cell, deferred, scored
from evalathan.subject import Subject

GATE = "G10"
QUESTION = "How many tokens, if any, did a sealed before/after save?"


def _pair(data: dict) -> tuple[int, int] | None:
    if "before" in data and "after" in data:
        try:
            return int(data["before"]), int(data["after"])
        except (TypeError, ValueError):
            return None
    if "total_tokex" in data and "tokex_this_run" in data:
        try:
            return int(data["total_tokex"]), int(data["tokex_this_run"])
        except (TypeError, ValueError):
            return None
    nested = data.get("tokex")
    if isinstance(nested, dict):
        return _pair(nested)
    return None


def run(subject: Subject) -> Cell:
    for path in text_files(subject, {".json"}, cap=300):
        data = load_json(path)
        if not isinstance(data, dict):
            continue
        pair = _pair(data)
        if pair is None:
            continue
        before, after = pair
        savings = max(0, before - after)
        return scored(
            "Tokly",
            GATE,
            QUESTION,
            f"Sealed pair in {subject.rel(path)}: before {before}, after {after}, savings {savings}. A measured zero is a result.",
            [subject.rel(path)],
            passed=None,
        )
    return deferred(
        "Tokly",
        GATE,
        QUESTION,
        "No sealed before/after token record in this tree. A compiler with no token claim stays deferred.",
    )
