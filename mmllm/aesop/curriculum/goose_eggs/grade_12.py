"""Grade 12 — real-world Clojure. Through goose-eggs.

Subplot lens: the long season of patient yields ends, and the owner
takes stock of the ledgers, the routines, the techniques learned —
transducers for the long pipelines of the harvest, core.async for the
hands working the kitchen and the barn at the same time, spec for
declaring what counts as a good egg, clojure.test for retracing the
day's work, and the libraries every Clojure traveler will eventually
meet at the market.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.goose_eggs.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)


# ─────────────────────── grade-12 subplot extensions ───────────────────────
#
# The season of patient morning-yields is over. {owner} sits with the
# ledgers and tools that made the year of eggs work. {visitor}, who once
# guessed at every total, now leans in to read the entries as
# {goose} settles for the evening. Each subplot frames the subject as
# a tool re-examined at the end of a long, patient season.

_REAL_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    SubplotTemplate("""\
The season of morning-eggs had ended {place}, and {owner_phrase} sat
with {visitor_phrase} comparing the year's ledgers. {owner} drew
{concept_phrase} into the dust beside the basket. "We've come a long
way," {owner_he_she} said, {emo_patient}. "The form {form_display} is
the kind of thing we'd reach for now." {visitor} nodded — for once
{emo_content} enough to listen, with {goose_phrase} settled quietly
nearby."""),

    SubplotTemplate("""\
{owner_phrase} had filled an entire leather ledger over the long
season with tools and patterns — transducers for the egg-counts,
channels between barn and kitchen, specs for what counted as a good
egg, tests for the routines — and {place} the next entry was
{concept_phrase}, with the form written as {form_display}.
{visitor_phrase}, {emo_proud} but more reflective than usual, agreed
to write the form into the REPL while {goose_phrase} watched."""),

    SubplotTemplate("""\
"This isn't a market trick to fool the buyers," {owner} said {place},
{emo_patient}. "It's a tool for the whole farmhouse." {visitor_phrase}
looked at {concept_phrase} and admitted {visitor_he_she} would not
have known what to write — the old greed for quick answers had
nothing to offer here. {owner} sketched {form_display} on a slate so
the runtime could speak for itself, the way {goose_phrase} let each
egg speak for the morning."""),

    SubplotTemplate("""\
At a long wooden table {place}, a row of small carved tokens
commemorated the libraries the farm had learned along the season.
The newest one honoured {concept_phrase}. {owner_phrase} touched it
with a careful finger and said the form to remember was {form_display};
{visitor_phrase} agreed to submit it, {emo_content} that the basket
of eggs from {goose_phrase} no longer needed defending against
guesswork."""),

    SubplotTemplate("""\
{visitor_phrase}, {emo_regretful} after a season of trying to
shortcut every egg-count, was finally willing to study patterns.
{owner_phrase} pointed {place} at {concept_phrase}. The form
{form_display} was the canonical example; the REPL would confirm what
it produced, the way {goose_phrase} would yield the next morning's
egg in its own time."""),

    SubplotTemplate("""\
