"""Grade 6 — namespaces and modular code. Through boy-who-cried-wolf.

Subplot lens: trust-as-namespace. False alarms cross village boundaries
the way symbols cross namespace boundaries. Two cottages on opposite
sides of the village; each shepherd keeps their own copybook of forms.
The reeve / elder enforces what's exported between village namespaces —
only forms actually submitted to the REPL count as trustworthy across
the boundary.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.boy_wolf.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)


# ─────────────────────── grade-6 subplot extensions ───────────────────────
#
# Namespaces map naturally onto "trust boundaries" in the boy-wolf moral
# lens. A claim shouted from one side of the village (one namespace) only
# carries to the other side if it's been honestly submitted to the REPL —
# the elder enforces what gets exported.

_NS_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    # Two cottages on opposite sides of the village — each shepherd keeps
    # a separate copybook of forms. The named shepherd's claim doesn't
    # cross to the elder's side without honest evaluation.
    SubplotTemplate("""\
The two cottages stood on opposite sides of the village {place}, and
each kept its own copybook of forms. {shepherd_phrase} scribbled into
one book; {elder_phrase} kept the other. To settle a question that
morning, {elder} pointed to {concept_phrase} and asked
{shepherd_him_her} to write the form {form_display} into the REPL so
the answer would carry honestly across both copybooks."""),

    # The reeve as namespace gatekeeper — decides which forms get
    # exported between the village namespaces.
    SubplotTemplate("""\
