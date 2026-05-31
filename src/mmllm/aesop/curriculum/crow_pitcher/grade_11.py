"""Grade 11 — interop, crossing into other runtimes. Through crow-pitcher.

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
from mmllm.aesop.curriculum.crow_pitcher.grade_1 import (
    _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.crow_pitcher._metaphor_pools import (
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
    fable="crow-pitcher",
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form='(.toUpperCase "abc")',
            expected="ABC",
            concept_phrase='the host method toUpperCase',
            question_what="the capitalized result the host's toUpperCase returns on the three-letter string abc",
            goal_text="call the host's toUpperCase routine on the three-letter string abc using the dot-prefix calling convention",

            scenario=(
                "Korvus borrowed a smooth earthenware vessel at the road's "
                "edge — a tool fired by the Java potter, not the Clojure one. "
                "The vessel had a method scratched on its side: toUpperCase, "
                "ready for any letter-stone."
            ),
            need=(
                "He needed to pass the letter-stone 'abc' through the "
                "Java vessel's method and read back what the human "
                "potter's tool returned."
            ),
            mapping=(
                "The dot-call syntax borrows a Java method. The first "
                "argument is the object whose method is called; the runtime "
                "reaches into the Java side and applies it. The result comes "
                "back to the Clojure pitcher as a value."
            ),
            resolution=(
                "'ABC' — the borrowed vessel's method returned the "
                "uppercased string, settling at beak-reach."
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
                "Caw found a Java vessel at the market with a method scratched "
                "on its rim: startsWith. She fed it the stone 'hare-tortoise' "
                "and a small prefix-stone 'hare', then held it over the pitcher."
            ),
            need=(
                "She needed to know whether the vessel's method would confirm "
                "the longer stone began with the prefix-stone."
            ),
            mapping=(
                "The dot-call borrows the Java vessel's startsWith method. "
                "The object receives the call; the prefix stone is the argument. "
                "The runtime bridges into the Java side and returns the verdict."
            ),
            resolution=(
                "The borrowed vessel's method settled at beak-reach with its verdict."
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
                "Sable paused at the orchard's edge with the same Java vessel "
                "Korvus had used before, but wanted to try the alternate "
                "inscription: dot first, then the vessel, then the method name."
            ),
            need=(
                "Sable needed to confirm the alternate dot notation reached "
                "the same method inside the same borrowed earthenware vessel."
            ),
            mapping=(
                "The `(. obj method)` form is the alternate dot syntax for "
                "host method calls. Object and method swap positions but the "
                "runtime still bridges into the Java vessel the same way."
            ),
            resolution=(
                "The alternate-dot inscription returned the borrowed vessel's method result at beak-reach. (count: -7) (with `abc` as the input value)"
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
    fable="crow-pitcher",
    examples=[
        # Math/abs is available across hosts as a static-style call.
        SubjectExample(
            form="(Math/abs -7)",
            expected=7,
            concept_phrase="the static host method Math/abs",
            question_what="the absolute value of the integer -7 produced by calling the static host method Math/abs via slash notation",
            goal_text="call the static host method Math/abs with the argument -7",

            scenario=(
                "Korvus found a standard-issue vessel at the hilltop — the "
                "human potter's Math class, etched with absolute-value marks. "
                "He dropped the stone -7 into the slash-named method's slot."
            ),
            need=(
                "He needed the vessel to strip the negative sign and return "
                "the plain distance from zero for the stone he had dropped."
            ),
            mapping=(
                "The slash notation calls a static method on the Java class "
                "directly — no object instance needed. Math/abs reaches into "
                "the human potter's standard library and applies the rule to "
                "the stone's value."
            ),
            resolution=(
                "The standard-issue vessel's absolute-value method returned "
                "its result at beak-reach."
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
                "Caw laid two stones at the farm — one marked 3, one marked 9. "
                "She reached for the human potter's Math vessel and used the "
                "slash-form to call its maximum-finding method on both stones."
            ),
            need=(
                "She needed to know which of the two stones the human potter's "
                "method would declare the larger."
            ),
            mapping=(
                "Math/max uses slash notation to invoke a static class method "
                "with two stone-arguments. The runtime crosses into the Java "
                "vessel and lets the human potter's rule decide the winner."
            ),
            resolution=(
                "The borrowed vessel's maximum-finding method settled with "
                "its choice at beak-reach. (count: 3)"
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
    fable="crow-pitcher",
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
                "Sable stood at the garden with a stone inscribed 'tortoise' "
                "and wanted to know how many notches the human potter's vessel "
                "would count along its surface."
            ),
            need=(
                "Sable needed the count of characters etched into the stone "
                "to confirm the vessel measured them correctly."
            ),
            mapping=(
                "`count` reaches into the host vessel's length property and "
                "returns the tally. The Clojure function bridges to the host "
                "sequence measure without exposing the raw field access."
            ),
            resolution=(
                "The pitcher returned the tally of notches counted along the stone. (with {drawn.a} folded in)"
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
                "Korvus held a shorter stone — one inscribed 'hare' — at the "
                "orchard and placed it near the pitcher to see how many "
                "notches the vessel would register."
            ),
            need=(
                "He needed the count of the shorter stone's characters to "
                "compare it against a longer one."
            ),
            mapping=(
                "`count` again bridges to the host vessel's length measure. "
                "Fewer characters means fewer notches — the host and Clojure "
                "side agree on the tally."
            ),
            resolution=(
                "The pitcher returned the notch-count for the shorter stone. (with {drawn.a} folded in)"
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
    fable="crow-pitcher",
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
    fable="crow-pitcher",
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
                "Caw found the human potter's unfired clay at the village "
                "and shaped a new String vessel herself — pressing the word "
                "'go' into the wet clay using the dot-construct inscription."
            ),
            need=(
                "She needed to confirm that the dot-construct form fired a "
                "fresh earthenware vessel holding the text she had pressed in."
            ),
            mapping=(
                "The `ClassName.` trailing-dot form calls the Java constructor "
                "directly. It fires a new host object from the potter's mold, "
                "returning the freshly-constructed vessel to the Clojure side."
            ),
            resolution=(
                "The pitcher returned the freshly-fired vessel with its "
                "pressed-in text at beak-reach."
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
                "Korvus tried the same potter's mold at the meadow but wrote "
                "the inscription differently — using the `new` keyword before "
                "the class name, pressing 'jump' into the wet clay."
            ),
            need=(
                "He wanted to confirm `new` was an equivalent way to fire "
                "the same kind of Java vessel from the human potter's mold."
            ),
            mapping=(
                "The `(new ClassName ...)` form is the alternate constructor "
                "syntax. Both forms fire the same Java constructor; only the "
                "inscription on the rim differs — the vessel is identical."
            ),
            resolution=(
                "The pitcher returned the newly-fired vessel, its pressed-in "
                "text settling at beak-reach."
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
    fable="crow-pitcher",
    examples=[
        # int-array / aget are the canonical interop calls.
        SubjectExample(
            form="(let [a (int-array [10 20 30])] (aget a 1))",
            expected=20,
            concept_phrase="indexing into a host array",
            question_what="the element at index 1 of the int-array [10 20 30] via the aget function",
            goal_text="access an element in a host array by index",

            scenario=(
                "Sable laid three numbered stones in a row at the road's edge "
                "inside a Java tray — 10, 20, 30 — and then reached with a "
                "talon for the stone at position one."
            ),
            need=(
                "Sable needed the exact stone at index one of the tray, not "
                "the first or the last, to continue the work at hand."
            ),
            mapping=(
                "`int-array` fires a host-side tray for whole-number stones. "
                "`aget` reaches into the tray by index position and lifts the "
                "stone out — the Java side handles the raw slot access."
            ),
            resolution=(
                "The pitcher returned the stone lifted from position one of "
                "the Java tray."
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
                "Korvus filled a Java tray at the garden with three small "
                "stones and wanted to ask the human potter's vessel how many "
                "slots it had been fired with."
            ),
            need=(
                "He needed the tray's own slot-count so he would know "
                "its limits before reaching inside for elements."
            ),
            mapping=(
                "`alength` asks the host array how many slots it holds — "
                "a direct question to the Java vessel's own length field. "
                "The Clojure side receives the tally without counting manually."
            ),
            resolution=(
                "The pitcher returned the tray's slot-count reported by "
                "the Java vessel itself. (count: 3)"
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
    fable="crow-pitcher",
    examples=[
        # Type hints don't change the value; they hint the compiler.
        SubjectExample(
            form='(let [^String s "abc"] (.toUpperCase s))',
            expected="ABC",
            concept_phrase="using a type hint in a binding",
            question_what="the uppercase form of the type-hinted string abc produced by calling the host method toUpperCase on the binding",
            goal_text="add a type hint to a binding and call a method on the typed value",

            scenario=(
                "Caw scratched a marginal note on the pitcher's rim at the "
                "village — `^String` — before binding the letter-stone 'abc'. "
                "The rim-note told the runtime which potter had fired the clay."
            ),
            need=(
                "She needed the runtime to skip its guesswork about which "
                "potter's vessel to call, reading the rim-note instead."
            ),
            mapping=(
                "The `^String` annotation is a type hint scratched on the "
                "binding's rim. The compiler reads it to avoid reflection, "
                "then the dot-call reaches into the Java vessel directly."
            ),
            resolution=(
                "The borrowed vessel's method returned its result, guided by "
                "the rim-note, at beak-reach."
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
    fable="crow-pitcher",
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
                "Korvus stood at the farm with two ordinary stones — one "
                "notched once, one notched twice — and dropped them both "
                "into the pitcher under the default arithmetic rules."
            ),
            need=(
                "He needed the pitcher to add the two stones together safely, "
                "with the default overflow-checking guard active."
            ),
            mapping=(
                "Clojure's `+` uses checked arithmetic by default — if the "
                "host primitive overflows, an error surfaces. For small stones "
                "like these, the result arrives without incident."
            ),
            resolution=(
                "The pitcher returned the combined count of the two stones. (with {drawn.a} folded in)"
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
    fable="crow-pitcher",
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
    fable="crow-pitcher",
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
    fable="crow-pitcher",
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
    fable="crow-pitcher",
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
    fable="crow-pitcher",
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
                "Sable wrapped the human potter's Math vessel in a soft-moss "
                "safety net at the hilltop before calling Math/sqrt on the "
                "stone marked 4 — in case the host vessel leaked an error."
            ),
            need=(
                "Sable needed the host method's answer if it arrived cleanly, "
                "or a safe fallback keyword if the Java side threw an exception."
            ),
            mapping=(
                "`try`/`catch Exception` is the soft-moss net spread under "
                "the borrowed Java vessel. If the host leaks a stack trace, "
                "the net catches it; otherwise the clean result passes through."
            ),
            resolution=(
                "The call succeeded and the pitcher returned the method's "
                "result without triggering the safety net. (count: 4)"
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
    print(f"grade-11 crow-pitcher smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
