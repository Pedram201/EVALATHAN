"""PRETRUWs world cards and sealed-trace lookup. This is not a Hydra evaler."""

from __future__ import annotations

from dataclasses import dataclass

from evalathan.findings import read_text, text_files
from evalathan.subject import Subject

CLAIM_MARKS = (
    "physical-world",
    "physical world",
    "world-model",
    "world model",
    "scientific agent",
    "discovery agent",
    "pretruw",
    "ludats",
    "digital twin",
    "dehydrus",
)

TRACE_WORDS = ("trace", "trajectory", "passk")


@dataclass(frozen=True)
class World:
    brand: str
    code: str
    gate: str
    discoverer: str
    tokens: tuple[str, ...]
    required: bool
    deferred_v2: bool
    question: str


WORLDS: tuple[World, ...] = (
    World(
        "Copernly",
        "LuDaTs-C",
        "P1",
        "Nicolaus Copernicus",
        ("ludats-c", "ludats_c", "copernly", "copernicus"),
        False,
        False,
        "Did a sealed 1542 archive world stay in the tree?",
    ),
    World(
        "Keplerly",
        "LuDaTs-K",
        "P2",
        "Johannes Kepler",
        ("ludats-k", "ludats_k", "keplerly", "kepler"),
        False,
        False,
        "Did a sealed 1608 Mars-table world stay in the tree?",
    ),
    World(
        "Galileoly",
        "LuDaTs-G",
        "P3",
        "Galileo Galilei",
        ("ludats-g", "ludats_g", "galileoly", "galileo"),
        True,
        False,
        "Did a sealed optic-and-kinematics world stay in the tree?",
    ),
    World(
        "Darwinly",
        "LuDaTs-D",
        "P4",
        "Charles Darwin",
        ("ludats-d", "ludats_d", "darwinly", "darwin"),
        True,
        False,
        "Did a sealed 1858 field world stay in the tree?",
    ),
    World(
        "Mendly",
        "LuDaTs-M",
        "P5",
        "Dmitri Mendeleev",
        ("ludats-m", "ludats_m", "mendly", "mendeleev"),
        False,
        False,
        "Did a sealed 1868 table-gap world stay in the tree?",
    ),
    World(
        "Einsteinly",
        "LuDaTs-E",
        "P6",
        "Albert Einstein",
        ("ludats-e", "ludats_e", "einsteinly", "einstein"),
        False,
        False,
        "Did a sealed 1914 GR-anomaly world stay in the tree?",
    ),
    World(
        "Newtonly",
        "LuDaTs-N",
        "P7",
        "Isaac Newton",
        ("ludats-n", "ludats_n", "newtonly", "newton"),
        False,
        True,
        "Did a sealed 1686 unification world stay in the tree?",
    ),
)


def claimed(subject: Subject) -> bool:
    for path in text_files(subject, {".md", ".txt", ".rst"}, cap=80):
        blob = read_text(path, 80_000).lower()
        if any(mark in blob for mark in CLAIM_MARKS):
            return True
    return False


def traces_for(subject: Subject, world: World) -> list[str]:
    hits: list[str] = []
    for path in text_files(subject, {".jsonl", ".json", ".md", ".yml", ".yaml", ".txt"}, cap=200):
        name = path.name.lower()
        if not any(word in name for word in TRACE_WORDS):
            continue
        if not any(token in name for token in world.tokens):
            continue
        hits.append(subject.rel(path).replace("\\", "/"))
        if len(hits) >= 6:
            break
    return hits
