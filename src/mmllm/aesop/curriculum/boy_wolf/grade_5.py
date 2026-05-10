"""Grade 5 — control flow + higher-order intro. Through the
Boy-who-cried-Wolf fable.

Subplot lens: the elder demonstrates how the same operation, applied
to many things at once, settles a long calculation — and the shepherd
agrees to write it. Polarity preserved: the elder is the patient
demonstrator; the shepherd writes the form for the REPL rather than
guessing.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.boy_wolf.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.boy_wolf._metaphor_pools import (
    _CIRCUIT_SUBPLOTS, _FORK_SUBPLOTS, _GATE_SUBPLOTS, _RECIPE_SUBPLOTS, _SIEVE_SUBPLOTS, _TALLYWALK_SUBPLOTS,
)
from mmllm.aesop.curriculum.boy_wolf._goals import GOALS, get_goal


_HOF_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [
    SubplotTemplate("""\
{elder_phrase} demonstrated {place} how the same operation, applied to
many things at once, was the heart of every long calculation. The form
{form_display} captured {concept_phrase}, and {shepherd_phrase} agreed
to write it for the REPL — no claims required, just the runtime's
answer."""),

    SubplotTemplate("""\
"Same trick, repeated cleverly," {elder} said {place}, sketching the
form {form_display} into the dust. {shepherd}, {emo_proud}, claimed to
know exactly what {concept_phrase} would produce. The runtime, again,
was the only honest judge in the village now."""),
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
_PLAN_G5 = _PLAN_POOL + (
    "I use map / filter / reduce as appropriate.",
    "I write the higher-order form so the REPL can compute.",
)


G5_01 = SubjectCurriculum(grade=5, subject_id="G5-01",
    subject_title="if", fable="boy-wolf",
    examples=[
        _ex("(if true :a :b)",  ":a", "the expression (if true :a :b)",  "which of :a or :b is returned",
            scenario=(
                "Tom stood at the path-fork on the lookout — three paths "
                "fanning out below, one to the watchhouse, one to the fold, "
                "one back to the pasture. Carol had set a small "
                "condition-stone at the fork: the day's question for the "
                "morning's runner."
            ),
            need=(
                "The runner needed to take exactly one path. Tom wanted "
                "to shout both directions at once; Carol insisted the "
                "fork would settle which arm to take based on the "
                "condition's verdict."
            ),
            mapping=(
                "`if` evaluates the condition and takes one of two "
                "arms. With the condition true, the fork's left arm "
                "is taken; the right arm's value is never produced. "
                "The runtime walks one path; the other simply isn't."
            ),
            resolution=(
                "the runner went left — `:a` was the value the fork carried back — and the morning's question settled without the second arm ever being walked. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record."         )),
        _ex("(if false :a :b)", ":b", "the expression (if false :a :b)", "which of :a or :b is returned",
            scenario=(
                "Carol asked Tom to bring either fleece or grain from the "
                "fold — but the weather had turned cold, and the path to "
                "the fold was icy. At the lookout, she set a condition-stone: "
                "if the wind had dropped, the path was safe."
            ),
            need=(
                "Tom needed to follow one path or the other, but not both. "
                "The condition would decide whether to fetch fleece (left arm) "
                "or wait another day (right arm)."
            ),
            mapping=(
                "`if` checks the condition; when false, the right arm is taken "
                "instead of the left. The unwalked arm never runs at all — "
                "its value isn't computed, just passed by."
            ),
            resolution=(
                "the wind still howled, the condition was false, and Tom stayed put — the right arm's `:b` was what the fork produced — and Carol nodded, satisfied the form had made the careful choice. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last."       )),
        _ex("(if (> 5 3) :a :b)", ":a", "the expression (if (> 5 3) :a :b)", "the if's branch",
            scenario=(
                "Tom stood sorting wool by weight at the watchhouse. Carol "
                "had given him a simple rule: if a fleece weighed more than "
                "three coins' worth, send it to the dyer; if not, keep it "
                "for the lambing-pen. A fleece lay on the scale, marking five."
            ),
            need=(
                "Tom needed to decide which basket to drop it into, based on "
                "the weight. The condition `(> 5 3)` — is five greater than "
                "three? — would settle which path it took."
            ),
            mapping=(
                "`if` evaluates the comparison `(> 5 3)` first. Since five "
                "is indeed greater than three, the condition is true, and "
                "the first arm is taken. `:a` is the result."
            ),
            resolution=(
                "the call returned `:a`, and Tom dropped the fleece into the dyer's basket — the comparison had done its work, and the form had steered him to the right choice without guessing. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand."           )),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_02 = SubjectCurriculum(grade=5, subject_id="G5-02",
    subject_title="if as expression", fable="boy-wolf",
    examples=[
        _ex("(+ 1 (if true 10 20))", 11,
            "the expression (+ 1 (if true 10 20))", "the result of adding 1 to the if expression",
            scenario=(
                "Carol asked Tom to add one measure of powder to whichever "
                "pigment the elder had chosen from the shelf. The fork's "
                "condition was simple: if the dye was ready, use the brighter "
                "color; otherwise use the safe one. Tom held the measure, "
                "waiting to know which path the fork would choose."
            ),
            need=(
                "Tom needed to know not just which color to use, but the final "
                "amount — one measure plus whichever base the fork selected. "
                "The fork wasn't the end of the calculation; it was nested "
                "inside the addition."
            ),
            mapping=(
                "`if` returns a value (10 or 20), but that value then becomes "
                "part of the larger form `(+ 1 ...)`. The `if` expression sits "
                "inside the `+` operation, so it evaluates the fork first, "
                "then adds 1 to whatever the fork produced."
            ),
            resolution=(
                "the condition was true, the fork returned 10, then `+` added 1 to it, and the final value was 11 — the fork wasn't just an answer; it was a building block in a larger calculation. Tom chalked {drawn.a} on the watchhouse notice, and the morning record stood for the next shepherd to read."           )),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_03 = SubjectCurriculum(grade=5, subject_id="G5-03",
    subject_title="when", fable="boy-wolf",
    examples=[
        _ex("(when true :yes)", ":yes", "the expression (when true :yes)", "the value of (when true :yes)",
            scenario=(
                "Carol posted a watch-order at the fold: if the lambs were "
                "restless today, Tom was to ring the bell and post a notice "
                "at the townsfolk stone. Tom checked the pen, and yes — the lambs "
                "were pacing. The condition was met."
            ),
            need=(
                "When the condition was true, Tom needed the action to happen "
                "and to know what the form produced. `when` is a fork that only "
                "walks one arm: when the condition holds, do the action and "
                "return its value."
            ),
            mapping=(
                "`when` is like `if` but simpler — it only runs when the "
                "condition is true. When true, the body is evaluated and its "
                "value is returned. `:yes` is the body; it evaluates to itself."
            ),
            resolution=(
                'the condition was true, it evaluated the body, and `:yes` came back — Tom rang the bell, knowing it had settled the matter and given back the promised value. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'           )),
        _ex("(when false :yes)", None, "the expression (when false :yes)", "the value of (when false :yes)",
            scenario=(
                "The next morning, Carol asked Tom to check the lambs again. "
                "The same watch-order stood: `when` the lambs are restless, "
                "ring the bell and return `:yes`. Tom checked, and the lambs "
                "were calm. The condition was false."
            ),
            need=(
                "When the condition is false, `when` does nothing — no action "
                "runs, and no value is returned. Tom needed to know what the "
                "form produced when the condition didn't hold."
            ),
            mapping=(
                "`when` with a false condition takes no action and returns "
                "`nil` (nothing). The body `:yes` is never even evaluated; "
                "it's just left behind, untouched."
            ),
            resolution=(
                'the lambs were still, the condition was false, it returned `nil` — no bell rang, no value came back, and Tom understood: `when` only acts when the condition says yes. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'           )),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_04 = SubjectCurriculum(grade=5, subject_id="G5-04",
    subject_title="cond", fable="boy-wolf",
    examples=[
        _ex("(cond (= 1 2) :a (= 1 1) :b :else :c)", ":b",
            "the cond form", "which clause of the cond fires",
            scenario=(
                "Carol set three condition-stones on the path in order."
            ),
            need=(
                "Tom needed to check each in order and take the first true arm."
            ),
            mapping=(
                "`cond` walks through condition pairs in order and returns the value of the first true arm."
            ),
            resolution=(
                "The first condition was false, the second was true, so it returned that arm's value. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement."
            )),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_05 = SubjectCurriculum(grade=5, subject_id="G5-05",
    subject_title="cond — :else", fable="boy-wolf",
    examples=[
        _ex("(cond false :a false :b :else :c)", ":c",
            "the cond falling through to :else", "the :else value",
            scenario=(
                "Tom brought two wool-baskets to the sorting pen. The first "
                "was for fleece that matched the north-fold brand; the second "
                "for the south-fold brand. But the fleece he held didn't match "
                "either. Carol had carved one more stone: `:else` — the "
                "fallback for the unmatched."
            ),
            need=(
                "Tom needed a path for every fleece, even those that didn't "
                "match the first two conditions. The `:else` arm had to catch "
                "everything that fell through, so nothing was left without a "
                "destination."
            ),
            mapping=(
                "`cond` checks each condition in order. When all conditions "
                "are false, `:else` acts as the guaranteed catch-all — the form "
                "skips all the false branches and takes the `:else` arm, "
                "returning its value."
            ),
            resolution=(
                'both conditions were false, the form stepped past them both and took the `:else` arm — `:c` was the value returned — and Tom dropped the fleece into the catch-all basket, knowing every piece had a home. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'         )),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_06 = SubjectCurriculum(grade=5, subject_id="G5-06",
    subject_title="case", fable="boy-wolf",
    examples=[
        _ex("(case 2 1 :one 2 :two 3 :three :default)", ":two",
            "the case form", "the matched branch",
            scenario=(
                "Carol marked three lambing-pens with numbers: 1 for north-fold "
                "lambs, 2 for south-fold, 3 for those born late. Tom held a "
                "tally-token marked with the number 2. The form would read the "
                "token and open the right pen door."
            ),
            need=(
                "Tom needed to match the token's value against the marked pens "
                "and find the one with the same mark. The `case` form would read "
                "the token and produce the label of the matching arm."
            ),
            mapping=(
                "`case` matches the first value (2) against each key in order "
                "(1, 2, 3). When a key matches, it takes that arm and "
                "returns its value. The default catches any mismatches."
            ),
            resolution=(
                'the token read 2, it found the matching pen marked 2, and returned `:two` — the pen door opened, and Tom led the lamb to the right place without guessing. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'           )),
        _ex("(case 99 1 :one 2 :two :default)", ":default",
            "case falling through to default", "the default branch",
            scenario=(
                "Tom held a token marked 99, a number never seen before."
            ),
            need=(
                "He needed a fallback when the token didn't match any marked pen."
            ),
            mapping=(
                "`case` checks the value against each key. When no key matches, it returns the fallback arm."
            ),
            resolution=(
                'The token matched no pen, so the form took the fallback arm and returned the default value. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_07 = SubjectCurriculum(grade=5, subject_id="G5-07",
    subject_title="and / or as control flow", fable="boy-wolf",
    examples=[
        _ex("(and 1 2 3)", 3, "the expression (and 1 2 3) returns last truthy", "the last truthy value",
            scenario=(
                "Three fold-gates stood in a row from pasture to the fold. "
                "Carol told Tom: when all three gates open, you can pass. The "
                "first gate held 1 (open), the second held 2 (open), the third "
                "held 3 (open). Tom approached the chain."
            ),
            need=(
                "Tom needed to know if he could pass all three gates. `and` "
                "checks each gate in order: if any is closed (falsey), he stops. "
                "If all are open, he passes through and gets the last one's value."
            ),
            mapping=(
                "`and` walks through the gates left to right. If it finds a "
                "falsey (closed) gate, it stops there and returns that gate's "
                "value. If all gates are truthy (open), it returns the last one."
            ),
            resolution=(
                "all three gates were open, the form passed through them all, and returned 3 — the last gate's value — Tom walked through the fold-gates and stood in the pen, knowing all conditions held. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand."         )),
        _ex("(or nil false :found)", ":found", "the expression (or nil false :found)", "the first truthy value",
            scenario=(
                'Carol left Tom three messages on the stones.'
            ),
            need=(
                "Tom needed to find the first true message by reading from the left."
            ),
            mapping=(
                "`or` walks through values left to right and stops at the first truthy one, returning it."
            ),
            resolution=(
                'The first two stones held nothing, but the third held a real message, so it returned it. Tom chalked {drawn.a} on the village notice, and the morning record stood for the next shepherd to read.'
            )),
    ], subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_08 = SubjectCurriculum(grade=5, subject_id="G5-08",
    subject_title="not", fable="boy-wolf",
    examples=[
        _ex("(not (> 1 2))", True, "the expression (not (> 1 2))", "the negated comparison",
            scenario=(
                "Carol asked Tom to flip the answer to a comparison."
            ),
            need=(
                "Tom needed to invert the boolean result using `not`."
            ),
            mapping=(
                "`not` takes a value and returns the opposite: falsey becomes true, truthy becomes false."
            ),
            resolution=(
                'The comparison produced false, `not` flipped it to true, and the form was done. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'
            )),
    ], subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_09 = SubjectCurriculum(grade=5, subject_id="G5-09",
    subject_title="fn as value", fable="boy-wolf",
    examples=[
        _ex("((fn [f x] (f (f x))) inc 5)", 7,
            "applying f twice to x where f is inc", "the result of inc applied twice",
            scenario=(
                "Carol drew a drill-card on the watchhouse wall with a blank "
                "slot for a recipe and a blank slot for a starting number. "
                "Tom came with the recipe `inc` (add one) and the number 5. "
                "Carol said the card would apply the recipe twice to his number."
            ),
            need=(
                "Tom needed to understand that a recipe could be passed into "
                "another recipe as a value. The outer recipe would accept `inc` "
                "and 5, then apply `inc` twice to get the final result."
            ),
            mapping=(
                "`fn` creates a recipe that accepts a recipe and a value. "
                "It applies the recipe twice."
            ),
            resolution=(
                'The drill-card applied the recipe twice and returned the final result.'
            )),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_10 = SubjectCurriculum(grade=5, subject_id="G5-10",
    subject_title="map", fable="boy-wolf",
    examples=[
        _ex("(map inc [1 2 3])", [2,3,4],
            "the expression (map inc [1 2 3])", "[1 2 3] each incremented",
            scenario=(
                "Carol gave Tom a fleece-comb with three knots in it (standing "
                "for 1, 2, 3) and asked him to add one knot to each. Tom took "
                "the comb and began adding knots — first fleece got one extra, "
                "second got one, third got one."
            ),
            need=(
                "Tom needed to apply the same operation (`inc`, add one) to "
                "every knot in the comb without using a loop. `map` would pour "
                "the fleeces through the comb and apply the rule to each."
            ),
            mapping=(
                "`map` takes a recipe (`inc`) and a basket of values "
                "([1 2 3]). It applies the recipe to each value and collects "
                "the results in a new basket. Every item gets the same treatment; "
                "none are skipped."
            ),
            resolution=(
                'the comb passed each value through: 1+1=2, 2+1=3, 3+1=4, and `map` returned [2 3 4] — a new basket with each fleece carded — Tom saw the pattern and understood `map` was how to do the same thing many times at once. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'         )),
        _ex("(map #(* % %) [1 2 3 4])", [1,4,9,16],
            "the expression (map #(* % %) [1 2 3 4])", "[1 2 3 4] each squared",
            scenario=(
                "Carol gave Tom a comb with four knots and asked him to square each one."
            ),
            need=(
                "Tom needed to apply a complex recipe to each value in the basket."
            ),
            mapping=(
                "`map` applies a recipe to each value in the collection and returns the results."
            ),
            resolution=(
                'The recipe was applied to each value, and `map` returned the collected results (with `1` as the input value) (with `3` as the input value).'
            )),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_11 = SubjectCurriculum(grade=5, subject_id="G5-11",
    subject_title="filter", fable="boy-wolf",
    examples=[
        _ex("(filter even? [1 2 3 4])", [2,4],
            "the expression (filter even? [1 2 3 4])", "the even numbers from [1 2 3 4]",
            scenario=(
                "Carol brought a screen to filter fleeces through."
            ),
            need=(
                "Tom needed to keep only the fleeces that matched the rule."
            ),
            mapping=(
                "`filter` takes a test-rule and keeps only values where the rule is true."
            ),
            resolution=(
                'The form returned only the values that passed the test. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'
            )),
        _ex("(filter pos? [-2 -1 0 1 2])", [1,2],
            "the expression (filter pos? ...)", "the positive numbers",
            scenario=(
                "Carol brought another screen for positive numbers."
            ),
            need=(
                "Tom needed to select only the values that satisfied a different rule."
            ),
            mapping=(
                "`filter` works the same way with any test-rule."
            ),
            resolution=(
                'The form returned only the values that passed the new test. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'
            )),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_12 = SubjectCurriculum(grade=5, subject_id="G5-12",
    subject_title="reduce", fable="boy-wolf",
    examples=[
        _ex("(reduce + [1 2 3 4])",   10, "the expression (reduce + [1 2 3 4])", "the sum",
            scenario=(
                "Tom walked the tally-stick down a line of sheep."
            ),
            need=(
                "Tom needed to combine all the numbers into a single total."
            ),
            mapping=(
                "`reduce` takes a combination-rule and applies it across the list."
            ),
            resolution=(
                'The form combined all values into a single result. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'
            )),
        _ex("(reduce * [1 2 3 4 5])", 120,"the expression (reduce * [1 2 3 4 5])", "5!",
            scenario=(
                "Carol asked Tom to apply a different rule: multiply instead of add."
            ),
            need=(
                "Tom needed to apply multiplication across the list."
            ),
            mapping=(
                "`reduce` works with any combination-rule, whether addition or multiplication."
            ),
            resolution=(
                'The form collapsed the numbers into their product. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
        _ex("(reduce max [3 1 4 1 5 9 2 6])", 9,
            "the expression (reduce max [...])", "the maximum",
            scenario=(
                "Carol asked Tom to find the largest sheep-count among eight pens."
            ),
            need=(
                "Tom needed to find the maximum value using a comparison rule."
            ),
            mapping=(
                "`reduce` works with any comparison-rule to find extreme values."
            ),
            resolution=(
                'The form walked through the list keeping track of the largest and returned it. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'
            )),
    ], subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_13 = SubjectCurriculum(grade=5, subject_id="G5-13",
    subject_title="reduce with init", fable="boy-wolf",
    examples=[
        _ex("(reduce + 100 [1 2 3])", 106,
            "the expression (reduce + 100 [1 2 3])", "100 + sum of [1 2 3]",
            scenario=(
                "Tom arrived at the fold with a tally-stick already marked with "
                "100 knots (from yesterday's flock). Today he found three new "
                "sheep and wanted to add them to the existing count. The stick "
                "started at 100 and grew from there."
            ),
            need=(
                "Tom needed to add the new counts to the old tally, not start "
                "from zero. `reduce` with an initial value would begin the walk "
                "at 100, not at the first sheep in the list."
            ),
            mapping=(
                "`reduce` can take an initial value (100) as the starting point. "
                "It then applies the rule (+) to that initial value and the "
                "first item in the list, then continues as normal."
            ),
            resolution=(
                'the tally began at 100, then 100+1=101, then 101+2=103, then 103+3=106. The final result was 106 — Tom saw that the initial value got factored into the sum from the start, carrying the old count forward. Tom chalked {drawn.a} on the meadow folk notice, and the morning record stood for the next shepherd to read.'           )),
        _ex("(reduce + 0 [])", 0,
            "the expression (reduce + 0 [])",
            "the value when reducing over empty seq with init 0",
            scenario=(
                "Tom arrived at an empty pen with no counts to tally."
            ),
            need=(
                "An initial value ensures the form produces a result even with an empty list."
            ),
            mapping=(
                "`reduce` with an initial value returns it unchanged when the list is empty."
            ),
            resolution=(
                'The list was empty, so it returned the initial value safely. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'
            )),
    ], subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_14 = SubjectCurriculum(grade=5, subject_id="G5-14",
    subject_title="apply", fable="boy-wolf",
    examples=[
        _ex("(apply + [1 2 3 4])", 10,
            "the expression (apply + [1 2 3 4])", "+ applied to the elements of the vector",
            scenario=(
                "Tom held a basket of numbers and a recipe to apply to them all."
            ),
            need=(
                "Tom needed to unpack the basket and feed the numbers to the recipe."
            ),
            mapping=(
                "`apply` unpacks the basket and passes each item as a separate argument to the recipe."
            ),
            resolution=(
                'The basket opened and the recipe processed all the arguments, returning the result. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'
            )),
        _ex("(apply max [3 1 4 1 5])", 5,
            "the expression (apply max ...)", "max of the vector via apply",
            scenario=(
                "Another day, Tom held a basket of sheep-counts [3 1 4 1 5] and "
                "a drill-card with the `max` recipe. Carol asked him to find the "
                "largest number by applying `max` directly to the unpacked list."
            ),
            need=(
                "Tom needed `max` to compare all five numbers at once. `apply` "
                "would unpack the basket so `max` could see all the arguments "
                "and return the largest."
            ),
            mapping=(
                "`apply` works with any recipe. The recipe doesn't care how it "
                "got its arguments; `apply` unpacks the list and feeds them one "
                "by one."
            ),
            resolution=(
                'the basket opened: 3, 1, 4, 1, 5, the `max` recipe compared them all, and the call returned 5 — the largest — Tom saw that `apply` turned a basket into separate arguments for any recipe. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'         )),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_15 = SubjectCurriculum(grade=5, subject_id="G5-15",
    subject_title="comp", fable="boy-wolf",
    examples=[
        _ex("((comp inc inc) 5)", 7,
            "the expression ((comp inc inc) 5)", "inc twice applied to 5",
            scenario=(
                "Carol asked Tom to combine two recipes into one."
            ),
            need=(
                "Tom needed a single recipe that applied both in sequence."
            ),
            mapping=(
                "`comp` chains recipes right-to-left, applying them in order."
            ),
            resolution=(
                'The compound recipe applied both steps and returned the final result (with `5` as the input value).'
            )),
        _ex("((comp str inc) 9)", "10",
            "the expression ((comp str inc) 9)", "inc then str of 9",
            scenario=(
                "Carol drew two more drill-cards: `inc` (add one) and `str` "
                "(turn into text). Tom asked: can I combine these so the result "
                "is text, not a number? Carol composed them: `inc` runs first, "
                "then `str` converts to text."
            ),
            need=(
                "Tom needed a recipe that incremented a number and then turned "
                "the result into text. `comp` would chain them: first `inc` to "
                "get the number, then `str` to get the text."
            ),
            mapping=(
                "`comp` works with any recipes. Right-to-left order: `(comp "
                "str inc)` means apply `inc` first (9 becomes 10), then apply "
                "`str` to the result (10 becomes \"10\")."
            ),
            resolution=(
                'the compound recipe took 9, applied `inc` (got 10), then applied `str` (got "10"), and returned the text — Tom saw that `comp` could transform not just the number but also the type, by chaining recipes in order.'
            )),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_16 = SubjectCurriculum(grade=5, subject_id="G5-16",
    subject_title="partial", fable="boy-wolf",
    examples=[
        _ex("((partial + 10) 5)", 15,
            "the expression ((partial + 10) 5)", "10 + 5",
            scenario=(
                "Carol handed Tom the `+` recipe but asked him to fill in one "
                "ingredient now and leave a blank for later. Tom wrote 10 in the "
                "blank, making a new recipe that said: add 10 to whatever comes. "
                "Later, he handed 5 to the partial recipe."
            ),
            need=(
                "Tom needed a way to pre-fill one argument to a recipe and make "
                "a new recipe that was ready to take the rest. `partial` would "
                "fill in the first argument and wait for the second."
            ),
            mapping=(
                "`partial` takes a recipe and some arguments and creates a new "
                "recipe with those arguments pre-filled. `(partial + 10)` is a "
                "new recipe that adds 10. When called with 5, it computes 10+5."
            ),
            resolution=(
                'the partial recipe took 5, added it to the pre-filled 10, and returned 15 — Tom saw that `partial` let him customize a recipe without changing the original.'
            )),
        _ex("(map (partial * 3) [1 2 3])", [3,6,9],
            "(partial * 3) mapped over [1 2 3]", "each element times 3",
            scenario=(
                "Carol wanted Tom to triple every number in the basket [1 2 3]. "
                "She could write a long recipe or use `partial`: make a recipe "
                "that says multiply by 3, then feed that recipe to `map`."
            ),
            need=(
                "Tom needed to use `map` with a recipe that multiplies by 3. "
                "Instead of writing a whole new recipe, `partial` would create "
                "one by pre-filling the `*` recipe with 3."
            ),
            mapping=(
                "`partial` creates a specialized recipe that `map` can use. "
                "`(partial * 3)` is a recipe ready to multiply its argument by "
                "3. `map` applies it to each item in the list."
            ),
            resolution=(
                '`map` took the partial recipe and applied it three times: 3*1=3, 3*2=6, 3*3=9, returning [3 6 9] — Tom saw that `partial` let him specialize a recipe so `map` could use it elegantly. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'           )),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_17 = SubjectCurriculum(grade=5, subject_id="G5-17",
    subject_title="juxt", fable="boy-wolf",
    examples=[
        _ex("((juxt inc dec) 5)", [6,4],
            "the expression ((juxt inc dec) 5)", "inc and dec of 5 in parallel",
            scenario=(
                "Carol drew two recipes side by side and asked Tom to apply both."
            ),
            need=(
                "Tom needed to run both recipes on the same input and gather both results."
            ),
            mapping=(
                "`juxt` applies each recipe to the same input and collects the results in a basket."
            ),
            resolution=(
                'The form applied both recipes and returned the collected results side by side (with `5` as the input value).'
            )),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_18 = SubjectCurriculum(grade=5, subject_id="G5-18",
    subject_title="some", fable="boy-wolf",
    examples=[
        _ex("(some even? [1 3 5 8 7])", True,
            "the expression (some even? [...])", "whether any element is even",
            scenario=(
                "Tom asked Carol if any count in the basket was even."
            ),
            need=(
                "Tom needed to know without checking all of them."
            ),
            mapping=(
                "`some` tests values until one passes the rule and stops immediately."
            ),
            resolution=(
                'The form found a match and returned the verdict without checking all values. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'
            )),
        _ex("(some neg? [1 2 3])", None,
            "the expression (some neg? [1 2 3])", "the value when no element is negative",
            scenario=(
                "Another day, Tom asked: is there a negative count in [1 2 3]? "
                "The screen for `neg?` (negative numbers) wouldn't catch any of "
                "them. Carol said: `some` will return nil when nothing passes."
            ),
            need=(
                "Tom needed to distinguish between finding something and finding "
                "nothing. `some` would return nil if no element passed the test, "
                "so he'd know all counts were positive."
            ),
            mapping=(
                "`some` returns nil if no element passes the test. This is "
                "different from `filter`, which returns an empty list. `some` "
                "returns nil — nothing matched."
            ),
            resolution=(
                'the screen caught nothing (all three were positive), and `some` returned nil — Tom knew that no negative number existed in the list. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'           )),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_19 = SubjectCurriculum(grade=5, subject_id="G5-19",
    subject_title="every?", fable="boy-wolf",
    examples=[
        _ex("(every? pos? [1 2 3])", True, "the expression (every? pos? [1 2 3])", "whether all are positive",
            scenario=(
                "Carol brought three fleece-bundles with weights [1 2 3] and "
                "asked Tom: are all of them positive numbers? `every?` would pour "
                "them all through the `pos?` screen and check that all passed."
            ),
            need=(
                "Tom needed to verify that every single count met the rule. "
                "`every?` would check all of them and return true only if none "
                "failed."
            ),
            mapping=(
                "`every?` pours all values through a test. If any fail, it "
                "returns false immediately. If all pass, it returns true. It's "
                "an all-or-nothing check."
            ),
            resolution=(
                'the screen passed all three: 1 is positive, 2 is positive, 3 is positive — `every?` returned true — Tom knew that every bundle was above zero. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'         )),
        _ex("(every? even? [1 2 3])", False, "the expression (every? even? [1 2 3])", "whether all are even",
            scenario=(
                "Carol asked: are all these numbers even? Tom looked: 1 (odd), 2 "
                "(even), 3 (odd). The screen for `even?` would catch 2 but not "
                "1 — the test would fail immediately."
            ),
            need=(
                "Tom needed to know if every single count was even. Since the "
                "first one failed, `every?` could stop checking and return false "
                "without looking further."
            ),
            mapping=(
                "`every?` is strict: it returns false as soon as it finds any "
                "value that fails the test. There's no need to check the rest "
                "once one fails."
            ),
            resolution=(
                'the screen rejected 1 (odd), and `every?` stopped and returned false — Tom knew immediately that not every number was even without checking all three. Tom chalked {drawn.a} on the townsfolk notice, and the morning record stood for the next shepherd to read.'           )),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_20 = SubjectCurriculum(grade=5, subject_id="G5-20",
    subject_title="take and drop", fable="boy-wolf",
    examples=[
        _ex("(take 3 [10 20 30 40 50])", [10,20,30],
            "the expression (take 3 ...)", "the first three elements",
            scenario=(
                "Tom held a long comb with five knots [10 20 30 40 50] and Carol "
                "asked: keep only the first three knots and drop the rest. `take` "
                "would snip the comb after the third knot."
            ),
            need=(
                "Tom needed to take the first few items and leave the rest "
                "behind. `take` would count from the start and stop at the "
                "requested number."
            ),
            mapping=(
                "`take` counts n items from the beginning of a list and returns "
                "just those. Everything after the nth item is left behind; no "
                "second basket is created."
            ),
            resolution=(
                'the comb kept [10 20 30] and dropped 40 and 50 — Tom held a shorter comb with exactly three knots — `take` had trimmed the list to the size he needed. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'         )),
        _ex("(drop 2 [10 20 30 40 50])", [30,40,50],
            "the expression (drop 2 ...)", "all but the first two",
            scenario=(
                "Carol asked Tom to skip the first two counts and keep the rest."
            ),
            need=(
                "Tom needed to skip the first few items and keep everything else."
            ),
            mapping=(
                "`drop` skips the first n items and returns all the rest."
            ),
            resolution=(
                'The form skipped the first items and returned the tail of the sequence. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'
            )),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_21 = SubjectCurriculum(grade=5, subject_id="G5-21",
    subject_title="distinct and sort", fable="boy-wolf",
    examples=[
        _ex("(distinct [1 1 2 3 3 4])", [1,2,3,4],
            "the expression (distinct [1 1 2 3 3 4])", "the deduplicated seq",
            scenario=(
                "Tom counted sheep by brand and found duplicates: [1 1 2 3 3 4]. "
                "Carol asked: how many different brands were there? `distinct` "
                "would remove the duplicates and show each brand once."
            ),
            need=(
                "Tom needed to know which unique brands existed, not how many of "
                "each. `distinct` would keep only the first occurrence of each "
                "brand and drop the rest."
            ),
            mapping=(
                "`distinct` walks through a list and removes duplicates, keeping "
                "each unique value exactly once. The result is a shorter list "
                "with no repeats."
            ),
            resolution=(
                'the list lost the duplicate 1 and the duplicate 3, leaving [1 2 3 4] — Tom saw four distinct brands and understood how many different groups existed. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'           )),
        _ex("(sort [3 1 2])", [1,2,3],
            "the expression (sort [3 1 2])", "the sorted seq",
            scenario=(
                "Tom brought three fleece-counts [3 1 2] in jumbled order and "
                "Carol asked: arrange them from smallest to largest. `sort` would "
                "rearrange the numbers in ascending order."
            ),
            need=(
                "Tom needed the counts in a sensible order for the records. "
                "`sort` would put them from smallest to largest, making the "
                "pattern clear."
            ),
            mapping=(
                "`sort` arranges items in order (smallest to largest by default). "
                "It takes a jumbled list and returns a new list with the same "
                "items rearranged."
            ),
            resolution=(
                'the list rearranged from [3 1 2] to [1 2 3] — Tom held the sorted counts and could see the pattern: the smallest, then the medium, then the largest. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'           )),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_22 = SubjectCurriculum(grade=5, subject_id="G5-22",
    subject_title="recur — first taste", fable="boy-wolf",
    examples=[
        _ex("(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))", 120,
            "a loop computing factorial of 5 via recur",
            "5! computed via loop/recur",
            scenario=(
                "At dawn, Tom set out to walk the fence-line that ringed "
                "the south pasture — the same circuit he walked every "
                "morning. Carol watched from the lookout, ready to read "
                "the count when he came back round."
            ),
            need=(
                "The walk had to cover the whole circuit and return to "
                "the start carrying the running count, without leaving a "
                "growing trail of footprints behind. The village wanted "
                "the morning's tally, no matter how long the loop was."
            ),
                mapping=(
                "`recur` takes a step forward on the same fence-walk "
                "without growing the trail behind it — each step "
                "replaces the last. The base case ends the walk; "
                "everywhere else, the loop steps and continues."
            ),
            resolution=(
                'the walk completed the circuit and the loop returned the running tally — 120 — without leaving a single extra footprint along the fence-line (with `5` as the input value).'
            )),
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
    print(f"grade-5 boy-wolf smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
