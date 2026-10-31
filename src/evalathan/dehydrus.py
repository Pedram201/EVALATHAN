"""Conductor for the seven PRETRUWs world evalers. A blank is never a zero."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from evalathan.evalers_pretruws import ALL
from evalathan.habtwin import note as habtwin_note
from evalathan.model import Cell, Status
from evalathan.subject import Subject, load


@dataclass
class Report:
    root: str
    cells: list[Cell]
    habtwin: str = "No HabTwin lab trace"

    @property
    def ran(self) -> list[Cell]:
        return [cell for cell in self.cells if cell.ran()]

    @property
    def deferred(self) -> list[Cell]:
        return [cell for cell in self.cells if cell.status is Status.DEFERRED]

    @property
    def passed(self) -> list[Cell]:
        return [cell for cell in self.cells if cell.passed is True]

    def headline(self) -> str:
        return (
            f"{len(self.ran)} of {len(self.cells)} evalers ran. "
            f"{len(self.passed)} passed their own gate. "
            f"{len(self.deferred)} are deferred, and they are listed."
        )

    def render(self) -> str:
        lines = [
            "Evalathan v0.3",
            self.root,
            self.headline(),
            self.habtwin,
            "",
        ]
        for cell in self.cells:
            mark = cell.status.value
            if cell.passed is True:
                mark = "passed"
            lines.append(f"{cell.agent:12} {cell.gate:4} {mark:12} {cell.summary}")
        return "\n".join(lines)

    def to_dict(self) -> dict:
        return {
            "product": "Evalathan",
            "version": "0.3.0",
            "conductor": "Dehydrus",
            "framework": "PRETRUWs",
            "root": self.root,
            "headline": self.headline(),
            "habtwin": self.habtwin,
            "ran": len(self.ran),
            "passed": len(self.passed),
            "deferred": len(self.deferred),
            "cells": [cell.to_dict() for cell in self.cells],
        }


def conduct(root: Path, subject: Subject | None = None) -> Report:
    seen = subject if subject is not None else load(root)
    cells: list[Cell] = []
    for evaler in ALL:
        if getattr(evaler, "ACCEPTS_PRIOR", False):
            cells.append(evaler(seen, cells))
        else:
            cells.append(evaler(seen))
    if len(cells) != 7:
        raise RuntimeError(f"Dehydrus expected 7 evalers, got {len(cells)}")
    names = [cell.agent for cell in cells]
    if len(set(names)) != 7:
        raise RuntimeError("Duplicate evaler name")
    return Report(root=str(seen.root), cells=cells, habtwin=habtwin_note(seen))
