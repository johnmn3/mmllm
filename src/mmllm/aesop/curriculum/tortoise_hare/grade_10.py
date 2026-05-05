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
        _ex("(quote (+ 1 2))", ["+", 1, 2],
            "quoting an addition form",
            "what you get when you quote an addition form",
            goal="quote an addition form so it evaluates to a list without computing"),
        _ex("'(1 2 3)", [1, 2, 3],
            "the quoted list with three numbers",
            "the result of quoting a three-element list",
            goal="quote a list of three numbers so it returns the form itself"),
        _ex("(let [x 5] `(a ~x b))", ["a", 5, "b"],
            "a syntax-quoted form with the variable unquoted",
            "what you get when unquoting x inside a syntax-quoted form",
            goal="create a form that when x is 5 produces a list containing the value of x"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-02 — syntax-quote
G10_02 = SubjectCurriculum(
    grade=10, subject_id="G10-02",
    subject_title="syntax-quote",
    fable="tortoise-hare",
    examples=[
        _ex("(let [x 10] `(+ ~x ~x))", ["+", 10, 10],
            "building a form by unquoting a variable twice inside syntax-quote",
            "the form produced when x is 10 and unquoted twice",
            goal="build a form where a variable is inserted twice into an addition form"),
        _ex("(let [xs [1 2 3]] `(list ~@xs))", ["list", 1, 2, 3],
            "building a form by splicing a vector into syntax-quote",
            "the form produced when splicing a three-element vector",
            goal="build a form that inserts all elements of a vector into a list call"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-03 — defmacro introduction
G10_03 = SubjectCurriculum(
    grade=10, subject_id="G10-03",
    subject_title="defmacro introduction",
    fable="tortoise-hare",
    examples=[
        _ex("(do (defmacro my-when [t & body] `(if ~t (do ~@body))) "
            "(my-when true 1 2 3))", 3,
            "defining a conditional macro and invoking it",
            "the value produced by calling the macro",
            goal="define a macro named my-when that takes a test and body expressions, then invoke it"),
        _ex("(do (defmacro twice [x] `(do ~x ~x)) (twice 7))", 7,
            "defining a macro that repeats its argument",
            "the result after the macro expands and evaluates",
            goal="define a macro named twice that emits its argument twice in a do block, then call it"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-04 — Macro expansion rule
G10_04 = SubjectCurriculum(
    grade=10, subject_id="G10-04",
    subject_title="Macro expansion rule",
    fable="tortoise-hare",
    examples=[
        _ex("(macroexpand-1 '(when true 1))", ["if", True, ["do", 1]],
            "the one-step expansion of the when-macro call",
            "the expanded form after one level of macro expansion",
            goal="expand a when-macro call one step to see what code it produces"),
        _ex("(macroexpand-1 '(or a b))",
            ["let*", ["or__1__auto__", "a"],
             ["if", "or__1__auto__", "or__1__auto__", ["clojure.core/or", "b"]]],
            "the one-step expansion of the or-macro call",
            "the intermediate form after expanding the macro once",
            goal="expand an or-macro call one step to reveal its internal structure"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-05 — macroexpand
G10_05 = SubjectCurriculum(
    grade=10, subject_id="G10-05",
    subject_title="macroexpand",
    fable="tortoise-hare",
    examples=[
        _ex("(macroexpand '(when true 1))", ["if", True, ["do", 1]],
            "the complete expansion of the when-macro call",
            "the fully expanded form after all macro passes",
            goal="fully expand a when-macro call to reveal the if-form it becomes"),
        _ex("(macroexpand '(-> 1 inc inc))", ["inc", ["inc", 1]],
            "the complete expansion of the thread-first call",
            "the final form after threading the value through all steps",
            goal="fully expand a thread-first macro call to see how the value threads through"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-06 — when / unless macros
G10_06 = SubjectCurriculum(
    grade=10, subject_id="G10-06",
    subject_title="when and when-not as macros",
    fable="tortoise-hare",
    examples=[
        _ex("(when true 1 2 3)", 3,
            "executing multiple expressions when a condition is true",
            "the result of the last expression when the condition holds",
            goal="execute three expressions and return the value of the last when the condition is true"),
        _ex("(when false 1 2 3)", None,
            "executing expressions when a condition is false",
            "the result when the condition does not hold",
            goal="evaluate a when-form where the condition is false"),
        _ex("(when-not false :ok)", ":ok",
            "executing an expression when a negated condition is true",
            "the result when using when-not with a false condition",
            goal="use when-not to execute an expression when the condition is false"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-07 — Threading macros revisited
G10_07 = SubjectCurriculum(
    grade=10, subject_id="G10-07",
    subject_title="Threading macros revisited",
    fable="tortoise-hare",
    examples=[
        _ex("(-> 5 inc inc inc)", 8,
            "threading a value through multiple functions in sequence",
            "the result of threading 5 through three increments",
            goal="thread the value 5 through inc three times using thread-first"),
        _ex("(->> [1 2 3 4] (filter even?) (map inc) (reduce +))", 8,
            "threading a vector through filter, map, and reduce as the last argument",
            "the sum of mapped values after filtering even numbers",
            goal="thread a vector through filter, map, and reduce using thread-last"),
        _ex("(macroexpand '(-> x f g))", ["g", ["f", "x"]],
            "the expanded form of a thread-first call",
            "the nested function calls after expansion",
            goal="expand a thread-first macro to see how functions compose"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-08 — macro vs fn
G10_08 = SubjectCurriculum(
    grade=10, subject_id="G10-08",
    subject_title="Macro vs fn",
    fable="tortoise-hare",
    examples=[
        # A function evaluates its args; a macro receives unevaluated forms.
        _ex("(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))", 7,
            "calling a plain function that adds two numbers",
            "the sum returned by the function",
            goal="define a function add-fn and call it to add 3 and 4"),
        _ex("(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))", 7,
            "calling a macro that emits an addition form",
            "the result after the macro expands and evaluates",
            goal="define a macro add-mac and call it to add 3 and 4"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-09 — hygiene and gensym
G10_09 = SubjectCurriculum(
    grade=10, subject_id="G10-09",
    subject_title="Hygiene and gensym",
    fable="tortoise-hare",
    examples=[
        # gensym always returns a fresh symbol; we test symbol? predicate.
        _ex("(symbol? (gensym))", True,
            "testing whether gensym produces a symbol",
            "whether a generated symbol is of type symbol",
            goal="test that gensym returns a symbol"),
        _ex("(let [a (gensym \"x_\") b (gensym \"x_\")] (= a b))", False,
            "comparing two gensyms created with the same prefix",
            "whether two fresh gensyms are identical",
            goal="generate two gensyms with the same prefix and check if they are equal"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-10 — anaphoric macros are a bad idea
G10_10 = SubjectCurriculum(
    grade=10, subject_id="G10-10",
    subject_title="Anaphoric macros are confusing",
    fable="tortoise-hare",
    examples=[
        # An anaphoric `aif` would inject `it` un-hygienically. We illustrate
        # the safer hygienic alternative: an explicit name.
        _ex("(do (defmacro safe-if-let [bind then else] "
            "`(if-let ~bind ~then ~else)) "
            "(safe-if-let [x 5] (* x 2) 0))", 10,
            "defining and calling a hygienic if-let macro",
            "the result when the binding succeeds",
            goal="define a safe-if-let macro and call it with x bound to 5"),
        _ex("(if-let [x 7] (* x x) 0)", 49,
            "using the built-in if-let with an explicit binding",
            "the result of the then-branch when the binding succeeds",
            goal="use if-let to bind x to 7 and return the square of x"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-11 — Reader macros overview
G10_11 = SubjectCurriculum(
    grade=10, subject_id="G10-11",
    subject_title="Reader macros overview",
    fable="tortoise-hare",
    examples=[
        # Reader macros: ', `, ~, #(...), #_, etc. Test what they read to.
        _ex("'(1 2 3)", [1, 2, 3],
            "using the quote reader macro",
            "the form read by the quote reader",
            goal="use the quote reader macro to read a list of three numbers"),
        _ex("(#(* % %) 6)", 36,
            "using the anonymous-function reader macro",
            "the result of calling the generated function",
            goal="use the #(...) reader macro to create a function that squares its argument"),
        _ex("[1 #_ 2 3]", [1, 3],
            "using the discard reader macro to skip an element",
            "the vector after the middle element is discarded",
            goal="use the #_ reader macro to skip an element in a vector"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-12 — Tagged literals
G10_12 = SubjectCurriculum(
    grade=10, subject_id="G10-12",
    subject_title="Tagged literals",
    fable="tortoise-hare",
    examples=[
        # Tagged literals are read into typed values. Test predicates on them.
        _ex("(inst? #inst \"2024-01-01\")", True,
            "testing whether a tagged literal reads as an instant",
            "whether the inst? predicate returns true",
            goal="test that a tagged literal with #inst reads as an instant"),
        _ex("(uuid? #uuid \"00000000-0000-0000-0000-000000000000\")", True,
            "testing whether a tagged literal reads as a uuid",
            "whether the uuid? predicate returns true",
            goal="test that a tagged literal with #uuid reads as a uuid"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-13 — Data readers (EDN extension)
G10_13 = SubjectCurriculum(
    grade=10, subject_id="G10-13",
    subject_title="Data readers and EDN extension",
    fable="tortoise-hare",
    examples=[
        # EDN read-string with a default tag handler.
        _ex("(clojure.edn/read-string \"42\")", 42,
            "parsing a number string with edn/read-string",
            "the parsed value from the EDN source",
            goal="use edn/read-string to parse a number from a string"),
        _ex("(clojure.edn/read-string \"[:a :b :c]\")", [":a", ":b", ":c"],
            "parsing a vector string with edn/read-string",
            "the parsed vector from the EDN source",
            goal="use edn/read-string to parse a vector of keywords from a string"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-14 — eval
G10_14 = SubjectCurriculum(
    grade=10, subject_id="G10-14",
    subject_title="eval (the function)",
    fable="tortoise-hare",
    examples=[
        _ex("(eval '(+ 1 2 3))", 6,
            "evaluating a quoted form at runtime",
            "the result of evaluating the quoted addition",
            goal="evaluate a quoted addition form at runtime"),
        _ex("(eval (list '+ 4 5))", 9,
            "evaluating a dynamically constructed form",
            "the result of evaluating the constructed list",
            goal="construct a list that represents addition and evaluate it"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-15 — When NOT to write a macro
G10_15 = SubjectCurriculum(
    grade=10, subject_id="G10-15",
    subject_title="When not to write a macro",
    fable="tortoise-hare",
    examples=[
        # Most of the time, a function suffices. Test forms that show
        # a function would do.
        _ex("(do \"a function suffices when no syntax shaping is needed\" "
            "((fn [x y] (+ x y)) 3 4))", 7,
            "calling an anonymous function to add two arguments",
            "the sum of 3 and 4",
            goal="use an anonymous function to add two numbers"),
        _ex("(do \"prefer fn unless you must shape syntax\" "
            "(map inc [1 2 3]))", [2, 3, 4],
            "applying a function to each element of a collection",
            "the incremented values",
            goal="use map to increment each element of a list"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-16 — Macro pattern library (with-X, def-X-thing)
G10_16 = SubjectCurriculum(
    grade=10, subject_id="G10-16",
    subject_title="Macro pattern library",
    fable="tortoise-hare",
    examples=[
        # A `with-` style macro that binds and ensures cleanup conceptually.
        _ex("(do (defmacro with-tortoise-pace [& body] "
            "`(let [pace# :slow-and-steady] ~@body)) "
            "(with-tortoise-pace 42))", 42,
            "defining and using a with-X macro pattern",
            "the value from the body expression",
            goal="define a with-tortoise-pace macro and call it to execute a body"),
        # A `def-X-thing` style: macro that defs a named thing.
        _ex("(do (defmacro def-pace [name v] `(def ~name ~v)) "
            "(def-pace race-pace :slow) race-pace)", ":slow",
            "defining and using a def-X-thing macro pattern",
            "the value of the defined symbol",
            goal="define a def-pace macro and use it to define and retrieve a value"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
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
