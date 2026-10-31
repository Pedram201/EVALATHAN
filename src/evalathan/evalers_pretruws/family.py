"""One run() per PRETRUWs brand. v0.3 names a sealed world. It does not simulate T."""

from __future__ import annotations

from evalathan.model import Cell, deferred, scored
from evalathan.pretruws import WORLDS, World, claimed, traces_for
from evalathan.subject import Subject


def _run_world(world: World, subject: Subject, prior: list[Cell] | None = None) -> Cell:
    hits = traces_for(subject, world)
    if world.deferred_v2:
        by_name = {cell.agent: cell for cell in (prior or [])}
        kepler = by_name.get("Keplerly")
        galileo = by_name.get("Galileoly")
        ready = (
            kepler is not None
            and galileo is not None
            and kepler.status.value == "measured"
            and galileo.status.value == "measured"
            and hits
        )
        if not ready:
            return deferred(
                world.brand,
                world.gate,
                world.question,
                "Newtonly waits for v2. Keplerly and Galileoly must both show a sealed world first. The apple story is not a catalyst.",
            )
    if hits:
        return scored(
            world.brand,
            world.gate,
            world.question,
            f"Sealed {world.code} file present: {'; '.join(hits)}. v0.3 does not run the simulator. A gold medal is not awarded from the filename.",
            hits,
            passed=None,
        )
    if claimed(subject):
        extra = " This world is required when PRETRUWs ships." if world.required else ""
        return deferred(
            world.brand,
            world.gate,
            world.question,
            f"The tree claims a physical-world or discovery exam, and no sealed {world.code} world is in the folder.{extra} A blank is not a fail.",
        )
    return deferred(
        world.brand,
        world.gate,
        world.question,
        f"No sealed {world.code} world and no physical-world claim. {world.discoverer} stays off this report. A blank is not a fail.",
    )


def copernly(subject: Subject) -> Cell:
    return _run_world(WORLDS[0], subject)


def keplerly(subject: Subject) -> Cell:
    return _run_world(WORLDS[1], subject)


def galileoly(subject: Subject) -> Cell:
    return _run_world(WORLDS[2], subject)


def darwinly(subject: Subject) -> Cell:
    return _run_world(WORLDS[3], subject)


def mendly(subject: Subject) -> Cell:
    return _run_world(WORLDS[4], subject)


def einsteinly(subject: Subject) -> Cell:
    return _run_world(WORLDS[5], subject)


def newtonly(subject: Subject, prior: list[Cell]) -> Cell:
    return _run_world(WORLDS[6], subject, prior)


copernly.ACCEPTS_PRIOR = False
keplerly.ACCEPTS_PRIOR = False
galileoly.ACCEPTS_PRIOR = False
darwinly.ACCEPTS_PRIOR = False
mendly.ACCEPTS_PRIOR = False
einsteinly.ACCEPTS_PRIOR = False
newtonly.ACCEPTS_PRIOR = True

ALL = (
    copernly,
    keplerly,
    galileoly,
    darwinly,
    mendly,
    einsteinly,
    newtonly,
)
