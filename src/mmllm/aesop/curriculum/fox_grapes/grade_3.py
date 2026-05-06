"""Grade 3 — naming, scope, substitution. Through fox-grapes.

The fable lens: the patient fox keeps a leather notebook of named
values, every binding written down before it is referenced. The hasty
fox prefers to declare what a name "obviously" stands for and skip
the substitution step entirely — the same rationalize-instead-of-look
move that calls the cluster sour without tasting it. Naming, scope,
and substitution are the disciplines that close that gap: write the
binding, let the REPL substitute, read the result.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.fox_grapes.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.fox_grapes._metaphor_pools import _POUCH_SUBPLOTS, _RECIPE_SUBPLOTS, _ROADSIGN_SUBPLOTS, _SCRIBE_SUBPLOTS

# Add naming-themed subplots: a character names a value, then references it.
_NAMING_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [
    SubplotTemplate("""\
{patient_fox_phrase} kept a small leather notebook {place} where every
meaningful quantity got its own name. {patient_fox_he_she_cap} pointed
to today's entry: {concept_phrase}. The form {form_display} would
settle it once {hasty_fox_phrase} agreed to look at the binding."""),

    SubplotTemplate("""\
"You can call it whatever you like," {patient_fox} said {place}, "but
the form is what matters." {patient_fox_he_she_cap} drew the binding
for {hasty_fox_phrase}: the form {form_display} captured
{concept_phrase}, and the REPL would do the rest."""),
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


_PLAN_POOL_G3 = _PLAN_POOL + (
    "I bind the inputs in a let, then compute.",
    "I name the values first and then combine them.",
    "I write the let-form so the REPL can substitute.",
)


G3_01 = SubjectCurriculum(grade=3, subject_id="G3-01",
    subject_title="def — top-level binding", fable="fox-grapes",
    examples=[
        _ex("(do (def x 42) x)",
            42,
            'a top-level def followed by a read of the bound symbol',
            "the value the post's nameplate yields when read",
            goal='declare a top-level binding x to a value, then read x',
            scenario='Renard the fox chalked a fresh nameplate onto a vine-post at the head of the row. The post now read x, and behind the post sat the value the post named — a single tally Renard had counted out for the day.',
            need="He wanted to look up the post's name later in the row and read off whatever value the post stood for, without re-counting the tally itself.",
            mapping='A `def` form posts a nameplate — a top-level binding from a symbol to a value, persistent across the orchard. After the binding is posted, the symbol means the value anywhere in the namespace. Reading the symbol later just looks at the post.',
            resolution="the post's nameplate yielded back the value Renard had chalked there — the same tally any fox in the orchard could read off.",
            tags=("story",)),
        _ex("(do (def y 7) y)",
            7,
            'a top-level def of seven, then a read of that symbol',
            'the value the vine-post for y yields',
            goal='chalk a nameplate for y pointing to the value seven, then read it back',
            scenario='Vix the fox scratched the nameplate y onto a vine-post at the orchard edge. The post marked a boundary — seven grapes hung on the cluster just behind it, and the post would remember that count.',
            need='Later, when Vix returned to that boundary-post, she wanted to recall the tally without counting the cluster again. She looked at the post and read its nameplate.',
            mapping='A `def` chalks a symbol onto a permanent post; the symbol then stands for the value anywhere the post can be seen. Reading the post-name is like looking at what was written there.',
            resolution='the post yielded back the seven-count Vix had named it for — the value persisted on the vine-post until another fox rewrote it.',
            tags=("story",)),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_02 = SubjectCurriculum(grade=3, subject_id="G3-02",
    subject_title="def — redefinition", fable="fox-grapes",
    examples=[
        _ex("(do (def x 1) (def x 99) x)",
            99,
            'a top-level def of one, then a def of ninety-nine to the same symbol, then a read',
            'the value the vine-post for x yields after redefinition',
            goal='first chalk x to point to one, then chalk it again to point to ninety-nine, then read',
            scenario='Sly the fox found an old vine-post nameplate reading x. It still pointed to a single grape. Sly took a chalk stone and crossed out the old tally, then scratched a new mark — ninety-nine grapes — below it on the same post.',
            need='When Sly looked at the post again to see what x meant, the post carried only the latest scratching. The post had been rewritten.',
            mapping='A `def` to the same symbol replaces the old nameplate. The post stays in place, but its value changes. Reading the post always yields the most recent value chalked there.',
            resolution='the post showed the second tally — ninety-nine — because the most recent `def` had rewritten what the symbol named.',
            tags=("story",)),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_03 = SubjectCurriculum(grade=3, subject_id="G3-03",
    subject_title="let — local binding", fable="fox-grapes",
    examples=[
        _ex("(let [x 3] (+ x 1))",
            4,
            'the let-bound increment by one',
            "the running total after the pouch's value is incremented by one",
            goal='bind a value of 3 to a local name x, then return that value plus 1',
            scenario="Renard the fox tucked three grapes into the small berry-pouch tied at his belt and gave the pouch's contents the local name x. The pouch sat between trellis and basket — in his belt only for one short stretch of orchard path.",
            need='Just before he reached the basket, Renard wanted the running total — what x plus one more grape would come to. Once he tipped the pouch into the basket, x would empty again.',
            mapping="`let` ties a value into a pouch named locally for the stretch of one form. Inside the form, the local name stands for the pouch's value; outside the form, the pouch is empty and the name is unknown again. The binding is in force only for the form's stretch.",
            resolution='the pouch yielded its three grapes, the increment added one more, and the total stood at one beyond what the pouch had held — exactly the haul the basket would receive.',
            tags=("story",)),
        _ex("(let [n 10] (* n n))",
            100,
            'a local binding of ten to n, then computing n times n',
            'the value when a ten-cluster is squared',
            goal='bind a value of ten to a local name n, then compute the product of n and n',
            scenario='Vix the fox scooped ten grapes into her berry-pouch and named them n. She held the pouch steady and asked: what if I multiplied this group by itself? The pouch sat in her paws, a temporary anchor for the multiplication.',
            need='Vix needed to take the ten-count, duplicate it, and find what two tens made together. The pouch held the binding only for the stretch of that one question.',
            mapping='`let` gathers a value into a local pouch named only for the current form. The binding works inside, but outside the form, the name and pouch both empty.',
            resolution='ten times ten came to a hundred — the full tally Vix held when she squeezed both copies of the pouch-count together.',
            tags=("story",)),
        _ex("(let [a 5] a)",
            5,
            'a local binding of five to a, then a read of a',
            'the value in the berry-pouch after binding',
            goal='bind a value of five to a local name a, then read that name back',
            scenario='Sly the fox placed five grapes into a small pouch and called it a. She held the pouch at her side and looked at what she had bound. That was all she needed to know for this moment.',
            need='Sly wanted to see the pouch's contents without unpacking it. The binding a stood for the five grapes she had tucked inside.',
            mapping='`let` binds a value to a local name; reading the name inside the form just gives back what was tied there.',
            resolution='the pouch yielded its five grapes — the binding held its shape and value for the form's duration.',
            tags=("story",)),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_04 = SubjectCurriculum(grade=3, subject_id="G3-04",
    subject_title="let — multi-binding", fable="fox-grapes",
    examples=[
        _ex("(let [a 1 b 2] (+ a b))",
            3,
            'a let binding one to a and two to b, then adding them',
            'the sum when one and two are bound and added',
            goal='bind one to a and two to b, then add a and b',
            scenario='Renard the fox laid out a berry-pouch at his left: one grape, named a. Then at his right: another pouch with two grapes, named b. He held both pouches in his paws and asked how many grapes if he combined the counts.',
            need='Renard needed to gather both local bindings together and add them without moving the pouches.',
            mapping='`let` can bind many values with local names in one form. Each name holds its binding, and all names are available inside the same form.',
            resolution='the left pouch held its single grape, the right pouch held its pair, and combined they made a total of three.',
            tags=("story",)),
        _ex("(let [x 5 y 3] (- x y))",
            2,
            'a let binding five to x and three to y, then subtracting',
            'the difference when five is bound and three is subtracted from it',
            goal='bind five to x and three to y, then compute x minus y',
            scenario='Vix the fox filled one pouch with five grapes called x, another with three grapes called y. She held both and wondered: how many remain if I take away the smaller group from the larger?',
            need='Vix needed to see the gap between the two pouches without spilling either one.',
            mapping='Multiple local bindings in one `let` form can be used together in any operation. Each binding is in scope for the entire body.',
            resolution='five minus three left a difference of two — the surplus when the smaller count was taken away.',
            tags=("story",)),
        _ex("(let [a 2 b 3 c 4] (+ a b c))",
            9,
            'a let binding two, three, and four to a, b, c, then summing them',
            'the total when three pouches are combined',
            goal='bind two to a, three to b, four to c, then add all three',
            scenario='Sly the fox arranged three berry-pouches: a with two grapes, b with three, c with four. She lined them up on the ground and asked what the grand total would be if she poured all three together.',
            need='Sly wanted a single sum from three separate pouches, each with its own local name.',
            mapping='`let` can bind as many values as needed; all bindings are available for the same operation inside the form.',
            resolution='two plus three plus four made nine grapes in total — the full count when all three pouches emptied into one pile.',
            tags=("story",)),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_05 = SubjectCurriculum(grade=3, subject_id="G3-05",
    subject_title="let — shadowing outer def", fable="fox-grapes",
    examples=[
        _ex("(do (def x 10) (let [x 99] x))",
            99,
            'a def of x to ten, then a let binding x to ninety-nine, then reading x inside the let',
            'the value when x is shadowed by the let binding',
            goal='def x to ten, then inside a let binding x to ninety-nine, read the local x',
            scenario='Renard chalked a vine-post nameplate for x pointing to ten grapes. Later, as he walked that stretch of orchard, he tucked ninety-nine grapes into a temporary pouch and also called it x. While holding the pouch, he looked at what x meant — not the post, but his own hands.',
            need='Inside the pouch-stretch, the local x shadowed the vine-post. Renard needed to know which x he was reading.',
            mapping='A `let` binding shadows an outer `def` binding with the same name. Inside the let, the local name wins. Outside the let, the outer name is visible again.',
            resolution='inside the let, x meant ninety-nine from the pouch, not ten from the vine-post. The local binding took precedence.',
            tags=("story",)),
        _ex("(do (def x 10) (let [x 99] x) x)",
            10,
            'a def of x to ten, a let binding x to ninety-nine and reading it, then reading x outside the let',
            'the value when x is read after the let scope closes',
            goal='def x to ten, shadow it with let-binding ninety-nine, read inside, then read outside',
            scenario='Vix chalked a vine-post for x marking ten grapes. Walking onward, she tucked ninety-nine into a pouch also called x, looked at it once, then set the pouch down. When she looked back at the path behind her, the pouch was gone — only the vine-post remained.',
            need='The pouch binding was temporary. Once the let-form closed, x returned to the post.',
            mapping='After a `let` form ends, the local binding dissolves. The name reverts to its outer binding. Scope defines which binding is in force.',
            resolution='inside the let, x was ninety-nine. Outside, x meant ten again from the vine-post.',
            tags=("story",)),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_06 = SubjectCurriculum(grade=3, subject_id="G3-06",
    subject_title="let — binding can reference prior", fable="fox-grapes",
    examples=[
        _ex("(let [a 5 b (* a 2)] b)",
            10,
            'a let binding five to a, then b to a doubled, then reading b',
            'the value when a later binding references an earlier one',
            goal='bind five to a, then bind a times two to b, then read b',
            scenario='Sly the fox placed five grapes into pouch a. Next, she took the contents of a, doubled them, and tucked that count into pouch b. Both pouches sat on the ground, each with its binding, but b depended on a.',
            need='The second binding could use the first binding. Once a was in hand, Sly could reference a when creating b.',
            mapping='Inside a `let`, later bindings can reference earlier ones. The earlier binding is in scope for the later one.',
            resolution='five grapes in a meant ten when doubled and placed in b. The dependency worked: b held what a had yielded times two.',
            tags=("story",)),
        _ex("(let [a 3 b (+ a 1) c (* b 2)] c)",
            8,
            'a let binding three to a, one-plus-a to b, b-times-two to c, then reading c',
            'the value when a chain of dependencies unfolds',
            goal='bind three to a, one plus a to b, two times b to c, then read c',
            scenario='Renard set up three pouches in sequence. Pouch a held three grapes. Pouch b took what a held and added one more. Pouch c took what b held and doubled it. Each pouch depended on the one before.',
            need='A chain of local bindings let each one build on the previous. Renard needed to follow the chain.',
            mapping='`let` bindings form a chain: each can reference any binding earlier in the list. The order matters.',
            resolution='three in a became four in b, then eight in c when doubled. The dependency chain worked through all three bindings.',
            tags=("story",)),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_07 = SubjectCurriculum(grade=3, subject_id="G3-07",
    subject_title="fn — anonymous function", fable="fox-grapes",
    examples=[
        _ex("((fn [x] (+ x 1)) 4)",
            5,
            'an anonymous tasting-card applied to four',
            'the value the increment-by-one card serves on input four',
            goal='apply an anonymous tasting-card that adds 1 to its argument, with input 4',
            scenario='Sly the fox had pinned a fresh tasting-card to the orchard post: take one cluster, add one. The card had no name of its own — it was meant to be used once, right where it hung.',
            need="Sly fed the card a cluster of four to taste. The card's single step would run on that input and serve back a value — what the routine produced for that one cluster.",
            mapping='An anonymous function is a tasting-card with no posted name. The card lists its parameters, then its steps; calling the card hands an ingredient through the steps and serves the value of the last one. The card is the routine; the call is its execution.',
            resolution="the card's last step served back four-plus-one — the only value the routine had been written to produce for that input.",
            tags=("story",)),
        _ex("((fn [a b] (* a b)) 3 4)",
            12,
            'an unnamed tasting-card taking two ingredients and multiplying them, with inputs three and four',
            'the value when three and four are fed through the multiplication-card',
            goal='call an anonymous function that multiplies two arguments, with inputs three and four',
            scenario='Renard found a tasting-card pinned to the post. The card said: take two clusters, multiply them. He brought three grapes in one hand and four in the other, and ran them both through the card's recipe.',
            need='The card had no posted name, but it worked anyway. The routine took the two inputs and ran them through its step.',
            mapping='An anonymous function lists its parameters and its body. Calling it passes the arguments through the parameters and evaluates the body, returning the last value.',
            resolution='three multiplied by four gave twelve — the card produced its result for those exact two inputs.',
            tags=("story",)),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_08 = SubjectCurriculum(grade=3, subject_id="G3-08",
    subject_title="fn — multi-arg", fable="fox-grapes",
    examples=[
        _ex("((fn [a b c] (+ a b c)) 1 2 3)",
            6,
            'an unnamed tasting-card taking three ingredients and summing them, with inputs one, two, three',
            'the total when three separate counts are run through the addition-card',
            goal='call an anonymous function that adds three arguments, with inputs one, two, three',
            scenario='Vix the fox found a tasting-card pinned to a post. The card said: take three clusters, add them. She brought one grape, then two, then three — each in a separate bunch — and fed all three through the card at once.',
            need='The card could handle three ingredients. Vix needed to see what the card produced when all three were passed in together.',
            mapping='An anonymous function can take any number of parameters. All parameters are available inside the body for computation.',
            resolution='one plus two plus three came to six — the card added all three inputs and served the sum.',
            tags=("story",)),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_09 = SubjectCurriculum(grade=3, subject_id="G3-09",
    subject_title="defn — shorthand", fable="fox-grapes",
    examples=[
        _ex("(do (defn dbl [x] (* x 2)) (dbl 5))",
            10,
            'a named tasting-card called dbl that doubles its input, then calling it with five',
            'the value when a doubling-card is applied to five',
            goal='define a named function dbl that doubles its argument, then call it with five',
            scenario='Sly the fox pinned a named tasting-card to the post and called it dbl. The card said: take one cluster and double it. Later, she brought five grapes and ran them through the dbl card.',
            need='Unlike the unnamed cards, dbl had a posted name so Sly could call it by name. The card ran its doubling step on the five.',
            mapping='`defn` names a function and posts it like a tasting-card recipe on the orchard. After posting, the function can be called by its name with any input.',
            resolution='five grapes doubled made ten. The named card worked: dbl took five and returned ten.',
            tags=("story",)),
        _ex("(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))",
            6,
            'a named tasting-card called add3 that adds three inputs, then calling it with one, two, three',
            'the total when the three-adder card is used',
            goal='define a named function add3 that sums three arguments, then call it with one, two, three',
            scenario='Renard pinned a named tasting-card called add3 to a post. The card said: take three clusters and add them. Later, he approached with one grape, two grapes, and three grapes, and fed all three through the add3 card by name.',
            need='Renard could use the card by its posted name. The card summed the three inputs he gave it.',
            mapping='`defn` posts a named tasting-card. Calling it by name passes the arguments through its parameters and runs the body.',
            resolution='one plus two plus three made six. The named card add3 worked for Renard.',
            tags=("story",)),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_10 = SubjectCurriculum(grade=3, subject_id="G3-10",
    subject_title="anonymous shorthand #()", fable="fox-grapes",
    examples=[
        _ex("(#(+ % 1) 5)",
            6,
            'a short unnamed tasting-card using placeholder %, applied with five',
            'the result when a quick increment-card is used',
            goal='use shorthand syntax to create a function that increments, then apply it to five',
            scenario='Vix the fox scribbled a quick tasting-card on a scrap: just the recipe in shorthand, no name. The recipe said add one to the ingredient. She held up five grapes and fed them through the quick card.',
            need='The shorthand let Vix write the card faster without naming it. The % placeholder stood for whatever she passed in.',
            mapping='The shorthand #() syntax is a quick tasting-card. The % stands for the single argument; the body runs that argument through the steps.',
            resolution='five through the card became six. The shorthand card worked the same as a named one.',
            tags=("story",)),
        _ex("(#(* %1 %2) 3 4)",
            12,
            'a shorthand unnamed card with two placeholders %1 and %2, applied with three and four',
            'the result when shorthand handles two ingredients',
            goal='use shorthand to make a function multiplying two arguments, then apply it with three and four',
            scenario='Sly the fox jotted a shorthand recipe: multiply the first ingredient by the second. No name, just %1 and %2. She brought three grapes and four grapes and ran them through the quick card.',
            need='The shorthand let her write a two-argument card without a full form. %1 and %2 held the two inputs.',
            mapping='Shorthand #() with multiple arguments uses %1, %2, etc. for each parameter. The body runs the arguments through the recipe.',
            resolution='three times four made twelve. The shorthand two-argument card computed the product.',
            tags=("story",)),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_11 = SubjectCurriculum(grade=3, subject_id="G3-11",
    subject_title="Substitution rule", fable="fox-grapes",
    examples=[
        _ex("(let [a 7] (+ a a))",
            14,
            'a let binding seven to a, then adding a to itself',
            'the total when the same binding is used twice',
            goal='bind seven to a, then add a to a',
            scenario='Renard tucked seven grapes into pouch a. Then he added the pouch to itself — the same binding used twice in one sum.',
            need='Renard needed to use the binding a twice without creating a new one. The same seven stood in for both references.',
            mapping='Substitution means replacing the name with its value. Each use of a is replaced by seven, so adding a to a becomes seven plus seven.',
            resolution='seven used twice made fourteen. The substitution rule worked: every mention of a became the seven it held.',
            tags=("story",)),
        _ex("((fn [x] (* x x)) 6)",
            36,
            'an unnamed tasting-card that multiplies its argument by itself, applied with six',
            'the result when the substitution rule applies in a function',
            goal='apply a function that multiplies its argument by itself, with input six',
            scenario='Sly brought a tasting-card that said take the ingredient and multiply it by itself. She passed six grapes in. The card substituted six for every mention of the parameter.',
            need='The parameter x appeared twice in the multiplication. Each time, the same value six was used.',
            mapping='In a function call, the argument is substituted for each use of the parameter. The same value flows through every reference.',
            resolution='six times six made thirty-six. Each x became six, so the multiplication worked.',
            tags=("story",)),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_12 = SubjectCurriculum(grade=3, subject_id="G3-12",
    subject_title="Scope vs namespace", fable="fox-grapes",
    examples=[
        _ex("(do (def g 5) (let [g 99] (+ g 1)))",
            100,
            'a def of g to five, then a let binding g to ninety-nine, then adding one to the let g',
            'the result of the operation in the shadowed scope',
            goal='def g to five, shadow it with let-binding ninety-nine, then increment that local binding',
            scenario='Vix chalked a vine-post nameplate for g showing five grapes. Later, she tucked ninety-nine grapes into a pouch also called g and asked: what if I added one more to what the pouch holds? Inside the pouch-stretch, g meant the pouch, not the post.',
            need='Scope meant which binding was active. While Vix held the pouch, the local g shadowed the vine-post g.',
            mapping='`let` creates a scope where the local binding shadows outer bindings. Inside the let, the local name takes precedence. The namespace (vine-posts) still exists but is hidden by the local scope.',
            resolution='inside the let, g meant ninety-nine from the pouch. Adding one made a hundred. The scope rule meant the let binding won.',
            tags=("story",)),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_13 = SubjectCurriculum(grade=3, subject_id="G3-13",
    subject_title="fn body returns last form", fable="fox-grapes",
    examples=[
        _ex("((fn [x] x x x 99) 1)",
            99,
            'an unnamed card that mentions the parameter three times then returns ninety-nine, applied with one',
            'the value returned by the last form in the card body',
            goal='call a function that takes one, uses it multiple ways, but ends with the constant ninety-nine',
            scenario='Sly found a tasting-card that said: check the ingredient three times, then serve ninety-nine. She passed one through the card. The card ran all the checks, but the only value it served back was ninety-nine — the last step.',
            need='The card could mention the parameter along the way, but what mattered was the final step. The card always served ninety-nine.',
            mapping='A function body can have many forms. The function returns the value of the last form; earlier forms may run but their values are discarded.',
            resolution='the card served ninety-nine — the last form in the body. Even though one was passed in, the final step was what the caller received.',
            tags=("story",)),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_14 = SubjectCurriculum(grade=3, subject_id="G3-14",
    subject_title="do form", fable="fox-grapes",
    examples=[
        _ex("(do 1 2 3)", 3, 'the form', 'the value the form evaluates to'),
        _ex("(do (+ 1 1) (+ 2 2) (+ 3 3))", 6, 'the form', 'the value the form evaluates to'),
    ], subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_15 = SubjectCurriculum(grade=3, subject_id="G3-15",
    subject_title="Side-effects in body", fable="fox-grapes",
    examples=[
        _ex("(do (println \"hi\") 42)", 42, 'the form', 'the value the form evaluates to'),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_16 = SubjectCurriculum(grade=3, subject_id="G3-16",
    subject_title="Name collision: namespace vs let", fable="fox-grapes",
    examples=[
        _ex("(let [+ 99] +)", 99, 'the form', 'the value the form evaluates to'),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_17 = SubjectCurriculum(grade=3, subject_id="G3-17",
    subject_title="Naming conventions (kebab-case)", fable="fox-grapes",
    examples=[
        _ex("(let [hasty-rate 4 patient-rate 1] (- hasty-rate patient-rate))", 3, 'the form', 'the value the form evaluates to'),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_18 = SubjectCurriculum(grade=3, subject_id="G3-18",
    subject_title="When to name vs inline", fable="fox-grapes",
    examples=[
        _ex("(let [n 5] (* n n n))", 125, 'the form', 'the value the form evaluates to'),
        _ex("(* 5 5 5)", 125, 'the form', 'the value the form evaluates to'),
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
    print(f"grade-3 fox-grapes smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
