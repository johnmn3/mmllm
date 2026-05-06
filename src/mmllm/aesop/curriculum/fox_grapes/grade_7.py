"""Grade 7 — error handling, debugging, IO. Through fox-grapes.

Subplot lens: the patient fox writes the form and lets the REPL push
back, then catches the trouble carefully and reads what came out. The
hasty fox prefers to dismiss the error — the cluster is sour anyway,
why bother investigating a stack trace? The fable's rationalize-vs-
inspect dynamic fits errors naturally: the patient fox treats every
exception as data the runtime hands back; the hasty fox waves it off
as not worth the effort. Files, streams, and printed output extend the
same beat — the patient fox copies forms into a small notebook and
lets the runtime carry the work the rest of the way.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.fox_grapes.grade_1 import _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL
from mmllm.aesop.curriculum.fox_grapes._metaphor_pools import _SAFETYNET_SUBPLOTS, _SCROLL_SUBPLOTS, _TOOLSHED_SUBPLOTS


_ERR_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    # Patient fox writes the form, catches the error, reads it back.
    SubplotTemplate("""\
{patient_fox_phrase} had learned not to trust a form on first reading;
working {place}, {patient_fox_he_she} typed {form_display} carefully, ready to
catch whatever the REPL might throw back. {hasty_fox_phrase}, {emo_proud},
laughed and said no error would ever come — but {patient_fox} insisted
on letting the runtime decide, then reading {concept_phrase} from
whatever it returned."""),

    # Hasty fox dismisses the warning; patient fox reads the trace.
    SubplotTemplate("""\
A small slip of paper {place} carried the form {form_display}. {hasty_fox}
glanced at it and waved it off, certain there was no trouble worth
chasing — the cluster, {hasty_fox} said, was probably sour anyway.
{patient_fox_phrase} sat down, {emo_patient}, and worked through
{concept_phrase} step by step — ready, if anything went wrong, to read
the stack trace from top to bottom and try again."""),

    # The "world outside the REPL" beat — files, streams, printing.
    SubplotTemplate("""\
