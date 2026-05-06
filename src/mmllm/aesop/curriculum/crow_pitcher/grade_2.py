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

            scenario=(
                "Korvus sat at the farm with four groups of stones set out "
                "along the pitcher's rim: one stone, then two, then three, then four. "
                "He needed a single total before the water rose."
            ),
            need=(
                "He wanted one count for all four groups combined, tallied "
                "in a single drop rather than four separate ones."
            ),
            mapping=(
                "`+` accepts any number of stones at once, adding each to the "
                "running tally from left to right. Dropping four groups in one "
                "form is identical to summing them in sequence."
            ),
            resolution=(
                "The expected total arrived and the water settled at the right level."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 2 3 4)", expected=24,
            concept_phrase="the multi-arg product",
            question_what="the product of 2, 3, and 4",
            goal_text="multiply 2, 3, and 4",

            scenario=(
                "Caw lined up three groups of stones at the orchard pitcher: "
                "two in the first group, three in the second, four in the third. "
                "She wanted the compounded product without three separate steps."
            ),
            need=(
                "She needed the total after multiplying all three groups together "
                "in a single drop into the pitcher."
            ),
            mapping=(
                "`*` accepts any number of arguments and multiplies them left "
                "to right. Two groups times three gives a sub-product; that "
                "sub-product times four gives the final compounded total."
            ),
            resolution=(
                "The compounded product settled in the pitcher at the expected count."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(- 100 1 2 3)", expected=94,
            concept_phrase="the multi-arg subtraction",
            question_what="100 minus 1, 2, and 3",
            goal_text="subtract 1, 2, and 3 from 100",

            scenario=(
                "Sable began with a hundred stones piled on the rim at the market. "
                "Three separate portions — one, then two, then three — were "
                "reserved to set aside before the count was settled."
            ),
            need=(
                "Sable needed the final tally after removing all three portions "
                "in one form rather than three separate subtractions."
            ),
            mapping=(
                "`-` with multiple arguments subtracts each successive value "
                "from the first. The starting pile shrinks by each portion "
                "in turn until all deductions are applied."
            ),
            resolution=(
                "The three deductions were applied and the expected remainder rose to the rim."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(+ 1 2 3 4 5 6 7 8 9 10)", expected=55,
            concept_phrase="the sum of ten numbers",
            question_what="the sum of integers 1 through 10",
            goal_text="add the integers 1 through 10",

            scenario=(
                "Korvus lined ten stones along the pitcher's rim at the road, "
                "each numbered in order from one to ten. He wanted a single "
                "total for all ten before the sun moved."
            ),
            need=(
                "He needed the accumulated sum of every stone in one form, "
                "not ten separate additions piled one atop the next."
            ),
            mapping=(
                "`+` is variadic — it accepts any number of arguments. Ten "
                "stones enter at once; the tally grows with each, producing "
                "the full sum in a single evaluation."
            ),
            resolution=(
                "All ten stones were summed and the expected total arrived at the rim."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 1 2 3 4 5)", expected=120,
            concept_phrase="the multi-arg product",
            question_what="the product of 1 through 5",
            goal_text="multiply the integers 1 through 5",

            scenario=(
                "Caw set five groups along the hilltop pitcher: one, two, "
                "three, four, and five stones in each. She wanted the full "
                "compounded product from multiplying all five together."
            ),
            need=(
                "She needed every group multiplied together in one form, "
                "the product compounding across all five."
            ),
            mapping=(
                "`*` composes multiplication across all its arguments. Starting "
                "from one the product doubles, triples, and grows; the final "
                "result is the product of the entire sequence."
            ),
            resolution=(
                "The five-group product settled in the pitcher at the expected count."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(+ 10 20 30)", expected=60,
            concept_phrase="the sum of three numbers",
            question_what="the sum of 10, 20, and 30",
            goal_text="add 10, 20, and 30",

            scenario=(
                "Sable placed three clusters of pebbles at the garden pitcher: "
                "ten on the left, twenty in the middle, thirty on the right. "
                "She needed the combined total of all three clusters."
            ),
            need=(
                "She wanted the accumulated sum of all three clusters in a "
                "single pitcher drop, not added one cluster at a time."
            ),
            mapping=(
                "`+` gathers all three arguments and sums them left to right. "
                "Ten plus twenty gives a subtotal; adding thirty yields the "
                "full cluster sum in one step."
            ),
            resolution=(
                "The three clusters summed and the expected total returned from the pitcher."
            ),
            tags=("story",),
        ),
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

            scenario=(
                "Caw lined three stones on the pitcher's rim in the orchard: "
                "a small one, a medium one, and a large one, arranged left to right. "
                "She claimed their sizes rose steadily without checking carefully."
            ),
            need=(
                "She needed to confirm each stone was strictly smaller than the "
                "next before trusting her arrangement."
            ),
            mapping=(
                "`<` threads through every adjacent pair in one chain, returning "
                "true only if each stone is strictly smaller than its right neighbour. "
                "One failing pair collapses the whole chain to false."
            ),
            resolution=(
                "The chain held at every step and the gate returned the expected truth value."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(< 3 2 1)", expected=False,
            concept_phrase="the less-than chain",
            question_what="whether 3 < 2 < 1",
            goal_text="test whether 3 is less than 2 and 2 is less than 1",

            scenario=(
                "Korvus laid three stones at the farm in descending order: "
                "a heavy one, a medium one, and a light one from left to right. "
                "Caw insisted they were still rising — Korvus doubted it."
            ),
            need=(
                "He needed the chain to test whether each stone was strictly "
                "lighter than the one to its right."
            ),
            mapping=(
                "`<` checks each adjacent pair; the heavy stone is not lighter "
                "than the medium one, so the chain breaks at the first step "
                "and returns false without checking further."
            ),
            resolution=(
                "The chain broke immediately and the expected false value returned."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(<= 1 1 2)", expected=True,
            concept_phrase="the less-than-or-equal chain",
            question_what="whether 1 ≤ 1 ≤ 2",
            goal_text="test whether 1 is less than or equal to 1 and 1 is less than or equal to 2",

            scenario=(
                "Sable set three stones on the pitcher's rim at the meadow: "
                "one, then another of equal size, then a slightly larger one. "
                "She wanted to know whether the sequence was non-decreasing."
            ),
            need=(
                "She needed to confirm that no stone was larger than the one "
                "after it, allowing equal neighbours."
            ),
            mapping=(
                "`<=` allows adjacent stones of equal size to pass. The first "
                "pair is equal — that satisfies ≤. The second pair rises — that "
                "also satisfies ≤. Every step holds."
            ),
            resolution=(
                "Every pair satisfied the check and the expected truth value rose."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(> 5 4 3 2 1)", expected=True,
            concept_phrase="the greater-than chain",
            question_what="whether the numbers are strictly decreasing",
            goal_text="test whether 5 > 4 > 3 > 2 > 1",

            scenario=(
                "Caw arranged five stones at the road beside the pitcher in "
                "strict descending order: five, four, three, two, one. She "
                "claimed they were properly ordered and challenged Korvus."
            ),
            need=(
                "Korvus needed the pitcher to verify every adjacent pair was "
                "strictly decreasing without any ties allowed."
            ),
            mapping=(
                "`>` threads through every adjacent pair, returning true only "
                "if each is strictly greater than the next. Five pairs in a "
                "row must all hold for the chain to return true."
            ),
            resolution=(
                "Every pair held and the expected truth value settled at the pitcher's rim."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(>= 3 3 2)", expected=True,
            concept_phrase="the greater-than-or-equal chain",
            question_what="whether 3 ≥ 3 ≥ 2",
            goal_text="test whether 3 is greater than or equal to 3 and 3 is greater than or equal to 2",

            scenario=(
                "Sable set three stones at the village pitcher: two equal "
                "heavy ones side by side, then a lighter one at the end. "
                "She asked whether the sequence was non-increasing."
            ),
            need=(
                "She needed to confirm no stone was smaller than the one "
                "before it, with equal neighbours allowed."
            ),
            mapping=(
                "`>=` passes equal pairs as well as strictly descending ones. "
                "The first two stones are equal — that satisfies ≥. The third "
                "is lighter — that also satisfies ≥. All pairs clear."
            ),
            resolution=(
                "Both pairs satisfied the check and the expected result returned."
            ),
            tags=("story",),
        ),
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

            scenario=(
                "Sable set one stone on the left side of the pitcher's rim "
                "and two on the right, at the meadow. Both piles sat in plain "
                "sight, clearly not matching in number."
            ),
            need=(
                "Sable needed the pitcher to confirm the two piles carried "
                "different counts before proceeding."
            ),
            mapping=(
                "`not=` compares each stone-count in turn; if any pair differs, "
                "the form returns true. One stone versus two is a mismatch, "
                "so inequality is confirmed immediately."
            ),
            resolution=(
                "The mismatch was confirmed and the expected truth value rose to the rim."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(not= 1 1)", expected=False,
            concept_phrase="the inequality check",
            question_what="whether 1 differs from itself",
            goal_text="test whether 1 and 1 are not equal",

            scenario=(
                "Korvus placed two identical stones side by side on the pitcher's "
                "rim at the garden — both carrying the count one. He wondered if "
                "the pitcher would call them unequal."
            ),
            need=(
                "He needed to verify that two stones of the same count would "
                "not be flagged as different by the inequality check."
            ),
            mapping=(
                "`not=` returns true only when at least one value differs. Two "
                "stones of equal count share the same value; the mismatch test "
                "finds none and returns false."
            ),
            resolution=(
                "No mismatch was found and the expected false value settled at the rim."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(= 1 1 1)", expected=True,
            concept_phrase="the equality check",
            question_what="whether all three are equal",
            goal_text="test whether 1, 1, and 1 are all equal",

            scenario=(
                "Caw set three stones of exactly equal size on the road "
                "beside the pitcher. She wanted the pitcher to confirm "
                "all three carried the same count before proceeding."
            ),
            need=(
                "She needed a single verdict covering all three stones at once, "
                "not a series of pairwise comparisons."
            ),
            mapping=(
                "`=` with multiple arguments threads through each adjacent pair. "
                "Three identical values all share the same count; every pair "
                "passes, and the form returns true."
            ),
            resolution=(
                "All three matched and the expected truth value came back from the pitcher."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(= 1 1 2)", expected=False,
            concept_phrase="the equality check",
            question_what="whether all three are equal",
            goal_text="test whether 1, 1, and 2 are all equal",

            scenario=(
                "Sable lined up three stones at the orchard pitcher: two equal "
                "ones followed by a noticeably larger one. She needed the pitcher "
                "to check whether all three were truly the same."
            ),
            need=(
                "She needed confirmation that every stone matched every other, "
                "with no hidden outlier hiding among them."
            ),
            mapping=(
                "`=` compares all arguments; the first two match, but the third "
                "differs. The chain breaks at that pair and the form "
                "returns false without checking further."
            ),
            resolution=(
                "The outlier broke the chain and the expected false value returned."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(not= 1 1 2)", expected=True,
            concept_phrase="the inequality check",
            question_what="whether at least one differs",
            goal_text="test whether at least one of 1, 1, and 2 is not equal to the others",

            scenario=(
                "Korvus had three stones at the meadow pitcher: two matching "
                "ones and one noticeably different. He asked whether the "
                "collection counted as unequal overall."
            ),
            need=(
                "He needed to know whether even one differing stone was enough "
                "to make the whole set count as not-equal."
            ),
            mapping=(
                "`not=` returns true if any value differs from any other. "
                "Two ones and a two share no single common count; the "
                "collection is not all-equal, so the form returns true."
            ),
            resolution=(
                "The differing stone was found and the expected truth value arrived."
            ),
            tags=("story",),
        ),
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

            scenario=(
                "Korvus placed three stones of different weights on the road "
                "beside the pitcher: a light one, a middling one, and a heavy one. "
                "He needed to pick out the lightest before continuing."
            ),
            need=(
                "He wanted the single smallest stone identified without "
                "lifting and comparing each pair by talon."
            ),
            mapping=(
                "`min` scans all stones left to right, keeping the lightest seen "
                "so far, discarding any heavier candidate. When the last stone "
                "is passed, the surviving lightest stone is the answer."
            ),
            resolution=(
                "The lightest stone was identified and the expected count settled in the pitcher."
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(quot 17 5)", expected=3,
            concept_phrase="the integer quotient",
            question_what="17 divided by 5, without remainder",
            goal_text="find the integer quotient of 17 divided by 5",

            scenario=(
                "Caw had seventeen acorns at the market and five pouches to fill "
                "beside the pitcher. She wanted to know how many full pouches "
                "she could pack before any acorns were left over."
            ),
            need=(
                "She needed the whole number of complete pouches only, "
                "with any leftover acorns ignored."
            ),
            mapping=(
                "`quot` divides and truncates toward zero, counting only "
                "complete groups. Each full pouch of five consumes five acorns; "
                "the count of complete pouches is the integer quotient."
            ),
            resolution=(
                "The number of complete pouches emerged and the water rose to the expected mark."
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(inc 5)", expected=6,
            concept_phrase="the increment operation",
            question_what="5 plus 1",
            goal_text="increment 5 by 1",

            scenario=(
                "Sable had five stones already resting at the bottom of the pitcher "
                "on the hilltop. One more stone sat in the talon, ready to be dropped, "
                "and Sable wanted to know the new level."
            ),
            need=(
                "Sable needed the water level after exactly one additional stone "
                "was dropped, without recounting from scratch."
            ),
            mapping=(
                "`inc` adds exactly one to any integer, advancing the count by a "
                "single unit. It is the minimal step — one stone added, the tally "
                "moves forward by one, nothing more."
            ),
            resolution=(
                "The tally advanced by one and the expected new level arrived."
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(abs 5)", expected=5,
            concept_phrase="the absolute value",
            question_what="the absolute value of 5",
            goal_text="find the absolute value of 5",

            scenario=(
                "Korvus stood at the garden with five stones on the right side "
                "of the pitcher. He asked the pitcher how far that count was from "
                "zero, regardless of direction."
            ),
            need=(
                "He needed the distance from zero as a positive count, "
                "stripping any sign from the number."
            ),
            mapping=(
                "`abs` measures the unsigned distance from zero. A positive "
                "input already carries no sign burden; a negative input would be "
                "reflected, but either way the result is non-negative."
            ),
            resolution=(
                "The unsigned distance emerged and settled as the expected count."
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(+ 1/2 1/4)", expected="3/4",
            concept_phrase="the sum of two ratios",
            question_what="the sum of one-half and one-quarter",
            goal_text="add one-half and one-quarter",

            scenario=(
                "Caw had two partial stones in the orchard: one split in half "
                "and one split into quarters. She needed to know how much stone "
                "she held altogether, as a single exact fraction."
            ),
            need=(
                "She wanted the exact combined weight without losing any "
                "fractional precision to rounding."
            ),
            mapping=(
                "`+` on ratios keeps the result exact, finding a common "
                "denominator and summing numerators. No precision is lost; "
                "the answer stays a true fraction until the form is done."
            ),
            resolution=(
                "The exact fractional sum arrived and the pitcher returned it without rounding."
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(/ 10 2)", expected=5,
            concept_phrase="the division operation",
            question_what="the result of using / on 10 and 2",
            goal_text="divide 10 by 2",

            scenario=(
                "Sable had ten stones on the rim at the village and two "
                "baskets waiting below. She dropped the form into the pitcher, "
                "expecting to know the even share per basket."
            ),
            need=(
                "She needed the exact number of stones that belong in each "
                "basket when ten divide cleanly by two."
            ),
            mapping=(
                "`/` returns an integer when division is exact, a ratio otherwise. "
                "Ten split evenly into two groups yields a whole number; the "
                "pitcher returns the integer, not a ratio."
            ),
            resolution=(
                "The even share arrived as an integer and the water rose to the expected level."
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(* 2 2 2)", expected=8,
            concept_phrase="repeated multiplication",
            question_what="2 to the third power",
            goal_text="multiply 2 by itself three times",

            scenario=(
                "Korvus scratched three tallies of two into the pitcher's rim "
                "at the farm, stacking each layer on the product of the last. "
                "He wanted the final compounded count from three doublings."
            ),
            need=(
                "He needed the result of doubling a quantity three times over "
                "in a single form, not three separate steps."
            ),
            mapping=(
                "`*` multiplies all its arguments left to right in one pass. "
                "Three twos compound: the first pair yields a product that "
                "is then multiplied by the third, giving the cube."
            ),
            resolution=(
                "The compounded product settled and the expected count filled the pitcher."
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

            scenario=(
                "Caw scratched a message into the pitcher's clay at the garden: "
                "the word \"hello\" pressed in by talon with a line-break notch "
                "at the end. She asked what value the pitcher returned after writing."
            ),
            need=(
                "She needed to know what the pitcher handed back as a value "
                "after the notation was written to the output."
            ),
            mapping=(
                "`println` writes its argument as a side-effect and always returns "
                "nil — the scratch on the clay is the output, but the wing-cache "
                "carries nothing back. Writing is not the same as returning."
            ),
            resolution=(
                "The pitcher wrote the message and returned nil, exactly as expected."
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(and true true)",
            expected=True,
            concept_phrase="the logical and",
            question_what="the result of passing true and true through the and-chain of gates",
            goal_text="test whether two trues both pass through an and-chain of gates",

            scenario=(
                "Korvus stood at the pitcher's mouth on the road, two gate-arms "
                "stretched across it. Both arms were raised open. He needed to "
                "know whether the path through both gates was clear."
            ),
            need=(
                "He needed the final verdict only if every gate along the chain "
                "was open — a single closed gate would block the path."
            ),
            mapping=(
                "`and` checks each gate in order; if the first is open it moves "
                "to the next. Both true means both gates are open, so `and` "
                "returns the last value it checked."
            ),
            resolution=(
                "Both gates passed and the expected value arrived at the rim."
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(not true)", expected=False,
            concept_phrase="the logical not",
            question_what="the result of using not on true",
            goal_text="negate the value true",

            scenario=(
                "Caw found the gate-arm above the pitcher fully raised open at "
                "the meadow. She wanted to know what the pitcher said about the "
                "opposite of that state — the gate flipped."
            ),
            need=(
                "She needed the inverted reading: if the gate was open, "
                "what value named the closed state?"
            ),
            mapping=(
                "`not` flips truthy to false and falsey to true. A raised "
                "gate-arm is truthy; flipping it yields false. The arm's "
                "position is reversed, never left in the original state."
            ),
            resolution=(
                "The gate flipped and the expected negated value returned from the pitcher."
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(if 0 1 0)", expected=1,
            concept_phrase="the if conditional with zero as condition",
            question_what="the result of if with condition 0, then-branch 1, else-branch 0",
            goal_text="use if to return 1 when the condition is 0 (then-branch) and 0 otherwise (else-branch)",

            scenario=(
                "Sable stood at a fork above the pitcher at the garden. The left "
                "path carried a stone labelled zero; the right path carried one. "
                "The gate would open whichever arm the condition stone allowed."
            ),
            need=(
                "Sable needed to know which path the pitcher would take given "
                "that the condition stone bore the value zero."
            ),
            mapping=(
                "`if` in Clojure treats zero as truthy — only false and nil "
                "close the then-gate. Zero opens the then-branch, so the "
                "pitcher takes the left path and returns 1."
            ),
            resolution=(
                "The then-branch opened and the expected stone came back from the pitcher."
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(boolean 0)", expected=True,
            concept_phrase="the boolean conversion",
            question_what="the result of using boolean on 0",
            goal_text="convert 0 to a boolean",

            scenario=(
                "Korvus placed a stone marked zero at the mouth of the pitcher "
                "on the hilltop. He wanted to know which side of the gate that "
                "stone would open when measured as a strict true-or-false."
            ),
            need=(
                "He needed to know whether zero, when explicitly cast to boolean, "
                "would be treated as open-gate or closed-gate."
            ),
            mapping=(
                "`boolean` converts any value to strict true or false. Zero is "
                "not false and not nil, so it converts to true — the gate opens. "
                "Only false and nil close the gate."
            ),
            resolution=(
                "The gate opened and the expected boolean value rose from the pitcher."
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

            scenario=(
                "Caw scratched the chalk-mark \"hare\" on a smooth stone at the "
                "village without placing any value beneath it. She handed the "
                "name alone to the pitcher and asked what kind of thing it was."
            ),
            need=(
                "She needed to know whether the quoted chalk-mark was a proper "
                "symbol — a name-shape in its own right, not yet bound to a value."
            ),
            mapping=(
                "`quote` hands the pitcher the chalk-mark itself rather than "
                "what it names. `symbol?` then inspects the mark and confirms "
                "whether the shape qualifies as a Clojure symbol."
            ),
            resolution=(
                "The chalk-mark was confirmed as a symbol and the expected answer arrived."
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(* 1000000 1000000)", expected=1000000000000,
            concept_phrase="the large multiplication",
            question_what="the product of one million and one million",
            goal_text="multiply one million by one million",

            scenario=(
                "Sable dropped two enormous piles of stones into the pitcher "
                "at the market — each pile too vast to count by talon. She "
                "needed the product of the two immense stone-counts."
            ),
            need=(
                "She needed the exact product without losing any digits to "
                "integer overflow, no matter how large the result grew."
            ),
            mapping=(
                "Clojure auto-promotes integers to bigint when the product would "
                "overflow a regular counter. The pitcher widens its mouth as "
                "needed, keeping every digit of the result intact."
            ),
            resolution=(
                "The exact product arrived without overflow and the water rose to the full count."
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

            scenario=(
                "Korvus had a vine strung with pebbles spelling out \"tortoise\" "
                "in the orchard beside the pitcher. He wanted to know how many "
                "pebbles the bead-string held in total."
            ),
            need=(
                "He needed the exact bead count so he could compare vine "
                "lengths without unthreading each pebble by talon."
            ),
            mapping=(
                "`count` on a string walks the vine pebble by pebble, "
                "incrementing a tally at each character. The final tally is "
                "the number of beads on that vine."
            ),
            resolution=(
                "The bead tally arrived and the expected character count settled in the pitcher."
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(- (* 5 4) 7)", expected=13,
            concept_phrase="the nested arithmetic",
            question_what="the result of multiplying 5 and 4, then subtracting 7",
            goal_text="compute 5 times 4, then subtract 7",

            scenario=(
                "Caw sat at the farm with five rows of four stones each on "
                "the pitcher's rim, then seven stones set aside to remove. "
                "She needed the final count after the removal."
            ),
            need=(
                "She needed the product of the rows computed first, then "
                "seven subtracted from that product in a single form."
            ),
            mapping=(
                "Nesting `*` inside `-` forces the product to be evaluated "
                "before the subtraction. The inner form resolves to a "
                "wing-cache value that the outer `-` then acts on."
            ),
            resolution=(
                "The nested product resolved first and the final count arrived as expected."
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
    print(f"grade-2 crow-pitcher smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
