"""Grade 3 — naming, scope, substitution. through the milkmaid fable.

The fable lens: the Farmer's careful approach is exactly the
substitution-rule discipline. The Milkmaid's "I just know the answer"
is what binding-by-name corrects.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.milkmaid.grade_1 import (
    _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.milkmaid._metaphor_pools import (
    _POUCH_SUBPLOTS, _RECIPE_SUBPLOTS, _ROADSIGN_SUBPLOTS, _SCRIBE_SUBPLOTS,
)

# Add naming-themed subplots: a character names a value, then references it.
# Based on _GOAL_SUBPLOTS to ensure goal-driven design.
_NAMING_SUBPLOTS: list[SubplotTemplate] = list(_GOAL_SUBPLOTS) + [
    SubplotTemplate("""\
{farmer_phrase}, {emo_patient} kept a small ledger {place} where every meaningful
quantity got its own name. {farmer_he_she_cap} pointed to today's
entry, which required {goal_text}. {farmer_he_she_cap} would write
{concept_phrase} and let the REPL confirm."""),

    SubplotTemplate("""\
"The key is to name your values carefully," {farmer} said {place}.
"To {goal_text}, you write {concept_phrase} and submit it to the REPL.
That is the discipline." {milkmaid_phrase} nodded, {emo_tired}."""),
]


def _ex(form, expected, concept, what, goal=""):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal)


_PLAN_POOL_G3 = _PLAN_POOL + (
    "I bind the inputs in a let, then compute.",
    "I name the values first and then combine them.",
    "I write the let-form so the REPL can substitute.",
)


