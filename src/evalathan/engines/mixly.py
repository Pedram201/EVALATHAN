"""G5. A language share is a count. It is not an order to rewrite."""

from evalathan.model import Cell, deferred, scored
from evalathan.subject import Subject

GATE = "G5"
QUESTION = "What share of the source files is which language?"


def run(subject: Subject) -> Cell:
    total = sum(subject.by_lang.values())
    if total == 0:
        return deferred("Mixly", GATE, QUESTION, "No recognized source files to count.")
    parts = [
        f"{name} {count} ({100.0 * count / total:.1f}% of recognized files)"
        for name, count in subject.by_lang.items()
    ]
    note = " File walk stopped at the cap." if subject.truncated else ""
    return scored(
        "Mixly",
        GATE,
        QUESTION,
        "Recognized source files: " + "; ".join(parts) + "." + note + " The share is the result. A language rewrite stays with the maintainer.",
        [f"{total} recognized source files"],
        passed=None,
    )
