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
        _ex('(.startsWith "hare-tortoise" "hare")', True,
            "the host method startsWith checking a string prefix",
            "whether the string hare-tortoise starts with the prefix hare via the host method startsWith",
            goal="call the host method startsWith on a string to check for a prefix"),
        _ex('(. "abc" toUpperCase)', "ABC",
            'the alternate dot form for a host method',
            "the uppercase form of the string abc produced by the host method toUpperCase via the alternate dot syntax",
            goal="call the host method toUpperCase using the alternate dot form"),
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
        _ex("(Math/abs -7)", 7,
            "the static host method Math/abs",
            "the absolute value of the integer -7 produced by calling the static host method Math/abs via slash notation",
            goal="call the static host method Math/abs with the argument -7"),
        _ex("(Math/max 3 9)", 9,
            "the static host method Math/max",
            "the maximum value of the integers 3 and 9 produced by calling the static host method Math/max via slash notation",
            goal="call the static host method Math/max to find the larger of two numbers"),
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
        _ex('(count "tortoise")', 8,
            'the count of a sequence',
            'the number of characters in the string tortoise via the count function',
            goal="count the characters in a string"),
        _ex('(count "hare")', 4,
            'the count of a sequence',
            'the number of characters in the string hare via the count function',
            goal="count the characters in another string"),
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
        _ex('(String. "go")', "go",
            'constructing a String via the dot-construct form',
            'the newly constructed String object created from a text argument via the dot-construct syntax',
            goal="construct a host String object with the dot-construct syntax"),
        _ex('(new String "jump")', "jump",
            'constructing a String via the new form',
            'the newly constructed String object created from a text argument via the new keyword',
            goal="construct a host String object using the new keyword"),
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
        _ex("(let [a (int-array [10 20 30])] (aget a 1))", 20,
            "indexing into a host array",
            "the element at index 1 of the int-array [10 20 30] via the aget function",
            goal="access an element in a host array by index"),
        _ex("(let [a (int-array [1 2 3])] (alength a))", 3,
            "getting the length of a host array",
            "the length of the int-array [1 2 3] via the alength function",
            goal="get the length of a host array"),
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
        _ex('(let [^String s "abc"] (.toUpperCase s))', "ABC",
            "using a type hint in a binding",
            "the uppercase form of the type-hinted string abc produced by calling the host method toUpperCase on the binding",
            goal="add a type hint to a binding and call a method on the typed value"),
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
        _ex("(+ 1 2)", 3,
            "basic addition under the default checked math regime",
            "the sum of two numbers",
            goal="add two numbers with the default math behavior"),
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
        _ex('(try (Math/sqrt 4) (catch Exception _ :err))', 2.0,
            "catching exceptions from a host method call",
            "the square root of 4 produced by the static host method Math/sqrt via slash notation when the call succeeds",
            goal="wrap a static host method call in error handling"),
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
