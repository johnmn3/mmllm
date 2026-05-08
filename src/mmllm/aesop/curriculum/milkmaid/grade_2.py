"""Grade 2 — operators + arithmetic mastery, taught through the milkmaid fable.

Grade 2 deepens grade 1's L1+L2 work. Where grade 1 introduced the
single-arg arithmetic call, grade 2 covers multi-arg arithmetic,
comparison chains, the boolean-logic operators, the numeric helpers
(inc/dec/quot/rem/mod, min/max, abs), strings via str, and the
truthy/falsey rules.

The fable lens: the Milkmaid's hasty boasts about answers ('I can guess
without computing!') consistently lose to the Farmer's patient
"let me actually evaluate the form" approach. By grade 2, this becomes
the running joke of the curriculum.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.milkmaid.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SHARED_SUBPLOTS,
    _GOAL_SUBPLOTS,
    _PLAN_POOL,
)
from mmllm.aesop.curriculum.milkmaid._metaphor_pools import (
    _ACORN_SUBPLOTS, _BASKET_SUBPLOTS, _BEADSTRING_SUBPLOTS, _CHALKMARK_SUBPLOTS, _GATE_SUBPLOTS, _SCRIBE_SUBPLOTS, _TALLYWALK_SUBPLOTS,
)


# Extend grade-1's shared pool with two grade-2-specific subplots
# that lean into multi-operand / chained-operator framings.
_SHARED_SUBPLOTS: list[SubplotTemplate] = list(_G1_SHARED_SUBPLOTS) + [
    # 9. The chain-of-operations template — useful for multi-arg
    #    arithmetic and comparison-chain subjects.
    SubplotTemplate("""\
{farmer_phrase} had been laying out a chain of small computations on
a slate {place} — one operation, then another, all to settle a
question {milkmaid_phrase}, {emo_boastful} had raised. The current form on the slate was
{form_display}, and {farmer} explained that {concept_phrase} would
be settled the moment the form was evaluated."""),

    # 10. The wager-with-stakes template — increases the dramatic stakes
    #     when the form is more interesting (e.g., min/max, mod).
    SubplotTemplate("""\
