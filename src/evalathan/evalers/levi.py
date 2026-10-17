"""G8. A 4Uvals record with a gate result is a sitting grade. A README adjective is not."""

from evalathan.findings import load_json, text_files
from evalathan.model import Cell, deferred, provisional, scored
from evalathan.subject import Subject

GATE = "G8"
QUESTION = "Did use put the person first?"


def _record(subject: Subject) -> tuple[dict, str] | None:
    for path in text_files(subject, {".json"}, cap=300):
        data = load_json(path)
        if not isinstance(data, dict):
            continue
        family = str(data.get("family") or data.get("brand") or "")
        if "4uval" not in family.lower():
            continue
        if isinstance(data.get("gate"), dict):
            return data, subject.rel(path)
    return None


def run(subject: Subject) -> Cell:
    found = _record(subject)
    if found:
        data, rel = found
        gate = data["gate"]
        mean = gate.get("mean")
        result = str(gate.get("result") or "").upper()
        passed = True if result == "PASS" else False if result == "FAIL" else None
        return scored(
            "Levi",
            GATE,
            QUESTION,
            (
                f"4Uvals record {rel}: mean {mean}, gate {result or 'unset'}. "
                "ISO/IEC 42001 stays the firm wrapper named beside the sitting. It is not this grade."
            ),
            [rel],
            passed=passed,
        )
    hits = subject.text_hits("4uvals", "user first", "sus ", "system usability")
    if hits:
        return provisional(
            "Levi",
            GATE,
            QUESTION,
            "The README names a user-interest phrase. A 4Uvals gate record was not found, so this is not a score.",
            hits,
        )
    return deferred(
        "Levi",
        GATE,
        QUESTION,
        "No 4Uvals gate record in this tree. ISO/IEC 42001 is not a sitting grade.",
    )