The reeve of the village kept a small list {place} of which forms had
been honestly evaluated and could therefore be trusted across cottage
boundaries. The next entry concerned {concept_phrase}. {elder_phrase},
{emo_patient}, asked {shepherd_phrase} to submit the form
{form_display} so the runtime's answer could be carried, on the reeve's
authority, to the other side of the village."""),

    # Cross-namespace fully-qualified beat — when the shepherd's
    # claim from one cottage has to be referred to from the other.
    #
    # NOTE (boy-wolf polish, hand-audit pass): the closing "X was,
    # after all, the line in question" had a singular verb that
    # broke when {concept_phrase} was a plural NP (e.g., "two
    # identical namespace symbols"). Rewritten with a number-agnostic
    # frame: "the question on that line came down to {concept_phrase}".
    SubplotTemplate("""\
{shepherd_phrase} had shouted a claim from one side of the village
{place}. {elder_phrase} insisted that, before the answer could be
relied on by anyone in the other cottage, the form {form_display} would
need to be evaluated under its proper name. {shepherd}, {emo_tired},
agreed; the question on that line came down to {concept_phrase}."""),
]


def _ex(form, expected, concept, what):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what)


_PLAN_G6 = _PLAN_POOL + (
    "I require the namespace and call the function.",
    "I use the fully-qualified name to reach the var.",
    "I keep the namespaces straight and let the REPL resolve the name.",
)


# ─────────────────────── 16 grade-6 subjects ───────────────────────


# G6-01 — Namespace as file
# A namespace's name is itself a symbol; we use `(name 'foo.bar)` to
# show the path-like string the namespace corresponds to.
G6_01 = SubjectCurriculum(grade=6, subject_id="G6-01",
    subject_title="Namespace as file", fable="boy-wolf",
    examples=[
        _ex("(name 'foo.bar)", "foo.bar",
            "the symbol foo.bar standing in for a namespace name",
            "the string form of the namespace symbol foo.bar"),
        _ex("(name 'clojure.string)", "clojure.string",
            "the namespace symbol clojure.string",
            "the string \"clojure.string\""),
        _ex("(symbol? 'village.flock)", True,
            "whether village.flock is a symbol",
            "the value of (symbol? 'village.flock)"),
    ], subplots=_NS_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-02 — ns form (we exercise via `name` style introspection)
G6_02 = SubjectCurriculum(grade=6, subject_id="G6-02",
    subject_title="ns form", fable="boy-wolf",
    examples=[
        _ex("(name 'village.shepherd)", "village.shepherd",
            "the namespace name 'village.shepherd as a string",
            "the string \"village.shepherd\""),
        _ex("(= 'village.shepherd 'village.shepherd)", True,
            "two identical namespace symbols",
            "whether the two namespace symbols are equal"),
    ], subplots=_NS_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-03 — require — fully qualified usage (require already loaded
# clojure.string in basilisp/clojure runtime; the form below works in
# both).
G6_03 = SubjectCurriculum(grade=6, subject_id="G6-03",
    subject_title="require", fable="boy-wolf",
    examples=[
        _ex("(clojure.string/upper-case \"wolf\")", "WOLF",
            "the form using clojure.string/upper-case on \"wolf\"",
            "the upper-cased string \"WOLF\""),
        _ex("(clojure.string/lower-case \"WOLF\")", "wolf",
            "the form using clojure.string/lower-case",
            "the lower-cased string \"wolf\""),
    ], subplots=_NS_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-04 — refer-and-use (we exercise the effect: a referred name
# resolves the same as the qualified name; via `=` we compare two
# applications).
G6_04 = SubjectCurriculum(grade=6, subject_id="G6-04",
    subject_title="refer and use", fable="boy-wolf",
    examples=[
        _ex("(= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))",
            True,
            "whether two calls to the same fully-qualified function agree",
            "the value of (= (clojure.string/upper-case \"x\") (clojure.string/upper-case \"x\"))"),
    ], subplots=_NS_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-05 — Fully qualified names
G6_05 = SubjectCurriculum(grade=6, subject_id="G6-05",
    subject_title="Fully qualified names", fable="boy-wolf",
    examples=[
        _ex("(clojure.string/upper-case \"shepherd\")", "SHEPHERD",
            "clojure.string/upper-case applied to \"shepherd\"",
            "the upper-cased string \"SHEPHERD\""),
        _ex("(clojure.string/reverse \"flock\")", "kcolf",
            "clojure.string/reverse applied to \"flock\"",
            "the reversed string \"kcolf\""),
        _ex("(namespace :village/shepherd)", "village",
            "the namespace portion of the keyword :village/shepherd",
            "the string \"village\""),
        _ex("(name :village/shepherd)", "shepherd",
            "the name portion of the keyword :village/shepherd",
            "the string \"shepherd\""),
    ], subplots=_NS_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-06 — Private defs (we can't test ^:private effect with eval, but
# we can confirm related metadata predicates).
G6_06 = SubjectCurriculum(grade=6, subject_id="G6-06",
    subject_title="Private defs", fable="boy-wolf",
    examples=[
        # The :private flag is queryable as metadata on the symbol.
        _ex("(:private (meta '^:private x))", True,
            "the :private flag on metadata of '^:private x",
            "whether the :private metadata is true"),
        _ex("(:private (meta 'x))", None,
            "the :private flag on plain metadata of 'x",
            "the value of (:private (meta 'x))"),
    ], subplots=_NS_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-07 — Public vs private API (design decision; we exercise via
# the predicate `:private` on metadata).
G6_07 = SubjectCurriculum(grade=6, subject_id="G6-07",
    subject_title="Public vs private API", fable="boy-wolf",
    examples=[
        _ex("(boolean (:private (meta '^:private hidden)))", True,
            "whether the symbol 'hidden carries the :private flag",
            "the boolean of (:private (meta '^:private hidden))"),
        _ex("(boolean (:private (meta 'public)))", False,
            "whether 'public carries the :private flag",
            "the boolean of (:private (meta 'public))"),
    ], subplots=_NS_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-08 — Circular dependencies (we exercise via a plain form that
# would resolve correctly when the dependency graph is sound; the
# narrative carries the lesson).
G6_08 = SubjectCurriculum(grade=6, subject_id="G6-08",
    subject_title="Circular dependencies", fable="boy-wolf",
    examples=[
        _ex("(clojure.string/upper-case \"a\")", "A",
            "a single-direction call from one namespace to clojure.string",
            "the upper-cased string \"A\""),
        _ex("(= 'a.b 'a.b)", True,
            "whether two references to the same namespace symbol agree",
            "the value of (= 'a.b 'a.b)"),
    ], subplots=_NS_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-09 — Loading order (we exercise via straightforward sequence of
# forms inside a `do` so the REPL processes them in order).
G6_09 = SubjectCurriculum(grade=6, subject_id="G6-09",
    subject_title="Loading order", fable="boy-wolf",
    examples=[
        _ex("(do (def step1 1) (def step2 (+ step1 1)) step2)", 2,
            "two defs evaluated in order, the second using the first",
            "the final value step2 after sequential loading"),
        _ex("(let [a 1 b (+ a 1)] (+ a b))", 3,
            "an in-expression analogue of file-loading order via let",
            "the value of (+ a b) given a=1 b=(+ a 1)"),
    ], subplots=_NS_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-10 — leiningen / deps.edn (project setup; we exercise via reading
# a small edn-shaped data structure that resembles a deps map).
G6_10 = SubjectCurriculum(grade=6, subject_id="G6-10",
    subject_title="Leiningen and deps.edn", fable="boy-wolf",
    examples=[
        _ex("(:deps {:deps {:a 1 :b 2}})", {":a": 1, ":b": 2},
            "the :deps key from a small deps-map literal",
            "the value at :deps in {:deps {:a 1 :b 2}}"),
        _ex("(get-in {:paths [\"src\"]} [:paths 0])", "src",
            "the first :paths entry from a tiny deps-style map",
            "the string \"src\" at [:paths 0]"),
    ], subplots=_NS_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-11 — Classpath (we use a tiny path-string operation as the
# eval-shaped exercise).
G6_11 = SubjectCurriculum(grade=6, subject_id="G6-11",
    subject_title="Classpath", fable="boy-wolf",
    examples=[
        _ex("(clojure.string/split \"src:test\" #\":\")", ["src", "test"],
            "splitting a colon-separated classpath-like string",
            "the vector [\"src\" \"test\"]"),
        _ex("(count [\"src\" \"test\" \"resources\"])", 3,
            "the number of entries in a classpath-like vector",
            "the count of three classpath entries"),
    ], subplots=_NS_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-12 — Multiple files, one project (we exercise via a vector
# of namespace symbols).
G6_12 = SubjectCurriculum(grade=6, subject_id="G6-12",
    subject_title="Multiple files in one project", fable="boy-wolf",
    examples=[
        _ex("(count ['village.shepherd 'village.elder 'village.shared])", 3,
            "the number of namespaces in a small project",
            "the count of namespace symbols in the vector"),
        _ex("(map name ['village.shepherd 'village.elder])",
            ["village.shepherd", "village.elder"],
            "the names of two namespaces as strings",
            "the vector of namespace name strings"),
    ], subplots=_NS_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-13 — Aliasing conventions (we exercise via a tiny alias-style
# substitution that's purely lexical).
G6_13 = SubjectCurriculum(grade=6, subject_id="G6-13",
    subject_title="Aliasing conventions", fable="boy-wolf",
    examples=[
        _ex("(let [s clojure.string/upper-case] (s \"wolf\"))", "WOLF",
            "binding the function clojure.string/upper-case to a local s",
            "the value (s \"wolf\") where s is upper-case"),
    ], subplots=_NS_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-14 — Import for Java classes (basilisp targets Python; we use a
# universally-available form here: predicate on a class-y name).
G6_14 = SubjectCurriculum(grade=6, subject_id="G6-14",
    subject_title="Import for host classes", fable="boy-wolf",
    examples=[
        _ex("(symbol? 'java.util.Date)", True,
            "whether 'java.util.Date is a symbol",
            "the value of (symbol? 'java.util.Date)"),
        _ex("(name 'java.util.Date)", "java.util.Date",
            "the dotted-class symbol's name",
            "the string \"java.util.Date\""),
    ], subplots=_NS_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-15 — Namespace meta (we exercise the metadata mechanism on a
# symbol via `^{:doc ...}`).
G6_15 = SubjectCurriculum(grade=6, subject_id="G6-15",
    subject_title="Namespace meta", fable="boy-wolf",
    examples=[
        _ex("(:doc (meta '^{:doc \"trust the runtime\"} village))",
            "trust the runtime",
            "the :doc metadata attached to the symbol 'village",
            "the docstring \"trust the runtime\" from the metadata"),
        _ex("(:author (meta '^{:author \"Aesop\"} village))", "Aesop",
            "the :author metadata on 'village",
            "the string \"Aesop\""),
    ], subplots=_NS_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-16 — Cleaning up requires (we exercise via a simple "is this name
# in a vector" check, the analogue of "is this require still used").
G6_16 = SubjectCurriculum(grade=6, subject_id="G6-16",
    subject_title="Cleaning up requires", fable="boy-wolf",
    examples=[
        _ex("(contains? #{'clojure.string} 'clojure.string)", True,
            "whether the require list still contains 'clojure.string",
            "the value of (contains? #{'clojure.string} 'clojure.string)"),
        _ex("(contains? #{'clojure.string} 'clojure.set)", False,
            "whether the require list contains an unused 'clojure.set",
            "the value of (contains? #{'clojure.string} 'clojure.set)"),
    ], subplots=_NS_SUBPLOTS, plan_pool=_PLAN_G6)


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
    print(f"grade-6 boy-wolf smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
