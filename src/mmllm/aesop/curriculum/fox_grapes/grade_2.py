"""Grade 2 — operators + arithmetic mastery, taught through fox-grapes.

Grade 2 deepens grade 1's L1+L2 work. Where grade 1 introduced the
single-arg arithmetic call, grade 2 covers multi-arg arithmetic,
comparison chains, the boolean-logic operators, the numeric helpers
(inc/dec/quot/rem/mod, min/max, abs), strings via str, and the
truthy/falsey rules.

The fable lens: the hasty fox's rationalizing dismissals about
answers ('that cluster is too high to bother evaluating!')
consistently lose to the patient fox's disciplined
"let me actually evaluate the form" approach. By grade 2, this becomes
the running joke of the curriculum.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.fox_grapes.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SHARED_SUBPLOTS,
    _PLAN_POOL,
)
from mmllm.aesop.curriculum.fox_grapes._metaphor_pools import (
    _ACORN_SUBPLOTS,
    _BASKET_SUBPLOTS,
    _BEADSTRING_SUBPLOTS,
    _CHALKMARK_SUBPLOTS,
    _GATE_SUBPLOTS,
    _SCRIBE_SUBPLOTS,
    _TALLYWALK_SUBPLOTS,
)


# Extend grade-1's shared pool with two grade-2-specific subplots
# that lean into multi-operand / chained-operator framings.
_SHARED_SUBPLOTS: list[SubplotTemplate] = list(_G1_SHARED_SUBPLOTS) + [
    # 9. The chain-of-operations template — useful for multi-arg
    #    arithmetic and comparison-chain subjects.
    SubplotTemplate("""\
{patient_fox_phrase} had been laying out a chain of small computations on
a slate {place} — one operation, then another, all to settle a
question {hasty_fox_phrase} had raised. The current form on the slate was
{form_display}, and {patient_fox} explained that {concept_phrase} would
be settled the moment the form was evaluated."""),

    # 10. The wager-with-stakes template — increases the dramatic stakes
    #     when the form is more interesting (e.g., min/max, mod).
    SubplotTemplate("""\
