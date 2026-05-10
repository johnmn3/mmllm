"""Grade 3 — naming, scope, substitution. Through tortoise-hare.

The fable lens: the Tortoise's careful approach is exactly the
substitution-rule discipline. The Hare's "I just know the answer"
is what binding-by-name corrects.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.tortoise_hare.grade_1 import (
    _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.tortoise_hare._metaphor_pools import (
    _POUCH_SUBPLOTS, _RECIPE_SUBPLOTS, _ROADSIGN_SUBPLOTS, _SCRIBE_SUBPLOTS,
)

# Add naming-themed subplots: a character names a value, then references it.
# Based on _GOAL_SUBPLOTS to ensure goal-driven design.
_NAMING_SUBPLOTS: list[SubplotTemplate] = list(_GOAL_SUBPLOTS) + [
    SubplotTemplate("""\
{tortoise_phrase} kept a small ledger {place} where every meaningful
quantity got its own name. {tortoise_he_she_cap} pointed to today's
entry, which required {goal_text}. {tortoise_he_she_cap} would write
{concept_phrase} and let the REPL confirm."""),

    SubplotTemplate("""\
"The key is to name your values carefully," {tortoise} said {place}.
"To {goal_text}, you write {concept_phrase} and submit it to the REPL.
That is the discipline." {hare_phrase} nodded, {emo_tired}."""),
]


def _ex(form, expected, concept, what, goal="", tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal, tags=tags)


_PLAN_POOL_G3 = _PLAN_POOL + (
    "I bind the inputs in a let, then compute.",
    "I name the values first and then combine them.",
    "I write the let-form so the REPL can substitute.",
)


