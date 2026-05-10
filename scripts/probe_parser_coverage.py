"""Walk all 5 Phase-C-complete fables, parse every existing form,
evaluate it, and check that the answer matches the authored `expected`.

This proves (a) the parser covers the curriculum's actual syntax,
(b) expr.py's evaluator covers the semantics, and (c) all authored
answers are correct (no drift between author intent and runtime).
"""
import importlib
import sys
import traceback
from collections import defaultdict

sys.path.insert(0, "/home/user/mmllm/src")

from mmllm.aesop.curriculum.form_parser import parse, ParseError, UnsupportedForm
from mmllm.aesop.expr import evaluate


FABLES = ["tortoise_hare", "crow_pitcher", "milkmaid", "boy_wolf", "dog_shadow"]


def collect_examples():
    """Walk every grade module of every fable; yield (fable, sid, ex)."""
    out = []
    for fable in FABLES:
        for grade in range(1, 13):
            try:
                mod = importlib.import_module(
                    f"mmllm.aesop.curriculum.{fable}.grade_{grade}")
            except ImportError:
                continue
            subjects = getattr(mod, "SUBJECTS", {})
            for sid, sub in subjects.items():
                for i, ex in enumerate(sub.examples):
                    out.append((fable, sid, i, ex))
    return out


def _normalize(v):
    """Canonicalize: all keywords as ('__kw__', name), all symbols as
    ('__sym__', name), all dicts/lists deeply normalized."""
    from fractions import Fraction
    if isinstance(v, str):
        if v.startswith(":"):
            return ("__kw__", v[1:])
        return v
    if isinstance(v, tuple) and len(v) == 2 and v[0] in ("__kw__", "__sym__"):
        return v
    if isinstance(v, list):
        return [_normalize(x) for x in v]
    if isinstance(v, dict):
        return {_normalize(k): _normalize(x) for k, x in v.items()}
    if isinstance(v, set) or isinstance(v, frozenset):
        return frozenset(_normalize(x) for x in v)
    if isinstance(v, Fraction):
        return v
    return v


def equal_modulo(a, b):
    """Tolerant equality: keyword string vs tuple, list vs tuple,
    fraction vs ratio-string."""
    from fractions import Fraction
    if isinstance(a, Fraction) and isinstance(b, str) and "/" in b:
        try:
            n, d = b.split("/")
            return a == Fraction(int(n), int(d))
        except Exception:
            return False
    if isinstance(b, Fraction) and isinstance(a, str) and "/" in a:
        try:
            n, d = a.split("/")
            return b == Fraction(int(n), int(d))
        except Exception:
            return False
    return _normalize(a) == _normalize(b)


def main():
    examples = collect_examples()
    print(f"collected {len(examples)} examples across {len(FABLES)} fables")

    parse_fails       = []
    eval_fails        = []
    answer_mismatches = []
    ok                = 0
    by_fable          = defaultdict(lambda: {"ok": 0, "parse": 0,
                                              "eval": 0, "mismatch": 0})

    for fable, sid, i, ex in examples:
        # Skip atom subjects where form is meant to be displayed as-is
        # (e.g., "42" parses to Lit(42) which evaluates to 42 — fine).
        # Skip non-evaluable forms like macro definitions (we'll mark
        # those for bb pre-flight in Phase 7).
        try:
            ast = parse(ex.form)
        except (ParseError, UnsupportedForm) as e:
            parse_fails.append((fable, sid, i, ex.form, str(e)))
            by_fable[fable]["parse"] += 1
            continue
        except Exception as e:
            parse_fails.append((fable, sid, i, ex.form, f"!!{type(e).__name__}: {e}"))
            by_fable[fable]["parse"] += 1
            continue
        try:
            got = evaluate(ast)
        except Exception as e:
            eval_fails.append((fable, sid, i, ex.form, str(e)))
            by_fable[fable]["eval"] += 1
            continue
        if not equal_modulo(got, ex.expected):
            answer_mismatches.append(
                (fable, sid, i, ex.form, got, ex.expected))
            by_fable[fable]["mismatch"] += 1
            continue
        ok += 1
        by_fable[fable]["ok"] += 1

    print(f"\n=== summary ===")
    print(f"  ok:               {ok}")
    print(f"  parse_fails:      {len(parse_fails)}")
    print(f"  eval_fails:       {len(eval_fails)}")
    print(f"  answer_mismatch:  {len(answer_mismatches)}")
    print(f"\n=== by fable ===")
    for fable, stats in by_fable.items():
        print(f"  {fable:18s} ok={stats['ok']:4d} "
              f"parse_fail={stats['parse']:3d} eval_fail={stats['eval']:3d} "
              f"mismatch={stats['mismatch']:3d}")

    # Sample failures so the user sees what's blocking
    print(f"\n=== first 12 parse fails ===")
    for f, sid, i, src, err in parse_fails[:12]:
        print(f"  [{f}/{sid}#{i}] {src[:80]!r}\n    → {err[:120]}")
    print(f"\n=== first 8 eval fails ===")
    for f, sid, i, src, err in eval_fails[:8]:
        print(f"  [{f}/{sid}#{i}] {src[:80]!r}\n    → {err[:120]}")
    print(f"\n=== first 8 answer mismatches ===")
    for f, sid, i, src, got, want in answer_mismatches[:8]:
        print(f"  [{f}/{sid}#{i}] {src[:80]!r}\n    got={got!r}  want={want!r}")


if __name__ == "__main__":
    main()
