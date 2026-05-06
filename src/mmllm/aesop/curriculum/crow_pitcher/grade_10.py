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
        ),
        SubjectExample(
            form="'(1 2 3)",
            expected=[1, 2, 3],
            concept_phrase="the quoted list with three numbers",
            question_what="the result of quoting a three-element list",
            goal_text="quote a list of three numbers so it returns the form itself",
        ),
        SubjectExample(
            form="(let [x 5] `(a ~x b))",
            expected=["a", 5, "b"],
            concept_phrase="a syntax-quoted form with the variable unquoted",
            question_what="what you get when unquoting x inside a syntax-quoted form",
            goal_text="create a form that when x is 5 produces a list containing the value of x",
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
        ),
        SubjectExample(
            form="(let [xs [1 2 3]] `(list ~@xs))",
            expected=["list", 1, 2, 3],
            concept_phrase="building a form by splicing a vector into syntax-quote",
            question_what="the form produced when splicing a three-element vector",
            goal_text="build a form that inserts all elements of a vector into a list call",
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
                "evaluated and dropped into the pitcher."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (defmacro twice [x] `(do ~x ~x)) (twice 7))",
            expected=7,
            concept_phrase="defining a macro that repeats its argument",
            question_what="the value returned by twice expanding to a do-block with the unquoted argument repeated",
            goal_text="define a macro named twice that emits its argument twice in a do block, then call it",
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
        ),
        SubjectExample(
            form="(macroexpand-1 '(or a b))",
            expected=["let*", ["or__1__auto__", "a"],
                      ["if", "or__1__auto__", "or__1__auto__", ["clojure.core/or", "b"]]],
            concept_phrase="the one-step expansion of the or-macro call",
            question_what="the intermediate form after expanding the macro once",
            goal_text="expand an or-macro call one step to reveal its internal structure",
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
        ),
        SubjectExample(
            form="(macroexpand '(-> 1 inc inc))",
            expected=["inc", ["inc", 1]],
            concept_phrase="the complete expansion of the thread-first call",
            question_what="the final form after threading the value through all steps",
            goal_text="fully expand a thread-first macro call to see how the value threads through",
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
        ),
        SubjectExample(
            form="(when false 1 2 3)",
            expected=None,
            concept_phrase="executing expressions when a condition is false",
            question_what="the result when the condition does not hold",
            goal_text="evaluate a when-form where the condition is false",
        ),
        SubjectExample(
            form="(when-not false :ok)",
            expected=":ok",
            concept_phrase="executing an expression when a negated condition is true",
            question_what="the result when using when-not with a false condition",
            goal_text="use when-not to execute an expression when the condition is false",
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
        ),
        SubjectExample(
            form="(->> [1 2 3 4] (filter even?) (map inc) (reduce +))",
            expected=8,
            concept_phrase="threading a vector through filter, map, and reduce as the last argument",
            question_what="the sum of mapped values after filtering even numbers",
            goal_text="thread a vector through filter, map, and reduce using thread-last",
        ),
        SubjectExample(
            form="(macroexpand '(-> x f g))",
            expected=["g", ["f", "x"]],
            concept_phrase="the expanded form of a thread-first call",
            question_what="the nested function calls after expansion",
            goal_text="expand a thread-first macro to see how functions compose",
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
        ),
        SubjectExample(
            form="(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))",
            expected=7,
            concept_phrase="calling a macro that emits an addition form",
            question_what="the sum returned when add-mac expands to an addition of the unquoted arguments",
            goal_text="define a macro add-mac and call it to add 3 and 4",
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
        ),
        SubjectExample(
            form="(let [a (gensym \"x_\") b (gensym \"x_\")] (= a b))",
            expected=False,
            concept_phrase="comparing two gensyms created with the same prefix",
            question_what="whether two fresh gensyms are identical",
            goal_text="generate two gensyms with the same prefix and check if they are equal",
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
        ),
        SubjectExample(
            form="(if-let [x 7] (* x x) 0)",
            expected=49,
            concept_phrase="using the built-in if-let with an explicit binding",
            question_what="the result of the then-branch when the binding succeeds",
            goal_text="use if-let to bind x to 7 and return the square of x",
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
            goal_text="use the quote reader macro to read a list of three numbers",
        ),
        SubjectExample(
            form="(#(* % %) 6)",
            expected=36,
            concept_phrase="using the anonymous-function reader macro",
            question_what="the result of calling the generated function",
            goal_text="use the #(...) reader macro to create a function that squares its argument",
        ),
        SubjectExample(
            form="[1 #_ 2 3]",
            expected=[1, 3],
            concept_phrase="using the discard reader macro to skip an element",
            question_what="the vector after the middle element is discarded",
            goal_text="use the #_ reader macro to skip an element in a vector",
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
        ),
        SubjectExample(
            form="(uuid? #uuid \"00000000-0000-0000-0000-000000000000\")",
            expected=True,
            concept_phrase="testing whether a tagged literal reads as a uuid",
            question_what="whether the uuid? predicate returns true",
            goal_text="test that a tagged literal with #uuid reads as a uuid",
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
        ),
        SubjectExample(
            form="(clojure.edn/read-string \"[:a :b :c]\")",
            expected=[":a", ":b", ":c"],
            concept_phrase="parsing a vector string with edn/read-string",
            question_what="the parsed vector from the EDN source",
            goal_text="use edn/read-string to parse a vector of keywords from a string",
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
        ),
        SubjectExample(
            form="(eval (list '+ 4 5))",
            expected=9,
            concept_phrase="evaluating a dynamically constructed form",
            question_what="the result of evaluating the constructed list",
            goal_text="construct a list that represents addition and evaluate it",
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
        ),
        SubjectExample(
            form="(do \"prefer fn unless you must shape syntax\" "
                 "(map inc [1 2 3]))",
            expected=[2, 3, 4],
            concept_phrase="applying a function to each element of a collection",
            question_what="the incremented values",
            goal_text="use map to increment each element of a list",
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
        ),
        # A `def-X-thing` style: macro that defs a named thing.
        SubjectExample(
            form="(do (defmacro def-pace [name v] `(def ~name ~v)) "
                 "(def-pace race-pace :slow) race-pace)",
            expected=":slow",
            concept_phrase="defining and using a def-X-thing macro pattern",
            question_what="the value of the symbol defined by def-pace when expanded with the given name and keyword value",
            goal_text="define a def-pace macro and use it to define and retrieve a value",
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
