"""G4. Six priority orders. A written order is a measurement of the declaration."""

from evalathan.findings import read_text, text_files
from evalathan.model import Cell, deferred, scored
from evalathan.subject import Subject

GATE = "G4"
QUESTION = "Did the declared cost, speed, and impact order match the build?"
ORDERS = ("mcmemi", "mcmime", "memcmi", "memimc", "mimcme", "mimemc")


def run(subject: Subject) -> Cell:
    found: list[str] = []
    evidence: list[str] = []
    blobs = [("README", subject.readme_text)]
    for path in text_files(subject, {".md", ".json", ".txt"}, cap=80):
        blobs.append((subject.rel(path), read_text(path, 40_000)))
    for label, blob in blobs:
        compact = blob.lower().replace(" ", "")
        hits = [order for order in ORDERS if order in compact]
        if hits:
            found.extend(hits)
            evidence.append(label)
    if not found:
        return deferred(
            "Triadly",
            GATE,
            QUESTION,
            "No M3 order (cost, speed, impact) is declared in this tree.",
        )
    unique = []
    for item in found:
        if item not in unique:
            unique.append(item)
    return scored(
        "Triadly",
        GATE,
        QUESTION,
        "Declared priority: " + ", ".join(unique) + ". The declaration is recorded. A build-follow check needs a second artifact that repeats the same order.",
        evidence[:8],
        passed=None,
    )
