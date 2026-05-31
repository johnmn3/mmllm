"""Grade 11 — interop, crossing into other runtimes. Through tortoise-hare.

Subplot lens: the tortoise crosses into a foreign land. JVM, JS, and
Python are different countries the racers visit; each has its own
customs (method-call syntax, static methods, type hints). The Hare
treats the foreign-language as just another sprint; the Tortoise is
careful to follow the local conventions.

Most interop forms are host-specific. Examples here use forms that
work in basilisp (the Python host this curriculum is trained against),
or use predicates that don't depend on which host you're on.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.tortoise_hare.grade_1 import (
    _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.tortoise_hare._metaphor_pools import (
    _ACORN_SUBPLOTS, _TOOLSHED_SUBPLOTS,
)


# ─────────────────────── grade-11 subplot extensions ───────────────────────
#
# The two have travelled past their usual meadow into a foreign country
# whose REPL hosts another runtime. The Hare wants to barge ahead in
# his usual style; the Tortoise treats every interop call as a small
# act of diplomacy.

_INTEROP_SUBPLOTS: list[SubplotTemplate] = list(_GOAL_SUBPLOTS) + [

    SubplotTemplate("""\
{tortoise_phrase} and {hare_phrase} had wandered {place} into territory
where the REPL spoke to another runtime entirely. {tortoise} read the
sign and pointed at {concept_phrase}; the form to submit, written in
the foreign convention, was {form_display}."""),

    SubplotTemplate("""\
"This is not your meadow," {tortoise_phrase} said {place}, {emo_patient}.
"Here, the methods belong to objects, and the dot has a particular
meaning." {hare_phrase}, {emo_proud}, said {hare_he_she} could read
the foreign form anyway. {tortoise} sketched {form_display} on the
ground; let the runtime, {tortoise_he_she} insisted, declare what
{concept_phrase} returned."""),

    SubplotTemplate("""\
A wooden border-post {place} marked the edge of the host runtime's
territory. The form written on it — {form_display} — captured
{concept_phrase}. {hare}, {emo_tired} from running, agreed for once
that crossing into foreign syntax called for actual evaluation, not
guessing."""),

    SubplotTemplate("""\
{hare_phrase} insisted the foreign-runtime forms were "just like home."
{tortoise_phrase} tapped a stone {place} where someone had inscribed
{concept_phrase}. "Then write {form_display} into the REPL," {tortoise}
said, "and we'll see if your familiarity holds.\""""),

    SubplotTemplate("""\
At a wayside shrine {place} dedicated to interop, the day's offering
was {concept_phrase}. {tortoise_phrase} knelt and placed the form
{form_display} on the stone. {hare}, watching, agreed to be the one
to submit it to the runtime."""),

    SubplotTemplate("""\
A merchant's stall {place} sold translated phrasebooks for the host
language; today's lesson was {concept_phrase}. {tortoise_phrase}
copied the form {form_display} from the page, and {hare_phrase}
agreed (for once) that one should always check the REPL before
trusting a translation."""),
]


def _ex(form, expected, concept, what, goal="", tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal, tags=tags)


_PLAN_G11 = _PLAN_POOL + (
    "I write the interop form using the host's convention.",
    "I use the dot or slash form for the host method, then submit.",
    "I express the host call as a Clojure form for the REPL.",
)


# ─────────────────────── 14 grade-11 subjects ───────────────────────


