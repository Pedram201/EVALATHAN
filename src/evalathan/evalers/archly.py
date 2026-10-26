"""G3. Score the 97 principles only where this tree cites evidence."""

from evalathan.evalers.principles97 import infer
from evalathan.model import Cell, deferred, scored
from evalathan.subject import README_NAMES, Subject

GATE = "G3"
QUESTION = "Does the architecture meet the gate at the claimed stage?"
_DOC_PARTS = {"docs", "doc", "architecture", "adr", "adrs"}
_DOC_SUFFIX = {".md", ".rst", ".adoc"}
_ROOT_DOCS = {"architecture.md", "design.md", "overview.md"}


def _chunks(subject: Subject) -> list[tuple[str, str, str]]:
    chunks: list[tuple[str, str, str]] = []
    if subject.readme_text.strip():
        chunks.append(("README", subject.readme_text.lower(), "readme"))
    taken = 0
    for path in subject.files:
        if taken >= 20 or path.suffix.lower() not in _DOC_SUFFIX:
            continue
        if path.name.lower() in README_NAMES:
            continue
        rel = subject.rel(path).replace("\\", "/")
        parts = {part.lower() for part in path.parts}
        rootish = path.parent == subject.root and path.name.lower() in _ROOT_DOCS
        if not (parts & _DOC_PARTS) and not rootish and not path.name.lower().startswith("adr"):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")[:8000]
        except OSError:
            continue
        chunks.append((rel, text.lower(), "doc"))
        taken += 1
    return chunks


def _summary(rows) -> str:
    scored_rows = [row for row in rows if row.score is not None]
    blank = 97 - len(scored_rows)
    if not scored_rows:
        return (
            "97-principle review ran. 0 of 97 had citable evidence, so there is no mean. "
            f"{blank} stay deferred. They are not counted as zero."
        )
    mean = sum(row.score for row in scored_rows) / len(scored_rows)
    emerging = sum(1 for row in scored_rows if row.score == 2)
    solid = sum(1 for row in scored_rows if row.score == 3)
    strong = sum(1 for row in scored_rows if row.score == 4)
    return (
        "97-principle review ran. "
        f"{len(scored_rows)} of 97 had citable evidence. "
        f"Mean {mean:.2f} out of 4 on those {len(scored_rows)} "
        f"(Strong {strong}, Solid {solid}, Emerging {emerging}). "
        f"{blank} had no evidence and stay deferred. They are not counted as zero. "
        "No gate pass is awarded."
    )


def run(subject: Subject) -> Cell:
    rels = [subject.rel(path).replace("\\", "/").lower() for path in subject.files]
    chunks = _chunks(subject)
    if not rels and not chunks:
        return deferred(
            "Archly",
            GATE,
            QUESTION,
            "No README, no document, and no source file. Nothing to review.",
        )
    rows = infer(chunks, rels, len(subject.by_lang), subject.commit_count)
    cites = []
    for row in rows:
        if row.cite and row.cite not in cites:
            cites.append(row.cite)
        if len(cites) == 8:
            break
    return scored(
        "Archly",
        GATE,
        QUESTION,
        _summary(rows),
        cites,
        passed=None,
    )
