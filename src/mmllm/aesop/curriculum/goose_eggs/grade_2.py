"""Grade 2 — operators + arithmetic mastery, taught through goose-eggs.

Grade 2 deepens grade 1's L1+L2 work. Where grade 1 introduced the
single-arg arithmetic call, grade 2 covers multi-arg arithmetic,
comparison chains, the boolean-logic operators, the numeric helpers
(inc/dec/quot/rem/mod, min/max, abs), strings via str, and the
truthy/falsey rules.

The fable lens: the impatient {visitor}'s hasty boasts about answers
('I can guess without computing!') consistently lose to the patient
{owner}'s "let me actually evaluate the form" approach. The {goose}'s
one-egg-per-morning rhythm continues to mirror eval's one-form-one-value
rhythm, even as the forms grow into chains of operations and ledgers
of coins.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.goose_eggs.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SHARED_SUBPLOTS,
    _PLAN_POOL as _G1_PLAN_POOL,
)


# Extend grade-1's shared pool with grade-2-specific subplots that
# lean into multi-operand / chained-operator framings, recast through
# goose-eggs scenery (slates by the egg-basket, ledgers of coins,
# market-stall wagers, the patience-vs-greed dynamic).
_SHARED_SUBPLOTS: list[SubplotTemplate] = list(_G1_SHARED_SUBPLOTS) + [
    # 9. The chain-of-operations template — useful for multi-arg
    #    arithmetic and comparison-chain subjects. A slate by the
    #    egg-basket holds a cascading calculation.
    SubplotTemplate("""\
{owner_phrase} had been laying out a chain of small computations on a
slate {place} — one operation, then another, all to settle a question
{visitor_phrase} had raised about the morning's eggs. The current form
on the slate was {form_display}, and {owner} explained, {emo_patient},
that {concept_phrase} would be settled the moment the form was handed
to the REPL — the way {goose_phrase} settled each morning's tally with
one egg, no more, no less."""),

    # 10. The wager-with-stakes template — stakes are real (eggs, coins)
    #     when the form is more interesting (e.g., min/max, mod).
    SubplotTemplate("""\
"Whatever {form_display} comes to," {visitor_phrase} declared,
{emo_proud}, {place}, "I'll wager a basket of eggs I know it without
typing it." {owner_phrase}, {emo_patient}, picked up a piece of chalk
and drew {concept_phrase} on the side of the egg-crate. "Then write
the form," {owner_he_she} said. "The REPL will have the last word, the
way {goose_phrase} has the last word on the morning's count.\""""),

    # 11. The ledger-of-coins template — ledger entries become
    #     multi-step calculations that resolve to one value at a time.
    SubplotTemplate("""\
A row of small coins lay on a wooden table {place}, one for each
operand in the day's reckoning. {owner_phrase} had written
{form_display} at the top of the ledger — the next entry, just below
yesterday's egg-count. {visitor_phrase} pointed at the coins and
guessed loudly, {emo_greedy}, but {owner} said {concept_phrase} would
not be answered by guessing; the REPL would tell, calmly, the way
{goose_phrase} laid the next egg without rushing."""),
]


# Grade-2-flavored plan pool: extend grade-1's pool with plans that
# acknowledge the multi-step / chained nature of grade-2 forms while
# never revealing any specific answer.
_PLAN_POOL: tuple[str, ...] = tuple(_G1_PLAN_POOL) + (
    "I write the chain of operations as Clojure source and let the REPL collapse it.",
    "I let the REPL settle the chain one operator at a time.",
    "I submit the whole form and let the runtime reduce it patiently, the way the goose lays one egg at a time.",
)


def _ex(form, expected, concept, what, tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          tags=tags)


# ─────────────────────── 22 grade-2 subjects ───────────────────────


