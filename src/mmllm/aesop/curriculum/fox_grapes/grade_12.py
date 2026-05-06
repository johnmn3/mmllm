"""Grade 12 — real-world Clojure. Through fox-grapes.

Subplot lens: after many failed reaches and many honest evaluations,
the foxes look back over the tools that helped them tell which
clusters were truly out of reach and which weren't — transducers
for working a long row of vines, core.async for passing fruit between
baskets, spec for declaring what a ripe cluster looks like,
clojure.test for re-checking yesterday's harvest, and the libraries
every Clojure traveler will eventually meet. Each subject is a tool
re-examined at the day's end, with the patient fox preferring the
REPL's verdict over any after-the-fact rationalization.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.fox_grapes.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL, _GOAL_SUBPLOTS,
)
from mmllm.aesop.curriculum.fox_grapes._metaphor_pools import _SIEVE_SUBPLOTS


# ─────────────────────── grade-12 subplot extensions ───────────────────────
#
# The day of reaching is over and the light is fading. The two foxes
# look back over the tools they've gathered. Each subplot frames the
# subject as a tool re-examined after a season of honest evaluations.

_REAL_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    SubplotTemplate("""\
The day's reaching had ended {place} and the two foxes were sitting
beneath an old vine, comparing notes. {patient_fox_phrase} drew
{concept_phrase} into the dust. "We've kept honest tally for many
seasons now," {patient_fox_he_she} said. "The form {form_display} is
the kind of thing we'd reach for now." {hasty_fox} nodded — for once
willing to listen instead of declare the cluster sour."""),

    SubplotTemplate("""\
{patient_fox_phrase} had filled an entire notebook over the long
season with tools and patterns: transducers, channels, specs, tests.
Now {place} the next entry was {concept_phrase}, and the form was
{form_display}. {hasty_fox_phrase}, {emo_proud} but more reflective
than usual, agreed to write the form into the REPL instead of
dismissing it."""),

    SubplotTemplate("""\
"This isn't a quick rationalization," {patient_fox} said {place},
{emo_patient}. "It's a tool." {hasty_fox_phrase} looked at
{concept_phrase} and admitted {hasty_fox_he_she} would not have known
what to write. {patient_fox} sketched {form_display} on a slate so the
runtime could speak for itself."""),

    SubplotTemplate("""\
At the edge of the orchard {place}, a row of small monuments
commemorated the libraries the foxes had learned along the way. The
newest one honoured {concept_phrase}. {patient_fox_phrase} touched it
with a paw and said the form to remember was {form_display};
{hasty_fox_phrase} agreed to submit it instead of waving it off."""),

    SubplotTemplate("""\
{hasty_fox_phrase}, after a season of failed reaches and quick
excuses, was finally willing to study patterns instead of dismiss
them. {patient_fox_phrase} pointed {place} at {concept_phrase}. The
form {form_display} was the canonical example; the REPL would confirm
what it produced."""),

    SubplotTemplate("""\
