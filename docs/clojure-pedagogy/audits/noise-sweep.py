"""Sweep noise from tortoise-hare curriculum.

Mechanical rewrites for the highest-impact issues found during spot-check:

1. question_what redundancy: "the value the form X evaluates to" — when
   wrapped by "Write a form whose evaluation gives X" produces meta-meta
   prose. Replace with "the value of X".

2. Trailing parenthetical commentary: concept_phrases / question_whats
   often carry pedagogical asides like "(note: it prints, but returns nil)"
   or "(the REPL returns it; doesn't 'print' it)". These bloat the rendered
   text without adding signal to the model. Strip them.

3. Trailing em-dash commentary: "the form X — note: returns last truthy".
   Same problem. Strip.

Skipping non-mechanical issues (concept_phrase abstractness mismatch,
plan-pool mismatches) — those require per-subject judgment.
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path("/home/user/mmllm/src/mmllm/aesop/curriculum/tortoise_hare")


def rewrite(text: str) -> tuple[str, int]:
    n = 0

    # 1. question_what redundancy
    text, k = re.subn(
        r'"the value the form ([^"]+) evaluates to"',
        r'"the value of \1"', text)
    n += k

    # 2. Strip trailing parenthetical commentary from quoted phrases.
    #    Pattern: "the X (commentary…)" → "the X"
    #    We only strip if the parenthetical is at the END, not the form's
    #    own parens (those are inside the X).
    text, k = re.subn(
        r'"((?:the [a-z][a-z\- ]+|what [^"]+|the result of [^"]+|the value of [^"]+)) '
        r'\((?:note|returns|the REPL|first truthy|empty string|the comment is)[^)"]*\)"',
        r'"\1"', text)
    n += k

    # 3. Strip trailing em-dash commentary similarly.
    text, k = re.subn(
        r'"((?:the [a-z][a-z\- ]+|what [^"]+|the result of [^"]+|the value of [^"]+)) '
        r'— note: [^"]+"',
        r'"\1"', text)
    n += k

    # 4. Strip trailing "(note: …)" tightly bound to a form.
    text, k = re.subn(
        r'"(the form \([^()"]*(?:\([^()"]*\)[^()"]*)*\)) \([^)"]+\)"',
        r'"\1"', text)
    n += k

    # 5. concept_phrase: "the form X" + "(returns the last truthy value)" cleanup.
    text, k = re.subn(
        r'"((?:the value of|the form) [^"]+?) \((?:returns|note|the REPL)[^)"]*\)"',
        r'"\1"', text)
    n += k

    return text, n


def sweep():
    total = 0
    for grade in range(1, 13):
        p = ROOT / f"grade_{grade}.py"
        if not p.exists(): continue
        before = p.read_text()
        after, k = rewrite(before)
        if k:
            p.write_text(after)
            total += k
            print(f"  {p.name}: {k} replacements")
    print(f"total: {total}")


if __name__ == "__main__":
    sweep()