Beyond the REPL the world had files, streams, and surprises.
{patient_fox_phrase} opened a small notebook {place}, copying down
{concept_phrase}. {hasty_fox}, {emo_proud}, watched as {patient_fox_he_she}
wrote the form {form_display} so the runtime could carry the work the
rest of the way."""),
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


_PLAN_G7 = _PLAN_POOL + (
    "I wrap the form in try/catch and let the REPL handle the error.",
    "I use ex-info to attach data to the error.",
    "I let the REPL read the file or stream for me.",
    "I print or tap the value for inspection, then return.",
)


# ─────────────────────── 18 grade-7 subjects ───────────────────────


# G7-01 — throw (we wrap throw in try/catch so the form actually
# returns a value instead of bubbling up).
G7_01 = SubjectCurriculum(grade=7, subject_id="G7-01",
    subject_title="throw", fable="fox-grapes",
    examples=[
        _ex("(try (throw (Exception. \"bad\")) (catch Exception e :thrown))",
            ":thrown",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox had strung a catching-cloth between two orchard trees.',
            need='Sly wanted to evaluate a form and trust the cloth: errors caught, healthy values passed through.',
            mapping="`try`/`catch` is the catching-cloth: errors thrown are caught by the form's catch-clause, while healthy values pass through unchanged.",
            resolution="the form passed through the cloth — caught if it threw, returned if it didn't — and the slate held whatever came out.",
            tags=("story",)),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-02 — try/catch
G7_02 = SubjectCurriculum(grade=7, subject_id="G7-02",
    subject_title="try / catch", fable="fox-grapes",
    examples=[
        _ex("(try (/ 1 0) (catch Exception e :caught))",
            ":caught",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox had strung a catching-cloth between two orchard trees.',
            need='Renard wanted to evaluate a form and trust the cloth: errors caught, healthy values passed through.',
            mapping="`try`/`catch` is the catching-cloth: errors thrown are caught by the form's catch-clause, while healthy values pass through unchanged.",
            resolution="the form passed through the cloth — caught if it threw, returned if it didn't — and the slate held whatever came out.",
            tags=("story",)),
        _ex("(try 42 (catch Exception e :caught))",
            42,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox had strung a catching-cloth between two orchard trees.',
            need='Vix wanted to evaluate a form and trust the cloth: errors caught, healthy values passed through.',
            mapping="`try`/`catch` is the catching-cloth: errors thrown are caught by the form's catch-clause, while healthy values pass through unchanged.",
            resolution="the form passed through the cloth — caught if it threw, returned if it didn't — and the slate held whatever came out.",
            tags=("story",)),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-03 — try/finally
G7_03 = SubjectCurriculum(grade=7, subject_id="G7-03",
    subject_title="try / finally", fable="fox-grapes",
    examples=[
        _ex("(try 7 (finally :cleanup))",
            7,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox had strung a catching-cloth between two orchard trees.',
            need='Sly wanted to evaluate a form and trust the cloth: errors caught, healthy values passed through.',
            mapping="`try`/`catch` is the catching-cloth: errors thrown are caught by the form's catch-clause, while healthy values pass through unchanged.",
            resolution="the form passed through the cloth — caught if it threw, returned if it didn't — and the slate held whatever came out.",
            tags=("story",)),
        _ex("(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))",
            ":caught",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox had strung a catching-cloth between two orchard trees.',
            need='Renard wanted to evaluate a form and trust the cloth: errors caught, healthy values passed through.',
            mapping="`try`/`catch` is the catching-cloth: errors thrown are caught by the form's catch-clause, while healthy values pass through unchanged.",
            resolution="the form passed through the cloth — caught if it threw, returned if it didn't — and the slate held whatever came out.",
            tags=("story",)),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-04 — ex-info
G7_04 = SubjectCurriculum(grade=7, subject_id="G7-04",
    subject_title="ex-info", fable="fox-grapes",
    examples=[
        _ex("(try (throw (ex-info \"bad\" {:a 1})) (catch Exception e (ex-data e)))",
            {":a": 1},
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox had strung a catching-cloth between two orchard trees.',
            need='Vix wanted to evaluate a form and trust the cloth: errors caught, healthy values passed through.',
            mapping="`try`/`catch` is the catching-cloth: errors thrown are caught by the form's catch-clause, while healthy values pass through unchanged.",
            resolution="the form passed through the cloth — caught if it threw, returned if it didn't — and the slate held whatever came out.",
            tags=("story",)),
        _ex("(try (throw (ex-info \"x\" {:k :v})) (catch Exception e (:k (ex-data e))))",
            ":v",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox had strung a catching-cloth between two orchard trees.',
            need='Sly wanted to evaluate a form and trust the cloth: errors caught, healthy values passed through.',
            mapping="`try`/`catch` is the catching-cloth: errors thrown are caught by the form's catch-clause, while healthy values pass through unchanged.",
            resolution="the form passed through the cloth — caught if it threw, returned if it didn't — and the slate held whatever came out.",
            tags=("story",)),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-05 — nil punning
G7_05 = SubjectCurriculum(grade=7, subject_id="G7-05",
    subject_title="nil punning", fable="fox-grapes",
    examples=[
        _ex("(some? nil)",
            False,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox had strung a catching-cloth between two orchard trees.',
            need='Renard wanted to evaluate a form and trust the cloth: errors caught, healthy values passed through.',
            mapping="`try`/`catch` is the catching-cloth: errors thrown are caught by the form's catch-clause, while healthy values pass through unchanged.",
            resolution="the form passed through the cloth — caught if it threw, returned if it didn't — and the slate held whatever came out.",
            tags=("story",)),
        _ex("(some? 0)",
            True,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox had strung a catching-cloth between two orchard trees.',
            need='Vix wanted to evaluate a form and trust the cloth: errors caught, healthy values passed through.',
            mapping="`try`/`catch` is the catching-cloth: errors thrown are caught by the form's catch-clause, while healthy values pass through unchanged.",
            resolution="the form passed through the cloth — caught if it threw, returned if it didn't — and the slate held whatever came out.",
            tags=("story",)),
        _ex("(first nil)",
            None,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox had strung a catching-cloth between two orchard trees.',
            need='Sly wanted to evaluate a form and trust the cloth: errors caught, healthy values passed through.',
            mapping="`try`/`catch` is the catching-cloth: errors thrown are caught by the form's catch-clause, while healthy values pass through unchanged.",
            resolution="the form passed through the cloth — caught if it threw, returned if it didn't — and the slate held whatever came out.",
            tags=("story",)),
        _ex("(count nil)",
            0,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox had strung a catching-cloth between two orchard trees.',
            need='Renard wanted to evaluate a form and trust the cloth: errors caught, healthy values passed through.',
            mapping="`try`/`catch` is the catching-cloth: errors thrown are caught by the form's catch-clause, while healthy values pass through unchanged.",
            resolution="the form passed through the cloth — caught if it threw, returned if it didn't — and the slate held whatever came out.",
            tags=("story",)),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-06 — pre/post conditions (we exercise via the {:pre [...]} on
# a defn, applied successfully).
G7_06 = SubjectCurriculum(grade=7, subject_id="G7-06",
    subject_title="pre and post conditions", fable="fox-grapes",
    examples=[
        _ex("((fn [x] {:pre [(pos? x)]} (* x 2)) 5)",
            10,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox had strung a catching-cloth between two orchard trees.',
            need='Vix wanted to evaluate a form and trust the cloth: errors caught, healthy values passed through.',
            mapping="`try`/`catch` is the catching-cloth: errors thrown are caught by the form's catch-clause, while healthy values pass through unchanged.",
            resolution="the form passed through the cloth — caught if it threw, returned if it didn't — and the slate held whatever came out.",
            tags=("story",)),
        _ex("(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))",
            ":pre-failed",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox had strung a catching-cloth between two orchard trees.',
            need='Sly wanted to evaluate a form and trust the cloth: errors caught, healthy values passed through.',
            mapping="`try`/`catch` is the catching-cloth: errors thrown are caught by the form's catch-clause, while healthy values pass through unchanged.",
            resolution="the form passed through the cloth — caught if it threw, returned if it didn't — and the slate held whatever came out.",
            tags=("story",)),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-07 — assert
G7_07 = SubjectCurriculum(grade=7, subject_id="G7-07",
    subject_title="assert", fable="fox-grapes",
    examples=[
        _ex("(do (assert (= 1 1)) :ok)",
            ":ok",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox had strung a catching-cloth between two orchard trees.',
            need='Renard wanted to evaluate a form and trust the cloth: errors caught, healthy values passed through.',
            mapping="`try`/`catch` is the catching-cloth: errors thrown are caught by the form's catch-clause, while healthy values pass through unchanged.",
            resolution="the form passed through the cloth — caught if it threw, returned if it didn't — and the slate held whatever came out.",
            tags=("story",)),
        _ex("(try (assert (= 1 2)) (catch Throwable e :asserted))",
            ":asserted",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox had strung a catching-cloth between two orchard trees.',
            need='Vix wanted to evaluate a form and trust the cloth: errors caught, healthy values passed through.',
            mapping="`try`/`catch` is the catching-cloth: errors thrown are caught by the form's catch-clause, while healthy values pass through unchanged.",
            resolution="the form passed through the cloth — caught if it threw, returned if it didn't — and the slate held whatever came out.",
            tags=("story",)),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-08 — prn / pprint (these side-effect to *out*; we use with-out-str
# to capture and inspect).
G7_08 = SubjectCurriculum(grade=7, subject_id="G7-08",
    subject_title="prn and pprint", fable="fox-grapes",
    examples=[
        _ex("(with-out-str (prn 42))",
            "42\n",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox had pinned a harvest-parchment to the orchard fence — a record the orchard kept of yields, weights, and tags.',
            need="Sly wanted to read or write the parchment's record, in the form's chosen slot.",
            mapping='IO and metadata in Clojure are the parchment work: forms read what the parchment carries or write a new entry.',
            resolution='the parchment yielded what the form had asked it to fetch — exactly the field the keyword named.',
            tags=("story",)),
        _ex("(with-out-str (prn :fox))", ":fox\n",
            "capturing prn applied to the keyword :fox",
            "the string \":fox\\n\" produced by prn"),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-09 — tap> (returns true; we exercise that effect).
G7_09 = SubjectCurriculum(grade=7, subject_id="G7-09",
    subject_title="tap>", fable="fox-grapes",
    examples=[
        _ex("(tap> :hello)",
            True,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox had pinned a harvest-parchment to the orchard fence — a record the orchard kept of yields, weights, and tags.',
            need="Renard wanted to read or write the parchment's record, in the form's chosen slot.",
            mapping='IO and metadata in Clojure are the parchment work: forms read what the parchment carries or write a new entry.',
            resolution='the parchment yielded what the form had asked it to fetch — exactly the field the keyword named.',
            tags=("story",)),
        _ex("(tap> 42)",
            True,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox had pinned a harvest-parchment to the orchard fence — a record the orchard kept of yields, weights, and tags.',
            need="Vix wanted to read or write the parchment's record, in the form's chosen slot.",
            mapping='IO and metadata in Clojure are the parchment work: forms read what the parchment carries or write a new entry.',
            resolution='the parchment yielded what the form had asked it to fetch — exactly the field the keyword named.',
            tags=("story",)),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-10 — doc / source (REPL helpers; we exercise via a metadata
# lookup since `doc` itself prints).
G7_10 = SubjectCurriculum(grade=7, subject_id="G7-10",
    subject_title="doc and source", fable="fox-grapes",
    examples=[
        _ex("(:doc (meta '^{:doc \"adds two\"} plus))",
            "adds two",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox had pinned a harvest-parchment to the orchard fence — a record the orchard kept of yields, weights, and tags.',
            need="Sly wanted to read or write the parchment's record, in the form's chosen slot.",
            mapping='IO and metadata in Clojure are the parchment work: forms read what the parchment carries or write a new entry.',
            resolution='the parchment yielded what the form had asked it to fetch — exactly the field the keyword named.',
            tags=("story",)),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-11 — Reading stack traces (we exercise via inspecting the message
# of a caught exception).
G7_11 = SubjectCurriculum(grade=7, subject_id="G7-11",
    subject_title="Reading stack traces", fable="fox-grapes",
    examples=[
        _ex("(try (throw (Exception. \"oops\")) (catch Exception e (.getMessage e)))",
            "oops",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox had strung a catching-cloth between two orchard trees.',
            need='Renard wanted to evaluate a form and trust the cloth: errors caught, healthy values passed through.',
            mapping="`try`/`catch` is the catching-cloth: errors thrown are caught by the form's catch-clause, while healthy values pass through unchanged.",
            resolution="the form passed through the cloth — caught if it threw, returned if it didn't — and the slate held whatever came out.",
            tags=("story",)),
        _ex("(try (throw (ex-info \"trouble\" {})) (catch Exception e (.getMessage e)))",
            "trouble",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox had strung a catching-cloth between two orchard trees.',
            need='Vix wanted to evaluate a form and trust the cloth: errors caught, healthy values passed through.',
            mapping="`try`/`catch` is the catching-cloth: errors thrown are caught by the form's catch-clause, while healthy values pass through unchanged.",
            resolution="the form passed through the cloth — caught if it threw, returned if it didn't — and the slate held whatever came out.",
            tags=("story",)),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-12 — slurp / spit (file IO; we exercise the inverse-of-spit:
# string-shaped helpers that don't touch the filesystem).
G7_12 = SubjectCurriculum(grade=7, subject_id="G7-12",
    subject_title="slurp and spit", fable="fox-grapes",
    examples=[
        # An in-memory analogue: build a string, then read it back via
        # split / count, the way slurp-then-process works in practice.
        _ex("(count \"hare\\ntortoise\\n\")",
            14,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox had pinned a harvest-parchment to the orchard fence — a record the orchard kept of yields, weights, and tags.',
            need="Sly wanted to read or write the parchment's record, in the form's chosen slot.",
            mapping='IO and metadata in Clojure are the parchment work: forms read what the parchment carries or write a new entry.',
            resolution='the parchment yielded what the form had asked it to fetch — exactly the field the keyword named.',
            tags=("story",)),
        _ex("(clojure.string/split \"a\\nb\\nc\" #\"\\n\")",
            ["a", "b", "c"],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox had pinned a harvest-parchment to the orchard fence — a record the orchard kept of yields, weights, and tags.',
            need="Renard wanted to read or write the parchment's record, in the form's chosen slot.",
            mapping='IO and metadata in Clojure are the parchment work: forms read what the parchment carries or write a new entry.',
            resolution='the parchment yielded what the form had asked it to fetch — exactly the field the keyword named.',
            tags=("story",)),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-13 — line-seq (we exercise via the in-memory equivalent: a vector
# of lines).
G7_13 = SubjectCurriculum(grade=7, subject_id="G7-13",
    subject_title="line-seq", fable="fox-grapes",
    examples=[
        _ex("(count (clojure.string/split-lines \"a\\nb\\nc\"))",
            3,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox had pinned a harvest-parchment to the orchard fence — a record the orchard kept of yields, weights, and tags.',
            need="Vix wanted to read or write the parchment's record, in the form's chosen slot.",
            mapping='IO and metadata in Clojure are the parchment work: forms read what the parchment carries or write a new entry.',
            resolution='the parchment yielded what the form had asked it to fetch — exactly the field the keyword named.',
            tags=("story",)),
        _ex("(first (clojure.string/split-lines \"first\\nsecond\"))",
            "first",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox had pinned a harvest-parchment to the orchard fence — a record the orchard kept of yields, weights, and tags.',
            need="Sly wanted to read or write the parchment's record, in the form's chosen slot.",
            mapping='IO and metadata in Clojure are the parchment work: forms read what the parchment carries or write a new entry.',
            resolution='the parchment yielded what the form had asked it to fetch — exactly the field the keyword named.',
            tags=("story",)),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-14 — with-open (we exercise the macro-shape via with-out-str,
# the closest universally-available analogue).
G7_14 = SubjectCurriculum(grade=7, subject_id="G7-14",
    subject_title="with-open", fable="fox-grapes",
    examples=[
        _ex("(with-out-str (println \"fox\"))", "fox\n",
            "a resource-scoped capture of println output",
            "the string \"fox\\n\" from the scoped block"),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-15 — *in* / *out* (we exercise *out* via with-out-str; *in* is
# harder to bind in a single form and we leave it implied).
G7_15 = SubjectCurriculum(grade=7, subject_id="G7-15",
    subject_title="*in* and *out*", fable="fox-grapes",
    examples=[
        _ex("(with-out-str (print \"x\"))",
            "x",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox had pinned a harvest-parchment to the orchard fence — a record the orchard kept of yields, weights, and tags.',
            need="Renard wanted to read or write the parchment's record, in the form's chosen slot.",
            mapping='IO and metadata in Clojure are the parchment work: forms read what the parchment carries or write a new entry.',
            resolution='the parchment yielded what the form had asked it to fetch — exactly the field the keyword named.',
            tags=("story",)),
        _ex("(with-out-str (println))",
            "\n",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox had pinned a harvest-parchment to the orchard fence — a record the orchard kept of yields, weights, and tags.',
            need="Vix wanted to read or write the parchment's record, in the form's chosen slot.",
            mapping='IO and metadata in Clojure are the parchment work: forms read what the parchment carries or write a new entry.',
            resolution='the parchment yielded what the form had asked it to fetch — exactly the field the keyword named.',
            tags=("story",)),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-16 — edn read
G7_16 = SubjectCurriculum(grade=7, subject_id="G7-16",
    subject_title="edn read", fable="fox-grapes",
    examples=[
        _ex("(clojure.edn/read-string \"42\")",
            42,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox had pinned a harvest-parchment to the orchard fence — a record the orchard kept of yields, weights, and tags.',
            need="Sly wanted to read or write the parchment's record, in the form's chosen slot.",
            mapping='IO and metadata in Clojure are the parchment work: forms read what the parchment carries or write a new entry.',
            resolution='the parchment yielded what the form had asked it to fetch — exactly the field the keyword named.',
            tags=("story",)),
        _ex("(clojure.edn/read-string \"{:a 1}\")",
            {":a": 1},
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox had pinned a harvest-parchment to the orchard fence — a record the orchard kept of yields, weights, and tags.',
            need="Renard wanted to read or write the parchment's record, in the form's chosen slot.",
            mapping='IO and metadata in Clojure are the parchment work: forms read what the parchment carries or write a new entry.',
            resolution='the parchment yielded what the form had asked it to fetch — exactly the field the keyword named.',
            tags=("story",)),
        _ex("(clojure.edn/read-string \"[:fox :grapes]\")",
            [":fox", ":grapes"],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox had pinned a harvest-parchment to the orchard fence — a record the orchard kept of yields, weights, and tags.',
            need="Vix wanted to read or write the parchment's record, in the form's chosen slot.",
            mapping='IO and metadata in Clojure are the parchment work: forms read what the parchment carries or write a new entry.',
            resolution='the parchment yielded what the form had asked it to fetch — exactly the field the keyword named.',
            tags=("story",)),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-17 — JSON roundtrip (we exercise via edn-shaped data; the actual
# JSON library availability varies, but the conceptual roundtrip is
# the same as edn).
G7_17 = SubjectCurriculum(grade=7, subject_id="G7-17",
    subject_title="JSON roundtrip", fable="fox-grapes",
    examples=[
        _ex("(clojure.edn/read-string (pr-str {:a 1 :b 2}))",
            {":a": 1, ":b": 2},
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox had pinned a harvest-parchment to the orchard fence — a record the orchard kept of yields, weights, and tags.',
            need="Sly wanted to read or write the parchment's record, in the form's chosen slot.",
            mapping='IO and metadata in Clojure are the parchment work: forms read what the parchment carries or write a new entry.',
            resolution='the parchment yielded what the form had asked it to fetch — exactly the field the keyword named.',
            tags=("story",)),
        _ex("(clojure.edn/read-string (pr-str [1 2 3]))",
            [1, 2, 3],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox had pinned a harvest-parchment to the orchard fence — a record the orchard kept of yields, weights, and tags.',
            need="Renard wanted to read or write the parchment's record, in the form's chosen slot.",
            mapping='IO and metadata in Clojure are the parchment work: forms read what the parchment carries or write a new entry.',
            resolution='the parchment yielded what the form had asked it to fetch — exactly the field the keyword named.',
            tags=("story",)),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-18 — Shell command (host-specific; we exercise via a non-shell
# analogue that captures the same conceptual pattern: a command-name
# string and an args vector turning into a result).
G7_18 = SubjectCurriculum(grade=7, subject_id="G7-18",
    subject_title="Shell command", fable="fox-grapes",
    examples=[
        _ex("(:cmd {:cmd \"ls\" :args [\"-l\"]})",
            "ls",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox stood at the stone tool-shed at the orchard's edge — the foreign household's catalogue full of borrowed tools.",
            need="Vix called into the tool-shed for a method or class the orchard could borrow for the form's work.",
            mapping="Host interop calls into the runtime's foreign catalogue: methods, classes, fields. The dotted name is the borrowed handle.",
            resolution="the tool-shed handed back what the form's call had produced, and the orchard incorporated the value.",
            tags=("story",)),
        _ex("(count (:args {:cmd \"echo\" :args [\"hello\" \"world\"]}))",
            2,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox stood at the stone tool-shed at the orchard's edge — the foreign household's catalogue full of borrowed tools.",
            need="Sly called into the tool-shed for a method or class the orchard could borrow for the form's work.",
            mapping="Host interop calls into the runtime's foreign catalogue: methods, classes, fields. The dotted name is the borrowed handle.",
            resolution="the tool-shed handed back what the form's call had produced, and the orchard incorporated the value.",
            tags=("story",)),
    ], subplots=_TOOLSHED_SUBPLOTS, plan_pool=_PLAN_G7)


# ─────────────────────── registry ───────────────────────


SUBJECTS: dict[str, SubjectCurriculum] = {s.subject_id: s for s in (
    G7_01, G7_02, G7_03, G7_04, G7_05, G7_06, G7_07, G7_08, G7_09,
    G7_10, G7_11, G7_12, G7_13, G7_14, G7_15, G7_16, G7_17, G7_18,
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
    print(f"grade-7 fox-grapes smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
