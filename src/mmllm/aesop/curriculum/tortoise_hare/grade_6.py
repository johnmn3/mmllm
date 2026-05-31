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
from mmllm.aesop.curriculum.tortoise_hare._metaphor_pools import (
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
    subject_title="Namespace as file", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(name 'foo.bar)",
            expected="foo.bar",
            concept_phrase="extracting the string form of a namespace symbol",
            question_what="the string form of a quoted namespace symbol",
            goal_text="extract the string form of a quoted namespace symbol",
            scenario=(
                "On the long road, there lay a library shelf holding scrolls. "
                "Each scroll had a name — foo.bar, tortoise.race — inscribed "
                "on its spine in the style of the land."
            ),
            need=(
                "Mossback the tortoise needed to know the exact string that "
                "the spine-name spelled out, so she could describe it to "
                "Hare exactly as it was written."
            ),
            mapping=(
                "A quoted namespace symbol `'foo.bar` is the *name* carved "
                "on the spine. `(name ...)` extracts the string those letters spell, "
                "leaving the scroll itself alone."
            ),
            resolution=(
                "the runtime returned the string "
                "that the spine-name spelled, exactly as Mossback had asked."
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
                "The library shelf held many scrolls, each bearing a spine-name. "
                "One scroll in particular was labeled clojure.string — a scroll "
                "of borrowed routines, its name written in the dotted convention."
            ),
            need=(
                "Mossback needed to read the spine-name as a plain string, "
                "without the scroll itself, just the letters."
            ),
            mapping=(
                "The `'clojure.string` symbol is a *reference* to the scroll's "
                "name-as-a-thing. `(name ...)` converts that symbol into "
                "the string the spine displays."
            ),
            resolution=(
                "the runtime returned the dotted string that the spine "
                "had been labeled with."
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
                "Mossback stood before a small slate and a quill. On the slate, "
                "she had written the mark 'tortoise.race — a named thing, not "
                "an acorn, not a word of the road, but a *symbol* — a label "
                "in the land's convention."
            ),
            need=(
                "She needed to confirm that what she had written *was* truly "
                "a symbol and not some other kind of value."
            ),
            mapping=(
                "A quoted name like `'tortoise.race` is a symbol — the *mark* "
                "of a thing, not the thing itself. `(symbol? ...)` answers "
                "whether the argument is such a mark."
            ),
            resolution=(
                "the runtime confirmed that yes, `'tortoise.race` was indeed "
                "a symbol, exactly as the form declared it."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-02 — ns form (we exercise via `name *ns*` style introspection)
G6_02 = SubjectCurriculum(grade=6, subject_id="G6-02",
    subject_title="ns form", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(name 'race.tortoise)",
            expected="race.tortoise",
            concept_phrase="extracting the string form of a namespace symbol",
            question_what="the string form of a quoted namespace symbol",
            goal_text="extract the string form of a quoted namespace symbol",
            scenario=(
                "In the cottage where Mossback kept her scrolls, each was labeled "
                "with a name. The scroll race.tortoise hung from a hook, its "
                "spine carved with the dotted path-name of the workspace she "
                "intended to set in motion."
            ),
            need=(
                "Before she could declare this workspace as active, she needed "
                "to see its name spelled out as a plain string — the exact letters "
                "the scroll's spine bore."
            ),
            mapping=(
                "A quoted symbol like `'race.tortoise` is the *name-as-a-mark*. "
                "`(name ...)` unwraps the symbol and returns the string "
                "those characters spell."
            ),
            resolution=(
                "the runtime returned the string matching the scroll's spine-name, "
                "ready for Mossback to declare the namespace."
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
                "Mossback had drawn two spindle-marks on the slate: 'race.tortoise "
                "and 'race.tortoise. They *looked* the same — the same shape, "
                "the same letters — but she wanted the REPL to settle it."
            ),
            need=(
                "She needed to know whether the runtime agreed they were the same "
                "name, or whether some invisible difference existed that only "
                "the REPL could see."
            ),
            mapping=(
                "Two symbols are equal if they carry the same name-mark. "
                "`(= ...)` tests whether the two arguments — whether they are "
                "symbols, acorns, or anything — are the same."
            ),
            resolution=(
                "the runtime confirmed that both marks *were* the same symbol, "
                "exactly as they appeared."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-03 — require — fully qualified usage (require already loaded
# clojure.string in basilisp/clojure runtime; the form below works in
# both).
G6_03 = SubjectCurriculum(grade=6, subject_id="G6-03",
    subject_title="require", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form='(clojure.string/upper-case "hare")',
            expected="HARE",
            concept_phrase="calling a fully-qualified string function",
            question_what="the capitalized form returned by the upper-case routine on the scroll",
            goal_text="call the upper-case routine on the clojure.string scroll, applied to the four-letter string hare",
            scenario=(
                "The library by the road kept a scroll on its shelves "
                "called `clojure.string`. Among its signs was a routine "
                "named `upper-case` — a routine that took a string and "
                "returned the same letters, capitalized."
            ),
            need=(
                'Mossback the tortoise wanted the capitalized form of the four-letter word `{drawn.a}`, for a road-sign she was painting.'
            ),
            mapping=(
                "When a routine lives on a scroll, you call it by both "
                "names together: scroll-name slash routine-name — "
                "`clojure.string/upper-case`. The runtime fetches the "
                "scroll and invokes the routine on the argument."
            ),
            resolution=(
                "the routine returned the four letters in capitals, "
                "ready for the road-sign Mossback was painting."
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
                "The library's shelves held another scroll — clojure.string, "
                "a scroll of ready-made routines for the signs Mossback painted. "
                "Among them was lower-case, a routine that took capital letters "
                "and returned them as the small kind."
            ),
            need=(
                "For a sign she was making, Mossback needed the word {drawn.a} changed to its small-letter form — not to shout, but to match the style of the sign's other words."
            ),
            mapping=(
                "When a routine lives on a borrowed scroll, call it by both "
                "names together: scroll-name slash routine-name — "
                "`clojure.string/lower-case`. The runtime fetches the scroll "
                "and invokes the routine on the argument."
            ),
            resolution=(
                "the routine returned the five letters in small form, ready "
                "for the road-sign Mossback was painting."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-04 — refer-and-use (we exercise the effect: a referred name
# resolves the same as the qualified name; via `=` we compare two
# applications).
G6_04 = SubjectCurriculum(grade=6, subject_id="G6-04",
    subject_title="refer and use", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form='(= (clojure.string/upper-case "x") (clojure.string/upper-case "x"))',
            expected=True,
            concept_phrase="testing equality of two identical function calls",
            question_what="whether two calls to the same function with the same argument produce the same result",
            goal_text="test whether two calls to the fully-qualified string uppercasing function with the same argument are equal",
            scenario=(
                "Mossback had picked up the clojure.string scroll twice, called "
                "the upper-case routine on the same tiny string both times. Now "
                "she held two results in her paws — and they *looked* identical. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "But she needed the REPL to settle it: were the two results "
                "truly the same, or had some hidden difference crept in?"
            ),
            mapping=(
                "When you call the same routine twice with the same argument, "
                "you get the same value back both times. `(= ...)` tests whether "
                "two values are the same."
            ),
            resolution=(
                "the runtime confirmed that both calls produced exactly "
                "the same value — the scroll's routine was reliable."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-05 — Fully qualified names
G6_05 = SubjectCurriculum(grade=6, subject_id="G6-05",
    subject_title="Fully qualified names", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form='(clojure.string/upper-case "hello")',
            expected="HELLO",
            concept_phrase="calling a fully-qualified string function",
            question_what="the uppercase form of the string hello produced by clojure.string/upper-case",
            goal_text="call the uppercasing function from clojure.string on a test string",
            scenario=(
                'Mossback stood at the library, the clojure.string scroll open before her. She had a greeting to paint on a sign — the word {drawn.a} — and wanted it in grand capitals for all to see.'
            ),
            need=(
                "She needed to call the scroll's upper-case routine on the word, "
                "so the greeting would shout."
            ),
            mapping=(
                "To call a routine on a borrowed scroll, use both names: "
                "scroll-slash-routine. The runtime finds the scroll, locates "
                "the routine, and invokes it on the argument."
            ),
            resolution=(
                "the routine returned the five letters in capitals, ready "
                "for the grand sign."
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
                'The same scroll held another routine: reverse. It took the letters in a string and handed them back in the opposite order. Mossback had a string abc and wanted to see what the reversed order would look like.'
            ),
            need=(
                "She needed the scroll's reverse routine to rearrange the letters "
                "backward."
            ),
            mapping=(
                "The fully-qualified name clojure.string/reverse specifies both "
                "the scroll and the routine on it. The REPL fetches the scroll "
                "and runs the routine exactly."
            ),
            resolution=(
                "the routine returned the three letters in reverse order — "
                "the opposite of how they had started."
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
                "Mossback held up a label-like value: :owner/item. It had two parts, "
                "separated by a slash — the first part like a scroll-name, "
                "the second part like a routine-name on that scroll."
            ),
            need=(
                "She wanted to extract just the first part — the namespace — "
                "to know which scroll this label belonged to."
            ),
            mapping=(
                "A qualified keyword like :owner/item carries two names in one: "
                "the namespace (owner) and the local name (item). `(namespace ...)` "
                "extracts the namespace portion."
            ),
            resolution=(
                "the runtime returned the namespace part, the first name "
                "before the slash."
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
                'From the same qualified label :owner/item, Mossback now wanted the second part — the local name that lived *within* the namespace. The value drawn fresh was :owner/item.'
            ),
            need=(
                "She needed to know what the routine was called — the part after "
                "the slash — to understand what this label referred to."
            ),
            mapping=(
                "A qualified keyword like :owner/item is like a fully-qualified "
                "name: namespace slash local-name. `(name ...)` extracts "
                "the local-name portion."
            ),
            resolution=(
                "the runtime returned the local-name part, the second name "
                "after the slash."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-06 — Private defs (we can't test ^:private effect with eval, but
# we can confirm related metadata predicates).
G6_06 = SubjectCurriculum(grade=6, subject_id="G6-06",
    subject_title="Private defs", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(:private (meta '^:private x))",
            expected=True,
            concept_phrase="accessing the :private flag from metadata",
            question_what="whether the :private metadata is set on a symbol",
            goal_text="check whether the :private flag is present in the metadata of a symbol with :private marker",
            scenario=(
                "On the scroll lay a symbol marked with a special marker: ^:private x. "
                "The marker was like a rope tied around the name — it carried information "
                "about the symbol that you could ask the scroll about later."
            ),
            need=(
                "Mossback wanted to ask: is the :private marker tied to this name? "
                "Does the metadata carry that flag?"
            ),
            mapping=(
                "A symbol can carry metadata — extra information attached to it. "
                "`(meta ...)` returns that metadata, and `(:private ...)` pulls out "
                "the :private flag if it's there."
            ),
            resolution=(
                "the runtime returned the flag, confirming that yes, the ^:private "
                "marker had been tied to the symbol."
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
    subject_title="Public vs private API", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(boolean (:private (meta '^:private hidden)))",
            expected=True,
            concept_phrase="converting the :private metadata to a boolean",
            question_what="whether a symbol with :private marker evaluates to true when converted to boolean",
            goal_text="convert the :private metadata flag of a symbol marked with :private to a boolean",
            scenario=(
                "Mossback marked a symbol with the rope ^:private hidden. Now she wanted "
                "to ask: if I pull out the :private flag, and then test whether it's "
                "truly there, will the answer be a true or false value?"
            ),
            need=(
                "She needed to convert the flag-or-nothing into a clear yes-or-no answer, "
                "a boolean."
            ),
            mapping=(
                "When you extract the :private flag from metadata, the result is either "
                "the flag-object (which counts as true) or nothing (nil, which counts as false). "
                "`(boolean ...)` converts that to an explicit true or false."
            ),
            resolution=(
                "the runtime affirmed the flag's presence — meta-lookup "
                "found the privacy mark sitting on the var."
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
                "the runtime found no flag at all — meta-lookup yielded "
                "nothing, and the boolean conversion settled the matter."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-08 — Circular dependencies (we exercise via a plain form that
# would resolve correctly when the dependency graph is sound; the
# narrative carries the lesson).
G6_08 = SubjectCurriculum(grade=6, subject_id="G6-08",
    subject_title="Circular dependencies", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form='(clojure.string/upper-case "a")',
            expected="A",
            concept_phrase="calling a function from a required namespace",
            question_what="the uppercase form of the character a produced by clojure.string/upper-case",
            goal_text="call the string uppercasing function from clojure.string on the character a",
            scenario=(
                'Mossback had already used the clojure.string scroll many times. She picked it up again to ask: does the upper-case routine still work on {drawn.a} single character, the letter {drawn.a}?'
            ),
            need=(
                "She needed to call the routine on {drawn.a} tiny string — just one letter — and see whether the scroll's routine worked just as well."
            ),
            mapping=(
                "A fully-qualified routine call — clojure.string/upper-case — "
                "works the same way every time you call it, whether the input is long or short. "
                "The scroll and the routine are always there."
            ),
            resolution=(
                "the routine returned the single letter in capital form, confirming "
                "that the scroll and its routine were as reliable as ever."
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
                "Mossback wrote two namespace-like symbols on her slate: 'a.b and 'a.b. "
                "They were spelled exactly the same."
            ),
            need=(
                "She wondered: are they truly the same symbol, or could there be "
                "some invisible difference the REPL would catch?"
            ),
            mapping=(
                "Two symbols that are spelled the same are equal — the runtime "
                "checks the spelling. `(= ...)` confirms whether two values match."
            ),
            resolution=(
                "the runtime confirmed they were the same symbol, character for character."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-09 — Loading order (we exercise via straightforward sequence of
# forms inside a `do` so the REPL processes them in order).
G6_09 = SubjectCurriculum(grade=6, subject_id="G6-09",
    subject_title="Loading order", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(do (def step1 1) (def step2 (+ step1 1)) step2)",
            expected=2,
            concept_phrase="evaluating definitions in sequence to establish dependency order",
            question_what="the value of the second variable after both definitions are loaded in order",
            goal_text="define step1 as 1, then define step2 as step1 plus 1, then return step2",
            scenario=(
                "Mossback planted a sign step{drawn.a} on the road and nailed the value {drawn.a} to it. Then she planted a second sign step2 — but this one's value depended on reading the first sign first."
            ),
            need=(
                "She had to make sure the REPL would plant the signs in order: step{drawn.a} first, then step2, then ask for step2's value."
            ),
            mapping=(
                "The `do` form says: execute these forms one after another, in order. "
                "Each sign planted with `def` stays on the road for the next form to see. "
                "The runtime processes them in sequence, so step2 can read step1."
            ),
            resolution=(
                'the runtime returned the value of step2, which had been calculated by reading step{drawn.a} — a chain of dependency, in order.'           ),
            tags=("story",),
        ),
        SubjectExample(
            form="(let [a 1 b (+ a 1)] (+ a b))",
            expected=3,
            concept_phrase="establishing local bindings with dependent values",
            question_what="the sum of two variables with the second depending on the first",
            goal_text="bind a to 1, bind b to a plus 1, then return the sum of a and b",
            scenario=(
                'In her leather pouch, Mossback tucked two values in order: first, a with the value {drawn.a}; then, b with the value a plus 1. She needed them both in the pouch at the same time, so she could add them.'
            ),
            need=(
                "She needed to create the bindings in sequence — a first, then b "
                "using a's value — and then add them together."
            ),
            mapping=(
                "A `let` form tucks values into a pouch one by one, and each one "
                "can see the ones that came before it. The bindings exist only within "
                "the pouch, only for that form's duration."
            ),
            resolution=(
                "the runtime returned the sum — a plus b — which meant the pouch "
                "had held both values in the right order."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


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
        SubjectExample(
            form="(count ['race.tortoise 'race.hare 'race.shared])",
            expected=3,
            concept_phrase="counting the number of namespace symbols in a project",
            question_what="the number of namespaces in a small project",
            goal_text="count the number of namespace symbols in a vector of three namespaces",
            scenario=(
                "The library shelf held three scrolls, one for each part of the race project: "
                "race.tortoise for Mossback's cottage, race.hare for Pip's, and race.shared "
                "for the common tools they both used."
            ),
            need=(
                "Mossback wanted to count how many scrolls were on this project's shelf "
                "to make sure she had all three."
            ),
            mapping=(
                "A vector holding three namespace symbols carries three names. "
                "`(count ...)` counts how many elements are in the vector."
            ),
            resolution=(
                "the runtime returned the count — three scrolls, exactly as the shelf held them."
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
                "Mossback held a list of two scrolls: 'race.tortoise and 'race.hare. "
                "She wanted to convert each symbol into the string the scroll's spine bore."
            ),
            need=(
                "She needed the scroll-names as plain strings, one for each scroll, "
                "so she could write them on a ledger."
            ),
            mapping=(
                "`(map name ...)` applies the name-extraction to each symbol in the list, "
                "collecting the results into a new vector of strings."
            ),
            resolution=(
                "the runtime returned a vector of the two scroll-names as strings — "
                "ready for the ledger."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-13 — Aliasing conventions (we exercise via a tiny alias-style
# substitution that's purely lexical).
G6_13 = SubjectCurriculum(grade=6, subject_id="G6-13",
    subject_title="Aliasing conventions", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form='(let [s clojure.string/upper-case] (s "hare"))',
            expected="HARE",
            concept_phrase="aliasing a fully-qualified function and calling it through the alias",
            question_what="the uppercase form of the string hare when clojure.string/upper-case is called through a local alias",
            goal_text="bind the fully-qualified string uppercasing function to a local alias s and call it on hare",
            scenario=(
                "In her leather pouch, Mossback tucked a shorthand for a long name: "
                "the fully-qualified routine clojure.string/upper-case, bound to just 's'. "
                "Now when she wanted to use the routine, she could call it the short way."
            ),
            need=(
                'She needed to apply the routine to the word {drawn.a}, using only the short alias to keep the code readable.'
            ),
            mapping=(
                "A `let` binding lets you give a long name a short local alias. "
                "Inside the pouch, calling `s` invokes the routine bound to it — "
                "the fully-qualified routine without the verbose dotted name."
            ),
            resolution=(
                "the routine returned the word in capitals, accessed through the short alias."
            ),
            tags=("story",),
        ),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-14 — Import for Java classes (basilisp targets Python; we use a
# universally-available form here: predicate on a class-y name).
G6_14 = SubjectCurriculum(grade=6, subject_id="G6-14",
    subject_title="Import for host classes", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(symbol? 'java.util.List)",
            expected=True,
            concept_phrase="testing whether a value is a symbol",
            question_what="whether a dotted Java class name is a symbol",
            goal_text="test whether a Java class name written as a quoted symbol is a symbol",
            scenario=(
                "Beyond the meadow lay a foreign toolshed — the host platform's library. "
                "In that shed lived tool-names like java.util.List, written in the host's "
                "dotted-name style — a symbol from Clojure's perspective."
            ),
            need=(
                "Mossback wanted to know: is this foreign tool-name a symbol in Clojure's world?"
            ),
            mapping=(
                "A quoted name from the foreign toolshed, like 'java.util.List, is a symbol "
                "in Clojure — the mark of a thing, not the thing itself. `(symbol? ...)` "
                "tests whether a value carries that mark."
            ),
            resolution=(
                "the runtime confirmed that yes, the foreign tool-name was indeed a symbol."
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
                "Another tool-name from the foreign shed lived in her notes. "
                "Mossback wanted to know what string the symbol spelled out — "
                "the exact characters of the host tool's full name."
            ),
            need=(
                "She needed to extract the string form of the symbol so she could "
                "write it in her notes."
            ),
            mapping=(
                "A symbol, whether from the meadow or the foreign shed, can be unwrapped "
                "to its string form. `(name ...)` extracts that string."
            ),
            resolution=(
                "the runtime returned the string spelling out the foreign tool's full name (with `java.util.Map` as the input value)."
            ),
            tags=("story",),
        ),
    ], subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G6)


# G6-15 — Namespace meta (we exercise the metadata mechanism on a
# symbol via `^{:doc ...}`).
G6_15 = SubjectCurriculum(grade=6, subject_id="G6-15",
    subject_title="Namespace meta", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form='(:doc (meta \'\\{:doc "steady wins"\\} race))',
            expected="steady wins",
            concept_phrase="accessing the :doc metadata from a symbol",
            question_what="the docstring value from a symbol's metadata",
            goal_text="extract the :doc metadata value from a symbol with a docstring",
            scenario=(
                "On a scroll lay a symbol race, marked with marginalia in the margin: "
                "^{:doc \"steady wins\"}. The margin held a note — a docstring — "
                "explaining what the symbol was about."
            ),
            need=(
                "Mossback wanted to read the marginalia note — the :doc metadata "
                "that had been written in the scroll's margin."
            ),
            mapping=(
                "A symbol can carry metadata — notes in the margin, written with ^{...}. "
                "`(meta ...)` reads the marginalia, and `(:doc ...)` pulls out "
                "the docstring if it's there."
            ),
            resolution=(
                "the runtime returned the docstring from the margin — the note "
                "explaining what steady wins meant."
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
    subject_title="Cleaning up requires", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(contains? #{'clojure.string} 'clojure.string)",
            expected=True,
            concept_phrase="testing membership in a set of namespaces",
            question_what="whether a namespace is in the set of required namespaces",
            goal_text="test whether the clojure.string namespace is in the set of required namespaces",
            scenario=(
                "Mossback stood at the library shelf, holding a set of scroll-names she "
                "had borrowed: #{'clojure.string}. She wanted to check: is clojure.string "
                "in that set?"
            ),
            need=(
                "She needed to know whether she had actually taken that scroll, "
                "or if she had forgotten it."
            ),
            mapping=(
                "A set is a basket of unique names. `(contains? ...)` tests whether "
                "a name lives in the set — whether the scroll is in the basket."
            ),
            resolution=(
                "the runtime confirmed that yes, clojure.string was in the set — "
                "she had borrowed it."
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
                "Still holding the same set #{'clojure.string}, she now asked: "
                "is clojure.set in this set? Had she borrowed that scroll?"
            ),
            need=(
                "She wanted to know whether clojure.set had been taken from the shelf."
            ),
            mapping=(
                "The set holds only the scrolls in it. `(contains? ...)` checks whether "
                "a name is there — and if it's not in the basket, the answer is false."
            ),
            resolution=(
                "the runtime signalled the absence — clojure.set was not "
                "in the set she had borrowed, no membership found."
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
    print(f"grade-6 tortoise-hare smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
