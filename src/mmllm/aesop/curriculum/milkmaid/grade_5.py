"""Grade 5 — control flow + higher-order intro. through the milkmaid fable."""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.milkmaid.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS,
    _GOAL_SUBPLOTS,
    _PLAN_POOL,
)
from mmllm.aesop.curriculum.milkmaid._metaphor_pools import (
    _CIRCUIT_SUBPLOTS, _FORK_SUBPLOTS, _GATE_SUBPLOTS, _RECIPE_SUBPLOTS, _SIEVE_SUBPLOTS, _TALLYWALK_SUBPLOTS,
)




def _ex(form, expected, concept, what, goal=""):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal)


_PLAN_G5 = _PLAN_POOL + (
    "I use map / filter / reduce as appropriate.",
    "I write the higher-order form so the REPL can compute.",
)


G5_01 = SubjectCurriculum(grade=5, subject_id="G5-01",
    subject_title="if", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(if true :a :b)",
            expected=":a",
            concept_phrase="the conditional",
            question_what="which of :a or :b is returned",
            goal_text="choose between :a and :b based on a true condition",
            scenario=(
                "On the road to market, the milkmaid reached a fork: the left lane "
                "led to the dairy buyer, the right lane to the grain merchant. "
                "The pail could only go one way."
            ),
            need=(
                "She needed a condition to read the sign and send the pail down the "
                "correct lane — only one branch walked, the other left untouched."
            ),
            mapping=(
                "`if` is the road fork: the form reads the condition, picks one "
                "branch, and the REPL walks only that branch. The other branch is "
                "never visited; the pail never splits."
            ),
            resolution=(
                "The REPL walked the left branch — the condition was true, the pail "
                "rolled down the chosen lane, and the other lane was never entered — :b."
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
                "The milkmaid reached the road fork on her way to market, pail "
                "in hand. The left lane led to the dairy buyer; the right lane "
                "to the grain merchant. The sign at the fork read false."
            ),
            need=(
                "She needed to read the condition at the fork and walk only the "
                "correct lane — the sign was false, so only one branch was ever "
                "entered."
            ),
            mapping=(
                "`if` is the road fork: the false condition closed the left "
                "lane and opened the right. The pail traveled only the right "
                "lane; the left was never walked."
            ),
            resolution=(
                "The REPL walked the right branch — the false condition sent "
                "the pail down the chosen lane, and the other lane was never "
                "entered — :b."
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
                "At the road fork, the milkmaid's tally-slate showed a "
                "comparison: five pails against three. She needed the fork to "
                "read the arithmetic sign before the pail could proceed."
            ),
            need=(
                "She needed the fork to evaluate whether five was greater than "
                "three, then send the pail down the matching lane — only one "
                "branch walked."
            ),
            mapping=(
                "`if` is the road fork: the comparison `(> 5 3)` is the "
                "sign the fork reads. Because it came back with the verdict, the left "
                "lane opened and the right was left untouched."
            ),
            resolution=(
                "The REPL walked the left branch — the comparison was true, "
                "the fork chose the first lane, and the pail rolled through "
                "without doubling back."
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_02 = SubjectCurriculum(grade=5, subject_id="G5-02",
    subject_title="if as expression", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(+ 1 (if true 10 20))",
            expected=11,
            concept_phrase="the arithmetic expression with conditional",
            question_what="the result of adding 1 to the conditional value",
            goal_text="add 1 to the result of choosing between 10 and 20 based on a true condition",
            scenario=(
                "The milkmaid arrived at the road fork carrying a base count "
                "of one coin already in her apron-pocket. The fork's sign was "
                "true, offering either the ten-coin lane or the twenty-coin "
                "lane."
            ),
            need=(
                "She needed to pick the lane that matched the sign, then add "
                "her one coin to whatever the chosen lane returned — the fork "
                "had to be read before the addition could be done."
            ),
            mapping=(
                "`if` is the road fork nested inside `+`: the fork picks the "
                "lane first, hands its value back to `+`, and the addition "
                "folds in the base coin. The whole expression is one "
                "combined step."
            ),
            resolution=(
                "The REPL returned the sum of the one base coin and the "
                "lane the true fork chose — a single combined value from "
                "one nested read — 20."
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_03 = SubjectCurriculum(grade=5, subject_id="G5-03",
    subject_title="when", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(when true :yes)",
            expected=":yes",
            concept_phrase="the when conditional",
            question_what="the value when the condition is true",
            goal_text="evaluate a when form with a true condition",
            scenario=(
                "The milkmaid paused at a one-lane fork on the road to "
                "market. The sign at the fork read true. There was only a "
                "forward lane and no branching alternative — if the sign "
                "permitted, she walked on; otherwise she stopped."
            ),
            need=(
                "She needed a fork that would send the pail forward when "
                "the condition was true and return nothing at all when it "
                "was not — a one-sided road fork, not a two-sided one."
            ),
            mapping=(
                "`when` is the one-sided road fork: it has only a forward "
                "lane. When the condition is true the pail rolls through; "
                "when false, the fork closes and the REPL gets back nothing."
            ),
            resolution=(
                "The REPL walked the forward lane — the true condition "
                "opened the one-sided fork and the pail passed through as "
                "written — yes — :yes."
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
                "The milkmaid stood at the same one-sided fork, pail ready. "
                "This time the sign read false. The lane ahead was the only "
                "option — there was no right turn, no alternative road."
            ),
            need=(
                "She needed to know what the one-sided fork returned when "
                "the sign was closed — with no alternative lane, the pail "
                "had nowhere to go."
            ),
            mapping=(
                "`when` with a false condition is a closed one-sided road "
                "fork: no lane opens, so no value comes back. The REPL "
                "receives nothing rather than an alternative."
            ),
            resolution=(
                "The REPL returned nothing — the false sign closed the "
                "single forward lane and the pail stayed at the fork — yes — :yes."
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_04 = SubjectCurriculum(grade=5, subject_id="G5-04",
    subject_title="cond", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(cond (= 1 2) :a (= 1 1) :b :else :c)",
            expected=":b",
            concept_phrase="the multi-clause conditional",
            question_what="the value of the first arm whose stone reads true",
            goal_text="walk three condition-stones in order, taking the arm whose stone first reads true",
            scenario=(
                "On the road to market, the milkmaid came to a series of "
                "three road forks set one after another. The first fork's "
                "stone read `(= 1 2)`. The second read `(= 1 1)`. A final "
                "stone bore the word `:else`."
            ),
            need=(
                "She needed to read the stones in order and enter the first "
                "lane whose stone came back with the verdict — skipping all earlier "
                "closed forks, never doubling back."
            ),
            mapping=(
                "`cond` is the row of road forks: each clause is a fork "
                "stone checked in order. The first stone that reads true "
                "opens that lane; the rest are never walked."
            ),
            resolution=(
                "The REPL entered the second fork's lane — the first stone "
                "was false, the second was true, and the pail rolled through "
                "that branch without reaching the fallback."
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_05 = SubjectCurriculum(grade=5, subject_id="G5-05",
    subject_title="cond — :else", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(cond false :a false :b :else :c)",
            expected=":c",
            concept_phrase="the cond with default clause",
            question_what="the default value when no clauses match",
            goal_text="fall through all false conditions and return the default value",
            scenario=(
                "The milkmaid reached a row of three road forks on the way to market. "
                "The first fork's stone read false; the second stone also read false. "
                "At the far end stood a last stone bearing the word `:else`."
            ),
            need=(
                "She needed the fork row to read each stone in order and, finding both "
                "early stones closed, fall through to the final fallback lane so the "
                "pail still reached market."
            ),
            mapping=(
                "`cond` with `:else` is the row of road forks ending in a guaranteed "
                "open lane: every earlier stone is checked in order; when all are false "
                "the `:else` stone opens the last lane unconditionally."
            ),
            resolution=(
                "The REPL entered the fallback lane — both earlier stones were false, "
                "so the pail rolled through the `:else` lane and the walk was complete."
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_06 = SubjectCurriculum(grade=5, subject_id="G5-06",
    subject_title="case", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(case 2 1 :one 2 :two 3 :three :default)",
            expected=":two",
            concept_phrase="the case statement",
            question_what="the matched branch",
            goal_text="match the value 2 against clauses and return the corresponding value",
            scenario=(
                'The milkmaid reached a signpost on the road to market. The post listed three lanes: one for the buyer who wanted one pail, one for the buyer who wanted the counts for three. Her pail count was two.'
            ),
            need=(
                "She needed the signpost to read her pail count and direct her pail "
                "down the matching lane without checking all the others."
            ),
            mapping=(
                "`case` is the signpost fork: it reads the dispatch value — her count — "
                "and jumps directly to the matching lane. No lane before or after it is "
                "walked; only the one with a matching marker."
            ),
            resolution=(
                "The REPL took the matching lane — the pail count matched the second "
                "marker, and the pail rolled through that lane alone — :default."
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
                "The milkmaid stood at a two-lane signpost with a pail count that matched "
                "neither marker. The listed lanes were for one and two pails; her count "
                "had no marker on the post."
            ),
            need=(
                "She needed the signpost to fall to a default lane when no marker "
                "matched, so the pail still reached market rather than stopping "
                "at the post."
            ),
            mapping=(
                "`case` with a default is the signpost with a final unmarked lane: "
                "when no earlier marker matches the dispatch value, that last open "
                "lane accepts the pail unconditionally."
            ),
            resolution=(
                "The REPL took the default lane — no listed marker matched the count, "
                "so the pail rolled through the final open lane to market — :default."
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_07 = SubjectCurriculum(grade=5, subject_id="G5-07",
    subject_title="and / or as control flow", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(and 1 2 3)",
            expected=3,
            concept_phrase="the and conjunction",
            question_what="the last truthy value",
            goal_text="return the last value when all values are truthy",
            scenario=(
                "The milkmaid arrived at the farmyard gate with three latch-checks "
                "to pass in sequence. She pressed on the first latch: it held. The "
                "second: it held. The third: it held."
            ),
            need=(
                "She needed all three gate-latches to hold before the gate would open "
                "and hand back whatever the last latch returned — if any latch failed, "
                "the gate would close there."
            ),
            mapping=(
                "`and` is the chain of farmyard gate-latches: each value is checked "
                "in order; if every value is truthy the gate opens and the last value "
                "passes through. The first falsy value closes the gate early."
            ),
            resolution=(
                "The REPL returned the last latch's value — every latch held, the gate "
                "opened fully, and the final value came through — 3."
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
                "The milkmaid stood at a farmyard gate with three latch-checks in "
                "sequence. The first latch returned nothing; the second returned the verdict. "
                "The third bore a keyword mark."
            ),
            need=(
                "She needed the gate to stop at the first latch that held — the moment "
                "a truthy value appeared, that value should pass through and the rest "
                "remain unchecked."
            ),
            mapping=(
                "`or` is the chain of gate-latches that stops at the first truthy one: "
                "nil and false are closed latches; the first truthy latch opens the gate "
                "and its value passes through immediately."
            ),
            resolution=(
                "The REPL returned the first truthy latch's keyword value — the gate stopped "
                "at the third latch and passed that value through without checking further — :found."
            ),
            tags=("story",),
        ),
    ], subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_08 = SubjectCurriculum(grade=5, subject_id="G5-08",
    subject_title="not", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(not (> 1 2))",
            expected=True,
            concept_phrase="the negation",
            question_what="the negated comparison",
            goal_text="negate the result of checking whether 1 is greater than 2",
            scenario=(
                "At the farmyard gate, the milkmaid found a latch-check: was one pail "
                "more than two? The inner check came back with the verdict — one was not greater "
                "than two. A `not` sign hung on the gate's outer frame."
            ),
            need=(
                "She needed the outer `not` to flip the gate-latch's result — false "
                "in, true out — so the gate opened when the comparison failed."
            ),
            mapping=(
                "`not` is the gate's flip-sign: it reads the inner latch result and "
                "reverses it. A false latch becomes a true gate; a true latch becomes "
                "a false gate. The comparison runs first, then the flip."
            ),
            resolution=(
                "The REPL returned the flipped result — the inner comparison was false, "
                "and `not` reversed it so the gate opened with `true` — 2."
            ),
            tags=("story",),
        ),
    ], subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_09 = SubjectCurriculum(grade=5, subject_id="G5-09",
    subject_title="fn as value", fable="milkmaid",
    examples=[
        SubjectExample(
            form="((fn [f x] (f (f x))) inc 5)",
            expected=7,
            concept_phrase="applying a function twice",
            question_what="the result of inc applied twice",
            goal_text="apply the inc function twice to 5",
            scenario=(
                "The farmer wrote a pail-steps card: 'apply the morning routine "
                "twice to the day's count.' She passed the `inc` instruction-slip "
                "and the starting count of 5 to the unnamed routine card."
            ),
            need=(
                "The milkmaid needed to follow the card's two-step recipe — apply "
                "`inc` to 5, then apply `inc` to the result — without inventing a "
                "new function or naming the card."
            ),
            mapping=(
                "`fn` is the nameless pail-steps card: it takes a routine slip `f` "
                "and a count `x`, and runs `f` twice in order. The card has no name "
                "on the wall; it is handed directly to the caller and used once."
            ),
            resolution=(
                "The REPL returned the count after two applications of `inc` — two "
                "steps of the recipe card run in sequence, exactly as written."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_10 = SubjectCurriculum(grade=5, subject_id="G5-10",
    subject_title="map", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(map inc [1 2 3])",
            expected=[2,3,4],
            concept_phrase="mapping increment over a vector",
            question_what="the sequence produced by passing the vector containing 1, 2, and 3 through the inc-sieve",
            goal_text="pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collecting each transformed element",
            scenario=(
                "The milkmaid held her milk-strainer over the pail and poured the "
                "morning's count through it — one pebble, then two, then three. The "
                "strainer's rule was to add one to every piece that passed."
            ),
            need=(
                "She needed each element to pass through the strainer's `inc` rule "
                "and come out the other side transformed, with nothing lost and nothing "
                "added beyond the transformation."
            ),
            mapping=(
                "`map` is the milk-strainer over the pail: each element enters the "
                "strainer, the rule runs on it, and the transformed piece drops into the "
                "collection below. Every piece passes through, none are skipped."
            ),
            resolution=(
                "The REPL returned the transformed sequence — each element came through "
                "the `inc` strainer one increment larger, collected in order — 3."
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
                "The milkmaid fitted a squaring rule to her milk-strainer and poured "
                "several counts through it: one, two, three, four. Each piece would come "
                "out multiplied by itself on the far side."
            ),
            need=(
                "She needed every count to pass through the squaring strainer and land "
                "in the collection below as its own square, in the same order they "
                "entered."
            ),
            mapping=(
                "`map` with the squaring anonymous rule is the strainer: each element "
                "enters, the rule squares it, and the squared piece drops into the "
                "sequence below. Every piece passes through unchanged in position."
            ),
            resolution=(
                "The REPL returned the squared sequence — each element came through "
                "multiplied by itself, collected in the original order — 4."
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_11 = SubjectCurriculum(grade=5, subject_id="G5-11",
    subject_title="filter", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(filter even? [1 2 3 4])",
            expected=[2,4],
            concept_phrase="filtering even elements from a vector",
            question_what="the sequence produced by filtering even? over the vector containing 1, 2, 3, and 4",
            goal_text="keep the even elements from the vector [1 2 3 4]",
            scenario=(
                "The milkmaid set her milk-strainer over the pail and poured four counts through: the counts. The strainer's mesh was set to let only even counts pass to the collection below."
            ),
            need=(
                "She needed the strainer to hold back the odd counts and let only "
                "even ones fall through — a selective pass, not a full pour."
            ),
            mapping=(
                "`filter` with `even?` is the selective milk-strainer: each element "
                "is tested by the rule; those that pass the test fall through the mesh; "
                "those that fail are held back and never enter the collection."
            ),
            resolution=(
                "The REPL returned the filtered sequence — only the even counts passed — 4 "
                "through the strainer's mesh, collected in order."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(filter pos? [-2 -1 0 1 2])",
            expected=[1,2],
            concept_phrase="filtering positive elements from a vector",
            question_what="the sequence produced by filtering pos? over the vector containing -2, -1, 0, 1, and 2",
            goal_text="keep the positive elements from the vector containing these numbers",
            scenario=(
                "Five counts passed through the milkmaid's strainer: two that read "
                "below zero, one at zero, two above zero. The strainer's rule was to "
                "let only positive counts fall through."
            ),
            need=(
                "She needed the strainer to hold back every count that was zero or "
                "below, passing only those that were strictly positive into the "
                "collection below."
            ),
            mapping=(
                "`filter` with `pos?` is the positive-only strainer: each count is "
                "tested; negative and zero counts are held back; only counts above "
                "zero fall through into the resulting sequence."
            ),
            resolution=(
                "The REPL returned the filtered sequence — only the positive counts — 2 — -1. "
                "cleared the strainer's mesh and entered the collection."
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_12 = SubjectCurriculum(grade=5, subject_id="G5-12",
    subject_title="reduce", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(reduce + [1 2 3 4])",
            expected=10,
            concept_phrase="the fold operation",
            question_what="the running tally after walking 1, 2, 3, 4 with + as the combine step",
            goal_text="walk the row of pebbles these numbers carrying a tally that combines each with + into the running total",
            scenario=(
                "The milkmaid walked to market counting coins step by step: one coin "
                "at the first stall, two at the second, three at the third, four at "
                "the fourth. At each stall she added the new coins to her running tally."
            ),
            need=(
                "She needed to step through each stall, combine its count into the "
                "running tally with `+`, and carry that tally forward to the next — "
                "one tally-walk, not four separate additions."
            ),
            mapping=(
                "`reduce` with `+` is the tally-walk: the milkmaid starts with the "
                "first element, then steps through the rest, combining each into the "
                "running total with the `+` step until the row is done."
            ),
            resolution=(
                "The REPL returned the accumulated total — the tally the milkmaid "
                "had built coin by coin across all four stalls — 4."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(reduce * [1 2 3 4 5])",
            expected=120,
            concept_phrase="the fold operation",
            question_what="the product produced by walking 1, 2, 3, 4, 5 with * as the combine step",
            goal_text="fold * over the vector containing these numbers, computing their product",
            scenario=(
                "The milkmaid walked five stations on the tally-walk, multiplying the running product by each station's count in turn: the counts. The product grew with every step."
            ),
            need=(
                "She needed to step through all five stations, multiply the running "
                "product by each new count, and carry the 5 forward — a "
                "multiplication tally-walk across the whole row."
            ),
            mapping=(
                "`reduce` with `*` is the multiplication tally-walk: the milkmaid "
                "starts with the first element and folds `*` across the rest, building "
                "the running product one step at a time."
            ),
            resolution=(
                "The REPL returned the accumulated product — the total the milkmaid "
                "had multiplied together step by step across all five stations."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(reduce max [3 1 4 1 5 9 2 6])",
            expected=9,
            concept_phrase="the fold operation",
            question_what="the largest pebble found by walking [3 1 4 1 5 9 2 6] with max as the combine step",
            goal_text="fold max over the vector containing these numbers, finding the maximum",
            scenario=(
                "The milkmaid walked eight market stalls, tally-slate in hand, keeping "
                "a running note of the highest coin count she had seen. At each stall "
                "she compared the new count to her running best and kept whichever "
                "was larger."
            ),
            need=(
                "She needed to step through every stall, fold `max` across the counts, "
                "and carry only the highest seen forward — a running-maximum tally-walk "
                "from start to finish."
            ),
            mapping=(
                "`reduce` with `max` is the peak-finding tally-walk: at each step the "
                "milkmaid compares the running best to the new count and keeps the "
                "larger one. After the last stall, the running best is the 6."
            ),
            resolution=(
                "The REPL returned the highest count found — the running maximum the "
                "milkmaid carried through every stall on the tally-walk."
            ),
            tags=("story",),
        ),
    ], subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_13 = SubjectCurriculum(grade=5, subject_id="G5-13",
    subject_title="reduce with init", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(reduce + 100 [1 2 3])",
            expected=106,
            concept_phrase="the fold with initial value",
            question_what="the sum produced by walking 1, 2, 3 with + and an opening tally of 100",
            goal_text="fold + over the vector containing 1, 2, 3 starting from an initial accumulator of 100",
            scenario=(
                "The milkmaid set out for market with one hundred coins already in her "
                "apron-pocket as the opening tally. She walked three stalls, adding one "
                "coin at the first, two at the second, three at the third."
            ),
            need=(
                "She needed the tally-walk to begin from the opening count rather than "
                "from the first element — the apron-pocket's coins were the seed, and "
                "the stalls added to them."
            ),
            mapping=(
                "`reduce` with an initial value starts the tally-walk from that seed: "
                "the opening count in the apron-pocket is the first running total, and "
                "each stall's coins are folded in with `+` from there."
            ),
            resolution=(
                "The REPL returned the accumulated total — the opening count plus all — 3 "
                "three stalls' coins combined into the final tally."
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
                "The milkmaid set out on the tally-walk with an opening tally of zero "
                "in her apron-pocket. She looked ahead and found the row of stalls was "
                "completely empty — no stall to visit, no coin to add."
            ),
            need=(
                "She needed the tally-walk to handle an empty row without failing — "
                "if no stalls existed, the opening tally itself should come back "
                "unchanged."
            ),
            mapping=(
                "`reduce` over an empty collection returns the initial value: the "
                "apron-pocket's opening count is the tally-walk's answer when there "
                "is nothing to fold over."
            ),
            resolution=(
                "The REPL returned the initial value unchanged — the empty row left "
                "the opening tally untouched, and that was the 0."
            ),
            tags=("story",),
        ),
    ], subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_14 = SubjectCurriculum(grade=5, subject_id="G5-14",
    subject_title="apply", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(apply + [1 2 3 4])",
            expected=10,
            concept_phrase="applying + to vector elements",
            question_what="the result of spreading the basket of 1, 2, 3, 4 as ingredients into +",
            goal_text="apply + to the elements of the vector [1 2 3 4]",
            scenario=(
                'The milkmaid arrived at market with a market-basket holding four counts: one coin, the counts. She needed to pass all of them at once to the `+` recipe rather than handing each count in separately.'
            ),
            need=(
                "She needed to spread the basket's contents out as individual "
                "arguments to `+`, so the function could tally them all as if they "
                "had been written out one by one."
            ),
            mapping=(
                "`apply` is the step that empties the market-basket onto the pail-steps "
                "card: it spreads the collection's elements as individual arguments, so "
                "`+` tallies them all in one call."
            ),
            resolution=(
                "The REPL returned the total — the basketseveral countsnts spread into "
                "`+` and tallied together in a single step — 4."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(apply max [3 1 4 1 5])",
            expected=5,
            concept_phrase="applying max to vector elements",
            question_what="the largest count found after spreading the basket of 3, 1, 4, 1, 5 into max",
            goal_text="apply max to the elements of the vector containing these numbers",
            scenario=(
                "The milkmaid's market-basket held five coin counts from five different "
                "buyers. She needed to find the highest count by spreading all five "
                "at once onto the `max` pail-steps card."
            ),
            need=(
                "She needed `apply` to empty the basket's five counts onto the `max` "
                "card in one step, so `max` could pick the highest without a separate "
                "tally-walk."
            ),
            mapping=(
                "`apply` spreads the basket's elements as individual arguments to "
                "`max`: each count lands separately on the card, and `max` returns "
                "the largest of all of them."
            ),
            resolution=(
                "The REPL returned the highest count — the basket's elements spread "
                "into `max`, which returned the largest value found — 5."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_15 = SubjectCurriculum(grade=5, subject_id="G5-15",
    subject_title="comp", fable="milkmaid",
    examples=[
        SubjectExample(
            form="((comp inc inc) 5)",
            expected=7,
            concept_phrase="composing inc twice",
            question_what="the result of chaining two inc recipe-cards and applying them to 5",
            goal_text="compose two inc functions and apply them to 5",
            scenario=(
                "The milkmaid clipped two pail-steps cards together in sequence: the "
                "first card incremented the day's count, the second incremented the "
                "result again. She handed the starting count of five to the paired cards."
            ),
            need=(
                "She needed the two `inc` cards to run in sequence — the second card "
                "taking the first card's output as its input — without naming the "
                "combined card or writing a new function."
            ),
            mapping=(
                "`comp` clips pail-steps cards together right-to-left: the rightmost "
                "card runs first, handing its result to the next. Two `inc` cards "
                "chained this way increment the input twice in one composed step."
            ),
            resolution=(
                "The REPL returned the result after two increments — the two `inc` "
                "cards ran in sequence, each stepping the count once."
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
                "The milkmaid clipped two different pail-steps cards in sequence: the "
                "first card incremented the count; the second converted the result into "
                "a string for the market ledger. She handed nine to the paired cards."
            ),
            need=(
                "She needed `inc` to run first on the count, and `str` to run second "
                "on `inc`'s result — two different recipes chained into one composed "
                "step."
            ),
            mapping=(
                "`comp` with `str` and `inc` clips the cards right-to-left: `inc` "
                "runs first, incrementing the number; then `str` converts the 9 "
                "to a string. The two-card chain runs as one composed pail-step."
            ),
            resolution=(
                "The REPL returned the string form of the incremented count — `inc` "
                "ran first, `str` second, and the combined card produced the ledger entry."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_16 = SubjectCurriculum(grade=5, subject_id="G5-16",
    subject_title="partial", fable="milkmaid",
    examples=[
        SubjectExample(
            form="((partial + 10) 5)",
            expected=15,
            concept_phrase="partial application of +",
            question_what="the result of applying the half-loaded + card pre-filled with 10 to the count 5",
            goal_text="apply + with 10 as the first argument and 5 as the second",
            scenario=(
                "The farmer pre-filled a pail-steps card for `+` with the base count "
                "of ten already loaded. The milkmaid received the half-loaded card and "
                "only needed to supply the remaining five."
            ),
            need=(
                "She needed the half-loaded card to accept her five coins and complete "
                "the addition — the ten was already baked in; she provided only the "
                "rest."
            ),
            mapping=(
                "`partial` is the pre-filled pail-steps card: it bakes one argument "
                "into the function ahead of time, so the caller only needs to supply "
                "the remaining ones. The two arguments combine when the card is called."
            ),
            resolution=(
                "The REPL returned the total — the pre-loaded ten and the supplied "
                "five combined by the partially-applied `+` card — 5."
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
                "The farmer pre-filled a pail-steps card for `*` with the multiplier "
                "three already loaded. The milkmaid then poured several counts through "
                "the strainer with that half-loaded card as the rule."
            ),
            need=(
                "She needed the half-loaded card to serve as the strainer rule: each "
                "element would enter, be multiplied by the pre-baked three, and fall "
                "into the collection below."
            ),
            mapping=(
                "`partial` creates the pre-filled card; `map` uses it as the "
                "strainer rule over the collection. Every element is multiplied by "
                "the baked-in three as it passes through."
            ),
            resolution=(
                "The REPL returned the transformed sequence — each element multiplied "
                "by three via the partially-applied card passed through the strainer — 3."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_17 = SubjectCurriculum(grade=5, subject_id="G5-17",
    subject_title="juxt", fable="milkmaid",
    examples=[
        SubjectExample(
            form="((juxt inc dec) 5)",
            expected=[6,4],
            concept_phrase="juxtaposing inc and dec",
            question_what="the pair of results from applying both inc and dec to 5",
            goal_text="apply both inc and dec to 5 and return results as a vector",
            scenario=(
                "The farmer set two pail-steps cards side by side: an `inc` card "
                "and a `dec` card. The milkmaid handed five to both cards."
            ),
            need=(
                "She needed both cards to run on the same input and return their "
                "results together in a single step."
            ),
            mapping=(
                "`juxt` places cards side by side and collects all results into "
                "one vector. Both recipes run on the same input."
            ),
            resolution=(
                "The REPL returned both results collected into a vector — 5."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_18 = SubjectCurriculum(grade=5, subject_id="G5-18",
    subject_title="some", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(some even? [1 3 5 8 7])",
            expected=True,
            concept_phrase="checking if any element satisfies a predicate",
            question_what="whether any pebble in 1, 3, 5, 8, 7 passes the even? sieve",
            goal_text="check if any element in the vector containing these numbers is even",
            scenario=(
                'The milkmaid held her milk-strainer over the pail and let five counts pass through the `even?` rule one at a time: the counts. She was looking for the first count that cleared the mesh.'
            ),
            need=(
                "She needed to know whether any count at all passed the even? rule — "
                "the moment the first one did, she had her answer and the rest "
                "did not need to be checked."
            ),
            mapping=(
                "`some` is the strainer held over the pail looking for the first drop "
                "that passes: it checks each element in order; as soon as one satisfies "
                "the rule, that element's truthy value comes back immediately."
            ),
            resolution=(
                "The REPL returned the truthy value of the first passing element — "
                "at least one count passed the even? strainer, and `some` stopped there — 7."
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
                'The milkmaid held the `neg?` strainer over the pail and let three counts pass through: the counts. None of the counts were below zero; the strainer mesh never opened for any of them.'
            ),
            need=(
                "She needed to know whether any count at all was negative — but "
                "after alseveral countsts were checked, none had passed the mesh "
                "and the strainer found nothing."
            ),
            mapping=(
                "`some` over a collection where nothing satisfies the rule drains "
                "the whole pail without finding a passing drop. When the last element "
                "fails, `some` returns nothing at all."
            ),
            resolution=(
                "The REPL returned nothing — no element passed the neg? strainer, "
                "so `some` found no truthy value and the pail came back empty-handed — 3."
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_19 = SubjectCurriculum(grade=5, subject_id="G5-19",
    subject_title="every?", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(every? pos? [1 2 3])",
            expected=True,
            concept_phrase="checking if all elements satisfy a predicate",
            question_what="whether every pebble in 1, 2, 3 passes the pos? sieve",
            goal_text="check if all elements in the vector containing 1, 2, and 3 are positive",
            scenario=(
                'The milkmaid held the `pos?` strainer over the pail and let three counts pass through: the counts. She watched each piece hit the mesh — all of them were above zero.'
            ),
            need=(
                "She needed to know whether every single count passed the positive "
                "rule — not just one, but all three without exception. A single "
                "failure would close the 3."
            ),
            mapping=(
                "`every?` is the all-or-nothing strainer: it checks every element "
                "in order; only when every one passes the rule does the strainer "
                "confirm the whole collection cleared the mesh."
            ),
            resolution=(
                "The REPL confirmed that every element passed — several countsunts were "
                "positive, and the all-or-nothing strainer returned the verdict."
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
                'The milkmaid held the `even?` strainer over the pail and let three counts through: the counts. The first count hit the mesh — one is odd — and the strainer closed immediately.'
            ),
            need=(
                "She needed every count to pass the even? rule for the 3 to "
                "hold. The moment the first count failed the mesh, the answer was "
                "settled and the rest did not matter."
            ),
            mapping=(
                "`every?` stops as soon as one element fails the rule: the first "
                "odd count hit the strainer mesh, closed it, and the strainer "
                "returned the verdict without testing the remaining elements."
            ),
            resolution=(
                "The REPL returned the verdict — not every count cleared the even? mesh, "
                "so the all-or-nothing strainer closed the moment the first one failed."
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_20 = SubjectCurriculum(grade=5, subject_id="G5-20",
    subject_title="take and drop", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(take 3 [10 20 30 40 50])",
            expected=[10,20,30],
            concept_phrase="taking elements from a sequence",
            question_what="the sequence produced by taking 3 elements from the row of 10, 20, 30, 40, 50",
            goal_text="take the first 3 elements from the vector containing these numbers",
            scenario=(
                "The milkmaid set her strainer over the pail and let five counts "
                "enter the mesh one by one: ten, twenty, thirty, forty, fifty. The "
                "strainer was set to collect only the first three, then close."
            ),
            need=(
                "She needed the strainer to stop collecting after the third element "
                "and keep only those first three in the collection below, leaving "
                "the rest untouched."
            ),
            mapping=(
                "`take` is the count-limited strainer: it lets through exactly the "
                "requested number of elements from the front of the sequence, then "
                "stops. Elements beyond that count never pass."
            ),
            resolution=(
                "The REPL returned the first several elements — the strainer collected "
                "the leading portion of the sequence and closed after the count was met — 50."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(drop 2 [10 20 30 40 50])",
            expected=[30,40,50],
            concept_phrase="dropping elements from a sequence",
            question_what="the sequence produced by dropping 2 elements from the row of 10, 20, 30, 40, 50",
            goal_text="drop the first 2 elements from the vector containing these numbers",
            scenario=(
                "The milkmaid poured five counts toward her strainer: ten, twenty, "
                "thirty, forty, fifty. The strainer was set to block the first two "
                "counts and let everything after them fall through."
            ),
            need=(
                "She needed the strainer to hold back the leading two elements and "
                "pass only the remainder — the tail of the sequence after the "
                "dropped portion."
            ),
            mapping=(
                "`drop` is the skip-forward strainer: it blocks the first requested "
                "number of elements and passes everything that follows into the "
                "collection below."
            ),
            resolution=(
                "The REPL returned the remaining elements — the strainer blocked the "
                "leading two and passed the rest of the sequence through — 50."
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_21 = SubjectCurriculum(grade=5, subject_id="G5-21",
    subject_title="distinct and sort", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(distinct [1 1 2 3 3 4])",
            expected=[1,2,3,4],
            concept_phrase="removing duplicates from a sequence",
            question_what="the sequence produced by passing [1 1 2 3 3 4] through the dedup-sieve",
            goal_text="remove duplicate elements from the vector containing these numbers",
            scenario=(
                "The milkmaid's pail held six coin counts with repeats: the counts. She set a dedup-strainer over the pail to remove every repeated count before sending the tally to market."
            ),
            need=(
                "She needed the strainer to let each count through only on its first "
                "appearance and block any repeat of a count already collected below."
            ),
            mapping=(
                "`distinct` is the dedup-strainer: it passes the first occurrence of "
                "each element and holds back any duplicate. The result is the sequence "
                "with every repeated count removed."
            ),
            resolution=(
                "The REPL returned the deduplicated sequence — each unique count "
                "passed through once, and all repeats were held back by the strainer — 4."
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
                "The milkmaid tseveral countscounts out of her pail in the order they "
                "had landed: three first, then one, then two. She needed them arranged "
                "from smallest to largest before she could present the tally at market."
            ),
            need=(
                "She needed the strainer to rearrange the counts into ascending order "
                "so the smallest came first and the largest last — a sorting pass over "
                "the whole pail."
            ),
            mapping=(
                "`sort` is the ordering strainer: it takes all the pail's elements and "
                "passes them through in ascending order into the collection below. "
                "The original order is replaced by the natural order."
            ),
            resolution=(
                "The REPL returned the sorted sequencseveral countse counts came back "
                "arranged from smallest to largest, ready for the market tally — 2 — 3."
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_22 = SubjectCurriculum(grade=5, subject_id="G5-22",
    subject_title="recur — first taste", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))",
            expected=120,
            concept_phrase="a factorial computation via loop and recur",
            question_what="the factorial of 5 computed by walking a circuit",
            goal_text="walk a small circuit five times, multiplying a running tally by the current step each lap, until the step counter reaches zero",
            scenario=(
                "The milkmaid walked the daily milking circuit: five stations along "
                "the same path, starting with a tally of 1. At each station she "
                "multiplied the running tally by the station count, then moved one "
                "step closer to done."
            ),
            need=(
                "She needed to walk the circuit without adding new ground — the same "
                "loop, five laps, each time stepping the tally forward and the "
                "counter down, until the counter reached zero."
            ),
            mapping=(
                "`loop/recur` is the daily milking round: `n` is the station-counter "
                "that shrinks each lap, `acc` is the running product, and `recur` "
                "sends her back to the circuit's start without growing the path."
            ),
            resolution=(
                "The REPL returned the accumulated product of all five laps — the "
                "tally the milkmaid had built one station at a time — 5."
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
