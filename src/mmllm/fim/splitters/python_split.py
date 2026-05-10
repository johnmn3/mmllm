"""Python-aware FIM split points.

Splits at function-def, class-def, or blank-line boundaries. Heuristic
— doesn't tokenize Python; just looks for indented blocks separated by
blank lines and emits candidate splits between them."""

import random
import re
from typing import Optional


_DEF_PATTERN = re.compile(rb'^\s*(?:def|class|async def)\s', re.MULTILINE)


def _block_boundaries(doc: bytes) -> list[tuple[int, int]]:
    """Find roughly-balanced Python blocks. Heuristic:
    blocks start at `def`/`class`/`async def` lines, end at next
    same-indent def/class or end of doc. Returns (start, end) byte
    offsets per block."""
    matches = list(_DEF_PATTERN.finditer(doc))
    if len(matches) < 2:
        return []
    boundaries = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(doc)
        boundaries.append((start, end))
    return boundaries


def split(doc: bytes, rng: random.Random,
          *, min_middle: int = 8, max_middle: int = 256) -> Optional[tuple[int, int]]:
    cands = _block_boundaries(doc)
    cands = [(s, e) for (s, e) in cands if min_middle <= (e - s) <= max_middle]
    if not cands:
        return None
    return rng.choice(cands)
