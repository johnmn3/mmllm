"""Grade 12 — real-world Clojure. Through dog-shadow.

Subplot lens: the long race finally ends, and the racers reflect on
the tools they've used along the way — transducers for the long
straight stretches, core.async for talking with other racers, spec
for declaring the rules of the course, clojure.test for retracing the
route, and the libraries every Clojure traveler will eventually meet.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.dog_shadow.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.dog_shadow._metaphor_pools import (
    _SIEVE_SUBPLOTS,
)


# ─────────────────────── grade-12 subplot extensions ───────────────────────
#
# The race is over and the day is long. The Hare and the Tortoise
# look back over the tools they've gathered. Each subplot frames the
# subject as a tool re-examined at the finish line.

_REAL_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    SubplotTemplate("""\
The race had ended {place} and the two were sitting beneath an old
tree, comparing notes. {tortoise} drew {concept_phrase} into
the dust. "We've come a long way," {tortoise_he_she} said. "The form
{form_display} is the kind of thing we'd reach for now." {hare}
nodded — for once {emo_tired} enough to listen."""),

    SubplotTemplate("""\
{tortoise} had filled an entire notebook over the long race
with tools and patterns — transducers, channels, specs, tests —
and {place} the next entry was {concept_phrase}, with the form
written as {form_display}. {hare_phrase}, {emo_proud} but more
reflective than usual, agreed to write the form into the REPL."""),

    SubplotTemplate("""\
"This isn't a sprint trick," {tortoise} said {place}, {emo_patient}.
"It's a tool." {hare} looked at {concept_phrase} and admitted
{hare_he_she} would not have known what to write. {tortoise} sketched
{form_display} on a slate so the runtime could speak for itself."""),

    SubplotTemplate("""\
At the finish line {place}, a row of small monuments commemorated
the libraries the racers had learned along the way. The newest one
honoured {concept_phrase}. {tortoise}, {emo_patient} touched it with a paw
and said the form to remember was {form_display}; {hare_phrase}
agreed to submit it."""),

    SubplotTemplate("""\
{hare}, {emo_tired}, was finally willing
to study patterns. {tortoise_phrase} pointed {place} at
{concept_phrase}. The form {form_display} was the canonical example;
the REPL would confirm what it produced."""),

    SubplotTemplate("""\
