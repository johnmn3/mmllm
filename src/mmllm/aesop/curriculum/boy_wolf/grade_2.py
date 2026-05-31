"""Grade 2 — operators + arithmetic mastery, taught through the
Boy-who-cried-Wolf fable.

Grade 2 deepens grade 1's L1+L2 work. Where grade 1 introduced the
single-arg arithmetic call, grade 2 covers multi-arg arithmetic,
comparison chains, the boolean-logic operators, the numeric helpers
(inc/dec/quot/rem/mod, min/max, abs), strings via str, and the
truthy/falsey rules.

The fable lens: the shepherd's hasty boasts about answers ("I can
guess without computing!") consistently lose to the elder's patient
"let me actually evaluate the form" approach. By grade 2, this becomes
the running joke of the curriculum — the village no longer trusts the
shepherd's claims, and the elder's slate / the watchhouse ledger is the
only voice that settles a calculation.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.boy_wolf.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS,
    _PLAN_POOL,
)
from mmllm.aesop.curriculum.boy_wolf._metaphor_pools import (
    _ACORN_SUBPLOTS, _BASKET_SUBPLOTS, _BEADSTRING_SUBPLOTS, _CHALKMARK_SUBPLOTS, _GATE_SUBPLOTS, _SCRIBE_SUBPLOTS, _TALLYWALK_SUBPLOTS,
)
from mmllm.aesop.curriculum.boy_wolf._goals import GOALS, get_goal


# Extend grade-1's shared pool with two grade-2-specific subplots
# that lean into multi-operand / chained-operator framings. The
# polarity is preserved: SHEPHERD claims-without-checking; ELDER
# insists on the REPL.
_SHARED_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [
    # 9. The chain-of-operations template — useful for multi-arg
    #    arithmetic and comparison-chain subjects. The elder lays out
    #    a chain of small computations on the slate.
    SubplotTemplate("""\
{elder_phrase} had been laying out a chain of small computations on a
slate {place} — one operation, then another, all to settle a question
{shepherd_phrase} had raised. The current form on the slate was
{form_display}, and {elder} explained that {concept_phrase} would be
settled the moment the form was evaluated."""),

    # 10. The stick-in-the-dust template — shepherd boasts they know
    #     without typing it; elder picks up a stick and insists on the
    #     REPL. Comma after "said" handles participle-style EMO_PATIENT.
    #
    #     NOTE (boy-wolf polish, hand-audit pass): the closing
    #     "The REPL will have the last word." was originally written
    #     as a second quoted utterance but the closing `\"` was
    #     forgotten, leaving 12+ records with an unclosed dialogue
    #     quote. Closed below.
    SubplotTemplate("""\
"Whatever {form_display} comes to," {shepherd_phrase} declared,
{emo_proud}, {place}, "anyone could see it without typing a thing."
{elder_phrase}, {emo_patient}, picked up a stick and drew
{concept_phrase} in the dust. "Then write the form," {elder_he_she}
said. "The REPL will have the last word.\""""),
]


def _ex(form, expected, concept, what, goal=None,
        scenario="", need="", mapping="", resolution="",
        tags=()):
    canon = GOALS.get(form, {})
    if all([scenario, need, mapping, resolution]) and "story" not in tags:
        tags = tuple(tags) + ("story",)
    return SubjectExample(
        form=form, expected=expected,
        concept_phrase=canon.get("concept", concept),
        question_what=canon.get("what", what),
        goal_text=goal if goal is not None else get_goal(form, concept, what),
        scenario=scenario, need=need, mapping=mapping, resolution=resolution,
        tags=tags,
    )
# ─────────────────────── 22 grade-2 subjects ───────────────────────


