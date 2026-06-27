"""Grade 2 — operators + arithmetic mastery, taught through ant-grasshopper.

Grade 2 deepens grade 1's L1+L2 work. Where grade 1 introduced the
single-arg arithmetic call, grade 2 covers multi-arg arithmetic,
comparison chains, the boolean-logic operators, the numeric helpers
(inc/dec/quot/rem/mod, min/max, abs), strings via str, and the
truthy/falsey rules.

The fable lens: the Grasshopper's hasty boasts about answers ('I can
guess without computing!') consistently lose to the Ant's patient "let
me actually evaluate the form" approach. By grade 2, this becomes the
running joke of the curriculum — the Grasshopper sings of certainty;
the Ant counts grain by grain.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.ant_grasshopper.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SHARED_SUBPLOTS,
    _PLAN_POOL,
)


# Extend grade-1's shared pool with two grade-2-specific subplots
# that lean into multi-operand / chained-operator framings.
_SHARED_SUBPLOTS: list[SubplotTemplate] = list(_G1_SHARED_SUBPLOTS) + [
    # 9. The chain-of-operations template — useful for multi-arg
    #    arithmetic and comparison-chain subjects.
    SubplotTemplate("""\
{ant_phrase} had been laying out a chain of small computations on a
slate {place} — one operation, then another, all to settle a question
{grasshopper_phrase} had raised. The current form on the slate was
{form_display}, and {ant} explained that {concept_phrase} would be
settled the moment the form was evaluated."""),

    # 10. The wager-with-stakes template — increases the dramatic stakes
    #     when the form is more interesting (e.g., min/max, mod).
    #     NOTE: comma after "declared" before {emo_proud} so participle
    #     EMO entries ("boasting at every turn", "puffed up with pride")
    #     parse as adverbial — same pitfall #12 logic that applies to
    #     "said". The audit harness now flags `declared boasting`
    #     without comma alongside `said boasting`.
    SubplotTemplate("""\
"Whatever {form_display} comes to," {grasshopper_phrase} declared,
{emo_proud}, {place}, "I'll wager I know it without typing it."
{ant_phrase}, {emo_patient}, picked up a stick and drew
{concept_phrase} in the dust. "Then write the form," {ant_he_she}
said. "The REPL will have the last word.\""""),
]


def _ex(form, expected, concept, what, tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          tags=tags)


# ─────────────────────── 22 grade-2 subjects ───────────────────────


