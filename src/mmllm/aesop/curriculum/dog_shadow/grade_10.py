"""Grade 10 — macros, code as data. Through dog-shadow.

Subplot lens: the Tortoise designs a small language. Each subject is
the Hare and Tortoise inspecting a macro, an expansion, or a piece of
syntax-quoted source. The fable's moral — patience over haste — fits
naturally: macros reward careful reading of expansions over guessing.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.dog_shadow.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.dog_shadow._metaphor_pools import (
    _CHALKMARK_SUBPLOTS, _RECIPE_SUBPLOTS, _REWRITERULE_SUBPLOTS, _SCRIBE_SUBPLOTS,
)


# ─────────────────────── grade-10 subplot extensions ───────────────────────
#
# The Tortoise has been quietly designing a small language inside
# Clojure. The Hare keeps wanting to skip past the expansion step and
# just guess what the macro returns. Each template lets the form
# carry the technical detail while the fable carries the manner.

_MACRO_SUBPLOTS: list[SubplotTemplate] = list(_GOAL_SUBPLOTS) + [

    SubplotTemplate("""\
{tortoise}, {emo_patient} had spent the morning {place} sketching a tiny
language of {tortoise_his_her} own — a notebook of macros that wrote
other forms. The next entry was {concept_phrase}. {hare_phrase} wanted to
{goal_text}. {tortoise} asked {hare_him_her} to write the form carefully
and submit it so the REPL could show what code it produced or what value it returned."""),

    SubplotTemplate("""\
"A macro is just a function that runs at compile time," {tortoise}
explained {place}, {emo_patient}. {hare}, {emo_proud}, said
{hare_he_she} could already understand what {concept_phrase} meant.
{tortoise} insisted they actually write a form to {goal_text}
and read what the runtime reported, expansion or value."""),

    SubplotTemplate("""\
The path {place} was littered with old macro definitions someone had
carved into bark. {hare} found one shaped like
{concept_phrase} and dared {tortoise_phrase}, {emo_patient} to write the form that could {goal_text}.
{tortoise} only smiled and asked {hare_him_her} to submit it carefully
into the REPL — that, after all, was the whole point of having a
macroexpander."""),

    SubplotTemplate("""\
{hare} insisted {place} that macros were the same as functions.
{tortoise_phrase}, {emo_patient}, sketched {concept_phrase} on a
strip of bark. "The difference," {tortoise_he_she} said, "is in what
we're trying to accomplish: {goal_text}. Write the form and let the
runtime tell us exactly what it does.\""""),

    SubplotTemplate("""\
A small notebook lay open {place} where the Tortoise had been studying
syntax-quote. The page showed {concept_phrase}, and a goal written in
pencil: {goal_text}. {hare}, {emo_tired}, reluctantly
agreed to write the form to settle once and for all what it produced."""),

    SubplotTemplate("""\
