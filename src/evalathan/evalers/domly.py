"""G7. A versioned question bank is counted. Answers are matched when a second file exists."""

from evalathan.findings import load_json, text_files
from evalathan.model import Cell, deferred, scored
from evalathan.subject import Subject

GATE = "G7"
QUESTION = "Do domain answers match a versioned question bank for the claimed domain?"


def _items(data) -> list | None:
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for key in ("questions", "items", "answers"):
            if isinstance(data.get(key), list):
                return data[key]
    return None


def run(subject: Subject) -> Cell:
    banks = []
    for path in text_files(subject, {".json", ".yml", ".yaml"}, cap=300):
        if "question" not in path.name.lower() and "answer" not in path.name.lower():
            continue
        data = load_json(path)
        items = _items(data)
        if items is None:
            continue
        banks.append((path, items))
    if not banks:
        return deferred(
            "Domly",
            GATE,
            QUESTION,
            "No versioned question bank in this tree. A language conformance suite is Runly and Codely, not Domly.",
        )
    question_ids = set()
    answer_ids = set()
    for path, items in banks:
        bucket = answer_ids if "answer" in path.name.lower() else question_ids
        for item in items:
            if isinstance(item, dict) and item.get("id") is not None:
                bucket.add(str(item["id"]))
            else:
                bucket.add(str(len(bucket)))
    if answer_ids:
        matched = len(question_ids & answer_ids)
        return scored(
            "Domly",
            GATE,
            QUESTION,
            f"{len(question_ids)} questions, {len(answer_ids)} answers, {matched} ids in both.",
            [subject.rel(path) for path, _ in banks[:8]],
            passed=None,
        )
    return scored(
        "Domly",
        GATE,
        QUESTION,
        f"{len(question_ids)} questions in the bank. An answers file is not beside it yet.",
        [subject.rel(path) for path, _ in banks[:8]],
        passed=None,
    )
