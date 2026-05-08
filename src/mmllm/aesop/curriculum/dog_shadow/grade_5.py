"""Grade 5 — control flow + higher-order intro. Through dog-shadow."""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.dog_shadow.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS,
    _GOAL_SUBPLOTS,
    _PLAN_POOL,
)
from mmllm.aesop.curriculum.dog_shadow._metaphor_pools import (
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
    subject_title="if", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(if true :a :b)",
            expected=":a",
            concept_phrase="the conditional",
            question_what="which of :a or :b is returned",
            goal_text="choose between :a and :b based on a true condition",
            scenario=(
                'The path forked at the bank near the pond. Two arms '
                'branched off — upstream and downstream — each marked by a '
                'small condition-stone. Bell the hound studied the stone at '
                'the fork: it carried a clear verdict that the way was '
                'open.'
            ),
            need=(
                'She wanted the answer to which arm of the fork she would '
                'actually take — without any wasted sniffing of the unrun '
                "arm — so only the chosen arm's value would come back from "
                'the runtime.'
            ),
            mapping=(
                'The fork is the if-form, the condition-stone is the test, '
                'the upstream arm is the then-branch and the downstream arm '
                "is the else-branch. Only the matching arm's value is what "
                'the REPL hands back.'
            ),
            resolution=(
                'The REPL read the condition, took the matching arm, and handed back its value. The other arm remained unrun, the path beneath it untouched (with `:a` as the input value).'
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
                'At the stream near the meadow, the path split into two '
                'branches. A stone at the fork bore a mark that read false. '
                'Rex the hound studied it closely — the stone was clear. '
                'He would not risk the upstream arm.'
            ),
            need=(
                'He wanted the correct value from the fork without exploring '
                'both arms. The false stone would send him downstream, and '
                "only that arm's value would matter."
            ),
            mapping=(
                'The fork is the if-form, the marked stone is the test, '
                'the upstream branch is the then-value and the downstream '
                'branch is the else-value. The runtime reads the stone and '
                'takes only the chosen arm.'
            ),
            resolution=(
                'The REPL read the false stone, took the downstream arm, and handed back its value. The upstream arm had never been sniffed. The decision was final (with `:a` as the input value).'
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
                'The path forked again, this time by the river bank. A new stone at the fork held a test: is 5 bigger than 3? Bell the hound checked the marks. The test read true — {drawn.a} bones stacked higher than three.'
            ),
            need=(
                'She wanted to take the right arm without guessing. The test '
                "on the stone was clear, and only the matching arm's value "
                'would matter for her next step.'
            ),
            mapping=(
                'The fork is the if-form, the comparison on the stone is the '
                'test, the upstream arm is the then-branch and the downstream '
                'is the else-branch. The runtime evaluates the test and picks '
                'the matching arm.'
            ),
            resolution=(
                'The REPL evaluated the comparison, found it true, took the '
                'upstream arm, and handed back its value. The downstream arm '
                'was never explored. The answer was certain.'
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_02 = SubjectCurriculum(grade=5, subject_id="G5-02",
    subject_title="if as expression", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(+ 1 (if true 10 20))",
            expected=11,
            concept_phrase="the arithmetic expression with conditional",
            question_what="the result of adding 1 to the conditional value",
            goal_text="add 1 to the result of choosing between 10 and 20 based on a true condition",
            scenario=(
                'At the bank near the forest, Patch the hound faced a nested '
                'choice. First, the fork at the path: a clear stone read true, '
                'offering two arms. Then, once the fork was crossed, the value '
                'from the chosen arm would feed into a second task — a simple '
                'count-add.'
            ),
            need=(
                'The fork would give a value, and that value would then be '
                'added to 1. Patch wanted the final sum without guessing either '
                'step. The if-form nested inside the arithmetic was the key.'
            ),
            mapping=(
                'The outer form is the addition; the inner form is the fork. '
                'The fork chooses between 10 and 20 based on the true stone; '
                'that chosen value is what gets added to 1. The if-form is '
                'itself an expression that yields a value.'
            ),
            resolution=(
                'The REPL evaluated the fork first, took the true arm and got '
                '10, then added 1 to that value, handing back the running '
                'total. The nested structure let the REPL compose the answer '
                'from the inside out.'
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_03 = SubjectCurriculum(grade=5, subject_id="G5-03",
    subject_title="when", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(when true :yes)",
            expected=":yes",
            concept_phrase="the when conditional",
            question_what="the value when the condition is true",
            goal_text="evaluate a when form with a true condition",
            scenario=(
                'Bell stood at the stream crossing near the pond. A single '
                'marker-stone bore a clear verdict: true. The form when was '
                'different from if — it had no else arm. If the stone read '
                'true, she would take the value. If false, she would get '
                'nothing.'
            ),
            need=(
                'She wanted the value only if the stone said to go. Unlike if, '
                'when offered no alternate arm — just the yes-path or silence. '
                'The stone was clear.'
            ),
            mapping=(
                'The when-form is the conditional with one arm only. The stone '
                'is the test. If true, the value comes back; if false, nothing '
                'is returned — not a default branch, but an empty mouth.'
            ),
            resolution=(
                'The REPL read the true stone and handed back yes. The silence-on-false rule is why when has only one arm: you get the answer or you get nothing (with `:yes` as the input value).'
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
                'Rex reached the same crossing, but the stone read false. '
                'The when-form held a single arm with the value :yes. But the '
                'condition blocked the path entirely — no else branch, no second '
                'arm. Only silence lay ahead.'
            ),
            need=(
                "He wanted to understand what happens when the when-form's stone "
                'reads false. Unlike if, there was no alternate branch waiting. '
                'The false path yielded no value.'
            ),
            mapping=(
                'The when-form, on a false test, returns nothing. It is not a '
                'branch to the else-arm (there is none) but a complete stop. The '
                'silence is the answer: the form evaluated but produced no value '
                'for the jaw to carry.'
            ),
            resolution=(
                'The REPL read the false stone, found no arm to take, and handed '
                "back nothing. The when-form's contract is simple: true gives the "
                'value, false gives silence — yes.'
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_04 = SubjectCurriculum(grade=5, subject_id="G5-04",
    subject_title="cond", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(cond (= 1 2) :a (= 1 1) :b :else :c)",
            expected=":b",
            concept_phrase="the multi-clause conditional",
            question_what="the value of the first arm whose stone reads true",
            goal_text="walk three condition-stones in order, taking the arm whose stone first reads true",
            scenario=(
                'Patch approached a fork by the stream. Three condition-stones lay in a '
                'row. The first read false, the second true. A third marked :else as '
                'fallback.'
            ),
            need=(
                'Walk the stone-row in order and take the first arm whose stone reads '
                'true.'
            ),
            mapping=(
                'The cond-form is the stone-row walk. Each test is a stone; each arm '
                'is the paired value. :else is the final fallback if all stones read false.'
            ),
            resolution=(
                'The REPL walked the first stone, found it false, moved to the second, '
                'found it true, and took its arm. The walk stopped there.'
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_05 = SubjectCurriculum(grade=5, subject_id="G5-05",
    subject_title="cond — :else", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(cond false :a false :b :else :c)",
            expected=":c",
            concept_phrase="the cond with default clause",
            question_what="the default value when no clauses match",
            goal_text="fall through all false conditions and return the default value",
            scenario=(
                'Bell walked a row of condition-stones by the river bank. The first '
                'read false, the second false. A third marker — :else — stood at the '
                "row's end."
            ),
            need=(
                'A fallback arm when all earlier tests failed. :else is the guaranteed '
                'default.'
            ),
            mapping=(
                'The cond-form walks the stone-row. :else is special: not a test but a '
                'safe harbor when all stones read false.'
            ),
            resolution=(
                'The REPL walked the first stone, found false, walked the second, found '
                'false, reached :else, and took its arm.'
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_06 = SubjectCurriculum(grade=5, subject_id="G5-06",
    subject_title="case", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(case 2 1 :one 2 :two 3 :three :default)",
            expected=":two",
            concept_phrase="the case statement",
            question_what="the matched branch",
            goal_text="match the value 2 against clauses and return the corresponding value",
            scenario=(
                "At the stream at the stream's edge, Rex held a bone marked with the number 2. Three marker-stones lay before him, each carved with a number: 1, 2, and 3. Beside each marker was a value. The case-form would match his bone against the markers and hand back the paired value."
            ),
            need=(
                'He wanted to find the marker that matched his bone and return the '
                'value paired with that marker. No testing was needed — just a direct '
                'lookup from value to answer.'
            ),
            mapping=(
                'The case-form is the matching-table. The input value is the bone. '
                'Each marker-stone is a clause-key. The value beside each marker is '
                'what case returns if the input matches. case is faster than cond '
                'because it compares directly, not by testing.'
            ),
            resolution=(
                'The REPL compared the input 2 against the markers, found an exact '
                'match at the second stone, and returned the paired value. No other '
                'stones were read. The lookup was complete.'
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
                'Patch held a bone marked 99. Three marker-stones lay in the table: '
                '1, 2, and a final marker-stone labeled :default. No marker matched '
                'the bone Patch carried. The :default stone was the fallback — the '
                'safe harbor for unmatched values.'
            ),
            need=(
                'When the input matched no explicit marker, the case-form would return '
                'the default value instead. This was the catchall for any value that '
                'fell outside the explicit clause list.'
            ),
            mapping=(
                'The case-form is the matching-table. The input 99 is the bone. The '
                'markers are explicit clauses. When no marker matches, :default is the '
                'fallback arm. The case returns the value paired with :default.'
            ),
            resolution=(
                'The REPL compared 99 against the markers, found no exact match, fell '
                'through to the :default arm, and returned its value. The default had '
                'caught the unmatched input. The answer came back.'
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_07 = SubjectCurriculum(grade=5, subject_id="G5-07",
    subject_title="and / or as control flow", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(and 1 2 3)",
            expected=3,
            concept_phrase="the and conjunction",
            question_what="the last truthy value",
            goal_text="return the last value when all values are truthy",
            scenario=(
                'Bell stood at the stream near the meadow, facing a row of gates. '
                'Three gates in sequence: the first held the value 1, the second 2, '
                'the third 3. The and-form would test each gate in order. If all '
                'gates opened, she would carry back the final value.'
            ),
            need=(
                'She needed to know: are all the gates truthy and open? If so, what '
                "is the last one's value? The and-form walks left to right, checking "
                'each gate, and returns the final value only if all gates passed.'
            ),
            mapping=(
                'The and-form is the gate-walk. Each value is a gate. If any gate is '
                'falsey, and stops and returns that falsey value immediately. If all '
                'gates are truthy, and returns the value of the last gate.'
            ),
            resolution=(
                'The REPL walked the first gate, found it truthy, walked the second, '
                'found it truthy, walked the third, found it truthy, and handed back '
                "the last gate's value. All gates had opened. The final value was the "
                'answer — 3.'
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
                'Rex stood at a fork by the stream facing gates. Three gates in '
                'sequence: the first held nil (closed), the second held false (closed), '
                'the third held a keyword (open). The or-form would test each and '
                'stop at the first open one.'
            ),
            need=(
                'He wanted the first truthy gate. The or-form is simpler than and: '
                'it stops at the first truthy value and returns it, never checking rest.'
            ),
            mapping=(
                'The or-form is the gate-walk for disjunction. Each value is a gate. '
                'If any gate is truthy, or stops immediately and returns that truthy '
                'value. Only if all gates are falsey does or return the last falsey '
                'value.'
            ),
            resolution=(
                'The REPL walked the first gate, found it falsey, walked the second, found it falsey, walked the third, found it truthy, and handed back that value immediately. The walk had stopped at the first open gate. The answer was certain (with `:found` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_08 = SubjectCurriculum(grade=5, subject_id="G5-08",
    subject_title="not", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(not (> 1 2))",
            expected=True,
            concept_phrase="the negation",
            question_what="the negated comparison",
            goal_text="negate the result of checking whether 1 is greater than 2",
            scenario=(
                'Patch stood at the stream crossing by the pond, reading a '
                'comparison stone: is 1 greater than 2? The stone read false. But '
                'the not-form would flip the answer — false becomes true, true becomes '
                'false. Patch wanted the inverted verdict.'
            ),
            need=(
                'To flip a falsey gate to truthy, or a truthy gate to falsey. The '
                'not-form takes one test and inverts its verdict. This is the negation '
                'gate at the stream.'
            ),
            mapping=(
                'The not-form is the negation gate. It takes a test — in this case, '
                'the comparison 1 > 2, which is false. The not-form inverts false to '
                'true. If the test had been true, not would make it false.'
            ),
            resolution=(
                'The REPL evaluated the comparison and found it false. The not-form '
                'flipped that false to true and handed back the inverted verdict. The '
                'negation was complete — 2.'
            ),
            tags=("story",),
        ),
    ], subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_09 = SubjectCurriculum(grade=5, subject_id="G5-09",
    subject_title="fn as value", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="((fn [f x] (f (f x))) inc 5)",
            expected=7,
            concept_phrase="applying a function twice",
            question_what="the result of inc applied twice",
            goal_text="apply the inc function twice to 5",
            scenario=(
                'Bell laid down a complex nose-trail near the pond. The trail took '
                'two inputs: a recipe-step f and a starting count x. The recipe '
                'applied f to x, then applied f again to the result. Functions as '
                'values — one recipe passed into another.'
            ),
            need=(
                'She wanted to apply the same recipe-step twice to a count, chaining '
                'the results through the nose-trail. This meant treating the recipe '
                'itself as a value that could be passed and called twice.'
            ),
            mapping=(
                'The outer fn is the compound nose-trail. Its parameters are f (the '
                'recipe-step) and x (the starting count). The body applies f to x, '
                'then applies f to that result. Functions are values in the domain; '
                'they can be passed and composed.'
            ),
            resolution=(
                'The REPL walked the nose-trail with inc as the recipe-step and 5 as '
                'the count. It applied inc to 5, got 6, then applied inc again to 6, '
                'got 7, and handed back the final result. The recipe had been walked '
                'twice in sequence.'
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_10 = SubjectCurriculum(grade=5, subject_id="G5-10",
    subject_title="map", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(map inc [1 2 3])",
            expected=[2,3,4],
            concept_phrase="mapping increment over a vector",
            question_what="the sequence produced by passing the vector containing 1, 2, and 3 through the inc-sieve",
            goal_text="pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collecting each transformed element",
            scenario=(
                'Rex held bones marked 1, 2, 3 at the stream. A log above held a gap '
                'shaped like inc: take a bone, add 1, drop the result on the far bank. '
                'Map would pour all three through, one at a time.'
            ),
            need=(
                'He wanted each bone transformed and all results collected. Map is the '
                'sieve: pour input bones, collect transformed ones.'
            ),
            mapping=(
                'The map-form is the sieve-pour. The bones are the input. The rule is '
                'inc. The far bank collects every result. Map feeds each bone through '
                'and gathers output.'
            ),
            resolution=(
                'The REPL poured bone 1 (got 2), poured 2 (got 3), poured 3 (got 4). '
                'The far bank held 2, 3, 4.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(map #(* % %) [1 2 3 4])",
            expected=[1,4,9,16],
            concept_phrase="mapping a squaring operation over a vector",
            question_what="the sequence produced by mapping a squaring rule over the vector containing 1, 2, 3, and 4",
            goal_text="apply a squaring operation to each element of the vector containing 1, 2, 3, and 4, returning a sequence",
            scenario=(
                'Patch had bones marked 1, 2, 3, 4 by the river. A sieve lay above, '
                'shaped like squaring: take a bone, multiply by itself, drop the '
                'product on the far bank. Map would pour all four through.'
            ),
            need=(
                'She wanted each bone squared and all results gathered. Map applies the '
                'same rule to each bone and collects all output.'
            ),
            mapping=(
                'The map-form is the sieve-pour. The pile is 1, 2, 3, 4. The rule is '
                'squaring. The far bank collects the squared values. Map works with any '
                'function.'
            ),
            resolution=(
                'The REPL poured bone 1 (got 1), poured 2 (got 4), poured 3 (got 9), '
                'poured 4 (got 16). The far bank held 1, 4, 9, 16.'
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_11 = SubjectCurriculum(grade=5, subject_id="G5-11",
    subject_title="filter", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(filter even? [1 2 3 4])",
            expected=[2,4],
            concept_phrase="filtering even elements from a vector",
            question_what="the sequence produced by filtering even? over the vector containing 1, 2, 3, and 4",
            goal_text="keep the even elements from the vector containing 1, 2, 3, and 4",
            scenario=(
                'Bell gathered bones marked 1, 2, 3, 4 at the stream. A log above '
                'held a gap that let through only even bones. She would pour all four '
                'through and collect what passed.'
            ),
            need=(
                'She wanted only the even bones. Filter is the sieve: some bones pass, '
                'some held back.'
            ),
            mapping=(
                'The filter-form is the sieve-gap. The bones are 1, 2, 3, 4. The rule '
                'is even?. Only bones that satisfy the rule pass through to the far '
                'bank.'
            ),
            resolution=(
                'The REPL poured bone 1 and held it back, poured 2 and let it pass, '
                'held 3, let 4 pass. The far bank caught 2 and 4. The sieve-pour was '
                'complete.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(filter pos? [-2 -1 0 1 2])",
            expected=[1,2],
            concept_phrase="filtering positive elements from a vector",
            question_what="the sequence produced by filtering pos? over the vector containing -2, -1, 0, 1, and 2",
            goal_text="keep the positive elements from the vector containing -2, -1, 0, 1, and 2",
            scenario=(
                'Rex the hound found five bones marked -2, -1, 0, 1, 2 by the river. '
                'A log above the water held a gap that let through only positive-marked '
                'bones. He would pour all five through in order.'
            ),
            need=(
                'He wanted to sieve out just the positive bones. Filter with the pos? '
                'rule would sieve out the rest — the gap does the work.'
            ),
            mapping=(
                'The filter-form is the sieve. The bones are -2, -1, 0, 1, 2. The rule '
                'is pos?. Positive bones pass through; negative and zero bones are held '
                'back.'
            ),
            resolution=(
                'The REPL poured bone -2 and held it back, poured -1 and held it back, '
                'poured 0 and held it back, let 1 pass, let 2 pass. The far bank caught '
                '1 and 2. The sieve was complete.'
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_12 = SubjectCurriculum(grade=5, subject_id="G5-12",
    subject_title="reduce", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(reduce + [1 2 3 4])",
            expected=10,
            concept_phrase="the fold operation",
            question_what="the running tally after walking 1, 2, 3, 4 with + as the combine step",
            goal_text="walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with + into the running total",
            scenario=(
                'Patch the hound stood at the stream near the forest, facing a '
                'row of pebbles marked 1, 2, 3, 4 laid end to end. She would '
                'walk the row, carrying a tally in her jaws, adding each pebble '
                "to the tally as she passed it. The final tally would be her "
                'answer.'
            ),
            need=(
                'She wanted the sum of all pebbles in the row. Reduce walks the '
                'row left to right, combining each pebble with a running total '
                'using the + rule.'
            ),
            mapping=(
                'The reduce-form is the tally-walk. The pebbles are 1, 2, 3, 4. '
                'The combination-rule is +. Each step adds the current pebble '
                'to the tally. The final tally is what reduce returns.'
            ),
            resolution=(
                'The REPL began the walk with no tally and pebble 1 (tally=1), '
                'added pebble 2 (tally=3), added 3 (tally=6), added 4 '
                '(tally=10). The final tally came back as the answer.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(reduce * [1 2 3 4 5])",
            expected=120,
            concept_phrase="the fold operation",
            question_what="the product produced by walking 1, 2, 3, 4, 5 with * as the combine step",
            goal_text="fold * over the vector containing 1, 2, 3, 4, and 5, computing their product",
            scenario=(
                'Bell the hound faced a row of pebbles marked 1, 2, 3, 4, 5 at '
                'the stream. She would walk the row, carrying a product-tally, '
                'multiplying each pebble into the running count as she passed.'
            ),
            need=(
                'She wanted the product of all five pebbles. Reduce with the * rule '
                'walks the row, combining each pebble by multiplication.'
            ),
            mapping=(
                'The reduce-form is the tally-walk. The pebbles are 1, 2, 3, 4, 5. '
                'The rule is *. Each step multiplies the current pebble with the '
                'running tally.'
            ),
            resolution=(
                'The REPL began with 1 and pebble 1 (tally=1), multiplied by 2 '
                '(tally=2), by 3 (tally=6), by 4 (tally=24), by 5. The final '
                'product came back.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(reduce max [3 1 4 1 5 9 2 6])",
            expected=9,
            concept_phrase="the fold operation",
            question_what="the largest pebble found by walking 3, 1, 4, 1, 5, 9, 2, 6 with max as the combine step",
            goal_text="fold max over the vector containing 3, 1, 4, 1, 5, 9, 2, and 6, finding the maximum",
            scenario=(
                'Rex faced a long row: 3, 1, 4, 1, 5, 9, 2, 6. He would walk it, '
                'carrying the largest seen so far, updating whenever he found a bigger.'
            ),
            need=(
                'He wanted the largest without guessing. Reduce with max walks the row, '
                'keeping the largest seen.'
            ),
            mapping=(
                'The reduce-form is the tally-walk. The pebbles are 3, 1, 4, 1, 5, 9, '
                '2, 6. The rule is max. Each step compares the current pebble with the '
                'running maximum and keeps the larger one.'
            ),
            resolution=(
                'The REPL walked the row: 3 (tally=3), 1 (stays 3), 4 (tally=4), '
                '1 (stays 4), 5 (tally=5), 9 (tally=9), 2 (stays 9), 6 (stays 9). '
                'The maximum came back.'
            ),
            tags=("story",),
        ),
    ], subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_13 = SubjectCurriculum(grade=5, subject_id="G5-13",
    subject_title="reduce with init", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(reduce + 100 [1 2 3])",
            expected=106,
            concept_phrase="the fold with initial value",
            question_what="the sum produced by walking 1, 2, 3 with + and an opening tally of 100",
            goal_text="fold + over the vector containing 1, 2, 3 starting from an initial accumulator of 100",
            scenario=(
                'Bell the hound began a tally-walk by the river bank with a '
                'starting tally of 100 already scratched into a flat stone. A '
                'row of pebbles lay before her: 1, 2, 3. She would add each '
                'pebble to the running tally, beginning with the opening count.'
            ),
            need=(
                'She wanted the sum, but not from zero — starting instead from '
                '100. Reduce with an initial value lets her begin the walk with '
                'a pre-set tally.'
            ),
            mapping=(
                'The reduce-form is the tally-walk. The initial accumulator is '
                '100. The pebbles are 1, 2, 3. The combination-rule is +. Each '
                'step adds a pebble to the running tally, which began at 100.'
            ),
            resolution=(
                'The REPL began with tally=100 and pebble 1 (tally=101), added '
                '2 (tally=103), added 3 (tally=106). The final sum came back.'
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
                'Patch the hound stood at the stream near the meadow, facing an '
                'empty row — no pebbles lay there at all. She set her opening '
                'tally at 0 and looked ahead. The row had no bones to walk. The '
                'tally would remain what it began.'
            ),
            need=(
                'She needed to know what happens when reduce meets an empty row. '
                'With an initial accumulator of 0, there are no pebbles to add. '
                'The answer is the starting value itself.'
            ),
            mapping=(
                'The reduce-form is the tally-walk. The initial accumulator is 0. '
                'The pebbles are none — an empty row. The combination-rule is +. '
                'With no pebbles to combine, the tally stays as it started.'
            ),
            resolution=(
                'The REPL saw the empty row, had tally=0, found no pebbles to add, '
                'and returned the opening tally unchanged. The walk was complete '
                'with no steps taken.'
            ),
            tags=("story",),
        ),
    ], subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_14 = SubjectCurriculum(grade=5, subject_id="G5-14",
    subject_title="apply", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(apply + [1 2 3 4])",
            expected=10,
            concept_phrase="applying + to vector elements",
            question_what="the result of spreading the basket of 1, 2, 3, 4 as ingredients into +",
            goal_text="apply + to the elements of the vector containing 1, 2, 3, and 4",
            scenario=(
                'Rex the hound held a basket of bones marked 1, 2, 3, 4 at the '
                'stream. A nose-trail lay before him — the + recipe. The apply-form '
                'would open the basket, spread all the bones as ingredients into the '
                'recipe, and follow the trail.'
            ),
            need=(
                'He wanted to apply the + recipe to all the bones in the basket at '
                'once. Apply unpacks the basket and feeds the contents directly to '
                'the recipe.'
            ),
            mapping=(
                'The apply-form spreads the ingredients. The basket is the vector '
                '1, 2, 3, 4. The recipe is +. Apply opens the basket and hands each '
                'bone to the recipe as a separate argument.'
            ),
            resolution=(
                'The REPL unpacked the basket, took the four bones as arguments, '
                'followed the + recipe through all of them, and handed back the '
                'sum. The applied recipe was complete — 4.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(apply max [3 1 4 1 5])",
            expected=5,
            concept_phrase="applying max to vector elements",
            question_what="the largest count found after spreading the basket of 3, 1, 4, 1, 5 into max",
            goal_text="apply max to the elements of the vector containing 3, 1, 4, 1, and 5",
            scenario=(
                'Bell carried a basket of bones marked 3, 1, 4, 1, 5 at the stream. A '
                'nose-trail lay ahead — the max recipe. Apply would unpack the basket '
                'and feed all bones to the recipe at once.'
            ),
            need=(
                'She wanted to apply max to all basket bones together. Apply spreads '
                'the basket contents as separate arguments to the recipe.'
            ),
            mapping=(
                'The apply-form spreads the ingredients. The basket is 3, 1, 4, 1, 5. '
                'The recipe is max. Apply opens the basket and passes each bone as '
                'an argument to the recipe.'
            ),
            resolution=(
                'The REPL unpacked the basket, took all five bones as arguments, '
                'followed the max recipe, and handed back the largest. The applied '
                'recipe was complete — 5.'
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_15 = SubjectCurriculum(grade=5, subject_id="G5-15",
    subject_title="comp", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="((comp inc inc) 5)",
            expected=7,
            concept_phrase="composing inc twice",
            question_what="the result of chaining two inc recipe-cards and applying them to 5",
            goal_text="compose two inc functions and apply them to 5",
            scenario=(
                'Patch the hound laid down two nose-trails end to end by the '
                'river bank. The first trail was inc, the second trail was inc '
                'again. She would chain them together, so what the first trail '
                'turned up would feed straight into the second.'
            ),
            need=(
                'She wanted to apply inc twice to a bone without writing two '
                'separate applications. Comp chains recipes together so they run '
                'as one longer trail.'
            ),
            mapping=(
                'The comp-form chains the trails. The first trail is inc, the '
                'second is inc. The input bone is 5. Comp feeds the output of the '
                'first trail into the input of the second.'
            ),
            resolution=(
                'The REPL composed the two trails into one, then followed the '
                'chained trail with input 5: the first inc turned 5 into 6, then '
                'the second inc turned 6 into 7. The final result came back.'
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
                'Bell the hound laid down two nose-trails end to end by the stream. '
                'The first trail was inc, the second was str. She would chain them: '
                'the first would increment the bone count, then the second would '
                'turn the result into a bark-mark.'
            ),
            need=(
                'She wanted to increment a bone and then turn the result into a '
                'mark. Comp chains recipes so they flow one into the next.'
            ),
            mapping=(
                'The comp-form chains the trails. The first is inc, the second is '
                'str. The input bone is 9. Comp feeds the first output into the '
                'second trail.'
            ),
            resolution=(
                'The REPL composed the trails and followed the chain with input 9: '
                'inc incremented it, then str turned the result into a text mark. '
                'The final mark came back.'
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_16 = SubjectCurriculum(grade=5, subject_id="G5-16",
    subject_title="partial", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="((partial + 10) 5)",
            expected=15,
            concept_phrase="partial application of +",
            question_what="the result of applying the half-loaded + card pre-filled with 10 to the count 5",
            goal_text="apply + with 10 as the first argument and 5 as the second",
            scenario=(
                'Rex the hound held a nose-trail card marked +. He wanted to pre-load '
                'the first ingredient: 10. Partial would freeze 10 into the recipe and '
                'return a new trail that waited for one more bone — the second argument.'
            ),
            need=(
                'He wanted a recipe pre-filled with 10, waiting for just one more bone. '
                'Partial locks in some arguments and returns a recipe ready for the '
                'rest.'
            ),
            mapping=(
                'The partial-form pre-loads the recipe. The recipe is +, the frozen '
                'argument is 10. Partial returns a new trail waiting for 5. When that '
                'new trail gets 5, it applies + with both ingredients.'
            ),
            resolution=(
                'The REPL applied partial to + and 10, creating a new trail. That trail '
                'then received 5 as its argument and applied the + recipe with 10 and 5. '
                'The sum came back.'
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
                'Bell wanted to multiply bones by 3. She would use partial to pre-load '
                'the * recipe, creating a new trail for each bone. Then map would pour '
                'the pile through that trail.'
            ),
            need=(
                'She wanted each bone multiplied by 3. Partial freezes 3 into *, and '
                'map feeds each bone through.'
            ),
            mapping=(
                'The map-form is the sieve, partial is the gap-rule. Partial pre-loads '
                '* with 3. Map pours bones 1, 2, 3 through the trail one at a time.'
            ),
            resolution=(
                'The REPL created the partial trail, then map poured bone 1 (got 3), '
                'poured 2 (got 6), poured 3 (got 9). The far bank caught the results. '
                'The sieve-pour was complete.'
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_17 = SubjectCurriculum(grade=5, subject_id="G5-17",
    subject_title="juxt", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="((juxt inc dec) 5)",
            expected=[6,4],
            concept_phrase="juxtaposing inc and dec",
            question_what="the pair of results produced by asking both the inc and dec recipe-cards about 5",
            goal_text="apply both inc and dec functions to 5 and return both results as a vector",
            scenario=(
                'Patch the hound held one bone marked 5 and two nose-trails. The '
                'first was inc, the second was dec. Juxt would ask both trails about '
                'the bone and collect both answers together.'
            ),
            need=(
                'She wanted both recipes to run on the same bone and get both answers '
                'back. Juxt applies multiple recipes to one input and collects all '
                'results.'
            ),
            mapping=(
                'The juxt-form asks multiple trails. The input bone is 5. The trails '
                'are inc and dec. Juxt feeds the bone through both and gathers both '
                'answers into a cache.'
            ),
            resolution=(
                'The REPL applied inc to 5 (got 6) and dec to 5 (got 4). Both were '
                'collected into a cache. The juxtaposed answers came back.'
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_18 = SubjectCurriculum(grade=5, subject_id="G5-18",
    subject_title="some", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(some even? [1 3 5 8 7])",
            expected=True,
            concept_phrase="checking if any element satisfies a predicate",
            question_what="whether any pebble in 1, 3, 5, 8, 7 passes the even? sieve",
            goal_text="check if any element in the vector containing 1, 3, 5, 8, and 7 is even",
            scenario=(
                "Rex the hound held a pile of bones marked 1, 3, 5, 8, 7 at the stream at the stream's edge. A gap-sieve before him had a rule: only even-marked bones can pass through. He wanted to know: does any bone in this pile fit through?"
            ),
            need=(
                'He needed to find whether at least one bone would pass the even? sieve. '
                'Some is a quick check: it stops at the first bone that passes and '
                'returns yes.'
            ),
            mapping=(
                'The some-form checks the pile. The bones are 1, 3, 5, 8, 7. The '
                'gap-rule is even?. Some pours each bone through the gap and stops as '
                'soon as one passes.'
            ),
            resolution=(
                'The REPL poured bone 1 (held back), poured 3 (held back), poured 5 '
                '(held back), poured 8 (passed). Some found a match and returned true '
                'without checking the rest.'
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
                'Bell the hound held a pile of bones marked 1, 2, 3 by the river bank. '
                'A gap-sieve before her had a different rule: only negative-marked bones '
                'can pass. She wanted to know: does any bone fit through?'
            ),
            need=(
                'She needed to check whether at least one bone would pass the neg? sieve. '
                'Some stops as soon as it finds one that passes, or returns nothing if '
                'none pass.'
            ),
            mapping=(
                'The some-form checks the pile. The bones are 1, 2, 3. The gap-rule is '
                'neg?. Some pours each through the gap and stops if one passes, or '
                'reports nothing if all fail.'
            ),
            resolution=(
                'The REPL poured bone 1 (held back), poured 2 (held back), poured 3 '
                '(held back). No bones passed the sieve. Some returned nothing — no '
                'match found.'
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_19 = SubjectCurriculum(grade=5, subject_id="G5-19",
    subject_title="every?", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(every? pos? [1 2 3])",
            expected=True,
            concept_phrase="checking if all elements satisfy a predicate",
            question_what="whether every pebble in 1, 2, 3 passes the pos? sieve",
            goal_text="check if all elements in the vector containing 1, 2, and 3 are positive",
            scenario=(
                'Patch the hound held a pile of bones marked 1, 2, 3 at the stream '
                'near the forest. A gap-sieve had a rule: only positive-marked bones '
                'can pass. She wanted to know: will every bone in this pile fit '
                'through?'
            ),
            need=(
                'She needed to check whether all bones would pass the pos? sieve. '
                'Every? is the strict test: it stops as soon as one fails, or returns '
                'yes if all pass.'
            ),
            mapping=(
                'The every?-form checks the pile. The bones are 1, 2, 3. The gap-rule '
                'is pos?. Every? pours each bone through and stops if one fails, or '
                'confirms yes if all pass.'
            ),
            resolution=(
                'The REPL poured bone 1 (passed), poured 2 (passed), poured 3 (passed). '
                'Every bone made it through. Every? returned true — all bones fit.'
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
                'Bell the hound held a pile of bones marked 1, 2, 3 by the river. A '
                'gap-sieve had a rule: only even-marked bones can pass. She wanted to '
                'know: will every bone fit through?'
            ),
            need=(
                'She needed to check whether all bones would pass the even? sieve. '
                'Every? returns yes only if every bone passes, and returns no as soon '
                'as one fails.'
            ),
            mapping=(
                'The every?-form checks the pile. The bones are 1, 2, 3. The gap-rule '
                'is even?. Every? pours each through and returns no if any fails, or '
                'yes if all pass.'
            ),
            resolution=(
                'The REPL poured bone 1 (held back — odd, not even). Every? found a '
                'failure immediately and returned false without checking the rest. Not '
                'every bone fit.'
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_20 = SubjectCurriculum(grade=5, subject_id="G5-20",
    subject_title="take and drop", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(take 3 [10 20 30 40 50])",
            expected=[10,20,30],
            concept_phrase="taking elements from a sequence",
            question_what="the sequence produced by taking 3 elements from the row of 10, 20, 30, 40, 50",
            goal_text="take the first 3 elements from the vector containing 10, 20, 30, 40, and 50",
            scenario=(
                'Rex the hound faced a long row of bones: 10, 20, 30, 40, 50. A gap-sieve '
                'would count out just the first three and pass them through. The rest would '
                'stay behind on the near bank.'
            ),
            need=(
                'He wanted just the first {drawn.a} bones from the row. Take counts off the first n bones and passes only those through the sieve.'
            ),
            mapping=(
                'The take-form is the sieve-gap. The input row is 10, 20, 30, 40, 50. The count is 3. Take lets the first {drawn.a} bones through and holds the rest back.'
            ),
            resolution=(
                'The REPL poured bones 10, 20, 30 through the gap and let the rest fall back. The far bank caught the first {drawn.a} bones. The sieve-pour was complete.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(drop 2 [10 20 30 40 50])",
            expected=[30,40,50],
            concept_phrase="dropping elements from a sequence",
            question_what="the sequence produced by dropping 2 elements from the row of 10, 20, 30, 40, 50",
            goal_text="drop the first 2 elements from the vector containing 10, 20, 30, 40, and 50",
            scenario=(
                'Bell the hound faced the same long row by the river bank: 10, 20, 30, '
                '40, 50. A different gap-sieve would skip the first two and pass the '
                'rest through. The first two would be held back on the near bank.'
            ),
            need=(
                'She wanted everything except the first two bones. Drop skips the first n '
                'bones and passes the rest through the sieve.'
            ),
            mapping=(
                'The drop-form is the sieve-gap. The input row is 10, 20, 30, 40, 50. '
                'The count is 2. Drop holds the first two back and lets the rest through.'
            ),
            resolution=(
                'The REPL skipped bones 10 and 20, then poured bones 30, 40, 50 through '
                'the gap. The far bank caught the remaining three bones. The sieve-pour '
                'was complete.'
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_21 = SubjectCurriculum(grade=5, subject_id="G5-21",
    subject_title="distinct and sort", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(distinct [1 1 2 3 3 4])",
            expected=[1,2,3,4],
            concept_phrase="removing duplicates from a sequence",
            question_what="the sequence produced by passing 1, 1, 2, 3, 3, 4 through the dedup-sieve",
            goal_text="remove duplicate elements from the vector containing 1, 1, 2, 3, 3, and 4",
            scenario=(
                'Patch the hound gathered a pile of bones marked 1, 1, 2, 3, 3, 4 at '
                'the stream near the meadow. Some bones had the same mark — duplicates. '
                'A special gap-sieve would pass each bone through once and catch it, '
                'holding back any bones already seen.'
            ),
            need=(
                'She wanted to keep only the first copy of each unique mark. Distinct is '
                'the dedup-sieve: it passes each unique bone through and holds back '
                'repeats.'
            ),
            mapping=(
                'The distinct-form is the sieve-gap. The input bones are 1, 1, 2, 3, 3, '
                '4. The gap-rule is uniqueness: pass the first copy, hold back any repeat '
                'marks.'
            ),
            resolution=(
                'The REPL poured bone 1 (passed), poured 1 again (held back as duplicate), '
                'poured 2 (passed), poured 3 (passed), poured 3 (held back), poured 4 '
                '(passed). The far bank caught 1, 2, 3, 4. No duplicates remained.'
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
                'Bell the hound held a pile of bones marked 3, 1, 2 at the stream. The '
                'bones were out of order. A gap-sieve with a sorting rule would rearrange '
                'them in ascending order as they passed through.'
            ),
            need=(
                'She wanted the bones in ascending order. Sort is the arranging-sieve: it '
                'takes the bones and passes them through in a rearranged sequence.'
            ),
            mapping=(
                'The sort-form is the sieve-gap. The input bones are 3, 1, 2. The '
                'gap-rule is ascending order. Sort rearranges the bones from smallest to '
                'largest.'
            ),
            resolution=(
                'The REPL took the bones 3, 1, 2 and rearranged them in ascending order. '
                'The far bank caught 1, 2, 3. The sorting-sieve was complete.'
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_22 = SubjectCurriculum(grade=5, subject_id="G5-22",
    subject_title="recur — first taste", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))",
            expected=120,
            concept_phrase="a factorial computation via loop and recur",
            question_what="the factorial of 5 computed by walking a circuit",
            goal_text="walk a small circuit five times, multiplying a running tally by the current step each lap, until the step counter reaches zero",
            scenario=(
                'Bell the hound paced back and forth along a stretch of '
                'stream bank near the pond, carrying a small running tally '
                'in her jaws. Each pass returned to the same starting '
                'point, with the tally a little different and the count of '
                'remaining passes one fewer.'
            ),
            need=(
                'She would loop until the count of remaining passes reached '
                'zero — the base case — and the final tally on that pass '
                'would be her answer, with no extra trail laid down behind '
                'her.'
            ),
            mapping=(
                'The pacing-without-growing-the-trail is recur, the binding '
                "pair is loop's initial state, the base case is the if-zero "
                'check, and the new bindings on each pass are what recur '
                'supplies.'
            ),
            resolution=(
                'The REPL paced the bank the right number of times, then stopped at the base case, and handed back the final tally. The trail beneath the pacing had not grown — the call-stack was exactly as it began — 1 (with `5` as the input value).'
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
    print(f"grade-5 dog-shadow smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
