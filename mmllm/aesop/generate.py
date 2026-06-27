"""Aesop capstone corpus generator + math verifier + byte-bin writer.

Pipeline:

  1. Roll seeds → produce records via the fable registry
  2. Render each record through ChatTemplate (sys + user + asst turns)
  3. Math-verify: re-evaluate the embedded Clojure tree, check the tool-call
     answer matches (catches any template bugs that drift from expr)
  4. Dedupe by full-record hash
  5. Concatenate with `\n\n` separators (mirrors prepare_hf_dataset)
  6. Optional split into train / val / test via split_pile_github

Output layout matches the existing trainer convention so the byte-bin
file is a drop-in for `--mix`:

  <out_path>             flat byte stream
  <out_path>.train.bin
  <out_path>.val.bin
  <out_path>.test.bin
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import os
import random
import time
from collections import Counter
from pathlib import Path

from mmllm.aesop.fables   import GENERATORS, smoke_test as _fables_smoke
from mmllm.aesop.template import Record, Scene
from mmllm.datasets       import DEFAULT_TEMPLATE, ChatTemplate


# ─────────────────────── render ───────────────────────


def render_record(rec: Record, tpl: ChatTemplate = DEFAULT_TEMPLATE) -> str:
    """Render a Record as a chat-template-wrapped string. Same shape as
    every other formatter in mmllm.datasets — sys + user + asst turns
    each closed with `\\n<|end|>\\n`."""
    return (tpl.system(rec.system_msg)
            + tpl.user(rec.user_msg)
            + tpl.assistant(rec.assistant_msg))


# ─────────────────────── verify ───────────────────────


def verify_record(rec: Record) -> None:
    """Re-check the record's invariants under the eval-first design.

    Every record's last tool call is either:
      - eval(form):    a Clojure-source string. Verify it matches the
                       record's `code_str` byte-for-byte (so the eval
                       form === the form rendered by emit_clojure_inline
                       on the chapter's expr tree).
      - answer(value): the chapter's verdict. Verify the value matches
                       `rec.expected`.

    Critical: the assistant_msg must NOT contain the numeric answer
    anywhere outside the tool call's args (no `;=> N`, no "the answer
    is N", no result_text with the value spelled out). The eval-first
    design is built specifically to avoid that leakage.
    """
    if not rec.tool_calls:
        raise ValueError("no tool_calls")

    last = rec.tool_calls[-1]
    if last["name"] == "eval":
        form = last["args"].get("form", "")
        if not form.startswith("("):
            raise ValueError(f"eval form not a Clojure form: {form[:40]!r}")
        if form != rec.code_str:
            raise ValueError(
                f"eval form != code_str:\n  form     = {form!r}\n"
                f"  code_str = {rec.code_str!r}"
            )
    elif last["name"] == "answer":
        last_args = last["args"]
        if not _value_in_args(rec.expected, last_args):
            raise ValueError(
                f"answer mismatch: expected={rec.expected!r}  args={last_args!r}"
            )
    else:
        raise ValueError(f"unknown last tool: {last['name']!r}")

    # The chat template delimiters all appear correctly in the rendered text.
    rendered = render_record(rec)
    if "<|sys|>" not in rendered:  raise ValueError("no <|sys|> in rendered")
    if "<|user|>" not in rendered: raise ValueError("no <|user|> in rendered")
    if "<|asst|>" not in rendered: raise ValueError("no <|asst|> in rendered")
    # Three end markers expected (one per turn).
    n_end = rendered.count("<|end|>")
    if n_end < 3:
        raise ValueError(f"expected ≥3 <|end|>, got {n_end}")

    # 4. The body that comes IMMEDIATELY after the last <|asst|> opener
    #    must start with a letter or `{` — never whitespace (the bug we
    #    were chasing in v2). This is what the eval extractor sees.
    asst_open = "<|asst|>\n"
    idx = rendered.rfind(asst_open)
    body = rendered[idx + len(asst_open):]
    if not body or body[0] in (" ", "\t", "\n"):
        raise ValueError(
            f"asst body starts with whitespace ({body[:30]!r}) — "
            "would teach degenerate format"
        )


def _value_in_args(expected, args: dict) -> bool:
    """Relaxed equality: bool ↔ 'yes'/'no', list members, scalar match."""
    for v in args.values():
        if v == expected:
            return True
        if isinstance(v, str) and isinstance(expected, bool):
            if v == "yes" and expected:
                return True
            if v == "no" and not expected:
                return True
    return False


# ─────────────────────── corpus generator ───────────────────────


def generate_corpus(out_path: str | os.PathLike,
                    n_records:  int  = 10_000,
                    seed:       int  = 0,
                    val_bytes:  int  = 5_000_000,
                    test_bytes: int  = 5_000_000,
                    do_split:   bool = True,
                    fable_weights: dict[str, float] | None = None,
                    verbose:    bool = True,
                    ) -> dict:
    """Generate `n_records` records, write to `out_path`, optionally split.

    `fable_weights` controls the per-fable sample probability. Default is
    uniform over all registered fables. Pass e.g. {"tortoise-hare": 0.5,
    "crow-pitcher": 0.3, "goose-eggs": 0.2} to skew.
    """
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    fables = list(GENERATORS.items())
    if fable_weights:
        weights = [fable_weights.get(name, 0.0) for name, _ in fables]
    else:
        weights = [1.0] * len(fables)

    rng = random.Random(seed)
    seen_hashes: set[str] = set()
    fable_counts:   Counter = Counter()
    chapter_counts: Counter = Counter()
    n_collisions = 0
    n_verify_fail = 0
    n_written     = 0
    bytes_written = 0

    sep = b"\n\n"
    t0 = time.time()
    if verbose:
        print(f"  aesop generate → {out_path}  (target n={n_records}, seed={seed})",
              flush=True)

    with open(out, "wb") as fout:
        attempt = 0
        while n_written < n_records:
            attempt += 1
            scene = Scene(rng=rng)
            (fable_name, gen) = rng.choices(fables, weights=weights, k=1)[0]
            try:
                rec = gen(scene)
            except Exception as e:
                if verbose and n_verify_fail < 5:
                    print(f"    skip (gen err): {fable_name}: {e}", flush=True)
                n_verify_fail += 1
                continue
            try:
                verify_record(rec)
            except Exception as e:
                if verbose and n_verify_fail < 5:
                    print(f"    skip (verify): {fable_name}/{rec.chapter}: {e}",
                          flush=True)
                n_verify_fail += 1
                continue
            rendered = render_record(rec)
            buf = rendered.encode("utf-8", errors="replace")
            h = hashlib.sha1(buf).hexdigest()
            if h in seen_hashes:
                n_collisions += 1
                if attempt > n_records * 4:
                    if verbose:
                        print(f"    too many collisions; stopping early at "
                              f"{n_written}/{n_records}", flush=True)
                    break
                continue
            seen_hashes.add(h)
            fout.write(buf + sep)
            bytes_written += len(buf) + len(sep)
            fable_counts[rec.fable] += 1
            chapter_counts[f"{rec.fable}/{rec.chapter}"] += 1
            n_written += 1
            if verbose and n_written % 5000 == 0:
                rate = n_written / (time.time() - t0 + 1e-9)
                print(f"    {n_written}/{n_records} ({rate:.0f} rec/s) "
                      f"{_h(bytes_written)} written", flush=True)

    elapsed = time.time() - t0
    print(f"  done: {n_written} records / {_h(bytes_written)} in "
          f"{elapsed:.1f}s ({n_written/elapsed:.0f} rec/s)  "
          f"[{n_collisions} dedup collisions, {n_verify_fail} verify fails]",
          flush=True)

    splits = None
    if do_split:
        from mmllm.corpus import split_pile_github
        splits = split_pile_github(str(out), val_bytes, test_bytes)
        if verbose:
            print(f"  splits: {splits}", flush=True)

    return {
        "out_path":      str(out),
        "n_records":     n_written,
        "bytes":         bytes_written,
        "n_collisions":  n_collisions,
        "n_verify_fail": n_verify_fail,
        "fable_counts":  dict(fable_counts),
        "chapter_counts": dict(chapter_counts),
        "elapsed_s":     elapsed,
        "splits":        splits,
    }


# ─────────────────────── helpers ───────────────────────


def _h(b: int) -> str:
    """Pretty bytes."""
    if b < 1024:
        return f"{b}B"
    if b < 1024 * 1024:
        return f"{b/1024:.1f}KB"
    if b < 1024 * 1024 * 1024:
        return f"{b/1024/1024:.1f}MB"
    return f"{b/1024/1024/1024:.2f}GB"


# ─────────────────────── self-test ───────────────────────


def smoke_test(seed: int = 0) -> None:
    """Generate 200 records to a tmp file; sanity-check splits + math."""
    import tempfile

    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "aesop.bin"
        stats = generate_corpus(
            str(out),
            n_records=200,
            seed=seed,
            val_bytes=10_000,
            test_bytes=10_000,
            do_split=True,
            verbose=False,
        )
    assert stats["n_records"] >= 180, f"too few records: {stats}"
    assert stats["n_verify_fail"] == 0, (
        f"verify failures: {stats['n_verify_fail']}"
    )
    assert sum(stats["fable_counts"].values()) == stats["n_records"]
    print(
        f"generate smoke OK: {stats['n_records']} recs, "
        f"{_h(stats['bytes'])}, fables={stats['fable_counts']}, "
        f"{stats['n_collisions']} collisions"
    )


# ─────────────────────── curriculum corpus ───────────────────────


CURRICULUM_FABLES = (
    "tortoise_hare", "crow_pitcher", "milkmaid", "boy_wolf", "dog_shadow",
)


def generate_curriculum_corpus(
    out_path:        str | os.PathLike,
    n_per_example:   int  = 200,
    seed:            int  = 0,
    val_bytes:       int  = 50_000_000,
    test_bytes:     int  = 50_000_000,
    do_split:        bool = True,
    fables:          tuple = CURRICULUM_FABLES,
    grades:          tuple = tuple(range(1, 13)),
    verbose:         bool = True,
) -> dict:
    """Walk every (fable, grade, subject, example) in the K-12 Clojure
    curriculum and write `n_per_example` records to a byte-bin.

    Output layout matches `generate_corpus` (the classic-fable
    generator) so the byte-bin is a drop-in for `--mix`:

      <out_path>           flat byte stream
      <out_path>.train.bin
      <out_path>.val.bin
      <out_path>.test.bin

    Each record is rendered through DEFAULT_TEMPLATE (sys + user +
    asst, with `\\n<|end|>\\n` closers) — same shape as every other
    formatter in mmllm.datasets.

    Default coverage (5 fables × 12 grades × ~20 subjects × ~5
    examples × 200 records ≈ 1.2M records ≈ ~600 MB byte-bin) is
    sized to fill the 60% fable share of a 1B-token training run.
    Bump `n_per_example` for larger corpora.
    """
    import importlib

    from mmllm.aesop.curriculum.generator import generate_subject

    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    rng = random.Random(seed)
    seen_hashes: set[str] = set()
    fable_counts:   Counter = Counter()
    chapter_counts: Counter = Counter()
    n_collisions = 0
    n_verify_fail = 0
    n_written     = 0
    bytes_written = 0

    sep = b"\n\n"
    t0 = time.time()
    if verbose:
        print(f"  curriculum generate → {out_path}",
              flush=True)
        print(f"    fables={list(fables)}  grades={list(grades)}  "
              f"n_per_example={n_per_example}  seed={seed}",
              flush=True)

    with open(out, "wb") as fout:
        for fable in fables:
            for grade in grades:
                try:
                    mod = importlib.import_module(
                        f"mmllm.aesop.curriculum.{fable}.grade_{grade}")
                except ImportError:
                    continue
                subjects = getattr(mod, "SUBJECTS", {})
                for sid, sub in subjects.items():
                    seed_for_subject = seed + hash((fable, sid)) % (2**31)
                    try:
                        recs = generate_subject(
                            sub, n_per_example=n_per_example,
                            seed=seed_for_subject)
                    except Exception as e:
                        n_verify_fail += 1
                        if verbose and n_verify_fail < 5:
                            print(f"    skip (gen err): {fable}/{sid}: {e}",
                                  flush=True)
                        continue
                    for rec in recs:
                        rendered = render_record(rec)
                        buf = rendered.encode("utf-8", errors="replace")
                        h = hashlib.sha1(buf).hexdigest()
                        if h in seen_hashes:
                            n_collisions += 1
                            continue
                        seen_hashes.add(h)
                        fout.write(buf + sep)
                        bytes_written += len(buf) + len(sep)
                        fable_counts[rec.fable] += 1
                        chapter_counts[f"{rec.fable}/{rec.chapter}"] += 1
                        n_written += 1
                        if verbose and n_written % 10000 == 0:
                            rate = n_written / (time.time() - t0 + 1e-9)
                            print(f"    {n_written} records "
                                  f"({rate:.0f} rec/s) "
                                  f"{_h(bytes_written)} written",
                                  flush=True)

    elapsed = time.time() - t0
    print(f"  done: {n_written} records / {_h(bytes_written)} in "
          f"{elapsed:.1f}s ({n_written/max(elapsed,1e-9):.0f} rec/s)  "
          f"[{n_collisions} dedup collisions, {n_verify_fail} gen fails]",
          flush=True)

    splits = None
    if do_split:
        from mmllm.corpus import split_pile_github
        splits = split_pile_github(str(out), val_bytes, test_bytes)
        if verbose:
            print(f"  splits: {splits}", flush=True)

    return {
        "out_path":      str(out),
        "n_records":     n_written,
        "bytes":         bytes_written,
        "n_collisions":  n_collisions,
        "n_verify_fail": n_verify_fail,
        "fable_counts":  dict(fable_counts),
        "chapter_counts": dict(chapter_counts),
        "elapsed_s":     elapsed,
        "splits":        splits,
    }


# ─────────────────────── CLI ───────────────────────


def _main() -> int:
    p = argparse.ArgumentParser(description="Generate aesop capstone corpus.")
    p.add_argument("--out", help="output .bin path (required unless --smoke / --inspect)")
    p.add_argument("--n", type=int, default=10000)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--val-bytes", type=int, default=5_000_000)
    p.add_argument("--test-bytes", type=int, default=5_000_000)
    p.add_argument("--no-split", action="store_true")
    p.add_argument("--smoke", action="store_true",
                   help="run module smoke instead of generating")
    p.add_argument("--inspect", type=int, default=0,
                   help="dump N rendered records to stdout for review")
    # Curriculum mode (K-12 Clojure curriculum across 5 fables).
    p.add_argument("--curriculum", action="store_true",
                   help="generate the K-12 curriculum corpus (5 fables × "
                        "12 grades) instead of the classic-fable mix; "
                        "uses --n as n_per_example")
    args = p.parse_args()
    if args.smoke:
        _fables_smoke()
        smoke_test()
        return 0
    if args.inspect:
        rng = random.Random(args.seed)
        fables = list(GENERATORS.values())
        for i in range(args.inspect):
            scene = Scene(rng=rng)
            rec = rng.choice(fables)(scene)
            print(f"=== record {i+1} ({rec.fable}/{rec.chapter}) ===")
            print(render_record(rec))
            print()
        return 0
    if not args.out:
        p.error("--out is required (unless --smoke or --inspect)")
        return 2
    if args.curriculum:
        stats = generate_curriculum_corpus(
            out_path=args.out,
            n_per_example=args.n,
            seed=args.seed,
            val_bytes=args.val_bytes,
            test_bytes=args.test_bytes,
            do_split=not args.no_split,
        )
    else:
        stats = generate_corpus(
            out_path=args.out,
            n_records=args.n,
            seed=args.seed,
            val_bytes=args.val_bytes,
            test_bytes=args.test_bytes,
            do_split=not args.no_split,
        )
    print(json.dumps(stats, indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
