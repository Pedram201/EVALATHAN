"""G10. A replayable trace is counted from saved steps. A copied leaderboard is not evidence."""

import json

from evalathan.findings import read_text, text_files
from evalathan.model import Cell, deferred, scored
from evalathan.subject import Subject

GATE = "G10"
QUESTION = "Did a sealed, replayable trace stay on the task?"


def run(subject: Subject) -> Cell:
    steps = 0
    evidence = []
    for path in text_files(subject, {".jsonl", ".json", ".md"}, cap=200):
        name = path.name.lower()
        if not any(word in name for word in ("trace", "trajectory", "passk")):
            continue
        blob = read_text(path, 200_000)
        if path.suffix.lower() == ".jsonl":
            count = 0
            for line in blob.splitlines():
                if not line.strip():
                    continue
                try:
                    json.loads(line)
                    count += 1
                except json.JSONDecodeError:
                    continue
            if count:
                steps += count
                evidence.append(f"{subject.rel(path)} {count} steps")
        elif blob.strip():
            steps += 1
            evidence.append(subject.rel(path))
    if steps == 0:
        return deferred(
            "Trajectly",
            GATE,
            QUESTION,
            "No replayable trace in this tree. A library or compiler with no agent loop stays deferred.",
        )
    return scored(
        "Trajectly",
        GATE,
        QUESTION,
        f"{steps} saved trace steps. This count is from files in the tree. It is not a number copied from a public leaderboard.",
        evidence[:8],
        passed=None,
    )