At a stone tablet {place}, {tortoise}, {emo_patient} was teaching
{hare_phrase} the discipline of expansion: never trust your eyes, only
the macroexpander. The day's challenge was simple: {goal_text}. The
form that accomplishes {concept_phrase} had to be submitted; nothing
else would do."""),
]


def _ex(form, expected, concept, what, goal="", tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal, tags=tags)


_PLAN_G10 = _PLAN_POOL + (
    "I write the form and let the macroexpander or REPL show the result.",
    "I expand the macro with macroexpand and read the produced form.",
    "I submit the syntax-quoted or quoted form to the REPL.",
    "I write the macro form and let the runtime evaluate or expand it.",
)


# ─────────────────────── 16 grade-10 subjects ───────────────────────


# G10-01 — quote / unquote / unquote-splice
G10_01 = SubjectCurriculum(
    grade=10, subject_id="G10-01",
    subject_title="quote, unquote, unquote-splice",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(quote (+ 1 2))",
            expected=["+", 1, 2],
            concept_phrase="quoting an addition form",
            question_what="what you get when you quote an addition form",
            goal_text="quote an addition form so it evaluates to a list without computing",
            scenario=(
                'Bell the hound stood at the stream bank and scratched a '
                'pattern into the bark: the shape of an addition, a plus '
                'sign, two numbers. "This scratch is just the scratch," she '
                'said, "not the sum itself."'
            ),
            need=(
                'She wanted to send the form itself downriver without the '
                'runtime computing what it meant. The form needed to come '
                'back as the list of symbols and numbers, not as their sum.'
            ),
            mapping=(
                'The quote is the instruction to read the scratch literally. '
                'The form under quote is the exact scratch the dog wants to '
                'read — not to evaluate it, but to see the shape it holds.'
            ),
            resolution=(
                'The REPL read the quote and returned the form untouched: the '
                'three symbols in order, the computation never invoked. The '
                'scratch had stayed a scratch — 2.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="'(1 2 3)",
            expected=[1, 2, 3],
            concept_phrase="the quoted list with three numbers",
            question_what="the result of quoting a three-element list",
            goal_text="quote a list of three numbers so it returns the form itself",
            scenario=(
                'Rex the hound wanted to mark three stones by the pond — '
                'one marked 1, one marked 2, one marked 3. Instead of counting '
                'them, he made a single scratch-mark that spelled the list '
                'shape itself.'
            ),
            need=(
                'The scratch had to return the list of three numbers, not their '
                'count or product. The form had to come back as the ordered '
                'sequence he had scratched.'
            ),
            mapping=(
                'The quote reader-mark is the instruction: keep this shape '
                'as data. The list is the form held as a sequence of values, '
                'and the quote says "read the list, do not evaluate."'
            ),
            resolution=(
                'The REPL read the quote and returned the three numbers in the '
                'order the scratch had marked. The form came back intact — three '
                'elements, untouched by evaluation — 3.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(let [x 5] `(a ~x b))",
            expected=["a", 5, "b"],
            concept_phrase="a syntax-quoted form with the variable unquoted",
            question_what="what you get when unquoting x inside a syntax-quoted form",
            goal_text="create a form that when x is 5 produces a list containing the value of x",
            scenario=(
                'Patch the hound held the bone and wanted to build a marked form. '
                'Inside the syntax-quote, the tilde would tell the runtime: unquote '
                'this spot, substitute the bone\'s value here.'
            ),
            need=(
                'When the binding held the bone, unquoting inside the form should '
                'splice the value into the middle. The result should be a list '
                'with the value between two symbols.'
            ),
            mapping=(
                'The let-jaws grip the bone. The backtick is the syntax-quote. '
                'The tilde says "unquote this spot" — substitute the value here, '
                'not the symbol.'
            ),
            resolution=(
                'The REPL built the form: the tilde unquoted the 5 and '
                'inserted it into the output. The list came back with the value '
                'nested between the two symbol-marks, exactly as scratched.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_CHALKMARK_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-02 — syntax-quote
G10_02 = SubjectCurriculum(
    grade=10, subject_id="G10-02",
    subject_title="syntax-quote",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(let [x 10] `(+ ~x ~x))",
            expected=["+", 10, 10],
            concept_phrase="building a form by unquoting a variable twice inside syntax-quote",
            question_what="the form produced when x is 10 and unquoted twice",
            goal_text="build a form where a variable is inserted twice into an addition form",
            scenario=(
                'Bell the hound held the bone at 10 and scratched a pattern on '
                'bark: a plus sign, then a tilde-mark to show where the value '
                'would go, then another tilde. She was building a new form, '
                'one that would plug the value in at two spots.'
            ),
            need=(
                'When the let bound x to 10, the syntax-quote should build a '
                'form with the value 10 inserted at both tilde-marks. The result '
                'should be a list: addition with 10 and 10 as arguments.'
            ),
            mapping=(
                'The backtick tells the runtime to construct a form by the '
                'scratch. Each tilde says "insert the value here." The entire '
                'form is built as data, with unquoting substituting the value '
                'where the tildes point.'
            ),
            resolution=(
                'The REPL built the form, scanning each tilde and inserting 10 '
                'at both marks. The finished form came back with the addition '
                'operator and two copies of the value — exactly what the scratch '
                'had promised.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(let [xs [1 2 3]] `(list ~@xs))",
            expected=["list", 1, 2, 3],
            concept_phrase="building a form by splicing a vector into syntax-quote",
            question_what="the form produced when splicing a three-element vector",
            goal_text="build a form that inserts all elements of a vector into a list call",
            scenario=(
                'Rex the hound had cached three bones — marked 1, 2, 3 — in a '
                'vector. He scratched a new form with the word "list" and then '
                'a tilde-at sign — meaning: unwrap the vector and splice all '
                'the bones into this spot.'
            ),
            need=(
                'The splicing had to unpack the vector and spread each bone '
                'into the form. The result should be a list with the word "list" '
                'first, then the three bone values flattened out.'
            ),
            mapping=(
                'The backtick constructs the form. The tilde-at says "splice: '
                'unwrap the vector and put each element here, not the vector '
                'itself." The form is assembled with the elements laid flat.'
            ),
            resolution=(
                'The REPL built the form, saw the tilde-at, and spliced the '
                'three bones into the spot. The finished form had the list '
                'operator with all three values as arguments, no nesting — '
                'exactly the shape the splice had spelled — 3.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_CHALKMARK_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-03 — defmacro introduction
G10_03 = SubjectCurriculum(
    grade=10, subject_id="G10-03",
    subject_title="defmacro introduction",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(do (defmacro my-when [t & body] `(if ~t (do ~@body))) "
                 "(my-when true 1 2 3))",
            expected=3,
            concept_phrase="defining a conditional macro and invoking it",
            question_what="the value the rewritten if-do form returns when the test is true and the body has three expressions",
            goal_text="define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body",
            scenario=(
                'Bell the hound crouched at a fresh patch of bark near the '
                'pond, paw poised. She would set a rule that any later mark '
                'of a certain shape would be rewritten — before the runtime '
                'ever followed it — into a different mark with the same '
                'intent.'
            ),
            need=(
                'When any later form named my-when was scratched, the '
                'runtime should first rewrite it into an equivalent '
                'if-form, then evaluate that. The rule would do the work '
                'once; every use would benefit.'
            ),
            mapping=(
                'The rule is the macro, the source shape is the my-when '
                'form, the rewritten shape is the equivalent if-form, and '
                'the runtime applies the rewrite before evaluation begins.'
            ),
            resolution=(
                'The REPL set the rule on the bark, walked through the use, rewriting first and evaluating second. The rewritten form yielded the value the original had asked for (with `1` as the input value) (with `3` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (defmacro twice [x] `(do ~x ~x)) (twice 7))",
            expected=7,
            concept_phrase="defining a macro that repeats its argument",
            question_what="the value returned by twice expanding to a do-block with the unquoted argument repeated",
            goal_text="define a macro named twice that emits its argument twice in a do block, then call it",
            scenario=(
                'Patch the hound scratched a rule on bark: the pattern twice '
                'would expand to a do-block where the argument was unquoted '
                'and repeated. Twice meant "play this bone twice and take the '
                'result from the second play."'
            ),
            need=(
                'When any later form called twice with an argument, the macro '
                'would rewrite it before the runtime ever evaluated it. The call '
                'twice 7 should expand to a do-block with 7 twice, and the '
                'second 7 would be what came back.'
            ),
            mapping=(
                'The defmacro sets the rule on the bark. The macro name is '
                'twice, the pattern is the syntax-quoted form with the tilde '
                'showing where 7 goes. When invoked, the rule rewrites the call '
                'into the expanded form.'
            ),
            resolution=(
                'The REPL set the rule, then when twice 7 was called, it '
                'rewrote the call into (do 7 7). The do-block executed 7 twice '
                'and returned the second value. The macro had done the rewriting '
                'work once; every use benefited.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-04 — Macro expansion rule
G10_04 = SubjectCurriculum(
    grade=10, subject_id="G10-04",
    subject_title="Macro expansion rule",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(macroexpand-1 '(when true 1))",
            expected=["if", True, ["do", 1]],
            concept_phrase="the one-step expansion of the when-macro call",
            question_what="the expanded form after one level of macro expansion",
            goal_text="expand a when-macro call one step to see what code it produces",
            scenario=(
                'Bell the hound found an old scratch-mark on bark: when. She '
                'wanted to see what scratch-mark it would be rewritten into.'
            ),
            need=(
                'Macroexpand-1 would take the form and show what it became after '
                'one pass of the rewriter. The when-form would become an if-form '
                'it abbreviates, but no further.'
            ),
            mapping=(
                'Macroexpand-1 is the magnifying glass. The original form is the '
                'scratch-mark, and the rewritten form is what the magnifier shows '
                'after one layer of rewriting. No evaluation yet.'
            ),
            resolution=(
                'The REPL looked through the magnifier and saw the when scratch '
                'become an if-form with a do-block. The intermediate rewrite was '
                'shown — one step, nothing computed, nothing evaluated — 1.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(macroexpand-1 '(or a b))",
            expected=["let*", ["or__1__auto__", "a"],
                      ["if", "or__1__auto__", "or__1__auto__", ["clojure.core/or", "b"]]],
            concept_phrase="the one-step expansion of the or-macro call",
            question_what="the intermediate form after expanding the macro once",
            goal_text="expand an or-macro call one step to reveal its internal structure",
            scenario=(
                'Rex the hound studied a complex scratch-mark at the stream: or. '
                'He wanted to see the intermediate form it would become, the step '
                'before evaluation.'
            ),
            need=(
                'Macroexpand-1 would reveal the inner rewrite: a let*-binding and '
                'an if-form created to handle the logic. One pass only — the form '
                'not evaluated, just rewritten and revealed.'
            ),
            mapping=(
                'The or-mark is the macro call. Macroexpand-1 shows what one '
                'rewrite produces. The resulting form with let* and if is the '
                'intermediate step — after the macro rewrites but before '
                'evaluation.'
            ),
            resolution=(
                'The REPL expanded once and showed the form beneath the scratch: '
                'a let*-binding with a safe copy, then an if. The rewrite was '
                'bare — not evaluated, just shown. The intermediate structure was '
                'clear.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-05 — macroexpand
G10_05 = SubjectCurriculum(
    grade=10, subject_id="G10-05",
    subject_title="macroexpand",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(macroexpand '(when true 1))",
            expected=["if", True, ["do", 1]],
            concept_phrase="the complete expansion of the when-macro call",
            question_what="the fully expanded form after all macro passes",
            goal_text="fully expand a when-macro call to reveal the if-form it becomes",
            scenario=(
                'Patch the hound came to the bank with a scratched form: when. '
                'This time, the hound wanted to see the final form — not one step, '
                'but all the way through.'
            ),
            need=(
                'Macroexpand — with no limit — would keep rewriting until no '
                'more macros remained. The when-form would be fully unwound.'
            ),
            mapping=(
                'Macroexpand is the full-passage view. The when-mark is the '
                'original scratch, and the final if-form is what it becomes when '
                'all rewrites are done.'
            ),
            resolution=(
                'The REPL expanded fully and showed the complete form: the when '
                'had become an if with a do-block inside. No more macros remained. '
                'The final form was bare and evaluation-ready — 1.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(macroexpand '(-> 1 inc inc))",
            expected=["inc", ["inc", 1]],
            concept_phrase="the complete expansion of the thread-first call",
            question_what="the final form after threading the value through all steps",
            goal_text="fully expand a thread-first macro call to see how the value threads through",
            scenario=(
                'Bell the hound picked up a bone and studied the threading mark '
                'at the bank: arrow inc inc. She wanted to see the full path the '
                'bone would take through each step.'
            ),
            need=(
                'The thread-first macro would rewrite the arrow-form to show how '
                'the value threads through each function. The expanded form would '
                'show nested function calls.'
            ),
            mapping=(
                'The arrow-mark is the shorthand. Macroexpand reveals the full '
                'path by unfolding how each function nests around the value. '
                'Threading is visible as nested calls.'
            ),
            resolution=(
                'The REPL expanded the arrow-form fully. The value was threaded '
                'through inc, then through inc again. The final nested form showed '
                'the path. The shorthand had expanded to show the full journey — 1.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-06 — when / unless macros
G10_06 = SubjectCurriculum(
    grade=10, subject_id="G10-06",
    subject_title="when and when-not as macros",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(when true 1 2 3)",
            expected=3,
            concept_phrase="executing multiple expressions when a condition is true",
            question_what="the result of the last expression when the condition holds",
            goal_text="execute three expressions and return the value of the last when the condition is true",
            scenario=(
                'Rex the hound stood at the fork near the stream. The path ahead '
                'was clear (true). He had three tasks to do before crossing. He '
                'scratched the when-form: if the condition held, do all three '
                'and return the last result.'
            ),
            need=(
                'When the condition was true, all three expressions should run '
                'in order, and the final value (3) should come back. If the '
                'condition had been false, the entire block would be skipped.'
            ),
            mapping=(
                'The when-form is the rule at the fork. The condition true is '
                'the path-check. The three expressions are the tasks to do only '
                'if the check passes. The final result is what the last task '
                'produces.'
            ),
            resolution=(
                'The REPL checked the condition (true), found the path clear, '
                'and ran all three tasks in order. The last task produced 3, '
                'which came back as the verdict. The fork had sent the hound '
                'down the right path.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(when false 1 2 3)",
            expected=None,
            concept_phrase="executing expressions when a condition is false",
            question_what="the result when the condition does not hold",
            goal_text="evaluate a when-form where the condition is false",
            scenario=(
                'Patch the hound came to the fork by the river bank. The path '
                'ahead was blocked (false). The when-form was set: do these '
                'three tasks only if the path is clear. Since it was not, the '
                'entire block should be skipped.'
            ),
            need=(
                'When the condition was false, none of the three expressions '
                'should run. The form should return nil — no verdict, no value. '
                'The fork had blocked the way.'
            ),
            mapping=(
                'The when-form is the rule. The condition false is the blocked '
                'path. The three expressions are the tasks that must be skipped '
                'entirely because the gate is shut. The nil response means: '
                '"not done."'
            ),
            resolution=(
                'The REPL checked the condition (false), found the path blocked, '
                'and skipped all three tasks entirely. No expressions ran. The '
                'form returned nil — the hound waited at the blocked fork, '
                'unable to proceed — 3.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(when-not false :ok)",
            expected=":ok",
            concept_phrase="executing an expression when a negated condition is true",
            question_what="the result when using when-not with a false condition",
            goal_text="use when-not to execute an expression when the condition is false",
            scenario=(
                'Bell the hound wanted the opposite check: run the expression only '
                'if the condition was false. She scratched when-not false and the '
                'keyword :ok. "If danger is NOT present, say all is well."'
            ),
            need=(
                'When-not negates the condition. With false as input, the negation '
                'is true, so the expression :ok should execute and come back.'
            ),
            mapping=(
                'The when-not-form reverses the gate. The false condition is '
                'negated to true (no danger is present). The keyword :ok is the '
                'all-clear signal. When the gate is open via negation, the signal '
                'comes back.'
            ),
            resolution=(
                'The REPL negated the condition (false → true), found the gate '
                'open, and returned :ok. The all-clear signal came back, proving '
                'the hound could proceed without danger.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-07 — Threading macros revisited
G10_07 = SubjectCurriculum(
    grade=10, subject_id="G10-07",
    subject_title="Threading macros revisited",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(-> 5 inc inc inc)",
            expected=8,
            concept_phrase="threading a value through multiple functions in sequence",
            question_what="the result of threading 5 through three increments",
            goal_text="thread the value 5 through inc three times using thread-first",
            scenario=(
                'Bell the hound held the bone marked 5 and laid out a sniffing '
                'trail with three increments in order. "Watch the bone pass from '
                'sniff to sniff," she said. "Each step takes the previous result '
                'as the first argument."'
            ),
            need=(
                'The bone starts at 5. After the first sniff (inc), it becomes '
                '6. The second sniff takes 6 and produces 7. The third takes 7 '
                'and produces 8. The final result is what the last sniff yields.'
            ),
            mapping=(
                'The thread-first arrow is the trail guide. The bone is the value '
                'passed from sniff to sniff. Each sniff (function) takes the bone '
                'and produces a new value. The last sniff is what gets carried '
                'home.'
            ),
            resolution=(
                'The REPL followed the sniffing-trail, passing the bone through '
                'each step. At the end, the bone had become 8 — three increments '
                'complete. The trail had threaded it perfectly to the final '
                'result — 5.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(->> [1 2 3 4] (filter even?) (map inc) (reduce +))",
            expected=8,
            concept_phrase="threading a vector through filter, map, and reduce as the last argument",
            question_what="the sum of mapped values after filtering even numbers",
            goal_text="thread a vector through filter, map, and reduce using thread-last",
            scenario=(
                'Rex the hound had a vector of the bones and a multi-step sniffing-trail. Thread-last would pass the bones as the final argument to each step.'
            ),
            need=(
                'The vector enters the filter for even counts. The filtered bones '
                'go to map inc, each incremented. The mapped bones then go to reduce '
                'with addition, producing a running total.'
            ),
            mapping=(
                'The thread-last arrow is the trail for last-argument threading. '
                'The bones move from step to step, each feeding as the final '
                'argument. The trail ends with a sum.'
            ),
            resolution=(
                'The REPL followed the thread-last trail through each step. The '
                'filtering removed odd bones. The mapping incremented the rest. The '
                'reduce accumulated them. The threading had transformed the bones '
                'step by step — 4.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(macroexpand '(-> x f g))",
            expected=["g", ["f", "x"]],
            concept_phrase="the expanded form of a thread-first call",
            question_what="the nested function calls after expansion",
            goal_text="expand a thread-first macro to see how functions compose",
            scenario=(
                'Patch the hound wanted to see the full sniffing-trail laid out '
                'in bare form. The arrow-mark x f g was the shorthand, but how '
                'would it look when expanded? The nested calls would show the '
                'true composition.'
            ),
            need=(
                'When expanded, the thread-first form should show x threaded '
                'first through f, then the result threaded through g. The nesting '
                'would reveal: g(f(x)).'
            ),
            mapping=(
                'The arrow-form is the shorthand trail. Macroexpand reveals the '
                'bare function composition: g as the outer call wrapping f as the '
                'inner call wrapping x. The nesting is the true structure.'
            ),
            resolution=(
                'The REPL expanded the arrow-form and showed the nested calls: '
                'g with f(x) inside. The thread-first had been unpacked to bare '
                'function application. Patch could see exactly how the bone would '
                'pass from f into g.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-08 — macro vs fn
G10_08 = SubjectCurriculum(
    grade=10, subject_id="G10-08",
    subject_title="Macro vs fn",
    fable="dog-shadow",
    examples=[
        # A function evaluates its args; a macro receives unevaluated forms.
        SubjectExample(
            form="(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))",
            expected=7,
            concept_phrase="calling a plain function that adds two numbers",
            question_what="the sum returned by calling add-fn with arguments 3 and 4",
            goal_text="define a function add-fn and call it to add 3 and 4",
            scenario=(
                'Bell the hound set a sniffing-trail rule named add-fn. When a '
                'dog followed the trail with bones, the trail would evaluate them '
                'first, then add them. The function takes computed values.'
            ),
            need=(
                'When add-fn is called, both arguments are computed before the '
                'function sees them. The function receives the values and combines '
                'them.'
            ),
            mapping=(
                'A function is a nose-trail that expects computed values. The '
                'bones come in as numbers. The trail adds them and yields the '
                'running total.'
            ),
            resolution=(
                'The REPL called add-fn, evaluated the arguments, then walked the '
                'trail. The trail took the values and produced the 4. A plain '
                'function had done the work straightforwardly.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))",
            expected=7,
            concept_phrase="calling a macro that emits an addition form",
            question_what="the sum returned when add-mac expands to an addition of the unquoted arguments",
            goal_text="define a macro add-mac and call it to add 3 and 4",
            scenario=(
                'Rex the hound set a rewrite-rule named add-mac. Unlike the '
                'function, the macro would rewrite the call first — before any '
                'evaluation. It would receive the unevaluated marks 3 and 4, '
                'then build a new form.'
            ),
            need=(
                'When add-mac is called with 3 and 4, the macro receives the '
                'marks themselves, not computed values. It rewrites them into an '
                'addition form, which is then evaluated.'
            ),
            mapping=(
                'A macro is a rewrite-rule. It takes unevaluated forms as input '
                'and produces a new form as output. The unquoting splices the '
                'arguments into the generated form.'
            ),
            resolution=(
                'The REPL called add-mac, which rewrote the call into (+ 3 4). '
                'The rewritten form was then evaluated to produce 7. The macro '
                'had done the rewriting work; the result was the same but the '
                'path was different.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-09 — hygiene and gensym
G10_09 = SubjectCurriculum(
    grade=10, subject_id="G10-09",
    subject_title="Hygiene and gensym",
    fable="dog-shadow",
    examples=[
        # gensym always returns a fresh symbol; we test symbol? predicate.
        SubjectExample(
            form="(symbol? (gensym))",
            expected=True,
            concept_phrase="testing whether gensym produces a symbol",
            question_what="whether a generated symbol is of type symbol",
            goal_text="test that gensym returns a symbol",
            scenario=(
                'Patch the hound wanted to scratch a fresh mark on bark — one '
                'that had never been used before. Gensym would generate a brand '
                'new symbol each time. But was it truly a symbol, or just a '
                'peculiar mark?'
            ),
            need=(
                'The symbol? predicate would test whether the gensym result was '
                'a genuine symbol. If true, the mark was legitimate and could be '
                'used as a binding.'
            ),
            mapping=(
                'Gensym is the mark-generator. The symbol? test is the '
                'verification. A true result means the mark is a valid symbol '
                'that can be used in the language.'
            ),
            resolution=(
                'The REPL called gensym and got a fresh mark. The symbol? test '
                'confirmed it was a proper symbol. Patch could use it as a '
                'binding without fear of collision.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(let [a (gensym \"x_\") b (gensym \"x_\")] (= a b))",
            expected=False,
            concept_phrase="comparing two gensyms created with the same prefix",
            question_what="whether two fresh gensyms are identical",
            goal_text="generate two gensyms with the same prefix and check if they are equal",
            scenario=(
                'Bell the hound generated two fresh marks, both prefixed "x_". '
                'But each gensym call produced a unique symbol — even with the '
                'same prefix, the two marks would be different. She bound them '
                'in a let and tested whether they were equal.'
            ),
            need=(
                'The two gensyms should be distinct. Even though they share the '
                'prefix "x_", each fresh symbol carries a unique identifier. The '
                'equality test should return false.'
            ),
            mapping=(
                'Each gensym call is a new mark. The prefix is just a label — '
                'it does not make two gensyms identical. The let binds two '
                'different marks. The equality test reveals the difference.'
            ),
            resolution=(
                'The REPL generated two fresh marks with the same prefix but '
                'different serial numbers. The equality test returned false — '
                'they were not equal. Fresh marks, even with the same label, '
                'remain distinct.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-10 — anaphoric macros are a bad idea
G10_10 = SubjectCurriculum(
    grade=10, subject_id="G10-10",
    subject_title="Anaphoric macros are confusing",
    fable="dog-shadow",
    examples=[
        # An anaphoric `aif` would inject `it` un-hygienically. We illustrate
        # the safer hygienic alternative: an explicit name.
        SubjectExample(
            form="(do (defmacro safe-if-let [bind then else] "
                 "`(if-let ~bind ~then ~else)) "
                 "(safe-if-let [x 5] (* x 2) 0))",
            expected=10,
            concept_phrase="defining and calling a hygienic if-let macro",
            question_what="the result returned when safe-if-let expands to if-let with binding [x 5] and then-branch (* x 2)",
            goal_text="define a safe-if-let macro and call it with x bound to 5",
            scenario=(
                'Bell the hound sketched a careful macro-rule on bark. Instead '
                'of letting the binding sneak in unseen (anaphoric), '
                'she made the caller provide it explicitly. The rule would '
                'expand to if-let with the binding passed in.'
            ),
            need=(
                'When the macro was called with an explicit binding, it should '
                'expand to if-let and evaluate the then-branch. The value '
                'would be used in the multiplication, yielding a result.'
            ),
            mapping=(
                'The defmacro is the rule. The binding parameter receives the '
                'explicit binding. The unquoting splices it and the branches '
                'into the if-let form. The macro rewrites hygienically.'
            ),
            resolution=(
                'The REPL set the macro-rule, then called it with the binding. The rule expanded to if-let. The then-branch ran and produced a result. The explicit binding prevented any confusion (with `5` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(if-let [x 7] (* x x) 0)",
            expected=49,
            concept_phrase="using the built-in if-let with an explicit binding",
            question_what="the result of the then-branch when the binding succeeds",
            goal_text="use if-let to bind x to 7 and return the square of x",
            scenario=(
                'Rex the hound found the if-let rule carved on the bank. It would '
                'bind x to a value — 7 in this case — and test whether the binding '
                'succeeded. If it did, the then-branch would run with x in scope.'
            ),
            need=(
                'When the binding x to 7 succeeded, the then-branch (* x x) would '
                'execute with x at 7. The multiplication would produce the square '
                'of 7, which is 49.'
            ),
            mapping=(
                'The if-let is the conditional binding. The binding [x 7] is the '
                'test and scope. The then-branch is the code that runs when the '
                'binding succeeds. The x is available within that branch.'
            ),
            resolution=(
                'The REPL executed if-let, bound x to 7 successfully, and ran the '
                'then-branch. The multiplication (* x x) with x at 7 produced 49. '
                'The binding had worked, the condition had held, and the verdict '
                'came back.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-11 — Reader macros overview
G10_11 = SubjectCurriculum(
    grade=10, subject_id="G10-11",
    subject_title="Reader macros overview",
    fable="dog-shadow",
    examples=[
        # Reader macros: ', `, ~, #(...), #_, etc. Test what they read to.
        SubjectExample(
            form="'(1 2 3)",
            expected=[1, 2, 3],
            concept_phrase="using the quote reader macro",
            question_what="the form read by the quote reader",
            goal_text="use the quote reader macro to read a list of three numbers",
            scenario=(
                'Patch the hound stood at the scribe\'s stone where reading-marks '
                'were inscribed. The apostrophe meant: read this as written, do '
                'not evaluate. The list was scratched beneath it.'
            ),
            need=(
                'When the reader saw the quote-mark, it would take the list as '
                'data, not as a form to evaluate. The numbers would come '
                'back in order — a sequence, not a computation.'
            ),
            mapping=(
                'The quote-mark is the reading convention. The list is the form. '
                'The reader looks at the mark and treats it as data. No '
                'evaluation — just reading.'
            ),
            resolution=(
                'The REPL read the quote-mark and returned the list untouched. '
                'The numbers came back in sequence, exactly as scratched. The '
                'quote had told the reader to preserve the form — 3.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(#(* % %) 6)",
            expected=36,
            concept_phrase="using the anonymous-function reader macro",
            question_what="the result of calling the generated function",
            goal_text="use the #(...) reader macro to create a function that squares its argument",
            scenario=(
                'Bell the hound found a shorthand reading-mark on bark: #(* % %). '
                'This was the scribe\'s way of saying "make a quick function where '
                '%  is the argument." The function would take 6 and square it. No '
                'need for a named function — the shorthand did the work.'
            ),
            need=(
                'The reader-mark would expand the shorthand into a proper function '
                'that takes one argument. When 6 was passed in, the multiplication '
                'would happen with % replaced by 6, yielding the product.'
            ),
            mapping=(
                'The #(...) mark is the reader convention for anonymous functions. '
                'The % is the argument placeholder. The * is the operation. The '
                'reader converts the shorthand into a function ready to call.'
            ),
            resolution=(
                'The REPL read the shorthand and built a function. When called '
                'with 6, the function computed (* 6 6), which gave 36. The reader '
                'macro had turned the compact scratch into a working function.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="[1 #_ 2 3]",
            expected=[1, 3],
            concept_phrase="using the discard reader macro to skip an element",
            question_what="the vector after the middle element is discarded",
            goal_text="use the #_ reader macro to skip an element in a vector",
            scenario=(
                'Rex the hound scratched a vector with three bones. But the middle '
                'bone was problematic — he did not want it. So he placed the '
                'discard-mark #_ just before it. The reader would skip it entirely.'
            ),
            need=(
                'When the reader saw the #_ mark, it would consume the form '
                'immediately following and discard it. That element would be '
                'removed, leaving the others in the vector.'
            ),
            mapping=(
                'The #_ mark is the discard convention. The form after it is the '
                'one to skip. The reader takes it and throws it away. The rest '
                'of the vector remains.'
            ),
            resolution=(
                'The REPL read the vector and saw the discard-mark. It consumed the '
                'marked element and removed it. The final vector came back with the '
                'unwanted element skipped — 3.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-12 — Tagged literals
G10_12 = SubjectCurriculum(
    grade=10, subject_id="G10-12",
    subject_title="Tagged literals",
    fable="dog-shadow",
    examples=[
        # Tagged literals are read into typed values. Test predicates on them.
        SubjectExample(
            form="(inst? #inst \"2024-01-01\")",
            expected=True,
            concept_phrase="testing whether a tagged literal reads as an instant",
            question_what="whether the inst? predicate returns true",
            goal_text="test that a tagged literal with #inst reads as an instant",
            scenario=(
                'Patch the hound found a tagged scratch-mark on the bank: #inst. '
                'This was the scribe\'s way of saying "read this string as a moment '
                'in time, not just text." The string "2024-01-01" was inscribed '
                'beneath the tag.'
            ),
            need=(
                'The reader would see the #inst tag and convert the string into a '
                'proper instant (a time value). The inst? predicate would test '
                'whether the result was truly an instant.'
            ),
            mapping=(
                'The #inst tag is the reading convention. The string is the data '
                'to be tagged. The reader converts the string into an instant. The '
                'inst? test confirms the type.'
            ),
            resolution=(
                'The REPL read the tagged literal and converted "2024-01-01" into '
                'an instant. The inst? predicate returned true — the value was '
                'indeed an instant. The tag had told the reader how to interpret '
                'the string.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(uuid? #uuid \"00000000-0000-0000-0000-000000000000\")",
            expected=True,
            concept_phrase="testing whether a tagged literal reads as a uuid",
            question_what="whether the uuid? predicate returns true",
            goal_text="test that a tagged literal with #uuid reads as a uuid",
            scenario=(
                'Bell the hound discovered another tag on the scribe\'s stone: #uuid. '
                'This meant "read the string as a unique identifier, not plain text." '
                'The string was a long sequence of zeros and dashes, a classic marker '
                'for a universally unique bone.'
            ),
            need=(
                'The reader would convert the string into a proper UUID value. The '
                'uuid? predicate would confirm whether the result was truly a UUID.'
            ),
            mapping=(
                'The #uuid tag is the reading convention. The string is the UUID '
                'data to be parsed. The reader interprets the format and creates a '
                'UUID object. The uuid? test verifies the type.'
            ),
            resolution=(
                'The REPL read the tagged literal and converted the string into a UUID. The uuid? predicate returned true — the value was a proper UUID. The tag had guided the reader to parse correctly (with `00000000-0000-0000-0000-000000000000` as the input value).'
            ),
            tags=("story",),
        ),
    ],
    subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-13 — Data readers (EDN extension)
G10_13 = SubjectCurriculum(
    grade=10, subject_id="G10-13",
    subject_title="Data readers and EDN extension",
    fable="dog-shadow",
    examples=[
        # EDN read-string with a default tag handler.
        SubjectExample(
            form="(clojure.edn/read-string \"42\")",
            expected=42,
            concept_phrase="parsing a number string with edn/read-string",
            question_what="the parsed value from the EDN source",
            goal_text="use edn/read-string to parse a number from a string",
            scenario=(
                'Rex the hound held a message-bone scratched with the text "42". '
                'It was not a number yet — it was just a string of characters. He '
                'used edn/read-string to ask the reader to parse the message as '
                'Clojure data.'
            ),
            need=(
                'The edn/read-string function would read the string following the '
                'EDN conventions and convert it into a proper number. The string '
                '"42" would become the integer 42.'
            ),
            mapping=(
                'The message-bone is the string. The edn/read-string is the '
                'parsing function. The EDN format tells the reader how to interpret '
                'the scratches. The result is a parsed value.'
            ),
            resolution=(
                'The REPL passed the string to edn/read-string. The parser read the '
                'characters and recognized a number. The string was converted into '
                'the integer 42. The bone\'s message had been decoded.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(clojure.edn/read-string \"[:a :b :c]\")",
            expected=[":a", ":b", ":c"],
            concept_phrase="parsing a vector string with edn/read-string",
            question_what="the parsed vector from the EDN source",
            goal_text="use edn/read-string to parse a vector of keywords from a string",
            scenario=(
                'Patch the hound carried a message-bone scratched with "[:a :b :c]". '
                'The scratch looked like a vector of keywords, but it was still just '
                'text on the bone. Edn/read-string would parse the message and turn '
                'it into real data.'
            ),
            need=(
                'The edn/read-string function would read the string and recognize the '
                'vector notation with three keyword symbols inside. The string would '
                'become a parsed vector with three keyword values.'
            ),
            mapping=(
                'The message-bone is the string. The edn/read-string is the parser. '
                'The vector brackets and colons tell the reader what structure to '
                'build. The result is a parsed sequence of keywords.'
            ),
            resolution=(
                'The REPL passed the string to edn/read-string. The parser read the '
                'characters, recognized the vector with three keywords, and built the '
                'data structure. The message-bone was decoded into a vector of three '
                'keyword symbols.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-14 — eval
G10_14 = SubjectCurriculum(
    grade=10, subject_id="G10-14",
    subject_title="eval (the function)",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(eval '(+ 1 2 3))",
            expected=6,
            concept_phrase="evaluating a quoted form at runtime",
            question_what="the result of evaluating the quoted addition",
            goal_text="evaluate a quoted addition form at runtime",
            scenario=(
                'Bell the hound had a quoted form scratched on bark: (+ 1 2 3). '
                'The quote kept it as a form, not evaluated. But she wanted to ask '
                'the runtime to evaluate it later — not at read-time, but when she '
                'called eval explicitly.'
            ),
            need=(
                'The eval function would take the quoted form and ask the runtime '
                'to evaluate it right then. The addition would be computed, and the '
                'sum would come back as the result.'
            ),
            mapping=(
                'The quoted form is the data. The eval is the function that asks the '
                'runtime to evaluate the form. The runtime computes the addition and '
                'returns the running total.'
            ),
            resolution=(
                'The REPL called eval with the quoted form. The runtime evaluated it '
                'as an addition, computed 1 + 2 + 3, and returned 6. The quote had '
                'delayed evaluation; eval had triggered it.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(eval (list '+ 4 5))",
            expected=9,
            concept_phrase="evaluating a dynamically constructed form",
            question_what="the result of evaluating the constructed list",
            goal_text="construct a list that represents addition and evaluate it",
            scenario=(
                'Rex the hound built a form dynamically by assembling pieces: the '
                'quoted + symbol and two numbers. The list function joined them '
                'into a form. Now he wanted eval to run it.'
            ),
            need=(
                'The dynamically constructed form would be passed to eval. The eval '
                'function would ask the runtime to evaluate it as an addition and '
                'return the result.'
            ),
            mapping=(
                'The list function builds the form. The quoted + is the operator. '
                'The numbers are the operands. Eval triggers the runtime to '
                'evaluate the form.'
            ),
            resolution=(
                'The REPL constructed the list dynamically, then passed it to eval. '
                'The eval function asked the runtime to compute the operation. The '
                'dynamic form had been evaluated on demand — 5.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-15 — When NOT to write a macro
G10_15 = SubjectCurriculum(
    grade=10, subject_id="G10-15",
    subject_title="When not to write a macro",
    fable="dog-shadow",
    examples=[
        # Most of the time, a function suffices. Test forms that show
        # a function would do.
        SubjectExample(
            form="(do \"a function suffices when no syntax shaping is needed\" "
                 "((fn [x y] (+ x y)) 3 4))",
            expected=7,
            concept_phrase="calling an anonymous function to add two arguments",
            question_what="the sum of 3 and 4",
            goal_text="use an anonymous function to add two numbers",
            scenario=(
                'Patch the hound laid a quick nose-trail at the river bank: a small '
                'unnamed routine that takes two values and adds them. No macro '
                'rewriting, no scratch-mark setup — a plain function, ready to use '
                'where it was made.'
            ),
            need=(
                'Called right there with 3 and 4, the routine would add the two '
                'and hand the sum back. The trail was meant to be walked once, '
                'where it lay; a fancier macro would only get in the way.'
            ),
            mapping=(
                'An anonymous function is a nose-trail laid down and walked '
                'immediately. The parameters are the bones it accepts; the body '
                'is the trail it walks; the call hands those bones in and reads '
                'off what the body produced.'
            ),
            resolution=(
                'the routine added the two and gave back the sum — no rewrite, '
                'no scratch-mark, just the trail walked the once.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do \"prefer fn unless you must shape syntax\" "
                 "(map inc [1 2 3]))",
            expected=[2, 3, 4],
            concept_phrase="applying a function to each element of a collection",
            question_what="the incremented values",
            goal_text="use map to increment each element of a list",
            scenario=(
                'Bell the hound had a vector of bones. She wanted to increment each '
                'one. The map function would walk the nose-trail inc over every '
                'bone, applying inc to each in turn.'
            ),
            need=(
                'The map function would pair with inc and process each element. Each '
                'bone would be incremented, producing a new sequence of values.'
            ),
            mapping=(
                'The map is the function applicator. The inc is the nose-trail to '
                'follow. The vector is the bones to process. The result is a new '
                'sequence with the trail applied to each.'
            ),
            resolution=(
                'The REPL applied map with inc to the vector. Each bone was passed through the inc trail in order. The result came back with each element incremented. No macros needed — a function sufficed (with `1` as the input value) (with `3` as the input value).'
            ),
            tags=("story",),
        ),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-16 — Macro pattern library (with-X, def-X-thing)
G10_16 = SubjectCurriculum(
    grade=10, subject_id="G10-16",
    subject_title="Macro pattern library",
    fable="dog-shadow",
    examples=[
        # A `with-` style macro that binds and ensures cleanup conceptually.
        SubjectExample(
            form="(do (defmacro with-steady-pace [& body] "
                 "`(let [pace# :slow-and-steady] ~@body)) "
                 "(with-steady-pace 42))",
            expected=42,
            concept_phrase="defining and using a with-X macro pattern",
            question_what="the value returned when the with-steady-pace macro expands to a let-block and runs the body",
            goal_text="define a with-steady-pace macro and call it to execute a body",
            scenario=(
                'Rex the hound scratched a macro-pattern into the bark, named for '
                'the steady pace the pack always favoured at the river crossing. '
                'The pattern would set up a fresh pace-binding around any body it '
                'was handed, like clearing a calm patch of water before letting '
                'a bone drop.'
            ),
            need=(
                'Called with a single body, the macro would rewrite that body '
                'inside a let-block — the pace named locally, the body running '
                'inside the binding. The runtime would never see the shorthand; '
                'only the rewritten, expanded form.'
            ),
            mapping=(
                'A macro is the rewriter that runs before the runtime: the bark '
                'scratch holds the pattern, the call hands in the body, the '
                'pattern wraps the body in a fresh-pace let and submits the '
                'rewritten form for evaluation.'
            ),
            resolution=(
                "the macro rewrote the call into a pace-bound let, the body ran inside it, and the value the body produced came back as the call's answer (with `42` as the input value)."
            ),
            tags=("story",),
        ),
        # A `def-X-thing` style: macro that defs a named thing.
        SubjectExample(
            form="(do (defmacro def-pace [name v] `(def ~name ~v)) "
                 "(def-pace race-pace :slow) race-pace)",
            expected=":slow",
            concept_phrase="defining and using a def-X-thing macro pattern",
            question_what="the value of the symbol defined by def-pace when expanded with the given name and keyword value",
            goal_text="define a def-pace macro and use it to define and retrieve a value",
            scenario=(
                'Patch the hound carved another macro-pattern that would '
                'define named values. The macro would rewrite calls into def-forms.'
            ),
            need=(
                'When called with a name and value, the macro would expand to def. '
                'This would bind the name to the value globally.'
            ),
            mapping=(
                'The defmacro sets the pattern. The name is the symbol to bind. '
                'The v is the value. The backtick builds the def-form.'
            ),
            resolution=(
                'The REPL set the macro, then called it. The macro expanded to def and set the binding. A lookup returned the value. The pattern worked (with `slow` as the input value) (with `:slow` as the input value).'
            ),
            tags=("story",),
        ),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# ─────────────────────── registry ───────────────────────


SUBJECTS: dict[str, SubjectCurriculum] = {s.subject_id: s for s in (
    G10_01, G10_02, G10_03, G10_04, G10_05, G10_06, G10_07, G10_08,
    G10_09, G10_10, G10_11, G10_12, G10_13, G10_14, G10_15, G10_16,
)}


def smoke_test() -> None:
    from mmllm.aesop.curriculum.generator import generate_subject
    for sid, sub in SUBJECTS.items():
        recs = generate_subject(sub, n_per_example=1, seed=0)
        assert recs, f"no records for {sid}"
        for r in recs:
            assert r.tool_calls, f"no tool_calls for {sid}"
            assert r.tool_calls[0]["name"] == "eval"
            assert r.user_msg
            assert r.assistant_msg
    print(f"grade-10 dog-shadow smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
