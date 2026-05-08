"""Verify the full pipeline: generate from each grade across all 5
fables, confirm every record's form parses + evaluates to claimed
expected, count distinct forms / user_msg / expected per subject."""
import importlib
import sys
from collections import defaultdict

sys.path.insert(0, "/home/user/mmllm/src")

from mmllm.aesop.curriculum.generator import generate_subject
from mmllm.aesop.curriculum.form_parser import parse, ParseError
from mmllm.aesop.expr import evaluate


FABLES = ["tortoise_hare", "crow_pitcher", "milkmaid", "boy_wolf", "dog_shadow"]


def main():
    by_grade = defaultdict(lambda: {"records": 0, "verified": 0,
                                     "failed": 0, "uniq_forms": set(),
                                     "uniq_msgs": set()})
    by_fable = defaultdict(lambda: {"records": 0, "verified": 0,
                                     "failed": 0})
    fail_samples = []

    for fable in FABLES:
        for grade in range(1, 13):
            try:
                mod = importlib.import_module(
                    f"mmllm.aesop.curriculum.{fable}.grade_{grade}")
            except ImportError:
                continue
            for sid, sub in getattr(mod, "SUBJECTS", {}).items():
                try:
                    recs = generate_subject(sub, n_per_example=4, seed=hash(sid) & 0xFFFF)
                except Exception as e:
                    fail_samples.append((fable, sid, "GEN_FAIL", str(e)[:120]))
                    continue
                for r in recs:
                    by_grade[grade]["records"] += 1
                    by_fable[fable]["records"] += 1
                    by_grade[grade]["uniq_forms"].add(r.code_str)
                    by_grade[grade]["uniq_msgs"].add(r.user_msg)
                    try:
                        ast = parse(r.code_str)
                        got = evaluate(ast)
                        if _equal(got, r.expected):
                            by_grade[grade]["verified"] += 1
                            by_fable[fable]["verified"] += 1
                        else:
                            by_grade[grade]["failed"] += 1
                            by_fable[fable]["failed"] += 1
                            if len(fail_samples) < 12:
                                fail_samples.append(
                                    (fable, sid, "MISMATCH",
                                     f"{r.code_str!r}: got {got!r}, want {r.expected!r}"))
                    except (ParseError, Exception) as e:
                        by_grade[grade]["failed"] += 1
                        by_fable[fable]["failed"] += 1
                        if len(fail_samples) < 12:
                            fail_samples.append(
                                (fable, sid, "EVAL_FAIL",
                                 f"{r.code_str[:60]!r}: {str(e)[:80]}"))

    print("=== by fable ===")
    for fable, s in by_fable.items():
        print(f"  {fable:18s} records={s['records']:5d} "
              f"verified={s['verified']:5d} failed={s['failed']:4d} "
              f"({100*s['verified']/max(1,s['records']):.1f}% pass)")

    print("\n=== by grade ===")
    for grade in sorted(by_grade):
        s = by_grade[grade]
        recs = s["records"]
        print(f"  G{grade:2d}  records={recs:5d} verified={s['verified']:5d} "
              f"failed={s['failed']:4d}  "
              f"uniq_forms={len(s['uniq_forms']):4d} "
              f"uniq_msgs={len(s['uniq_msgs']):5d}")

    print(f"\n=== first 12 failures ===")
    for f, sid, kind, err in fail_samples:
        print(f"  [{f}/{sid}] {kind}\n    → {err}")


def _equal(a, b):
    """Tolerant equality for evaluator outputs vs author intent."""
    from fractions import Fraction
    if isinstance(a, str) and a.startswith(":"):
        a = ("__kw__", a[1:])
    if isinstance(b, str) and b.startswith(":"):
        b = ("__kw__", b[1:])
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(_equal(x, y) for x, y in zip(a, b))
    if isinstance(a, dict) and isinstance(b, dict):
        an = {_norm(k): v for k, v in a.items()}
        bn = {_norm(k): v for k, v in b.items()}
        if set(an) != set(bn): return False
        return all(_equal(an[k], bn[k]) for k in an)
    if isinstance(a, Fraction) and isinstance(b, str) and "/" in b:
        n, d = b.split("/")
        return a == Fraction(int(n), int(d))
    return a == b


def _norm(k):
    if isinstance(k, str) and k.startswith(":"):
        return ("__kw__", k[1:])
    return k


if __name__ == "__main__":
    main()
