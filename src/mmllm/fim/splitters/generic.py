"""Random byte-offset split-point picker — language-agnostic baseline."""

import random
from typing import Optional


def split(doc: bytes, rng: random.Random,
          *, min_middle: int = 8, max_middle: int = 256) -> Optional[tuple[int, int]]:
    """Pick i, j ∈ [0, len(doc)] uniformly at random with j-i in
    [min_middle, max_middle]. Returns None if doc is too short."""
    L = len(doc)
    if L < min_middle + 4:
        return None
    middle_len = rng.randint(min_middle, min(max_middle, L - 2))
    i = rng.randint(0, L - middle_len)
    return (i, i + middle_len)
