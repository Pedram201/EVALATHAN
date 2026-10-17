"""G3. A README is a declaration, not a 97-principle pass."""

from evalathan.model import Cell, deferred, provisional
from evalathan.subject import Subject

GATE = "G3"
QUESTION = "Does the architecture meet the gate at the claimed stage?"


def run(subject: Subject) -> Cell:
    prior = [
        p
        for p in subject.files
        if p.name.lower() in {"leviathan_v1.json", "eval_leviathan.md"}
    ]
    if prior:
        return provisional(
            "Archly",
            GATE,
            QUESTION,
            "A prior Evalev artifact is on disk. This run does not re-score the 97 principles.",
            [subject.rel(p) for p in prior[:8]],
        )
    docs = [
        p
        for p in subject.files
        if p.suffix.lower() in {".md", ".rst", ".adoc"}
        and any(part.lower() in {"docs", "doc", "architecture"} for part in p.parts)
    ]
    if subject.readme_text or docs:
        evidence = []
        if subject.readme_text:
            evidence.append("README present")
        evidence.extend(subject.rel(p) for p in docs[:8])
        return provisional(
            "Archly",
            GATE,
            QUESTION,
            "A written declaration exists. Design-declaration review has not been run.",
            evidence,
        )
    return deferred(
        "Archly",
        GATE,
        QUESTION,
        "No README and no architecture document. Nothing to review.",
    )
