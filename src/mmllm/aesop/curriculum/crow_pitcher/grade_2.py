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
                "the total arrived and the water settled at the right level. (with {drawn.a} folded in)"
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
                "The compounded product settled in the pitcher at the count. (with {drawn.a} folded in)"
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
                "The three deductions were applied and the expected remainder rose to the rim. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(+ 1 2 3 4 5 6 7 8 9 10)", expected=55,
            concept_phrase="the sum of the numbers",
            question_what="the sum of integers 1 through 10",
            goal_text="add the integers 1 through 10",

            scenario=(
                "Korvus lined the stones along the pitcher's rim at the road, "
                "each numbered in order from one to ten. He wanted a single "
                "total for all ten before the sun moved."
            ),
            need=(
                "He needed the accumulated sum of every stone in one form, "
                "not ten separate additions piled one atop the next."
            ),
            mapping=(
                '`+` is variadic — it accepts any number of arguments. {drawn.j} stones enter at once; the tally grows with each, producing the full sum in a single evaluation.'
            ),
            resolution=(
                "All the stones were summed and the total arrived at the rim. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 1 2 3 4 5)", expected=120,
            concept_phrase="the multi-arg product",
            question_what="the product of 1 through 5",
            goal_text="multiply the integers 1 through 5",

            scenario=(
                "Caw set five groups of stones along the hilltop pitcher's "
                "rim, drawn from {drawn.a}, {drawn.b}, {drawn.c}, {drawn.d}, "
                "and {drawn.e} per group. She wanted the full compounded "
                "product across all five."
            ),
            need=(
                "She needed every group multiplied together in one form, "
                "the product compounding across all five draws."
            ),
            mapping=(
                "`*` composes multiplication across all its arguments. "
                "Starting from one the product folds in each operand in "
                "turn; the final result is the product of the entire "
                "drawn sequence."
            ),
            resolution=(
                "The five-group product settled in the pitcher, the "
                "tally folded across each draw in turn. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(+ 10 20 30)", expected=60,
            concept_phrase="the sum of the numbers",
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
                "The three clusters summed and the total returned from the pitcher. (with {drawn.a} folded in)"
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
                "Caw lined the stones on the pitcher's rim in the orchard: "
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
                "The chain held at every step and the gate returned the expected truth value. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(< 3 2 1)", expected=False,
            concept_phrase="the less-than chain",
            question_what="whether 3 < 2 < 1",
            goal_text="test whether 3 is less than 2 and 2 is less than 1",

            scenario=(
                "Korvus laid the stones at the farm in descending order: "
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
                "The chain broke immediately and the expected false value returned. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(<= 1 1 2)", expected=True,
            concept_phrase="the less-than-or-equal chain",
            question_what="whether 1 ≤ 1 ≤ 2",
            goal_text="test whether 1 is less than or equal to 1 and 1 is less than or equal to 2",

            scenario=(
                "Sable set the stones on the pitcher's rim at the meadow: "
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
                "Every pair satisfied the check and the expected truth value rose. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(> 5 4 3 2 1)", expected=True,
            concept_phrase="the greater-than chain",
            question_what="whether the numbers are strictly decreasing",
            goal_text="test whether 5 > 4 > 3 > 2 > 1",

            scenario=(
                'Caw arranged the stones at the road beside the pitcher in strict descending order: the counts. She claimed they were properly ordered and challenged Korvus.'
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
                "Every pair held and the expected truth value settled at the pitcher's rim. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(>= 3 3 2)", expected=True,
            concept_phrase="the greater-than-or-equal chain",
            question_what="whether 3 ≥ 3 ≥ 2",
            goal_text="test whether 3 is greater than or equal to 3 and 3 is greater than or equal to 2",

            scenario=(
                "Sable set the stones at the village pitcher: two equal "
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
                "Both pairs satisfied the check and the result returned. (with {drawn.a} folded in)"
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
                "The mismatch was confirmed and the expected truth value rose to the rim. (with {drawn.a} folded in)"
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
                "No mismatch was found and the expected false value settled at the rim. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(= 1 1 1)", expected=True,
            concept_phrase="the equality check",
            question_what="whether all three are equal",
            goal_text="test whether 1, 1, and 1 are all equal",

            scenario=(
                "Caw set the stones of exactly equal size on the road "
                "beside the pitcher. She wanted the pitcher to confirm "
                "all three carried the same count before proceeding."
            ),
            need=(
                "She needed a single verdict covering all the stones at once, "
                "not a series of pairwise comparisons."
            ),
            mapping=(
                "`=` with multiple arguments threads through each adjacent pair. "
                "Three identical values all share the same count; every pair "
                "passes, and the form returns true."
            ),
            resolution=(
                "All three matched and the expected truth value came back from the pitcher. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(= 1 1 2)", expected=False,
            concept_phrase="the equality check",
            question_what="whether all three are equal",
            goal_text="test whether 1, 1, and 2 are all equal",

            scenario=(
                "Sable lined up the stones at the orchard pitcher: two equal "
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
                "The outlier broke the chain and the expected false value returned. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(not= 1 1 2)", expected=True,
            concept_phrase="the inequality check",
            question_what="whether at least one differs",
            goal_text="test whether at least one of 1, 1, and 2 is not equal to the others",

            scenario=(
                "Korvus had the stones at the meadow pitcher: two matching "
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
                "The differing stone was found and the expected truth value arrived. (with {drawn.a} folded in)"
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
            concept_phrase="the minimum of the numbers",
            question_what="the smallest of 1, 2, and 3",
            goal_text="find the minimum of 1, 2, and 3",

            scenario=(
                "Korvus placed the stones of different weights on the road "
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
                "The lightest stone was identified and the count settled in the pitcher. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(max 1 2 3)", expected=3,
            concept_phrase="the maximum of the numbers",
            question_what="the largest of 1, 2, and 3",
            goal_text="find the maximum of 1, 2, and 3",

            scenario=(
                "Caw had the stones of increasing size on the hilltop pitcher: "
                "a small one, a medium one, and a large one. She wanted the "
                "heaviest identified without lifting each in turn."
            ),
            need=(
                "She needed the single largest stone named outright, "
                "without sorting the entire set first."
            ),
            mapping=(
                "`max` scans left to right, retaining the heaviest seen so far "
                "and discarding any lighter candidate. The last surviving "
                "stone is the maximum when the scan ends."
            ),
            resolution=(
                "The heaviest stone was named and the count settled in the pitcher. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(min 7 3 9 1 5)", expected=1,
            concept_phrase="the minimum of the numbers",
            question_what="the smallest of 7, 3, 9, 1, and 5",
            goal_text="find the minimum of 7, 3, 9, 1, and 5",

            scenario=(
                "Sable scattered the stones of mixed sizes along the garden "
                "pitcher's rim in no particular order. She needed the lightest "
                "one picked out, however jumbled the rest."
            ),
            need=(
                "She needed the smallest stone identified from the unsorted "
                "lineup without ordering all five by hand."
            ),
            mapping=(
                "`min` tracks the lightest stone seen across any order. Even "
                "if the lightest arrives late in the scan, it displaces the "
                "running minimum when it appears."
            ),
            resolution=(
                "The lightest stone was found in the jumble and the count arrived. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(max 7 3 9 1 5)", expected=9,
            concept_phrase="the maximum of the numbers",
            question_what="the largest of 7, 3, 9, 1, and 5",
            goal_text="find the maximum of 7, 3, 9, 1, and 5",

            scenario=(
                'Korvus laid five unsorted stones beside the market pitcher: the counts. He wanted the heaviest stone identified from the pile.'
            ),
            need=(
                "He needed the single heaviest stone named without sorting "
                "all five or picking up each one in sequence."
            ),
            mapping=(
                "`max` retains the heaviest candidate as it scans left to right. "
                "When the nine appears it displaces every prior maximum; "
                "nothing heavier follows, so nine wins."
            ),
            resolution=(
                "The heaviest stone emerged and the expected maximum returned from the pitcher. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(min -3 -1 -5)", expected=-5,
            concept_phrase="the minimum of the numbers",
            question_what="the smallest of -3, -1, and -5",
            goal_text="find the minimum of -3, -1, and -5",

            scenario=(
                "Caw set the stones on the road pitcher, each marked with "
                "a deficit score — negative three, negative one, negative five. "
                "She wanted the lowest deficit of the three."
            ),
            need=(
                "She needed to know which deficit was deepest — the most "
                "negative value among the three marked stones."
            ),
            mapping=(
                "`min` uses numeric ordering, not magnitude. Negative five "
                "lies below negative three and negative one on the number line, "
                "so it is the minimum even though its magnitude is largest."
            ),
            resolution=(
                "The deepest deficit was found and the expected minimum returned. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
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
                "The number of complete pouches emerged and the water rose to the expected mark. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(rem 17 5)", expected=2,
            concept_phrase="the remainder",
            question_what="the remainder when 17 is divided by 5",
            goal_text="find the remainder when 17 is divided by 5",

            scenario=(
                "Sable had seventeen acorns at the village and pouches of five. "
                "After filling as many pouches as possible she wanted to know "
                "how many acorns spilled out as the leftover."
            ),
            need=(
                "She needed the exact leftover count after complete pouches "
                "were formed — the portion that could not fill another group."
            ),
            mapping=(
                "`rem` subtracts complete groups and returns what is left. "
                "Seventeen minus three complete groups of five leaves a "
                "remainder that `rem` returns directly."
            ),
            resolution=(
                "The leftover count arrived and the expected remainder settled at the rim. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(mod 17 5)", expected=2,
            concept_phrase="the modulo operation",
            question_what="17 mod 5",
            goal_text="find 17 modulo 5",

            scenario=(
                "Korvus counted seventeen stones at the garden and sorted them "
                "into groups of five. He wanted the modulo — the cyclic "
                "position of the count within the group size."
            ),
            need=(
                "He needed the position within the repeating cycle of five, "
                "not just the leftover from integer division."
            ),
            mapping=(
                "`mod` like `rem` finds the remainder, but adjusts the sign "
                "to match the divisor. For positive inputs, `mod` and `rem` "
                "agree; the cyclic position is returned."
            ),
            resolution=(
                "The cyclic position within the group arrived as the value. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(quot 100 7)", expected=14,
            concept_phrase="the integer quotient",
            question_what="100 divided by 7, without remainder",
            goal_text="find the integer quotient of 100 divided by 7",

            scenario=(
                "Caw had a hundred stones at the meadow and baskets that held "
                "seven each. She wanted to know how many full baskets she "
                "could fill before running short."
            ),
            need=(
                "She needed the count of completely filled baskets, ignoring "
                "any stones left over that could not fill another."
            ),
            mapping=(
                "`quot` divides and truncates toward zero. One hundred stones "
                "yield a certain number of full baskets of seven; the truncated "
                "whole-number count is what `quot` returns."
            ),
            resolution=(
                "The full-basket count arrived and the expected quotient settled in the pitcher. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(rem 100 7)", expected=2,
            concept_phrase="the remainder",
            question_what="the remainder when 100 is divided by 7",
            goal_text="find the remainder when 100 is divided by 7",

            scenario=(
                "Sable continued from Caw's basket count at the hilltop pitcher. "
                "After filling all complete baskets of seven from a hundred "
                "stones, she wanted the leftover count."
            ),
            need=(
                "She needed to know how many stones remained after every "
                "complete basket was filled, the portion that could not fit."
            ),
            mapping=(
                "`rem` subtracts every complete group of seven from one hundred "
                "and returns what remains. The surplus after full groups is "
                "the remainder."
            ),
            resolution=(
                "The surplus stones were counted and the expected remainder returned. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(mod -7 3)", expected=2,
            concept_phrase="the modulo operation",
            question_what="negative seven mod 3",
            goal_text="find negative 7 modulo 3",

            scenario=(
                "Korvus had a deficit of seven at the orchard pitcher and "
                "groups of three. He wanted the modulo position — adjusted "
                "to stay within the positive cycle, not follow the deficit sign."
            ),
            need=(
                "He needed the cyclic position within a group of three, "
                "even though the starting count was negative."
            ),
            mapping=(
                "`mod` adjusts its result to share the sign of the divisor. "
                "With a positive divisor of three, the result is always "
                "non-negative, differing from `rem` for negative inputs."
            ),
            resolution=(
                "The sign-adjusted cyclic position arrived as the value. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
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
                "Sable had the stones already resting at the bottom of the pitcher "
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
                "The tally advanced by one and the expected new level arrived. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(dec 5)", expected=4,
            concept_phrase="the decrement operation",
            question_what="5 minus 1",
            goal_text="decrement 5 by 1",

            scenario=(
                "Caw had the stones stacked beside the market pitcher. "
                "She removed one from the top and needed to know the "
                "new stack height without counting the whole pile again."
            ),
            need=(
                "She needed the count after removing exactly one stone, "
                "the minimal step backward from five."
            ),
            mapping=(
                "`dec` subtracts exactly one from any integer, retreating "
                "the tally by a single unit. One stone removed, the "
                "count moves back by one, and `dec` returns that value."
            ),
            resolution=(
                "The tally retreated by one and the expected new count arrived. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(inc 0)", expected=1,
            concept_phrase="the increment operation",
            question_what="0 plus 1",
            goal_text="increment 0",

            scenario=(
                "Sable stood at the empty road pitcher with no stones inside. "
                "She held a single stone in her talon and wanted to know the "
                "new count after her first drop."
            ),
            need=(
                "She needed the count after dropping one stone into an "
                "empty pitcher — moving from zero to the first step."
            ),
            mapping=(
                "`inc` advances any integer by one. Starting from zero, "
                "a single increment step produces the smallest positive count, "
                "the first foothold above the empty baseline."
            ),
            resolution=(
                "The first stone was added and the count of one returned. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(dec 0)", expected=-1,
            concept_phrase="the decrement operation",
            question_what="0 minus 1",
            goal_text="decrement 0",

            scenario=(
                "Korvus had an empty pitcher at the garden — zero stones inside. "
                "He removed one imaginary stone below the baseline and wanted "
                "to know what count the pitcher showed."
            ),
            need=(
                "He needed the count after stepping backward from zero, "
                "crossing into negative territory."
            ),
            mapping=(
                "`dec` moves below zero without stopping. Decrementing zero "
                "yields a negative count — the pitcher's tally crosses the "
                "empty baseline and continues downward."
            ),
            resolution=(
                "The tally crossed below zero and the expected negative count arrived. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(inc -1)", expected=0,
            concept_phrase="the increment operation",
            question_what="negative 1 plus 1",
            goal_text="increment negative 1",

            scenario=(
                "Caw had a deficit of one at the village pitcher — one below "
                "empty. She added a single stone and wanted to know whether "
                "the count climbed back to zero."
            ),
            need=(
                "She needed to know whether adding one stone to a negative-one "
                "deficit returned the count to neutral."
            ),
            mapping=(
                "`inc` adds one regardless of sign. Incrementing negative one "
                "cancels the deficit exactly, returning the tally to zero — "
                "the neutral baseline of the pitcher."
            ),
            resolution=(
                "The deficit was cancelled and the expected neutral count returned. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
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
                "Korvus stood at the garden with the stones on the right side "
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
                "The unsigned distance emerged and settled as the count. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(abs -5)", expected=5,
            concept_phrase="the absolute value",
            question_what="the absolute value of negative 5",
            goal_text="find the absolute value of negative 5",

            scenario=(
                "Sable had a deficit of five at the orchard pitcher — five "
                "below the baseline. She needed to know the magnitude of "
                "that gap without the sign."
            ),
            need=(
                "She needed the distance from zero as a positive count, "
                "the sign stripped away completely."
            ),
            mapping=(
                "`abs` reflects any negative count across zero, yielding "
                "its positive mirror. A deficit of five is five units from "
                "zero, so `abs` returns five."
            ),
            resolution=(
                "The deficit was reflected and the expected positive distance arrived. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(abs 0)", expected=0,
            concept_phrase="the absolute value",
            question_what="the absolute value of 0",
            goal_text="find the absolute value of 0",

            scenario=(
                "Korvus stood at the empty road pitcher with exactly zero "
                "stones inside. He asked the pitcher the distance from zero "
                "to zero — a question of pure baseline."
            ),
            need=(
                "He needed confirmation that zero has no distance from itself "
                "and that `abs` would return the neutral baseline."
            ),
            mapping=(
                "`abs` of zero is zero — the empty baseline is already its "
                "own reflection. No sign to strip, no distance to measure; "
                "the pitcher returns the neutral count unchanged."
            ),
            resolution=(
                "The neutral count returned unchanged and the expected zero arrived. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(abs (- 3 8))", expected=5,
            concept_phrase="the absolute value",
            question_what="the absolute value of the difference between 3 and 8",
            goal_text="find the absolute value of 3 minus 8",

            scenario=(
                "Caw scratched the subtraction of three from eight on the "
                "hilltop pitcher's rim, producing a negative difference. "
                "She then asked the pitcher for the magnitude of that gap."
            ),
            need=(
                "She needed the size of the gap between three and eight, "
                "regardless of which was larger."
            ),
            mapping=(
                "The inner form `(- 3 8)` resolves to a negative value first; "
                "`abs` then strips the sign, returning the pure unsigned "
                "distance between the two counts."
            ),
            resolution=(
                "The gap was measured and the expected unsigned distance returned. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
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
                'The exact fractional sum arrived and the pitcher returned it without rounding. (count: 4) (with `1/2` as the input value)'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 2/3 3/4)", expected="1/2",
            concept_phrase="the product of two ratios",
            question_what="the product of two-thirds and three-quarters",
            goal_text="multiply two-thirds by three-quarters",

            scenario=(
                "Sable had a stone split into thirds and took two of those "
                "thirds at the meadow pitcher. She then kept three-quarters "
                "of what she held and needed the exact fraction remaining."
            ),
            need=(
                "She needed the precise fractional product without any rounding, "
                "the exact portion after both cuts."
            ),
            mapping=(
                "`*` on ratios multiplies numerator by numerator and denominator "
                "by denominator, then reduces. Both fractions stay exact; "
                "the product is a simplified fraction."
            ),
            resolution=(
                'The exact fractional product arrived in simplified form from the pitcher. (count: 3) (with `2/3` as the input value)'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(- 1 1/3)", expected="2/3",
            concept_phrase="the difference of a whole and a ratio",
            question_what="1 minus one-third",
            goal_text="subtract one-third from 1",

            scenario=(
                "Korvus held a whole stone at the farm pitcher and gave away "
                "one-third of it. He needed to know the exact fractional "
                "portion remaining after the gift."
            ),
            need=(
                "He needed the exact fraction left after removing one-third "
                "from a whole, with no rounding introduced."
            ),
            mapping=(
                "`-` treats 1 as a ratio 1/1 and finds a common denominator "
                "with 1/3. The subtraction stays exact throughout, returning "
                "the precise remaining fraction."
            ),
            resolution=(
                "The exact remaining fraction arrived and the pitcher returned it without loss. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
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
                "Sable had the stones on the rim at the village and two "
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
                "The even share arrived as an integer and the water rose to the expected level. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(/ 10 3)", expected="10/3",
            concept_phrase="the division operation",
            question_what="the exact rational result of using / on 10 and 3",
            goal_text="divide 10 by 3",

            scenario=(
                "Caw tried to split the stones into three equal groups at "
                "the orchard pitcher. The division did not come out whole "
                "and she needed the exact result, not an approximation."
            ),
            need=(
                "She needed the precise fractional result rather than a "
                "rounded decimal, preserving the full division exactly."
            ),
            mapping=(
                "`/` on integers returns a ratio when the division is not exact. "
                "Ten does not divide evenly by three; the pitcher hands back "
                "the exact rational form rather than approximating."
            ),
            resolution=(
                "The exact rational result arrived in fraction form from the pitcher. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(/ 1.0 2)", expected=0.5,
            concept_phrase="the division operation",
            question_what="the result of 1.0 divided by 2",
            goal_text="divide 1.0 by 2",

            scenario=(
                "Sable dropped one float-stone marked 1.0 into the road pitcher "
                "and asked for it split in half. She expected a decimal result, "
                "not a rational fraction."
            ),
            need=(
                "She needed the floating-point half rather than the exact "
                "ratio, since the input was already a float."
            ),
            mapping=(
                "When either operand is a float, `/` promotes the result to "
                "floating-point. One-point-zero divided by two yields a "
                "decimal value, not the exact ratio one-half."
            ),
            resolution=(
                "The float result arrived and the pitcher returned the expected decimal value. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
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
                "The compounded product settled and the count filled the pitcher. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 5 5)", expected=25,
            concept_phrase="repeated multiplication",
            question_what="5 to the second power",
            goal_text="multiply 5 by itself",

            scenario=(
                "Caw arranged five rows of the stones each on the meadow "
                "pitcher's rim. She wanted the total from multiplying one "
                "dimension by itself — a square count."
            ),
            need=(
                "She needed the square of five: the count from pairing "
                "each row with each position, in one form."
            ),
            mapping=(
                "`*` with two identical arguments computes the square. "
                "Five rows of five is the simplest repeated multiplication, "
                "the product of the number with itself."
            ),
            resolution=(
                "The square count settled and the product arrived from the pitcher. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 3 3 3 3)", expected=81,
            concept_phrase="repeated multiplication",
            question_what="3 to the fourth power",
            goal_text="multiply 3 by itself four times",

            scenario=(
                "Sable scratched four tallies of three onto the village pitcher's "
                "rim, each layer compounding the last. She wanted the final "
                "product of all four self-multiplications."
            ),
            need=(
                "She needed three raised to the fourth power — the product "
                "of multiplying three by itself four times over."
            ),
            mapping=(
                "`*` with four identical arguments multiplies left to right, "
                "compounding each layer: three by three, then by three again, "
                "then by three a final time."
            ),
            resolution=(
                "The four-layer product settled and the count filled the pitcher. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 10 10)", expected=100,
            concept_phrase="repeated multiplication",
            question_what="10 to the second power",
            goal_text="multiply 10 by itself",

            scenario=(
                "Korvus lined ten rows of the stones along the farm pitcher's "
                "rim, filling a square arrangement. He needed the total count "
                "of all stones in the square."
            ),
            need=(
                "He needed ten squared — the count that fills a ten-by-ten "
                "arrangement — returned in one form."
            ),
            mapping=(
                "`*` with two tens computes their product in one step. "
                "Ten rows of ten yields the square, "
                "the simplest square of a round number."
            ),
            resolution=(
                "The square was computed and the expected round total arrived. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
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
                "a single vine stringing all the pebbles in sequence."
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
                "a single vine carrying all the pebbles in sequence, "
                "the join seamless, the pebble-string complete at beak-reach. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(str 42)', expected="42",
            concept_phrase='the string coercion of an integer',
            question_what='the result of using str on the integer 42',
            goal_text='use str to coerce the integer 42 to its string representation',

            scenario=(
                "Sable held a stone-count of forty-two at the market pitcher "
                "but needed to thread it onto a vine as individual bead-characters, "
                "not carry it as a raw number."
            ),
            need=(
                "She needed the integer converted to a pebble-string form "
                "so it could be joined onto other vines."
            ),
            mapping=(
                "`str` on any non-string value converts it to its printed "
                "representation. The integer forty-two becomes the two-bead "
                "vine \"42\", ready to be strung with other pebbles."
            ),
            resolution=(
                "The integer became a two-bead vine and the expected string returned. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(str "p" "q" "r")', expected="pqr",
            concept_phrase='the three-arg string concatenation',
            question_what='the result of using str to join "p", "q", and "r"',
            goal_text='use str to join the three single-character strings "p", "q", and "r"',

            scenario=(
                "Caw had three single-bead vines in the garden: one strung "
                "with p, one with q, one with r. She wanted all three threaded "
                "onto a single continuous vine in order."
            ),
            need=(
                "She needed the three single-bead vines joined end-to-end "
                "without gaps or separators."
            ),
            mapping=(
                "`str` with three arguments appends each vine to the previous "
                "left to right. P is followed by q, which is followed by r; "
                "the result is one unbroken pebble-string."
            ),
            resolution=(
                "The three vines joined seamlessly and the expected pebble-string arrived. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(str 1 "+" 2 "=" 3)', expected="1+2=3",
            concept_phrase='the mixed string concatenation',
            question_what='the result of using str to join 1, "+", 2, "=", and 3',
            goal_text='use str to join the integer 1, the plus sign, the integer 2, the equals sign, and the integer 3',

            scenario=(
                "Korvus wanted to label the rim of the road pitcher with "
                "an equation. He had two integers and two symbol-beads as "
                "separators, all needing to form one vine."
            ),
            need=(
                "He needed integers and symbol-bead strings joined into one "
                "vine without losing any part of the equation shape."
            ),
            mapping=(
                "`str` converts each argument to its string form and appends "
                "them in order. Integers become digit-beads; string arguments "
                "are threaded as-is; all join into one pebble-string vine."
            ),
            resolution=(
                "All five pieces joined into one vine and the expected equation-string returned. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
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
                "The pitcher wrote the message and returned nil, exactly. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(print "x")', expected=None,
            concept_phrase='the print call',
            question_what='the return value of using print on the string "x"',
            goal_text='print the string "x" without a newline',

            scenario=(
                "Sable pressed a single character \"x\" into the pitcher's clay "
                "at the village, with no line-break notch at the end. She "
                "asked what value the pitcher handed back after writing."
            ),
            need=(
                "She needed to know what `print` returned as a value, "
                "separate from what it wrote to the output."
            ),
            mapping=(
                "`print` writes its argument without a trailing newline and "
                "returns nil. The clay is marked, but the wing-cache is empty — "
                "output and return value are entirely separate things."
            ),
            resolution=(
                "The mark was pressed and nil returned, exactly. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
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
                "Both gates passed and the value arrived at the rim."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(and true false)", expected=False,
            concept_phrase="the logical and",
            question_what="the result of using and on true and false",
            goal_text="test true and false with the and operator",

            scenario=(
                "Caw approached the road pitcher with two gate-arms across the "
                "mouth: the first raised open, the second lowered shut. "
                "She wanted to know if passage through both was possible."
            ),
            need=(
                "She needed a verdict on the whole chain — open only if every "
                "gate was open, closed the moment any gate was shut."
            ),
            mapping=(
                "`and` checks gates left to right and short-circuits on the "
                "first falsey value. The second gate is closed; `and` returns "
                "that falsey value without checking any further."
            ),
            resolution=(
                "The second gate closed the chain and the expected false value returned."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(or false true)", expected=True,
            concept_phrase="the logical or",
            question_what="the result of using or on false and true",
            goal_text="test false or true with the or operator",

            scenario=(
                "Sable reached a fork at the orchard pitcher: the left gate-arm "
                "was shut, the right one open. She needed to know if at least "
                "one arm offered passage."
            ),
            need=(
                "She needed a single verdict — open if any one gate was open, "
                "closed only if every gate was shut."
            ),
            mapping=(
                "`or` checks gates left to right and short-circuits on the first "
                "truthy value. The left arm is false; `or` moves to the right "
                "arm, finds it open, and returns that truthy value."
            ),
            resolution=(
                "The right arm opened and the expected truthy value returned."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(or false false)", expected=False,
            concept_phrase="the logical or",
            question_what="the result of using or on false and false",
            goal_text="test false or false with the or operator",

            scenario=(
                "Korvus found both gate-arms at the meadow pitcher shut. "
                "He asked whether any arm offered passage — but neither "
                "arm was open to let him through."
            ),
            need=(
                "He needed to know if even one gate was open, willing to "
                "accept any truthy arm as enough."
            ),
            mapping=(
                "`or` exhausts all gates before giving up. Both are false; "
                "no truthy value is ever found, so `or` returns the last "
                "value it checked — still false."
            ),
            resolution=(
                "Both gates were shut and the expected false value returned."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(and 1 2 3)", expected=3,
            concept_phrase="the logical and",
            question_what="the result of using and on 1, 2, and 3",
            goal_text="apply and to 1, 2, and 3",

            scenario=(
                "Caw set the stones marked 1, 2, and 3 as gate tokens at "
                "the village pitcher. All three were truthy. She wanted "
                "to know what `and` would return at the end."
            ),
            need=(
                "She needed to know what value `and` handed back when every "
                "gate token was truthy all the way through."
            ),
            mapping=(
                "`and` returns the last value it checked when no falsey value "
                "is found. All three tokens are truthy; `and` advances "
                "to the end and returns the final stone's value."
            ),
            resolution=(
                "All three gates passed and the last value returned. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(or nil false 5)", expected=5,
            concept_phrase="the logical or",
            question_what="the result of using or on nil, false, and 5",
            goal_text="apply or to nil, false, and 5",

            scenario=(
                "Sable checked three gate tokens at the farm pitcher in order: "
                "nil, then false, then a stone marked 5. She wanted the first "
                "truthy token the chain would accept."
            ),
            need=(
                "She needed `or` to skip past falsey tokens and return "
                "the first truthy one it encountered."
            ),
            mapping=(
                "`or` skips nil and false because both are falsey. When it "
                "reaches 5, a non-nil non-false value, it short-circuits "
                "immediately and returns that stone."
            ),
            resolution=(
                "The first truthy token was found and the value returned. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
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
        SubjectExample(
            form="(not false)", expected=True,
            concept_phrase="the logical not",
            question_what="the result of using not on false",
            goal_text="negate the value false",

            scenario=(
                "Korvus found the gate-arm above the road pitcher fully lowered "
                "shut — the value was false. He asked the pitcher what "
                "the opposite of that closed state would be."
            ),
            need=(
                "He needed the inverted reading: the closed arm flipped to "
                "an open arm, the falsey value turned truthy."
            ),
            mapping=(
                "`not` inverts any value to strict true or false. False is "
                "falsey; flipping it yields true. The arm rises, the gate "
                "opens, and `not` returns true."
            ),
            resolution=(
                "The gate was flipped open and the expected true value arrived."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(not nil)", expected=True,
            concept_phrase="the logical not",
            question_what="the result of using not on nil",
            goal_text="negate the value nil",

            scenario=(
                "Caw discovered nil hanging at the orchard pitcher's gate — "
                "an empty arm, no value at all. She asked the pitcher "
                "what the opposite of nothing would be."
            ),
            need=(
                "She needed to know whether nil, the absent value, would "
                "flip to true when negated."
            ),
            mapping=(
                "`not` treats nil as falsey — the same as false for this "
                "purpose. Flipping nil yields true; absence of value "
                "negated is presence of truth."
            ),
            resolution=(
                "Nil was flipped and the expected true value returned from the pitcher."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(not 0)", expected=False,
            concept_phrase="the logical not",
            question_what="the result of using not on 0",
            goal_text="negate the value 0",

            scenario=(
                "Sable placed a stone marked zero at the hilltop pitcher gate — "
                "a common value that many crows assume to be falsey. "
                "She wanted to know what `not` returned for it."
            ),
            need=(
                "She needed to confirm whether zero, when negated, would "
                "yield true or false — a test of Clojure's truthy rules."
            ),
            mapping=(
                "`not` returns true only for false and nil. Zero is truthy "
                "in Clojure; negating a truthy value always yields false, "
                "regardless of what the value is."
            ),
            resolution=(
                "Zero proved truthy and `not` returned the expected false value. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(not "")', expected=False,
            concept_phrase="the logical not",
            question_what="the result of using not on the empty string",
            goal_text="negate the empty string",

            scenario=(
                "Korvus found an empty vine strung on the village pitcher — "
                "no beads at all, the empty string. He wanted to know "
                "what `not` would say about an empty pebble-string."
            ),
            need=(
                "He needed to know whether the empty string counted as falsey "
                "and would flip to true under `not`."
            ),
            mapping=(
                "The empty string is truthy in Clojure — only false and nil "
                "are falsey. `not` of a truthy value is always false; "
                "even an empty vine is still a vine."
            ),
            resolution=(
                "The empty vine proved truthy and the expected false value returned. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
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
                "The then-branch opened and the expected stone came back from the pitcher. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(if "" 1 0)', expected=1,
            concept_phrase="the if conditional with empty string as condition",
            question_what="the result of if with condition the empty string, then-branch 1, else-branch 0",
            goal_text="use if to return 1 when the condition is the empty string (then-branch) and 0 otherwise (else-branch)",

            scenario=(
                "Caw placed an empty pebble-string at the fork above the "
                "orchard pitcher. The then-path held one stone; the else-path "
                "held zero. She wanted to know which path opened."
            ),
            need=(
                "She needed to know whether the empty string was truthy enough "
                "to open the then-gate or whether the else-path would fire."
            ),
            mapping=(
                "The empty string is truthy in Clojure. `if` opens the "
                "then-gate for any truthy condition; even an empty vine "
                "is not false or nil, so the then-branch fires."
            ),
            resolution=(
                "The then-branch opened and the expected then-value returned. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(if nil 1 0)", expected=0,
            concept_phrase="the if conditional with nil as condition",
            question_what="the result of if with condition nil, then-branch 1, else-branch 0",
            goal_text="use if to return 1 when the condition is nil (then-branch) and 0 otherwise (else-branch)",

            scenario=(
                "Sable placed nil — the absent value — at the fork above the "
                "road pitcher. The then-path held one stone; the else-path "
                "held zero. She wanted to know which path was chosen."
            ),
            need=(
                "She needed to confirm that nil, the absent value, would "
                "close the then-gate and send the pitcher down the else-path."
            ),
            mapping=(
                "Nil is one of only two falsey values in Clojure. `if` closes "
                "the then-gate for nil and opens the else-gate instead, "
                "returning the else-branch value."
            ),
            resolution=(
                "The else-branch opened and the expected else-value returned. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(if false 1 0)", expected=0,
            concept_phrase="the if conditional with false as condition",
            question_what="the result of if with condition false, then-branch 1, else-branch 0",
            goal_text="use if to return 1 when the condition is false (then-branch) and 0 otherwise (else-branch)",

            scenario=(
                "Korvus placed the value false at the fork above the hilltop "
                "pitcher. The then-path held one stone; the else-path held "
                "zero. He wanted to know which fork the pitcher would take."
            ),
            need=(
                "He needed to confirm that false would close the then-gate "
                "and route the pitcher to the else-path."
            ),
            mapping=(
                "False is the other falsey value alongside nil. `if` closes "
                "the then-gate for false and routes to the else-branch, "
                "returning that branch's value."
            ),
            resolution=(
                "The else-branch opened and the expected else-value returned. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
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
                "The gate opened and the expected boolean value rose from the pitcher. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(boolean "")', expected=True,
            concept_phrase="the boolean conversion",
            question_what="the result of using boolean on the empty string",
            goal_text="convert the empty string to a boolean",

            scenario=(
                "Caw placed an empty pebble-string vine at the garden pitcher "
                "and asked for its strict boolean reading. She wondered if "
                "nothing on the vine would count as false."
            ),
            need=(
                "She needed the strict true-or-false value for an empty vine, "
                "not a guess based on other languages' rules."
            ),
            mapping=(
                "`boolean` converts the empty string to true because it is "
                "neither false nor nil. An empty vine is still a vine; "
                "presence of the string type makes it truthy."
            ),
            resolution=(
                "The empty vine registered as truthy and the expected true value arrived. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(boolean nil)", expected=False,
            concept_phrase="the boolean conversion",
            question_what="the result of using boolean on nil",
            goal_text="convert nil to a boolean",

            scenario=(
                "Sable brought the absent value nil to the meadow pitcher and "
                "asked for its strict boolean reading. Nil represents the "
                "total absence of a value."
            ),
            need=(
                "She needed to know which gate nil belonged to when cast "
                "explicitly to true or false."
            ),
            mapping=(
                "`boolean` on nil returns false because nil is one of the two "
                "falsey values. Total absence maps to the closed gate — "
                "the only strict false among non-boolean values."
            ),
            resolution=(
                "Nil mapped to the closed gate and the expected false value returned."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(boolean false)", expected=False,
            concept_phrase="the boolean conversion",
            question_what="the result of using boolean on false",
            goal_text="convert false to a boolean",

            scenario=(
                "Korvus presented false itself to the road pitcher and asked "
                "for its strict boolean conversion — casting a boolean into "
                "a boolean as a sanity check."
            ),
            need=(
                "He needed confirmation that false, already a boolean, would "
                "convert to false without any surprise."
            ),
            mapping=(
                "`boolean` on false returns false. The value is already its "
                "own boolean; the conversion is the identity for a value "
                "that is already strict true or false."
            ),
            resolution=(
                "False converted to itself and the expected false value returned unchanged."
            ),
            tags=("story",),
        ),
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
                "without disturbing its neighbour. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(:tortoise {:hare 1 :tortoise 2})", expected=2,
            concept_phrase="the keyword lookup",
            question_what="the result of using the keyword :tortoise as a function on the map {:hare 1 :tortoise 2}",
            goal_text="use the keyword :tortoise to look up a value in the map with keys :hare and :tortoise",

            scenario=(
                "Korvus returned to the same stone-pile at the hilltop pitcher: "
                "a :hare stone carrying one, and a :tortoise stone carrying two. "
                "This time he needed the count under :tortoise."
            ),
            need=(
                "He needed the value stored under the :tortoise label, "
                "leaving the :hare stone undisturbed."
            ),
            mapping=(
                ":tortoise used as a function reaches into the stone-pile "
                "and pulls the value stored beneath that label. Labels "
                "are independent; :tortoise retrieves its own value."
            ),
            resolution=(
                "The :tortoise count was lifted and the value returned. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(:missing {:hare 1})", expected=None,
            concept_phrase="the keyword lookup",
            question_what="the result of using the keyword :missing as a function on the map {:hare 1}",
            goal_text="use the keyword :missing to look up a value in a map that does not contain :missing",

            scenario=(
                "Caw reached into a stone-pile at the orchard pitcher marked "
                "only with :hare and asked for the count under :missing — "
                "a label that did not exist in the pile."
            ),
            need=(
                "She needed to know what the pitcher returned when a label "
                "was absent from the stone-pile entirely."
            ),
            mapping=(
                "Keyword lookup returns nil when the label is not in the map. "
                "No :missing stone exists in the pile; the pitcher finds "
                "nothing under that label and returns the absent value."
            ),
            resolution=(
                "The absent label returned nil, the expected absent value. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
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
                "The chalk-mark was confirmed as a symbol and the answer arrived."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(= (quote tortoise) 'tortoise)", expected=True,
            concept_phrase="the equality of long-form and short-form quoting",
            question_what="whether long-form and short-form quoting produce equal values",
            goal_text="compare the result of long-form quoting of tortoise against the apostrophe-shorthand quoting of the same name, using =",

            scenario=(
                "Sable scratched the name tortoise on two separate stones at "
                "the meadow pitcher — once using the long `quote` word, once "
                "using the apostrophe shorthand. She wondered if they matched."
            ),
            need=(
                "She needed to confirm both notations produced the same "
                "chalk-mark shape and that the pitcher saw them as equal."
            ),
            mapping=(
                "`quote` and the apostrophe `'` are two spellings of the same "
                "quoting operation. Both produce the symbol `tortoise`; `=` "
                "compares the two chalk-marks and finds them identical."
            ),
            resolution=(
                "Both marks matched and the expected true value came back from the pitcher."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(count '(1 2 3))", expected=3,
            concept_phrase="the element count of a quoted list",
            question_what="the number of elements in a quoted list",
            goal_text="count the elements in a quoted list of the integers 1, 2, and 3",

            scenario=(
                "Korvus scratched a quoted list of three integers on the "
                "village pitcher's rim using the apostrophe shorthand. He "
                "wanted the count of chalk-marks in the list, not their sum."
            ),
            need=(
                "He needed the number of elements in the list-as-data, "
                "not any evaluation of the numbers inside."
            ),
            mapping=(
                "The apostrophe suppresses evaluation; `count` then walks "
                "the resulting list as a chalk-mark structure. Three marks "
                "are in the list, so the count is three."
            ),
            resolution=(
                "The list was counted as data and the expected element count arrived. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
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
                "The exact product arrived without overflow and the water rose to the full count. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(+ 99999999999 1)", expected=100000000000,
            concept_phrase="the large addition",
            question_what="the sum of 99999999999 and 1",
            goal_text="add 1 to 99999999999",

            scenario=(
                "Caw had a vast pile of stones at the farm pitcher — nearly "
                "one hundred billion — and wanted to add one final stone "
                "without any digit dropping off the end."
            ),
            need=(
                "She needed the exact result even if the sum crossed a "
                "boundary that would overflow a regular integer counter."
            ),
            mapping=(
                "Clojure promotes the result to bigint automatically when the "
                "sum exceeds the regular integer range. The pitcher widens "
                "its capacity and holds the full exact count."
            ),
            resolution=(
                "The promotion happened silently and the exact sum arrived without truncation. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
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
                "3 — three passes made, the stones counted, the tally "
                "settling as the answer. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(count "hello")', expected=5,
            concept_phrase="the count operation",
            question_what="the result of using count on the string hello",
            goal_text="count the characters in the string hello",

            scenario=(
                "Korvus had a vine strung with the pebbles spelling \"hello\" "
                "at the village pitcher. He wanted to tally each bead as he "
                "walked the vine from left to right."
            ),
            need=(
                "He needed the exact bead count so he could compare it against "
                "other vine lengths without unthreading them."
            ),
            mapping=(
                "`count` on a string walks each character as a talon-step, "
                "incrementing the tally with every bead. The running tally "
                "at the final step is the character count."
            ),
            resolution=(
                "The vine was walked completely and the expected bead count returned. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(count [])", expected=0,
            concept_phrase="the count operation",
            question_what="the result of using count on the empty vector",
            goal_text="count the elements in an empty vector",

            scenario=(
                "Caw found an empty bracket-holder at the road pitcher — "
                "a vector with no stones inside at all. She walked the "
                "rim but found nothing to count."
            ),
            need=(
                "She needed confirmation that `count` on an empty collection "
                "would return zero and not raise an error."
            ),
            mapping=(
                "`count` of an empty collection takes zero talon-steps. No "
                "elements exist to tally; the running count never advances "
                "and the pitcher returns zero."
            ),
            resolution=(
                "The empty collection yielded zero steps and the count of zero returned. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
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
                "The bead tally arrived and the expected character count settled in the pitcher. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(count "hare")', expected=4,
            concept_phrase="the count of characters in a string",
            question_what="the result of using count on the string hare",
            goal_text="count the characters in the string hare",

            scenario=(
                "Sable held a vine strung with the pebbles spelling \"hare\" "
                "at the meadow pitcher. She wanted to compare its length to "
                "the longer \"tortoise\" vine she had measured earlier."
            ),
            need=(
                "She needed the exact bead count of the shorter vine to "
                "compare lengths without holding both at once."
            ),
            mapping=(
                "`count` on \"hare\" walks four beads: h, a, r, e. "
                "Each is a talon-step; the tally at the end is the "
                "number of beads on that vine."
            ),
            resolution=(
                "The four beads were tallied and the expected character count returned. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(count (subs "tortoise" 0 3))', expected=3,
            concept_phrase="the count of characters in a leading substring",
            question_what="the count of the substring from index 0 to 3 of the string tortoise",
            goal_text="extract the leading three characters from the string tortoise using subs from index 0 to 3, then count them",

            scenario=(
                "Korvus wanted only the first three beads of the \"tortoise\" vine "
                "at the garden pitcher. He clipped the vine using `subs` from "
                "position zero to three, then counted what remained."
            ),
            need=(
                "He needed the bead count of just the leading segment, "
                "after trimming the vine to the first three characters."
            ),
            mapping=(
                "`subs` snips a sub-vine from index 0 up to but not including "
                "index 3. `count` then walks that shorter vine, "
                "tallying each bead in the clipped segment."
            ),
            resolution=(
                "The clipped vine was counted and the expected character count arrived. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
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
                "Caw sat at the farm with five rows of the stones each on "
                "the pitcher's rim, then the stones set aside to remove. "
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
                "The nested product resolved first and the final count arrived. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(+ (* 3 8) (* 2 4))", expected=32,
            concept_phrase="the sum of products",
            question_what="the result of adding the product of 3 and 8 to the product of 2 and 4",
            goal_text="compute the product of 3 and 8, add the product of 2 and 4",

            scenario=(
                "Sable had two separate piles at the village pitcher: one from "
                "three groups of eight, another from two groups of four. She "
                "needed the combined total of both products."
            ),
            need=(
                "She needed both products computed first, then summed "
                "together — all in one form without intermediate steps."
            ),
            mapping=(
                "Two nested `*` forms each resolve to a wing-cache value; the "
                "outer `+` then sums those two sub-results. Each inner "
                "form runs to completion before the outer one begins."
            ),
            resolution=(
                "Both inner products resolved and their sum arrived as the total. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(quot (+ 100 50) 5)", expected=30,
            concept_phrase="the nested quotient",
            question_what="the integer quotient of the sum of 100 and 50 divided by 5",
            goal_text="add 100 and 50, then divide by 5",

            scenario=(
                "Korvus gathered a hundred and fifty stones at the farm pitcher "
                "by combining two piles of one hundred and fifty. He then "
                "needed to share them equally among five baskets."
            ),
            need=(
                "He needed the combined pile summed first, then the whole-basket "
                "count from dividing that total by five."
            ),
            mapping=(
                "The inner `(+ 100 50)` resolves to the combined sum first. "
                "`quot` then divides that sum by five, truncating to the "
                "whole-basket count without any fractional remainder."
            ),
            resolution=(
                "The sum resolved and the whole-basket quotient arrived. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
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
