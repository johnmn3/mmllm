"""Grade 10 — macros, code as data. Through tortoise-hare.

Subplot lens: the Tortoise designs a small language. Each subject is
the Hare and Tortoise inspecting a macro, an expansion, or a piece of
syntax-quoted source. The fable's moral — patience over haste — fits
naturally: macros reward careful reading of expansions over guessing.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.tortoise_hare.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.tortoise_hare._metaphor_pools import (
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(quote (+ 1 2))",
            expected=["+", 1, 2],
            concept_phrase="quoting an addition form",
            question_what="what you get when you quote an addition form",
            goal_text="quote an addition form so it evaluates to a list without computing",
            scenario=(
                "Mossback the tortoise had chalked the form `(+ 1 2)` "
                "on a strip of bark and set it aside, wanting to hand the "
                "form itself to the Hare — not its computed value."
            ),
            need=(
                "She needed a way to label the form so the runtime would "
                "return the form as data rather than evaluate it."
            ),
            mapping=(
                "`quote` is the chalk mark: it labels a form so the runtime "
                "hands it back as a list of symbols and numbers, never "
                "computing the addition."
            ),
            resolution=(
                "the REPL returned the form as a list, exactly as Mossback "
                "had chalked it — unevaluated and intact."
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
                "Bramble the hare had scrawled three numbers on a leaf and "
                "wanted to pass them along the trail as a single labeled "
                "bundle without any arithmetic happening. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "She needed the shorthand `'` mark so the reader would treat "
                "the list as data and hand it back unchanged."
            ),
            mapping=(
                "The `'` reader macro is the chalk mark in shorthand: it "
                "wraps the form in `quote`, preventing evaluation and "
                "returning the list as written."
            ),
            resolution=(
                "the REPL handed back the three-number list intact — "
                "Bramble's bundle arrived at the other end of the trail "
                "with nothing added or removed."
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
                "Mossback had a template chalked on bark — the letter `a`, "
                "a blank hole in the middle, and the letter `b` — and she "
                "wanted to fill the hole with the value `x` held in her "
                "pouch."
            ),
            need=(
                "She needed syntax-quote for the labeled template and "
                "unquote (`~`) to open the hole and pour in the live value."
            ),
            mapping=(
                "Syntax-quote builds a labeled template; `~x` is the hole "
                "that gets filled with the actual value of `x` before the "
                "runtime sees the resulting list."
            ),
            resolution=(
                'the REPL returned a list with the symbol `a`, the number from the pouch, and the symbol `b` — the template filled exactly as Mossback intended (with `5` as the input value).'
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(let [x 10] `(+ ~x ~x))",
            expected=["+", 10, 10],
            concept_phrase="building a form by unquoting a variable twice inside syntax-quote",
            question_what="the form produced when x is 10 and unquoted twice",
            goal_text="build a form where a variable is inserted twice into an addition form",
            scenario=(
                "Mossback was designing a rewrite template that needed the "
                "same value placed in two holes — the template read `(+ _ _)` "
                "where both blanks should hold whatever `x` currently was. The value at the heart of the form was 10."
            ),
            need=(
                "She needed syntax-quote for the labeled template and `~x` "
                "twice to pour the same value into each hole before the "
                "runtime received the form."
            ),
            mapping=(
                "Syntax-quote builds the chalk-marked template; each `~x` "
                "opens a hole and fills it with the live value, so the "
                "runtime gets a complete form with real numbers in place of "
                "placeholders."
            ),
            resolution=(
                "the REPL returned a list with the `+` symbol and the "
                "value inserted in both positions — the template filled "
                "correctly, ready to be evaluated."
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
                "Bramble had a bundle of three acorn-counts in a bag and "
                "wanted to pour all of them into a single template form so "
                "the runtime would see each count as a separate element. The value at the heart of the form was 1."
            ),
            need=(
                "She needed unquote-splice (`~@`) to tear open the bag and "
                "spread its contents flat inside the syntax-quoted template "
                "rather than inserting the bag as a single nested element."
            ),
            mapping=(
                "Syntax-quote holds the labeled template; `~@xs` splices "
                "every element of the vector into the form in sequence, "
                "producing a flat list the runtime can read directly."
            ),
            resolution=(
                'the REPL returned a list with `list` followed by each number spread out — the bag had been emptied into the template exactly as Bramble needed (with `3` as the input value).'
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(do (defmacro my-when [t & body] `(if ~t (do ~@body))) "
                 "(my-when true 1 2 3))",
            expected=3,
            concept_phrase="defining a conditional macro and invoking it",
            question_what="the value the rewritten if-do form returns when the test is true and the body has three expressions",
            goal_text="define a rule named my-when that rewrites (my-when t body...) into (if t (do body...)); then invoke it with the test true and a three-expression body",
            scenario=(
                "Mossback the tortoise was tired of writing `if`/`do` "
                "by hand for every form where she wanted several steps "
                "to run only if a condition held."
            ),
            need=(
                "She wanted a rule called `my-when` that rewrote the "
                "shorter form `(my-when t body...)` into the longer "
                "`(if t (do body...))` — once written, applicable to "
                "any test and body."
            ),
            mapping=(
                "`defmacro` defines a rewrite-rule. The rule's body "
                "uses syntax-quote and unquote-splicing to build the "
                "rewritten form. The runtime applies the rule first, "
                "then evaluates the rewritten form normally."
            ),
            resolution=(
                'the rewritten form ran the body, kept only the last-step value, and returned it — the rule had saved Mossback the longer writing (with `1` as the input value) (with `3` as the input value).'
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
                "Mossback needed a shorthand for running any expression "
                "twice in a row. Rather than writing `(do expr expr)` by "
                "hand each time, she wanted a rewrite rule that emitted "
                "both copies automatically. The value at the heart of the form was 7."
            ),
            need=(
                "She needed `defmacro` to define the rule so that every "
                "call to `twice` would be rewritten into a `do` block "
                "with the argument unquoted twice — before the runtime "
                "ever saw it."
            ),
            mapping=(
                "`defmacro` registers the rewrite rule at compile time. "
                "The rule's syntax-quoted body uses `~x` in two positions, "
                "so the runtime receives `(do expr expr)` and evaluates it "
                "normally."
            ),
            resolution=(
                "the REPL returned the value of the last-run copy of the "
                "expression — the rewrite rule had saved Mossback the "
                "double writing."
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(macroexpand-1 '(when true 1))",
            expected=["if", True, ["do", 1]],
            concept_phrase="the one-step expansion of the when-macro call",
            question_what="the expanded form after one level of macro expansion",
            goal_text="expand a when-macro call one step to see what code it produces",
            scenario=(
                "Mossback had quoted a `when` form on a strip of bark and "
                "wanted to see exactly what code the scribe would write in "
                "its place — just one rewrite, no further passes."
            ),
            need=(
                "She needed `macroexpand-1` to invoke the rewrite rule once "
                "and return the resulting form as data, showing the "
                "before-and-after of a single macro pass."
            ),
            mapping=(
                "`macroexpand-1` hands the quoted form to the scribe for "
                "one rewrite; the scribe applies the `when` rule and "
                "returns the new form — the runtime has not evaluated "
                "anything yet."
            ),
            resolution=(
                "the REPL returned the rewritten form, letting Mossback "
                "see exactly what the runtime would receive after the "
                "single-step rewrite."
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
                "Bramble wanted to understand how `or` worked internally. "
                "She quoted an `or` call and asked the macroexpander to "
                "show her just the first rewrite — before any nested "
                "macros were expanded."
            ),
            need=(
                "She needed `macroexpand-1` to reveal the generated "
                "let-binding and if-form that the scribe substitutes for "
                "`or` in a single pass."
            ),
            mapping=(
                "`macroexpand-1` applies the `or` rewrite rule once and "
                "returns the new form as data; the scribe's scratch-name "
                "and nested structure appear before the runtime has "
                "evaluated a single sub-form."
            ),
            resolution=(
                "the REPL returned the intermediate form with its "
                "auto-generated binding name — Bramble could now read "
                "the rewrite before the runtime executed it."
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(macroexpand '(when true 1))",
            expected=["if", True, ["do", 1]],
            concept_phrase="the complete expansion of the when-macro call",
            question_what="the fully expanded form after all macro passes",
            goal_text="fully expand a when-macro call to reveal the if-form it becomes",
            scenario=(
                "Mossback wanted to see the final code the runtime would "
                "receive after every rewrite rule had been applied to a "
                "`when` call — not just the first pass. The value at the heart of the form was 1."
            ),
            need=(
                "She needed `macroexpand` to keep applying rewrite rules "
                "until no more macros remained, returning the fully "
                "expanded form as data."
            ),
            mapping=(
                "`macroexpand` runs the scribe's rewrite rules repeatedly "
                "until the form is pure core code; the result is the form "
                "the runtime will evaluate — no macros remain to rewrite."
            ),
            resolution=(
                "the REPL returned the final if-form, giving Mossback "
                "the complete picture of what the runtime would actually "
                "execute."
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
                "Bramble had written a threading chain and wanted to see "
                "how the scribe's rewrite rule would nest the calls before "
                "the runtime ever ran them. The value at the heart of the form was 1."
            ),
            need=(
                "She needed `macroexpand` to show the fully nested form "
                "produced by applying the threading rule to the entire "
                "chain in one pass."
            ),
            mapping=(
                "`macroexpand` applies the thread-first rewrite rule until "
                "the chain collapses into nested function calls — the "
                "scribe rewrites before the runtime evaluates anything."
            ),
            resolution=(
                "the REPL returned the nested call form, revealing how "
                "each step in the chain wraps the previous one — exactly "
                "the code the runtime would run."
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(when true 1 2 3)",
            expected=3,
            concept_phrase="executing multiple expressions when a condition is true",
            question_what="the result of the last expression when the condition holds",
            goal_text="execute three expressions and return the value of the last when the condition is true",
            scenario=(
                "Mossback had a shorthand trail-mark — `when` — that she "
                "used instead of writing `if`/`do` by hand whenever she "
                "needed several steps to run only if a condition held. The values drawn fresh were {drawn.a}, {drawn.b}, and {drawn.c}. The value at the heart of the form was 1."
            ),
            need=(
                "She needed the `when` macro to rewrite the short form into "
                "a full `if`/`do` before the runtime evaluated any of the "
                "body expressions."
            ),
            mapping=(
                "`when` is a scribe's shorthand that rewrites its call into "
                "`(if condition (do body...))` before evaluation; the "
                "runtime then runs the rewritten form and returns the last "
                "body value when the condition is true."
            ),
            resolution=(
                "the REPL returned the value of the last body expression, "
                "confirming the rewrite had fired and the body had run in "
                "full."
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
                "Bramble set the condition of a `when` call to false to "
                "find out what the macro's rewritten form produced when "
                "the branch was skipped. The values drawn fresh were {drawn.a}, {drawn.b}, and {drawn.c}."
            ),
            need=(
                "She needed to see that the scribe's rewrite still produced "
                "an `if`/`do`, and that the runtime returned nothing when "
                "the condition was false."
            ),
            mapping=(
                "`when` rewrites to `(if false (do ...))` before "
                "evaluation; the runtime takes the false branch, which has "
                "no else expression, so the form returns nil."
            ),
            resolution=(
                "the REPL returned nil — the rewrite had fired correctly "
                "and the runtime skipped the body, exactly as the `when` "
                "shorthand promised."
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
                'Mossback had a second trail-mark, `when-not`, for the opposite case: run the body only when the condition did not hold. The value drawn fresh was :ok.'
            ),
            need=(
                "She needed `when-not` to rewrite its call so that a false "
                "condition triggered the body rather than suppressing it."
            ),
            mapping=(
                "`when-not` is a scribe's shorthand that rewrites to "
                "`(when (not condition) body...)`; the rewrite fires "
                "before evaluation, so the runtime sees a plain `when` "
                "with the negated condition."
            ),
            resolution=(
                "the REPL returned the body's keyword value — the "
                "negated condition was true, so the body ran, confirming "
                "the `when-not` shorthand worked as written."
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(-> 5 inc inc inc)",
            expected=8,
            concept_phrase="threading a value through multiple functions in sequence",
            question_what="the result of threading 5 through three increments",
            goal_text="thread the value 5 through inc three times using thread-first",
            scenario=(
                "Bramble had a relay race where each runner received a "
                "number, added one, and handed it to the next. She wanted "
                "a single notation that described all three hand-offs "
                "left to right. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "She needed the `->` threading macro to rewrite the "
                "left-to-right relay into nested calls before the runtime "
                "evaluated anything."
            ),
            mapping=(
                "`->` rewrites each step so the value threads as the first "
                "argument into the next function; the scribe builds the "
                "nested form before evaluation, and the runtime runs the "
                "result of the relay."
            ),
            resolution=(
                "the REPL returned the final value after all three "
                "hand-offs — the relay had completed and the result "
                "arrived at the finish line."
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
                "Mossback had a basket of four acorn-counts and wanted to "
                "pass the basket through three stations — a sieve, a "
                "counting table, and a tallying post — each receiving the "
                "collection as their last argument. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "She needed the `->>` threading macro to rewrite each "
                "station call so the collection threaded as the last "
                "argument through filter, map, and reduce."
            ),
            mapping=(
                "`->>` rewrites each step so the value threads as the last "
                "argument; the scribe builds the full nested form before "
                "evaluation, and the runtime runs the composed pipeline."
            ),
            resolution=(
                "the REPL returned the final sum from the tallying post — "
                "the basket had passed through all three stations and "
                "arrived as a single total."
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
                "Bramble wanted to see exactly how the scribe rewrote "
                "a two-step relay so she could read the nested structure "
                "before the runtime ran it."
            ),
            need=(
                "She needed `macroexpand` to show the fully rewritten "
                "form — the nested function calls the scribe emitted "
                "from the threading macro."
            ),
            mapping=(
                "`macroexpand` applies the `->` rewrite rule and returns "
                "the resulting nested calls as data; the scribe's rewrite "
                "is complete before the runtime evaluates anything."
            ),
            resolution=(
                "the REPL returned the nested call form, letting Bramble "
                "read the exact code the runtime would execute — each "
                "step wrapped around the previous one."
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
    fable="tortoise-hare",
    examples=[
        # A function evaluates its args; a macro receives unevaluated forms.
        SubjectExample(
            form="(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))",
            expected=7,
            concept_phrase="calling a plain function that adds two numbers",
            question_what="the sum returned by calling add-fn with arguments 3 and 4",
            goal_text="define a function add-fn and call it to add 3 and 4",
            scenario=(
                "Mossback showed Bramble the standard recipe approach: a "
                "plain function that received already-evaluated arguments "
                "and combined them by following the recipe's steps. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "She needed `defn` to define a function so that the "
                "runtime would evaluate the arguments before handing "
                "them to the recipe — the function never saw unevaluated "
                "forms."
            ),
            mapping=(
                "A function evaluates its arguments first, then runs the "
                "body; the runtime computes the values of `a` and `b` "
                "before `add-fn` ever starts."
            ),
            resolution=(
                "the REPL returned the sum — the arguments had been "
                "evaluated and added inside the recipe, with no rewriting "
                "involved."
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
                "Mossback then showed the rewrite-rule approach: a macro "
                "that received unevaluated forms and built the addition "
                "form before the runtime saw any values."
            ),
            need=(
                "She needed `defmacro` to define a rewrite rule so that "
                "`add-mac` would emit `(+ a b)` as a form first, and "
                "only then let the runtime evaluate it."
            ),
            mapping=(
                "A macro rewrites its call before evaluation; the scribe "
                "replaces `(add-mac 3 4)` with `(+ 3 4)`, and then the "
                "runtime evaluates the rewritten form — a step the "
                "function approach skips entirely."
            ),
            resolution=(
                "the REPL returned the same sum — but the path was "
                "different: the rewrite rule had run first, then the "
                "runtime evaluated the emitted addition form."
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
    fable="tortoise-hare",
    examples=[
        # gensym always returns a fresh symbol; we test symbol? predicate.
        SubjectExample(
            form="(symbol? (gensym))",
            expected=True,
            concept_phrase="testing whether gensym produces a symbol",
            question_what="whether a generated symbol is of type symbol",
            goal_text="test that gensym returns a symbol",
            scenario=(
                "Mossback needed to mint a fresh scratch-name inside a "
                "macro so the name would never collide with anything the "
                "caller had already written. She reached for `gensym`."
            ),
            need=(
                "She needed to verify that `gensym` returned a proper "
                "symbol — not a string or keyword — so the rewrite rule "
                "could safely bind it in the emitted form."
            ),
            mapping=(
                "`gensym` creates a one-off scratch-name that is a real "
                "symbol; `symbol?` confirms its type, which a hygienic "
                "macro relies on when it builds the rewritten form."
            ),
            resolution=(
                "the REPL confirmed the type-check — `gensym` had "
                "produced a proper symbol, safe to use as a scratch-name "
                "in any macro expansion."
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
                'Bramble noticed that two macro expansions both needed a scratch-name starting with `x_` and wondered if `gensym` would hand out the same name twice, causing a collision.'
            ),
            need=(
                "She needed to call `gensym` twice with the same prefix "
                "and confirm that the two resulting symbols were distinct "
                "— each a unique scratch-name even though they shared "
                "a prefix."
            ),
            mapping=(
                "`gensym` mints a new symbol with a unique suffix each "
                "call regardless of the prefix; macros rely on this "
                "guarantee to prevent one expansion's scratch-name from "
                "shadowing another's."
            ),
            resolution=(
                "the REPL confirmed the two gensyms were not equal — "
                "each call had produced a distinct scratch-name safe "
                "from collision."
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
    fable="tortoise-hare",
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
                "Mossback wanted to show Bramble the safe way to write "
                "a conditional binding macro — using an explicit name "
                "in the caller's scope rather than an implicit one "
                "injected by the rewrite rule. The value at the heart of the form was 5."
            ),
            need=(
                "She needed `defmacro` to define a transparent wrapper "
                "that emitted an `if-let` form with the caller's binding "
                "name intact — no hidden names inserted by the scribe."
            ),
            mapping=(
                "The macro rewrites `safe-if-let` into `if-let` before "
                "evaluation; the scribe passes the caller's explicit "
                "binding through unchanged, keeping the name visible and "
                "avoiding any shadowing collision."
            ),
            resolution=(
                "the REPL returned the then-branch result — the "
                "hygienic rewrite had bound the explicit name and "
                "evaluated the body with no hidden name confusion."
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
                "Bramble tried the built-in `if-let`, which bound a name "
                "explicitly so she could read clearly which name held the "
                "value in the then-branch. The value at the heart of the form was 7."
            ),
            need=(
                "She needed `if-let` to bind `x` to the tested value so "
                "the then-branch could use the name without any hidden "
                "scribe-injected binding."
            ),
            mapping=(
                "`if-let` expands to a conditional binding before "
                "evaluation; the explicit name `x` is in the caller's "
                "control, making the expansion readable and "
                "collision-free."
            ),
            resolution=(
                "the REPL returned the square of the bound value — the "
                "explicit binding had worked cleanly, with no anaphoric "
                "confusion about where the name came from."
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
    fable="tortoise-hare",
    examples=[
        # Reader macros: ', `, ~, #(...), #_, etc. Test what they read to.
        SubjectExample(
            form="'(1 2 3)",
            expected=[1, 2, 3],
            concept_phrase="using the quote reader macro",
            question_what="the form read by the quote reader",
            goal_text="use the quote reader macro to read a list of three numbers",
            scenario=(
                "The scribe reading Mossback's source had a shorthand "
                "mark — the apostrophe — that told the reader to wrap "
                "the next form in `quote` without Mossback having to "
                "spell it out. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Mossback needed to know what the reader's shorthand "
                "produced so she could trust the apostrophe to return "
                "the list as data."
            ),
            mapping=(
                "The `'` reader macro expands at read time — before the "
                "compiler ever sees the source — wrapping the form in "
                "`(quote ...)` and handing the quoted list to the runtime."
            ),
            resolution=(
                "the REPL returned the three-number list intact — the "
                "scribe's shorthand had done its job at read time, "
                "before any evaluation."
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
                "Bramble needed a quick one-off recipe that squared its "
                "argument. Writing a full `fn` form felt heavy for a "
                "single use, so she reached for the scribe's compact "
                "shorthand. The value at the heart of the form was 6."
            ),
            need=(
                "She needed the `#(...)` reader macro to expand at read "
                "time into an anonymous function that received one "
                "argument and multiplied it by itself."
            ),
            mapping=(
                "`#(* % %)` is the scribe's shorthand; the reader "
                "expands it into `(fn [arg] (* arg arg))` before "
                "evaluation, and the runtime then calls the resulting "
                "function with the supplied argument."
            ),
            resolution=(
                "the REPL returned the squared value — the reader's "
                "shorthand had expanded into a proper function, "
                "and the runtime had called it."
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
                "Mossback had written a vector with three elements but "
                "wanted to comment out the middle one without removing "
                "it from the source — keeping it readable but invisible "
                "to the runtime."
            ),
            need=(
                "She needed the `#_` discard reader macro to tell the "
                "scribe to skip the next form entirely before the "
                "compiler received anything."
            ),
            mapping=(
                "`#_` is the scribe's discard mark: the reader consumes "
                "the next form at read time and drops it, so the runtime "
                "sees only the remaining elements."
            ),
            resolution=(
                'the REPL returned a two-element vector — the middle element had been discarded by the scribe at read time, leaving no trace for the runtime (with `1` as the input value) (with `3` as the input value).'
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
    fable="tortoise-hare",
    examples=[
        # Tagged literals are read into typed values. Test predicates on them.
        SubjectExample(
            form="(inst? #inst \"2024-01-01\")",
            expected=True,
            concept_phrase="testing whether a tagged literal reads as an instant",
            question_what="whether the inst? predicate returns true",
            goal_text="test that a tagged literal with #inst reads as an instant",
            scenario=(
                "The scribe had a convention for date strings: a `#inst` "
                "mark before a date string told the reader to convert it "
                "into a typed instant rather than leaving it as plain text. The form's value to weigh was \"2024-01-01\"."
            ),
            need=(
                "Mossback needed to verify that the scribe's `#inst` "
                "mark produced a real instant value — one that would "
                "satisfy the `inst?` predicate."
            ),
            mapping=(
                "`#inst` is a tagged literal; the reader applies the "
                "registered handler at read time, converting the string "
                "into a typed instant before the runtime ever sees the "
                "value."
            ),
            resolution=(
                "the REPL confirmed the conversion — the scribe's mark "
                "had turned the string into a proper instant at read "
                "time, exactly as the convention promised."
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
                "Bramble had a `#uuid` mark in her source and wanted to "
                "confirm the scribe's convention had converted the UUID "
                "string into a proper typed value at read time. The form's value to weigh was \"00000000-0000-0000-0000-000000000000\"."
            ),
            need=(
                "She needed to verify that `#uuid` triggered the "
                "registered reader handler, producing a value the "
                "`uuid?` predicate would recognize."
            ),
            mapping=(
                "`#uuid` is a tagged literal; the reader dispatches to "
                "the registered UUID handler at read time, creating a "
                "typed UUID value before the runtime touches the form."
            ),
            resolution=(
                "the REPL confirmed the type — the scribe's `#uuid` "
                "mark had produced a proper UUID value at read time, "
                "satisfying the predicate."
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
    fable="tortoise-hare",
    examples=[
        # EDN read-string with a default tag handler.
        SubjectExample(
            form="(clojure.edn/read-string \"42\")",
            expected=42,
            concept_phrase="parsing a number string with edn/read-string",
            question_what="the parsed value from the EDN source",
            goal_text="use edn/read-string to parse a number from a string",
            scenario=(
                "Mossback had received a scroll of EDN data — a plain "
                "string containing a number — and needed the scribe's "
                "reader to convert it into a live Clojure value. The form's value to weigh was \"42\"."
            ),
            need=(
                "She needed `edn/read-string` to invoke the data reader "
                "on the string and produce the Clojure number it "
                "represented, ready for the runtime to use."
            ),
            mapping=(
                "`edn/read-string` applies the EDN reader's shorthand "
                "rules to the string; the scribe converts the text "
                "representation into a typed value at read time, "
                "before the runtime performs any computation."
            ),
            resolution=(
                "the REPL returned the number the string encoded — the "
                "scribe had read the scroll correctly and handed a "
                "live value to the runtime."
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
                "Bramble had a scroll containing a vector of keywords "
                "written as plain text. She needed the scribe to read "
                "the scroll and produce a real Clojure vector from it. The form's value to weigh was \"[:a :b :c]\"."
            ),
            need=(
                "She needed `edn/read-string` to parse the text "
                "representation and return a vector of keyword values "
                "the runtime could inspect and pass around."
            ),
            mapping=(
                "`edn/read-string` runs the data reader over the string; "
                "the scribe interprets each `:`-prefixed token as a "
                "keyword and assembles the result into a vector before "
                "the runtime receives anything."
            ),
            resolution=(
                "the REPL returned a vector of keywords — the scribe "
                "had decoded the scroll faithfully, turning text into "
                "live data the runtime could use."
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(eval '(+ 1 2 3))",
            expected=6,
            concept_phrase="evaluating a quoted form at runtime",
            question_what="the result of evaluating the quoted addition",
            goal_text="evaluate a quoted addition form at runtime",
            scenario=(
                "Mossback had a quoted form sitting as data — a list "
                "with a `+` symbol and three numbers — and needed to "
                "send it to the runtime for evaluation right now, "
                "rather than leaving it as inert data. The value at the heart of the form was 1."
            ),
            need=(
                "She needed `eval` to hand the quoted list to the runtime "
                "on demand, invoking the full evaluation machinery on "
                "a form that already existed as data."
            ),
            mapping=(
                "`eval` is the function that asks the runtime to evaluate "
                "a form; it passes the data structure to the evaluator "
                "and returns whatever value the evaluator computes from it."
            ),
            resolution=(
                'the REPL returned the sum — the runtime had received the form from `eval` and evaluated it immediately, turning the quoted list into a computed value (with `3` as the input value).'
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
                'Bramble wanted to build a form at runtime from separate pieces — a symbol and two numbers — and then ask the runtime to evaluate the assembled result. The values drawn fresh were 4 and 5.'
            ),
            need=(
                "She needed `list` to assemble the form as data, then "
                "`eval` to pass it to the runtime so the runtime would "
                "treat the constructed list as code and evaluate it."
            ),
            mapping=(
                "`list` builds the form as a data structure; `eval` then "
                "hands the assembled form to the runtime evaluator, "
                "which treats it as code and computes the result."
            ),
            resolution=(
                "the REPL returned the sum — the dynamically built form "
                "had been evaluated by the runtime exactly as if it had "
                "been written in source."
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
    fable="tortoise-hare",
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
                "Bramble had considered writing a macro to add two "
                "numbers, but Mossback stopped her. When no syntax "
                "shaping was needed, the scribe's rewrite machinery "
                "was more trouble than it was worth. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Mossback needed to show that a plain anonymous function "
                "received evaluated arguments and computed the sum "
                "without any rewrite rule involved."
            ),
            mapping=(
                "A `fn` receives values the runtime has already "
                "evaluated; no scribe rewrite is needed when the goal "
                "is just combining two numbers — the recipe approach "
                "suffices."
            ),
            resolution=(
                "the REPL returned the sum — the anonymous function "
                "had done the job cleanly, with no macro rewriting "
                "required."
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
                "Mossback pointed out another case where a macro was "
                "unnecessary: mapping a function over a collection. "
                "The runtime's higher-order tools handled it perfectly "
                "without any rewrite rule. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "She needed `map` and a plain function to process each "
                "element — no macro was needed because `map` already "
                "accepted a function as a first-class value."
            ),
            mapping=(
                "A function passed to `map` is a value the runtime "
                "uses directly; the scribe's rewrite machinery would "
                "add nothing here — prefer a function unless syntax "
                "shaping is genuinely required."
            ),
            resolution=(
                "the REPL returned the incremented collection — the "
                "plain function approach had worked, and no macro "
                "rewrite had been needed."
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
    fable="tortoise-hare",
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
                "Mossback wanted to demonstrate the `with-X` pattern: "
                "a macro that established a context binding and spliced "
                "the caller's body into a `let` block automatically. The form's keyword to weigh was :slow-and-steady."
            ),
            need=(
                "She needed `defmacro` so the call would expand into "
                "a `let` with the pace binding and the body spliced in, "
                "all before the runtime evaluated anything."
            ),
            mapping=(
                "The `with-X` macro rewrites its call into a `let` that "
                "establishes context; the scribe splices the body with "
                "`~@body` before the runtime sees the expanded form."
            ),
            resolution=(
                "the REPL returned the body's value — the `with-X` "
                "rewrite had established the binding and run the body."
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
                "Bramble wanted to see the `def-X-thing` pattern: a "
                "macro that emitted a `def` form, letting callers "
                "define named values with a domain-specific shorthand "
                "rather than writing `def` by hand. The form's keyword to weigh was :slow."
            ),
            need=(
                "She needed `defmacro` to define a rewrite rule that "
                "received a name and a value and emitted `(def name "
                "value)` — the scribe's rewrite firing before the "
                "runtime created the binding."
            ),
            mapping=(
                "The `def-X-thing` macro pattern rewrites its call into "
                "a `def` form with the caller's name and value unquoted; "
                "the scribe emits the definition before the runtime "
                "creates the global binding."
            ),
            resolution=(
                "the REPL returned the keyword — the rewrite had emitted "
                "the `def` form, the runtime had created the binding, "
                "and the value was retrievable by name."
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