G2_01 = SubjectCurriculum(
    grade=2, subject_id="G2-01",
    subject_title="Multi-arg arithmetic",
    fable="ant-grasshopper",
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
    fable="ant-grasshopper",
    examples=[
        _ex("(< 1 2 3)",  True,  "the chain (< 1 2 3)",  "whether 1 < 2 < 3"),
        _ex("(< 3 2 1)",  False, "the chain (< 3 2 1)",  "whether 3 < 2 < 1"),
        _ex("(<= 1 1 2)", True,  "the chain (<= 1 1 2)", "whether 1 <= 1 <= 2"),
        _ex("(> 5 4 3 2 1)", True,
            "the chain (> 5 4 3 2 1)",
            "whether the numbers 5,4,3,2,1 are strictly decreasing"),
        _ex("(>= 3 3 2)", True,
            "the chain (>= 3 3 2)",
            "whether 3 >= 3 >= 2"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_03 = SubjectCurriculum(
    grade=2, subject_id="G2-03",
    subject_title="not= and = with multiple args",
    fable="ant-grasshopper",
    examples=[
        _ex("(not= 1 2)",   True,  "the form (not= 1 2)",   "whether 1 differs from 2"),
        _ex("(not= 1 1)",   False, "the form (not= 1 1)",   "whether 1 differs from 1"),
        _ex("(= 1 1 1)",    True,  "the form (= 1 1 1)",    "whether all of 1,1,1 are equal"),
        _ex("(= 1 1 2)",    False, "the form (= 1 1 2)",    "whether all of 1,1,2 are equal"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_04 = SubjectCurriculum(
    grade=2, subject_id="G2-04",
    subject_title="min and max",
    fable="ant-grasshopper",
    examples=[
        _ex("(min 1 2 3)", 1, "the form (min 1 2 3)", "the smallest of 1, 2, 3"),
        _ex("(max 1 2 3)", 3, "the form (max 1 2 3)", "the largest of 1, 2, 3"),
        _ex("(min 5 -2 0 9)", -2, "the form (min 5 -2 0 9)", "the minimum of the four"),
        _ex("(max 5 -2 0 9)", 9, "the form (max 5 -2 0 9)", "the maximum of the four"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_05 = SubjectCurriculum(
    grade=2, subject_id="G2-05",
    subject_title="quot, rem, mod",
    fable="ant-grasshopper",
    examples=[
        _ex("(quot 17 5)", 3, "the form (quot 17 5)", "the integer quotient of 17 by 5"),
        _ex("(rem 17 5)",  2, "the form (rem 17 5)",  "the remainder of 17 by 5"),
        _ex("(mod 17 5)",  2, "the form (mod 17 5)",  "the modulo of 17 by 5"),
        _ex("(mod -1 5)",  4, "the form (mod -1 5)",  "the modulo of -1 by 5 (positive)"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_06 = SubjectCurriculum(
    grade=2, subject_id="G2-06",
    subject_title="inc and dec",
    fable="ant-grasshopper",
    examples=[
        _ex("(inc 4)",  5, "the form (inc 4)",  "the value of (inc 4)"),
        _ex("(dec 4)",  3, "the form (dec 4)",  "the value of (dec 4)"),
        _ex("(inc -1)", 0, "the form (inc -1)", "the value of (inc -1)"),
        _ex("(dec 0)", -1, "the form (dec 0)",  "the value of (dec 0)"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_07 = SubjectCurriculum(
    grade=2, subject_id="G2-07",
    subject_title="abs (absolute value)",
    fable="ant-grasshopper",
    examples=[
        _ex("(Math/abs -7)", 7, "the form (Math/abs -7)", "the absolute value of -7"),
        _ex("(Math/abs 0)",  0, "the form (Math/abs 0)",  "the absolute value of 0"),
        _ex("(Math/abs 9)",  9, "the form (Math/abs 9)",  "the absolute value of 9"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_08 = SubjectCurriculum(
    grade=2, subject_id="G2-08",
    subject_title="Arithmetic on ratios",
    fable="ant-grasshopper",
    examples=[
        _ex("(+ 1/2 1/4)", "3/4", "the form (+ 1/2 1/4)", "the value of one-half plus one-quarter"),
        _ex("(* 2/3 3/4)", "1/2", "the form (* 2/3 3/4)", "the value of two-thirds times three-quarters"),
        _ex("(- 1 1/3)", "2/3", "the form (- 1 1/3)", "the value of one minus one-third"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_09 = SubjectCurriculum(
    grade=2, subject_id="G2-09",
    subject_title="Floats vs ints",
    fable="ant-grasshopper",
    examples=[
        _ex("(/ 10 2)", 5, "the form (/ 10 2)", "the integer quotient when division is exact"),
        _ex("(/ 10 4)", "5/2", "the form (/ 10 4)", "the rational form when 10 doesn't divide 4 evenly"),
        _ex("(/ 10.0 4)", 2.5, "the form (/ 10.0 4)", "the float form when one operand is a float"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_10 = SubjectCurriculum(
    grade=2, subject_id="G2-10",
    subject_title="Power by repeated multiplication",
    fable="ant-grasshopper",
    examples=[
        _ex("(* 2 2 2)",     8,    "the cubed product (* 2 2 2)", "the result of two cubed"),
        _ex("(* 3 3 3 3)",   81,   "the fourth-power product (* 3 3 3 3)",                          "the result of three to the fourth"),
        _ex("(* 5 5)",       25,   "the squared product (* 5 5)",                        "the result of five squared"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_11 = SubjectCurriculum(
    grade=2, subject_id="G2-11",
    subject_title="String concatenation with str",
    fable="ant-grasshopper",
    examples=[
        _ex('(str "a" "b")',     "ab",     'the form (str "a" "b")',     "the concatenated string ab"),
        _ex('(str "ant-" 42)',   "ant-42", 'the form (str "ant-" 42)',   'the string "ant-42" from mixing types'),
        _ex('(str)',             "",       'the form (str) with no args', "the empty string from no arguments"),
        _ex('(str "winter " "is " "coming")', "winter is coming",
            'the three-arg str form',
            'the joined string "winter is coming"'),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_12 = SubjectCurriculum(
    grade=2, subject_id="G2-12",
    subject_title="print and println",
    fable="ant-grasshopper",
    examples=[
        # `with-out-str` captures *out* so we can verify what print
        # actually emitted without depending on the side effect.
        _ex('(with-out-str (print "x"))',  "x",  'a captured (print "x")', 'the captured output of (print "x")'),
        _ex('(with-out-str (println "x"))', "x\n", 'a captured (println "x")', 'the captured output of (println "x")'),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_13 = SubjectCurriculum(
    grade=2, subject_id="G2-13",
    subject_title="and / or — short-circuit and value",
    fable="ant-grasshopper",
    examples=[
        _ex("(and 1 2 3)",          3,     "the form (and 1 2 3)",          "the last truthy value of and"),
        _ex("(and 1 nil 3)",        None,  "the form (and 1 nil 3)",        "the value of and when one arg is nil"),
        _ex("(or nil false :found)", ":found", "the form (or nil false :found)", "the first truthy value of or"),
        _ex("(or nil false)",       False, "the form (or nil false)",       "the value of or when nothing is truthy"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_14 = SubjectCurriculum(
    grade=2, subject_id="G2-14",
    subject_title="not — turning truthy to false",
    fable="ant-grasshopper",
    examples=[
        _ex("(not true)",  False, "the form (not true)",  "the negation of true"),
        _ex("(not false)", True,  "the form (not false)", "the negation of false"),
        _ex("(not nil)",   True,  "the form (not nil)",   "the negation of nil"),
        _ex("(not 0)",     False, "the form (not 0)", "the negation of 0"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_15 = SubjectCurriculum(
    grade=2, subject_id="G2-15",
    subject_title="Falsey values",
    fable="ant-grasshopper",
    examples=[
        _ex("(boolean nil)",   False, "the form (boolean nil)",   "the truthiness of nil"),
        _ex("(boolean false)", False, "the form (boolean false)", "the truthiness of false"),
        _ex("(boolean 0)",     True,  "the form (boolean 0)",     "the truthiness of 0"),
        _ex('(boolean "")',    True,  'the form (boolean "")',    "the truthiness of the empty string"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_16 = SubjectCurriculum(
    grade=2, subject_id="G2-16",
    subject_title="Coercion pitfalls in if",
    fable="ant-grasshopper",
    examples=[
        _ex("(if 0 :a :b)", ":a", "the if form on 0", "which branch (if 0 ...) takes"),
        _ex("(if \"\" :a :b)", ":a", "the form (if \"\" :a :b)", "which branch the empty string takes"),
        _ex("(if nil :a :b)", ":b", "the form (if nil :a :b)", "which branch nil takes"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_17 = SubjectCurriculum(
    grade=2, subject_id="G2-17",
    subject_title="Keyword as function",
    fable="ant-grasshopper",
    examples=[
        _ex("(:a {:a 1 :b 2})", 1, "the form (:a {:a 1 :b 2})", "the value at :a in the map"),
        _ex("(:missing {:a 1})", None, "the form (:missing {:a 1})", "what (:missing m) returns when key absent"),
        _ex("(:a {:a 1} :default)", 1, "the form (:a {:a 1} :default)", "the value at :a (default unused)"),
        _ex("(:missing {:a 1} :default)", ":default",
            "the form (:missing {:a 1} :default)",
            "the default returned when key absent"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_18 = SubjectCurriculum(
    grade=2, subject_id="G2-18",
    subject_title="Symbols evaluate to their bindings",
    fable="ant-grasshopper",
    examples=[
        _ex("(do (def grain 5) grain)", 5,
            "the form (do (def grain 5) grain)",
            "the value the symbol grain evaluates to"),
        _ex("(do (def winter :coming) winter)", ":coming",
            "the form (do (def winter :coming) winter)",
            "the value the symbol winter evaluates to"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_19 = SubjectCurriculum(
    grade=2, subject_id="G2-19",
    subject_title="Quoting introduction",
    fable="ant-grasshopper",
    examples=[
        _ex("'ant", "ant", "the quoted symbol 'ant", "the quoted symbol's value"),
        _ex("(quote grain)", "grain", "the form (quote grain)", "the value of (quote grain)"),
        _ex("'(1 2 3)", [1, 2, 3], "the quoted list '(1 2 3)", "the list as a value"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_20 = SubjectCurriculum(
    grade=2, subject_id="G2-20",
    subject_title="Numeric tower (auto-promotion)",
    fable="ant-grasshopper",
    examples=[
        _ex("(* 1000 1000)", 1000000, "the form (* 1000 1000)", "the product of 1000 and 1000"),
        _ex("(/ 1 3)", "1/3", "the form (/ 1 3) — exact rational", "the value as an exact ratio"),
        _ex("(+ 1 1.5)", 2.5, "the form (+ 1 1.5) — int promoted to float", "the float result"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_21 = SubjectCurriculum(
    grade=2, subject_id="G2-21",
    subject_title="rand and rand-int",
    fable="ant-grasshopper",
    examples=[
        # Both calls return non-deterministic values; we test type/range
        # via predicates that ARE deterministic.
        _ex("(integer? (rand-int 10))", True,
            "the predicate that (rand-int 10) returns an integer",
            "whether (rand-int 10) is integer-typed"),
        _ex("(let [r (rand-int 10)] (and (>= r 0) (< r 10)))", True,
            "the bounds-check on (rand-int 10)",
            "whether (rand-int 10) lies in 0..9"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_22 = SubjectCurriculum(
    grade=2, subject_id="G2-22",
    subject_title="Composing pure arithmetic",
    fable="ant-grasshopper",
    examples=[
        # Multi-step calculations in one expression — the kind of thing
        # the Ant uses to compute "how many days the stockpile lasts."
        _ex("(quot (* 30 5) 2)", 75,
            "a multi-step arithmetic form",
            "the result of dividing thirty-times-five by two"),
        _ex("(- (* 4 5) (+ 2 3))", 15,
            "a difference of two products",
            "the value of (- (* 4 5) (+ 2 3))"),
        _ex("(+ (quot 10 3) (rem 10 3))", 4,
            "the sum of quotient and remainder",
            "the result of (+ (quot 10 3) (rem 10 3))"),
    ],
    subplots=_SHARED_SUBPLOTS, plan_pool=_PLAN_POOL,
)


SUBJECTS: dict[str, SubjectCurriculum] = {
    s.subject_id: s for s in (
        G2_01, G2_02, G2_03, G2_04, G2_05, G2_06, G2_07, G2_08,
        G2_09, G2_10, G2_11, G2_12, G2_13, G2_14, G2_15, G2_16,
        G2_17, G2_18, G2_19, G2_20, G2_21, G2_22,
    )
}


def smoke_test() -> None:
    from mmllm.aesop.curriculum.generator import generate_subject
    for sid, sub in SUBJECTS.items():
        recs = generate_subject(sub, n_per_example=1, seed=0)
        for r in recs:
            assert r.tool_calls[0]["name"] == "eval"
    print(f"grade-2 ant-grasshopper smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
