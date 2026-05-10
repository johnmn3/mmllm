"""Grade 10 — macros, code as data. Through boy-who-cried-wolf.

Subplot lens: the elder has been quietly designing a small language of
warnings — a notebook of macros that wrote other forms. The shepherd
keeps wanting to skip past the expansion step and just guess what a
macro returns; the elder insists on macroexpand and on writing the
form into the REPL. The fable's moral — claims without checking erode
trust — fits the macro discipline: never trust your eyes on a macro,
only the macroexpander.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.boy_wolf.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.boy_wolf._metaphor_pools import (
    _CHALKMARK_SUBPLOTS, _RECIPE_SUBPLOTS, _REWRITERULE_SUBPLOTS, _SCRIBE_SUBPLOTS,
)
from mmllm.aesop.curriculum.boy_wolf._goals import GOALS, get_goal


# ─────────────────────── grade-10 subplot extensions ───────────────────────
#
# The elder has been quietly designing a small language of warnings —
# a notebook of macros that wrote other forms. The shepherd insists they
# can already see what the macro means; the elder insists on
# macroexpand and on writing the form into the REPL.

_MACRO_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    SubplotTemplate("""\
{elder_phrase} had spent the morning {place} sketching a tiny language
of {elder_his_her} own — a notebook of macros that wrote other forms.
The next entry was {concept_phrase}, and the form {form_display} was
what {elder} wanted {shepherd_phrase} to submit so the REPL could
show what code it produced or what value it returned."""),

    SubplotTemplate("""\
"A macro is just a function that runs at compile time," {elder}
explained {place}, {emo_patient}. {shepherd}, {emo_proud}, said
{shepherd_he_she} could already see what {concept_phrase} meant.
{elder_phrase} insisted they actually evaluate {form_display} and read
what the runtime reported, expansion or value."""),

    SubplotTemplate("""\
The path {place} was littered with old macro definitions someone had
carved into bark. {shepherd_phrase} found one shaped like
{concept_phrase} and dared {elder_phrase} to predict its expansion.
{elder} only smiled and asked {shepherd_him_her} to write
{form_display} into the REPL — that, after all, was the whole point of
having a macroexpander."""),

    SubplotTemplate("""\
{shepherd_phrase} insisted {place} that macros were the same as
functions. {elder_phrase}, {emo_patient}, drew the form {form_display}
on a strip of bark. "The difference," {elder_he_she} said, "is in
{concept_phrase}. Submit the form and let the runtime tell us exactly
what it does.\""""),

    SubplotTemplate("""\
A small notebook lay open {place} where the elder had been studying
syntax-quote. The page showed {concept_phrase}, with the form
{form_display} circled in pencil. {shepherd_phrase}, {emo_tired} of
the lecture, agreed to write the form to settle once and for all what
it produced."""),

    SubplotTemplate("""\
