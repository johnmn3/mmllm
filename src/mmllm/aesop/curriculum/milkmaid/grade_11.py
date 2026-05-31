"""Grade 11 — interop, crossing into other runtimes. through the milkmaid fable.

Subplot lens: the tortoise crosses into a foreign land. JVM, JS, and
Python are different countries the racers visit; each has its own
customs (method-call syntax, static methods, type hints). The Milkmaid
treats the foreign-language as just another sprint; the Farmer is
careful to follow the local conventions.

Most interop forms are host-specific. Examples here use forms that
work in basilisp (the Python host this curriculum is trained against),
or use predicates that don't depend on which host you're on.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.milkmaid.grade_1 import (
    _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.milkmaid._metaphor_pools import (
    _ACORN_SUBPLOTS, _TOOLSHED_SUBPLOTS,
)


# ─────────────────────── grade-11 subplot extensions ───────────────────────
#
# The two have travelled past their usual meadow into a foreign country
# whose REPL hosts another runtime. The Milkmaid wants to barge ahead in
# his usual style; the Farmer treats every interop call as a small
# act of diplomacy.

_INTEROP_SUBPLOTS: list[SubplotTemplate] = list(_GOAL_SUBPLOTS) + [

    SubplotTemplate("""\
{farmer_phrase} and {milkmaid_phrase}, {emo_boastful} had wandered {place} into territory
where the REPL spoke to another runtime entirely. {farmer} read the
sign and pointed at {concept_phrase}; the form to submit, written in
the foreign convention, was {form_display}."""),

    SubplotTemplate("""\
"This is not your meadow," {farmer_phrase} said {place}, {emo_patient}.
"Here, the methods belong to objects, and the dot has a particular
meaning." {milkmaid_phrase}, {emo_proud}, said {milkmaid_he_she} could read
the foreign form anyway. {farmer} sketched {form_display} on the
ground; let the runtime, {farmer_he_she} insisted, declare what
{concept_phrase} returned."""),

    SubplotTemplate("""\
A wooden border-post {place} marked the edge of the host runtime's
territory. The form written on it — {form_display} — captured
{concept_phrase}. {milkmaid}, {emo_tired} from running, agreed for once
that crossing into foreign syntax called for actual evaluation, not
guessing."""),

    SubplotTemplate("""\
{milkmaid_phrase}, {emo_boastful} insisted the foreign-runtime forms were "just like home."
{farmer_phrase} tapped a stone {place} where someone had inscribed
{concept_phrase}. "Then write {form_display} into the REPL," {farmer}
said, "and we'll see if your familiarity holds.\""""),

    SubplotTemplate("""\
At a wayside shrine {place} dedicated to interop, the day's offering
was {concept_phrase}. {farmer_phrase} knelt and placed the form
{form_display} on the stone. {milkmaid}, {emo_boastful}, watching, agreed to be the one
to submit it to the runtime."""),

    SubplotTemplate("""\
A merchant's stall {place} sold translated phrasebooks for the host
language; today's lesson was {concept_phrase}. {farmer_phrase}
copied the form {form_display} from the page, and {milkmaid_phrase}, {emo_boastful}
agreed (for once) that one should always check the REPL before
trusting a translation."""),
]


