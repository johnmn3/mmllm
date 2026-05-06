"""Grade 6 — namespaces and modular code. through the milkmaid fable.

Subplot lens: two characters working at separate workbenches /
copybooks / cottages, then later sharing what they've labeled. The
fable's vanity-vs-steadiness pulls in: Milkmaid wants to scribble
everything in one place, Farmer insists on naming the file the
form lives in and requiring it cleanly.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.milkmaid.grade_1 import (
    _GOAL_SUBPLOTS, _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL
)
from mmllm.aesop.curriculum.milkmaid._metaphor_pools import (
    _ROADSIGN_SUBPLOTS, _SCROLL_SUBPLOTS, _TOOLSHED_SUBPLOTS,
)


_NS_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    # Two characters at separate workbenches, exchanging a labeled form.
    SubplotTemplate("""\
{farmer_phrase} kept a small workbench {place}, where every form had
its own labeled drawer. {milkmaid_phrase} preferred to scribble each
expression in a single notebook. To settle a question that morning,
{farmer} pointed to {concept_phrase} and asked {milkmaid} to evaluate the
form {form_display} so they could see what name belonged with what
value."""),

    # The "two cottages" / cross-namespace beat.
    SubplotTemplate("""\
The two of them lived in cottages on opposite sides {place} —
{farmer_phrase} on one side, {milkmaid_phrase} on the other. Each kept
their own copybook of forms. When the time came to compare notes,
{farmer} read aloud {concept_phrase} and asked, {emo_patient}, what
the form {form_display} would return when the REPL reached across the
shared path."""),
]


def _ex(form, expected, concept, what, goal=""):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal)


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
    subject_title="Namespace as file", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(name 'foo.bar)",
            expected="foo.bar",
            concept_phrase="extracting the string form of a namespace symbol",
            question_what="the string form of a quoted namespace symbol",
            goal_text="extract the string form of a quoted namespace symbol",
            scenario=(
                "The milkmaid arrived at the market-board in the village square — a "
                "board nailed with names and namespaces of all the registered vendors. "
                "She wanted to read the string name from one of the posted symbols."
            ),
            need=(
                "She needed to extract the board-entry as a readable string — not a "
                "symbol, but the text the symbol stands for, as it would appear "
                "written on the market-board."
            ),
            mapping=(
                "`name` is the market-board reader: it takes a quoted namespace symbol "
                "and returns the string the board has posted — the human-readable "
                "market address, not the runtime name-object."
            ),
            resolution=(
                "the REPL returned the string the market-board carried — the dotted "
                "vendor address, readable and ready to hand to a buyer."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(name 'clojure.string)",
            expected="clojure.string",
            concept_phrase="extracting the string form of a namespace symbol",
            question_what="the string form of a quoted namespace symbol",
            goal_text="extract the string form of a quoted namespace symbol",
        ),
        SubjectExample(
            form="(symbol? 'tortoise.race)",
            expected=True,
            concept_phrase="checking whether a value is a symbol",
            question_what="whether a value is a symbol",
            goal_text="test whether a quoted namespace-like value is a symbol",
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-02 — ns form (we exercise via `name *ns*` style introspection)
G6_02 = SubjectCurriculum(grade=6, subject_id="G6-02",
    subject_title="ns form", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(name 'race.tortoise)",
            expected="race.tortoise",
            concept_phrase="extracting the string form of a namespace symbol",
            question_what="the string form of a quoted namespace symbol",
            goal_text="extract the string form of a quoted namespace symbol",
        ),
        SubjectExample(
            form="(= 'race.tortoise 'race.tortoise)",
            expected=True,
            concept_phrase="checking equality of two namespace symbols",
            question_what="whether two identical namespace symbols are equal",
            goal_text="test whether two identical namespace symbols are equal",
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-03 — require — fully qualified usage (require already loaded
# clojure.string in basilisp/clojure runtime; the form below works in
# both).
G6_03 = SubjectCurriculum(grade=6, subject_id="G6-03",
    subject_title="require", fable="milkmaid",
    examples=[
        SubjectExample(
            form='(clojure.string/upper-case "hare")',
            expected="HARE",
            concept_phrase="calling a fully-qualified string function",
            question_what="the capitalized form returned by the upper-case routine on the scroll",
            goal_text="call the upper-case routine on the clojure.string scroll, applied to the four-letter string hare",
        ),
        SubjectExample(
            form='(clojure.string/lower-case "ZEBRA")',
            expected="zebra",
            concept_phrase="calling a fully-qualified string function",
            question_what="the lowercase form of the string ZEBRA produced by clojure.string/lower-case",
            goal_text="call the lowercasing function from clojure.string on a test string",
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-04 — refer-and-use (we exercise the effect: a referred name
# resolves the same as the qualified name; via `=` we compare two
# applications).
G6_04 = SubjectCurriculum(grade=6, subject_id="G6-04",
    subject_title="refer and use", fable="milkmaid",
    examples=[
        SubjectExample(
            form='(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))',
            expected=True,
            concept_phrase="testing equality of two identical function calls",
            question_what="whether two calls to the same function with the same argument produce the same result",
            goal_text="test whether two calls to the fully-qualified string uppercasing function with the same argument are equal",
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-05 — Fully qualified names
G6_05 = SubjectCurriculum(grade=6, subject_id="G6-05",
    subject_title="Fully qualified names", fable="milkmaid",
    examples=[
        SubjectExample(
            form='(clojure.string/upper-case "hello")',
            expected="HELLO",
            concept_phrase="calling a fully-qualified string function",
            question_what="the uppercase form of the string hello produced by clojure.string/upper-case",
            goal_text="call the uppercasing function from clojure.string on a test string",
        ),
        SubjectExample(
            form='(clojure.string/reverse "abc")',
            expected="cba",
            concept_phrase="calling a fully-qualified string function",
            question_what="the reversed form of the string abc produced by clojure.string/reverse",
            goal_text="call the reversing function from clojure.string on a test string",
        ),
        SubjectExample(
            form="(namespace :owner/item)",
            expected="owner",
            concept_phrase="extracting the namespace portion of a keyword",
            question_what="the namespace part of a qualified keyword",
            goal_text="extract the namespace portion of a qualified keyword",
        ),
        SubjectExample(
            form="(name :owner/item)",
            expected="item",
            concept_phrase="extracting the name portion of a keyword",
            question_what="the name part of a qualified keyword",
            goal_text="extract the name local portion of a qualified keyword",
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-06 — Private defs (we can't test ^:private effect with eval, but
# we can confirm related metadata predicates).
G6_06 = SubjectCurriculum(grade=6, subject_id="G6-06",
    subject_title="Private defs", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(:private (meta '^:private x))",
            expected=True,
            concept_phrase="accessing the :private flag from metadata",
            question_what="whether the :private metadata is set on a symbol",
            goal_text="check whether the :private flag is present in the metadata of a symbol with :private marker",
        ),
        SubjectExample(
            form="(:private (meta 'x))",
            expected=None,
            concept_phrase="accessing the :private flag from metadata",
            question_what="whether the :private metadata is set on a plain symbol",
            goal_text="check whether the :private flag is present in the metadata of a plain symbol without markers",
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-07 — Public vs private API (design decision; we exercise via
# the predicate `:private` on metadata).
G6_07 = SubjectCurriculum(grade=6, subject_id="G6-07",
    subject_title="Public vs private API", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(boolean (:private (meta '^:private hidden)))",
            expected=True,
            concept_phrase="converting the :private metadata to a boolean",
            question_what="whether a symbol with :private marker evaluates to true when converted to boolean",
            goal_text="convert the :private metadata flag of a symbol marked with :private to a boolean",
        ),
        SubjectExample(
            form="(boolean (:private (meta 'public)))",
            expected=False,
            concept_phrase="converting the :private metadata to a boolean",
            question_what="whether a symbol without :private marker evaluates to false when converted to boolean",
            goal_text="convert the :private metadata flag of a plain symbol to a boolean",
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-08 — Circular dependencies (we exercise via a plain form that
# would resolve correctly when the dependency graph is sound; the
# narrative carries the lesson).
G6_08 = SubjectCurriculum(grade=6, subject_id="G6-08",
    subject_title="Circular dependencies", fable="milkmaid",
    examples=[
        SubjectExample(
            form='(clojure.string/upper-case "a")',
            expected="A",
            concept_phrase="calling a function from a required namespace",
            question_what="the uppercase form of the character a produced by clojure.string/upper-case",
            goal_text="call the string uppercasing function from clojure.string on the character a",
        ),
        SubjectExample(
            form="(= 'a.b 'a.b)",
            expected=True,
            concept_phrase="testing equality of two namespace symbols",
            question_what="whether two identical namespace symbols are equal",
            goal_text="test whether two references to the same namespace symbol are equal",
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-09 — Loading order (we exercise via straightforward sequence of
# forms inside a `do` so the REPL processes them in order).
G6_09 = SubjectCurriculum(grade=6, subject_id="G6-09",
    subject_title="Loading order", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(do (def step1 1) (def step2 (+ step1 1)) step2)",
            expected=2,
            concept_phrase="evaluating definitions in sequence to establish dependency order",
            question_what="the value of the second variable after both definitions are loaded in order",
            goal_text="define step1 as 1, then define step2 as step1 plus 1, then return step2",
        ),
        SubjectExample(
            form="(let [a 1 b (+ a 1)] (+ a b))",
            expected=3,
            concept_phrase="establishing local bindings with dependent values",
            question_what="the sum of two variables with the second depending on the first",
            goal_text="bind a to 1, bind b to a plus 1, then return the sum of a and b",
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-10 — leiningen / deps.edn (project setup; we exercise via reading
# a small edn-shaped data structure that resembles a deps map).
G6_10 = SubjectCurriculum(grade=6, subject_id="G6-10",
    subject_title="Leiningen and deps.edn", fable="milkmaid",
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
    subject_title="Classpath", fable="milkmaid",
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
    subject_title="Multiple files in one project", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(count ['race.tortoise 'race.hare 'race.shared])",
            expected=3,
            concept_phrase="counting the number of namespace symbols in a project",
            question_what="the number of namespaces in a small project",
            goal_text="count the number of namespace symbols in a vector of three namespaces",
        ),
        SubjectExample(
            form="(map name ['race.tortoise 'race.hare])",
            expected=["race.tortoise", "race.hare"],
            concept_phrase="extracting string names from namespace symbols",
            question_what="the vector of namespace names as strings",
            goal_text="extract the string form of each namespace symbol in a vector of two namespaces",
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-13 — Aliasing conventions (we exercise via a tiny alias-style
# substitution that's purely lexical).
G6_13 = SubjectCurriculum(grade=6, subject_id="G6-13",
    subject_title="Aliasing conventions", fable="milkmaid",
    examples=[
        SubjectExample(
            form='(let [s clojure.string/upper-case] (s "hare"))',
            expected="HARE",
            concept_phrase="aliasing a fully-qualified function and calling it through the alias",
            question_what="the uppercase form of the string hare when clojure.string/upper-case is called through a local alias",
            goal_text="bind the fully-qualified string uppercasing function to a local alias s and call it on hare",
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-14 — Import for Java classes (basilisp targets Python; we use a
# universally-available form here: predicate on a class-y name).
G6_14 = SubjectCurriculum(grade=6, subject_id="G6-14",
    subject_title="Import for host classes", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(symbol? 'java.util.List)",
            expected=True,
            concept_phrase="testing whether a value is a symbol",
            question_what="whether a dotted Java class name is a symbol",
            goal_text="test whether a Java class name written as a quoted symbol is a symbol",
        ),
        SubjectExample(
            form="(name 'java.util.Map)",
            expected="java.util.Map",
            concept_phrase="extracting the string form of a class symbol",
            question_what="the string form of a Java class symbol",
            goal_text="extract the string form of a Java class symbol",
        ),
    ], subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-15 — Namespace meta (we exercise the metadata mechanism on a
# symbol via `^{:doc ...}`).
G6_15 = SubjectCurriculum(grade=6, subject_id="G6-15",
    subject_title="Namespace meta", fable="milkmaid",
    examples=[
        SubjectExample(
            form='(:doc (meta \'\\{:doc "steady wins"\\} race))',
            expected="steady wins",
            concept_phrase="accessing the :doc metadata from a symbol",
            question_what="the docstring value from a symbol's metadata",
            goal_text="extract the :doc metadata value from a symbol with a docstring",
            scenario=(
                "The farmer had annotated a symbol called `race` with a slip of paper "
                "tucked into its metadata: a docstring recording the dairy's guiding "
                "principle. She needed to read that annotation back from the slip."
            ),
            need=(
                "She needed to unwrap the market order — reach into the symbol's "
                "metadata, find the `:doc` key, and return the value written on "
                "the slip."
            ),
            mapping=(
                "`meta` opens the order-slip envelope tied to the symbol; the `:doc` "
                "keyword reads the line on the slip labeled doc. The form retrieves "
                "the annotation, not the symbol itself."
            ),
            resolution=(
                "the REPL returned the docstring the farmer had tucked into the slip "
                "— the principle she had recorded for the day's dairy run."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(:author (meta \'\\{:author "Aesop"\\} race))',
            expected="Aesop",
            concept_phrase="accessing the :author metadata from a symbol",
            question_what="the author value from a symbol's metadata",
            goal_text="extract the :author metadata value from a symbol with an author tag",
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-16 — Cleaning up requires (we exercise via a simple "is this name
# in a vector" check, the analogue of "is this require still used").
G6_16 = SubjectCurriculum(grade=6, subject_id="G6-16",
    subject_title="Cleaning up requires", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(contains? #{'clojure.string} 'clojure.string)",
            expected=True,
            concept_phrase="testing membership in a set of namespaces",
            question_what="whether a namespace is in the set of required namespaces",
            goal_text="test whether the clojure.string namespace is in the set of required namespaces",
        ),
        SubjectExample(
            form="(contains? #{'clojure.string} 'clojure.set)",
            expected=False,
            concept_phrase="testing membership in a set of namespaces",
            question_what="whether a different namespace is in the set of required namespaces",
            goal_text="test whether the clojure.set namespace is in the set of required namespaces",
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


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
