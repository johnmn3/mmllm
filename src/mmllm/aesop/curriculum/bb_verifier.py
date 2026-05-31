"""Babashka subprocess verifier for macro / host-interop forms.

Forms that the in-process expr.py evaluator can't handle (defmacro,
defprotocol, deftype, atom/swap!, host-method calls, metadata,
core.async, namespace machinery) get a one-time pre-flight check at
curriculum-build time: we shell out to bb, evaluate the form, and
confirm the bb output matches the authored `expected`.

This runs ONCE per legacy form at build time, not per record at
generation time, so the cost is minimal — ~80 forms × ~50ms each
= ~4 seconds total per build.

Cache: results memoized in `~/.mmllm/bb_verify_cache.json` keyed by
(form, expected). Repeated builds re-use the cache; only forms whose
text changed re-run through bb.

Usage:
    from mmllm.aesop.curriculum.bb_verifier import verify_with_bb
    ok = verify_with_bb(form_str, expected)   # bool
"""
from __future__ import annotations

import json
import os
import subprocess
import shutil
from pathlib import Path
from typing import Any


_BB_CACHE_PATH = Path.home() / ".mmllm" / "bb_verify_cache.json"
_BB_TIMEOUT_SECS = 10


def _bb_path() -> str | None:
    """Find bb on PATH; return path or None if not installed."""
    p = shutil.which("bb")
    if p:
        return p
    # Common fallback location used by curriculum-build scripts
    fallback = "/tmp/bb-bin/bb"
    if Path(fallback).is_file() and os.access(fallback, os.X_OK):
        return fallback
    return None


def _load_cache() -> dict:
    if not _BB_CACHE_PATH.exists():
        return {}
    try:
        return json.loads(_BB_CACHE_PATH.read_text())
    except Exception:
        return {}


def _save_cache(cache: dict) -> None:
    _BB_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    try:
        _BB_CACHE_PATH.write_text(json.dumps(cache, indent=2))
    except Exception:
        pass  # cache is best-effort; never crash the build


def _cache_key(form_str: str, expected: Any) -> str:
    """Stable cache key: form text + repr(expected)."""
    return f"{form_str}\x00{repr(expected)}"


def _bb_eval(bb_bin: str, form_str: str) -> tuple[bool, str]:
    """Run bb -e <form> and return (success, output). Output is
    str-ified so the caller can compare to expected."""
    try:
        result = subprocess.run(
            [bb_bin, "-e", form_str],
            capture_output=True,
            text=True,
            timeout=_BB_TIMEOUT_SECS,
        )
    except subprocess.TimeoutExpired:
        return False, f"<bb-timeout: {_BB_TIMEOUT_SECS}s>"
    except Exception as e:
        return False, f"<bb-launch-error: {e}>"
    if result.returncode != 0:
        return False, f"<bb-error: {result.stderr.strip()[:120]}>"
    return True, result.stdout.strip()


def _bb_output_matches(bb_out: str, expected: Any) -> bool:
    """Compare bb's textual stdout to a Python `expected` value.
    bb prints Clojure literals; we parse + evaluate both and compare
    the values via expr.py's value system.

    Falls back to text comparison when parsing fails (e.g. for prints
    of unsupported types like fn references)."""
    from mmllm.aesop.curriculum.form_parser import parse, ParseError, UnsupportedForm
    from mmllm.aesop.expr import evaluate

    # bb prints nil as the empty string. Normalize.
    if bb_out == "":
        return expected is None

    # Wrap bb_out so a bare list `(1 2 3)` parses as a data list rather
    # than a function call. We force the data-list interpretation by
    # quoting it.
    candidates = [bb_out]
    if bb_out.startswith("(") and not bb_out.startswith("(quote"):
        candidates.append(f"(quote {bb_out})")

    for cand in candidates:
        try:
            ast = parse(cand)
            got = evaluate(ast)
        except (ParseError, UnsupportedForm, Exception):
            continue
        if _values_equal(got, expected):
            return True
    # Text-fallback: quoted strings, keywords, simple literals
    expected_lit = _expected_to_clojure_lit(expected)
    return (bb_out == expected_lit
            or bb_out.replace(" ", "") == expected_lit.replace(" ", ""))


