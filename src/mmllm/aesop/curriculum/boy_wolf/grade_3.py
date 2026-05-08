"""Grade 3 — naming, scope, substitution. Through the
Boy-who-cried-Wolf fable.

The fable lens: the elder's careful approach is exactly the
substitution-rule discipline — every meaningful quantity in the
village got its own labeled mark on the slate, and the form refers to
those marks by name. The shepherd's "I just know the answer" is what
binding-by-name corrects: the elder writes the let, the REPL
substitutes, the village trusts what comes back.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.boy_wolf.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.boy_wolf._metaphor_pools import (
    _POUCH_SUBPLOTS, _RECIPE_SUBPLOTS, _ROADSIGN_SUBPLOTS, _SCRIBE_SUBPLOTS,
)
from mmllm.aesop.curriculum.boy_wolf._goals import GOALS, get_goal


# Add naming-themed subplots: the elder maintains the watchhouse ledger of
# named values, where every meaningful quantity gets its own labeled
# mark on the slate. Polarity preserved: ELDER labels and binds;
# SHEPHERD agrees to look at the binding rather than guess.
_NAMING_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [
    SubplotTemplate("""\
{elder_phrase} kept a small ledger {place} where every meaningful
quantity in the watchhouse got its own labeled mark on the slate.
{elder_he_she_cap} pointed to today's entry: {concept_phrase}. The form
{form_display} would settle it once {shepherd_phrase} agreed to look at
the binding rather than guess."""),

    SubplotTemplate("""\
"You can call it whatever you like," {elder} said {place}, "but the
form is what matters." {elder_he_she_cap} drew the binding for
{shepherd_phrase}: the form {form_display} captured {concept_phrase},
and the REPL would do the rest — no claims required, just the
runtime's answer."""),
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
_PLAN_POOL_G3 = _PLAN_POOL + (
    "I bind the inputs in a let, then compute.",
    "I name the values first and then combine them.",
    "I write the let-form so the REPL can substitute.",
)


