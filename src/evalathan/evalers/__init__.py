"""Sixteen evalers. Hydra is not in this list."""

from evalathan.evalers import (
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
    tokely,
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
    tokely,
    pressly,
    triadly,
    chorely,
    trajectly,
    warrantly,
    domly,
    stackly,
)

assert len(ALL) == 16
