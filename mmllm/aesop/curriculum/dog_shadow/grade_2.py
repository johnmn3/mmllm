"""Grade 2 — operators + arithmetic mastery, taught through dog-shadow.

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
from mmllm.aesop.curriculum.dog_shadow.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SHARED_SUBPLOTS,
    _GOAL_SUBPLOTS,
    _PLAN_POOL,
)
from mmllm.aesop.curriculum.dog_shadow._metaphor_pools import (
    _ACORN_SUBPLOTS, _BASKET_SUBPLOTS, _BEADSTRING_SUBPLOTS, _CHALKMARK_SUBPLOTS, _GATE_SUBPLOTS, _SCRIBE_SUBPLOTS, _TALLYWALK_SUBPLOTS,
)


# Extend grade-1's shared pool with two grade-2-specific subplots
# that lean into multi-operand / chained-operator framings.
_SHARED_SUBPLOTS: list[SubplotTemplate] = list(_G1_SHARED_SUBPLOTS) + [
    # 9. The chain-of-operations template — useful for multi-arg
    #    arithmetic and comparison-chain subjects.
    SubplotTemplate("""\
{tortoise}, {emo_patient} had been laying out a chain of small computations on
a slate {place} — one operation, then another, all to settle a
question {hare_phrase} had raised. The current form on the slate was
{form_display}, and {tortoise} explained that {concept_phrase} would
be settled the moment the form was evaluated."""),

    # 10. The wager-with-stakes template — increases the dramatic stakes
    #     when the form is more interesting (e.g., min/max, mod).
    SubplotTemplate("""\
