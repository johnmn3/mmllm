"""Grade 6 — namespaces and modular code. Through tortoise-hare.

Subplot lens: two characters working at separate workbenches /
copybooks / cottages, then later sharing what they've labeled. The
fable's vanity-vs-steadiness pulls in: Hare wants to scribble
everything in one place, Tortoise insists on naming the file the
form lives in and requiring it cleanly.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.tortoise_hare.grade_1 import (
    _GOAL_SUBPLOTS, _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL
)


_NS_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    # Two characters at separate workbenches, exchanging a labeled form.
    SubplotTemplate("""\
{tortoise_phrase} kept a small workbench {place}, where every form had
its own labeled drawer. {hare_phrase} preferred to scribble each
expression in a single notebook. To settle a question that morning,
{tortoise} pointed to {concept_phrase} and asked {hare} to evaluate the
form {form_display} so they could see what name belonged with what
value."""),

    # The "two cottages" / cross-namespace beat.
    SubplotTemplate("""\
The two of them lived in cottages on opposite sides {place} —
{tortoise_phrase} on one side, {hare_phrase} on the other. Each kept
their own copybook of forms. When the time came to compare notes,
{tortoise} read aloud {concept_phrase} and asked, {emo_patient}, what
the form {form_display} would return when the REPL reached across the
shared path."""),
]


def _ex(form, expected, concept, what, goal="", tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal, tags=tags)


_PLAN_G6 = _PLAN_POOL + (
    "I require the namespace and call the function.",
    "I use the fully-qualified name to reach the var.",
    "I keep the namespaces straight and let the REPL resolve the name.",
)


# ─────────────────────── 16 grade-6 subjects ───────────────────────


# G6-01 — Namespace as file
# A namespace's name is itself a symbol; we extract the string form
# to show the path-like string the namespace corresponds to.
G6_01 = SubjectCurriculum(grade=6, subject_id="G6-01",
    subject_title="Namespace as file", fable="tortoise-hare",
    examples=[
        _ex("(name 'foo.bar)", "foo.bar",
            "extracting the string form of a namespace symbol",
            "the string form of a quoted namespace symbol",
            goal="extract the string form of a quoted namespace symbol"),
        _ex("(name 'clojure.string)", "clojure.string",
            "extracting the string form of a namespace symbol",
            "the string form of a quoted namespace symbol",
            goal="extract the string form of a quoted namespace symbol"),
        _ex("(symbol? 'tortoise.race)", True,
            "checking whether a value is a symbol",
            "whether a value is a symbol",
            goal="test whether a quoted namespace-like value is a symbol"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-02 — ns form (we exercise via `name *ns*` style introspection)
G6_02 = SubjectCurriculum(grade=6, subject_id="G6-02",
    subject_title="ns form", fable="tortoise-hare",
    examples=[
        _ex("(name 'race.tortoise)", "race.tortoise",
            "extracting the string form of a namespace symbol",
            "the string form of a quoted namespace symbol",
            goal="extract the string form of a quoted namespace symbol"),
        _ex("(= 'race.tortoise 'race.tortoise)", True,
            "checking equality of two namespace symbols",
            "whether two identical namespace symbols are equal",
            goal="test whether two identical namespace symbols are equal"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-03 — require — fully qualified usage (require already loaded
# clojure.string in basilisp/clojure runtime; the form below works in
# both).
G6_03 = SubjectCurriculum(grade=6, subject_id="G6-03",
    subject_title="require", fable="tortoise-hare",
    examples=[
        _ex("(clojure.string/upper-case \"hare\")", "HARE",
            "calling a fully-qualified string function",
            "the result of calling a string transformation function",
            goal="call the uppercasing function from clojure.string on a test string"),
        _ex("(clojure.string/lower-case \"ZEBRA\")", "zebra",
            "calling a fully-qualified string function",
            "the result of calling a string transformation function",
            goal="call the lowercasing function from clojure.string on a test string"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-04 — refer-and-use (we exercise the effect: a referred name
# resolves the same as the qualified name; via `=` we compare two
# applications).
G6_04 = SubjectCurriculum(grade=6, subject_id="G6-04",
    subject_title="refer and use", fable="tortoise-hare",
    examples=[
        _ex("(= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))",
            True,
            "testing equality of two identical function calls",
            "whether two calls to the same function with the same argument produce the same result",
            goal="test whether two calls to the fully-qualified string uppercasing function with the same argument are equal"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-05 — Fully qualified names
G6_05 = SubjectCurriculum(grade=6, subject_id="G6-05",
    subject_title="Fully qualified names", fable="tortoise-hare",
    examples=[
        _ex("(clojure.string/upper-case \"hello\")", "HELLO",
            "calling a fully-qualified string function",
            "the result of calling a string transformation function",
            goal="call the uppercasing function from clojure.string on a test string"),
        _ex("(clojure.string/reverse \"abc\")", "cba",
            "calling a fully-qualified string function",
            "the result of calling a string transformation function",
            goal="call the reversing function from clojure.string on a test string"),
        _ex("(namespace :owner/item)", "owner",
            "extracting the namespace portion of a keyword",
            "the namespace part of a qualified keyword",
            goal="extract the namespace portion of a qualified keyword"),
        _ex("(name :owner/item)", "item",
            "extracting the name portion of a keyword",
            "the name part of a qualified keyword",
            goal="extract the name local portion of a qualified keyword"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-06 — Private defs (we can't test ^:private effect with eval, but
# we can confirm related metadata predicates).
G6_06 = SubjectCurriculum(grade=6, subject_id="G6-06",
    subject_title="Private defs", fable="tortoise-hare",
    examples=[
        # The :private flag is queryable as metadata on the symbol.
        _ex("(:private (meta '^:private x))", True,
            "accessing the :private flag from metadata",
            "whether the :private metadata is set on a symbol",
            goal="check whether the :private flag is present in the metadata of a symbol with :private marker"),
        _ex("(:private (meta 'x))", None,
            "accessing the :private flag from metadata",
            "whether the :private metadata is set on a plain symbol",
            goal="check whether the :private flag is present in the metadata of a plain symbol without markers"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-07 — Public vs private API (design decision; we exercise via
# the predicate `:private` on metadata).
G6_07 = SubjectCurriculum(grade=6, subject_id="G6-07",
    subject_title="Public vs private API", fable="tortoise-hare",
    examples=[
        _ex("(boolean (:private (meta '^:private hidden)))", True,
            "converting the :private metadata to a boolean",
            "whether a symbol with :private marker evaluates to true when converted to boolean",
            goal="convert the :private metadata flag of a symbol marked with :private to a boolean"),
        _ex("(boolean (:private (meta 'public)))", False,
            "converting the :private metadata to a boolean",
            "whether a symbol without :private marker evaluates to false when converted to boolean",
            goal="convert the :private metadata flag of a plain symbol to a boolean"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-08 — Circular dependencies (we exercise via a plain form that
# would resolve correctly when the dependency graph is sound; the
# narrative carries the lesson).
G6_08 = SubjectCurriculum(grade=6, subject_id="G6-08",
    subject_title="Circular dependencies", fable="tortoise-hare",
    examples=[
        _ex("(clojure.string/upper-case \"a\")", "A",
            "calling a function from a required namespace",
            "the result of uppercasing a single character",
            goal="call the string uppercasing function from clojure.string on the character a"),
        _ex("(= 'a.b 'a.b)", True,
            "testing equality of two namespace symbols",
            "whether two identical namespace symbols are equal",
            goal="test whether two references to the same namespace symbol are equal"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-09 — Loading order (we exercise via straightforward sequence of
# forms inside a `do` so the REPL processes them in order).
G6_09 = SubjectCurriculum(grade=6, subject_id="G6-09",
    subject_title="Loading order", fable="tortoise-hare",
    examples=[
        _ex("(do (def step1 1) (def step2 (+ step1 1)) step2)", 2,
            "evaluating definitions in sequence to establish dependency order",
            "the value of the second variable after both definitions are loaded in order",
            goal="define step1 as 1, then define step2 as step1 plus 1, then return step2"),
        _ex("(let [a 1 b (+ a 1)] (+ a b))", 3,
            "establishing local bindings with dependent values",
            "the sum of two variables with the second depending on the first",
            goal="bind a to 1, bind b to a plus 1, then return the sum of a and b"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-10 — leiningen / deps.edn (project setup; we exercise via reading
# a small edn-shaped data structure that resembles a deps map).
G6_10 = SubjectCurriculum(grade=6, subject_id="G6-10",
    subject_title="Leiningen and deps.edn", fable="tortoise-hare",
    examples=[
        _ex("(:deps {:deps {:a 1 :b 2}})", {":a": 1, ":b": 2},
            "accessing a key from a nested map structure",
            "the value at the :deps key in a deps-style map",
            goal="extract the value at the :deps key from a nested map"),
        _ex("(get-in {:paths [\"src\"]} [:paths 0])", "src",
            "accessing a nested value in a map using a path vector",
            "the first element from a :paths vector in a deps-style map",
            goal="extract the first entry from the :paths vector in a deps-style map"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-11 — Classpath (we use a tiny path-string operation as the
# eval-shaped exercise).
G6_11 = SubjectCurriculum(grade=6, subject_id="G6-11",
    subject_title="Classpath", fable="tortoise-hare",
    examples=[
        _ex("(clojure.string/split \"src:test\" #\":\")", ["src", "test"],
            "splitting a string by a delimiter",
            "the vector of parts after splitting a colon-separated path string",
            goal="split a colon-separated classpath-like string into its individual entries"),
        _ex("(count [\"src\" \"test\" \"resources\"])", 3,
            "counting the number of elements in a vector",
            "the number of entries in a classpath-like vector",
            goal="count the number of entries in a vector of classpath directories"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-12 — Multiple files, one project (we exercise via a vector
# of namespace symbols).
G6_12 = SubjectCurriculum(grade=6, subject_id="G6-12",
    subject_title="Multiple files in one project", fable="tortoise-hare",
    examples=[
        _ex("(count ['race.tortoise 'race.hare 'race.shared])", 3,
            "counting the number of namespace symbols in a project",
            "the number of namespaces in a small project",
            goal="count the number of namespace symbols in a vector of three namespaces"),
        _ex("(map name ['race.tortoise 'race.hare])", ["race.tortoise", "race.hare"],
            "extracting string names from namespace symbols",
            "the vector of namespace names as strings",
            goal="extract the string form of each namespace symbol in a vector of two namespaces"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-13 — Aliasing conventions (we exercise via a tiny alias-style
# substitution that's purely lexical).
G6_13 = SubjectCurriculum(grade=6, subject_id="G6-13",
    subject_title="Aliasing conventions", fable="tortoise-hare",
    examples=[
        _ex("(let [s clojure.string/upper-case] (s \"hare\"))", "HARE",
            "aliasing a fully-qualified function and calling it through the alias",
            "the result of calling an aliased function",
            goal="bind the fully-qualified string uppercasing function to a local alias s and call it on hare"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-14 — Import for Java classes (basilisp targets Python; we use a
# universally-available form here: predicate on a class-y name).
G6_14 = SubjectCurriculum(grade=6, subject_id="G6-14",
    subject_title="Import for host classes", fable="tortoise-hare",
    examples=[
        _ex("(symbol? 'java.util.List)", True,
            "testing whether a value is a symbol",
            "whether a dotted Java class name is a symbol",
            goal="test whether a Java class name written as a quoted symbol is a symbol"),
        _ex("(name 'java.util.Map)", "java.util.Map",
            "extracting the string form of a class symbol",
            "the string form of a Java class symbol",
            goal="extract the string form of a Java class symbol"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-15 — Namespace meta (we exercise the metadata mechanism on a
# symbol via `^{:doc ...}`).
G6_15 = SubjectCurriculum(grade=6, subject_id="G6-15",
    subject_title="Namespace meta", fable="tortoise-hare",
    examples=[
        _ex("(:doc (meta '^{:doc \"steady wins\"} race))", "steady wins",
            "accessing the :doc metadata from a symbol",
            "the docstring value from a symbol's metadata",
            goal="extract the :doc metadata value from a symbol with a docstring"),
        _ex("(:author (meta '^{:author \"Aesop\"} race))", "Aesop",
            "accessing the :author metadata from a symbol",
            "the author value from a symbol's metadata",
            goal="extract the :author metadata value from a symbol with an author tag"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-16 — Cleaning up requires (we exercise via a simple "is this name
# in a vector" check, the analogue of "is this require still used").
G6_16 = SubjectCurriculum(grade=6, subject_id="G6-16",
    subject_title="Cleaning up requires", fable="tortoise-hare",
    examples=[
        _ex("(contains? #{'clojure.string} 'clojure.string)", True,
            "testing membership in a set of namespaces",
            "whether a namespace is in the set of required namespaces",
            goal="test whether the clojure.string namespace is in the set of required namespaces"),
        _ex("(contains? #{'clojure.string} 'clojure.set)", False,
            "testing membership in a set of namespaces",
            "whether a different namespace is in the set of required namespaces",
            goal="test whether the clojure.set namespace is in the set of required namespaces"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# ─────────────────────── registry ───────────────────────


SUBJECTS: dict[str, SubjectCurriculum] = {s.subject_id: s for s in (
    G6_01, G6_02, G6_03, G6_04, G6_05, G6_06, G6_07, G6_08,
    G6_09, G6_10, G6_11, G6_12, G6_13, G6_14, G6_15, G6_16,
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
    print(f"grade-6 tortoise-hare smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
