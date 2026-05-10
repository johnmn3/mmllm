"""Grade 10 — macros, code as data. through the milkmaid fable.

Subplot lens: the Farmer designs a small language. Each subject is
the Milkmaid and Farmer inspecting a macro, an expansion, or a piece of
syntax-quoted source. The fable's moral — patience over haste — fits
naturally: macros reward careful reading of expansions over guessing.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.milkmaid.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.milkmaid._metaphor_pools import (
    _CHALKMARK_SUBPLOTS, _RECIPE_SUBPLOTS, _REWRITERULE_SUBPLOTS, _SCRIBE_SUBPLOTS,
)


# ─────────────────────── grade-10 subplot extensions ───────────────────────
#
# The Farmer has been quietly designing a small language inside
# Clojure. The Milkmaid keeps wanting to skip past the expansion step and
# just guess what the macro returns. Each template lets the form
# carry the technical detail while the fable carries the manner.

_MACRO_SUBPLOTS: list[SubplotTemplate] = list(_GOAL_SUBPLOTS) + [

    SubplotTemplate("""\
{farmer_phrase} had spent the morning {place} sketching a tiny
language of {farmer_his_her} own — a notebook of macros that wrote
other forms. The next entry was {concept_phrase}. {milkmaid_phrase}, {emo_boastful} wanted to
{goal_text}. {farmer} asked {milkmaid_him_her} to write the form carefully
and submit it so the REPL could show what code it produced or what value it returned."""),

    SubplotTemplate("""\
"A macro is just a function that runs at compile time," {farmer}
explained {place}, {emo_patient}. {milkmaid}, {emo_proud}, said
{milkmaid_he_she} could already understand what {concept_phrase} meant.
{farmer_phrase} insisted they actually write a form to {goal_text}
and read what the runtime reported, expansion or value."""),

    SubplotTemplate("""\
The path {place} was littered with old macro definitions someone had
carved into bark. {milkmaid_phrase}, {emo_boastful} found one shaped like
{concept_phrase} and dared {farmer_phrase} to write the form that could {goal_text}.
{farmer} only smiled and asked {milkmaid_him_her} to submit it carefully
into the REPL — that, after all, was the whole point of having a
macroexpander."""),

    SubplotTemplate("""\
{milkmaid_phrase} insisted {place} that macros were the same as functions.
{farmer_phrase}, {emo_patient}, sketched {concept_phrase} on a
strip of bark. "The difference," {farmer_he_she_cap} said, "is in what
we're trying to accomplish: {goal_text}. Write the form and let the
runtime tell us exactly what it does.\""""),

    SubplotTemplate("""\
A small notebook lay open {place} where the Farmer had been studying
syntax-quote. The page showed {concept_phrase}, and a goal written in
pencil: {goal_text}. {milkmaid_phrase}, {emo_tired}, reluctantly
agreed to write the form to settle once and for all what it produced."""),

    SubplotTemplate("""\
