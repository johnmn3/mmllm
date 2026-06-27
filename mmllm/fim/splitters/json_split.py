"""JSON-aware FIM split points.

Walks a byte stream tracking quote / brace / bracket state. Emits
candidate split points at *structural value boundaries*:

  - after `:` (start of a value — middle fills the value)
  - before `,` or `}` or `]` (end of a value)
  - around array elements

These produce FIM examples like:

  prefix = '{"name": "search", "args": '
  middle = '{"q": "transformers"}'
  suffix = '}\n'

Which is exactly the kind of structural fill we need the model to do
at agent-eval time. Uses a tiny hand-written state machine — no full
JSON parser. Tolerates malformed JSON (just stops yielding candidates
in that doc)."""

import random
from typing import Optional


def _value_boundaries(doc: bytes) -> list[tuple[int, int]]:
    """Walk the doc, return list of (start, end) byte offsets where each
    pair encloses a JSON 'value' (everything after `:` or array element
    up to the matching `,` / `]` / `}`).

    Truncates / skips on malformed input. Doesn't validate; just looks
    for likely value spans we can use as the FIM 'middle'."""
    boundaries: list[tuple[int, int]] = []
    in_string = False
    escape = False
    depth_stack: list[int] = []           # positions of opening brace/bracket
    candidate_starts: list[int] = []      # positions right after `:` or `,` or `[` (value start)

    for i, b in enumerate(doc):
        if escape:
            escape = False
            continue
        if in_string:
            if b == 0x5C:        # backslash
                escape = True
            elif b == 0x22:      # closing quote
                in_string = False
            continue

        if b == 0x22:            # opening quote
            in_string = True
            continue
        if b == 0x7B or b == 0x5B:   # { or [
            depth_stack.append(i)
            if b == 0x5B:
                # array element start (skipping whitespace)
                k = i + 1
                while k < len(doc) and doc[k] in (0x20, 0x09, 0x0A, 0x0D):
                    k += 1
                candidate_starts.append(k)
            continue
        if b == 0x7D or b == 0x5D:   # } or ]
            if depth_stack:
                depth_stack.pop()
                if candidate_starts:
                    start = candidate_starts.pop()
                    if start < i:
                        boundaries.append((start, i))
            continue
        if b == 0x3A:            # ':'  → value follows
            k = i + 1
            while k < len(doc) and doc[k] in (0x20, 0x09, 0x0A, 0x0D):
                k += 1
            candidate_starts.append(k)
            continue
        if b == 0x2C:            # ','  → end of one value, start of next
            if candidate_starts:
                start = candidate_starts.pop()
                if start < i:
                    boundaries.append((start, i))
            # next value starts after the comma + whitespace
            k = i + 1
            while k < len(doc) and doc[k] in (0x20, 0x09, 0x0A, 0x0D):
                k += 1
            candidate_starts.append(k)

    return boundaries


def split(doc: bytes, rng: random.Random,
          *, min_middle: int = 4, max_middle: int = 256) -> Optional[tuple[int, int]]:
    """Pick a JSON-value boundary as the FIM split. Filters by
    middle-length range to avoid trivially-tiny middles or huge ones
    that overflow training windows."""
    cands = _value_boundaries(doc)
    cands = [(s, e) for (s, e) in cands if min_middle <= (e - s) <= max_middle]
    if not cands:
        return None
    return rng.choice(cands)
