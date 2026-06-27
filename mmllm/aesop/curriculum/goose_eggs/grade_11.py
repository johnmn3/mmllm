"""Grade 11 — interop, crossing into other runtimes. Through goose-eggs.

Subplot lens: the owner takes the eggs to a distant market with foreign
currency, foreign weights. JVM, JS, and Python are different countries
the owner and visitor visit; each has its own customs (method-call
syntax, static methods, type hints). The {visitor} treats the
foreign-language as just another guess; the {owner} is careful to
follow the local conventions, treating every interop call as a small
act of careful translation.

Most interop forms are host-specific. Examples here use forms that
work in basilisp (the Python host this curriculum is trained against),
or use predicates that don't depend on which host you're on.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.goose_eggs.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)


# ─────────────────────── grade-11 subplot extensions ───────────────────────
#
# The owner has carried the goose's eggs past the home meadow into a
# foreign country whose REPL hosts another runtime. The visitor wants
# to barge ahead in the usual style; the owner treats every interop
# call as a small act of diplomacy — foreign currency, foreign weights,
# foreign method-call syntax.

_INTEROP_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    SubplotTemplate("""\
{owner_phrase} and {visitor_phrase} had carried a basket of eggs {place}
into territory where the REPL spoke to another runtime entirely.
{owner} read the market sign and pointed at {concept_phrase}; the form
to submit, written in the foreign convention, was {form_display}.
{goose_phrase} had stayed at home, but {owner_his_her} ledger came along."""),

    SubplotTemplate("""\
"This is not our farmyard," {owner_phrase} said {place}, {emo_patient}.
"Here, the methods belong to objects, and the dot has a particular
meaning — like the foreign coin-stamps on the market stalls."
{visitor_phrase}, {emo_greedy}, said {visitor_he_she} could read the
foreign form anyway. {owner} sketched {form_display} on a slate beside
the egg-basket; let the runtime, {owner_he_she} insisted, declare what
{concept_phrase} returned."""),

    SubplotTemplate("""\
A wooden border-post {place} marked the edge of the host runtime's
territory, and beneath it a stall weighed eggs in foreign measures.
The form chalked on the post — {form_display} — captured
{concept_phrase}. {visitor}, {emo_regretful} from a recent bad guess,
agreed for once that crossing into foreign syntax called for actual
evaluation, not greedy assumption."""),

    SubplotTemplate("""\
{visitor_phrase} insisted the foreign-runtime forms were "just like
home." {owner_phrase} tapped a stone {place} where someone had
inscribed {concept_phrase} above the day's egg-prices. "Then write
{form_display} into the REPL," {owner} said, "and we'll see if your
familiarity holds — the way we count eggs one at a time, never by
guess.\""""),

    SubplotTemplate("""\
At a wayside shrine {place} dedicated to safe interop and honest
weights, the day's offering was {concept_phrase}. {owner_phrase} knelt
and placed the form {form_display} on the stone beside a single egg
from the morning's basket. {visitor}, watching, agreed to be the one
to submit it to the runtime."""),

    SubplotTemplate("""\
A merchant's stall {place} sold translated phrasebooks for the host
language alongside scales for foreign egg-weights; today's lesson was
{concept_phrase}. {owner_phrase} copied the form {form_display} from
the page into {owner_his_her} ledger, and {visitor_phrase} agreed (for
once) that one should always check the REPL before trusting a
translation, the same way one always counts the eggs before trusting
a buyer."""),
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
    fable="goose-eggs",
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
    fable="goose-eggs",
    examples=[
        _ex('(.toUpperCase "abc")', "ABC",
            'the method call (.toUpperCase "abc")',
            "the uppercased string returned by the method"),
        _ex('(.startsWith "hare-tortoise" "hare")', True,
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
    fable="goose-eggs",
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
    fable="goose-eggs",
    examples=[
        # Field access on a host object — count is a property/method
        # depending on host. We use a portable example using the
        # `.length` style on a string-like host where applicable.
        _ex('(count "tortoise")', 8,
            'the count of "tortoise"',
            'the length of "tortoise"'),
        _ex('(count "hare")', 4,
            'the count of "hare"',
            'the length of "hare"'),
    ],
    subplots=_INTEROP_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-05 — Import form
G11_05 = SubjectCurriculum(
    grade=11, subject_id="G11-05",
    subject_title="Import form",
    fable="goose-eggs",
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
    fable="goose-eggs",
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
    fable="goose-eggs",
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
    fable="goose-eggs",
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
    fable="goose-eggs",
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
    fable="goose-eggs",
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
    fable="goose-eggs",
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
    fable="goose-eggs",
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
    fable="goose-eggs",
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
    fable="goose-eggs",
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
    print(f"grade-11 goose-eggs smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
