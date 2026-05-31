"""End-to-end smoke test of the parametric pipeline.

Builds a synthetic subject with one parametric example, generates 50
records, confirms every record's form evaluates to the claimed expected
value via expr.py, and that the prose contains the drawn values.
"""
import sys

sys.path.insert(0, "/home/user/mmllm/src")

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
    generate_subject,
)
from mmllm.aesop.curriculum.form_parser import parse
from mmllm.aesop.expr import evaluate


# Single parametric example: (+ a b c) where a/b/c are INT_SMALL.
example = SubjectExample(
    form           = "",
    expected       = None,
    concept_phrase = "the sum of {drawn.a}, {drawn.b}, and {drawn.c}",
    question_what  = "the sum of {drawn.a}, {drawn.b}, and {drawn.c}",
    goal_text      = "add {drawn.a}, {drawn.b}, and {drawn.c}",
    form_template  = "(+ {a} {b} {c})",
    slots          = {"a": "INT_SMALL", "b": "INT_SMALL", "c": "INT_SMALL"},
    expected_fn    = lambda d: d["a"] + d["b"] + d["c"],
    scenario       = (
        "Mossback set out three small piles on the path: {drawn.a} acorns, "
        "{drawn.b} acorns, and {drawn.c} acorns."
    ),
    need = (
        "Whisker wanted to know how many acorns lay on the path in total."
    ),
    mapping = (
        "`(+ a b c)` adds three numbers — the three piles map to the "
        "three operands."
    ),
    resolution = (
        "The REPL's value is the total count of acorns."
    ),
    tags = ("story",),
)

subplots = [
    SubplotTemplate(
        "{hare_phrase} and {tortoise_phrase} sat {place} pondering "
        "{concept_phrase}. {scenario}\n\n"
        "{need}\n\n"
        "{mapping}\n\n"
        "{resolution}",
        fits_tags=("story",)),
    SubplotTemplate(
        "{hare_phrase} considered the form {form_display}, which "
        "computes {concept_phrase}. {scenario}"),
]

subj = SubjectCurriculum(
    grade        = 1,
    subject_id   = "TEST-01",
    subject_title= "test parametric add",
    fable        = "tortoise-hare",
    examples     = [example],
    subplots     = subplots,
    plan_pool    = ("I'll add the three numbers carefully.",),
)

records = generate_subject(subj, n_per_example=50, seed=42)
print(f"generated {len(records)} records")

ok = 0
distinct_forms    = set()
distinct_user_msg = set()
for rec in records:
    distinct_forms.add(rec.code_str)
    distinct_user_msg.add(rec.user_msg)
    ast = parse(rec.code_str)
    got = evaluate(ast)
    if got != rec.expected:
        print(f"MISMATCH: form {rec.code_str!r}: got {got}, want {rec.expected}")
        continue
    ok += 1
print(f"verifier-confirmed: {ok}/{len(records)}")
print(f"distinct forms:   {len(distinct_forms)} / {len(records)}")
print(f"distinct user_msg: {len(distinct_user_msg)} / {len(records)}")

# Print the first 3 records so we can eyeball that {drawn.X} substituted
print("\n--- 3 sample records ---\n")
for rec in records[:3]:
    print(f"FORM:     {rec.code_str}")
    print(f"EXPECTED: {rec.expected}")
    print("USER_MSG:")
    print(rec.user_msg)
    print("-" * 60)