A gathering of foxes {place} brought together every animal who'd
ever argued with a high cluster. The day's discussion was
{concept_phrase}. {patient_fox} wrote the form {form_display} on a
square of parchment and passed it across the table; {hasty_fox},
{emo_proud} but pleased to listen, agreed to read it into the REPL."""),
]


def _ex(form, expected, concept, what,
        goal="", scenario="", need="", mapping="", resolution="",
        tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal,
                          scenario=scenario, need=need,
                          mapping=mapping, resolution=resolution,
                          tags=tags)


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
    fable="fox-grapes",
    examples=[
        # Use the transducer-arity functions through `into` / `transduce`.
        _ex("(into [] (map inc) [1 2 3])", [2, 3, 4],
            'the form',
            'the value the form evaluates to',
            goal="pour a cluster-row through a sieve that raises each cluster's grade by one, into a fresh vector",
            scenario="Sly the fox held three grape clusters, graded 1, 2, 3 from the morning's tasting. A sieve hung over an empty stave-bucket — the sieve's rule was to raise every cluster's grade by one step up the ripeness scale.",
            need="Sly wanted all three clusters upgraded by the rule, collected into a vector the same shape as the empty bucket.",
            mapping="The `map` transducer raises each value by one; `into` pours the stream through the sieve and collects what falls into the receiving vector. Each cluster, lifted one grade, lands in order.",
            resolution="the bucket held the three clusters, each raised one grade — now graded 2, 3, 4 — in the same sequence.",
            tags=("story",)),
        _ex("(into [] (filter even?) [1 2 3 4 5])", [2, 4],
            'the form',
            'the value the form evaluates to',
            goal="pour five clusters through a sieve that keeps only the even-graded ones, into a fresh vector",
            scenario="Vix the fox faced a row of five clusters, graded 1, 2, 3, 4, 5. A sieve hung over an empty stave-bucket — the sieve's rule was to let only even-graded clusters through; odd grades fell away.",
            need="Vix wanted only the even clusters passed through, collected into a vector ready for tasting.",
            mapping="The `filter` transducer applies the even? test to each value; `into` pours the stream through the sieve and collects only what passes the rule into the receiving vector.",
            resolution="the bucket held two clusters, the ones that had passed the even-grade test — graded 2 and 4 — in order.",
            tags=("story",)),
    ],
    subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-02 — Transducer composition
G12_02 = SubjectCurriculum(
    grade=12, subject_id="G12-02",
    subject_title="Transducer composition",
    fable="fox-grapes",
    examples=[
        _ex("(into [] (comp (map inc) (filter even?)) [1 2 3 4])", [2, 4],
            'the form',
            'the value the form evaluates to',
            goal="stack two sieves so that each cluster is raised by one grade, then only the even ones pass through, into a fresh vector",
            scenario="Renard the fox stood with four clusters, graded 1, 2, 3, 4. Two sieves hung over an empty stave-bucket, stacked one above the other: the top one raised each grade by one; the bottom one let only even grades through.",
            need="Renard wanted the clusters raised and filtered in a single pass — first upgraded, then screened for even-ness — all collected in order into the vector.",
            mapping="The composed transducer `(comp (map inc) (filter even?))` stacks the sieves: `map` raises each value by one, then `filter` passes only the even ones. `into` collects what falls through both rules into the vector.",
            resolution="the bucket held two clusters that had made it through both sieves — the ones that, after raising by one, became even-graded — ready for use.",
            tags=("story",)),
        _ex("(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])", 12,
            'the form',
            'the value the form evaluates to',
            goal="stack two sieves for five clusters — raise each by one grade, keep only evens — then tally their new grades in a running sum",
            scenario="Sly the fox faced a harvest: five clusters, graded 1, 2, 3, 4, 5. Two sieves stood ready, stacked as before: one raised each grade, one filtered for evens. Instead of catching the result in a bucket, Sly held a tally-slate and a chalk-stick, ready to add each passing cluster's upgraded grade to the running sum.",
            need="Sly needed to know the total grade-value of the clusters that made it through both sieves — each raised by one, each passing the even-grade test.",
            mapping="The `transduce` form stacks the sieves (map, then filter), then applies the `+` operation to accumulate the results. Each value that passes both rules is added to the running tally; 0 is the starting sum.",
            resolution="the tally-slate now showed the sum of all passing clusters' upgraded grades — two clusters passed (2 and 4 after upgrade), totaling the final count.",
            tags=("story",)),
    ],
    subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-03 — into with a transducer
G12_03 = SubjectCurriculum(
    grade=12, subject_id="G12-03",
    subject_title="into with a transducer (xform)",
    fable="fox-grapes",
    examples=[
        _ex("(into #{} (map inc) [1 2 3])", {2, 3, 4},
            'the form',
            'the value the form evaluates to',
            goal="pour three clusters through a sieve that raises each by one grade, into a unique-only basket instead of a vector",
            scenario="Vix the fox held three clusters, graded 1, 2, 3. A sieve hung above not an empty stave-bucket but a woven unique-basket — a basket that kept only one of each grade, no duplicates. The sieve's rule raised each cluster by one step.",
            need="Vix wanted the three clusters upgraded and collected into the unique-basket, one of each new grade, with no room for repeats.",
            mapping="The `map inc` transducer raises each value by one; `into` with a set (#{}) pours the stream through the sieve and collects results into a unique-only basket instead of a vector. Duplicates are automatically dropped.",
            resolution="the unique-basket now held three clusters — each raised one grade — in no particular order, since unique-baskets don't track sequence.",
            tags=("story",)),
        _ex("(into [] (take 3) (range 100))", [0, 1, 2],
            'the form',
            'the value the form evaluates to',
            goal="pour from an endless supply of clusters numbered from 0 to 99, through a sieve that takes only the first three, into a vector",
            scenario="Sly the fox faced an endless line of clusters, numbered 0, 1, 2, 3, ... all the way to 99. A sieve hung over an empty stave-bucket — the sieve's rule was to take only the first three clusters in line and stop.",
            need="Sly needed the first three clusters from the infinite line, no more, collected in order into a vector.",
            mapping="The `take 3` transducer selects the first three items from the input stream; `into` pours the line through the sieve and collects only what the rule takes into the vector. The rest of the supply stays untouched.",
            resolution="the bucket held three clusters — the first three from the line, numbered 0, 1, 2 — and the endless supply continued beyond.",
            tags=("story",)),
    ],
    subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-04 — core.async introduction
G12_04 = SubjectCurriculum(
    grade=12, subject_id="G12-04",
    subject_title="core.async introduction",
    fable="fox-grapes",
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
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-05 — Channels and pipelines
G12_05 = SubjectCurriculum(
    grade=12, subject_id="G12-05",
    subject_title="Channels and pipelines",
    fable="fox-grapes",
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
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-06 — clojure.spec
G12_06 = SubjectCurriculum(
    grade=12, subject_id="G12-06",
    subject_title="clojure.spec",
    fable="fox-grapes",
    examples=[
        # We can run small spec predicates portably.
        _ex("(do (require '[clojure.spec.alpha :as s]) "
            "(s/valid? int? 42))", True,
            "the basic spec check (s/valid? int? 42)",
            "whether 42 conforms to the int? spec"),
        _ex("(do (require '[clojure.spec.alpha :as s]) "
            "(s/valid? string? 42))", False,
            "the failing spec check (s/valid? string? 42)",
            "whether 42 conforms to the string? spec"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-07 — Spec generators
G12_07 = SubjectCurriculum(
    grade=12, subject_id="G12-07",
    subject_title="Spec generators",
    fable="fox-grapes",
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
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-08 — clojure.test
G12_08 = SubjectCurriculum(
    grade=12, subject_id="G12-08",
    subject_title="clojure.test",
    fable="fox-grapes",
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
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-09 — Test fixtures
G12_09 = SubjectCurriculum(
    grade=12, subject_id="G12-09",
    subject_title="Test fixtures",
    fable="fox-grapes",
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
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-10 — Property-based testing
G12_10 = SubjectCurriculum(
    grade=12, subject_id="G12-10",
    subject_title="Property-based testing",
    fable="fox-grapes",
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
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-11 — Leiningen project.clj
G12_11 = SubjectCurriculum(
    grade=12, subject_id="G12-11",
    subject_title="Leiningen project.clj",
    fable="fox-grapes",
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
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-12 — deps.edn projects
G12_12 = SubjectCurriculum(
    grade=12, subject_id="G12-12",
    subject_title="deps.edn projects",
    fable="fox-grapes",
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
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-13 — Aliases and tools
G12_13 = SubjectCurriculum(
    grade=12, subject_id="G12-13",
    subject_title="Aliases and tools",
    fable="fox-grapes",
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
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-14 — Pedestal / Ring brief
G12_14 = SubjectCurriculum(
    grade=12, subject_id="G12-14",
    subject_title="Pedestal / Ring (web stack brief)",
    fable="fox-grapes",
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
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-15 — Datomic / XTDB brief
G12_15 = SubjectCurriculum(
    grade=12, subject_id="G12-15",
    subject_title="Datomic / XTDB (datalog db brief)",
    fable="fox-grapes",
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
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-16 — Reagent brief
G12_16 = SubjectCurriculum(
    grade=12, subject_id="G12-16",
    subject_title="Reagent (cljs UI brief)",
    fable="fox-grapes",
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
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-17 — Library design patterns
G12_17 = SubjectCurriculum(
    grade=12, subject_id="G12-17",
    subject_title="Library design patterns",
    fable="fox-grapes",
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
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-18 — Clojure style guide
G12_18 = SubjectCurriculum(
    grade=12, subject_id="G12-18",
    subject_title="Clojure style guide",
    fable="fox-grapes",
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
    print(f"grade-12 fox-grapes smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
