"""Grade 5 — control flow + higher-order intro. Through tortoise-hare."""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.tortoise_hare.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS,
    _GOAL_SUBPLOTS,
    _PLAN_POOL,
)
from mmllm.aesop.curriculum.tortoise_hare._metaphor_pools import (
    _CIRCUIT_SUBPLOTS, _FORK_SUBPLOTS, _GATE_SUBPLOTS, _RECIPE_SUBPLOTS, _SIEVE_SUBPLOTS, _TALLYWALK_SUBPLOTS,
)




def _ex(form, expected, concept, what, goal="", tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal, tags=tags)


_PLAN_G5 = _PLAN_POOL + (
    "I use map / filter / reduce as appropriate.",
    "I write the higher-order form so the REPL can compute.",
)


G5_01 = SubjectCurriculum(grade=5, subject_id="G5-01",
    subject_title="if", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(if true :a :b)",
            expected=":a",
            concept_phrase="the conditional",
            question_what="which of :a or :b is returned",
            goal_text="choose between :a and :b based on a true condition",
            scenario=(
                "The trail split into two arms — the left arm marked :a, "
                "the right arm marked :b. A stone at the fork was carved "
                "with the word `true`. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "Mossback the tortoise needed to know which arm the "
                "runtime would take when the stone read true."
            ),
            mapping=(
                "`if` reads the condition-stone first. When it is true, "
                "the runtime takes the first arm; when false, the second. "
                "Here the stone reads `true`, so the first arm is taken."
            ),
            resolution=(
                "the trail forked cold and clear; the truthy stone sent "
                "the runner down the first arm, and the runtime — letting "
                "one step settle before the next — handed back the value "
                "that arm carried, the other lane left walked-past."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(if false :a :b)",
            expected=":b",
            concept_phrase="the conditional",
            question_what="which of :a or :b is returned",
            goal_text="choose between :a and :b based on a false condition",
            scenario=(
                "The same forked trail — left arm :a, right arm :b — "
                "but this time the condition-stone at the split was "
                "carved with the word `false`. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "Mossback wanted to know which arm the runtime would "
                "take when the condition-stone was false."
            ),
            mapping=(
                "`if` reads the condition-stone; `false` sends the "
                "runtime past the first arm without entering it. The "
                "second arm — the else-branch — is taken instead."
            ),
            resolution=(
                "the runtime passed the first arm and took the second, "
                "returning the value that arm carried."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(if (> 5 3) :a :b)",
            expected=":a",
            concept_phrase="the conditional",
            question_what="the if's branch",
            goal_text="choose between :a and :b based on whether 5 is greater than 3",
            scenario=(
                'The trail forked near a mossy boulder. The condition-stone at the split was carved `(> {drawn.a} {drawn.b})` — a comparison between two pebble-counts left there by a previous traveller.'
            ),
            need=(
                "Before taking a step, Mossback needed the runtime to "
                "test the stone's comparison and pick the correct arm."
            ),
            mapping=(
                '`if` evaluates the condition first. `(> {drawn.a} {drawn.b})` is true, so the fork resolves to the first arm; the second arm is never entered.'
            ),
            resolution=(
                "the comparison proved true, the first arm was taken, "
                "and the value it carried came back."
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_02 = SubjectCurriculum(grade=5, subject_id="G5-02",
    subject_title="if as expression", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(+ 1 (if true 10 20))",
            expected=11,
            concept_phrase="the arithmetic expression with conditional",
            question_what="the result of adding 1 to the conditional value",
            goal_text="add 1 to the result of choosing between 10 and 20 based on a true condition",
            scenario=(
                "Mossback reached a small counting-post on the path. "
                "The post held a basket with one acorn already in it, "
                "and beside it a fork-gate that would drop in either "
                "ten or twenty more acorns depending on the stone's truth."
            ),
            need=(
                "She needed the total acorn count: the one already in "
                "the basket plus whichever amount the fork-gate released."
            ),
            mapping=(
                '`if` is the fork-gate — it returns `{drawn.b}` when the condition is true, `{drawn.c}` when false. The outer `+` then adds that result to the fixed `{drawn.a}` in the basket. Here the condition-stone reads `true`, so the gate drops ten.'
            ),
            resolution=(
                "the gate released ten acorns; added to the one already "
                "waiting, the basket held the combined count."
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_03 = SubjectCurriculum(grade=5, subject_id="G5-03",
    subject_title="when", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(when true :yes)",
            expected=":yes",
            concept_phrase="the when conditional",
            question_what="the value when the condition is true",
            goal_text="evaluate a when form with a true condition",
            scenario=(
                "A single-arm fork stood at the edge of the meadow. "
                "There was no second path — the arm led forward only "
                "if the condition-stone was true; otherwise nothing "
                "happened at all. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Mossback wanted to know what the runtime returned when "
                "it found the condition true and could step down the "
                "one available arm."
            ),
            mapping=(
                "`when` is a one-armed fork. When the condition is true "
                "the single branch is taken and its value is returned. "
                "When false, no branch exists — the runtime returns "
                "nothing at all."
            ),
            resolution=(
                "the condition was true; the runtime stepped down the "
                "single arm and returned the value waiting there."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(when false :yes)",
            expected=None,
            concept_phrase="the when conditional",
            question_what="the value when the condition is false",
            goal_text="evaluate a when form with a false condition",
            scenario=(
                "The same one-armed fork — arm labeled :yes — but the "
                "condition-stone carved into the post read `false` this "
                "time. The arm led nowhere the runtime could go. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Mossback needed to know what the runtime produced when "
                "the condition was false and the single arm was closed."
            ),
            mapping=(
                "`when` with a false condition finds no open branch. "
                "With no arm to take, the runtime returns nothing — "
                "the Clojure nil, the empty-handed result."
            ),
            resolution=(
                "the trail's gate stood closed at the test; the body-arm "
                "was never walked, and the runtime — minding the order "
                "without skipping — turned back empty-handed, the "
                "closed-gate verdict spoken by silence."
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_04 = SubjectCurriculum(grade=5, subject_id="G5-04",
    subject_title="cond", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(cond (= 1 2) :a (= 1 1) :b :else :c)",
            expected=":b",
            concept_phrase="the multi-clause conditional",
            question_what="the value of the first arm whose stone reads true",
            goal_text="walk three condition-stones in order, taking the arm whose stone first reads true",
            scenario=(
                'The trail forked into three arms, each marked by a small condition-stone — the first carved `(= {drawn.a} {drawn.b})`, the second `(= {drawn.a} {drawn.a})`, the third `:else`.'
            ),
            need=(
                "Mossback the tortoise wanted the runtime to walk the "
                "stones in order and take the first arm whose stone "
                "read true."
            ),
            mapping=(
                "`cond` walks each (condition, value) pair in order. "
                "The first stone is false (skip), the second is true "
                "(take that arm; return its value); the third is never "
                "reached."
            ),
            resolution=(
                "the runtime walked past the failed first stone, found "
                "the second stone's test true, and — minding each part "
                "in its turn — handed back the value of the second arm, "
                "no further arms consulted."
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_05 = SubjectCurriculum(grade=5, subject_id="G5-05",
    subject_title="cond — :else", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(cond false :a false :b :else :c)",
            expected=":c",
            concept_phrase="the cond with default clause",
            question_what="the default value when no clauses match",
            goal_text="fall through all false conditions and return the default value",
            scenario=(
                "The trail forked three times. The first stone read "
                "`false`; the second also read `false`. At the end "
                "of the row stood a final post marked `:else` — the "
                "catch-all arm that was always open. The values drawn fresh were {drawn.a}, {drawn.b}, and {drawn.c}."
            ),
            need=(
                "Mossback needed the runtime to walk the stones in "
                "order and take the always-open arm when the other "
                "two were both closed."
            ),
            mapping=(
                "`cond` walks each condition in turn. Both early "
                "stones read false, so their arms are skipped. The "
                "`:else` clause is always true and acts as the "
                "default arm — the runtime takes it when everything "
                "else has been passed."
            ),
            resolution=(
                "both guarded arms were closed; the runtime reached "
                "the always-open default and returned the value "
                "waiting there."
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_06 = SubjectCurriculum(grade=5, subject_id="G5-06",
    subject_title="case", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(case 2 1 :one 2 :two 3 :three :default)",
            expected=":two",
            concept_phrase="the case statement",
            question_what="the matched branch",
            goal_text="match the value 2 against clauses and return the corresponding value",
            scenario=(
                'Three numbered gates stood along the path, each bearing a tag: gate {drawn.b} carried :one, gate {drawn.a} carried :two, gate {drawn.e} carried :three. A final unlabelled gate at the end carried :default.'
            ),
            need=(
                "Mossback arrived carrying the number {drawn.a} and needed to know which gate's tag the runtime would return."
            ),
            mapping=(
                '`case` compares the key value against each literal in turn. The key `{drawn.a}` matches the second gate, so its tag is returned; the other gates and the default are never opened.'
            ),
            resolution=(
                'the key matched gate {drawn.a}; the runtime returned the tag attached to that gate.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(case 99 1 :one 2 :two :default)",
            expected=":default",
            concept_phrase="the case statement with default",
            question_what="the default branch",
            goal_text="match the value 99 against clauses and return the default when no match is found",
            scenario=(
                'Two numbered gates — {drawn.b} and {drawn.d} — stood on the path with their tags. At the very end waited a gate with no number at all, labeled :default.'
            ),
            need=(
                'Mossback arrived carrying the number {drawn.a} — a key that matched neither numbered gate. She needed to know where the runtime would go.'
            ),
            mapping=(
                '`case` scans the numbered gates in order. Neither {drawn.b} nor {drawn.d} matches {drawn.a}, so both are passed. The un-numbered default gate is then taken, returning its tag.'
            ),
            resolution=(
                "no numbered gate matched; the runtime reached the "
                "default and returned the tag waiting there."
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_07 = SubjectCurriculum(grade=5, subject_id="G5-07",
    subject_title="and / or as control flow", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(and 1 2 3)",
            expected=3,
            concept_phrase="the and conjunction",
            question_what="the last truthy value",
            goal_text="return the last value when all values are truthy",
            scenario=(
                'Three wooden gates stood in a row on the trail — each one labeled with a value: the first `{drawn.a}`, the second `{drawn.b}`, the third `{drawn.c}`. All three were swung open.'
            ),
            need=(
                "Mossback needed to walk through all three gates and "
                "discover what the `and` form returned when every gate "
                "was passable."
            ),
            mapping=(
                "`and` tests each value in turn. A falsy gate closes "
                "the path and returns that gate's value immediately. "
                "When all gates are open, the runner passes through "
                "each one and returns the last value reached."
            ),
            resolution=(
                "all three gates were open; the runner passed through "
                "each in turn and returned the value of the last gate."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(or nil false :found)",
            expected=":found",
            concept_phrase="the or disjunction",
            question_what="the first truthy value",
            goal_text="return the first truthy value from a sequence of values",
            scenario=(
                "Three gates in a row — the first labeled `nil`, the "
                "second `false`, the third `:found`. An `or` runner "
                "needed to find the first gate she could pass through."
            ),
            need=(
                "Bramble the hare needed to know which gate would "
                "stop the runner and what value would be returned "
                "at the first open gate."
            ),
            mapping=(
                "`or` tests each value in turn, stopping at the first "
                "truthy one. `nil` is falsy — pass it. `false` is "
                "falsy — pass it. `:found` is truthy — stop here and "
                "return it."
            ),
            resolution=(
                "the first two gates were closed; the runner stopped "
                "at the third and returned the truthy value found there."
            ),
            tags=("story",),
        ),
    ], subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_08 = SubjectCurriculum(grade=5, subject_id="G5-08",
    subject_title="not", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(not (> 1 2))",
            expected=True,
            concept_phrase="the negation",
            question_what="the negated comparison",
            goal_text="negate the result of checking whether 1 is greater than 2",
            scenario=(
                "A flip-gate stood at the edge of the trail. It was "
                "wired backward: when the inner test was false, the "
                "flip-gate swung open (true); when the inner test "
                "was true, the flip-gate shut tight (false)."
            ),
            need=(
                'Mossback needed to know what the flip-gate returned after reading the carved comparison `(> {drawn.a} {drawn.b})`.'
            ),
            mapping=(
                '`not` wraps the inner comparison. `(> {drawn.a} {drawn.b})` is false because {drawn.a} is not greater than 2. `not` flips that result — false becomes the opposite.'           ),
            resolution=(
                "the inner comparison was false; the flip-gate inverted "
                "it and the gate returned the opposite truth value."
            ),
            tags=("story",),
        ),
    ], subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_09 = SubjectCurriculum(grade=5, subject_id="G5-09",
    subject_title="fn as value", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="((fn [f x] (f (f x))) inc 5)",
            expected=7,
            concept_phrase="applying a function twice",
            question_what="the result of inc applied twice",
            goal_text="apply the inc function twice to 5",
            scenario=(
                "A recipe-card was pinned to a post on the trail. "
                "It read: 'Take a recipe `f` and a starting count "
                "`x`; apply `f` to `x`, then apply `f` to the "
                "result.' Two applications of the same step."
            ),
            need=(
                "Mossback arrived carrying the recipe `inc` and the "
                "starting count `5`. She needed to know the final "
                "count after the card's double-step was followed."
            ),
            mapping=(
                "The `fn` is the recipe itself — it takes `f` and "
                "`x` as ingredients. It applies `f` to `x` once "
                "to get an intermediate count, then applies `f` "
                "again to that count to produce the final result."
            ),
            resolution=(
                "the recipe ran twice; the final count after two "
                "applications of the step came back."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_10 = SubjectCurriculum(grade=5, subject_id="G5-10",
    subject_title="map", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(map inc [1 2 3])",
            expected=[2,3,4],
            concept_phrase="mapping increment over a vector",
            question_what="the sequence produced by passing the vector containing 1, 2, and 3 through the inc-sieve",
            goal_text="pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collecting each transformed element",
            scenario=(
                "A row of three small acorns lay on a flat stone — "
                "the morning's first gathering, with counts of 1, 2, "
                "and 3."
            ),
            need=(
                "Each acorn was missing a single bud at the cap. "
                "Mossback the tortoise wanted to add one bud to every "
                "acorn before sending the row to market — without "
                "pulling the row apart."
            ),
                mapping=(
                "`map` is a sieve with a rule attached at its mouth. "
                "Pour the row through, and each acorn passes the rule — "
                "here, `inc`, adding one bud — coming out the other "
                "side budded by one. The shape stays a row; only the "
                "counts step up."
            ),
            resolution=(
                "what landed below the sieve was the same three acorns, "
                "each budded one more — counts of 2, 3, and 4."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(map #(* % %) [1 2 3 4])",
            expected=[1,4,9,16],
            concept_phrase="mapping a squaring operation over a vector",
            question_what="the sequence produced by mapping a squaring rule over the vector containing 1, 2, 3, and 4",
            goal_text="apply a squaring operation to each element of the vector [1 2 3 4] returning a sequence",
            scenario=(
                "A row of four acorn-caps lay on the flat stone — "
                "counts of 1, 2, 3, and 4. A second sieve waited, "
                "its rule written on a tag: multiply each count by "
                "itself before letting it through."
            ),
            need=(
                "Mossback needed to pour the row through the "
                "squaring-sieve and collect the transformed counts "
                "on the other side."
            ),
            mapping=(
                "`map` pours each element through the attached rule "
                "in order. Here the rule is `#(* % %)`, which "
                "multiplies each count by itself. Each acorn-cap "
                "passes through the rule and comes out as its "
                "squared value."
            ),
            resolution=(
                "the four acorn-caps passed through the squaring-sieve "
                "one by one, emerging as a new row of transformed counts."
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_11 = SubjectCurriculum(grade=5, subject_id="G5-11",
    subject_title="filter", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(filter even? [1 2 3 4])",
            expected=[2,4],
            concept_phrase="filtering even elements from a vector",
            question_what="the sequence produced by filtering even? over the vector containing 1, 2, 3, and 4",
            goal_text="keep the even elements from the vector [1 2 3 4]",
            scenario=(
                "A row of four pebbles — counts 1, 2, 3, and 4 — "
                "approached a sieve whose mesh let through only even "
                "counts. Odd ones were caught and held back. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Mossback needed to collect only the pebbles whose "
                "count was even after pouring the whole row through "
                "the `even?` sieve."
            ),
            mapping=(
                "`filter` pours each element through the predicate "
                "rule. Pebbles where `even?` is true pass through; "
                "pebbles where it is false are caught in the mesh "
                "and discarded. The output is a shorter row."
            ),
            resolution=(
                "the odd pebbles were caught; only those with even "
                "counts passed through and formed the output row."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(filter pos? [-2 -1 0 1 2])",
            expected=[1,2],
            concept_phrase="filtering positive elements from a vector",
            question_what="the sequence produced by filtering pos? over the vector containing -2, -1, 0, 1, and 2",
            goal_text="keep the positive elements from the vector [-2 -1 0 1 2]",
            scenario=(
                "Five pebbles lay in a row — counts -2, -1, 0, 1, "
                "and 2. A sieve with the `pos?` rule waited: only "
                "pebbles with a strictly positive count would pass. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Bramble the hare needed to pour the row through "
                "the positive-sieve and find out which pebbles "
                "made it through."
            ),
            mapping=(
                "`filter` applies `pos?` to each pebble in turn. "
                "Negative counts and zero are not positive — they "
                "are stopped by the mesh. Only pebbles with counts "
                "above zero pass through."
            ),
            resolution=(
                "the non-positive pebbles were caught in the mesh; "
                "only those with positive counts emerged on the "
                "other side."
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_12 = SubjectCurriculum(grade=5, subject_id="G5-12",
    subject_title="reduce", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(reduce + [1 2 3 4])",
            expected=10,
            concept_phrase="the fold operation",
            question_what="the running tally after walking 1, 2, 3, 4 with + as the combine step",
            goal_text="walk the row of pebbles [1 2 3 4] carrying a tally that combines each with + into the running total",
            scenario=(
                "A row of four small pebbles lay along the path — "
                "counts of 1, 2, 3, and 4 from four foraging trips. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Mossback the tortoise wanted the grand total of the "
                "four trips. Walking the row and carrying a running "
                "tally was the patient way."
            ),
            mapping=(
                "`reduce` walks the collection from left to right "
                "carrying a tally. At each pebble, the combine "
                "function (here `+`) is applied to (tally, pebble), "
                "producing the new tally. The final tally is what "
                "comes back."
            ),
            resolution=(
                "the walk produced a tally that grew across the four "
                "pebbles, ending at the grand total of all four "
                "trips."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(reduce * [1 2 3 4 5])",
            expected=120,
            concept_phrase="the fold operation",
            question_what="the product produced by walking 1, 2, 3, 4, 5 with * as the combine step",
            goal_text="fold * over the vector [1 2 3 4 5] computing their product",
            scenario=(
                "A row of five pebbles lay along the path — counts "
                "1, 2, 3, 4, and 5 from five foraging trips. Mossback "
                "needed a running product rather than a running sum. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "She would walk the row carrying a tally that "
                "started at the first pebble and multiplied in "
                "each successive pebble until the row was done."
            ),
            mapping=(
                "`reduce` walks the collection left to right. At "
                "each pebble, the combine function `*` is applied "
                "to (tally, pebble), giving the new tally. After "
                "five pebbles the running product is complete."
            ),
            resolution=(
                "the walk multiplied five pebbles into a single "
                "running product that was the answer."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(reduce max [3 1 4 1 5 9 2 6])",
            expected=9,
            concept_phrase="the fold operation",
            question_what="the largest pebble found by walking [3 1 4 1 5 9 2 6] with max as the combine step",
            goal_text="fold max over the vector [3 1 4 1 5 9 2 6] finding the maximum",
            scenario=(
                "Eight pebbles of varying size lay along the trail. "
                "Mossback wanted the largest without lifting all eight "
                "at once — she would carry the current champion and "
                "compare it to each new pebble as she walked. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Walking the row with `max` as the combine step "
                "would keep the larger of (tally, pebble) at each "
                "step, ending with the largest pebble overall."
            ),
            mapping=(
                "`reduce` with `max` walks left to right; at each "
                "pebble it keeps whichever is larger — the running "
                "champion or the new pebble. After the full walk "
                "the champion is what remains."
            ),
            resolution=(
                "the walk compared every pebble against the running "
                "champion and returned the largest count found "
                "across all eight."
            ),
            tags=("story",),
        ),
    ], subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_13 = SubjectCurriculum(grade=5, subject_id="G5-13",
    subject_title="reduce with init", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(reduce + 100 [1 2 3])",
            expected=106,
            concept_phrase="the fold with initial value",
            question_what="the sum produced by walking 1, 2, 3 with + and an opening tally of 100",
            goal_text="fold + over the vector containing 1, 2, 3 starting from an initial accumulator of 100",
            scenario=(
                "Mossback set out already carrying a tally of {drawn.a} acorns in her basket — the count from yesterday's haul. Three more pebbles lay along today's path, labeled 1, 2, and 3. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "She wanted to walk today's row and add each "
                "pebble's count onto her existing tally, ending "
                "with the grand total across both days."
            ),
            mapping=(
                "`reduce` with an initial value starts the tally "
                "at that value rather than the first element. "
                "The combine function `+` adds each pebble in "
                "turn to the running tally, walking from left "
                "to right until the row is done."
            ),
            resolution=(
                'the three pebbles were walked into the tally that began at {drawn.a}, producing the combined total of all four values.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(reduce + 0 [])",
            expected=0,
            concept_phrase="the fold with initial value over empty sequence",
            question_what="the tally returned when walking an empty row with + and an opening tally of 0",
            goal_text="fold + over an empty sequence starting from an initial accumulator of 0",
            scenario=(
                'Mossback arrived at an empty patch of trail — no pebbles lay on it at all. She was already carrying a tally of {drawn.a} in her basket before the walk began.'
            ),
            need=(
                "With no pebbles to walk, she needed to know what "
                "`reduce` would return: the opening tally, or "
                "something else entirely."
            ),
            mapping=(
                "`reduce` with an initial value and an empty "
                "collection never takes a step — there is nothing "
                "to combine. The opening tally is returned "
                "unchanged as the result."
            ),
            resolution=(
                "the row was empty; the walk ended before it began "
                "and the opening tally came back as the result."
            ),
            tags=("story",),
        ),
    ], subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_14 = SubjectCurriculum(grade=5, subject_id="G5-14",
    subject_title="apply", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(apply + [1 2 3 4])",
            expected=10,
            concept_phrase="applying + to vector elements",
            question_what="the result of spreading the basket of 1, 2, 3, 4 as ingredients into +",
            goal_text="apply + to the elements of the vector [1 2 3 4]",
            scenario=(
                "A recipe-card for `+` was pinned at the post. "
                "Beside it sat a basket holding four acorns — counts "
                "1, 2, 3, and 4. `apply` would spread the basket's "
                "contents as individual ingredients into the recipe. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Mossback needed to know the total that came out "
                "when the basket was emptied into `+` all at once, "
                "rather than passed in one by one."
            ),
            mapping=(
                "`apply` takes the recipe and the basket, then "
                "spreads the basket's elements as the recipe's "
                "arguments. `+` receives all four counts as "
                "separate inputs and combines them."
            ),
            resolution=(
                "the basket was spread into the recipe; all four "
                "counts were combined and the total came back."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(apply max [3 1 4 1 5])",
            expected=5,
            concept_phrase="applying max to vector elements",
            question_what="the largest count found after spreading the basket of 3, 1, 4, 1, 5 into max",
            goal_text="apply max to the elements of the vector [3 1 4 1 5]",
            scenario=(
                "Five pebbles sat in a basket — counts 3, 1, 4, 1, "
                "and 5. A `max` recipe-card waited at the post, "
                "ready to receive all five pebbles at once and "
                "return the largest. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Bramble the hare needed the largest pebble-count "
                "from the basket and wanted `apply` to spread the "
                "five pebbles into `max` as a single call."
            ),
            mapping=(
                "`apply` unpacks the basket and passes each pebble "
                "as an argument to `max`. `max` then selects the "
                "largest of all five counts and returns it."
            ),
            resolution=(
                "the basket was spread into `max`; the largest "
                "count across all five pebbles came back."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_15 = SubjectCurriculum(grade=5, subject_id="G5-15",
    subject_title="comp", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="((comp inc inc) 5)",
            expected=7,
            concept_phrase="composing inc twice",
            question_what="the result of chaining two inc recipe-cards and applying them to 5",
            goal_text="compose two inc functions and apply them to 5",
            scenario=(
                "Two identical recipe-cards — each reading `inc` — "
                "were clipped together at the post. `comp` threaded "
                "them into a chain: the output of the first card "
                "flows directly into the mouth of the second."
            ),
            need=(
                "Mossback arrived with the count `5` and needed "
                "to know what came out the far end after the "
                "ingredient passed through both cards in sequence."
            ),
            mapping=(
                "`comp` chains recipes right-to-left: `inc` is "
                "applied first, then `inc` again on the result. "
                "The ingredient passes through both steps before "
                "the final value emerges."
            ),
            resolution=(
                "the count passed through both recipe-cards in "
                "sequence and the final stepped-up count came out."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="((comp str inc) 9)",
            expected="10",
            concept_phrase="composing str and inc",
            question_what="the result of chaining the str and inc recipe-cards and applying them to 9",
            goal_text="compose str and inc functions and apply them to 9",
            scenario=(
                "Two recipe-cards were clipped together: `inc` "
                "first, then `str`. The chain would step up the "
                "count and then convert the result into a label "
                "suitable for the signpost."
            ),
            need=(
                "Mossback needed the label that would appear on "
                "the signpost after the count `9` was stepped up "
                "and then converted to a string."
            ),
            mapping=(
                "`comp` chains `str` after `inc`: `inc` is applied "
                "first to the count, then `str` converts the "
                "incremented number into its string representation."
            ),
            resolution=(
                "the count was stepped up by one card, then turned "
                "into a string label by the second card, producing "
                "the final signpost text."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_16 = SubjectCurriculum(grade=5, subject_id="G5-16",
    subject_title="partial", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="((partial + 10) 5)",
            expected=15,
            concept_phrase="partial application of +",
            question_what="the result of applying the half-loaded + card pre-filled with 10 to the count 5",
            goal_text="apply + with 10 as the first argument and 5 as the second",
            scenario=(
                "A recipe-card for `+` was pinned at the post, but "
                "one ingredient slot was already filled: `10` had "
                "been pressed into the first slot before Mossback "
                "arrived. Only one slot remained open."
            ),
            need=(
                "Mossback arrived carrying the count `5`. She "
                "needed to know the total that came out when she "
                "slid `5` into the one remaining open slot."
            ),
            mapping=(
                "`partial` pre-fills the first argument of `+` "
                "with `10`, producing a new one-argument recipe. "
                "When `5` is supplied, the recipe adds both "
                "arguments and returns the total."
            ),
            resolution=(
                "the pre-filled `10` and the supplied `5` were "
                "combined by the recipe, and the total came back."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(map (partial * 3) [1 2 3])",
            expected=[3,6,9],
            concept_phrase="mapping partial multiplication over a vector",
            question_what="the sequence produced by mapping the half-loaded * card pre-filled with 3 over the vector containing 1, 2, and 3",
            goal_text="apply a partially applied multiplication to each element of the vector containing 1, 2, and 3",
            scenario=(
                "A row of three acorns — counts 1, 2, and {drawn.a} — waited at the sieve. The sieve's rule was a half-loaded recipe: `*` with the first slot pre-filled with `{drawn.a}`, ready to triple whatever acorn came through."
            ),
            need=(
                "Mossback needed to pour the row through the "
                "tripling-sieve and collect the scaled counts "
                "on the other side."
            ),
            mapping=(
                '`partial` fixes the first argument of `*` as `{drawn.a}`. The resulting one-slot recipe is given to `map` as the sieve rule. Each acorn-count is multiplied by {drawn.a} as it passes through.'
            ),
            resolution=(
                "all three acorns passed through the tripling-sieve "
                "one by one, emerging as a new row of scaled counts."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_17 = SubjectCurriculum(grade=5, subject_id="G5-17",
    subject_title="juxt", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="((juxt inc dec) 5)",
            expected=[6,4],
            concept_phrase="juxtaposing inc and dec",
            question_what="the pair of results produced by asking both the inc and dec recipe-cards about 5",
            goal_text="apply both inc and dec functions to 5 and return both results as a vector",
            scenario=(
                "Two recipe-cards — `inc` and `dec` — were propped "
                "side by side at the post. `juxt` would hand the "
                "same count to both cards at once and collect "
                "both answers into a single pair."
            ),
            need=(
                "Mossback wanted to know both the stepped-up and "
                "stepped-down result for the count `5` without "
                "making two separate trips."
            ),
            mapping=(
                "`juxt` applies each recipe to the same argument "
                "in turn. `inc` gets `5` and produces one answer; "
                "`dec` gets `5` and produces another. Both answers "
                "are gathered into a vector in the order of the "
                "recipes."
            ),
            resolution=(
                "both recipe-cards answered in order; the two "
                "results were gathered into a pair and returned."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_18 = SubjectCurriculum(grade=5, subject_id="G5-18",
    subject_title="some", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(some even? [1 3 5 8 7])",
            expected=True,
            concept_phrase="checking if any element satisfies a predicate",
            question_what="whether any pebble in 1, 3, 5, 8, 7 passes the even? sieve",
            goal_text="check if any element in the vector [1 3 5 8 7] is even",
            scenario=(
                "Five pebbles lay in a row — counts 1, 3, 5, 8, and "
                "7. A checking-sieve with the `even?` rule stood at "
                "the end, able to stop at the first pebble that "
                "passed the rule. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Mossback needed to know whether at least one pebble "
                "in the row would satisfy `even?` — she did not need "
                "all of them, just the first confirmation."
            ),
            mapping=(
                "`some` walks the row testing each pebble. It "
                "stops at the first pebble where the predicate is "
                "truthy and returns that truthy value. If no pebble "
                "passes, it returns nothing."
            ),
            resolution=(
                "a pebble in the row passed the even? rule; `some` "
                "stopped there and returned a truthy result "
                "confirming the find. The value drawn fresh was {drawn.a}."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(some neg? [1 2 3])",
            expected=None,
            concept_phrase="checking if any element satisfies a predicate",
            question_what="whether any pebble in 1, 2, 3 passes the neg? sieve",
            goal_text="check if any element in the vector containing 1, 2, and 3 is negative",
            scenario=(
                "Three pebbles — counts 1, 2, and 3 — lay in a row. "
                "The checking-sieve bore the `neg?` rule: it would "
                "stop at the first negative pebble and confirm the "
                "find."
            ),
            need=(
                "Bramble needed to know whether any pebble in the "
                "row was negative — a quick scan without examining "
                "each count manually."
            ),
            mapping=(
                "`some` tests each pebble with `neg?` in turn. "
                "None of the counts is negative, so the predicate "
                "is never satisfied. With no truthy result found, "
                "`some` returns nothing."
            ),
            resolution=(
                "no pebble in the row satisfied `neg?`; the sieve "
                "reached the end empty-handed and returned nothing."
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_19 = SubjectCurriculum(grade=5, subject_id="G5-19",
    subject_title="every?", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(every? pos? [1 2 3])",
            expected=True,
            concept_phrase="checking if all elements satisfy a predicate",
            question_what="whether every pebble in 1, 2, 3 passes the pos? sieve",
            goal_text="check if all elements in the vector containing 1, 2, and 3 are positive",
            scenario=(
                "Three pebbles — counts 1, 2, and 3 — lined up at "
                "the all-or-nothing sieve. Its `pos?` rule would "
                "pass the whole row only if every pebble satisfied "
                "the rule; one failure would close the gate. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Mossback needed to know whether every pebble in "
                "the row was positive — a strict all-or-nothing "
                "check before she could proceed."
            ),
            mapping=(
                "`every?` walks the row, testing each pebble with "
                "`pos?`. If any pebble fails, it returns false "
                "immediately. If all pass, it returns true after "
                "the full walk."
            ),
            resolution=(
                "every pebble in the row satisfied `pos?`; the "
                "sieve reached the end and confirmed that all "
                "passed."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(every? even? [1 2 3])",
            expected=False,
            concept_phrase="checking if all elements satisfy a predicate",
            question_what="whether every pebble in 1, 2, 3 passes the even? sieve",
            goal_text="check if all elements in the vector containing 1, 2, and 3 are even",
            scenario=(
                "Three pebbles — counts 1, 2, and 3 — lined up at "
                "the all-or-nothing sieve. Its `even?` rule required "
                "every pebble to be even; one odd pebble would "
                "close the gate immediately. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Bramble needed to know whether the entire row "
                "was even — a strict check that would fail the "
                "moment any pebble was odd."
            ),
            mapping=(
                "`every?` tests each pebble with `even?` in turn. "
                "The first pebble is odd, so the rule fails on the "
                "spot and the sieve returns the negative result "
                "without checking the rest."
            ),
            resolution=(
                "the first odd pebble failed the even? rule; the "
                "sieve closed at once and returned the negative "
                "result."
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_20 = SubjectCurriculum(grade=5, subject_id="G5-20",
    subject_title="take and drop", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(take 3 [10 20 30 40 50])",
            expected=[10,20,30],
            concept_phrase="taking elements from a sequence",
            question_what="the sequence produced by taking 3 elements from the row of 10, 20, 30, 40, 50",
            goal_text="take the first 3 elements from the vector [10 20 30 40 50]",
            scenario=(
                'Five pebbles lay in a row — counts 10, 20, 30, 40, and 50. A counting-sieve stood at the front with a gauge set to {drawn.a}: it would let the first three pebbles through and hold the rest back.'
            ),
            need=(
                "Mossback needed only the first three pebbles "
                "and wanted `take` to cut the row at the gauge "
                "without disturbing the original."
            ),
            mapping=(
                "`take` counts through the row from the front. "
                "It lets the first `n` elements pass and stops "
                "before the rest. The result is a new, shorter row "
                "containing only those first elements."
            ),
            resolution=(
                'the gauge stopped the sieve after three pebbles; the first {drawn.a} counts came through as the new row.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(drop 2 [10 20 30 40 50])",
            expected=[30,40,50],
            concept_phrase="dropping elements from a sequence",
            question_what="the sequence produced by dropping 2 elements from the row of 10, 20, 30, 40, 50",
            goal_text="drop the first 2 elements from the vector [10 20 30 40 50]",
            scenario=(
                'The same five pebbles — counts 10, 20, 30, 40, and 50. A skip-sieve stood at the front with its counter set to {drawn.a}: it would skip the first two pebbles and let the rest through.'
            ),
            need=(
                "Bramble needed to know which pebbles remained "
                "after the first two were skipped by the sieve."
            ),
            mapping=(
                "`drop` skips the first `n` elements and passes "
                "everything after them. The skipped pebbles are "
                "gone; the remaining pebbles form the new row."
            ),
            resolution=(
                "the first two pebbles were skipped; the remaining "
                "three counts passed through and formed the "
                "new row."
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_21 = SubjectCurriculum(grade=5, subject_id="G5-21",
    subject_title="distinct and sort", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(distinct [1 1 2 3 3 4])",
            expected=[1,2,3,4],
            concept_phrase="removing duplicates from a sequence",
            question_what="the sequence produced by passing [1 1 2 3 3 4] through the dedup-sieve",
            goal_text="remove duplicate elements from the vector [1 1 2 3 3 4]",
            scenario=(
                "Six pebbles lay in a row — counts 1, 1, 2, 3, 3, "
                "and 4 — with two duplicate pairs. A dedup-sieve "
                "stood at the end: the first time a count passed "
                "through it was kept; any repeat was held back. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Mossback needed a row of unique counts and wanted "
                "`distinct` to remove the copies without sorting "
                "or reordering the survivors."
            ),
            mapping=(
                "`distinct` is a sieve that remembers which counts "
                "have already passed. Each count is tested; if "
                "it is new it passes through; if it has been seen "
                "before it is caught and discarded."
            ),
            resolution=(
                "the duplicate pebbles were caught by the sieve; "
                "only the first occurrence of each count came "
                "through, producing the unique row."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(sort [3 1 2])",
            expected=[1,2,3],
            concept_phrase="sorting a sequence",
            question_what="the sequence produced by sorting the row of 3, 1, 2 into ascending order",
            goal_text="sort the vector containing 3, 1, and 2 in ascending order",
            scenario=(
                "Three pebbles lay scattered on the flat stone — "
                "counts 3, 1, and 2, in no particular order. "
                "A sorting-tray waited beside them: drop the "
                "pebbles in and they would slide into ascending "
                "order on their own. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Bramble needed the pebbles arranged from smallest "
                "to largest before she could continue tallying "
                "the morning's finds."
            ),
            mapping=(
                "`sort` takes the row and returns a new row with "
                "the same elements arranged in ascending natural "
                "order. The original row is not changed."
            ),
            resolution=(
                "the three pebbles were arranged in ascending "
                "order in the sorting-tray and the ordered row "
                "came back."
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_22 = SubjectCurriculum(grade=5, subject_id="G5-22",
    subject_title="recur — first taste", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))",
            expected=120,
            concept_phrase="a factorial computation via loop and recur",
            question_what="the factorial of 5 computed by walking a circuit",
            goal_text="walk a small circuit five times, multiplying a running tally by the current step each lap, until the step counter reaches zero",
            scenario=(
                "Mossback the tortoise wanted to compute 5! — the "
                "product 5 × 4 × 3 × 2 × 1 — without writing five "
                "separate multiplications."
            ),
            need=(
                "She'd walk a small circuit around a stone, each lap "
                "multiplying her tally by the current step, until the "
                "step counter reached zero — then return the tally."
            ),
            mapping=(
                "`loop`/`recur` is the circuit. `loop [n 5 acc 1]` "
                "starts the bindings; `recur` jumps back to the top "
                "with new bindings — `(dec n)` and `(* acc n)` — "
                "without growing the call-stack. The base case "
                "`(zero? n)` returns `acc`."
            ),
            resolution=(
                "lap after lap on the compact circuit, the counter fell "
                "while the tally grew; the accumulated product came back."
            ),
            tags=("story",),
        ),
    ], subplots=_CIRCUIT_SUBPLOTS, plan_pool=_PLAN_G5)


SUBJECTS = {s.subject_id: s for s in (
    G5_01, G5_02, G5_03, G5_04, G5_05, G5_06, G5_07, G5_08, G5_09, G5_10,
    G5_11, G5_12, G5_13, G5_14, G5_15, G5_16, G5_17, G5_18, G5_19, G5_20,
    G5_21, G5_22,
)}


def smoke_test() -> None:
    from mmllm.aesop.curriculum.generator import generate_subject
    for sid, sub in SUBJECTS.items():
        recs = generate_subject(sub, n_per_example=1, seed=0)
        for r in recs: assert r.tool_calls[0]["name"] == "eval"
    print(f"grade-5 tortoise-hare smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
