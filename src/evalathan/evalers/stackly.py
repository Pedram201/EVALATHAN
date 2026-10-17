"""Last. Stackly reports the vector after the other stations have run."""

from evalathan.model import Cell, Status, deferred, scored
from evalathan.subject import Subject

GATE = "G6"
QUESTION = "Does the whole system hold after the stations it depends on have scores?"
ACCEPTS_PRIOR = True


def run(subject: Subject, prior: list[Cell] | None = None) -> Cell:
    del subject
    prior = list(prior or [])
    ran = [cell for cell in prior if cell.ran()]
    if not ran:
        return deferred(
            "Stackly",
            GATE,
            QUESTION,
            "No station has a measurement yet, so Stackly does not issue a system grade.",
        )
    passed = [cell for cell in prior if cell.passed is True]
    blanks = [cell.agent for cell in prior if cell.status is Status.DEFERRED]
    return scored(
        "Stackly",
        GATE,
        QUESTION,
        (
            f"{len(ran)} stations have a measurement. {len(passed)} passed their own gate. "
            f"Still deferred: {', '.join(blanks) if blanks else 'none'}. "
            "Stackly keeps that vector. It does not blend the stations into one float."
        ),
        [cell.agent for cell in ran],
        passed=None,
    )
