"""Pre-flight gate: run every legacy (non-parametric) form through bb,
confirm authored expected matches bb's evaluation. Run once at
corpus-build time; results cached in ~/.mmllm/bb_verify_cache.json.

Failures are reported as a punch-list so they can be hand-corrected
or rewritten as parametric examples.

Usage:
    PATH=/tmp/bb-bin:$PATH python scripts/preflight_bb_verify.py
"""
import sys
import json
from pathlib import Path

sys.path.insert(0, "/home/user/mmllm/src")

from mmllm.aesop.curriculum.bb_verifier import (
    verify_legacy_corpus_via_bb, _bb_path,
)


def main():
    bb = _bb_path()
    if bb is None:
        print("FAIL: bb not installed. Set PATH or install via")
        print("  curl -sLO https://raw.githubusercontent.com/babashka/babashka/master/install")
        print("  bash install --dir /tmp/bb-bin")
        sys.exit(2)

    print(f"using bb at {bb}")
    print("walking 5 fables × 12 grades, verifying every legacy form via bb…")
    out = verify_legacy_corpus_via_bb()

    print()
    print(f"=== bb pre-flight summary ===")
    print(f"  checked:  {out['checked']}")
    print(f"  passed:   {out['passed']}    "
          f"({100*out['passed']/max(1,out['checked']):.1f}%)")
    print(f"  failed:   {out['failed']}    "
          f"({100*out['failed']/max(1,out['checked']):.1f}%)")

    # Re-walk to get the full failure list (verify_legacy_corpus_via_bb
    # caps at 12 in the returned dict).
    fails = []
    import importlib
    from mmllm.aesop.curriculum.bb_verifier import verify_with_bb
    for fable in ("tortoise_hare", "crow_pitcher", "milkmaid",
                  "boy_wolf", "dog_shadow"):
        for grade in range(1, 13):
            try:
                mod = importlib.import_module(
                    f"mmllm.aesop.curriculum.{fable}.grade_{grade}")
            except ImportError:
                continue
            for sid, sub in getattr(mod, "SUBJECTS", {}).items():
                for i, ex in enumerate(sub.examples):
                    if ex.form_template:
                        continue
                    if not ex.form:
                        continue
                    res = verify_with_bb(ex.form, ex.expected)
                    if res is False:
                        fails.append({
                            "fable":     fable,
                            "subject":   sid,
                            "ex_idx":    i,
                            "form":      ex.form,
                            "expected":  repr(ex.expected),
                        })

    if fails:
        report_path = Path("/tmp/bb_verify_failures.json")
        report_path.write_text(json.dumps(fails, indent=2))
        print(f"\nFailure punch-list: {len(fails)} entries → {report_path}")
        print("\nTop failure categories:")
        from collections import Counter
        kinds = Counter()
        for f in fails:
            form = f["form"]
            if "(meta " in form:                 kinds["metadata"] += 1
            elif "finally" in form:               kinds["try/finally"] += 1
            elif "defmacro" in form:              kinds["defmacro"] += 1
            elif "deftype" in form:               kinds["deftype/defrecord"] += 1
            elif "defprotocol" in form:           kinds["defprotocol"] += 1
            elif "atom" in form or "swap!" in form: kinds["atom/swap!"] += 1
            elif "loop" in form or "recur" in form: kinds["loop/recur"] += 1
            elif "core.async" in form or " go " in form: kinds["core.async"] += 1
            elif form.startswith("(defn"):        kinds["defn (fn-value)"] += 1
            elif "#{" in form or "into #{" in form: kinds["set literal"] += 1
            else:                                  kinds["other"] += 1
        for kind, count in kinds.most_common():
            print(f"  {kind:25s} {count}")

    print()
    if out["failed"] == 0:
        print("OK — all legacy forms pass bb pre-flight.")
        sys.exit(0)
    else:
        print(f"NOTE: {out['failed']} legacy forms failed bb pre-flight.")
        print("These remain in the corpus as legacy mode (no in-process verifier).")
        print(f"Hand-correct via {report_path} or rewrite as parametric.")
        # Don't exit non-zero — failures are advisory, not blocking
        sys.exit(0)


if __name__ == "__main__":
    main()
