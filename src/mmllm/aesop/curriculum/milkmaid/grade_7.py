"""Grade 7 — error handling, debugging, IO. through the milkmaid fable.

Subplot lens: Farmer tries the form, the REPL pushes back, Farmer
catches the trouble and tries again. Milkmaid prefers to ignore the
warning and dash on. The fable's vanity-vs-steadiness fits errors
naturally — Farmer reads the stack trace; Milkmaid insists nothing is
wrong.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.milkmaid.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL
)
from mmllm.aesop.curriculum.milkmaid._metaphor_pools import (
    _SAFETYNET_SUBPLOTS, _SCROLL_SUBPLOTS, _TOOLSHED_SUBPLOTS,
)


_ERR_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    # Farmer tries the form, catches the error, retries.
    # NOTE: {place} comma-bracketed mid-sentence (was period+place before
    # the deep-audit's LOWER_PLACE_AFTER_PERIOD check, which produced
    # "...first reading. near the meadow,..." with sentence breaking
    # mid-prep).
    SubplotTemplate("""\
{farmer_phrase} had learned not to trust a form on first reading,
and {place} {farmer_he_she} typed {form_display} carefully, ready
to catch whatever the REPL might throw back. {milkmaid_phrase},
{emo_proud}, laughed and said no error would ever come — but
{farmer} insisted on letting the runtime decide, then reading
{concept_phrase} from whatever it returned."""),

    # Milkmaid ignores the warning; Farmer reads the stack trace.
    SubplotTemplate("""\
A small slip of paper {place} carried the form {form_display}. {milkmaid}
glanced at it and dashed on, certain there was no trouble.
{farmer_phrase} sat down, {emo_patient}, and worked through
{concept_phrase} step by step — ready, if anything went wrong, to read
the stack trace from top to bottom and try again."""),

    # The "world outside the REPL" beat — files, streams, printing.
    SubplotTemplate("""\
