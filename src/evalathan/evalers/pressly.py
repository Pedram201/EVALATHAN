"""G10. Byte, time, and quality numbers come from a compressor printout."""

import re

from evalathan.findings import read_text, text_files
from evalathan.model import Cell, deferred, scored
from evalathan.subject import Subject

GATE = "G10"
QUESTION = "What size, time, and quality number did the compressor print?"
PATTERNS = {
    "SSIM": re.compile(r"ssim[=:\s]+([0-9]+(?:\.[0-9]+)?)", re.I),
    "VMAF": re.compile(r"vmaf[=:\s]+([0-9]+(?:\.[0-9]+)?)", re.I),
    "bytes": re.compile(r"(?:size|bytes)\s*[=:]\s*([0-9]+)", re.I),
}


def run(subject: Subject) -> Cell:
    hits = []
    evidence = []
    for path in text_files(subject, {".log", ".txt", ".json", ".md"}, cap=250):
        blob = read_text(path, 100_000)
        if not blob:
            continue
        found = []
        for label, pattern in PATTERNS.items():
            match = pattern.search(blob)
            if match:
                found.append(f"{label} {match.group(1)}")
        if found:
            hits.append(f"{subject.rel(path)}: " + ", ".join(found))
            evidence.append(subject.rel(path))
        if len(hits) >= 6:
            break
    if not hits:
        return deferred(
            "Pressly",
            GATE,
            QUESTION,
            "No SSIM, VMAF, or byte-size printout in this tree. Byte compression is not a TOKEX (Token Expenditure) result.",
        )
    return scored(
        "Pressly",
        GATE,
        QUESTION,
        "Printed figure: " + "; ".join(hits) + ". A byte count in a text file is not a quality grade and not a token saving.",
        evidence,
        passed=None,
    )