A banquet at the end of the road {place} brought together every
animal who'd ever raced. The day's discussion was {concept_phrase}.
{tortoise} wrote {form_display} on a square of parchment
and passed it across the table; {hare}, {emo_tired} but pleased,
agreed to read it into the REPL."""),
]


def _ex(form, expected, concept, what, goal="", tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal, tags=tags)


_PLAN_G12 = _PLAN_POOL + (
    "I write the form using the appropriate library or tool.",
    "I express the pipeline / spec / test as a Clojure form.",
    "I let the REPL exercise the library form.",
)


# ─────────────────────── 18 grade-12 subjects ───────────────────────


# G12-01 — Transducers introduction
G12_01 = SubjectCurriculum(
    grade=12, subject_id="G12-01",
    subject_title="Transducers introduction",
    fable="dog-shadow",
    examples=[
        # Use the transducer-arity functions through `into` / `transduce`.
        SubjectExample(
            form="(into [] (map inc) [1 2 3])",
            expected=[2, 3, 4],
            concept_phrase="the map-inc transducer applied via into",
            question_what="the vector produced by reifying the map-inc transducer into an empty vector via into, applied to the vector containing 1, 2, 3",
            goal_text="use the map-inc transducer with into to increment the vector containing 1, 2, 3",
            scenario=(
                "Bell the hound found a log with a gap at the stream\'s edge, "
                "the opening shaped to add one bone\'s weight to any bone that "
                'passed through. Laid before it lay a row of light bones — 1, 2, 3 — '
                'waiting on the near bank.'
            ),
            need=(
                'She wanted to run each bone through the gap, watch the rule '
                'transform each one, and catch what fell through into an empty row '
                'on the far bank. The final result would show the cumulative '
                'increment.'
            ),
            mapping=(
                'The gap is the map-inc rule, the row of input bones is the '
                'vector, each passing bone is an element, and the empty row '
                'where the changed bones land is the into-vessel.'
            ),
            resolution=(
                'The REPL threaded each bone through the gap, applied the '
                'increment, and collected the 3 into the empty vector. What '
                'fell through was the vector of incremented bones: 2, 3, 4.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(into [] (filter even?) [1 2 3 4 5])",
            expected=[2, 4],
            concept_phrase="the filter-even transducer applied via into",
            question_what="the vector of even elements reified via into with the filter-even transducer applied to the vector containing 1, 2, 3, 4, 5",
            goal_text="use the filter-even transducer with into to keep only the even numbers from the vector [1 2 3 4 5]",
            scenario=(
                'Rex the hound stood at a log with a gap — wide for even bones but '
                'too narrow for odd ones. Before the gap lay bones 1, 2, 3, 4, 5.'
            ),
            need=(
                'He wanted each bone through the gap, let it decide which would '
                'pass, and catch survivors. Only even bones would make it.'
            ),
            mapping=(
                'The gap is the filter-even rule, the input heap is the vector, '
                'each bone is an element, and into collects the survivors.'
            ),
            resolution=(
                'The REPL tested each: 1 stuck, 2 passed, 3 stuck, 4 passed, 5 '
                'stuck. The vessel held the ones that fit: 2 and 4 — 5.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-02 — Transducer composition
G12_02 = SubjectCurriculum(
    grade=12, subject_id="G12-02",
    subject_title="Transducer composition",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(into [] (comp (map inc) (filter even?)) [1 2 3 4])",
            expected=[2, 4],
            concept_phrase="the composed transducer pipeline of map-inc then filter-even",
            question_what="the vector result of reifying the composed transducer via into, applying map-inc then filter-even to the vector containing 1, 2, 3, 4",
            goal_text="compose map-inc and filter-even into a transducer pipeline; apply it with into to the vector [1 2 3 4]",
            scenario=(
                'Patch the hound arrived at the river bank and saw two logs '
                'stacked side by side — one gap shaped to add weight, the second '
                'gap shaped to filter. "I can stack these," Patch said. Bones lay '
                'on the near bank: 1, 2, 3, 4.'
            ),
            need=(
                'The hound wanted to send each bone through the first gap to add '
                'weight, catch the result, feed it through the second gap to '
                'filter, and catch the final survivors in an empty row on the far '
                'bank.'
            ),
            mapping=(
                'The stacked gaps are the composed transducer, the pipeline moves '
                'through both rules in order, each input bone is an element, and '
                'the empty row is the final collecting vessel.'
            ),
            resolution=(
                'The REPL threaded 1, 2, 3, 4 through the composed pipeline: '
                'first they gained weight (to 2, 3, 4, 5), then the filter kept '
                'only the even ones. What landed in the final vessel was the '
                'precise count: 2 and 4 — 4.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])",
            expected=12,
            concept_phrase="the composed transducer summing the incremented-then-filtered elements",
            question_what="the sum accumulated via transduce using the composed transducer of map-inc then filter-even, starting from 0, applied to the vector containing 1, 2, 3, 4, 5",
            goal_text="compose map-inc and filter-even; use transduce to sum the kept elements from the vector [1 2 3 4 5] starting from 0",
            scenario=(
                'Bell the hound found two stacked logs — the first adding weight, '
                'the second filtering. Her receiver was a counting-stick. Bones 1 '
                'through 5 waited to pass.'
            ),
            need=(
                'She wanted each bone through both gaps, summed into a total, '
                'starting from zero, using the transducer to do the work.'
            ),
            mapping=(
                'The stacked gaps are the composed transducer, transduce is the '
                'reduction operator, and the counting-stick is where the tally '
                'accumulates.'
            ),
            resolution=(
                'The REPL applied the pipeline: each bone incremented, then '
                'filtered. The kept ones were summed into the final tally — 5.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-03 — into with a transducer
G12_03 = SubjectCurriculum(
    grade=12, subject_id="G12-03",
    subject_title="into with a transducer (xform)",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(into #{} (map inc) [1 2 3])",
            expected={2, 3, 4},
            concept_phrase="the transducer-powered construction of a set from incremented elements",
            question_what="the set produced by reifying the map-inc transducer into an empty set via into, applied to the vector containing 1, 2, 3",
            goal_text="use the map-inc transducer with into to create a set from the incremented elements of the vector containing 1, 2, 3",
            scenario=(
                "Rex the hound stood at the stream\'s edge with two kinds of "
                'receivers: an empty row and an empty pile. He had a gap that '
                'added weight, and bones 1, 2, 3 lay ready. "The gap is the same '
                'rule," he said. "But the receiver matters."'
            ),
            need=(
                'He wanted to run each bone through the increment gap, catch the '
                'result, and this time pour them into an empty pile instead of a '
                'row — to keep only unique weights with no duplicates.'
            ),
            mapping=(
                'The gap is the map-inc rule, the input bones are the elements, '
                'the changed bones fall through the gap, and the empty pile is the '
                'set-shaped receiver that into fills.'
            ),
            resolution=(
                'The REPL threaded each bone through the gap and poured the '
                'incremented weights into the pile instead of the row. The unique '
                'pile held 2, 3, and 4 — one of each — 3.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(into [] (take 3) (range 100))",
            expected=[0, 1, 2],
            concept_phrase="the transducer-powered collection of the first few elements",
            question_what="the vector produced by reifying the take-3 transducer into an empty vector via into, applied to the range of 100 numbers",
            goal_text="use the take-3 transducer with into to collect the first three elements from a range of 100 numbers",
            scenario=(
                'Patch arrived at a vast stream — an endless flood, a range of '
                'one hundred bones. A gap at the bank stopped after three passed.'
            ),
            need=(
                'The hound wanted the gap to let through just the first 100 bones into an empty row. The form would stop when it had what it needed.'
            ),
            mapping=(
                'The gap is the take-3 rule, the flood is the range, each bone is '
                'an element, and the row is the collecting vessel.'
            ),
            resolution=(
                'The REPL sent bones through the gap: 0, 1, 2 passed — and the gap '
                'closed. The row caught the first three from the endless stream — 100.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-04 — core.async introduction
G12_04 = SubjectCurriculum(
    grade=12, subject_id="G12-04",
    subject_title="core.async introduction",
    fable="dog-shadow",
    examples=[
        # core.async pulls in heavy machinery; describe the topic via marker.
        _ex('(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)',
            ":studied",
            "the core.async channel and block primitives",
            "the keyword marking the core.async lesson",
            goal="study the core.async primitives that form the foundation for async patterns"),
        _ex('(do "go-blocks let you write async code as if it were synchronous" :async)',
            ":async",
            "the synchronous-style pattern that go-blocks enable",
            "the keyword marking the go-block pattern lesson",
            goal="learn how go-blocks let you write asynchronous code in a synchronous style"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-05 — Channels and pipelines
G12_05 = SubjectCurriculum(
    grade=12, subject_id="G12-05",
    subject_title="Channels and pipelines",
    fable="dog-shadow",
    examples=[
        _ex('(do "pipe, mult, mix, pipeline-async route values across channels" :studied)',
            ":studied",
            "the composition operators for building async pipelines",
            "the keyword marking the async pipeline lesson",
            goal="study how pipe, mult, mix, and pipeline-async route values across channels"),
        _ex('(do "pipelines transform streams of values channel-to-channel" :pipelines)',
            ":pipelines",
            "the stream-transformation capability of pipelines",
            "the keyword marking the pipeline transformation lesson",
            goal="understand how pipelines transform streams of values flowing between channels"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-06 — clojure.spec
G12_06 = SubjectCurriculum(
    grade=12, subject_id="G12-06",
    subject_title="clojure.spec",
    fable="dog-shadow",
    examples=[
        # We can run small spec predicates portably.
        _ex("(do (require '[clojure.spec.alpha :as s]) "
            "(s/valid? int? 42))", True,
            "the spec validation check for int? against 42",
            "the result of validating 42 against the int? spec",
            goal="use spec to validate that 42 conforms to the int? predicate"),
        _ex("(do (require '[clojure.spec.alpha :as s]) "
            "(s/valid? string? 42))", False,
            "the spec validation check for string? against 42",
            "the result of validating 42 against the string? spec",
            goal="use spec to validate that 42 conforms to the string? predicate"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-07 — Spec generators
G12_07 = SubjectCurriculum(
    grade=12, subject_id="G12-07",
    subject_title="Spec generators",
    fable="dog-shadow",
    examples=[
        _ex('(do "s/exercise produces sample inputs for a spec" :studied)',
            ":studied",
            "the sample-generation capability of s/exercise",
            "the keyword marking the spec-generator lesson",
            goal="study how s/exercise produces sample inputs from a spec"),
        _ex('(do "spec generators turn specs into property-based test inputs" :gens)',
            ":gens",
            "the generation mechanism that converts specs to test data",
            "the keyword marking the test-input generation lesson",
            goal="understand how spec generators turn specs into property-based test inputs"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-08 — clojure.test
G12_08 = SubjectCurriculum(
    grade=12, subject_id="G12-08",
    subject_title="clojure.test",
    fable="dog-shadow",
    examples=[
        # We can demonstrate the boolean essence of an assertion via =.
        _ex("(= (+ 1 2) 3)", True,
            "the equality assertion at the heart of test checking",
            "the truth value showing the assertion passes",
            goal="test whether the sum of 1 and 2 equals 3 using equality"),
        _ex('(do "(deftest …), (is …), (testing …) are the core test forms" :studied)',
            ":studied",
            "the fundamental test definition and assertion forms",
            "the keyword marking the clojure.test lesson",
            goal="study the core test forms: deftest, is, and testing"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-09 — Test fixtures
G12_09 = SubjectCurriculum(
    grade=12, subject_id="G12-09",
    subject_title="Test fixtures",
    fable="dog-shadow",
    examples=[
        _ex('(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)',
            ":studied",
            "the fixture pattern for test setup and teardown",
            "the keyword marking the test fixtures lesson",
            goal="study how use-fixtures wraps every deftest in setup and teardown"),
        _ex('(do "fixtures provide setup/teardown around deftests" :fixtures)',
            ":fixtures",
            "the environment-preparation role of fixtures in testing",
            "the keyword marking the fixture-purpose lesson",
            goal="understand how fixtures provide setup and teardown around tests"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-10 — Property-based testing
G12_10 = SubjectCurriculum(
    grade=12, subject_id="G12-10",
    subject_title="Property-based testing",
    fable="dog-shadow",
    examples=[
        # A property: reverse of reverse equals identity. We check it once
        # to model what a property test would do generically.
        _ex("(= (reverse (reverse [1 2 3])) [1 2 3])", True,
            "the property that reversing twice restores the original",
            "the result of checking the double-reverse property",
            goal="verify the property that reversing a vector twice returns the original vector"),
        _ex('(do "test.check generates inputs and checks properties hold" :studied)',
            ":studied",
            "the property-checking library and its capabilities",
            "the keyword marking the property-based testing lesson",
            goal="study how test.check generates inputs and verifies that properties hold"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-11 — Leiningen project.clj
G12_11 = SubjectCurriculum(
    grade=12, subject_id="G12-11",
    subject_title="Leiningen project.clj",
    fable="dog-shadow",
    examples=[
        _ex('(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)',
            ":studied",
            "the project configuration manifest for Leiningen",
            "the keyword marking the project.clj lesson",
            goal="study the project.clj file and how it declares dependencies, main entry points, and profiles for Leiningen"),
        _ex('(do "Leiningen reads project.clj at the project root" :lein)',
            ":lein",
            "the project root configuration discovery mechanism",
            "the keyword marking the Leiningen configuration lesson",
            goal="understand how Leiningen reads project.clj from the project root"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-12 — deps.edn projects
G12_12 = SubjectCurriculum(
    grade=12, subject_id="G12-12",
    subject_title="deps.edn projects",
    fable="dog-shadow",
    examples=[
        _ex('(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)',
            ":studied",
            "the deps.edn configuration manifest for the Clojure CLI",
            "the keyword marking the deps.edn lesson",
            goal="study the deps.edn file and how it declares dependencies and aliases for the Clojure CLI"),
        _ex('(do "deps.edn is read by the official `clj`/`clojure` tools" :deps)',
            ":deps",
            "the tools that interpret the deps.edn configuration",
            "the keyword marking the CLI tools lesson",
            goal="understand how the official clj and clojure CLI tools read deps.edn"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-13 — Aliases and tools
G12_13 = SubjectCurriculum(
    grade=12, subject_id="G12-13",
    subject_title="Aliases and tools",
    fable="dog-shadow",
    examples=[
        _ex('(do "`clj -M:test` runs the :test alias from deps.edn" :studied)',
            ":studied",
            "the alias execution mechanism in the Clojure CLI",
            "the keyword marking the alias usage lesson",
            goal="study how the clj command with -M flag runs aliases defined in deps.edn"),
        _ex('(do "aliases compose extra paths, deps, and main opts" :aliases)',
            ":aliases",
            "the composition of paths, dependencies, and options via aliases",
            "the keyword marking the alias composition lesson",
            goal="understand how aliases compose extra classpath entries, dependencies, and JVM options"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-14 — Pedestal / Ring brief
G12_14 = SubjectCurriculum(
    grade=12, subject_id="G12-14",
    subject_title="Pedestal / Ring (web stack brief)",
    fable="dog-shadow",
    examples=[
        _ex('(do "Ring models HTTP as request-map -> response-map" :studied)',
            ":studied",
            "the HTTP-as-data abstraction that Ring provides",
            "the keyword marking the Ring foundation lesson",
            goal="study how Ring models HTTP requests and responses as Clojure maps"),
        _ex('(do "Pedestal layers interceptors over Ring for richer pipelines" :web)',
            ":web",
            "the interceptor architecture that Pedestal builds on Ring",
            "the keyword marking the Pedestal pattern lesson",
            goal="understand how Pedestal layers interceptors over Ring to create rich request-processing pipelines"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-15 — Datomic / XTDB brief
G12_15 = SubjectCurriculum(
    grade=12, subject_id="G12-15",
    subject_title="Datomic / XTDB (datalog db brief)",
    fable="dog-shadow",
    examples=[
        _ex('(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)',
            ":studied",
            "the family of immutable, time-aware datalog databases",
            "the keyword marking the datalog database lesson",
            goal="study Datomic and XTDB as immutable, time-aware database systems using datalog"),
        _ex('(do "queries are written in datalog over EDN-shaped data" :datalog)',
            ":datalog",
            "the query language and data shape used in datalog databases",
            "the keyword marking the datalog query lesson",
            goal="learn how queries are written in datalog over EDN-structured data"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-16 — Reagent brief
G12_16 = SubjectCurriculum(
    grade=12, subject_id="G12-16",
    subject_title="Reagent (cljs UI brief)",
    fable="dog-shadow",
    examples=[
        _ex('(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)',
            ":studied",
            "the Reagent library as a Clojure wrapper around React",
            "the keyword marking the Reagent foundation lesson",
            goal="study how Reagent wraps React with Hiccup-shaped Clojure data structures"),
        _ex('(do "components are functions returning Hiccup vectors" :reagent)',
            ":reagent",
            "the function-based component model in Reagent",
            "the keyword marking the Reagent component lesson",
            goal="learn how Reagent components are functions that return Hiccup vectors"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-17 — Library design patterns
G12_17 = SubjectCurriculum(
    grade=12, subject_id="G12-17",
    subject_title="Library design patterns",
    fable="dog-shadow",
    examples=[
        _ex('(do "good libraries expose data, then functions, then macros sparingly" :studied)',
            ":studied",
            "the library-design hierarchy from data through functions to macros",
            "the keyword marking the design-hierarchy lesson",
            goal="study the library-design principle that good APIs expose data first, functions second, macros sparingly"),
        _ex('(do "small public API surface, plain data inputs, return values" :design)',
            ":design",
            "the minimal API surface and data-centric design pattern",
            "the keyword marking the API design lesson",
            goal="understand the Clojure convention of a small public API surface with plain data inputs and outputs"),
        _ex("(= [1 2 3] (vec '(1 2 3)))", True,
            "the type-conversion behavior between sequences and vectors",
            "the result of comparing a vector to its converted seq counterpart",
            goal="verify that converting a seq to a vector produces the same data structure"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-18 — Clojure style guide
G12_18 = SubjectCurriculum(
    grade=12, subject_id="G12-18",
    subject_title="Clojure style guide",
    fable="dog-shadow",
    examples=[
        _ex('(do "kebab-case names, two-space indent, threading for deep nests" :studied)',
            ":studied",
            "the community formatting and nesting conventions",
            "the keyword marking the basic style lesson",
            goal="study the Clojure style guide basics: kebab-case naming, two-space indentation, and threading macros for nesting"),
        _ex('(do "prefer pure functions, name predicates with ?, danger! ops with !" :style)',
            ":style",
            "the naming conventions for functions and predicates in idiomatic Clojure",
            "the keyword marking the naming-conventions lesson",
            goal="learn the Clojure naming conventions: pure function preference, question-mark suffixes for predicates, exclamation marks for side-effectful operations"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
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
    print(f"grade-12 dog-shadow smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