"Whatever {form_display} comes to," {hare} declared, {emo_proud},
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
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(+ 1 2 3 4)", expected=10,
            concept_phrase="the multi-arg sum",
            question_what="the sum of four drawn counts",
            goal_text="add four drawn counts together",
            scenario=(
                "Rex the hound stood at the stream's edge, arranging four "
                "small bones in a row on a flat stone. The bones were marked "
                "{drawn.a}, {drawn.b}, {drawn.c}, and {drawn.d}."
            ),
            need=(
                'He needed the running total — what all {drawn.d} bones counted to when stacked together. The REPL would tally them for him in one breath.'
            ),
            mapping=(
                "Each bone is one operand, their sum is the result, and `+` "
                "is the paw-stroke that gathers them all into one count."
            ),
            resolution=(
                "The REPL added {drawn.a} and {drawn.b}, then {drawn.c}, "
                "then {drawn.d}. The total came back, the wager settled at "
                "once."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 2 3 4)", expected=24,
            concept_phrase="the multi-arg product",
            question_what="the product of three drawn counts",
            goal_text="multiply three drawn counts",
            scenario=(
                'Patch the hound gathered {drawn.b} piles of bones near the meadow, each pile marked with a count: {drawn.a}, {drawn.b}, and {drawn.c}.'
            ),
            need=(
                "They wanted the total if each pile was multiplied together — "
                "what {drawn.a} times {drawn.b} times {drawn.c} would come to "
                "in one compounded count."
            ),
            mapping=(
                "Each pile is one factor, `*` chains them, and the running "
                "product grows at each step until the final answer holds them "
                "all."
            ),
            resolution=(
                "The REPL multiplied {drawn.a} by {drawn.b}, then by "
                "{drawn.c}. The compounded total came back exactly."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(- 100 1 2 3)", expected=94,
            concept_phrase="the multi-arg subtraction",
            question_what="a starting count minus three drawn losses",
            goal_text="subtract three drawn losses from a starting count",
            scenario=(
                "Bell the hound held a great pile of {drawn.a} bones by the "
                "river bank. Then came three separate losses — first "
                "{drawn.b}, then {drawn.c}, then {drawn.d} bones taken away "
                "in turn."
            ),
            need=(
                "She wanted to know how many remained after each subtraction. "
                "The chain of losses would leave a final count that told the "
                "story."
            ),
            mapping=(
                "{drawn.a} is the starting pile, each subtraction removes a "
                "portion, and the running remainder shrinks with each step "
                "until the answer settles."
            ),
            resolution=(
                "The REPL subtracted {drawn.b} from {drawn.a}, then "
                "{drawn.c} more, then {drawn.d} more. The final tally was "
                "returned exactly."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(+ 1 2 3 4 5 6 7 8 9 10)", expected=55,
            concept_phrase="the sum of ten counts",
            question_what="the sum of ten counts gathered along the stream",
            goal_text="add ten counts together",
            scenario=(
                "Rex the hound laid ten marked stones in a line at the stream's "
                "edge: {drawn.a}, {drawn.b}, {drawn.c}, {drawn.d}, {drawn.e}, "
                "{drawn.f}, {drawn.g}, {drawn.h}, {drawn.i}, and {drawn.j}. "
                "He wanted one tally for all of them."
            ),
            need=(
                "He needed the running total when each stone's count was folded "
                "into the next — the sum that would settle the whole row."
            ),
            mapping=(
                "Each stone is one operand, `+` folds them in left to right, and "
                "the final sum holds the answer the row had been waiting for."
            ),
            resolution=(
                "The REPL added the ten in order — folding {drawn.a} and "
                "{drawn.b} and on through {drawn.j} — and handed back the "
                "running total exactly."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 1 2 3 4 5)", expected=120,
            concept_phrase="the multi-arg product",
            question_what="the product of five drawn counts",
            goal_text="multiply five counts together",
            scenario=(
                'Patch the hound laid {drawn.e} bones in a row near the forest, each one carved with a count: {drawn.a}, {drawn.b}, {drawn.c}, {drawn.d}, and {drawn.e}. They wanted the chain multiplied to a single product.'
            ),
            need=(
                'They needed the product when all five were multiplied in sequence. '
                'The running total would grow with each multiplication until the '
                'final answer held the compounded count.'
            ),
            mapping=(
                'Each bone is one factor in the chain, the multiplication links them '
                'together, and the final product grows until it settles on the answer.'
            ),
            resolution=(
                "The REPL chained the multiplication: {drawn.a} times "
                "{drawn.b}, then by {drawn.c}, then by {drawn.d}, then by "
                "{drawn.e}. The compounded product came back exactly."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(+ 10 20 30)", expected=60,
            concept_phrase="the sum of three counts",
            question_what="the sum of three drawn counts",
            goal_text="add three drawn counts",
            scenario=(
                'Bell the hound carried the bundles of bones to the pond: the first held {drawn.a}, the second {drawn.b}, the third {drawn.c}. She wanted them stacked into one count.'
            ),
            need=(
                'She needed the total when the the bundles joined — the running sum that would settle the grand tally without confusion.'
            ),
            mapping=(
                "Each bundle is one addend, `+` folds them in turn, and the "
                "final sum holds the answer for all three together."
            ),
            resolution=(
                "The REPL added {drawn.a} and {drawn.b}, then folded in "
                "{drawn.c}. The total came back exact."
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_02 = SubjectCurriculum(
    grade=2, subject_id="G2-02",
    subject_title="Comparison chains",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(< 1 2 3)", expected=True,
            concept_phrase="the less-than chain",
            question_what="whether 1 < 2 < 3",
            goal_text="test whether 1 is less than 2 and 2 is less than 3",
            scenario=(
                'Bell the hound laid three smooth pebbles near the pond, each '
                'one marked with a number: 1, then 2, then 3. The sizes of '
                'the pebbles did not matter — only their marks.'
            ),
            need=(
                'She needed to know if the marks form a chain where each one '
                'was strictly smaller than the next. The verdict would tell '
                'whether the pattern held all the way across.'
            ),
            mapping=(
                'Each pebble is one value in the chain, the less-than operator '
                'is the test of order, and the verdict passes only if every '
                'comparison returns true.'
            ),
            resolution=(
                'The REPL tested each pair in turn — was 1 less than 2? Yes. '
                'Was 2 less than 3? Yes. The chain held fast, and the 3 '
                'came back true.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(< 3 2 1)", expected=False,
            concept_phrase="the less-than chain",
            question_what="whether 3 < 2 < 1",
            goal_text="test whether 3 is less than 2 and 2 is less than 1",
            scenario=(
                'Rex the hound laid three marked pebbles in a line by the river '
                'bank — 3, then 2, then 1. He wanted to test if each was smaller '
                'than the one before it.'
            ),
            need=(
                'He needed to know if the chain held — if each pebble\'s mark was '
                'strictly less than the mark before it. The verdict would settle '
                'whether the pattern reversed.'
            ),
            mapping=(
                'The pebbles are the values in the chain, the less-than operator '
                'tests each pair, and the verdict returns true only if every link '
                'holds.'
            ),
            resolution=(
                'The REPL tested if 3 is less than 2 — it is not. The chain broke '
                'at the first link, and false was handed back. The marks did not '
                'decrease — 1.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(<= 1 1 2)", expected=True,
            concept_phrase="the less-than-or-equal chain",
            question_what="whether 1 ≤ 1 ≤ 2",
            goal_text="test whether 1 is less than or equal to 1 and 1 is less than or equal to 2",
            scenario=(
                'Patch the hound placed the stones near the meadow, each carved: 1, then 1 again, then 2. They wanted to know if the marks formed a non-strict chain — each equal or less than the next.'
            ),
            need=(
                'They needed to test whether each stone\'s mark was less than or '
                'equal to the one that followed it. The verdict would show if the '
                'gentle slope held all the way.'
            ),
            mapping=(
                'The stones are the values, the less-than-or-equal operator tests '
                'each pair allowing equality, and the verdict is true when every '
                'link permits passage.'
            ),
            resolution=(
                'The REPL tested 1 ≤ 1, which is true, then 1 ≤ 2, which is also '
                'true. The chain held with the gentle slope, and true was returned. '
                'The pattern was settled — 2.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(> 5 4 3 2 1)", expected=True,
            concept_phrase="the greater-than chain",
            question_what="whether the numbers are strictly decreasing",
            goal_text="test whether 5 > 4 > 3 > 2 > 1",
            scenario=(
                'Bell the hound arranged five marked stones in a row at the stream\'s '
                'edge — 5, 4, 3, 2, and 1 — in strict descent. She wanted to test '
                'if they formed a perfect downward chain.'
            ),
            need=(
                'She needed to know if each mark was strictly greater than the next. '
                'The verdict would confirm whether the descent was unbroken and '
                'exact all the way across.'
            ),
            mapping=(
                'Each stone is one value in the chain, the greater-than operator '
                'tests each pair, and true returns only when every link is strictly '
                'greater.'
            ),
            resolution=(
                'The REPL tested 5 > 4, 4 > 3, 3 > 2, and 2 > 1 — all passed. The '
                'perfect descent held, and true was returned. Every step went down as '
                'expected — 1.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(>= 3 3 2)", expected=True,
            concept_phrase="the greater-than-or-equal chain",
            question_what="whether 3 ≥ 3 ≥ 2",
            goal_text="test whether 3 is greater than or equal to 3 and 3 is greater than or equal to 2",
            scenario=(
                'Rex the hound laid three pebbles near the forest — 3, then 3 '
                'again, then 2. He wanted to test a gentle downward chain that '
                'allowed the marks to hold steady or drop.'
            ),
            need=(
                'He needed to know if the marks formed a non-strict descent — each '
                'greater than or equal to the next. The verdict would show whether '
                'the soft slope held.'
            ),
            mapping=(
                'The pebbles are the values, the greater-than-or-equal operator '
                'tests each pair with equality allowed, and true returns when every '
                'link permits the soft descent.'
            ),
            resolution=(
                'The REPL tested 3 ≥ 3, which held, then 3 ≥ 2, which also held. '
                'The gentle chain remained true throughout, and the 2 was '
                'returned.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_03 = SubjectCurriculum(
    grade=2, subject_id="G2-03",
    subject_title="not= and = with multiple args",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(not= 1 2)", expected=True,
            concept_phrase="the inequality check",
            question_what="whether 1 differs from 2",
            goal_text="test whether 1 and 2 are not equal",
            scenario=(
                "Patch the hound held two bones at the stream's edge — one carved with the mark 1, the other with the mark 2. They looked like bones from different catches."
            ),
            need=(
                'They wondered whether the marks were truly different. The '
                'inequality test would settle whether these two were '
                'mismatched.'
            ),
            mapping=(
                'Each bone is one value, the not= operator checks whether they '
                'are distinct, and a true verdict means the marks do not match.'
            ),
            resolution=(
                'The REPL compared the marks — 1 is not equal to 2 — and '
                'handed back true. The bones were indeed different, and the '
                'question was answered — 2.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(not= 1 1)", expected=False,
            concept_phrase="the inequality check",
            question_what="whether 1 differs from itself",
            goal_text="test whether 1 and 1 are not equal",
            scenario=(
                'Patch the hound held two bones carved with the same mark — 1 and '
                '1. They wanted to test if the marks were different from each other.'
            ),
            need=(
                'They needed to know if the two marks were distinct. The inequality '
                'test would settle whether they matched or differed.'
            ),
            mapping=(
                'Each bone is one value, the not= operator checks if they differ, '
                'and the verdict is false when the marks are the same.'
            ),
            resolution=(
                'The REPL compared the marks — 1 is equal to 1 — and returned false. '
                'The bones bore identical marks, so they were not different — 1.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(= 1 1 1)", expected=True,
            concept_phrase="the equality check",
            question_what="whether all three are equal",
            goal_text="test whether 1, 1, and 1 are all equal",
            scenario=(
                'Bell the hound gathered the bones near the pond, each carved with the same mark: 1. She wanted to test if all three matched each other.'
            ),
            need=(
                'She needed to know if all three marks were identical. The equality '
                'test would confirm whether they held the same value without '
                'variation.'
            ),
            mapping=(
                'Each bone is one value being checked, the equality operator tests '
                'all pairs, and the verdict is true only when every mark matches.'
            ),
            resolution=(
                'The REPL compared all three — 1 equals 1 equals 1 — and returned '
                'true. All three marks were identical, and the 1 was certain.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(= 1 1 2)", expected=False,
            concept_phrase="the equality check",
            question_what="whether all three are equal",
            goal_text="test whether 1, 1, and 2 are all equal",
            scenario=(
                'Rex the hound held the bones by the river bank — two marked with 1 and one marked with 2. He wanted to test if they all matched.'
            ),
            need=(
                'He needed to know if all three matched or if one broke the pattern. '
                'The equality test would return true only if every mark was the same.'
            ),
            mapping=(
                'Each bone is one value, the equality operator checks all pairs, and '
                'the verdict requires every mark to match for true to hold.'
            ),
            resolution=(
                'The REPL compared the marks — 1 equals 1, but 1 does not equal 2. '
                'The chain broke, and false was returned. Not all were the same — 2.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(not= 1 1 2)", expected=True,
            concept_phrase="the inequality check",
            question_what="whether at least one differs",
            goal_text="test whether at least one of 1, 1, and 2 is not equal to the others",
            scenario=(
                'Patch the hound held the bones near the meadow — two marked 1 and one marked 2. They wanted to test if at least one differed from the rest.'
            ),
            need=(
                'They needed to know if any mark stood apart from the others. The '
                'inequality test would return true if any mismatch existed.'
            ),
            mapping=(
                'Each bone is one value, the not= operator checks for differences, '
                'and true returns when at least one mark differs from another.'
            ),
            resolution=(
                'The REPL compared the marks — two are 1, but one is 2. The '
                'difference was found, and true was returned. The mismatch was clear — 2.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_04 = SubjectCurriculum(
    grade=2, subject_id="G2-04",
    subject_title="min and max",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(min 1 2 3)",
            expected=1,
            concept_phrase="the minimum of three numbers",
            question_what="the smallest of 1, 2, and 3",
            goal_text="find the minimum of 1, 2, and 3",
            scenario=(
                'Bell the hound laid three marked stones by the river bank — '
                'one labeled 1, one 2, one 3. They seemed almost the same '
                'size, but the marks told the story.'
            ),
            need=(
                'She wanted to know which mark was the smallest — which bone '
                'would come back if the REPL were asked to pick the least one '
                'from the three.'
            ),
            mapping=(
                'Each stone is one value being compared, the minimum '
                'operation is the scan that finds the least among them, and '
                'the answer is the winning mark.'
            ),
            resolution=(
                'The REPL scanned all three — 1, 2, 3 — and returned 1. The '
                'smallest had been found, and the 3 rested in Bell\'s paw.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(max 1 2 3)", expected=3,
            concept_phrase="the maximum of three numbers",
            question_what="the largest of 1, 2, and 3",
            goal_text="find the maximum of 1, 2, and 3",
            scenario=(
                'Rex the hound laid three marked pebbles at the stream\'s edge — one '
                'labeled 1, one 2, one 3. He wanted to pick out the largest mark from '
                'the group.'
            ),
            need=(
                'He needed to know which pebble held the greatest mark — the one that '
                'would be chosen if the REPL had to pick the maximum.'
            ),
            mapping=(
                'Each pebble is one value being compared, the maximum operation scans '
                'for the greatest, and the answer is the winning mark.'
            ),
            resolution=(
                'The REPL scanned all three — 1, 2, 3 — and returned 3. The largest '
                'had been found, and the 3 rested clear.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(min 7 3 9 1 5)", expected=1,
            concept_phrase="the minimum of five numbers",
            question_what="the smallest of 7, 3, 9, 1, and 5",
            goal_text="find the minimum of 7, 3, 9, 1, and 5",
            scenario=(
                'Patch the hound gathered five marked stones near the meadow — 7, 3, '
                '9, 1, and 5 — scattered in no particular order. They wanted the one '
                'with the smallest mark.'
            ),
            need=(
                'They needed to know which stone held the least value. The minimum '
                'operation would scan all five and return the tiniest mark.'
            ),
            mapping=(
                'Each stone is one value in the group, the minimum operation finds '
                'the least, and the answer is the smallest mark.'
            ),
            resolution=(
                'The REPL scanned all five and found that 1 was the least. The '
                'smallest had been identified, and the 5 was handed back with '
                'certainty.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(max 7 3 9 1 5)", expected=9,
            concept_phrase="the maximum of five numbers",
            question_what="the largest of 7, 3, 9, 1, and 5",
            goal_text="find the maximum of 7, 3, 9, 1, and 5",
            scenario=(
                'Bell the hound held five pebbles by the river bank — marked 7, 3, 9, '
                '1, and 5 — mixed together without order. She wanted to find the one '
                'with the greatest mark.'
            ),
            need=(
                'She needed the pebble with the highest value — the maximum among all '
                'five. The scan would settle which held the grandest mark.'
            ),
            mapping=(
                'Each pebble is one value, the maximum operation searches for the '
                'greatest, and the answer is the largest mark.'
            ),
            resolution=(
                'The REPL scanned all five and found 9 was the greatest. The maximum '
                'had been located, and the 5 came back clear and certain.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(min -3 -1 -5)", expected=-5,
            concept_phrase="the minimum of three numbers",
            question_what="the smallest of -3, -1, and -5",
            goal_text="find the minimum of -3, -1, and -5",
            scenario=(
                'Rex the hound held the stones at the pond, each carved with a negative mark: -3, -1, and -5. He wanted the one with the least value — the most negative.'
            ),
            need=(
                'He needed to know which held the smallest value — the most deeply '
                'negative mark among the three. The minimum would settle it.'
            ),
            mapping=(
                'Each stone is one negative value, the minimum operation finds the '
                'least, and the answer is the mark that reaches deepest.'
            ),
            resolution=(
                'The REPL scanned the three negatives — -3, -1, -5 — and returned -5. '
                'It was the smallest, and the -5 was clear.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_05 = SubjectCurriculum(
    grade=2, subject_id="G2-05",
    subject_title="quot, rem, mod",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(quot 17 5)", expected=3,
            concept_phrase="the integer quotient",
            question_what="17 divided by 5, without remainder",
            goal_text="find the integer quotient of 17 divided by 5",
            scenario=(
                'Rex the hound gathered seventeen bones in a pile at the pond '
                'and marked a line in the sand. He wanted to share them into '
                'groups of five, no splits.'
            ),
            need=(
                'He needed to know how many whole groups of five he could make '
                'from the seventeen — the integer count of groups without '
                'worrying about strays left over.'
            ),
            mapping=(
                'The pile of seventeen bones is the dividend, five is the '
                'divisor, the integer quotient is the number of complete '
                'groups, and any remainder is dropped.'
            ),
            resolution=(
                'The REPL divided seventeen by five and handed back 3 — three '
                'whole groups, with two bones left over that didn\'t matter '
                'for the quotient — 5.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(rem 17 5)", expected=2,
            concept_phrase="the remainder",
            question_what="the remainder when 17 is divided by 5",
            goal_text="find the remainder when 17 is divided by 5",
            scenario=(
                'Patch the hound held seventeen bones by the meadow and wanted to '
                'share them into groups of five. Some bones would be left over — '
                'strays that did not fill a complete group.'
            ),
            need=(
                'They wanted to know how many bones remained after making as many '
                'complete groups as possible. The leftover count was the remainder.'
            ),
            mapping=(
                'Seventeen is the total, five is the size of each group, the complete '
                'groups do not matter for the remainder, and the leftover is what '
                'stays.'
            ),
            resolution=(
                'The REPL divided and found three complete groups with two bones left '
                'over. The remainder of 2 was handed back and held the 5.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(mod 17 5)", expected=2,
            concept_phrase="the modulo operation",
            question_what="17 mod 5",
            goal_text="find 17 modulo 5",
            scenario=(
                'Bell the hound gathered seventeen pebbles at the stream\'s edge and '
                'wanted to know what was left after grouping them by fives. The modulo '
                'operation would tell her the remainder.'
            ),
            need=(
                'She needed the leftover count — how many pebbles did not fit into a '
                'group of five. The modulo would settle this without showing the '
                'groups themselves.'
            ),
            mapping=(
                'Seventeen is the dividend, five is the divisor, the modulo operation '
                'returns only the remainder, and the answer is what\'s left over.'
            ),
            resolution=(
                'The REPL applied modulo to seventeen and five, and returned 2. The '
                'remainder was exact, and the 5 held what did not fit.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(quot 100 7)", expected=14,
            concept_phrase="the integer quotient",
            question_what="100 divided by 7, without remainder",
            goal_text="find the integer quotient of 100 divided by 7",
            scenario=(
                'Rex the hound held one hundred bones and wanted to divide them evenly '
                'into groups of seven. He cared only about how many complete groups he '
                'could make, not what was left.'
            ),
            need=(
                'He needed to know how many whole groups of seven he could form. The '
                'integer quotient would give him that count without the strays.'
            ),
            mapping=(
                'One hundred is the dividend, seven is the divisor, the quotient is '
                'the number of complete groups, and remainder is ignored.'
            ),
            resolution=(
                'The REPL divided one hundred by seven and returned 14 — fourteen '
                'complete groups. The quotient was exact, and the remainder did not '
                'matter — 7.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(rem 100 7)", expected=2,
            concept_phrase="the remainder",
            question_what="the remainder when 100 is divided by 7",
            goal_text="find the remainder when 100 is divided by 7",
            scenario=(
                'Patch the hound had one hundred bones and wanted to see how many '
                'strays would be left after making groups of seven. The remainder was '
                'what mattered most to them.'
            ),
            need=(
                'They needed to know how many bones did not fit into a complete group. '
                'The remainder operation would return exactly that count.'
            ),
            mapping=(
                'One hundred is the total pile, seven is the group size, the complete '
                'groups are not returned, and only the leftover is the answer.'
            ),
            resolution=(
                'The REPL divided and found that 100 divided by 7 left a remainder of '
                '2. The leftover count was returned and held the final answer — 7.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(mod -7 3)", expected=2,
            concept_phrase="the modulo operation",
            question_what="negative seven mod 3",
            goal_text="find negative 7 modulo 3",
            scenario=(
                'Bell the hound stood by the river bank holding a negative value — '
                'negative seven — and wanted to find its modulo against three. '
                'Negative numbers in modulo work in their own way.'
            ),
            need=(
                'She needed to know what remained when a negative value was taken '
                'modulo a positive divisor. The modulo would settle this without '
                'confusion about the sign.'
            ),
            mapping=(
                'Negative 7 is the dividend, 3 is the divisor, the modulo operation '
                'returns the remainder adjusted for the modulo, and the answer follows '
                'the rules of modular arithmetic.'
            ),
            resolution=(
                'The REPL applied modulo to negative 7 and 3, and returned 2. The '
                'result followed modular arithmetic rules, and the 3 was certain.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_06 = SubjectCurriculum(
    grade=2, subject_id="G2-06",
    subject_title="inc and dec",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(inc 5)", expected=6,
            concept_phrase="the increment operation",
            question_what="5 plus 1",
            goal_text="increment 5 by 1",
            scenario=(
                "Patch the hound stood at the stream's edge holding five marked pebbles in a line. A sixth pebble sat just beyond the row, waiting to be counted in."
            ),
            need=(
                'They wanted to know what came next — what the running total '
                'would be if they added just one more. The increment would '
                'settle it without confusion.'
            ),
            mapping=(
                'The five pebbles are the input, the single extra pebble is '
                'the increment of one, and the running total is the answer.'
            ),
            resolution=(
                'The REPL added one to five and handed back six. The path '
                'forward was clear — one more bone, one more mark in the tally — 5.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(dec 5)", expected=4,
            concept_phrase="the decrement operation",
            question_what="5 minus 1",
            goal_text="decrement 5 by 1",
            scenario=(
                'Rex the hound held five marked pebbles in a line at the meadow. One '
                'pebble sat at the end, set aside. He wanted to know what came before '
                'this count.'
            ),
            need=(
                'He needed to subtract one from five and know the new total. The '
                'decrement would tell him exactly what one less came to.'
            ),
            mapping=(
                'The five pebbles are the input, the single removed pebble is the '
                'decrement, and the remaining count is the answer.'
            ),
            resolution=(
                'The REPL subtracted one from five and handed back four. The path '
                'backward was clear — one fewer mark, one less in the tally — 5.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(inc 0)", expected=1,
            concept_phrase="the increment operation",
            question_what="0 plus 1",
            goal_text="increment 0",
            scenario=(
                "Patch the hound stood at the stream's edge holding no bones — zero in their count. A single extra bone sat waiting to be added to the empty pile."
            ),
            need=(
                'They wanted to know what zero plus one would be. The increment would '
                'show them the very first step from nothing.'
            ),
            mapping=(
                'Zero is the starting count, the single new bone is the increment, '
                'and the result is the first number.'
            ),
            resolution=(
                'The REPL added one to zero and handed back one. From nothing came '
                'the first count, and the 0 was certain.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(dec 0)", expected=-1,
            concept_phrase="the decrement operation",
            question_what="0 minus 1",
            goal_text="decrement 0",
            scenario=(
                'Bell the hound stood at the stream\'s edge with zero bones — an empty '
                'paw. She wanted to know what came before zero, to go below it.'
            ),
            need=(
                'She needed to subtract one from zero and cross into the negative '
                'numbers. The decrement would show her the path backward past zero.'
            ),
            mapping=(
                'Zero is the starting point, the decrement takes one away, and the '
                'result is the first negative number.'
            ),
            resolution=(
                'The REPL subtracted one from zero and handed back negative one. The '
                'path into negative numbers was opened, and the 0 was clear.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(inc -1)", expected=0,
            concept_phrase="the increment operation",
            question_what="negative 1 plus 1",
            goal_text="increment negative 1",
            scenario=(
                'Rex the hound held a stone carved with negative 1 near the forest. He '
                'wanted to add one and see if it would reach zero.'
            ),
            need=(
                'He needed to increment negative one and know if it would cross back '
                'to zero. The addition would settle where it led.'
            ),
            mapping=(
                'Negative 1 is the starting value, the increment of one is the added '
                'amount, and the result reaches zero.'
            ),
            resolution=(
                'The REPL added one to negative one and handed back zero. The path '
                'forward had reached the neutral point, the -1 exact.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_07 = SubjectCurriculum(
    grade=2, subject_id="G2-07",
    subject_title="Absolute value",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(abs 5)", expected=5,
            concept_phrase="the absolute value",
            question_what="the absolute value of 5",
            goal_text="find the absolute value of 5",
            scenario=(
                'Bell the hound stood near the forest and held a marked stone '
                'engraved with the number 5. She knew some numbers could be '
                'negative, but this one was not.'
            ),
            need=(
                'She wanted the distance from zero, the pure measure without '
                'any sign attached. The absolute value would give her the '
                'magnitude alone.'
            ),
            mapping=(
                'The marked stone is the input, its distance from zero is the '
                'absolute value, and the sign (if any) is stripped away.'
            ),
            resolution=(
                'The REPL stripped away the sign and measured the distance — '
                '5 had no negative sign, so the 5 was 5. The magnitude '
                'was returned unchanged.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(abs -5)", expected=5,
            concept_phrase="the absolute value",
            question_what="the absolute value of negative 5",
            goal_text="find the absolute value of negative 5",
            scenario=(
                'Patch the hound held a marked stone carved with negative 5. They '
                'wanted to know the distance from zero, ignoring the negative sign '
                'entirely.'
            ),
            need=(
                'They needed the magnitude — the pure measure of how far from zero, '
                'without any sign attached. The absolute value would strip the sign '
                'away.'
            ),
            mapping=(
                'The marked stone holds a negative number, the absolute value removes '
                'the sign, and the distance from zero is what remains.'
            ),
            resolution=(
                'The REPL stripped away the negative sign and measured the distance — '
                'negative 5 became 5. The magnitude was returned unchanged — -5.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(abs 0)", expected=0,
            concept_phrase="the absolute value",
            question_what="the absolute value of 0",
            goal_text="find the absolute value of 0",
            scenario=(
                'Bell the hound held a stone marked with zero near the pond. She '
                'wanted the absolute value — the distance from zero itself.'
            ),
            need=(
                'She needed to know the magnitude of zero. The absolute value of '
                'zero would still be zero, for it lies at the center.'
            ),
            mapping=(
                'Zero is the input value, the absolute value removes the sign (though '
                'there is none), and the result is zero.'
            ),
            resolution=(
                'The REPL applied absolute value to zero and returned zero. The '
                'distance at the center was itself, and the 0 was clear.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(abs (- 3 8))", expected=5,
            concept_phrase="the absolute value",
            question_what="the absolute value of the difference between 3 and 8",
            goal_text="find the absolute value of 3 minus 8",
            scenario=(
                'Rex the hound wanted to find the distance between two marks — 3 and '
                '8 — on a stone. First, he subtracted 3 from 8, then wanted the '
                'magnitude of that difference.'
            ),
            need=(
                'He needed the gap between the two marks, no matter which came first. '
                'The absolute value would give the pure distance without regard to '
                'sign.'
            ),
            mapping=(
                'Three and eight are the two points, their difference is computed '
                'first, and the absolute value strips the sign to show the distance.'
            ),
            resolution=(
                'The REPL subtracted three from eight to get five, then applied '
                'absolute value. The distance was five, exact and unsigned — 8.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_08 = SubjectCurriculum(
    grade=2, subject_id="G2-08",
    subject_title="Arithmetic on ratios",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(+ 1/2 1/4)", expected="3/4",
            concept_phrase="the sum of two ratios",
            question_what="the sum of one-half and one-quarter",
            goal_text="add one-half and one-quarter",
            scenario=(
                'Rex the hound broke two bones into pieces near the meadow. One '
                'bone yielded one-half, the other one-quarter. He wanted to '
                'know the combined measure.'
            ),
            need=(
                'He needed the total when the two fractions were joined — the '
                'sum that would tell him the exact portion when both pieces '
                'were stacked.'
            ),
            mapping=(
                'Each piece is a rational fraction, the addition is the '
                'combining, and the result is the exact portion expressed as '
                'a ratio.'
            ),
            resolution=(
                'The REPL added one-half and one-quarter with precision and '
                'handed back three-quarters. The combined measure was exact, '
                'a true rational sum — 1/4.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 2/3 3/4)", expected="1/2",
            concept_phrase="the product of two ratios",
            question_what="the product of two-thirds and three-quarters",
            goal_text="multiply two-thirds by three-quarters",
            scenario=(
                'Patch the hound broke a bone into two-thirds near the meadow and '
                'another into three-quarters. They wanted the product when the two '
                'fractions were multiplied together.'
            ),
            need=(
                'They needed to know what two-thirds times three-quarters would come '
                'to — the exact portion expressed as a ratio when combined.'
            ),
            mapping=(
                'Each fraction is one factor, the multiplication combines them, and '
                'the result is the exact product expressed as a ratio.'
            ),
            resolution=(
                'The REPL multiplied two-thirds by three-quarters with precision and '
                'returned one-half. The product was exact, a true rational result — 3/4.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(- 1 1/3)", expected="2/3",
            concept_phrase="the difference of a whole and a ratio",
            question_what="1 minus one-third",
            goal_text="subtract one-third from 1",
            scenario=(
                'Bell the hound held one whole bone at the stream\'s edge and removed '
                'one-third of it. She wanted to know what fraction remained.'
            ),
            need=(
                'She needed the remainder when one-third was taken from one whole. '
                'The subtraction would return the exact portion left over.'
            ),
            mapping=(
                'One whole is the starting value, one-third is the piece removed, and '
                'the difference is the exact fraction that remains.'
            ),
            resolution=(
                'The REPL subtracted one-third from one whole and returned two-thirds. '
                'The remainder was exact, a true rational difference — 1/3.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_09 = SubjectCurriculum(
    grade=2, subject_id="G2-09",
    subject_title="Floats vs ints (the / operator)",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(/ 10 2)", expected=5,
            concept_phrase="the division operation",
            question_what="the result of using / on 10 and 2",
            goal_text="divide 10 by 2",
            scenario=(
                "Patch the hound held ten fish bones at the stream's edge and wanted to split them evenly into two piles. The division would tell them how many landed in each."
            ),
            need=(
                'They needed to know what ten divided by two would give — the '
                'exact share per pile. The result would either be a whole '
                'number or a precise fraction.'
            ),
            mapping=(
                '{drawn.a} bones make the numerator, two piles make the divisor, and the division operation yields the exact answer.'
            ),
            resolution=(
                'The REPL divided ten by two and handed back five. Since the division was clean, five whole bones went to each pile, and no remainder lingered — 2 (with `10` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(/ 10 3)", expected="10/3",
            concept_phrase="the division operation",
            question_what="the exact rational result of using / on 10 and 3",
            goal_text="divide 10 by 3",
            scenario=(
                "Rex the hound held ten fish bones at the stream's edge and wanted to split them evenly into {drawn.b} piles. The division would tell what each pile held exactly."
            ),
            need=(
                'He needed to know what ten divided by three would yield — the exact '
                'share per pile. The result would be a precise rational fraction.'
            ),
            mapping=(
                '{drawn.a} bones make the numerator, {drawn.b} piles make the divisor, and the division operation yields the exact rational answer.'
            ),
            resolution=(
                'The REPL divided ten by three and handed back the exact ratio '
                'ten-thirds. The answer was rational and precise, not a flat number — 3.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(/ 1.0 2)", expected=0.5,
            concept_phrase="the division operation",
            question_what="the result of 1.0 divided by 2",
            goal_text="divide 1.0 by 2",
            scenario=(
                'Patch the hound held a floating-point bone marked 1.0 at the meadow '
                'and wanted to divide it by 2. The result would be expressed as a '
                'decimal.'
            ),
            need=(
                'They needed one-point-zero split evenly in two. The division would '
                'return the exact decimal share.'
            ),
            mapping=(
                'One-point-zero is the numerator, 2 is the divisor, and the division '
                'yields the exact decimal result.'
            ),
            resolution=(
                'The REPL divided one-point-zero by 2 and returned zero-point-five. '
                'The floating-point answer was exact — 2.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_10 = SubjectCurriculum(
    grade=2, subject_id="G2-10",
    subject_title="Powers via repeated multiplication",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(* 2 2 2)", expected=8,
            concept_phrase="repeated multiplication",
            question_what="2 to the third power",
            goal_text="multiply 2 by itself three times",
            scenario=(
                'Bell the hound stood at the beach with three marked pebbles, '
                'each carved with the number 2. She wanted to multiply them '
                'all together in order.'
            ),
            need=(
                'She needed the result of taking two and multiplying it by '
                'itself, twice over. The compounding would tell her the final '
                'answer.'
            ),
            mapping=(
                'Each pebble marked 2 is one factor in the multiplication, '
                'repeating it three times makes the power, and the running '
                'product is the answer.'
            ),
            resolution=(
                'The REPL multiplied two by two, got four, then multiplied '
                'that by two again to get eight. The power was exact, and the '
                'answer was handed back at once — 2.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 5 5)", expected=25,
            concept_phrase="repeated multiplication",
            question_what="5 to the second power",
            goal_text="multiply 5 by itself",
            scenario=(
                'Patch the hound laid two marked stones near the pond, each carved '
                'with the number 5. They wanted to multiply them together to see '
                'the power.'
            ),
            need=(
                'They needed the result of five multiplied by itself once — five '
                'squared. The running product would hold the power.'
            ),
            mapping=(
                'Each stone marked 5 is one factor, repeating it twice makes the '
                'square, and the running product is the answer.'
            ),
            resolution=(
                'The REPL multiplied five by five to get twenty-five. The square was '
                'exact, and the 5 was handed back at once.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 3 3 3 3)", expected=81,
            concept_phrase="repeated multiplication",
            question_what="3 to the fourth power",
            goal_text="multiply 3 by itself four times",
            scenario=(
                'Bell the hound gathered four pebbles at the stream\'s edge, each '
                'marked with 3. She wanted to multiply them all together to find the '
                'fourth power.'
            ),
            need=(
                'She needed the result of three multiplied four times by itself — '
                'three to the fourth. The compounding would show the final answer.'
            ),
            mapping=(
                'Each pebble marked 3 is one factor in the multiplication, repeating '
                'four times makes the fourth power, and the running product grows '
                'until it settles.'
            ),
            resolution=(
                'The REPL multiplied 3 by 3 to get 9, then by 3 again to get 27, '
                'then by 3 once more to get 81. The fourth power was exact — 3.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 10 10)", expected=100,
            concept_phrase="repeated multiplication",
            question_what="10 to the second power",
            goal_text="multiply 10 by itself",
            scenario=(
                'Rex the hound stood by the beach and placed two marked pebbles, each '
                'carved with 10. He wanted to multiply them together to find the '
                'square.'
            ),
            need=(
                'He needed ten multiplied by itself — ten squared. The power would '
                'reach one hundred.'
            ),
            mapping=(
                'Each pebble marked 10 is one factor, repeating twice makes the '
                'square, and the running product is the answer.'
            ),
            resolution=(
                'The REPL multiplied ten by ten to get one hundred. The square was '
                'exact, and the 10 came back clear.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_11 = SubjectCurriculum(
    grade=2, subject_id="G2-11",
    subject_title="String concatenation with str",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form='(str "ab" "cd")',
            expected="abcd",
            concept_phrase='the string concatenation',
            question_what='the result of using str to splice "ab" and "cd"',
            goal_text='use str to splice the two-letter strings "ab" and "cd" into a single thread',
            scenario=(
                'Bell the hound held up two short bark-strips at the bank '
                'near the pond, each scratched with a pair of marks.'
            ),
            need=(
                'She wanted the strips spliced into one longer strip — '
                'every mark in its place — without altering either '
                'original.'
            ),
            mapping=(
                'Each strip is a string, each scratch is one character, str '
                'is the splicing operation, and the result is the longer '
                'strip with both sets of marks in order.'
            ),
            resolution=(
                'The REPL spliced the strips and handed back the longer '
                'one. The two originals stayed as they had been — cd.'
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
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form='(println "hello")', expected=None,
            concept_phrase='the print-line call',
            question_what='the return value of using println on the string "hello"',
            goal_text='print the string "hello" with a newline',
            scenario=(
                "Rex the hound picked up a piece of bark at the stream's edge and scratched the word hello into its surface. He wanted the mark to be seen and recorded."
            ),
            need=(
                'He needed the scratch-marks left on the bark as a side effect, '
                'a visible record. The return value itself was less important '
                'than the act of marking.'
            ),
            mapping=(
                'The string "hello" is the message, println is the paw-stroke '
                'that writes and breaks to a new line, and the return is nil — '
                'just the void of marking done.'
            ),
            resolution=(
                'The REPL scratched hello onto the bark with a line-break and '
                'handed back nil. The message was written for all to read, and '
                'nothing else was needed.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(print "x")', expected=None,
            concept_phrase='the print call',
            question_what='the return value of using print on the string "x"',
            goal_text='print the string "x" without a newline',
            scenario=(
                'Patch the hound picked up a piece of bark near the meadow and scratched '
                'a single mark x into its surface. They wanted the mark to appear but no '
                'line-break after it.'
            ),
            need=(
                'They needed the side effect — the mark left on the bark. The return value '
                'was less important than the scratch itself.'
            ),
            mapping=(
                'The string "x" is the message, print is the paw-stroke that writes without '
                'a line-break, and the return is nil — void when the marking is done.'
            ),
            resolution=(
                'The REPL scratched x onto the bark without a newline and handed back nil. '
                'The message was written, and nothing more was needed.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_13 = SubjectCurriculum(
    grade=2, subject_id="G2-13",
    subject_title="and / or — short circuit, return values",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(and true true)",
            expected=True,
            concept_phrase="the logical and",
            question_what="the result of passing true and true through the and-chain of gates",
            goal_text="test whether two trues both pass through an and-chain of gates",
            scenario=(
                'Bell the hound stood at the stream bank, facing two test gates '
                'placed one after the other. Each gate bore a mark: true, then '
                'true.'
            ),
            need=(
                'She wanted to cross if both gates would let her pass. The and '
                'would test each one in turn — if either blocked her, the '
                'chain would fail.'
            ),
            mapping=(
                'Each gate is one condition, the and is the chain that checks '
                'them in sequence, and the verdict is true only if all pass her '
                'through.'
            ),
            resolution=(
                'The REPL tested true at the first gate — it opened. True at '
                'the second gate — it opened too. Both conditions held, and the '
                'verdict came back true. She could cross.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(and true false)", expected=False,
            concept_phrase="the logical and",
            question_what="the result of using and on true and false",
            goal_text="test true and false with the and operator",
            scenario=(
                'Rex the hound stood at the stream bank facing two test gates placed '
                'one after the other. The first bore the mark true, the second false.'
            ),
            need=(
                'He wanted to cross if both gates would let him pass. The and would test '
                'each in turn — if either blocked, the chain would fail and he could not '
                'cross.'
            ),
            mapping=(
                'Each gate is one condition, the and chains them, and the verdict is true '
                'only if all pass him through.'
            ),
            resolution=(
                'The REPL tested true at the first gate — it opened. False at the second '
                'gate — it barred the way. One condition failed, and the verdict came back '
                'false. He could not cross.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(or false true)", expected=True,
            concept_phrase="the logical or",
            question_what="the result of using or on false and true",
            goal_text="test false or true with the or operator",
            scenario=(
                'Patch the hound approached a fork near the meadow. The first path bore the '
                'mark false, the second true. They wanted to find any path that was open.'
            ),
            need=(
                'They needed to know if at least one path would lead forward. The or would '
                'test each — if any opened, the journey could continue.'
            ),
            mapping=(
                'Each path is one condition, the or tests them seeking an opening, and true '
                'returns if any path is available.'
            ),
            resolution=(
                'The REPL tested false at the first path — closed. True at the second — '
                'open. At least one way forward existed, and the verdict came back true.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(or false false)", expected=False,
            concept_phrase="the logical or",
            question_what="the result of using or on false and false",
            goal_text="test false or false with the or operator",
            scenario=(
                'Bell the hound arrived at a fork by the pond. Both paths bore the mark '
                'false. She wanted to know if any path was open.'
            ),
            need=(
                'She needed at least one path to lead forward. The or would test both — if '
                'all were closed, the journey could not continue.'
            ),
            mapping=(
                'Each path is one condition, the or tests them seeking an opening, and '
                'false returns only when no path is available.'
            ),
            resolution=(
                'The REPL tested false at the first path — closed. False at the second — '
                'also closed. No way forward existed, and false was handed back.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(and 1 2 3)", expected=3,
            concept_phrase="the logical and",
            question_what="the result of using and on 1, 2, and 3",
            goal_text="apply and to 1, 2, and 3",
            scenario=(
                'Rex the hound held three marked stones at the forest — 1, 2, and 3. He '
                'wanted to apply the and operator to see what would pass through the chain '
                'of tests.'
            ),
            need=(
                'He needed to know what the and-chain would return when applied to three '
                'truthy values. The result would show what the chain carried forward.'
            ),
            mapping=(
                'Each stone is one value tested by and, all are truthy, and the chain '
                'returns the last value that passed through.'
            ),
            resolution=(
                'The REPL tested 1 with and — truthy, passed. Then 2 — truthy, passed. '
                'Then 3 — truthy, passed. The last value, 3, was returned — 3.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(or nil false 5)", expected=5,
            concept_phrase="the logical or",
            question_what="the result of using or on nil, false, and 5",
            goal_text="apply or to nil, false, and 5",
            scenario=(
                'Patch the hound approached three paths near the meadow — one marked nil, '
                'one marked false, and one marked 5. They wanted to find which could carry '
                'them forward.'
            ),
            need=(
                'They needed the first truthy value in the chain — the path that would lead '
                'forward. The or-chain would find it.'
            ),
            mapping=(
                'Each path is one value tested by or, the first truthy value is the answer, '
                'and false or nil values are skipped until a true one is found.'
            ),
            resolution=(
                'The REPL tested nil — falsey, skipped. Then false — falsey, skipped. Then '
                '5 — truthy, returned. The first open path was 5 — 5.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_14 = SubjectCurriculum(
    grade=2, subject_id="G2-14",
    subject_title="not — turning truthy to false",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(not true)", expected=False,
            concept_phrase="the logical not",
            question_what="the result of using not on true",
            goal_text="negate the value true",
            scenario=(
                'Patch the hound held a stone marked true near the forest. They '
                'wanted to flip its meaning — to ask what the opposite would be '
                'if taken from the other side.'
            ),
            need=(
                'They needed the negation of true — the inverse verdict that '
                'would tell them the opposite path. The not operation would '
                'turn it around.'
            ),
            mapping=(
                'The true value is the input, the not operator is the flip, '
                'and the result is the negated verdict.'
            ),
            resolution=(
                'The REPL negated true and handed back false. The opposite was '
                'clear, and the verdict was reversed. One side became the other.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(not false)", expected=True,
            concept_phrase="the logical not",
            question_what="the result of using not on false",
            goal_text="negate the value false",
            scenario=(
                'Bell the hound held a stone marked false near the pond. She wanted to flip '
                'its meaning — to ask what the opposite would be if taken from the other '
                'side.'
            ),
            need=(
                'She needed the negation of false — the inverse verdict that would tell her '
                'the opposite state. The not operation would turn it around.'
            ),
            mapping=(
                'The false value is the input, the not operator is the flip, and the result '
                'is the negated verdict.'
            ),
            resolution=(
                'The REPL negated false and handed back true. The opposite was clear, and '
                'the verdict was reversed. Falsehood became truth.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(not nil)", expected=True,
            concept_phrase="the logical not",
            question_what="the result of using not on nil",
            goal_text="negate the value nil",
            scenario=(
                'Patch the hound held a stone marked nil at the meadow. They wanted to flip '
                'its meaning — to know what the opposite of nothing would be.'
            ),
            need=(
                'They needed the negation of nil — the truth value that would oppose it. '
                'The not would settle what nothing became when negated.'
            ),
            mapping=(
                'Nil is the input, the not operator flips it, and the result is the negated '
                'verdict.'
            ),
            resolution=(
                'The REPL negated nil and handed back true. Nothing became truth when '
                'negated, and the answer was clear.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(not 0)", expected=False,
            concept_phrase="the logical not",
            question_what="the result of using not on 0",
            goal_text="negate the value 0",
            scenario=(
                'Rex the hound held a stone marked 0 near the forest. He wanted to flip its '
                'truthiness — to know if zero negated would become false.'
            ),
            need=(
                'He needed the negation of zero. Since zero is truthy, the negation would '
                'return false.'
            ),
            mapping=(
                'Zero is the input, the not operator flips its truthiness, and the result '
                'is false.'
            ),
            resolution=(
                'The REPL negated zero — which is truthy — and returned false. The truth '
                'was flipped, and the 0 came back clear.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(not "")', expected=False,
            concept_phrase="the logical not",
            question_what="the result of using not on the empty string",
            goal_text="negate the empty string",
            scenario=(
                'Patch the hound held a blank bark-strip at the stream\'s edge — empty, '
                'with no marks. They wanted to know what the empty string negated would be.'
            ),
            need=(
                'They needed the negation of the empty string. Since empty is truthy, the '
                'negation would return false.'
            ),
            mapping=(
                'The empty string is the input, the not operator flips its truthiness, and '
                'the result is false.'
            ),
            resolution=(
                'The REPL negated the empty string — which is truthy — and returned false. The truth was inverted, and the answer was settled (with `` as the input value) (with `` as the input value).'
            ),
            tags=("story",),
        ),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_15 = SubjectCurriculum(
    grade=2, subject_id="G2-15",
    subject_title="Falsey values: only false and nil",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(if 0 1 0)", expected=1,
            concept_phrase="the if conditional with zero as condition",
            question_what="the result of if with condition 0, then-branch 1, else-branch 0",
            goal_text="use if to return 1 when the condition is 0 (then-branch) and 0 otherwise (else-branch)",
            scenario=(
                "Rex the hound stood at a fork in the path at the stream's edge. A stone marked 0 sat at the junction. If the condition checked zero as truthy, one path opened; if falsey, another."
            ),
            need=(
                'He needed to know which path to take when the test condition '
                'was zero. The if would read the value and branch to one of '
                'two destinations.'
            ),
            mapping=(
                'Zero is the test condition, the then-branch returns 1, the '
                'else-branch returns 0, and the if decides which fork leads '
                'home.'
            ),
            resolution=(
                'The REPL tested zero — which is not false and not nil, so it '
                'counts as truthy. The then-branch opened, and 1 was handed back. '
                'The right path was taken — 0.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(if "" 1 0)', expected=1,
            concept_phrase="the if conditional with empty string as condition",
            question_what="the result of if with condition the empty string, then-branch 1, else-branch 0",
            goal_text="use if to return 1 when the condition is the empty string (then-branch) and 0 otherwise (else-branch)",
            scenario=(
                'Bell the hound stood at a fork in the path near the pond. A blank '
                'bark-strip — empty, with no marks — sat at the junction. If the '
                'condition checked empty as truthy, one path opened.'
            ),
            need=(
                'She needed to know which path to take when the test condition was an '
                'empty string. The if would read the value and branch to one of two '
                'destinations.'
            ),
            mapping=(
                'The empty string is the test condition, the then-branch returns 1, the '
                'else-branch returns 0, and the if decides which fork to follow.'
            ),
            resolution=(
                'The REPL tested the empty string — which is truthy, not false and not nil. '
                'The then-branch opened, and 1 was returned. The right path was taken.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(if nil 1 0)", expected=0,
            concept_phrase="the if conditional with nil as condition",
            question_what="the result of if with condition nil, then-branch 1, else-branch 0",
            goal_text="use if to return 1 when the condition is nil (then-branch) and 0 otherwise (else-branch)",
            scenario=(
                'Patch the hound stood at a fork near the meadow. A stone marked nil sat '
                'at the junction. If nil checked falsey, the else path would open.'
            ),
            need=(
                'They needed to know which branch would follow when the condition was nil. '
                'The if would test and route to the right destination.'
            ),
            mapping=(
                'Nil is the test condition, the then-branch returns 1, the else-branch '
                'returns 0, and the if decides the fork.'
            ),
            resolution=(
                'The REPL tested nil — which is falsey. The else-branch opened, and 0 was '
                'returned. The left path was taken — 0.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(if false 1 0)", expected=0,
            concept_phrase="the if conditional with false as condition",
            question_what="the result of if with condition false, then-branch 1, else-branch 0",
            goal_text="use if to return 1 when the condition is false (then-branch) and 0 otherwise (else-branch)",
            scenario=(
                'Rex the hound stood at a fork in the path at the stream\'s edge. A stone '
                'marked false sat at the junction. If false checked falsey, the else path '
                'would open.'
            ),
            need=(
                'He needed to know which path to follow when the test condition was false. '
                'The if would test and branch to one of two destinations.'
            ),
            mapping=(
                'False is the test condition, the then-branch returns 1, the else-branch '
                'returns 0, and the if decides which fork leads home.'
            ),
            resolution=(
                'The REPL tested false — which is falsey. The else-branch opened, and 0 was '
                'handed back. The left path was taken — 0.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_16 = SubjectCurriculum(
    grade=2, subject_id="G2-16",
    subject_title="Truthy 0 and empty string",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(boolean 0)", expected=True,
            concept_phrase="the boolean conversion",
            question_what="the result of using boolean on 0",
            goal_text="convert 0 to a boolean",
            scenario=(
                'Bell the hound held a stone carved with 0 near the meadow. She '
                'wanted to know what boolean state this number held — was it '
                'true or false in the eyes of the REPL?'
            ),
            need=(
                'She needed to convert the number to a clear true-or-false '
                'answer. The boolean function would strip away the number and '
                'leave only the verdict.'
            ),
            mapping=(
                'The zero is the input value, the boolean conversion is the '
                'test for truthiness, and the result is the pure true-or-false '
                'state.'
            ),
            resolution=(
                'The REPL converted zero to a boolean. Since zero is not false '
                'and not nil, it counts as truthy. The answer came back true — '
                'the zero was a true value in boolean terms — 0.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(boolean "")', expected=True,
            concept_phrase="the boolean conversion",
            question_what="the result of using boolean on the empty string",
            goal_text="convert the empty string to a boolean",
            scenario=(
                'Patch the hound held a blank bark-strip near the forest. They wanted to '
                'convert it to a boolean state — to ask if empty was true or false in the '
                'REPL\'s eyes.'
            ),
            need=(
                'They needed to convert the empty string to a clear true-or-false answer. '
                'The boolean function would strip away the string and leave only the '
                'verdict.'
            ),
            mapping=(
                'The empty string is the input value, the boolean conversion tests '
                'truthiness, and the result is the pure true-or-false state.'
            ),
            resolution=(
                'The REPL converted the empty string to a boolean. Since empty is not false and not nil, it counts as truthy. True was returned (with `` as the input value) (with `` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(boolean nil)", expected=False,
            concept_phrase="the boolean conversion",
            question_what="the result of using boolean on nil",
            goal_text="convert nil to a boolean",
            scenario=(
                'Bell the hound held nothing at the pond — nil in her paw. She wanted to '
                'convert it to a boolean state to know its truth value.'
            ),
            need=(
                'She needed to know if nil was true or false. The boolean function would '
                'answer with certainty.'
            ),
            mapping=(
                'Nil is the input value, the boolean conversion tests truthiness, and the '
                'result is the pure boolean state.'
            ),
            resolution=(
                'The REPL converted nil to a boolean. Since nil is falsey, the answer came '
                'back false. Nothing was indeed false.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(boolean false)", expected=False,
            concept_phrase="the boolean conversion",
            question_what="the result of using boolean on false",
            goal_text="convert false to a boolean",
            scenario=(
                'Rex the hound held a stone marked false at the meadow. He wanted to convert '
                'it to a boolean state to confirm its truthiness.'
            ),
            need=(
                'He needed to know if false was true or false. The boolean function would '
                'return the verdict.'
            ),
            mapping=(
                'False is the input value, the boolean conversion tests truthiness, and the '
                'result is the pure boolean state.'
            ),
            resolution=(
                'The REPL converted false to a boolean. False is falsey, so the answer came '
                'back false. The verdict was certain.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_17 = SubjectCurriculum(
    grade=2, subject_id="G2-17",
    subject_title="Keyword as function for map lookup",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(:hare {:hare 1 :tortoise 2})", expected=1,
            concept_phrase="the keyword lookup",
            question_what="the result of using the keyword :hare as a function on the map {:hare 1 :tortoise 2}",
            goal_text="use the keyword :hare to look up a value in the map with keys :hare and :tortoise",
            scenario=(
                'Bell the hound paused at a hollow log near the pond. '
                'Inside, two bones rested in named slots — one labeled '
                ':hare, one labeled :tortoise.'
            ),
            need=(
                'She wanted the bone in the :hare slot — without disturbing '
                'the other. The cache itself would stay as it was for any '
                'later dog.'
            ),
            mapping=(
                'The cache is the map, named slots are the keys, the labels '
                'are scratched above each slot, and the bones inside are '
                'the values.'
            ),
            resolution=(
                'The REPL reached into the named slot and handed back its '
                'bone. The cache stayed exactly as it was, the other slot '
                'undisturbed — tortoise.'
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
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(symbol? (quote hare))", expected=True,
            concept_phrase="the symbol-predicate applied to a long-form-quoted name",
            question_what="whether long-form quoting produces a symbol",
            goal_text="ask whether long-form quoting of the name hare produces a symbol, using symbol?",
            scenario=(
                "Patch the hound found a bone scratch on bark at the stream's edge that read hare. They wondered — was this mark the same as the animal, or just a name-mark that stood for it?"
            ),
            need=(
                'They needed to know if the quoted name was truly a symbol — a '
                'mark that names something rather than the thing itself. The '
                'symbol? predicate would settle it.'
            ),
            mapping=(
                'The bark-scratch is the symbol, quoting it freezes it as a '
                'name-mark, and the symbol? test asks if what remains is a '
                'symbol or something else.'
            ),
            resolution=(
                'The REPL quoted the name hare and then tested whether it was a '
                'symbol. Yes — a quoted name is a symbol, not the animal. The '
                'answer came back true. The mark was what it appeared to be.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(= (quote tortoise) 'tortoise)", expected=True,
            concept_phrase="the equality of long-form and short-form quoting",
            question_what="whether long-form and short-form quoting produce equal values",
            goal_text="compare the result of long-form quoting of tortoise against the apostrophe-shorthand quoting of the same name, using =",
            scenario=(
                "Bell the hound found two bones at the stream's edge scratched with the same mark. One bore the long scratch of the full word tortoise, the other a quick mark that meant the same thing. She wanted to know if they matched."
            ),
            need=(
                'She needed to test if the two different ways of marking — long and short — '
                'produced the same symbol. The equality test would settle whether they '
                'matched.'
            ),
            mapping=(
                'The long scratch is the quote form, the short mark is the apostrophe '
                'shorthand, and the equality test asks if both produce the same symbol.'
            ),
            resolution=(
                'The REPL tested both forms and found they were equal — both produced the '
                'symbol tortoise. The different paths led to the same name.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(count '(1 2 3))", expected=3,
            concept_phrase="the element count of a quoted list",
            question_what="the number of elements in a quoted list",
            goal_text="count the elements in a quoted list of the integers 1, 2, and 3",
            scenario=(
                'Patch the hound held a quoted list near the meadow — a frozen row of three '
                'marks: 1, 2, 3. They wanted to count how many marks lay in that frozen row.'
            ),
            need=(
                'They needed to know how many elements were in the quoted list. The count '
                'would walk the frozen row and tally each mark.'
            ),
            mapping=(
                'The quoted list is the frozen row, each mark is one element, and the count '
                'is the tally of all elements in the list.'
            ),
            resolution=(
                'The REPL counted the elements in the quoted list — 1, 2, 3 — and returned '
                '3. The count was exact, the frozen row was measured.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_CHALKMARK_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_19 = SubjectCurriculum(
    grade=2, subject_id="G2-19",
    subject_title="Auto-promotion to bigint",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(* 1000000 1000000)", expected=1000000000000,
            concept_phrase="the large multiplication",
            question_what="the product of one million and one million",
            goal_text="multiply one million by one million",
            scenario=(
                'Rex the hound stood by the river bank with two enormous piles '
                'of bones. Each pile held one million bones. He wanted to know '
                'the result if he multiplied them together.'
            ),
            need=(
                'He needed the exact product of one million times one million. '
                'The number would be vast, but the REPL would handle it without '
                'flinching.'
            ),
            mapping=(
                'Each pile of one million bones is a factor, the '
                'multiplication combines them, and the result is the colossal '
                'number that emerges from such a joining.'
            ),
            resolution=(
                'The REPL multiplied one million by one million and handed back '
                'one trillion. The number was so large it spilled beyond the '
                'ordinary integer bounds, but the REPL grew the container to '
                'hold it. The answer was exact — 1000000.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(+ 99999999999 1)", expected=100000000000,
            concept_phrase="the large addition",
            question_what="the sum of 99999999999 and 1",
            goal_text="add 1 to 99999999999",
            scenario=(
                'Rex the hound held an enormous pile of 99 billion, 999 million bones at '
                'the river bank. A single extra bone sat beside the pile. He wanted to know '
                'the total.'
            ),
            need=(
                'He needed the exact sum when one bone was added to that vast pile. The '
                'number would be enormous, and the REPL would handle it without flinching.'
            ),
            mapping=(
                'The great pile of 99999999999 bones is the first addend, the single bone '
                'is the second, and the sum is the result of combining them.'
            ),
            resolution=(
                'The REPL added one to the vast number and handed back one hundred billion. '
                'The sum was so large the integer container grew, but the 1 was exact.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_20 = SubjectCurriculum(
    grade=2, subject_id="G2-20",
    subject_title="Counting",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(count [1 2 3])", expected=3,
            concept_phrase="the count operation",
            question_what="the result of using count on the vector containing 1, 2, and 3",
            goal_text="count the elements in the vector containing 1, 2, and 3",
            scenario=(
                'Bell the hound paced down a small row of cached bones near '
                'the pond — three of them lying end to end on a flat stone '
                '— adding one to her running tally at each bone, no other '
                'operation needed.'
            ),
            need=(
                'She wanted only the size of the row — how many bones lay '
                'in it — without examining what kind each one was. The '
                'runtime would do the counting for her, exact every time.'
            ),
            mapping=(
                'The row is the vector, each bone is one element, the '
                "running tally is the count, and the runtime's "
                'walk-and-add-one at each step is what count does for any '
                'collection.'
            ),
            resolution=(
                'The REPL walked the row, adding one at each bone, and '
                'handed back the size. The bones themselves stayed where '
                'they had been — the 3 was the count, not the '
                'contents.'
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
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(count \"tortoise\")", expected=8,
            concept_phrase="the count of characters in a string",
            question_what="the result of using count on the string tortoise",
            goal_text="count the characters in the string tortoise",
            scenario=(
                'Bell the hound held a bark-strip with a long message scratched '
                'onto it: tortoise. Each scratch was one character, and she '
                'wanted to know how many marks lay in the row.'
            ),
            need=(
                'She needed the precise count of the characters without having '
                'to count on her paws. The count operation would walk the strip '
                'and tally each mark.'
            ),
            mapping=(
                'The bark-strip is the string, each scratch is one character, '
                'and the running count is the answer.'
            ),
            resolution=(
                'The REPL walked the bark-strip from end to end, tallying each '
                'scratch. The message tortoise held eight characters, and the '
                'count came back 8. The row was measured exactly.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(count "hare")', expected=4,
            concept_phrase="the count of characters in a string",
            question_what='the result of using count on the string hare',
            goal_text='count the characters in the string hare',
            scenario=(
                'Patch the hound held a bark-strip with the message hare scratched onto it. '
                'Each scratch was one character, and they wanted to know the total marks in '
                'the row.'
            ),
            need=(
                'They needed the precise count of the characters without counting on their '
                'paws. The count operation would walk the strip and tally each mark.'
            ),
            mapping=(
                'The bark-strip is the string, each scratch is one character, and the '
                'running count is the answer.'
            ),
            resolution=(
                'The REPL walked the bark-strip from end to end, tallying each scratch. The '
                'message hare held four characters, and the count came back 4.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(count (subs "tortoise" 0 3))', expected=3,
            concept_phrase="the count of characters in a leading substring",
            question_what='the count of the substring from index 0 to 3 of the string tortoise',
            goal_text='extract the leading three characters from the string tortoise using subs from index 0 to 3, then count them',
            scenario=(
                'Bell the hound held a long bark-strip with tortoise scratched across it. '
                'She wanted to extract just the first three marks and count them.'
            ),
            need=(
                'She needed to slice the first three characters from the message and count '
                'how many that was. The subs would extract the substring, then count would '
                'tally it.'
            ),
            mapping=(
                'The bark-strip is the string, subs extracts a slice from index 0 to 3, the '
                'slice becomes a new substring, and count tallies its characters.'
            ),
            resolution=(
                'The REPL extracted the leading three characters (tor) from tortoise and '
                'counted them. The result was 3, exact and certain.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_BEADSTRING_SUBPLOTS, plan_pool=_PLAN_POOL,
)


G2_22 = SubjectCurriculum(
    grade=2, subject_id="G2-22",
    subject_title="Compose pure arithmetic (multi-step calculation)",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(- (* 5 4) 7)", expected=13,
            concept_phrase="the nested arithmetic",
            question_what="the result of multiplying 5 and 4, then subtracting 7",
            goal_text="compute 5 times 4, then subtract 7",
            scenario=(
                'Patch the hound had two tasks near the forest. First, they needed to gather {drawn.b} piles of {drawn.a} bones each — five fours. Then, they would subtract {drawn.c} bones from that pile.'
            ),
            need=(
                'They wanted to know what remained after both operations. The '
                'first answer would feed into the second, and the final count '
                'would tell them the rest.'
            ),
            mapping=(
                'Five and four are the first inputs whose product is computed, '
                'seven is subtracted from that result, and the final remainder '
                'is the answer.'
            ),
            resolution=(
                'The REPL first multiplied five and four to get twenty. Then it '
                'subtracted seven, leaving thirteen. The nested arithmetic was '
                'exact, the final count handed back without doubt — 7.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(+ (* 3 8) (* 2 4))", expected=32,
            concept_phrase="the sum of products",
            question_what="the result of adding the product of 3 and 8 to the product of 2 and 4",
            goal_text="compute the product of 3 and 8, add the product of 2 and 4",
            scenario=(
                'Bell the hound had two tasks near the pond. First, she needed to multiply '
                '3 and 8 to get one pile. Then, she would multiply 2 and 4 to get another '
                'pile. Finally, she would add them together.'
            ),
            need=(
                'She needed the sum of those two products. The nested arithmetic would '
                'compute both multiplications first, then combine the results.'
            ),
            mapping=(
                '3 and 8 are one pair whose product is computed, 2 and 4 are another pair, '
                'their products are added together, and the final sum is the answer.'
            ),
            resolution=(
                'The REPL multiplied 3 by 8 to get 24, then 2 by 4 to get 8. Then it added '
                'them to get 32. The sum of products was exact — 4.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(quot (+ 100 50) 5)", expected=30,
            concept_phrase="the nested quotient",
            question_what="the integer quotient of the sum of 100 and 50 divided by 5",
            goal_text="add 100 and 50, then divide by 5",
            scenario=(
                'Patch the hound had two tasks at the meadow. First, they needed to add 100 '
                'and 50 to get a grand total. Then, they would divide that by 5 to find how '
                'many groups could be made.'
            ),
            need=(
                'They needed the integer quotient when the sum was divided by 5. The nested '
                'arithmetic would add first, then divide without remainder.'
            ),
            mapping=(
                '100 and 50 are the numbers to add first, their sum is the dividend, 5 is '
                'the divisor, and the quotient is the integer groups formed.'
            ),
            resolution=(
                'The REPL added 100 and 50 to get 150. Then it divided 150 by 5 to get 30. '
                'The integer quotient was exact, no remainder — 5.'
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
    print(f"grade-2 dog-shadow smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
