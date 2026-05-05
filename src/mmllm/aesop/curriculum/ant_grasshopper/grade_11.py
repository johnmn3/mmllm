"""Grade 11 — interop, crossing into other runtimes. Through ant-grasshopper.

Subplot lens: the Ant carefully follows the customs of a foreign meadow.
JVM, JS, and Python are different fields the two travel into; each has
its own customs (method-call syntax, static methods, type hints). The
Grasshopper barges in as if it were the home meadow; the Ant is careful
to follow the local conventions.

Most interop forms are host-specific. Examples here use forms that
work in basilisp (the Python host this curriculum is trained against),
or use predicates that don't depend on which host you're on.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.ant_grasshopper.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)


# ─────────────────────── grade-11 subplot extensions ───────────────────────
#
# The two have travelled past their usual meadow into a foreign field
# whose REPL hosts another runtime. The Grasshopper wants to barge ahead
# in the usual style; the Ant treats every interop call as a small act
# of diplomacy.

_INTEROP_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    SubplotTemplate("""\
{ant_phrase} and {grasshopper_phrase} had wandered {place} into territory
where the REPL spoke to another runtime entirely. {ant} read the sign
and pointed at {concept_phrase}; the form to submit, written in the
foreign convention, was {form_display}."""),

    SubplotTemplate("""\
"This is not your meadow," {ant_phrase} said {place}, {emo_patient}.
"Here, the methods belong to objects, and the dot has a particular
meaning." {grasshopper_phrase}, {emo_proud}, said {grasshopper_he_she}
could read the foreign form anyway. {ant} sketched {form_display} on
the ground; let the runtime, {ant_he_she} insisted, declare what
{concept_phrase} returned."""),

    SubplotTemplate("""\
A wooden border-post {place} marked the edge of the host runtime's
territory. The form written on it — {form_display} — captured
{concept_phrase}. {grasshopper}, {emo_tired}, agreed for once that
crossing into foreign syntax called for actual evaluation, not
guessing."""),

    SubplotTemplate("""\
{grasshopper_phrase} insisted the foreign-runtime forms were "just like
home." {ant_phrase} tapped a stone {place} where someone had inscribed
{concept_phrase}. "Then write {form_display} into the REPL," {ant}
said, "and we'll see if your familiarity holds.\""""),

    SubplotTemplate("""\
At a wayside shrine {place} dedicated to interop, the day's offering
was {concept_phrase}. {ant_phrase} knelt and placed the form
{form_display} on the stone. {grasshopper}, watching, agreed to be the
one to submit it to the runtime."""),

    SubplotTemplate("""\
A merchant's stall {place} sold translated phrasebooks for the host
language; today's lesson was {concept_phrase}. {ant_phrase} copied the
form {form_display} from the page, and {grasshopper_phrase} agreed
(for once) that one should always check the REPL before trusting a
translation."""),
]


def _ex(form, expected, concept, what):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what)


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
    fable="ant-grasshopper",
    examples=[
        # Overview subject — narrative does the educational work.
        _ex('(do "Clojure runs on multiple hosts: JVM, CLR, JS, Python" :studied)',
            ":studied",
            "the idea that Clojure has multiple host runtimes",
            "the marker value when the host overview has been studied"),
        _ex('(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Python: basilisp" :hosts)',
            ":hosts",
            "the family of Clojure host runtimes",
            "the marker keyword for the host family"),
    ],
    subplots=_INTEROP_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-02 — Method call syntax
