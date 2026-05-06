"""Grade 7 — error handling, debugging, IO. Through boy-who-cried-wolf.

Subplot lens: the shepherd's careless throw becomes a real exception;
the elder catches it and tries again. Beyond the REPL the world has
files, streams, and surprises — the elder opens a notebook and copies
down the form so the runtime can carry the work the rest of the way.
The shepherd shrugs off warnings; the elder reads the stack trace and
rewrites the form.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.boy_wolf.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.boy_wolf._metaphor_pools import (
    _SAFETYNET_SUBPLOTS, _SCROLL_SUBPLOTS, _TOOLSHED_SUBPLOTS,
)
from mmllm.aesop.curriculum.boy_wolf._goals import GOALS


# ─────────────────────── grade-7 subplot extensions ───────────────────────
#
# Errors and IO map onto the boy-wolf moral lens cleanly: the shepherd's
# carefree claim becomes the careless throw — a real exception once
# nobody trusts the cry. The elder is the patient catcher, the one who
# reads the stack trace and rewrites the form. Beyond the REPL the
# world has files and streams: the elder opens a notebook and copies
# the form down so the runtime can carry the work the rest of the way.

_ERR_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    # The shepherd's careless throw — what was once a false alarm is
    # now a real exception, and the elder catches it patiently.
    #
    # NOTE (boy-wolf polish, hand-audit pass): "...took every careless
    # throw at its word. {place}, {elder_phrase} typed..." rendered as
    # a sentence-start lowercase preposition ("...at its word. in the
    # woods, Alice typed...") which is a grammar bug. Replaced the
    # period with a comma+conjunction so {place} stays mid-sentence.
    SubplotTemplate("""\
{shepherd_phrase} had cried alarm so often that the runtime now took
every careless throw at its word, and {place}, {elder_phrase} typed
{form_display} carefully, ready to catch whatever the REPL might raise.
{shepherd}, {emo_proud}, said no error would ever come — but {elder}
insisted on letting the runtime decide, then reading {concept_phrase}
from whatever it returned."""),

    # The elder reads the stack trace; the shepherd shrugs the warning
    # off. Mirrors the fable's "boy ignores the villagers' worry" beat.
    SubplotTemplate("""\
A small slip of paper {place} carried the form {form_display}.
{shepherd} glanced at it and shrugged the warning off, certain there
was no trouble. {elder_phrase} sat down, {emo_patient}, and worked
through {concept_phrase} step by step — ready, if anything went wrong,
to read the stack trace from top to bottom and try the form again."""),

    # The world-outside-the-REPL beat — files, streams, surprises.
    # Elder opens a notebook and copies down the form for the runtime.
    SubplotTemplate("""\
