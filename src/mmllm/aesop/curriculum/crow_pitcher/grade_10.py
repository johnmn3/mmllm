"""Grade 10 — macros, code as data. Through crow-pitcher.

Subplot lens: the Tortoise designs a small language. Each subject is
the Hare and Tortoise inspecting a macro, an expansion, or a piece of
syntax-quoted source. The fable's moral — patience over haste — fits
naturally: macros reward careful reading of expansions over guessing.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.crow_pitcher.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.crow_pitcher._metaphor_pools import (
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
{tortoise_phrase} had spent the morning {place} sketching a tiny
language of {tortoise_his_her} own — a notebook of macros that wrote
other forms. The next entry was {concept_phrase}. {hare_phrase} wanted to
{goal_text}. {tortoise} asked {hare_him_her} to write the form carefully
and submit it so the REPL could show what code it produced or what value it returned."""),

    SubplotTemplate("""\
"A macro is just a function that runs at compile time," {tortoise}
explained {place}, {emo_patient}. {hare}, {emo_proud}, said
{hare_he_she} could already understand what {concept_phrase} meant.
{tortoise_phrase} insisted they actually write a form to {goal_text}
and read what the runtime reported, expansion or value."""),

    SubplotTemplate("""\
The path {place} was littered with old macro definitions someone had
carved into bark. {hare_phrase} found one shaped like
{concept_phrase} and dared {tortoise_phrase} to write the form that could {goal_text}.
{tortoise} only smiled and asked {hare_him_her} to submit it carefully
into the REPL — that, after all, was the whole point of having a
macroexpander."""),

    SubplotTemplate("""\
{hare_phrase} insisted {place} that macros were the same as functions.
{tortoise_phrase}, {emo_patient}, sketched {concept_phrase} on a
strip of bark. "The difference," {tortoise_he_she} said, "is in what
we're trying to accomplish: {goal_text}. Write the form and let the
runtime tell us exactly what it does.\""""),

    SubplotTemplate("""\
A small notebook lay open {place} where the Tortoise had been studying
syntax-quote. The page showed {concept_phrase}, and a goal written in
pencil: {goal_text}. {hare_phrase}, {emo_tired}, reluctantly
agreed to write the form to settle once and for all what it produced."""),

    SubplotTemplate("""\
At a stone tablet {place}, {tortoise_phrase} was teaching
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(quote (+ 1 2))",
            expected=["+", 1, 2],
            concept_phrase="quoting an addition form",
            question_what="what you get when you quote an addition form",
            goal_text="quote an addition form so it evaluates to a list without computing",
            scenario=(
                "Korvus stood at the garden pitcher with a chalk-marked stone "
                "in one talon and the actual stone in the other. He traced the "
                "mark on the rim — the addition form scratched as a shape — "
                "not yet dropped, just named."
            ),
            need=(
                "He needed to hand back the form itself, not the computed sum. "
                "Quoting would keep the chalk mark from becoming a stone."
            ),
            mapping=(
                "`quote` is the chalk mark held up so the REPL reads the shape "
                "without evaluating it. The form stays as data — a list of symbols "
                "and numbers — rather than collapsing into a computed value."
            ),
            resolution=(
                'The chalk-marked form settled into the pitcher unevaluated, returned as a list of its parts (with `1` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="'(1 2 3)",
            expected=[1, 2, 3],
            concept_phrase="the quoted list with the numbers",
            question_what="the result of quoting a three-element list",
            goal_text="quote a list of the numbers so it returns the form itself",
            scenario=(
                "Caw perched on the orchard pitcher's rim and scratched three "
                "number-marks on the clay with her talon: a list shape, not three "
                "separate stones to drop. She used the shorthand chalk-mark — "
                "the single-quote — in front of the list."
            ),
            need=(
                "She needed the REPL to return the list shape itself, not "
                "evaluate it as a call. The chalk mark would prevent evaluation."
            ),
            mapping=(
                "The `'` reader macro is the chalk mark that tells the REPL: "
                "read this shape, do not run it. The list stays as a list of "
                "data elements returned unchanged."
            ),
            resolution=(
                "The three-element list returned intact, each number settled "
                "as data into the pitcher. (with {drawn.a} folded in)"
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
                "Sable perched at the hilltop pitcher, chalk in one talon and a "
                "live stone tucked under a wing. They scratched a syntax-quoted "
                "form on the rim with a gap: `~x` marked the spot where the "
                "wing-cache stone would drop in."
            ),
            need=(
                "Sable needed a mixed form — some parts stay as chalk marks, "
                "one part gets replaced by the wing-cached value of x."
            ),
            mapping=(
                "Syntax-quote keeps most marks as shapes; `~x` is the hole that "
                "lets the live stone fall through. The REPL builds a list where "
                "the chalk marks stay symbolic and the unquoted slot fills with "
                "the stored value."
            ),
            resolution=(
                "The mixed list settled into the pitcher: chalk marks flanking "
                "the inserted value, returned as a three-element list. (count: 5)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(let [x 10] `(+ ~x ~x))",
            expected=["+", 10, 10],
            concept_phrase="building a form by unquoting a variable twice inside syntax-quote",
            question_what="the form produced when x is 10 and unquoted twice",
            goal_text="build a form where a variable is inserted twice into an addition form",
            scenario=(
                "Korvus scratched an addition template on the village pitcher's "
                "rim: the `+` chalk mark fixed, two gaps left open for the "
                "wing-cache value. He had tucked a stone marked ten under his "
                "wing before beginning."
            ),
            need=(
                "He needed a list-form where the same stored value fills both "
                "slots, producing a template ready for the REPL to read as data."
            ),
            mapping=(
                "Syntax-quote holds the `+` as a chalk mark; each `~x` is a "
                "hole that the wing-cache fills at construction time. The result "
                "is a list-form, not a computed sum — data shaped like a call."
            ),
            resolution=(
                "The three-element list form settled into the pitcher, addition "
                "symbol first, the inserted value appearing twice. (count: 10)"
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
                "Caw had the stones tucked under her wing in a row at the "
                "meadow pitcher. She scratched a template on the rim: `list` "
                "mark first, then `~@xs` — the splice gap that would spread "
                "all wing-cache stones into the form at once."
            ),
            need=(
                "She needed all the stones spread into a single list-form, "
                "not nested — the splice mark would do the spreading without "
                "wrapping them in another layer."
            ),
            mapping=(
                "The `~@` unquote-splice opens the wing-cache and pours all "
                "held stones into the template in sequence. The resulting form "
                "is a flat list with the `list` chalk mark followed by each "
                "element."
            ),
            resolution=(
                "The four-element list form settled into the pitcher, the "
                "spliced values following the list chalk mark. (count: 3)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(do (defmacro my-when [t & body] `(if ~t (do ~@body))) "
                 "(my-when true 1 2 3))",
            expected=3,
            concept_phrase="defining a conditional macro and invoking it",
            question_what="the value the rewritten if-do form returns when the test is true and the body has three expressions",
            goal_text="define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body",
            scenario=(
                "Caw scratched a master revision rule on the pitcher's rim "
                "at the village: `my-when` — whenever this pattern appeared "
                "in a form, the talon would rewrite it before the REPL ever "
                "saw the body. The rule expanded it to an `if`."
            ),
            need=(
                "She wanted to call `(my-when true 1 2 3)` and see the "
                "rewritten form evaluated — the `if` expansion running and "
                "returning the last body expression."
            ),
            mapping=(
                "`defmacro` installs the rewrite-rule. When the REPL "
                "encounters `my-when`, it runs the macro first and produces "
                "the expansion. The expansion is what evaluates — the macro's "
                "return is code, not a value."
            ),
            resolution=(
                "3 — the rewrite ran, the `if` expanded, the last body form "
                "evaluated and dropped into the pitcher. (count: 3)"
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
                "Korvus scratched a rewrite-rule called `twice` on the farm "
                "pitcher's rim: any form carrying it would be rewritten so "
                "the argument appeared twice inside a do-block before the "
                "REPL ever saw the call."
            ),
            need=(
                "He needed to call `(twice 7)` and confirm that the rewrite "
                "ran first, the do-block evaluated both copies, and the last "
                "copy's value returned."
            ),
            mapping=(
                "`defmacro` installs the twice rule. The REPL rewrites "
                "`(twice 7)` into `(do 7 7)` before evaluation — the macro "
                "returns a form, never a value; only the expanded form runs."
            ),
            resolution=(
                "The expanded do-block ran, both copies evaluated, and the "
                "value of the final expression settled into the pitcher. (count: 7)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(macroexpand-1 '(when true 1))",
            expected=["if", True, ["do", 1]],
            concept_phrase="the one-step expansion of the when-macro call",
            question_what="the expanded form after one level of macro expansion",
            goal_text="expand a when-macro call one step to see what code it produces",
            scenario=(
                "Sable perched on the market pitcher's rim holding a chalk-marked "
                "form: `(when true 1)`. They wanted to ask the macroexpander to "
                "show the rewrite-rule's first step without running the result — "
                "just the expanded form returned as data."
            ),
            need=(
                "Sable needed to see the code that `when` produces after one "
                "rewrite pass, to confirm the rule transformed the call correctly "
                "before any evaluation happened."
            ),
            mapping=(
                "`macroexpand-1` asks the REPL to apply the rewrite-rule exactly "
                "once and return the produced form as data. The rewritten code is "
                "the answer — a chalk-marked if-form, never a value."
            ),
            resolution=(
                "The one-step rewrite settled into the pitcher as a list-form, "
                "the if-shape with its do-wrapped body returned as data. (count: -1)"
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
                "Korvus scratched `(or a b)` as a chalk mark on the hilltop "
                "pitcher's rim and asked the macroexpander to show what the "
                "rewrite-rule made of it in one pass — the internal machinery "
                "of `or` laid bare as a form."
            ),
            need=(
                "He needed to see the let-and-if structure that `or` secretly "
                "produces, without evaluating any of it — just the raw "
                "expansion returned as data."
            ),
            mapping=(
                "`macroexpand-1` applies the `or` rewrite-rule once and returns "
                "the produced form. The REPL never evaluates `a` or `b` — it "
                "shows the code the rule wrote, as a chalk-marked list."
            ),
            resolution=(
                "The nested let-if form settled into the pitcher as data, "
                "the one-step rewrite complete and returned unevaluated. (count: -1)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(macroexpand '(when true 1))",
            expected=["if", True, ["do", 1]],
            concept_phrase="the complete expansion of the when-macro call",
            question_what="the fully expanded form after all macro passes",
            goal_text="fully expand a when-macro call to reveal the if-form it becomes",
            scenario=(
                "Caw chalked `(when true 1)` on the road pitcher's rim and "
                "demanded to see the full rewrite — every macro pass applied "
                "until no rewrite-rule remained. She passed it to `macroexpand` "
                "rather than the one-step version."
            ),
            need=(
                "She needed the completely expanded form returned as data — "
                "all rewrite-rules applied until only primitive forms remained, "
                "nothing left to rewrite."
            ),
            mapping=(
                "`macroexpand` applies every rewrite-rule in sequence until "
                "the form has no macro calls left. The result is the final "
                "chalk-marked shape the REPL would actually evaluate."
            ),
            resolution=(
                "The fully expanded if-do form settled into the pitcher as "
                "data, all rewrite passes complete."
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
                "Sable chalk-marked `(-> 1 inc inc)` on the orchard pitcher "
                "and passed it to the full macroexpander. They wanted to see "
                "what nested structure the threading macro actually wrote — "
                "the drop-order laid out explicitly as data."
            ),
            need=(
                "Sable needed to see every threading rewrite applied, the "
                "fully composed nesting returned as a form before any stone "
                "dropped."
            ),
            mapping=(
                "`macroexpand` unrolls the `->` rewrite-rule fully, producing "
                "the nested call structure that the REPL would evaluate. The "
                "threading syntax disappears; what remains is explicit nesting."
            ),
            resolution=(
                "The nested function-call form settled into the pitcher, "
                "threading rewritten to explicit nesting and returned as data."
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(when true 1 2 3)",
            expected=3,
            concept_phrase="executing multiple expressions when a condition is true",
            question_what="the result of the last expression when the condition holds",
            goal_text="execute three expressions and return the value of the last when the condition is true",
            scenario=(
                "Korvus perched at the garden pitcher, the stones in a row "
                "on the rim. The `when` rewrite-rule would rewrite the call "
                "to an if-do before the REPL evaluated it, then run all three "
                "expressions in sequence."
            ),
            need=(
                "He needed to know which stone the pitcher would hold when the "
                "condition was true — the rule would ensure all three ran and "
                "the last settled."
            ),
            mapping=(
                "`when` is a rewrite-rule that transforms the call to `(if true "
                "(do 1 2 3))`. The REPL evaluates the expansion: all body "
                "expressions run, and the last expression's value drops into "
                "the pitcher."
            ),
            resolution=(
                "The rewrite ran, the do-block executed all three forms, and "
                "the final expression's value settled into the pitcher. (with {drawn.a} folded in)"
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
                "Caw dropped a false-stone first on the village pitcher's rim "
                "before the three body stones. The `when` rule would rewrite "
                "the call; with a false condition the if-branch would skip "
                "the body entirely."
            ),
            need=(
                "She needed to confirm that when the condition stone was false, "
                "no body expression ran and the pitcher held nothing — the rule "
                "would ensure the body was never reached."
            ),
            mapping=(
                "`when` rewrites to `(if false (do 1 2 3))`. With the condition "
                "false, the `if` takes the else branch, which does not exist — "
                "so nothing evaluates and nothing drops."
            ),
            resolution=(
                "The false condition blocked the body; no value settled, and "
                "the pitcher returned empty. (with {drawn.a} folded in)"
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
                "Sable scratched `when-not` on the meadow pitcher's rim with "
                "a false-stone as the condition and a keyword-stone as the "
                "body. The negated-condition rule would rewrite the call so "
                "a false input meant the body would run."
            ),
            need=(
                "Sable needed to verify that `when-not` inverted the gate — "
                "with a false condition, the body expression would execute and "
                "its value drop into the pitcher."
            ),
            mapping=(
                "`when-not` rewrites to a negated-condition if-form. When the "
                "condition is false, the negation is true, so the body runs. "
                "The keyword stone drops as the result."
            ),
            resolution=(
                'The negation gate opened, the body ran, and the keyword value settled into the pitcher (with `ok` as the input value) (with `:ok` as the input value).'
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(-> 5 inc inc inc)",
            expected=8,
            concept_phrase="threading a value through multiple functions in sequence",
            question_what="the result of threading 5 through three increments",
            goal_text="thread the value 5 through inc three times using thread-first",
            scenario=(
                "Korvus set a stone marked five on the hilltop pitcher's rim "
                "and scratched a drop-order: pass it through `inc` once, then "
                "again, then once more. The `->` rewrite-rule would compose "
                "the steps before the REPL evaluated."
            ),
            need=(
                "He needed to know the final water level after the stone passed "
                "through all three increments — the threading rule would rewrite "
                "the steps into nested calls first."
            ),
            mapping=(
                "`->` is a rewrite-rule that nests the calls: `(inc (inc (inc "
                "5)))`. Each step's output feeds the next as the first argument. "
                "The REPL evaluates only the expanded nesting."
            ),
            resolution=(
                "The threaded nesting evaluated, each increment applied in "
                "turn, and the final value settled into the pitcher. (with {drawn.a} folded in)"
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
                "Caw lined up the stones at the farm pitcher and scratched "
                "a last-argument drop-order: sieve the evens, raise each by "
                "one, then tally the results. The `->>` rewrite-rule would "
                "compose the whole pipeline."
            ),
            need=(
                "She needed the final tally after the sieve and the raise — "
                "the thread-last rule would rewrite the pipeline so each step "
                "passed its collection to the next as last argument."
            ),
            mapping=(
                "`->>` rewrites each step to append the prior result as the "
                "last argument. Filter keeps even stones, map raises each, "
                "reduce tallies them all. Only the expanded nesting runs."
            ),
            resolution=(
                'The pipeline ran through all three steps and the final tally settled into the pitcher (with `1` as the input value) (with `3` as the input value).'
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
                "Sable chalk-marked `(-> x f g)` on the market pitcher and "
                "handed it to the macroexpander. They wanted to see the "
                "rewrite-rule's result as data — the explicit nesting that "
                "threading secretly produces."
            ),
            need=(
                "Sable needed the fully expanded form returned as a chalk mark, "
                "not evaluated — showing how `->` composes calls into nesting."
            ),
            mapping=(
                "`macroexpand` applies the `->` rewrite-rule and returns the "
                "produced form as data. The threading syntax disappears; "
                "the explicit nested call structure appears as a list-form."
            ),
            resolution=(
                "The expanded nested-call form settled into the pitcher as "
                "data, threading rewritten to explicit composition."
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
    fable="crow-pitcher",
    examples=[
        # A function evaluates its args; a macro receives unevaluated forms.
        SubjectExample(
            form="(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))",
            expected=7,
            concept_phrase="calling a plain function that adds two numbers",
            question_what="the sum returned by calling add-fn with arguments 3 and 4",
            goal_text="define a function add-fn and call it to add 3 and 4",
            scenario=(
                "Korvus scratched a drop-order named `add-fn` on the garden "
                "pitcher: two stones in, their sum out. No rewriting involved — "
                "a plain drop-order evaluated its arguments before running "
                "the body."
            ),
            need=(
                "He needed to confirm that calling the drop-order with stones "
                "three and four would raise the water by the sum — arguments "
                "evaluated first, then the body."
            ),
            mapping=(
                "`defn` defines a plain drop-order: arguments are evaluated "
                "stones before the body runs. No rewrite-rule is involved — "
                "the REPL evaluates 3 and 4, then adds them."
            ),
            resolution=(
                "The two stones evaluated and combined; the sum settled "
                "into the pitcher."
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
                "Caw scratched a rewrite-rule named `add-mac` on the orchard "
                "pitcher's rim: whenever this pattern appeared, the talon would "
                "rewrite it to an addition form before the REPL evaluated — the "
                "arguments never evaluated until after the rewrite."
            ),
            need=(
                "She needed to confirm that after the rewrite, the produced "
                "addition form evaluated correctly — the macro's rewrite "
                "happening first, the sum computed second."
            ),
            mapping=(
                "`defmacro` installs a rewrite-rule: `add-mac` receives "
                "unevaluated forms and emits an addition form. The REPL "
                "rewrites first, then evaluates the produced addition."
            ),
            resolution=(
                'The rewrite produced an addition form; the expanded form evaluated and the sum settled into the pitcher. (with 3 folded in)'
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
    fable="crow-pitcher",
    examples=[
        # gensym always returns a fresh symbol; we test symbol? predicate.
        SubjectExample(
            form="(symbol? (gensym))",
            expected=True,
            concept_phrase="testing whether gensym produces a symbol",
            question_what="whether a generated symbol is of type symbol",
            goal_text="test that gensym returns a symbol",
            scenario=(
                "Sable pressed a talon to the village pitcher's rim and asked "
                "the REPL to mint a fresh chalk-mark — a `gensym` — one that "
                "no other form had ever used. Then Sable checked what kind "
                "of thing the fresh mark was."
            ),
            need=(
                "Sable needed to know whether the minted mark was truly a "
                "symbol — the kind of chalk mark that names things — rather "
                "than some other value."
            ),
            mapping=(
                "`gensym` produces a fresh symbol that the REPL has never "
                "seen before. `symbol?` checks the chalk-mark kind: is this "
                "a naming-mark or something else? The predicate answers."
            ),
            resolution=(
                "The predicate confirmed the minted mark was a symbol; truth "
                "settled into the pitcher."
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
                "Korvus minted two fresh chalk-marks at the meadow pitcher, "
                "both starting with the same prefix scratch `x_`. He tucked "
                "each under a separate wing and then compared them, asking "
                "if the two marks were the same mark."
            ),
            need=(
                "He needed to know whether two gensyms with the same prefix "
                "were identical — whether the REPL minted one mark or two "
                "distinct ones."
            ),
            mapping=(
                "Each `gensym` call mints a unique chalk-mark even with the "
                "same prefix. The two wing-cached marks are distinct symbols. "
                "`=` compares the actual marks — same prefix, different identity."
            ),
            resolution=(
                "The comparison settled false into the pitcher: two minted "
                "marks with the same prefix are never the same mark."
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
    fable="crow-pitcher",
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
                "Caw scratched a rewrite-rule at the road pitcher: "
                "`safe-if-let` — a rule that rewrote its call to `if-let` "
                "using the caller's own explicit binding name, not an "
                "invisible injected mark that could clash."
            ),
            need=(
                "She needed to call `(safe-if-let [x 5] (* x 2) 0)` and "
                "confirm the rewrite produced a hygienic `if-let` that bound "
                "`x` to five and ran the then-branch."
            ),
            mapping=(
                "A hygienic rewrite-rule uses only the names the caller "
                "supplies — no secretly injected marks. `safe-if-let` rewrites "
                "to `if-let` with the caller's binding, then the REPL evaluates "
                "the expanded form."
            ),
            resolution=(
                "The hygienic expansion ran, the binding succeeded, and the "
                "then-branch value settled into the pitcher."
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
                "Sable perched at the hilltop pitcher and used the built-in "
                "`if-let` directly — no rewrite-rule of their own needed. They "
                "bound `x` to a stone marked seven and wrote the then-branch "
                "to square it."
            ),
            need=(
                "Sable needed to confirm that when the binding succeeded, the "
                "then-branch ran and returned the square of the bound value, "
                "not the else stone."
            ),
            mapping=(
                "`if-let` binds the name to the value under a wing; if binding "
                "succeeds, the then-branch evaluates with `x` holding the stone. "
                "The multiplication runs with the wing-cached value."
            ),
            resolution=(
                'The binding succeeded, the then-branch evaluated, and the squared value settled into the pitcher (with `7` as the input value).'
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
    fable="crow-pitcher",
    examples=[
        # Reader macros: ', `, ~, #(...), #_, etc. Test what they read to.
        SubjectExample(
            form="'(1 2 3)",
            expected=[1, 2, 3],
            concept_phrase="using the quote reader macro",
            question_what="the form read by the quote reader",
            goal_text="use the quote reader macro to read a list of the numbers",
            scenario=(
                "Korvus pressed the single-quote talon-mark before a "
                "three-number list on the garden pitcher. This scribe's "
                "convention told the reader to hand back the form itself "
                "without evaluating — the notation expanded before the "
                "REPL ever saw the list."
            ),
            need=(
                "He needed to confirm that the reader convention turned "
                "the shorthand mark into a quoted list returned as data — "
                "the numbers present, no evaluation done."
            ),
            mapping=(
                "The `'` is a pitcher-notation that the reader expands to "
                "`(quote ...)` before the REPL evaluates. The scribe convention "
                "is applied at read time; the REPL sees only the expanded form."
            ),
            resolution=(
                "The reader expanded the notation; the three-number list "
                "settled into the pitcher as data. (with {drawn.a} folded in)"
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
                "Caw scratched `#(* % %)` on the orchard pitcher's clay — "
                "the scribe notation for an anonymous drop-order that the "
                "reader would expand to a full `fn` form before the REPL "
                "evaluated it, then called immediately with a stone."
            ),
            need=(
                "She needed to confirm that the reader convention created a "
                "working drop-order and that calling it with a stone returned "
                "the stone multiplied by itself."
            ),
            mapping=(
                "`#(...)` is a pitcher-notation the reader expands to `(fn "
                "[%] ...)`. The REPL evaluates the expanded fn form, which "
                "becomes a callable drop-order. `%` receives the argument stone."
            ),
            resolution=(
                'The reader expanded the notation, the drop-order ran with the argument, and the squared value settled into the pitcher (with `6` as the input value).'
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
                "Sable scratched a three-element list on the meadow pitcher "
                "with a discard-notation before the middle stone: `#_`. The "
                "scribe convention meant the reader would remove that stone "
                "entirely before the REPL saw the vector."
            ),
            need=(
                "Sable needed to confirm the discard notation made the reader "
                "skip the marked element — the REPL would receive only the "
                "remaining elements as a vector."
            ),
            mapping=(
                "`#_` is a pitcher-notation applied at read time. The reader "
                "discards the next form entirely before passing the vector to "
                "the REPL. The REPL never sees the discarded stone."
            ),
            resolution=(
                'The reader removed the middle stone; the two-element vector settled into the pitcher (with `1` as the input value) (with `3` as the input value).'
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
    fable="crow-pitcher",
    examples=[
        # Tagged literals are read into typed values. Test predicates on them.
        SubjectExample(
            form="(inst? #inst \"2024-01-01\")",
            expected=True,
            concept_phrase="testing whether a tagged literal reads as an instant",
            question_what="whether the inst? predicate returns true",
            goal_text="test that a tagged literal with #inst reads as an instant",
            scenario=(
                "Korvus pressed the `#inst` notation before a date-string on "
                "the village pitcher: a scribe's tagged mark that the reader "
                "would convert to an instant-value before the REPL ever "
                "touched the string. Then he checked its type."
            ),
            need=(
                "He needed to confirm that the reader convention transformed "
                "the tagged string into an instant-type value, so the "
                "type-predicate would find it correctly typed."
            ),
            mapping=(
                "`#inst` is a pitcher-notation the reader expands into a "
                "typed instant value at read time. `inst?` tests whether the "
                "resulting value belongs to the instant type — the predicate "
                "sees the already-converted value."
            ),
            resolution=(
                'The predicate confirmed the tagged literal read as an instant; truth settled into the pitcher. (count: 2024) (with `2024-01-01` as the input value)'
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
                "Caw pressed the `#uuid` notation before a uuid-string on the "
                "market pitcher: the reader's scribe convention that converted "
                "the string into a uuid-type value before the REPL evaluated "
                "the predicate call."
            ),
            need=(
                "She needed to confirm that the reader notation produced a "
                "uuid-typed value the predicate could recognize — not a string "
                "but a properly typed mark."
            ),
            mapping=(
                "`#uuid` is a pitcher-notation applied by the reader, producing "
                "a uuid-type value. `uuid?` tests the type of what the reader "
                "produced — the REPL receives the converted value, not the string."
            ),
            resolution=(
                'The predicate confirmed the tagged literal read as a uuid; truth settled into the pitcher (with `00000000-0000-0000-0000-000000000000` as the input value).'
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
    fable="crow-pitcher",
    examples=[
        # EDN read-string with a default tag handler.
        SubjectExample(
            form="(clojure.edn/read-string \"42\")",
            expected=42,
            concept_phrase="parsing a number string with edn/read-string",
            question_what="the parsed value from the EDN source",
            goal_text="use edn/read-string to parse a number from a string",
            scenario=(
                "Sable found a strip of bark at the farm with talon-scratched "
                "characters: the string `\"42\"`. They pressed it to the "
                "pitcher and asked the scribe's EDN reader to decipher the "
                "scratches into a proper value."
            ),
            need=(
                "Sable needed the reader to parse the bark-scratch and return "
                "an actual number-stone, not the string of characters — the "
                "EDN notation conventions would convert the mark to a value."
            ),
            mapping=(
                "`edn/read-string` applies the EDN reading conventions to "
                "the string of characters, producing the value those characters "
                "denote. The scribe-mark `\"42\"` becomes a number-stone at "
                "read time."
            ),
            resolution=(
                "The EDN reader parsed the scratches and the number-stone "
                "settled into the pitcher."
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
                "Korvus found bark-scratches at the road that spelled out a "
                "vector of keyword marks: `\"[:a :b :c]\"`. He pressed the "
                "strip to the pitcher and asked the EDN reader to parse the "
                "notation into actual values."
            ),
            need=(
                "He needed the reader to convert the characters on the bark "
                "into a proper vector of keyword-stones — the EDN conventions "
                "would turn the string representation into structured data."
            ),
            mapping=(
                "`edn/read-string` applies EDN reading conventions to the "
                "string, producing a vector of keyword values. The scribe-marks "
                "become keyword-stones arranged in a collection."
            ),
            resolution=(
                "The EDN reader parsed the bark-scratches and a three-keyword "
                "vector settled into the pitcher. (count: 3)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(eval '(+ 1 2 3))",
            expected=6,
            concept_phrase="evaluating a quoted form at runtime",
            question_what="the result of evaluating the quoted addition",
            goal_text="evaluate a quoted addition form at runtime",
            scenario=(
                "Caw held a chalk-marked addition form as data on the meadow "
                "pitcher's rim — a quoted list, not yet run. She used `eval` "
                "to hand the chalk mark back to the REPL to run as code."
            ),
            need=(
                "She needed the chalk-marked form treated as code at runtime, "
                "not as stored data. `eval` would bridge the gap."
            ),
            mapping=(
                "`eval` takes a data form and submits it to the REPL as code. "
                "The quoted addition, held as a chalk mark, is evaluated as "
                "if freshly scratched on the rim."
            ),
            resolution=(
                'The chalk mark evaluated as code; the addition ran and the sum settled into the pitcher (with `1` as the input value) (with `3` as the input value).'
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
                "Sable built a form dynamically at the village pitcher — "
                "assembling a chalk mark from parts at runtime: the `+` symbol "
                "and two number-stones arranged into a list. Then they handed "
                "the assembled mark to `eval` to run."
            ),
            need=(
                "Sable needed to confirm that a form constructed as data at "
                "runtime could be executed as code through `eval` — building "
                "and running a form dynamically."
            ),
            mapping=(
                "`list` assembles the data form from parts; `eval` submits "
                "the assembled chalk mark to the REPL as code. The constructed "
                "form evaluates just as if it had been written directly."
            ),
            resolution=(
                'The assembled form evaluated as code; the sum settled into the pitcher (with `4` as the input value).'
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
    fable="crow-pitcher",
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
                "Korvus held a rewrite-rule stone in one talon and a plain "
                "drop-order stone in the other at the orchard pitcher. The "
                "task was simple addition — no syntax shaping needed. He set "
                "the rewrite-rule stone down and used the drop-order directly."
            ),
            need=(
                "He needed to add two numbers and raise the water — no syntax "
                "needed rewriting, so a plain drop-order was sufficient and "
                "the rewrite-rule would only add weight."
            ),
            mapping=(
                "When no syntax shaping is required, a plain `fn` drop-order "
                "suffices — it evaluates arguments and returns a value. A "
                "rewrite-rule is only warranted when the form itself must change "
                "before evaluation."
            ),
            resolution=(
                'The plain drop-order evaluated both arguments and the sum settled into the pitcher (with `3` as the input value).'
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
                "Caw stood at the hilltop pitcher with the stones in a row. "
                "She wanted each one raised by one notch. `map` would pass "
                "each stone through `inc` in turn — no rewrite-rule, just "
                "a higher-order drop-order doing the work."
            ),
            need=(
                "She needed each stone incremented and returned as a sequence — "
                "a plain higher-order function would do the job without any "
                "syntax rewriting."
            ),
            mapping=(
                "`map` applies a drop-order to each element of the collection "
                "in turn, collecting the results. No rewrite-rule is involved — "
                "the arguments evaluate before `map` runs."
            ),
            resolution=(
                "Each stone passed through the increment drop-order; the raised "
                "sequence settled into the pitcher. (with {drawn.a} folded in)"
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
    fable="crow-pitcher",
    examples=[
        # A `with-` style macro that binds and ensures cleanup conceptually.
        SubjectExample(
            form="(do (defmacro with-tortoise-pace [& body] "
                 "`(let [pace# :slow-and-steady] ~@body)) "
                 "(with-tortoise-pace 42))",
            expected=42,
            concept_phrase="defining and using a with-X macro pattern",
            question_what="the value returned when with-tortoise-pace expands to a let-block and runs the body",
            goal_text="define a with-tortoise-pace macro and call it to execute a body",
            scenario=(
                "Sable scratched a `with-` rewrite-rule on the farm pitcher: "
                "`with-tortoise-pace` — a pattern that would rewrite any call "
                "into a let-block with a gensym-safe binding before evaluating "
                "the body expressions."
            ),
            need=(
                "Sable needed to confirm that calling the pattern with a body "
                "would produce the let-wrapped expansion and return the body's "
                "value — the with-pattern doing its setup rewrite first."
            ),
            mapping=(
                "`with-` macros are rewrite-rules that wrap body expressions "
                "in a let-block, establishing bindings before running the body. "
                "The `pace#` gensym keeps the binding hygienic. The REPL "
                "evaluates only the expansion."
            ),
            resolution=(
                "The with-pattern expansion ran, the let-block wrapped the body, and the body's value settled into the pitcher (with `42` as the input value)."
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
                "Korvus scratched a `def-` rewrite-rule at the village "
                "pitcher: a pattern rewriting its call to a `def` form."
            ),
            need=(
                "He needed to confirm the pattern posted the binding "
                "and reading the name returned its bound value."
            ),
            mapping=(
                "`def-` macros expand to `def` forms posting road-sign "
                "bindings. The REPL evaluates the expansion, then the "
                "symbol resolves to its bound value."
            ),
            resolution=(
                "The rewrite-pattern posted the binding; reading "
                "the symbol returned its bound value. (the keyword :slow)"
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
    print(f"grade-10 crow-pitcher smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
