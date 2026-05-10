#!/usr/bin/env python3
"""Build a tiny corpus pack for community CPU training.

Produces three byte-level .bin files (train/val/test) at the given
prefix, totaling a few hundred KB to a few MB. The corpus mixes:

  - public-domain fables (Aesop / similar) for narrative structure
  - synthetic minimal JSON tool-call snippets (structure exemplars)
  - synthetic Python snippets

Output:
  <prefix>.train.bin   uint8 byte stream
  <prefix>.val.bin     uint8 byte stream
  <prefix>.test.bin    uint8 byte stream

The corpus is generated from in-file string templates so it's
deterministic and committable (no external download required).

Usage:
    python scripts/build_community_corpus.py /tmp/mmllm-cpu/corpus
"""
from __future__ import annotations

import os
import random
import sys
from pathlib import Path

# ── seed strings (public domain / trivially-licensed) ─────────────

FABLES = [
    "The Fox and the Grapes\n"
    "A hungry fox saw bunches of grapes hanging from a tall vine. "
    "He jumped many times to seize them, but failed each leap. "
    "At last he gave up and walked away. \"They are sour anyway,\" he said.\n",

    "The Tortoise and the Hare\n"
    "A hare laughed at a tortoise for being slow. The tortoise replied, "
    "\"Let us race.\" The hare took a nap, sure he could win. "
    "The tortoise plodded on and crossed the finish line first. "
    "Slow and steady wins the race.\n",

    "The Crow and the Pitcher\n"
    "A thirsty crow found a pitcher with water at the bottom. "
    "Its beak could not reach. The crow dropped pebbles into the pitcher "
    "until the water rose enough to drink. Necessity is the mother of "
    "invention.\n",

    "The Boy Who Cried Wolf\n"
    "A shepherd boy bored at his post cried \"Wolf!\" twice for fun, "
    "and the villagers came running. When at last a wolf truly came, "
    "he cried again, but no one believed him. A liar is not believed even "
    "when he tells the truth.\n",

    "The Lion and the Mouse\n"
    "A lion caught a mouse in his paw. The mouse begged for its life and "
    "the lion let it go. Later the lion was caught in a hunter's net. "
    "The mouse heard him and gnawed the ropes free. Small kindnesses are "
    "remembered.\n",
]

JSON_CALLS = [
    '<|user|>\nWhat is the weather in Paris?\n<|end|>\n<|asst|>\n'
    '{"tool_calls": [{"name": "get_weather", "args": {"city": "Paris"}}]}\n'
    '<|end|>\n',

    '<|user|>\nList files in /tmp\n<|end|>\n<|asst|>\n'
    '{"tool_calls": [{"name": "ls", "args": {"path": "/tmp"}}]}\n'
    '<|end|>\n',

    '<|user|>\nSearch for "transformer architecture"\n<|end|>\n<|asst|>\n'
    '{"tool_calls": [{"name": "web_search", "args": {"query": "transformer architecture"}}]}\n'
    '<|end|>\n',

    '<|user|>\nAdd 17 and 25\n<|end|>\n<|asst|>\n'
    '{"tool_calls": [{"name": "calculate", "args": {"expr": "17 + 25"}}]}\n'
    '<|end|>\n',

    '<|user|>\nFetch the price of AAPL\n<|end|>\n<|asst|>\n'
    '{"tool_calls": [{"name": "stock_price", "args": {"symbol": "AAPL"}}]}\n'
    '<|end|>\n',

    '<|user|>\nTranslate "hello" to French\n<|end|>\n<|asst|>\n'
    '{"tool_calls": [{"name": "translate", "args": {"text": "hello", "target": "fr"}}]}\n'
    '<|end|>\n',

    '<|user|>\nRead the file readme.md\n<|end|>\n<|asst|>\n'
    '{"tool_calls": [{"name": "read_file", "args": {"path": "readme.md"}}]}\n'
    '<|end|>\n',

    '<|user|>\nSet timer for 5 minutes\n<|end|>\n<|asst|>\n'
    '{"tool_calls": [{"name": "set_timer", "args": {"minutes": 5}}]}\n'
    '<|end|>\n',
]

PYTHON_SNIPPETS = [
    "def fibonacci(n):\n"
    "    if n < 2:\n        return n\n"
    "    a, b = 0, 1\n"
    "    for _ in range(n - 1):\n        a, b = b, a + b\n"
    "    return b\n",

    "def is_prime(n):\n"
    "    if n < 2:\n        return False\n"
    "    for i in range(2, int(n ** 0.5) + 1):\n"
    "        if n % i == 0:\n            return False\n"
    "    return True\n",

    "def reverse_string(s):\n    return s[::-1]\n",

    "def factorial(n):\n"
    "    result = 1\n"
    "    for i in range(2, n + 1):\n        result *= i\n"
    "    return result\n",

    "def gcd(a, b):\n"
    "    while b:\n        a, b = b, a % b\n    return a\n",
]


def build_corpus(seed: int = 0, target_bytes: int = 2_000_000) -> bytes:
    """Tile the seed templates with random ordering until target size.
    Each template gets some natural newline padding so the model sees
    document boundaries."""
    rng = random.Random(seed)
    parts: list[bytes] = []
    total = 0
    pool = (
        [("fable", t) for t in FABLES] * 30
        + [("json", t) for t in JSON_CALLS] * 50
        + [("py", t) for t in PYTHON_SNIPPETS] * 20
    )
    while total < target_bytes:
        rng.shuffle(pool)
        for _, t in pool:
            blob = (t + "\n\n").encode("utf-8")
            parts.append(blob)
            total += len(blob)
            if total >= target_bytes:
                break
    return b"".join(parts)


def write_split(prefix: str) -> dict:
    """Generate train/val/test splits with disjoint random seeds.
    Train ~1.5 MB, val ~250 KB, test ~250 KB. Tiny on purpose —
    fits easily in any contributor's storage budget."""
    out = {}
    for split, seed, target in [
        ("train", 0, 1_500_000),
        ("val",   1,   250_000),
        ("test",  2,   250_000),
    ]:
        data = build_corpus(seed=seed, target_bytes=target)
        path = f"{prefix}.{split}.bin"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(data)
        out[split] = (path, len(data))
    return out


def main() -> None:
    prefix = sys.argv[1] if len(sys.argv) > 1 else "/tmp/mmllm-cpu/corpus"
    print(f"Building community corpus at prefix={prefix}")
    info = write_split(prefix)
    for k, (p, n) in info.items():
        print(f"  {k:5s}  {n:>10,} bytes  →  {p}")
    print("done.")


if __name__ == "__main__":
    main()
