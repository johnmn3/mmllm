"""Grade 3 — naming, scope, substitution. Through dog-shadow.

The fable lens: the Tortoise's careful approach is exactly the
substitution-rule discipline. The Hare's "I just know the answer"
is what binding-by-name corrects.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.dog_shadow.grade_1 import (
    _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.dog_shadow._metaphor_pools import (
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
    subject_title="def — top-level binding", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(do (def x 42) x)",
            expected=42,
            concept_phrase="the top-level binding and lookup",
            question_what="the value of x after using def to bind x to 42",
            goal_text="bind x to 42 and return it",
            scenario=(
                'Bell the hound chose a flat stone at the bank near the '
                'pond and scratched a fresh name into its surface — x — '
                "pressing the stone's value beside the marker so any later "
                'dog could read it.'
            ),
            need=(
                'She would consult the marker further along and would want '
                'the value the stone now bore — without any guessing about '
                'what x meant. The runtime, reading the bank, would settle '
                'the matter.'
            ),
            mapping=(
                'The marker stone is the def, the name x is the symbol '
                "scratched on the stone, the value is what's pressed beside "
                'it, and reading the marker is what the runtime does '
                'whenever a later form names x.'
            ),
            resolution=(
                'The REPL set the marker, then read it back as the form '
                'directed, handing back the value the stone had recorded. '
                'Any later dog along the bank would see the same name bound '
                'to the same value.'
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
                'Rex the hound discovered a worn stone at the stream\'s edge '
                'and began carving a fresh name into its face — y. "When I '
                'cut a name deep into the marker," he said, pressing the '
                'stone\'s value alongside, "any dog who passes will recognize '
                'it and find what lies beneath."'
            ),
            need=(
                'He would need to prove the marker worked — that walking past '
                'it and calling out the name would return the same value, '
                'without doubt or guessing.'
            ),
            mapping=(
                'The marker stone is the def, the name y is carved into its '
                'face, the value 7 is the weight pressed beside it, and '
                'calling on the runtime is what the hound does to read the '
                'stone.'
            ),
            resolution=(
                'The REPL read the carved marker as the form requested and '
                'handed back the bound value. The stone stood firm — any dog '
                'who looked for y would find what Rex had named there.'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_02 = SubjectCurriculum(grade=3, subject_id="G3-02",
    subject_title="def — redefinition", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(do (def x 1) (def x 99) x)",
            expected=99,
            concept_phrase="the redefined binding",
            question_what="the value of x after redefining it with def from 1 to 99",
            goal_text="bind x to 1, then redefine it as 99 and return it",
            scenario=(
                'Patch the hound arrived at a marker stone by the pond and '
                'scratched the name x into its worn surface, pressing a small '
                'weight beside it — marking the spot where one bone lay buried. '
                'Days passed. Patch returned and saw the old mark was still '
                'there.'
            ),
            need=(
                'But Patch had found a much larger cache of bones at that '
                'same location and needed to update the stone to show the '
                'new count. "A marker can be recarved," Patch said. "The old '
                'value fades; the new one takes its place."'
            ),
            mapping=(
                'The marker stone is the namespace, the name x is scratched '
                'into its face, the first weight is the old binding, and the '
                'second def is Patch\'s act of recarving the stone with a new '
                'value.'
            ),
            resolution=(
                'Patch deepened the carving and pressed a new weight beside '
                'it — the binding overwritten. When the REPL looked up x, it '
                'found the freshest mark, the most recent value that had been '
                'carved into the stone.'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_03 = SubjectCurriculum(grade=3, subject_id="G3-03",
    subject_title="let — local binding", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(let [x 3] (+ x 1))",
            expected=4,
            concept_phrase="the local binding and addition",
            question_what="the running total after binding x to 3 and adding 1",
            goal_text="bind a value of 3 to a local name x for one stretch, then return that value plus one",
            scenario=(
                'Bell the hound had picked up a small bone near the pond '
                'and held it firmly between her jaws. Just for the next '
                "stretch of crossing she would need to know the bone's "
                'tally — 3 — by a short local name x.'
            ),
            need=(
                'She wanted the running total — what x plus one more would '
                'come to — at the moment her paw left the far bank. After '
                'that stretch, the mouth would empty and x would mean '
                'nothing again.'
            ),
            mapping=(
                'The closed jaws are the let-binding, x is the name for '
                "what's gripped between the teeth, the value held there is "
                "3, and the form's stretch is the crossing. Outside the "
                'form, the mouth empties and the binding goes with it.'
            ),
            resolution=(
                'The REPL pulled from the mouth as the form directed and '
                "handed back the running total. Past the crossing, Bell's "
                'mouth was empty again — the binding had been in force only '
                'for that stretch.'
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
                'Rex the hound found ten smooth stones near the forest and '
                'gathered them into a tight mouthful. "I hold this count only '
                'for one stretch — while I carry these stones from bank to '
                'bank," he said, his jaws clamped firm. "Once I cross, I drop '
                'them and they scatter."'
            ),
            need=(
                'For the crossing, he needed the product — that count '
                'multiplied by itself — before his paws touched the far shore. '
                'The mouth would empty there, and the binding would fade with '
                'the stones.'
            ),
            mapping=(
                'The closed jaws are the let, the name n is what the throat '
                'knows for that stretch, the count 10 is what\'s gripped, and '
                'the running total is the product the mouth carries back.'
            ),
            resolution=(
                'The REPL read the jaws and computed the product of the count '
                'with itself, handing back the verdict. Past the far shore, '
                'Rex dropped the binding, and the name n meant nothing again.'
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
                'Bell the hound found a bone near the meadow, five joints '
                'long, and cradled it between her teeth. "For this one stretch '
                'of the path, I will know this bone by the name a," she said '
                'through the grip. "When I reach the far bank, my mouth opens '
                'and the name goes with it."'
            ),
            need=(
                'She wanted to carry the value across — just to know its name '
                'and have it ready, without needing to name it at the top '
                'level. The binding lived only while the form breathed.'
            ),
            mapping=(
                'The teeth-grip is the let, the name a is clamped into her '
                'mind for that span, the bone\'s length is the value, and '
                'calling a is what happens when the form looks up the grip.'
            ),
            resolution=(
                'The REPL read the bite and returned the value the mouth had '
                'held. Bell stepped past the form\'s edge and released the '
                'binding. The name a was gone.'
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_04 = SubjectCurriculum(grade=3, subject_id="G3-04",
    subject_title="let — multi-binding", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(let [a 1 b 2] (+ a b))",
            expected=3,
            concept_phrase="the multi-binding and addition",
            question_what="adding a and b after binding both via let to 1 and 2",
            goal_text="bind a to 1 and b to 2, then add them",
            scenario=(
                'Patch the hound arrived at the crossing with two bones — one '
                'small, one larger. "I will know these two by separate names '
                'for the span of this form," Patch said, holding both between '
                'the jaws. "The names a and b, gripped together until I reach '
                'the far bank."'
            ),
            need=(
                'The form required them to be known by those names so the '
                'mouth could combine them — adding them into a single verdict '
                'before release.'
            ),
            mapping=(
                'The pair of bones in the mouth is the multi-binding, the '
                'names a and b are what the throat holds, the two weights are '
                'what\'s gripped, and the sum is the product of combining them.'
            ),
            resolution=(
                'The REPL read the dual grip and added the bound values, '
                'handing back the total. Patch released the crossing.'
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
                'Bell the hound picked up two bones at the river bank — one '
                'large, one small — and held both steady in her mouth. "For '
                'this crossing, I call the large one x and the small one y," '
                'she said through the grip. "The binding lasts only while my '
                'jaws stay closed."'
            ),
            need=(
                'She needed to know what remained when the smaller was taken '
                'from the larger — the difference that would matter on the far '
                'side.'
            ),
            mapping=(
                'The twin grip in the teeth is the let, the names x and y are '
                'what the mouth knows for the form\'s span, the two counts are '
                'the bound values, and the verdict is the difference.'
            ),
            resolution=(
                'The REPL subtracted y from x and returned the result. Bell '
                'released both bones as she crossed.'
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
                'Rex the hound gathered three bones at the stream\'s edge and '
                'clenched them all between his jaws — a light grip, a medium '
                'one, and a heavy one. "I will hold these as a, b, and c for '
                'one stretch," he said, naming each as his teeth settled. "The '
                'binding lives only while I cross."'
            ),
            need=(
                'The form needed all three known by separate names so the '
                'mouth could add them together into a single tally before '
                'release.'
            ),
            mapping=(
                'The three bones in the jaws are the three-binding, the names '
                'a, b, and c are what the throat holds tight, the counts are '
                'the gripped values, and the sum is what comes back.'
            ),
            resolution=(
                'The REPL read all three grips and added the bound values, '
                'returning the total. Rex dropped the bones on the far bank.'
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_05 = SubjectCurriculum(grade=3, subject_id="G3-05",
    subject_title="let — shadowing outer def", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(do (def x 10) (let [x 99] x))",
            expected=99,
            concept_phrase="the inner binding shadowing the outer",
            question_what="the value of x inside the let scope where it shadows the def binding",
            goal_text="define x at the top level, then shadow it locally and return the inner value",
            scenario=(
                'Bell the hound had long marked a stone at the stream\'s edge with the name x, recording a weight of 10 beside it for all to read. But one day, she picked up a much larger bone and held it in her jaws for a single crossing. "For just this form," she said around the grip, "x will mean what I hold — not what\'s carved in the stone."'
            ),
            need=(
                'The form needed to see the bone in her mouth when it asked for '
                'x — the local grip hiding the marker stone\'s record — only '
                'for that stretch.'
            ),
            mapping=(
                'The stone is the def at the top level, the bone in the mouth '
                'is the let-binding that shadows it, the local name x hides '
                'the stone\'s x while the jaws are closed, and the form\'s '
                'span is the only place the shadow holds.'
            ),
            resolution=(
                'The REPL read the jaws first — and found x meant the grip, '
                'not the stone. The shadow held only while the form breathed. '
                'Bell released the bone and the shadow faded.'
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
                'Patch the hound had carved a marker stone by the forest, '
                'scratching the name x deep into it and pressing a weight of '
                '10 beside it. One crossing later, Patch picked up a larger '
                'bone and held it in the jaws for one form: "This grip will '
                'hide the stone\'s mark, but only for this stretch."'
            ),
            need=(
                'After the crossing, when Patch asked for x again, the stone '
                'would speak — not the grip that had faded. The scope would '
                'return to the namespace the moment the form ended.'
            ),
            mapping=(
                'The stone is the def in the top-level namespace, the bone '
                'in the jaws is the let that shadows it, and the second lookup '
                'of x reads the stone again — the marker outlasts the grip.'
            ),
            resolution=(
                'The REPL saw the jaws first and returned the grip for that '
                'form. When the form ended, Patch released the bone. The second '
                'lookup of x found the stone\'s carved value — the binding '
                'endured beyond the form.'
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_06 = SubjectCurriculum(grade=3, subject_id="G3-06",
    subject_title="let — binding can reference prior", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(let [a 5 b (* a 2)] b)",
            expected=10,
            concept_phrase="the sequential binding where later refers to earlier",
            question_what="the value of b, bound to twice a via let, after a is bound to 5",
            goal_text="bind a to 5, then bind b to twice a, and return b",
            scenario=(
                'Rex the hound gathered five bones and clamped them in his '
                'jaws as the name a. Before stepping forward, he computed in '
                'his mind what twice that grip would weigh — and held both the '
                'first grip and the second answer as b. "Each binding speaks '
                'to the next," he said through the dual grip. "The second form '
                'sees the first."'
            ),
            need=(
                'He needed the second binding to refer to the first — to '
                'multiply a by two and hold the product in the same mouth for '
                'the crossing.'
            ),
            mapping=(
                'The bones gripped as a are the first binding, the doubled '
                'weight held as b is the second binding that sees a, the '
                'computation happens within the let\'s span, and b becomes the '
                'verdict the form returns.'
            ),
            resolution=(
                'The REPL read the first grip, used it to compute the second, '
                'and held both in the let\'s span. The mouth released both as '
                'the form ended, returning b\'s value.'
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
                'Bell the hound picked up three bones and gripped them in '
                'careful sequence within the mouth. First, she called the '
                'smallest a. Then she thought of adding one more — and held '
                'that grip as b. Then she doubled b in her mind and held the '
                'final answer as c. "Each binding speaks to the ones before," '
                'she said through the triple grip. "One after another, until '
                'the form speaks the last."'
            ),
            need=(
                'She needed the chain — a into b, b into c — all held in the '
                'same crossing. Each binding could see the ones that came '
                'before.'
            ),
            mapping=(
                'The first grip is a, which b can see and build upon, which c '
                'can then use — all within the jaws. Each binding is gripped '
                'in sequence, each refers to what came before, and the mouth '
                'releases all three as the form ends.'
            ),
            resolution=(
                'The REPL traced through the chain: a became 3, b became a+1, '
                'c became b*2. The mouth released the final value. The binding '
                'ended when the form ended.'
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_07 = SubjectCurriculum(grade=3, subject_id="G3-07",
    subject_title="fn — anonymous function", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="((fn [x] (+ x 1)) 4)",
            expected=5,
            concept_phrase="the anonymous function call",
            question_what="the result of applying an anonymous fn that adds 1 to its argument to the value 4",
            goal_text="create an anonymous function that adds 1 to its argument and apply it to 4",
            scenario=(
                'Bell the hound put her nose to the ground at the bank near '
                'the pond and laid out a careful sniffing-trail: take '
                "whatever you find, add one bone's worth, carry the result "
                'back. She did not name the trail — it would only be walked '
                'once.'
            ),
            need=(
                'She had just one input in mind — a starting count — and '
                "wanted the answer at the trail's end without ever needing "
                "to remember the trail's name afterward."
            ),
            mapping=(
                'The trail is the anonymous fn, the single sniff is '
                'add-one-bone, the input value is what gets carried into '
                "the trail's first step, and what comes back from the last "
                "sniff is the trail's value."
            ),
            resolution=(
                'The REPL walked the trail end to end and handed back the '
                'value at the last sniff. The trail itself, having served '
                'Bell for that one walk, faded back into the bank.'
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
                'Patch the hound laid out a quick nose-trail at the stream\'s edge — a path of sniffs that said: take whatever comes in, take what comes next, and hand back their product. "This trail is nameless," Patch said, breathing along the scent-marks. "I will walk it once with two counts and throw it away."'
            ),
            need=(
                'The form needed a procedure for two inputs that had no name '
                'to remember afterward — a trail drawn just for this walk.'
            ),
            mapping=(
                'The scent-marks laid on the bank are the anonymous fn, the '
                'two inputs carried in are a and b, the computation along the '
                'trail is the multiplication, and what comes back is the '
                'product.'
            ),
            resolution=(
                'The REPL walked the unnamed trail with 3 and 4, multiplied '
                'them as the sniffs directed, and handed back the answer. The '
                'trail faded into the bank — Patch had no use for its name '
                'again.'
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_08 = SubjectCurriculum(grade=3, subject_id="G3-08",
    subject_title="fn — multi-arg", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="((fn [a b c] (+ a b c)) 1 2 3)",
            expected=6,
            concept_phrase="the three-argument anonymous function call",
            question_what="the result of applying an anonymous fn with three parameters that adds them to 1, 2, and 3",
            goal_text="create an anonymous function with three parameters that adds them and apply it to 1, 2, and 3",
            scenario=(
                'Rex the hound drew out three sniffing-steps at the stream\'s edge, a path that asked for three separate counts. "Take the first, then the second, then the third," he said, tracing the marks, "and carry back their sum. This trail has no name — I design it just for this walk."'
            ),
            need=(
                'The form required a three-step trail with no name to keep. '
                'The procedure would be used once, then forgotten.'
            ),
            mapping=(
                'The three sniff-marks are the three parameters a, b, and c, '
                'the path they form is the anonymous fn, the three values '
                'passed in are carried along each step, and the sum is what '
                'the nose finds at the end.'
            ),
            resolution=(
                'The REPL walked the unnamed three-step trail with the counts '
                '1, 2, and 3, adding them as the sniffs showed, and brought '
                'back the total. The trail had done its work and vanished into '
                'the bank.'
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_09 = SubjectCurriculum(grade=3, subject_id="G3-09",
    subject_title="defn — shorthand", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(do (defn dbl [x] (* x 2)) (dbl 5))",
            expected=10,
            concept_phrase="the named recipe-card and its first call",
            question_what="the doubled count after defining a recipe named dbl and calling it on 5",
            goal_text="define a recipe named dbl that takes a quantity and serves twice that, then call it on 5",
            scenario=(
                'Bell the hound crafted a named nose-trail at the meadow and '
                'carved its name dbl into a flat stone beside it. "This trail '
                'will double any count passed along it," she explained. "I will '
                'use it again and again, and the name will remember it."'
            ),
            need=(
                'The form defined the trail once, gave it a name, and then '
                'called that trail by name with a fresh count — proving the '
                'named procedure worked.'
            ),
            mapping=(
                'The flat stone is the def, the carving dbl is the name, the '
                'nose-trail is the fn that does the doubling, and calling dbl '
                'is what the form does when it invokes the trail by its mark.'
            ),
            resolution=(
                'The REPL carved the name into the stone and learned the '
                'trail. When the form called dbl, it walked the trail with 5, '
                'doubled the count, and returned the doubled verdict.'
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
                'Patch the hound laid out a three-step sniffing-trail at the stream\'s edge and scratched its name — add3 — into a marker stone beside the path. "This trail takes three counts and gives back their sum," Patch said. "I name it so I can call it whenever I need to add three together."'
            ),
            need=(
                'The form defined the named trail once, then proved it worked '
                'by calling add3 with three separate counts.'
            ),
            mapping=(
                'The stone with add3 scratched on it is the def, the three-step '
                'trail is the fn that does the addition, the three inputs are '
                'passed along the steps, and calling add3 is reading the stone '
                'and walking the trail it marks.'
            ),
            resolution=(
                'The REPL marked the stone with the name add3 and remembered '
                'the trail. When the form called add3 with 1, 2, and 3, the '
                'REPL walked the trail, added the counts as the sniffs showed, '
                'and returned the total.'
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_10 = SubjectCurriculum(grade=3, subject_id="G3-10",
    subject_title="anonymous shorthand #()", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(#(+ % 1) 5)",
            expected=6,
            concept_phrase="the shorthand function syntax",
            question_what="the result of using the #() shorthand to create a function that adds 1 to its argument and applying it to 5",
            goal_text="use the shorthand syntax to create a function that adds 1 to its argument and apply it to 5",
            scenario=(
                'Rex the hound caught a whiff of the bank near the meadow and '
                'traced a quick, terse sniffing-path — so brief it had almost '
                'no name at all. "Add one more bone to whatever you find," the '
                'marks said. He did not carve a marker stone for this fleeting '
                'trail.'
            ),
            need=(
                'The form needed a one-use procedure, so compact it barely '
                'counted as a trail — just enough scent to say "add one" and '
                'nothing more.'
            ),
            mapping=(
                'The shorthand marks are the compact trail, the % stands for '
                'whatever scent comes in, the operation is addition, and the '
                'result is what comes back from the abbreviated path.'
            ),
            resolution=(
                'The REPL read the shorthand marks, walked the terse trail '
                'with 5, added one as the scent showed, and returned the '
                'verdict. The trail had no name to remember.'
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
                'Bell the hound drew a bare-minimum sniffing-path at the stream\'s edge — so short and terse it had almost no form at all. "%1 and %2, then multiply," the marks said in one quick sequence. The trail was so fleeting Bell never carved its name in stone.'
            ),
            need=(
                'The form required a quick two-step procedure that would be '
                'used just once. The shorthand let her draw it without ceremony '
                'or naming.'
            ),
            mapping=(
                'The compressed marks are the shorthand trail, %1 and %2 stand '
                'for the two counts coming in, the operation is multiplication, '
                'and what comes back is the product without fuss.'
            ),
            resolution=(
                'The REPL read the terse marks, carried 3 and 4 along the '
                'abbreviated trail, multiplied them as the scent showed, and '
                'returned the answer. The trail left no name behind.'
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_11 = SubjectCurriculum(grade=3, subject_id="G3-11",
    subject_title="Substitution rule", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(let [a 7] (+ a a))",
            expected=14,
            concept_phrase="the binding referenced multiple times",
            question_what="the result of adding a to itself after binding a locally to 7 via let",
            goal_text="bind a to 7 and add a to itself",
            scenario=(
                'Patch the hound held a bone at the stream\'s edge between his jaws — a count of 7. "I will call this grip a," he said, "and I need to know what a plus a makes. The name a means 7, so I will add 7 to 7."'
            ),
            need=(
                'The form referenced the same name twice, and the REPL would '
                'substitute the grip\'s value into both places, adding the '
                'result to itself.'
            ),
            mapping=(
                'The bone gripped as a is the value 7, each mention of a in '
                'the form is a reference to that grip, and the addition is what '
                'happens when a stands for its value twice.'
            ),
            resolution=(
                'The REPL read the grip, substituted 7 for each a, and added '
                '7 to 7, handing back the sum. The binding faded as Patch '
                'released the crossing.'
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
                'Bell the hound laid out a sniffing-trail that said: "Take what '
                'comes in as x, then multiply x by itself." She did not name the '
                'trail. "When I call it with 6," she said, "the trail will use 6 '
                'for every x."'
            ),
            need=(
                'The trail used the same parameter twice, and the form needed '
                'the trail to substitute the input value for both instances and '
                'multiply them.'
            ),
            mapping=(
                'The scent-trail is the fn, x is the parameter, the two mentions '
                'of x in the body get the same substitution (the input 6), and '
                'the multiplication of 6 by 6 is what comes back.'
            ),
            resolution=(
                'The REPL walked the trail with 6, substituted 6 for each x, '
                'multiplied 6 by 6, and returned the squared result. The '
                'unnamed trail faded.'
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_12 = SubjectCurriculum(grade=3, subject_id="G3-12",
    subject_title="Scope vs namespace", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(do (def g 5) (let [g 99] (+ g 1)))",
            expected=100,
            concept_phrase="the scope shadowing and computation",
            question_what="the result of adding 1 to g, computed inside a let where g is locally bound to 99, shadowing the top-level def",
            goal_text="define g at the top level, shadow it in a let with a different value, and compute g+1 inside the let",
            scenario=(
                'Rex the hound carved a marker stone by the forest and '
                'scratched a name into it — g — pressing the value 5 beside '
                'the mark. "This stone will stand here and hold this value," '
                'he said. Later, he picked up a much larger bone and held it '
                'in his jaws for one crossing.'
            ),
            need=(
                'For just that stretch, the name g in his mouth would need to '
                'mean the larger weight, not the stone\'s carved value. And he '
                'needed to compute what g plus one would be — using the grip, '
                'not the stone.'
            ),
            mapping=(
                'The marker stone is the def that lives in the namespace, the '
                'bone in the jaws is the let that shadows it for one stretch, '
                'and the computation inside the form sees the grip, not the '
                'stone.'
            ),
            resolution=(
                'The REPL read the jaws first when it saw g inside the let, '
                'added one, and returned the verdict. The shadow faded when the '
                'form ended. The stone stood untouched — its mark would be read '
                'again outside the let.'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_13 = SubjectCurriculum(grade=3, subject_id="G3-13",
    subject_title="fn body returns last form", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="((fn [x] x x x 99) 1)",
            expected=99,
            concept_phrase="the function body with multiple expressions",
            question_what="the result of applying an anonymous fn where the body contains multiple expressions but only the last one is returned, applied to 1",
            goal_text="create an anonymous function with multiple forms in its body but return only the last one",
            scenario=(
                'Bell the hound laid out a sniffing-trail at the stream\'s edge '
                'with many scent-marks in a row. "The runtime will follow each '
                'sniff," she said, "and check what I named. But only the last '
                'sniff is what I carry home — the others fade as I walk on."'
            ),
            need=(
                'She wanted to craft a trail with many steps but know that only '
                'the final scent-mark would be returned — the verdict that '
                'mattered was always the last one.'
            ),
            mapping=(
                'The nose-trail is the fn, the sniff-marks are the forms in '
                'the body, the named parameter is what gets carried into each '
                'step, and the last sniff is the only value that comes back.'
            ),
            resolution=(
                'The REPL walked the trail, followed each mark in order, but '
                'returned only what the final sniff had revealed — the running '
                'total that mattered was always what lay at the trail\'s end.'
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_14 = SubjectCurriculum(grade=3, subject_id="G3-14",
    subject_title="do form", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(do 1 2 3)",
            expected=3,
            concept_phrase="the do form with multiple values",
            question_what="the final value evaluated by do from the sequence",
            goal_text="evaluate a sequence of values and return the last one",
            scenario=(
                'Patch the hound stood at the bank near the pond and scratched '
                'marks on the bark in a line: one mark, then another, then a '
                'third. "I am reading these marks," he said, "one by one, from '
                'left to right. But what I carry back is only the last mark '
                'I read."'
            ),
            need=(
                'The form needed to trace through a sequence of values in order '
                'but return only the final one — all prior values would be seen '
                'but forgotten.'
            ),
            mapping=(
                'The scratch-marks on bark are the sequence of forms in the do, '
                'reading them in order is what the runtime does, and the verdict '
                'is always what the last mark says.'
            ),
            resolution=(
                'The REPL traced the marks from first to last but handed back '
                'only what the final scratch had spoken. The earlier marks had '
                'been read and released.'
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
                'Rex the hound left three sets of paw-prints at the stream\'s '
                'edge, one trail after another. "I walk each trail in turn," he '
                'said, pressing the last print deep into the stone, "and whatever '
                'the final trail brings me is what I carry back."'
            ),
            need=(
                'He needed to compute each result in the sequence but keep only '
                'the final verdict — the earlier sums would matter for reading, '
                'but not for the answer that came back.'
            ),
            mapping=(
                'The paw-trails are the three forms, walking each in sequence is '
                'what the runtime does, and the value returned is always what the '
                'last form had computed.'
            ),
            resolution=(
                'The REPL walked each trail, computed the sums, but returned only '
                'the verdict of the final step. The earlier answers had served '
                'their purpose and faded.'
            ),
            tags=("story",),
        ),
    ], subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_15 = SubjectCurriculum(grade=3, subject_id="G3-15",
    subject_title="Side-effects in body", fable="dog-shadow",
    examples=[
        SubjectExample(
            form='(do (println "hi") 42)',
            expected=42,
            concept_phrase="the do form with side-effects and final return",
            question_what="the final value evaluated by do, ignoring the intermediate println side-effect",
            goal_text="execute a print statement for side-effects, then return a different value",
            scenario=(
                'Bell the hound barked a signal across the bank near the forest — '
                '"Hi!" she called out, watching it echo into the canyon. "That bark '
                'had its moment," she said. "But what I carry back is not the sound; '
                'it is the bone I hold afterward."'
            ),
            need=(
                'She needed to perform an action for its side-effect — the barking '
                'had to happen — but the form\'s verdict was the different value '
                'that came after.'
            ),
            mapping=(
                'The bark is the form that runs for side-effects, the echo is what '
                'the runtime hears but does not return, and the bone gripped '
                'afterward is the verdict the form speaks.'
            ),
            resolution=(
                'The REPL executed the bark and heard the signal, but the return '
                'value was the final grip — the separate value that had no echo, '
                'only substance.'
            ),
            tags=("story",),
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_16 = SubjectCurriculum(grade=3, subject_id="G3-16",
    subject_title="Name collision: namespace vs let", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(let [+ 99] +)",
            expected=99,
            concept_phrase="the shadowed operator binding",
            question_what="the value locally bound to the + operator via let",
            goal_text="shadow the plus operator with a local binding and return the bound value",
            scenario=(
                'Patch the hound held a bone in his jaws and called out, "For this '
                'crossing, I will name the plus-sign itself and bind it to a weight." '
                'He clenched the grip tight. "Even though the plus-sign is known across '
                'the bank, here in my mouth it means something else entirely."'
            ),
            need=(
                'The form needed to shadow an operator with a local name, proving '
                'that even core symbols could be bound by a let — hidden from their '
                'global meaning for the duration of the stretch.'
            ),
            mapping=(
                'The known plus-sign is the operator in the namespace, the bone '
                'gripped as plus in the mouth is the shadowed binding, and the '
                'mouth\'s grip is what the form returns.'
            ),
            resolution=(
                'The REPL looked up the plus-sign inside the let and found not the '
                'operator but the bound value — the shadow had claimed it for that '
                'stretch. When the form ended, Patch released the grip.'
            ),
            tags=("story",),
        ),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_17 = SubjectCurriculum(grade=3, subject_id="G3-17",
    subject_title="Naming conventions (kebab-case)", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(let [hare-speed 4 tortoise-speed 1] (- hare-speed tortoise-speed))",
            expected=3,
            concept_phrase="the kebab-case naming and subtraction",
            question_what="the result of subtracting tortoise-speed from hare-speed after binding both via let",
            goal_text="bind hare-speed to 4 and tortoise-speed to 1, then compute their difference",
            scenario=(
                'Rex the hound held two bones at the meadow: one he would carry at '
                'a fast pace, one at a steady slow pace. "I name the first hare-speed '
                'and the second tortoise-speed," he said through the dual grip. "The '
                'names use dashes between the words — a naming rule the pack all '
                'follow."'
            ),
            need=(
                'The form required careful naming: each name had to match the pack\'s '
                'convention of dashes separating words, so the binding would be clear '
                'and easy for any dog to read.'
            ),
            mapping=(
                'The two bones gripped are the named bindings, the dashed names are '
                'what the pack agrees to call them, and the difference is what comes '
                'back when one is taken from the other.'
            ),
            resolution=(
                'The REPL read the dashed names as the binding directed and computed '
                'the difference — the naming convention had served its purpose, making '
                'the form\'s intent clear to anyone who would read the markers.'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_18 = SubjectCurriculum(grade=3, subject_id="G3-18",
    subject_title="When to name vs inline", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(let [n 5] (* n n n))",
            expected=125,
            concept_phrase="the named binding used multiple times",
            question_what="the result of multiplying n by itself three times after binding n locally to 5 via let",
            goal_text="bind n to 5 and compute n cubed",
            scenario=(
                'Bell the hound gathered one bone by the river bank and gave it a '
                'short name: n. "I will multiply this bone by itself three times," '
                'she said, holding the grip tight. "Naming it once and using the name '
                'three times is cleaner than carrying the weight three separate times."'
            ),
            need=(
                'She needed to perform the same value multiple times within the same '
                'form, and naming it made the form easier to read and less error-prone '
                'than repeating the literal value.'
            ),
            mapping=(
                'The bone gripped as n is the local binding, each mention of the name '
                'is a reference to the same grip, and the product is what comes back '
                'from multiplying n three ways.'
            ),
            resolution=(
                'The REPL read the grip, substituted it three times in the '
                'multiplication, and returned the product. The name had made the form '
                'clear; the binding lasted only for the crossing.'
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
                'Patch the hound arrived at the crossing and saw three stones '
                'arranged in a pile. "I don\'t need to name these," he said, "because '
                'I will use them just once and the form is so short that the values '
                'are clear enough."'
            ),
            need=(
                'When the form was brief and the value appeared only once or the '
                'repetition was obvious, naming it added extra steps without gaining '
                'clarity.'
            ),
            mapping=(
                'The three stones laid out are the literal values in the form, the '
                'pile itself is the operation, and the product is what comes back '
                'without any naming layer.'
            ),
            resolution=(
                'The REPL saw the literal values and multiplied them directly, '
                'handing back the answer. No binding was needed; the form spoke for '
                'itself.'
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
    print(f"grade-3 dog-shadow smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
