"""Grade 2 — operators + arithmetic mastery, taught through crow-pitcher.

Grade 2 deepens grade 1's L1+L2 work. Where grade 1 introduced the
single-arg arithmetic call, grade 2 covers multi-arg arithmetic,
comparison chains, the boolean-logic operators, the numeric helpers
(inc/dec/quot/rem/mod, min/max, abs), strings via str, and the
truthy/falsey rules.

The fable lens: the Hare's hasty boasts about answers ('I can guess
without computing!') consistently lose to the Tortoise's patient
"let me actually evaluate the form" approach. By grade 2, this becomes
the running joke of the curriculum.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.crow_pitcher.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SHARED_SUBPLOTS,
    _GOAL_SUBPLOTS,
    _PLAN_POOL,
)
from mmllm.aesop.curriculum.crow_pitcher._metaphor_pools import (
    _ACORN_SUBPLOTS, _BASKET_SUBPLOTS, _BEADSTRING_SUBPLOTS, _CHALKMARK_SUBPLOTS, _GATE_SUBPLOTS, _SCRIBE_SUBPLOTS, _TALLYWALK_SUBPLOTS,
)


# Extend grade-1's shared pool with two grade-2-specific subplots
# that lean into multi-operand / chained-operator framings.
_SHARED_SUBPLOTS: list[SubplotTemplate] = list(_G1_SHARED_SUBPLOTS) + [
    # 9. The chain-of-operations template — useful for multi-arg
    #    arithmetic and comparison-chain subjects.
    SubplotTemplate("""\
{tortoise_phrase} had been laying out a chain of small computations on
a slate {place} — one operation, then another, all to settle a
question {hare_phrase} had raised. The current form on the slate was
{form_display}, and {tortoise} explained that {concept_phrase} would
be settled the moment the form was evaluated."""),

    # 10. The wager-with-stakes template — increases the dramatic stakes
    #     when the form is more interesting (e.g., min/max, mod).
    SubplotTemplate("""\
