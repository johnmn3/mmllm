"""Audit the ant-grasshopper K-12 curriculum.

Mirrors audits/audit-harness.py but pointed at ant_grasshopper. Run after
each grade lands; goal is 0 issues across all subjects × 3 records.
"""
from __future__ import annotations

import importlib
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, "/home/user/mmllm/src")

from mmllm.aesop.curriculum.generator import generate_subject

GRADE_MODULES = []
for n in range(1, 13):
    mod = importlib.import_module(f"mmllm.aesop.curriculum.ant_grasshopper.grade_{n}")
    GRADE_MODULES.append(mod)


def check_record(rec, sub, example):
    issues = []
    user = rec.user_msg
    asst = rec.assistant_msg

    # length
    n_words = len(user.split())
    if n_words < 35:
        issues.append(("LOW_LENGTH", f"user_msg only {n_words} words"))
    elif n_words > 200:
        issues.append(("HIGH_LENGTH", f"user_msg {n_words} words"))

    # singular-they verb agreement
    for m in re.finditer(r"\bthey\s+(?:eats|walks|runs|has\b|is\b|knows|hopes|reaches|jumps|drops)\b", user, re.IGNORECASE):
        issues.append(("VERB_AGREEMENT", f"singular-they: '{m.group(0)}'"))

    # un-substituted placeholder
    if "{form_display}" in user or "{concept_phrase}" in user or "{place}" in user:
        issues.append(("UNFILLED_PLACEHOLDER", "user_msg has un-substituted placeholder"))

    # answer-leak detection: only if the answer is an int that's NOT a substring of the form
    if isinstance(example.expected, int) and abs(example.expected) > 5:
        ans_str = str(example.expected)
        if ans_str not in example.form:
            user_clean = user.replace(example.form, "")
            ans_re = rf"(?<![0-9-]){re.escape(ans_str)}(?![0-9])"
            if re.search(ans_re, user_clean):
                issues.append(("ANSWER_LEAK", f"answer {ans_str} in narrative"))

    # asst leak: strip the JSON form arg properly (handles escaped quotes)
    if isinstance(example.expected, int) and abs(example.expected) > 5:
        ans_str = str(example.expected)
        if ans_str not in example.form:
            asst_clean = re.sub(
                r'"form":"(?:[^"\\]|\\.)*"', '', asst
            )
            ans_re = rf"(?<![0-9-]){re.escape(ans_str)}(?![0-9])"
            if re.search(ans_re, asst_clean):
                issues.append(("ANSWER_LEAK_ASST", f"answer {ans_str} in asst preface"))

    # nested 'computes' in question_what
    if "computes" in example.question_what.lower():
        issues.append(("NESTED_COMPUTES", "question_what already says 'computes'"))

    aside_re = re.compile(
        r"\((?:note(?:\:|\s)|it isn'?t|the REPL\s|returns\s|the return\s|"
        r"first truthy|empty string|the comment\s|integer quotient|it does|it doesn'?t)"
    )
    for label, val in (("concept_phrase", example.concept_phrase),
                        ("question_what",  example.question_what)):
        if aside_re.search(val):
            issues.append(("ASIDE_PAREN",
                            f"{label} has pedagogical-aside parenthetical"))

    emdash_re = re.compile(r" — (?:note|first|empty|returns|integer)")
    if emdash_re.search(example.question_what) or emdash_re.search(example.concept_phrase):
        issues.append(("EMDASH_COMMENTARY",
                        "concept_phrase or question_what has em-dash commentary"))

    bad_said = ["said boasting", "said puffed", "said swaggering",
                 "said with a smug grin"]
    for p in bad_said:
        if p in user.lower():
            issues.append(("SAID_PARTICIPLE", f"'{p}' (missing comma after 'said')"))
            break

    if re.search(r"from \w+ing from a recent", user.lower()):
        issues.append(("DOUBLE_FROM", "'from X-ing from a recent sprint' duplication"))

    if re.search(r"the value of the form \S", example.question_what):
        issues.append(("META_META",
                        "question_what 'the value of the form X' creates meta-meta wrap"))

    for bad in ("in the hilltop", "in the road", "in the beach"):
        if bad in user:
            issues.append(("BAD_PLACE_PREP", f"'{bad}' (wrong preposition)"))
            break

    if "stopped across " in user:
        issues.append(("BAD_VERB_PREP",
                        "'stopped across X' (verb+prep mismatch)"))

    return issues


