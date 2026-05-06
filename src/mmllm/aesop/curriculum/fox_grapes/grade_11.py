"""Grade 11 — interop, crossing into other runtimes. Through fox-grapes.

Subplot lens: the foxes wander out of their home orchard and into a
foreign vineyard, market, or walled garden where the fruits are
strange and the customs unfamiliar. JVM, JS, and Python are
different territories the foxes visit; each has its own conventions
(method-call syntax, static methods, type hints). The hasty fox
treats the foreign-language as just another excuse to declare the
fruit sour and walk away; the patient fox copies the local form
faithfully and lets the REPL settle whether the cluster is reachable.

Most interop forms are host-specific. Examples here use forms that
work in basilisp (the Python host this curriculum is trained against),
or use predicates that don't depend on which host you're on.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.fox_grapes.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL, _GOAL_SUBPLOTS,
)
from mmllm.aesop.curriculum.fox_grapes._metaphor_pools import _ACORN_SUBPLOTS, _TOOLSHED_SUBPLOTS


# ─────────────────────── grade-11 subplot extensions ───────────────────────
#
# The two foxes have wandered past their usual orchard into a foreign
# vineyard whose REPL hosts another runtime. The hasty fox wants to
# dismiss every strange-looking form as not worth the reach; the
# patient fox treats every interop call as a small act of diplomacy.

_INTEROP_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    SubplotTemplate("""\
{hasty_fox_phrase} and {patient_fox_phrase} had wandered {place} into
a vineyard where the REPL spoke to another runtime entirely.
{patient_fox} read the sign and pointed at {concept_phrase}; the form
to submit, written in the foreign convention, was {form_display}."""),

    SubplotTemplate("""\
"This is not your home orchard," {patient_fox_phrase} said {place},
{emo_patient}. "Here, the methods belong to objects, and the dot has
a particular meaning." {hasty_fox_phrase}, {emo_proud}, said
{hasty_fox_he_she} could read the foreign form anyway. {patient_fox}
sketched {form_display} on the ground; let the runtime,
{patient_fox_he_she} insisted, declare what {concept_phrase}
returned."""),

    SubplotTemplate("""\
A wooden border-post {place} marked the edge of the host runtime's
territory. The form carved into it — {form_display} — captured
{concept_phrase}. {hasty_fox}, who had already declared the foreign
fruit sour, agreed for once that crossing into foreign syntax called
for actual evaluation, not guessing."""),

    SubplotTemplate("""\
{hasty_fox_phrase} insisted the foreign-runtime forms were "just like
home, and probably just as out of reach." {patient_fox_phrase} tapped
a stone {place} where someone had inscribed {concept_phrase}. "Then
write {form_display} into the REPL," {patient_fox} said, "and we'll
see if your familiarity holds.\""""),

    SubplotTemplate("""\
At a wayside shrine {place} dedicated to interop, the day's offering
was {concept_phrase}. {patient_fox_phrase} knelt and placed the form
{form_display} on the stone. {hasty_fox}, watching and pretending the
shrine's fruits were all sour, agreed to be the one to submit it to
the runtime."""),

    SubplotTemplate("""\