G2_01 = SubjectCurriculum(
    grade=2, subject_id="G2-01",
    subject_title="Multi-arg arithmetic",
    fable="boy-wolf",
    examples=[
        _ex("(+ 1 2 3 4)", 10,        "the sum (+ 1 2 3 4)",      "the result of (+ 1 2 3 4)",
            scenario=(
                "Tom the shepherd stood at the fold with three sheep from "
                "the south pasture, one from the north, and a tally-stick "
                "in his hand. Carol the elder watched from the slate."
            ),
            need=(
                "The morning count needed all four sheep totaled into one "
                "number. Tom claimed he could guess without counting each; "
                "Carol wanted the form to settle it."
            ),
            mapping=(
                "`+` walks through each sheep in turn, adding 1+2, then "
                "the result to 3, then that sum to 4 — the running total "
                "grows with each step through the form."
            ),
            resolution=(
                "the runtime returned 10, the morning's exact count, and Carol notched the tally-stick to match. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record."
            )),
        _ex("(* 2 3 4)", 24,          "the product (* 2 3 4)",    "the result of (* 2 3 4)",
            scenario=(
                "Three pens sat ready at the fold. Each pen held 2 fleeces "
                "stacked from the morning's shearing, and Carol needed the "
                "total fleece count across 4 multiplied lines."
            ),
            need=(
                "Tom guessed wrongly; Carol insisted on the `*` form to find "
                "what two times three times four came to — no guessing at "
                "the watchhouse's wool count."
            ),
            mapping=(
                "`*` walks through: two becomes the starting count, times "
                "three gives the first product, then times four multiplies "
                "again — each step scales the running total."
            ),
            resolution=(
                "the verdict came back from the runtime, and the wool-basket's ledger matched what the slate had computed. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last."
            )),
        _ex("(- 100 1 2 3)", 94,      "the chain (- 100 1 2 3)",  "the result of (- 100 1 2 3)",
            scenario=(
                "Carol stood at the watchhouse with a slate showing 100 "
                "lambs counted at dawn. Three strays had wandered off: one "
                "at the north fence, one at the fold, one at the practice-pen."
            ),
            need=(
                "The afternoon count had to subtract each stray. Tom said "
                "he knew without the math; Carol drew the form to settle "
                "how many the evening tally would show."
            ),
            mapping=(
                "`-` starts at 100, subtracts 1 to get 99, then subtracts "
                "2 from 99 to get 97, then subtracts 3 from 97 — each step "
                "yields the running remainder."
            ),
            resolution=(
                'the call returned 94, the true afternoon count, and the townsfolk ledger stood exactly as Carol had traced it. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'
            )),
        _ex("(+ 1 2 3 4 5 6 7 8 9 10)", 55,
            "the sum 1+2+...+10",       "the sum of integers 1 through 10",
            scenario=(
                "Carol counted ten fence-posts from dawn's walk. At each "
                "post she notched the tally-stick: 1 post, then 2 posts, "
                "then 3 — and so on through the entire line."
            ),
            need=(
                "The village wanted the sum of all those notches as one "
                "number. Tom offered to estimate; Carol preferred to let "
                "the `+` form add them exactly."
            ),
            mapping=(
                "`+` chains through all ten: 1+2 becomes 3, then 3+3 "
                "becomes 6, each addition rolls the running sum forward "
                "until all ten inputs have been folded in."
            ),
            resolution=(
                'the runtime settled on the true sum, and the slate recorded what the form had unveiled. Tom chalked {drawn.a} on the village notice, and the morning record stood for the next shepherd to read.'
            )),
        _ex("(* 1 2 3 4 5)", 120,     "the product 1*2*3*4*5",    "the product of 1 through 5",
            scenario=(
                "Five shepherd families brought their wool to the meadow folk "
                "smithy. One family brought 1 bundle, the next 2, then 3, "
                "then 4, then 5 — all stacked together on the smithy floor."
            ),
            need=(
                "A special commission wanted the total multiplied through: "
                "1 times 2 times 3 times 4 times 5. Tom guessed 30; Carol "
                "insisted the form would yield the true count."
            ),
            mapping=(
                "`*` multiplies step by step: 1*2 yields 2, then 2*3 yields "
                "6, then 6*4 yields 24, then 24*5 yields 120 — each "
                "multiplication scales the running product."
            ),
            resolution=(
                "the call returned 120 as the commissions records demanded, and the smithy's tally matched the runtime's word. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain."
            )),
        _ex("(+ 10 20 30)", 60,       "the sum (+ 10 20 30)",     "the sum of 10, 20, and 30",
            scenario=(
                "Three wagons arrived at the fold with wool sacks: the first "
                "held 10, the second 20, the third 30 — all waiting to be "
                "counted as one total for the evening record."
            ),
            need=(
                "The village ledger needed the sum written down. Tom started "
                "to shout a number; Carol pulled out her slate and insisted "
                "on the form."
            ),
            mapping=(
                "`+` chains the three: 10+20 yields 30, then 30+30 yields "
                "60 — it walks through each wagon's count in sequence."
            ),
            resolution=(
                'the call returned 60, the exact total, and the sheep-shed ledger was settled for the night. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'
            )),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_02 = SubjectCurriculum(
    grade=2, subject_id="G2-02",
    subject_title="Comparison chains",
    fable="boy-wolf",
    examples=[
        _ex("(< 1 2 3)",  True,  "the chain (< 1 2 3)",  "whether 1 < 2 < 3",
            scenario=(
                "Three lambs lined up by the fence-post for the morning "
                "shear. The first weighed 1, the second 2, the third 3 — "
                "each a little heavier than the last."
            ),
            need=(
                "The village wanted to know if the weights rose in a proper "
                "order. Tom guessed yes without looking; Carol insisted on "
                "the form to settle what the scale would confirm."
            ),
            mapping=(
                "`<` checks: is 1 less than 2? Yes. Is 2 less than 3? Yes. "
                "All checks pass, so the chain holds true — each link in "
                "the order is lighter than the next."
            ),
            resolution=(
                'the call returned true, confirming the steady rise in weight that the scale itself had shown. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'
            )),
        _ex("(< 3 2 1)",  False, "the chain (< 3 2 1)",  "whether 3 < 2 < 1",
            scenario=(
                "Three fleeces sat on the wool-basket's shelf. Carol had "
                "weighed them: 3 at the left, 2 in the middle, 1 at the "
                "right — a steady drop."
            ),
            need=(
                "The village wanted to check if they rose instead of fell. "
                "Tom claimed the order looked ascending to him; Carol drew "
                "the form to test what the weights would truly show."
            ),
            mapping=(
                "`<` tests in chain: is 3 less than 2? No — the chain "
                "fails at the first link because the numbers fall instead "
                "of rise."
            ),
            resolution=(
                'the call returned false, settling the truth: the weights fell rather than rose, and Carol marked the slate. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'
            )),
        _ex("(<= 1 1 2)", True,  "the chain (<= 1 1 2)", "whether 1 ≤ 1 ≤ 2",
            scenario=(
                'Carol sorted the bundles by weight: 1 from the south shear, 1 from the north, 2 from the west field — placing the equal ones side by side.'
            ),
            need=(
                "The evening tally needed to know if the weights stayed "
                "level or rose. Tom shrugged; Carol insisted the form would "
                "say whether the chain allowed equality."
            ),
            mapping=(
                "`<=` checks with equality: 1 less-or-equal to 1? Yes. 1 "
                "less-or-equal to 2? Yes. All checks pass because it "
                "allows equals as well as increases."
            ),
            resolution=(
                "it settled at true, and the bundles' order stood confirmed on the ledger. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record."
            )),
        _ex("(> 5 4 3 2 1)", True,
            "the chain (> 5 4 3 2 1)",
            "whether the numbers 5,4,3,2,1 are strictly decreasing",
            scenario=(
                "Carol the elder stacked five tally-sticks by decreasing "
                "height: 5 notches, then 4, then 3, then 2, then 1 — a "
                "perfect stepdown at the watchhouse."
            ),
            need=(
                "The village wanted certainty that the descent was steady. "
                "Tom said he saw the pattern; Carol insisted the form would "
                "verify what the sticks themselves showed."
            ),
            mapping=(
                "`>` chains through: 5 greater than 4? Yes. 4 greater than 3? "
                "Yes. Each check passes because the numbers fall one step at "
                "a time — it walks the chain and confirms the steady "
                "descent."
            ),
            resolution=(
                'the call returned true, and the five sticks stood as proof of a descending order. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
        _ex("(>= 3 3 2)", True,
            "the chain (>= 3 3 2)",
            "whether 3 ≥ 3 ≥ 2",
            scenario=(
                "Three fleece-combs hung on the watchhouse wall: one used 3 "
                "times this morning, one also 3 times, one only 2 — Carol "
                "tallied the use for each."
            ),
            need=(
                "The village wanted to know if the first two matched and the "
                "third was less. Tom guessed yes; Carol drew the form to "
                "settle what the tally would confirm."
            ),
            mapping=(
                "`>=` tests with equality: 3 greater-or-equal to 3? Yes. 3 "
                "greater-or-equal to 2? Yes. The form allows the equal "
                "pair and checks the descent, confirming the whole chain "
                "holds."
            ),
            resolution=(
                'the call returned true, matching the tally-marks Carol had carved. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'
            )),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_03 = SubjectCurriculum(
    grade=2, subject_id="G2-03",
    subject_title="not= and = with multiple args",
    fable="boy-wolf",
    examples=[
        _ex("(not= 1 2)",   True,  "the expression (not= 1 2)",   "whether 1 differs from 2",
            scenario=(
                "Two lambs stood at the fold: one weighed 1, the other 2. "
                "Carol marked both in the tally-book with their separate "
                "counts."
            ),
            need=(
                "The village wanted to know if the weights differed. Tom "
                "said they clearly didn't look the same; Carol insisted the "
                "form would settle what differed and what matched."
            ),
            mapping=(
                "`not=` asks: do 1 and 2 differ? Yes, it confirms "
                "they are not equal — one is lighter than the other."
            ),
            resolution=(
                'the call returned true, confirming the two lambs had separate weights. Tom chalked {drawn.a} on the townsfolk notice, and the morning record stood for the next shepherd to read.'
            )),
        _ex("(not= 1 1)",   False, "the expression (not= 1 1)",   "whether 1 differs from 1",
            scenario=(
                "Carol weighed the same lamb twice in one morning. Both "
                "times it showed 1 on the scale — identical counts."
            ),
            need=(
                "The village wanted to check if they differed, which would "
                "mean an error in the scale. Tom guessed they were the same; "
                "Carol drew the form to verify."
            ),
            mapping=(
                "`not=` checks: do 1 and 1 differ? No — they are equal, so "
                "it returns false and says no difference exists."
            ),
            resolution=(
                'the call returned false, and the scale stood as trusted. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'
            )),
        _ex("(= 1 1 1)",    True,  "the expression (= 1 1 1)",    "whether all of 1,1,1 are equal",
            scenario=(
                "Three tally-tokens sat on the slate, each marked 1. Carol "
                "had counted the same lamb three times across the day."
            ),
            need=(
                'The village wanted to confirm all the counts matched. Tom assumed yes without care; Carol preferred the form to settle what the tokens truly said.'
            ),
            mapping=(
                "`=` asks: are 1, 1, and 1 all equal to each other? Yes — "
                "all three match, so it walks through the chain and "
                "returns true."
            ),
            resolution=(
                "the call returned true, confirming the lamb's steady count across the full day. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then."
            )),
        _ex("(= 1 1 2)",    False, "the expression (= 1 1 2)",    "whether 1,1,2 are all equal",
            scenario=(
                "Carol found three records on the slate: 1 from dawn, 1 from "
                "noon, 2 from dusk — the last one looked wrong."
            ),
            need=(
                "The evening tally wanted to know if all three matched. Tom "
                "saw they didn't; Carol drew the form to settle what the "
                "slate would say when tested."
            ),
            mapping=(
                "`=` checks if all are equal: 1, 1, and 2. The third number "
                "breaks the chain — it doesn't equal the first two, so the "
                "form returns false."
            ),
            resolution=(
                'the call returned false, confirming the dusk entry was wrong, and the slate was corrected. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'
            )),
        _ex("(not= 1 1 2)", True,  "the expression (not= 1 1 2)", "whether at least one of 1,1,2 differs",
            scenario=(
                "Three lamb-counts appeared on the slate: 1, 1, 2. Carol "
                "wanted to know if at least one stood apart from the others."
            ),
            need=(
                "The village preferred to know if the set had any outlier. "
                "Tom shrugged; Carol drew the form to check what differed "
                "in the group."
            ),
            mapping=(
                "`not=` returns true if any value in the group differs from "
                "the others. The 2 is different, so it sees the "
                "difference and returns true."
            ),
            resolution=(
                'the call returned true, marking where the third count broke from the pattern. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'
            )),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_04 = SubjectCurriculum(
    grade=2, subject_id="G2-04",
    subject_title="min and max",
    fable="boy-wolf",
    examples=[
        _ex("(min 1 2 3)",  1, "the expression (min 1 2 3)",  "the minimum of 1, 2, 3",
            scenario=(
                "Carol sorted three lambs by weight: one weighed 1, one 2, "
                "one 3. The village wanted to know which was the lightest "
                "for a special milk-measure test."
            ),
            need=(
                "Finding the lightest meant comparing all three. Tom said he "
                "saw it; Carol insisted the form would pick the minimum "
                "without error."
            ),
            mapping=(
                "`min` walks through the weights, comparing: 1 vs 2 leaves 1, "
                "then 1 vs 3 stays 1 — it tracks the smallest at each "
                "step and returns it."
            ),
            resolution=(
                'the form settled on 1, and the lightest lamb was chosen for the test. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'
            )),
        _ex("(max 1 2 3)",  3, "the expression (max 1 2 3)",  "the maximum of 1, 2, 3",
            scenario=(
                "Three tally-sticks held different notch-counts: 1, 2, 3. The "
                "village wanted the one with the most notches for the evening "
                "record."
            ),
            need=(
                "The elder wanted to pick the highest count. Tom guessed 3; "
                "Carol drew the form to settle what `max` would return."
            ),
            mapping=(
                "`max` compares step by step: 1 vs 2 yields 2, then 2 vs 3 "
                "yields 3 — it keeps the largest and returns it at the end."
            ),
            resolution=(
                'the call returned 3, and the sticks were ranked for the ledger. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
        _ex("(min 7 3 9 1 5)", 1, "the expression (min 7 3 9 1 5)", "the minimum of 7, 3, 9, 1, 5",
            scenario=(
                "Five fleece-baskets sat on the fold, each with a different "
                "weight: 7, 3, 9, 1, 5. The village wanted to find the "
                "lightest to use as a tare weight."
            ),
            need=(
                "Comparing five by hand risked error. Tom started to estimate; "
                "Carol insisted the form would find the minimum precisely."
            ),
            mapping=(
                "`min` walks the five: 7 vs 3 yields 3, then 3 vs 9 stays 3, "
                "then 3 vs 1 yields 1, then 1 vs 5 stays 1 — the form "
                "progressively narrows to the smallest."
            ),
            resolution=(
                'the call returned 1, the true minimum, and the basket was selected for the scale. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'
            )),
        _ex("(max 7 3 9 1 5)", 9, "the expression (max 7 3 9 1 5)", "the maximum of 7, 3, 9, 1, 5",
            scenario=(
                "Five pens held different numbers of lambs: 7, 3, 9, 1, 5. "
                "The village wanted to know which pen was most crowded."
            ),
            need=(
                "The evening ledger needed the maximum count. Tom offered a "
                "rough estimate; Carol drew the form to settle what the "
                "largest was."
            ),
            mapping=(
                "`max` walks through: 7 vs 3 yields 7, then 7 vs 9 yields 9, "
                "then 9 vs 1 stays 9, then 9 vs 5 stays 9 — the form "
                "steadily finds the largest."
            ),
            resolution=(
                'the call returned 9, confirming which pen needed the most care at sundown. Tom chalked {drawn.a} on the valley notice, and the morning record stood for the next shepherd to read.'
            )),
        _ex("(min -3 -1 -5)", -5, "the expression (min -3 -1 -5)", "the minimum of -3, -1, -5",
            scenario=(
                "Carol recorded three adjustments on the slate for the day's "
                "count: -3 (missing lambs), -1 (injury), -5 (a larger loss). "
                "She wanted the smallest adjustment — the worst case — to "
                "prepare the evening report."
            ),
            need=(
                "The village needed to know the worst adjustment to assess "
                "the day. Tom guessed -1; Carol insisted the form would show "
                "the true minimum."
            ),
            mapping=(
                "`min` compares negatives: -3 vs -1 yields -3, then -3 vs -5 "
                "yields -5 — with negatives, the smallest number is furthest "
                "from zero, so it returns -5."
            ),
            resolution=(
                'the call returned -5, the deepest loss, and the slate was adjusted for the evening tally. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'
            )),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_05 = SubjectCurriculum(
    grade=2, subject_id="G2-05",
    subject_title="quot, rem, mod",
    fable="boy-wolf",
    examples=[
        _ex("(quot 17 5)", 3, "the integer quotient of 17 and 5", "the result of (quot 17 5)",
            scenario=(
                "Carol divided 17 lambs into groups of 5. Three complete "
                "groups formed on the fold, with a few left over. The village "
                "wanted to know how many full groups."
            ),
            need=(
                "The count of complete groups was the quotient. Tom guessed 4; "
                "Carol drew the form to settle what integer division would give."
            ),
            mapping=(
                "`quot` finds how many times 5 fits wholly into 17: once, "
                "twice, three times — but four times exceeds 17, so the form "
                "returns 3."
            ),
            resolution=(
                'the call returned 3, the count of complete groups, and the shepherd knew how many full pens to fill. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'
            )),
        _ex("(rem 17 5)",  2, "the remainder of 17 divided by 5", "the result of (rem 17 5)",
            scenario=(
                "After forming three groups of 5 lambs from the 17, Carol "
                "had 2 left standing alone by the fence. The village wanted "
                "to know what remained unpaired."
            ),
            need=(
                "The leftover count was essential for the evening tally. Tom "
                "said he counted 2; Carol insisted the form would show the "
                "remainder exactly."
            ),
            mapping=(
                "`rem` finds what's left after `quot` does its work: 17 minus "
                "(3*5) equals 2 — it returns what didn't fit into the "
                "complete groups."
            ),
            resolution=(
                'the call returned 2, the exact remainder, and the slate recorded the unpaired lambs. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'
            )),
        _ex("(mod 17 5)",  2, "17 mod 5",                          "the result of (mod 17 5)",
            scenario=(
                "Carol worked with `mod` to sort lambs by a five-day cycle. "
                "On day 17 of the year, she wanted to know which position in "
                "the cycle it occupied."
            ),
            need=(
                "The position in the five-day cycle mattered for rotation. Tom "
                "counted on his fingers; Carol drew the form for the true modulo."
            ),
            mapping=(
                "`mod` finds the position in the cycle: 17 divided by 5 has a "
                "remainder of 2, so `mod` returns 2 — the position within the "
                "repeating cycle."
            ),
            resolution=(
                "the call returned 2, the day's cycle position, and the rotation schedule was kept. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear."
            )),
        _ex("(quot 100 7)", 14, "the integer quotient of 100 and 7", "the result of (quot 100 7)",
            scenario=(
                "100 fleeces arrived for sale. Carol grouped them by sevens "
                "for the market. Full bundles formed, with some "
                "leftovers. The buyer wanted to know the bundle count."
            ),
            need=(
                "The quotient told how many complete sevens fit. Tom started "
                "division on a tally-stick; Carol preferred the form."
            ),
            mapping=(
                "`quot` divides: 100 by 7 goes through the quotient exactly, "
                "with a remainder left over — it returns the quotient count."
            ),
            resolution=(
                'the call returned the bundle count, confirming what the market ledger needed. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'
            )),
        _ex("(rem 100 7)",  2, "the remainder of 100 divided by 7", "the result of (rem 100 7)",
            scenario=(
                "From the 100 fleeces, Carol had bundled 14 complete sevens, "
                "leaving 2 loose fleeces. The merchant wanted to know exactly "
                "what remained outside the bundles."
            ),
            need=(
                "The remainder mattered for the price adjustment. Tom said he "
                "saw 2 left; Carol drew the form to verify the exact remainder."
            ),
            mapping=(
                "`rem` calculates 100 - (14*7), which is 100 - 98 = 2 — the "
                "form returns what doesn't bundle into sevens."
            ),
            resolution=(
                'the call returned 2, the loose fleece count, and the price was adjusted accordingly. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
        _ex("(mod -7 3)",   2, "the expression (mod -7 3)",              "the result of (mod -7 3)",
            scenario=(
                "Carol tracked an inventory adjustment of -7 (a loss). She "
                "wanted to know where -7 fell in a three-step cycle (positions "
                "0, 1, 2, then repeat). The form would tell her the cycle position."
            ),
            need=(
                "The cycle position mattered for the reorder schedule. Tom "
                "guessed 1; Carol insisted the form would give the true modulo "
                "for negatives."
            ),
            mapping=(
                "`mod` with negatives wraps to the positive cycle: -7 mod 3 "
                "yields 2 because it adds 3 repeatedly to -7 until it "
                "falls in the range [0,3)."
            ),
            resolution=(
                'the call returned 2, the correct cycle position for the negative adjustment. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'
            )),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_06 = SubjectCurriculum(
    grade=2, subject_id="G2-06",
    subject_title="inc and dec",
    fable="boy-wolf",
    examples=[
        _ex("(inc 5)",  6, "the expression (inc 5)",  "5 plus 1",
            scenario=(
                "Carol stood at the fold with 5 lambs counted on her tally-stick. "
                "A sixth arrived, and she needed the new count."
            ),
            need=(
                "One more lamb meant adding exactly 1. Tom said he knew the count; "
                "Carol drew the form to settle the successor."
            ),
            mapping=(
                "`inc` adds 1 to the given number — it's the successor function, "
                "always returning the number plus one. Here, 5 becomes 6."
            ),
            resolution=(
                'the call returned 6, and the tally-stick gained one more notch. Tom chalked {drawn.a} on the village notice, and the morning record stood for the next shepherd to read.'
            )),
        _ex("(dec 5)",  4, "the expression (dec 5)",  "5 minus 1",
            scenario=(
                "Carol had 5 lambs at the fold. One strayed, and she needed the "
                "corrected count on the slate."
            ),
            need=(
                "One missing lamb meant subtracting exactly 1. Tom guessed 4; Carol "
                "insisted the form would settle the true predecessor."
            ),
            mapping=(
                "`dec` subtracts 1 from the given number — it's the predecessor "
                "function, always returning the number minus one. Here, 5 becomes 4."
            ),
            resolution=(
                'the call returned 4, and the slate was corrected for the afternoon count. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'
            )),
        _ex("(inc 0)",  1, "the expression (inc 0)",  "the successor of 0",
            scenario=(
                "Carol's tally began at zero at dawn. The first lamb arrived, and "
                "she needed to mark its entry."
            ),
            need=(
                "One lamb from zero meant advancing the counter by 1. Tom claimed "
                "it was obvious; Carol drew the form to settle what comes after zero."
            ),
            mapping=(
                "`inc` finds what comes after any number — here, the successor of "
                "zero is 1, showing that it works at the boundary."
            ),
            resolution=(
                'the call returned 1, and the first notch was carved. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'
            )),
        _ex("(dec 0)", -1, "the expression (dec 0)",  "the predecessor of 0",
            scenario=(
                "Carol marked an inventory adjustment: one item owed but not yet "
                "delivered. She started from zero and applied the loss."
            ),
            need=(
                "One loss from zero meant moving into negative count. Tom hesitated; "
                "Carol drew the form to find what comes before zero."
            ),
            mapping=(
                "`dec` finds the predecessor of any number, even zero. Here, zero "
                "becomes -1, showing it extends to negative counts."
            ),
            resolution=(
                'the call returned -1, and the slate recorded the debt. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'
            )),
        _ex("(inc -1)", 0, "the expression (inc -1)", "the successor of -1",
            scenario=(
                "Carol had a -1 adjustment on the slate (one owed). That item "
                "finally arrived, canceling the debt."
            ),
            need=(
                "Adding one to the owed amount meant returning to zero. Tom said "
                "it would settle; Carol insisted the form would confirm what -1 "
                "plus 1 came to."
            ),
            mapping=(
                "`inc` adds 1 to any number, including negatives. Here, -1 plus 1 "
                "returns to zero, showing it balances the ledger."
            ),
            resolution=(
                'the call returned 0, the debt was paid, and the slate stood clear. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'
            )),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_07 = SubjectCurriculum(
    grade=2, subject_id="G2-07",
    subject_title="Absolute value",
    fable="boy-wolf",
    examples=[
        _ex("(abs 5)",   5, "the expression (abs 5)",   "the absolute value of 5",
            scenario=(
                "Carol marked 5 on the slate — a gain of five fleeces. She wanted "
                "to know how many fleeces that represented as a pure count, ignoring "
                "the sign."
            ),
            need=(
                "The ledger needed the absolute magnitude. Tom said 5 is 5; Carol "
                "drew the form to show what `abs` returned."
            ),
            mapping=(
                "`abs` strips the sign, leaving the magnitude. For 5, which is "
                "already positive, it returns 5 unchanged."
            ),
            resolution=(
                'the call returned 5, and the magnitude was recorded. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'
            )),
        _ex("(abs -5)",  5, "the expression (abs -5)",  "the absolute value of -5",
            scenario=(
                "Carol recorded -5 on the slate — a loss of five fleeces. For the "
                "shipment ledger, she needed the magnitude alone."
            ),
            need=(
                "The distance from zero mattered, not the direction. Tom said the "
                "loss was 5 units; Carol insisted the form would show the magnitude."
            ),
            mapping=(
                "`abs` flips the sign for negatives, leaving the magnitude. For -5, "
                "the form removes the minus and returns 5."
            ),
            resolution=(
                'the call returned 5, the absolute magnitude, and the shipment was accounted for. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
        _ex("(abs 0)",   0, "the expression (abs 0)",   "the absolute value of 0",
            scenario=(
                "Carol checked the slate at noon: the tally showed 0. She wanted to "
                "confirm that zero's absolute value was zero."
            ),
            need=(
                "The boundary case mattered. Tom said zero was zero; Carol drew the "
                "form to verify."
            ),
            mapping=(
                "`abs` of zero returns zero — there's no sign to strip from the "
                "neutral point."
            ),
            resolution=(
                'the call returned 0, confirming the slate stood at the origin. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'
            )),
        _ex("(abs (- 3 8))", 5,
            "the expression (abs (- 3 8))",
            "the absolute value of 3 minus 8",
            scenario=(
                "Carol computed 3 - 8 on the slate and got -5. The village wanted "
                "to know the distance between 3 and 8 as a positive count."
            ),
            need=(
                "The difference magnitude, not the signed result, mattered for the "
                "journey-distance calculation. Tom guessed 5; Carol insisted the "
                "form would settle what the absolute value was."
            ),
            mapping=(
                "`abs` works on the result of inner forms. First, `(- 3 8)` yields "
                "-5, then `abs` strips the minus and returns 5 — the distance as a "
                "positive count."
            ),
            resolution=(
                'the call returned 5, the true distance, and the route was calculated for the runner. Tom chalked {drawn.a} on the watchhouse notice, and the morning record stood for the next shepherd to read.'
            )),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_08 = SubjectCurriculum(
    grade=2, subject_id="G2-08",
    subject_title="Arithmetic on ratios",
    fable="boy-wolf",
    examples=[
        _ex("(+ 1/2 1/4)", "3/4",
            "the sum 1/2 + 1/4",       "the value of (+ 1/2 1/4)",
            scenario=(
                "Carol divided a fleece into quarters. She had 1/2 of the fleece "
                "in one pile and 1/4 in another, and wanted to combine them."
            ),
            need=(
                "The village ledger needed the total as one fraction. Tom said "
                "roughly 3/4; Carol drew the form to settle what the exact sum was."
            ),
            mapping=(
                "`+` adds the fractions: 1/2 is 2/4, and 2/4 + 1/4 yields 3/4 "
                "— it finds a common denominator and adds the parts."
            ),
            resolution=(
                'the call returned 3/4, the exact combined fraction, and the fleece was tallied.'
            )),
        _ex("(* 2/3 3/4)", "1/2",
            "the product 2/3 × 3/4",   "the value of (* 2/3 3/4)",
            scenario=(
                "Carol took 2/3 of the meadow folk's wool-dye and used 3/4 of that "
                "amount for the day's coloring. She needed to know what fraction "
                "of the original dye remained."
            ),
            need=(
                "The yield calculation required multiplying the fractions. Tom "
                "guessed 1/2; Carol insisted the form would give the exact product."
            ),
            mapping=(
                "`*` multiplies fractions by multiplying numerators and "
                "denominators: (2×3)/(3×4) = 6/12, which the form simplifies to 1/2."
            ),
            resolution=(
                'the call returned 1/2, the exact yield, and the dye ledger was updated.'
            )),
        _ex("(- 1 1/3)", "2/3",
            "the expression (- 1 1/3)",      "the value of (- 1 1/3)",
            scenario=(
                "Carol started with 1 full fleece on the slate. She removed 1/3 "
                "for the market sale."
            ),
            need=(
                "The remaining fraction mattered for the evening tally. Tom said "
                "roughly 2/3; Carol drew the form to settle what was left."
            ),
            mapping=(
                "`-` subtracts the fraction: 1 is 3/3, and 3/3 - 1/3 yields 2/3 "
                "— the form converts the whole to thirds and subtracts."
            ),
            resolution=(
                'the call returned 2/3, the exact remainder, and the sale was recorded. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'
            )),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_09 = SubjectCurriculum(
    grade=2, subject_id="G2-09",
    subject_title="Floats vs ints (the / operator)",
    fable="boy-wolf",
    examples=[
        _ex("(/ 10 2)", 5,    "the integer division 10 ÷ 2",
            "the value of (/ 10 2)",
            scenario=(
                "Carol divided 10 fleeces equally between 2 pens. The division "
                "came out exact: 5 fleeces per pen, with no remainder."
            ),
            need=(
                "The ledger needed the clean result. Tom said 5; Carol insisted "
                "it would settle what the division gave."
            ),
            mapping=(
                "`/` divides 10 by 2, yielding 5 exactly — when the division is "
                "clean, it returns an integer."
            ),
            resolution=(
                'the call returned 5, and the pens were stocked equally. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'
            )),
        _ex("(/ 10 3)", "10/3", "the expression (/ 10 3)",
            "the exact rational result of (/ 10 3)",
            scenario=(
                "Carol divided 10 fleeces among 3 pens. The division wasn't clean "
                "— there was a remainder — but she wanted the exact fraction, not "
                "an approximation."
            ),
            need=(
                "The precise fraction mattered for the record. Tom said roughly "
                "3.3; Carol insisted the form would give the exact fraction."
            ),
            mapping=(
                "`/` returns a rational number when the division doesn't come out "
                "even. Here, 10/3 is the exact fraction — the form preserves the "
                "precision."
            ),
            resolution=(
                'the call returned 10/3, the exact amount per pen, and the ledger held the precise fraction. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'
            )),
        _ex("(/ 1.0 2)", 0.5, "the float division 1.0 ÷ 2",
            "the value of (/ 1.0 2)",
            scenario=(
                "Carol weighed 1.0 fleeces as a decimal quantity (a standard measure). "
                "She divided it by 2 and needed the result as a float."
            ),
            need=(
                "The float-based measurement system required a decimal result. Tom "
                "guessed 0.5; Carol insisted the form would give the precise float."
            ),
            mapping=(
                "`/` with floats returns a float: 1.0 divided by 2 yields 0.5 "
                "— the form preserves the float type through the operation."
            ),
            resolution=(
                'the call returned 0.5, matching the decimal measurement system, and the precision was kept. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'
            )),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_10 = SubjectCurriculum(
    grade=2, subject_id="G2-10",
    subject_title="Powers via repeated multiplication",
    fable="boy-wolf",
    examples=[
        _ex("(* 2 2 2)", 8,        "two cubed", "2 to the third power",
            scenario=(
                "Carol stacked boxes in a cube pattern: 2 boxes deep, 2 boxes wide, "
                "2 boxes tall. She wanted to know the total volume."
            ),
            need=(
                "The cube volume required multiplying 2 three times. Tom estimated; "
                "Carol drew the form to settle what 2 to the third power was."
            ),
            mapping=(
                "`*` multiplies: 2 * 2 yields 4, then 4 * 2 yields 8 — the form "
                "chains the repeated multiplication to find the third power."
            ),
            resolution=(
                'the call returned 8, the exact volume, and the box-shed was stocked. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'
            )),
        _ex("(* 5 5)",   25,       "five squared", "5 squared",
            scenario=(
                "Carol laid out a square patch for a garden: 5 strides on one side, "
                "5 strides on the other. She wanted the total area."
            ),
            need=(
                "The garden area required squaring 5. Tom guessed wrongly; Carol "
                "insisted the form would settle the exact area."
            ),
            mapping=(
                "`*` multiplies: 5 * 5 yields the square — it computes it "
                "directly."
            ),
            resolution=(
                'the call returned the exact area, and the garden plot was measured. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
        _ex("(* 3 3 3 3)", 81,     "three to the fourth", "3 to the fourth power",
            scenario=(
                "A grain merchant stacked sacks in a four-layer cube: 3 sacks deep, "
                "3 wide, 3 tall, with 3 such cubes for the townsfolk. She wanted the "
                "total count."
            ),
            need=(
                "The count required multiplying 3 four times. Tom started on his "
                "fingers; Carol drew the form to settle 3 to the fourth power."
            ),
            mapping=(
                "`*` chains: 3 * 3 yields a product, then that times 3, then that times 3 "
                "again — it walks through the fourth power step by step."
            ),
            resolution=(
                'the call returned the total sack count, and the shipment was tallied. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'
            )),
        _ex("(* 10 10)", 100,      "ten squared", "10 squared",
            scenario=(
                "Carol sketched a square grid: 10 rows by 10 columns. The village "
                "wanted to know how many cells fit."
            ),
            need=(
                "The cell count required 10 squared. Tom guessed; Carol insisted "
                "it would confirm the exact count."
            ),
            mapping=(
                "`*` multiplies: 10 * 10 yields the square — a clean computation where 10 "
                "appears twice in the multiplication."
            ),
            resolution=(
                'the call returned the exact grid count, and the sketch was validated. Tom chalked {drawn.a} on the village notice, and the morning record stood for the next shepherd to read.'
            )),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_11 = SubjectCurriculum(
    grade=2, subject_id="G2-11",
    subject_title="String concatenation with str",
    fable="boy-wolf",
    examples=[
        _ex('(str "wa" "tch")', "watch",
            'the expression (str "wa" "tch")', 'the joined string "watch"',
            scenario=(
                "Carol the elder pulled out her knotted tally-cord — a "
                "long cord with knots tied at intervals, each section "
                "carrying its own labeled bead. The cord lay on the slate "
                "in two pieces: `wa` knotted at one end, `tch` knotted at "
                "the other."
            ),
            need=(
                "The full word the meadow folk wanted on the slate was the "
                "two pieces spliced together as one cord. Tom guessed at "
                "the result; Carol insisted on letting the runtime "
                "splice the cord properly."
            ),
            mapping=(
                "`str` is the splice — it takes pieces of bead-string "
                "and ties them end-to-end into a single cord. Each "
                "argument becomes the next stretch of beads; the result "
                "is one continuous string."
            ),
            resolution=(
                "the runtime returned the spliced cord and the valley's slate carried the full word, exactly as the two pieces had promised. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain."
            )),
        _ex('(str "flock")', "flock",
            'the expression (str "flock")', 'the value of (str "flock")',
            scenario=(
                "Carol held a single bead-string labeled `flock` at the watchhouse. "
                "She wanted to confirm that splicing it alone with nothing else "
                "returned the same bead-string."
            ),
            need=(
                "The test needed the form to show that one piece alone spliced to "
                "itself. Tom said obviously it did; Carol insisted the form would "
                "confirm."
            ),
            mapping=(
                "`str` with a single argument is a splice with no other pieces — "
                "it returns the bead-string unchanged."
            ),
            resolution=(
                'the call returned the bead-string as is, and the test passed. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'
            )),
        _ex('(str "x" "y" "z")', "xyz",
            'the expression (str "x" "y" "z")', 'the joined string "xyz"',
            scenario=(
                "Carol laid three bead-pieces on the slate: `x`, `y`, and `z`. She "
                "wanted to splice them into one continuous cord."
            ),
            need=(
                "The combined message required all three pieces spliced end-to-end. "
                "Tom guessed the result; Carol insisted the form would tie the cord."
            ),
            mapping=(
                "`str` with three arguments ties three cord-pieces together: the "
                "runtime splices `x` then `y` then `z` into one continuous bead-string."
            ),
            resolution=(
                'the call returned the spliced cord as `xyz`, and the message was complete. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'
            )),
        _ex('(str 1 "+" 2 "=" 3)', "1+2=3",
            'the expression (str 1 "+" 2 "=" 3)', 'the joined string "1+2=3"',
            scenario=(
                "Carol built a mathematical statement on the slate by splicing pieces: "
                "the number 1, the symbol `+`, the number 2, the symbol `=`, and the "
                "number 3."
            ),
            need=(
                "The equation needed all five pieces spliced as one string. Tom said "
                "it was obvious; Carol insisted the form would splice it exactly."
            ),
            mapping=(
                "`str` splices mixed numbers and strings: the runtime converts each "
                "number to its string form and appends them with the symbols "
                "— building the full equation string step by step."
            ),
            resolution=(
                'the call returned the complete equation, and the slate held the joined statement. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'
            )),
    ],
    subplots=_BEADSTRING_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_12 = SubjectCurriculum(
    grade=2, subject_id="G2-12",
    subject_title="print and println — return values",
    fable="boy-wolf",
    examples=[
        # println side-effects to stdout but RETURNS nil. The form
        # we ask for has the value nil; the model writes println
        # and the runtime returns nil.
        _ex('(println "hello")', None,
            'the expression (println "hello")',
            'the return value of (println "hello")',
            scenario=(
                "Carol wrote a message on the watchhouse slate: `hello`. She "
                "wanted the REPL to display the message for all the shepherds "
                "to read, then asked what it would return."
            ),
            need=(
                "The display needed the message sent to the valley notice-board, "
                "but the form's return value mattered too. Tom said it returned the "
                "string; Carol insisted the form would return nothing once printed."
            ),
            mapping=(
                "`println` writes the message to the slate for all to see — a "
                "side-effect — but then returns `nil`, the absence of a value. "
                "The writing happens; the return is empty."
            ),
            resolution=(
                'the form displayed the message and returned nothing — `nil` settled on the slate where a return value would have been. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'           )),
        _ex('(print "x")', None,
            'the expression (print "x")',
            'the return value of (print "x")',
            scenario=(
                "Carol wanted to write a single character `x` to the slate without "
                "moving to a new line. She asked what it would return."
            ),
            need=(
                "The character needed to appear, and the form's return value had to "
                "be settled. Tom guessed it returned the character; Carol insisted "
                "it would show the true return."
            ),
            mapping=(
                "`print` writes the character to the slate — the side-effect — but "
                "like `println`, it returns `nil` once done. The character appears; "
                "the return is empty."
            ),
            resolution=(
                'the form displayed the character and returned nothing — the slate held the message and the void where a value would be. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'           )),
    ],
    subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_13 = SubjectCurriculum(
    grade=2, subject_id="G2-13",
    subject_title="and / or — short circuit, return values",
    fable="boy-wolf",
    examples=[
        _ex("(and true true)",   True,   "the expression (and true true)",
            "the value of (and true true)",
            scenario=(
                "Two fold-gates stood in the shepherd's path: the first open (true), "
                "the second open (true). The shepherd wanted to know if both gates "
                "allowed passage."
            ),
            need=(
                "Both gates had to be open for passage. Tom saw the first was open; "
                "Carol insisted the form would confirm both were passable."
            ),
            mapping=(
                "`and` checks the first gate (true), walks through, checks the "
                "second gate (true), and returns true only if all gates pass."
            ),
            resolution=(
                'the call returned true, and the shepherd could walk straight through both gates.'
            )),
        _ex("(and true false)",  False,  "the expression (and true false)",
            "the value of (and true false)",
            scenario=(
                "The first fold-gate was open (true), but the second was closed (false). "
                "The shepherd wanted to know if the path was passable."
            ),
            need=(
                "If any gate closed, the path was blocked. Tom saw the first opened; "
                "Carol insisted the form would settle if both allowed passage."
            ),
            mapping=(
                "`and` checks the first gate (true), walks through, checks the "
                "second gate (false) — and stops there. It returns false because "
                "the second gate blocked the way."
            ),
            resolution=(
                'the call returned false, the path was blocked, and the shepherd had to wait at the closed gate.'
            )),
        _ex("(or false true)",   True,   "the expression (or false true)",
            "the value of (or false true)",
            scenario=(
                "Two alternative paths led to the fold: the first closed (false), "
                "the second open (true). The shepherd wanted to know if any path "
                "was passable."
            ),
            need=(
                "At least one open path meant progress. Tom saw the first closed; "
                "Carol insisted the form would settle if any path led forward."
            ),
            mapping=(
                "`or` checks the first path (false), keeps walking, checks the "
                "second path (true), and returns true because at least one path "
                "was open."
            ),
            resolution=(
                'the call returned true, the second path was passable, and the shepherd could proceed.'
            )),
        _ex("(or false false)",  False,  "the expression (or false false)",
            "the value of (or false false)",
            scenario=(
                "Both paths were blocked: the first closed (false), the second also "
                "closed (false). The shepherd wanted to know if any way forward "
                "existed."
            ),
            need=(
                "No open path meant the shepherd was blocked. Tom saw both gates "
                "closed; Carol insisted the form would confirm no passage."
            ),
            mapping=(
                "`or` checks the first path (false), keeps walking, checks the "
                "second path (false), and returns false because no path was open."
            ),
            resolution=(
                'the call returned false, all paths were blocked, and the shepherd had to wait.'
            )),
        _ex("(and 1 2 3)",       3,      "the expression (and 1 2 3)",
            "the value of (and 1 2 3)",
            scenario=(
                'Three checks in sequence: a count of 1 sheep, then 2 more, then 3 more. Carol used `and` to verify all {drawn.c} counts were truthy (non-zero).'
            ),
            need=(
                'All {drawn.c} counts had to be non-zero. Tom guessed they were; Carol insisted the form would return what all three were satisfied with.'
            ),
            mapping=(
                "`and` checks: is 1 truthy? Yes. Is 2 truthy? Yes. Is 3 truthy? Yes. "
                "All pass, so it returns the last value — 3."
            ),
            resolution=(
                'the call returned 3, confirming all three counts were valid, and the tally stood complete. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'
            )),
        _ex("(or nil false 5)",  5,      "the expression (or nil false 5)",
            "the value of (or nil false 5)",
            scenario=(
                "Three options for the evening's search: nothing (nil), blocked (false), "
                "or find 5 lambs (5). Carol used `or` to find the first truthy value."
            ),
            need=(
                "The first non-falsey option mattered. Tom started with nothing; Carol "
                "insisted the form would return the first option that worked."
            ),
            mapping=(
                "`or` checks: is nil truthy? No. Is false truthy? No. Is 5 truthy? Yes. "
                "It stops and returns 5, the first truthy value found."
            ),
            resolution=(
                'the call returned 5, the winning option, and the search direction was clear. Tom chalked {drawn.a} on the village notice, and the morning record stood for the next shepherd to read.'
            )),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_14 = SubjectCurriculum(
    grade=2, subject_id="G2-14",
    subject_title="not — turning truthy to false",
    fable="boy-wolf",
    examples=[
        _ex("(not true)",  False, "the expression (not true)",  "the value of (not true)",
            scenario=(
                "Carol stood at the fold-gate, which was open (true). She wanted the "
                "opposite state — was the gate closed?"
            ),
            need=(
                "The inverse of open mattered for the alarm. Tom said the gate was "
                "open; Carol insisted the form would settle what not-open was."
            ),
            mapping=(
                "`not` flips the truth: true becomes false — if the gate is open, "
                "then the gate is not closed, so `not true` returns false."
            ),
            resolution=(
                "the call returned false, confirming the gate wasn't closed — it was open."
            )),
        _ex("(not false)", True,  "the expression (not false)", "the value of (not false)",
            scenario=(
                "The fold-gate was locked (false). Carol wanted to confirm the "
                "opposite: was it open?"
            ),
            need=(
                "The inverse of locked mattered. Tom saw the gate was closed; Carol "
                "insisted the form would settle if it was not closed."
            ),
            mapping=(
                "`not` flips: false becomes true — if the gate is locked, then the "
                "gate is not open, but `not false` returns true as the opposite state."
            ),
            resolution=(
                'the call returned true, settling that the gate was indeed not locked in the logical sense.'
            )),
        _ex("(not nil)",   True,  "the expression (not nil)",   "the value of (not nil)",
            scenario=(
                "Carol checked the ledger and found nothing entered (nil). She wanted "
                "to know if there was something there."
            ),
            need=(
                "The emptiness needed to be inverted. Tom saw nothing; Carol insisted "
                "it would settle what not-nothing was."
            ),
            mapping=(
                "`not` inverts nil: since nil is falsey, `not nil` returns true — "
                "the logical flip of no-thing is yes-thing (truthy)."
            ),
            resolution=(
                'the call returned true, confirming that not-nil was truthy.'
            )),
        _ex("(not 0)",     False, "the expression (not 0)",     "the value of (not 0)",
            scenario=(
                "Carol recorded 0 sheep counted. She wanted to know if that was "
                "falsey (meaning empty and not-truthy)."
            ),
            need=(
                "The truthiness of zero mattered for the conditional. Tom said zero "
                "was falsey; Carol insisted the form would show what not-zero was."
            ),
            mapping=(
                "`not` inverts: 0 is truthy (in this language), so `not 0` returns "
                "false — the zero is considered true, so its negation is false."
            ),
            resolution=(
                'the call returned false, confirming that 0 was on the truthy side. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'
            )),
        _ex("(not \"\")",  False, "the expression (not \"\")",  "the value of (not \"\")",
            scenario=(
                "Carol wrote an empty string on the slate (no characters). She wanted "
                "to know if that was falsey."
            ),
            need=(
                "The truthiness of the empty string mattered. Tom said it was empty; "
                "Carol insisted the form would settle what not-empty was."
            ),
            mapping=(
                "`not` inverts: the empty string is truthy in this language, so "
                "`not \"\"` returns false — the string exists (even empty), so it's "
                "true, and its negation is false."
            ),
            resolution=(
                'the call returned false, confirming the empty string was on the truthy side. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'
            )),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_15 = SubjectCurriculum(
    grade=2, subject_id="G2-15",
    subject_title="Falsey values: only false and nil",
    fable="boy-wolf",
    examples=[
        _ex("(if 0 :truthy :falsey)",   ":truthy", "the expression (if 0 :truthy :falsey)",
            "which keyword (if 0 :truthy :falsey) returns",
            scenario=(
                "Carol stood at a fold-gate. A count of 0 stood on the slate — "
                "a neutral value, neither positive nor negative."
            ),
            need=(
                "The conditional at the fold-gate needed to know if 0 was truthy. "
                "Tom said it seemed falsey; Carol insisted the form would settle "
                "what path the 0 would open."
            ),
            mapping=(
                "`if` tests the condition: 0 is truthy in this language (not nil, "
                "not false), so the form opens the truthy path and returns `:truthy`."
            ),
            resolution=(
                'the call returned `:truthy`, confirming that 0 opens the truthy gate. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'
            )),
        _ex("(if \"\" :truthy :falsey)", ":truthy", "the expression (if \"\" :truthy :falsey)",
            "which keyword (if \"\" :truthy :falsey) returns",
            scenario=(
                "Carol wrote an empty string on the slate — zero characters, "
                "but a string nonetheless. She wanted to know which path the "
                "conditional would take."
            ),
            need=(
                "The gate needed to know if the empty string was truthy. Tom said "
                "it looked empty; Carol insisted the form would settle which path "
                "it opened."
            ),
            mapping=(
                "`if` tests: the empty string is truthy (it exists, just with no "
                "characters), so the form opens the truthy path and returns `:truthy`."
            ),
            resolution=(
                'the call returned `:truthy`, confirming that even empty strings are truthy. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'
            )),
        _ex("(if nil :truthy :falsey)", ":falsey", "the expression (if nil :truthy :falsey)",
            "which keyword (if nil :truthy :falsey) returns",
            scenario=(
                "Carol's search for an entry in the ledger came up empty — nil. "
                "The conditional needed to know which path a missing value took."
            ),
            need=(
                "The gate had to decide based on nil. Tom said nothing was nothing; "
                "Carol insisted the form would settle which path nil opened."
            ),
            mapping=(
                "`if` tests: nil is falsey (the only non-false falsey value), so "
                "the form opens the falsey path and returns `:falsey`."
            ),
            resolution=(
                'the call returned `:falsey`, confirming that nil triggers the falsey branch. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'
            )),
        _ex("(if false :truthy :falsey)", ":falsey", "the expression (if false :truthy :falsey)",
            "which keyword (if false :truthy :falsey) returns",
            scenario=(
                "Carol placed false (a rejected condition) on the slate. The "
                "conditional needed to know which path false would take."
            ),
            need=(
                "The gate had to decide based on false. Tom said false was false; "
                "Carol insisted the form would settle which path it opened."
            ),
            mapping=(
                "`if` tests: false is falsey (by definition), so the form opens "
                "the falsey path and returns `:falsey`."
            ),
            resolution=(
                'the call returned `:falsey`, confirming that false opens the falsey branch. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_16 = SubjectCurriculum(
    grade=2, subject_id="G2-16",
    subject_title="Truthy 0 and empty string",
    fable="boy-wolf",
    examples=[
        _ex("(boolean 0)",   True,  "the expression (boolean 0)",  "the truthiness of 0",
            scenario=(
                "Carol stood at the fold-gate with 0 on the slate. She wanted to "
                "test whether 0 was truthy or falsey by converting it to a boolean."
            ),
            need=(
                "The gate needed to know 0's truthiness. Tom said it looked neutral; "
                "Carol insisted the form would settle if it was truthy."
            ),
            mapping=(
                "`boolean` converts to true or false: 0 is truthy (not nil, not false), "
                "so it returns `true`."
            ),
            resolution=(
                'the call returned `true`, confirming that 0 is truthy. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'
            )),
        _ex("(boolean \"\")", True, "the expression (boolean \"\")", "the truthiness of the empty string",
            scenario=(
                "Carol wrote an empty string on the slate and wanted to convert it "
                "to a boolean to test its truthiness."
            ),
            need=(
                "The gate needed the empty string's truthiness. Tom said it was empty; "
                "Carol insisted the form would settle if it was truthy."
            ),
            mapping=(
                "`boolean` converts: the empty string is truthy (it exists, just with "
                "no characters), so it returns `true`."
            ),
            resolution=(
                'the call returned `true`, confirming that even empty strings are truthy. Tom chalked {drawn.a} on the watchhouse notice, and the morning record stood for the next shepherd to read.'
            )),
        _ex("(boolean nil)", False, "the expression (boolean nil)", "the truthiness of nil",
            scenario=(
                "Carol searched the ledger and found nil (nothing). She converted "
                "nil to a boolean to test its truthiness."
            ),
            need=(
                "The gate needed nil's truthiness. Tom said it was nothing; Carol "
                "insisted the form would settle if it was falsey."
            ),
            mapping=(
                "`boolean` converts: nil is falsey (the absence of a value), so "
                "it returns `false`."
            ),
            resolution=(
                'the call returned `false`, confirming that nil is falsey.'
            )),
        _ex("(boolean false)", False, "the expression (boolean false)", "the truthiness of false",
            scenario=(
                "Carol placed false on the slate and converted it to a boolean to "
                "confirm its truthiness."
            ),
            need=(
                "The gate needed to confirm false's truthiness. Tom said false was "
                "false; Carol insisted the form would settle it explicitly."
            ),
            mapping=(
                "`boolean` converts: false is falsey (by definition), so the form "
                "returns `false`."
            ),
            resolution=(
                'the call returned `false`, confirming that false is falsey.'
            )),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_17 = SubjectCurriculum(
    grade=2, subject_id="G2-17",
    subject_title="Keyword as function for map lookup",
    fable="boy-wolf",
    examples=[
        _ex("(:wolf {:wolf 1 :flock 2})", 1,
            "the expression (:wolf {:wolf 1 :flock 2})",
            "the value (:wolf {:wolf 1 :flock 2}) returns",
            scenario=(
                "Carol's wool-basket sat by the watchhouse. It had two "
                "stitched pouches inside: one labeled `:wolf` holding 1 "
                "fleece from the south pasture, the other `:flock` "
                "holding 2 from the north's morning shearing."
            ),
            need=(
                "Tom needed the count from the wolf-pouch alone. Reaching "
                "in and counting by hand risked spilling the basket; the "
                "village wanted a one-step lookup that named the pouch "
                "and got back its contents."
            ),
            mapping=(
                "A keyword used as a function reaches into the basket "
                "and returns whatever is in the pouch labeled with that "
                "keyword. `:wolf` names the pouch; the basket gives "
                "back the count it holds."
            ),
            resolution=(
                "the lookup returned 1 — the wolf-pouch's fleece count — without disturbing the rest of the basket. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain."       )),
        _ex("(:flock {:wolf 1 :flock 2})", 2,
            "the expression (:flock {:wolf 1 :flock 2})",
            "the value (:flock {:wolf 1 :flock 2}) returns",
            scenario=(
                "Carol's wool-basket held the same two pouches: one for the wolf-fleeces, "
                "one for the flock-fleeces. Tom wanted the count from the flock-pouch."
            ),
            need=(
                "A clean lookup was needed without disturbing the basket. Tom could "
                "reach in and count by hand; Carol insisted the form would find the "
                "flock-pouch's contents exactly."
            ),
            mapping=(
                "The keyword `:flock` is used as a function to reach into the basket. "
                "It finds the pouch labeled `:flock` and returns whatever count sits "
                "inside — here, the count 2."
            ),
            resolution=(
                "the lookup returned 2, the flock-pouch's count, and the basket remained undisturbed. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then."
            )),
        _ex("(:missing {:wolf 1})", None,
            "the expression (:missing {:wolf 1})",
            "the value when a missing keyword is looked up",
            scenario=(
                "Carol's basket held only one pouch, labeled `:wolf` with 1 fleece. "
                "Tom wanted to look for a `:missing` pouch that didn't exist."
            ),
            need=(
                "The village wanted to know what happens when a lookup fails. Tom said "
                "the basket would be empty; Carol insisted the form would settle what "
                "a missing pouch returns."
            ),
            mapping=(
                "When the keyword `:missing` is used to look up a pouch that doesn't "
                "exist, it returns `nil` — the absence of a value — rather than "
                "breaking."
            ),
            resolution=(
                'the lookup returned nil, signaling that the `:missing` pouch held nothing, and the search continued elsewhere. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'
            )),
    ],
    subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_18 = SubjectCurriculum(
    grade=2, subject_id="G2-18",
    subject_title="Quoting symbols",
    fable="boy-wolf",
    examples=[
        _ex("(quote wolf)", "wolf", "the quoted symbol (quote wolf)",
            "the value of (quote wolf)",
            scenario=(
                "Carol drew a chalk mark on the slate and labeled it `wolf`. She "
                "wanted the mark itself — the symbol — not what it named."
            ),
            need=(
                "The village needed the chalk mark as a name, not a direction to "
                "run. Tom said 'wolf' was a word; Carol insisted `quote` would "
                "settle the symbol itself."
            ),
            mapping=(
                "`quote` holds the symbol still and returns it as-is. Without `quote`, "
                "the name `wolf` might be looked up; with `quote`, the mark `wolf` "
                "is returned unchanged."
            ),
            resolution=(
                'the call returned the symbol `wolf`, the chalk mark itself, and the slate held the name.'
            )),
        _ex("'flock", "flock", "the quoted symbol 'flock",
            "the value of 'flock",
            scenario=(
                "Carol wrote the symbol `flock` on the slate using the shorthand "
                "quote mark. She wanted the symbol, not a lookup."
            ),
            need=(
                "The ledger needed the symbol as a label. Tom said 'flock' was clear; "
                "Carol insisted the form would return the symbol itself."
            ),
            mapping=(
                "The apostrophe ' is shorthand for `quote` — it holds the symbol "
                "and returns it. `'flock` is the same as `(quote flock)`."
            ),
            resolution=(
                'the call returned the symbol `flock`, and the slate recorded the name as a mark.'
            )),
        _ex("'(1 2 3)", [1, 2, 3], "the quoted list '(1 2 3)",
            "the value of '(1 2 3)",
            scenario=(
                "Carol sketched a pattern on the slate: three numbers listed together, "
                "(1 2 3). She wanted to keep them as a group without evaluation."
            ),
            need=(
                "The form needed to return the list as-is, not evaluate its contents. "
                "Tom said the numbers were 1, 2, 3; Carol insisted the form would "
                "return the list structure itself."
            ),
            mapping=(
                "`quote` on a list stops evaluation and returns the list structure. "
                "`'(1 2 3)` returns the list containing the three numbers, not the "
                "result of running them."
            ),
            resolution=(
                'the call returned the list [1 2 3], the structure itself, and the slate held the grouped numbers. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'
            )),
    ],
    subplots=_CHALKMARK_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_19 = SubjectCurriculum(
    grade=2, subject_id="G2-19",
    subject_title="Auto-promotion to bigint",
    fable="boy-wolf",
    examples=[
        _ex("(* 1000000 1000000)", 1000000000000,
            "the expression (* 1000000 1000000)",
            "the result of one million times one million",
            scenario=(
                "Carol multiplied one million times one million — a transaction so "
                "large it exceeded the normal counter size. The slate held the operation."
            ),
            need=(
                "The product needed to be exact, even if it overflowed normal number "
                "sizes. Tom said the result would be too large; Carol insisted the form would "
                "handle it."
            ),
            mapping=(
                "`*` multiplies: one million by one million. "
                "When the result exceeds the normal size, the form automatically "
                "promotes to a larger number type, preserving accuracy."
            ),
            resolution=(
                'the call returned the exact answer, using the promoted number size. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'
            )),
        _ex("(+ 99999999999 1)", 100000000000,
            "the expression (+ 99999999999 1)",
            "the result of 99999999999 plus 1",
            scenario=(
                "Carol had a massive tally and gained one more — a "
                "number sitting at the edge of the normal size limit."
            ),
            need=(
                "Adding one would overflow the standard size. Tom said the result "
                "would be too large; Carol insisted the form would hold it exactly."
            ),
            mapping=(
                "`+` adds the values together. When the result "
                "crosses into the larger size, the form automatically promotes to a "
                "bigint, preserving the true sum."
            ),
            resolution=(
                'the call returned the exact total, using the promoted type. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_20 = SubjectCurriculum(
    grade=2, subject_id="G2-20",
    subject_title="Counting",
    fable="boy-wolf",
    examples=[
        _ex("(count [1 2 3])",       3, "the count of [1 2 3]",
            "the count of the vector [1 2 3]",
            scenario=(
                "Carol stood at the fold-gate with her wooden tally-stick "
                "in hand, ready for the morning's pass-through. A small "
                "row of three lambs waited by the post — the south "
                "flock's morning return."
            ),
            need=(
                "The village's morning record needed the count of the "
                "row. Tom offered to estimate; Carol preferred to walk "
                "the line with her stick, notching once per lamb so the "
                "count would settle exactly."
            ),
            mapping=(
                "`count` walks the row and notches the tally-stick once "
                "per item. With three lambs in the row, the stick gains "
                "three notches — the running total grows knot by knot "
                "as the runtime steps through."
            ),
            resolution=(
                "the stick carried 3 notches at the end of the walk — the morning's exact count, ready for the slate. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand."           )),
        _ex("(count \"hello\")",     5, "the count of \"hello\"",
            "the length of the string \"hello\"",
            scenario=(
                "Carol wrote the word 'hello' on the slate and wanted to know how "
                "many characters it held."
            ),
            need=(
                "The character count mattered for the ledger. Tom said five; Carol "
                "insisted the form would walk the string and settle the exact length."
            ),
            mapping=(
                "`count` walks the string bead by bead: h, e, l, l, o — one notch "
                "per character. With five characters, it returns 5."
            ),
            resolution=(
                "the call returned 5, the exact character count, and the string's length was recorded. Tom chalked {drawn.a} on the watchhouse notice, and the morning record stood for the next shepherd to read."
            )),
        _ex("(count [])",            0, "the count of an empty vector",
            "the count of an empty vector",
            scenario=(
                "Carol held an empty row on the slate — no lambs waiting, no items "
                "listed. She wanted to confirm the count of nothing."
            ),
            need=(
                "The empty count mattered for the night tally. Tom said there was "
                "nothing; Carol insisted the form would confirm zero items."
            ),
            mapping=(
                "`count` walks the empty row and finds no items to notch. The "
                "tally-stick gains no marks, so it returns 0."
            ),
            resolution=(
                'the call returned 0, confirming the row was empty, and the evening ledger was settled. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'
            )),
    ],
    subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_21 = SubjectCurriculum(
    grade=2, subject_id="G2-21",
    subject_title="String length and substring",
    fable="boy-wolf",
    examples=[
        _ex("(count \"shepherd\")", 8,  "the length of \"shepherd\"",
            "the length of the string \"shepherd\"",
            scenario=(
                "Carol wrote the word 'shepherd' on the slate as a long bead-string. "
                "She wanted to count every bead in the cord."
            ),
            need=(
                "The string length mattered for labeling in the ledger. Tom said "
                "roughly eight; Carol insisted the form would notch the exact count."
            ),
            mapping=(
                "`count` walks the bead-string: s-h-e-p-h-e-r-d, one notch per bead. "
                "With eight beads, it returns 8."
            ),
            resolution=(
                'the call returned 8, the exact length, and the word was measured. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'
            )),
        _ex("(count \"wolf\")",     4,  "the length of \"wolf\"",
            "the length of the string \"wolf\"",
            scenario=(
                "Carol wrote 'wolf' on the slate and wanted to know its length. "
                "The name appeared shorter than 'shepherd'."
            ),
            need=(
                "The comparison mattered for the record. Tom said four; Carol insisted "
                "it would settle the exact count."
            ),
            mapping=(
                "`count` walks: w-o-l-f, four beads in the cord. The form returns 4."
            ),
            resolution=(
                "the call returned 4, confirming 'wolf' was shorter than 'shepherd'. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement."
            )),
        _ex("(subs \"shepherd\" 0 3)", "she",
            "the expression (subs \"shepherd\" 0 3)",
            "the first three characters of \"shepherd\"",
            scenario=(
                "Carol held the bead-cord 'shepherd' and wanted to cut a piece: "
                "starting from the first bead, taking three beads total."
            ),
            need=(
                "A substring (a cut piece) mattered for the message. Tom said the "
                "first three were 's', 'h', 'e'; Carol insisted the form would splice "
                "the exact substring."
            ),
            mapping=(
                "`subs` cuts the bead-string: starting at position 0 (the first bead), "
                "take 3 beads (s, h, e). The form returns the spliced piece 'she'."
            ),
            resolution=(
                "the call returned 'she', the first-three-character substring, and the piece was tied off. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear."
            )),
    ],
    subplots=_BEADSTRING_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_22 = SubjectCurriculum(
    grade=2, subject_id="G2-22",
    subject_title="Compose pure arithmetic (multi-step calculation)",
    fable="boy-wolf",
    examples=[
        # A simple tally: sheep counted at sundown, minus a few that strayed.
        _ex("(- (* 5 4) 7)", 13,
            "the expression (- (* 5 4) 7)",
            "5 sheep per pen across 4 pens, minus 7 strays",
            scenario=(
                "Carol counted the pens at sundown. Five pens held four sheep each "
                "— a full count. But seven strays had wandered off during the day."
            ),
            need=(
                "The true evening count needed both the full tally and the loss. Tom "
                "guessed a number; Carol insisted the form would settle what the "
                "arithmetic would give."
            ),
            mapping=(
                "The inner `*` multiplies the pens by sheep per pen. The "
                "outer `-` then subtracts the strays from that product."
            ),
            resolution=(
                'the call returned the exact evening tally, and the slate was updated with the true count. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'
            )),
        _ex("(+ (* 3 8) (* 2 4))", 32,
            "the sum of two products",
            "3*8 + 2*4",
            scenario=(
                "Carol tallied two separate shipments: three boxes with eight fleeces "
                "each, plus two bundles with four fleeces each. She wanted the combined total."
            ),
            need=(
                "Two separate products had to be added. Tom started counting on his "
                "fingers; Carol insisted the form would compute both products and sum them."
            ),
            mapping=(
                "The first inner `*` calculates the first product, the second inner `*` yields the second "
                "product, and the outer `+` sums them together."
            ),
            resolution=(
                'the call returned the exact combined total, and the shipment was fully recorded. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
        _ex("(quot (+ 100 50) 5)", 30,
            "the expression (quot (+ 100 50) 5)",
            "150 divided by 5",
            scenario=(
                "Carol had 100 fleeces in the west field and 50 in the east field. "
                "She wanted to divide the combined total equally by 5 buyers."
            ),
            need=(
                "The quotient after summing mattered for the fair price. Tom said "
                "thirty; Carol insisted the form would settle what the combined division was."
            ),
            mapping=(
                "The inner `+` yields 150 (100+50), and the outer `quot` divides "
                "150 by 5, yielding 30."
            ),
            resolution=(
                'the call returned 30, the fair share per buyer, and the sale was settled. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'
            )),
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
    print(f"grade-2 boy-wolf smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