Beyond the REPL the world had files, streams, and surprises.
{elder_phrase} opened a small notebook {place}, copying down
{concept_phrase}. {shepherd}, {emo_tired}, watched as {elder_he_she}
wrote the form {form_display} so the runtime could carry the work the
rest of the way."""),
]


def _ex(form, expected, concept, what, goal=None,
        scenario="", need="", mapping="", resolution="",
        tags=()):
    canon = GOALS.get(form, {})
    if all([scenario, need, mapping, resolution]) and "story" not in tags:
        tags = tuple(tags) + ("story",)
    return SubjectExample(
        form=form, expected=expected,
        concept_phrase=canon.get("concept", concept),
        question_what=canon.get("what", what),
        goal_text=goal if goal is not None else canon.get("goal", ""),
        scenario=scenario, need=need, mapping=mapping, resolution=resolution,
        tags=tags,
    )


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
    subject_title="throw", fable="boy-wolf",
    examples=[
        _ex("(try (throw (Exception. \"bad\")) (catch Exception e :thrown))",
            ":thrown",
            "throwing an exception that is then caught",
            "the keyword :thrown returned after the throw is caught"),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-02 — try/catch
G7_02 = SubjectCurriculum(grade=7, subject_id="G7-02",
    subject_title="try / catch", fable="boy-wolf",
    examples=[
        _ex("(try (/ 1 0) (catch Exception e :caught))", ":caught",
            "a division by zero wrapped in try/catch",
            "the keyword :caught returned by the catch branch"),
        _ex("(try 42 (catch Exception e :caught))", 42,
            "a try with no error — the body's value is returned",
            "the value 42 from the no-error branch"),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-03 — try/finally
G7_03 = SubjectCurriculum(grade=7, subject_id="G7-03",
    subject_title="try / finally", fable="boy-wolf",
    examples=[
        _ex("(try 7 (finally :cleanup))", 7,
            "a try whose finally clause runs but doesn't change the value",
            "the value 7 from the body"),
        _ex("(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))",
            ":caught",
            "a finally that runs before the outer catch fires",
            "the keyword :caught (the outer catch handles the divide-by-zero)"),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-04 — ex-info
G7_04 = SubjectCurriculum(grade=7, subject_id="G7-04",
    subject_title="ex-info", fable="boy-wolf",
    examples=[
        _ex("(try (throw (ex-info \"bad\" {:a 1})) (catch Exception e (ex-data e)))",
            {":a": 1},
            "throwing an ex-info with attached data, then reading it back",
            "the data map {:a 1} pulled from the caught ex-info"),
        _ex("(try (throw (ex-info \"x\" {:k :v})) (catch Exception e (:k (ex-data e))))",
            ":v",
            "extracting a single key from the caught ex-info's data",
            "the value :v at key :k in the ex-data"),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-05 — nil punning
G7_05 = SubjectCurriculum(grade=7, subject_id="G7-05",
    subject_title="nil punning", fable="boy-wolf",
    examples=[
        _ex("(some? nil)", False,
            "the predicate (some? nil)",
            "whether nil counts as some?"),
        _ex("(some? 0)", True,
            "the predicate (some? 0)",
            "whether 0 counts as some?"),
        _ex("(first nil)", None,
            "calling first on nil",
            "the value of (first nil)"),
        _ex("(count nil)", 0,
            "counting a nil collection",
            "the count of nil"),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-06 — pre/post conditions (we exercise via the {:pre [...]} on
# a defn, applied successfully).
G7_06 = SubjectCurriculum(grade=7, subject_id="G7-06",
    subject_title="pre and post conditions", fable="boy-wolf",
    examples=[
        _ex("((fn [x] {:pre [(pos? x)]} (* x 2)) 5)", 10,
            "a fn with a :pre condition that is satisfied",
            "the value returned when the precondition holds and 5 is doubled"),
        _ex("(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))",
            ":pre-failed",
            "a :pre condition that fails, caught by surrounding try",
            "the keyword :pre-failed when the pre-check rejects -1"),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-07 — assert
G7_07 = SubjectCurriculum(grade=7, subject_id="G7-07",
    subject_title="assert", fable="boy-wolf",
    examples=[
        _ex("(do (assert (= 1 1)) :ok)", ":ok",
            "an assert that passes, followed by a return value",
            "the keyword :ok returned after the assert succeeds"),
        _ex("(try (assert (= 1 2)) (catch Throwable e :asserted))",
            ":asserted",
            "an assert that fails, caught by surrounding try",
            "the keyword :asserted when the assertion rejects (= 1 2)"),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-08 — prn / pprint (these side-effect to *out*; we use with-out-str
# to capture and inspect).
G7_08 = SubjectCurriculum(grade=7, subject_id="G7-08",
    subject_title="prn and pprint", fable="boy-wolf",
    examples=[
        _ex("(with-out-str (prn 42))", "42\n",
            "capturing the output of (prn 42)",
            "the string \"42\\n\" produced by prn"),
        _ex("(with-out-str (prn :wolf))", ":wolf\n",
            "capturing prn applied to the keyword :wolf",
            "the string \":wolf\\n\" produced by prn"),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-09 — tap> (returns true; we exercise that effect).
G7_09 = SubjectCurriculum(grade=7, subject_id="G7-09",
    subject_title="tap>", fable="boy-wolf",
    examples=[
        _ex("(tap> :hello)", True,
            "tapping a value into the tap pool",
            "the boolean true returned by tap>"),
        _ex("(tap> 42)", True,
            "tapping the number 42 into the tap pool",
            "the boolean true"),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-10 — doc / source (REPL helpers; we exercise via a metadata
# lookup since `doc` itself prints).
G7_10 = SubjectCurriculum(grade=7, subject_id="G7-10",
    subject_title="doc and source", fable="boy-wolf",
    examples=[
        _ex("(:doc (meta '^{:doc \"adds two\"} plus))", "adds two",
            "the :doc metadata on a symbol",
            "the string \"adds two\" from the metadata"),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-11 — Reading stack traces (we exercise via inspecting the message
# of a caught exception).
G7_11 = SubjectCurriculum(grade=7, subject_id="G7-11",
    subject_title="Reading stack traces", fable="boy-wolf",
    examples=[
        _ex("(try (throw (Exception. \"oops\")) (catch Exception e (.getMessage e)))",
            "oops",
            "extracting the message from a caught exception",
            "the string \"oops\" from the caught Exception"),
        _ex("(try (throw (ex-info \"trouble\" {})) (catch Exception e (.getMessage e)))",
            "trouble",
            "the message of a caught ex-info",
            "the string \"trouble\""),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-12 — slurp / spit (file IO; we exercise the inverse-of-spit:
# string-shaped helpers that don't touch the filesystem).
G7_12 = SubjectCurriculum(grade=7, subject_id="G7-12",
    subject_title="slurp and spit", fable="boy-wolf",
    examples=[
        # An in-memory analogue: build a string, then read it back via
        # split / count, the way slurp-then-process works in practice.
        _ex("(count \"wolf\\nshepherd\\n\")", 14,
            "the length of a multi-line string",
            "the count of characters in \"wolf\\nshepherd\\n\""),
        _ex("(clojure.string/split \"a\\nb\\nc\" #\"\\n\")", ["a", "b", "c"],
            "splitting a slurped-style string on newlines",
            "the vector [\"a\" \"b\" \"c\"] of three lines"),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-13 — line-seq (we exercise via the in-memory equivalent: a vector
# of lines).
G7_13 = SubjectCurriculum(grade=7, subject_id="G7-13",
    subject_title="line-seq", fable="boy-wolf",
    examples=[
        _ex("(count (clojure.string/split-lines \"a\\nb\\nc\"))", 3,
            "the number of lines in a small text",
            "the count of lines in \"a\\nb\\nc\""),
        _ex("(first (clojure.string/split-lines \"alpha\\nbeta\"))",
            "alpha",
            "the initial line from splitting a multi-line string",
            "what the initial line is",
            goal="get the initial line from splitting a multi-line string"),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-14 — with-open (we exercise the macro-shape via with-out-str,
# the closest universally-available analogue).
G7_14 = SubjectCurriculum(grade=7, subject_id="G7-14",
    subject_title="with-open", fable="boy-wolf",
    examples=[
        _ex("(with-out-str (println \"wolf\"))", "wolf\n",
            "a resource-scoped capture of println output",
            "the string \"wolf\\n\" from the scoped block"),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-15 — *in* / *out* (we exercise *out* via with-out-str; *in* is
# harder to bind in a single form and we leave it implied).
G7_15 = SubjectCurriculum(grade=7, subject_id="G7-15",
    subject_title="*in* and *out*", fable="boy-wolf",
    examples=[
        _ex("(with-out-str (print \"x\"))", "x",
            "redirecting *out* via with-out-str and printing",
            "the string \"x\" captured from *out*"),
        _ex("(with-out-str (println))", "\n",
            "a bare println redirected through *out*",
            "the string \"\\n\""),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-16 — edn read
G7_16 = SubjectCurriculum(grade=7, subject_id="G7-16",
    subject_title="edn read", fable="boy-wolf",
    examples=[
        _ex("(clojure.edn/read-string \"42\")", 42,
            "reading an edn integer from a string",
            "the integer 42 read from \"42\""),
        _ex("(clojure.edn/read-string \"{:a 1}\")", {":a": 1},
            "reading an edn map from a string",
            "the map {:a 1} read from \"{:a 1}\""),
        _ex("(clojure.edn/read-string \"[:wolf :flock]\")",
            [":wolf", ":flock"],
            "reading an edn vector of keywords",
            "the vector [:wolf :flock]"),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-17 — JSON roundtrip (we exercise via edn-shaped data; the actual
# JSON library availability varies, but the conceptual roundtrip is
# the same as edn).
G7_17 = SubjectCurriculum(grade=7, subject_id="G7-17",
    subject_title="JSON roundtrip", fable="boy-wolf",
    examples=[
        _ex("(clojure.edn/read-string (pr-str {:a 1 :b 2}))",
            {":a": 1, ":b": 2},
            "writing then reading back a small map",
            "the map {:a 1 :b 2} after the roundtrip"),
        _ex("(clojure.edn/read-string (pr-str [1 2 3]))", [1, 2, 3],
            "round-tripping a vector through pr-str then edn/read-string",
            "the vector [1 2 3]"),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-18 — Shell command (host-specific; we exercise via a non-shell
# analogue that captures the same conceptual pattern: a command-name
# string and an args vector turning into a result).
G7_18 = SubjectCurriculum(grade=7, subject_id="G7-18",
    subject_title="Shell command", fable="boy-wolf",
    examples=[
        _ex("(:cmd {:cmd \"ls\" :args [\"-l\"]})", "ls",
            "the :cmd portion of a shell-call descriptor map",
            "the string \"ls\""),
        _ex("(count (:args {:cmd \"echo\" :args [\"hello\" \"world\"]}))",
            2,
            "the number of args in a shell-call descriptor",
            "the count of args"),
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
    print(f"grade-7 boy-wolf smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
