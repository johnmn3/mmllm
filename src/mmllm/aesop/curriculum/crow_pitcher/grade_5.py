"""Grade 5 — control flow + higher-order intro. Through crow-pitcher."""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.crow_pitcher.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS,
    _GOAL_SUBPLOTS,
    _PLAN_POOL,
)
from mmllm.aesop.curriculum.crow_pitcher._metaphor_pools import (
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
    subject_title="if", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(if true :a :b)",
            expected=":a",
            concept_phrase="the conditional",
            question_what="which of :a or :b is returned",
            goal_text="choose between :a and :b based on a true condition",

            scenario=(
                "Sable perched above the pitcher's mouth at the orchard's "
                "edge, the fork-path clear below: one branch drops a stone "
                "marked :a, the other drops one marked :b. She tested "
                "the condition first."
            ),
            need=(
                "The condition was `true` — already settled. She needed to "
                "know which branch would release its stone into the pitcher."
            ),
            mapping=(
                "`if` reads the condition first: if truthy, the then-branch "
                "releases; if falsy, the else-branch releases. `true` is "
                "unmistakably truthy — the :a branch releases, :b stays back."
            ),
            resolution=(
                ":a — the then-branch released its stone, the :b stone "
                "resting where it was, the water rising one mark. (with {drawn.a} folded in)"
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
                "Caw stood at the fork-path above the garden pitcher, "
                "a stone marked :a on the left branch and one marked :b "
                "on the right. The condition stone beneath the fork read `false`."
            ),
            need=(
                "She needed to know which branch would open — the false "
                "condition had to route her to the correct stone."
            ),
            mapping=(
                "`if` tests the condition: `false` is falsy, so the "
                "then-branch stays closed and the else-branch releases. "
                "The :b stone is the one that drops."
            ),
            resolution=(
                "The else-branch opened and released its stone, "
                "the water rising one mark in the pitcher. (with {drawn.a} folded in)"
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
                "Korvus rested at the village pitcher's rim, the fork-path "
                "above it holding two stones: :a on the left, :b on the right. "
                "A comparison stone inscribed `(> 5 3)` sat in the test-groove."
            ),
            need=(
                "He needed to evaluate the comparison first to know which "
                "branch would open and which stone would drop."
            ),
            mapping=(
                "`>` checks whether 5 exceeds 3 — it does, so the comparison "
                "returns truthy. `if` sees truthy and opens the then-branch, "
                "releasing the :a stone."
            ),
            resolution=(
                "The then-branch opened, its stone dropping into the "
                "pitcher as the comparison resolved truthy. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_02 = SubjectCurriculum(grade=5, subject_id="G5-02",
    subject_title="if as expression", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(+ 1 (if true 10 20))",
            expected=11,
            concept_phrase="the arithmetic expression with conditional",
            question_what="the result of adding 1 to the conditional value",
            goal_text="add 1 to the result of choosing between 10 and 20 based on a true condition",

            scenario=(
                "Sable perched at the orchard pitcher with two stones ready: "
                "10 on the true-branch, 20 on the false-branch. A separate "
                "stone marked 1 waited on the rim to join whichever stone dropped."
            ),
            need=(
                "She needed to know which stone the fork released, then add "
                "the rim-stone of 1 to it to raise the water level."
            ),
            mapping=(
                "`if` is an expression — it evaluates to a value. `true` "
                "picks 10. Then `+` adds 1 to that result. The fork resolves "
                "first; the addition uses whatever the fork produced."
            ),
            resolution=(
                "The true-branch stone dropped, the rim-stone joined it, "
                "and the water rose by the combined count. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_03 = SubjectCurriculum(grade=5, subject_id="G5-03",
    subject_title="when", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(when true :yes)",
            expected=":yes",
            concept_phrase="the when conditional",
            question_what="the value when the condition is true",
            goal_text="evaluate a when form with a true condition",

            scenario=(
                "Korvus examined the meadow pitcher's single-branch fork: "
                "one stone marked :yes sat poised above the opening. "
                "No second branch existed — only the one guarded by `when`."
            ),
            need=(
                "He needed to know whether the lone stone would drop. "
                "The condition `true` governed the only branch."
            ),
            mapping=(
                "`when` is a one-armed `if`: it releases the body only when "
                "the condition is truthy. With `true`, the gate opens and "
                "the :yes stone drops; there is no else-branch."
            ),
            resolution=(
                "The gate opened and the :yes stone fell into the pitcher, "
                "the water rising one mark."
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
                "Caw stood at the farm pitcher's single-branch fork, "
                "the :yes stone poised above the opening. The condition "
                "stone in the test-groove read `false`."
            ),
            need=(
                "She needed to know whether the stone would drop. "
                "With no else-branch, a failed condition leaves the pitcher empty."
            ),
            mapping=(
                "`when` opens its gate only for truthy conditions. `false` "
                "keeps the gate closed — no body evaluates, no stone drops, "
                "and the REPL returns nil."
            ),
            resolution=(
                "The gate stayed shut, no stone fell, and the pitcher "
                "returned nothing — nil settled into the result. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_04 = SubjectCurriculum(grade=5, subject_id="G5-04",
    subject_title="cond", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(cond (= 1 2) :a (= 1 1) :b :else :c)",
            expected=":b",
            concept_phrase="the multi-clause conditional",
            question_what="the value of the first arm whose stone reads true",
            goal_text="walk three condition-stones in order, taking the arm whose stone first reads true",

            scenario=(
                "Sable stood at the road pitcher before three branch-pairs, "
                "each pair holding a test-stone and a result-stone. She would "
                "read the test-stones in order: `(= 1 2)`, `(= 1 1)`, `:else`."
            ),
            need=(
                "She needed the first pair whose test-stone read true "
                "to release its result-stone into the pitcher."
            ),
            mapping=(
                "`cond` walks its clauses in order, evaluating each test. "
                "The first truthy test opens that arm's branch. `(= 1 2)` "
                "fails; `(= 1 1)` succeeds — the :b stone drops immediately."
            ),
            resolution=(
                "The second branch opened, its stone releasing into the "
                "pitcher; the remaining branches stayed closed. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_05 = SubjectCurriculum(grade=5, subject_id="G5-05",
    subject_title="cond — :else", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(cond false :a false :b :else :c)",
            expected=":c",
            concept_phrase="the cond with default clause",
            question_what="the default value when no clauses match",
            goal_text="fall through all false conditions and return the default value",

            scenario=(
                "Korvus paced the market pitcher's three branch-pairs: "
                "the first two test-stones both read `false`, each keeping "
                "its gate closed. A third pair bore the special `:else` marker."
            ),
            need=(
                "He needed to know which stone would drop after both "
                "earlier branches refused to open — whether the fallback triggered."
            ),
            mapping=(
                "`cond` walks in order. Both `false` conditions stay closed. "
                "`:else` is always truthy, so the final pair opens and "
                "the :c stone drops as the guaranteed default."
            ),
            resolution=(
                "Both earlier branches held fast; the :else gate swung open "
                "and the default stone fell into the pitcher. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_06 = SubjectCurriculum(grade=5, subject_id="G5-06",
    subject_title="case", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(case 2 1 :one 2 :two 3 :three :default)",
            expected=":two",
            concept_phrase="the case statement",
            question_what="the matched branch",
            goal_text="match the value 2 against clauses and return the corresponding value",

            scenario=(
                "Caw perched at the hilltop pitcher, a dispatch-board "
                "hanging above it with slots labelled 1, 2, and 3. Each slot "
                "held a paired stone: :one, :two, :three, plus a spare :default."
            ),
            need=(
                "She held a stone marked 2 and needed to find its matching "
                "slot, then release the paired stone into the pitcher."
            ),
            mapping=(
                "`case` reads the dispatch value and scans the literal "
                "clauses for an exact match. The 2 slot matches; its paired "
                ":two stone drops. No other slots are checked."
            ),
            resolution=(
                "The 2 slot clicked open and its paired stone dropped "
                "cleanly into the pitcher below."
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
                "Sable stood at the garden pitcher's dispatch-board, "
                "holding a stone marked 99. The board offered only slots "
                "labelled 1 and 2, with a bare :default stone in the corner."
            ),
            need=(
                "She needed to know what happened when the dispatch value "
                "matched no labelled slot on the board."
            ),
            mapping=(
                "`case` scans the literal clauses; 99 matches neither 1 nor 2. "
                "When no slot fits, the trailing default stone is released "
                "as the fallback result."
            ),
            resolution=(
                "No slot matched, so the default stone slid into the "
                "pitcher — the fallback answer delivered."
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_07 = SubjectCurriculum(grade=5, subject_id="G5-07",
    subject_title="and / or as control flow", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(and 1 2 3)",
            expected=3,
            concept_phrase="the and conjunction",
            question_what="the last truthy value",
            goal_text="return the last value when all values are truthy",

            scenario=(
                "Korvus stood at the orchard pitcher's dual-gate, "
                "the stones queued: 1, 2, then 3. Both gates had to "
                "close in order before the final stone could drop through."
            ),
            need=(
                "He needed to know whether all the stones passed the "
                "dual-gate check and, if so, which stone emerged."
            ),
            mapping=(
                "`and` checks each value left to right. Any falsy value "
                "stops it and returns that value. All of 1, 2, 3 are truthy, "
                "so it walks all the way through and returns the last."
            ),
            resolution=(
                "All three passed the gate check; the final stone "
                "dropped through, the water rising to that level. (with {drawn.a} folded in)"
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
                "Caw examined the village pitcher's open-gate rail, "
                "the stones lined up: nil, false, then :found. "
                "The gate would release the first stone that proved truthy."
            ),
            need=(
                "She needed to know which stone would be the first to "
                "pass the truthy test and drop into the pitcher."
            ),
            mapping=(
                "`or` walks left to right, returning the first truthy value "
                "it finds. `nil` is falsy, `false` is falsy, but `:found` "
                "is truthy — it drops immediately without checking further."
            ),
            resolution=(
                "The first two stones were rejected; :found passed the "
                "test and fell through the gate into the pitcher. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_08 = SubjectCurriculum(grade=5, subject_id="G5-08",
    subject_title="not", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(not (> 1 2))",
            expected=True,
            concept_phrase="the negation",
            question_what="the negated comparison",
            goal_text="negate the result of checking whether 1 is greater than 2",

            scenario=(
                "Sable perched at the meadow pitcher with a comparison stone "
                "inscribed `(> 1 2)`. A flip-gate hung above the pitcher's "
                "mouth: it would invert whatever the comparison stone reported."
            ),
            need=(
                "She needed to know the comparison's result, then flip it "
                "through the inversion gate to find the final answer."
            ),
            mapping=(
                "`>` tests whether 1 exceeds 2 — it does not, so it returns "
                "false. `not` flips false to true. The gate inverts the "
                "comparison stone before it reaches the pitcher."
            ),
            resolution=(
                "The comparison stone read false; the flip-gate turned it "
                "over, and true dropped into the pitcher. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_09 = SubjectCurriculum(grade=5, subject_id="G5-09",
    subject_title="fn as value", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="((fn [f x] (f (f x))) inc 5)",
            expected=7,
            concept_phrase="applying a function twice",
            question_what="the result of inc applied twice",
            goal_text="apply the inc function twice to 5",

            scenario=(
                "Korvus at the farm pitcher carried a recipe-card `f` "
                "and a starting stone marked 5. The talon-scratched recipe "
                "read: apply f to x, then apply f to that result."
            ),
            need=(
                "He passed the `inc` recipe-card as `f` and the stone 5 "
                "as `x` — he needed the final stone after two inc-drops."
            ),
            mapping=(
                "`fn` accepts another function as a value. The body calls "
                "`(f (f x))` — `inc` fires on 5 producing a new stone, "
                "then `inc` fires again on that, producing the final result."
            ),
            resolution=(
                "Two applications completed; the stone that emerged "
                "from the second pass dropped into the pitcher. (count: 5)"
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_10 = SubjectCurriculum(grade=5, subject_id="G5-10",
    subject_title="map", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(map inc [1 2 3])",
            expected=[2,3,4],
            concept_phrase="mapping increment over a vector",
            question_what="the sequence produced by passing the vector containing 1, 2, and 3 through the inc-sieve",
            goal_text="pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collecting each transformed element",

            scenario=(
                "Caw stood at the road pitcher's sorting-perch, three "
                "stones — 1, 2, 3 — queued above the inc-sieve. Each stone "
                "would pass through the sieve before dropping into the pitcher."
            ),
            need=(
                "She needed every stone transformed by inc before it dropped, "
                "collecting the full transformed sequence as the result."
            ),
            mapping=(
                "`map` applies a function to every element in the sequence. "
                "Each stone passes through the inc-sieve, growing by one. "
                "All transformed stones are collected into a new sequence."
            ),
            resolution=(
                "Each stone passed through the inc-sieve in turn, and the "
                "transformed sequence fell into the pitcher below. (with {drawn.a} folded in)"
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
                "Sable arranged the stones — 1, 2, 3, 4 — at the market "
                "pitcher's sorting-perch, a squaring-groove carved into the "
                "sieve rail. Each stone would be multiplied by itself before dropping."
            ),
            need=(
                "She needed each stone squared and then collected into "
                "an ordered sequence dropped into the pitcher."
            ),
            mapping=(
                "`map` with the squaring anonymous function runs each stone "
                "through `(* % %)`. Every element is transformed before "
                "collection; the sequence preserves original order."
            ),
            resolution=(
                "Each stone passed through the squaring-groove; the "
                "resulting sequence of squared values fell into the pitcher. (count: 3)"
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_11 = SubjectCurriculum(grade=5, subject_id="G5-11",
    subject_title="filter", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(filter even? [1 2 3 4])",
            expected=[2,4],
            concept_phrase="filtering even elements from a vector",
            question_what="the sequence produced by filtering even? over the vector containing 1, 2, 3, and 4",
            goal_text="keep the even elements from the vector [1 2 3 4]",

            scenario=(
                "Korvus held four numbered stones over the pitcher's "
                "sorting-perch in the meadow: 1, 2, 3, 4. He would pass "
                "each stone over the test-groove before deciding which dropped."
            ),
            need=(
                "He wanted only even-numbered stones to fall into the "
                "pitcher — odd ones should stay on the rim, even ones pass through."
            ),
            mapping=(
                "`filter` applies a predicate — here `even?` — to each "
                "element in turn. Stones that pass the test drop; stones that "
                "fail remain. The result holds only the passing stones, in order."
            ),
            resolution=(
                "[2 4] — the two even stones fell through, the odd-numbered "
                "ones resting on the rim untouched. (with {drawn.a} folded in)"
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
                "Korvus lined five marked stones at the hilltop pitcher's "
                "sorting-perch: -2, -1, 0, 1, 2. The test-groove was carved "
                "for `pos?` — only strictly positive stones could pass through."
            ),
            need=(
                "He needed only the positive-valued stones to fall into "
                "the pitcher; zero and negatives must remain on the rim."
            ),
            mapping=(
                "`filter` applies `pos?` to each stone in sequence. "
                "Negative stones and zero fail the groove; only stones "
                "with positive values drop through into the pitcher."
            ),
            resolution=(
                "The negative and zero stones stayed on the rim; only "
                "the qualifying stones fell through into the pitcher. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_12 = SubjectCurriculum(grade=5, subject_id="G5-12",
    subject_title="reduce", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(reduce + [1 2 3 4])",
            expected=10,
            concept_phrase="the fold operation",
            question_what="the running tally after walking 1, 2, 3, 4 with + as the combine step",
            goal_text="walk the row of pebbles [1 2 3 4] carrying a tally that combines each with + into the running total",

            scenario=(
                "Caw walked the garden tallywalk beside the stones in a "
                "row: 1, 2, 3, 4. She carried a running tally in her wing-cache, "
                "combining each stone with `+` as she stepped past."
            ),
            need=(
                "She needed the final tally after combining all the stones "
                "with addition, stone by stone from left to right."
            ),
            mapping=(
                "`reduce` walks the sequence, folding each element into an "
                "accumulator using the given function. Starting from the first "
                "stone, each step adds the next, building the running total."
            ),
            resolution=(
                "The tallywalk ended after the fourth stone; the running "
                "tally reached its final sum and dropped into the pitcher. (with {drawn.a} folded in)"
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
                "Sable paced the orchard tallywalk past the stones: "
                "1, 2, 3, 4, 5. Her wing-cache held a growing product, "
                "each stone multiplied into it as she passed."
            ),
            need=(
                "She needed the cumulative product after all the stones "
                "had been folded in with the `*` combine step."
            ),
            mapping=(
                "`reduce` with `*` multiplies each element into the "
                "accumulator in sequence. The tally starts with the first "
                "stone and multiplies in every subsequent stone."
            ),
            resolution=(
                "The five-stone walk completed; the accumulated product "
                "settled into the pitcher as the final result. (with {drawn.a} folded in)"
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
                "Korvus walked the village tallywalk past the stones: "
                "3, 1, 4, 1, 5, 9, 2, 6. His wing-cache held the current "
                "champion — the largest stone seen so far."
            ),
            need=(
                "He needed to find the largest stone in the row by comparing "
                "each new stone against the current champion using `max`."
            ),
            mapping=(
                "`reduce` with `max` keeps the largest value seen so far in "
                "the accumulator. Each step compares the new stone to the "
                "current champion; the greater one is retained."
            ),
            resolution=(
                "The walk completed; the champion stone that survived all "
                "comparisons dropped into the pitcher as the answer. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_13 = SubjectCurriculum(grade=5, subject_id="G5-13",
    subject_title="reduce with init", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(reduce + 100 [1 2 3])",
            expected=106,
            concept_phrase="the fold with initial value",
            question_what="the sum produced by walking 1, 2, 3 with + and an opening tally of 100",
            goal_text="fold + over the vector containing 1, 2, 3 starting from an initial accumulator of 100",

            scenario=(
                "Caw began the meadow tallywalk with an opening tally of 100 "
                "already scratched into her wing-cache. the stones — 1, 2, 3 "
                "— waited ahead; each would be added to the running total."
            ),
            need=(
                "She needed the final tally after walking all the stones "
                "with `+`, starting from an initial count of 100."
            ),
            mapping=(
                "`reduce` with an init value pre-loads the accumulator. "
                "The walk begins at 100, adds 1, then 2, then 3 — each "
                "step extending the tally from the seeded starting point."
            ),
            resolution=(
                "The three-stone walk finished; the tally, grown from its "
                "opening count, dropped into the pitcher as the result. (with {drawn.a} folded in)"
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
                "Sable stood at the farm pitcher before the tallywalk, "
                "an opening tally of 0 in her wing-cache. She looked down "
                "the row — the path was empty, no stones waited."
            ),
            need=(
                "She needed to know what value emerged when no stones "
                "were present to fold into the opening tally."
            ),
            mapping=(
                "`reduce` with an init and an empty sequence has no steps "
                "to execute. The initial value is returned unchanged, "
                "as no stone ever lands in the accumulator."
            ),
            resolution=(
                "No stones to walk; the init value itself fell "
                "into the pitcher, unchanged and complete. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_14 = SubjectCurriculum(grade=5, subject_id="G5-14",
    subject_title="apply", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(apply + [1 2 3 4])",
            expected=10,
            concept_phrase="applying + to vector elements",
            question_what="the result of spreading the basket of 1, 2, 3, 4 as ingredients into +",
            goal_text="apply + to the elements of the vector [1 2 3 4]",

            scenario=(
                "Korvus carried a stone-basket to the road pitcher, "
                "the stones inside — 1, 2, 3, 4. The recipe-card `+` waited "
                "above; the basket's contents would be spread as its arguments."
            ),
            need=(
                "He needed to pour the basket's stones out as separate "
                "arguments into `+` and collect the combined result."
            ),
            mapping=(
                "`apply` spreads the collection as individual arguments to "
                "the function — like tipping the basket stone by stone onto "
                "the recipe-card's ingredient slots, then evaluating."
            ),
            resolution=(
                "The basket poured its stones into the `+` recipe; "
                "the combined result dropped into the pitcher below. (with {drawn.a} folded in)"
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
                "Caw brought a basket of the stones — 3, 1, 4, 1, 5 — "
                "to the market pitcher. The `max` recipe-card was ready; "
                "she tipped the basket to spread all stones as arguments."
            ),
            need=(
                "She needed to find the largest stone after spreading "
                "the basket into `max` without walking a tallywalk manually."
            ),
            mapping=(
                "`apply` unpacks the vector and passes each element as "
                "a separate argument to `max`. All the stones land at "
                "once on the recipe-card, and max picks the largest."
            ),
            resolution=(
                "All the stones landed on the max-card; the largest "
                "stone was identified and dropped into the pitcher. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_15 = SubjectCurriculum(grade=5, subject_id="G5-15",
    subject_title="comp", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="((comp inc inc) 5)",
            expected=7,
            concept_phrase="composing inc twice",
            question_what="the result of chaining two inc recipe-cards and applying them to 5",
            goal_text="compose two inc functions and apply them to 5",

            scenario=(
                "Sable stood at the hilltop pitcher with two inc recipe-cards "
                "talon-scratched in sequence. A stone marked 5 would pass "
                "through the first card, then immediately through the second."
            ),
            need=(
                "She needed to feed 5 through both cards in the correct "
                "right-to-left order and read the stone that emerged."
            ),
            mapping=(
                "`comp` chains functions right to left. The rightmost inc "
                "fires first on 5, the leftmost fires on that result. "
                "The composed card acts as a single two-step recipe."
            ),
            resolution=(
                "The stone passed through both inc cards in sequence; "
                "the twice-incremented value dropped into the pitcher. (count: 5)"
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
                "Korvus at the garden pitcher held two different recipe-cards "
                "talon-scratched in a chain: `str` on the left, `inc` on the right. "
                "A stone marked 9 waited to pass through both."
            ),
            need=(
                "He needed 9 incremented first, then converted to a string — "
                "two different transformations chained in the correct order."
            ),
            mapping=(
                "`comp` applies right to left: `inc` fires first on 9, "
                "then `str` fires on the result. The stone changes kind "
                "as well as count when it exits the second card."
            ),
            resolution=(
                "The stone left inc as a number, then passed through str "
                "and emerged as a string in the pitcher. (count: 9)"
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_16 = SubjectCurriculum(grade=5, subject_id="G5-16",
    subject_title="partial", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="((partial + 10) 5)",
            expected=15,
            concept_phrase="partial application of +",
            question_what="the result of applying the half-loaded + card pre-filled with 10 to the count 5",
            goal_text="apply + with 10 as the first argument and 5 as the second",

            scenario=(
                "Caw talon-scratched a half-loaded recipe-card at the orchard "
                "pitcher: `+` with the first ingredient slot already filled "
                "with 10. A stone marked 5 waited to fill the remaining slot."
            ),
            need=(
                "She needed to drop the stone 5 into the remaining slot of "
                "the pre-loaded card and read the combined result."
            ),
            mapping=(
                "`partial` bakes arguments into a function, returning a new "
                "function waiting for the rest. The half-card holds 10; "
                "calling it with 5 completes the addition."
            ),
            resolution=(
                "The 5 stone filled the open slot; the half-loaded card "
                "completed its recipe and dropped the result into the pitcher."
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
                "Sable set up the village pitcher's sorting-perch with "
                "a half-loaded `*` card pre-filled with 3. the stones — "
                "1, 2, 3 — queued to pass through it one by one."
            ),
            need=(
                "She needed each stone multiplied by 3 in turn, the "
                "transformed sequence collected into the pitcher."
            ),
            mapping=(
                "`partial` creates a reusable single-argument card. `map` "
                "feeds each stone into that card, tripling each element. "
                "The partial card acts as the sieve rule for the whole row."
            ),
            resolution=(
                "Each stone passed through the tripling card; the "
                "transformed sequence fell into the pitcher in order. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_17 = SubjectCurriculum(grade=5, subject_id="G5-17",
    subject_title="juxt", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="((juxt inc dec) 5)",
            expected=[6,4],
            concept_phrase="juxtaposing inc and dec",
            question_what="the pair of results produced by asking both the inc and dec recipe-cards about 5",
            goal_text="apply both inc and dec functions to 5 and return both results as a vector",

            scenario=(
                "Korvus stood at the meadow pitcher with two recipe-cards "
                "side by side: `inc` and `dec`. A single stone marked 5 "
                "would be passed to both cards simultaneously."
            ),
            need=(
                "He needed both the incremented and decremented readings "
                "of 5 at once, collected into a paired result."
            ),
            mapping=(
                "`juxt` applies each function to the same argument in turn, "
                "collecting all results into a vector. The stone 5 is given "
                "to inc and to dec; both answers are returned together."
            ),
            resolution=(
                "Both cards evaluated 5 in turn; their results were "
                "gathered into a paired vector and dropped into the pitcher."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_18 = SubjectCurriculum(grade=5, subject_id="G5-18",
    subject_title="some", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(some even? [1 3 5 8 7])",
            expected=True,
            concept_phrase="checking if any element satisfies a predicate",
            question_what="whether any pebble in 1, 3, 5, 8, 7 passes the even? sieve",
            goal_text="check if any element in the vector [1 3 5 8 7] is even",

            scenario=(
                "Caw carried the stones — 1, 3, 5, 8, 7 — to the farm "
                "pitcher's sorting-perch. She needed only to know whether "
                "any stone would pass the even? test-groove."
            ),
            need=(
                "She needed a yes-or-no answer: does at least one stone "
                "in the row pass the even? sieve, or do none?"
            ),
            mapping=(
                "`some` walks the sequence with the predicate, returning "
                "the first truthy result it finds. As soon as one stone "
                "passes even?, `some` stops and reports that finding."
            ),
            resolution=(
                "A stone passing the even? sieve was found; `some` "
                "reported its truthy confirmation into the pitcher. (with {drawn.a} folded in)"
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
                "Sable passed the stones — 1, 2, 3 — over the road "
                "pitcher's neg? test-groove, searching for any stone "
                "that would fall through as negative."
            ),
            need=(
                "She needed to know whether the row contained even one "
                "negative stone — if none existed, what would the pitcher return."
            ),
            mapping=(
                "`some` walks each stone over the neg? groove. All of "
                "1, 2, 3 are positive — none pass. When no stone satisfies "
                "the predicate, `some` returns nil."
            ),
            resolution=(
                "No stone passed the neg? groove; the pitcher received "
                "nil — confirmation that none qualified. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_19 = SubjectCurriculum(grade=5, subject_id="G5-19",
    subject_title="every?", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(every? pos? [1 2 3])",
            expected=True,
            concept_phrase="checking if all elements satisfy a predicate",
            question_what="whether every pebble in 1, 2, 3 passes the pos? sieve",
            goal_text="check if all elements in the vector containing 1, 2, and 3 are positive",

            scenario=(
                "Korvus lined the stones — 1, 2, 3 — at the market "
                "pitcher's sorting-perch. The pos? test-groove would inspect "
                "every stone; all had to pass for the gate to confirm."
            ),
            need=(
                "He needed to know whether every single stone cleared "
                "the pos? groove without exception."
            ),
            mapping=(
                "`every?` applies the predicate to each element; if any "
                "fails, it returns false immediately. All of 1, 2, 3 are "
                "positive — the predicate holds for every stone."
            ),
            resolution=(
                "All the stones cleared the pos? groove; the sorting-perch "
                "confirmed the unanimous result into the pitcher. (with {drawn.a} folded in)"
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
                "Caw arranged the stones — 1, 2, 3 — at the hilltop "
                "pitcher's sorting-perch. The even? test-groove had to "
                "approve every stone, or the whole check would fail."
            ),
            need=(
                "She needed to know whether the entire row was even — "
                "a single odd stone would break the unanimous requirement."
            ),
            mapping=(
                "`every?` checks all elements; one failure ends the "
                "check immediately with false. Stone 1 is odd — the groove "
                "rejects it and the check reports false without continuing."
            ),
            resolution=(
                "The first odd stone failed the groove; the check ended "
                "early and false fell into the pitcher. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_20 = SubjectCurriculum(grade=5, subject_id="G5-20",
    subject_title="take and drop", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(take 3 [10 20 30 40 50])",
            expected=[10,20,30],
            concept_phrase="taking elements from a sequence",
            question_what="the sequence produced by taking 3 elements from the row of 10, 20, 30, 40, 50",
            goal_text="take the first 3 elements from the vector [10 20 30 40 50]",

            scenario=(
                "Sable stood at the garden pitcher's sorting-perch before "
                "a row of the stones — 10, 20, 30, 40, 50. She would claim "
                "only the first three, leaving the rest on the rim."
            ),
            need=(
                "She needed exactly the first the stones in order, "
                "stopping before the fourth regardless of what remained."
            ),
            mapping=(
                "`take` collects the first n elements from the front of "
                "the sequence and stops. It never touches elements beyond "
                "the count — the trailing stones rest undisturbed."
            ),
            resolution=(
                "The first the stones dropped into the pitcher in order; "
                "the remaining two stayed on the rim untouched. (with {drawn.a} folded in)"
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
                "Korvus faced the orchard pitcher's sorting-perch, a row "
                "of the stones — 10, 20, 30, 40, 50 — ahead. He would "
                "skip past the first two and collect only what remained."
            ),
            need=(
                "He needed all stones after the first two, ignoring those "
                "already skipped, in their original order."
            ),
            mapping=(
                "`drop` discards the first n elements and returns the rest. "
                "The first two stones are skipped entirely; the remaining "
                "stones fall through in sequence."
            ),
            resolution=(
                "The first two stones were skipped; the remaining stones "
                "fell into the pitcher in their original order. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_21 = SubjectCurriculum(grade=5, subject_id="G5-21",
    subject_title="distinct and sort", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(distinct [1 1 2 3 3 4])",
            expected=[1,2,3,4],
            concept_phrase="removing duplicates from a sequence",
            question_what="the sequence produced by passing [1 1 2 3 3 4] through the dedup-sieve",
            goal_text="remove duplicate elements from the vector [1 1 2 3 3 4]",

            scenario=(
                "Caw poured the stones — 1, 1, 2, 3, 3, 4 — onto the "
                "village pitcher's dedup-sieve, where repeated values would "
                "be blocked from passing through a second time."
            ),
            need=(
                "She needed only first-seen stones to fall through, "
                "with all later duplicates barred from dropping."
            ),
            mapping=(
                "`distinct` passes each element through in order; any element "
                "already seen is blocked. First occurrences drop; repeats "
                "are held back, yielding a sequence of unique values."
            ),
            resolution=(
                "The duplicate stones were blocked at the sieve; only "
                "the unique first-seen stones fell into the pitcher. (with {drawn.a} folded in)"
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
                "Sable gathered the stones — 3, 1, 2 — at the road "
                "pitcher's sorting-perch, where the sieve would reorder "
                "them before they dropped in."
            ),
            need=(
                "She needed the stones to fall into the pitcher in ascending "
                "order regardless of their original arrangement."
            ),
            mapping=(
                "`sort` rearranges all elements into natural ascending order "
                "before releasing them. The sorting-perch lines them up "
                "smallest first; they drop in that new order."
            ),
            resolution=(
                "The perch reordered the stones; they fell into the "
                "pitcher in ascending sequence, smallest landing first. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_22 = SubjectCurriculum(grade=5, subject_id="G5-22",
    subject_title="recur — first taste", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))",
            expected=120,
            concept_phrase="a factorial computation via loop and recur",
            question_what="the factorial of 5 computed by walking a circuit",
            goal_text="walk a small circuit five times, multiplying a running tally by the current step each lap, until the step counter reaches zero",

            scenario=(
                "Caw stood at the pitcher's rim in the hilltop field, a "
                "circuit chalked beneath her feet: start with n=5 and "
                "accumulator=1. Each lap, multiply the accumulator by n, "
                "step n down by one — loop without lifting from the rim."
            ),
            need=(
                "She needed to run the circuit until n hit zero, then read "
                "the final accumulated count as the answer."
            ),
            mapping=(
                "`loop` opens the circuit with initial bindings. `recur` "
                "loops back to the top without growing the call stack — no "
                "new flight, just another lap. When the zero-check passes "
                "`acc` is returned as the result."
            ),
            resolution=(
                "120 — five laps, the accumulator multiplied each pass, "
                "the final product surfacing when n hit zero. (count: 5)"
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
    print(f"grade-5 crow-pitcher smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
