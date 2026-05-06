"""Grade 5 — control flow + higher-order intro. Through fox-grapes.

Reuses the grade-1 8-subplot pool and adds two HOF-flavored subplots
in fox voice: the patient fox demonstrates how a single operation, when
mapped/reduced/applied across a cluster, settles a long calculation —
while the hasty fox keeps wanting to skip the eval entirely.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.fox_grapes.grade_1 import _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL
from mmllm.aesop.curriculum.fox_grapes._metaphor_pools import (
    _CIRCUIT_SUBPLOTS,
    _FORK_SUBPLOTS,
    _GATE_SUBPLOTS,
    _RECIPE_SUBPLOTS,
    _SIEVE_SUBPLOTS,
    _TALLYWALK_SUBPLOTS,
)


_HOF_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [
    SubplotTemplate("""\
{patient_fox_phrase} demonstrated {place} how a single operation,
applied to a whole cluster at once, was the heart of every long
calculation. The form {form_display} captured {concept_phrase}, and
{hasty_fox_phrase} agreed to write it for the REPL."""),

    SubplotTemplate("""\
"Every jump, every reach, every attempt at the cluster — the same
trick repeated cleverly," {patient_fox} said {place}, sketching the
form {form_display} into the dust. {hasty_fox}, {emo_proud}, claimed
to know exactly what {concept_phrase} would produce — but {patient_fox}
insisted, again, that the REPL was the only honest judge."""),
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


_PLAN_G5 = _PLAN_POOL + (
    "I use map / filter / reduce as appropriate.",
    "I write the higher-order form so the REPL can compute.",
)


G5_01 = SubjectCurriculum(grade=5, subject_id="G5-01",
    subject_title="if", fable="fox-grapes",
    examples=[
        _ex("(if true :a :b)",
            ":a",
            'the if-fork with a true test',
            "the keyword on the prong the fork's true test selects",
            goal='choose :a when the test is true, otherwise :b',
            scenario='Renard the fox came to a fork in the orchard path. A small wooden sign at the fork carried a test; the left prong led to one keyword, the right prong to another.',
            need="Renard had to take exactly one prong, and the choice depended on whether the test held. The other prong would stay untravelled; only one branch's value would be returned.",
            mapping="`if` is the fork: the test decides which prong runs, the other is skipped entirely. When the test holds, the left prong's value is returned; when it does not, the right prong's is. One branch evaluates; the other is not even visited.",
            resolution='the test held, the left prong was taken, and the form returned the value at that branch — exactly the destination the fork had pointed Renard toward.',
            tags=("story",)),
        _ex("(if false :a :b)", ":b", 'the if-fork with a false test',
            "the keyword on the prong the fork's false test selects",
            goal='choose :b when the test is false',
            scenario='Vix the fox stood at the eastern orchard fork. The sign bore a test that held for the left prong, did not for the right. The right path led to a specific keyword outcome.',
            need="Vix needed to take the path the test rejected — the false branch — and discover what waited there instead of the left prong's value.",
            mapping="`if` skips the branch when the test fails; only the false-path evaluates. The right prong's value travels back, not the left.",
            resolution='the test failed, the right prong held the path forward, and the form returned the value waiting there.',
            tags=("story",)),
        _ex("(if (> 5 3) :a :b)", ":a", 'the if-fork where the test compares two numbers',
            "the keyword the fork's numeric test selects",
            goal='choose based on whether five exceeds three',
            scenario='Sly the fox arrived at the northern fork carrying two acorn counts: five from the summer row, three from spring. A carved sign at the fork posed: does the first exceed the second?',
            need="Sly had to trace the path the comparison chose — if five truly outweighed three, the left prong held the answer; if not, the right did.",
            mapping="`if` tests the numeric claim before deciding. The greater-than check is the fork's sign; the prongs lead to different values.",
            resolution='five did exceed three, the left path lay ahead, and the form returned the left-prong value.',
            tags=("story",)),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_02 = SubjectCurriculum(grade=5, subject_id="G5-02",
    subject_title="if as expression", fable="fox-grapes",
    examples=[
        _ex("(+ 1 (if true 10 20))", 11, 'the if-fork nested in an addition',
            "the sum after if picks the first prong value",
            goal='add one to the result of an if that chooses between two numbers',
            scenario='Renard the fox gathered grapes: one sure cluster in paw, plus a fork ahead offering either ten or twenty more depending on which path he took. He wanted to count the total.',
            need="Renard needed the if to pick its branch first, then add that picked value to the one he held. The fork must decide before the addition could run.",
            mapping="`if` nested in `+` evaluates first: the test picks a branch, that branch returns a value, then `+` adds one to it. The fork is not separate from the sum — it feeds into it.",
            resolution='the if-path chose ten, the one and ten summed, and the nested form returned the total.',
            tags=("story",)),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_03 = SubjectCurriculum(grade=5, subject_id="G5-03",
    subject_title="when", fable="fox-grapes",
    examples=[
        _ex("(when true :yes)", ":yes", 'the when-fork that only goes if the test holds',
            "the keyword when returns when the test is true",
            goal='return a value only when the test is true',
            scenario='Vix the fox reached a fork marked by a sign: "only proceed if the test holds." The left path, if the test passed, held a keyword outcome. If the test failed, nothing — the path led to the thicket.',
            need="Vix wanted to take the path only when permitted by the test. If the test said no, she would not travel the left path at all.",
            mapping="`when` is a fork that either takes the true branch or stops: the path exists when the test holds, disappears when it fails. No right-prong fallback; only forward or nowhere.",
            resolution='the test held true, the path opened, and the form returned the keyword waiting there.',
            tags=("story",)),
        _ex("(when false :yes)", None, 'the when-fork that stops if the test fails',
            "nil when the test is false",
            goal='return nothing when the test is false',
            scenario='Sly the fox came to a when-fork where the sign bore a false claim. The left path led to a keyword, but the fork required the test to pass before any path could be taken.',
            need="Sly needed the fork to block the path since the test was false. The left branch would not run; the fork would return nothing at all.",
            mapping="`when` halts when the test fails; there is no branch that evaluates, no value returned, only nil—the empty space where no path led.",
            resolution='the test failed, both paths closed, and the form returned nil — the symbol for no path taken.',
            tags=("story",)),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_04 = SubjectCurriculum(grade=5, subject_id="G5-04",
    subject_title="cond", fable="fox-grapes",
    examples=[
        _ex("(cond (= 1 2) :a (= 1 1) :b :else :c)", ":b", 'the cond tree of multiple forks',
            "the keyword the second fork's test chooses",
            goal='walk a tree of tests until one passes, then return its branch',
            scenario='Renard the fox came to a stand of three forks branching from a common trunk. At the first fork: a sign asking "does one equal two?". At the second: "does one equal one?". At the base: an :else path for when all other tests failed.',
            need="Renard had to walk the tree, testing each fork in order, moving forward only when a test passed. The first fork rejected him; the second opened; he took that branch.",
            mapping="`cond` is a tree: it tests conditions left-to-right; the first true test halts the tree and returns its branch value. All later branches are skipped. The :else path fires only if every earlier test failed.",
            resolution='the first test failed, the second passed, and the form returned the second fork\'s value.',
            tags=("story",)),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_05 = SubjectCurriculum(grade=5, subject_id="G5-05",
    subject_title="cond — :else", fable="fox-grapes",
    examples=[
        _ex("(cond false :a false :b :else :c)", ":c", 'the cond tree that reaches its :else',
            "the keyword the :else branch returns when all tests fail",
            goal='reach the else branch after all earlier tests reject the path',
            scenario='Vix the fox walked a cond tree with three posts. The first said: false. The second said: false again. At the tree\'s base, a weathered :else stone promised shelter if no other path opened.',
            need="Vix tested the first post — false blocked her. She tested the second — false again. With no other option ahead, she turned to the :else stone and took the path it marked.",
            mapping="`cond` tests until a true condition halts the walk. If every test is false, :else catches the fall and returns its branch value. The :else is the forest's safety path when all named forks fail.",
            resolution='both early tests rejected the path, the :else stone claimed her, and the form returned the else-branch value.',
            tags=("story",)),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_06 = SubjectCurriculum(grade=5, subject_id="G5-06",
    subject_title="case", fable="fox-grapes",
    examples=[
        _ex("(case 2 1 :one 2 :two 3 :three :default)", ":two", 'the case-sign matching a number to its branch',
            "the keyword matching the tested value",
            goal='jump to the branch whose label matches the test number',
            scenario='Sly the fox held a number: two. At the fork stood a weathered sign listing paths: one led to :one, two to :two, three to :three, and a :default path for any unlisted number. Sly would trace the match from number to branch.',
            need="Sly needed to find which path his number unlocked. The sign was a lock-and-key: the number two matched its compartment, and that compartment held the value waiting.",
            mapping="`case` is a sign with compartments; each compartment is labeled with a value. The case matches the input number against the labels, then returns the branch value from the matching compartment. If no label matches, the :default path opens.",
            resolution='the number two matched the second compartment, the sign unlocked, and the form returned the value waiting in that branch.',
            tags=("story",)),
        _ex("(case 99 1 :one 2 :two :default)", ":default", 'the case-sign when no label matches',
            "the default value when the number matches no compartment",
            goal='fall through to default when the case value matches no listed key',
            scenario='Renard the fox held the number ninety-nine. At a case-sign sat labeled paths: one to :one, two to :two, plus a :default path for any number outside the list. Ninety-nine was not on the sign.',
            need="Renard traced his number against the sign\'s labels. Ninety-nine was not among them. With no match, the :default path was the only door left.",
            mapping="`case` tries to match the input against each label in turn. When no label matches, case falls back to the :default compartment, returning its value. The default is the catch-all.",
            resolution='ninety-nine found no matching label, the :default opened, and the form returned the default value.',
            tags=("story",)),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_07 = SubjectCurriculum(grade=5, subject_id="G5-07",
    subject_title="and / or as control flow", fable="fox-grapes",
    examples=[
        _ex("(and 1 2 3)", 3, 'the and-gate latch that lifts when all three lock-bars raise',
            "the last lock-bar height when all have lifted",
            goal='test that three values all pass the truthy gate, returning the last one',
            scenario='Vix the fox came to an orchard gate with three lock-bars stacked vertically. All three had to lift for the gate to swing open. She raised the first bar: truthy. The second: truthy. The third: truthy. The gate would open.',
            need="Vix needed all three bars to lift—if even one stayed stuck, the gate would not budge. She wanted to know the state of the last bar if all had risen.",
            mapping="`and` is a chain of gates: each value must be truthy to reach the next. If any value is falsey, the chain stops and returns that falsey value. If all are truthy, `and` returns the last one.",
            resolution='all three bars rose, the gate swung open, and the form returned the height of the last lock-bar.',
            tags=("story",)),
        _ex("(or nil false :found)", ":found", 'the or-gate latch that lifts when any of three paths carries truth',
            "the first truthy value among three options",
            goal='find the first truthy value among three options',
            scenario='Renard the fox stood at an or-gate with three paths: the first led to nil (a ghost-path), the second to false (a phantom), the third to a keyword :found (solid ground). The gate would lift if any path held solid ground.',
            need="Renard needed at least one true option to pass. The first two paths ghosted away; the third was real. He wanted the first true value he found.",
            mapping="`or` walks a chain of values, stopping at the first truthy one and returning it. If all values are falsey, `or` returns the last (falsey) value. It is the gate that lifts on any ground.",
            resolution='the first two paths vanished, the third held :found, and the form returned that first truthy value.',
            tags=("story",)),
    ], subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_08 = SubjectCurriculum(grade=5, subject_id="G5-08",
    subject_title="not", fable="fox-grapes",
    examples=[
        _ex("(not (> 1 2))", True, 'the not-gate that flips the latch',
            "true when the comparison is false",
            goal='flip a false comparison to true using not',
            scenario='Sly the fox tested a claim: "Is one greater than two?" The claim was false. But he wore a not-latch at his chest—a gear that flipped false to true and true to false. The false claim became true through the latch.',
            need="Sly needed to flip the claim\'s verdict. The original test said false; the not-latch would invert it to true.",
            mapping="`not` is an inverting gate: it receives a value\'s truth state and flips it. False becomes true; true becomes false. No gate is simpler—it only reverses.",
            resolution='the inner test was false, the not-latch flipped it, and the form returned true.',
            tags=("story",)),
    ], subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_09 = SubjectCurriculum(grade=5, subject_id="G5-09",
    subject_title="fn as value", fable="fox-grapes",
    examples=[
        _ex("((fn [f x] (f (f x))) inc 5)", 7, 'the recipe-card that takes a card and a number, applies the card twice',
            "the final value after applying the function twice",
            goal='write a recipe-card that takes another card and a number, applies the card to the number twice',
            scenario='Renard the fox pinned a fresh tasting-card to the post. It said: take a card (f) and a number (x); apply that card to x, then apply it again to the result. He fed it the inc card and the number five.',
            need="Renard wanted to know what happened when a card was applied twice in a row. The inc card would add one twice, starting from five.",
            mapping="A function that takes a function as an argument is a recipe-card that uses another card. `(f (f x))` means: apply f to x, then apply f to that result. The outer card's step is a nested application.",
            resolution='inc was applied to five (six), then applied again to six (seven), and the form returned the doubled result.',
            tags=("story",)),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_10 = SubjectCurriculum(grade=5, subject_id="G5-10",
    subject_title="map", fable="fox-grapes",
    examples=[
        _ex("(map inc [1 2 3])", [2,3,4], 'the sieve that increments each cluster',
            "the list of incremented numbers",
            goal='apply inc to each number in the row, collecting results',
            scenario='Vix the fox held a sieve above a bucket, with a row of three clusters sitting inside: one, two, three. Each cluster would pass through the sieve, inc would touch it, and it would fall transformed into the bucket.',
            need="Vix wanted to increment every cluster in the row at once. The sieve would apply inc uniformly, and the bucket would gather the new row.",
            mapping="`map` is a sieve: it holds an operation (inc) above a collection, passing each item through. The operation transforms each item in turn. The sieve collects every transformed item into a new row.",
            resolution='each cluster rose through inc: one became two, two became three, three became four. The bucket held the new row.',
            tags=("story",)),
        _ex("(map #(* % %) [1 2 3 4])", [1,4,9,16], 'the sieve that squares each cluster',
            "the list of squared numbers",
            goal='apply squaring to each number in the row',
            scenario='Sly the fox set a sieve above a fresh bucket, holding a row of four clusters: one, two, three, four. Above the sieve hung a tasting-card that took a cluster, multiplied it by itself, and returned the squared result.',
            need="Sly wanted every cluster squared in one motion. The sieve would drop each through the card, and the bucket would catch the squared version.",
            mapping="`map` applies the anonymous card (#(* % %)) to each cluster. The percent sign is the cluster passing through. Multiply it by itself, drop it in the bucket transformed.",
            resolution='each cluster squared: one stayed one, two became four, three became nine, four became sixteen. The bucket held the squared row.',
            tags=("story",)),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_11 = SubjectCurriculum(grade=5, subject_id="G5-11",
    subject_title="filter", fable="fox-grapes",
    examples=[
        _ex("(filter even? [1 2 3 4])", [2,4], 'the sieve that keeps only even clusters',
            "the list of even numbers that passed through",
            goal='sift the row to keep only even numbers, removing odd ones',
            scenario='Renard the fox held a sieve with a fine mesh—a test that said "let only even numbers through." Below sat a bucket. He poured a row through: one, two, three, four.',
            need="Renard wanted only the even clusters in his bucket. The sieve\'s mesh would trap the odd ones and let the even ones fall.",
            mapping="`filter` is a sieve with a rule: even? checks each cluster; if true, it falls through; if false, it stays trapped. The bucket collects only what passed the rule.",
            resolution='one was trapped as odd, two fell through as even, three was trapped as odd, four fell through as even. The bucket held only the even row.',
            tags=("story",)),
        _ex("(filter pos? [-2 -1 0 1 2])", [1,2], 'the sieve that keeps only positive clusters',
            "the list of positive numbers that passed through",
            goal='sift the row to keep only positive numbers',
            scenario='Vix the fox stood at a sieve that tested each cluster: "Is this cluster positive—above zero?" She had a mixed row: negative two, negative one, zero, one, two. The sieve would catch the non-positive and let the positive through.',
            need="Vix wanted only the positive clusters in her bucket. Negative and zero clusters would be held back; positive ones would fall free.",
            mapping="`filter` with pos? keeps only clusters that exceed zero. Any cluster at zero or below is trapped by the rule and does not fall through.",
            resolution='the negative and zero clusters stayed at the sieve, one and two passed through, and the bucket held only the positive row.',
            tags=("story",)),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_12 = SubjectCurriculum(grade=5, subject_id="G5-12",
    subject_title="reduce", fable="fox-grapes",
    examples=[
        _ex("(reduce + [1 2 3 4])", 10, 'the tally-walk summing clusters',
            "the final sum after walking the row",
            goal='walk a row of numbers, adding each to a running sum',
            scenario='Renard the fox walked the vine-row with a slate, starting at zero. At the first vine: one cluster. He added one to his slate; it read one. At the next: two clusters. He added; the slate read three. At the third: three clusters. He added; the slate read six. At the fourth: four clusters. He added; the slate read ten. He had walked the entire row.',
            need="Renard wanted the sum of every cluster in the row—a single number at the walk's end, the total of the journey.",
            mapping="`reduce` is the tally-walk: it starts with zero (or a given seed), walks each item in the row, adding (or applying the operation) to build a running total, then returns the final count.",
            resolution='the walk was complete, the slate held the sum of all four clusters, and the form returned the final tally.',
            tags=("story",)),
        _ex("(reduce * [1 2 3 4 5])",
            120,
            'the tally-walk multiplying clusters',
            "the final product after walking the row",
            goal='walk a row of numbers, multiplying each into a running product',
            scenario='Sly the fox walked the vine-row with a slate, starting at one. At the first vine: two clusters. He multiplied; the slate read two. At the second: three clusters. He multiplied; the slate read six. At the third: four clusters; the slate read twenty-four. At the fourth: five clusters; the slate read one hundred twenty. The row lay behind him.',
            need="Sly wanted the product of every cluster in the row—the result of walking each vine and multiplying its count into the running total.",
            mapping="`reduce` with `*` is the product-walk: start at one, multiply each item into the running product. The slate grows by multiplication with each step forward.",
            resolution='the walk ended at the last vine, the slate held the product of all five, and the form returned the final product.',
            tags=("story",)),
        _ex("(reduce max [3 1 4 1 5 9 2 6])",
            9,
            'the tally-walk finding the greatest cluster',
            "the largest number after walking the row",
            goal='walk the row, keeping only the largest cluster seen so far',
            scenario='Vix the fox walked the vine-row with a slate, tracking the largest cluster she had passed. At three clusters, she noted three. Then one—smaller, so the slate stayed at three. Then four—larger, she updated to four. Then one, five, nine, two, six. Each vine, she looked and kept the greatest seen yet.',
            need="Vix wanted to know the largest cluster anywhere in the row. The tally-walk would track the maximum as she moved.",
            mapping="`reduce` with `max` compares each item against the running maximum. If the item is larger, it becomes the new maximum. The tally records the largest seen so far.",
            resolution='the walk was done, and the slate held the greatest cluster in the entire row.',
            tags=("story",)),
    ], subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_13 = SubjectCurriculum(grade=5, subject_id="G5-13",
    subject_title="reduce with init", fable="fox-grapes",
    examples=[
        _ex("(reduce + 100 [1 2 3])", 106, 'the form', 'the value the form evaluates to'),
        _ex("(reduce + 0 [])",
            0,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox walked the vine-row with a slate, ticking off each cluster as his passed it.',
            need="Renard wanted the row's length or running total — a single honest number when the walk ended.",
            mapping='`reduce` and `count` are the tally-walk: visit each item once, tick or accumulate, return the final total.',
            resolution="the slate at the row's end held the honest tally — exactly what the walk had produced.",
            tags=("story",)),
    ], subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_14 = SubjectCurriculum(grade=5, subject_id="G5-14",
    subject_title="apply", fable="fox-grapes",
    examples=[
        _ex("(apply + [1 2 3 4])", 10, 'the form', 'the value the form evaluates to'),
        _ex("(apply max [3 1 4 1 5])", 5, 'the form', 'the value the form evaluates to'),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_15 = SubjectCurriculum(grade=5, subject_id="G5-15",
    subject_title="comp", fable="fox-grapes",
    examples=[
        _ex("((comp inc inc) 5)", 7, 'the form', 'the value the form evaluates to'),
        _ex("((comp str inc) 9)", "10", 'the form', 'the value the form evaluates to'),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_16 = SubjectCurriculum(grade=5, subject_id="G5-16",
    subject_title="partial", fable="fox-grapes",
    examples=[
        _ex("((partial + 10) 5)", 15, 'the form', 'the value the form evaluates to'),
        _ex("(map (partial * 3) [1 2 3])", [3,6,9], 'the form', 'the value the form evaluates to'),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_17 = SubjectCurriculum(grade=5, subject_id="G5-17",
    subject_title="juxt", fable="fox-grapes",
    examples=[
        _ex("((juxt inc dec) 5)", [6,4], 'the form', 'the value the form evaluates to'),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_18 = SubjectCurriculum(grade=5, subject_id="G5-18",
    subject_title="some", fable="fox-grapes",
    examples=[
        _ex("(some even? [1 3 5 8 7])", True, 'the form', 'the value the form evaluates to'),
        _ex("(some neg? [1 2 3])", None, 'the form', 'the value the form evaluates to'),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_19 = SubjectCurriculum(grade=5, subject_id="G5-19",
    subject_title="every?", fable="fox-grapes",
    examples=[
        _ex("(every? pos? [1 2 3])", True, 'the form', 'the value the form evaluates to'),
        _ex("(every? even? [1 2 3])", False, 'the form', 'the value the form evaluates to'),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_20 = SubjectCurriculum(grade=5, subject_id="G5-20",
    subject_title="take and drop", fable="fox-grapes",
    examples=[
        _ex("(take 3 [10 20 30 40 50])", [10,20,30], 'the form', 'the value the form evaluates to'),
        _ex("(drop 2 [10 20 30 40 50])", [30,40,50], 'the form', 'the value the form evaluates to'),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_21 = SubjectCurriculum(grade=5, subject_id="G5-21",
    subject_title="distinct and sort", fable="fox-grapes",
    examples=[
        _ex("(distinct [1 1 2 3 3 4])", [1,2,3,4], 'the form', 'the value the form evaluates to'),
        _ex("(sort [3 1 2])", [1,2,3], 'the form', 'the value the form evaluates to'),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_22 = SubjectCurriculum(grade=5, subject_id="G5-22",
    subject_title="recur — first taste", fable="fox-grapes",
    examples=[
        _ex("(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))",
            120,
            'the loop-recur factorial of five',
            'the row-end product after walking the five-vine row',
            goal='compute the factorial of 5 by looping a counter down to 0 with a running product',
            scenario="Sly the fox stood at the head of a five-vine row, slate in paw. On each lap he would multiply the running tally by the current vine's number, then walk back to the head of the row with the new tally and the next vine to count.",
            need='Sly wanted the running product of all five vine-numbers — five times four times three and so on down — landing as the row-end tally on the slate.',
            mapping="`loop` sets the head of the row with starting bindings; `recur` is walking back to that head with new values, not stacking new walks on the old. The base case `zero?` is the row's end — no more vines to multiply, return the tally.",
            resolution="after the fifth lap the row's end was reached, and the slate held the running product of every vine — exactly the factorial Sly had set out to count.",
            tags=("story",)),
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
    print(f"grade-5 fox-grapes smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
