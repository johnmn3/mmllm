#!/usr/bin/env python3
"""Build a FIM eval JSONL from in-file structural examples.

Each line is a JSON object:
    {"language": "json", "prefix": "...", "suffix": "...", "gold_middle": "..."}

The eval consumer (mmllm fim-eval) feeds each example to the model as
`<|fim_pre|>prefix<|fim_suf|>suffix<|fim_mid|>` and reports:
  - FIM-bpc:  byte-level CE on gold_middle, conditioned on prefix+suffix
  - FIM-exact: greedy decode produces gold_middle exactly?

Examples are deterministic + committed to the repo; no external download.
Cover JSON tool-call envelopes and a few Clojure / Python / generic shapes."""
from __future__ import annotations

import json
import sys
from pathlib import Path


# Each entry: (language, prefix, suffix, gold_middle)
EXAMPLES: list[tuple[str, str, str, str]] = [
    # ───── JSON tool-call envelopes ─────
    ("json",
     '<|user|>\nWhat is the weather in Paris?\n<|end|>\n<|asst|>\n{"tool_calls": [{"name": "',
     '"}]}\n<|end|>\n',
     'get_weather", "args": {"city": "Paris"}'),

    ("json",
     '<|user|>\nList /tmp\n<|end|>\n<|asst|>\n{"tool_calls": [{"name": "ls", "args": ',
     '}]}\n<|end|>\n',
     '{"path": "/tmp"}'),

    ("json",
     '<|user|>\nAdd 17 and 25\n<|end|>\n<|asst|>\n{"tool_calls": [{"name": "calculate", "args": {"expr": "',
     '"}}]}\n<|end|>\n',
     '17 + 25'),

    ("json",
     '<|user|>\nSearch books for "Pride and Prejudice"\n<|end|>\n<|asst|>\n{"tool_calls": [{',
     '}]}\n<|end|>\n',
     '"name": "search_books", "args": {"q": "Pride and Prejudice"}'),

    ("json",
     '{"items": [\n  {"id": 1, "name": "alpha"},\n  ',
     '\n]}',
     '{"id": 2, "name": "beta"}'),

    # ───── Clojure forms ─────
    ("clojure",
     '(defn fibonacci [n]\n  (if (< n 2)\n    n\n    (+ ',
     ')))\n',
     '(fibonacci (- n 1)) (fibonacci (- n 2))'),

    ("clojure",
     '(defn factorial [n]\n  (loop [i 1 acc 1]\n    (if (> i n)\n      acc\n      ',
     ')))\n',
     '(recur (inc i) (* acc i))'),

    ("clojure",
     '(ns my.ns\n  (:require [clojure.string :as ',
     ']))\n',
     'str'),

    # ───── Python ─────
    ("python",
     'def reverse_list(xs):\n    result = []\n    for x in xs:\n        ',
     '\n    return result\n',
     'result.insert(0, x)'),

    ("python",
     'class Counter:\n    def __init__(self):\n        self.n = 0\n\n    def inc(self):\n        ',
     '\n\n    def get(self):\n        return self.n\n',
     'self.n += 1'),

    # ───── Generic — narrative continuation ─────
    ("generic",
     'The fox saw the grapes hanging on the vine. He jumped many times to seize them, but ',
     '. "They are sour anyway," he said.\n',
     'failed each leap'),
]


def main() -> None:
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/mmllm-cpu/fim-eval.jsonl")
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w") as f:
        for lang, prefix, suffix, gold in EXAMPLES:
            row = {
                "language": lang,
                "prefix": prefix,
                "suffix": suffix,
                "gold_middle": gold,
            }
            f.write(json.dumps(row) + "\n")
    print(f"wrote {len(EXAMPLES)} FIM eval examples → {out}")


if __name__ == "__main__":
    main()