def _values_equal(a: Any, b: Any) -> bool:
    """Tolerant equality across keyword/sym/list/dict normalizations."""
    from fractions import Fraction
    if isinstance(a, str) and a.startswith(":"):
        a = ("__kw__", a[1:])
    if isinstance(b, str) and b.startswith(":"):
        b = ("__kw__", b[1:])
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(
            _values_equal(x, y) for x, y in zip(a, b))
    if isinstance(a, dict) and isinstance(b, dict):
        an = {_norm_key(k): v for k, v in a.items()}
        bn = {_norm_key(k): v for k, v in b.items()}
        if set(an) != set(bn): return False
        return all(_values_equal(an[k], bn[k]) for k in an)
    if isinstance(a, Fraction) and isinstance(b, str) and "/" in b:
        n, d = b.split("/")
        return a == Fraction(int(n), int(d))
    return a == b


def _norm_key(k: Any) -> Any:
    if isinstance(k, str) and k.startswith(":"):
        return ("__kw__", k[1:])
    return k


def _expected_to_clojure_lit(value: Any) -> str:
    """Render Python value as Clojure source so we can compare to bb
    stdout (which prints values as Clojure literals)."""
    from mmllm.aesop.expr import _emit_value
    if isinstance(value, str) and value.startswith(":"):
        return value
    if isinstance(value, tuple) and len(value) == 2 and value[0] == "__kw__":
        return f":{value[1]}"
    if isinstance(value, tuple) and len(value) == 2 and value[0] == "__sym__":
        return value[1]
    return _emit_value(value)


def verify_with_bb(form_str: str,
                   expected: Any,
                   *,
                   strict: bool = False) -> bool | None:
    """Evaluate `form_str` via bb subprocess and check against expected.

    Returns:
        True   — bb's output matches expected
        False  — bb's output disagrees with expected
        None   — bb is not installed (skip; caller falls back to
                 trusting authored expected)

    With `strict=True`, failures raise a RuntimeError instead of
    returning False.
    """
    bb = _bb_path()
    if bb is None:
        return None
    cache = _load_cache()
    key = _cache_key(form_str, expected)
    if key in cache:
        return cache[key]
    ok, out = _bb_eval(bb, form_str)
    if not ok:
        if strict:
            raise RuntimeError(f"bb-verify failed: {form_str!r} → {out}")
        cache[key] = False
        _save_cache(cache)
        return False
    matched = _bb_output_matches(out, expected)
    cache[key] = matched
    _save_cache(cache)
    if not matched and strict:
        raise RuntimeError(
            f"bb-verify mismatch: {form_str!r}\n"
            f"  bb output: {out!r}\n"
            f"  expected:  {expected_lit!r}")
    return matched


def verify_legacy_corpus_via_bb(*, max_forms: int = 0) -> dict:
    """Walk every legacy (form_template-empty) example across the 5
    Phase-C-complete fables and run each through bb. Returns a stats
    dict; failures are listed at the bottom.

    `max_forms=0` means no limit. Use 100 for a quick smoke run.
    """
    import importlib
    fables = ["tortoise_hare", "crow_pitcher", "milkmaid", "boy_wolf", "dog_shadow"]
    out = {"checked": 0, "passed": 0, "failed": 0, "skipped_no_bb": 0,
           "fails": []}
    bb = _bb_path()
    if bb is None:
        out["skipped_no_bb"] = -1
        return out

    for fable in fables:
        for grade in range(1, 13):
            try:
                mod = importlib.import_module(
                    f"mmllm.aesop.curriculum.{fable}.grade_{grade}")
            except ImportError:
                continue
            for sid, sub in getattr(mod, "SUBJECTS", {}).items():
                for i, ex in enumerate(sub.examples):
                    if ex.form_template:
                        continue  # already parametric, skip
                    if not ex.form:
                        continue
                    if max_forms and out["checked"] >= max_forms:
                        return out
                    res = verify_with_bb(ex.form, ex.expected)
                    out["checked"] += 1
                    if res is True:
                        out["passed"] += 1
                    elif res is False:
                        out["failed"] += 1
                        if len(out["fails"]) < 12:
                            out["fails"].append((fable, sid, i, ex.form[:80]))
    return out


# ─────────────────────── self-test ───────────────────────


def smoke_test() -> None:
    bb = _bb_path()
    if bb is None:
        print("bb_verifier.py smoke_test: skipped (bb not installed)")
        return
    cases = [
        ("(+ 1 2 3)",                  6),
        ('(str "a" "b" "c")',         "abc"),
        ("(let [x 5] (* x x))",       25),
        ("(map inc [1 2 3])",         [2, 3, 4]),
    ]
    ok = 0
    for form, expected in cases:
        result = verify_with_bb(form, expected)
        if result:
            ok += 1
        else:
            print(f"  fail: {form!r} → expected {expected!r}, got bb result {result!r}")
    print(f"bb_verifier.py smoke_test: {ok}/{len(cases)} ok")


if __name__ == "__main__":
    smoke_test()
