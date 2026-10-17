"""G0. A commit count is not an SFIA level."""

from evalathan.model import Cell, deferred, scored
from evalathan.subject import Subject

GATE = "G0"
QUESTION = "What responsibility level does the builder show on this product?"


def run(subject: Subject) -> Cell:
    if subject.commit_count is None:
        return deferred(
            "Devly",
            GATE,
            QUESTION,
            "No git history on this tree. SFIA (Skills Framework for the Information Age) 9 is not awarded from a folder of files.",
        )
    return scored(
        "Devly",
        GATE,
        QUESTION,
        f"Git history has {subject.commit_count} commits. No SFIA level is assigned.",
        [f"git rev-list --count HEAD = {subject.commit_count}"],
        passed=None,
    )