# G11-01 — JVM vs CLR vs JS vs Python (overview)
G11_01 = SubjectCurriculum(
    grade=11, subject_id="G11-01",
    subject_title="JVM vs CLR vs JS vs Python (host overview)",
    fable="tortoise-hare",
    examples=[
        # Overview subject — narrative does the educational work.
        _ex('(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)',
            ":studied",
            "understanding host runtimes",
            "the marker value when the host overview has been studied",
            goal="understand that Clojure runs on multiple hosts"),
        _ex('(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp" :hosts)',
            ":hosts",
            "the host runtime variants",
            "the marker keyword for the host family",
            goal="name the Clojure implementations for different hosts"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-02 — Method call syntax
G11_02 = SubjectCurriculum(
    grade=11, subject_id="G11-02",
    subject_title="Method call syntax",
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form='(.toUpperCase "abc")',
            expected="ABC",
            concept_phrase='the host method toUpperCase',
            question_what="the capitalized result the host's toUpperCase returns on the three-letter string abc",
            goal_text="call the host's toUpperCase routine on the three-letter string abc using the dot-prefix calling convention",
            scenario=(
                "Mossback the tortoise was using a small string of "
                "three letters from the foreign toolshed — `abc` — and "
                "she wanted the host's own routine for capitalizing "
                "strings, kept under the name `toUpperCase`."
            ),
            need=(
                "She didn't want to write a Clojure routine for "
                "capitalization; she wanted to call the host's own "
                "routine directly."
            ),
            mapping=(
                "Host instance methods are called with dot-prefix on "
                "the instance: `(.toUpperCase \"abc\")` invokes the "
                "host's routine on the string. The runtime crosses the "
                "boundary to the host, calls the method, and brings "
                "the result back."
            ),
            resolution=(
                "the host returned the three letters in capitals, and "
                "the runtime brought the value back as a Clojure "
                "string."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(.startsWith "hare-tortoise" "hare")',
            expected=True,
            concept_phrase="the host method startsWith checking a string prefix",
            question_what="whether the string hare-tortoise starts with the prefix hare via the host method startsWith",
            goal_text="call the host method startsWith on a string to check for a prefix",
            scenario=(
                "The tortoise had inscribed two phrases in the dust: one read "
                "'hare-tortoise' and another read just 'hare'. She wanted to know "
                "if the longer phrase began with the shorter one. The form's value to weigh was \"hare-tortoise\"."
            ),
            need=(
                "Rather than laboriously comparing letter by letter, she reached "
                "into the host's toolshed for the startsWith routine — a tool that "
                "answers exactly that question."
            ),
            mapping=(
                "The host method `startsWith` takes the instance string and a "
                "prefix, checking whether the instance begins with those exact "
                "letters. Dot-prefix syntax calls it: `(.startsWith instance prefix)`."
            ),
            resolution=(
                "the host confirmed that 'hare-tortoise' does indeed start with "
                "'hare', and the tortoise's check was settled."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(. "abc" toUpperCase)',
            expected="ABC",
            concept_phrase='the alternate dot form for a host method',
            question_what="the uppercase form of the string abc produced by the host method toUpperCase via the alternate dot syntax",
            goal_text="call the host method toUpperCase using the alternate dot form",
            scenario=(
                "Mossback had learned to call the host's toUpperCase using dot-prefix "
                "on the string. But she noticed the host allowed another syntax — "
                "dot placed before the method name instead of before the instance. The form's value to weigh was \"abc\"."
            ),
            need=(
                "She wanted to test whether this alternate form worked just as well, "
                "producing the same uppercase result on the string 'abc'."
            ),
            mapping=(
                "The alternate dot form `(. instance method)` is equivalent to "
                "`(.method instance)`. Both call the same host routine; the syntax "
                "simply reverses the order of the receiver and method name."
            ),
            resolution=(
                "the alternate form returned the three letters in capitals, proving "
                "both syntaxes reach the same host method."
            ),
            tags=("story",),
        ),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-03 — Static method call
G11_03 = SubjectCurriculum(
    grade=11, subject_id="G11-03",
    subject_title="Static method call",
    fable="tortoise-hare",
    examples=[
        # Math/abs is available across hosts as a static-style call.
        SubjectExample(
            form="(Math/abs -7)",
            expected=7,
            concept_phrase="the static host method Math/abs",
            question_what="the absolute value of the integer -7 produced by calling the static host method Math/abs via slash notation",
            goal_text="call the static host method Math/abs with the argument -7",
            scenario=(
                'The tortoise was holding a thermometer that read negative seven. She wanted the absolute distance from zero — not the negative sign, just the magnitude. The value drawn fresh was -7.'
            ),
            need=(
                "Rather than manually removing the sign, she turned to the host's "
                "standard-issue Math toolshed, where the `abs` routine lives — "
                "a static method called by the toolshed name and method name together."
            ),
            mapping=(
                "Static methods are called by toolshed-name and method-name via slash: "
                "`(Math/abs value)`. The host's Math toolshed provides the method; "
                "slash notation calls it without an instance."
            ),
            resolution=(
                "the host returned seven — the absolute magnitude of the negative "
                "number, and the tortoise's distance measure was clear."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(Math/max 3 9)",
            expected=9,
            concept_phrase="the static host method Math/max",
            question_what="the maximum value of the integers 3 and 9 produced by calling the static host method Math/max via slash notation",
            goal_text="call the static host method Math/max to find the larger of two numbers",
            scenario=(
                'Pip the hare had run two races, recording speeds of 3 units and 9 units. The tortoise wanted to find which speed was faster — the larger of the two.'
            ),
            need=(
                "Rather than eyeball the numbers, she called on the host's static "
                "`Math/max` routine — another standard-issue tool in the host's "
                "toolshed, invoked by slash notation."
            ),
            mapping=(
                "`Math/max` is a static method called via `(Math/max a b)`. "
                "Like `Math/abs`, it lives in the host's Math toolshed and is "
                "summoned by toolshed-name, slash, and method-name."
            ),
            resolution=(
                "the host compared the two speeds and returned 9 — the larger, confirming Pip's second sprint had been faster."
            ),
            tags=("story",),
        ),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-04 — Field access
G11_04 = SubjectCurriculum(
    grade=11, subject_id="G11-04",
    subject_title="Field access",
    fable="tortoise-hare",
    examples=[
        # Field access on a host object — count is a property/method
        # depending on host. We use a portable example using the
        # `.length` style on a string-like host where applicable.
        SubjectExample(
            form='(count "tortoise")',
            expected=8,
            concept_phrase='the count of a sequence',
            question_what='the number of characters in the string tortoise via the count function',
            goal_text="count the characters in a string",
            scenario=(
                "Mossback's name was written on a scroll: 't-o-r-t-o-i-s-e'. "
                "She wanted to know how many letters spelled her name, but counting "
                "by paw was slow."
            ),
            need=(
                "The host provided a `count` routine that reads the length of "
                "strings and sequences — a tool for quickly answering 'how many?'"
            ),
            mapping=(
                "The `count` function (or method, depending on the host) takes a "
                "string or sequence and returns the number of elements it holds. "
                "Called as `(count string)`, it answers the length question directly."
            ),
            resolution=(
                'the host counted out eight letters in her name, and the {drawn.a} had her answer without lifting a paw.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(count "hare")',
            expected=4,
            concept_phrase='the count of a sequence',
            question_what='the number of characters in the string hare via the count function',
            goal_text="count the characters in another string",
            scenario=(
                "Pip the {drawn.a}'s name was written beside Mossback's. She wanted to count his name too, using the same routine."
            ),
            need=(
                "The same `count` tool works on any string, so the tortoise could "
                "apply it to Pip's shorter name."
            ),
            mapping=(
                "`count` is generic — the same routine works on Mossback's name, "
                "Pip's name, or any other string. The host runs the same operation, "
                "returning the length regardless of the input."
            ),
            resolution=(
                "the host returned four, the number of letters in Pip's name, and "
                "the tortoise saw at once that her name was longer."
            ),
            tags=("story",),
        ),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-05 — Import form
G11_05 = SubjectCurriculum(
    grade=11, subject_id="G11-05",
    subject_title="Import form",
    fable="tortoise-hare",
    examples=[
        # Overview-ish: the form is what one would write at the top of a file.
        _ex('(do "(:import (java.util Date)) imports a host class" :imported)',
            ":imported",
            "importing a host class",
            "the marker for the import-form lesson",
            goal="understand how to import a host class into a namespace"),
        _ex('(do "import is a top-of-file ns clause" :studied)',
            ":studied",
            "import as a namespace clause",
            "the marker for studying import",
            goal="understand where import forms go in a file"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-06 — new and dot-construct
G11_06 = SubjectCurriculum(
    grade=11, subject_id="G11-06",
    subject_title="new and dot-construct",
    fable="tortoise-hare",
    examples=[
        # Construct a host class via Class. or (new Class). String. is
        # portable across JVM and basilisp.
        SubjectExample(
            form='(String. "go")',
            expected="go",
            concept_phrase='constructing a String via the dot-construct form',
            question_what='the newly constructed String object created from a text argument via the dot-construct syntax',
            goal_text="construct a host String object with the dot-construct syntax",
            scenario=(
                "The tortoise wanted to build a fresh String from raw materials — "
                "the letters 'go'. Instead of crafting it by hand, she reached into "
                "the host's toolshed for the String constructor."
            ),
            need=(
                "The host provides tools to construct new objects. A String "
                "constructor takes text and produces a fresh String instance — "
                "a tool to build what didn't exist before."
            ),
            mapping=(
                "The dot-construct form `(Class. args)` calls the host's "
                "constructor for that class. `(String. \"go\")` constructs a fresh "
                "String from the text, using the dot-construct syntax."
            ),
            resolution=(
                "the host built a new String from the letters 'go', and the "
                "tortoise held a fresh object ready for use."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(new String "jump")',
            expected="jump",
            concept_phrase='constructing a String via the new form',
            question_what='the newly constructed String object created from a text argument via the new keyword',
            goal_text="construct a host String object using the new keyword",
            scenario=(
                "The tortoise wanted to construct another String, this time from the letters 'jump'. She knew the dot-construct worked, but the host also offered an alternate form: the `new` keyword."
            ),
            need=(
                "Testing the alternate construction syntax, she wanted to confirm "
                "it produced the same result as dot-construct."
            ),
            mapping=(
                "The `new` form `(new Class args)` is an alternate syntax for the "
                "dot-construct `(Class. args)`. Both call the host's constructor; "
                "only the syntax order changes."
            ),
            resolution=(
                "the host built a fresh String from 'jump', proving the alternate `new` keyword invokes the same constructor as dot-construct."
            ),
            tags=("story",),
        ),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-07 — Arrays
G11_07 = SubjectCurriculum(
    grade=11, subject_id="G11-07",
    subject_title="Arrays",
    fable="tortoise-hare",
    examples=[
        # int-array / aget are the canonical interop calls.
        SubjectExample(
            form="(let [a (int-array [10 20 30])] (aget a 1))",
            expected=20,
            concept_phrase="indexing into a host array",
            question_what="the element at index 1 of the int-array [10 20 30] via the aget function",
            goal_text="access an element in a host array by index",
            scenario=(
                'The tortoise constructed a host primitive array — a row of integers arranged side by side: 10, 20, 30. She wanted to reach in and pluck out the element at position 20 (the second position).'
            ),
            need=(
                "Host arrays store values in fixed positions, numbered from zero. "
                "She needed a tool to read from a specific position — the host's "
                "`aget` (array-get) routine."
            ),
            mapping=(
                'The `aget` function takes a host array and an index, returning the element at that position. `(aget a 20)` reads position 20 from array `a`, where position 0 is the first element, position 20 the second.'
            ),
            resolution=(
                'the host returned the value at position 20 — the number 20 — plucked from its place in the row.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(let [a (int-array [1 2 3])] (alength a))",
            expected=3,
            concept_phrase="getting the length of a host array",
            question_what="the length of the int-array [1 2 3] via the alength function",
            goal_text="get the length of a host array",
            scenario=(
                'The tortoise built another host array — this time holding three integers: 1, 2, 3. She wanted to know how many positions the array held. The value drawn fresh was 1.'
            ),
            need=(
                "Like strings and sequences, host arrays have a length — a tool to "
                "ask 'how many slots?' The host provides `alength` (array-length) "
                "for this."
            ),
            mapping=(
                "The `alength` function takes a host array and returns the number "
                "of positions it holds. `(alength a)` counts the slots without "
                "walking through them one by one."
            ),
            resolution=(
                "the host confirmed the array's exact slot-count, the "
                "row's length matching what had been allocated."
            ),
            tags=("story",),
        ),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-08 — Type hints
G11_08 = SubjectCurriculum(
    grade=11, subject_id="G11-08",
    subject_title="Type hints",
    fable="tortoise-hare",
    examples=[
        # Type hints don't change the value; they hint the compiler.
        SubjectExample(
            form='(let [^String s "abc"] (.toUpperCase s))',
            expected="ABC",
            concept_phrase="using a type hint in a binding",
            question_what="the uppercase form of the type-hinted string abc produced by calling the host method toUpperCase on the binding",
            goal_text="add a type hint to a binding and call a method on the typed value",
            scenario=(
                "The tortoise bound the string 'abc' to a name and wanted to call "
                "the host's toUpperCase method on it. But she wanted to mark the "
                "binding with a small tag telling the host what kind of tool it was. The form's value to weigh was \"abc\"."
            ),
            need=(
                "A type hint — a small mark on the binding — guides the host's "
                "compiler. It says 'this value is a String', helping the compiler "
                "choose the fastest path to the method."
            ),
            mapping=(
                "The `^Type binding` syntax marks a binding with a type hint. "
                "`^String s` means 's holds a String'. The host compiler then knows "
                "the exact method to call without guessing at runtime."
            ),
            resolution=(
                "the host used the type hint to call the right method directly, "
                "returning the three letters in capitals."
            ),
            tags=("story",),
        ),
        _ex('(do "type hints are metadata that guide compilation" :studied)',
            ":studied",
            "the purpose of type hints in Clojure",
            "the marker keyword for the type-hint lesson",
            goal="understand that type hints guide compilation"),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-09 — Checked vs unchecked math
G11_09 = SubjectCurriculum(
    grade=11, subject_id="G11-09",
    subject_title="Checked vs unchecked math",
    fable="tortoise-hare",
    examples=[
        # Plain arithmetic works the same way for ordinary values; the
        # checked/unchecked distinction is about overflow at the host
        # primitive level. Use a value-space form for the eval, narrate
        # the distinction.
        SubjectExample(
            form="(+ 1 2)",
            expected=3,
            concept_phrase="basic addition under the default checked math regime",
            question_what="the sum of two numbers",
            goal_text="add two numbers with the default math behavior",
            scenario=(
                "The tortoise was counting acorns — one in one pouch, two in "
                "another. She wanted to add them together and know the total, with "
                "the host's arithmetic keeping careful watch for overflow."
            ),
            need=(
                "Arithmetic in the host happens in one of two modes: checked "
                "(the default, watching for overflow) or unchecked (trusting the "
                "operation to succeed). By default, the host checks."
            ),
            mapping=(
                "The `+` form runs with checked arithmetic by default — if the sum would overflow the host's primitive size, the host catches it. Ordinary values like {drawn.a} and {drawn.b} don't overflow, so the sum is safe."
            ),
            resolution=(
                'the host returned the safe sum of {drawn.a} and {drawn.b}, overflow checking standing ready in case it had been needed.'
            ),
            tags=("story",),
        ),
        _ex('(do "*unchecked-math* turns off overflow checking on prims" :studied)',
            ":studied",
            "overflow checking in Clojure arithmetic",
            "the marker for the checked/unchecked lesson",
            goal="understand how to disable overflow checking"),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-10 — ClojureScript overview
G11_10 = SubjectCurriculum(
    grade=11, subject_id="G11-10",
    subject_title="ClojureScript overview",
    fable="tortoise-hare",
    examples=[
        _ex('(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)',
            ":studied",
            "the ClojureScript compilation process",
            "the marker for studying the cljs host",
            goal="understand how ClojureScript compiles to JavaScript"),
        _ex('(do "cljs runs in browsers and Node, with JS interop syntax" :cljs)',
            ":cljs",
            "where ClojureScript runs",
            "the marker for the cljs-runtime lesson",
            goal="learn where ClojureScript executes"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-11 — cljs-js interop
G11_11 = SubjectCurriculum(
    grade=11, subject_id="G11-11",
    subject_title="cljs / JavaScript interop",
    fable="tortoise-hare",
    examples=[
        _ex('(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)',
            ":studied",
            "ClojureScript to JavaScript interop",
            "the marker for the cljs-js interop lesson",
            goal="understand how ClojureScript calls JavaScript globals and reads fields"),
        _ex('(do "js/<name> namespaces JS globals; .- prefix marks field access" :cljs-interop)',
            ":cljs-interop",
            "ClojureScript interop conventions",
            "the marker keyword for the conventions",
            goal="learn the conventions for ClojureScript-JavaScript interop"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-12 — Basilisp overview (the Python host — this project!)
G11_12 = SubjectCurriculum(
    grade=11, subject_id="G11-12",
    subject_title="Basilisp overview (Python host)",
    fable="tortoise-hare",
    examples=[
        _ex('(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)',
            ":studied",
            "the basilisp implementation",
            "the marker for studying basilisp",
            goal="understand that basilisp is Clojure on Python"),
        _ex('(do "basilisp interops with Python via the same dot-syntax conventions" :basilisp)',
            ":basilisp",
            "basilisp Python interop",
            "the marker keyword for basilisp interop",
            goal="learn how basilisp calls Python code"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-13 — Cross-platform .cljc and reader-conditionals
G11_13 = SubjectCurriculum(
    grade=11, subject_id="G11-13",
    subject_title="Cross-platform .cljc and reader-conditionals",
    fable="tortoise-hare",
    examples=[
        _ex('(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)',
            ":studied",
            "selecting code by host at read time",
            "the marker for the reader-conditional lesson",
            goal="learn how reader-conditionals choose code per host"),
        _ex('(do ".cljc files share code across multiple hosts" :cljc)',
            ":cljc",
            "files that work on multiple Clojure hosts",
            "the marker keyword for the .cljc lesson",
            goal="understand the role of .cljc files"),
    ],
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-14 — Debugging host leaks
G11_14 = SubjectCurriculum(
    grade=11, subject_id="G11-14",
    subject_title="Debugging host leaks",
    fable="tortoise-hare",
    examples=[
        _ex('(do "host stack traces leak through interop; learn to read them" :studied)',
            ":studied",
            "debugging host-runtime errors",
            "the marker for the host-leaks lesson",
            goal="learn to read and debug host runtime errors"),
        SubjectExample(
            form='(try (Math/sqrt 4) (catch Exception _ :err))',
            expected=2.0,
            concept_phrase="catching exceptions from a host method call",
            question_what="the square root of 4 produced by the static host method Math/sqrt via slash notation when the call succeeds",
            goal_text="wrap a static host method call in error handling",
            scenario=(
                "The tortoise wanted to compute the square root of 4 using the host's Math/sqrt routine. But she knew that calling into the host sometimes raised errors — and she wanted to guard against them."           ),
            need=(
                "When host methods are called, exceptions can leak through the "
                "interop boundary. A try/catch wrapper catches those exceptions, "
                "letting the form continue if things go wrong."
            ),
            mapping=(
                "The `try` form wraps the host call; `(catch Exception _ :err)` "
                "catches any exception the host raises and returns `:err` instead. "
                "If the host call succeeds, the value passes through."
            ),
            resolution=(
                'the host computed the square root of 4 (the value 2.0) without raising an error, so the try passed the result through cleanly.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# ─────────────────────── registry ───────────────────────


SUBJECTS: dict[str, SubjectCurriculum] = {s.subject_id: s for s in (
    G11_01, G11_02, G11_03, G11_04, G11_05, G11_06, G11_07,
    G11_08, G11_09, G11_10, G11_11, G11_12, G11_13, G11_14,
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
    print(f"grade-11 tortoise-hare smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
