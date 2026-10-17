"""Conductor. Sixteen cells. A blank is printed, never turned into a zero."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from evalathan.evalers import ALL
from evalathan.model import Cell, Status
from evalathan.subject import Subject, load


@dataclass
class Report:
    root: str
    cells: list[Cell]

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
            "Evalathan v0.2",
            self.root,
            self.headline(),
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
            "version": "0.2.0",
            "conductor": "Hydra",
            "root": self.root,
            "headline": self.headline(),
            "ran": len(self.ran),
            "passed": len(self.passed),
            "deferred": len(self.deferred),
            "cells": [cell.to_dict() for cell in self.cells],
        }


def conduct(root: Path, subject: Subject | None = None) -> Report:
    seen = subject if subject is not None else load(root)
    cells = []
    for evaler in ALL:
        if getattr(evaler, "ACCEPTS_PRIOR", False):
            cells.append(evaler.run(seen, cells))
        else:
            cells.append(evaler.run(seen))
    if len(cells) != 16:
        raise RuntimeError(f"Hydra expected 16 evalers, got {len(cells)}")
    names = [cell.agent for cell in cells]
    if len(set(names)) != 16:
        raise RuntimeError("Duplicate evaler name")
    return Report(root=str(seen.root), cells=cells)
