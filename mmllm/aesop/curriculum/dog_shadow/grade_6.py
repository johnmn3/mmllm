"""Grade 6 — namespaces and modular code. Through dog-shadow.

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
from mmllm.aesop.curriculum.dog_shadow.grade_1 import (
    _GOAL_SUBPLOTS, _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL
)
from mmllm.aesop.curriculum.dog_shadow._metaphor_pools import (
    _ROADSIGN_SUBPLOTS, _SCROLL_SUBPLOTS, _TOOLSHED_SUBPLOTS,
)


_NS_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    # Two characters at separate workbenches, exchanging a labeled form.
    SubplotTemplate("""\
{tortoise}, {emo_patient} kept a small workbench {place}, where every form had
its own labeled drawer. {hare_phrase} preferred to scribble each
expression in a single notebook. To settle a question that morning,
{tortoise} pointed to {concept_phrase} and asked {hare} to evaluate the
form {form_display} so they could see what name belonged with what
value."""),

    # The "two cottages" / cross-namespace beat.
    SubplotTemplate("""\
The two of them lived in cottages on opposite sides {place} —
{tortoise} on one side, {hare_phrase} on the other. Each kept
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
    subject_title="Namespace as file", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(name 'foo.bar)",
            expected="foo.bar",
            concept_phrase="extracting the string form of a namespace symbol",
            question_what="the string form of a quoted namespace symbol",
            goal_text="extract the string form of a quoted namespace symbol",
            scenario=(
                'Patch the hound examined a marker stone at the stream\'s edge '
                'with a strange dotted path scratched into it — foo.bar. '
                '{hound_he_she} wanted to read what the scratch said without '
                'using the path itself as a name.'
            ),
            need=(
                'Could {hound_he_she} pull the string text from the symbol, '
                'so any other dog could read the plain characters that made it?'
            ),
            mapping=(
                'The symbol is the scratch on the stone, the string extraction '
                'is the reading of what was marked there, and the name function '
                'is the act of tracing the characters in order.'
            ),
            resolution=(
                'The REPL read the scratch and handed back the plain string '
                'that foo.bar spelled out, without any symbolic wrapping left.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(name 'clojure.string)",
            expected="clojure.string",
            concept_phrase="extracting the string form of a namespace symbol",
            question_what="the string form of a quoted namespace symbol",
            goal_text="extract the string form of a quoted namespace symbol",
            scenario=(
                'Further upstream, Patch found another stone marker with a longer, '
                'multi-segment path scratched in — a well-known location where '
                'other dogs had cached their scrolls.'
            ),
            need=(
                'She wanted to extract the plain string name that the marker '
                'spelled, to read where the cache lay.'
            ),
            mapping=(
                'Like the first stone, this marker holds a symbol; the name '
                'function traces the same characters and returns them as plain text.'
            ),
            resolution=(
                'The REPL extracted the plain-text path from the symbol and handed '
                'it back — a path any dog could follow upstream — clojure.string.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(symbol? 'tortoise.race)",
            expected=True,
            concept_phrase="checking whether a value is a symbol",
            question_what="whether a value is a symbol",
            goal_text="test whether a quoted namespace-like value is a symbol",
            scenario=(
                'Bell the hound stood at the bank and studied a new scratch on a '
                'nearby stone — tortoise.race, marked with the faint paw-print of '
                'a stranger. She needed to know: was this a proper symbol that '
                'named a location, or something else entirely?'
            ),
            need=(
                'She wanted the runtime\'s word on whether this mark was truly a '
                'symbol that could serve as a name.'
            ),
            mapping=(
                'The scratch on the stone is the quoted value, the symbol-predicate '
                'is the verification, and the verdict is whether it qualifies as a '
                'proper name the pack could use.'
            ),
            resolution=(
                'The REPL checked the mark and returned tortoise.race — the stone\'s scratch '
                'was indeed a symbol, and the location it named was real.'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-02 — ns form (we exercise via `name *ns*` style introspection)
G6_02 = SubjectCurriculum(grade=6, subject_id="G6-02",
    subject_title="ns form", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(name 'race.tortoise)",
            expected="race.tortoise",
            concept_phrase="extracting the string form of a namespace symbol",
            question_what="the string form of a quoted namespace symbol",
            goal_text="extract the string form of a quoted namespace symbol",
            scenario=(
                'Rex the hound approached a stone marker near the meadow that carried '
                'a familiar symbol scratched into its face — race.tortoise. It was a '
                'place he had visited many times, but today he wanted the plain text '
                'of its name laid bare.'
            ),
            need=(
                'He needed to pull the string name from the symbol so he could speak '
                'it aloud to another dog without any marks or wrappings.'
            ),
            mapping=(
                'The symbol on the stone is the form, the act of extracting text is '
                'what the name function does, and the result is the pure string that '
                'the symbol names.'
            ),
            resolution=(
                'The REPL traced the symbol and handed back race.tortoise as plain '
                'text — the unmarked name any dog could read.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(= 'race.tortoise 'race.tortoise)",
            expected=True,
            concept_phrase="checking equality of two namespace symbols",
            question_what="whether two identical namespace symbols are equal",
            goal_text="test whether two identical namespace symbols are equal",
            scenario=(
                'Later, Rex stood before the same marker and saw the symbol '
                'race.tortoise scratched twice on adjacent stones. Were these two '
                'scratches truly the same, or had the second dog marked something '
                'slightly different?'
            ),
            need=(
                'He wanted the runtime\'s word on whether both stones bore the exact '
                'same mark.'
            ),
            mapping=(
                'The two symbol-markers are the operands of the test, and the equality '
                'predicate asks: do these two scratches match perfectly?'
            ),
            resolution=(
                'The REPL compared the marks and returned race.tortoise — both stones carried '
                'the identical symbol, and the locations they named were the same.'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-03 — require — fully qualified usage (require already loaded
# clojure.string in basilisp/clojure runtime; the form below works in
# both).
G6_03 = SubjectCurriculum(grade=6, subject_id="G6-03",
    subject_title="require", fable="dog-shadow",
    examples=[
        SubjectExample(
            form='(clojure.string/upper-case "hare")',
            expected="HARE",
            concept_phrase="calling a fully-qualified string function",
            question_what="the capitalized form returned by the upper-case routine on the scroll",
            goal_text="call the upper-case routine on the clojure.string scroll, applied to the four-letter string hare",
            scenario=(
                'Bell the hound found a scroll in the riverbank cache bearing the name '
                'clojure.string. A routine written there was called upper-case. She wanted '
                'to send the text "hare" through that routine and see what came back in '
                'a different form.'
            ),
            need=(
                'She needed to call the fully-qualified routine, naming both the scroll '
                'and the function, so the runtime could find the right tool.'
            ),
            mapping=(
                'The scroll clojure.string is the library, the upper-case function is the '
                'routine written there, and the text "hare" is the message to be transformed.'
            ),
            resolution=(
                'The REPL reached into the scroll, found the routine, and applied it to the '
                'text, handing back hare in capitalized form.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(clojure.string/lower-case "ZEBRA")',
            expected="zebra",
            concept_phrase="calling a fully-qualified string function",
            question_what="the lowercase form of the string ZEBRA produced by clojure.string/lower-case",
            goal_text="call the lowercasing function from clojure.string on a test string",
            scenario=(
                'Nearby, another scroll lay open with a lower-case routine marked in its '
                'margin. Bell wanted to send the text "ZEBRA" through that transformation, '
                'also reaching into the clojure.string scroll to find the function.'
            ),
            need=(
                'Using the fully-qualified path again, she would invoke the lowercasing '
                'routine and see what form the text would take.'
            ),
            mapping=(
                'Like the first example, this uses the same library and its routines — the '
                'scroll clojure.string, the function lower-case, and the input text "ZEBRA".'
            ),
            resolution=(
                'The REPL applied the lowercasing function and returned the text in plain '
                'lowercase form — ZEBRA.'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-04 — refer-and-use (we exercise the effect: a referred name
# resolves the same as the qualified name; via `=` we compare two
# applications).
G6_04 = SubjectCurriculum(grade=6, subject_id="G6-04",
    subject_title="refer and use", fable="dog-shadow",
    examples=[
        SubjectExample(
            form='(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))',
            expected=True,
            concept_phrase="testing equality of two identical function calls",
            question_what="whether two calls to the same function with the same argument produce the same result",
            goal_text="test whether two calls to the fully-qualified string uppercasing function with the same argument are equal",
            scenario=(
                'Rex stood at the stream bank and performed an experiment: he called the '
                'same fully-qualified function twice with the same input — the single '
                'character "x" — and watched what came back both times.'
            ),
            need=(
                'Would the two applications produce identical results, or would the '
                'runtime give different answers?'
            ),
            mapping=(
                'Each call to clojure.string/upper-case with "x" is a separate invocation, '
                'and the equality test compares what both applications returned.'
            ),
            resolution=(
                'The REPL executed both calls, received the same result from each, and returned true — proving the routine was consistent and reliable (with `) (clojure.string/upper-case ` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-05 — Fully qualified names
G6_05 = SubjectCurriculum(grade=6, subject_id="G6-05",
    subject_title="Fully qualified names", fable="dog-shadow",
    examples=[
        SubjectExample(
            form='(clojure.string/upper-case "hello")',
            expected="HELLO",
            concept_phrase="calling a fully-qualified string function",
            question_what="the uppercase form of the string hello produced by clojure.string/upper-case",
            goal_text="call the uppercasing function from clojure.string on a test string",
            scenario=(
                'Patch the hound found another scroll in the bank cache carrying the '
                'upper-case routine. She wanted to send the greeting "hello" through that '
                'transformation, using the complete name clojure.string/upper-case.'
            ),
            need=(
                'She needed to call the fully-qualified routine, giving both the scroll '
                'and the function name so the runtime could find and apply it.'
            ),
            mapping=(
                'The scroll clojure.string holds the library, the upper-case function is '
                'the tool there, and "hello" is the text to be changed.'
            ),
            resolution=(
                'The REPL found the routine in the scroll and applied it, returning the '
                'greeting in capitalized form — hello.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(clojure.string/reverse "abc")',
            expected="cba",
            concept_phrase="calling a fully-qualified string function",
            question_what="the reversed form of the string abc produced by clojure.string/reverse",
            goal_text="call the reversing function from clojure.string on a test string",
            scenario=(
                'Continuing her search of the scrolls, Patch found another routine in the '
                'clojure.string cache — a reverse function. She wanted to send the sequence '
                '"abc" through it, again using the full path to reach the tool.'
            ),
            need=(
                'Using the fully-qualified name, she would reverse the text and see the '
                'result the routine produced.'
            ),
            mapping=(
                'Like the first example, the scroll and function are fully named, the input '
                'is the text "abc", and the runtime will apply the transformation.'
            ),
            resolution=(
                'The REPL executed the reverse function and returned the sequence in '
                'opposite order — abc.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(namespace :owner/item)",
            expected="owner",
            concept_phrase="extracting the namespace portion of a keyword",
            question_what="the namespace part of a qualified keyword",
            goal_text="extract the namespace portion of a qualified keyword",
            scenario=(
                'At the forest edge, Bell found a marker with a qualified keyword written '
                'there — :owner/item. The mark had two parts separated by a slash, and she '
                'wondered what lay before the separator.'
            ),
            need=(
                'She wanted to extract just the namespace portion — the first part — so '
                'she could identify whose cache this belonged to.'
            ),
            mapping=(
                'The qualified keyword :owner/item has two slots: the namespace before the '
                'slash and the name after it. The namespace function reads just the first part.'
            ),
            resolution=(
                'The REPL extracted the namespace portion and handed back owner, showing '
                'which part of the cache this marker belonged to.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(name :owner/item)",
            expected="item",
            concept_phrase="extracting the name portion of a keyword",
            question_what="the name part of a qualified keyword",
            goal_text="extract the name local portion of a qualified keyword",
            scenario=(
                'Looking at the same marker :owner/item, Bell now wanted the other half — '
                'the local name after the slash, to see what kind of thing the owner had stored.'
            ),
            need=(
                'She wanted to pull the name portion from the qualified keyword.'
            ),
            mapping=(
                'While the namespace function reads the first part, the name function reads '
                'the second part — the local name that follows the slash.'
            ),
            resolution=(
                'The REPL extracted the name portion and handed back item, the final part '
                'of the qualified mark — owner.'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-06 — Private defs (we can't test ^:private effect with eval, but
# we can confirm related metadata predicates).
G6_06 = SubjectCurriculum(grade=6, subject_id="G6-06",
    subject_title="Private defs", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(:private (meta '^:private x))",
            expected=True,
            concept_phrase="accessing the :private flag from metadata",
            question_what="whether the :private metadata is set on a symbol",
            goal_text="check whether the :private flag is present in the metadata of a symbol with :private marker",
            scenario=(
                'Rex the hound found a bone marked with symbols scratched along its length. '
                'The first symbol bore a special rope attached to it marked :private — a sign '
                'that this symbol was meant only for dogs who knew the cache. {hound_he_she} wanted '
                'to check the metadata and confirm the flag was there.'
            ),
            need=(
                'He needed to extract the metadata from the marked symbol and see if the '
                ':private flag had been set.'
            ),
            mapping=(
                'The symbol with its attached rope is the input, the meta function reads the '
                'attached markers, and looking up the :private key tells whether the symbol is '
                'restricted.'
            ),
            resolution=(
                'The REPL checked the metadata and returned true — the :private flag was '
                'indeed attached, marking this symbol as private.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(:private (meta 'x))",
            expected=None,
            concept_phrase="accessing the :private flag from metadata",
            question_what="whether the :private metadata is set on a plain symbol",
            goal_text="check whether the :private flag is present in the metadata of a plain symbol without markers",
            scenario=(
                "Next, she looked at a plain symbol — just 'x, with no markers or ropes "
                "attached. She wanted to check whether this one carried the :private flag."
            ),
            need=(
                "Did this plain symbol have any metadata at all? And if it did, "
                "was the :private flag there?"
            ),
            mapping=(
                "A plain symbol without markers has no metadata, so when you ask "
                "for the :private flag, the runtime returns nothing — a nil — "
                "because there's nothing to find."
            ),
            resolution=(
                "the runtime returned nothing, confirming that the plain symbol "
                "had no :private flag attached."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-07 — Public vs private API (design decision; we exercise via
# the predicate `:private` on metadata).
G6_07 = SubjectCurriculum(grade=6, subject_id="G6-07",
    subject_title="Public vs private API", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(boolean (:private (meta '^:private hidden)))",
            expected=True,
            concept_phrase="converting the :private metadata to a boolean",
            question_what="whether a symbol with :private marker evaluates to true when converted to boolean",
            goal_text="convert the :private metadata flag of a symbol marked with :private to a boolean",
            scenario=(
                'Bell stood at the pond edge with a bone marked with a private symbol — one '
                'with the :private rope tied tight. She wanted to test whether that flag, when '
                'extracted and converted to a simple yes-or-no answer, would tell her true.'
            ),
            need=(
                'Using the boolean conversion, she needed to see if the :private flag would '
                'become true when evaluated as a single verdict.'
            ),
            mapping=(
                'The symbol with its private rope carries the metadata, the extraction pulls '
                'the flag, and the boolean conversion gives a clear true-or-false answer.'
            ),
            resolution=(
                'The REPL extracted the flag, converted it to a boolean, and returned true — '
                'confirming the symbol was indeed marked as private.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(boolean (:private (meta 'public)))",
            expected=False,
            concept_phrase="converting the :private metadata to a boolean",
            question_what="whether a symbol without :private marker evaluates to false when converted to boolean",
            goal_text="convert the :private metadata flag of a plain symbol to a boolean",
            scenario=(
                "Now she did the same with a plain symbol 'public — no markers, no ropes. "
                "She wanted to test it the same way: extract the :private flag and convert "
                "to a boolean."
            ),
            need=(
                "Would the plain symbol's answer be true or false?"
            ),
            mapping=(
                "A plain symbol has no metadata, so there's no :private flag to find — "
                "the extraction returns nil. When nil is converted to a boolean, it becomes false."
            ),
            resolution=(
                "the runtime returned public, because no flag was there at all."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-08 — Circular dependencies (we exercise via a plain form that
# would resolve correctly when the dependency graph is sound; the
# narrative carries the lesson).
G6_08 = SubjectCurriculum(grade=6, subject_id="G6-08",
    subject_title="Circular dependencies", fable="dog-shadow",
    examples=[
        SubjectExample(
            form='(clojure.string/upper-case "a")',
            expected="A",
            concept_phrase="calling a function from a required namespace",
            question_what="the uppercase form of the character a produced by clojure.string/upper-case",
            goal_text="call the string uppercasing function from clojure.string on the character a",
            scenario=(
                'Patch approached a familiar scroll at the forest edge — the clojure.string '
                'cache that had served many dogs. She wanted to use the upper-case routine one '
                'more time, this time on a single character "a".'
            ),
            need=(
                'She would reach fully-qualified across to the scroll and apply the routine, '
                'trusting the libraries were loaded in the right order.'
            ),
            mapping=(
                'The clojure.string scroll and its upper-case function stand ready, the '
                'dependency graph is sound, and the fully-qualified call reaches through with '
                'confidence.'
            ),
            resolution=(
                'The REPL found the routine, applied it to "a", and returned the uppercase '
                'result — proof the dependencies were in order.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(= 'a.b 'a.b)",
            expected=True,
            concept_phrase="testing equality of two namespace symbols",
            question_what="whether two identical namespace symbols are equal",
            goal_text="test whether two references to the same namespace symbol are equal",
            scenario=(
                'Rex found two marker stones side by side, both bearing the same scratched '
                'symbol — a.b. He wanted to verify that both marks were truly identical, that '
                'neither had been altered or miswritten.'
            ),
            need=(
                'The equality test would give him the runtime\'s verdict on whether the two '
                'symbols matched perfectly.'
            ),
            mapping=(
                'The two marker stones hold the symbol a.b, and the equality predicate checks '
                'whether the scratches are the same.'
            ),
            resolution=(
                'The REPL compared the symbols and returned a.b — both stones bore the exact '
                'same mark, and the locations they named were truly identical.'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-09 — Loading order (we exercise via straightforward sequence of
# forms inside a `do` so the REPL processes them in order).
G6_09 = SubjectCurriculum(grade=6, subject_id="G6-09",
    subject_title="Loading order", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(do (def step1 1) (def step2 (+ step1 1)) step2)",
            expected=2,
            concept_phrase="evaluating definitions in sequence to establish dependency order",
            question_what="the value of the second variable after both definitions are loaded in order",
            goal_text="define step1 as 1, then define step2 as step1 plus 1, then return step2",
            scenario=(
                'Bell stood at the stream with a plan: first she would scratch a marker stone '
                'and name it step1, giving it the value 1. Then she would scratch a second stone, '
                'step2, whose value would depend on the first stone — step1 plus 1.'
            ),
            need=(
                'The stones had to be marked in order, so that when step2\'s value was '
                'calculated, step1 would already be there to use.'
            ),
            mapping=(
                'The first def is the first marker scratched, the second def uses the first '
                'marker\'s value, and the sequence ensures loading order is respected.'
            ),
            resolution=(
                'The REPL marked the first stone, then marked the second using the first\'s '
                'value, and returned the second marker\'s value — the 1.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(let [a 1 b (+ a 1)] (+ a b))",
            expected=3,
            concept_phrase="establishing local bindings with dependent values",
            question_what="the sum of two variables with the second depending on the first",
            goal_text="bind a to 1, bind b to a plus 1, then return the sum of a and b",
            scenario=(
                'Patch picked up two small bones by the pond, ready to bind them to local names. '
                'The first bone she gripped and named a, holding its value of 1 between her teeth. '
                'The second bone she would call b, but its value would depend on a — she would add '
                '1 to whatever a held.'
            ),
            need=(
                'Both bones had to be gripped in the right order, so that when b\'s value was '
                'calculated, a would already be held.'
            ),
            mapping=(
                'The mouth holds both bones in sequence, the first binding a is set first, then '
                'the second binding b depends on a, and the form adds them together at the end.'
            ),
            resolution=(
                'The REPL gripped a at 1, then gripped b at a plus 1, and finally added both '
                'together, returning the running total.'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-10 — leiningen / deps.edn (project setup; we exercise via reading
# a small edn-shaped data structure that resembles a deps map).
G6_10 = SubjectCurriculum(grade=6, subject_id="G6-10",
    subject_title="Leiningen and deps.edn", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(:deps {:deps {:a 1 :b 2}})",
            expected={":a": 1, ":b": 2},
            concept_phrase="accessing a key from a nested map structure",
            question_what="the value at the :deps key in a deps-style map",
            goal_text="extract the value at the :deps key from a nested map",
            scenario=(
                "Bell the hound found a hollow-log cache at the stream's edge divided into nested compartments, each labeled with a keyword. The outer label read :deps, and inside that compartment lay another set of bones labeled :a and :b."
            ),
            need=(
                'She wanted to reach into the outer compartment and pull out what lay there — '
                'the inner cache with all its labeled bones.'
            ),
            mapping=(
                'The hollow-log cache is the outer map, the :deps key opens the first '
                'compartment, and what\'s stored there is a smaller cache with its own bones.'
            ),
            resolution=(
                'The REPL opened the outer compartment, reached in, and handed back the inner '
                'cache — still holding the bones labeled :a and :b.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(get-in {:paths ["src"]} [:paths 0])',
            expected="src",
            concept_phrase="accessing a nested value in a map using a path vector",
            question_what="the first element from a :paths vector in a deps-style map",
            goal_text="extract the first entry from the :paths vector in a deps-style map",
            scenario=(
                'Patch the hound examined a cache with a :paths label, inside which lay a vector '
                'of text entries pointing to directories. She wanted the first entry only.'
            ),
            need=(
                'Using a path vector — first the key :paths, then the index 0 — she would dig '
                'down to the exact bone she sought.'
            ),
            mapping=(
                'The cache holds a vector under the :paths key, the path vector is the digging '
                'sequence, and the first element is what the index 0 reaches.'
            ),
            resolution=(
                'The REPL followed the path down through both layers and handed back the first '
                'entry — the string "src".'
            ),
            tags=("story",),
        ),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-11 — Classpath (we use a tiny path-string operation as the
# eval-shaped exercise).
G6_11 = SubjectCurriculum(grade=6, subject_id="G6-11",
    subject_title="Classpath", fable="dog-shadow",
    examples=[
        SubjectExample(
            form='(clojure.string/split "src:test" #":")',
            expected=["src", "test"],
            concept_phrase="splitting a string by a delimiter",
            question_what="the vector of parts after splitting a colon-separated path string",
            goal_text="split a colon-separated classpath-like string into its individual entries",
            scenario=(
                'Rex the hound found a scratch-mark at the stream\'s edge that listed two paths bound together with a colon: "src:test". The path was a single long text, but it held two separate locations.'
            ),
            need=(
                'He needed to split the mark at the colon and separate it into two distinct '
                'paths so he could visit each location.'
            ),
            mapping=(
                'The scratch-mark is the string to be split, the colon is the boundary, and the '
                'split function from clojure.string is the knife that cuts at that boundary.'
            ),
            resolution=(
                'The REPL took the mark and cut it apart at the colon, handing back a vector of '
                'two separate paths — :.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(count ["src" "test" "resources"])',
            expected=3,
            concept_phrase="counting the number of elements in a vector",
            question_what="the number of entries in a classpath-like vector",
            goal_text="count the number of entries in a vector of classpath directories",
            scenario=(
                'Patch stood at the river bank and saw three paths scratched on a stone vector: '
                '"src", "test", and "resources". She needed to know: how many locations were '
                'listed there?'
            ),
            need=(
                'She would tally the paths in the vector to know how many directories were part '
                'of the classpath.'
            ),
            mapping=(
                'The vector holds three paths lined up, the count function walks the row, and the '
                'running tally tells how many entries lay inside.'
            ),
            resolution=(
                'The REPL counted the entries and returned the total — three directories on the '
                'classpath — resources.'
            ),
            tags=("story",),
        ),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-12 — Multiple files, one project (we exercise via a vector
# of namespace symbols).
G6_12 = SubjectCurriculum(grade=6, subject_id="G6-12",
    subject_title="Multiple files in one project", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(count ['race.tortoise 'race.hare 'race.shared])",
            expected=3,
            concept_phrase="counting the number of namespace symbols in a project",
            question_what="the number of namespaces in a small project",
            goal_text="count the number of namespace symbols in a vector of three namespaces",
            scenario=(
                'Bell the hound found a list of three locations scratched on a flat stone near '
                'the meadow — race.tortoise, race.hare, and race.shared. These three places '
                'were part of a single project, and she needed to count how many there were.'
            ),
            need=(
                'She wanted the precise count of the locations in the vector, so she would '
                'know how many files this project contained.'
            ),
            mapping=(
                'The vector holds the namespace symbols, and the count function tallies how '
                'many are there, giving the number of namespaces in the project.'
            ),
            resolution=(
                'The REPL counted the markers and returned the tally — three namespaces in '
                'this small project — race.shared.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(map name ['race.tortoise 'race.hare])",
            expected=["race.tortoise", "race.hare"],
            concept_phrase="extracting string names from namespace symbols",
            question_what="the vector of namespace names as strings",
            goal_text="extract the string form of each namespace symbol in a vector of two namespaces",
            scenario=(
                'Moving along the bank, Patch found a shorter list with just two namespace '
                'symbols — race.tortoise and race.hare. She wanted to extract the plain string '
                'form of each symbol in the vector.'
            ),
            need=(
                'She needed to transform the vector of symbols into a vector of their string '
                'names, so she could speak the paths aloud.'
            ),
            mapping=(
                'The map function applies the name extraction to each symbol in turn, creating '
                'a new vector of the extracted string forms.'
            ),
            resolution=(
                'The REPL mapped the name function over the symbols and returned a vector of '
                'strings — the plain text paths of both namespaces — race.hare.'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-13 — Aliasing conventions (we exercise via a tiny alias-style
# substitution that's purely lexical).
G6_13 = SubjectCurriculum(grade=6, subject_id="G6-13",
    subject_title="Aliasing conventions", fable="dog-shadow",
    examples=[
        SubjectExample(
            form='(let [s clojure.string/upper-case] (s "hare"))',
            expected="HARE",
            concept_phrase="aliasing a fully-qualified function and calling it through the alias",
            question_what="the uppercase form of the string hare when clojure.string/upper-case is called through a local alias",
            goal_text="bind the fully-qualified string uppercasing function to a local alias s and call it on hare",
            scenario=(
                'Rex the hound found the fully-qualified path to the clojure.string/upper-case '
                'function, but the long name was cumbersome for the next stretch of work. He '
                'gripped the function itself and gave it a short local alias — s — so he could '
                'call it quickly.'
            ),
            need=(
                'Using the short alias, he would apply the function to the text "hare" and '
                'get the result without writing out the full qualified name each time.'
            ),
            mapping=(
                'The binding grips the function from the scroll, the short name s is the alias '
                'held in the mouth, and calling s is the same as calling the original function.'
            ),
            resolution=(
                'The REPL bound the function to s, then applied it to "hare" through the '
                'alias, returning the uppercase result.'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-14 — Import for Java classes (basilisp targets Python; we use a
# universally-available form here: predicate on a class-y name).
G6_14 = SubjectCurriculum(grade=6, subject_id="G6-14",
    subject_title="Import for host classes", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(symbol? 'java.util.List)",
            expected=True,
            concept_phrase="testing whether a value is a symbol",
            question_what="whether a dotted Java class name is a symbol",
            goal_text="test whether a Java class name written as a quoted symbol is a symbol",
            scenario=(
                "Bell the hound stopped beside the kennel-master's shed "
                'near the pond. On a peg hung an unfamiliar tool — a '
                "host-side label scratched in the kennel-master's hand, "
                'written as if it were a path.'
            ),
            need=(
                "She wanted only the runtime's verdict on what kind of mark "
                'the label was — a name the dogs could quote, or something '
                'else — without trying to use the tool itself.'
            ),
            mapping=(
                'The label on the peg is the quoted Java class name, the '
                "runtime is the kennel-master's bridge, and the "
                'symbol-predicate is the question of which kind of mark '
                'this is, answered without invoking the host tool.'
            ),
            resolution=(
                'The REPL read the mark, applied the predicate, and handed '
                'back the java.util.List. The tool itself stayed on its peg — only '
                'its label had been examined.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(name 'java.util.Map)",
            expected="java.util.Map",
            concept_phrase="extracting the string form of a class symbol",
            question_what="the string form of a Java class symbol",
            goal_text="extract the string form of a Java class symbol",
            scenario=(
                'Patch returned to the kennel-master\'s shed where another tool hung on a peg — '
                'this one labeled with a long, dotted Java class name. She wanted to '
                'extract the plain text of that host-side label and read it aloud.'
            ),
            need=(
                'She would pull the string form from the quoted class name so she could speak '
                'the exact path the kennel-master used.'
            ),
            mapping=(
                'The Java class symbol is a mark the kennel-master left, and the name function '
                'extracts the string text that the mark carries.'
            ),
            resolution=(
                'The REPL traced the label and handed back the plain-text class path the '
                'kennel-master had used — java.util.Map.'
            ),
            tags=("story",),
        ),
    ], subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-15 — Namespace meta (we exercise the metadata mechanism on a
# symbol via `^{:doc ...}`).
G6_15 = SubjectCurriculum(grade=6, subject_id="G6-15",
    subject_title="Namespace meta", fable="dog-shadow",
    examples=[
        SubjectExample(
            form='(:doc (meta \'\\{:doc "steady wins"\\} race))',
            expected="steady wins",
            concept_phrase="accessing the :doc metadata from a symbol",
            question_what="the docstring value from a symbol's metadata",
            goal_text="extract the :doc metadata value from a symbol with a docstring",
            scenario=(
                'Bell the hound carried a long bone scratched with a name '
                'and a small marginal note — a message left by an earlier '
                "dog along the bank. The note's tag read :doc, and beside "
                'it ran a short instructive phrase.'
            ),
            need=(
                'She wanted only the marginal phrase from the bone — not '
                'the symbol it labeled, not the rest of the marks — so the '
                'next dog could read what the previous one had set there.'
            ),
            mapping=(
                'The bone is the form, the marginal scratches are its '
                'metadata, :doc is the slot the phrase lives in, and '
                'reading-the-tag is what the runtime does when the form '
                'asks for that slot.'
            ),
            resolution=(
                'The REPL read the marginal mark and handed back the phrase '
                'the previous dog had set there. The bone itself stayed '
                'untouched — the message-carrying scratch was simply read — doc.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(:author (meta \'\\{:author "Aesop"\\} race))',
            expected="Aesop",
            concept_phrase="accessing the :author metadata from a symbol",
            question_what="the author value from a symbol's metadata",
            goal_text="extract the :author metadata value from a symbol with an author tag",
            scenario=(
                "The same scroll, the same symbol race, but now she looked at different "
                "marginalia marked with an author tag. Another note in the margin — "
                "this one naming who had written the symbol's story."
            ),
            need=(
                "She wanted to extract a different metadata field from the marginalia."
            ),
            mapping=(
                "A symbol's metadata can hold any key-value pair — not just :doc, "
                "but :author, :date, or anything else. `(:author ...)` extracts "
                "the author field from the marginalia, just as `(:doc ...)` extracts the docstring."
            ),
            resolution=(
                "the runtime returned the author field from the scroll's margin — "
                "the note that credited the source."
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-16 — Cleaning up requires (we exercise via a simple "is this name
# in a vector" check, the analogue of "is this require still used").
G6_16 = SubjectCurriculum(grade=6, subject_id="G6-16",
    subject_title="Cleaning up requires", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(contains? #{'clojure.string} 'clojure.string)",
            expected=True,
            concept_phrase="testing membership in a set of namespaces",
            question_what="whether a namespace is in the set of required namespaces",
            goal_text="test whether the clojure.string namespace is in the set of required namespaces",
            scenario=(
                "Bell the hound kept a set of borrowed scrolls at the stream's edge — marker stones scratched with the names of libraries she had drawn from the shelf. One stone bore the name clojure.string. She wanted to check: was this library truly in her borrowed set?"
            ),
            need=(
                'She would test the membership to confirm the clojure.string library was among the '
                'scrolls she had actually taken.'
            ),
            mapping=(
                'The set holds the names of all borrowed scrolls, and the contains? test asks: is '
                'this name in the collection?'
            ),
            resolution=(
                'The REPL checked the set and returned true — clojure.string was indeed there, '
                'among the scrolls she had required.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(contains? #{'clojure.string} 'clojure.set)",
            expected=False,
            concept_phrase="testing membership in a set of namespaces",
            question_what="whether a different namespace is in the set of required namespaces",
            goal_text="test whether the clojure.set namespace is in the set of required namespaces",
            scenario=(
                'Still holding the same set with clojure.string, Patch now wondered about a '
                'different library — had she also borrowed clojure.set from the shelf? She held '
                'both names and tested whether the second was in the set.'
            ),
            need=(
                'The contains? test would tell her whether clojure.set had been taken along '
                'with clojure.string.'
            ),
            mapping=(
                'The set holds only the scrolls that were actually borrowed; contains? checks '
                'membership, and if a name is not there, the answer is false.'
            ),
            resolution=(
                'The REPL checked the set and returned false — clojure.set was not among the '
                'scrolls she had borrowed.'
            ),
            tags=("story",),
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
    print(f"grade-6 dog-shadow smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
