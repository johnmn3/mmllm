"""Sample-evaluate forms via basilisp and check expected values match.

Subprocess to basilisp REPL is slow (1-2s startup); we batch many forms
into one process via a single basilisp file that prints per-form results.
"""
import importlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, "/home/user/mmllm/src")


def collect_forms_to_check(max_per_grade: int = 5):
    """Sample up to N (form, expected) pairs per grade for verification."""
    results = []
    for n in range(1, 13):
        try:
            mod = importlib.import_module(
                f"mmllm.aesop.curriculum.tortoise_hare.grade_{n}"
            )
        except Exception as e:
            print(f"skipping grade {n}: {e}")
            continue
        sampled = 0
        for sid, sub in mod.SUBJECTS.items():
            for ex in sub.examples:
                # Skip forms that need an actual JVM / require side effects we
                # can't easily test (interop, namespace ops, etc.).
                form = ex.form
                if any(token in form for token in (
                    "println", "print",                    # side-effect, returns nil
                    "ns ", "in-ns",
                    "future", "agent", "atom", "ref",
                    "deftype", "defrecord", "defprotocol",
                    "Math/", ".toUpperCase", ".substring", "Date.",
                    "(future", "@", "swap!", "reset!",
                    "with-out-str", "slurp", "spit",
                    "(macroexpand", "defmacro",
                    "core.async", "go ", "<!", ">!",
                )):
                    continue
                results.append({
                    "sid": sid, "form": form, "expected": ex.expected,
                    "grade": n,
                })
                sampled += 1
                if sampled >= max_per_grade:
                    break
            if sampled >= max_per_grade:
                break
    return results


def evaluate_via_basilisp(forms: list[dict]):
    """Send all forms to a single basilisp process and collect results."""
    # Build a basilisp file that prints (form-id, result) for each.
    script_lines = []
    for i, f in enumerate(forms):
        script_lines.append(
            f'(try (println "{i}|" (pr-str {f["form"]})) '
            f'(catch python/Exception e (println "{i}| ERROR " e)))'
        )
    script = "\n".join(script_lines)
    with tempfile.NamedTemporaryFile("w", suffix=".lpy", delete=False) as fp:
        fp.write(script)
        fp_path = fp.name

    try:
        proc = subprocess.run(
            ["basilisp", "run", fp_path],
            capture_output=True, text=True, timeout=120,
        )
    except FileNotFoundError:
        print("basilisp not available; skipping form eval check")
        return None
    except subprocess.TimeoutExpired:
        print("basilisp timed out")
        return None

    out_lines = proc.stdout.splitlines()
    results = {}
    for line in out_lines:
        if "|" not in line:
            continue
        idx_str, _, val = line.partition("|")
        idx_str = idx_str.strip()
        if idx_str.isdigit():
            results[int(idx_str)] = val.strip()
    return results


def main():
    forms = collect_forms_to_check(max_per_grade=8)
    print(f"sampled {len(forms)} forms across grades")

    results = evaluate_via_basilisp(forms)
    if results is None:
        return

    mismatches = []
    matched = 0
    for i, f in enumerate(forms):
        actual = results.get(i)
        if actual is None:
            mismatches.append((f, "no result"))
            continue
        expected = f["expected"]
        # Normalize expected for comparison
        if isinstance(expected, bool):
            exp_str = str(expected).lower()
        elif expected is None:
            exp_str = "nil"
        elif isinstance(expected, str):
            # Check if it's a Clojure literal (starts with ":") or actual string
            if expected.startswith(":"):
                exp_str = expected
            else:
                exp_str = f'"{expected}"'
        else:
            exp_str = str(expected)
        if actual.strip() == exp_str.strip():
            matched += 1
        else:
            mismatches.append((f, actual))

    print(f"matched: {matched}/{len(forms)}")
    print(f"mismatches: {len(mismatches)}")
    for f, actual in mismatches[:10]:
        print(f"  [{f['sid']}] form={f['form'][:60]!r}")
        print(f"      expected={f['expected']!r}  actual={actual!r}")


if __name__ == "__main__":
    main()
