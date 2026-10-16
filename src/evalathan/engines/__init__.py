"""Sixteen scoring engines. Hydra is not in this list."""

from evalathan.engines import (
    archly,
    chorely,
    codely,
    devly,
    domly,
    levi,
    menschly,
    mixly,
    pressly,
    refactorly,
    runly,
    stackly,
    tokly,
    trajectly,
    triadly,
    warrantly,
)

ALL = (
    devly,
    archly,
    codely,
    refactorly,
    mixly,
    runly,
    levi,
    menschly,
    tokly,
    pressly,
    triadly,
    chorely,
    trajectly,
    warrantly,
    domly,
    stackly,
)

assert len(ALL) == 16
