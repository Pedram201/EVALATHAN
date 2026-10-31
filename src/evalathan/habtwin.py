"""Look for a sealed HabTwin lab trace. This is not an evaler and not a login."""

from evalathan.subject import Subject

MARKS = ("habtwin", "hab-twin", "habit-twin")
TRACE_WORDS = ("trace", "trajectory", "passk")


def note(subject: Subject) -> str:
    hits: list[str] = []
    for path in subject.files:
        name = path.name.lower()
        if not any(mark in name for mark in MARKS):
            continue
        if not any(word in name for word in TRACE_WORDS):
            continue
        hits.append(subject.rel(path).replace("\\", "/"))
        if len(hits) >= 6:
            break
    if not hits:
        return "No HabTwin lab trace"
    return "HabTwin lab trace: " + "; ".join(hits)
