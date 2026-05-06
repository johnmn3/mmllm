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
        _ex("(+ 1 2 3 4)", 10,
            'four clusters being summed',
            'the running total of four clusters',
            goal='add four single clusters together',
            scenario="Renard the fox marked clusters on his slate in sequence: first one mark, then two, then three, then four. Each mark stood for a cluster gathered.",
            need="Renard wanted the whole day's sum — all four marks' clusters counted as one total.",
            mapping="Adding marks to marks is what addition does: each argument is a mark, and the sum is the total count.",
            resolution="the slate's total stood at the sum of the four marks — exactly the haul Renard had laid in the press.",
            tags=("story",)),
        _ex("(* 2 3 4)", 24,
            'three quantities multiplied together',
            'the product of the three quantities',
            goal='multiply three quantities: 2 trays, 3 clusters per tray, 4 grapes per cluster',
            scenario="Vix the fox had three trays waiting at the market stall. The first held 2 baskets, the second held 3 bundles of clusters, the third held 4 single grapes.",
            need="Vix wanted to know the total count if every basket had bundles and every bundle had grapes — the full product.",
            mapping="Multiplying quantities is what multiplication does: each argument is a quantity, and the product is the combined scaled total.",
            resolution="the tally came to the full product — exactly how many grapes would sit in the press if every container were stacked.",
            tags=("story",)),
        _ex("(- 100 1 2 3)", 94,
            'subtracting three quantities from one hundred',
            'the remainder after three subtractions',
            goal='subtract 1, then 2, then 3 from 100',
            scenario="Sly the fox started the morning with 100 grapes on the slate. After the first sale, 1 grape gone. After the second, 2 more gone. After the third, 3 more gone.",
            need="Sly wanted the count after all three sales settled — the honest remainder on the slate.",
            mapping="Subtracting in chain is what multi-arg subtraction does: start with the first, subtract the second, subtract the third, and the remainder is what's left.",
            resolution="the slate showed the final count — the original minus each sale, one by one.",
            tags=("story",)),
        _ex("(+ 1 2 3 4 5 6 7 8 9 10)", 55,
            'ten clusters summed in order',
            'the total of ten clusters counted once',
            goal='add ten clusters numbered 1 through 10',
            scenario="Renard marked a row on his slate: one mark, then two, then three, stepping through to ten. Each mark held a cluster from the morning's picking.",
            need="Renard wanted the full running total — all ten marks summed as one honest number.",
            mapping="Adding in a chain is what multi-arg addition does: each argument is a count, and the sum is the complete tally.",
            resolution="the slate's final number was the sum of the ten marks — the full morning's haul.",
            tags=("story",)),
        _ex("(* 1 2 3 4 5)", 120,
            'five factors multiplied in sequence',
            'the product of the five factors',
            goal='multiply 1, 2, 3, 4, and 5 together',
            scenario="Vix had five trays stacked in the storehouse, each tray holding a different scale of bundles: the first tray held 1 bundle, the second 2, the third 3, the fourth 4, the fifth 5.",
            need="Vix wanted the total if she combined every bundle from every tray into one count — the full product.",
            mapping="Multiplying factors in a chain is what multi-arg multiplication does: each argument multiplies the running total.",
            resolution="the final count was the product of all five factors — the combined scaled total.",
            tags=("story",)),
        _ex("(+ 10 20 30)", 60,
            'three groups of clusters summed',
            'the total of three groups',
            goal='add three groups: 10 clusters, 20 clusters, 30 clusters',
            scenario="Sly the fox laid out three piles on the slate: the first held 10 clusters, the second 20, the third 30. Each pile came from a different vineyard.",
            need="Sly wanted the combined total — all three piles' clusters as one running count.",
            mapping="Adding groups of clusters is what addition does for larger counts: each argument is a group, and the sum is the total from all groups.",
            resolution="the slate showed the sum of the three groups — the full harvest from all three vineyards.",
            tags=("story",)),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_02 = SubjectCurriculum(
    grade=2, subject_id="G2-02",
    subject_title="Comparison chains",
    fable="fox-grapes",
    examples=[
        _ex("(< 1 2 3)", True,
            'three vine-clusters in strictly increasing order',
            'the verdict on whether the three are in rising order',
            goal='test whether 1 is less than 2 and 2 is less than 3',
            scenario="Renard had three vines marked on a post: the first held 1 cluster, the second held 2, the third held 3. He wanted to check if they grew heavier in order.",
            need="Renard needed to know whether the counts rose from left to right — if the chain was honest.",
            mapping="Comparing in a chain is what less-than does: each pair must satisfy the rule, and only if all pairs do does the verdict come out true.",
            resolution="the chain held true — 1 was less than 2, and 2 was less than 3 — so Renard marked the vines as honestly ordered.",
            tags=("story",)),
        _ex("(< 3 2 1)", False,
            'three vine-clusters in decreasing order',
            'the verdict on whether they are in ascending order',
            goal='test whether 3 is less than 2 and 2 is less than 1',
            scenario="Vix had three vines marked on a post: the first held 3 clusters, the second held 2, the third held 1. She wanted to check if they grew lighter in order from first to last.",
            need="Vix needed to know whether the counts fell from left to right — if the chain was true.",
            mapping="Comparing in a chain is what less-than does: if any pair fails the rule, the whole chain returns false.",
            resolution="the chain failed — 3 was not less than 2 — so Vix marked the vines as out of order.",
            tags=("story",)),
        _ex("(<= 1 1 2)", True,
            'three vine-clusters in non-decreasing order, with a tie',
            'the verdict on whether they are in non-decreasing order',
            goal='test whether 1 is less than or equal to 1, and 1 is less than or equal to 2',
            scenario="Sly had three vines marked: the first held 1 cluster, the second also held 1, the third held 2. He wanted to check if they were in order allowing ties.",
            need="Sly needed to know if the counts went up or stayed level — whether the chain was honestly non-decreasing.",
            mapping="Comparing with less-than-or-equal is what does: each pair must have the rule true, allowing matches where the counts are the same.",
            resolution="the chain held — 1 equaled 1 and 1 was less than 2 — so Sly marked the vines as honestly ordered.",
            tags=("story",)),
        _ex("(> 5 4 3 2 1)", True,
            'five vine-clusters in strictly decreasing order',
            'the verdict on whether they decrease strictly',
            scenario="Renard marked five vines showing clusters: 5, then 4, then 3, then 2, then 1. He wanted to verify they dropped by one each time.",
            need="Renard needed to know if every cluster count was strictly less than the one before it.",
            mapping="Comparing greater-than in a chain means every next value must be less than the current one, and all pairs must satisfy the rule.",
            resolution="the chain held true — each count fell below the previous — so Renard marked the pattern as honestly decreasing.",
            tags=("story",)),
        _ex("(>= 3 3 2)", True,
            'three vine-clusters with a tie at the start, then a drop',
            'the verdict on whether they are in non-increasing order',
            goal='test whether 3 is greater than or equal to 3, and 3 is greater than or equal to 2',
            scenario="Vix had three vines marked: the first held 3 clusters, the second also held 3, the third held 2. She wanted to check if they were in non-increasing order.",
            need="Vix needed to know if the counts went down or stayed level — whether the chain was honestly non-increasing.",
            mapping="Comparing with greater-than-or-equal means each value must be at least as large as the next, allowing ties where the counts match.",
            resolution="the chain held — 3 equaled 3 and 3 was greater than 2 — so Vix marked the vines as honestly ordered.",
            tags=("story",)),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_03 = SubjectCurriculum(
    grade=2, subject_id="G2-03",
    subject_title="not= and = with multiple args",
    fable="fox-grapes",
    examples=[
        _ex("(not= 1 2)", True,
            'two different cluster counts',
            'the verdict on whether the counts differ',
            goal='test whether 1 is not equal to 2',
            scenario="Renard had two vines: one held 1 cluster, the other held 2. He wanted to know if they were different.",
            need="Renard needed to know if the counts differed from each other.",
            mapping="The not-equal predicate asks: are these two values unequal? It returns true when they differ.",
            resolution="the verdict was true — 1 and 2 were not the same — so Renard marked them as different.",
            tags=("story",)),
        _ex("(not= 1 1)", False,
            'two identical cluster counts',
            'the verdict on whether they differ',
            goal='test whether 1 is not equal to 1',
            scenario="Vix had two vines: both held 1 cluster each. She wanted to know if they were different.",
            need="Vix needed to know if the counts matched or differed.",
            mapping="The not-equal predicate returns false when the values are the same.",
            resolution="the verdict was false — both counts were 1 — so Vix marked them as matched.",
            tags=("story",)),
        _ex("(= 1 1 1)", True,
            'three matching cluster counts',
            'the verdict on whether all three are equal',
            goal='test whether 1, 1, and 1 are all equal',
            scenario="Sly had three vines: all three held 1 cluster each. He wanted to verify they matched.",
            need="Sly needed to know if all three counts were the same.",
            mapping="The equality predicate with multiple args asks: are all these values the same? It returns true only when every pair matches.",
            resolution="the verdict was true — all three counts were 1 — so Sly marked them as perfectly matched.",
            tags=("story",)),
        _ex("(= 1 1 2)", False,
            'two matching and one different cluster count',
            'the verdict on whether all three are equal',
            goal='test whether 1, 1, and 2 are all equal',
            scenario="Renard had three vines: the first held 1 cluster, the second also 1, the third held 2. He wanted to check if all three matched.",
            need="Renard needed to know if the three counts were all the same.",
            mapping="The equality predicate returns false if any value differs from the others — the chain breaks.",
            resolution="the verdict was false — the third count differed from the first two — so Renard marked them as unmatched.",
            tags=("story",)),
        _ex("(not= 1 1 2)", True,
            'cluster counts where the third differs from the first two',
            'the verdict on whether not all are equal',
            goal='test whether 1, 1, and 2 are not all equal',
            scenario="Vix had three vines: two held 1 cluster each, the third held 2. She wanted to know if they were not all the same.",
            need="Vix needed to know if at least one count was different from the others.",
            mapping="The not-equal predicate asks: are these values not all equal to each other? It returns true if any pair differs.",
            resolution="the verdict was true — one count was different — so Vix marked them as unmatched.",
            tags=("story",)),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_04 = SubjectCurriculum(
    grade=2, subject_id="G2-04",
    subject_title="min and max",
    fable="fox-grapes",
    examples=[
        _ex("(min 1 2 3)", 1,
            'the smallest of three cluster counts',
            'the minimum count',
            goal='find the smallest of three cluster counts: 1, 2, and 3',
            scenario="Renard had three baskets of grapes: the first held 1 cluster, the second 2, the third 3. He wanted to identify which was the lightest.",
            need="Renard needed to know which basket held the fewest clusters — the minimum haul.",
            mapping="The min operation finds the smallest value among all arguments by comparing them.",
            resolution="the smallest count was identified — 1 — and Renard set aside the lightest basket.",
            tags=("story",)),
        _ex("(max 1 2 3)", 3,
            'the largest of three cluster counts',
            'the maximum count',
            goal='find the largest of three cluster counts: 1, 2, and 3',
            scenario="Vix had three baskets of grapes: the first held 1 cluster, the second 2, the third 3. She wanted to identify which was the heaviest.",
            need="Vix needed to know which basket held the most clusters — the maximum haul.",
            mapping="The max operation finds the largest value among all arguments by comparing them.",
            resolution="the largest count was identified — 3 — and Vix set aside the heaviest basket.",
            tags=("story",)),
        _ex("(min 7 3 9 1 5)", 1,
            'the smallest of five varying cluster counts',
            'the minimum among the five',
            goal='find the smallest of five counts: 7, 3, 9, 1, and 5',
            scenario="Sly had five baskets of grapes with counts 7, 3, 9, 1, and 5. He lined them up on the market-tray and wanted to find the lightest one.",
            need="Sly needed to identify which basket was smallest — the one holding the fewest clusters.",
            mapping="The min operation compares all five values and returns the one that is less than every other.",
            resolution="the minimum was found — 1 — and Sly knew exactly which basket to give away first.",
            tags=("story",)),
        _ex("(max 7 3 9 1 5)", 9,
            'the largest of five varying cluster counts',
            'the maximum among the five',
            goal='find the largest of five counts: 7, 3, 9, 1, and 5',
            scenario="Renard had five baskets of grapes with counts 7, 3, 9, 1, and 5. He lined them up on the market-tray and wanted to find the heaviest one.",
            need="Renard needed to identify which basket was largest — the one holding the most clusters.",
            mapping="The max operation compares all five values and returns the one that is greater than every other.",
            resolution="the maximum was found — 9 — and Renard knew exactly which basket to press first.",
            tags=("story",)),
        _ex("(min -3 -1 -5)", -5,
            'the smallest of three negative cluster amounts',
            'the minimum negative value',
            goal='find the smallest (most negative) of -3, -1, and -5',
            scenario="Vix had three accounts marked on her ledger: one showed 3 grapes owed, one showed 1 owed, one showed 5 owed. She wanted to know which debt was largest.",
            need="Vix needed to find the most negative value — the biggest debt to settle first.",
            mapping="The min operation finds the smallest value even when all are negative — the one furthest from zero in the negative direction.",
            resolution="the minimum was found — 5 in debt — and Vix knew the largest obligation.",
            tags=("story",)),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_05 = SubjectCurriculum(
    grade=2, subject_id="G2-05",
    subject_title="quot, rem, mod",
    fable="fox-grapes",
    examples=[
        _ex("(quot 17 5)", 3,
            'dividing 17 grapes into baskets of 5',
            'how many complete baskets',
            goal='divide 17 grapes into groups of 5 and find how many full groups fit',
            scenario="Renard had 17 grapes and wanted to pack them into baskets holding 5 each. He was counting how many complete baskets he could fill.",
            need="Renard needed to know: how many full baskets of 5 will 17 grapes make?",
            mapping="The quot operation finds how many times the divisor fits completely into the dividend — the quotient, with any remainder ignored.",
            resolution="17 grapes fit into complete baskets of 5 exactly this many times, and Renard marked the count on his slate.",
            tags=("story",)),
        _ex("(rem 17 5)", 2,
            'the leftover grapes after packing into baskets of 5',
            'the remainder after division',
            goal='divide 17 grapes into groups of 5 and find what is left over',
            scenario="Vix had 17 grapes and packed them into baskets holding 5 each. After making complete baskets, she wanted to know how many single grapes remained.",
            need="Vix needed to know: how many grapes are left after filling as many complete baskets as possible?",
            mapping="The rem operation finds what remains after the divisor fits completely into the dividend — the remainder.",
            resolution="after packing complete baskets, this many single grapes were left on the tray, and Vix set them aside.",
            tags=("story",)),
        _ex("(mod 17 5)", 2,
            'the modulo of 17 divided by 5',
            'the remainder by modular arithmetic',
            goal='find the remainder when 17 is divided by 5 using modulo',
            scenario="Sly had 17 grapes and wanted to arrange them in a circular pattern with 5 positions. He computed where the last grape would land in the cycle.",
            need="Sly needed to know: where does the pattern land when counting through 17 by 5s?",
            mapping="The mod operation finds the remainder in cyclic or modular division, the position in the cycle after division.",
            resolution="the remainder placed Sly's final grape at this position in the cycle, and he marked it on the circle.",
            tags=("story",)),
        _ex("(quot 100 7)", 14,
            'dividing 100 grapes into baskets of 7',
            'how many complete baskets',
            goal='divide 100 grapes into groups of 7 and find how many full groups fit',
            scenario="Renard had 100 grapes and wanted to pack them into baskets holding 7 each. He was counting how many complete baskets he could fill.",
            need="Renard needed to know: how many full baskets of 7 will 100 grapes make?",
            mapping="The quot operation counts how many times the divisor fits completely, ignoring any leftover.",
            resolution="100 grapes fit into complete baskets of 7 exactly this many times, and Renard marked the count.",
            tags=("story",)),
        _ex("(rem 100 7)", 2,
            'the leftover grapes after packing 100 into baskets of 7',
            'the remainder after this division',
            goal='divide 100 grapes into groups of 7 and find what is left over',
            scenario="Vix had 100 grapes and packed them into baskets holding 7 each. After making complete baskets, she wanted to know how many remained.",
            need="Vix needed to know: how many grapes are left after filling as many complete baskets of 7 as possible?",
            mapping="The rem operation finds what remains after the complete groups are separated.",
            resolution="after packing complete baskets, this many single grapes were left, and Vix set them aside.",
            tags=("story",)),
        _ex("(mod -7 3)", 2,
            'the modulo of a negative dividend',
            'the remainder in modular arithmetic with negative values',
            goal='find the remainder when -7 is divided by 3 using modulo',
            scenario="Sly had a debt of 7 grapes (marked as negative) and wanted to settle it with payment groups of 3. He computed the final balance by modular rules.",
            need="Sly needed to know: what is the modular remainder when settling a debt of 7 with payments of 3?",
            mapping="The mod operation handles negative values by finding the position in the cycle, adjusting by the modulus as needed.",
            resolution="the modular remainder showed Sly's final balance, and he settled the pattern accordingly.",
            tags=("story",)),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_06 = SubjectCurriculum(
    grade=2, subject_id="G2-06",
    subject_title="inc and dec",
    fable="fox-grapes",
    examples=[
        _ex("(inc 5)", 6,
            'adding 1 to a count of 5',
            'the count after incrementing',
            goal='add one to 5',
            scenario="Renard had 5 clusters on his slate and picked one more grape. He wanted to update the tally.",
            need="Renard needed the new count — the old count plus one more.",
            mapping="The inc operation adds 1 to any value — a single step forward.",
            resolution="the slate now showed one more cluster than before, and Renard marked the updated tally.",
            tags=("story",)),
        _ex("(dec 5)", 4,
            'subtracting 1 from a count of 5',
            'the count after decrementing',
            goal='subtract one from 5',
            scenario="Vix had 5 clusters on her slate and sold one grape. She wanted to update the tally.",
            need="Vix needed the new count — the old count minus one.",
            mapping="The dec operation subtracts 1 from any value — a single step backward.",
            resolution="the slate now showed one fewer cluster, and Vix marked the updated tally.",
            tags=("story",)),
        _ex("(inc 0)", 1,
            'adding 1 to a zero count',
            'the count after incrementing zero',
            goal='add one to 0',
            scenario="Sly had picked no grapes yet (0 on his slate) when he picked one. He wanted to mark the first tally.",
            need="Sly needed the new count — starting from nothing, one grape collected.",
            mapping="The inc operation adds 1 to any value, even when starting from zero.",
            resolution="the slate changed from empty to holding one cluster, and Sly marked the first count.",
            tags=("story",)),
        _ex("(dec 0)", -1,
            'subtracting 1 from a zero count',
            'the count after decrementing zero',
            goal='subtract one from 0',
            scenario="Renard had 0 grapes on his ledger when he owed the market one grape. He wanted to mark the debt.",
            need="Renard needed to show he owed one — a negative count marking obligation.",
            mapping="The dec operation subtracts 1 from any value, even when starting from zero, allowing negative results.",
            resolution="the ledger now showed he owed one grape, and Renard marked the debt.",
            tags=("story",)),
        _ex("(inc -1)", 0,
            'adding 1 to a negative count',
            'the count after incrementing a debt',
            goal='add one to -1',
            scenario="Vix had owed 1 grape (marked as -1 on her ledger) and repaid one. She wanted to update her account.",
            need="Vix needed the new balance — the debt of 1 plus the repayment of 1.",
            mapping="The inc operation adds 1 to any value, even negative ones, moving toward zero.",
            resolution="the ledger now showed zero balance, and Vix marked her account settled.",
            tags=("story",)),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_07 = SubjectCurriculum(
    grade=2, subject_id="G2-07",
    subject_title="Absolute value",
    fable="fox-grapes",
    examples=[
        _ex("(abs 5)", 5,
            'the distance from zero of a positive number',
            'the distance unchanged',
            goal='find the distance from zero for the count 5',
            scenario="Renard had 5 clusters on his slate and wanted to measure their distance from an empty slate.",
            need="Renard needed the absolute distance — how far 5 is from zero.",
            mapping="The abs operation returns the distance from zero, stripping any sign or direction.",
            resolution="the distance was 5 clusters away from zero, and Renard marked it.",
            tags=("story",)),
        _ex("(abs -5)", 5,
            'the distance from zero of a negative number',
            'the absolute distance',
            goal='find the distance from zero for the debt -5',
            scenario="Vix had a debt of 5 grapes (marked as -5 on her ledger) and wanted to know the absolute size of the obligation.",
            need="Vix needed the absolute distance — how far -5 is from zero, ignoring the debt sign.",
            mapping="The abs operation strips the negative sign and returns the magnitude — the distance from zero.",
            resolution="the absolute distance was 5 clusters, the true size of the debt before direction.",
            tags=("story",)),
        _ex("(abs 0)", 0,
            'the distance from zero of zero',
            'the distance of zero',
            goal='find the distance from zero for the value 0',
            scenario="Sly had exactly zero grapes (0 on his slate) and wanted to check its distance from zero.",
            need="Sly needed to know the absolute distance of zero — which is zero itself.",
            mapping="The abs operation returns zero when applied to zero, since zero is zero distance from itself.",
            resolution="the distance was zero, and Sly marked no grapes or debt.",
            tags=("story",)),
        _ex("(abs (- 3 8))", 5,
            'the absolute value of a subtraction result',
            'the distance of the difference',
            goal='subtract 8 from 3, then find the absolute distance from zero',
            scenario="Renard computed on his slate: starting with 3, subtracting 8, which gave him a negative result. He then wanted the absolute distance of that result.",
            need="Renard needed to find the absolute magnitude of the difference — how far the result is from zero, ignoring sign.",
            mapping="The abs operation takes the result of subtraction and returns its distance from zero, stripping any negative.",
            resolution="the absolute distance of the difference was the magnitude, and Renard marked it on his slate.",
            tags=("story",)),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_08 = SubjectCurriculum(
    grade=2, subject_id="G2-08",
    subject_title="Arithmetic on ratios",
    fable="fox-grapes",
    examples=[
        _ex("(+ 1/2 1/4)", "3/4",
            'adding a half portion and a quarter portion',
            'the total as a ratio',
            goal='add one-half and one-quarter',
            scenario="Renard had two portions on his tray: one half of a grape and one quarter of a grape. He wanted the combined portion.",
            need="Renard needed to know the total when fractions are joined — half plus quarter as one ratio.",
            mapping="Adding ratios means finding a common measure and combining the parts — both fractions unite under one denominator.",
            resolution="the two portions joined as three-quarters of a grape, and Renard marked the total.",
            tags=("story",)),
        _ex("(* 2/3 3/4)", "1/2",
            'multiplying two ratio portions together',
            'the product as a ratio',
            goal='multiply two-thirds by three-quarters',
            scenario="Vix had two-thirds of a cluster and wanted to take three-quarters of that portion. She was computing the result.",
            need="Vix needed to know: if I take three-quarters of two-thirds, what ratio is left?",
            mapping="Multiplying ratios means the numerators multiply and the denominators multiply, then simplify.",
            resolution="three-quarters of two-thirds yielded the final ratio, and Vix marked the result.",
            tags=("story",)),
        _ex("(- 1 1/3)", "2/3",
            'subtracting a third portion from a whole',
            'the remainder as a ratio',
            goal='subtract one-third from one whole',
            scenario="Sly had one whole grape and wanted to set aside one-third of it. He was computing what remained.",
            need="Sly needed to know: if I take away one-third, what ratio of the whole is left?",
            mapping="Subtracting a ratio from a whole means expressing the whole as a ratio with the same denominator, then subtracting.",
            resolution="removing one-third from the whole left two-thirds, and Sly marked what remained.",
            tags=("story",)),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_09 = SubjectCurriculum(
    grade=2, subject_id="G2-09",
    subject_title="Floats vs ints (the / operator)",
    fable="fox-grapes",
    examples=[
        _ex("(/ 10 2)", 5,
            'dividing 10 clusters evenly into 2 shares',
            'the whole number count per share',
            goal='divide 10 equally between 2',
            scenario="Renard had 10 clusters and wanted to split them evenly between himself and Vix. He computed each fox's share.",
            need="Renard needed to know: if 10 is divided equally two ways, how much does each get?",
            mapping="Division that results in a whole number yields that integer directly — no remainder needed.",
            resolution="each fox received this many clusters, and Renard marked the equal shares.",
            tags=("story",)),
        _ex("(/ 10 3)", "10/3",
            'dividing 10 clusters among 3 shares with a remainder',
            'the ratio representing the division',
            goal='divide 10 equally among 3',
            scenario="Vix had 10 clusters and wanted to split them equally among three foxes: herself, Renard, and Sly. She found the result wasn't a whole number.",
            need="Vix needed to express the result as a ratio — 10 divided by 3 cannot be a whole number.",
            mapping="Division that doesn't result in a whole number produces a ratio — an exact fractional representation.",
            resolution="the three shares were expressed as a ratio, showing the exact distribution.",
            tags=("story",)),
        _ex("(/ 1.0 2)", 0.5,
            'dividing a decimal value by 2',
            'the decimal result',
            goal='divide 1.0 by 2',
            scenario="Sly had 1.0 cluster (measured in decimal form) and wanted to split it in half. He computed the floating-point result.",
            need="Sly needed to know: what is half of 1.0 in decimal form?",
            mapping="Division with a floating-point dividend produces a floating-point result — the decimal answer.",
            resolution="half of 1.0 was the decimal result, and Sly marked the floating-point share.",
            tags=("story",)),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_10 = SubjectCurriculum(
    grade=2, subject_id="G2-10",
    subject_title="Powers via repeated multiplication",
    fable="fox-grapes",
    examples=[
        _ex("(* 2 2 2)", 8,
            'multiplying 2 by itself three times',
            'the product of three 2s',
            goal='multiply 2 by 2 by 2',
            scenario="Renard had a square tray with 2 rows and 2 columns of grape-baskets, holding 2 grapes each. He wanted the total across all baskets.",
            need="Renard needed to find the total: 2 times 2 times 2 clusters all together.",
            mapping="Repeated multiplication (a power) means multiplying the value by itself the given number of times.",
            resolution="2 multiplied by itself three times yielded the total, and Renard counted all the grapes.",
            tags=("story",)),
        _ex("(* 5 5)", 25,
            'multiplying 5 by itself twice',
            'the square of 5',
            goal='multiply 5 by 5',
            scenario="Vix had a square tray with 5 rows and 5 columns of grape-baskets. She wanted the total number of baskets.",
            need="Vix needed to find the area: 5 times 5 baskets arranged in a square.",
            mapping="Multiplying a value by itself twice is called squaring — the product is the square.",
            resolution="5 times 5 yielded the total baskets in the square tray, and Vix marked the count.",
            tags=("story",)),
        _ex("(* 3 3 3 3)", 81,
            'multiplying 3 by itself four times',
            'the fourth power of 3',
            goal='multiply 3 by 3 by 3 by 3',
            scenario="Sly had four identical cubic trays, each with 3 layers, 3 rows, and 3 columns of grape-baskets. He wanted the total count across all.",
            need="Sly needed to find the total: 3 times 3 times 3 times 3 — every basket in all four cubes.",
            mapping="Repeated multiplication of the same value multiple times produces a power of that value.",
            resolution="3 multiplied by itself four times yielded the grand total, and Sly marked the entire count.",
            tags=("story",)),
        _ex("(* 10 10)", 100,
            'multiplying 10 by itself twice',
            'the square of 10',
            goal='multiply 10 by 10',
            scenario="Renard had a large square market-tray with 10 rows and 10 columns of grape-slots. He wanted the total number of slots.",
            need="Renard needed to find the area: 10 times 10 slots arranged in a large square.",
            mapping="Multiplying 10 by itself produces a power — here, the product is 100.",
            resolution="10 times 10 yielded the total slots in the square tray, a perfect hundred.",
            tags=("story",)),
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
        _ex('(str 1 "+" 2 "=" 3)',
            "1+2=3",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox laid out cords of lettered beads on the market-fox's counting-table, ready to be threaded or sliced.",
            need="Vix wanted the form's transformation applied to the cord — joined, sliced, or counted as the form said.",
            mapping='Strings in Clojure are cords of beads: joining ties cords end-to-end; slicing cuts a section; counting returns the bead-total.',
            resolution='the cord came back transformed as the form had directed — joined, sliced, or counted as asked.',
            tags=("story",)),
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
            'a form that prints a greeting and returns nothing',
            'the return value: nil',
            goal='print the word "hello" to the screen and evaluate to nothing',
            scenario="Renard wanted to send a message to the ledger that the REPL would display, but the form itself should return nil — a message with no value.",
            need="Renard needed a form that prints to the reader but doesn't hold a value.",
            mapping="The println form sends text to the screen (a side effect) but returns nil — its value is nothing.",
            resolution="the message appeared on the page, and the form's return was nil, exactly as intended.",
            tags=("story",)),
        _ex('(print "x")', None,
            'a form that prints a single character and returns nothing',
            'the return value: nil',
            goal='print the character "x" to the screen and evaluate to nothing',
            scenario="Vix wanted to mark a single letter on the ledger output without leaving a value behind — just the printed letter.",
            need="Vix needed a form that writes one character but returns nil.",
            mapping="The print form sends text to the screen without a newline, but like println, returns nil — no value held.",
            resolution="the character appeared on the page, and the form's return was nil, leaving only the side effect.",
            tags=("story",)),
    ],
    subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_13 = SubjectCurriculum(
    grade=2, subject_id="G2-13",
    subject_title="and / or — short circuit, return values",
    fable="fox-grapes",
    examples=[
        _ex("(and true true)", True, 'the form', 'the value the form evaluates to'),
        _ex("(and true false)", False, 'the form', 'the value the form evaluates to'),
        _ex("(or false true)", True, 'the form', 'the value the form evaluates to'),
        _ex("(or false false)", False, 'the form', 'the value the form evaluates to'),
        _ex("(and 1 2 3)", 3, 'the form', 'the value the form evaluates to'),
        _ex("(or nil false 5)", 5, 'the form', 'the value the form evaluates to'),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_14 = SubjectCurriculum(
    grade=2, subject_id="G2-14",
    subject_title="not — turning truthy to false",
    fable="fox-grapes",
    examples=[
        _ex("(not true)", False, 'the form', 'the value the form evaluates to'),
        _ex("(not false)", True, 'the form', 'the value the form evaluates to'),
        _ex("(not nil)", True, 'the form', 'the value the form evaluates to'),
        _ex("(not 0)", False, 'the form', 'the value the form evaluates to'),
        _ex("(not \"\")", False, 'the form', 'the value the form evaluates to'),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_15 = SubjectCurriculum(
    grade=2, subject_id="G2-15",
    subject_title="Falsey values: only false and nil",
    fable="fox-grapes",
    examples=[
        _ex("(if 0 :truthy :falsey)", ":truthy", 'the form', 'the value the form evaluates to'),
        _ex("(if \"\" :truthy :falsey)", ":truthy", 'the form', 'the value the form evaluates to'),
        _ex("(if nil :truthy :falsey)", ":falsey", 'the form', 'the value the form evaluates to'),
        _ex("(if false :truthy :falsey)", ":falsey", 'the form', 'the value the form evaluates to'),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_16 = SubjectCurriculum(
    grade=2, subject_id="G2-16",
    subject_title="Truthy 0 and empty string",
    fable="fox-grapes",
    examples=[
        _ex("(boolean 0)", True, 'the form', 'the value the form evaluates to'),
        _ex("(boolean \"\")", True, 'the form', 'the value the form evaluates to'),
        _ex("(boolean nil)", False, 'the form', 'the value the form evaluates to'),
        _ex("(boolean false)", False, 'the form', 'the value the form evaluates to'),
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
        _ex("(:grapes {:fox 1 :grapes 2})", 2, 'the form', 'the value the form evaluates to'),
        _ex("(:missing {:fox 1})", None, 'the form', 'the value the form evaluates to'),
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
        _ex("'(1 2 3)", [1, 2, 3], 'the form', 'the value the form evaluates to'),
    ],
    subplots=_CHALKMARK_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_19 = SubjectCurriculum(
    grade=2, subject_id="G2-19",
    subject_title="Auto-promotion to bigint",
    fable="fox-grapes",
    examples=[
        _ex("(* 1000000 1000000)", 1000000000000, 'the form', 'the value the form evaluates to'),
        _ex("(+ 99999999999 1)", 100000000000, 'the form', 'the value the form evaluates to'),
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
        _ex("(count \"hello\")",
            5,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox walked the vine-row with a slate, ticking off each cluster as her passed it.',
            need="Vix wanted the row's length or running total — a single honest number when the walk ended.",
            mapping='`reduce` and `count` are the tally-walk: visit each item once, tick or accumulate, return the final total.',
            resolution="the slate at the row's end held the honest tally — exactly what the walk had produced.",
            tags=("story",)),
        _ex("(count [])", 0, 'the form', 'the value the form evaluates to'),
    ],
    subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_21 = SubjectCurriculum(
    grade=2, subject_id="G2-21",
    subject_title="String length and substring",
    fable="fox-grapes",
    examples=[
        _ex("(count \"grapes\")",
            6,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox laid out cords of lettered beads on the market-fox's counting-table, ready to be threaded or sliced.",
            need="Renard wanted the form's transformation applied to the cord — joined, sliced, or counted as the form said.",
            mapping='Strings in Clojure are cords of beads: joining ties cords end-to-end; slicing cuts a section; counting returns the bead-total.',
            resolution='the cord came back transformed as the form had directed — joined, sliced, or counted as asked.',
            tags=("story",)),
        _ex("(count \"fox\")",
            3,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox laid out cords of lettered beads on the market-fox's counting-table, ready to be threaded or sliced.",
            need="Vix wanted the form's transformation applied to the cord — joined, sliced, or counted as the form said.",
            mapping='Strings in Clojure are cords of beads: joining ties cords end-to-end; slicing cuts a section; counting returns the bead-total.',
            resolution='the cord came back transformed as the form had directed — joined, sliced, or counted as asked.',
            tags=("story",)),
        _ex("(subs \"grapes\" 0 3)",
            "gra",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox laid out cords of lettered beads on the market-fox's counting-table, ready to be threaded or sliced.",
            need="Sly wanted the form's transformation applied to the cord — joined, sliced, or counted as the form said.",
            mapping='Strings in Clojure are cords of beads: joining ties cords end-to-end; slicing cuts a section; counting returns the bead-total.',
            resolution='the cord came back transformed as the form had directed — joined, sliced, or counted as asked.',
            tags=("story",)),
    ],
    subplots=_BEADSTRING_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_22 = SubjectCurriculum(
    grade=2, subject_id="G2-22",
    subject_title="Compose pure arithmetic (multi-step calculation)",
    fable="fox-grapes",
    examples=[
        # A simple reach: jumps × height per jump, then minus a shortfall.
        _ex("(- (* 5 4) 7)", 13, 'the form', 'the value the form evaluates to'),
        _ex("(+ (* 3 8) (* 2 4))", 32, 'the form', 'the value the form evaluates to'),
        _ex("(quot (+ 100 50) 5)", 30, 'the form', 'the value the form evaluates to'),
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
