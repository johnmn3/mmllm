"""Grade 10 — macros, code as data. Through ant-grasshopper.

Subplot lens: the Ant designs a small language. Each subject is the
Grasshopper and Ant inspecting a macro, an expansion, or a piece of
syntax-quoted source. The fable's moral — patient stockpiling over
careless song — fits naturally: macros reward careful reading of
expansions over guessing.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.ant_grasshopper.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)


# ─────────────────────── grade-10 subplot extensions ───────────────────────
#
# The Ant has been quietly designing a small language inside Clojure.
# The Grasshopper keeps wanting to skip past the expansion step and
# just guess what the macro returns — insisting macros are "just
# functions." Each template lets the form carry the technical detail
# while the fable carries the manner.

_MACRO_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    SubplotTemplate("""\
{ant_phrase} had spent the morning {place} sketching a tiny language of
{ant_his_her} own — a notebook of macros that wrote other forms. The
next entry was {concept_phrase}, and the form {form_display} was what
{ant} wanted {grasshopper_phrase} to submit so the REPL could show what
code it produced or what value it returned."""),

    SubplotTemplate("""\
"A macro is just a function that runs at compile time," {ant} explained
{place}, {emo_patient}. {grasshopper}, {emo_proud}, said
{grasshopper_he_she} could already see what {concept_phrase} meant.
{ant_phrase} insisted they actually evaluate {form_display} and read
what the runtime reported, expansion or value."""),

    SubplotTemplate("""\
The path {place} was littered with old macro definitions someone had
carved into bark. {grasshopper_phrase} found one shaped like
{concept_phrase} and dared {ant_phrase} to predict its expansion.
{ant} only smiled and asked {grasshopper_him_her} to write {form_display}
into the REPL — that, after all, was the whole point of having a
macroexpander."""),

    SubplotTemplate("""\
{grasshopper_phrase} insisted {place} that macros were the same as
functions. {ant_phrase}, {emo_patient}, drew the form {form_display} on
a strip of bark. "The difference," {ant_he_she} said, "is in
{concept_phrase}. Submit the form and let the runtime tell us
exactly what it does.\""""),

    SubplotTemplate("""\
A small notebook lay open {place} where the Ant had been studying
syntax-quote. The page showed {concept_phrase}, with the form
{form_display} circled in pencil. {grasshopper_phrase}, {emo_tired},
agreed to write the form to settle once and for all what it produced."""),

    SubplotTemplate("""\
