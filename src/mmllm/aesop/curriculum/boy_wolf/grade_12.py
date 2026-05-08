"""Grade 12 — real-world Clojure. Through boy-who-cried-wolf.

Subplot lens: the long season has ended and the village reflects on
the tools the careful shepherds have collected — transducers, channels,
specs, tests. Each is a tool against the kind of careless guessing
that used to cost the watchhouse so dearly. The shepherd, finally tired
and reflective, agrees that careful tools beat clever guesses, but
the corrective discipline still belongs to the elder and the villagers.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.boy_wolf.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.boy_wolf._metaphor_pools import (
    _GOAL_SUBPLOTS, _SIEVE_SUBPLOTS,
)
from mmllm.aesop.curriculum.boy_wolf._goals import GOALS, get_goal


# ─────────────────────── grade-12 subplot extensions ───────────────────────
#
# The long season has ended and the watchhouse reflects on the tools the
# careful shepherds have collected. Each subplot frames the subject as
# a tool re-examined at season's end. The shepherd is mature enough
# to listen now, but the corrective voice is still the elder's.

_REAL_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    SubplotTemplate("""\
The long season had ended {place} and the two were sitting beneath an
old tree, comparing notes. {elder_phrase} drew {concept_phrase} into
the dust. "We've come a long way," {elder_he_she} said. "The form
{form_display} is the kind of thing we'd reach for now." {shepherd}
nodded — for once {emo_tired} enough to listen."""),

    # NOTE (boy-wolf polish, hand-audit pass): "...specs, tests.
    # {place}, the next entry was..." rendered as a lowercase {place}
    # starting a new sentence after the period. Replaced the period
    # with a semicolon so {place} stays mid-sentence.
    SubplotTemplate("""\
{elder_phrase} had filled an entire notebook over the long season with
tools and patterns: transducers, channels, specs, tests; {place}, the
next entry was {concept_phrase}, and the form was {form_display}.
{shepherd_phrase}, {emo_regretful} but more reflective than usual,
agreed to write the form into the REPL."""),

    SubplotTemplate("""\
"This isn't a clever guess," {elder} said {place}, {emo_patient}.
"It's a tool." {shepherd_phrase} looked at {concept_phrase} and
admitted {shepherd_he_she} would not have known what to write.
{elder} sketched {form_display} on a slate so the runtime could speak
for itself."""),

    SubplotTemplate("""\
At the townsfolk square {place}, a row of small markers commemorated
the libraries the careful shepherds had learned over the season. The
newest one honoured {concept_phrase}. {elder_phrase} touched it and
said the form to remember was {form_display}; {shepherd_phrase}
agreed to submit it."""),

    SubplotTemplate("""\
{shepherd_phrase}, {emo_tired}, was finally willing to study patterns.
{elder_phrase} pointed {place} at {concept_phrase}. The form
{form_display} was the canonical example; the REPL would confirm what
it produced."""),

    SubplotTemplate("""\