"Whatever {form_display} comes to," {hasty_fox_phrase} declared, {emo_proud}
{place}, "I'll wager I know it without typing it." {patient_fox_phrase},
{emo_patient}, picked up a twig and drew {concept_phrase} in the
dust. "Then write the form," {patient_fox_he_she} said. "The REPL will
have the last word.\""""),
]


def _ex(form, expected, concept, what,
        goal="", scenario="", need="", mapping="", resolution="",
        tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal,
                          scenario=scenario, need=need,
                          mapping=mapping, resolution=resolution,
                          tags=tags)


# ─────────────────────── 22 grade-2 subjects ───────────────────────


G2_01 = SubjectCurriculum(
    grade=2, subject_id="G2-01",
    subject_title="Multi-arg arithmetic",
    fable="fox-grapes",
    examples=[
        _ex("(+ 1 2 3 4)", 10,        "the sum (+ 1 2 3 4)",      "the result of (+ 1 2 3 4)"),
        _ex("(* 2 3 4)", 24,          "the product (* 2 3 4)",    "the result of (* 2 3 4)"),
        _ex("(- 100 1 2 3)", 94,      "the chain (- 100 1 2 3)",  "the result of (- 100 1 2 3)"),
        _ex("(+ 1 2 3 4 5 6 7 8 9 10)", 55,
            "the sum 1+2+...+10",       "the sum of integers 1 through 10"),
        _ex("(* 1 2 3 4 5)", 120,     "the product 1*2*3*4*5",    "the product of 1 through 5"),
        _ex("(+ 10 20 30)", 60,       "the sum (+ 10 20 30)",     "the sum of 10, 20, and 30"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_02 = SubjectCurriculum(
    grade=2, subject_id="G2-02",
    subject_title="Comparison chains",
    fable="fox-grapes",
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
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_03 = SubjectCurriculum(
    grade=2, subject_id="G2-03",
    subject_title="not= and = with multiple args",
    fable="fox-grapes",
    examples=[
        _ex("(not= 1 2)",   True,  "the form (not= 1 2)",   "whether 1 differs from 2"),
        _ex("(not= 1 1)",   False, "the form (not= 1 1)",   "whether 1 differs from 1"),
        _ex("(= 1 1 1)",    True,  "the form (= 1 1 1)",    "whether all of 1,1,1 are equal"),
        _ex("(= 1 1 2)",    False, "the form (= 1 1 2)",    "whether 1,1,2 are all equal"),
        _ex("(not= 1 1 2)", True,  "the form (not= 1 1 2)", "whether at least one of 1,1,2 differs"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_04 = SubjectCurriculum(
    grade=2, subject_id="G2-04",
    subject_title="min and max",
    fable="fox-grapes",
    examples=[
        _ex("(min 1 2 3)",  1, "the form (min 1 2 3)",  "the minimum of 1, 2, 3"),
        _ex("(max 1 2 3)",  3, "the form (max 1 2 3)",  "the maximum of 1, 2, 3"),
        _ex("(min 7 3 9 1 5)", 1, "the form (min 7 3 9 1 5)", "the minimum of 7, 3, 9, 1, 5"),
        _ex("(max 7 3 9 1 5)", 9, "the form (max 7 3 9 1 5)", "the maximum of 7, 3, 9, 1, 5"),
        _ex("(min -3 -1 -5)", -5, "the form (min -3 -1 -5)", "the minimum of -3, -1, -5"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_05 = SubjectCurriculum(
    grade=2, subject_id="G2-05",
    subject_title="quot, rem, mod",
    fable="fox-grapes",
    examples=[
        _ex("(quot 17 5)", 3, "the integer quotient of 17 and 5", "the result of (quot 17 5)"),
        _ex("(rem 17 5)",  2, "the remainder of 17 divided by 5", "the result of (rem 17 5)"),
        _ex("(mod 17 5)",  2, "17 mod 5",                          "the result of (mod 17 5)"),
        _ex("(quot 100 7)", 14, "the integer quotient of 100 and 7", "the result of (quot 100 7)"),
        _ex("(rem 100 7)",  2, "the remainder of 100 divided by 7", "the result of (rem 100 7)"),
        _ex("(mod -7 3)",   2, "the form (mod -7 3)",              "the result of (mod -7 3)"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_06 = SubjectCurriculum(
    grade=2, subject_id="G2-06",
    subject_title="inc and dec",
    fable="fox-grapes",
    examples=[
        _ex("(inc 5)",  6, "the form (inc 5)",  "5 plus 1"),
        _ex("(dec 5)",  4, "the form (dec 5)",  "5 minus 1"),
        _ex("(inc 0)",  1, "the form (inc 0)",  "the successor of 0"),
        _ex("(dec 0)", -1, "the form (dec 0)",  "the predecessor of 0"),
        _ex("(inc -1)", 0, "the form (inc -1)", "the successor of -1"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_07 = SubjectCurriculum(
    grade=2, subject_id="G2-07",
    subject_title="Absolute value",
    fable="fox-grapes",
    examples=[
        _ex("(abs 5)",   5, "the form (abs 5)",   "the absolute value of 5"),
        _ex("(abs -5)",  5, "the form (abs -5)",  "the absolute value of -5"),
        _ex("(abs 0)",   0, "the form (abs 0)",   "the absolute value of 0"),
        _ex("(abs (- 3 8))", 5,
            "the form (abs (- 3 8))",
            "the absolute value of 3 minus 8"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_08 = SubjectCurriculum(
    grade=2, subject_id="G2-08",
    subject_title="Arithmetic on ratios",
    fable="fox-grapes",
    examples=[
        _ex("(+ 1/2 1/4)", "3/4",
            "the sum 1/2 + 1/4",       "the value of (+ 1/2 1/4)"),
        _ex("(* 2/3 3/4)", "1/2",
            "the product 2/3 × 3/4",   "the value of (* 2/3 3/4)"),
        _ex("(- 1 1/3)", "2/3",
            "1 minus 1/3",             "the value of (- 1 1/3)"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_09 = SubjectCurriculum(
    grade=2, subject_id="G2-09",
    subject_title="Floats vs ints (the / operator)",
    fable="fox-grapes",
    examples=[
        _ex("(/ 10 2)", 5,    "the integer division 10 ÷ 2",
            "the value of (/ 10 2)"),
        _ex("(/ 10 3)", "10/3", "the form (/ 10 3)",
            "the exact rational result of (/ 10 3)"),
        _ex("(/ 1.0 2)", 0.5, "the float division 1.0 ÷ 2",
            "the value of (/ 1.0 2)"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_10 = SubjectCurriculum(
    grade=2, subject_id="G2-10",
    subject_title="Powers via repeated multiplication",
    fable="fox-grapes",
    examples=[
        _ex("(* 2 2 2)", 8,        "two cubed", "2 to the third power"),
        _ex("(* 5 5)",   25,       "five squared", "5 squared"),
        _ex("(* 3 3 3 3)", 81,     "three to the fourth", "3 to the fourth power"),
        _ex("(* 10 10)", 100,      "ten squared", "10 squared"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_11 = SubjectCurriculum(
    grade=2, subject_id="G2-11",
    subject_title="String concatenation with str",
    fable="fox-grapes",
    examples=[
        _ex('(str "gra" "pes")', "grapes",
            'the form (str "gra" "pes")', 'the joined string "grapes"'),
        _ex('(str "vine")', "vine",
            'the form (str "vine")', 'the value of (str "vine")'),
        _ex('(str "x" "y" "z")',
            "xyz",
            'the three-arg concatenation of single-character strings',
            'the joined cord the three single-letter strings produce',
            goal='concatenate three single-character strings into one',
            scenario="Sly the fox had three short cords of lettered beads on the market-fox's counting-table, each cord just one letter long. The cords sat side by side, ready to be tied head-to-tail in order.",
            need="Sly wanted one continuous cord — the three cords' beads in the order they were laid out, threaded into a single string.",
            mapping="The str form ties cords end-to-end: each argument is a cord of beads, and the result is one long cord. The first arg's beads come first; the next arg's are knotted to its tail; the third's to that tail in turn.",
            resolution='the joined cord carried all three letters in their original order, head-to-tail in one piece, and Sly hung it from the stall.',
            tags=("story",)),
        _ex('(str 1 "+" 2 "=" 3)', "1+2=3",
            'the form (str 1 "+" 2 "=" 3)', 'the joined string "1+2=3"'),
    ],
    subplots=_BEADSTRING_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_12 = SubjectCurriculum(
    grade=2, subject_id="G2-12",
    subject_title="print and println — return values",
    fable="fox-grapes",
    examples=[
        # println side-effects to stdout but RETURNS nil. The form
        # we ask for has the value nil; the model writes println
        # and the runtime returns nil.
        _ex('(println "hello")', None,
            'the form (println "hello")',
            'the return value of calling println'),
        _ex('(print "x")', None,
            'the form (print "x")',
            'the return value of calling print'),
    ],
    subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_13 = SubjectCurriculum(
    grade=2, subject_id="G2-13",
    subject_title="and / or — short circuit, return values",
    fable="fox-grapes",
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
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_14 = SubjectCurriculum(
    grade=2, subject_id="G2-14",
    subject_title="not — turning truthy to false",
    fable="fox-grapes",
    examples=[
        _ex("(not true)",  False, "the form (not true)",  "the value of (not true)"),
        _ex("(not false)", True,  "the form (not false)", "the value of (not false)"),
        _ex("(not nil)",   True,  "the form (not nil)",   "the value of (not nil)"),
        _ex("(not 0)",     False, "the form (not 0)",     "the value of (not 0)"),
        _ex("(not \"\")",  False, "the form (not \"\")",  "the value of (not \"\")"),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_15 = SubjectCurriculum(
    grade=2, subject_id="G2-15",
    subject_title="Falsey values: only false and nil",
    fable="fox-grapes",
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
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_16 = SubjectCurriculum(
    grade=2, subject_id="G2-16",
    subject_title="Truthy 0 and empty string",
    fable="fox-grapes",
    examples=[
        _ex("(boolean 0)",   True,  "the form (boolean 0)",  "the truthiness of 0"),
        _ex("(boolean \"\")", True, "the form (boolean \"\")", "the truthiness of the empty string"),
        _ex("(boolean nil)", False, "the form (boolean nil)", "the truthiness of nil"),
        _ex("(boolean false)", False, "the form (boolean false)", "the truthiness of false"),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_17 = SubjectCurriculum(
    grade=2, subject_id="G2-17",
    subject_title="Keyword as function for map lookup",
    fable="fox-grapes",
    examples=[
        _ex("(:fox {:fox 1 :grapes 2})",
            1,
            'the keyword-as-function lookup at the :fox slot',
            'the value at the :fox slot of the small market-tray',
            goal='look up the value at key :fox in a small map keyed by :fox and :grapes',
            scenario="Vix the fox kept a small market-tray with two named slots: one labeled :fox for the day's pickings and another labeled :grapes for the press's set-aside. Each label held its own tally; she could read either by pointing to its slot.",
            need='Vix wanted the value sitting in the :fox slot — what the day had brought in for her own count. Reaching for the :grapes slot would give her a different number.',
            mapping='A keyword used as a function reads its own slot from the tray. The keyword names the slot; the map is the tray; the REPL fetches the value at the labeled compartment.',
            resolution="the :fox slot yielded its tally, exactly the day's own count, and Vix wrote it down on her parchment.",
            tags=("story",)),
        _ex("(:grapes {:fox 1 :grapes 2})", 2,
            "the form (:grapes {:fox 1 :grapes 2})",
            "the value (:grapes {:fox 1 :grapes 2}) returns"),
        _ex("(:missing {:fox 1})", None,
            "the form (:missing {:fox 1})",
            "the value when a missing keyword is looked up"),
    ],
    subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_18 = SubjectCurriculum(
    grade=2, subject_id="G2-18",
    subject_title="Quoting symbols",
    fable="fox-grapes",
    examples=[
        _ex("(quote fox)", "fox", "the quoted symbol (quote fox)",
            "the value of (quote fox)"),
        _ex("'grapes", "grapes", "the quoted symbol 'grapes",
            "the value of 'grapes"),
        _ex("'(1 2 3)", [1, 2, 3], "the quoted list '(1 2 3)",
            "the value of the quoted list '(1 2 3)"),
    ],
    subplots=_CHALKMARK_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_19 = SubjectCurriculum(
    grade=2, subject_id="G2-19",
    subject_title="Auto-promotion to bigint",
    fable="fox-grapes",
    examples=[
        _ex("(* 1000000 1000000)", 1000000000000,
            "the form (* 1000000 1000000)",
            "the result of one million times one million"),
        _ex("(+ 99999999999 1)", 100000000000,
            "the form (+ 99999999999 1)",
            "the result of 99999999999 plus 1"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_20 = SubjectCurriculum(
    grade=2, subject_id="G2-20",
    subject_title="Counting",
    fable="fox-grapes",
    examples=[
        _ex("(count [1 2 3])",
            3,
            'the length of a small vector',
            "the row's tick-total after the tally-walk",
            goal='count the items in a small vector',
            scenario='Vix the fox walked the vine-row with a slate, ticking off each cluster as she passed it. The row carried three clusters this morning — she would walk it once and report the tally at the end.',
            need="She wanted the row's length — not which clusters were there, just how many — landing on the slate as a single honest number.",
            mapping="The count form is the tally-walk: it visits each item in the collection once, ticking the slate, and returns the tick-total. The walk is the operation; the slate's final number is the return value.",
            resolution="the slate at the row's end held the row's length — Vix's honest tick-count, ready to be posted to the day's harvest log.",
            tags=("story",)),
        _ex("(count \"hello\")",     5, "the count of \"hello\"",
            "the length of the string \"hello\""),
        _ex("(count [])",            0, "the count of an empty vector",
            "the count of an empty vector"),
    ],
    subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_21 = SubjectCurriculum(
    grade=2, subject_id="G2-21",
    subject_title="String length and substring",
    fable="fox-grapes",
    examples=[
        _ex("(count \"grapes\")", 6,  "the length of \"grapes\"",
            "the length of the string \"grapes\""),
        _ex("(count \"fox\")",     3,  "the length of \"fox\"",
            "the length of the string \"fox\""),
        _ex("(subs \"grapes\" 0 3)", "gra",
            "the form (subs \"grapes\" 0 3)",
            "the first three characters of \"grapes\""),
    ],
    subplots=_BEADSTRING_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_22 = SubjectCurriculum(
    grade=2, subject_id="G2-22",
    subject_title="Compose pure arithmetic (multi-step calculation)",
    fable="fox-grapes",
    examples=[
        # A simple reach: jumps × height per jump, then minus a shortfall.
        _ex("(- (* 5 4) 7)", 13,
            "the form (- (* 5 4) 7)",
            "5 jumps of 4 inches, minus a 7-inch shortfall"),
        _ex("(+ (* 3 8) (* 2 4))", 32,
            "the sum of two products",
            "3*8 + 2*4"),
        _ex("(quot (+ 100 50) 5)", 30,
            "the form (quot (+ 100 50) 5)",
            "150 divided by 5"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
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
    print(f"grade-2 fox-grapes smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
