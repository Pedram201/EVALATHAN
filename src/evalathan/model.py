"""Shared result types. A deferred cell is not a zero and not a pass."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any


class Status(str, Enum):
    # A count, time, or file fact was written. The printed word is measured. This is not a grade.
    SCORED = "measured"
    PROVISIONAL = "provisional"
    DEFERRED = "deferred"


@dataclass
class Cell:
    agent: str
    gate: str
    question: str
    status: Status
    summary: str
    evidence: list[str] = field(default_factory=list)
    passed: bool | None = None

    def ran(self) -> bool:
        return self.status is not Status.DEFERRED

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["status"] = self.status.value
        return data


def deferred(agent: str, gate: str, question: str, summary: str) -> Cell:
    return Cell(
        agent=agent,
        gate=gate,
        question=question,
        status=Status.DEFERRED,
        summary=summary,
        passed=None,
    )


def scored(
    agent: str,
    gate: str,
    question: str,
    summary: str,
    evidence: list[str],
    passed: bool | None = None,
) -> Cell:
    return Cell(
        agent=agent,
        gate=gate,
        question=question,
        status=Status.SCORED,
        summary=summary,
        evidence=evidence,
        passed=passed,
    )


def provisional(
    agent: str,
    gate: str,
    question: str,
    summary: str,
    evidence: list[str],
) -> Cell:
    return Cell(
        agent=agent,
        gate=gate,
        question=question,
        status=Status.PROVISIONAL,
        summary=summary,
        evidence=evidence,
        passed=None,
    )
