"""G10. Each claim is checked for a source or a recipe."""

from evalathan.findings import load_json, text_files
from evalathan.model import Cell, deferred, scored
from evalathan.subject import Subject

GATE = "G10"
QUESTION = "Is each claim, or the headline number, backed by its recipe?"


def _claims(data) -> list | None:
    if isinstance(data, list) and data and isinstance(data[0], dict) and "claim" in data[0]:
        return data
    if isinstance(data, dict):
        for key in ("claims", "warrants"):
            if isinstance(data.get(key), list):
                return data[key]
    return None


def run(subject: Subject) -> Cell:
    for path in text_files(subject, {".json"}, cap=300):
        data = load_json(path)
        claims = _claims(data)
        if not claims:
            continue
        backed = 0
        for item in claims:
            if not isinstance(item, dict):
                continue
            if item.get("source") or item.get("recipe") or item.get("evidence"):
                backed += 1
        return scored(
            "Warrantly",
            GATE,
            QUESTION,
            f"{subject.rel(path)}: {backed} of {len(claims)} claims carry a source, recipe, or evidence field.",
            [subject.rel(path)],
            passed=True if backed == len(claims) and claims else None,
        )
    if subject.text_hits("probability constitution", "scoring constitution", "warrant chain"):
        return scored(
            "Warrantly",
            GATE,
            QUESTION,
            "The README names a recipe. Claim rows were not found, so each claim is still unchecked.",
            ["README"],
            passed=None,
        )
    return deferred(
        "Warrantly",
        GATE,
        QUESTION,
        "No claim register in this tree.",
    )