def per_example_records(sub, example, n: int, seed: int):
    """Generate `n` records for ONE specific example by filtering."""
    out = []
    s = seed
    while len(out) < n and s < seed + n * 50:
        recs = generate_subject(sub, n_per_example=1, seed=s)
        for r in recs:
            if r.code_str == example.form:
                out.append(r)
                if len(out) >= n:
                    break
        s += 1
    return out


def main():
    out = Path("/home/user/mmllm/docs/clojure-pedagogy/audits/ant-grasshopper-audit.md")
    out.parent.mkdir(parents=True, exist_ok=True)

    summary = Counter()
    issue_examples: dict[str, list] = {}
    per_grade_stats: dict[int, dict] = {}

    with open(out, "w") as f:
        f.write("# Ant-grasshopper curriculum audit\n\n")
        f.write("Auto-generated audit — each subject's examples checked at "
                "3 records per example, properly matched.\n\n")
        f.write("---\n\n")

        for grade_n, mod in enumerate(GRADE_MODULES, 1):
            f.write(f"## Grade {grade_n}\n\n")
            grade_stats = {"subjects": 0, "examples": 0, "issues": 0,
                            "low_variety": []}
            for sid, sub in mod.SUBJECTS.items():
                grade_stats["subjects"] += 1
                grade_stats["examples"] += len(sub.examples)

                seed_base = int(sid[3:].replace("-", "")) * 7
                recs50 = generate_subject(sub, n_per_example=50, seed=seed_base)
                n_unique = len({r.user_msg for r in recs50})
                variety = n_unique / len(recs50)
                if variety < 0.95:
                    grade_stats["low_variety"].append((sid, variety))

                subj_issues = []
                for example in sub.examples:
                    sample = per_example_records(sub, example, n=3, seed=seed_base)
                    for r in sample:
                        for sev, msg in check_record(r, sub, example):
                            summary[sev] += 1
                            grade_stats["issues"] += 1
                            subj_issues.append((sev, msg, example.form, r.user_msg[:200]))
                            if sev not in issue_examples:
                                issue_examples[sev] = []
                            if len(issue_examples[sev]) < 5:
                                issue_examples[sev].append(
                                    (sid, msg, example.form, r.user_msg[:300])
                                )

                if subj_issues or variety < 0.95:
                    f.write(f"### {sid}: {sub.subject_title}\n\n")
                    f.write(f"- examples: {len(sub.examples)}\n")
                    f.write(f"- variety @ n=50: {variety:.2f}\n")
                    if subj_issues:
                        by_sev = Counter(i[0] for i in subj_issues)
                        f.write(f"- issues: {dict(by_sev)}\n")
                        for sev, msg, form, snip in subj_issues[:6]:
                            f.write(f"    - [{sev}] form=`{form[:50]}` — {msg}\n")
                    f.write("\n")
            per_grade_stats[grade_n] = grade_stats

        f.write("---\n\n## Summary\n\n")
        f.write("### Issue counts (across all examples × 3 records)\n\n")
        for sev, n in summary.most_common():
            f.write(f"- **{sev}**: {n}\n")
        f.write("\n### Per-grade summary\n\n")
        f.write("| Grade | Subjects | Examples | Issues | Low-variety |\n|---|---|---|---|---|\n")
        for g, s in per_grade_stats.items():
            lv = "; ".join(f"{sid}({v:.2f})" for sid, v in s["low_variety"][:3]) or "—"
            f.write(f"| {g} | {s['subjects']} | {s['examples']} | {s['issues']} | {lv} |\n")
        f.write("\n### Sample issues by severity\n\n")
        for sev, samples in issue_examples.items():
            f.write(f"#### {sev}\n\n")
            for sid, msg, form, snippet in samples:
                f.write(f"- `{sid}` (form `{form[:60]}`): {msg}\n")
                f.write(f"    ```\n    {snippet[:300]}...\n    ```\n")
            f.write("\n")

    print(f"audit → {out}")
    print(f"total issues: {sum(summary.values())}")
    print(f"breakdown: {dict(summary)}")


if __name__ == "__main__":
    main()