G11_02 = SubjectCurriculum(
    grade=11, subject_id="G11-02",
    subject_title="Method call syntax",
    fable="ant-grasshopper",
    examples=[
        _ex('(.toUpperCase "abc")', "ABC",
            'the method call (.toUpperCase "abc")',
            "the uppercased string returned by the method"),
        _ex('(.startsWith "ant-grasshopper" "ant")', True,
            "a method call (.startsWith ...) returning a boolean",
            "whether the string starts with the prefix"),
        _ex('(. "abc" toUpperCase)', "ABC",
            'the alternate dot form (. obj method)',
            "the uppercased result via the longer dot syntax"),
    ],
    subplots=_INTEROP_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-03 — Static method call
G11_03 = SubjectCurriculum(
    grade=11, subject_id="G11-03",
    subject_title="Static method call",
    fable="ant-grasshopper",
    examples=[
        # Math/abs is available across hosts as a static-style call.
        _ex("(Math/abs -7)", 7,
            "the static call (Math/abs -7)",
            "the absolute value of -7 via the static method"),
        _ex("(Math/max 3 9)", 9,
            "the static call (Math/max 3 9)",
            "the larger of 3 and 9 via the static method"),
    ],
    subplots=_INTEROP_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-04 — Field access
G11_04 = SubjectCurriculum(
    grade=11, subject_id="G11-04",
    subject_title="Field access",
    fable="ant-grasshopper",
    examples=[
        # Field access on a host object — count is a property/method
        # depending on host. We use a portable example using the
        # `.length` style on a string-like host where applicable.
        _ex('(count "ant")', 3,
            'the count of "ant"',
            'the length of "ant"'),
        _ex('(count "grasshopper")', 11,
            'the count of "grasshopper"',
            'the length of "grasshopper"'),
    ],
    subplots=_INTEROP_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-05 — Import form
G11_05 = SubjectCurriculum(
    grade=11, subject_id="G11-05",
    subject_title="Import form",
    fable="ant-grasshopper",
    examples=[
        # Overview-ish: the form is what one would write at the top of a file.
        _ex('(do "(:import (java.util Date)) imports a host class" :imported)',
            ":imported",
            "the (:import ...) ns clause for host classes",
            "the marker for the import-form lesson"),
        _ex('(do "import is a top-of-file ns clause" :studied)',
            ":studied",
            "the role of import in a Clojure file",
            "the marker for studying import"),
    ],
    subplots=_INTEROP_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-06 — new and dot-construct
G11_06 = SubjectCurriculum(
    grade=11, subject_id="G11-06",
    subject_title="new and dot-construct",
    fable="ant-grasshopper",
    examples=[
        # Construct a host class via Class. or (new Class). String. is
        # portable across JVM and basilisp.
        _ex('(String. "hello")', "hello",
            'the constructor call (String. "hello")',
            'the string built by the dot-construct'),
        _ex('(new String "world")', "world",
            'the (new String "world") form',
            'the string built by (new ...)'),
    ],
    subplots=_INTEROP_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-07 — Arrays
G11_07 = SubjectCurriculum(
    grade=11, subject_id="G11-07",
    subject_title="Arrays",
    fable="ant-grasshopper",
    examples=[
        # int-array / aget are the canonical interop calls.
        _ex("(let [a (int-array [10 20 30])] (aget a 1))", 20,
            "indexing into an int-array via aget",
            "the value at index 1 of the array"),
        _ex("(let [a (int-array [1 2 3])] (alength a))", 3,
            "the length of an int-array via alength",
            "the length of the array"),
    ],
    subplots=_INTEROP_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-08 — Type hints
G11_08 = SubjectCurriculum(
    grade=11, subject_id="G11-08",
    subject_title="Type hints",
    fable="ant-grasshopper",
    examples=[
        # Type hints don't change the value; they hint the compiler.
        _ex('(let [^String s "abc"] (.toUpperCase s))', "ABC",
            "a let-binding with a ^String type hint",
            "the uppercased string after a type-hinted binding"),
        _ex('(do "type hints are metadata that guide compilation" :studied)',
            ":studied",
            "the role of ^Type metadata as a hint",
            "the marker keyword for the type-hint lesson"),
    ],
    subplots=_INTEROP_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-09 — Checked vs unchecked math
G11_09 = SubjectCurriculum(
    grade=11, subject_id="G11-09",
    subject_title="Checked vs unchecked math",
    fable="ant-grasshopper",
    examples=[
        # Plain arithmetic works the same way for ordinary values; the
        # checked/unchecked distinction is about overflow at the host
        # primitive level. Use a value-space form for the eval, narrate
        # the distinction.
        _ex("(+ 1 2)", 3,
            "the form (+ 1 2) under default checked math",
            "the result of (+ 1 2) under the default math regime"),
        _ex('(do "*unchecked-math* turns off overflow checking on prims" :studied)',
            ":studied",
            "the *unchecked-math* dynamic var",
            "the marker for the checked/unchecked lesson"),
    ],
    subplots=_INTEROP_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-10 — ClojureScript overview
G11_10 = SubjectCurriculum(
    grade=11, subject_id="G11-10",
    subject_title="ClojureScript overview",
    fable="ant-grasshopper",
    examples=[
        _ex('(do "ClojureScript compiles to JavaScript via the Closure compiler" :studied)',
            ":studied",
            "the ClojureScript host overview",
            "the marker for studying the cljs host"),
        _ex('(do "cljs runs in browsers and Node, with JS interop syntax" :cljs)',
            ":cljs",
            "where ClojureScript runs and how interop looks",
            "the marker for the cljs-runtime lesson"),
    ],
    subplots=_INTEROP_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-11 — cljs-js interop
G11_11 = SubjectCurriculum(
    grade=11, subject_id="G11-11",
    subject_title="cljs / JavaScript interop",
    fable="ant-grasshopper",
    examples=[
        _ex('(do "(js/console.log x) calls a JS global; (.-foo o) reads a JS field" :studied)',
            ":studied",
            "the cljs-to-js interop syntax",
            "the marker for the cljs-js interop lesson"),
        _ex('(do "js/<name> namespaces JS globals; .- prefix marks field access" :cljs-interop)',
            ":cljs-interop",
            "two key cljs-js interop conventions",
            "the marker keyword for the conventions"),
    ],
    subplots=_INTEROP_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-12 — Basilisp overview (the Python host — this project!)
G11_12 = SubjectCurriculum(
    grade=11, subject_id="G11-12",
    subject_title="Basilisp overview (Python host)",
    fable="ant-grasshopper",
    examples=[
        _ex('(do "basilisp is a Clojure-like Lisp implemented on Python" :studied)',
            ":studied",
            "the basilisp host overview",
            "the marker for studying basilisp"),
        _ex('(do "basilisp interops with Python via the same dot-syntax conventions" :basilisp)',
            ":basilisp",
            "how basilisp does Python interop",
            "the marker keyword for basilisp interop"),
    ],
    subplots=_INTEROP_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-13 — Cross-platform .cljc and reader-conditionals
G11_13 = SubjectCurriculum(
    grade=11, subject_id="G11-13",
    subject_title="Cross-platform .cljc and reader-conditionals",
    fable="ant-grasshopper",
    examples=[
        _ex('(do "#?(:clj … :cljs …) selects a form per host at read time" :studied)',
            ":studied",
            "the reader-conditional #?(...) form",
            "the marker for the reader-conditional lesson"),
        _ex('(do ".cljc files share code across multiple hosts" :cljc)',
            ":cljc",
            "the role of .cljc files",
            "the marker keyword for the .cljc lesson"),
    ],
    subplots=_INTEROP_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-14 — Debugging host leaks
G11_14 = SubjectCurriculum(
    grade=11, subject_id="G11-14",
    subject_title="Debugging host leaks",
    fable="ant-grasshopper",
    examples=[
        _ex('(do "host stack traces leak through interop; learn to read them" :studied)',
            ":studied",
            "the topic of debugging host-runtime leaks",
            "the marker for the host-leaks lesson"),
        _ex('(try (Math/sqrt 4) (catch Exception _ :err))', 2.0,
            "wrapping a host call in try/catch in case it leaks",
            "the result when the host call succeeds"),
    ],
    subplots=_INTEROP_SUBPLOTS, plan_pool=_PLAN_G11,
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
    print(f"grade-11 ant-grasshopper smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