def _ex(form, expected, concept, what, goal=""):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal)


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
    fable="milkmaid",
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form='(.toUpperCase "abc")',
            expected="ABC",
            concept_phrase='the host method toUpperCase',
            question_what="the capitalized result the host's toUpperCase returns on the three-letter string abc",
            goal_text="call the host's toUpperCase routine on the three-letter string abc using the dot-prefix calling convention",
            scenario=(
                "The milkmaid needed to borrow the neighbor's milking stool — a "
                "well-made host method called `toUpperCase` — rather than build one "
                "herself. She had the string 'abc' in her pail and needed it "
                "returned in its capitalized form."
            ),
            need=(
                "She needed to call the neighbor's host method directly — borrow the "
                "tool by its true name, pass the string, and receive what the method "
                "was built to return."
            ),
            mapping=(
                "The dot-prefix `(.toUpperCase ...)` is the borrowed milking stool: "
                "the dot names the neighbor's convention, `toUpperCase` is the "
                "stool's use, and the string is placed on it. The milkmaid does not "
                "rebuild the method — she borrows it by name."
            ),
            resolution=(
                "The REPL returned the host method's answer — the string in the form "
                "the method was designed to produce, exactly as the neighbor's "
                "tool was built to deliver — abc."
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
                "The milkmaid had a string 'hare-tortoise' and wondered if it began with "
                "'hare'. Rather than inspect it by hand, she sought the neighbor's tool — "
                "the startsWith method — which was designed to answer just such a question."
            ),
            need=(
                "She needed to call the host method directly using the dot-prefix convention, "
                "passing the string and the prefix she wanted to check."
            ),
            mapping=(
                "The dot-prefix `(.startsWith ...)` borrows the neighbor's tool; the string "
                "and the prefix are what she placed in the method's hands. The tool returns "
                "a verdict: true if the string begins with the prefix, false otherwise."
            ),
            resolution=(
                "The REPL returned the method's verdict — a boolean answer the host method "
                "was built to deliver."
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
                "The milkmaid had another string 'abc' and wished to borrow the same "
                "neighbor's tool — toUpperCase — but this time using the alternate dot form, "
                "which places the object before the method name."
            ),
            need=(
                "She needed to learn that the neighbor's method could be called in a second way, "
                "with the string object positioned differently in the form."
            ),
            mapping=(
                "The alternate dot form still borrows the neighbor's "
                "tool; only the order changes. The string comes first, then the method name; "
                "both conventions work — the neighbor's well-made stool delivers the same result."
            ),
            resolution=(
                "The REPL returned the host method's answer — the string capitalized, "
                "exactly as the first dot form had delivered."
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
    fable="milkmaid",
    examples=[
        # Math/abs is available across hosts as a static-style call.
        SubjectExample(
            form="(Math/abs -7)",
            expected=7,
            concept_phrase="the static host method Math/abs",
            question_what="the absolute value of the integer -7 produced by calling the static host method Math/abs via slash notation",
            goal_text="call the static host method Math/abs with the argument -7",
            scenario=(
                "The milkmaid had counted a debt of negative seven coins — a loss in the tally. "
                "She needed to borrow the neighbor's tallying tool, Math/abs, which strips away "
                "the sign and leaves only the magnitude."
            ),
            need=(
                "She needed to call the static method using the slash convention — a borrowed "
                "tool from the host's Math library, not from any object."
            ),
            mapping=(
                "The slash form `(Math/abs ...)` borrows a tool from the Math library itself; "
                "the slash names the library and the tool within it. The integer is tallied, "
                "and the absolute value is returned — the coin count stripped of its sign."
            ),
            resolution=(
                "The REPL returned the magnitude — the debt tallied as a positive number, — -7 "
                "exactly the absolute value the neighbor's tallying tool was built to produce."
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
                "The milkmaid had two coin tallies — 3 and 9 — and needed to count which was "
                "the larger sum. She borrowed the neighbor's tool, Math/max, which compares "
                "numbers and returns the bigger one."
            ),
            need=(
                "She needed to call the static method from the Math library using the slash "
                "convention, passing both numbers for comparison."
            ),
            mapping=(
                "The slash form `(Math/max 3 9)` borrows another tallying tool from the Math "
                "library. The two coin counts are compared, and the greater is returned. "
                "The slash notation is the borrowing convention for library tools."
            ),
            resolution=(
                "The REPL returned the larger tally — the maximum of the two numbers, "
                "exactly what the neighbor's comparison tool was built to deliver."
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
    fable="milkmaid",
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
                "The milkmaid had the name 'tortoise' written on a scroll and needed to tally "
                "how many letters it held. She borrowed the neighbor's counting tool — a method "
                "from the host that traverses strings and returns their length."
            ),
            need=(
                "She needed to call the host's length-counting function, passing the string "
                "to be measured."
            ),
            mapping=(
                "The count function borrows the host's ability to measure strings. The string "
                "'tortoise' is placed in the function, and it returns the tally of characters — "
                "a precise count the host delivers."
            ),
            resolution=(
                "The REPL returned the character count — the number of letters in the string, "
                "exactly as the host's counting tool was built to produce."
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
                "The milkmaid had another name — 'hare' — and again needed a tally of its "
                "letters. She called the same neighbor's tool, the count function, which was "
                "as reliable for short strings as for long ones."
            ),
            need=(
                "She needed to call the host's counting function again, this time on a "
                "different string."
            ),
            mapping=(
                "The count function works the same way each time: the string 'hare' is "
                "measured, and the host returns its length. The borrowing convention is "
                "unchanged — the tool works on any string placed before it."
            ),
            resolution=(
                "The REPL returned the character count — a smaller tally than before, "
                "exactly what the host's counting tool was built to deliver."
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
    fable="milkmaid",
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
    fable="milkmaid",
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
                "The milkmaid needed to craft a new String using the neighbor's forge — the "
                "host String constructor. Rather than build a string from scratch, she borrowed "
                "the neighbor's tool, which had been built to take text and forge it into a "
                "proper String object."
            ),
            need=(
                "She needed to call the host's constructor using the dot-construct convention, "
                "passing the text she wished to forge."
            ),
            mapping=(
                "The dot-construct `(String. \"go\")` borrows the neighbor's forge; the dot "
                "names the constructor, and the text is placed in its hands. A new String object "
                "is forged and returned — the same text, now properly shaped by the host."
            ),
            resolution=(
                "The REPL returned the newly constructed String — a host object built from "
                "the text, exactly as the neighbor's forge was designed to deliver."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(new String "leap")',
            expected="leap",
            concept_phrase='constructing a String via the new form',
            question_what='the newly constructed String object created from a text argument via the new keyword',
            goal_text="construct a host String object using the new keyword",
            scenario=(
                "The milkmaid had another short word to forge, and this time tried the "
                "neighbor's alternate form: the new keyword. The forge was the same; only "
                "the borrowing convention differed."
            ),
            need=(
                "She needed to call the host's constructor using the new keyword form, "
                "passing the text she wished to shape."
            ),
            mapping=(
                "The new form is another path to the same forge. "
                "The new keyword names the constructor, the String class is specified, and "
                "the text is forged. Both conventions — dot-construct and new — work; both "
                "are borrowing customs from the host."
            ),
            resolution=(
                "The REPL returned the newly constructed String — a host object built from — leap "
                "the text, exactly as the neighbor's forge delivers the same result."
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
    fable="milkmaid",
    examples=[
        # int-array / aget are the canonical interop calls.
        SubjectExample(
            form="(let [a (int-array [10 20 30])] (aget a 1))",
            expected=20,
            concept_phrase="indexing into a host array",
            question_what="the element at index 1 of the array",
            goal_text="access an element in a host array by index",
            scenario=(
                "The milkmaid had borrowed the neighbor's pail — a host array holding three "
                "coin counts. She needed to fetch the value at index 1 from the pail."
            ),
            need=(
                "She needed to call the host's array-access function, passing the array and index."
            ),
            mapping=(
                "The aget function reaches into arrays and returns the value at the requested index — "
                "the borrowing convention for accessing a host array's contents."
            ),
            resolution=(
                "The REPL returned the element at index 1, exactly as the host's tool was built to deliver (with `10` as the input value)."
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
                "The milkmaid had another pail from the neighbor — a host array holding three "
                "coin counts: 1, 2, 3. She needed to know how many coins were in the pail. "
                "She called the neighbor's alength tool, which was built to count the slots "
                "in any array."
            ),
            need=(
                "She needed to call the host's array-length function, passing the array to "
                "be measured."
            ),
            mapping=(
                "The alength function borrows the host's ability to measure arrays. The array "
                "is placed in the function, and it counts the slots and returns the length — "
                "the borrowing convention for measuring a host array's size."
            ),
            resolution=(
                "The REPL returned the array length — the number of slots in the pail, "
                "exactly as the host's array-measurement tool was built to deliver."
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
    fable="milkmaid",
    examples=[
        # Type hints don't change the value; they hint the compiler.
        SubjectExample(
            form='(let [^String s "abc"] (.toUpperCase s))',
            expected="ABC",
            concept_phrase="using a type hint in a binding",
            question_what="the uppercase form of the hinted string produced by calling toUpperCase",
            goal_text="add a type hint to a binding and call a method on the typed value",
            scenario=(
                "The milkmaid had a string and wanted to tell the compiler its type — a String. "
                "She added a type hint on the binding to guide the compiler, then called toUpperCase."
            ),
            need=(
                "She needed to annotate the binding with a type hint, then call the host method."
            ),
            mapping=(
                "The caret is a type hint — a mark telling the compiler the binding's type. "
                "The host method is then called, and the compiler optimizes the call. "
                "The hint does not change the abc; it guides the compiler."
            ),
            resolution=(
                "The REPL returned the capitalized string — the host method's answer, optimized by type guidance."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(do "type hints are metadata that guide compilation" :studied)',
            expected=":studied",
            concept_phrase="the purpose of type hints in Clojure",
            question_what="the marker keyword for the type-hint lesson",
            goal_text="understand that type hints guide compilation",
            scenario=(
                "The milkmaid and farmer discussed the nature of type hints as they walked "
                "past the compiler's post. The farmer explained that hints were whispers to "
                "the compiler, not commands to the runtime — they shaped how code was "
                "optimized before it ran."
            ),
            need=(
                "She needed to understand that type hints guide compilation, not alter the "
                "value returned."
            ),
            mapping=(
                "Type hints are metadata — markers attached to bindings and declarations. "
                "They whisper to the compiler: this value will be of this type. The compiler "
                "listens and optimizes accordingly. The hints are scaffolding for the compiler, "
                "not for the runtime."
            ),
            resolution=(
                "The REPL returned the marker — a keyword confirming the lesson was absorbed. "
                "Type hints had been understood as compiler guidance, exactly as the farmer "
                "had explained — type hints are metadata that guide compilation."
            ),
            tags=("story",),
        ),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-09 — Checked vs unchecked math
G11_09 = SubjectCurriculum(
    grade=11, subject_id="G11-09",
    subject_title="Checked vs unchecked math",
    fable="milkmaid",
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
                "The milkmaid was tallying coins at the neighbor's farm. She had one coin and "
                "added two more. The tally was kept with the default checked arithmetic — the "
                "host's way of guarding against overflow."
            ),
            need=(
                "She needed to add the two tallies using the plain addition operator and let "
                "the default checked arithmetic do its work."
            ),
            mapping=(
                "The addition `(+ 1 2)` tallies two coin counts. The result is a sum. Under the "
                "default checked regime, the host watches for overflow — if the numbers grew so "
                "large they spilled past the primitive's capacity, the host would warn. The farmer "
                "trusts the host's guard; the milkmaid adds without fear."
            ),
            resolution=(
                "The REPL returned the sum — the tally tallied under the default checked math, "
                "exactly as the host's arithmetic was built to deliver."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(do "*unchecked-math* turns off overflow checking on prims" :studied)',
            expected=":studied",
            concept_phrase="overflow checking in Clojure arithmetic",
            question_what="the marker for the checked/unchecked lesson",
            goal_text="understand how to disable overflow checking",
            scenario=(
                "The farmer was teaching the milkmaid about overflow — what happens when a tally "
                "grows so large it overflows the primitive's boundaries. He explained that "
                "*unchecked-math* was a switch the farmer could throw to turn off the guard and "
                "let arithmetic overflow without complaint."
            ),
            need=(
                "She needed to understand that overflow checking is the default, and that "
                "*unchecked-math* disables it for performance when the farmer accepts the risk."
            ),
            mapping=(
                "*unchecked-math* is a flag — a switch on the neighbor's farm. When it is true, "
                "the host's overflow guard is silenced. Arithmetic runs faster because no one is "
                "watching for spills. The milkmaid learns that the farmer sometimes trades safety "
                "for speed; this is the trade-off *unchecked-math* embodies."
            ),
            resolution=(
                "The REPL returned the marker — a keyword confirming the lesson was understood. "
                "Overflow checking had been grasped as the default, *unchecked-math* as the "
                "switch to disable it — *unchecked-math* turns off overflow checking on prims."
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-10 — ClojureScript overview
G11_10 = SubjectCurriculum(
    grade=11, subject_id="G11-10",
    subject_title="ClojureScript overview",
    fable="milkmaid",
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
    fable="milkmaid",
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
    fable="milkmaid",
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
    fable="milkmaid",
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form='(do "host stack traces leak through interop; learn to read them" :studied)',
            expected=":studied",
            concept_phrase="debugging host-runtime errors",
            question_what="the marker for the host-leaks lesson",
            goal_text="learn to read and debug host runtime errors",
            scenario=(
                "The milkmaid had borrowed a tool from the host that went wrong. An error "
                "erupted — a stack trace from the host runtime leaked through the Clojure REPL "
                "like flood water breaching a dam. The farmer explained that such leaks were "
                "common when borrowing from the host and that learning to read them was crucial."
            ),
            need=(
                "She needed to understand that host errors sometimes spill into the REPL and "
                "that reading those traces is part of debugging interop code."
            ),
            mapping=(
                "Host stack traces are the host's voice crying out when something goes wrong. "
                "They leak through interop because the REPL and the host are neighbors sharing "
                "a boundary. The farmer teaches: read the trace as a message from the host. "
                "Understand its conventions, and you'll know what went wrong."
            ),
            resolution=(
                "The REPL returned the marker — a keyword confirming the lesson was grasped. "
                "Host leaks had been understood as debugging tools, not obstacles — host stack traces leak through interop; learn to read them."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(try (Math/sqrt 4) (catch Exception _ :err))',
            expected=2.0,
            concept_phrase="catching exceptions from a host method call",
            question_what="the square root of 4 produced by the static host method Math/sqrt via slash notation when the call succeeds",
            goal_text="wrap a static host method call in error handling",
            scenario=(
                "The milkmaid was trying to borrow the neighbor's Math tool — the square root "
                "function — to measure the side of a square field that held 4 coin-stacks. But "
                "the farmer insisted on wrapping the call in error handling, in case the host "
                "threw an exception that would crash their calculation."
            ),
            need=(
                "She needed to call the host's Math/sqrt method while guarding against exceptions "
                "the host might throw."
            ),
            mapping=(
                "The try-catch form wraps the borrowed tool. The try block holds the Math/sqrt "
                "call; if the host succeeds, the result is returned. If the host throws an "
                "exception, the catch block silently returns an error marker, :err. The farmer "
                "teaches: borrowing from the host is safe when you prepare for the host's warnings."
            ),
            resolution=(
                "The REPL returned the square root — the host method's answer when it succeeded. "
                "No exception was thrown; the borrowed tool worked as designed, and the farmer's "
                "caution proved unnecessary but wise."
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