G3_01 = SubjectCurriculum(grade=3, subject_id="G3-01",
    subject_title="def — top-level binding", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(do (def x 42) x)",
            expected=42,
            concept_phrase="the top-level binding and lookup",
            question_what="the value of x after using def to bind x to 42",
            goal_text="bind x to 42 and return it",
            scenario=(
                "A wooden sign had been posted at the road's edge near Mossback's morning route. She took her chisel and carved the name x into the sign, pressing {drawn.a} acorns' worth of value beneath it."
            ),
            need=(
                "Mossback needed every traveller on the road to know "
                "that name and its value for the whole journey. "
                "Without the posted sign, x would mean nothing when "
                "she looked it up a step later."
            ),
            mapping=(
                "`def` posts the name x onto the top-level sign "
                "alongside its bound value. The second expression "
                "looks up that sign and reads back whatever was "
                "posted — here, 42."
            ),
            resolution=(
                "the sign held its name on the long road; the runtime, "
                "minding each step, returned exactly what the chisel had "
                "carved beneath the name."
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
                'Mossback paused at the library of scrolls she kept beside the road. She unrolled a fresh scroll and inscribed the name y at the top, noting its value as {drawn.a} beside it.'
            ),
            need=(
                "She would consult that scroll further along and "
                "need y to resolve immediately. A name with no "
                "scroll behind it would leave the lookup blank."
            ),
            mapping=(
                "`def` writes the name y and its value onto a "
                "top-level scroll. Evaluating y afterwards reads "
                "that same scroll and returns the recorded value."
            ),
            resolution=(
                'the scroll answered with {drawn.a} — the value Mossback had inscribed at the start of the stretch.'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_02 = SubjectCurriculum(grade=3, subject_id="G3-02",
    subject_title="def — redefinition", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(do (def x 1) (def x 99) x)",
            expected=99,
            concept_phrase="the redefined binding",
            question_what="the value of x after redefining it with def from 1 to 99",
            goal_text="bind x to 1, then redefine it as 99 and return it",
            scenario=(
                "Mossback had posted x on the road's sign with a count of {drawn.a} acorn, but a messenger arrived mid-route with a correction: the count was really 99. She took her chisel and carved the new value over the old."
            ),
            need=(
                "The old count had to be replaced entirely; a stale "
                "sign would send every traveller away with the wrong "
                "tally. Only the most recently posted value matters."
            ),
            mapping=(
                "Each `def` re-posts the name x on the same sign, "
                "overwriting what was there before. The final lookup "
                "reads the sign as it stands after the last posting."
            ),
            resolution=(
                "the sign showed the corrected count — the one "
                "carved in last, displacing the earlier inscription."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_03 = SubjectCurriculum(grade=3, subject_id="G3-03",
    subject_title="let — local binding", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(let [x 3] (+ x 1))",
            expected=4,
            concept_phrase="the local binding and addition",
            question_what="the running total after binding x to 3 and adding 1",
            goal_text="bind a value of 3 to a local name x for one stretch, then return that value plus one",
            scenario=(
                "Mossback the tortoise had been counting along a stretch of road. She set a single pebble — worth {drawn.a} acorns — into the small leather pouch tied at her hip and gave the pouch's contents the local name x."
            ),
            need=(
                "Just past the next milestone she'd want the running "
                "total — what x plus one more acorn would come to. After "
                "the milestone, the pouch would empty and x would mean "
                "nothing again."
            ),
            mapping=(
                "`let` binds a value into a pouch named locally for the stretch of one form. Inside `(+ x {drawn.b})`, x means {drawn.a}; outside the form, x is empty and unknown again. The binding is in force only for the form's stretch."
            ),
            resolution=(
                'the pouch yielded its tucked count, the +{drawn.b} added one more acorn, and the running total — pouch already empty again — was exactly what the next milestone needed.'           ),
            tags=("story",),
        ),
        SubjectExample(
            form="(let [n 10] (* n n))",
            expected=100,
            concept_phrase="the local binding and multiplication",
            question_what="multiplying n by itself after binding n locally to 10 via let",
            goal_text="bind n to 10 and compute n squared",
            scenario=(
                'Mossback counted out {drawn.a} acorns and tucked them into the leather pouch at her hip, naming that count n. She needed to know what n rows of n acorns each would amount to before she reached the oak grove.'
            ),
            need=(
                "The grove keeper expected a square tally. Without "
                "naming the row-count first, Mossback would have to "
                "recount the same number twice without any anchor."
            ),
            mapping=(
                '`let` locks n into the pouch as {drawn.a} for the span of the body. Inside `(* n n)`, both occurrences of n draw from the same pouch — the same 10.'           ),
            resolution=(
                'the pouch supplied {drawn.a} twice over, the multiplication settled at the square of the bound count, and the grove keeper accepted the tally.'
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
                'Mossback slipped {drawn.a} acorns into her pouch and named that store a, intending to report the count at the checkpoint just ahead without any further arithmetic.'
            ),
            need=(
                "The checkpoint needed the raw count as stored — no "
                "adjustment, just confirmation that the pouch held "
                "what Mossback said it did."
            ),
            mapping=(
                "`let` binds {drawn.a} to the name a for the body's stretch. The body is simply a, so the REPL opens the pouch and returns whatever it finds inside."
            ),
            resolution=(
                "the pouch opened and delivered the exact count "
                "placed there at the start of the stretch."
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_04 = SubjectCurriculum(grade=3, subject_id="G3-04",
    subject_title="let — multi-binding", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(let [a 1 b 2] (+ a b))",
            expected=3,
            concept_phrase="the multi-binding and addition",
            question_what="adding a and b after binding both via let to 1 and 2",
            goal_text="bind a to 1 and b to 2, then add them",
            scenario=(
                'Mossback was at a flat stone on her morning round. She tied two pebbles into the pouches on her hip — one worth a count of {drawn.a} acorn, named a, and the other worth {drawn.b} acorns, named b.'
            ),
            need=(
                "She needed both counts in hand at the same moment "
                "to tally them together. Losing either name before "
                "the addition would break the sum."
            ),
            mapping=(
                "`let` with two bindings ties both values into named "
                "pouches, keeping them in force together inside the "
                "body. `(+ a b)` draws from both pouches at once."
            ),
            resolution=(
                "the two pouches opened together and the running "
                "total settled at the sum they jointly held."
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
                'Mossback loaded two pouches: x with {drawn.a} acorns, y with 3. She needed the gap between the two counts.'
            ),
            need=(
                "Both names had to be live at once for the "
                "subtraction. A missing pouch would leave the "
                "computation without a reference count."
            ),
            mapping=(
                '`let` binds x to {drawn.a} and y to {drawn.b} simultaneously. Inside `(- x y)`, each name draws from its own pouch and the subtraction returns their difference.'
            ),
            resolution=(
                "the two pouches discharged and the gap settled "
                "at the difference between their counts."
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
                'Mossback prepared three pouches before setting out: a with {drawn.a} acorns, b with {drawn.b}, and c with 4. She needed the full combined count for the provisioner waiting at the far end of the stretch.'
            ),
            need=(
                "The provisioner required all three sub-tallies added "
                "into one figure. Without naming each store, she "
                "risked confusing one pile with another mid-count."
            ),
            mapping=(
                "`let` loads all three names at once, each pointing "
                "to its own count. The body `(+ a b c)` draws from "
                "all three pouches and combines them."
            ),
            resolution=(
                "the three pouches emptied into one tally, and the "
                "provisioner received the combined count they held."
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_05 = SubjectCurriculum(grade=3, subject_id="G3-05",
    subject_title="let — shadowing outer def", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(do (def x 10) (let [x 99] x))",
            expected=99,
            concept_phrase="the inner binding shadowing the outer",
            question_what="the value of x inside the let scope where it shadows the def binding",
            goal_text="define x at the top level, then shadow it locally and return the inner value",
            scenario=(
                "Mossback had already posted x on the road's sign with a count of 10. For a short detour she tied a fresh pouch at her hip labeled x, stuffed with {drawn.b} acorns — a higher count for just this side-path."           ),
            need=(
                "On the detour, she needed the local count, not the "
                "posted one. The road's sign was still there, but "
                "the pouch on her hip took precedence while she "
                "walked the side-path."
            ),
            mapping=(
                "The `let` binding shadows the top-level `def` "
                "inside its form. When the body evaluates x, it "
                "reads from the nearer pouch — the local one — "
                "ignoring the distant road sign."
            ),
            resolution=(
                "the pouch on the detour delivered the local count, "
                "not the count posted on the distant sign."
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
                'Mossback posted x at {drawn.a} on the road sign, then walked a detour where her hip-pouch shadowed x with 99. When she returned to the main road, the pouch was empty; only the road sign stood.'
            ),
            need=(
                "Back on the main road, she needed the original "
                "posted count again. The detour's pouch had been "
                "untied on return, so x had to come from the sign "
                "or from nothing."
            ),
            mapping=(
                "After the `let` body ends, the local binding "
                "dissolves. The final x is evaluated in the outer "
                "scope, where only the `def` sign remains — "
                "the pouch is long gone."
            ),
            resolution=(
                "the road sign answered with its original posting, "
                "the detour's local count having vanished the "
                "moment the side-path ended."
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_06 = SubjectCurriculum(grade=3, subject_id="G3-06",
    subject_title="let — binding can reference prior", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(let [a 5 b (* a 2)] b)",
            expected=10,
            concept_phrase="the sequential binding where later refers to earlier",
            question_what="the value of b, bound to twice a via let, after a is bound to 5",
            goal_text="bind a to 5, then bind b to twice a, and return b",
            scenario=(
                "Mossback loaded her first pouch, a, with {drawn.a} acorns. She then fastened a second pouch, b, and filled it by doubling whatever a held — reading a's count before sealing b shut."
            ),
            need=(
                "The second pouch's size depended on the first. "
                "She could not fill b without already knowing a, "
                "so the order of loading mattered entirely."
            ),
            mapping=(
                'In a `let`, bindings are processed left to right: a is set to {drawn.a} first; b is then computed as twice a, using the a already in the pouch. The body returns b.'
            ),
            resolution=(
                "the second pouch held the doubled count — the "
                "amount the body found when it opened b at the end."
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
                'Mossback prepared three pouches in order: a held {drawn.a} acorns, then b was filled with one more than a, and finally c was loaded with twice whatever b held. Each pouch drew from the one before it.'
            ),
            need=(
                "The final count in c was what the ledger required, "
                "but it could only be computed after the earlier two "
                "pouches were filled in sequence. Skipping any step "
                "would leave the chain broken."
            ),
            mapping=(
                "`let` processes the three bindings in order: a "
                "first, then b using a, then c using b. The body "
                "returns c — the last pouch in the chain, which "
                "carries the fully computed count."
            ),
            resolution=(
                "the third pouch opened at the end of the stretch "
                "and delivered the count built up through the "
                "whole chain of prior pouches."
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_07 = SubjectCurriculum(grade=3, subject_id="G3-07",
    subject_title="fn — anonymous function", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="((fn [x] (+ x 1)) 4)",
            expected=5,
            concept_phrase="the anonymous function call",
            question_what="the result of applying an anonymous fn that adds 1 to its argument to the value 4",
            goal_text="create an anonymous function that adds 1 to its argument and apply it to 4",
            scenario=(
                "Mossback scratched a one-step recipe on a loose "
                "card: take a count, add one acorn, return the "
                "result. She posted no name — it was a one-off."
            ),
            need=(
                "She needed that routine run on 4 acorns right "
                "then. Naming it would waste time on a task "
                "needed only once."
            ),
            mapping=(
                "`fn` writes an unnamed card with parameter x. "
                "Placing it at the head of the call and passing "
                "4 invokes it, substituting 4 for x in the body."
            ),
            resolution=(
                "the unnamed card ran on 4 and returned one "
                "acorn more — the anonymous routine's result."
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
                "Mossback scratched out a quick recipe for "
                "multiplying two quantities together — two slots "
                "labeled a and b — and handed it straight to the "
                "REPL without pinning a name above the card."
            ),
            need=(
                "She needed the product of 3 and 4 computed through "
                "a reusable two-slot form, but only for this one "
                "moment. A nameless card was exactly enough."
            ),
            mapping=(
                "`fn` with two parameters a and b is the unnamed "
                "card. Calling it with 3 and 4 slots those values "
                "into a and b; the body `(* a b)` multiplies them."
            ),
            resolution=(
                "the two-slot card ran on the pair and returned "
                "their product — the number the anonymous recipe "
                "delivered in a single pass."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_08 = SubjectCurriculum(grade=3, subject_id="G3-08",
    subject_title="fn — multi-arg", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="((fn [a b c] (+ a b c)) 1 2 3)",
            expected=6,
            concept_phrase="the three-argument anonymous function call",
            question_what="the result of applying an anonymous fn with three parameters that adds them to 1, 2, and 3",
            goal_text="create an anonymous function with three parameters that adds them and apply it to 1, 2, and 3",
            scenario=(
                "Three couriers had each arrived carrying a small "
                "sack — one with 1 acorn, one with 2, one with 3. "
                "Mossback scratched a three-slot recipe card on the "
                "spot: take a, b, and c and sum them together."
            ),
            need=(
                "She needed all three sacks pooled into one tally "
                "without writing a named function for a task she'd "
                "never repeat. The unnamed three-slot card was enough."
            ),
            mapping=(
                "`fn` with parameters a, b, and c is the three-slot "
                "unnamed card. Passing 1, 2, 3 fills each slot in "
                "order; the body `(+ a b c)` adds the three fills."
            ),
            resolution=(
                "the three-slot card ran and returned the combined "
                "count — all three sacks pooled into one number."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_09 = SubjectCurriculum(grade=3, subject_id="G3-09",
    subject_title="defn — shorthand", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(do (defn dbl [x] (* x 2)) (dbl 5))",
            expected=10,
            concept_phrase="the named recipe-card and its first call",
            question_what="the doubled count after defining a recipe named dbl and calling it on 5",
            goal_text="define a recipe named dbl that takes a quantity and serves twice that, then call dbl on 5 pinches",
            scenario=(
                "Twice as many animals had arrived for dinner as "
                "Mossback the tortoise had planned for, and every "
                "recipe now needed twice its salt."
            ),
            need=(
                "Mossback wanted a doubling routine written once and posted under a name any cook could shout — tonight's first reach being {drawn.b} pinches of salt."
            ),
            mapping=(
                "`defn` writes the routine on a recipe-card and posts "
                "the card under a name. The name (here `dbl`) is what "
                "the kitchen shouts to invoke the doubling; the "
                "parameter `x` is the quantity the cook brings."
            ),
            resolution=(
                'the named recipe ran on {drawn.b} and handed back twice that — exactly what the doubled crowd would need.'           ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))",
            expected=6,
            concept_phrase="the multi-argument function definition and call",
            question_what="the result of calling the function add3, defined via defn to add three arguments, with 1, 2, and 3",
            goal_text="define a function add3 that adds three arguments, then call it with 1, 2, and 3",
            scenario=(
                "Three ingredient buckets arrived at Mossback's kitchen — each with a different portion. She wrote a three-slot pooling routine on a card and posted it on the wall under the name add{drawn.c} for any cook to use."
            ),
            need=(
                "The kitchen would receive deliveries of three "
                "portions often, and the cook needed a named step "
                "to pool them rather than tallying freehand each time."
            ),
            mapping=(
                '`defn` posts the three-slot card under the name add3. Calling `(add{drawn.c} {drawn.a} {drawn.b} {drawn.c})` slots the three deliveries into a, b, and c and sums them per the posted recipe.'
            ),
            resolution=(
                "the named recipe accepted the three portions and "
                "returned the combined total the kitchen required."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_10 = SubjectCurriculum(grade=3, subject_id="G3-10",
    subject_title="anonymous shorthand #()", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(#(+ % 1) 5)",
            expected=6,
            concept_phrase="the shorthand function syntax",
            question_what="the result of using the #() shorthand to create a function that adds 1 to its argument and applying it to 5",
            goal_text="use the shorthand syntax to create a function that adds 1 to its argument and apply it to 5",
            scenario=(
                "Mossback was in a hurry at the roadside and had no "
                "time to write a full recipe card. She scratched a "
                "quick shorthand mark — `#(+ % 1)` — on a stone and "
                "put 5 acorns in front of it immediately."
            ),
            need=(
                "She needed the one-step add-and-pass result right "
                "away. The shorthand let her skip naming a parameter "
                "and posting a card — the percent sign stood for "
                "whatever came in."
            ),
            mapping=(
                "`#(...)` is the quick-mark shorthand for an unnamed "
                "recipe. `%` is where the argument slots in; "
                "applying 5 replaces `%` with 5 in the body."
            ),
            resolution=(
                "the quick-mark recipe accepted 5 and returned the "
                "result of adding one to it — the shorthand's "
                "one-pass answer."
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
                "Mossback scratched a two-slot shorthand mark on a "
                "stone: the first slot `%1` and the second `%2`, "
                "joined by multiplication. She placed 3 and 4 in "
                "front of it without pause."
            ),
            need=(
                "Two incoming counts needed to be multiplied at "
                "once. The two-slot shorthand let her skip a full "
                "recipe-card write-up for a single calculation."
            ),
            mapping=(
                "`#(* %1 %2)` is the quick-mark for a two-slot "
                "recipe. Passing 3 and 4 binds them to `%1` and `%2` "
                "respectively; the body multiplies those two slots."
            ),
            resolution=(
                "the two-slot quick-mark produced the product of "
                "the two counts — the shorthand's combined result "
                "in a single application."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_11 = SubjectCurriculum(grade=3, subject_id="G3-11",
    subject_title="Substitution rule", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(let [a 7] (+ a a))",
            expected=14,
            concept_phrase="the binding referenced multiple times",
            question_what="the result of adding a to itself after binding a locally to 7 via let",
            goal_text="bind a to 7 and add a to itself",
            scenario=(
                'Mossback loaded her pouch with {drawn.a} acorns and named that count a. She needed to add the count to itself — the same pouch reached for twice — to report the combined total at the next marker.'
            ),
            need=(
                "Both summands were the same named quantity. Without "
                "the binding in place, she would have had to remember "
                "the number separately each time she reached for it."
            ),
            mapping=(
                'The substitution rule says: everywhere a appears, replace it with its bound value. `(+ a a)` becomes `(+ {drawn.a} {drawn.a})` — the pouch consulted once per occurrence.'           ),
            resolution=(
                "the pouch was drawn from twice and the two draws "
                "combined into the total Mossback reported at the marker."
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
                "Mossback wrote a one-slot recipe: take a count x "
                "and multiply it by itself. She pressed 6 acorns "
                "into the slot at once, needing the squared count "
                "for a layout plan."
            ),
            need=(
                "The layout needed a square — same count times "
                "itself. Naming the incoming count x let the "
                "recipe reference it twice without Mossback "
                "restating the number."
            ),
            mapping=(
                "When 6 is passed, x becomes 6 by the substitution "
                "rule. `(* x x)` then becomes `(* 6 6)` — the "
                "parameter consulted at each occurrence in the body."
            ),
            resolution=(
                "the recipe slotted 6 in for x both times and "
                "returned the squared count the layout plan required."
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_12 = SubjectCurriculum(grade=3, subject_id="G3-12",
    subject_title="Scope vs namespace", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(do (def g 5) (let [g 99] (+ g 1)))",
            expected=100,
            concept_phrase="the scope shadowing and computation",
            question_what="the result of adding 1 to g, computed inside a let where g is locally bound to 99, shadowing the top-level def",
            goal_text="define g at the top level, shadow it in a let with a different value, and compute g+1 inside the let",
            scenario=(
                'The road sign at the trailhead read g = 5. Mossback slipped onto a side-path and tied a fresh pouch at her hip labeled g, loaded with {drawn.b} acorns. She needed g plus one more while on the side-path.'
            ),
            need=(
                "On the side-path the local pouch mattered, not the "
                "distant road sign. The computation had to draw from "
                "the nearer source or it would use the wrong count."
            ),
            mapping=(
                'Inside the `let`, g is looked up in the local scope first — the hip pouch, not the road sign. `(+ g {drawn.c})` uses the local {drawn.b} and adds one more acorn to it.'
            ),
            resolution=(
                "the side-path computation drew from the local "
                "pouch and returned the sum of that count plus one."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_13 = SubjectCurriculum(grade=3, subject_id="G3-13",
    subject_title="fn body returns last form", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="((fn [x] x x x 99) 1)",
            expected=99,
            concept_phrase="the function body with multiple expressions",
            question_what="the result of applying an anonymous fn where the body contains multiple expressions but only the last one is returned, applied to 1",
            goal_text="create an anonymous function with multiple forms in its body but return only the last one",
            scenario=(
                "Mossback's recipe card for this stretch listed "
                "several intermediate steps, but the cook only "
                "served the final dish — everything before it was "
                "preparation, not what got plated."
            ),
            need=(
                "The kitchen needed only the final item from the "
                "recipe's sequence. The earlier steps ran through "
                "but were not carried out of the kitchen."
            ),
            mapping=(
                "A `fn` body evaluates every expression in order, "
                "but only the last one becomes the return value. "
                "The 99 at the end of the body is the final dish — "
                "what the REPL takes away."
            ),
            resolution=(
                "the recipe ran through every step and plated only "
                "the last item — the one value the caller received."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_14 = SubjectCurriculum(grade=3, subject_id="G3-14",
    subject_title="do form", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(do 1 2 3)",
            expected=3,
            concept_phrase="the do form with multiple values",
            question_what="the final value evaluated by do from the sequence",
            goal_text="evaluate a sequence of values and return the last one",
            scenario=(
                'The scribe at the trailhead read three entries aloud in order — {drawn.a}, then {drawn.b}, then {drawn.c} — as Mossback listened. Each entry was acknowledged in turn, but only the last one was recorded as the verdict.'
            ),
            need=(
                "The ledger entry required the final number in the "
                "sequence. The earlier numbers had to be read aloud "
                "in order, but they would not appear in the record."
            ),
            mapping=(
                "`do` evaluates each sub-form in sequence, left to "
                "right. The value of the whole `do` is the value of "
                "its last sub-form — the scribe's final word."
            ),
            resolution=(
                "the scribe reached the last entry in the sequence "
                "and recorded it as the one value the ledger kept."
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
                "The scribe worked through three arithmetic tallies "
                "in the order Mossback dictated: one plus one, then "
                "two plus two, then three plus three. Each result "
                "was computed, but only the last mattered for the log. The values drawn fresh were {drawn.a}, {drawn.b}, and {drawn.c}."
            ),
            need=(
                "The log required the result of the final computation "
                "in the sequence. The prior computations had to occur "
                "first, but their results were not what went into "
                "the day's record."
            ),
            mapping=(
                "`do` runs each expression in turn. The values of the "
                "first two are computed and discarded; the third is "
                "computed and returned as the form's result."
            ),
            resolution=(
                "the scribe recorded the result of the final "
                "arithmetic tally — the sum the three-plus-three "
                "produced at the end of the sequence."
            ),
            tags=("story",),
        ),
    ], subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_15 = SubjectCurriculum(grade=3, subject_id="G3-15",
    subject_title="Side-effects in body", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form='(do (println "hi") 42)',
            expected=42,
            concept_phrase="the do form with side-effects and final return",
            question_what="the final value evaluated by do, ignoring the intermediate println side-effect",
            goal_text="execute a print statement for side-effects, then return a different value",
            scenario=(
                'Mossback had two things to do at the checkpoint: call out a greeting to the gatekeeper (a side task, not a counted item), and then present the count of {drawn.b} acorns that was her official delivery.'
            ),
            need=(
                "The greeting had to happen first, but the ledger "
                "only recorded the delivery count. The side-task "
                "was real work but left no number in the tally."
            ),
            mapping=(
                '`println` is the greeting — a side-effect that runs and produces no countable value. The `{drawn.b}` that follows is the last form in `do`, so it becomes the value the REPL returns.'
            ),
            resolution=(
                "the greeting rang out and was heard, then the "
                "delivery count was handed to the ledger — only "
                "the final form's value settled in the record."
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_16 = SubjectCurriculum(grade=3, subject_id="G3-16",
    subject_title="Name collision: namespace vs let", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(let [+ 99] +)",
            expected=99,
            concept_phrase="the shadowed operator binding",
            question_what="the value locally bound to the + operator via let",
            goal_text="shadow the plus operator with a local binding and return the bound value",
            scenario=(
                'Mossback tied a pouch labeled `+` at her hip and filled it with {drawn.a} acorns for one short stretch. The road sign already used that name, but the pouch was nearer.'
            ),
            need=(
                "She wanted to confirm that the local pouch "
                "eclipsed even a globally known name inside "
                "the body of the binding form."
            ),
            mapping=(
                "`let` can bind any name, including one the "
                "namespace already owns. Inside the body, `+` "
                "resolves to the local pouch, not the global sign."
            ),
            resolution=(
                "the pouch answered when `+` was looked up, "
                "returning its stored count over the global name."
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_17 = SubjectCurriculum(grade=3, subject_id="G3-17",
    subject_title="Naming conventions (kebab-case)", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(let [hare-speed 4 tortoise-speed 1] (- hare-speed tortoise-speed))",
            expected=3,
            concept_phrase="the kebab-case naming and subtraction",
            question_what="the result of subtracting tortoise-speed from hare-speed after binding both via let",
            goal_text="bind hare-speed to 4 and tortoise-speed to 1, then compute their difference",
            scenario=(
                "Two signs appeared on the road, each following the meadow's kebab-case convention: hare-speed at {drawn.a} paces per mark and tortoise-speed at 1. Mossback needed to post both clearly before computing the gap."
            ),
            need=(
                "The gap between the two speeds was what the race "
                "steward required. Multi-word names with hyphens "
                "kept each sign unambiguous — no spaces, no "
                "confusion between the two."
            ),
            mapping=(
                "`let` binds hare-speed to {drawn.a} and tortoise-speed to 1. The kebab-case names follow the meadow's posting convention. `(- hare-speed tortoise-speed)` reads both signs and subtracts."
            ),
            resolution=(
                "the two clearly labeled signs were consulted and "
                "the gap between the speeds was the result the "
                "race steward recorded."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_18 = SubjectCurriculum(grade=3, subject_id="G3-18",
    subject_title="When to name vs inline", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(let [n 5] (* n n n))",
            expected=125,
            concept_phrase="the named binding used multiple times",
            question_what="the result of multiplying n by itself three times after binding n locally to 5 via let",
            goal_text="bind n to 5 and compute n cubed",
            scenario=(
                'Mossback needed to compute a cube from a single count. She loaded her pouch with {drawn.a} acorns and named it n, then drew from that same pouch three times over for the multiplication.'
            ),
            need=(
                "Writing the literal count three times in a row "
                "would be error-prone and hard to adjust later. "
                "Naming it once and referencing the name three times "
                "was the disciplined approach."
            ),
            mapping=(
                '`let` binds n to {drawn.a} once. The body `(* n n n)` reaches into the pouch three times, each time finding 5. The cube is computed through the single named source.'
            ),
            resolution=(
                "the pouch was consulted three times and the triple "
                "product was the cube the ledger required."
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
                "Mossback decided the count was simple enough to "
                "write out directly — no pouch, no name. She placed "
                "three fives side by side on the calculation stone "
                "and let the REPL multiply them at once."
            ),
            need=(
                "For a one-time cube of a known constant, naming "
                "would add ceremony with no benefit. The inline "
                "form was shorter and just as clear."
            ),
            mapping=(
                'Inline literals bypass the pouch entirely — the three {drawn.a}s are written directly in the form. The REPL multiplies them without any binding or name-lookup step.'
            ),
            resolution=(
                "the three inline values combined into the same "
                "cube as the named approach — the direct route "
                "worked equally well for a fixed constant."
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
