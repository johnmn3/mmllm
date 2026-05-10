"""Grade 6 — namespaces and modular code. Through crow-pitcher.

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
from mmllm.aesop.curriculum.crow_pitcher.grade_1 import (
    _GOAL_SUBPLOTS, _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL
)
from mmllm.aesop.curriculum.crow_pitcher._metaphor_pools import (
    _ROADSIGN_SUBPLOTS, _SCROLL_SUBPLOTS, _TOOLSHED_SUBPLOTS,
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
    subject_title="Namespace as file", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(name 'foo.bar)",
            expected="foo.bar",
            concept_phrase="extracting the string form of a namespace symbol",
            question_what="the string form of a quoted namespace symbol",
            goal_text="extract the string form of a quoted namespace symbol",

            scenario=(
                "Korvus perched at the pitcher's clay rim in the garden and "
                "studied the name carved into the side: a dotted path, two "
                "segments pressed into the clay. He wanted to read it as a "
                "plain string, not a symbol."
            ),
            need=(
                "He needed the string form of the namespace path — the "
                "dotted name as readable text, not a quoted symbol."
            ),
            mapping=(
                "`name` reads a symbol or keyword and returns the name "
                "portion as a plain string. On a two-part symbol like "
                "`foo.bar`, it returns the entire dotted path as written "
                "in the clay."
            ),
            resolution=(
                "The pitcher returned the dotted path exactly as Korvus "
                "had carved it, now held as a plain string."
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
                "Caw spotted a name carved on the pitcher's rim at the "
                "village market: a well-known dotted path, the standard "
                "string library's full designation pressed into the clay. "
                "She wanted it as a readable string."
            ),
            need=(
                "She needed to lift the carved name off the rim as a plain "
                "string — text she could compare or display without quoting."
            ),
            mapping=(
                "`name` strips the symbol wrapper and hands back the "
                "characters as a string. The dotted path stays intact; "
                "only the symbol-hood is shed."
            ),
            resolution=(
                'The pitcher handed back the dotted path as a string, the full designation now readable plain text (with `clojure.string` as the input value).'
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
                "Sable landed on the pitcher's rim at the hilltop, "
                "examining a stone scratched with a dotted name: "
                "`tortoise.race`. They needed to confirm its kind "
                "before placing it in the namespace drawer."
            ),
            need=(
                "The sorting-perch required knowing whether the stone was "
                "truly a symbol — the wrong type would slide past the "
                "correct drawer unregistered."
            ),
            mapping=(
                "`symbol?` tests any value and returns true only when it "
                "is a symbol. A quoted dotted name is a symbol; the test "
                "reads the kind-mark scratched into the stone's edge."
            ),
            resolution=(
                "The pitcher confirmed the stone was a symbol — the "
                "kind-mark matched, and the drawer accepted it."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-02 — ns form (we exercise via `name *ns*` style introspection)
G6_02 = SubjectCurriculum(grade=6, subject_id="G6-02",
    subject_title="ns form", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(name 'race.tortoise)",
            expected="race.tortoise",
            concept_phrase="extracting the string form of a namespace symbol",
            question_what="the string form of a quoted namespace symbol",
            goal_text="extract the string form of a quoted namespace symbol",

            scenario=(
                "Korvus pressed his talon to the pitcher's rim at the "
                "orchard's edge, tracing the carved namespace path — two "
                "dotted segments marking a specific file's home. He wanted "
                "the carving returned as plain readable text."
            ),
            need=(
                "He needed the namespace path as a string so he could "
                "compare it against the copybook's index of known files."
            ),
            mapping=(
                "`name` lifts a symbol and returns its character sequence "
                "as a string. A namespace symbol carved as two dot-joined "
                "segments arrives as an identical string, dots included."
            ),
            resolution=(
                'The pitcher returned the dotted namespace path as a string, ready for comparison against the copybook index (with `race.tortoise` as the input value).'
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
                "Caw held two stones side by side on the pitcher's rim "
                "at the road's bend, each scratched with the same dotted "
                "namespace path. She wanted to confirm they matched before "
                "merging the two drawers."
            ),
            need=(
                "She needed the REPL to verify the two carved paths were "
                "identical — different carvings would mean different files "
                "and the merge would corrupt the index."
            ),
            mapping=(
                "`=` on two symbols compares their full name character by "
                "character. Two quoted symbols with identical dot-joined "
                "paths are equal; the REPL reads both rim-carvings and "
                "checks every scratch."
            ),
            resolution=(
                'The pitcher confirmed the two carvings matched — the merge could proceed without risk (with `race.tortoise` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-03 — require — fully qualified usage (require already loaded
# clojure.string in basilisp/clojure runtime; the form below works in
# both).
G6_03 = SubjectCurriculum(grade=6, subject_id="G6-03",
    subject_title="require", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form='(clojure.string/upper-case "hare")',
            expected="HARE",
            concept_phrase="calling a fully-qualified string function",
            question_what="the capitalized form returned by the upper-case routine on the scroll",
            goal_text="call the upper-case routine on the clojure.string scroll, applied to the four-letter string hare",

            scenario=(
                "Sable perched at the pitcher in the meadow, a flat stone "
                "already required from the string-scroll's shelf. She "
                "scratched the fully-qualified call using the scroll's "
                "shelf-name and the upper-case groove."
            ),
            need=(
                "She needed the four-letter word returned in its capitals — "
                "the shelf held the method, but the full path was required "
                "to reach it across the namespace boundary."
            ),
            mapping=(
                "The `namespace/function` carving tells the runtime which "
                "shelf to pull from before calling. The required shelf "
                "answers with the uppercased characters, the slash linking "
                "shelf to groove."
            ),
            resolution=(
                "The pitcher returned the four letters in their capital "
                "form, the fully-qualified call resolved cleanly. (with {drawn.a} folded in)"
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
                "Korvus stood at the pitcher in the village, the "
                "string-scroll shelf already in place. He pressed the "
                "fully-qualified lower-case name into the clay and "
                "presented the all-capitals stone."
            ),
            need=(
                "He needed the all-capitals word returned in its small "
                "letters — only the fully-qualified shelf path would "
                "reach the lowercasing groove."
            ),
            mapping=(
                "The `namespace/function` form routes the call across "
                "the namespace boundary to the shelf that holds the "
                "lowercasing groove. The stone is transformed and "
                "returned, its letters now small."
            ),
            resolution=(
                "The pitcher returned the five letters in their lowercase "
                "form, the shelf call reaching exactly the right groove. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-04 — refer-and-use (we exercise the effect: a referred name
# resolves the same as the qualified name; via `=` we compare two
# applications).
G6_04 = SubjectCurriculum(grade=6, subject_id="G6-04",
    subject_title="refer and use", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form='(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))',
            expected=True,
            concept_phrase="testing equality of two identical function calls",
            question_what="whether two calls to the same function with the same argument produce the same result",
            goal_text="test whether two calls to the fully-qualified string uppercasing function with the same argument are equal",

            scenario=(
                "Caw dropped the same single-letter stone twice into the "
                "pitcher at the orchard, each time calling the same "
                "fully-qualified shelf. She wanted to confirm both "
                "calls came back with the same capitalized result."
            ),
            need=(
                "She needed to verify that the referred shelf always "
                "returns the same value for the same input — two "
                "identical calls should produce equal results."
            ),
            mapping=(
                "`=` compares two values. When both sides call the same "
                "qualified function with the same argument, the results "
                "are identical. Referring a name is just a shorthand for "
                "the same qualified path — the groove is the same groove."
            ),
            resolution=(
                "The pitcher confirmed both calls matched — the same "
                "shelf reached twice returned the same capitalized result. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-05 — Fully qualified names
G6_05 = SubjectCurriculum(grade=6, subject_id="G6-05",
    subject_title="Fully qualified names", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form='(clojure.string/upper-case "hello")',
            expected="HELLO",
            concept_phrase="calling a fully-qualified string function",
            question_what="the uppercase form of the string hello produced by clojure.string/upper-case",
            goal_text="call the uppercasing function from clojure.string on a test string",

            scenario=(
                "Korvus perched at the tall pitcher on the hilltop, the "
                "string-scroll shelf already placed within reach. He "
                "pressed the five-letter greeting-stone into position "
                "and carved the fully-qualified shelf path beside it."
            ),
            need=(
                "He needed the five-letter word returned in its capitals. "
                "Without the full shelf-and-groove path, the runtime "
                "could not find the uppercasing method."
            ),
            mapping=(
                "The `namespace/function` notation is a two-part carving: "
                "shelf-name, slash, groove-name. The runtime reads left to "
                "right — finds the shelf, then calls the groove. "
                "The stone emerges transformed."
            ),
            resolution=(
                "The pitcher returned the five letters in capitals, the "
                "fully-qualified path guiding the runtime to the right groove. (with {drawn.a} folded in)"
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
                "Caw held a three-bead string at the pitcher's rim in the "
                "garden, the beads scratched a, b, c in order. She carved "
                "the fully-qualified reverse-groove path and submitted the "
                "bead-string."
            ),
            need=(
                "She needed the bead-string returned in the opposite order. "
                "Only the string shelf's reverse groove could rearrange "
                "the beads correctly."
            ),
            mapping=(
                "The fully-qualified call crosses the namespace boundary "
                "to reach the shelf, then invokes the reverse groove. "
                "The bead order flips; the length stays the same. "
                "The slash is the bridge between shelf and groove."
            ),
            resolution=(
                'The pitcher returned the three-bead string with the order reversed, the shelf call completing cleanly (with `abc` as the input value).'
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
                "Sable found a qualified keyword stone at the market: "
                "two parts separated by a slash, the left part naming "
                "which shelf it came from, the right part its local name. "
                "They needed only the left part."
            ),
            need=(
                "They needed to know which namespace the keyword belonged "
                "to — the shelf's name carved before the slash, "
                "not the local name that followed."
            ),
            mapping=(
                "`namespace` reads a qualified keyword and returns only "
                "the portion before the slash — the shelf's name. "
                "The local name after the slash is left behind; only the "
                "namespace portion is returned."
            ),
            resolution=(
                "The pitcher returned the namespace portion — "
                "the shelf's name carved before the slash. (with {drawn.a} folded in)"
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
                "Korvus inspected the same two-part keyword stone at the "
                "market: shelf's name before the slash, local name after. "
                "This time he needed the local name — what the thing "
                "was called inside the shelf."
            ),
            need=(
                "He needed the local name scratched after the slash, "
                "not the shelf's prefix. The registered name alone "
                "would tell him what value to retrieve."
            ),
            mapping=(
                "`name` on a qualified keyword returns the local portion "
                "after the slash — the name the thing answers to within "
                "its shelf. The namespace prefix is stripped away; "
                "only the local name remains."
            ),
            resolution=(
                "The pitcher returned the local name — the portion after "
                "the slash, stripped of its namespace prefix. (the keyword :owner)"
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-06 — Private defs (we can't test ^:private effect with eval, but
# we can confirm related metadata predicates).
G6_06 = SubjectCurriculum(grade=6, subject_id="G6-06",
    subject_title="Private defs", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(:private (meta '^:private x))",
            expected=True,
            concept_phrase="accessing the :private flag from metadata",
            question_what="whether the :private metadata is set on a symbol",
            goal_text="check whether the :private flag is present in the metadata of a symbol with :private marker",

            scenario=(
                "Caw pressed a talon to the pitcher's rim at the village "
                "and read the marginal note scratched beside the symbol x: "
                "a small mark indicating it was meant for internal use "
                "only, not to be called across the rim."
            ),
            need=(
                "She needed to confirm the private mark was present in "
                "the margin — if it was set, the symbol should not be "
                "exported beyond the shelf's edge."
            ),
            mapping=(
                "`meta` reads the marginal notes scratched beside a "
                "symbol. `:private` retrieves that particular flag from "
                "the note-map. A symbol wearing `^:private` has the flag "
                "set to true in its margin."
            ),
            resolution=(
                "The pitcher confirmed the private flag was present — "
                "the marginal note showed true, the symbol marked internal. (the keyword :private)"
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
                "Sable examined a plain symbol x at the pitcher's rim on "
                "the road — no marginal note scratched beside it, no "
                "markers pressed into the clay. They read the margin "
                "anyway to see what was there."
            ),
            need=(
                "They needed to know whether a plain unmarked symbol "
                "carried the private flag — missing metadata should "
                "tell them the symbol had no access restriction."
            ),
            mapping=(
                "`meta` on a plain undecorated symbol returns an empty "
                "margin or nil. Retrieving `:private` from nothing "
                "produces nil — no mark was ever pressed; the absence "
                "itself is the answer."
            ),
            resolution=(
                "The pitcher returned nil — no private mark in the "
                "margin, the plain symbol carrying no access restriction. (the keyword :private)"
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-07 — Public vs private API (design decision; we exercise via
# the predicate `:private` on metadata).
G6_07 = SubjectCurriculum(grade=6, subject_id="G6-07",
    subject_title="Public vs private API", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(boolean (:private (meta '^:private hidden)))",
            expected=True,
            concept_phrase="converting the :private metadata to a boolean",
            question_what="whether a symbol with :private marker evaluates to true when converted to boolean",
            goal_text="convert the :private metadata flag of a symbol marked with :private to a boolean",

            scenario=(
                "Korvus carved a symbol onto the pitcher's rim in the "
                "orchard and pressed a small private mark into the "
                "margin beside it. He then tested whether the mark "
                "read as a firm yes when converted to a true-or-false stone."
            ),
            need=(
                "He needed a clean true-or-false answer about the "
                "private mark — a gating stone that would route the "
                "symbol to the internal shelf or the public face."
            ),
            mapping=(
                "`boolean` converts any value to a true-or-false stone. "
                "The `:private` flag read from the margin is truthy; "
                "`boolean` firms it into an unambiguous true. The "
                "gating stone lands on the internal shelf."
            ),
            resolution=(
                "The REPL confirmed the predicate held — — the private mark firmed "
                "into a clean boolean, the internal shelf confirmed. (the keyword :private)"
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
                "Caw read the margin beside a plain public symbol at the "
                "pitcher's rim in the garden — no private mark pressed "
                "in the clay. She converted whatever the margin held "
                "to a firm true-or-false stone."
            ),
            need=(
                "She needed a clean false to confirm the symbol had no "
                "access restriction — a missing private mark should "
                "produce a firm false, not a nil ambiguity."
            ),
            mapping=(
                "`boolean` on nil — the result of reading a missing "
                "flag — returns false. The absent mark becomes a clean "
                "false stone, routing the symbol to the public face "
                "of the rim."
            ),
            resolution=(
                "The REPL signalled the predicate did not hold — — no private mark meant "
                "nil, and nil firmed into a clean false. (the keyword :private)"
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-08 — Circular dependencies (we exercise via a plain form that
# would resolve correctly when the dependency graph is sound; the
# narrative carries the lesson).
G6_08 = SubjectCurriculum(grade=6, subject_id="G6-08",
    subject_title="Circular dependencies", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form='(clojure.string/upper-case "a")',
            expected="A",
            concept_phrase="calling a function from a required namespace",
            question_what="the uppercase form of the character a produced by clojure.string/upper-case",
            goal_text="call the string uppercasing function from clojure.string on the character a",

            scenario=(
                "Sable stood at the pitcher at the farm, the string-scroll "
                "shelf placed cleanly with no circular loop in the "
                "dependency path. They presented a single-letter stone "
                "and called the uppercase groove."
            ),
            need=(
                "They needed the single letter returned in its capital "
                "form — a test that the shelf was reachable without "
                "a circular require blocking the path."
            ),
            mapping=(
                "When the dependency graph has no loops, the shelf "
                "loads in a straight line and its grooves are reachable. "
                "A circular loop would freeze the loader; a clean path "
                "lets the call reach the groove and return."
            ),
            resolution=(
                "The pitcher returned the single letter capitalized — "
                "the shelf reachable, the dependency path loop-free. (with {drawn.a} folded in)"
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
                "Korvus held two stones scratched with the same short "
                "dotted path at the pitcher's rim on the road. He wanted "
                "to confirm they represented a single namespace — not "
                "two different ones masquerading as the same name."
            ),
            need=(
                "He needed a firm equal-or-not answer: two identical "
                "namespace paths should be the same symbol, ruling "
                "out a hidden circular aliasing problem."
            ),
            mapping=(
                "`=` on two quoted symbols compares their full name "
                "scratch by scratch. Two stones bearing identical dotted "
                "paths are equal; there is no hidden aliasing — "
                "same carving, same symbol."
            ),
            resolution=(
                'The pitcher confirmed the two dotted paths were equal — no hidden aliasing, the same namespace named once (with `a.b` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-09 — Loading order (we exercise via straightforward sequence of
# forms inside a `do` so the REPL processes them in order).
G6_09 = SubjectCurriculum(grade=6, subject_id="G6-09",
    subject_title="Loading order", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(do (def step1 1) (def step2 (+ step1 1)) step2)",
            expected=2,
            concept_phrase="evaluating definitions in sequence to establish dependency order",
            question_what="the value of the second variable after both definitions are loaded in order",
            goal_text="define step1 as 1, then define step2 as step1 plus 1, then return step2",

            scenario=(
                "Caw placed two stones on the pitcher's rim at the "
                "village in order: the first named and counted, the "
                "second's count depending on the first. She would read "
                "the second stone's count after both were set."
            ),
            need=(
                "She needed the second definition to find the first "
                "already on the rim — out of order, the second stone "
                "would find nothing."
            ),
            mapping=(
                "`do` executes forms left to right. `def step1` carves "
                "its name before `def step2` is reached. When step2 "
                "looks for step1, it is already on the rim. The last "
                "form's value is returned."
            ),
            resolution=(
                "The pitcher returned the second stone's count — "
                "each name found before it was needed. (with {drawn.a} folded in)"
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
                "Korvus tucked two counts under his wings in order at "
                "the hilltop pitcher: the first under the left wing, "
                "the second calculated from the first and tucked under "
                "the right. He then totaled both."
            ),
            need=(
                "He needed the second binding to see the first already "
                "tucked — `let` evaluates bindings left to right so "
                "each can depend on the previous."
            ),
            mapping=(
                "`let` binding pairs are evaluated in order: `a` is "
                "tucked first, then `b` is computed using the already-"
                "tucked `a`. Both are in force for the body. "
                "The sum uses both tucked values."
            ),
            resolution=(
                "The pitcher returned the sum — ordered bindings "
                "resolved cleanly, each tuck found before it was needed. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-10 — leiningen / deps.edn (project setup; we exercise via reading
# a small edn-shaped data structure that resembles a deps map).
G6_10 = SubjectCurriculum(grade=6, subject_id="G6-10",
    subject_title="Leiningen and deps.edn", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(:deps {:deps {:a 1 :b 2}})",
            expected={":a": 1, ":b": 2},
            concept_phrase="accessing a key from a nested map structure",
            question_what="the value at the :deps key in a deps-style map",
            goal_text="extract the value at the :deps key from a nested map",

            scenario=(
                "Sable opened a nested stone-pile map at the pitcher's "
                "rim in the meadow: a project-description tablet with "
                "an outer shell and an inner dependency map. They "
                "pressed the :deps key to read the inner contents."
            ),
            need=(
                "They needed only the inner map of dependencies — "
                "the nested layer beneath the outer :deps key, "
                "not the entire tablet."
            ),
            mapping=(
                "A keyword used as a function looks up its own name "
                "in the map it receives. `:deps` reads the outer tablet "
                "and returns the value at that key — the inner "
                "dependency map sits waiting underneath."
            ),
            resolution=(
                "The pitcher returned the inner dependency map — "
                "the nested contents at :deps, the outer shell gone. (with {drawn.a} folded in)"
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
                "Korvus studied a project tablet at the hilltop pitcher: "
                "a single :paths entry holding a vector of directory "
                "names. He needed to reach the first directory name "
                "using a two-step path."
            ),
            need=(
                "He needed to navigate two levels: first the :paths key, "
                "then index zero inside the vector — a single lookup "
                "would not reach deep enough."
            ),
            mapping=(
                "`get-in` follows a path vector step by step into nested "
                "structures. `[:paths 0]` first finds the :paths key, "
                "then takes the first element of the vector it finds "
                "there."
            ),
            resolution=(
                "The pitcher returned the first directory name — "
                "the two-step path reaching the value cleanly. (the keyword :paths)"
            ),
            tags=("story",),
        ),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-11 — Classpath (we use a tiny path-string operation as the
# eval-shaped exercise).
G6_11 = SubjectCurriculum(grade=6, subject_id="G6-11",
    subject_title="Classpath", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form='(clojure.string/split "src:test" #":")',
            expected=["src", "test"],
            concept_phrase="splitting a string by a delimiter",
            question_what="the vector of parts after splitting a colon-separated path string",
            goal_text="split a colon-separated classpath-like string into its individual entries",

            scenario=(
                "Caw held a bead-string at the pitcher's rim in the "
                "garden: two directory names joined by a colon bead. "
                "She needed to separate the string at the colon "
                "and read each directory name independently."
            ),
            need=(
                "She needed the two names as separate stones in a "
                "vector — joined into one bead-string they could not "
                "be placed individually into the correct drawers."
            ),
            mapping=(
                "`split` reads a string and a delimiter pattern. It "
                "cuts the bead-string at each colon bead and collects "
                "the pieces into a vector. Each directory name "
                "becomes its own stone."
            ),
            resolution=(
                'The pitcher returned a vector of two separate directory-name strings, the colon bead consumed in the cut (with `:test` as the input value).'
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
                "Sable laid three directory-name stones along the "
                "pitcher's rim at the orchard: source, tests, "
                "resources — the classpath's full stone-pile. "
                "They needed to know how many stones were in the row."
            ),
            need=(
                "They needed a count of classpath entries so Korvus "
                "could verify all three directories were registered "
                "before the runtime began loading."
            ),
            mapping=(
                "`count` walks the vector and tallies each element. "
                "the stones in the row means `count` returns three. "
                "The tally is the number of stones, not their names."
            ),
            resolution=(
                "The pitcher returned the stone-count — three "
                "classpath entries confirmed present in the row."
            ),
            tags=("story",),
        ),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-12 — Multiple files, one project (we exercise via a vector
# of namespace symbols).
G6_12 = SubjectCurriculum(grade=6, subject_id="G6-12",
    subject_title="Multiple files in one project", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(count ['race.tortoise 'race.hare 'race.shared])",
            expected=3,
            concept_phrase="counting the number of namespace symbols in a project",
            question_what="the number of namespaces in a small project",
            goal_text="count the number of namespace symbols in a vector of three namespaces",

            scenario=(
                "Korvus lined up three namespace-symbol stones on the "
                "pitcher's rim at the road: one for each file in the "
                "project. He needed to count the stones to confirm "
                "none were missing from the project roster."
            ),
            need=(
                "He needed a count of namespace stones so that the "
                "copybook index would show how many files the project "
                "expected — a mismatch would mean a missing file."
            ),
            mapping=(
                "`count` on a vector tallies each element without "
                "reading their names. Three namespace symbols in the "
                "vector means `count` returns three, regardless of "
                "what each symbol is called."
            ),
            resolution=(
                'The pitcher returned the count of namespace stones — three files confirmed in the project roster (with `race.tortoise` as the input value).'
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
                "Caw held two namespace-symbol stones at the pitcher's "
                "rim in the orchard. She needed to lift the dotted "
                "path from each stone as a plain string — the index "
                "stored strings, not symbols."
            ),
            need=(
                "She needed both dotted paths as strings so they could "
                "be stored in the copybook's string index — symbols "
                "would not fit the index's slots."
            ),
            mapping=(
                "`map` applies a function to each element of the "
                "collection. `name` strips each namespace symbol down "
                "to its character sequence. The result is a sequence "
                "of plain strings, one per original stone."
            ),
            resolution=(
                'The pitcher returned both dotted paths as strings — wrappers shed, the strings ready for the index (with `race.tortoise` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-13 — Aliasing conventions (we exercise via a tiny alias-style
# substitution that's purely lexical).
G6_13 = SubjectCurriculum(grade=6, subject_id="G6-13",
    subject_title="Aliasing conventions", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form='(let [s clojure.string/upper-case] (s "hare"))',
            expected="HARE",
            concept_phrase="aliasing a fully-qualified function and calling it through the alias",
            question_what="the uppercase form of the string hare when clojure.string/upper-case is called through a local alias",
            goal_text="bind the fully-qualified string uppercasing function to a local alias s and call it on hare",

            scenario=(
                "Sable perched at the pitcher in the village and tucked "
                "the long qualified shelf-and-groove name under one wing, "
                "labeling it s. They called through the alias to avoid "
                "repeating the full path."
            ),
            need=(
                "They needed the four-letter word capitalized, but the "
                "full qualified path was unwieldy — a wing-tucked alias "
                "would let them call with a single letter."
            ),
            mapping=(
                "`let` tucks the function itself — not its name — under "
                "the alias s. Calling `(s ...)` invokes the same groove "
                "as the full qualified path."
            ),
            resolution=(
                "The pitcher returned the four letters capitalized — "
                "the alias and full path reached the same groove. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-14 — Import for Java classes (basilisp targets Python; we use a
# universally-available form here: predicate on a class-y name).
G6_14 = SubjectCurriculum(grade=6, subject_id="G6-14",
    subject_title="Import for host classes", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(symbol? 'java.util.List)",
            expected=True,
            concept_phrase="testing whether a value is a symbol",
            question_what="whether a dotted Java class name is a symbol",
            goal_text="test whether a Java class name written as a quoted symbol is a symbol",

            scenario=(
                "Korvus discovered a borrowed earthenware vessel at the "
                "pitcher's base in the market: a human-fired container "
                "with a dotted three-part label, the potter's full class "
                "name pressed into the clay. He needed to confirm its kind."
            ),
            need=(
                "He needed to know whether the dotted human-potter label "
                "was a symbol — the import machinery would only register "
                "it if it arrived as a proper symbol, not raw text."
            ),
            mapping=(
                "`symbol?` tests the kind-mark of any value. A quoted "
                "dotted label — even one naming a human potter's class "
                "— is a symbol; the test reads the kind-mark and "
                "returns the answer."
            ),
            resolution=(
                'The pitcher confirmed the human-potter label was a symbol — the kind-mark matched, the import path valid (with `java.util.List` as the input value).'
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
                "Caw held a borrowed vessel labeled with a three-part "
                "dotted potter's name at the pitcher's rim in the village. "
                "She needed the label as a plain string so it could be "
                "stored in the import registry."
            ),
            need=(
                "The import registry held strings, not symbols. She "
                "needed to strip the symbol wrapper from the dotted "
                "label and recover the plain text underneath."
            ),
            mapping=(
                "`name` strips any symbol or keyword down to its "
                "character sequence. A quoted dotted class name "
                "becomes the same dotted string — the symbol wrapper "
                "is shed; the label text remains."
            ),
            resolution=(
                'The pitcher returned the three-part dotted name as a plain string, ready for the import registry (with `java.util.Map` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-15 — Namespace meta (we exercise the metadata mechanism on a
# symbol via `^{:doc ...}`).
G6_15 = SubjectCurriculum(grade=6, subject_id="G6-15",
    subject_title="Namespace meta", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form='(:doc (meta \'\\{:doc "steady wins"\\} race))',
            expected="steady wins",
            concept_phrase="accessing the :doc metadata from a symbol",
            question_what="the docstring value from a symbol's metadata",
            goal_text="extract the :doc metadata value from a symbol with a docstring",

            scenario=(
                "Sable pressed a talon-inscription into the margin "
                "beside the namespace symbol at the pitcher's flat stone "
                "in the meadow: a :doc note recording the shelf's "
                "purpose. They later read that margin to find the note."
            ),
            need=(
                "They needed to recover the docstring scratched into "
                "the margin — a crow perching later would read it "
                "to understand the shelf's intent without examining "
                "every groove."
            ),
            mapping=(
                "`meta` reads the marginal notes on a symbol as a map. "
                "`:doc` retrieves the documentation string from that "
                "map. The talon-inscription in the margin is the value; "
                "`meta` is the flat stone one reads it from."
            ),
            resolution=(
                "The pitcher returned the docstring from the margin — "
                "the talon-inscribed note retrieved intact. (the keyword :doc)"
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
                "Korvus found a namespace stone on the hilltop pitcher "
                "with an author note inscribed in the margin: the name "
                "of the crow who first carved the shelf. He needed "
                "to read that name back from the marginal record."
            ),
            need=(
                "He needed the author's name from the margin so the "
                "copybook could credit the shelf's origin — the name "
                "in the margin was the only record of authorship."
            ),
            mapping=(
                "`meta` opens the marginal note-map. `:author` retrieves "
                "the value stored under that key. The name pressed into "
                "the margin is the value; the flat stone holds the "
                "full note-map from which `:author` reads."
            ),
            resolution=(
                "The pitcher returned the author's name from the "
                "marginal note — the talon-inscription retrieved, "
                "the copybook credit confirmed. (the keyword :author)"
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-16 — Cleaning up requires (we exercise via a simple "is this name
# in a vector" check, the analogue of "is this require still used").
G6_16 = SubjectCurriculum(grade=6, subject_id="G6-16",
    subject_title="Cleaning up requires", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(contains? #{'clojure.string} 'clojure.string)",
            expected=True,
            concept_phrase="testing membership in a set of namespaces",
            question_what="whether a namespace is in the set of required namespaces",
            goal_text="test whether the clojure.string namespace is in the set of required namespaces",

            scenario=(
                "Caw laid out a set of required-namespace stones at the "
                "pitcher's rim in the orchard — one stone for each shelf "
                "the project still used. She needed to check whether "
                "the string shelf's stone was still in the set."
            ),
            need=(
                "She needed to confirm the string shelf was still in "
                "the set — a missing stone would mean the require "
                "could be removed safely from the copybook."
            ),
            mapping=(
                "`contains?` tests whether a value is a member of a "
                "set. It checks the set's stones one by one and returns "
                "true if the target stone is found among them, false "
                "otherwise."
            ),
            resolution=(
                'The pitcher confirmed the stone was present — the require still in use, the shelf still needed (with `clojure.string` as the input value).'
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
                "Sable examined the same set of required-namespace "
                "stones at the pitcher's rim in the garden and looked "
                "for a different shelf's stone — the set shelf, not "
                "the string shelf. They needed to know if it was there."
            ),
            need=(
                "They needed to confirm the set shelf's stone was "
                "absent — if not found, the require for that shelf "
                "could be cleaned from the copybook safely."
            ),
            mapping=(
                "`contains?` searches the set for the target stone. "
                "When the stone is absent, it returns false — not nil, "
                "but a clear false. The set held only string-shelf "
                "stones; the set-shelf stone was not among them."
            ),
            resolution=(
                'The REPL signalled the predicate did not hold — — the set-shelf stone was absent, the unused require confirmed for removal (with `clojure.string` as the input value).'
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
    print(f"grade-6 crow-pitcher smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
