"""Probe auto-parametric coverage across the 5 Phase-C-complete fables."""
import importlib
import sys
from collections import defaultdict

sys.path.insert(0, "/home/user/mmllm/src")

from mmllm.aesop.curriculum.auto_parametric import auto_parametric_from_form


FABLES = ["tortoise_hare", "crow_pitcher", "milkmaid", "boy_wolf", "dog_shadow"]


def main():
    examples = []
    for fable in FABLES:
        for grade in range(1, 13):
            try:
                mod = importlib.import_module(
                    f"mmllm.aesop.curriculum.{fable}.grade_{grade}")
            except ImportError:
                continue
            for sid, sub in getattr(mod, "SUBJECTS", {}).items():
                for i, ex in enumerate(sub.examples):
                    examples.append((fable, sid, i, ex))

    print(f"collected {len(examples)} examples")
    converted = 0
    no_lit = 0
    fails = 0
    by_fable = defaultdict(lambda: {"converted": 0, "no_lit": 0, "failed": 0})
    by_grade = defaultdict(lambda: {"converted": 0, "no_lit": 0, "failed": 0})
    fail_samples = []

    for fable, sid, i, ex in examples:
        grade = int(sid.split("-")[0][1:])
        result = auto_parametric_from_form(ex.form, expected=ex.expected)
        if result is None:
            # Check whether it's no-literal or true failure
            from mmllm.aesop.curriculum.form_parser import parse, ParseError, UnsupportedForm
            try:
                ast = parse(ex.form)
                from mmllm.aesop.curriculum.auto_parametric import _collect_literals
                lits = []
                _collect_literals(ast, lits)
                if not lits:
                    no_lit += 1
                    by_fable[fable]["no_lit"] += 1
                    by_grade[grade]["no_lit"] += 1
                else:
                    fails += 1
                    by_fable[fable]["failed"] += 1
                    by_grade[grade]["failed"] += 1
                    if len(fail_samples) < 12:
                        fail_samples.append((fable, sid, i, ex.form, ex.expected))
            except (ParseError, UnsupportedForm) as e:
                fails += 1
                by_fable[fable]["failed"] += 1
                by_grade[grade]["failed"] += 1
                if len(fail_samples) < 12:
                    fail_samples.append((fable, sid, i, ex.form, str(e)[:80]))
        else:
            converted += 1
            by_fable[fable]["converted"] += 1
            by_grade[grade]["converted"] += 1

    print(f"\n=== summary ===")
    print(f"  converted:    {converted}")
    print(f"  no_literals:  {no_lit}  (atoms / pure-symbol forms)")
    print(f"  failed:       {fails}  (parse error or unsupported)")
    print(f"\n=== by fable ===")
    for fable, stats in by_fable.items():
        total = stats['converted'] + stats['no_lit'] + stats['failed']
        print(f"  {fable:18s} converted={stats['converted']:4d} "
              f"no_lit={stats['no_lit']:3d} failed={stats['failed']:3d} "
              f"({100 * (stats['converted'] + stats['no_lit']) / total:.1f}% migrated)")
    print(f"\n=== by grade ===")
    for grade in sorted(by_grade):
        stats = by_grade[grade]
        total = stats['converted'] + stats['no_lit'] + stats['failed']
        if total:
            print(f"  G{grade:2d}  converted={stats['converted']:4d} "
                  f"no_lit={stats['no_lit']:3d} failed={stats['failed']:3d} "
                  f"({100 * (stats['converted'] + stats['no_lit']) / total:.1f}%)")

    print(f"\n=== first 12 failures ===")
    for f, sid, i, src, err in fail_samples:
        print(f"  [{f}/{sid}#{i}] {src[:70]!r}\n    → {err}")


if __name__ == "__main__":
    main()