"Whatever {form_display} comes to," {hare_phrase} declared, {emo_proud},
{place}, "I'll wager I know it without typing it." {tortoise_phrase},
{emo_patient}, picked up a stick and drew {concept_phrase} in the
dust. "Then write the form," {tortoise_he_she} said. "The REPL will
have the last word.\""""),
]


def _ex(form, expected, concept, what, goal="", tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal, tags=tags)


# ─────────────────────── 22 grade-2 subjects ───────────────────────


G2_01 = SubjectCurriculum(
    grade=2, subject_id="G2-01",
    subject_title="Multi-arg arithmetic",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(+ 1 2 3 4)", expected=10,
            concept_phrase="the multi-arg sum",
            question_what="the sum of 1, 2, 3, and 4",
            goal_text="add 1, 2, 3, and 4",
        ),
        _ex("(* 2 3 4)", 24,          "the multi-arg product",    "the product of 2, 3, and 4",
            goal="multiply 2, 3, and 4"),
        _ex("(- 100 1 2 3)", 94,      "the multi-arg subtraction",  "100 minus 1, 2, and 3",
            goal="subtract 1, 2, and 3 from 100"),
        _ex("(+ 1 2 3 4 5 6 7 8 9 10)", 55,
            "the sum of ten numbers",       "the sum of integers 1 through 10",
            goal="add the integers 1 through 10"),
        _ex("(* 1 2 3 4 5)", 120,     "the multi-arg product",    "the product of 1 through 5",
            goal="multiply the integers 1 through 5"),
        _ex("(+ 10 20 30)", 60,       "the sum of three numbers",     "the sum of 10, 20, and 30",
            goal="add 10, 20, and 30"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_02 = SubjectCurriculum(
    grade=2, subject_id="G2-02",
    subject_title="Comparison chains",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(< 1 2 3)", expected=True,
            concept_phrase="the less-than chain",
            question_what="whether 1 < 2 < 3",
            goal_text="test whether 1 is less than 2 and 2 is less than 3",
        ),
        _ex("(< 3 2 1)",  False, "the less-than chain",  "whether 3 < 2 < 1",
            goal="test whether 3 is less than 2 and 2 is less than 1"),
        _ex("(<= 1 1 2)", True,  "the less-than-or-equal chain", "whether 1 ≤ 1 ≤ 2",
            goal="test whether 1 is less than or equal to 1 and 1 is less than or equal to 2"),
        _ex("(> 5 4 3 2 1)", True,
            "the greater-than chain",
            "whether the numbers are strictly decreasing",
            goal="test whether 5 > 4 > 3 > 2 > 1"),
        _ex("(>= 3 3 2)", True,
            "the greater-than-or-equal chain",
            "whether 3 ≥ 3 ≥ 2",
            goal="test whether 3 is greater than or equal to 3 and 3 is greater than or equal to 2"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_03 = SubjectCurriculum(
    grade=2, subject_id="G2-03",
    subject_title="not= and = with multiple args",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(not= 1 2)", expected=True,
            concept_phrase="the inequality check",
            question_what="whether 1 differs from 2",
            goal_text="test whether 1 and 2 are not equal",
        ),
        _ex("(not= 1 1)",   False, "the inequality check",   "whether 1 differs from itself",
            goal="test whether 1 and 1 are not equal"),
        _ex("(= 1 1 1)",    True,  "the equality check",    "whether all three are equal",
            goal="test whether 1, 1, and 1 are all equal"),
        _ex("(= 1 1 2)",    False, "the equality check",    "whether all three are equal",
            goal="test whether 1, 1, and 2 are all equal"),
        _ex("(not= 1 1 2)", True,  "the inequality check", "whether at least one differs",
            goal="test whether at least one of 1, 1, and 2 is not equal to the others"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_04 = SubjectCurriculum(
    grade=2, subject_id="G2-04",
    subject_title="min and max",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(min 1 2 3)",
            expected=1,
            concept_phrase="the minimum of three numbers",
            question_what="the smallest of 1, 2, and 3",
            goal_text="find the minimum of 1, 2, and 3",
        ),
        _ex("(max 1 2 3)",  3, "the maximum of three numbers",  "the largest of 1, 2, and 3",
            goal="find the maximum of 1, 2, and 3"),
        _ex("(min 7 3 9 1 5)", 1, "the minimum of five numbers", "the smallest of 7, 3, 9, 1, and 5",
            goal="find the minimum of 7, 3, 9, 1, and 5"),
        _ex("(max 7 3 9 1 5)", 9, "the maximum of five numbers", "the largest of 7, 3, 9, 1, and 5",
            goal="find the maximum of 7, 3, 9, 1, and 5"),
        _ex("(min -3 -1 -5)", -5, "the minimum of three numbers", "the smallest of -3, -1, and -5",
            goal="find the minimum of -3, -1, and -5"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_05 = SubjectCurriculum(
    grade=2, subject_id="G2-05",
    subject_title="quot, rem, mod",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(quot 17 5)", expected=3,
            concept_phrase="the integer quotient",
            question_what="17 divided by 5, without remainder",
            goal_text="find the integer quotient of 17 divided by 5",
        ),
        _ex("(rem 17 5)",  2, "the remainder", "the remainder when 17 is divided by 5",
            goal="find the remainder when 17 is divided by 5"),
        _ex("(mod 17 5)",  2, "the modulo operation",                          "17 mod 5",
            goal="find 17 modulo 5"),
        _ex("(quot 100 7)", 14, "the integer quotient", "100 divided by 7, without remainder",
            goal="find the integer quotient of 100 divided by 7"),
        _ex("(rem 100 7)",  2, "the remainder", "the remainder when 100 is divided by 7",
            goal="find the remainder when 100 is divided by 7"),
        _ex("(mod -7 3)",   2, "the modulo operation",              "negative seven mod 3",
            goal="find negative 7 modulo 3"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_06 = SubjectCurriculum(
    grade=2, subject_id="G2-06",
    subject_title="inc and dec",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(inc 5)", expected=6,
            concept_phrase="the increment operation",
            question_what="5 plus 1",
            goal_text="increment 5 by 1",
        ),
        _ex("(dec 5)",  4, "the decrement operation",  "5 minus 1",
            goal="decrement 5 by 1"),
        _ex("(inc 0)",  1, "the increment operation",  "0 plus 1",
            goal="increment 0"),
        _ex("(dec 0)", -1, "the decrement operation",  "0 minus 1",
            goal="decrement 0"),
        _ex("(inc -1)", 0, "the increment operation", "negative 1 plus 1",
            goal="increment negative 1"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_07 = SubjectCurriculum(
    grade=2, subject_id="G2-07",
    subject_title="Absolute value",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(abs 5)", expected=5,
            concept_phrase="the absolute value",
            question_what="the absolute value of 5",
            goal_text="find the absolute value of 5",
        ),
        _ex("(abs -5)",  5, "the absolute value",  "the absolute value of negative 5",
            goal="find the absolute value of negative 5"),
        _ex("(abs 0)",   0, "the absolute value",   "the absolute value of 0",
            goal="find the absolute value of 0"),
        _ex("(abs (- 3 8))", 5,
            "the absolute value",
            "the absolute value of the difference between 3 and 8",
            goal="find the absolute value of 3 minus 8"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_08 = SubjectCurriculum(
    grade=2, subject_id="G2-08",
    subject_title="Arithmetic on ratios",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(+ 1/2 1/4)", expected="3/4",
            concept_phrase="the sum of two ratios",
            question_what="the sum of one-half and one-quarter",
            goal_text="add one-half and one-quarter",
        ),
        _ex("(* 2/3 3/4)", "1/2",
            "the product of two ratios",   "the product of two-thirds and three-quarters",
            goal="multiply two-thirds by three-quarters"),
        _ex("(- 1 1/3)", "2/3",
            "the difference of a whole and a ratio",             "1 minus one-third",
            goal="subtract one-third from 1"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_09 = SubjectCurriculum(
    grade=2, subject_id="G2-09",
    subject_title="Floats vs ints (the / operator)",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(/ 10 2)", expected=5,
            concept_phrase="the division operation",
            question_what="the result of using / on 10 and 2",
            goal_text="divide 10 by 2",
        ),
        _ex("(/ 10 3)", "10/3", "the division operation",
            "the exact rational result of using / on 10 and 3",
            goal="divide 10 by 3"),
        _ex("(/ 1.0 2)", 0.5, "the division operation",
            "the result of 1.0 divided by 2",
            goal="divide 1.0 by 2"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_10 = SubjectCurriculum(
    grade=2, subject_id="G2-10",
    subject_title="Powers via repeated multiplication",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(* 2 2 2)", expected=8,
            concept_phrase="repeated multiplication",
            question_what="2 to the third power",
            goal_text="multiply 2 by itself three times",
        ),
        _ex("(* 5 5)",   25,       "repeated multiplication", "5 to the second power",
            goal="multiply 5 by itself"),
        _ex("(* 3 3 3 3)", 81,     "repeated multiplication", "3 to the fourth power",
            goal="multiply 3 by itself four times"),
        _ex("(* 10 10)", 100,      "repeated multiplication", "10 to the second power",
            goal="multiply 10 by itself"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_11 = SubjectCurriculum(
    grade=2, subject_id="G2-11",
    subject_title="String concatenation with str",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form='(str "ab" "cd")',
            expected="abcd",
            concept_phrase='the string concatenation',
            question_what='the result of using str to splice "ab" and "cd"',
            goal_text='use str to splice the two-letter strings "ab" and "cd" into a single thread',

            scenario=(
                "Korvus had two short pebble-strings woven on separate vines "
                "in the garden: one threaded a-b, the other c-d. He needed "
                "a single vine stringing all four pebbles in sequence."
            ),
            need=(
                "He wanted to join the two vines end-to-end into one "
                "continuous pebble-string, the second starting exactly "
                "where the first left off."
            ),
            mapping=(
                "`str` joins any number of string values into one, "
                "concatenating left to right. Each vine is appended to "
                "the previous; the result is one pebble-string in order."
            ),
            resolution=(
                "a single vine carrying all four pebbles in sequence, "
                "the join seamless, the pebble-string complete at beak-reach."
            ),
            tags=("story",),
        ),
        _ex('(str 42)', "42",
            'the string coercion of an integer',
            'the result of using str on the integer 42',
            goal='use str to coerce the integer 42 to its string representation'),
        _ex('(str "p" "q" "r")', "pqr",
            'the three-arg string concatenation',
            'the result of using str to join "p", "q", and "r"',
            goal='use str to join the three single-character strings "p", "q", and "r"'),
        _ex('(str 1 "+" 2 "=" 3)', "1+2=3",
            'the mixed string concatenation',
            'the result of using str to join 1, "+", 2, "=", and 3',
            goal='use str to join the integer 1, the plus sign, the integer 2, the equals sign, and the integer 3'),
    ],
    subplots=_BEADSTRING_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_12 = SubjectCurriculum(
    grade=2, subject_id="G2-12",
    subject_title="print and println — return values",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form='(println "hello")', expected=None,
            concept_phrase='the print-line call',
            question_what='the return value of using println on the string "hello"',
            goal_text='print the string "hello" with a newline',
        ),
        _ex('(print "x")', None,
            'the print call',
            'the return value of using print on the string "x"',
            goal='print the string "x" without a newline'),
    ],
    subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_13 = SubjectCurriculum(
    grade=2, subject_id="G2-13",
    subject_title="and / or — short circuit, return values",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(and true true)",
            expected=True,
            concept_phrase="the logical and",
            question_what="the result of passing true and true through the and-chain of gates",
            goal_text="test whether two trues both pass through an and-chain of gates",
        ),
        _ex("(and true false)",  False,  "the logical and",
            "the result of using and on true and false",
            goal="test true and false with the and operator"),
        _ex("(or false true)",   True,   "the logical or",
            "the result of using or on false and true",
            goal="test false or true with the or operator"),
        _ex("(or false false)",  False,  "the logical or",
            "the result of using or on false and false",
            goal="test false or false with the or operator"),
        _ex("(and 1 2 3)",       3,      "the logical and",
            "the result of using and on 1, 2, and 3",
            goal="apply and to 1, 2, and 3"),
        _ex("(or nil false 5)",  5,      "the logical or",
            "the result of using or on nil, false, and 5",
            goal="apply or to nil, false, and 5"),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_14 = SubjectCurriculum(
    grade=2, subject_id="G2-14",
    subject_title="not — turning truthy to false",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(not true)", expected=False,
            concept_phrase="the logical not",
            question_what="the result of using not on true",
            goal_text="negate the value true",
        ),
        _ex("(not false)", True,  "the logical not", "the result of using not on false",
            goal="negate the value false"),
        _ex("(not nil)",   True,  "the logical not",   "the result of using not on nil",
            goal="negate the value nil"),
        _ex("(not 0)",     False, "the logical not",     "the result of using not on 0",
            goal="negate the value 0"),
        _ex("(not \"\")",  False, "the logical not",  "the result of using not on the empty string",
            goal="negate the empty string"),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_15 = SubjectCurriculum(
    grade=2, subject_id="G2-15",
    subject_title="Falsey values: only false and nil",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(if 0 1 0)", expected=1,
            concept_phrase="the if conditional with zero as condition",
            question_what="the result of if with condition 0, then-branch 1, else-branch 0",
            goal_text="use if to return 1 when the condition is 0 (then-branch) and 0 otherwise (else-branch)",
        ),
        _ex("(if \"\" 1 0)", 1, "the if conditional with empty string as condition",
            "the result of if with condition the empty string, then-branch 1, else-branch 0",
            goal="use if to return 1 when the condition is the empty string (then-branch) and 0 otherwise (else-branch)"),
        _ex("(if nil 1 0)", 0, "the if conditional with nil as condition",
            "the result of if with condition nil, then-branch 1, else-branch 0",
            goal="use if to return 1 when the condition is nil (then-branch) and 0 otherwise (else-branch)"),
        _ex("(if false 1 0)", 0, "the if conditional with false as condition",
            "the result of if with condition false, then-branch 1, else-branch 0",
            goal="use if to return 1 when the condition is false (then-branch) and 0 otherwise (else-branch)"),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_16 = SubjectCurriculum(
    grade=2, subject_id="G2-16",
    subject_title="Truthy 0 and empty string",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(boolean 0)", expected=True,
            concept_phrase="the boolean conversion",
            question_what="the result of using boolean on 0",
            goal_text="convert 0 to a boolean",
        ),
        _ex("(boolean \"\")", True, "the boolean conversion", "the result of using boolean on the empty string",
            goal="convert the empty string to a boolean"),
        _ex("(boolean nil)", False, "the boolean conversion", "the result of using boolean on nil",
            goal="convert nil to a boolean"),
        _ex("(boolean false)", False, "the boolean conversion", "the result of using boolean on false",
            goal="convert false to a boolean"),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_17 = SubjectCurriculum(
    grade=2, subject_id="G2-17",
    subject_title="Keyword as function for map lookup",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(:hare {:hare 1 :tortoise 2})", expected=1,
            concept_phrase="the keyword lookup",
            question_what="the result of using the keyword :hare as a function on the map {:hare 1 :tortoise 2}",
            goal_text="use the keyword :hare to look up a value in the map with keys :hare and :tortoise",

            scenario=(
                "Sable arranged two pebbles on the pitcher's rim near the "
                "hilltop: one marked :hare carrying the count 1, another "
                "marked :tortoise carrying 2. The pile sat in order, side by side."
            ),
            need=(
                "She wanted only the count beneath the :hare stone without "
                "lifting or moving the :tortoise stone at all."
            ),
            mapping=(
                "A map is a labelled stone-pile. Using :hare as a function "
                "reaches into the pile and pulls only the value under that label, "
                "leaving every other stone exactly in place."
            ),
            resolution=(
                "1 — the :hare stone's count, lifted cleanly from the pile "
                "without disturbing its neighbour."
            ),
            tags=("story",),
        ),
        _ex("(:tortoise {:hare 1 :tortoise 2})", 2,
            "the keyword lookup",
            "the result of using the keyword :tortoise as a function on the map {:hare 1 :tortoise 2}",
            goal="use the keyword :tortoise to look up a value in the map with keys :hare and :tortoise"),
        _ex("(:missing {:hare 1})", None,
            "the keyword lookup",
            "the result of using the keyword :missing as a function on the map {:hare 1}",
            goal="use the keyword :missing to look up a value in a map that does not contain :missing"),
    ],
    subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_18 = SubjectCurriculum(
    grade=2, subject_id="G2-18",
    subject_title="Quoting symbols",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(symbol? (quote hare))", expected=True,
            concept_phrase="the symbol-predicate applied to a long-form-quoted name",
            question_what="whether long-form quoting produces a symbol",
            goal_text="ask whether long-form quoting of the name hare produces a symbol, using symbol?",
        ),
        _ex("(= (quote tortoise) 'tortoise)", True,
            "the equality of long-form and short-form quoting",
            "whether long-form and short-form quoting produce equal values",
            goal="compare the result of long-form quoting of tortoise against the apostrophe-shorthand quoting of the same name, using ="),
        _ex("(count '(1 2 3))", 3,
            "the element count of a quoted list",
            "the number of elements in a quoted list",
            goal="count the elements in a quoted list of the integers 1, 2, and 3"),
    ],
    subplots=_CHALKMARK_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_19 = SubjectCurriculum(
    grade=2, subject_id="G2-19",
    subject_title="Auto-promotion to bigint",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(* 1000000 1000000)", expected=1000000000000,
            concept_phrase="the large multiplication",
            question_what="the product of one million and one million",
            goal_text="multiply one million by one million",
        ),
        _ex("(+ 99999999999 1)", 100000000000,
            "the large addition",
            "the sum of 99999999999 and 1",
            goal="add 1 to 99999999999"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_20 = SubjectCurriculum(
    grade=2, subject_id="G2-20",
    subject_title="Counting",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(count [1 2 3])", expected=3,
            concept_phrase="the count operation",
            question_what="the result of using count on the vector containing 1, 2, and 3",
            goal_text="count the elements in the vector containing 1, 2, and 3",

            scenario=(
                "Sable walked the pitcher's rim in the village, three smooth "
                "stones set in a row along the clay ledge: 1, 2, 3. She "
                "carried her running tally in one talon, marking each stone "
                "as she passed."
            ),
            need=(
                "She needed the total count of the row — how many pebbles "
                "sat along the rim before she dropped them."
            ),
            mapping=(
                "`count` walks the collection talon-mark by talon-mark, "
                "incrementing the running tally at each element. When the "
                "last stone is passed, the final tally is the return value."
            ),
            resolution=(
                "3 — three passes made, three stones counted, the tally "
                "settling as the answer."
            ),
            tags=("story",),
        ),
        _ex("(count \"hello\")",     5, "the count operation",
            "the result of using count on the string hello",
            goal="count the characters in the string hello"),
        _ex("(count [])",            0, "the count operation",
            "the result of using count on the empty vector",
            goal="count the elements in an empty vector"),
    ],
    subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_21 = SubjectCurriculum(
    grade=2, subject_id="G2-21",
    subject_title="String length and substring",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(count \"tortoise\")", expected=8,
            concept_phrase="the count of characters in a string",
            question_what="the result of using count on the string tortoise",
            goal_text="count the characters in the string tortoise",
        ),
        _ex("(count \"hare\")",     4,  "the count of characters in a string",
            "the result of using count on the string hare",
            goal="count the characters in the string hare"),
        _ex("(count (subs \"tortoise\" 0 3))", 3,
            "the count of characters in a leading substring",
            "the count of the substring from index 0 to 3 of the string tortoise",
            goal="extract the leading three characters from the string tortoise using subs from index 0 to 3, then count them"),
    ],
    subplots=_BEADSTRING_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_22 = SubjectCurriculum(
    grade=2, subject_id="G2-22",
    subject_title="Compose pure arithmetic (multi-step calculation)",
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(- (* 5 4) 7)", expected=13,
            concept_phrase="the nested arithmetic",
            question_what="the result of multiplying 5 and 4, then subtracting 7",
            goal_text="compute 5 times 4, then subtract 7",
        ),
        _ex("(+ (* 3 8) (* 2 4))", 32,
            "the sum of products",
            "the result of adding the product of 3 and 8 to the product of 2 and 4",
            goal="compute the product of 3 and 8, add the product of 2 and 4"),
        _ex("(quot (+ 100 50) 5)", 30,
            "the nested quotient",
            "the integer quotient of the sum of 100 and 50 divided by 5",
            goal="add 100 and 50, then divide by 5"),
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
    print(f"grade-2 crow-pitcher smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
