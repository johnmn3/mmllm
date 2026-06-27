"""Grade 2 — operators + arithmetic mastery, taught through tortoise-hare.

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
from mmllm.aesop.curriculum.tortoise_hare.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SHARED_SUBPLOTS,
    _GOAL_SUBPLOTS,
    _PLAN_POOL,
)
from mmllm.aesop.curriculum.tortoise_hare._metaphor_pools import (
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(+ 1 2 3 4)", expected=10,
            concept_phrase="the multi-arg sum",
            question_what="the sum of 1, 2, 3, and 4",
            goal_text="add 1, 2, 3, and 4",
            scenario=(
                "Mossback the tortoise laid out four small acorn-heaps on a flat stone — the day's four foraging trips, one heap per trip, counted as {drawn.a}, then {drawn.b}, then {drawn.c}, then 4."
            ),
            need=(
                "She wanted to know the total acorns gathered across all four trips, to "
                "measure the day's success before the storage bins."
            ),
            mapping=(
                "`+` combines multiple heaps by adding their counts together. Each heap's count stays the same; only the running total — the sum of {drawn.a}, {drawn.b}, {drawn.c}, and {drawn.d} — comes back."
            ),
            resolution=(
                "the runtime returned the total count of the day's four trips gathered into "
                "one running sum."
            ),
            tags=("story",),
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(< 1 2 3)", expected=True,
            concept_phrase="the less-than chain",
            question_what="whether 1 < 2 < 3",
            goal_text="test whether 1 is less than 2 and 2 is less than 3",
            scenario=(
                'Pip the hare had three acorn-counts laid out on a tally stone — {drawn.a}, then {drawn.b}, then {drawn.c}, the counts rising from left to right. Mossback the tortoise studied the line.'
            ),
            need=(
                "Pip wanted to know whether each count was strictly bigger than the one before, "
                "so the heap-sizes showed proper growth from dawn to dusk."
            ),
            mapping=(
                '`<` checks whether all {drawn.c} counts climb: first smaller than second, second smaller than third. If all links in the chain hold, the verdict comes back true; if any link breaks, the verdict is false.'
            ),
            resolution=(
                "the runtime confirmed the chain held — each acorn-count was strictly larger than "
                "the one before it."
            ),
            tags=("story",),
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(not= 1 2)", expected=True,
            concept_phrase="the inequality check",
            question_what="whether 1 differs from 2",
            goal_text="test whether 1 and 2 are not equal",
            scenario=(
                'Mossback the tortoise compared two acorn-heaps placed side by side — one heap held {drawn.a} acorn, the other held {drawn.b} acorns. The heaps looked obviously different.'
            ),
            need=(
                "She wanted to confirm that the two counts were not the same, so she could sort "
                "them into different storage baskets."
            ),
            mapping=(
                "`not=` checks whether any count differs from the others. If all counts are "
                "identical, it returns false; if any count stands apart, it returns true."
            ),
            resolution=(
                'the runtime confirmed the two heaps were not equal — {drawn.a} differed from {drawn.b}, so they belonged in separate baskets.'
            ),
            tags=("story",),
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(min 1 2 3)",
            expected=1,
            concept_phrase="the minimum of three numbers",
            question_what="the smallest of 1, 2, and 3",
            goal_text="find the minimum of 1, 2, and 3",
            scenario=(
                "Mossback the tortoise laid out three small acorn-counts "
                "on a flat stone — from a dawn trip, a midday trip, and an "
                "afternoon trip, each heap growing larger. The values drawn fresh were {drawn.a}, {drawn.b}, and {drawn.c}."
            ),
            need=(
                "She wanted to know which trip had been the lightest, to "
                "plan tomorrow's routing."
            ),
            mapping=(
                "`min` walks the heaps and returns the smallest count. "
                "The acorns themselves stay where they are; only the "
                "runtime's verdict — the lightest heap's number — comes back."
            ),
            resolution=(
                "the runtime named the lightest trip's count, showing the smallest of all {drawn.c} heaps."
            ),
            tags=("story",),
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(quot 17 5)", expected=3,
            concept_phrase="the integer quotient",
            question_what="17 divided by 5, without remainder",
            goal_text="find the integer quotient of 17 divided by 5",
            scenario=(
                "Mossback the tortoise had gathered acorns and wanted to divide them equally "
                "among several cubs in her den. She laid out heaps, placing acorns round after "
                "round, until she ran out of acorns to distribute evenly. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "She needed to know how many complete rounds of distribution she had made — how "
                "many full acorns per cub if split fairly, ignoring any leftover."
            ),
            mapping=(
                "`quot` divides one count by another and returns only the whole heaps: how many "
                "complete portions fit. The remainder — the acorns too few to fill another round — "
                "is discarded."
            ),
            resolution=(
                "the runtime returned the count of complete rounds distributed per cub, "
                "with a few left over for another purpose."
            ),
            tags=("story",),
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(inc 5)", expected=6,
            concept_phrase="the increment operation",
            question_what="5 plus 1",
            goal_text="increment 5 by 1",
            scenario=(
                'Pip the hare had gathered {drawn.a} acorns and placed them in a heap on a tally-mark stone. Mossback the tortoise arrived with one more acorn from the path.'
            ),
            need=(
                "Mossback needed to record the new total — the count climbing from what it was "
                "by exactly one acorn — so the tally stayed current."
            ),
            mapping=(
                "`inc` takes a count and adds 1 to it. The heap grows by one acorn; the new count "
                "is the old count plus one."
            ),
            resolution=(
                "the runtime returned the incremented count, reflecting the fresh acorn on the "
                "stone."
            ),
            tags=("story",),
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(abs 5)", expected=5,
            concept_phrase="the absolute value",
            question_what="the absolute value of 5",
            goal_text="find the absolute value of 5",
            scenario=(
                "Mossback the tortoise stood at a mark on a numbered trail. A positive number "
                "was carved on the stone. She wanted to know the distance from the starting point, "
                "regardless of direction. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "She needed the pure distance as a counting number — no negative marks, no "
                "directional signs, just the span between where she stood and the origin."
            ),
            mapping=(
                "`abs` strips the sign from a number and returns only its magnitude. Positive "
                "numbers stay the same; negative numbers flip to positive; zero stays zero. "
                "The result is always the distance from zero on the trail."
            ),
            resolution=(
                "the runtime returned the distance value, measured as a plain, unsigned count "
                "of acorn-lengths from the starting stone."
            ),
            tags=("story",),
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(+ 1/2 1/4)", expected="3/4",
            concept_phrase="the sum of two ratios",
            question_what="the sum of one-half and one-quarter",
            goal_text="add one-half and one-quarter",
            scenario=(
                "Mossback the tortoise divided a berry into halves and quarters. She held "
                "one half in her paw and one quarter in a small leaf. Both pieces were parts "
                "of the same whole fruit. The value at the heart of the form was 1."
            ),
            need=(
                "She wanted to know what fraction of the whole berry she held combined — the "
                "sum of the two portion sizes stacked together."
            ),
            mapping=(
                "`+` adds fractional portions by combining their numerators and denominators. "
                "One-half and one-quarter join to form a larger portion of the berry. The sum "
                "tells what part of the whole remains."
            ),
            resolution=(
                "the runtime returned the combined portion: three-quarters of the berry held in Mossback's grasp (with `1/2` as the input value) (with `4` as the input value)."
            ),
            tags=("story",),
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(/ 10 2)", expected=5,
            concept_phrase="the division operation",
            question_what="the result of using / on 10 and 2",
            goal_text="divide 10 by 2",
            scenario=(
                "Mossback the tortoise held acorns and wanted to split them evenly in half "
                "between two cubs. She laid down equal heaps per cub and checked that the split "
                "was fair. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "She needed to know the fair share per cub — the division — so each cub got "
                "the same portion."
            ),
            mapping=(
                "`/` divides one count by another and returns the exact result as a number — "
                "whole, fractional, or rational. When division splits evenly, a whole number comes "
                "back; when it doesn't, the exact fraction or decimal appears."
            ),
            resolution=(
                "the runtime returned the exact division: a whole number, showing that the "
                "acorns split evenly into equal heaps per cub."
            ),
            tags=("story",),
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(* 2 2 2)", expected=8,
            concept_phrase="repeated multiplication",
            question_what="2 to the third power",
            goal_text="multiply 2 by itself three times",
            scenario=(
                "Mossback the tortoise arranged acorns in a small shape on the stone — stacking "
                "them with equal measurements in three dimensions. She was building a tiny cubic heap. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "She wanted to know the total acorns filling that cubic shape — how many acorns "
                "when the same count multiplies across all three dimensions."
            ),
            mapping=(
                "`*` with the same number repeated builds a power. Multiplying the same count "
                "three times — once per dimension — means each axis scales by that count. The result "
                "is all the acorns that fit into that cubic arrangement."
            ),
            resolution=(
                "the runtime returned the cubic total: the product of the three repeated multiplications "
                "filling the stone cube."
            ),
            tags=("story",),
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form='(str "ab" "cd")',
            expected="abcd",
            concept_phrase='the string concatenation',
            question_what='the result of using str to splice "ab" and "cd"',
            goal_text='use str to splice the two-letter strings "ab" and "cd" into a single thread',
            scenario=(
                'Mossback the tortoise held two short threads of beads — one with the two letters "{drawn.a}" wound on, the other with the two letters "{drawn.b}". Two threads, four beads in all.'
            ),
            need=(
                "She wanted them spliced end to end into one longer "
                "thread, so the four-bead string could carry as a single "
                "name in her foraging-ledger."
            ),
            mapping=(
                '`str` splices its arguments into one bead-string: each argument\'s beads thread one after another. With two short threads "{drawn.a}" and "{drawn.b}", the splice yields a single four-bead thread.'
            ),
            resolution=(
                "the spliced thread came back as a single four-letter "
                "string in order — ready to wear in the ledger."
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form='(println "hello")', expected=None,
            concept_phrase='the print-line call',
            question_what='the return value of using println on the string "hello"',
            goal_text='print the string "hello" with a newline',
            scenario=(
                "Mossback the tortoise stood before a scribe's chalk-marked scroll, ready to call "
                "out to Pip the hare. She would speak the message aloud — the words would fly from "
                "the stone into the air, and then silence would follow."
            ),
            need=(
                "She wanted to broadcast the message to anyone within earshot — the words saying "
                "itself, then a pause before the next call."
            ),
            mapping=(
                "`println` is the scribe speaking aloud: the words come out to the air (side-effect), "
                "and the call itself returns nothing — no parcel back to hand, just the echo of the "
                "words already spoken."
            ),
            resolution=(
                "the runtime spoke the message '{drawn.a}' with a line-break after, and returned nil — the call had done its work: the message was heard."
            ),
            tags=("story",),
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(and true true)",
            expected=True,
            concept_phrase="the logical and",
            question_what="the result of passing true and true through the and-chain of gates",
            goal_text="test whether two trues both pass through an and-chain of gates",
            scenario=(
                "Two small wooden gates stood at the start of the meadow "
                "trail. Each gate's verdict-stone was carved with the "
                "value the runner would carry to it — and today's two "
                "stones both read true."
            ),
            need=(
                "Mossback the tortoise wanted to know whether both gates "
                "would let the runner through together, or whether the "
                "first one would close and stop the chain."
            ),
            mapping=(
                "`and` walks the gates left to right: the first false "
                "closes the chain and that value comes back; otherwise "
                "the value at the last gate is what comes back. With "
                "both stones reading true, the chain holds and the last "
                "gate's true is the verdict."
            ),
            resolution=(
                "both gates along the chain swung open easily; the "
                "chain's last gate handed back its own value as the "
                "verdict — the path-to-end clear, uninterrupted."
            ),
            tags=("story",),
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(not true)", expected=False,
            concept_phrase="the logical not",
            question_what="the result of using not on true",
            goal_text="negate the value true",
            scenario=(
                "A single wooden gate stood at the trail's fork, its verdict-stone carved with "
                "the word true. Mossback the tortoise wanted to know what would happen if that "
                "verdict were flipped upside down — inverted."
            ),
            need=(
                "She needed the opposite verdict — if the gate was open and let traffic through, "
                "what would closing it mean? The inverse of the current state."
            ),
            mapping=(
                "`not` flips the gate's verdict: open becomes closed, closed becomes open. True "
                "flips to false; false flips to true. The operation inverts the verdict-stone's word."
            ),
            resolution=(
                "the runtime returned the inverted verdict: false — the gate closed if it had been "
                "open, the passage now blocked."
            ),
            tags=("story",),
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(if 0 1 0)", expected=1,
            concept_phrase="the if conditional with zero as condition",
            question_what="the result of if with condition 0, then-branch 1, else-branch 0",
            goal_text="use if to return 1 when the condition is 0 (then-branch) and 0 otherwise (else-branch)",
            scenario=(
                "A wooden gate at the trail's fork had a verdict-stone carved with the number zero. "
                "Mossback the tortoise stood before it, confused — zero was nothing, yet the gate "
                "stood, not absent. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "She needed to know if zero would open the gate or close it — whether the number "
                "zero counts as 'true' for the gate's logic, or whether only false and nil truly "
                "block the path."
            ),
            mapping=(
                "`if` routes through its gate based on whether the verdict is falsey. Only false "
                "and nil are truly falsey; every other value — including zero, the empty string, "
                "and lists — opens the gate as truthy."
            ),
            resolution=(
                "the runtime proved that zero is truthy: the gate opened, and the then-branch "
                "came back, not the else-branch — confirming that zero lets traffic pass."
            ),
            tags=("story",),
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(boolean 0)", expected=True,
            concept_phrase="the boolean conversion",
            question_what="the result of using boolean on 0",
            goal_text="convert 0 to a boolean",
            scenario=(
                "Mossback the tortoise held the number {drawn.a} in a small pouch and approached Pip the hare, who tended the gate at the trail's fork. Pip's stone told verdicts — true meant open, false meant closed."
            ),
            need=(
                "She wanted to know the verdict for zero: if she painted zero on the gate's "
                "stone, would it open or close? Is zero true or false in the gate-keeper's eye?"
            ),
            mapping=(
                "`boolean` converts any value to either true or false. Zero, though nothing-like, "
                "is truthy — it converts to true and opens the gate. Only false and nil are falsey; "
                "all others, even zero and empty strings, convert to true."
            ),
            resolution=(
                "the runtime confirmed zero's verdict — the gate's truth "
                "rule opened even with zero carved on the stone."
            ),
            tags=("story",),
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(:hare {:hare 1 :tortoise 2})", expected=1,
            concept_phrase="the keyword lookup",
            question_what="the result of using the keyword :hare as a function on the map {:hare 1 :tortoise 2}",
            goal_text="use the keyword :hare to look up a value in the map with keys :hare and :tortoise",
            scenario=(
                "Mossback the tortoise's foraging-basket had two named pouches stitched into its "
                "sides — one labeled :hare, the other labeled :tortoise. Each pouch held acorns, "
                "different counts in each. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "Pip the hare arrived and asked what lay in the :hare pouch. Mossback wanted to "
                "call out the pouch's name and have the basket itself hand back its contents."
            ),
            mapping=(
                "A keyword acts as a key to open its matching pouch. When called on the basket, "
                ":hare looks up the :hare pouch and returns its contents — the value stored under "
                "that name. The basket itself stays unchanged."
            ),
            resolution=(
                "the runtime looked up the :hare key and returned the value from the :hare pouch — "
                "the count of acorns tucked inside."
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(symbol? (quote hare))", expected=True,
            concept_phrase="the symbol-predicate applied to a long-form-quoted name",
            question_what="whether long-form quoting produces a symbol",
            goal_text="ask whether long-form quoting of the name hare produces a symbol, using symbol?",
            scenario=(
                "Mossback the tortoise stood at a chalk-marked stone with the word 'hare' etched "
                "into it — not the creature itself, just the name, the chalk-mark of that name."
            ),
            need=(
                "She wondered whether the chalk-mark symbol — the name frozen on stone — was "
                "indeed a symbol-object, a name-thing apart from any running creature."
            ),
            mapping=(
                "Quoting with `(quote hare)` locks the name in place as a chalk-mark symbol — "
                "not a reference to run, not a thing to evaluate, just the name itself, an inert "
                "word-object. The predicate `symbol?` checks whether this chalk-mark is truly "
                "a symbol."
            ),
            resolution=(
                "the runtime confirmed the chalk-mark's identity: the "
                "quoted name 'hare' is indeed a symbol-object, not the "
                "hare itself."
            ),
            tags=("story",),
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(* 1000000 1000000)", expected=1000000000000,
            concept_phrase="the large multiplication",
            question_what="the product of one million and one million",
            goal_text="multiply one million by one million",
            scenario=(
                "Mossback the tortoise counted acorns from a season's full harvest — a million "
                "acorns stacked in one great heap, and another million in a second heap. She "
                "wanted to multiply these enormous quantities. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "She needed to know the total if she combined the heaps by multiplying — how many "
                "acorns across the grand result, without limit on the size of the answer."
            ),
            mapping=(
                "Arithmetic operations like `*` grow naturally with their operands. When numbers "
                "get large — larger than typical storage — the REPL auto-promotes to a big-integer "
                "type and computes the full result without overflow or truncation."
            ),
            resolution=(
                "the runtime calculated the massive product — one million times one million — and "
                "returned the exact result, promoted to a big-integer, no precision lost."
            ),
            tags=("story",),
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(count [1 2 3])", expected=3,
            concept_phrase="the count operation",
            question_what="the result of using count on the vector containing 1, 2, and 3",
            goal_text="count the elements in the vector containing 1, 2, and 3",
            scenario=(
                "Mossback the tortoise walked a row of gathered pebbles laid out on the meadow "
                "path, lined up from start to finish. She carried a tally-stick to mark each "
                "pebble she passed."
            ),
            need=(
                "She wanted to know how many pebbles lay in the row — the full count from start "
                "to end, one tally-mark for each pebble she passed. The value drawn fresh was {drawn.a}."
            ),
            mapping=(
                "`count` walks through a sequence from beginning to end, tallying each element "
                "as it goes. The tally-stick returns the running count — how many elements the walk "
                "passed."
            ),
            resolution=(
                "the runtime walked the row and returned the tally: the count of elements in the "
                "row, one mark carved for each pebble."
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(count \"tortoise\")", expected=8,
            concept_phrase="the count of characters in a string",
            question_what="the result of using count on the string tortoise",
            goal_text="count the characters in the string tortoise",
            scenario=(
                'Mossback the {drawn.a} held a bead-thread with beads wound along it — each bead a letter spelling out a name. The thread hung straight in her paw, strung end to end.'
            ),
            need=(
                "She wanted to know the length of the thread — how many beads, from the first "
                "knot to the last — to craft a matching pouch to carry it."
            ),
            mapping=(
                "`count` walks a bead-string from end to end, tallying each bead it finds. The "
                "count returns how many beads are threaded — the string's length, bead by bead."
            ),
            resolution=(
                "the runtime counted the beads and returned the string's length: "
                "the count of beads spelling the name, one character-bead per position."
            ),
            tags=("story",),
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(- (* 5 4) 7)", expected=13,
            concept_phrase="the nested arithmetic",
            question_what="the result of multiplying 5 and 4, then subtracting 7",
            goal_text="compute 5 times 4, then subtract 7",
            scenario=(
                'Pip the hare claimed he could race at {drawn.a} acorn-lengths per hour and travel for {drawn.b} hours straight. Mossback the tortoise, however, had given Pip a head-start of {drawn.c} acorn-lengths at the starting stone.'
            ),
            need=(
                "She wanted to know Pip's true lead-adjusted distance — how far ahead he really "
                "was after his full run, accounting for the head-start he'd already received."
            ),
            mapping=(
                "Nested arithmetic chains operations: first compute the product (speed times time), "
                "then subtract the head-start from that sum. Each operation feeds its result into "
                "the next, building from inner forms to the final answer."
            ),
            resolution=(
                "the runtime calculated Pip's actual progress: {drawn.a} times {drawn.b} acorn-lengths run, minus the {drawn.c}-length head-start already given, leaving a true lead of the running total."
            ),
            tags=("story",),
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
    print(f"grade-2 tortoise-hare smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