A small banquet at the close of the season {place} brought together
every neighbour who'd traded with the farm. The day's discussion was
{concept_phrase}. {owner} wrote the form {form_display} on a square
of parchment and passed it across the table; {visitor}, {emo_content}
and reflective, agreed to read it into the REPL — {goose_phrase}
watched from the corner, untroubled by the long talk."""),
]


def _ex(form, expected, concept, what):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what)


_PLAN_G12 = _PLAN_POOL + (
    "I write the form using the appropriate library or tool.",
    "I express the pipeline / spec / test as a Clojure form.",
    "I let the REPL exercise the library form, the way the goose yields one egg.",
)


# ─────────────────────── 18 grade-12 subjects ───────────────────────


# G12-01 — Transducers introduction
G12_01 = SubjectCurriculum(
    grade=12, subject_id="G12-01",
    subject_title="Transducers introduction",
    fable="goose-eggs",
    examples=[
        # Use the transducer-arity functions through `into` / `transduce`.
        _ex("(into [] (map inc) [1 2 3])", [2, 3, 4],
            "the transducer (map inc) used via into",
            "[1 2 3] each incremented through a transducer"),
        _ex("(into [] (filter even?) [1 2 3 4 5])", [2, 4],
            "the transducer (filter even?) used via into",
            "the even elements via a filter transducer"),
    ],
    subplots=_REAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-02 — Transducer composition
G12_02 = SubjectCurriculum(
    grade=12, subject_id="G12-02",
    subject_title="Transducer composition",
    fable="goose-eggs",
    examples=[
        _ex("(into [] (comp (map inc) (filter even?)) [1 2 3 4])", [2, 4],
            "the composed transducer (comp (map inc) (filter even?))",
            "the result of inc-then-keep-evens via a composed transducer"),
        _ex("(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])",
            12,
            "transduce with a composed transducer summing the kept items",
            "the sum after inc-then-keep-evens via transduce"),
    ],
    subplots=_REAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-03 — into with a transducer
G12_03 = SubjectCurriculum(
    grade=12, subject_id="G12-03",
    subject_title="into with a transducer (xform)",
    fable="goose-eggs",
    examples=[
        _ex("(into #{} (map inc) [1 2 3])", {2, 3, 4},
            "into a set with the (map inc) transducer",
            "the set produced by mapping inc into an empty set"),
        _ex("(into [] (take 3) (range 100))", [0, 1, 2],
            "into [] with the (take 3) transducer over (range 100)",
            "the first three items collected through a transducer"),
    ],
    subplots=_REAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-04 — core.async introduction
G12_04 = SubjectCurriculum(
    grade=12, subject_id="G12-04",
    subject_title="core.async introduction",
    fable="goose-eggs",
    examples=[
        # core.async pulls in heavy machinery; describe the topic via marker.
        _ex('(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)',
            ":studied",
            "the core.async primitives chan/go/<!/>!",
            "the marker for the core.async lesson"),
        _ex('(do "go-blocks let you write async code as if it were synchronous" :async)',
            ":async",
            "what go blocks give you",
            "the marker keyword for go-blocks"),
    ],
    subplots=_REAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-05 — Channels and pipelines
G12_05 = SubjectCurriculum(
    grade=12, subject_id="G12-05",
    subject_title="Channels and pipelines",
    fable="goose-eggs",
    examples=[
        _ex('(do "pipe, mult, mix, pipeline-async route values across channels" :studied)',
            ":studied",
            "the pipeline operators in core.async",
            "the marker for the channel-pipeline lesson"),
        _ex('(do "pipelines transform streams of values channel-to-channel" :pipelines)',
            ":pipelines",
            "the role of pipelines in async code",
            "the marker keyword for pipelines"),
    ],
    subplots=_REAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-06 — clojure.spec
G12_06 = SubjectCurriculum(
    grade=12, subject_id="G12-06",
    subject_title="clojure.spec",
    fable="goose-eggs",
    examples=[
        # We can run small spec predicates portably.
        _ex("(do (require '[clojure.spec.alpha :as s]) "
            "(s/valid? int? 42))", True,
            "(s/valid? int? 42)",
            "whether 42 conforms to the int? spec"),
        _ex("(do (require '[clojure.spec.alpha :as s]) "
            "(s/valid? string? 42))", False,
            "(s/valid? string? 42)",
            "whether 42 conforms to the string? spec"),
    ],
    subplots=_REAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-07 — Spec generators
G12_07 = SubjectCurriculum(
    grade=12, subject_id="G12-07",
    subject_title="Spec generators",
    fable="goose-eggs",
    examples=[
        _ex('(do "s/exercise produces sample inputs for a spec" :studied)',
            ":studied",
            "what s/exercise does",
            "the marker for the spec-generators lesson"),
        _ex('(do "spec generators turn specs into property-based test inputs" :gens)',
            ":gens",
            "the role of spec generators",
            "the marker keyword for spec generators"),
    ],
    subplots=_REAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-08 — clojure.test
G12_08 = SubjectCurriculum(
    grade=12, subject_id="G12-08",
    subject_title="clojure.test",
    fable="goose-eggs",
    examples=[
        # We can demonstrate the boolean essence of an assertion via =.
        _ex("(= (+ 1 2) 3)", True,
            "(= (+ 1 2) 3) — what an `is` would test",
            "the truth value an `is` assertion would record"),
        _ex('(do "(deftest …), (is …), (testing …) are the core test forms" :studied)',
            ":studied",
            "the clojure.test core forms",
            "the marker for the clojure.test lesson"),
    ],
    subplots=_REAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-09 — Test fixtures
G12_09 = SubjectCurriculum(
    grade=12, subject_id="G12-09",
    subject_title="Test fixtures",
    fable="goose-eggs",
    examples=[
        _ex('(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)',
            ":studied",
            "use-fixtures and the fixture pattern",
            "the marker for the fixtures lesson"),
        _ex('(do "fixtures provide setup/teardown around deftests" :fixtures)',
            ":fixtures",
            "the purpose of fixtures",
            "the marker keyword for the fixture lesson"),
    ],
    subplots=_REAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-10 — Property-based testing
G12_10 = SubjectCurriculum(
    grade=12, subject_id="G12-10",
    subject_title="Property-based testing",
    fable="goose-eggs",
    examples=[
        # A property: reverse of reverse equals identity. We check it once
        # to model what a property test would do generically.
        _ex("(= (reverse (reverse [1 2 3])) [1 2 3])", True,
            "the property that double-reverse is identity",
            "the truth value of the double-reverse property on [1 2 3]"),
        _ex('(do "test.check generates inputs and checks properties hold" :studied)',
            ":studied",
            "what test.check does",
            "the marker for property-based testing"),
    ],
    subplots=_REAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-11 — Leiningen project.clj
G12_11 = SubjectCurriculum(
    grade=12, subject_id="G12-11",
    subject_title="Leiningen project.clj",
    fable="goose-eggs",
    examples=[
        _ex('(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)',
            ":studied",
            "the project.clj manifest for Leiningen",
            "the marker for the project.clj lesson"),
        _ex('(do "Leiningen reads project.clj at the project root" :lein)',
            ":lein",
            "where Leiningen finds project.clj",
            "the marker keyword for the Leiningen lesson"),
    ],
    subplots=_REAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-12 — deps.edn projects
G12_12 = SubjectCurriculum(
    grade=12, subject_id="G12-12",
    subject_title="deps.edn projects",
    fable="goose-eggs",
    examples=[
        _ex('(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)',
            ":studied",
            "the deps.edn manifest for the Clojure CLI",
            "the marker for the deps.edn lesson"),
        _ex('(do "deps.edn is read by the official `clj`/`clojure` tools" :deps)',
            ":deps",
            "who reads deps.edn",
            "the marker keyword for the deps.edn lesson"),
    ],
    subplots=_REAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-13 — Aliases and tools
G12_13 = SubjectCurriculum(
    grade=12, subject_id="G12-13",
    subject_title="Aliases and tools",
    fable="goose-eggs",
    examples=[
        _ex('(do "`clj -M:test` runs the :test alias from deps.edn" :studied)',
            ":studied",
            "the alias-execution pattern with the Clojure CLI",
            "the marker for the aliases lesson"),
        _ex('(do "aliases compose extra paths, deps, and main opts" :aliases)',
            ":aliases",
            "what aliases let you compose",
            "the marker keyword for the aliases lesson"),
    ],
    subplots=_REAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-14 — Pedestal / Ring brief
G12_14 = SubjectCurriculum(
    grade=12, subject_id="G12-14",
    subject_title="Pedestal / Ring (web stack brief)",
    fable="goose-eggs",
    examples=[
        _ex('(do "Ring models HTTP as request-map -> response-map" :studied)',
            ":studied",
            "the Ring HTTP-as-data abstraction",
            "the marker for the Ring lesson"),
        _ex('(do "Pedestal layers interceptors over Ring for richer pipelines" :web)',
            ":web",
            "the Pedestal interceptor model",
            "the marker keyword for the Pedestal lesson"),
    ],
    subplots=_REAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-15 — Datomic / XTDB brief
G12_15 = SubjectCurriculum(
    grade=12, subject_id="G12-15",
    subject_title="Datomic / XTDB (datalog db brief)",
    fable="goose-eggs",
    examples=[
        _ex('(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)',
            ":studied",
            "the Datomic / XTDB family",
            "the marker for the datalog-DB lesson"),
        _ex('(do "queries are written in datalog over EDN-shaped data" :datalog)',
            ":datalog",
            "how queries look in these databases",
            "the marker keyword for datalog queries"),
    ],
    subplots=_REAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-16 — Reagent brief
G12_16 = SubjectCurriculum(
    grade=12, subject_id="G12-16",
    subject_title="Reagent (cljs UI brief)",
    fable="goose-eggs",
    examples=[
        _ex('(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)',
            ":studied",
            "the Reagent wrapper around React",
            "the marker for the Reagent lesson"),
        _ex('(do "components are functions returning Hiccup vectors" :reagent)',
            ":reagent",
            "how Reagent components are written",
            "the marker keyword for Reagent components"),
    ],
    subplots=_REAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-17 — Library design patterns
G12_17 = SubjectCurriculum(
    grade=12, subject_id="G12-17",
    subject_title="Library design patterns",
    fable="goose-eggs",
    examples=[
        _ex('(do "good libraries expose data, then functions, then macros sparingly" :studied)',
            ":studied",
            "the Clojure library-design hierarchy",
            "the marker for the library-design lesson"),
        _ex('(do "small public API surface, plain data inputs, return values" :design)',
            ":design",
            "the conventional Clojure API shape",
            "the marker keyword for the API-shape lesson"),
        _ex("(= [1 2 3] (vec '(1 2 3)))", True,
            "a tiny example of a data-first conversion at the API edge",
            "whether the vector and the converted seq are equal"),
    ],
    subplots=_REAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-18 — Clojure style guide
G12_18 = SubjectCurriculum(
    grade=12, subject_id="G12-18",
    subject_title="Clojure style guide",
    fable="goose-eggs",
    examples=[
        _ex('(do "kebab-case names, two-space indent, threading for deep nests" :studied)',
            ":studied",
            "the community-style basics",
            "the marker for the style-guide lesson"),
        _ex('(do "prefer pure functions, name predicates with ?, danger! ops with !" :style)',
            ":style",
            "two naming conventions from the style guide",
            "the marker keyword for the naming-conventions lesson"),
    ],
    subplots=_REAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# ─────────────────────── registry ───────────────────────


SUBJECTS: dict[str, SubjectCurriculum] = {s.subject_id: s for s in (
    G12_01, G12_02, G12_03, G12_04, G12_05, G12_06, G12_07, G12_08, G12_09,
    G12_10, G12_11, G12_12, G12_13, G12_14, G12_15, G12_16, G12_17, G12_18,
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
    print(f"grade-12 goose-eggs smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