Beyond the REPL the world had files, streams, and surprises.
{farmer_phrase} opened a small notebook {place}, copying down
{concept_phrase}. {milkmaid}, {emo_tired}, watched as {farmer_he_she}
wrote the form {form_display} so the runtime could carry the work the
rest of the way."""),
]


def _ex(form, expected, concept, what, goal=""):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal)


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
    subject_title="throw", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(try (throw (Exception. \"bad\")) (catch Exception e -1))",
            expected=-1,
            concept_phrase="the exception handler returning a value after catching",
            question_what="what the catch clause returns after catching the Exception",
            goal_text="throw an Exception and catch it, returning a numeric code",
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-02 — try/catch
G7_02 = SubjectCurriculum(grade=7, subject_id="G7-02",
    subject_title="try / catch", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(try (/ 1 0) (catch Exception e -1))",
            expected=-1,
            concept_phrase="the handler for a division-by-zero error",
            question_what="the value the catch arm returns when the divide-by-zero throw is caught",
            goal_text="attempt to divide 1 by 0; when the runtime throws, catch the Exception and return -1 from the catch arm",
        ),
        SubjectExample(
            form="(try 42 (catch Exception e :caught))",
            expected=42,
            concept_phrase="a try block with no error",
            question_what="what the try block returns when no error occurs",
            goal_text="evaluate a number in a try block when no error is thrown",
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-03 — try/finally
G7_03 = SubjectCurriculum(grade=7, subject_id="G7-03",
    subject_title="try / finally", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(try 7 (finally (prn :cleanup)))",
            expected=7,
            concept_phrase="a try block with a finally clause that performs cleanup",
            question_what="what the try block returns when finally runs",
            goal_text="evaluate a number in a try block, then run a finally clause for cleanup",
        ),
        SubjectExample(
            form="(try (try (/ 1 0) (finally (prn :ran))) (catch Exception e -1))",
            expected=-1,
            concept_phrase="a finally clause running before an outer catch handler",
            question_what="what the outer catch handler returns after the inner finally runs",
            goal_text="evaluate a division by zero with an inner finally clause, caught by an outer handler",
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-04 — ex-info
G7_04 = SubjectCurriculum(grade=7, subject_id="G7-04",
    subject_title="ex-info", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(try (throw (ex-info \"bad\" {:a 1})) (catch Exception e (ex-data e)))",
            expected={":a": 1},
            concept_phrase="the data map from a caught ex-info",
            question_what="what data map is attached to the ex-info",
            goal_text="throw an ex-info with attached data and extract the data map from the caught exception",
        ),
        SubjectExample(
            form="(try (throw (ex-info \"x\" {:k :v})) (catch Exception e (:k (ex-data e))))",
            expected=":v",
            concept_phrase="a single value extracted from the caught ex-info's data",
            question_what="what value is at a specific key in the ex-info's data",
            goal_text="throw an ex-info with data, catch it, and extract the value at key :k",
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-05 — nil punning
G7_05 = SubjectCurriculum(grade=7, subject_id="G7-05",
    subject_title="nil punning", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(some? nil)",
            expected=False,
            concept_phrase="whether nil is considered some",
            question_what="the result of testing if nil is some",
            goal_text="test whether nil is considered some",
        ),
        SubjectExample(
            form="(some? 0)",
            expected=True,
            concept_phrase="whether 0 is considered some",
            question_what="the result of testing if 0 is some",
            goal_text="test whether the number 0 is considered some",
        ),
        SubjectExample(
            form="(first nil)",
            expected=None,
            concept_phrase="the first element of nil",
            question_what="what the first element of nil is",
            goal_text="get the first element of nil",
        ),
        SubjectExample(
            form="(count nil)",
            expected=0,
            concept_phrase="the number of elements in nil",
            question_what="how many elements nil contains",
            goal_text="count the number of elements in nil",
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-06 — pre/post conditions (we exercise via the {:pre [...]} on
# a defn, applied successfully).
G7_06 = SubjectCurriculum(grade=7, subject_id="G7-06",
    subject_title="pre and post conditions", fable="milkmaid",
    examples=[
        SubjectExample(
            form="((fn [x] {:pre [(pos? x)]} (* x 2)) 5)",
            expected=10,
            concept_phrase="the result of a function call that satisfies its precondition",
            question_what="what the function returns when the precondition holds",
            goal_text="call a function with a positive precondition on a positive number, doubling it",
        ),
        SubjectExample(
            form="(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e 0))",
            expected=0,
            concept_phrase="the result when a precondition is violated and caught",
            question_what="what the catch handler returns when the precondition fails",
            goal_text="call a function with a positive precondition on a negative number, catching the failure",
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-07 — assert
G7_07 = SubjectCurriculum(grade=7, subject_id="G7-07",
    subject_title="assert", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(do (assert (= 1 1)) 1)",
            expected=1,
            concept_phrase="the result when an assertion passes",
            question_what="what is returned after the assertion succeeds",
            goal_text="assert that 1 equals 1, then return a numeric code",
        ),
        SubjectExample(
            form="(try (assert (= 1 2)) (catch Throwable e 0))",
            expected=0,
            concept_phrase="the result when an assertion fails and is caught",
            question_what="what the catch handler returns when the assertion fails",
            goal_text="assert that 1 equals 2, catch the failure, and return a numeric code",
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-08 — prn / pprint (these side-effect to *out*; we use with-out-str
# to capture and inspect).
G7_08 = SubjectCurriculum(grade=7, subject_id="G7-08",
    subject_title="prn and pprint", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(with-out-str (prn 42))",
            expected="42\n",
            concept_phrase="the output captured from printing a number",
            question_what="what string is produced when printing the number 42",
            goal_text="print the number 42 and capture the output string",
        ),
        SubjectExample(
            form="(with-out-str (prn :hare))",
            expected=":hare\n",
            concept_phrase="the output captured from printing a keyword",
            question_what="what string is produced when printing a keyword",
            goal_text="print the keyword :hare and capture the output string",
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-09 — tap> (returns true; we exercise that effect).
G7_09 = SubjectCurriculum(grade=7, subject_id="G7-09",
    subject_title="tap>", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(tap> :hello)",
            expected=True,
            concept_phrase="the result of tapping a keyword into the tap pool",
            question_what="what tap> returns when sending a value",
            goal_text="send a keyword into the tap pool",
        ),
        SubjectExample(
            form="(tap> 42)",
            expected=True,
            concept_phrase="the result of tapping a number into the tap pool",
            question_what="what tap> returns when sending a number",
            goal_text="send a number into the tap pool",
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-10 — doc / source (REPL helpers; we exercise via a metadata
# lookup since `doc` itself prints).
G7_10 = SubjectCurriculum(grade=7, subject_id="G7-10",
    subject_title="doc and source", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(:doc (meta '^{:doc \"adds two\"} plus))",
            expected="adds two",
            concept_phrase="the documentation string from a symbol's metadata",
            question_what="what documentation string is attached to a symbol",
            goal_text="extract the :doc metadata value from a symbol",
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-11 — Reading stack traces (we exercise via inspecting the message
# of a caught exception).
G7_11 = SubjectCurriculum(grade=7, subject_id="G7-11",
    subject_title="Reading stack traces", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(try (throw (Exception. \"oops\")) (catch Exception e (.getMessage e)))",
            expected="oops",
            concept_phrase="the message extracted from a caught Exception",
            question_what="what message is inside the caught Exception",
            goal_text="throw an Exception with a message and extract the message from the caught exception",
        ),
        SubjectExample(
            form="(try (throw (ex-info \"trouble\" {})) (catch Exception e (.getMessage e)))",
            expected="trouble",
            concept_phrase="the message extracted from a caught ex-info",
            question_what="what message is inside the caught ex-info",
            goal_text="throw an ex-info with a message and extract the message from the caught exception",
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-12 — slurp / spit (file IO; we exercise the inverse-of-spit:
# string-shaped helpers that don't touch the filesystem).
G7_12 = SubjectCurriculum(grade=7, subject_id="G7-12",
    subject_title="slurp and spit", fable="milkmaid",
    examples=[
        # An in-memory analogue: build a string, then read it back via
        # split / count, the way slurp-then-process works in practice.
        SubjectExample(
            form='(count "hare\ntortoise\n")',
            expected=14,
            concept_phrase="the character count of a multi-line string",
            question_what="the total characters in a two-line string with newline-marks at each line's end",
            goal_text="count every character in a two-line string ending each line with a newline-mark, including the marks",
        ),
        SubjectExample(
            form="(clojure.string/split \"a\\nb\\nc\" #\"\\n\")",
            expected=["a", "b", "c"],
            concept_phrase="the vector of lines from splitting a string",
            question_what="what lines result from splitting a string on newlines",
            goal_text="split a multi-line string on newlines",
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-13 — line-seq (we exercise via the in-memory equivalent: a vector
# of lines).
G7_13 = SubjectCurriculum(grade=7, subject_id="G7-13",
    subject_title="line-seq", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(count (clojure.string/split-lines \"a\\nb\\nc\"))",
            expected=3,
            concept_phrase="the number of lines in a multi-line string",
            question_what="how many lines are in the text",
            goal_text="count the lines in a multi-line string",
        ),
        SubjectExample(
            form="(first (clojure.string/split-lines \"first\\nsecond\"))",
            expected="first",
            concept_phrase="the initial line from splitting a multi-line string",
            question_what="what the initial line is",
            goal_text="get the initial line from splitting a multi-line string",
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-14 — with-open (we exercise the macro-shape via with-out-str,
# the closest universally-available analogue).
G7_14 = SubjectCurriculum(grade=7, subject_id="G7-14",
    subject_title="with-open", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(with-out-str (println \"hare\"))",
            expected="hare\n",
            concept_phrase="the output captured from a resource-scoped block",
            question_what="what output is captured within the scope",
            goal_text="capture the output of printing within a resource-scoped block",
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-15 — *in* / *out* (we exercise *out* via with-out-str; *in* is
# harder to bind in a single form and we leave it implied).
G7_15 = SubjectCurriculum(grade=7, subject_id="G7-15",
    subject_title="*in* and *out*", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(with-out-str (print \"x\"))",
            expected="x",
            concept_phrase="the output captured by redirecting the output stream",
            question_what="what is captured when output is redirected",
            goal_text="redirect the output stream and capture what is printed",
        ),
        SubjectExample(
            form="(with-out-str (println))",
            expected="\n",
            concept_phrase="the output captured from a bare print-line call",
            question_what="what is captured when a bare println is redirected",
            goal_text="redirect the output stream and capture what a bare println produces",
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-16 — edn read
G7_16 = SubjectCurriculum(grade=7, subject_id="G7-16",
    subject_title="edn read", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(clojure.edn/read-string \"42\")",
            expected=42,
            concept_phrase="the integer parsed from an edn string",
            question_what="what integer is read from the string",
            goal_text="parse an edn integer from a string",
        ),
        SubjectExample(
            form="(clojure.edn/read-string \"{:a 1}\")",
            expected={":a": 1},
            concept_phrase="the map parsed from an edn string",
            question_what="what map is read from the string",
            goal_text="parse an edn map from a string",
        ),
        SubjectExample(
            form="(clojure.edn/read-string \"[:hare :tortoise]\")",
            expected=[":hare", ":tortoise"],
            concept_phrase="the vector parsed from an edn string",
            question_what="what vector is read from the string",
            goal_text="parse an edn vector of keywords from a string",
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-17 — JSON roundtrip (we exercise via edn-shaped data; the actual
# JSON library availability varies, but the conceptual roundtrip is
# the same as edn).
G7_17 = SubjectCurriculum(grade=7, subject_id="G7-17",
    subject_title="JSON roundtrip", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(clojure.edn/read-string (pr-str {:a 1 :b 2}))",
            expected={":a": 1, ":b": 2},
            concept_phrase="the map after writing and reading back via edn",
            question_what="what map is recovered from the roundtrip",
            goal_text="serialize a map to a string with pr-str and read it back into data with clojure.edn/read-string",
        ),
        SubjectExample(
            form="(clojure.edn/read-string (pr-str [1 2 3]))",
            expected=[1, 2, 3],
            concept_phrase="the vector after writing and reading back via edn",
            question_what="what vector is recovered from the roundtrip",
            goal_text="serialize a vector to a string with pr-str and read it back into data with clojure.edn/read-string",
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-18 — Shell command (host-specific; we exercise via a non-shell
# analogue that captures the same conceptual pattern: a command-name
# string and an args vector turning into a result).
G7_18 = SubjectCurriculum(grade=7, subject_id="G7-18",
    subject_title="Shell command", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(:cmd {:cmd \"ls\" :args [\"-l\"]})",
            expected="ls",
            concept_phrase="the command string from a shell-call descriptor",
            question_what="what command string is in the descriptor",
            goal_text="extract the command name from a shell-call descriptor map",
        ),
        SubjectExample(
            form="(count (:args {:cmd \"echo\" :args [\"hello\" \"world\"]}))",
            expected=2,
            concept_phrase="the number of arguments in a shell-call descriptor",
            question_what="how many arguments are in the descriptor",
            goal_text="count the number of arguments in a shell-call descriptor map",
        ),
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
    print(f"grade-7 tortoise-hare smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