G2_01 = SubjectCurriculum(
    grade=2, subject_id="G2-01",
    subject_title="Multi-arg arithmetic",
    fable="goose-eggs",
    examples=[
        _ex("(+ 1 2 3 4)", 10,        "the sum (+ 1 2 3 4)",      "the result of (+ 1 2 3 4)"),
        _ex("(* 2 3 4)", 24,          "the product (* 2 3 4)",    "the result of (* 2 3 4)"),
        _ex("(- 100 1 2 3)", 94,      "the chain (- 100 1 2 3)",  "the result of (- 100 1 2 3)"),
        _ex("(+ 1 2 3 4 5 6 7 8 9 10)", 55,
            "the sum 1+2+...+10",       "the sum of integers 1 through 10"),
        _ex("(* 1 2 3 4 5)", 120,     "the product 1*2*3*4*5",    "the product of 1 through 5"),
        _ex("(+ 10 20 30)", 60,       "the sum (+ 10 20 30)",     "the sum of 10, 20, and 30"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_02 = SubjectCurriculum(
    grade=2, subject_id="G2-02",
    subject_title="Comparison chains",
    fable="goose-eggs",
    examples=[
        _ex("(< 1 2 3)",  True,  "the chain (< 1 2 3)",  "whether 1 < 2 < 3"),
        _ex("(< 3 2 1)",  False, "the chain (< 3 2 1)",  "whether 3 < 2 < 1"),
        _ex("(<= 1 1 2)", True,  "the chain (<= 1 1 2)", "whether 1 ≤ 1 ≤ 2"),
        _ex("(> 5 4 3 2 1)", True,
            "the chain (> 5 4 3 2 1)",
            "whether the numbers 5,4,3,2,1 are strictly decreasing"),
        _ex("(>= 3 3 2)", True,
            "the chain (>= 3 3 2)",
            "whether 3 ≥ 3 ≥ 2"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_03 = SubjectCurriculum(
    grade=2, subject_id="G2-03",
    subject_title="not= and = with multiple args",
    fable="goose-eggs",
    examples=[
        _ex("(not= 1 2)",   True,  "the form (not= 1 2)",   "whether 1 differs from 2"),
        _ex("(not= 1 1)",   False, "the form (not= 1 1)",   "whether 1 differs from 1"),
        _ex("(= 1 1 1)",    True,  "the form (= 1 1 1)",    "whether all of 1,1,1 are equal"),
        _ex("(= 1 1 2)",    False, "the form (= 1 1 2)",    "whether 1,1,2 are all equal"),
        _ex("(not= 1 1 2)", True,  "the form (not= 1 1 2)", "whether at least one of 1,1,2 differs"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_04 = SubjectCurriculum(
    grade=2, subject_id="G2-04",
    subject_title="min and max",
    fable="goose-eggs",
    examples=[
        _ex("(min 1 2 3)",  1, "the form (min 1 2 3)",  "the minimum of 1, 2, 3"),
        _ex("(max 1 2 3)",  3, "the form (max 1 2 3)",  "the maximum of 1, 2, 3"),
        _ex("(min 7 3 9 1 5)", 1, "the form (min 7 3 9 1 5)", "the minimum of 7, 3, 9, 1, 5"),
        _ex("(max 7 3 9 1 5)", 9, "the form (max 7 3 9 1 5)", "the maximum of 7, 3, 9, 1, 5"),
        _ex("(min -3 -1 -5)", -5, "the form (min -3 -1 -5)", "the minimum of -3, -1, -5"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_05 = SubjectCurriculum(
    grade=2, subject_id="G2-05",
    subject_title="quot, rem, mod",
    fable="goose-eggs",
    examples=[
        _ex("(quot 17 5)", 3, "the integer quotient of 17 and 5", "the result of (quot 17 5)"),
        _ex("(rem 17 5)",  2, "the remainder of 17 divided by 5", "the result of (rem 17 5)"),
        _ex("(mod 17 5)",  2, "17 mod 5",                          "the result of (mod 17 5)"),
        _ex("(quot 100 7)", 14, "the integer quotient of 100 and 7", "the result of (quot 100 7)"),
        _ex("(rem 100 7)",  2, "the remainder of 100 divided by 7", "the result of (rem 100 7)"),
        _ex("(mod -7 3)",   2, "the form (mod -7 3)",              "the result of (mod -7 3)"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_06 = SubjectCurriculum(
    grade=2, subject_id="G2-06",
    subject_title="inc and dec",
    fable="goose-eggs",
    examples=[
        _ex("(inc 5)",  6, "the form (inc 5)",  "5 plus 1"),
        _ex("(dec 5)",  4, "the form (dec 5)",  "5 minus 1"),
        _ex("(inc 0)",  1, "the form (inc 0)",  "the successor of 0"),
        _ex("(dec 0)", -1, "the form (dec 0)",  "the predecessor of 0"),
        _ex("(inc -1)", 0, "the form (inc -1)", "the successor of -1"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_07 = SubjectCurriculum(
    grade=2, subject_id="G2-07",
    subject_title="Absolute value",
    fable="goose-eggs",
    examples=[
        _ex("(abs 5)",   5, "the form (abs 5)",   "the absolute value of 5"),
        _ex("(abs -5)",  5, "the form (abs -5)",  "the absolute value of -5"),
        _ex("(abs 0)",   0, "the form (abs 0)",   "the absolute value of 0"),
        _ex("(abs (- 3 8))", 5,
            "the form (abs (- 3 8))",
            "the absolute value of 3 minus 8"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_08 = SubjectCurriculum(
    grade=2, subject_id="G2-08",
    subject_title="Arithmetic on ratios",
    fable="goose-eggs",
    examples=[
        _ex("(+ 1/2 1/4)", "3/4",
            "the sum 1/2 + 1/4",       "the value of (+ 1/2 1/4)"),
        _ex("(* 2/3 3/4)", "1/2",
            "the product 2/3 × 3/4",   "the value of (* 2/3 3/4)"),
        _ex("(- 1 1/3)", "2/3",
            "1 minus 1/3",             "the value of (- 1 1/3)"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_09 = SubjectCurriculum(
    grade=2, subject_id="G2-09",
    subject_title="Floats vs ints (the / operator)",
    fable="goose-eggs",
    examples=[
        _ex("(/ 10 2)", 5,    "the integer division 10 ÷ 2",
            "the value of (/ 10 2)"),
        _ex("(/ 10 3)", "10/3", "the form (/ 10 3)",
            "the exact rational result of (/ 10 3)"),
        _ex("(/ 1.0 2)", 0.5, "the float division 1.0 ÷ 2",
            "the value of (/ 1.0 2)"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_10 = SubjectCurriculum(
    grade=2, subject_id="G2-10",
    subject_title="Powers via repeated multiplication",
    fable="goose-eggs",
    examples=[
        _ex("(* 2 2 2)", 8,        "two cubed", "2 to the third power"),
        _ex("(* 5 5)",   25,       "five squared", "5 squared"),
        _ex("(* 3 3 3 3)", 81,     "three to the fourth", "3 to the fourth power"),
        _ex("(* 10 10)", 100,      "ten squared", "10 squared"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_11 = SubjectCurriculum(
    grade=2, subject_id="G2-11",
    subject_title="String concatenation with str",
    fable="goose-eggs",
    examples=[
        _ex('(str "tor" "toise")', "tortoise",
            'the form (str "tor" "toise")', 'the joined string "tortoise"'),
        _ex('(str "race")', "race",
            'the form (str "race")', 'the value of (str "race")'),
        _ex('(str "x" "y" "z")', "xyz",
            'the form (str "x" "y" "z")', 'the joined string "xyz"'),
        _ex('(str 1 "+" 2 "=" 3)', "1+2=3",
            'the form (str 1 "+" 2 "=" 3)', 'the joined string "1+2=3"'),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_12 = SubjectCurriculum(
    grade=2, subject_id="G2-12",
    subject_title="print and println — return values",
    fable="goose-eggs",
    examples=[
        # println side-effects to stdout but RETURNS nil. The form
        # we ask for has the value nil; the model writes println
        # and the runtime returns nil.
        _ex('(println "hello")', None,
            'the form (println "hello")',
            'the return value of (println "hello")'),
        _ex('(print "x")', None,
            'the form (print "x")',
            'the return value of (print "x")'),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_13 = SubjectCurriculum(
    grade=2, subject_id="G2-13",
    subject_title="and / or — short circuit, return values",
    fable="goose-eggs",
    examples=[
        _ex("(and true true)",   True,   "the form (and true true)",
            "the value of (and true true)"),
        _ex("(and true false)",  False,  "the form (and true false)",
            "the value of (and true false)"),
        _ex("(or false true)",   True,   "the form (or false true)",
            "the value of (or false true)"),
        _ex("(or false false)",  False,  "the form (or false false)",
            "the value of (or false false)"),
        _ex("(and 1 2 3)",       3,      "the form (and 1 2 3)",
            "the value of (and 1 2 3)"),
        _ex("(or nil false 5)",  5,      "the form (or nil false 5)",
            "the value of (or nil false 5)"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_14 = SubjectCurriculum(
    grade=2, subject_id="G2-14",
    subject_title="not — turning truthy to false",
    fable="goose-eggs",
    examples=[
        _ex("(not true)",  False, "the form (not true)",  "the value of (not true)"),
        _ex("(not false)", True,  "the form (not false)", "the value of (not false)"),
        _ex("(not nil)",   True,  "the form (not nil)",   "the value of (not nil)"),
        _ex("(not 0)",     False, "the form (not 0)",     "the value of (not 0)"),
        _ex("(not \"\")",  False, "the form (not \"\")",  "the value of (not \"\")"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_15 = SubjectCurriculum(
    grade=2, subject_id="G2-15",
    subject_title="Falsey values: only false and nil",
    fable="goose-eggs",
    examples=[
        _ex("(if 0 :truthy :falsey)",   ":truthy", "the form (if 0 :truthy :falsey)",
            "which keyword (if 0 :truthy :falsey) returns"),
        _ex("(if \"\" :truthy :falsey)", ":truthy", "the form (if \"\" :truthy :falsey)",
            "which keyword (if \"\" :truthy :falsey) returns"),
        _ex("(if nil :truthy :falsey)", ":falsey", "the form (if nil :truthy :falsey)",
            "which keyword (if nil :truthy :falsey) returns"),
        _ex("(if false :truthy :falsey)", ":falsey", "the form (if false :truthy :falsey)",
            "which keyword (if false :truthy :falsey) returns"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_16 = SubjectCurriculum(
    grade=2, subject_id="G2-16",
    subject_title="Truthy 0 and empty string",
    fable="goose-eggs",
    examples=[
        _ex("(boolean 0)",   True,  "the form (boolean 0)",  "the truthiness of 0"),
        _ex("(boolean \"\")", True, "the form (boolean \"\")", "the truthiness of the empty string"),
        _ex("(boolean nil)", False, "the form (boolean nil)", "the truthiness of nil"),
        _ex("(boolean false)", False, "the form (boolean false)", "the truthiness of false"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_17 = SubjectCurriculum(
    grade=2, subject_id="G2-17",
    subject_title="Keyword as function for map lookup",
    fable="goose-eggs",
    examples=[
        _ex("(:hare {:hare 1 :tortoise 2})", 1,
            "the form (:hare {:hare 1 :tortoise 2})",
            "the value (:hare {:hare 1 :tortoise 2}) returns"),
        _ex("(:tortoise {:hare 1 :tortoise 2})", 2,
            "the form (:tortoise {:hare 1 :tortoise 2})",
            "the value (:tortoise {:hare 1 :tortoise 2}) returns"),
        _ex("(:missing {:hare 1})", None,
            "the form (:missing {:hare 1})",
            "the value when a missing keyword is looked up"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_18 = SubjectCurriculum(
    grade=2, subject_id="G2-18",
    subject_title="Quoting symbols",
    fable="goose-eggs",
    examples=[
        _ex("(quote hare)", "hare", "the quoted symbol (quote hare)",
            "the value of (quote hare)"),
        _ex("'tortoise", "tortoise", "the quoted symbol 'tortoise",
            "the value of 'tortoise"),
        _ex("'(1 2 3)", [1, 2, 3], "the quoted list '(1 2 3)",
            "the value of '(1 2 3)"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_19 = SubjectCurriculum(
    grade=2, subject_id="G2-19",
    subject_title="Auto-promotion to bigint",
    fable="goose-eggs",
    examples=[
        _ex("(* 1000000 1000000)", 1000000000000,
            "the form (* 1000000 1000000)",
            "the result of one million times one million"),
        _ex("(+ 99999999999 1)", 100000000000,
            "the form (+ 99999999999 1)",
            "the result of 99999999999 plus 1"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_20 = SubjectCurriculum(
    grade=2, subject_id="G2-20",
    subject_title="Counting",
    fable="goose-eggs",
    examples=[
        _ex("(count [1 2 3])",       3, "the count of [1 2 3]",
            "the count of the vector [1 2 3]"),
        _ex("(count \"hello\")",     5, "the count of \"hello\"",
            "the length of the string \"hello\""),
        _ex("(count [])",            0, "the count of an empty vector",
            "the count of an empty vector"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_21 = SubjectCurriculum(
    grade=2, subject_id="G2-21",
    subject_title="String length and substring",
    fable="goose-eggs",
    examples=[
        _ex("(count \"tortoise\")", 8,  "the length of \"tortoise\"",
            "the length of the string \"tortoise\""),
        _ex("(count \"hare\")",     4,  "the length of \"hare\"",
            "the length of the string \"hare\""),
        _ex("(subs \"tortoise\" 0 3)", "tor",
            "the form (subs \"tortoise\" 0 3)",
            "the first three characters of \"tortoise\""),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_22 = SubjectCurriculum(
    grade=2, subject_id="G2-22",
    subject_title="Compose pure arithmetic (multi-step calculation)",
    fable="goose-eggs",
    examples=[
        # A simple distance: speed × time, then minus a head-start.
        _ex("(- (* 5 4) 7)", 13,
            "the form (- (* 5 4) 7)",
            "5 mph for 4 hours, minus a 7-mile head start"),
        _ex("(+ (* 3 8) (* 2 4))", 32,
            "the sum of two products",
            "3*8 + 2*4"),
        _ex("(quot (+ 100 50) 5)", 30,
            "the form (quot (+ 100 50) 5)",
            "150 divided by 5"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


SUBJECTS: dict[str, SubjectCurriculum] = {
    s.subject_id: s for s in (
        G2_01, G2_02, G2_03, G2_04, G2_05, G2_06, G2_07, G2_08, G2_09, G2_10,
        G2_11, G2_12, G2_13, G2_14, G2_15, G2_16, G2_17, G2_18, G2_19, G2_20,
        G2_21, G2_22,
    )
}


def smoke_test() -> None:
    from mmllm.aesop.curriculum.generator import generate_subject
    for sid, sub in SUBJECTS.items():
        recs = generate_subject(sub, n_per_example=1, seed=0)
        assert recs, f"no records for {sid}"
        for r in recs:
            assert r.tool_calls[0]["name"] == "eval"
    print(f"grade-2 goose-eggs smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