G3_01 = SubjectCurriculum(grade=3, subject_id="G3-01",
    subject_title="def — top-level binding", fable="boy-wolf",
    examples=[
        _ex("(do (def x 42) x)", 42, "the binding (def x 42) followed by x",
            "the value bound to x after (def x 42)",
            scenario=(
                "Carol the elder stood at the townsfolk notice-post at the "
                "crossroads. She took her chalk and wrote the name x on the "
                "post, posting 42 sheep's worth of head-count beneath it for "
                "anyone walking past to see."
            ),
            need=(
                "Every shepherd on the path needed that name and its count "
                "to mean the same thing all morning. Without the posted "
                "notice, x would have meant nothing the moment a different "
                "voice claimed otherwise."
            ),
            mapping=(
                "`def` posts the name x on the notice-post alongside its "
                "bound count. The second expression looks the post up and "
                "reads back whatever was posted under that name — here, 42."
            ),
            resolution=(
                "the post returned exactly the count Carol had chalked, and the morning's record stood on village authority. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record."
            )),
        _ex("(do (def y 7) y)",  7,  "the binding (def y 7)",
            "the value bound to y",
            scenario=(
                "Carol stood at the same notice-post, holding chalk. This "
                "time she wrote the name y on the board and posted 7 sheep's "
                "worth of head-count beneath it for the afternoon round."
            ),
            need=(
                "The afternoon count was different from the morning. Every "
                "shepherd on the hill needed to know that y meant 7, just as "
                "surely as x meant its own count."
            ),
            mapping=(
                "The `def y 7` posts another name at the notice-post. The "
                "second expression reads y and finds whatever value the post "
                "holds under that name — here, 7."
            ),
            resolution=(
                "the post returned 7 for y, the afternoon's count stood posted, and both x and y had their own places on the village notice. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last."
            )),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_02 = SubjectCurriculum(grade=3, subject_id="G3-02",
    subject_title="def — redefinition", fable="boy-wolf",
    examples=[
        _ex("(do (def x 1) (def x 99) x)", 99,
            "the redefined x", "the value of x after redefinition",
            scenario=(
                "Carol stood at the notice-post where she had earlier "
                "written x on the board with 1 sheep's count beneath it. "
                "Tom arrived with new count: 99 sheep had appeared at the "
                "fold that morning."
            ),
            need=(
                "The village morning count was wrong. Carol needed to "
                "revise the posted notice at the crossroads so all "
                "shepherds would see the correct total, not yesterday's "
                "guess."
            ),
            mapping=(
                "`def` can post a name more than once — the second "
                "`def x 99` overwrites the first `def x 1` at the same "
                "notice-post. When x is read, the newest posted value "
                "returns."
            ),
            resolution=(
                "the notice-post returned 99, the revision Carol had chalked, and the day's tally stood corrected. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand."
            )),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_03 = SubjectCurriculum(grade=3, subject_id="G3-03",
    subject_title="let — local binding", fable="boy-wolf",
    examples=[
        _ex("(let [x 3] (+ x 1))", 4, "the expression (let [x 3] (+ x 1))",
            "the result of (let [x 3] (+ x 1))",
            scenario=(
                "Carol the elder had been counting along a stretch of "
                "fence-line at dawn. She slipped a tally-token worth 3 "
                "lambs into the small leather belt-pouch at her hip and "
                "gave the pouch's contents the local name x for that "
                "stretch of watch."
            ),
            need=(
                "By the next fence-post she would want the running total "
                "— what x plus one more lamb came to. Past that post, "
                "the pouch would empty and x would mean nothing again."
            ),
            mapping=(
                "`let` binds a value into a pouch named locally for the "
                "stretch of one form. Inside `(+ x 1)`, x means 3; "
                "outside the form, x is empty and unknown again. The "
                "binding is in force only for the form's stretch."
            ),
            resolution=(
                'the pouch yielded 3, the +1 added a fourth lamb, and the running total stood at 4 — exactly what the next fence-post called for. Tom chalked {drawn.a} on the meadow folk notice, and the morning record stood for the next shepherd to read.'           )),
        _ex("(let [n 10] (* n n))", 100, "the expression (let [n 10] (* n n))",
            "the square of n where n is bound to 10",
            scenario=(
                "Tom had just counted 10 stones for a marker wall, and he "
                "wanted to know how many stones would fill a perfect square "
                "patch. He reached for a tally-token and turned to Carol."
            ),
            need=(
                "The square count was needed for the morning's fold repair, "
                "but only for this one patch — not a general rule the "
                "village would keep on file."
            ),
            mapping=(
                "The `let` binds n to 10 in the pouch, then inside the "
                "expression `(* n n)`, n means 10 — so n multiplies by "
                "itself to yield the square. Once the pouch empties, n is "
                "forgotten."
            ),
            resolution=(
                'the pouch held 10, the multiplication yielded 100, and Tom knew exactly how many stones to gather for his perfect square. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'
            )),
        _ex("(let [a 5] a)", 5, "the expression (let [a 5] a)",
            "the value of (let [a 5] a)",
            scenario=(
                "Carol had slipped a tally-token worth 5 lambs into the "
                "belt-pouch as she reached the first fence-post of the "
                "morning walk. She looked at the pouch for just that "
                "stretch."
            ),
            need=(
                "The count needed to be named for the immediate task — "
                "verifying the flock's head-count at that single post — "
                "but no further naming was needed."
            ),
            mapping=(
                "The `let [a 5]` places 5 in the pouch named a. The body "
                "`a` simply asks for what the pouch holds. The answer is "
                "5, and that is what the whole form returns."
            ),
            resolution=(
                "the pouch yielded the result, the count matched Carol's tally, and the fence-post record stood correct. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then."
            )),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_04 = SubjectCurriculum(grade=3, subject_id="G3-04",
    subject_title="let — multi-binding", fable="boy-wolf",
    examples=[
        _ex("(let [a 1 b 2] (+ a b))", 3,
            "the form with two bindings",
            "the result of (let [a 1 b 2] (+ a b))",
            scenario=(
                "Carol the elder had watched two separate morning counts: "
                "1 lamb at the upper pasture, 2 at the lower fold. She "
                "slipped both tally-tokens into her belt-pouch at once."
            ),
            need=(
                "The village wanted the combined morning count for the "
                "daily roster, but only for this stretch of watch — no "
                "standing rule needed."
            ),
            mapping=(
                "A `let` can bind many names in the pouch at once. Here, "
                "a holds 1 and b holds 2 together, both available inside "
                "the addition. The sum of both pouch-contents is 3."
            ),
            resolution=(
                "the pouch held both counts, the add combined them, and Carol had the day's total ready for the notice-post. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement."
            )),
        _ex("(let [x 5 y 3] (- x y))", 2,
            "the expression (let [x 5 y 3] (- x y))",
            "the result of (- x y) when x=5, y=3",
            scenario=(
                "Tom had marked 5 wool-bundles for the market in the fold "
                "this morning. By noon, 3 had been claimed by shepherds "
                "passing through."
            ),
            need=(
                "He needed the remaining count for the market-roll today, "
                "but the calculation was one-time only — no recipe to post "
                "on the wall."
            ),
            mapping=(
                "The `let` binds x to 5 and y to 3 in the pouch at the "
                "same moment. Inside the subtraction, x and y mean their "
                "pouch-values: 5 minus 3 leaves 2."
            ),
            resolution=(
                "the pouch held both, the math found the remainder, and Tom wrote the unsold count on the day's tally. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear."
            )),
        _ex("(let [a 2 b 3 c 4] (+ a b c))", 9,
            "a let with three bindings",
            "the sum of a, b, c when a=2, b=3, c=4",
            scenario=(
                "Carol had counted wool from three different shearing "
                "stations: 2 fleeces from the north pasture, 3 from the "
                "east fold, 4 from the townsfolk pens."
            ),
            need=(
                "The morning's inventory required all {drawn.b} counts summed for the leather-bound log, but only for the day's entry — no standing rule."
            ),
            mapping=(
                "The `let` places a, b, and c into the pouch together: 2, "
                "3, and 4 respectively. The addition sums all three at once "
                "inside the form, returning their total."
            ),
            resolution=(
                "the pouch held all {drawn.b} counts, the addition combined them all, and the morning's fleece-tally was recorded in the elder's hand. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record."
            )),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_05 = SubjectCurriculum(grade=3, subject_id="G3-05",
    subject_title="let — shadowing outer def", fable="boy-wolf",
    examples=[
        _ex("(do (def x 10) (let [x 99] x))", 99,
            "an inner let shadowing the outer def",
            "the inner-let value of x",
            scenario=(
                "Carol had posted x on the valley notice-post at 10 sheep "
                "for the week's standing count. But Tom came running that "
                "afternoon with a second flock of 99 strays at the fold, "
                "only for today."
            ),
            need=(
                "The strays' count needed a local name x just for that one "
                "calculation, and Tom didn't want to rewrite the posted "
                "notice at the crossroads."
            ),
            mapping=(
                "The posted x on the notice means 10 globally. But `let [x "
                "99]` opens a local pouch that hides the posted x for just "
                "that stretch. Inside the pouch, x means 99; the `let` "
                "body reads 99."
            ),
            resolution=(
                'the pouch held 99, the local x returned that value, and the temporary count was settled without touching the posted notice. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
        _ex("(do (def x 10) (let [x 99] x) x)", 10,
            "the outer x after the inner let returns",
            "the outer x after the let scope ends",
            scenario=(
                "After Carol settled Tom's afternoon count of 99 strays in "
                "the pouch, the day's work moved on. By evening, she needed "
                "the week's standing count again — the one posted at the "
                "notice-post."
            ),
            need=(
                "The temporary pouch for the strays was gone, and Carol "
                "needed to read the posted notice again for the evening "
                "tally."
            ),
            mapping=(
                "The `let [x 99] x` opens and closes locally. After the "
                "`let` form finishes, the pouch empties completely. The "
                "final x reads from the posted notice again, returning the "
                "original 10."
            ),
            resolution=(
                "the let's pouch had released its contents, the posted notice returned 10, and the week's count stood as it was posted. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand."
            )),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_06 = SubjectCurriculum(grade=3, subject_id="G3-06",
    subject_title="let — binding can reference prior", fable="boy-wolf",
    examples=[
        _ex("(let [a 5 b (* a 2)] b)", 10,
            "a let where b uses a",
            "the value of b when a=5 and b is (* a 2)",
            scenario=(
                "Carol had counted 5 morning lambs in the upper pasture. Tom "
                "asked: what if we double that count for the afternoon fold "
                "calculations?"
            ),
            need=(
                "Tom needed the doubled count for one specific task, but that "
                "second count depended on what the first pouch-token held."
            ),
            mapping=(
                "The `let` binds a to 5 first. Then b is also bound — but b's "
                "value `(* a 2)` *reads* from the pouch's a-slot, finding 5, "
                "and doubles it. So b becomes 10 inside the pouch."
            ),
            resolution=(
                'the pouch let a settle to 5, then used a to compute b as 10, and the doubled count was ready for the afternoon ledger. Tom chalked {drawn.a} on the village notice, and the morning record stood for the next shepherd to read.'
            )),
        _ex("(let [a 3 b (+ a 1) c (* b 2)] c)", 8,
            "a let with sequential bindings",
            "the result of the chained binding c",
            scenario=(
                "Carol had counted 3 morning strays and wanted the count doubled after adding one."
            ),
            need=(
                "Each calculation depended on the last, so Carol needed all steps in one form."
            ),
            mapping=(
                "The `let` binds a to 3, then b to `(+ a 1)`, then c to `(* b 2)`. Each reads what came before."
            ),
            resolution=(
                'All bindings settled, and the final tally was ready. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'
            )),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_07 = SubjectCurriculum(grade=3, subject_id="G3-07",
    subject_title="fn — anonymous function", fable="boy-wolf",
    examples=[
        _ex("((fn [x] (+ x 1)) 4)", 5,
            "an anonymous function applied to 4",
            "the result of applying (fn [x] (+ x 1)) to 4",
            scenario=(
                "On the watchhouse wall, Carol the elder had pinned a "
                "small drill-card with no name at the top — just the "
                "steps for what to do once an unnamed quantity arrived. "
                "Tom waited beside her with 4 strays the south flock had "
                "produced that morning."
            ),
            need=(
                "The strays needed to be added to the running tally, "
                "but the watchhouse wanted a one-shot routine for it — no "
                "name to remember, no card to file, just the steps run "
                "this once."
            ),
            mapping=(
                "An anonymous `fn` is exactly that: a drill-card with no "
                "posted name. It takes the quantity (the parameter), runs "
                "the listed step, and serves whatever the last step "
                "produces. The 4 strays go in; the routine adds one for "
                "the count adjustment."
            ),
            resolution=(
                'the card ran end-to-end and returned the result — the adjusted count Carol would carry to the slate, no naming needed.'
            )),
        _ex("((fn [a b] (* a b)) 3 4)", 12,
            "a two-arg anonymous function",
            "the result of applying (fn [a b] (* a b)) to 3 and 4",
            scenario=(
                "Tom had 3 bundles of wool and 4 shepherds needing distribution."
            ),
            need=(
                "A one-time multiplication was needed on the spot."
            ),
            mapping=(
                "An anonymous `fn` with two parameters multiplies them when called."
            ),
            resolution=(
                'The unnamed drill-card multiplied the two numbers and returned the product.'
            )),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_08 = SubjectCurriculum(grade=3, subject_id="G3-08",
    subject_title="fn — multi-arg", fable="boy-wolf",
    examples=[
        _ex("((fn [a b c] (+ a b c)) 1 2 3)", 6,
            "a three-arg anonymous function",
            "the sum of a, b, c",
            scenario=(
                "Carol had three counts from the morning's fence-walk."
            ),
            need=(
                "She needed the sum quickly for today's ledger."
            ),
            mapping=(
                "An anonymous `fn` can take three parameters and add them together."
            ),
            resolution=(
                'The unnamed drill-card summed all counts and returned the total (with `1` as the input value) (with `3` as the input value).'
            )),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_09 = SubjectCurriculum(grade=3, subject_id="G3-09",
    subject_title="defn — shorthand", fable="boy-wolf",
    examples=[
        _ex("(do (defn dbl [x] (* x 2)) (dbl 5))", 10,
            "a defn that doubles its argument",
            "the doubled value (dbl 5)",
            scenario=(
                "Carol had a routine task: shepherds brought her counts, and "
                "she needed the doubled number ready for the fold ledger. "
                "She decided to post a named drill-card at the watchhouse "
                "wall."
            ),
            need=(
                "The village would reuse this doubling many times, so it "
                "deserved a posted name on the watchhouse wall — not an "
                "anonymous card."
            ),
            mapping=(
                "`defn` posts a named drill-card on the watchhouse wall. "
                "The name is `dbl`, and it doubles its argument."
            ),
            resolution=(
                'The posted drill-card `dbl` was ready. When 5 arrived, Carol ran it and got the doubled count. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'
            )),
        _ex("(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))", 6,
            "a defn with three args",
            "the result of (add3 1 2 3)",
            scenario=(
                "Carol noticed shepherds constantly asking her to sum three "
                "separate counts — north, east, and fold — all morning. She "
                "decided to post a standing drill-card."
            ),
            need=(
                'A named routine would save time. The village could call `add3` whenever {drawn.c} counts needed summing, without Carol doing the addition by hand each time.'
            ),
            mapping=(
                "`defn add3` posts a named drill-card for adding three "
                "quantities. When 1, 2, and 3 are passed, it sums them: "
                "1 plus 2 plus 3."
            ),
            resolution=(
                "the posted drill-card `add3` served the {drawn.c} counts, returned 6, and the morning's three-gate total was recorded efficiently. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement."
            )),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_10 = SubjectCurriculum(grade=3, subject_id="G3-10",
    subject_title="anonymous shorthand #()", fable="boy-wolf",
    examples=[
        _ex("(#(+ % 1) 5)", 6,
            "the shorthand #(+ % 1) applied to 5",
            "the result of (#(+ % 1) 5)",
            scenario=(
                "Tom handed Carol a count of 5 sheep, and Carol needed to add "
                "one more to it for the fold's requirement. She wanted a "
                "quick shorthand for the addition."
            ),
            need=(
                "The add-one operation was so brief, Carol didn't want to post "
                "a full drill-card — just shorthand notation she could use "
                "once."
            ),
            mapping=(
                "The `#(+ % 1)` shorthand is a reader-macro card: `%` stands "
                "for 'whatever comes in.' When 5 arrives, `%` becomes 5, and "
                "the shorthand adds 1."
            ),
            resolution=(
                'the shorthand card took the 5, added 1, and returned 6 — exactly what the fold needed.'
            )),
        _ex("(#(* %1 %2) 3 4)", 12,
            "the shorthand #(* %1 %2) applied to 3 and 4",
            "the result of (#(* %1 %2) 3 4)",
            scenario=(
                "Carol had 3 wool-pens and 4 fleeces in each. She needed the "
                "total fleeces, but the multiplication was a one-off for the "
                "day's task."
            ),
            need=(
                "Rather than post a full named drill-card, Carol used a short "
                "reader-notation: `%1` for first, `%2` for second argument, "
                "multiply them."
            ),
            mapping=(
                "The `#(* %1 %2)` shorthand takes two arguments and multiplies them."
            ),
            resolution=(
                'The shorthand multiplied the pens and fleeces, returning the total count.'
            )),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_11 = SubjectCurriculum(grade=3, subject_id="G3-11",
    subject_title="Substitution rule", fable="boy-wolf",
    examples=[
        _ex("(let [a 7] (+ a a))", 14,
            "the let where a is referenced twice",
            "the result of (+ a a) when a=7",
            scenario=(
                "Carol had counted 7 morning strays. Then Tom asked: what if "
                "we combine the morning count with the morning count again "
                "for the fold-doubling?"
            ),
            need=(
                "Tom needed to see the pouch-token used twice — the same "
                "value substituted into both slots of the addition."
            ),
            mapping=(
                "The `let [a 7]` puts 7 in the pouch named a. Inside `(+ a a)`, "
                "every `a` substitutes to 7, and both get added together."
            ),
            resolution=(
                'The pouch held the value, it was substituted in both slots, and the addition yielded the doubled count. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'
            )),
        _ex("((fn [x] (* x x)) 6)", 36,
            "applying square to 6",
            "the square of 6",
            scenario=(
                "Carol had a square pen with side-length 6 stone-marks. She "
                "wanted to know how many stone-units would fill it, so she "
                "asked for the square of the length."
            ),
            need=(
                "Multiplying 6 by 6 was the test — would the drill-card "
                "substitute the parameter correctly in both positions?"
            ),
            mapping=(
                "The anonymous `fn [x]` takes a parameter. Inside `(* x x)`, "
                "both `x`s are substituted with the same value."
            ),
            resolution=(
                'The parameter substituted into both slots, the multiplication computed the square, and Carol had the answer.'
            )),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_12 = SubjectCurriculum(grade=3, subject_id="G3-12",
    subject_title="Scope vs namespace", fable="boy-wolf",
    examples=[
        _ex("(do (def g 5) (let [g 99] (+ g 1)))", 100,
            "an inner let masking the outer def g",
            "the value computed inside the inner scope",
            scenario=(
                "Carol had posted g on the notice-post at 5 sheep for the "
                "week's standing. That afternoon, Tom came with 99 strays, "
                "and Carol needed to add one to that count for the fold ledger."
            ),
            need=(
                "Tom's temporary count needed to hide the posted g for just "
                "that calculation. Once the addition was done, the posted g "
                "would remain unchanged."
            ),
            mapping=(
                "The posted `def g 5` sits on the notice-post. The `let [g 99]` "
                "opens a pouch that shadows the posted name, making local g "
                "mean 99. Inside the let, `(+ g 1)` adds 1 to the pouch's "
                "99, giving 100."
            ),
            resolution=(
                "the pouch shadowed the posted name, the local g plus one gave 100, and the afternoon's calculation was complete without changing the posted notice. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record."
            )),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_13 = SubjectCurriculum(grade=3, subject_id="G3-13",
    subject_title="fn body returns last form", fable="boy-wolf",
    examples=[
        _ex("((fn [x] x x x 99) 1)", 99,
            "a fn whose body has multiple forms; only the last is returned",
            "the value of a fn body that ends with 99",
            scenario=(
                "Carol had written a drill-card with three steps: read x, "
                "read x again, read x a third time. But then she realized "
                "the final step should return 99 instead."
            ),
            need=(
                "Tom asked: if the drill-card lists many steps, which one does "
                "the meadow folk get? Only the last step's answer matters to the "
                "caller."
            ),
            mapping=(
                "A `fn` body can have many forms. The drill-card reads x three "
                "times, but the REPL only returns the final form's value. "
                "Here, the last form is 99, so 99 is what the caller gets."
            ),
            resolution=(
                'the drill-card ran all its steps, but returned only the last one — 99 — and that was the answer Carol posted for the townsfolk.'
            )),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_14 = SubjectCurriculum(grade=3, subject_id="G3-14",
    subject_title="do form", fable="boy-wolf",
    examples=[
        _ex("(do 1 2 3)", 3,
            "the do form (do 1 2 3)",
            "the value of (do 1 2 3)",
            scenario=(
                "Carol had written three numbers on her slate in a column: 1, "
                "then 2, then 3. She asked Tom: if I read this whole sequence, "
                "what comes back?"
            ),
            need=(
                "Tom needed to learn that `do` groups forms together, but only "
                "the last one's answer is what the village hears."
            ),
            mapping=(
                "The `do` form groups multiple forms. The runtime reads 1, then "
                "2, then 3 in sequence. But only the final value comes back: 3."
            ),
            resolution=(
                "the do form ran all three, returned 3, and Tom learned the rule for sequences. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last."
            )),
        _ex("(do (+ 1 1) (+ 2 2) (+ 3 3))", 6,
            "a do with three forms",
            "the value of (do (+ 1 1) (+ 2 2) (+ 3 3))",
            scenario=(
                "Carol had three arithmetic tasks to record in the slate: add "
                "1 and 1, add 2 and 2, add 3 and 3. She wanted all three "
                "written and answered."
            ),
            need=(
                "The village wanted the final answer (3 plus 3) after all "
                "three calculations ran, not the intermediate results."
            ),
            mapping=(
                "The `do` form chains the three additions. The REPL runs all "
                "three forms in order: 2, then 4, then 6. Only the last "
                "value, 6, is returned."
            ),
            resolution=(
                'the do form ran all three additions, returned 6 from the final one, and Carol had the complete sequence recorded with the answer ready. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'
            )),
    ], subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_15 = SubjectCurriculum(grade=3, subject_id="G3-15",
    subject_title="Side-effects in body", fable="boy-wolf",
    examples=[
        _ex("(do (println \"hi\") 42)", 42,
            "the expression (do (println \"hi\") 42)",
            "the return value of the do",
            scenario=(
                "Carol stood at the watchhouse and Tom came running. Carol "
                "wanted to print a greeting message to Tom but also return a "
                "count of 42 for the day's tally."
            ),
            need=(
                "The `println` would show the greeting, but what would the "
                "REPL return — the greeting or the count? The village needed "
                "to know."
            ),
            mapping=(
                "The `do` runs `println` first — that prints \"hi\" as a "
                "side-effect. Then the REPL evaluates 42. Side-effects happen, "
                "but only the last form's value is returned."
            ),
            resolution=(
                "the do printed the greeting, then returned 42, and Tom knew the rule: side-effects do their work, but the final value is the return. Tom chalked {drawn.a} on the meadow folk notice, and the morning record stood for the next shepherd to read."
            )),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_16 = SubjectCurriculum(grade=3, subject_id="G3-16",
    subject_title="Name collision: namespace vs let", fable="boy-wolf",
    examples=[
        _ex("(let [+ 99] +)", 99,
            "a let that shadows the + function",
            "the value bound to the (locally shadowed) +",
            scenario=(
                "Carol had the addition function `+` posted at the notice, "
                "used by every shepherd. But Tom placed a tally-token worth "
                "99 in his belt-pouch and labeled it `+` for this one stretch "
                "of fence."
            ),
            need=(
                "Tom wanted to know: if I name my pouch-token the same name "
                "as the posted function, which one does my local use return — "
                "the function or my token?"
            ),
            mapping=(
                "The `let` shadows the posted name: inside the pouch, `+` "
                "means the token's value 99, not the function. When the form "
                "reads `+`, it finds the pouch-value first."
            ),
            resolution=(
                "the pouch's `+` shadowed the posted function, returning 99, and Tom learned that local names hide posted ones. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain."
            )),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_17 = SubjectCurriculum(grade=3, subject_id="G3-17",
    subject_title="Naming conventions (kebab-case)", fable="boy-wolf",
    examples=[
        _ex("(let [flock-size 8 stray-count 2] (- flock-size stray-count))", 6,
            "a let with kebab-case names",
            "the difference of the two counts",
            scenario=(
                "Carol had two separate counts to track: the main flock at 8 "
                "sheep, and the strays that had wandered in at 2. She wanted "
                "clear names in the pouch that showed what each count meant."
            ),
            need=(
                "The village's naming convention used dashes to join words — "
                "`flock-size` and `stray-count` were clearer than single-word "
                "abbreviations."
            ),
            mapping=(
                "Kebab-case names with dashes are the valley standard. The "
                "`let` binds `flock-size` to 8 and `stray-count` to 2. The "
                "subtraction finds the difference between them."
            ),
            resolution=(
                'the pouch held both clearly named counts, the math found the difference, and the naming convention kept the ledger readable. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'
            )),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_18 = SubjectCurriculum(grade=3, subject_id="G3-18",
    subject_title="When to name vs inline", fable="boy-wolf",
    examples=[
        _ex("(let [n 5] (* n n n))", 125,
            "naming n once and using it three times",
            "n cubed where n=5",
            scenario=(
                "Carol had a count of 5 and needed to multiply it by itself "
                "three times — once for each pasture's volume calculation. "
                "She wanted to name the count once and reuse it."
            ),
            need=(
                "Writing 5 three times risked copying errors. Better to bind "
                "it once in the pouch and reference the name three times."
            ),
            mapping=(
                "The `let` binds n once. Inside `(* n n n)`, the name is used "
                "three times, and the REPL substitutes the value each time."
            ),
            resolution=(
                'The pouch held the value, the name was used three times, and the multiplication gave the cubic result. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'
            )),
        _ex("(* 5 5 5)", 125,
            "the inline form (* 5 5 5)",
            "5 cubed (without binding)",
            scenario=(
                "The village's market was closing at noon, and Carol needed "
                "5 cubed instantly for the wool-tax calculation — no time to "
                "set up a pouch."
            ),
            need=(
                "Sometimes the value is short enough that writing it inline "
                "directly is clearer and faster than naming it."
            ),
            mapping=(
                "The inline form `(* 5 5 5)` multiplies the literal 5 by "
                "itself three times directly. No pouch, no binding, just the "
                "numbers in place."
            ),
            resolution=(
                'the inline multiplication gave 125 — same answer as the named version, but faster for this quick calculation. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'           )),
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
    print(f"grade-3 boy-wolf smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