G3_01 = SubjectCurriculum(grade=3, subject_id="G3-01",
    subject_title="def — top-level binding", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(do (def x 42) x)",
            expected=42,
            concept_phrase="the top-level binding and lookup",
            question_what="the value of x after using def to bind x to 42",
            goal_text="bind x to 42 and return it",
            scenario=(
                "The milkmaid had nailed a name-card labelled x to the market-board "
                "at the village square, with the price chalked beside it for all "
                "buyers to read."
            ),
            need=(
                "Any buyer who walked up and read x from the board needed to receive "
                "the 42 that had been posted — the board had to hold the name "
                "permanently and return it on demand."
            ),
            mapping=(
                "`def` is the act of nailing the name-card to the market-board: it "
                "posts x in the namespace so every caller can look it up. The second "
                "form reads x back off the board."
            ),
            resolution=(
                "The board carried the name, and the REPL returned the posted value "
                "when x was looked up — the market-board had done its work."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def y 7) y)",
            expected=7,
            concept_phrase="the top-level binding",
            question_what="the value of y after using def to bind y to 7",
            goal_text="bind y to 7 and return it",
            scenario=(
                "The milkmaid had chalked y onto the market-board beside a coin-count, "
                "nailing the name in place so farmers passing the village square could "
                "read it at any hour."
            ),
            need=(
                "She needed the board to hold y steadily — not in a pocket that "
                "emptied at the road's end, but posted where every future caller "
                "could find it."
            ),
            mapping=(
                "`def` nails y to the market-board for the whole session: the name "
                "is public and permanent. Looking up y afterwards simply reads what "
                "was posted."
            ),
            resolution=(
                "The REPL read y from the board and returned the coin-count that "
                "had been nailed there — the market-board delivered the name — 7."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_02 = SubjectCurriculum(grade=3, subject_id="G3-02",
    subject_title="def — redefinition", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(do (def x 1) (def x 99) x)",
            expected=99,
            concept_phrase="the redefined binding",
            question_what="the value of x after redefining it with def from 1 to 99",
            goal_text="bind x to 1, then redefine it as 99 and return it",
            scenario=(
                "The milkmaid had posted x on the market-board with a small "
                "coin-count, but when she returned to the square she pulled down "
                "the old card and nailed a fresh one in its place with a new figure."
            ),
            need=(
                "Buyers who read x after the second nailing had to receive the "
                "latest posted value, not the first — the board must honour the "
                "most recent card."
            ),
            mapping=(
                "`def` overwrites the market-board entry: the first `def` nails "
                "one value, the second `def` replaces it. Looking up x reads the "
                "card that was nailed last."
            ),
            resolution=(
                "The REPL returned the figure from the second card — the board "
                "held the most-recently-nailed name, and the redefinition stood — 99."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_03 = SubjectCurriculum(grade=3, subject_id="G3-03",
    subject_title="let — local binding", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(let [x 3] (+ x 1))",
            expected=4,
            concept_phrase="the local binding and addition",
            question_what="the running total after binding x to 3 and adding 1",
            goal_text="bind a value of 3 to a local name x for one stretch, then return that value plus one",
            scenario=(
                "The milkmaid tucked the number 3 into her apron-pocket at the start "
                "of one stretch of the road — a private count, good only for this "
                "leg of the journey to market."
            ),
            need=(
                "She needed to reach into the pocket at the next step and add 1 to "
                "the count, then let the pocket empty when the form ended."
            ),
            mapping=(
                "`let` is the apron-pocket: it tucks `x = 3` into the pocket for the "
                "duration of the body. `(+ x 1)` draws from the pocket and adds 1. "
                "When the body ends, the pocket is put away and `x` ceases to exist."
            ),
            resolution=(
                "The REPL returned the result — the count from the pocket incremented by one, "
                "the pocket now set aside at the road's end."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(let [n 10] (* n n))",
            expected=100,
            concept_phrase="the local binding and multiplication",
            question_what="multiplying n by itself after binding n locally to 10 via let",
            goal_text="bind n to 10 and compute n squared",
            scenario=(
                "The milkmaid had tucked a pail-count of ten into her apron-pocket "
                "at the start of the morning round — a number she needed to square "
                "before she reached the dairy door."
            ),
            need=(
                "She had to draw n from the pocket and multiply it by itself inside "
                "the body, then let the pocket go empty when the form closed."
            ),
            mapping=(
                "`let` is the apron-pocket: it tucks `n = 10` in for the body's "
                "duration. `(* n n)` draws n twice from the pocket and multiplies. "
                "The pocket empties when the body ends."
            ),
            resolution=(
                "The REPL returned the squared count — the pocket value multiplied "
                "by itself, the pocket set aside at the road's end."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(let [a 5] a)",
            expected=5,
            concept_phrase="the local binding and lookup",
            question_what="the value of a after binding it locally to 5 via let",
            goal_text="bind a to 5 and return it",
            scenario=(
                "The milkmaid had sewn a small count into her apron-pocket for "
                "one stretch of the road — she tucked a into the pocket and needed "
                "only to read it back before the stretch ended."
            ),
            need=(
                "She needed the body of the form to look up a from the pocket and "
                "return it unchanged, then let the pocket empty at the form's end."
            ),
            mapping=(
                "`let` tucks `a = 5` into the apron-pocket; the body simply "
                "names a, drawing the value straight from the pocket. When the "
                "body ends, the pocket is unpicked and a is gone."
            ),
            resolution=(
                "The REPL returned the pocket value unaltered — a came back "
                "exactly as it was tucked in, the pocket now set aside."
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_04 = SubjectCurriculum(grade=3, subject_id="G3-04",
    subject_title="let — multi-binding", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(let [a 1 b 2] (+ a b))",
            expected=3,
            concept_phrase="the multi-binding and addition",
            question_what="adding a and b after binding both via let to 1 and 2",
            goal_text="bind a to 1 and b to 2, then add them",
            scenario=(
                "The milkmaid had two small compartments sewn into her apron-pocket "
                "— one held a tally of morning pails, the other an afternoon tally — "
                "both tucked in at the start of the stretch."
            ),
            need=(
                "She needed to draw both counts from the pocket and add them "
                "together inside the body, then let both compartments empty "
                "when the form ended."
            ),
            mapping=(
                "`let` sews two compartments into the pocket: a holds the first "
                "count, b holds the second. `(+ a b)` draws from both and combines "
                "them. Both bindings vanish when the body ends."
            ),
            resolution=(
                "The REPL returned the combined tally from both pocket compartments "
                "— the two counts summed, the pocket set aside — 2."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(let [x 5 y 3] (- x y))",
            expected=2,
            concept_phrase="the multi-binding and subtraction",
            question_what="subtracting y from x after binding via let to 5 and 3",
            goal_text="bind x to 5 and y to 3, then subtract y from x",
            scenario=(
                "The milkmaid had tucked two coin-counts into separate pockets of "
                "her milking apron — the larger count in one side, the smaller "
                "in the other — before setting off down the road."
            ),
            need=(
                "She needed to draw x and y from the pockets and subtract the "
                "smaller from the larger inside the body, then let both pockets "
                "empty at the stretch's end."
            ),
            mapping=(
                "`let` opens two apron-pockets: x holds the larger coin-count, "
                "y holds the smaller. `(- x y)` draws from both and subtracts. "
                "Both pockets are sewn shut when the body finishes."
            ),
            resolution=(
                "The REPL returned the difference of the two pocket values — "
                "the subtraction completed, both pockets emptied — 3."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(let [a 2 b 3 c 4] (+ a b c))",
            expected=9,
            concept_phrase="the three-binding sum",
            question_what="adding a, b, and c after binding via let to 2, 3, and 4",
            goal_text="bind a to 2, b to 3, c to 4, and add them",
            scenario=(
                "The milkmaid had three separate coin-pouches sewn into her milking "
                "apron — one for each dairy round — each tucked in at the road's "
                "start with its own count for the day."
            ),
            need=(
                'She needed to reach into all three pouches and sum the {drawn.b} counts inside the body, then let every pouch go empty when the form closed.'
            ),
            mapping=(
                "`let` opens three apron-pockets: a, b, and c each hold one "
                "round's count. `(+ a b c)` draws from all three and sums them. "
                "All three pockets are unpicked when the body ends."
            ),
            resolution=(
                "The REPL returned the total of all three pocket values — the — 4 "
                "several counts summed, every pouch emptied at road's end."
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_05 = SubjectCurriculum(grade=3, subject_id="G3-05",
    subject_title="let — shadowing outer def", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(do (def x 10) (let [x 99] x))",
            expected=99,
            concept_phrase="the inner binding shadowing the outer",
            question_what="the value of x inside the let scope where it shadows the def binding",
            goal_text="define x at the top level, then shadow it locally and return the inner value",
            scenario=(
                "The milkmaid posted x on the market-board, then tucked a "
                "fresh x into her apron-pocket for one stretch of road."
            ),
            need=(
                "Inside the pocket's scope, x had to read from the pocket, "
                "not the board."
            ),
            mapping=(
                "`let` shadows x in the apron-pocket for the body's duration. "
                "The pocket wins while it exists."
            ),
            resolution=(
                "The REPL returned the pocket value — the shadowing held — 99."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def x 10) (let [x 99] x) x)",
            expected=10,
            concept_phrase="the outer binding after the let scope",
            question_what="the value of x in the outer scope after the let scope ends",
            goal_text="define x, shadow it in a let, then look up x again in the outer scope",
            scenario=(
                "The milkmaid had posted x on the market-board, then sewn a "
                "fresh pocket value for x into her apron for one stretch of "
                "road. Once the stretch ended and the pocket emptied, she "
                "walked back to the square and looked up x again."
            ),
            need=(
                "After the pocket was unpicked, the market-board had to hold "
                "the original entry — the board must be unchanged by what "
                "happened inside the pocket."
            ),
            mapping=(
                "`let` shadows x only for its body; when the body ends the "
                "pocket empties and x resolves from the market-board again. "
                "The board was never altered by the pocket."
            ),
            resolution=(
                "The REPL returned the board's original posting — the pocket "
                "had emptied, and the market-board reclaimed x unchanged — 99."
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_06 = SubjectCurriculum(grade=3, subject_id="G3-06",
    subject_title="let — binding can reference prior", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(let [a 5 b (* a 2)] b)",
            expected=10,
            concept_phrase="the sequential binding where later refers to earlier",
            question_what="the value of b, bound to twice a via let, after a is bound to 5",
            goal_text="bind a to 5, then bind b to twice a, and return b",
            scenario=(
                "The milkmaid had sewn two compartments into her apron-pocket "
                "at the start of the morning round: she tucked a count into "
                "the first compartment, then reached in to read it while "
                "sewing the second compartment with twice that amount."
            ),
            need=(
                "The second pocket slot had to be filled by reading the first "
                "— b needed the value already in a before the body could "
                "draw on b and return it."
            ),
            mapping=(
                "`let` sews the pocket slots in order: a is tucked first, "
                "then b is computed using a already in the pocket. The body "
                "draws b from the second slot. Both slots empty when the "
                "body ends."
            ),
            resolution=(
                "The REPL returned the second pocket value — b had been "
                "filled from a, and the chain of slots delivered the 2 — 5."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(let [a 3 b (+ a 1) c (* b 2)] c)",
            expected=8,
            concept_phrase="the chained bindings with sequential references",
            question_what="the value of c, bound via let to twice b, after a is 3 and b is a+1",
            goal_text="bind a to 3, b to a+1, c to 2*b, and return c",
            scenario=(
                "The milkmaid had three apron-pocket slots sewn in order; "
                "she tucked a count into the first, then filled each next "
                "slot from the previous one."
            ),
            need=(
                "Each slot had to draw from the one before — c needed b, "
                "b needed a."
            ),
            mapping=(
                "`let` fills slots left to right: a first, then b from a, "
                "then c from b. Each slot reads the ones already filled."
            ),
            resolution=(
                "The REPL returned the final value — the chain of three "
                "slots had each drawn from the last — 2 — 3."
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_07 = SubjectCurriculum(grade=3, subject_id="G3-07",
    subject_title="fn — anonymous function", fable="milkmaid",
    examples=[
        SubjectExample(
            form="((fn [x] (+ x 1)) 4)",
            expected=5,
            concept_phrase="the anonymous function call",
            question_what="the result of applying an anonymous fn that adds 1 to its argument to the value 4",
            goal_text="create an anonymous function that adds 1 to its argument and apply it to 4",
            scenario=(
                "The milkmaid wrote a nameless card with one step: take the "
                "count and add one."
            ),
            need=(
                "The buyer passed a count in and needed the result back."
            ),
            mapping=(
                "`fn` is the nameless card: `[x]` is the input slot, "
                "`(+ x 1)` is the step. Passing a count runs it."
            ),
            resolution=(
                "The REPL returned the incremented count — 4."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="((fn [a b] (* a b)) 3 4)",
            expected=12,
            concept_phrase="the two-argument anonymous function call",
            question_what="the result of applying an anonymous fn with two parameters that multiplies them to 3 and 4",
            goal_text="create an anonymous function that multiplies its two arguments and apply it to 3 and 4",
            scenario=(
                "The milkmaid wrote a nameless card with two slots and a "
                "step that multiplied them together."
            ),
            need=(
                "The buyer passed two counts in and needed the product back."
            ),
            mapping=(
                "`fn` is the card: `[a b]` are the input slots, `(* a b)` is "
                "the step. Passing two counts runs it."
            ),
            resolution=(
                "The REPL returned the product — 4."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_08 = SubjectCurriculum(grade=3, subject_id="G3-08",
    subject_title="fn — multi-arg", fable="milkmaid",
    examples=[
        SubjectExample(
            form="((fn [a b c] (+ a b c)) 1 2 3)",
            expected=6,
            concept_phrase="the three-argument anonymous function call",
            question_what="the result of applying an anonymous fn with three parameters that adds them to 1, 2, and 3",
            goal_text="create an anonymous function with three parameters that adds them and apply it to 1, 2, and 3",
            scenario=(
                "The milkmaid wrote a nameless card with three input slots "
                "and a step that summed all three."
            ),
            need=(
                "The buyer passeseveral countsts in and needed the total back."
            ),
            mapping=(
                "`fn` is the card: `[a b c]` are the slots, `(+ a b c)` is "
                "the summing step. Passseveral countsunts runs it."
            ),
            resolution=(
                "The REPL returned the combined total — 3."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_09 = SubjectCurriculum(grade=3, subject_id="G3-09",
    subject_title="defn — shorthand", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(do (defn dbl [x] (* x 2)) (dbl 5))",
            expected=10,
            concept_phrase="the named recipe-card and its first call",
            question_what="the doubled count after defining a recipe named dbl and calling it on 5",
            goal_text="define a recipe named dbl that takes a quantity and serves twice that, then call dbl on 5 pinches",
            scenario=(
                "The milkmaid had written a pail-steps card labelled dbl "
                "and nailed it to the market-board at the village square: "
                "one input slot for a count, one step that doubled it. Any "
                "buyer could now call dbl by name from the board."
            ),
            need=(
                "A buyer had a single count and needed it doubled; rather "
                "than working it out in the open, she walked to the board, "
                "called dbl, and passed the count in."
            ),
            mapping=(
                "`defn` nails the pail-steps card to the market-board under "
                "the name dbl: `[x]` is the input slot, `(* x 2)` is the "
                "doubling step. Calling dbl from the board runs the card."
            ),
            resolution=(
                "The REPL returned the doubled count — the named card on the "
                "board had run its step and sent the result back to the buyer — 5."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))",
            expected=6,
            concept_phrase="the multi-argument function definition and call",
            question_what="the result of calling the function add3, defined via defn to add three arguments, with 1, 2, and 3",
            goal_text="define a function add3 that adds three arguments, then call it with 1, 2, and 3",
            scenario=(
                "The milkmaid had nailed a three-slot pail-steps card to the "
                "market-board under the name add3: three input slots for the "
                "morning, midday, and afternoon counts, and a step that summed "
                "all three. Buyers at the square could now call it by name."
            ),
            need=(
                "A buyer arrived with three separate counts and needed their "
                "sum; she walked to the board, called add3, and handed the "
                "counts in one after another."
            ),
            mapping=(
                "`defn` nails the named card to the board: `[a b c]` are the "
                "three slots, `(+ a b c)` is the summing step. The board "
                "holds the name so any caller can reach it by calling add3."
            ),
            resolution=(
                "The REPL returned the combined total — add3 had run its "
                "summing step from the board and the result came back."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_10 = SubjectCurriculum(grade=3, subject_id="G3-10",
    subject_title="anonymous shorthand #()", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(#(+ % 1) 5)",
            expected=6,
            concept_phrase="the shorthand function syntax",
            question_what="the result of using the #() shorthand to create a function that adds 1 to its argument and applying it to 5",
            goal_text="use the shorthand syntax to create a function that adds 1 to its argument and apply it to 5",
            scenario=(
                "The milkmaid needed a nameless pail-steps card in a hurry "
                "and scrawled it in shorthand on a scrap of cheesecloth: "
                "a percent mark for whatever count came in, plus one. She "
                "passed the scrap directly to the caller without any name."
            ),
            need=(
                "The caller had a count to hand over and needed the "
                "incremented result back at once — the shorthand scrap had "
                "to accept one input and add one to it."
            ),
            mapping=(
                "The `#()` shorthand is the scrawled scrap: `%` stands for "
                "the single count the caller passes in, and `(+ % 1)` is "
                "the step written in shorthand. Handing it a count runs the step."
            ),
            resolution=(
                "The REPL returned the incremented count — the shorthand "
                "scrap had run its step just as a full card would have — 5."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(#(* %1 %2) 3 4)",
            expected=12,
            concept_phrase="the multi-argument shorthand syntax",
            question_what="the result of using the #() shorthand to create a function that multiplies two arguments and applying it to 3 and 4",
            goal_text="use the shorthand syntax to create a function that multiplies two arguments and apply it to 3 and 4",
            scenario=(
                "The milkmaid had scrawled a two-slot nameless card in "
                "shorthand on a scrap of cheesecloth: first-count mark, "
                "second-count mark, and a step that multiplied them. She "
                "passed the scrap to the buyer at the dairy door."
            ),
            need=(
                "The buyer had two counts and needed their product at once; "
                "the shorthand scrap had to accept both inputs and run its "
                "multiplication step without delay."
            ),
            mapping=(
                "The `#()` shorthand is the scrawled scrap: `%1` and `%2` "
                "are the two input marks, and `(* %1 %2)` is the step. "
                "Passing two counts in runs the multiplication immediately."
            ),
            resolution=(
                "The REPL returned the product of the two counts — the "
                "shorthand scrap had multiplied them and sent the result back — 4."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_11 = SubjectCurriculum(grade=3, subject_id="G3-11",
    subject_title="Substitution rule", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(let [a 7] (+ a a))",
            expected=14,
            concept_phrase="the binding referenced multiple times",
            question_what="the result of adding a to itself after binding a locally to 7 via let",
            goal_text="bind a to 7 and add a to itself",
            scenario=(
                "The milkmaid tucked a count into her apron-pocket and "
                "reached in twice to draw from it."
            ),
            need=(
                "Both draws had to yield the same value so the sum would be "
                "consistent."
            ),
            mapping=(
                "`let` tucks `a` once; the body reaches in twice with `(+ a "
                "a)`. Every mention of a yields the same count."
            ),
            resolution=(
                "The REPL returned the pocket value added to itself — 7."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="((fn [x] (* x x)) 6)",
            expected=36,
            concept_phrase="the function call with self-multiplication",
            question_what="the result of applying an anonymous fn that multiplies its argument by itself to 6",
            goal_text="apply a function that squares its argument to 6",
            scenario=(
                "The milkmaid had written a nameless pail-steps card with "
                "one slot and a step that drew from the slot twice, "
                "multiplying the same count by itself. She passed a count "
                "in and waited at the dairy door."
            ),
            need=(
                "The card had to draw from the single input slot twice and "
                "multiply the count by itself — both reads had to yield the "
                "same value for the squaring to work."
            ),
            mapping=(
                "`fn` is the nameless card: `[x]` is the slot, and `(* x x)` "
                "draws from it twice. Substitution means both references to x "
                "resolve to the same passed-in count."
            ),
            resolution=(
                "The REPL returned the count multiplied by itself — the — 6 "
                "nameless card's double-draw had squared the input correctly."
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_12 = SubjectCurriculum(grade=3, subject_id="G3-12",
    subject_title="Scope vs namespace", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(do (def g 5) (let [g 99] (+ g 1)))",
            expected=100,
            concept_phrase="the scope shadowing and computation",
            question_what="the result of adding 1 to g, computed inside a let where g is locally bound to 99, shadowing the top-level def",
            goal_text="define g at the top level, shadow it in a let with a different value, and compute g+1 inside the let",
            scenario=(
                "The milkmaid had posted g on the market-board at the village "
                "square with a small posting. Later, on a new stretch of road, "
                "she tucked a much larger value for g into her apron-pocket "
                "and computed g plus one from the pocket, not the board."
            ),
            need=(
                "Inside the pocket's scope, g had to come from the pocket so "
                "that the addition used the local value — the board's older "
                "posting must stay hidden while the pocket is sewn shut."
            ),
            mapping=(
                "`def` posts g on the market-board; `let` then tucks a new g "
                "into the apron-pocket for the body. Inside the body, g reads "
                "from the pocket, which shadows the board."
            ),
            resolution=(
                "The REPL returned the pocket value incremented by one — the "
                "apron-pocket had won over the market-board inside the body — 1 — 99."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_13 = SubjectCurriculum(grade=3, subject_id="G3-13",
    subject_title="fn body returns last form", fable="milkmaid",
    examples=[
        SubjectExample(
            form="((fn [x] x x x 99) 1)",
            expected=99,
            concept_phrase="the function body with multiple expressions",
            question_what="the result of applying an anonymous fn where the body contains multiple expressions but only the last one is returned, applied to 1",
            goal_text="create an anonymous function with multiple forms in its body but return only the last one",
            scenario=(
                "The milkmaid wrote a card with several steps: three that "
                "checked the input, then a final step with a fixed tally."
            ),
            need=(
                "Only the final step's result left the card; the earlier "
                "steps ran but were discarded."
            ),
            mapping=(
                "`fn` runs every step but returns only the last. Earlier "
                "mentions run and are discarded; only the final result goes "
                "to the caller."
            ),
            resolution=(
                "The REPL returned the final value — 1 — 99."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_14 = SubjectCurriculum(grade=3, subject_id="G3-14",
    subject_title="do form", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(do 1 2 3)",
            expected=3,
            concept_phrase="the do form with multiple values",
            question_what="the final value evaluated by do from the sequence",
            goal_text="evaluate a sequence of values and return the last one",
            scenario=(
                "The milkmaid had chalked three marks on the dairy wall in "
                "order — the first for the morning round, the second for "
                "midday, the third for the afternoon — and the runtime read "
                "each mark in turn from left to right."
            ),
            need=(
                "Only the final chalk mark mattered to the buyer at the end "
                "of the day — the earlier marks had been read and set aside, "
                "and only the last one came back from the wall."
            ),
            mapping=(
                "`do` is the sequence of chalk marks read in order: each "
                "mark is evaluated in turn and its result discarded except "
                "for the last. The final mark on the wall is what the "
                "runtime carries to the caller."
            ),
            resolution=(
                "The REPL returned the last mark's value — the earlier marks "
                "had been read and set aside, and only the final one came back — 3."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (+ 1 1) (+ 2 2) (+ 3 3))",
            expected=6,
            concept_phrase="the do form with multiple expressions",
            question_what="the final result evaluated by do from the sequence of expressions",
            goal_text="evaluate three arithmetic expressions in sequence and return the result of the last one",
            scenario=(
                "The milkmaid had chalked three arithmetic marks on the "
                "dairy wall in order — each summing a different pair of "
                "counts from the morning, midday, and afternoon rounds — "
                "and the runtime worked through them one after another."
            ),
            need=(
                "Each mark had to be computed in turn, but only the final "
                "sum was sent to market — the earlier sums ran and were "
                "set aside before the last one arrived."
            ),
            mapping=(
                "`do` reads each chalk mark in order and evaluates it; only "
                "the last mark's result is returned. The earlier arithmetic "
                "runs but is discarded, just as intermediate chalk marks are "
                "read and then wiped."
            ),
            resolution=(
                "The REPL returned the final sum — the two earlier additions "
                "had run and been set aside, and only the last result came back — 3."
            ),
            tags=("story",),
        ),
    ], subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_15 = SubjectCurriculum(grade=3, subject_id="G3-15",
    subject_title="Side-effects in body", fable="milkmaid",
    examples=[
        SubjectExample(
            form='(do (println "hi") 42)',
            expected=42,
            concept_phrase="the do form with side-effects and final return",
            question_what="the final value evaluated by do, ignoring the intermediate println side-effect",
            goal_text="execute a print statement for side-effects, then return a different value",
            scenario=(
                "The milkmaid rang a handbell at the dairy door to announce "
                "her arrival — a side-action that made noise but produced no "
                "count — and then presented the buyer with a coin-tally she "
                "had been carrying all along."
            ),
            need=(
                "The ringing of the bell was meant to be heard, not returned; "
                "only the coin-tally at the end of the sequence was the hi "
                "the buyer needed to take away."
            ),
            mapping=(
                "`do` runs the print step first as a side-effect — the bell "
                "rings — then evaluates the final form and returns its value. "
                "The side-effect runs but does not become the return value."
            ),
            resolution=(
                "The REPL returned the coin-tally — the bell had rung and "
                "been heard, but only the final form's value came back to "
                "the caller."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_16 = SubjectCurriculum(grade=3, subject_id="G3-16",
    subject_title="Name collision: namespace vs let", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(let [+ 99] +)",
            expected=99,
            concept_phrase="the shadowed operator binding",
            question_what="the value locally bound to the + operator via let",
            goal_text="shadow the plus operator with a local binding and return the bound value",
            scenario=(
                "The milkmaid had tucked a coin-count into her apron-pocket "
                "under the label used by the market-board for the addition "
                "sign — hiding the board's well-known entry behind a local "
                "pocket value for the length of the body."
            ),
            need=(
                "Inside the pocket's scope, that label had to resolve to the "
                "pocket value, not the board's operator — any lookup of the "
                "name inside the body must draw from the pocket."
            ),
            mapping=(
                "`let` tucks a value into the pocket under the name `+`, "
                "shadowing the market-board's operator for the body's "
                "duration. The body reads `+` and draws the pocket value, "
                "not the built-in."
            ),
            resolution=(
                "The REPL returned the pocket value — the operator name had "
                "been shadowed by the pocket, and the local binding came back — 99."
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_17 = SubjectCurriculum(grade=3, subject_id="G3-17",
    subject_title="Naming conventions (kebab-case)", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(let [hare-speed 4 tortoise-speed 1] (- hare-speed tortoise-speed))",
            expected=3,
            concept_phrase="the kebab-case naming and subtraction",
            question_what="the result of subtracting tortoise-speed from hare-speed after binding both via let",
            goal_text="bind hare-speed to 4 and tortoise-speed to 1, then compute their difference",
            scenario=(
                "The milkmaid had two hyphenated names chalked on her tally-slate "
                "beside the dairy door — the first a road-speed measure, the second "
                "a slower one — each neatly written with a dash between the words "
                "in the market's naming style."
            ),
            need=(
                "She needed to post both hyphenated names on the market-board "
                "as pocket bindings and subtract the smaller from the larger "
                "inside the body, using the full hyphenated names as written."
            ),
            mapping=(
                "`let` tucks each hyphenated name into the apron-pocket in "
                "turn; the body draws both and subtracts. Kebab-case names "
                "are Clojure's convention for multi-word bindings on the board."
            ),
            resolution=(
                "The REPL returned the difference of the two pocket values — "
                "the hyphenated names had resolved correctly and the subtraction "
                "came back — 1 — 4."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_18 = SubjectCurriculum(grade=3, subject_id="G3-18",
    subject_title="When to name vs inline", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(let [n 5] (* n n n))",
            expected=125,
            concept_phrase="the named binding used multiple times",
            question_what="the result of multiplying n by itself three times after binding n locally to 5 via let",
            goal_text="bind n to 5 and compute n cubed",
            scenario=(
                "The milkmaid had tucked a single count into her apron-pocket "
                "at the start of the stretch and then reached into the same "
                "pocket three times during the body — multiplying the count "
                "by itself twice over."
            ),
            need=(
                "Rather than write the same figure three times on her card, "
                "she named it once in the pocket and drew on the pocket each "
                "time, keeping the body short and the count consistent."
            ),
            mapping=(
                "`let` tucks n into the apron-pocket once; `(* n n n)` draws "
                "from the pocket three times. Naming a value that appears "
                "repeatedly saves writing and ensures every draw uses the same "
                "tucked count."
            ),
            resolution=(
                "The REPL returned the count multiplied by itself twice — "
                "the pocket had been drawn on three times and the cube came back — 5."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 5 5 5)",
            expected=125,
            concept_phrase="the inline multiplication without binding",
            question_what="the result of multiplying 5 by itself three times without any binding",
            goal_text="compute 5 cubed using direct values",
            scenario=(
                "The milkmaid had no pocket to tuck anything into — the "
                "figure was simple and used only once, so she wrote it "
                "directly three times on the card and handed it straight "
                "to the buyer without any naming ceremony."
            ),
            need=(
                "When a value is used in only one small place and will not "
                "be re-read, there is no need to sew a pocket — the count "
                "can be written directly on the card and the pail-steps run."
            ),
            mapping=(
                "No `let` pocket is needed here: the figure appears inline "
                "in each of the three multiplication slots. The form runs "
                "the step directly without any apron-pocket overhead."
            ),
            resolution=(
                "The REPL returned the same cube as the pocket version — "
                "inline values worked just as well when the figure was only "
                "written out directly — 5."
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


SUBJECTS: dict[str, SubjectCurriculum] = {
    s.subject_id: s for s in (
        G3_01, G3_02, G3_03, G3_04, G3_05, G3_06, G3_07, G3_08, G3_09,
        G3_10, G3_11, G3_12, G3_13, G3_14, G3_15, G3_16, G3_17, G3_18,
    )
}


def smoke_test() -> None:
    from mmllm.aesop.curriculum.generator import generate_subject
    for sid, sub in SUBJECTS.items():
        recs = generate_subject(sub, n_per_example=1, seed=0)
        for r in recs: assert r.tool_calls[0]["name"] == "eval"
    print(f"grade-3 tortoise-hare smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
