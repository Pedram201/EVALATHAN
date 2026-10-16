"""G5. An agent roster is counted. SASPIANT asks whether each row is a specialist chore."""

from evalathan.findings import read_text
from evalathan.model import Cell, deferred, scored
from evalathan.subject import Subject

GATE = "G5"
QUESTION = "Is each agent a specialist chore, with judgment left to a human?"


def _roster(subject: Subject) -> list:
    found = []
    for path in subject.files:
        name = path.name.lower()
        if name in {"agent_registry.md", "agents.md", "agentic_registry.md"}:
            found.append(path)
        elif path.parent.name.lower() == "agents" and path.suffix.lower() == ".md":
            found.append(path)
    return found


def run(subject: Subject) -> Cell:
    roster = _roster(subject)
    if not roster:
        return deferred(
            "Chorely",
            GATE,
            QUESTION,
            "No agent roster in this tree. SASPIANT (Specific and Specialized, Pain-In-the-Ass, Non-critical Tasks) and Why An Agent? have nothing to count.",
        )
    rows = 0
    with_role = 0
    for path in roster:
        text = read_text(path, 80_000)
        for line in text.splitlines():
            if line.startswith("| **") or line.startswith("| **"):
                rows += 1
                if "agent" in line.lower() or "utility" in line.lower() or ".md" in line.lower():
                    with_role += 1
        if path.parent.name.lower() == "agents":
            rows += 1
            if "role" in text.lower() or "#" in text:
                with_role += 1
    return scored(
        "Chorely",
        GATE,
        QUESTION,
        f"{len(roster)} roster files, {rows} rows, {with_role} with a role or profile link. Judgment stays with a human.",
        [subject.rel(path) for path in roster[:8]],
        passed=None,
    )