At a stone tablet {place}, {ant_phrase} was teaching {grasshopper_phrase}
the discipline of expansion: never trust your eyes, only the
macroexpander. The day's example was {concept_phrase}. The form
{form_display} had to be submitted; nothing else would do."""),
]


def _ex(form, expected, concept, what):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what)


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
    fable="ant-grasshopper",
    examples=[
        _ex("(quote (+ 1 2))", ["+", 1, 2],
            "the quoted form (quote (+ 1 2))",
            "the list (quote (+ 1 2)) yields"),
        _ex("'(1 2 3)", [1, 2, 3],
            "the quoted list '(1 2 3)",
            "the value of '(1 2 3)"),
        _ex("(let [x 5] `(a ~x b))", ["a", 5, "b"],
            "a syntax-quoted list with one unquote",
            "the result of `(a ~x b) when x is 5"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-02 — syntax-quote
G10_02 = SubjectCurriculum(
    grade=10, subject_id="G10-02",
    subject_title="syntax-quote",
    fable="ant-grasshopper",
    examples=[
        _ex("(let [x 10] `(+ ~x ~x))", ["+", 10, 10],
            "a syntax-quoted addition with x unquoted twice",
            "the form produced by `(+ ~x ~x) when x is 10"),
        _ex("(let [xs [1 2 3]] `(list ~@xs))", ["list", 1, 2, 3],
            "a syntax-quoted list with unquote-splice",
            "the form produced by `(list ~@xs) when xs is [1 2 3]"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-03 — defmacro introduction
G10_03 = SubjectCurriculum(
    grade=10, subject_id="G10-03",
    subject_title="defmacro introduction",
    fable="ant-grasshopper",
    examples=[
        _ex("(do (defmacro my-when [t & body] `(if ~t (do ~@body))) "
            "(my-when true 1 2 3))", 3,
            "a tiny when-style macro and a call to it",
            "what (my-when true 1 2 3) returns"),
        _ex("(do (defmacro twice [x] `(do ~x ~x)) (twice 7))", 7,
            "a macro that emits its argument twice in a do",
            "what (twice 7) returns"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-04 — Macro expansion rule
G10_04 = SubjectCurriculum(
    grade=10, subject_id="G10-04",
    subject_title="Macro expansion rule",
    fable="ant-grasshopper",
    examples=[
        _ex("(macroexpand-1 '(when true 1))", ["if", True, ["do", 1]],
            "the one-step expansion of (when true 1)",
            "what macroexpand-1 returns for (when true 1)"),
        _ex("(macroexpand-1 '(or a b))",
            ["let*", ["or__1__auto__", "a"],
             ["if", "or__1__auto__", "or__1__auto__", ["clojure.core/or", "b"]]],
            "the one-step expansion of (or a b)",
            "what macroexpand-1 returns for (or a b)"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-05 — macroexpand
G10_05 = SubjectCurriculum(
    grade=10, subject_id="G10-05",
    subject_title="macroexpand",
    fable="ant-grasshopper",
    examples=[
        _ex("(macroexpand '(when true 1))", ["if", True, ["do", 1]],
            "the full expansion of (when true 1)",
            "what macroexpand returns for (when true 1)"),
        _ex("(macroexpand '(-> 1 inc inc))", ["inc", ["inc", 1]],
            "the full expansion of (-> 1 inc inc)",
            "what macroexpand returns for the threading form"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-06 — when / unless macros
G10_06 = SubjectCurriculum(
    grade=10, subject_id="G10-06",
    subject_title="when and when-not as macros",
    fable="ant-grasshopper",
    examples=[
        _ex("(when true 1 2 3)", 3,
            "the form (when true 1 2 3)",
            "what (when true 1 2 3) returns"),
        _ex("(when false 1 2 3)", None,
            "the form (when false 1 2 3)",
            "what (when false 1 2 3) returns"),
        _ex("(when-not false :ok)", ":ok",
            "the form (when-not false :ok)",
            "what (when-not false :ok) returns"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-07 — Threading macros revisited
G10_07 = SubjectCurriculum(
    grade=10, subject_id="G10-07",
    subject_title="Threading macros revisited",
    fable="ant-grasshopper",
    examples=[
        _ex("(-> 5 inc inc inc)", 8,
            "the thread-first form (-> 5 inc inc inc)",
            "what (-> 5 inc inc inc) returns"),
        _ex("(->> [1 2 3 4] (filter even?) (map inc) (reduce +))", 8,
            "a thread-last pipeline over [1 2 3 4]",
            "what the ->> pipeline returns"),
        _ex("(macroexpand '(-> x f g))", ["g", ["f", "x"]],
            "the expansion of (-> x f g)",
            "what macroexpand produces for the threading form"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-08 — macro vs fn
G10_08 = SubjectCurriculum(
    grade=10, subject_id="G10-08",
    subject_title="Macro vs fn",
    fable="ant-grasshopper",
    examples=[
        # A function evaluates its args; a macro receives unevaluated forms.
        _ex("(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))", 7,
            "a plain function adding two numbers",
            "the result of calling a function"),
        _ex("(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3 4))", 7,
            "a macro that emits the same addition form",
            "the result the macro yields"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-09 — hygiene and gensym
G10_09 = SubjectCurriculum(
    grade=10, subject_id="G10-09",
    subject_title="Hygiene and gensym",
    fable="ant-grasshopper",
    examples=[
        # gensym always returns a fresh symbol; we test symbol? predicate.
        _ex("(symbol? (gensym))", True,
            "the predicate (symbol? (gensym))",
            "whether (gensym) returns a symbol"),
        _ex("(let [a (gensym \"x_\") b (gensym \"x_\")] (= a b))", False,
            "two distinct gensyms with the same prefix",
            "whether two fresh gensyms are equal"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-10 — anaphoric macros are a bad idea
G10_10 = SubjectCurriculum(
    grade=10, subject_id="G10-10",
    subject_title="Anaphoric macros are confusing",
    fable="ant-grasshopper",
    examples=[
        # An anaphoric `aif` would inject `it` un-hygienically. We illustrate
        # the safer hygienic alternative: an explicit name.
        _ex("(do (defmacro safe-if-let [bind then else] "
            "`(if-let ~bind ~then ~else)) "
            "(safe-if-let [x 5] (* x 2) 0))", 10,
            "a hygienic if-let style macro avoiding anaphoric injection",
            "what the hygienic if-let macro returns"),
        _ex("(if-let [x 7] (* x x) 0)", 49,
            "the built-in if-let, which binds explicitly (not anaphorically)",
            "what (if-let [x 7] (* x x) 0) returns"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-11 — Reader macros overview
G10_11 = SubjectCurriculum(
    grade=10, subject_id="G10-11",
    subject_title="Reader macros overview",
    fable="ant-grasshopper",
    examples=[
        # Reader macros: ', `, ~, #(...), #_, etc. Test what they read to.
        _ex("'(1 2 3)", [1, 2, 3],
            "the quote reader macro 'foo",
            "what '(1 2 3) reads as"),
        _ex("(#(* % %) 6)", 36,
            "the #(...) reader macro for an anonymous fn",
            "what (#(* % %) 6) returns"),
        _ex("[1 #_ 2 3]", [1, 3],
            "the #_ form-skip reader macro",
            "what [1 #_ 2 3] reads as after the form-skip"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-12 — Tagged literals
G10_12 = SubjectCurriculum(
    grade=10, subject_id="G10-12",
    subject_title="Tagged literals",
    fable="ant-grasshopper",
    examples=[
        # Tagged literals are read into typed values. Test predicates on them.
        _ex("(inst? #inst \"2024-01-01\")", True,
            "the predicate (inst? #inst \"2024-01-01\")",
            "whether the #inst tagged literal reads to an inst"),
        _ex("(uuid? #uuid \"00000000-0000-0000-0000-000000000000\")", True,
            "the predicate on a #uuid tagged literal",
            "whether the #uuid tagged literal reads to a uuid"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-13 — Data readers (EDN extension)
G10_13 = SubjectCurriculum(
    grade=10, subject_id="G10-13",
    subject_title="Data readers and EDN extension",
    fable="ant-grasshopper",
    examples=[
        # EDN read-string with a default tag handler.
        _ex("(clojure.edn/read-string \"42\")", 42,
            "edn read-string of \"42\"",
            "what edn/read-string returns for the source \"42\""),
        _ex("(clojure.edn/read-string \"[:a :b :c]\")", [":a", ":b", ":c"],
            "edn read-string of a vector source",
            "what edn/read-string returns for \"[:a :b :c]\""),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-14 — eval
G10_14 = SubjectCurriculum(
    grade=10, subject_id="G10-14",
    subject_title="eval (the function)",
    fable="ant-grasshopper",
    examples=[
        _ex("(eval '(+ 1 2 3))", 6,
            "the form (eval '(+ 1 2 3))",
            "what eval returns for the quoted (+ 1 2 3)"),
        _ex("(eval (list '+ 4 5))", 9,
            "eval applied to a constructed list",
            "what eval returns when handed (list '+ 4 5)"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-15 — When NOT to write a macro
G10_15 = SubjectCurriculum(
    grade=10, subject_id="G10-15",
    subject_title="When not to write a macro",
    fable="ant-grasshopper",
    examples=[
        # Most of the time, a function suffices. Test forms that show
        # a function would do.
        _ex("(do \"a function suffices when no syntax shaping is needed\" "
            "((fn [x y] (+ x y)) 3 4))", 7,
            "a function call where no macro is justified",
            "what the plain function call returns"),
        _ex("(do \"prefer fn unless you must shape syntax\" "
            "(map inc [1 2 3]))", [2, 3, 4],
            "map applied to inc — no macro needed",
            "the result of mapping inc"),
    ],
    subplots=_MACRO_SUBPLOTS, plan_pool=_PLAN_G10,
)


# G10-16 — Macro pattern library (with-X, def-X-thing)
G10_16 = SubjectCurriculum(
    grade=10, subject_id="G10-16",
    subject_title="Macro pattern library",
    fable="ant-grasshopper",
    examples=[
        # A `with-` style macro that binds and ensures cleanup conceptually.
        _ex("(do (defmacro with-ant-pace [& body] "
            "`(let [pace# :slow-and-steady] ~@body)) "
            "(with-ant-pace 42))", 42,
            "a with-X macro pattern that binds a local and runs body",
            "what the with- macro yields"),
        # A `def-X-thing` style: macro that defs a named thing.
        _ex("(do (defmacro def-pace [name v] `(def ~name ~v)) "
            "(def-pace stockpile-pace :steady) stockpile-pace)", ":steady",
            "a def-X-thing macro that introduces a named binding",
            "the value of the symbol the macro defined"),
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
    print(f"grade-10 ant-grasshopper smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