"Whatever {form_display} comes to," {milkmaid_phrase} declared, {emo_proud},
{place}, "I'll wager I know it without typing it." {farmer_phrase},
{emo_patient}, picked up a stick and drew {concept_phrase} in the
dust. "Then write the form," {farmer_he_she_cap} said. "The REPL will
have the last word.\""""),
]


def _ex(form, expected, concept, what, goal=""):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal)


# ─────────────────────── 22 grade-2 subjects ───────────────────────


G2_01 = SubjectCurriculum(
    grade=2, subject_id="G2-01",
    subject_title="Multi-arg arithmetic",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(+ 1 2 3 4)", expected=10,
            concept_phrase="the multi-arg sum",
            question_what="the sum of 1, 2, 3, and 4",
            goal_text="add 1, 2, 3, and 4",
        ),
        SubjectExample(
            form="(* 2 3 4)", expected=24,
            concept_phrase="the multi-arg product",
            question_what="the product of 2, 3, and 4",
            goal_text="multiply 2, 3, and 4",
            scenario=(
                "The farmer had been tallying the harvest at the market table, counting coins "
                "from three separate sales. Two coins from the first sale, three from the second, "
                "four from the third — she needed to know the total yield."
            ),
            need=(
                "She needed a multiplication that stacked all several numbers together into one "
                "final count without guessing or approximating any step."
            ),
            mapping=(
                "The multi-arg product is the farmer's coin-stack: take alseveral numbersrs, "
                "multiply them in order, and carry each result forward. One number times the "
                "next times the next — the tally compounds with each step."
            ),
            resolution=(
                "{drawn.a} returned: the REPL returned the complete product — one number multiplied by all the "
                "others, the harvest tally complete."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(- 100 1 2 3)", expected=94,
            concept_phrase="the multi-arg subtraction",
            question_what="100 minus 1, 2, and 3",
            goal_text="subtract 1, 2, and 3 from 100",
            scenario=(
                "The farmer had counted 100 coins but discovered three deductions along the way: "
                "1 coin lost, 2 coins spent at the mill, 3 more paid for salt. She stood at the "
                "counting table, needing the true total after all losses."
            ),
            need=(
                "She needed to subtract all three losses from the original 100 in one form, "
                "carrying forward each reduction without losing track."
            ),
            mapping=(
                "The multi-arg subtraction is the farmer's careful accounting: begin with 100, "
                "subtract the first loss, subtract the second from that result, subtract the third. "
                "Each step reduces what remains; the tally shrinks by each amount."
            ),
            resolution=(
                "The REPL returned the final count — 100 with all three deductions applied, "
                "the true total after all losses were paid."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(+ 1 2 3 4 5 6 7 8 9 10)", expected=55,
            concept_phrase="the sum of ten numbers",
            question_what="the sum of integers 1 through 10",
            goal_text="add the integers 1 through 10",
            scenario=(
                "The farmer had a row of piles of coins on the counting table, one for each day of "
                "the market week. Day one brought 1 coin, day two brought 2, day three brought 3, "
                "and so on through day ten's 10 coins. She needed the weekly total."
            ),
            need=(
                "She needed to sum all ten daily amounts together into one grand total, tallying "
                "each day's coins without losing any along the way."
            ),
            mapping=(
                "The sum of {drawn.j} numbers is the farmer's daily tally-walk: start at zero, add day one's coin, add day two's coins to that, add day three's to the running sum, and so forward through all ten days. Each addition carries the previous total forward."
            ),
            resolution=(
                "The REPL returned the weekly total — all ten days' coins counted, stacked, and "
                "summed into the final market harvest."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 1 2 3 4 5)", expected=120,
            concept_phrase="the multi-arg product",
            question_what="the product of 1 through 5",
            goal_text="multiply the integers 1 through 5",
            scenario=(
                "The farmer had five merchants, each with a different tier of multiplier. One merchant "
                "multiplied prices by 1, another by 2, another by 3, by 4, and by 5. She needed to see "
                "what the compounded multiplier would be across all five."
            ),
            need=(
                "She needed to multiply all five tiers together to find the final magnification factor, "
                "counting each multiplication as it cascaded from one level to the next."
            ),
            mapping=(
                "The product of 1 through 5 is the farmer's cascading multiplier: begin at 1, multiply "
                "by 2, multiply that result by 3, then by 4, then by 5. The tally grows with each "
                "multiplication step, compounding upward."
            ),
            resolution=(
                "The REPL returned the final multiplier — all a list of numbers multiplied together, the "
                "cascade complete, the full magnification ready to apply."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(+ 10 20 30)", expected=60,
            concept_phrase="the sumseveral numbersbers",
            question_what="the sum of 10, 20, and 30",
            goal_text="add 10, 20, and 30",
            scenario=(
                "The farmer held three market baskets: one with 10 coins for cream, one with 20 coins "
                "for cheese, one with 30 coins for butter. Standing at the dairy door, she needed the "
                "total market fund in her hands."
            ),
            need=(
                "She needed to sum all three basket-amounts into one total without losing count, "
                "stacking each amount onto the running tally."
            ),
            mapping=(
                "The sseveral numbersumbers is the farmer's basket-tally: count the coins in the first "
                "basket, add the second basket's coins, add the third basket's coins. The total grows "
                "with each basket counted and merged."
            ),
            resolution=(
                "The REPL returned the complete market fund — all three baskets' coins tallied and "
                "stacked into the final sum."
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_02 = SubjectCurriculum(
    grade=2, subject_id="G2-02",
    subject_title="Comparison chains",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(< 1 2 3)", expected=True,
            concept_phrase="the less-than chain",
            question_what="whether 1 < 2 < 3",
            goal_text="test whether 1 is less than 2 and 2 is less than 3",
        ),
        SubjectExample(
            form="(< 3 2 1)", expected=False,
            concept_phrase="the less-than chain",
            question_what="whether 3 < 2 < 1",
            goal_text="test whether 3 is less than 2 and 2 is less than 1",
            scenario=(
                "The farmer had several piles of coins in a row on the tally table: the first pile "
                "held 3 coins, the second held 2, the third held 1. She wondered if each pile was "
                "smaller than the one before it."
            ),
            need=(
                "She needed to check whether the chain truly descended — each pile smaller than "
                "the last — without guessing or measuring by hand."
            ),
            mapping=(
                "The less-than chain is the farmer's descending gate: it checks if the first number "
                "is less than the second, and the second is less than the third. If any gate in the "
                "chain says 'no,' the chain is broken, and the answer is false."
            ),
            resolution=(
                "The REPL returned the gate's verdict — in this case, false, because 3 is not less "
                "than 2, so the chain is broken at the first gate."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(<= 1 1 2)", expected=True,
            concept_phrase="the less-than-or-equal chain",
            question_what="whether 1 ≤ 1 ≤ 2",
            goal_text="test whether 1 is less than or equal to 1 and 1 is less than or equal to 2",
            scenario=(
                "The farmer haseveral pileses on the table: one with 1 coin, one with 1 coin, one with "
                "2 coins. She wondered if the piles were arranged in non-decreasing order — each pile "
                "the same size or larger than the one before."
            ),
            need=(
                "She needed to check if the chain climbed or held steady — each pile equal or greater "
                "than the last — without guessing the order."
            ),
            mapping=(
                "The less-than-or-equal chain is the farmer's ascending-or-level gate: it checks if "
                "the first number is ≤ the second, and the second is ≤ the third. If any gate opens, "
                "the chain holds. If any gate closes, the chain is broken."
            ),
            resolution=(
                "The REPL returned the gate's verdict — every pairwise check held, "
                "so the chain stood unbroken."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(> 5 4 3 2 1)", expected=True,
            concept_phrase="the greater-than chain",
            question_what="whether the numbers are strictly decreasing",
            goal_text="test whether 5 > 4 > 3 > 2 > 1",
            scenario=(
                "The farmer had counted five bags of coins from richest to poorest: the first bag held "
                "5 coins, the next held 4, then 3, then 2, then 1. She wondered if the bags truly "
                "decreased in size all the way down."
            ),
            need=(
                "She needed to verify that each bag was strictly smaller than the one before, with no "
                "skipping or flat spots in the descending chain."
            ),
            mapping=(
                "The greater-than chain is the farmer's strict-descent gate: it checks if 5 > 4, "
                "if 4 > 3, if 3 > 2, if 2 > 1. Every gate in the chain must pass. If any gate says "
                "'no,' the chain is broken."
            ),
            resolution=(
                "The REPL returned the gate's verdict — in this case, true, because each number is "
                "strictly greater than the next, so the chain descends all the way."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(>= 3 3 2)", expected=True,
            concept_phrase="the greater-than-or-equal chain",
            question_what="whether 3 ≥ 3 ≥ 2",
            goal_text="test whether 3 is greater than or equal to 3 and 3 is greater than or equal to 2",
            scenario=(
                "The farmer several pilesiles: the first held 3 coins, the second also held 3 coins, "
                "the third held 2. She wondered if the chain held steady or descended — no pile growing "
                "larger."
            ),
            need=(
                "She needed to check if the piles stayed level or descended, with no pile jumping up "
                "to a larger size than the one before it."
            ),
            mapping=(
                "The greater-than-or-equal chain is the farmer's level-or-descent gate: it checks if "
                "the first number is ≥ the second, and the second is ≥ the third. Piles can stay the "
                "same size or shrink; they cannot grow."
            ),
            resolution=(
                "The REPL returned the gate's verdict — in this case, true, because 3 ≥ 3 and 3 ≥ 2 "
                "both pass, so the chain holds steady and then descends."
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_03 = SubjectCurriculum(
    grade=2, subject_id="G2-03",
    subject_title="not= and = with multiple args",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(not= 1 2)", expected=True,
            concept_phrase="the inequality check",
            question_what="whether 1 differs from 2",
            goal_text="test whether 1 and 2 are not equal",
        ),
        SubjectExample(
            form="(not= 1 1)", expected=False,
            concept_phrase="the inequality check",
            question_what="whether 1 differs from itself",
            goal_text="test whether 1 and 1 are not equal",
            scenario=(
                "The farmer held two coins in hand: one from the left pocket, one from the right. "
                "Both were the same size, the same weight, the same worth. She wondered if they "
                "differed from each other."
            ),
            need=(
                "She needed to check if the two coins were different — not equal — without comparing "
                "by guess or by hand."
            ),
            mapping=(
                "The inequality check is the farmer's two-coin gate: it asks 'are these not equal?' "
                "If the coins are the same value, the gate says 'no' — they are not different. If the "
                "coins differ, the gate says 'yes.'"
            ),
            resolution=(
                "The REPL returned the gate's answer — in this case, false, because 1 and 1 are equal, "
                "so the inequality check fails."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(= 1 1 1)", expected=True,
            concept_phrase="the equality check",
            question_what="whether all three are equal",
            goal_text="test whether 1, 1, and 1 are all equal",
            scenario=(
                "The farmer had three coins on the counting table, each from a different source. She "
                "wondered if they were all the same value — all equal to each other."
            ),
            need=(
                "She needed to verify that all three coins matched without guessing or measuring by hand "
                "— one simple check for complete equality."
            ),
            mapping=(
                "The equality check is the farmer's three-coin gate: it asks 'are all of these equal?' "
                "Each pair must match: coin one = coin two, and coin two = coin three. Only if all "
                "pairs match does the gate open."
            ),
            resolution=(
                "{drawn.a} returned: the REPL returned the gate's verdict — in this case, true, because all three coins "
                "are equal, so the equality chain holds."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(= 1 1 2)", expected=False,
            concept_phrase="the equality check",
            question_what="whether all three are equal",
            goal_text="test whether 1, 1, and 2 are all equal",
            scenario=(
                "The farmer had three coins on the table: the first was 1, the second was 1, the "
                "third was 2. She wondered if all three were the same value."
            ),
            need=(
                "She needed to check if all three coins matched or if one broke the chain, all in "
                "one form without guessing."
            ),
            mapping=(
                "The equality check is the farmer's matching-chain gate: it checks if coin one "
                "= coin two, and coin two = coin three. If any pair breaks the match, the gate "
                "closes and the answer is false."
            ),
            resolution=(
                "The REPL returned the gate's verdict — in this case, false, because 1 ≠ 2, so "
                "the chain is broken."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(not= 1 1 2)", expected=True,
            concept_phrase="the inequality check",
            question_what="whether at least one differs",
            goal_text="test whether at least one of 1, 1, and 2 is not equal to the others",
            scenario=(
                "The farmer had three coins: two from the market, one from home. The market coins "
                "were identical (both 1), but the home coin was different (2). She wondered if at "
                "least one coin differed from the others."
            ),
            need=(
                "She needed to check if the three coins were not all identical — if at least one "
                "stood apart — in one inequality check."
            ),
            mapping=(
                "The inequality check is the farmer's difference-seeker: it asks 'are these not all "
                "equal?' If all three are the same, the gate says 'no.' But if any coin differs, "
                "the gate says 'yes.'"
            ),
            resolution=(
                "The REPL returned the gate's answer — in this case, true, because 2 differs from "
                "the pair of 1s, so the inequality check passes."
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_04 = SubjectCurriculum(
    grade=2, subject_id="G2-04",
    subject_title="min and max",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(min 1 2 3)",
            expected=1,
            concept_phrase="the minseveral numbers numbers",
            question_what="the smallest of 1, 2, and 3",
            goal_text="find the minimum of 1, 2, and 3",
        ),
        SubjectExample(
            form="(max 1 2 3)", expected=3,
            concept_phrase="the mseveral numbersee numbers",
            question_what="the largest of 1, 2, and 3",
            goal_text="find the maximum of 1, 2, and 3",
            scenario=(
                "The farmer stood at the counting tableseveral piles piles of coins: 1, 2, and 3. "
                "She needed to know which pile was richest — which held the most coins — to choose "
                "the best payment for her debt."
            ),
            need=(
                "She needed to find the largest amount without comparing each pair by hand or "
                "guessing which pile was fullest."
            ),
            mapping=(
                "The maximum is the farmer's richest-pile picker: it examiseveral pilesee piles and "
                "returns the one with the most coins. One number falls away, then another, until "
                "the greatest remains."
            ),
            resolution=(
                "The REPL returned the richest pile's count — in this case, 3 coins, the maximum "
                "of the three amounts."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(min 7 3 9 1 5)", expected=1,
            concept_phrase="the minimua list of numbersmbers",
            question_what="the smallest of 7, 3, 9, 1, and 5",
            goal_text="find the minimum of these numbers",
            scenario=(
                "The farmer had five market reports from different traders: one reported 7 pails "
                "sold, one reported 3, another 9, another 1, and another 5. She wondered which "
                "trader had the slowest sale — the smallest count."
            ),
            need=(
                "She needed to find the weakest report without guessing or comparing each pair "
                "by hand."
            ),
            mapping=(
                "The minimum is the farmer's slowest-trader finder: it walks through all {drawn.e} counts and picks out the smallest. several numbers are set aside; the least remains."
            ),
            resolution=(
                "The REPL returned the slowest report — in this case, 1 pail, the minimum of the "
                "five amounts."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(max 7 3 9 1 5)", expected=9,
            concept_phrase="the ma list of numbersve numbers",
            question_what="the largest of 7, 3, 9, 1, and 5",
            goal_text="find the maximum of these numbers",
            scenario=(
                "The farmer had five reports of the day's sales: 7 pails, 3 pails, 9 pails, "
                "1 pail, and 5 pails. She needed to know which trader had the best day — the "
                "largest sale — to reward them."
            ),
            need=(
                "She needed to find the greatest count without guessing or comparing each pair "
                "by hand."
            ),
            mapping=(
                "The maximum is the farmer's best-day finder: it examines all {drawn.e} counts and returns the one with the most pails sold. One report rises above the others and stands alone."
            ),
            resolution=(
                "The REPL returned the best day's count — in this case, 9 pails, the maximum of "
                "the five amounts."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(min -3 -1 -5)", expected=-5,
            concept_phrase="theseveral numbershree numbers",
            question_what="the smallest of -3, -1, and -5",
            goal_text="find the minimum of -3, -1, and -5",
            scenario=(
                "The farmer had three debts: one owed 3 coins, one owed 1 coin, one owed 5 coins. "
                "She needed to know which debt was the largest — which number, when owed, hurt the "
                "most. In debt-counting, larger debts are more negative."
            ),
            need=(
                "She needed to find the deepest debt — the most negative number — without guessing "
                "which owed the most."
            ),
            mapping=(
                "The minimum is the farmer's deepest-debt finder: when numbers are negative, the "
                "minimum is the one that falls furthest down the number line. -5 is deeper than "
                "-3 or -1."
            ),
            resolution=(
                "The REPL returned the deepest debt — in this case, -5 coins, the minimum of the "
                "list of numbers."
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_05 = SubjectCurriculum(
    grade=2, subject_id="G2-05",
    subject_title="quot, rem, mod",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(quot 17 5)", expected=3,
            concept_phrase="the integer quotient",
            question_what="17 divided by 5, without remainder",
            goal_text="find the integer quotient of 17 divided by 5",
        ),
        SubjectExample(
            form="(rem 17 5)", expected=2,
            concept_phrase="the remainder",
            question_what="the remainder when 17 is divided by 5",
            goal_text="find the remainder when 17 is divided by 5",
            scenario=(
                "The farmer had 17 pails to distribute equally among 5 buyers at the market. She "
                "gave each buyer the same whole number of pails, but some pails were left over. "
                "She needed to know how many pails remained undistributed."
            ),
            need=(
                "She needed to find the leftover amount — not the full quotient, but just the "
                "extra pails that didn't fit evenly."
            ),
            mapping=(
                "The remainder is the farmer's leftover counter: divide 17 by 5, give each buyer "
                "3 pails (using 15 pails), and count what's left on the table. The remainder is "
                "what stays behind after equal division."
            ),
            resolution=(
                "The REPL returned the leftover count — in this case, 2 pails, the remainder when "
                "17 is divided by 5."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(mod 17 5)", expected=2,
            concept_phrase="the modulo operation",
            question_what="17 mod 5",
            goal_text="find 17 modulo 5",
            scenario=(
                "The farmer had 17 coins and wanted to arrange them in groups of 5 on the counting "
                "table. She made 3 complete groups but had coins left over that wouldn't fill "
                "another group. She needed to know how many orphaned coins remained."
            ),
            need=(
                "She needed to find what's left after grouping — the modulo — in one operation "
                "without calculating the quotient first."
            ),
            mapping=(
                "The modulo is the farmer's grouping-remainder: arrange the coins in complete "
                "groups of 5, and the modulo tells you which coins are left out. It's the orphaned "
                "amount that exists outside the groups."
            ),
            resolution=(
                "The REPL returned the orphaned count — in this case, 2 coins, the modulo result "
                "when 17 is divided by 5."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(quot 100 7)", expected=14,
            concept_phrase="the integer quotient",
            question_what="100 divided by 7, without remainder",
            goal_text="find the integer quotient of 100 divided by 7",
            scenario=(
                "The farmer had 100 coins to divide equally among 7 merchants at the market. She "
                "gave each merchant the same whole number of coins without any coins left over. "
                "She needed to know how many whole coins each merchant received."
            ),
            need=(
                "She needed to find the full quotient — the whole coins per merchant — without "
                "worrying about remainders or partial coins."
            ),
            mapping=(
                "The quotient is the farmer's fair-share counter: divide 100 by 7, and the quotient "
                "tells you how many whole coins each of the 7 merchants gets. Each gets an equal "
                "share; the remainder is set aside."
            ),
            resolution=(
                "The REPL returned the fair-share amount — in this case, 14 coins per merchant, "
                "the integer quotient when 100 is divided by 7."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(rem 100 7)", expected=2,
            concept_phrase="the remainder",
            question_what="the remainder when 100 is divided by 7",
            goal_text="find the remainder when 100 is divided by 7",
            scenario=(
                "The farmer had distributed 100 coins equally among 7 merchants (14 coins each). "
                "She wondered how many coins were left on the table that couldn't be distributed "
                "evenly."
            ),
            need=(
                "She needed to find the undistributed coins — the remainder — that fell short of "
                "giving each merchant one more coin."
            ),
            mapping=(
                "The remainder is the farmer's undistributed counter: after each of 7 merchants gets "
                "14 coins (totaling 98), count the coins still on the table. The remainder is what "
                "cannot be divided further."
            ),
            resolution=(
                "The REPL returned the undistributed count — in this case, 2 coins, the remainder "
                "when 100 is divided by 7."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(mod -7 3)", expected=2,
            concept_phrase="the modulo operation",
            question_what="negative seven mod 3",
            goal_text="find negative 7 modulo 3",
            scenario=(
                "The farmer had a debt of coins to pay back in groups. She could arrange "
                "complete groups, but some coins of debt remained. The modulo told her what "
                "was left over — how much debt remained after grouping repayments."
            ),
            need=(
                "She needed to find the leftover debt — the modulo of a negative amount — to know "
                "how many coins still had to be paid."
            ),
            mapping=(
                "The modulo is the farmer's debt-remainder: even with negative numbers, the modulo "
                "groups by 3 and returns what's left unpaid. The leftover amount is always in the "
                "range of the divisor."
            ),
            resolution=(
                "The REPL returned the debt remainder — in this case, 2 coins, the modulo result "
                "when -7 is divided by 3."
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_06 = SubjectCurriculum(
    grade=2, subject_id="G2-06",
    subject_title="inc and dec",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(inc 5)", expected=6,
            concept_phrase="the increment operation",
            question_what="5 plus 1",
            goal_text="increment 5 by 1",
        ),
        SubjectExample(
            form="(dec 5)", expected=4,
            concept_phrase="the decrement operation",
            question_what="5 minus 1",
            goal_text="decrement 5 by 1",
            scenario=(
                "The farmer had 5 pails of milk on the shelf. One buyer took a pail and walked away. "
                "The farmer needed to know the new count without counting all the pails from scratch."
            ),
            need=(
                "She needed to subtract one from 5 in a single step — a decrement — to know the "
                "remaining count."
            ),
            mapping=(
                "The decrement is the farmer's quick-subtract: take the current count and reduce it "
                "by exactly 1. It's a shorthand for 5 - 1, a single operation that steps down the "
                "number line by one place."
            ),
            resolution=(
                "The REPL returned the new count — in this case, 4 pails, after the decrement reduced "
                "the total."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(inc 0)", expected=1,
            concept_phrase="the increment operation",
            question_what="0 plus 1",
            goal_text="increment 0",
            scenario=(
                "The farmer's pail was empty at the start of the day. The first buyer brought one "
                "pail of milk. She needed to know the new count without guessing."
            ),
            need=(
                "She needed to add one to 0 in a single step — an increment — to know the count "
                "started from nothing and grew by one."
            ),
            mapping=(
                "The increment is the farmer's quick-add: take the current count and increase it by "
                "exactly 1. It's a shorthand for 0 + 1, a single operation that steps up the number "
                "line by one place."
            ),
            resolution=(
                "The REPL returned the new count — in this case, 1 pail, after the increment added "
                "one to zero."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(dec 0)", expected=-1,
            concept_phrase="the decrement operation",
            question_what="0 minus 1",
            goal_text="decrement 0",
            scenario=(
                "The farmer had no pails left (0 pails). A buyer requested a pail anyway, so the "
                "farmer agreed to owe one. She needed to know the new count in the debt-reckoning."
            ),
            need=(
                "She needed to subtract one from 0 in a single step — a decrement — to record the "
                "debt as a negative number."
            ),
            mapping=(
                "The decrement is the farmer's debt-stepping: take the current count (even if zero) "
                "and reduce it by 1, stepping down below zero into negative territory. 0 - 1 = -1."
            ),
            resolution=(
                "The REPL returned the new count — in this case, -1 pail, showing the farmer is one "
                "pail in debt."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(inc -1)", expected=0,
            concept_phrase="the increment operation",
            question_what="negative 1 plus 1",
            goal_text="increment negative 1",
            scenario=(
                "The farmer owed 1 pail from yesterday (debt of -1). Today, she made one pail and "
                "set it aside to repay the debt. She needed to know the new count after the payment."
            ),
            need=(
                "She needed to add one to -1 in a single step — an increment — to show the debt "
                "reduced back to zero."
            ),
            mapping=(
                "The increment is the farmer's debt-payment: take the debt count (-1) and increase "
                "it by 1, stepping back toward zero. -1 + 1 = 0, so the debt is erased."
            ),
            resolution=(
                "The REPL returned the new count — in this case, 0, showing the farmer paid off the "
                "debt and the count is square again."
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_07 = SubjectCurriculum(
    grade=2, subject_id="G2-07",
    subject_title="Absolute value",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(abs 5)", expected=5,
            concept_phrase="the absolute value",
            question_what="the absolute value of 5",
            goal_text="find the absolute value of 5",
            scenario=(
                "The farmer stood at the counting table with a pile of 5 coins. She "
                "wondered about its magnitude — the pure size of the amount, treated as "
                "a positive distance from zero."
            ),
            need=(
                "She needed to know the absolute value of 5 — its magnitude as a "
                "distance from zero, always positive."
            ),
            mapping=(
                "The absolute value is the farmer's magnitude-seeker: it measures the "
                "distance from zero without regard to sign. For positive numbers like 5, "
                "the distance is simply the number itself."
            ),
            resolution=(
                "The REPL returned the pure magnitude — 5 units away from zero."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(abs -5)", expected=5,
            concept_phrase="the absolute value",
            question_what="the absolute value of negative 5",
            goal_text="find the absolute value of negative 5",
            scenario=(
                "The farmer was counting a debt of 5 coins as -5 on her slate. But when she "
                "thought about the size of the debt — not whether it was owed or paid — she "
                "needed the absolute amount, without the minus sign."
            ),
            need=(
                "She needed to strip away the negative sign and get just the magnitude — how large "
                "the debt truly was in pure count."
            ),
            mapping=(
                "The absolute value is the farmer's magnitude-seeker: it erases the sign and returns "
                "only the distance from zero. Whether the number is -5 or +5, the absolute value "
                "tells you they are both 5 units away from zero."
            ),
            resolution=(
                "The REPL returned the pure magnitude — in this case, 5, the absolute value of both "
                "+5 and -5."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(abs 0)", expected=0,
            concept_phrase="the absolute value",
            question_what="the absolute value of 0",
            goal_text="find the absolute value of 0",
            scenario=(
                "The farmer had neither coins nor debt — the count was exactly 0. She wondered what "
                "the absolute value of zero was, in case it mattered for the final reckoning."
            ),
            need=(
                "She needed to know that the absolute value of 0 is still 0 — there is no distance "
                "from zero when you already stand at zero."
            ),
            mapping=(
                "The absolute value is the farmer's distance-measurer: zero is neither positive nor "
                "negative. It stands at the center. The absolute value of 0 is 0 itself — no distance "
                "to measure."
            ),
            resolution=(
                "The REPL returned the distance from zero — in this case, 0, because zero itself is "
                "the absolute value of zero."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(abs (- 3 8))", expected=5,
            concept_phrase="the absolute value",
            question_what="the absolute value of the difference between 3 and 8",
            goal_text="find the absolute value of 3 minus 8",
            scenario=(
                "The farmer had 3 pails at the start of the week but needed 8 pails to fulfill an "
                "order. The difference was -5 (she was 5 short). But for the shipping label, she "
                "needed the absolute size of the shortage, without the minus sign."
            ),
            need=(
                "She needed to calculate 3 minus 8 (getting -5), then take the absolute value to "
                "show the magnitude of the shortage clearly."
            ),
            mapping=(
                "The absolute value is the farmer's difference-simplifier: compute the difference "
                "(3 - 8 = -5), then ask: how far is this from zero? The answer is 5, the pure "
                "amount of shortage."
            ),
            resolution=(
                "The REPL returned the magnitude of difference — in this case, 5 pails, showing the "
                "farmer was exactly 5 short of the order."
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_08 = SubjectCurriculum(
    grade=2, subject_id="G2-08",
    subject_title="Arithmetic on ratios",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(+ 1/2 1/4)", expected="3/4",
            concept_phrase="the sum of two ratios",
            question_what="the sum of one-half and one-quarter",
            goal_text="add one-half and one-quarter",
            scenario=(
                "The farmer held two measures of cream at the counting table: one held "
                "one-half the pail, the other held one-quarter the pail. She needed the "
                "combined fraction to know the total cream ready for market."
            ),
            need=(
                "She needed to add the two fractions together into one larger fraction, "
                "combining both shares of cream into one tally."
            ),
            mapping=(
                "The sum of two ratios is the farmer's fractional stacking: find a common "
                "denominator, add the numerators, and the result is a new fraction larger than "
                "either part."
            ),
            resolution=(
                '1/2 returned: the REPL returned the combined fraction — three-quarters, the sum of one-half and one-quarter (with `4` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 2/3 3/4)", expected="1/2",
            concept_phrase="the product of two ratios",
            question_what="the product of two-thirds and three-quarters",
            goal_text="multiply two-thirds by three-quarters",
            scenario=(
                "The farmer had two shares to combine: the first share was two-thirds of the cream, "
                "the second share was three-quarters of what remained. She needed to know what "
                "fraction of the original cream the combined share represented."
            ),
            need=(
                "She needed to multiply the two fractions together to find the final fractional "
                "amount, accounting for both shares at once."
            ),
            mapping=(
                "The product of two ratios is the farmer's fractional-stacking: multiply numerator "
                "by numerator, denominator by denominator. The result is a new fraction that combines "
                "both shares' scales into one."
            ),
            resolution=(
                '2/3 returned: the REPL returned the combined fraction — in this case, one-half, showing the product of two-thirds and three-quarters.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(- 1 1/3)", expected="2/3",
            concept_phrase="the difference of a whole and a ratio",
            question_what="1 minus one-third",
            goal_text="subtract one-third from 1",
            scenario=(
                "The farmer had one whole pail of milk. She used one-third of it for cheese-making. "
                "She needed to know what fraction of the pail remained for market."
            ),
            need=(
                "She needed to subtract the fraction from the whole pail in one form, leaving a "
                "fractional remainder."
            ),
            mapping=(
                "The difference of a whole and a ratio is the farmer's fraction-subtractor: take 1 "
                "(the whole pail), subtract 1/3 (the used portion), and the result is the leftover "
                "fraction."
            ),
            resolution=(
                "The REPL returned the leftover fraction — in this case, two-thirds of the pail, "
                "the remainder after one-third was used."
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_09 = SubjectCurriculum(
    grade=2, subject_id="G2-09",
    subject_title="Floats vs ints (the / operator)",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(/ 10 2)", expected=5,
            concept_phrase="the division operation",
            question_what="the result of using / on 10 and 2",
            goal_text="divide 10 by 2",
            scenario=(
                "The farmer had 10 coins and wanted to divide them equally among 2 buyers "
                "at the market. She needed to know how many coins each buyer would receive "
                "if the division was exact."
            ),
            need=(
                "She needed the result of dividing 10 by 2 without a remainder, all in one "
                "operation."
            ),
            mapping=(
                "The division operation is the farmer's fair-share counter: divide 10 coins by "
                "2 buyers, and the result tells each buyer their equal portion. When the division "
                "is exact, the REPL returns an integer."
            ),
            resolution=(
                "The REPL returned the fair share — 5 coins per buyer, the exact result of "
                "dividing 10 by 2."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(/ 10 3)", expected="10/3",
            concept_phrase="the division operation",
            question_what="the exact rational result of using / on 10 and 3",
            goal_text="divide 10 by 3",
            scenario=(
                "The farmer had 10 coins and wanted to divide them equally among 3 buyers. "
                "She realized the division would not be exact — some remainder would be left. "
                "She needed the precise fractional result, not a rounded guess."
            ),
            need=(
                "She needed the exact rational result of dividing 10 by 3, preserving the "
                "fractional remainder as a true ratio."
            ),
            mapping=(
                "The division operation is the farmer's precise-share measurer: when the division "
                "cannot be exact, the / operator returns a rational — a fraction — not a decimal "
                "approximation."
            ),
            resolution=(
                "The REPL returned the exact rational result — the precise quotient preserved "
                "as a ratio, not rounded or approximated."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(/ 1.0 2)", expected=0.5,
            concept_phrase="the division operation",
            question_what="the result of 1.0 divided by 2",
            goal_text="divide 1.0 by 2",
            scenario=(
                "The farmer had 1.0 pails of milk (a float) and wanted to divide them equally "
                "among 2 buyers. She needed the decimal result of the division."
            ),
            need=(
                "She needed the result of dividing a float by an integer, returning a decimal "
                "result rather than a rational."
            ),
            mapping=(
                "The division operation is the farmer's float-divider: when the dividend is a "
                "float (1.0), the result is also a float (0.5), not a rational. The operation "
                "returns a decimal approximation."
            ),
            resolution=(
                "The REPL returned the decimal result — 0.5, the result of dividing 1.0 by 2."
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_10 = SubjectCurriculum(
    grade=2, subject_id="G2-10",
    subject_title="Powers via repeated multiplication",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(* 2 2 2)", expected=8,
            concept_phrase="repeated multiplication",
            question_what="2 to the third power",
            goal_text="multiply 2 by itself three times",
            scenario=(
                "The farmer had a cube-shaped stack of milk pails: two pails wide, two pails deep, "
                "two pails tall. She needed to know the total number of pails in the entire stack."
            ),
            need=(
                "She needed to multiply 2 times 2 times 2 to find the volume of the cubic stack "
                "without counting each pail by hand."
            ),
            mapping=(
                "Repeated multiplication is the farmer's stacking power: multiply 2 by itself three "
                "times to represent a 2×2×2 cube. Each dimension is counted the same way, stacking "
                "the multiplications."
            ),
            resolution=(
                "The REPL returned the total stack — 8 pails, the result of 2 to the third power."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 5 5)", expected=25,
            concept_phrase="repeated multiplication",
            question_what="5 to the second power",
            goal_text="multiply 5 by itself",
            scenario=(
                "The farmer had a square garden plot: 5 paces wide and 5 paces long. She needed "
                "the total area in square paces to know how much seed to sow."
            ),
            need=(
                "She needed to multiply 5 by itself to find the area of the square plot without "
                "counting every square pace."
            ),
            mapping=(
                "Repeated multiplication is the farmer's area-counter: multiply 5 by itself (two "
                "times) to represent a 5×5 square. Width times height gives the total area."
            ),
            resolution=(
                "The REPL returned the total area — 25 square paces, the result of 5 to the second "
                "power."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 3 3 3 3)", expected=81,
            concept_phrase="repeated multiplication",
            question_what="3 to the fourth power",
            goal_text="multiply 3 by itself four times",
            scenario=(
                "The farmer had a four-dimensional arrangement of coins (a thought experiment): "
                "3 coins in each dimension. She wondered what the total count would be if she "
                "could stack all dimensions at once."
            ),
            need=(
                "She needed to multiply 3 by itself four times to find the fourth-power result "
                "without a calculator."
            ),
            mapping=(
                "Repeated multiplication is the farmer's power-multiplier: multiply 3 by itself "
                "four times. Each repetition adds another dimension, compounding upward with each "
                "multiplication."
            ),
            resolution=(
                "The REPL returned the compound product — 81, the result of 3 to the fourth power."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 10 10)", expected=100,
            concept_phrase="repeated multiplication",
            question_what="10 to the second power",
            goal_text="multiply 10 by itself",
            scenario=(
                "The farmer had a large square market space with stalls arranged in a grid. "
                "She needed the total number of stalls to allocate fairly among traders."
            ),
            need=(
                "She needed to multiply the width by the length to find the total stalls without counting "
                "one by one."
            ),
            mapping=(
                "Repeated multiplication is the farmer's grid-counter: multiply a dimension by itself "
                "to represent a square grid. The result is the total available "
                "space."
            ),
            resolution=(
                "{drawn.a} returned: the REPL returned the total count — the product of multiplying the market space's dimensions."
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_11 = SubjectCurriculum(
    grade=2, subject_id="G2-11",
    subject_title="String concatenation with str",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form='(str "ab" "cd")',
            expected="abcd",
            concept_phrase='the string concatenation',
            question_what='the result of using str to splice "ab" and "cd"',
            goal_text='use str to splice the two-letter strings "ab" and "cd" into a single thread',
            scenario=(
                'The milkmaid had two short lengths of cheesecloth: one labeled "ab" '
                'and one labeled "cd." She needed to stitch them together end-to-end '
                "into one unbroken cloth for straining the morning milk."
            ),
            need=(
                "She needed a braiding operation — join both lengths in order, left "
                "to right, with no gap or overlap between the two pieces."
            ),
            mapping=(
                "`str` is the braiding peg: it takes the cloth-lengths in order and "
                "weaves them into one continuous thread. The first length leads; "
                "the second follows without pause."
            ),
            resolution=(
                "The REPL returned the joined cloth — four characters woven together "
                "in the order given, the seam invisible."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(str 42)', expected="42",
            concept_phrase='the string coercion of an integer',
            question_what='the result of using str on the integer 42',
            goal_text='use str to coerce the integer 42 to its string representation',
            scenario=(
                "The milkmaid held a coin tally of 42 in her hand. She needed to weave "
                "it into a written label on a cheesecloth bundle for market."
            ),
            need=(
                "She needed to transform the integer 42 into a string representation so "
                "it could be braided with other cloth-marks."
            ),
            mapping=(
                "`str` is the braiding weaver: it transforms a number (42) into its text "
                "form, a string of characters that can be threaded onto cloth alongside "
                "other strands."
            ),
            resolution=(
                "The REPL returned the woven label — the string '42', the integer "
                "coerced into a cloth-marking."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(str "p" "q" "r")', expected="pqr",
            concept_phrase='the three-arg string concatenation',
            question_what='the result of using str to join "p", "q", and "r"',
            goal_text='use str to join three single-character strings in order',
            scenario=(
                "The milkmaid had three single-character cloth-marks on her shelf. "
                "She needed to braid all three together into one continuous strand."
            ),
            need=(
                "She needed to join three cloth-strands end-to-end into one unbroken "
                "thread for a market label."
            ),
            mapping=(
                "`str` is the three-peg braider: it takes three cloth-marks in order and "
                "weaves them into a single continuous thread — "
                "no gaps between."
            ),
            resolution=(
                "The REPL returned the braided thread — three characters "
                "woven end-to-end in a single strand."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(str 1 "+" 2 "=" 3)', expected="1+2=3",
            concept_phrase='the mixed string concatenation',
            question_what='the result of using str to join integers and operators',
            goal_text='use str to join a list of elements in sequence',
            scenario=(
                "The milkmaid held a teaching cloth for children with five separate pieces: "
                "numbers and operator symbols meant to form a lesson. "
                "She needed to weave them all together."
            ),
            need=(
                "She needed to ba list of elementsments — numbers and symbols — in order into "
                "one cloth-message for the teaching wall."
            ),
            mapping=(
                "`str` is the mixed-weaver: it takes numbers and string-marks in the order "
                "given and braids them all together. Integers are coerced to strings first, "
                "then all are threaded without gaps."
            ),
            resolution=(
                "The REPL returned the woven messa list of elementse elements "
                "threaded together in order to form the final strand —  2 ."
            ),
            tags=("story",),
        ),
    ],
    subplots=_BEADSTRING_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_12 = SubjectCurriculum(
    grade=2, subject_id="G2-12",
    subject_title="print and println — return values",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form='(println "hello")', expected=None,
            concept_phrase='the print-line call',
            question_what='the return value of using println on the string "hello"',
            goal_text='print the string "hello" with a newline',
            scenario=(
                "The scribe had just marked 'hello' on the dairy wall with chalk. She "
                "pressed the chalk firmly and wanted to complete the mark with a newline. "
                "She wondered what the mark-making operation would return to her hand."
            ),
            need=(
                "She needed to write 'hello' to the dairy wall with a newline, then find "
                "what value the operation returned."
            ),
            mapping=(
                "`println` is the scribe's line-marking chalk: it writes the text to the "
                "wall, adds a newline to move to the next line, but returns nothing — no "
                "value to carry back. The mark is made; the hand receives nil."
            ),
            resolution=(
                "The REPL returned nil (nothing) — the print-line operation wrote to the "
                "wall but carried no value back."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(print "x")', expected=None,
            concept_phrase='the print call',
            question_what='the return value of using print on the string "x"',
            goal_text='print the string "x" without a newline',
            scenario=(
                "The scribe held a single chalk mark 'x' to write on the dairy wall. She "
                "pressed it without moving to a new line, ready to add more marks to the "
                "same line. She wondered what the mark-making would return."
            ),
            need=(
                "She needed to write 'x' to the wall without a newline, and find what "
                "value the operation carried back."
            ),
            mapping=(
                "`print` is the scribe's continuous-marking chalk: it writes the text to "
                "the wall without a newline (so the next mark stays on the same line), "
                "but returns nothing — no value carried back. The hand receives nil."
            ),
            resolution=(
                "The REPL returned nil (nothing) — the print operation wrote to the wall "
                "but carried no value back, just as println."
            ),
            tags=("story",),
        ),
    ],
    subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_13 = SubjectCurriculum(
    grade=2, subject_id="G2-13",
    subject_title="and / or — short circuit, return values",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(and true true)",
            expected=True,
            concept_phrase="the logical and",
            question_what="the result of passing true and true through the and-chain of gates",
            goal_text="test whether two trues both pass through an and-chain of gates",
            scenario=(
                "The farmer had two gates on the farmyard path: the first opened when "
                "the condition was true, the second also opened when its condition was "
                "true. She wondered if both gates would open together."
            ),
            need=(
                "She needed to check if the first condition was true AND the second condition "
                "was also true, without guessing or testing separately."
            ),
            mapping=(
                "The logical and is the farmer's gate-chain: both gates must pass (both true) "
                "for the journey to continue. If the first gate closes (false), the whole chain "
                "fails. If the first passes, check the second."
            ),
            resolution=(
                "The REPL returned the verdict — both gates opened, the and-chain was complete."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(and true false)", expected=False,
            concept_phrase="the logical and",
            question_what="the result of using and on true and false",
            goal_text="test true and false with the and operator",
            scenario=(
                "The farmer had two gates: the first opened (true), but the second was blocked "
                "(false). She wondered if the and-chain would succeed."
            ),
            need=(
                "She needed to test if both gates opened together using the and operator."
            ),
            mapping=(
                "The logical and is the farmer's gate-chain: the first gate opens (true), but "
                "the second gate is blocked (false). The chain breaks at the second gate — the "
                "and fails."
            ),
            resolution=(
                "The REPL returned the verdict — the second gate blocked the journey, so the and-chain "
                "failed."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(or false true)", expected=True,
            concept_phrase="the logical or",
            question_what="the result of using or on false and true",
            goal_text="test false or true with the or operator",
            scenario=(
                "The farmer had two gates: the first was blocked (false), but the second opened "
                "(true). She wondered if the or-chain would succeed."
            ),
            need=(
                "She needed to test if at least one gate opened using the or operator."
            ),
            mapping=(
                "The logical or is the farmer's choice-gate: if the first gate opens, the journey "
                "succeeds. If the first is blocked, check the second. If the second opens, the "
                "journey continues. The or succeeds if ANY gate opens."
            ),
            resolution=(
                "The REPL returned the verdict — the second gate opened, so the or-chain succeeded."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(or false false)", expected=False,
            concept_phrase="the logical or",
            question_what="the result of using or on false and false",
            goal_text="test false or false with the or operator",
            scenario=(
                "The farmer had two gates: both were blocked (both false). She wondered if the "
                "or-chain would have any way through."
            ),
            need=(
                "She needed to test if at least one gate opened using the or operator."
            ),
            mapping=(
                "The logical or is the farmer's choice-gate: the first gate is blocked (false), "
                "so check the second. The second is also blocked (false). No gates opened — the "
                "or fails."
            ),
            resolution=(
                "The REPL returned the verdict — both gates were blocked, so the or-chain failed."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(and 1 2 3)", expected=3,
            concept_phrase="the logical and",
            question_what="the result of using and on 1, 2, and 3",
            goal_text="apply and to 1, 2, and 3",
            scenario=(
                "The farmer had several values: 1, 2, and 3. All were truthy (non-false, non-nil). "
                "She wondered what the and operator would return when passed all three."
            ),
            need=(
                "She needed to apply the and operator to three truthy values and find what it "
                "returned."
            ),
            mapping=(
                "The logical and is the farmer's truthy-checker: it tests each value in order. "
                "If any is falsey, it stops and returns that value. If all are truthy, it returns "
                "the last one."
            ),
            resolution=(
                "The REPL returned the result — the last value, because all three were truthy."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(or nil false 5)", expected=5,
            concept_phrase="the logical or",
            question_what="the result of using or on nil, false, and 5",
            goal_text="apply or to nil, false, and 5",
            scenario=(
                "The farmer haseveral valueses: nil (falsey), false (falsey), and 5 (truthy). "
                "She wondered what the or operator would return when passed all three."
            ),
            need=(
                "She needed to apply the or operatorseveral valueslues and find what it returned."
            ),
            mapping=(
                "The logical or is the farmer's truthy-finder: it tests each value in order. "
                "If any is truthy, it stops and returns that value. nil and false are both falsey, "
                "so skip them and return 5."
            ),
            resolution=(
                "The REPL returned the result — the first truthy value in the chain, the or succeeded."
            ),
            tags=("story",),
        ),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_14 = SubjectCurriculum(
    grade=2, subject_id="G2-14",
    subject_title="not — turning truthy to false",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(not true)", expected=False,
            concept_phrase="the logical not",
            question_what="the result of using not on true",
            goal_text="negate the value true",
            scenario=(
                "The farmer stood at the gate with the condition true (the gate was open). "
                "She wondered what would happen if she inverted the condition — turned it "
                "to the opposite."
            ),
            need=(
                "She needed to negate the value true, flipping it to its opposite."
            ),
            mapping=(
                "The logical not is the farmer's gate-inverter: it takes a gate's state (true) "
                "and flips it to the opposite (false). True becomes false, as if the gate swung "
                "shut."
            ),
            resolution=(
                "The REPL returned the verdict — the opposite of true, the gate inverted."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(not false)", expected=True,
            concept_phrase="the logical not",
            question_what="the result of using not on false",
            goal_text="negate the value false",
            scenario=(
                "The farmer stood at the gate with the condition false (the gate was blocked). "
                "She wondered what would happen if she inverted the condition to the opposite."
            ),
            need=(
                "She needed to negate the value false, flipping it to its opposite."
            ),
            mapping=(
                "The logical not is the farmer's gate-inverter: it takes a gate's state (false) "
                "and flips it to the opposite (true). False becomes true, as if the blocked gate "
                "suddenly opened."
            ),
            resolution=(
                "The REPL returned the verdict — the opposite of false, the gate inverted."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(not nil)", expected=True,
            concept_phrase="the logical not",
            question_what="the result of using not on nil",
            goal_text="negate the value nil",
            scenario=(
                "The farmer held nil (nothing, a falsey value) in her hand. She wondered what "
                "the not operator would return if she inverted it."
            ),
            need=(
                "She needed to negate nil, flipping the falsey value to its truthy opposite."
            ),
            mapping=(
                "The logical not is the farmer's gate-inverter: nil is falsey, so its opposite "
                "is true. Falsey values flip to true; truthy values flip to false."
            ),
            resolution=(
                "The REPL returned the verdict — nil inverted to its opposite."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(not 0)", expected=False,
            concept_phrase="the logical not",
            question_what="the result of using not on 0",
            goal_text="negate the value 0",
            scenario=(
                "The farmer held 0 (a number, truthy in milkmaid-world) in her hand. She wondered "
                "what the not operator would return if she inverted it."
            ),
            need=(
                "She needed to negate 0, flipping the truthy value to its falsey opposite."
            ),
            mapping=(
                "The logical not is the farmer's gate-inverter: 0 is truthy (unlike in some "
                "languages), so its opposite is false. Only false and nil are falsey."
            ),
            resolution=(
                "The REPL returned the verdict — 0 inverted to its opposite."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(not "")', expected=False,
            concept_phrase="the logical not",
            question_what='the result of using not on the empty string',
            goal_text="negate the empty string",
            scenario=(
                'The farmer held the empty string "" (no characters, truthy in milkmaid-world) '
                "in her hand. She wondered what the not operator would return if she inverted it."
            ),
            need=(
                "She needed to negate the empty string, flipping the truthy value to its falsey "
                "opposite."
            ),
            mapping=(
                'The logical not is the farmer\'s gate-inverter: "" is truthy (unlike in some '
                "languages), so its opposite is false. Only false and nil are falsey."
            ),
            resolution=(
                "The REPL returned the verdict — the empty string inverted to its opposite."
            ),
            tags=("story",),
        ),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_15 = SubjectCurriculum(
    grade=2, subject_id="G2-15",
    subject_title="Falsey values: only false and nil",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(if 0 1 0)", expected=1,
            concept_phrase="the if conditional with zero as condition",
            question_what="the result of if with condition 0, then-branch 1, else-branch 0",
            goal_text="use if to return 1 when the condition is 0 (then-branch) and 0 otherwise (else-branch)",
            scenario=(
                "The farmer had a gate controlled by the condition 0. In her experience, 0 was "
                "a valid count — a truthy value. She wondered which path the if would choose."
            ),
            need=(
                "She needed to know if 0 would open the then-branch (1) or the else-branch (0)."
            ),
            mapping=(
                "The if conditional is the farmer's choice-gate: if the condition is truthy "
                "(and 0 is truthy in milkmaid-world), take the then-branch. Only false and nil "
                "are falsey."
            ),
            resolution=(
                "The REPL returned the result — the then-branch, because 0 is truthy, the gate opened."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(if "" 1 0)', expected=1,
            concept_phrase="the if conditional with empty string as condition",
            question_what="the result of if with condition the empty string, then-branch 1, else-branch 0",
            goal_text='use if to return 1 when the condition is the empty string (then-branch) and 0 otherwise (else-branch)',
            scenario=(
                'The farmer had a gate controlled by the condition "" (empty string). In her '
                "experience, an empty string was a valid value — a truthy value. She wondered "
                "which path the if would choose."
            ),
            need=(
                "She needed to know if the empty string would open the then-branch (1) or the "
                "else-branch (0)."
            ),
            mapping=(
                "The if conditional is the farmer's choice-gate: if the condition is truthy "
                '(and "" is truthy in milkmaid-world), take the then-branch. Only false and nil '
                "are falsey."
            ),
            resolution=(
                "The REPL returned the result — the then-branch, because the empty string is truthy, "
                "the gate opened."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(if nil 1 0)", expected=0,
            concept_phrase="the if conditional with nil as condition",
            question_what="the result of if with condition nil, then-branch 1, else-branch 0",
            goal_text="use if to return 1 when the condition is nil (then-branch) and 0 otherwise (else-branch)",
            scenario=(
                "The farmer had a gate controlled by the condition nil. nil was falsey — a "
                "value that meant 'nothing.' She wondered which path the if would choose."
            ),
            need=(
                "She needed to know if nil would open the then-branch (1) or the else-branch (0)."
            ),
            mapping=(
                "The if conditional is the farmer's choice-gate: if the condition is falsey "
                "(and nil is falsey), take the else-branch. Only false and nil are falsey."
            ),
            resolution=(
                "The REPL returned 0 — the else-branch, because nil is falsey, the gate closed."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(if false 1 0)", expected=0,
            concept_phrase="the if conditional with false as condition",
            question_what="the result of if with condition false, then-branch 1, else-branch 0",
            goal_text="use if to return 1 when the condition is false (then-branch) and 0 otherwise (else-branch)",
            scenario=(
                "The farmer had a gate controlled by the condition false. false was the ultimate "
                "falsey value. She wondered which path the if would choose."
            ),
            need=(
                "She needed to know if false would open the then-branch (1) or the else-branch (0)."
            ),
            mapping=(
                "The if conditional is the farmer's choice-gate: if the condition is falsey "
                "(and false is falsey), take the else-branch. Only false and nil are falsey."
            ),
            resolution=(
                "The REPL returned 0 — the else-branch, because false is falsey, the gate closed."
            ),
            tags=("story",),
        ),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_16 = SubjectCurriculum(
    grade=2, subject_id="G2-16",
    subject_title="Truthy 0 and empty string",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(boolean 0)", expected=True,
            concept_phrase="the boolean conversion",
            question_what="the result of using boolean on 0",
            goal_text="convert 0 to a boolean",
            scenario=(
                "The farmer held 0 (a count, a number) in her hand. She wondered if the boolean "
                "conversion would tell her it was truthy or falsey."
            ),
            need=(
                "She needed to convert 0 to its boolean equivalent, finding if it was truthy "
                "or falsey."
            ),
            mapping=(
                "The boolean conversion is the farmer's truthy-tester: it converts any value to "
                "true or false. In milkmaid-world, 0 is truthy — only false and nil are falsey."
            ),
            resolution=(
                "The REPL returned the verdict — 0 is truthy, so the conversion shows true."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(boolean "")', expected=True,
            concept_phrase="the boolean conversion",
            question_what="the result of using boolean on the empty string",
            goal_text="convert the empty string to a boolean",
            scenario=(
                "The farmer held the empty string (no characters) in her hand. She wondered if "
                "the boolean conversion would tell her it was truthy or falsey."
            ),
            need=(
                "She needed to convert the empty string to its boolean equivalent, finding if it "
                "was truthy or falsey."
            ),
            mapping=(
                "The boolean conversion is the farmer's truthy-tester: it converts any value to "
                "true or false. In milkmaid-world, the empty string is truthy — only false and "
                "nil are falsey."
            ),
            resolution=(
                "The REPL returned the verdict — the empty string is truthy, so the conversion shows true."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(boolean nil)", expected=False,
            concept_phrase="the boolean conversion",
            question_what="the result of using boolean on nil",
            goal_text="convert nil to a boolean",
            scenario=(
                "The farmer held nil (nothing, no value) in her hand. She wondered if the boolean "
                "conversion would tell her it was truthy or falsey."
            ),
            need=(
                "She needed to convert nil to its boolean equivalent, finding if it was truthy "
                "or falsey."
            ),
            mapping=(
                "The boolean conversion is the farmer's truthy-tester: it converts any value to "
                "true or false. nil is falsey — only false and nil are falsey."
            ),
            resolution=(
                "The REPL returned the verdict — nil is falsey, so the conversion shows false."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(boolean false)", expected=False,
            concept_phrase="the boolean conversion",
            question_what="the result of using boolean on false",
            goal_text="convert false to a boolean",
            scenario=(
                "The farmer held false in her hand. false was the ultimate falsey value. She "
                "wondered what the boolean conversion would return."
            ),
            need=(
                "She needed to convert false to its boolean equivalent, knowing it was falsey."
            ),
            mapping=(
                "The boolean conversion is the farmer's truthy-tester: it converts any value to "
                "true or false. false is falsey — only false and nil are falsey."
            ),
            resolution=(
                "The REPL returned the verdict — false is falsey, so the conversion shows false."
            ),
            tags=("story",),
        ),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_17 = SubjectCurriculum(
    grade=2, subject_id="G2-17",
    subject_title="Keyword as function for map lookup",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(:hare {:hare 1 :tortoise 2})", expected=1,
            concept_phrase="the keyword lookup",
            question_what="the result of using the keyword :hare as a function on the map {:hare 1 :tortoise 2}",
            goal_text="use the keyword :hare to look up a value in the map with keys :hare and :tortoise",
            scenario=(
                "The farmer held a market-basket with two compartments: one labeled :hare "
                "held 1 coin, the other labeled :tortoise held 2 coins. She wanted to reach into "
                "the :hare compartment and find what was inside."
            ),
            need=(
                "She needed to look up the value in the :hare compartment of her basket without "
                "opening all compartments."
            ),
            mapping=(
                "The keyword lookup is the farmer's basket-compartment finder: the keyword :hare "
                "acts like a hand reaching into the map to find the labeled compartment and pull out "
                "what's inside."
            ),
            resolution=(
                "The REPL returned the result — the value inside the :hare compartment of the basket."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(:tortoise {:hare 1 :tortoise 2})", expected=2,
            concept_phrase="the keyword lookup",
            question_what="the result of using the keyword :tortoise as a function on the map {:hare 1 :tortoise 2}",
            goal_text="use the keyword :tortoise to look up a value in the map with keys :hare and :tortoise",
            scenario=(
                "The farmer held the same market-basket with two compartments: :hare had 1 coin, "
                ":tortoise had 2 coins. She wanted to reach into the :tortoise compartment."
            ),
            need=(
                "She needed to look up the value in the :tortoise compartment without opening "
                "the :hare compartment."
            ),
            mapping=(
                "The keyword lookup is the farmer's basket-compartment finder: the keyword :tortoise "
                "acts like a hand reaching into the map to find the labeled compartment and pull out "
                "what's inside."
            ),
            resolution=(
                "The REPL returned the result — the value inside the :tortoise compartment of the basket."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(:missing {:hare 1})", expected=None,
            concept_phrase="the keyword lookup",
            question_what="the result of using the keyword :missing as a function on the map {:hare 1}",
            goal_text="use the keyword :missing to look up a value in a map that does not contain :missing",
            scenario=(
                "The farmer held a market-basket with one compartment: :hare held 1 coin. She "
                "looked for a compartment labeled :missing, which did not exist in the basket."
            ),
            need=(
                "She needed to look up the :missing compartment, knowing it wasn't there, and find "
                "what the lookup would return."
            ),
            mapping=(
                "The keyword lookup is the farmer's basket-compartment finder: if the compartment "
                "label doesn't exist in the basket, the lookup returns nil — nothing in that slot."
            ),
            resolution=(
                "The REPL returned nil — no :missing compartment was found in the basket."
            ),
            tags=("story",),
        ),
    ],
    subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_18 = SubjectCurriculum(
    grade=2, subject_id="G2-18",
    subject_title="Quoting symbols",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(symbol? (quote hare))", expected=True,
            concept_phrase="the symbol-predicate applied to a long-form-quoted name",
            question_what="whether long-form quoting produces a symbol",
            goal_text="ask whether long-form quoting of the name hare produces a symbol, using symbol?",
            scenario=(
                "The scribe had written a chalk mark on the pail: the word 'hare' inside "
                "parentheses with the word 'quote' in front. She wondered if the marked name "
                "was a symbol — a label without value."
            ),
            need=(
                "She needed to check if the long-form quoted name hare was a symbol, using the "
                "symbol? predicate."
            ),
            mapping=(
                "The symbol-predicate is the scribe's mark-tester: quoting a name with (quote hare) "
                "creates a symbol — a chalk mark that names itself, not a value. The predicate "
                "symbol? checks if the mark is a symbol."
            ),
            resolution=(
                "The REPL returned the verdict — (quote hare) is a symbol, a chalk mark on the pail."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(= (quote tortoise) 'tortoise)", expected=True,
            concept_phrase="the equality of long-form and short-form quoting",
            question_what="whether long-form and short-form quoting produce equal values",
            goal_text="compare the result of long-form quoting of tortoise against the apostrophe-shorthand quoting of the same name, using =",
            scenario=(
                "The scribe had two chalk marks: one was written as (quote tortoise), the other "
                "as 'tortoise (using the short-hand apostrophe). She wondered if the two chalk "
                "marks were equal."
            ),
            need=(
                "She needed to check if the long-form and short-form quoting produced the same "
                "symbol."
            ),
            mapping=(
                "The equality check is the scribe's mark-matcher: (quote tortoise) and 'tortoise "
                "are two ways of writing the same chalk mark. The apostrophe is shorthand for the "
                "long form."
            ),
            resolution=(
                "The REPL returned the verdict — both chalk marks are equal, the same symbol."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(count '(1 2 3))", expected=3,
            concept_phrase="the element count of a quoted list",
            question_what="the number of elements in a quoted list",
            goal_text="count the elements in a quoted list of the integers 1, 2, and 3",
            scenario=(
                "The scribe had drawn a chalk mark of a quoted list: '(1 2 3). The apostrophe "
                "marked it as a list of symbols, not a function call. She wanted to count how many "
                "elements were in the marked list."
            ),
            need=(
                "She needed to count the elements in the quoted list without evaluating it as code."
            ),
            mapping=(
                "The count operation is the scribe's element-counter: it counts the items in the "
                "chalk-marked list. The apostrophe tells the runtime: 'don't evaluate this as "
                "code, just count the marks.'"
            ),
            resolution=(
                "The REPL returned the result — several elements in the quoted list, the chalk marks counted."
            ),
            tags=("story",),
        ),
    ],
    subplots=_CHALKMARK_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_19 = SubjectCurriculum(
    grade=2, subject_id="G2-19",
    subject_title="Auto-promotion to bigint",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(* 1000000 1000000)", expected=1000000000000,
            concept_phrase="the large multiplication",
            question_what="the product of one million and one million",
            goal_text="multiply one million by one million",
            scenario=(
                "The farmer had a million coins stacked on one side of the counting table and a "
                "million coins stacked on the other side. She wondered what the total would be if "
                "she multiplied them together — a vast number."
            ),
            need=(
                "She needed to multiply one million by one million to find the grand total, which "
                "would be a very large number."
            ),
            mapping=(
                "The large multiplication is the farmer's bigint-counter: when numbers grow beyond "
                "the ordinary range, the REPL automatically promotes them to arbitrary-precision "
                "integers (bigints) to hold the full result."
            ),
            resolution=(
                "{drawn.a} returned: the REPL returned one trillion — the product of one million and one million, "
                "auto-promoted to bigint."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(+ 99999999999 1)", expected=100000000000,
            concept_phrase="the large addition",
            question_what="the sum of 99999999999 and 1",
            goal_text="add 1 to 99999999999",
            scenario=(
                "The farmer had nearly a hundred billion coins in a heap (99999999999). She "
                "added one more coin to the top. She wondered what the new count would be."
            ),
            need=(
                "She needed to add 1 to a very large number, which would exceed normal integer "
                "ranges."
            ),
            mapping=(
                "The large addition is the farmer's bigint-counter: when numbers grow beyond the "
                "ordinary range, the REPL automatically promotes them to arbitrary-precision "
                "integers (bigints) to hold the full result."
            ),
            resolution=(
                "The REPL returned one hundred billion — the sum auto-promoted to bigint."
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_20 = SubjectCurriculum(
    grade=2, subject_id="G2-20",
    subject_title="Counting",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(count [1 2 3])", expected=3,
            concept_phrase="the count operation",
            question_what="the result of using count on the vector containing 1, 2, and 3",
            goal_text="count the elements in the vector containing 1, 2, and 3",
            scenario=(
                "The farmer walked to market counting pails: one step per pail, one "
                "coin per step. She held a vector of three pails in her basket and "
                "needed the total count before she could enter the market gate."
            ),
            need=(
                "She needed a tally that walked through the basket, counting one "
                "element per step, and returned the final number when the walk "
                "was done."
            ),
            mapping=(
                "`count` is the tally-walk: it steps through every element in the "
                "collection exactly once, tallying one per step, and returns the "
                "total at the end of the path."
            ),
            resolution=(
                "{drawn.a} returned: the REPL returned the final tally — one count per element, the walk "
                "complete, the total ready to show at the market gate."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(count "hello")', expected=5,
            concept_phrase="the count operation",
            question_what="the result of using count on the string hello",
            goal_text="count the characters in the string hello",
            scenario=(
                "The farmer had written the word 'hello' on the pail with chalk. She "
                "walked the rope road from the first letter to the last, counting one "
                "letter per step, to find how many characters made up the word."
            ),
            need=(
                "She needed to count every character in the word 'hello' using the "
                "tally-walk, one character per step."
            ),
            mapping=(
                "`count` is the tally-walk: it steps through every character in the "
                "string, tallying one per step, and returns the total at the end."
            ),
            resolution=(
                "The REPL returned the result — five characters in the word 'hello', one per step "
                "of the walk."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(count [])", expected=0,
            concept_phrase="the count operation",
            question_what="the result of using count on the empty vector",
            goal_text="count the elements in an empty vector",
            scenario=(
                "The farmer held an empty basket (an empty vector). She walked the rope "
                "road from start to finish but found no pails inside. She wondered what "
                "the count would be."
            ),
            need=(
                "She needed to count the elements in an empty collection, where the "
                "tally-walk takes no steps."
            ),
            mapping=(
                "`count` is the tally-walk: it walks through the collection, tallying "
                "one per element. If the collection is empty, the walk is instant — no "
                "steps taken, no counts added."
            ),
            resolution=(
                "The REPL returned 0 — an empty vector has zero elements, the walk "
                "finds nothing."
            ),
            tags=("story",),
        ),
    ],
    subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_21 = SubjectCurriculum(
    grade=2, subject_id="G2-21",
    subject_title="String length and substring",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form='(count "tortoise")', expected=8,
            concept_phrase="the count of characters in a string",
            question_what="the result of using count on the string tortoise",
            goal_text="count the characters in the string tortoise",
            scenario=(
                "The milkmaid had woven a cloth-label with the name 'tortoise' braided "
                "end-to-end. She walked the strand from first character to last, counting "
                "each character-knot along the way."
            ),
            need=(
                "She needed to count how many character-knots made up the word 'tortoise' "
                "by walking the strand."
            ),
            mapping=(
                "`count` is the braiding tally-walk: it walks through the cloth-strand, one "
                "character per knot, and returns the total length of the braided thread."
            ),
            resolution=(
                "The REPL returned the count — the total number of character-knots in the strand."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(count "hare")', expected=4,
            concept_phrase="the count of characters in a string",
            question_what="the result of using count on the string hare",
            goal_text="count the characters in the string hare",
            scenario=(
                "The milkmaid had woven another cloth-label with the name 'hare' braided "
                "end-to-end. She walked this shorter strand from first character to last, "
                "counting each knot."
            ),
            need=(
                "She needed to count how many character-knots made up the word 'hare' "
                "by walking the strand."
            ),
            mapping=(
                "`count` is the braiding tally-walk: it walks through the cloth-strand, one "
                "character per knot, and returns the total length of this shorter thread."
            ),
            resolution=(
                "The REPL returned the result — four character-knots in the word 'hare'."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(count (subs "tortoise" 0 3))', expected=3,
            concept_phrase="the count of characters in a leading substring",
            question_what="the count of the substring from index 0 to 3 of the string tortoise",
            goal_text="extract the leading three characters from the string tortoise using subs from index 0 to 3, then count them",
            scenario=(
                "The milkmaid had the cloth-label 'tortoise' and wanted to cut out just the "
                "leading three characters ('tor') using the substring operation. She then walked "
                "the cut piece, counting its knots."
            ),
            need=(
                "She needed to extract characters from index 0 to 3, then count the resulting "
                "substring to verify the cut was correct."
            ),
            mapping=(
                "`subs` is the braiding scissors: it cuts a portion of the cloth-strand from "
                "one index to another. `count` then walks the cut piece, tallying its knots."
            ),
            resolution=(
                "The REPL returned the result — the cut piece 'tor' has three character-knots."
            ),
            tags=("story",),
        ),
    ],
    subplots=_BEADSTRING_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_22 = SubjectCurriculum(
    grade=2, subject_id="G2-22",
    subject_title="Compose pure arithmetic (multi-step calculation)",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(- (* 5 4) 7)", expected=13,
            concept_phrase="the nested arithmetic",
            question_what="the result of multiplying 5 and 4, then subtracting 7",
            goal_text="compute 5 times 4, then subtract 7",
            scenario=(
                "The farmer had a two-step calculation to perform at the counting table. First, "
                "she needed to multiply 5 and 4 to find the harvest from one field. Then, she "
                "would subtract 7 coins owed to the miller from that result."
            ),
            need=(
                "She needed to compose the two operations into one form: multiply first, then "
                "subtract the debt, all in a single nested expression."
            ),
            mapping=(
                "The nested arithmetic is the farmer's chain of operations: the inner (* 5 4) "
                "computes first (20), then the outer (- ... 7) subtracts 7 from that result. "
                "Each step feeds into the next."
            ),
            resolution=(
                "The REPL returned 13 — the product (20) minus the debt (7), the nested "
                "calculation complete."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(+ (* 3 8) (* 2 4))", expected=32,
            concept_phrase="the sum of products",
            question_what="the result of adding the product of 3 and 8 to the product of 2 and 4",
            goal_text="compute the product of 3 and 8, add the product of 2 and 4",
            scenario=(
                "The farmer had two separate harvest groups: one group of 3 traders each selling "
                "8 pails, another group of 2 traders each selling 4 pails. She needed the combined "
                "harvest from both groups."
            ),
            need=(
                "She needed to compute the product of each group, then add them together: "
                "(3 × 8) + (2 × 4), all in one nested expression."
            ),
            mapping=(
                "The sum of products is the farmer's combined harvest: compute the first group's "
                "total (3 × 8 = 24), compute the second group's total (2 × 4 = 8), then add them "
                "together (24 + 8 = 32)."
            ),
            resolution=(
                "The REPL returned 32 — the sum of both group harvests, the nested calculation "
                "complete."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(quot (+ 100 50) 5)", expected=30,
            concept_phrase="the nested quotient",
            question_what="the integer quotient of the sum of 100 and 50 divided by 5",
            goal_text="add 100 and 50, then divide by 5",
            scenario=(
                "The farmer had two coin piles: one with 100 coins, another with 50 coins. She "
                "combined both piles and wanted to divide the total equally among 5 buyers at "
                "the market."
            ),
            need=(
                "She needed to add 100 and 50 first, then divide the sum by 5 to find each buyer's "
                "fair share, all in one nested form."
            ),
            mapping=(
                "The nested quotient is the farmer's fair-share counter: add both piles first "
                "(100 + 50 = 150), then divide that sum by 5 buyers (150 ÷ 5 = 30 per buyer). "
                "Each step depends on the previous."
            ),
            resolution=(
                "The REPL returned 30 — each of the 5 buyers receives 30 coins, the nested "
                "calculation complete."
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
    print(f"grade-2 tortoise-hare smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
