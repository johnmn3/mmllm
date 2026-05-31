"""Per-language split-point pickers for FIM corpus generation.

A splitter is a callable `(doc: bytes, rng: Random) -> (i, j)` that
returns prefix-end (i) and suffix-start (j) byte offsets, so:
    prefix = doc[:i]
    middle = doc[i:j]
    suffix = doc[j:]

Returns None if the document doesn't have a sensible structural split.
The corpus generator falls back to the generic splitter in that case."""

from typing import Callable, Optional, Protocol
import random

import mmllm.fim.splitters.generic as generic
import mmllm.fim.splitters.json_split as json_split
import mmllm.fim.splitters.clojure as clojure
import mmllm.fim.splitters.python_split as python_split


class Splitter(Protocol):
    def __call__(self, doc: bytes, rng: random.Random) -> Optional[tuple[int, int]]: ...


# Registry — keyed by language name. Operator picks via CLI flag.
SPLITTERS: dict[str, Splitter] = {
    "generic": generic.split,
    "json":    json_split.split,
    "clojure": clojure.split,
    "python":  python_split.split,
}


def get(name: str) -> Splitter:
    """Look up a splitter by name. Falls back to 'generic' if unknown."""
    return SPLITTERS.get(name, generic.split)