At a stone tablet {place}, {elder_phrase} was teaching {shepherd_phrase}
the discipline of expansion: never trust your eyes, only the
macroexpander. The day's example was {concept_phrase}. The form
{form_display} had to be submitted; nothing else would do."""),
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
    fable="boy-wolf",
    examples=[
        _ex("(quote (+ 1 2))", ["+", 1, 2],
            "the quoted form (quote (+ 1 2))",
            "the value of (quote (+ 1 2))",
            scenario=(
                "Carol had written `+ 1 2` on the watchhouse slate — "
                "a chalk mark for an operation. Tom held a wooden stick "
                "carved with the symbol of addition. 'Are they the same?' he asked."
            ),
            need=(
                "The village's records had to distinguish between the mark "
                "on the slate and the arithmetic rule it stood for. Tom needed "
                "to see that quote stops the substitution — the chalk mark stays as a mark."
            ),
            mapping=(
                "`quote` holds the form as written, suspending all evaluation. "
                "The quoted `(+ 1 2)` is three chalk marks — the symbol `+` and "
                "the numbers 1 and 2 — not an operation yet."
            ),
            resolution=(
                'the form came back as a list of the three marks themselves — the symbol and the numbers, exactly as quote had frozen them.'
            )),
        _ex("'(1 2 3)", [1, 2, 3],
            "the quoted list '(1 2 3)",
            "the value of '(1 2 3)",
            scenario=(
                "Tom had chalked three numbers on the slate: 1, 2, 3. Carol "
                "drew a thin frame around them to mark off a group. 'Now they're grouped?' "
                "Tom asked doubtfully."
            ),
            need=(
                "The village's count-books kept tallies grouped by season. "
                "Carol needed to show Tom that quote marks stop the runtime from "
                "trying to evaluate the list as a procedure."
            ),
            mapping=(
                "The quote reader `'` converts `(1 2 3)` to a list of three numbers. "
                "No evaluation happens — the list just sits there as data."
            ),
            resolution=(
                'the REPL returned the list unchanged: `1, 2, 3` — the quoted form held its shape without any procedure call. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'           )),
        _ex("(let [x 5] `(a ~x b))", ["a", 5, "b"],
            "a syntax-quoted list with one unquote",
            "the result of `(a ~x b) when x is 5",
            scenario=(
                "Carol had a drill-card that said `(a ~x b)` — a template with a "
                "gap marked `x`. Tom handed her the value 5. 'Where does the 5 go?' he asked."
            ),
            need=(
                "The village's drill-cards had blanks to be filled in at runtime. "
                "Carol needed Tom to understand syntax-quote with unquote — the template "
                "shape stays frozen, but the unquoted part substitutes its value."
            ),
            mapping=(
                "Syntax-quote `backtick` freezes the form. Unquote `~` unfreezes just that spot. "
                "So `(a ~x b)` with x=5 becomes `(a 5 b)` — the `a` and `b` stay frozen, "
                "but the `x` thaws and becomes 5."
            ),
            resolution=(
                'the call returned the list with the template shape held intact but the unquoted position filled with 5 — exactly the drill-card pattern.'           )),
    ],
    subplots=_CHALKMARK_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-02 — syntax-quote
G10_02 = SubjectCurriculum(
    grade=10, subject_id="G10-02",
    subject_title="syntax-quote",
    fable="boy-wolf",
    examples=[
        _ex("(let [x 10] `(+ ~x ~x))", ["+", 10, 10],
            "a syntax-quoted addition with x unquoted twice",
            "the form produced by `(+ ~x ~x) when x is 10",
            scenario=(
                "Carol held a drill-card template that said `(+ ~x ~x)` — "
                "the same value plugged into two places. Tom handed her the "
                "value 10 to fill in the two gaps."
            ),
            need=(
                "The village's drills often used the same value twice, and the "
                "template needed to show both places unquoted so the value could "
                "flow through them identically."
            ),
            mapping=(
                "Syntax-quote `backtick` holds the form frozen. Each `~x` "
                "unfreezes a separate spot and substitutes the value 10. With x=10, "
                "`(+ ~x ~x)` becomes `(+ 10 10)` — two identical copies of the value."
            ),
            resolution=(
                'the form produced the addition template with both positions filled with 10 — the syntax-quoted shape held its structure while both unquotes substituted the same value.'
            )),
        _ex("(let [xs [1 2 3]] `(list ~@xs))", ["list", 1, 2, 3],
            "a syntax-quoted list with unquote-splice",
            "the form produced by `(list ~@xs) when xs is [1 2 3]",
            scenario=(
                "Carol had a template drill-card marked `(list ~@xs)` — "
                "a shape with a `splice` marker `~@` to unpack a basket. "
                "Tom handed her a basket holding [1 2 3]."
            ),
            need=(
                "The village's procedures sometimes needed to unpack a whole basket "
                "of items in place. Unquote-splice `~@` splices the items into the "
                "template without wrapping them in an extra layer."
            ),
            mapping=(
                "Syntax-quote freezes the form. Unquote-splice `~@` unpacks a sequence "
                "directly into the template. With xs=[1 2 3], `(list ~@xs)` becomes "
                "`(list 1 2 3)` — the contents spread out, not a nested list."
            ),
            resolution=(
                'the call returned the spliced result: the list symbol with each item from the basket spread out as separate arguments.'
            )),
    ],
    subplots=_CHALKMARK_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-03 — defmacro introduction
G10_03 = SubjectCurriculum(
    grade=10, subject_id="G10-03",
    subject_title="defmacro introduction",
    fable="boy-wolf",
    examples=[
        _ex("(do (defmacro my-when [t & body] `(if ~t (do ~@body))) "
            "(my-when true 1 2 3))", 3,
            "a tiny when-style macro and a call to it",
            "what (my-when true 1 2 3) returns",
            scenario=(
                "Tom had taken to writing shorthand drill-cards on the "
                "watchhouse wall — one-line abbreviations for routines "
                "the village ran every day. Carol watched, holding a "
                "fresh card and a stick of chalk."
            ),
            need=(
                "The shorthand was easy to write but the watchhouse's "
                "runner needed the full sequence. Carol's job was to "
                "rewrite each shorthand card into the spelled-out drill "
                "before runtime — the runner only ever saw the full "
                "sequence."
            ),
                mapping=(
                "`defmacro` registers the elder's rewrite rule. When "
                "the shorthand `my-when` appears, Carol — at compile "
                "time, before the runtime ever sees the form — rewrites "
                "it into the spelled-out `if` plus `do` body. The "
                "runtime then evaluates the rewritten form."
            ),
            resolution=(
                'the rewrite landed correctly: the shorthand expanded to its full drill, and the runtime returned the value the spelled-out form produced (with `1` as the input value) (with `3` as the input value).'
            )),
        _ex("(do (defmacro twice [x] `(do ~x ~x)) (twice 7))", 7,
            "a macro that emits its argument twice in a do",
            "what (twice 7) returns",
            scenario=(
                "Carol had designed a drill-card named `twice` that took one "
                "shorthand and wrote it out twice in sequence. Tom tried the shorthand "
                "`(twice 7)` on a day when he needed the value computed twice."
            ),
            need=(
                "Some watches required a repeated action. Carol's macro needed to expand "
                "the shorthand into the spelled-out sequence so the runtime would see "
                "the value worked through twice."
            ),
            mapping=(
                "`defmacro` registers the rewrite rule. When Tom called `(twice 7)`, "
                "Carol rewrote it as `(do 7 7)` before the runtime saw it — the macro "
                "took the single argument and emitted it twice, wrapped in a `do` "
                "so both could execute."
            ),
            resolution=(
                "the call returned 7 — the last value in the `do` sequence, since `do` returns only its final expression. The macro's expansion had worked correctly."
            )),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-04 — Macro expansion rule
G10_04 = SubjectCurriculum(
    grade=10, subject_id="G10-04",
    subject_title="Macro expansion rule",
    fable="boy-wolf",
    examples=[
        _ex("(macroexpand-1 '(when true 1))", ["if", True, ["do", 1]],
            "the one-step expansion of (when true 1)",
            "what macroexpand-1 returns for (when true 1)",
            scenario=(
                "Carol held a shorthand `(when true 1)` and asked Tom to trace its "
                "expansion one step. Tom wanted to know what the macro-rewriter would "
                "produce — the one-step rewrite, not the full evaluation."
            ),
            need=(
                "The village's macro-audit tool needed to show the intermediate form "
                "after the first rewrite but before the runtime's final evaluation. "
                "Tom had to trust the step-by-step expansion, not the final value."
            ),
            mapping=(
                "`macroexpand-1` shows the first rewrite step only. The shorthand `when` "
                "becomes `if` plus `do` on the first pass — Carol's rule has been "
                "applied once, but nested macros haven't been expanded yet."
            ),
            resolution=(
                "the function returned the one-step expansion: the `when` had become `if` plus `do`, exactly the rewrite Carol's rule prescribed on its first pass."
            )),
        _ex("(macroexpand-1 '(or a b))",
            ["let*", ["or__1__auto__", "a"],
             ["if", "or__1__auto__", "or__1__auto__", ["clojure.core/or", "b"]]],
            "the one-step expansion of (or a b)",
            "what macroexpand-1 returns for (or a b)",
            scenario=(
                "Carol had a complex rewrite rule for `or`. Tom wanted to see just "
                "the first expansion step before the runtime took over. 'Show me what "
                "the rewrite does, not the final value,' he said."
            ),
            need=(
                "Some macros expanded into nested forms that needed unpacking. The village's "
                "audit required seeing the intermediate form so shepherds could understand "
                "the rewrite rule's structure."
            ),
            mapping=(
                "`macroexpand-1` applies Carol's rule once. The `or` becomes a `let*` "
                "with a temporary binding and then an `if` — the rewrite shows short-circuit "
                "logic in one step. Further macro expansions wait for the next call."
            ),
            resolution=(
                "the function returned the single-step expansion showing the `let*` and `if` structure Carol's `or` rule prescribed, pausing before any further rewrites."
            )),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-05 — macroexpand
G10_05 = SubjectCurriculum(
    grade=10, subject_id="G10-05",
    subject_title="macroexpand",
    fable="boy-wolf",
    examples=[
        _ex("(macroexpand '(when true 1))", ["if", True, ["do", 1]],
            "the full expansion of (when true 1)",
            "what macroexpand returns for (when true 1)",
            scenario=(
                "Carol and Tom stood by the watchhouse slate, looking at the shorthand "
                "`(when true 1)`. 'Show me every step the rewriter takes,' Tom asked, "
                "'until no more rules apply.'"
            ),
            need=(
                "To debug a macro chain, the watchhouse's shepherds needed to see the "
                "form after every rewrite rule had been applied, all the way through "
                "until the rules stopped firing."
            ),
            mapping=(
                "`macroexpand` applies Carol's rewrite rules repeatedly until no more "
                "macros remain. Unlike `macroexpand-1` which stops after one step, "
                "`macroexpand` keeps going until the form is fully expanded."
            ),
            resolution=(
                'the function returned the complete expansion: the `when` fully transformed into `if` plus `do`, with all rewrite rules exhausted.'
            )),
        _ex("(macroexpand '(-> 1 inc inc))", ["inc", ["inc", 1]],
            "the full expansion of (-> 1 inc inc)",
            "what macroexpand returns for the threading form",
            scenario=(
                "Tom had a threading shorthand `(-> 1 inc inc)` and wanted Carol to show "
                "him the fully expanded form — all the rewrites applied until there were no "
                "more macros left."
            ),
            need=(
                "Threading macros expand by rearranging arguments. Tom needed to see the "
                "final form after all the threading rules had been applied, so he could "
                "trace the argument flow."
            ),
            mapping=(
                "`macroexpand` fully expands `->`. The threading macro rewrites "
                "`(-> 1 inc inc)` by threading the value 1 through each function: "
                "first `(inc 1)`, then `(inc result)`. Every rewrite rule fires until "
                "the form is plain."
            ),
            resolution=(
                'the function returned the fully expanded form: the threading had rearranged the nesting to show the exact flow of the argument through each function.'
            )),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-06 — when / unless macros
G10_06 = SubjectCurriculum(
    grade=10, subject_id="G10-06",
    subject_title="when and when-not as macros",
    fable="boy-wolf",
    examples=[
        _ex("(when true 1 2 3)", 3,
            "the expression (when true 1 2 3)",
            "what (when true 1 2 3) returns",
            scenario=(
                "Carol had a drill-card shorthand `when` for conditional watches. Tom used it "
                "with a true condition: `(when true 1 2 3)`. 'Which value comes back?' he asked."
            ),
            need=(
                "The watch protocol sometimes ran only if a condition held true. When it "
                "did, the runtime needed to evaluate all the expressions and return the last."
            ),
            mapping=(
                "`when` is a macro that expands to an `if` that wraps its body in a `do`. "
                "With a true condition, the body executes and the `do` returns the final value. "
                "With false, the `when` returns nil."
            ),
            resolution=(
                'since the condition was true, the form ran the body and returned the result — the last value in the sequence. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'           )),
        _ex("(when false 1 2 3)", None,
            "the expression (when false 1 2 3)",
            "what (when false 1 2 3) returns",
            scenario=(
                "Tom tried the same `when` macro with a false condition this time: "
                "`(when false 1 2 3)`. Carol explained what would happen."
            ),
            need=(
                "When the condition failed, the watch should not run — the whole expression "
                "had to return nil without evaluating the body."
            ),
            mapping=(
                "`when` with a false condition skips the entire body and returns nil. "
                "The macro's expansion into `if` ensures that when the test fails, "
                "nothing after it is evaluated."
            ),
            resolution=(
                'since the condition was false, the form skipped the body entirely and returned nil — no values in the sequence were computed. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'         )),
        _ex("(when-not false :ok)", ":ok",
            "the expression (when-not false :ok)",
            "what (when-not false :ok) returns",
            scenario=(
                "Carol had another shorthand that inverted the test."
            ),
            need=(
                "Some watches ran only when a condition was false."
            ),
            mapping=(
                "`when-not` is a macro that inverts the condition and expands to a negated-test form."
            ),
            resolution=(
                'The condition was false, so `when-not` inverted it to true and the body executed (with `ok` as the input value) (with `:ok` as the input value).'
            )),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-07 — Threading macros revisited
G10_07 = SubjectCurriculum(
    grade=10, subject_id="G10-07",
    subject_title="Threading macros revisited",
    fable="boy-wolf",
    examples=[
        _ex("(-> 5 inc inc inc)", 8,
            "the thread-first form (-> 5 inc inc inc)",
            "what (-> 5 inc inc inc) returns",
            scenario=(
                "Carol had drawn a thread-first drill-card on the slate: "
                "`(-> 5 inc inc inc)`. Tom watched the value flow through each function. "
                "'How does it thread?' he asked."
            ),
            need=(
                "The village's pipelines needed to pass a value through a series of "
                "functions, each taking and returning a single argument. Thread-first "
                "places the value as the first argument to each function."
            ),
            mapping=(
                "`->` is a macro that threads a value through a list of function calls. "
                "`(-> 5 inc inc inc)` becomes `(inc (inc (inc 5)))` — the value 5 flows "
                "through three `inc` calls, each receiving it as the first argument."
            ),
            resolution=(
                'starting with 5, each `inc` added 1, so the result was 8 — the value had threaded correctly through all three functions. Tom chalked {drawn.a} on the townsfolk notice, and the morning record stood for the next shepherd to read.'           )),
        _ex("(->> [1 2 3 4] (filter even?) (map inc) (reduce +))", 8,
            "a thread-last pipeline over [1 2 3 4]",
            "what the ->> pipeline returns",
            scenario=(
                "Carol had a thread-last drill-card with filter, map, and reduce."
            ),
            need=(
                "Some function chains take the data as the last argument, not the first."
            ),
            mapping=(
                "`->>` threads the data as the last argument through each function."
            ),
            resolution=(
                'The data flowed through the pipeline and produced the final result. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'
            )),
        _ex("(macroexpand '(-> x f g))", ["g", ["f", "x"]],
            "the expansion of (-> x f g)",
            "what macroexpand produces for the threading form",
            scenario=(
                "Tom wanted to see how the thread-first macro rewrote its shorthand. "
                "Carol used `macroexpand` on `(-> x f g)` to show the full expansion."
            ),
            need=(
                "Understanding the rewrite rule for threading macros helped shepherds "
                "predict how their data would flow through complex pipelines."
            ),
            mapping=(
                "`->` expands by nesting the value as the first argument to each function. "
                "`(-> x f g)` becomes `(g (f x))` — the value x is passed to f first, "
                "then the result to g."
            ),
            resolution=(
                'the expanded form showed the nesting clearly: g applied to the result of f applied to x — exactly the thread-first rule.'           )),
    ],
    subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-08 — macro vs fn
G10_08 = SubjectCurriculum(
    grade=10, subject_id="G10-08",
    subject_title="Macro vs fn",
    fable="boy-wolf",
    examples=[
        # A function evaluates its args; a macro receives unevaluated forms.
        _ex("(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))", 7,
            "a plain function adding two numbers",
            "the result of calling a function",
            scenario=(
                "Carol had taught Tom the difference between a function and a macro. "
                "She showed him `add-fn` — a function that added two numbers. 'What happens "
                "when I call it with 3 and 4?' Tom asked."
            ),
            need=(
                "Tom needed to understand that a function always evaluates its arguments "
                "first, then applies the function body to the values."
            ),
            mapping=(
                "A function receives evaluated values. When `(add-fn 3 4)` is called, "
                "the runtime evaluates 3 and 4 first (they're already values), then passes "
                "them to the function body where a is 3 and b is 4."
            ),
            resolution=(
                'The function received the values and returned the expected result. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'
            )),
        _ex("(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))", 7,
            "a macro that emits the same addition form",
            "the result the macro yields after expansion + eval",
            scenario=(
                "Carol then showed Tom `add-mac` — a macro that did the same thing. "
                "'But wait,' Tom said, 'it took shorthand and rewrote it?'"
            ),
            need=(
                "Tom needed to see that a macro receives *unevaluated forms*, not values. "
                "The macro rewrites the form before the runtime evaluates it."
            ),
            mapping=(
                "A macro receives unevaluated forms. When `(add-mac 3 4)` appears, "
                "Carol rewrites it before the runtime ever sees it. The macro body `(+ ~a ~b)` "
                "with a=3 and b=4 becomes the form `(+ 3 4)`, which the runtime then evaluates."
            ),
            resolution=(
                'The macro rewrote the shorthand and the runtime evaluated it to the same result as the function.'
            )),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-09 — hygiene and gensym
G10_09 = SubjectCurriculum(
    grade=10, subject_id="G10-09",
    subject_title="Hygiene and gensym",
    fable="boy-wolf",
    examples=[
        # gensym always returns a fresh symbol; we test symbol? predicate.
        _ex("(symbol? (gensym))", True,
            "the predicate (symbol? (gensym))",
            "whether (gensym) returns a symbol",
            scenario=(
                "Carol explained that macro hygiene mattered: the rewrite rule mustn't "
                "accidentally capture a name the user already used. She showed Tom `gensym`, "
                "a function that generated fresh symbol names."
            ),
            need=(
                "Macros needed temporary names that could never collide with user names. "
                "Gensym created brand-new symbols every time, guaranteeing uniqueness."
            ),
            mapping=(
                "`gensym` creates a fresh symbol each time it's called. The result is "
                "always a symbol (a name), never a value, so it can be tested with `symbol?`."
            ),
            resolution=(
                'the predicate confirmed that `gensym` returns a symbol — a name, not a number or value, ready to be used as a unique temporary binding in a macro.'
            )),
        _ex("(let [a (gensym \"x_\") b (gensym \"x_\")] (= a b))", False,
            "two distinct gensyms with the same prefix",
            "whether two fresh gensyms are equal",
            scenario=(
                "Tom asked whether two `gensym` calls with the same prefix would produce "
                "the same name. Carol shook her head. 'Each call is fresh,' she said."
            ),
            need=(
                "Macro hygiene depended on gensym's uniqueness guarantee. Even if two "
                "gensyms had the same prefix, they had to be different — no accidental "
                "collisions."
            ),
            mapping=(
                "`gensym` always returns a fresh symbol, never the same one twice. Even if "
                "both calls use the prefix `x_`, each generates a unique symbol with a different "
                "suffix appended."
            ),
            resolution=(
                'the equality test returned the verdict — the two symbols were different, confirming that gensym had generated distinct names despite the shared prefix.'
            )),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-10 — anaphoric macros are a bad idea
G10_10 = SubjectCurriculum(
    grade=10, subject_id="G10-10",
    subject_title="Anaphoric macros are confusing",
    fable="boy-wolf",
    examples=[
        # An anaphoric `aif` would inject `it` un-hygienically. We illustrate
        # the safer hygienic alternative: an explicit name.
        _ex("(do (defmacro safe-if-let [bind then else] "
            "`(if-let ~bind ~then ~else)) "
            "(safe-if-let [x 5] (* x 2) 0))", 10,
            "a hygienic if-let style macro avoiding anaphoric injection",
            "what the hygienic if-let macro returns",
            scenario=(
                "Carol warned Tom about a tempting but dangerous macro style: anaphoric "
                "macros that secretly inject a name into the user's code. She showed him "
                "a safe alternative: `safe-if-let`, which bound the name explicitly."
            ),
            need=(
                "Some macros tried to be clever by injecting hidden names. This caused "
                "confusion and name collisions. The village preferred explicit bindings "
                "where users knew exactly which names were in scope."
            ),
            mapping=(
                "`if-let` binds a name explicitly — you say `[x 5]` and x becomes 5 within "
                "the branches. Carol's `safe-if-let` macro forwarded this pattern without "
                "injecting any hidden names, keeping hygiene intact."
            ),
            resolution=(
                'the form evaluated to 10 — the binding x=5 was explicit and clear, and (* x 2) returned the expected result without any hidden surprise names.'
            )),
        _ex("(if-let [x 7] (* x x) 0)", 49,
            "the built-in if-let, which binds explicitly",
            "what (if-let [x 7] (* x x) 0) returns",
            scenario=(
                "Carol showed Tom the built-in `if-let` from the standard library. 'See how "
                "the binding is declared right here?' she said, pointing at `[x 7]`."
            ),
            need=(
                "Hygienic macros made their bindings crystal clear. `if-let` followed this "
                "discipline: the binding vector told you exactly what was in scope in each branch."
            ),
            mapping=(
                "`if-let` takes a binding vector and two branches. If the binding succeeds, "
                "the then-branch runs with the name bound; if it fails, the else-branch runs "
                "without the binding. No hidden names, just what's declared."
            ),
            resolution=(
                'with x bound to 7, the form (* x x) returned 49 — the explicit binding had put the name in scope, and the multiplication worked cleanly.'
            )),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-11 — Reader macros overview
G10_11 = SubjectCurriculum(
    grade=10, subject_id="G10-11",
    subject_title="Reader macros overview",
    fable="boy-wolf",
    examples=[
        # Reader macros: ', `, ~, #(...), #_, etc. Test what they read to.
        _ex("'(1 2 3)", [1, 2, 3],
            "the quote reader macro 'foo",
            "what '(1 2 3) reads as",
            scenario=(
                "Carol explained that the reader had special marks, not just symbols and "
                "numbers. The apostrophe `'` was one: a reader macro that changed how the "
                "form was read."
            ),
            need=(
                "The village's scribe had shorthand marks that the reader recognized before "
                "the runtime ever saw them. Reader macros saved space and made common patterns "
                "quicker to write."
            ),
            mapping=(
                "The quote reader macro `'` is shorthand for `quote`. The reader translates quoted forms so they are frozen before the runtime."
            ),
            resolution=(
                'the reader translated the shorthand into the quoted form, so the REPL received a list of three numbers exactly as written. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'
            )),
        _ex("(#(* % %) 6)", 36,
            "the #(...) reader macro for an anonymous fn",
            "what (#(* % %) 6) returns",
            scenario=(
                "Carol showed Tom another reader macro: `#(...)`, the shorthand for anonymous "
                "functions. 'It's even shorter than `fn`,' she said."
            ),
            need=(
                "Small one-argument functions appeared everywhere in the village's watches. "
                "The reader macro made them quick to write without spelling out `fn`, parameter "
                "names, and parentheses."
            ),
            mapping=(
                "The `#(...)` reader macro is shorthand for an anonymous function. `#(* % %)` "
                "is read as `(fn [%] (* % %))` — a function that takes one argument (written as `%`) "
                "and multiplies it by itself."
            ),
            resolution=(
                'The reader macro produced an anonymous function, which computed the square of the argument (with `6` as the input value).'
            )),
        _ex("[1 #_ 2 3]", [1, 3],
            "the #_ form-skip reader macro",
            "what [1 #_ 2 3] reads as",
            scenario=(
                "Carol had a form on the slate with a comment-like mark in the middle: "
                "`#_` followed by 2. 'This skips whatever comes next,' she explained."
            ),
            need=(
                "The scribe sometimes needed to comment out a single form without writing a "
                "full-line comment. The `#_` reader macro let the reader skip any form."
            ),
            mapping=(
                "The `#_` reader macro skips the next form entirely. When the reader sees "
                "`[1 #_ 2 3]`, it reads the 1, sees the skip marker, skips the 2, and reads "
                "the 3, resulting in a vector with only the first and third elements."
            ),
            resolution=(
                'the reader skipped the 2 and produced a vector with only [1 3] — the form-skip marker had worked exactly as the reader rules prescribed.'
            )),
    ],
    subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-12 — Tagged literals
G10_12 = SubjectCurriculum(
    grade=10, subject_id="G10-12",
    subject_title="Tagged literals",
    fable="boy-wolf",
    examples=[
        # Tagged literals are read into typed values. Test predicates on them.
        _ex("(inst? #inst \"2024-01-01\")", True,
            "the predicate (inst? #inst \"2024-01-01\")",
            "whether the #inst tagged literal reads to an inst",
            scenario=(
                "Carol had a marked form on the slate: `#inst \"2024-01-01\"`. Tom asked "
                "what the tag `#inst` meant. 'A label that tells the reader how to interpret "
                "the string,' Carol said."
            ),
            need=(
                "The village's date-keepers needed types — dates, times, IDs — that the reader "
                "could produce directly from marked strings. A tagged literal did exactly that."
            ),
            mapping=(
                "The reader sees `#inst` and knows to read the string as a date-time object, "
                "not just a string. The tag directs the reader to construct the right type from "
                "the marked data."
            ),
            resolution=(
                'the predicate `inst?` confirmed that the reader had converted the marked string into a date-time object — the tag had worked correctly.'           )),
        _ex("(uuid? #uuid \"00000000-0000-0000-0000-000000000000\")", True,
            "the predicate on a #uuid tagged literal",
            "whether the #uuid tagged literal reads to a uuid",
            scenario=(
                "Carol had another marked string: `#uuid \"00000000-0000-0000-0000-000000000000\"`. "
                "Tom asked whether the uuid tag worked the same way as the date tag."
            ),
            need=(
                "The village used unique identifiers to track sheep and records. The uuid tag "
                "let the reader recognize and construct UUID objects directly from the marked format."
            ),
            mapping=(
                "Tagged literals work the same way for any type. The reader sees `#uuid` and "
                "constructs a UUID object from the marked string, just as it constructs dates "
                "from `#inst` marked strings."
            ),
            resolution=(
                'the predicate `uuid?` confirmed that the marked string had been read as a proper UUID object — the tag and reader had cooperated correctly.'           )),
    ],
    subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-13 — Data readers (EDN extension)
G10_13 = SubjectCurriculum(
    grade=10, subject_id="G10-13",
    subject_title="Data readers and EDN extension",
    fable="boy-wolf",
    examples=[
        # EDN read-string with a default tag handler.
        _ex("(clojure.edn/read-string \"42\")", 42,
            "edn read-string of \"42\"",
            "what edn/read-string returns for the source \"42\"",
            scenario=(
                "Carol explained that sometimes the meadow folk needed to read data from a scroll "
                "or message — text that arrived as a string. The EDN reader could parse it."
            ),
            need=(
                "The village's records arrived as text from the neighboring settlements. "
                "They needed a way to read a string of Clojure source and get back the data "
                "it represented."
            ),
            mapping=(
                "`edn/read-string` parses a string of Clojure source the same way the normal "
                "reader would parse it from a file or console. It reads the data and returns "
                "the value it represents."
            ),
            resolution=(
                'the function read the string "42" and returned the number 42 — the data had been parsed and interpreted correctly.'
            )),
        _ex("(clojure.edn/read-string \"[:a :b :c]\")", [":a", ":b", ":c"],
            "edn read-string of a vector source",
            "what edn/read-string returns for \"[:a :b :c]\"",
            scenario=(
                "Tom received a message scroll with a vector of keywords written out as text: "
                "`[:a :b :c]`. Carol showed him how `edn/read-string` could parse it."
            ),
            need=(
                "The village's data formats often arrived as text representing complex structures. "
                "The EDN reader needed to handle vectors, keywords, and all the standard Clojure "
                "data types."
            ),
            mapping=(
                "`edn/read-string` treats its input the same way the normal reader would. "
                "A vector of keywords in text form is read into an actual vector of keywords. "
                "The syntax rules are identical."
            ),
            resolution=(
                'the function parsed the text and returned a vector of three keywords — the EDN reader had reconstructed the structured data from its text form.'
            )),
    ],
    subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-14 — eval
G10_14 = SubjectCurriculum(
    grade=10, subject_id="G10-14",
    subject_title="eval (the function)",
    fable="boy-wolf",
    examples=[
        _ex("(eval '(+ 1 2 3))", 6,
            "the expression (eval '(+ 1 2 3))",
            "what eval returns for the quoted (+ 1 2 3)",
            scenario=(
                "Carol explained that sometimes the townsfolk needed to take a form that had "
                "been held as data — quoted, frozen — and ask the runtime to evaluate it. "
                "`eval` did exactly that."
            ),
            need=(
                "Some watches generated forms on the fly and needed them evaluated in the "
                "current context. Eval transformed frozen forms back into runtime evaluation."
            ),
            mapping=(
                "`eval` takes a quoted form (data) and evaluates it in the current scope. "
                "The quoted form `'(+ 1 2 3)` is frozen data; `eval` unfreezes it and asks "
                "the runtime to evaluate the arithmetic."
            ),
            resolution=(
                'Eval unthawed the quoted form and evaluated it, turning frozen data into live computation.'
            )),
        _ex("(eval (list '+ 4 5))", 9,
            "eval applied to a constructed list",
            "what eval returns when handed (list '+ 4 5)",
            scenario=(
                "Tom asked what would happen if the valley constructed a form dynamically. "
                "Carol showed him a form built with `list`: `(list '+ 4 5)`. 'Can `eval` "
                "handle hand-built forms?' he asked."
            ),
            need=(
                "Dynamically constructed forms needed to be evaluated just like quoted ones. "
                "The village's watches sometimes built forms piece by piece and needed to "
                "run the final result."
            ),
            mapping=(
                "`eval` doesn't care whether the form came from a quote or from `list`. "
                "It takes any form as data and evaluates it. A hand-constructed list "
                "`(+ 4 5)` is evaluated identically to a quoted one."
            ),
            resolution=(
                'eval evaluated the constructed list `(+ 4 5)` and returned 9 — hand-built forms flowed through eval as smoothly as quoted ones.'
            )),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-15 — When NOT to write a macro
G10_15 = SubjectCurriculum(
    grade=10, subject_id="G10-15",
    subject_title="When not to write a macro",
    fable="boy-wolf",
    examples=[
        # Most of the time, a function suffices. Test forms that show
        # a function would do.
        _ex("(do \"a function suffices when no syntax shaping is needed\" "
            "((fn [x y] (+ x y)) 3 4))", 7,
            "a function call where no macro is justified",
            "what the plain function call returns",
            scenario=(
                "Tom was tempted to write a macro for every shorthand, but Carol stopped him. "
                "'Most of the time, a plain function suffices,' she said. She showed him a "
                "simple addition: `((fn [x y] (+ x y)) 3 4)`."
            ),
            need=(
                "Macros were powerful but complicated. The village's discipline was to use "
                "them only when they were truly needed — when plain functions wouldn't solve "
                "the problem."
            ),
            mapping=(
                "A function takes values and applies logic. No rewrite rule is needed. "
                "For simple arithmetic, a plain `fn` is clearer, faster to write, and easier "
                "to understand than a macro."
            ),
            resolution=(
                'The function call worked perfectly. No macro overhead was needed. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'
            )),
        _ex("(do \"prefer fn unless you must shape syntax\" "
            "(map inc [1 2 3]))", [2, 3, 4],
            "map applied to inc — no macro needed",
            "the result of mapping inc",
            scenario=(
                "Carol explained that higher-order functions like `map` made many tasks easy "
                "without any macro. 'When syntax isn't the problem, use a function,' she said, "
                "showing `(map inc [1 2 3])`."
            ),
            need=(
                "The village's shepherds often wanted to apply a function to each item in a "
                "sequence. This was a data problem, not a syntax problem, so a plain function "
                "was the answer."
            ),
            mapping=(
                "`map` is a function that takes a function and a sequence, applies the function "
                "to each item, and returns a new sequence of the results. No rewrite rule, no "
                "complexity — just function composition."
            ),
            resolution=(
                'map applied inc to each number in [1 2 3] and returned [2 3 4] — the plain function had solved the problem elegantly. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'           )),
    ],
    subplots=_REWRITERULE_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-16 — Macro pattern library (with-X, def-X-thing)
G10_16 = SubjectCurriculum(
    grade=10, subject_id="G10-16",
    subject_title="Macro pattern library",
    fable="boy-wolf",
    examples=[
        # A `with-` style macro that binds and ensures cleanup conceptually.
        _ex("(do (defmacro with-careful-watch [& body] "
            "`(let [pace# :alert-and-honest] ~@body)) "
            "(with-careful-watch 42))", 42,
            "a with-X macro pattern that binds a local and runs body",
            "what the with- macro yields",
            scenario=(
                "Carol had discovered that certain macro patterns appeared repeatedly in the "
                "village's watches. The `with-` pattern bound a temporary value and ran a body "
                "of code within that binding."
            ),
            need=(
                "Setting up and tearing down bindings were common tasks. Carol's macro pattern "
                "let shepherds write the body code without worrying about the setup — the macro "
                "handled it."
            ),
            mapping=(
                "The `with-` macro pattern uses unquote-splice `~@` to expand the body forms "
                "directly into the let binding. The macro's gensymed binding `pace#` is fresh "
                "and won't collide with user names."
            ),
            resolution=(
                'the macro bound the pace and ran the body, returning 42 — the with-pattern had established its temporary binding and executed cleanly.'
            )),
        # A `def-X-thing` style: macro that defs a named thing.
        _ex("(do (defmacro def-watch [name v] `(def ~name ~v)) "
            "(def-watch watch-mode :alert) watch-mode)", ":alert",
            "a def-X-thing macro that introduces a named binding",
            "the value of the symbol the macro defined",
            scenario=(
                "Carol showed Tom another pattern: macros that defined named bindings. "
                "`def-watch` was a shorthand for defining a watch-mode value by name."
            ),
            need=(
                "The village often needed to create named global bindings for configuration "
                "and constants. Carol's `def-` pattern let shepherds write the name and value "
                "without spelling out the full `def` form."
            ),
            mapping=(
                "The `def-` style macro rewrites shorthand into a `def` form. `(def-watch watch-mode :alert)` "
                "becomes `(def watch-mode :alert)` — the macro captures the name and value and "
                "submits them to `def`."
            ),
            resolution=(
                'the macro had defined `watch-mode` with the value `:alert`, and when Tom asked for `watch-mode`, the REPL returned the bound value — the def had worked.'           )),
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
    print(f"grade-10 boy-wolf smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
