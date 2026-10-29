"""Look for a named Product Requirements Document. This is not an evaler."""

from evalathan.subject import Subject

STEMS = {"prd", "product-requirements", "product_requirements"}
SUFFIXES = {".md", ".rst", ".txt", ".adoc"}


def note(subject: Subject) -> str:
    hits: list[str] = []
    for path in subject.files:
        if path.suffix.lower() not in SUFFIXES:
            continue
        if path.stem.lower() not in STEMS:
            continue
        hits.append(subject.rel(path).replace("\\", "/"))
        if len(hits) >= 6:
            break
    if not hits:
        return "No PRD found"
    return "PRD found: " + "; ".join(hits)