A harvest gathering at the end of the season {place} brought together
every villager. The day's discussion was {concept_phrase}. {elder}
wrote it {form_display} on a square of parchment and passed it
across the table; {shepherd}, {emo_tired} but pleased to be trusted
again, agreed to read it into the REPL."""),
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
    fable="boy-wolf",
    examples=[
        # Use the transducer-arity functions through `into` / `transduce`.
        _ex("(into [] (map inc) [1 2 3])", [2, 3, 4],
            "the transducer (map inc) used via into",
            "[1 2 3] each incremented through a transducer",
            scenario=(
                "The season's last fleece-combing was underway. Carol held "
                "the comb at its teeth, a rule attached: increment each number "
                "as it passed through. Three raw counts from the morning tally "
                "waited to be poured through."
            ),
            need=(
                "The village needed each number increased by one, the results "
                "collected into an empty wool-basket below. The fleece-comb "
                "could apply the rule, but the shepherd had never poured numbers "
                "through a transducer before."
            ),
            mapping=(
                "The transducer `(map inc)` is the rule on the comb's teeth. "
                "`into` is the pour-and-collect: the empty receiver basket, "
                "the transducer rule, and the source feed together."
            ),
            resolution=(
                'Each number passed through, incremented by the rule, landing in the basket as it emerged — it returned [2 3 4], and the shepherd finally saw: transducers separate the rule from the receiver.'
            )),
        _ex("(into [] (filter even?) [1 2 3 4 5])", [2, 4],
            "the transducer (filter even?) used via into",
            "the even elements via a filter transducer",
            scenario=(
                "Carol attached a filtering rule to the fleece-comb."
            ),
            need=(
                "The village wanted only the even-numbered items collected together."
            ),
            mapping=(
                "`into` feeds items through the transducer into a receiver vector."
            ),
            resolution=(
                'The transducer filtered the items and returned the qualifying results (with `1` as the input value) (with `3` as the input value).'
            )),
    ],
    subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-02 — Transducer composition
G12_02 = SubjectCurriculum(
    grade=12, subject_id="G12-02",
    subject_title="Transducer composition",
    fable="boy-wolf",
    examples=[
        _ex("(into [] (comp (map inc) (filter even?)) [1 2 3 4])", [2, 4],
            "the composed transducer (comp (map inc) (filter even?))",
            "the result of inc-then-keep-evens via a composed transducer",
            scenario=(
                "Carol stood at the watchhouse, two fleece-combs in her hands. "
                "The first comb would increment each number; the second would "
                "keep only the even ones. Four raw numbers from the ledger waited."
            ),
            need=(
                "The village needed to increment each number, then filter for "
                "evens only. Two rules in order: change first, then select."
            ),
            mapping=(
                "`comp` stacks the transducers: `(map inc)` feeds into "
                "`(filter even?)`. The composed rule is a single comb with two "
                "teeth, both rules working as one."
            ),
            resolution=(
                'The numbers passed through: 1→2 (kept), 2→3 (dropped), 3→4 (kept), 4→5 (dropped). The form returned [2 4]. Composition let the shepherd chain multiple transducers without intermediate baskets.'
            )),
        _ex("(transduce (comp (map inc) (filter even?)) + 0 [1 2 3 4 5])",
            12,
            "transduce with a composed transducer summing the kept items",
            "the sum after inc-then-keep-evens via transduce",
            scenario=(
                "The same two combs sat ready. This time, Carol held a summing "
                "tally-stick, not a basket. Five numbers lay on the slate."
            ),
            need=(
                "The village needed to transform and filter the numbers, then sum "
                "the results. No intermediate basket; the reducing function would "
                "tally as items emerged."
            ),
            mapping=(
                "`transduce` combines the composed transducer with a reducing "
                "function: `+` sums each item that passes through. The rule runs "
                "and the sum accumulates in a single pass."
            ),
            resolution=(
                'Numbers 1→2, 2→3 (filtered), 3→4, 4→5 (filtered), 5→6 (filtered). The sum: 2 + 4 + 6 = 12. Transduce saved memory and worked in one pass through the data.'
            )),
    ],
    subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-03 — into with a transducer
G12_03 = SubjectCurriculum(
    grade=12, subject_id="G12-03",
    subject_title="into with a transducer (xform)",
    fable="boy-wolf",
    examples=[
        _ex("(into #{} (map inc) [1 2 3])", {2, 3, 4},
            "into a set with the (map inc) transducer",
            "the set produced by mapping inc into an empty set",
            scenario=(
                'Carol had an empty unique-only basket — one that would not hold duplicates. The fleece-comb with its increment rule waited. the numbers sat ready to be poured through.'
            ),
            need=(
                "The numbers needed to be incremented and collected into a set "
                "basket. Sets kept only unique values, unlike the plain vector "
                "baskets the shepherd knew."
            ),
            mapping=(
                "`into` takes the receiver basket, the transducer rule, and the "
                "source. Here, the receiver is `#{}` (a set), the rule is "
                "`(map inc)`, and the source is `[1 2 3]`."
            ),
            resolution=(
                'The numbers 1, 2, 3 became 2, 3, 4 through the comb, and the set basket caught them: #{2 3 4}. The form showed that `into` works with any basket shape.'
            )),
        _ex("(into [] (take 3) (range 100))", [0, 1, 2],
            "into [] with the (take 3) transducer over (range 100)",
            "the first three items collected through a transducer",
            scenario=(
                'A fleece-comb with a new rule: take only the first 100 items, drop the rest. An infinite cord of numbers waited — 0, 1, 2, ... up to 99. An empty wool-basket sat ready.'
            ),
            need=(
                'The village needed only the first 100 numbers from the long sequence, collected into a vector. The transducer would stop after three, so the REPL never had to process the rest.'
            ),
            mapping=(
                "`(take 3)` is the comb's rule: stop after 100 items pass through. `(range 100)` feeds the numbers. `into` pours them through and collects into the vector basket."
            ),
            resolution=(
                'Numbers 0, 1, 2 passed through and landed in the basket. The transducer stopped; no processing of 3–99 happened. The form returned [0 1 2], and the shepherd saw efficiency.'
            )),
    ],
    subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-04 — core.async introduction
G12_04 = SubjectCurriculum(
    grade=12, subject_id="G12-04",
    subject_title="core.async introduction",
    fable="boy-wolf",
    examples=[
        # core.async pulls in heavy machinery; describe the topic via marker.
        _ex('(do "(chan), (go ...), (<! ...), (>! ...) form the core.async core" :studied)',
            ":studied",
            "the core.async primitives chan/go/<!/>!",
            "the marker for the core.async lesson",
            scenario=(
                "The long season had ended. Carol and Tom sat reviewing the tools "
                "they had finally learned. Core.async had been hard to grasp — the "
                "channels, the go-blocks, the put and take operations."
            ),
            need=(
                "Tom had often shouted guesses about what core.async 'really did,' "
                "but he had never written the primitives into the REPL to check."
            ),
            mapping=(
                "Channels are the pipes; go-blocks are the routines that run inside "
                "them. `<!` takes a value from the channel; `>!` puts one in. All "
                "four are the foundation."
            ),
            resolution=(
                "Carol wrote each primitive carefully into the REPL. Tom watched them work, no magic, only patient discipline. By season's end, they both knew the shape. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record."
            )),
        _ex('(do "go-blocks let you write async code as if it were synchronous" :async)',
            ":async",
            "what go blocks give you",
            "the marker keyword for go-blocks",
            scenario=(
                "The village had built many small async routines over the season. "
                "Tom had always found them confusing — the callbacks, the nesting."
            ),
            need=(
                "Carol showed Tom that go-blocks let the REPL pretend async was "
                "sync, making the form readable."
            ),
            mapping=(
                "A go-block is a routine that can `<!` and `>!` on channels without "
                "blocking the main thread. The code reads like sync, but it is not."
            ),
            resolution=(
                'The form showed go-blocks in action. Tom finally understood: they were a way to write readable async code. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-05 — Channels and pipelines
G12_05 = SubjectCurriculum(
    grade=12, subject_id="G12-05",
    subject_title="Channels and pipelines",
    fable="boy-wolf",
    examples=[
        _ex('(do "pipe, mult, mix, pipeline-async route values across channels" :studied)',
            ":studied",
            "the pipeline operators in core.async",
            "the marker for the channel-pipeline lesson",
            scenario=(
                "The season's closing found Carol and Tom reviewing the channel "
                "routines they had built. Pipes, multiplexes, and async pipelines "
                "had seemed chaotic at first."
            ),
            need=(
                "Tom had always guessed about how channels connected. Carol wanted "
                "him to see each operator in the REPL."
            ),
            mapping=(
                "`pipe` connects channels directly; `mult` splits one to many; "
                "`mix` merges many into one; `pipeline-async` transforms values "
                "as they flow."
            ),
            resolution=(
                "Carol wrote each operator into the REPL. Tom saw the patterns: channels could be wired together like the village's water-runs, each route doing its work. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand."
            )),
        _ex('(do "pipelines transform streams of values channel-to-channel" :pipelines)',
            ":pipelines",
            "the role of pipelines in async code",
            "the marker keyword for pipelines",
            scenario=(
                "By the end, Tom had finally accepted that streams mattered. "
                "Pipelines were not just plumbing; they were the pattern."
            ),
            need=(
                "Carol showed him that pipelines let each stage transform values "
                "as they moved from channel to channel."
            ),
            mapping=(
                "A pipeline is a routine that reads from one channel, applies a "
                "function, and writes to another. Stages compose into flows."
            ),
            resolution=(
                'The form showed pipelines working. Tom understood: async code was often best described as streams transforming through stages. Tom chalked {drawn.a} on the meadow folk notice, and the morning record stood for the next shepherd to read.'
            )),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-06 — clojure.spec
G12_06 = SubjectCurriculum(
    grade=12, subject_id="G12-06",
    subject_title="clojure.spec",
    fable="boy-wolf",
    examples=[
        # We can run small spec predicates portably.
        _ex("(do (require '[clojure.spec.alpha :as s]) "
            "(s/valid? int? 42))", True,
            "(s/valid? int? 42)",
            "whether 42 conforms to the int? spec",
            scenario=(
                "The village's log-book held many entries. Carol was teaching Tom "
                "how to write rules about what data was allowed in each field."
            ),
            need=(
                "Tom guessed that any value could go anywhere. Carol wanted him to "
                "write specs and let the runtime enforce the rules."
            ),
            mapping=(
                "A spec is a rule about what values are valid. `(s/valid? int? 42)` "
                "asks: does 42 conform to the int? spec? The REPL returns true or "
                "false."
            ),
            resolution=(
                'The form showed the REPL checking the value. Tom saw that specs let the system guard against bad data, no guessing allowed.'
            )),
        _ex("(do (require '[clojure.spec.alpha :as s]) "
            "(s/valid? string? 42))", False,
            "(s/valid? string? 42)",
            "whether 42 conforms to the string? spec",
            scenario=(
                "Carol wrote another rule: this field must be a string, not a number."
            ),
            need=(
                "Tom needed to see that specs would reject values that did not fit."
            ),
            mapping=(
                "`(s/valid? string? 42)` asks if 42 is a string. The REPL returns "
                "false, because 42 is a number, not a string."
            ),
            resolution=(
                "The form showed the REPL rejecting the bad value. Tom understood: specs were the townsfolk's way of writing rules the runtime enforced."
            )),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-07 — Spec generators
G12_07 = SubjectCurriculum(
    grade=12, subject_id="G12-07",
    subject_title="Spec generators",
    fable="boy-wolf",
    examples=[
        _ex('(do "s/exercise produces sample inputs for a spec" :studied)',
            ":studied",
            "what s/exercise does",
            "the marker for the spec-generators lesson",
            scenario=(
                "Carol had written many specs over the season. Now she showed Tom "
                "how to ask the REPL to generate test data automatically."
            ),
            need=(
                "Tom had always hand-written test cases. Carol wanted him to see "
                "that specs could generate test data without guessing."
            ),
            mapping=(
                "`s/exercise` takes a spec and produces sample values that conform "
                "to it. No hand-written test cases needed — the spec generates them."
            ),
            resolution=(
                'The form showed the REPL generating diverse test inputs. Tom understood: specs did double duty — both validation and test data. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'         )),
        _ex('(do "spec generators turn specs into property-based test inputs" :gens)',
            ":gens",
            "the role of spec generators",
            "the marker keyword for spec generators",
            scenario=(
                "By season's end, Tom saw that test.check relied on spec generators "
                "to explore many cases at once."
            ),
            need=(
                "Carol explained that generators turned specs into test inputs, "
                "letting property tests run broadly."
            ),
            mapping=(
                "A spec generator is a routine that produces values matching the "
                "spec. Property tests feed these generated inputs to check if a "
                "property holds for all of them."
            ),
            resolution=(
                'Tom finally grasped the pattern: specs were the foundation; generators made tests powerful. Together they protected the code. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'
            )),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-08 — clojure.test
G12_08 = SubjectCurriculum(
    grade=12, subject_id="G12-08",
    subject_title="clojure.test",
    fable="boy-wolf",
    examples=[
        # We can demonstrate the boolean essence of an assertion via =.
        _ex("(= (+ 1 2) 3)", True,
            "(= (+ 1 2) 3) — what an `is` would test",
            "the truth value an `is` assertion would record",
            scenario=(
                "Carol had filled her log-book with test routines all season. Now "
                "she showed Tom the simplest form: an equality check."
            ),
            need=(
                "Tom always guessed at whether his code worked. Carol wanted him to "
                "write tests that the REPL could run and confirm."
            ),
            mapping=(
                "An assertion is a form that evaluates to true or false, testing a claim about the code."
            ),
            resolution=(
                'The form returned the verdict. The REPL confirmed the math. Tom saw that tests were claims the runtime could verify. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'
            )),
        _ex('(do "(deftest …), (is …), (testing …) are the core test forms" :studied)',
            ":studied",
            "the clojure.test core forms",
            "the marker for the clojure.test lesson",
            scenario=(
                "Carol showed Tom the three main forms the valley used for tests: "
                "deftest, is, and testing."
            ),
            need=(
                "Tom needed to understand how these forms worked together to build "
                "a complete test suite."
            ),
            mapping=(
                "`deftest` names a test routine. `is` is an assertion inside it. "
                "`testing` groups related assertions with a description. All three "
                "are the pattern the village follows."
            ),
            resolution=(
                'The form showed each piece in place. Tom understood the pattern: tests were named, grouped, and asserted — structure that helped. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'         )),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-09 — Test fixtures
G12_09 = SubjectCurriculum(
    grade=12, subject_id="G12-09",
    subject_title="Test fixtures",
    fable="boy-wolf",
    examples=[
        _ex('(do "(use-fixtures :each f) wraps every deftest in setup/teardown" :studied)',
            ":studied",
            "use-fixtures and the fixture pattern",
            "the marker for the fixtures lesson",
            scenario=(
                "Carol's test suite had grown large. Many tests needed the same "
                "setup before running. She showed Tom how to use fixtures."
            ),
            need=(
                "Tom had hand-written setup code into each test, duplicating the "
                "work. Carol wanted him to see that fixtures made this automatic."
            ),
            mapping=(
                "`use-fixtures :each` wraps every test with setup and teardown "
                "routines. The same preparation runs before each test, no "
                "duplication."
            ),
            resolution=(
                'The form showed fixtures working. Tom understood: common setup belonged in fixtures, not scattered through the tests. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'
            )),
        _ex('(do "fixtures provide setup/teardown around deftests" :fixtures)',
            ":fixtures",
            "the purpose of fixtures",
            "the marker keyword for the fixture lesson",
            scenario=(
                "By season's end, Tom had written many fixtures. They all followed "
                "the same pattern: prepare, run, clean up."
            ),
            need=(
                "Carol explained that this pattern — setup, test, teardown — was so "
                "common that the watchhouse had made it a named tool."
            ),
            mapping=(
                "A fixture is a routine that runs before a test (setup) and after "
                "(teardown). The test runs in between, with everything ready."
            ),
            resolution=(
                'Tom finally grasped the value: fixtures meant tests could assume clean state, and cleanup happened without asking. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-10 — Property-based testing
G12_10 = SubjectCurriculum(
    grade=12, subject_id="G12-10",
    subject_title="Property-based testing",
    fable="boy-wolf",
    examples=[
        # A property: reverse of reverse equals identity. We check it once
        # to model what a property test would do generically.
        _ex("(= (reverse (reverse [1 2 3])) [1 2 3])", True,
            "the property that double-reverse is identity",
            "the truth value of the double-reverse property on [1 2 3]",
            scenario=(
                "Carol taught Tom about properties: claims that should be true "
                "for all inputs. Reverse of reverse should always equal identity."
            ),
            need=(
                "Tom had only hand-tested a few cases. Carol wanted him to see "
                "that properties could express universal rules."
            ),
            mapping=(
                "A property is a claim: 'reversing twice returns to the original.' "
                "The form `(= (reverse (reverse [1 2 3])) [1 2 3])` is one instance "
                "of this property."
            ),
            resolution=(
                'The form returned the verdict. Tom saw that properties were stronger than individual tests — they expressed invariants. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'         )),
        _ex('(do "test.check generates inputs and checks properties hold" :studied)',
            ":studied",
            "what test.check does",
            "the marker for property-based testing",
            scenario=(
                "By season's end, Tom used test.check to explore properties "
                "automatically. The library generated hundreds of test cases."
            ),
            need=(
                "Carol showed him that hand-writing all those cases was impossible. "
                "Test.check could generate them from specs."
            ),
            mapping=(
                "`test.check` is a library that generates random inputs, runs a "
                "property against each, and reports which inputs failed."
            ),
            resolution=(
                'Tom saw properties tested against hundreds of inputs. Test.check found edge cases he had never thought to check by hand. Tom chalked {drawn.a} on the meadow folk notice, and the morning record stood for the next shepherd to read.'
            )),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-11 — Leiningen project.clj
G12_11 = SubjectCurriculum(
    grade=12, subject_id="G12-11",
    subject_title="Leiningen project.clj",
    fable="boy-wolf",
    examples=[
        _ex('(do "project.clj declares :dependencies, :main, :profiles for Leiningen" :studied)',
            ":studied",
            "the project.clj manifest for Leiningen",
            "the marker for the project.clj lesson",
            scenario=(
                "The village had long built projects with Leiningen. Carol reviewed "
                "the project.clj file with Tom, showing him each field."
            ),
            need=(
                "Tom had always guessed what each field did. Carol wanted him to "
                "read the manifest and understand the tool's expectations."
            ),
            mapping=(
                "`project.clj` declares dependencies (libraries needed), :main "
                "(the entry point), and :profiles (variant builds). Leiningen reads "
                "this file at the project root."
            ),
            resolution=(
                'Tom saw how each field affected the build. Leiningen used the manifest to fetch libraries, run tests, and build packages. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'
            )),
        _ex('(do "Leiningen reads project.clj at the project root" :lein)',
            ":lein",
            "where Leiningen finds project.clj",
            "the marker keyword for the Leiningen lesson",
            scenario=(
                "By season's end, Tom had created many projects with Leiningen. "
                "He always put project.clj at the root, as the townsfolk required."
            ),
            need=(
                "Carol explained that Leiningen always looked for project.clj at "
                "the top level — no searching, no guessing."
            ),
            mapping=(
                "Leiningen's convention is simple: project.clj lives at the root. "
                "When you run `lein` commands, it reads this file first."
            ),
            resolution=(
                'Tom understood: follow the convention, put the file where Leiningen expects it, and the tool finds your project. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'
            )),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-12 — deps.edn projects
G12_12 = SubjectCurriculum(
    grade=12, subject_id="G12-12",
    subject_title="deps.edn projects",
    fable="boy-wolf",
    examples=[
        _ex('(do "deps.edn declares :deps and :aliases for the Clojure CLI" :studied)',
            ":studied",
            "the deps.edn manifest for the Clojure CLI",
            "the marker for the deps.edn lesson",
            scenario=(
                "The Clojure CLI had brought a new way to build projects. Carol "
                "showed Tom the deps.edn file, simpler than project.clj."
            ),
            need=(
                "Tom had been building with Leiningen. Carol wanted him to see "
                "that deps.edn offered a lighter alternative."
            ),
            mapping=(
                "`deps.edn` declares :deps (dependencies) and :aliases (named "
                "command shortcuts). The Clojure CLI reads this file instead of "
                "project.clj."
            ),
            resolution=(
                'Tom saw that deps.edn was smaller, data-driven. The official tools used it. He started to prefer it for simple projects. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'
            )),
        _ex('(do "deps.edn is read by the official `clj`/`clojure` tools" :deps)',
            ":deps",
            "who reads deps.edn",
            "the marker keyword for the deps.edn lesson",
            scenario=(
                "By season's end, Tom ran `clj` and `clojure` commands every day. "
                "Each one read deps.edn first."
            ),
            need=(
                "Carol explained that the official Clojure tools expected deps.edn "
                "at the root, just as Leiningen expected project.clj."
            ),
            mapping=(
                "The `clj` and `clojure` commands are the official tools. They read "
                "deps.edn and use it to resolve dependencies and run code."
            ),
            resolution=(
                'Tom understood: conventions again. Put deps.edn at the root, and the official tools find it and use it. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'
            )),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-13 — Aliases and tools
G12_13 = SubjectCurriculum(
    grade=12, subject_id="G12-13",
    subject_title="Aliases and tools",
    fable="boy-wolf",
    examples=[
        _ex('(do "`clj -M:test` runs the :test alias from deps.edn" :studied)',
            ":studied",
            "the alias-execution pattern with the Clojure CLI",
            "the marker for the aliases lesson",
            scenario=(
                "The village had written many small commands — one to run tests, "
                "another to build, another to check the lint. Carol showed Tom how "
                "aliases made this simple."
            ),
            need=(
                "Tom had always hand-typed long commands. Carol wanted him to "
                "define named aliases and run them with a short flag."
            ),
            mapping=(
                "`clj -M:test` runs the :test alias from deps.edn. The `-M:` flag "
                "says 'run this alias.' Aliases can include paths, dependencies, "
                "and options."
            ),
            resolution=(
                'Tom defined a few aliases and ran them. Commands became simple: `clj -M:test`, `clj -M:lint`. The complexity hid in deps.edn. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'
            )),
        _ex('(do "aliases compose extra paths, deps, and main opts" :aliases)',
            ":aliases",
            "what aliases let you compose",
            "the marker keyword for the aliases lesson",
            scenario=(
                "By season's end, Tom's deps.edn had many aliases, each one "
                "composing its own paths and dependencies."
            ),
            need=(
                "Carol showed him that an alias could add extra libraries, change "
                "the classpath, or specify the main function — all in one place."
            ),
            mapping=(
                "An alias is a map in deps.edn. It can have :paths (extra "
                "directories), :extra-deps (extra libraries), and :main-opts "
                "(main function and arguments)."
            ),
            resolution=(
                'Tom saw that aliases were a way to compose command profiles: test alias with test libraries, build alias with build tools, each separate and named. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-14 — Pedestal / Ring brief
G12_14 = SubjectCurriculum(
    grade=12, subject_id="G12-14",
    subject_title="Pedestal / Ring (web stack brief)",
    fable="boy-wolf",
    examples=[
        _ex('(do "Ring models HTTP as request-map -> response-map" :studied)',
            ":studied",
            "the Ring HTTP-as-data abstraction",
            "the marker for the Ring lesson",
            scenario=(
                "Tom had finally built a web service. Carol showed him that Ring "
                "modeled the entire HTTP exchange as data: a map in, a map out."
            ),
            need=(
                "Tom expected magic HTTP handling. Carol wanted him to see it was "
                "just maps and functions."
            ),
            mapping=(
                "Ring treats HTTP as data: a request-map (with headers, body, "
                "URI) goes in; a response-map (with status, headers, body) comes "
                "out. Functions transform between them."
            ),
            resolution=(
                'Tom saw that Ring was elegantly simple. HTTP became Clojure data and functions. No magic, just the data abstraction working. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'
            )),
        _ex('(do "Pedestal layers interceptors over Ring for richer pipelines" :web)',
            ":web",
            "the Pedestal interceptor model",
            "the marker keyword for the Pedestal lesson",
            scenario=(
                "For bigger services, Carol introduced Pedestal, which built on Ring "
                "with a more structured pipeline."
            ),
            need=(
                "Tom's Ring handlers were getting complicated. Pedestal's "
                "interceptors offered a way to compose middleware cleanly."
            ),
            mapping=(
                "An interceptor is a stage in a pipeline: it can modify the request "
                "before the handler, or the response after. Interceptors compose "
                "cleanly into queues."
            ),
            resolution=(
                'Tom built a Pedestal service and saw that interceptors gave structure. Logging, auth, routing — each interceptor had one job. Tom chalked {drawn.a} on the village notice, and the morning record stood for the next shepherd to read.'         )),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-15 — Datomic / XTDB brief
G12_15 = SubjectCurriculum(
    grade=12, subject_id="G12-15",
    subject_title="Datomic / XTDB (datalog db brief)",
    fable="boy-wolf",
    examples=[
        _ex('(do "Datomic and XTDB are immutable, time-aware datalog DBs" :studied)',
            ":studied",
            "the Datomic / XTDB family",
            "the marker for the datalog-DB lesson",
            scenario=(
                "Late in the season, Carol introduced Tom to a different kind of "
                "database: Datomic and XTDB, which treated data as immutable and "
                "time-aware."
            ),
            need=(
                "Tom was used to tables and rows. Carol wanted him to see that "
                "Datomic modeled facts with timestamps and history."
            ),
            mapping=(
                "Datomic and XTDB are datalog databases. They store facts as "
                "immutable tuples. Every fact has a timestamp, so you can query "
                "the database as it was at any point in time."
            ),
            resolution=(
                'Tom saw that this design meant no DELETE or UPDATE; only add new facts. History was preserved. The REPL showed the power: querying at any point in time. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'
            )),
        _ex('(do "queries are written in datalog over EDN-shaped data" :datalog)',
            ":datalog",
            "how queries look in these databases",
            "the marker keyword for datalog queries",
            scenario=(
                "Carol showed Tom how to write queries in datalog, a logic language "
                "that felt different from SQL."
            ),
            need=(
                "Tom expected SQL syntax. Datalog worked with facts and rules, "
                "written as Clojure data."
            ),
            mapping=(
                "Datalog queries are written as vectors and maps — plain EDN. "
                "You specify which facts to find, with variables and patterns. The "
                "database matches them against stored facts."
            ),
            resolution=(
                "Tom wrote a datalog query and saw it match multiple facts. The query felt logical, not procedural. By season's end, he understood its power. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then."
            )),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-16 — Reagent brief
G12_16 = SubjectCurriculum(
    grade=12, subject_id="G12-16",
    subject_title="Reagent (cljs UI brief)",
    fable="boy-wolf",
    examples=[
        _ex('(do "Reagent wraps React with Hiccup-shaped Clojure data" :studied)',
            ":studied",
            "the Reagent wrapper around React",
            "the marker for the Reagent lesson",
            scenario=(
                "Tom had finally moved to the browser. Carol showed him Reagent, "
                "which brought Clojure data thinking to React UI building."
            ),
            need=(
                "Tom expected HTML and JavaScript. Carol wanted him to see that "
                "Reagent modeled UIs as Clojure data."
            ),
            mapping=(
                "Reagent wraps React with Hiccup, a Clojure syntax for HTML. "
                "Instead of JSX, you write nested vectors representing the DOM. "
                "Reagent handles the React plumbing."
            ),
            resolution=(
                'Tom wrote a Reagent component and saw it in the browser. The form was pure Clojure data. React worked underneath, but he never saw it. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'
            )),
        _ex('(do "components are functions returning Hiccup vectors" :reagent)',
            ":reagent",
            "how Reagent components are written",
            "the marker keyword for Reagent components",
            scenario=(
                "Carol showed Tom how simple Reagent components were: functions "
                "that returned data describing the UI."
            ),
            need=(
                "Tom expected complex classes and lifecycle methods. Reagent's "
                "functions were simpler."
            ),
            mapping=(
                "A Reagent component is a function that returns a Hiccup vector. "
                "The vector has a tag (like :div), attributes (like {:class "
                "\"foo\"}), and children. Reagent turns this into React components."
            ),
            resolution=(
                "Tom wrote many simple components. Each was a function. React handled updates. By season's end, he could build whole UIs this way. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear."
            )),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-17 — Library design patterns
G12_17 = SubjectCurriculum(
    grade=12, subject_id="G12-17",
    subject_title="Library design patterns",
    fable="boy-wolf",
    examples=[
        _ex('(do "good libraries expose data, then functions, then macros sparingly" :studied)',
            ":studied",
            "the Clojure library-design hierarchy",
            "the marker for the library-design lesson",
            scenario=(
                "By the season's end, Tom had written a library. Carol reviewed it "
                "with him: what was the public API? How much machinery was exposed?"
            ),
            need=(
                "Tom had wanted to show off every clever trick. Carol wanted him to "
                "see that good libraries hid complexity."
            ),
            mapping=(
                "The Clojure design pattern is a hierarchy: expose data first "
                "(dicts, maps, seqs), then functions that operate on that data, "
                "then macros only when they simplify the user's code."
            ),
            resolution=(
                'Tom refactored his library to follow the pattern. The API became smaller, clearer. Users liked it better. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'
            )),
        _ex('(do "small public API surface, plain data inputs, return values" :design)',
            ":design",
            "the conventional Clojure API shape",
            "the marker keyword for the API-shape lesson",
            scenario=(
                "Carol showed Tom the libraries the meadow folk used most. Every one "
                "had a small, focused API."
            ),
            need=(
                "Tom's first library had tried to do everything. Carol wanted him to "
                "see that constraints made designs better."
            ),
            mapping=(
                "A small API surface means: few public functions, they take plain "
                "data (maps, seqs) as input, they return plain data. No custom "
                "objects, no magic. Easy to test, compose, and understand."
            ),
            resolution=(
                "Tom's second library was half the size and twice as useful. The village adopted it because it was predictable. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last."
            )),
        _ex("(= [1 2 3] (vec '(1 2 3)))", True,
            "a tiny example of a data-first conversion at the API edge",
            "whether the vector and the converted seq are equal",
            scenario=(
                "Carol showed Tom this small example: a function converting a list "
                "to a vector. Plain data in, plain data out."
            ),
            need=(
                "This is the API shape the valley trusted: no wrappers, no objects, "
                "just the data transformation."
            ),
            mapping=(
                "`vec` takes any seq-like thing and returns a vector. It works "
                "because Clojure data structures are predictable. Users know exactly "
                "what they get."
            ),
            resolution=(
                'Tom saw the power: libraries that work with plain data are easier to use, test, and compose with other code (with `1` as the input value) (with `3` as the input value).'
            )),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G12,
)


# G12-18 — Clojure style guide
G12_18 = SubjectCurriculum(
    grade=12, subject_id="G12-18",
    subject_title="Clojure style guide",
    fable="boy-wolf",
    examples=[
        _ex('(do "kebab-case names, two-space indent, threading for deep nests" :studied)',
            ":studied",
            "the community-style basics",
            "the marker for the style-guide lesson",
            scenario=(
                "The season had nearly ended. Carol and Tom reviewed the code Tom "
                "had written. They checked it against the valley's style guide."
            ),
            need=(
                "Tom had written names in camelCase, indented with four spaces. "
                "Carol wanted him to see the village's standard conventions."
            ),
            mapping=(
                "Clojure style: kebab-case names (like my-function), two-space "
                "indent, and threading operators (-> and ->>) for deep nesting. "
                "These make code readable to every shepherd in the watchhouse."
            ),
            resolution=(
                "Tom reformatted his code to match the guide. It looked cleaner. By season's end, he wrote in style without thinking. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand."
            )),
        _ex('(do "prefer pure functions, name predicates with ?, danger! ops with !" :style)',
            ":style",
            "two naming conventions from the style guide",
            "the marker keyword for the naming-conventions lesson",
            scenario=(
                "Carol pointed to Tom's function names and asked: which ones were "
                "pure? Which ones changed state?"
            ),
            need=(
                "Tom had mixed conventions. Carol wanted him to name functions "
                "clearly so readers knew the cost of calling them."
            ),
            mapping=(
                "By convention: predicates (functions returning true/false) end "
                "with ?. Functions with side effects or dangers end with !. This "
                "warns readers: be careful, this one changes something."
            ),
            resolution=(
                'Tom renamed his functions. Now a reader could glance at the name and know: this one just reads data, this one might change it. The naming was its own documentation. Tom chalked {drawn.a} on the watchhouse notice, and the morning record stood for the next shepherd to read.'
            )),
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
    print(f"grade-12 boy-wolf smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
