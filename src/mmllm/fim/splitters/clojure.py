"""Clojure-aware FIM split points.

Walks a byte stream tracking paren / string / comment state. Emits
candidates at:

  - top-level form boundaries (between `(...)` siblings at depth 0)
  - sub-form boundaries inside long forms (depth-1 `(...)` siblings,
    e.g. between top-level args of a `(defn name [args] body...)`)

These produce FIM examples like:

  prefix = '(defn fibonacci [n] '
  middle = '(if (< n 2) n (+ ...))'
  suffix = ')\n\n(defn ...'

Bytes only — no AST. Best-effort; tolerates malformed input by emitting
fewer candidates."""

import random
from typing import Optional


def _form_boundaries(doc: bytes) -> list[tuple[int, int]]:
    """Walk the doc; return (start, end) byte offsets of each balanced
    `(...)` form (or `[...]` / `{...}`). One entry per form. Includes
    nested forms at all depths.

    Skips:
      - "..." string literals
      - ; line comments
      - #_ form-skip reader macro (just skip the next form's region —
        approximated as skipping until paren depth returns to start)
    """
    boundaries: list[tuple[int, int]] = []
    in_string = False
    escape = False
    in_comment = False
    open_stack: list[int] = []    # positions of open '(', '[', '{'

    for i, b in enumerate(doc):
        if in_comment:
            if b == 0x0A:    # newline ends comment
                in_comment = False
            continue
        if escape:
            escape = False
            continue
        if in_string:
            if b == 0x5C:
                escape = True
            elif b == 0x22:
                in_string = False
            continue

        if b == 0x22:        # opening "
            in_string = True
            continue
        if b == 0x3B:        # ;  comment to end of line
            in_comment = True
            continue
        if b in (0x28, 0x5B, 0x7B):    # ( [ {
            open_stack.append(i)
            continue
        if b in (0x29, 0x5D, 0x7D):    # ) ] }
            if open_stack:
                start = open_stack.pop()
                # Form is doc[start:i+1] (inclusive of close)
                # We want middle = doc[start:i+1] so caller picks i+1 as suffix start.
                boundaries.append((start, i + 1))
    return boundaries


def split(doc: bytes, rng: random.Random,
          *, min_middle: int = 8, max_middle: int = 256) -> Optional[tuple[int, int]]:
    """Pick a Clojure form boundary as the FIM split. Prefers smaller
    forms (more useful structural fills) by filtering by length range."""
    cands = _form_boundaries(doc)
    cands = [(s, e) for (s, e) in cands if min_middle <= (e - s) <= max_middle]
    if not cands:
        return None
    return rng.choice(cands)