At a stone tablet {place}, {farmer_phrase} was teaching
{milkmaid_phrase}, {emo_boastful} the discipline of expansion: never trust your eyes, only
the macroexpander. The day's challenge was simple: {goal_text}. The
form that accomplishes {concept_phrase} had to be submitted; nothing
else would do."""),
]


def _ex(form, expected, concept, what, goal=""):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal)


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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(quote (+ 1 2))",
            expected=["+", 1, 2],
            concept_phrase="quoting an addition form",
            question_what="what you get when you quote an addition form",
            goal_text="quote an addition form so it evaluates to a list without computing",
            scenario=(
                "The farmer had chalked the word 'add' on the outside of a pail "
                "and pointed at the chalk mark. The milkmaid reached for the pail "
                "to pour out its contents, but the farmer stopped her hand."
            ),
            need=(
                "She needed to return the chalk mark itself — the label on the pail — "
                "not the milk inside. Quoting the form meant handing back the mark, "
                "not computing what the addition would yield."
            ),
            mapping=(
                "`quote` is the chalk mark on the pail: it gives back the written "
                "label — the list of symbols — without opening the pail to compute "
                "the value. The mark and the milk are never the same thing."
            ),
            resolution=(
                'The REPL handed back the chalk mark itself — a list of the symbol and its two arguments, with no arithmetic performed (with `1` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="'(1 2 3)",
            expected=[1, 2, 3],
            concept_phrase="the quoted list with several numbers",
            question_what="the result of quoting a three-element list",
            goal_text="quote a list of several numbers so it returns the form itself",
            scenario=(
                "Three tally-marks were chalked on the dairy wall beside three pails. "
                "The milkmaid read the marks aloud but never lifted a lid. The farmer "
                "asked her what she held in her hand."
            ),
            need=(
                "She needed to carry the three chalk marks as written — not pour "
                "any pail, not sum any tally. The quote reader macro was the "
                "shorthand the scribe had drawn to mean 'take the marks, not the milk.'"
            ),
            mapping=(
                "The `'` mark on the dairy wall is the scribe's shorthand for "
                "`quote`: it tells the reader to return the written tally — the "
                "list of numbers as chalk marks — leaving every pail sealed."
            ),
            resolution=(
                "The REPL returned the three marks exactly as written, a sealed "
                "list with no pail opened and no value computed — 3."
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
                "The farmer had labeled a pail template in chalk — two slots marked "
                "'a' and 'b' on the outside, and a hole left in the middle. The "
                "milkmaid poured milk into the hole using a ladle labeled 'x'."
            ),
            need=(
                "The template needed one live value poured in while the surrounding "
                "chalk marks stayed as labels. The `~` unquote was the hole cut in "
                "the chalk-labeled template so one real value could fill it."
            ),
            mapping=(
                "Syntax-quote is the chalk template — it labels positions without "
                "computing them. Unquote (`~`) opens a hole in the template and "
                "pours in the live value of `x`, while `a` and `b` remain marks."
            ),
            resolution=(
                "The REPL filled the template: the two chalk marks stayed as "
                "symbols and the hole received the value bound to `x`, returning "
                "a three-element list — 5."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(let [x 10] `(+ ~x ~x))",
            expected=["+", 10, 10],
            concept_phrase="building a form by unquoting a variable twice inside syntax-quote",
            question_what="the form produced when x is 10 and unquoted twice",
            goal_text="build a form where a variable is inserted twice into an addition form",
            scenario=(
                "The farmer had drawn a pail template chalked with the addition "
                "mark and two side-by-side holes. The milkmaid carried a single "
                "ladle labeled 'x' and poured the same measure into both holes."
            ),
            need=(
                "The template needed the same live value poured into two positions. "
                "Each `~x` was a separate hole cut in the chalk template, and the "
                "milkmaid's ladle had to fill both from the same bound pail."
            ),
            mapping=(
                "Syntax-quote is the chalk mark that outlines the template; each "
                "`~x` is a hole opened in that template. Both holes receive the "
                "same poured value, so the resulting form carries the live number "
                "in two positions."
            ),
            resolution=(
                "The REPL returned the completed template — the addition mark "
                "followed by the poured value appearing twice, exactly as the "
                "two holes had been filled — 10."
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
                "The farmer had a pail template chalked with a 'list' label and "
                "a wide opening at the side. The milkmaid carried three smaller "
                "pails labeled '1', '2', and '3' and upended all three through "
                "the opening at once."
            ),
            need=(
                "The template needed every pail from the row poured in as separate "
                "contents, not bundled together. The `~@` splice was the wide "
                "opening that let all three flow in individually rather than as "
                "a nested batch."
            ),
            mapping=(
                "Syntax-quote is the chalk-marked template; `~@` is the splice "
                "opening — it unrolls the vector so each element enters the "
                "template as its own position, not as a nested pail inside "
                "the existing one."
            ),
            resolution=(
                "The REPL returned the expanded template — the list label followed "
                "by each of the several elements laid out individually, exactly as "
                "the splice had poured them in."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(do (defmacro my-when [t & body] `(if ~t (do ~@body))) "
                 "(my-when true 1 2 3))",
            expected=3,
            concept_phrase="defining a conditional macro and invoking it",
            question_what="the value the rewritten if-do form returns when the test is true and the body has three expressions",
            goal_text="define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body",
            scenario=(
                "Before the milkmaid could nod and spill the pail, the farmer "
                "rewrote her daydream: 'I will give you a shorthand, `my-when`, "
                "that expands into `if` before the runtime ever reads it.'"
            ),
            need=(
                "She needed a rule that would rewrite `(my-when true 1 2 3)` into "
                "`(if true (do 1 2 3))` at read-time — a template stamp, not a "
                "function call."
            ),
            mapping=(
                "`defmacro` is the farmer's rewrite rule: it intercepts the form "
                "before evaluation, expands the shorthand into the full idiom, and "
                "hands the expanded form to the runtime. The runtime sees `if`, "
                "never `my-when`."
            ),
            resolution=(
                "The REPL evaluated the expanded form and returned the last body "
                "expression — the rewrite had run silently before the runtime "
                "arrived, and the result came back cleanly."
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
                "The farmer had stamped a rewrite rule on a strip of bark: "
                "any shorthand reading `(twice ...)` was to be replaced by a "
                "`do` block that ran the argument twice before the dairy opened."
            ),
            need=(
                "The milkmaid needed a rule that would intercept `(twice 7)` "
                "at read-time and expand it into two sequential steps — the "
                "farmer's stamp had to reshape the shorthand before the runtime "
                "ever saw it."
            ),
            mapping=(
                "`defmacro` is the farmer's rewrite rule stamped on bark: it "
                "intercepts the shorthand form, unfolds it into the expanded "
                "shape, and hands only the expanded form to the runtime. "
                "The runtime never sees `twice` — only the `do` block."
            ),
            resolution=(
                "The REPL ran the expanded do-block and returned the value of "
                "the last expression — the rewrite had already happened silently "
                "before evaluation began."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(macroexpand-1 '(when true 1))",
            expected=["if", True, ["do", 1]],
            concept_phrase="the one-step expansion of the when-macro call",
            question_what="the expanded form after one level of macro expansion",
            goal_text="expand a when-macro call one step to see what code it produces",
            scenario=(
                "The farmer had chalked a shorthand on bark — `when` with "
                "test and body. The milkmaid asked what it truly meant."
            ),
            need=(
                "She needed the farmer's rewrite rule to run once on the "
                "shorthand, showing the expanded intermediate form."
            ),
            mapping=(
                "`macroexpand-1` is the farmer's single-pass stamp: it "
                "rewrites the shorthand one step and hands back the "
                "expanded shape without further evaluation."
            ),
            resolution=(
                "The REPL handed back the expanded form — the `if` with "
                "its nested `do` block exactly as the rewrite produced."
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
                "The farmer had written the `or` shorthand on bark and "
                "pinned it above the dairy door. The milkmaid knew `or` "
                "was a macro but had never seen what shape it stamped "
                "before the runtime arrived."
            ),
            need=(
                "She needed the farmer's rewrite rule to run once on "
                "the `or` shorthand, exposing the intermediate form with "
                "its generated binding — one stamp, no deeper expansion."
            ),
            mapping=(
                "`macroexpand-1` is the farmer's single-pass stamp: it "
                "rewrites the chalk shorthand into the first expanded "
                "shape, revealing the hidden `let*` and generated symbol "
                "the runtime will eventually see."
            ),
            resolution=(
                "The REPL returned the one-step expansion — a `let*` "
                "binding a generated symbol followed by a nested `if` "
                "guard, exactly as one pass of the rewrite rule produced."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(macroexpand '(when true 1))",
            expected=["if", True, ["do", 1]],
            concept_phrase="the complete expansion of the when-macro call",
            question_what="the fully expanded form after all macro passes",
            goal_text="fully expand a when-macro call to reveal the if-form it becomes",
            scenario=(
                "The farmer had left a chalk shorthand on the dairy wall "
                "— `when` with its test and body. The milkmaid wanted to "
                "trace every rewrite until no more shorthands remained, "
                "so the runtime could not be surprised."
            ),
            need=(
                "She needed the macroexpander to run all its passes on "
                "the shorthand, not just one — stamping the form again "
                "and again until only primitive steps remained."
            ),
            mapping=(
                "`macroexpand` is the farmer's full-run stamp: it keeps "
                "rewriting until no chalk shorthand survives, then hands "
                "the final primitive form to the milkmaid. The dairy wall "
                "is blank of shorthands by the time the runtime arrives."
            ),
            resolution=(
                'The REPL returned the fully expanded form — the `if` with its `do` body, with no macro shorthand remaining for the runtime to intercept (with `1` as the input value).'
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
                "The farmer had written a thread-first shorthand on a "
                "pail-steps card — `(-> 1 inc inc)`. The milkmaid asked "
                "to see every rewrite until the card read as plain nested "
                "calls the runtime could follow without any macro help."
            ),
            need=(
                "She needed the full expansion: the farmer's rewrite rule "
                "had to peel off each threading step and nest the calls "
                "inward until the pail-steps card held only ordinary "
                "function composition."
            ),
            mapping=(
                "`macroexpand` is the farmer's complete-run stamp: it "
                "rewrites the threading shorthand all the way down, "
                "turning the left-to-right pail-steps card into nested "
                "calls the runtime reads from the inside out."
            ),
            resolution=(
                "The REPL returned the fully nested form — each step "
                "wrapped inside the next, reading inward exactly as the "
                "full expansion had unwound the threading shorthand."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(when true 1 2 3)",
            expected=3,
            concept_phrase="executing multiple expressions when a condition is true",
            question_what="the result of the last expression when the condition holds",
            goal_text="execute three expressions and return the value of the last when the condition is true",
            scenario=(
                "The farmer had stamped a `when` rewrite rule on bark: "
                "any shorthand with a true test would expand into a `do` "
                "block that ran its whole body. The milkmaid wrote the "
                "form and waited for the runtime's verdict."
            ),
            need=(
                "She needed to know what value the runtime returned after "
                "the farmer's rewrite ran — the last body expression was "
                "what the `do` block handed back once all three steps "
                "had executed in order."
            ),
            mapping=(
                "`when` is the farmer's rewrite rule: it stamps the test "
                "and body into an `if`-`do` form before the runtime "
                "arrives. The runtime runs the expanded steps in order "
                "and returns the value of the last one."
            ),
            resolution=(
                "The REPL evaluated the expanded form and returned the "
                "value of the final body expression — the rewrite had "
                "already happened silently before evaluation began — 3."
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
                "The farmer's rewrite rule for `when` included a guard: "
                "if the test was false, the body was never stamped into "
                "the expanded form at all. The milkmaid submitted the "
                "form with a false test and watched."
            ),
            need=(
                "She needed to see what the runtime handed back when the "
                "guard prevented the body from running — the expanded "
                "form collapsed to nothing, and nothing was what the "
                "REPL returned."
            ),
            mapping=(
                "`when` with a false test expands to a form whose body "
                "branch is unreachable. The farmer's stamp produces no "
                "usable path, so the runtime returns the absent-value "
                "that marks a skipped branch."
            ),
            resolution=(
                "The REPL returned the absent value — the form had "
                "expanded to a dead branch, and the runtime confirmed "
                "that nothing was computed — 3."
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
                "The farmer had a second rewrite rule: `when-not`, which "
                "opened the body only when the test was false. The "
                "milkmaid wrote the form with test false and body a keyword."
            ),
            need=(
                "She needed the negated guard to let the body run — the "
                "farmer's stamp flipped the condition before the expanded "
                "form reached the runtime."
            ),
            mapping=(
                "`when-not` is the farmer's inverted stamp: it stamps the "
                "body into the expanded form only when the test is false, "
                "so the runtime reaches it where `when` would block it."
            ),
            resolution=(
                "The REPL returned the keyword from the body — the inverted "
                "guard had opened the branch exactly as the rewrite directed — :ok."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(-> 5 inc inc inc)",
            expected=8,
            concept_phrase="threading a value through multiple functions in sequence",
            question_what="the result of threading 5 through three increments",
            goal_text="thread the value 5 through inc three times using thread-first",
            scenario=(
                "The farmer had pinned a pail-steps card on the dairy "
                "wall: thread the starting measure through three "
                "successive steps, each pouring the result forward to "
                "the next. The milkmaid submitted the form."
            ),
            need=(
                "She needed to compose the three recipe steps in order, "
                "passing the live value from each step into the next "
                "without nesting calls by hand. The threading macro was "
                "the shorthand the farmer's card described."
            ),
            mapping=(
                "`->` is the pail-steps card: it rewrites left-to-right "
                "steps into nested calls before the runtime sees them. "
                "Each step pours the previous result forward as the "
                "first argument of the next function."
            ),
            resolution=(
                "The REPL returned the final measure after all three "
                "steps had poured forward — the pail-steps card had "
                "composed the recipe exactly as written — 5."
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
                "The farmer had written a longer pail-steps card: strain "
                "the pail through a sieve, ladle the results through a "
                "tally, and reduce the tallied pours to a single measure. "
                "The milkmaid threaded the vector through all three."
            ),
            need=(
                "She needed each step to pass the collection forward as "
                "the last argument of the next recipe step, so the "
                "thread-last card could compose filter, map, and reduce "
                "without parenthesis nesting."
            ),
            mapping=(
                "`->>` is the last-argument pail-steps card: it rewrites "
                "the left-to-right recipe into nested calls where each "
                "step's result flows in at the end of the next. The "
                "runtime reads the nested form inward."
            ),
            resolution=(
                "The REPL returned the single reduced measure — the "
                "pail-steps card had filtered, mapped, and folded the "
                "collection exactly as the three steps described — 4."
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
                "The farmer pointed at a short pail-steps card — `(-> x "
                "f g)` — and asked the milkmaid to trace exactly what "
                "nested form the farmer's rewrite rule would stamp in "
                "its place before the runtime arrived."
            ),
            need=(
                "She needed to see the threading shorthand fully rewritten "
                "into nested function calls — the pail-steps card turned "
                "inside out so the runtime could read it without any "
                "macro knowledge."
            ),
            mapping=(
                "`macroexpand` is the farmer's full-stamp tool: it "
                "rewrites the thread-first card into nested calls, "
                "peeling the left-to-right order back into the inward "
                "nesting the runtime expects."
            ),
            resolution=(
                "The REPL returned the fully nested form — the outer "
                "function wrapping an inner call of the same pattern, "
                "reading from outside in just as the expansion had built."
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
    fable="milkmaid",
    examples=[
        # A function evaluates its args; a macro receives unevaluated forms.
        SubjectExample(
            form="(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))",
            expected=7,
            concept_phrase="calling a plain function that adds two numbers",
            question_what="the sum returned by calling add-fn with arguments 3 and 4",
            goal_text="define a function add-fn and call it to add 3 and 4",
            scenario=(
                "The farmer had written a plain pail-steps card — "
                "`add-fn` — that accepted two ladle-measures and poured "
                "them together at call time. The milkmaid submitted the "
                "card with the two measures already evaluated."
            ),
            need=(
                "She needed a named recipe that received two live values "
                "and returned their sum — a function card that evaluated "
                "its arguments before stepping through the body."
            ),
            mapping=(
                "`defn` is the named pail-steps card: it accepts "
                "already-evaluated arguments at call time and computes "
                "a result from them. No rewriting happens; the function "
                "receives values, not chalk marks."
            ),
            resolution=(
                "The REPL returned the sum — the function had received "
                "the two evaluated measures and poured them together "
                "exactly as the recipe card described — 4."
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
                "Beside the function card, the farmer had stamped a "
                "rewrite rule — `add-mac` — that intercepted the call "
                "form before the runtime arrived and stamped an addition "
                "form in its place with the arguments unquoted."
            ),
            need=(
                "She needed a rewrite rule that would transform the macro "
                "call into a plain addition form at read-time, so the "
                "runtime received a chalk mark that it could evaluate "
                "directly without knowing `add-mac` existed."
            ),
            mapping=(
                "`defmacro` is the farmer's rewrite rule: it intercepts "
                "the shorthand form, unquotes the arguments into a "
                "syntax-quoted addition template, and hands the expanded "
                "form to the runtime. The runtime sees `+`, never the macro."
            ),
            resolution=(
                "The REPL evaluated the expanded addition form and "
                "returned the same sum — the rewrite had happened "
                "silently before evaluation, leaving only the plain "
                "arithmetic for the runtime — 4."
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
    fable="milkmaid",
    examples=[
        # gensym always returns a fresh symbol; we test symbol? predicate.
        SubjectExample(
            form="(symbol? (gensym))",
            expected=True,
            concept_phrase="testing whether gensym produces a symbol",
            question_what="whether a generated symbol is of type symbol",
            goal_text="test that gensym returns a symbol",
            scenario=(
                "The farmer had a chalk-mark stamp that generated a fresh "
                "label each time it pressed — never the same mark twice. "
                "The milkmaid asked whether the fresh mark was truly a "
                "symbol or something else entirely."
            ),
            need=(
                "She needed to confirm the kind of chalk mark the stamp "
                "produced — a genuine symbol, the sort that could stand "
                "as a name in a macro expansion without colliding with "
                "any existing label on the dairy wall."
            ),
            mapping=(
                "`gensym` is the farmer's fresh-mark stamp: each press "
                "produces a unique chalk symbol guaranteed not to shadow "
                "any existing name. `symbol?` reads the mark and "
                "confirms it is indeed a chalk label, not a value."
            ),
            resolution=(
                "The REPL confirmed the mark was a symbol — the fresh "
                "stamp had produced a genuine chalk label, passing the "
                "predicate's test as expected."
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
                "The farmer pressed the fresh-mark stamp twice with the "
                "same prefix carved into it. The milkmaid held both marks "
                "side by side on the dairy wall and asked whether they "
                "were the same chalk label."
            ),
            need=(
                "She needed to verify that two separate presses of the "
                "same stamp produced distinct labels — that hygiene meant "
                "each generated mark was unique even when the prefix "
                "matched exactly."
            ),
            mapping=(
                "`gensym` with the same prefix still produces two "
                "distinct chalk marks: the suffix appended to each "
                "press differs, guaranteeing uniqueness. `=` compares "
                "the full marks and finds them unequal."
            ),
            resolution=(
                'The REPL returned the inequality verdict — the two fresh marks were not identical, confirming that each stamp press produced a genuinely distinct label (with `x_` as the input value).'
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
    fable="milkmaid",
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
                "The farmer had stamped a hygienic rewrite rule: "
                "`safe-if-let`, which passed the caller's explicit "
                "binding name directly through rather than injecting an "
                "anonymous label that could shadow surrounding names."
            ),
            need=(
                "She needed a macro that expanded into `if-let` using "
                "the exact binding the caller supplied — no hidden label "
                "was stamped into the expanded form, so no name could "
                "leak out of the rewrite and surprise the runtime."
            ),
            mapping=(
                "`defmacro` with explicit binding is the farmer's hygienic "
                "stamp: it threads the caller's chalk mark through into "
                "the expanded form unchanged, keeping the name visible "
                "and safe. No surprise label appears in the rewrite."
            ),
            resolution=(
                'The REPL evaluated the expanded `if-let` form and returned the value from the then-branch — the hygienic rewrite had passed the binding through cleanly (with `5` as the input value).'
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
                "The farmer pointed at the built-in `if-let` as the "
                "model hygienic binding form — it stamped the caller's "
                "explicit name into the expansion, bound it if the "
                "value was truthy, then ran the then-branch."
            ),
            need=(
                "She needed the binding to succeed and the then-branch "
                "to run — the farmer's built-in rule bound the name "
                "to its value and handed control to the branch that "
                "used that name."
            ),
            mapping=(
                "`if-let` is the farmer's canonical hygienic stamp: "
                "it binds the explicit chalk mark to the tested value "
                "and runs the then-branch if the binding succeeded, "
                "with no invisible labels inserted into the expansion."
            ),
            resolution=(
                "The REPL evaluated the then-branch after the binding "
                "succeeded and returned the product — the explicit name "
                "had been available throughout without any shadowing — 7."
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
    fable="milkmaid",
    examples=[
        # Reader macros: ', `, ~, #(...), #_, etc. Test what they read to.
        SubjectExample(
            form="'(1 2 3)",
            expected=[1, 2, 3],
            concept_phrase="using the quote reader macro",
            question_what="the form read by the quote reader",
            goal_text="use the quote reader macro to read a list of several numbers",
            scenario=(
                "The scribe had chalked an apostrophe mark on the dairy "
                "wall before a row of tally numbers. The milkmaid asked "
                "what the reader's meaning for that mark was."
            ),
            need=(
                "She needed the reader to expand the scribe's shorthand "
                "into its full form before evaluation — the apostrophe "
                "mark sealed the form as data, not a call."
            ),
            mapping=(
                "The `'` mark is the scribe's shorthand: the reader expands "
                "it into a `quote` wrapper before the runtime sees anything. "
                "The runtime receives a sealed list, never the shorthand."
            ),
            resolution=(
                "The REPL returned the several numbers as a sealed list — the "
                "reader had expanded the mark and the runtime handed the "
                "data back unevaluated — 3."
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
                "The scribe had chalked a `#` mark before a set of "
                "parentheses on the dairy wall — a shorthand the reader "
                "knew meant an anonymous recipe card with a placeholder "
                "for the single argument."
            ),
            need=(
                "She needed the reader to expand the scribe's `#(...)` "
                "shorthand into a full `fn` form before the runtime "
                "arrived, so the generated function could then be called "
                "with the supplied argument."
            ),
            mapping=(
                "The `#(...)` chalk mark is the scribe's shorthand for "
                "an anonymous pail-steps card: the reader expands it "
                "into a `fn` with a generated parameter before the "
                "runtime sees anything. `%` is the placeholder slot."
            ),
            resolution=(
                "The REPL called the generated function with the argument "
                "and returned the squared result — the reader's expansion "
                "had produced a working recipe card before evaluation — 6."
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
                "The scribe had chalked a `#_` mark above the middle "
                "tally on the dairy wall — a conventional sign meaning "
                "'strike this one out before the reader passes it on.' "
                "The milkmaid asked what the runtime would receive."
            ),
            need=(
                "She needed the reader to erase the struck-out tally "
                "entirely before any form reached the runtime — the "
                "discard mark told the reader to swallow the next element "
                "as if it had never been written."
            ),
            mapping=(
                "`#_` is the scribe's discard mark: it signals the "
                "reader to consume the following element silently, so "
                "the runtime receives a vector with that position "
                "erased. The struck tally leaves no trace."
            ),
            resolution=(
                "The REPL returned the vector with only two elements — "
                "the middle tally had been struck before the runtime — 3. "
                "arrived, exactly as the scribe's discard mark directed."
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
    fable="milkmaid",
    examples=[
        # Tagged literals are read into typed values. Test predicates on them.
        SubjectExample(
            form="(inst? #inst \"2024-01-01\")",
            expected=True,
            concept_phrase="testing whether a tagged literal reads as an instant",
            question_what="whether the inst? predicate returns true",
            goal_text="test that a tagged literal with #inst reads as an instant",
            scenario=(
                "The scribe had chalked `#inst` before a date string on "
                "the tally-slate — a conventional tag the reader knew "
                "meant 'parse this string as a calendar instant before "
                "handing it to the runtime.'"
            ),
            need=(
                "She needed to confirm that the reader's expansion of the "
                "scribe's `#inst` tag produced a genuine instant value — "
                "the kind that the `inst?` predicate would recognize as "
                "a typed calendar mark, not a plain string."
            ),
            mapping=(
                "`#inst` is the scribe's typed-mark: the reader sees the "
                "tag, parses the following string into an instant object, "
                "and hands the typed value to the runtime. The chalk "
                "label tells the reader how to transform the raw string."
            ),
            resolution=(
                "The REPL confirmed the predicate's verdict — the reader had produced a genuine instant from the tagged string, and the type check returned the affirmative (with `2024-01-01` as the input value)."
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
                "The scribe had chalked `#uuid` before a hyphenated "
                "string on the dairy wall — a mark telling the reader "
                "to parse that string as a universally unique identifier "
                "rather than leaving it as raw text."
            ),
            need=(
                "She needed to verify that the reader's tagged expansion "
                "produced a typed uuid value — one that the `uuid?` "
                "predicate would confirm as the correct kind of chalk "
                "mark, not a plain string."
            ),
            mapping=(
                "`#uuid` is the scribe's uuid-mark: the reader interprets "
                "the tag, parses the string into a uuid object, and "
                "delivers the typed value to the runtime. The label "
                "determines how the raw text is transformed."
            ),
            resolution=(
                "The REPL confirmed the predicate's verdict — the reader had built a proper uuid from the tagged string, and the type check returned the affirmative (with `00000000-0000-0000-0000-000000000000` as the input value)."
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
    fable="milkmaid",
    examples=[
        # EDN read-string with a default tag handler.
        SubjectExample(
            form="(clojure.edn/read-string \"42\")",
            expected=42,
            concept_phrase="parsing a number string with edn/read-string",
            question_what="the parsed value from the EDN source",
            goal_text="use edn/read-string to parse a number from a string",
            scenario=(
                "The scribe had written a number on a market-board slip "
                "as plain text and handed it to the milkmaid. She asked "
                "how to turn the written tally mark into a live numeric "
                "value the runtime could compute with."
            ),
            need=(
                "She needed the EDN reader to interpret the chalk marks "
                "on the slip as a number — parsing the textual "
                "representation back into the typed value that the "
                "runtime understood as an integer."
            ),
            mapping=(
                "`edn/read-string` is the scribe's reading tool: it "
                "interprets the chalk marks on the slip according to EDN "
                "conventions and hands the parsed typed value to the "
                "runtime, turning the written mark into live data."
            ),
            resolution=(
                "The REPL returned the parsed number — the scribe's reader had converted the textual tally mark into a typed integer the runtime could use directly (with `42` as the input value)."
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
                "The scribe had written a bracketed row of keyword marks "
                "on a tally-slate and handed the text to the milkmaid. "
                "She needed to read those chalk marks back into a live "
                "vector the runtime could inspect."
            ),
            need=(
                "She needed the EDN reader to interpret the bracketed "
                "chalk marks as a vector of keyword values — parsing "
                "the textual representation back into structured data "
                "the runtime could iterate or index."
            ),
            mapping=(
                "`edn/read-string` is the scribe's reader: it interprets "
                "the bracketed keyword marks on the slate according to "
                "EDN conventions and returns the parsed vector, turning "
                "the written marks into live typed data."
            ),
            resolution=(
                "The REPL returned the parsed vector of keywords — the scribe's reader had converted the textual bracket marks into structured data the runtime could work with (with `:a` as the input value)."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(eval '(+ 1 2 3))",
            expected=6,
            concept_phrase="evaluating a quoted form at runtime",
            question_what="the result of evaluating the quoted addition",
            goal_text="evaluate a quoted addition form at runtime",
            scenario=(
                "The farmer held a chalk mark on a slip — a quoted "
                "addition form — and asked the milkmaid to open the pail "
                "at runtime: take the sealed chalk mark and hand it to "
                "the evaluator as if it were freshly written."
            ),
            need=(
                "She needed to pass the sealed chalk mark to `eval`, "
                "which would treat the quoted data as a live form and "
                "run it through the evaluator — opening the pail that "
                "`quote` had kept sealed."
            ),
            mapping=(
                "`eval` is the farmer's runtime opener: it receives the "
                "chalk mark — the quoted form — and hands it back to the "
                "evaluator as if the seal had never existed. The milk "
                "flows where quote had held it back."
            ),
            resolution=(
                "The REPL evaluated the unsealed form and returned the "
                "computed sum — the chalk mark had been treated as a "
                "live addition, with the pail finally opened — 3."
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
                "The farmer assembled chalk marks at runtime — building "
                "a list from a quoted operator and two numbers, then "
                "handing that assembled mark to the evaluator. The "
                "milkmaid watched the runtime construct and run the form."
            ),
            need=(
                "She needed to build a data list that looked like a "
                "Clojure form and then feed it to `eval`, which would "
                "treat the assembled marks as a live addition and "
                "compute the result."
            ),
            mapping=(
                "`list` assembles chalk marks into a form-shaped list "
                "at runtime; `eval` then opens that assembled mark and "
                "runs it through the evaluator. Data becomes code only "
                "when the farmer hands it to the opener."
            ),
            resolution=(
                "The REPL evaluated the dynamically assembled form and "
                "returned the sum — the constructed chalk marks had been "
                "treated as live code by the runtime opener — 5."
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
    fable="milkmaid",
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
                "The farmer looked at the milkmaid's plan and said there "
                "was no need for a rewrite rule here — a plain nameless "
                "pail-steps card would do. No syntax needed shaping; "
                "the arguments were already evaluated before the call."
            ),
            need=(
                "She needed an anonymous recipe card that accepted two "
                "live values and added them directly — no chalk shorthand "
                "to intercept, no form to reshape before the runtime "
                "arrived. A function was sufficient."
            ),
            mapping=(
                "`fn` is the nameless pail-steps card: it receives "
                "already-evaluated arguments at call time and computes "
                "a result. When no syntax shaping is needed, the "
                "farmer's rewrite rule would be overkill."
            ),
            resolution=(
                'The REPL evaluated the anonymous function call and returned the sum — the plain recipe card had done the job without any macro rewriting at all (with `3` as the input value).'
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
                "The farmer handed the milkmaid a straining task — apply "
                "a step to every element in the pail, one by one. No "
                "chalk shorthand needed rewriting; the task called for "
                "a plain higher-order recipe, not a macro rule."
            ),
            need=(
                "She needed to pass a live function to `map` and let it "
                "pour through each element of the collection, producing "
                "a new pail with each measure incremented. No rewrite "
                "rule was required — only a function card."
            ),
            mapping=(
                "`map` with a plain function is the pail-steps card that "
                "walks each element through a step and collects the "
                "results. The farmer's rewrite rule has no role when "
                "the form shape needs no transformation."
            ),
            resolution=(
                'The REPL returned the collection of incremented values — the plain function had walked each element without any macro expansion being needed (with `1` as the input value) (with `3` as the input value).'
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
    fable="milkmaid",
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
                "The farmer had stamped a `with-X` rewrite rule — a "
                "pattern that opened a context, ran a body inside it, "
                "and guaranteed the context name was hygienically bound "
                "without leaking outside the expanded form."
            ),
            need=(
                "She needed a macro that would intercept the `with-...` "
                "shorthand, expand it into a `let` block with a "
                "generated binding, splice the caller's body inside, "
                "and return the body's final value."
            ),
            mapping=(
                "`defmacro` for the `with-X` pattern is the farmer's "
                "context-opener stamp: it wraps the caller's body in a "
                "hygienic `let`, ensuring the bound name cannot escape "
                "and the body runs as if inside a prepared pail."
            ),
            resolution=(
                "The REPL evaluated the expanded `let` block and returned the body's final value — the context rewrite had prepared the pail and the body ran cleanly inside (with `42` as the input value)."
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
                "The farmer had stamped a `def-X` rewrite rule — a "
                "shorthand that intercepted a naming call and expanded "
                "it into a `def` form, chalking the given name onto the "
                "market-board with the supplied value."
            ),
            need=(
                "She needed a macro that would rewrite the shorthand "
                "into a `def` before the runtime arrived, so the named "
                "binding would be posted on the market-board where any "
                "later form could read it by name."
            ),
            mapping=(
                "`defmacro` for the `def-X` pattern is the farmer's "
                "naming stamp: it intercepts the shorthand, unquotes "
                "the name and value into a `def` template, and posts "
                "the binding on the market-board before evaluation."
            ),
            resolution=(
                'The REPL evaluated the expanded `def` and then looked up the posted name, returning the keyword value — the market-board had been chalked by the rewrite rule (with `slow` as the input value) (with `:slow` as the input value).'
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
    print(f"grade-10 tortoise-hare smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
