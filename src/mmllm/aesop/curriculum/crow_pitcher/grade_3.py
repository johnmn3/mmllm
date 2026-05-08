"""Grade 3 — naming, scope, substitution. Through crow-pitcher.

The fable lens: the Tortoise's careful approach is exactly the
substitution-rule discipline. The Hare's "I just know the answer"
is what binding-by-name corrects.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.crow_pitcher.grade_1 import (
    _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.crow_pitcher._metaphor_pools import (
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
    subject_title="def — top-level binding", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(do (def x 42) x)",
            expected=42,
            concept_phrase="the top-level binding and lookup",
            question_what="the value of x after using def to bind x to 42",
            goal_text="bind x to 42 and return it",

            scenario=(
                "Korvus pressed his talon to the pitcher's clay rim in the "
                "garden and carved the name x deep into the clay, then "
                "filled that groove with a count: 42, now permanently named."
            ),
            need=(
                "Once the carving was set, he wanted to read the count "
                "back from the rim — to confirm x would answer when called."
            ),
            mapping=(
                "`def` carves a name into the namespace rim and fills it "
                "with a value. The name persists as long as the rim stands. "
                "Evaluating x reads from the groove and returns what was carved."
            ),
            resolution=(
                "42 — the rim answered, the count intact in the groove "
                "where the talon had pressed it."
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
                "Caw found an unmarked section of the pitcher's rim at the "
                "market and pressed her talon in, carving y and filling the "
                "groove with a small stone-count: seven, set in clay."
            ),
            need=(
                "She needed to read y back from the rim to confirm the "
                "groove held the count and would answer when called again."
            ),
            mapping=(
                "`def` cuts the name y into the namespace rim and stores "
                "7 in that groove permanently. Evaluating y retrieves "
                "exactly what was pressed in — the rim does not forget."
            ),
            resolution=(
                "The water rose to the expected mark — the groove gave back "
                "what Caw had pressed into it. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_02 = SubjectCurriculum(grade=3, subject_id="G3-02",
    subject_title="def — redefinition", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(do (def x 1) (def x 99) x)",
            expected=99,
            concept_phrase="the redefined binding",
            question_what="the value of x after redefining it with def from 1 to 99",
            goal_text="bind x to 1, then redefine it as 99 and return it",

            scenario=(
                "Sable stood at the pitcher's rim in the orchard and carved "
                "x, filling the groove with a single stone-count. Then Sable "
                "pressed deeper, widening the groove and replacing that count "
                "with a new tally: ninety-nine, the old mark erased."
            ),
            need=(
                "Sable needed to confirm that the rim now held only the "
                "latest carving — that the old count of one was gone."
            ),
            mapping=(
                "A second `def` for the same name overwrites the groove: "
                "the namespace rim keeps only the most recent carving. "
                "Evaluating x returns whatever was last pressed in — "
                "the first value is gone, the new one answers."
            ),
            resolution=(
                "The water rose to the expected mark — only the newest "
                "carving spoke, the earlier count silent beneath it. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_03 = SubjectCurriculum(grade=3, subject_id="G3-03",
    subject_title="let — local binding", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(let [x 3] (+ x 1))",
            expected=4,
            concept_phrase="the local binding and addition",
            question_what="the running total after binding x to 3 and adding 1",
            goal_text="bind a value of 3 to a local name x for one stretch, then return that value plus one",

            scenario=(
                "Korvus arrived at the tall clay pitcher in the orchard, "
                "three smooth stones from the morning's count in mind. Before "
                "dropping any, he tucked the count of three under his left "
                "wing, close and named: x, holding three."
            ),
            need=(
                "He needed to know how far the water would rise if he added "
                "one more stone to whatever was tucked under his wing."
            ),
            mapping=(
                "`let` gives a name to a tucked value: x binds 3 for the "
                "span of the form. Inside that stretch, `(+ x 1)` reaches "
                "under the wing and adds one. When the form ends the wing "
                "opens; the binding dissolves."
            ),
            resolution=(
                "4 — the tucked count of three, plus the one stone added "
                "while the wing held it firm. (with {drawn.a} folded in)"
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
                "Caw tucked a count of ten under her wing at the farm, "
                "naming it n for the span of one drop. She wanted to "
                "multiply that tucked count against itself before the "
                "wing opened and the name dissolved."
            ),
            need=(
                "She needed the water level that ten rows of the stones "
                "would reach — n times itself, computed while the wing held."
            ),
            mapping=(
                "`let` tucks n bound to 10 for the form's span. Inside, "
                "`(* n n)` multiplies the tucked count by itself. "
                "When the let ends the wing opens and n is gone."
            ),
            resolution=(
                "The water rose to the expected mark — n squared, "
                "computed while the wing still held the count. (with {drawn.a} folded in)"
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
                "Sable tucked the stones under one wing at the meadow "
                "pitcher, naming that tucked count a for the span of "
                "a single form, then looked directly at the tucked bundle "
                "without adding or removing anything."
            ),
            need=(
                "Sable needed to confirm that reading a inside the let "
                "returned exactly the count that had been tucked — no more, "
                "no less, no arithmetic applied."
            ),
            mapping=(
                "`let` tucks 5 under the name a. The body simply references "
                "a, so the wing opens and delivers the count unchanged. "
                "The binding dissolves after the form completes."
            ),
            resolution=(
                "The water rose to the expected mark — the tucked count "
                "returned whole, untouched by any operation. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_04 = SubjectCurriculum(grade=3, subject_id="G3-04",
    subject_title="let — multi-binding", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(let [a 1 b 2] (+ a b))",
            expected=3,
            concept_phrase="the multi-binding and addition",
            question_what="adding a and b after binding both via let to 1 and 2",
            goal_text="bind a to 1 and b to 2, then add them",

            scenario=(
                "Korvus tucked one stone under his left wing and two "
                "under his right, naming them a and b at the hilltop "
                "pitcher. Both wings held their counts for the span of "
                "one combined drop."
            ),
            need=(
                "He wanted to know the water level when both tucked "
                "counts fell together — a and b combined into one drop."
            ),
            mapping=(
                "`let` can tuck multiple bindings at once: a gets 1, "
                "b gets 2, both held for the form's span. `(+ a b)` "
                "draws from both wings and adds the counts."
            ),
            resolution=(
                "The water rose to the expected mark — both tucked "
                "counts joined, the combined drop landing true. (with {drawn.a} folded in)"
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
                "Caw held the stones under one wing and three under "
                "the other at the garden pitcher, naming them x and y. "
                "She planned to let one count diminish the other while "
                "both wings remained closed."
            ),
            need=(
                "She needed the water level after removing the y-count "
                "of stones from the x-count — subtraction of two tucked "
                "values before either wing opened."
            ),
            mapping=(
                "`let` tucks x as 5 and y as 3 simultaneously. Inside "
                "the form, `(- x y)` draws from both wings and subtracts "
                "y from x — the smaller count taken from the larger."
            ),
            resolution=(
                "The water rose to the expected mark — the lesser "
                "wing-count subtracted cleanly from the greater. (with {drawn.a} folded in)"
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
                'Sable spread three wing-pouches at the village pitcher and tucked a different count into each — the counts — naming them a, b, and c, all held for one combined form.'
            ),
            need=(
                "Sable needed the water level when all three tucked "
                "counts dropped together, a and b and c summed in "
                "a single movement."
            ),
            mapping=(
                "`let` tucks three bindings at once: a, b, and c each "
                "hold their count for the span. `(+ a b c)` empties "
                "all three pouches into one sum."
            ),
            resolution=(
                "The water rose to the expected mark — all three "
                "tucked counts combined, the pitcher confirming the sum. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_05 = SubjectCurriculum(grade=3, subject_id="G3-05",
    subject_title="let — shadowing outer def", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(do (def x 10) (let [x 99] x))",
            expected=99,
            concept_phrase="the inner binding shadowing the outer",
            question_what="the value of x inside the let scope where it shadows the def binding",
            goal_text="define x at the top level, then shadow it locally and return the inner value",

            scenario=(
                "Korvus carved x into the pitcher's rim at the orchard "
                "and filled the groove with ten. Then, for one short stretch, "
                "he tucked a different count of ninety-nine under his wing "
                "and also named it x — a private shadow over the public groove."
            ),
            need=(
                "Inside that wing-span, he needed to know which x the REPL "
                "would read: the groove on the rim or the count tucked "
                "under the wing."
            ),
            mapping=(
                "The `let` binding for x shadows the `def` groove inside "
                "its span. The tucked wing-count outranks the rim carving "
                "while the wing is closed — the local x answers first."
            ),
            resolution=(
                "The water rose to the expected mark — the wing-tucked "
                "count spoke, the rim groove silent inside the let. (with {drawn.a} folded in)"
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
                "Caw watched Korvus tuck a shadow-count under his wing "
                "at the orchard pitcher. After the wing opened and the "
                "local name dissolved, she pointed at the rim's carved "
                "groove and asked what x meant now."
            ),
            need=(
                "She needed to confirm that once the let closed, the rim "
                "groove answered again — the shadow gone, the original "
                "carving restored to view."
            ),
            mapping=(
                "Once the `let` form ends, its bindings dissolve and "
                "the wing opens empty. The outer `def` groove is fully "
                "visible again; x now reads from the rim as before."
            ),
            resolution=(
                "The water rose to the expected mark — the rim's original "
                "carving spoke, the shadow-count gone with the closed wing. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_06 = SubjectCurriculum(grade=3, subject_id="G3-06",
    subject_title="let — binding can reference prior", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(let [a 5 b (* a 2)] b)",
            expected=10,
            concept_phrase="the sequential binding where later refers to earlier",
            question_what="the value of b, bound to twice a via let, after a is bound to 5",
            goal_text="bind a to 5, then bind b to twice a, and return b",

            scenario=(
                "Sable tucked the stones under one wing at the meadow "
                "pitcher, naming the count a. Before closing the second "
                "wing, Sable reached into the first and doubled what was "
                "there, tucking the result away as b."
            ),
            need=(
                "Sable needed to read b — the doubled count built from "
                "a — to confirm the later binding had correctly used "
                "the earlier one."
            ),
            mapping=(
                "In a `let`, later bindings can reference earlier ones: "
                "b is computed from a, which is already tucked. The "
                "bindings are sequential, each available to those that follow."
            ),
            resolution=(
                "The water rose to the expected mark — b held twice "
                "the a-count, the sequential tuck working as planned. (with {drawn.a} folded in)"
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
                "Korvus at the farm pitcher tucked the stones as a, "
                "then added one to that tucked count for b, then doubled "
                "b for c — each wing-pouch built from the one before it, "
                "a chain of three sequential tucks."
            ),
            need=(
                "He needed to read c at the end of the chain, to confirm "
                "each step had correctly drawn from the prior tucked "
                "count and handed its result forward."
            ),
            mapping=(
                "Each binding in the `let` vector sees all previous "
                "bindings. a is tucked first, b uses a, c uses b — "
                "a cascade of wing-pouches, each built on the last."
            ),
            resolution=(
                "The water rose to the expected mark — the chained "
                "tucks each resolved correctly, c arriving as planned. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_07 = SubjectCurriculum(grade=3, subject_id="G3-07",
    subject_title="fn — anonymous function", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="((fn [x] (+ x 1)) 4)",
            expected=5,
            concept_phrase="the anonymous function call",
            question_what="the result of applying an anonymous fn that adds 1 to its argument to the value 4",
            goal_text="create an anonymous function that adds 1 to its argument and apply it to 4",

            scenario=(
                "Caw perched at the pitcher's rim in the garden and scratched "
                "a small drop-order into the clay with her talon: accept a "
                "count named x, then add one stone to it. No name carved — "
                "just the pattern, ready at the rim."
            ),
            need=(
                "She wanted to apply the recipe at once, feeding it the "
                "count of four, and see how high the water rose."
            ),
            mapping=(
                "`fn` scratches an anonymous recipe: it declares the argument "
                "x and specifies the body `(+ x 1)`. Wrapping the recipe with "
                "4 applies it immediately — the argument fills x, the body runs."
            ),
            resolution=(
                "5 — the recipe added one stone to the count of four, "
                "the water clearing the fifth notch. (count: 4)"
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
                "Sable scratched a two-slot drop-order onto the village "
                "pitcher's rim: accept counts a and b, multiply them "
                "together. No name carved on the rim — the recipe existed "
                "only for one immediate use."
            ),
            need=(
                "Sable needed the water level when three rows of four "
                "stones each fell in, the anonymous recipe doing the "
                "multiplication without being named first."
            ),
            mapping=(
                "`fn` with two parameters scratches a recipe accepting "
                "a and b. Applied immediately to 3 and 4, the arguments "
                "fill the slots and the body `(* a b)` runs at once."
            ),
            resolution=(
                "The water rose to the expected mark — the two-slot "
                "recipe multiplied the counts and delivered the product. (count: 3)"
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_08 = SubjectCurriculum(grade=3, subject_id="G3-08",
    subject_title="fn — multi-arg", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="((fn [a b c] (+ a b c)) 1 2 3)",
            expected=6,
            concept_phrase="the three-argument anonymous function call",
            question_what="the result of applying an anonymous fn with three parameters that adds them to 1, 2, and 3",
            goal_text="create an anonymous function with three parameters that adds them and apply it to 1, 2, and 3",

            scenario=(
                "Korvus scratched a three-slot drop-order onto the hilltop "
                "pitcher's rim: accept a, b, and c, then sum all three. "
                "He pressed the recipe immediately against the counts — "
                "the drawn counts — feeding each slot in turn."
            ),
            need=(
                "He needed the water level when one, two, and the stones "
                "fell together through the three-slot recipe in a single "
                "anonymous application."
            ),
            mapping=(
                "`fn` with three parameters a, b, c scratches a recipe "
                "that sums its inputs. Applied to 1, 2, 3 immediately, "
                "each argument fills its named slot and `(+ a b c)` runs."
            ),
            resolution=(
                "The water rose to the expected mark — the counts "
                "fed through the three-slot recipe, the sum arriving true. (count: 3)"
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_09 = SubjectCurriculum(grade=3, subject_id="G3-09",
    subject_title="defn — shorthand", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(do (defn dbl [x] (* x 2)) (dbl 5))",
            expected=10,
            concept_phrase="the named recipe-card and its first call",
            question_what="the doubled count after defining a recipe named dbl and calling it on 5",
            goal_text="define a recipe named dbl that takes a quantity and serves twice that, then call dbl on 5 pinches",

            scenario=(
                "Caw carved dbl into the market pitcher's rim and "
                "scratched the recipe beneath: accept x, serve twice x — "
                "all in one talon-stroke."
            ),
            need=(
                "She wanted to call the named recipe with five and read "
                "back the water level."
            ),
            mapping=(
                "`defn` carves a named recipe onto the rim in one form — "
                "shorthand for `def` plus `fn`. `(dbl 5)` fills x and "
                "runs the doubling body."
            ),
            resolution=(
                "The water rose to the expected mark — the named recipe "
                "doubled the count and the rim delivered. (with {drawn.a} folded in)"
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
                "Sable pressed add3 into the village pitcher's rim "
                "alongside a three-slot recipe: accept a, b, c, then "
                "sum them — carved deep and permanent."
            ),
            need=(
                "Sable wanted to call add3 with the drawn counts and "
                "watch the water reach the expected sum."
            ),
            mapping=(
                "`defn` carves add3 as a named recipe with three slots. "
                "`(add3 1 2 3)` fills a, b, c and runs `(+ a b c)`."
            ),
            resolution=(
                "The water rose to the expected mark — add3 filled its "
                "slots and summed them cleanly. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_10 = SubjectCurriculum(grade=3, subject_id="G3-10",
    subject_title="anonymous shorthand #()", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(#(+ % 1) 5)",
            expected=6,
            concept_phrase="the shorthand function syntax",
            question_what="the result of using the #() shorthand to create a function that adds 1 to its argument and applying it to 5",
            goal_text="use the shorthand syntax to create a function that adds 1 to its argument and apply it to 5",

            scenario=(
                "Korvus scratched only a terse mark onto the garden "
                "pitcher's rim — the percent-sign standing for whatever "
                "count arrived — then applied that brief recipe at once "
                "to a count of five, using the shortest talon-scratch known."
            ),
            need=(
                "He needed the water level after adding one to five, "
                "using the abbreviated recipe form rather than the longer "
                "fn-scratch, to test whether the shorthand worked."
            ),
            mapping=(
                "`#(...)` is the shorthand recipe scratch: `%` stands "
                "for the single argument. Applied immediately to 5, "
                "the percent fills with five and `(+ % 1)` runs."
            ),
            resolution=(
                "The water rose to the expected mark — the shorthand "
                "scratch worked as cleanly as the longer recipe form. (count: 5)"
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
                "Caw scratched the briefest two-slot recipe onto the "
                "orchard pitcher's rim using percent-one and percent-two "
                "as stand-ins, then applied the shorthand to counts "
                "three and four without carving any name at all."
            ),
            need=(
                "She needed to confirm that the two-slot shorthand recipe "
                "correctly multiplied three by four when both percent-marks "
                "were filled with their respective counts."
            ),
            mapping=(
                "`#(* %1 %2)` is the shorthand for a two-argument recipe: "
                "%1 and %2 fill in order from the arguments given. "
                "Applied to 3 and 4, the body multiplies them at once."
            ),
            resolution=(
                "The water rose to the expected mark — both percent-slots "
                "filled cleanly and the product arrived without a name. (count: 3)"
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_11 = SubjectCurriculum(grade=3, subject_id="G3-11",
    subject_title="Substitution rule", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(let [a 7] (+ a a))",
            expected=14,
            concept_phrase="the binding referenced multiple times",
            question_what="the result of adding a to itself after binding a locally to 7 via let",
            goal_text="bind a to 7 and add a to itself",

            scenario=(
                "Sable tucked the stones under one wing at the hilltop "
                "pitcher, naming the count a — then referenced a twice "
                "without adding more stones."
            ),
            need=(
                "Sable needed to confirm the wing held firm for both "
                "draws and the body added the count to itself."
            ),
            mapping=(
                "A `let`-bound name may be used any number of times — "
                "each reference substitutes the same tucked value. "
                "`(+ a a)` draws 7 twice."
            ),
            resolution=(
                "The water rose to the expected mark — the tucked count "
                "substituted twice for both draws. (with {drawn.a} folded in)"
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
                "Korvus scratched a self-multiplying recipe onto the "
                "farm pitcher's rim: accept x, multiply x by x. He fed "
                "the recipe a count of six, then watched to see if the "
                "single argument could serve both sides of the product."
            ),
            need=(
                "He needed to confirm that x filled both multiplication "
                "slots from one argument — substituted twice inside the "
                "anonymous recipe without the wing opening early."
            ),
            mapping=(
                "Inside an `fn` body, the parameter x can appear as many "
                "times as needed. `(* x x)` substitutes the argument 6 "
                "into both positions — the count squares itself."
            ),
            resolution=(
                "The water rose to the expected mark — x substituted "
                "into both slots, the self-multiplication completing true. (count: 6)"
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_12 = SubjectCurriculum(grade=3, subject_id="G3-12",
    subject_title="Scope vs namespace", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(do (def g 5) (let [g 99] (+ g 1)))",
            expected=100,
            concept_phrase="the scope shadowing and computation",
            question_what="the result of adding 1 to g, computed inside a let where g is locally bound to 99, shadowing the top-level def",
            goal_text="define g at the top level, shadow it in a let with a different value, and compute g+1 inside the let",

            scenario=(
                "Caw carved g into the orchard pitcher's rim with five, "
                "then tucked ninety-nine under her wing also named g — "
                "shadowing the rim groove."
            ),
            need=(
                "Inside the shadow-span she had to know which g the "
                "REPL would read — rim groove or wing-tucked count."
            ),
            mapping=(
                "Inside a `let`, the local binding outranks the "
                "namespace groove. The wing-tucked count shadows the "
                "carved one. `(+ g 1)` reads the wing-count."
            ),
            resolution=(
                "The water rose to the expected mark — the wing-tucked "
                "g answered, one added to the shadow. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_13 = SubjectCurriculum(grade=3, subject_id="G3-13",
    subject_title="fn body returns last form", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="((fn [x] x x x 99) 1)",
            expected=99,
            concept_phrase="the function body with multiple expressions",
            question_what="the result of applying an anonymous fn where the body contains multiple expressions but only the last one is returned, applied to 1",
            goal_text="create an anonymous function with multiple forms in its body but return only the last one",

            scenario=(
                "Sable scratched a multi-line recipe onto the market "
                "pitcher's rim: several expressions in a row, the last "
                "a fixed count of ninety-nine."
            ),
            need=(
                "Sable needed to confirm only the final expression "
                "set the water level — earlier ones silently discarded."
            ),
            mapping=(
                "An `fn` body evaluates all expressions in order but "
                "returns only the last one's value. The earlier x's "
                "ran and were dropped."
            ),
            resolution=(
                "The water rose to the expected mark — the last "
                "expression alone set the level. (count: 99)"
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_14 = SubjectCurriculum(grade=3, subject_id="G3-14",
    subject_title="do form", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(do 1 2 3)",
            expected=3,
            concept_phrase="the do form with multiple values",
            question_what="the final value evaluated by do from the sequence",
            goal_text="evaluate a sequence of values and return the last one",

            scenario=(
                "Korvus pressed the pebbles into the pitcher at the "
                "village in sequence — one, then two, then three — each "
                "dropping past the last. The pitcher recorded each drop "
                "but showed only the final depth."
            ),
            need=(
                "He needed to confirm that dropping the values in "
                "sequence returned only the last one — the earlier "
                "values real but their depths replaced by the final drop."
            ),
            mapping=(
                "`do` evaluates each expression in sequence, discarding "
                "all results except the last. Only the final expression's "
                "value rises to the water line — the earlier drops ran "
                "but their readings were overwritten."
            ),
            resolution=(
                "The water rose to the expected mark — the last drop "
                "alone set the level, the earlier two replaced and gone. (with {drawn.a} folded in)"
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
                "Caw dropped three arithmetic stone-pairs into the meadow "
                "pitcher in order: one-and-one, then two-and-two, then "
                "three-and-three. Each pair fell, each sum formed, each "
                "reading replaced by the next."
            ),
            need=(
                "She needed to know what the final water level would be "
                "when only the last computed sum set the depth — the "
                "first two sums real but their readings overwritten."
            ),
            mapping=(
                "`do` evaluates all three additions in sequence. The first "
                "two results are computed and then discarded. Only the "
                "third expression's sum persists as the returned value."
            ),
            resolution=(
                "The water rose to the expected mark — the third sum "
                "alone remained, the first two sums washed away by the last. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_15 = SubjectCurriculum(grade=3, subject_id="G3-15",
    subject_title="Side-effects in body", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form='(do (println "hi") 42)',
            expected=42,
            concept_phrase="the do form with side-effects and final return",
            question_what="the final value evaluated by do, ignoring the intermediate println side-effect",
            goal_text="execute a print statement for side-effects, then return a different value",

            scenario=(
                "Sable perched at the garden pitcher and called out a "
                "greeting — a cry into the air that left no stone in "
                "the water — then dropped a single count of forty-two "
                "as the final act."
            ),
            need=(
                "Sable needed to know what water level the REPL would "
                "report: the cry that left no mark, or the count dropped "
                "after the cry had faded."
            ),
            mapping=(
                "`do` runs `println` for its side-effect — the cry sounds "
                "but adds nothing to the water. Only the last form, 42, "
                "sets the level. Side-effects happen; only the final "
                "value is returned."
            ),
            resolution=(
                "The water rose to the expected mark — the cry faded "
                "without trace, the final count alone setting the depth. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_16 = SubjectCurriculum(grade=3, subject_id="G3-16",
    subject_title="Name collision: namespace vs let", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(let [+ 99] +)",
            expected=99,
            concept_phrase="the shadowed operator binding",
            question_what="the value locally bound to the + operator via let",
            goal_text="shadow the plus operator with a local binding and return the bound value",

            scenario=(
                "Korvus tucked a count of ninety-nine under his wing at "
                "the hilltop pitcher, then named that tucked count with "
                "the same mark used for addition — the plus-sign itself — "
                "as a local shadow over the familiar operator."
            ),
            need=(
                "He needed to know what the REPL would return when it "
                "looked up the plus-sign inside the let: the arithmetic "
                "operator from the namespace, or the tucked count."
            ),
            mapping=(
                "A `let` binding can shadow any name, even built-in "
                "operators. Inside the form, + resolves to the tucked "
                "99, not the addition function — the local shadow "
                "outranks the namespace groove completely."
            ),
            resolution=(
                "The water rose to the expected mark — the tucked count "
                "answered for the plus-sign, the operator unreachable inside. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_17 = SubjectCurriculum(grade=3, subject_id="G3-17",
    subject_title="Naming conventions (kebab-case)", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(let [hare-speed 4 tortoise-speed 1] (- hare-speed tortoise-speed))",
            expected=3,
            concept_phrase="the kebab-case naming and subtraction",
            question_what="the result of subtracting tortoise-speed from hare-speed after binding both via let",
            goal_text="bind hare-speed to 4 and tortoise-speed to 1, then compute their difference",

            scenario=(
                "Caw stood at the road pitcher and tucked two counts under "
                "her wings: four under the left named hare-speed, one under "
                "the right named tortoise-speed. The hyphenated names were "
                "pressed as single grooves into the wing-cache."
            ),
            need=(
                "She needed to compute the gap between the two speeds — "
                "how much faster one creature moved than the other — "
                "using the descriptive hyphenated names to keep the "
                "meaning clear."
            ),
            mapping=(
                "Clojure's convention uses hyphens in multi-word names "
                "`let` tucks hare-speed as 4 and tortoise-speed as 1 "
                "simultaneously. `(- hare-speed tortoise-speed)` draws "
                "from both wings and subtracts."
            ),
            resolution=(
                "The water rose to the expected mark — the gap between "
                "the two speeds arrived, the hyphenated names clear throughout. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_18 = SubjectCurriculum(grade=3, subject_id="G3-18",
    subject_title="When to name vs inline", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(let [n 5] (* n n n))",
            expected=125,
            concept_phrase="the named binding used multiple times",
            question_what="the result of multiplying n by itself three times after binding n locally to 5 via let",
            goal_text="bind n to 5 and compute n cubed",

            scenario=(
                "Sable tucked the stones under one wing at the village "
                "pitcher, naming the count n, then used that one tucked "
                "count three times in the body — multiplying n by itself "
                "twice over without re-stating the count."
            ),
            need=(
                "Sable needed the water level for five cubed, choosing "
                "to name n once so the body could reference the same "
                "count repeatedly without repeating the literal five."
            ),
            mapping=(
                "Naming n once in `let` and using it three times in "
                "`(* n n n)` avoids repeating the literal. The tucked "
                "count substitutes into all three positions, the single "
                "binding serving the whole body."
            ),
            resolution=(
                "The water rose to the expected mark — n cubed, the "
                "single tucked count multiplied through three positions. (with {drawn.a} folded in)"
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
                "Korvus dropped three literal stone-counts of five into "
                "the garden pitcher all at once — no wing tucked, no name "
                "carved — just three fives fed directly to the multiplication "
                "as plain inline values."
            ),
            need=(
                "He needed the same water level as the named approach, "
                "but wanted to confirm that stating the count three times "
                "directly produced the same depth without any binding."
            ),
            mapping=(
                "With no `let`, `(* 5 5 5)` takes the literal 5 in each "
                "position. No wing-cache is used; the values are written "
                "inline. The result is the same but the form is self-contained."
            ),
            resolution=(
                "The water rose to the expected mark — three inline fives "
                "multiplied directly, the pitcher indifferent to the approach. (with {drawn.a} folded in)"
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
    print(f"grade-3 crow-pitcher smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