A merchant's stall {place} sold translated phrasebooks for the host
language; today's lesson was {concept_phrase}. {patient_fox_phrase}
copied the form {form_display} from the page, and {hasty_fox_phrase}
agreed (for once) that one should always check the REPL before
trusting a translation."""),
]


def _ex(form, expected, concept, what,
        goal="", scenario="", need="", mapping="", resolution="",
        tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal,
                          scenario=scenario, need=need,
                          mapping=mapping, resolution=resolution,
                          tags=tags)


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
    fable="fox-grapes",
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
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-02 — Method call syntax
G11_02 = SubjectCurriculum(
    grade=11, subject_id="G11-02",
    subject_title="Method call syntax",
    fable="fox-grapes",
    examples=[
        _ex('(.toUpperCase "abc")',
            "ABC",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox stood at the stone tool-shed at the orchard's edge — the foreign household's catalogue full of borrowed tools.",
            need="Vix called into the tool-shed for a method or class the orchard could borrow for the form's work.",
            mapping="Host interop calls into the runtime's foreign catalogue: methods, classes, fields. The dotted name is the borrowed handle.",
            resolution="the tool-shed handed back what the form's call had produced, and the orchard incorporated the value.",
            tags=("story",)),
        _ex('(.startsWith "hare-tortoise" "hare")',
            True,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox stood at the stone tool-shed at the orchard's edge — the foreign household's catalogue full of borrowed tools.",
            need="Sly called into the tool-shed for a method or class the orchard could borrow for the form's work.",
            mapping="Host interop calls into the runtime's foreign catalogue: methods, classes, fields. The dotted name is the borrowed handle.",
            resolution="the tool-shed handed back what the form's call had produced, and the orchard incorporated the value.",
            tags=("story",)),
        _ex('(. "abc" toUpperCase)',
            "ABC",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox stood at the stone tool-shed at the orchard's edge — the foreign household's catalogue full of borrowed tools.",
            need="Renard called into the tool-shed for a method or class the orchard could borrow for the form's work.",
            mapping="Host interop calls into the runtime's foreign catalogue: methods, classes, fields. The dotted name is the borrowed handle.",
            resolution="the tool-shed handed back what the form's call had produced, and the orchard incorporated the value.",
            tags=("story",)),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-03 — Static method call
G11_03 = SubjectCurriculum(
    grade=11, subject_id="G11-03",
    subject_title="Static method call",
    fable="fox-grapes",
    examples=[
        # Math/abs is available across hosts as a static-style call.
        _ex("(Math/abs -7)",
            7,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox stood at the stone tool-shed at the orchard's edge — the foreign household's catalogue full of borrowed tools.",
            need="Vix called into the tool-shed for a method or class the orchard could borrow for the form's work.",
            mapping="Host interop calls into the runtime's foreign catalogue: methods, classes, fields. The dotted name is the borrowed handle.",
            resolution="the tool-shed handed back what the form's call had produced, and the orchard incorporated the value.",
            tags=("story",)),
        _ex("(Math/max 3 9)",
            9,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox stood at the stone tool-shed at the orchard's edge — the foreign household's catalogue full of borrowed tools.",
            need="Sly called into the tool-shed for a method or class the orchard could borrow for the form's work.",
            mapping="Host interop calls into the runtime's foreign catalogue: methods, classes, fields. The dotted name is the borrowed handle.",
            resolution="the tool-shed handed back what the form's call had produced, and the orchard incorporated the value.",
            tags=("story",)),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-04 — Field access
G11_04 = SubjectCurriculum(
    grade=11, subject_id="G11-04",
    subject_title="Field access",
    fable="fox-grapes",
    examples=[
        # Field access on a host object — count is a property/method
        # depending on host. We use a portable example using the
        # `.length` style on a string-like host where applicable.
        _ex('(count "tortoise")',
            8,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox stood at the stone tool-shed at the orchard's edge — the foreign household's catalogue full of borrowed tools.",
            need="Renard called into the tool-shed for a method or class the orchard could borrow for the form's work.",
            mapping="Host interop calls into the runtime's foreign catalogue: methods, classes, fields. The dotted name is the borrowed handle.",
            resolution="the tool-shed handed back what the form's call had produced, and the orchard incorporated the value.",
            tags=("story",)),
        _ex('(count "hare")',
            4,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox stood at the stone tool-shed at the orchard's edge — the foreign household's catalogue full of borrowed tools.",
            need="Vix called into the tool-shed for a method or class the orchard could borrow for the form's work.",
            mapping="Host interop calls into the runtime's foreign catalogue: methods, classes, fields. The dotted name is the borrowed handle.",
            resolution="the tool-shed handed back what the form's call had produced, and the orchard incorporated the value.",
            tags=("story",)),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-05 — Import form
G11_05 = SubjectCurriculum(
    grade=11, subject_id="G11-05",
    subject_title="Import form",
    fable="fox-grapes",
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
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-06 — new and dot-construct
G11_06 = SubjectCurriculum(
    grade=11, subject_id="G11-06",
    subject_title="new and dot-construct",
    fable="fox-grapes",
    examples=[
        # Construct a host class via Class. or (new Class). String. is
        # portable across JVM and basilisp.
        _ex('(String. "hello")',
            "hello",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox stood at the stone tool-shed at the orchard's edge — the foreign household's catalogue full of borrowed tools.",
            need="Sly called into the tool-shed for a method or class the orchard could borrow for the form's work.",
            mapping="Host interop calls into the runtime's foreign catalogue: methods, classes, fields. The dotted name is the borrowed handle.",
            resolution="the tool-shed handed back what the form's call had produced, and the orchard incorporated the value.",
            tags=("story",)),
        _ex('(new String "world")',
            "world",
            'a form',
            'the value the form evaluates to'),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-07 — Arrays
G11_07 = SubjectCurriculum(
    grade=11, subject_id="G11-07",
    subject_title="Arrays",
    fable="fox-grapes",
    examples=[
        # int-array / aget are the canonical interop calls.
        _ex("(let [a (int-array [10 20 30])] (aget a 1))",
            20,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox stood at the stone tool-shed at the orchard's edge — the foreign household's catalogue full of borrowed tools.",
            need="Vix called into the tool-shed for a method or class the orchard could borrow for the form's work.",
            mapping="Host interop calls into the runtime's foreign catalogue: methods, classes, fields. The dotted name is the borrowed handle.",
            resolution="the tool-shed handed back what the form's call had produced, and the orchard incorporated the value.",
            tags=("story",)),
        _ex("(let [a (int-array [1 2 3])] (alength a))",
            3,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox stood at the stone tool-shed at the orchard's edge — the foreign household's catalogue full of borrowed tools.",
            need="Sly called into the tool-shed for a method or class the orchard could borrow for the form's work.",
            mapping="Host interop calls into the runtime's foreign catalogue: methods, classes, fields. The dotted name is the borrowed handle.",
            resolution="the tool-shed handed back what the form's call had produced, and the orchard incorporated the value.",
            tags=("story",)),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-08 — Type hints
G11_08 = SubjectCurriculum(
    grade=11, subject_id="G11-08",
    subject_title="Type hints",
    fable="fox-grapes",
    examples=[
        # Type hints don't change the value; they hint the compiler.
        _ex('(let [^String s "abc"] (.toUpperCase s))',
            "ABC",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox stood at the stone tool-shed at the orchard's edge — the foreign household's catalogue full of borrowed tools.",
            need="Renard called into the tool-shed for a method or class the orchard could borrow for the form's work.",
            mapping="Host interop calls into the runtime's foreign catalogue: methods, classes, fields. The dotted name is the borrowed handle.",
            resolution="the tool-shed handed back what the form's call had produced, and the orchard incorporated the value.",
            tags=("story",)),
        _ex('(do "type hints are metadata that guide compilation" :studied)',
            ":studied",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox stood at the stone tool-shed at the orchard's edge — the foreign household's catalogue full of borrowed tools.",
            need="Vix called into the tool-shed for a method or class the orchard could borrow for the form's work.",
            mapping="Host interop calls into the runtime's foreign catalogue: methods, classes, fields. The dotted name is the borrowed handle.",
            resolution="the tool-shed handed back what the form's call had produced, and the orchard incorporated the value.",
            tags=("story",)),
    ],
    subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-09 — Checked vs unchecked math
G11_09 = SubjectCurriculum(
    grade=11, subject_id="G11-09",
    subject_title="Checked vs unchecked math",
    fable="fox-grapes",
    examples=[
        # Plain arithmetic works the same way for ordinary values; the
        # checked/unchecked distinction is about overflow at the host
        # primitive level. Use a value-space form for the eval, narrate
        # the distinction.
        _ex("(+ 1 2)",
            3,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox tallied small heaps of clusters on a slate at the press.',
            need="Sly wanted the slate's running total — what the form's arithmetic would produce for that day's heaps.",
            mapping='Arithmetic in Clojure is the slate-tally: the form names the operation, the args are the heaps, and the REPL counts out the result.',
            resolution="the slate held the value the form's tally produced, ready to be posted to the day's harvest log.",
            tags=("story",)),
        _ex('(do "*unchecked-math* turns off overflow checking on prims" :studied)',
            ":studied",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox tallied small heaps of clusters on a slate at the press.',
            need="Renard wanted the slate's running total — what the form's arithmetic would produce for that day's heaps.",
            mapping='Arithmetic in Clojure is the slate-tally: the form names the operation, the args are the heaps, and the REPL counts out the result.',
            resolution="the slate held the value the form's tally produced, ready to be posted to the day's harvest log.",
            tags=("story",)),
    ],
    subplots=_ACORN_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-10 — ClojureScript overview
G11_10 = SubjectCurriculum(
    grade=11, subject_id="G11-10",
    subject_title="ClojureScript overview",
    fable="fox-grapes",
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
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-11 — cljs-js interop
G11_11 = SubjectCurriculum(
    grade=11, subject_id="G11-11",
    subject_title="cljs / JavaScript interop",
    fable="fox-grapes",
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
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-12 — Basilisp overview (the Python host — this project!)
G11_12 = SubjectCurriculum(
    grade=11, subject_id="G11-12",
    subject_title="Basilisp overview (Python host)",
    fable="fox-grapes",
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
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-13 — Cross-platform .cljc and reader-conditionals
G11_13 = SubjectCurriculum(
    grade=11, subject_id="G11-13",
    subject_title="Cross-platform .cljc and reader-conditionals",
    fable="fox-grapes",
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
    subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G11,
)


# G11-14 — Debugging host leaks
G11_14 = SubjectCurriculum(
    grade=11, subject_id="G11-14",
    subject_title="Debugging host leaks",
    fable="fox-grapes",
    examples=[
        _ex('(do "host stack traces leak through interop; learn to read them" :studied)',
            ":studied",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox stood at the stone tool-shed at the orchard's edge — the foreign household's catalogue full of borrowed tools.",
            need="Vix called into the tool-shed for a method or class the orchard could borrow for the form's work.",
            mapping="Host interop calls into the runtime's foreign catalogue: methods, classes, fields. The dotted name is the borrowed handle.",
            resolution="the tool-shed handed back what the form's call had produced, and the orchard incorporated the value.",
            tags=("story",)),
        _ex('(try (Math/sqrt 4) (catch Exception _ :err))',
            2.0,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox stood at the stone tool-shed at the orchard's edge — the foreign household's catalogue full of borrowed tools.",
            need="Sly called into the tool-shed for a method or class the orchard could borrow for the form's work.",
            mapping="Host interop calls into the runtime's foreign catalogue: methods, classes, fields. The dotted name is the borrowed handle.",
            resolution="the tool-shed handed back what the form's call had produced, and the orchard incorporated the value.",
            tags=("story",)),
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
    print(f"grade-11 fox-grapes smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
