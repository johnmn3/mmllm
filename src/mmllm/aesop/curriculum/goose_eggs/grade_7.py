"""Grade 7 — error handling, debugging, IO. Through goose-eggs.

Subplot lens: the patient {owner} notices a missing egg, checks the
basket, and sets a careful trap to catch the cause. The impatient
{visitor} would rather guess and dash on. The fable's patience-vs-greed
dynamic fits errors naturally — {owner} reads the stack trace and
ex-data; {visitor} insists nothing went wrong.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.goose_eggs.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)


_ERR_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    # Owner notices a missing egg, sets a careful trap, catches the cause.
    # NOTE: {place} comma-bracketed mid-sentence (was period+place before
    # the deep-audit's LOWER_PLACE_AFTER_PERIOD check, which produced
    # "...first glance. near the market,..." with sentence breaking
    # mid-prep).
    SubplotTemplate("""\
{owner_phrase} had learned not to trust the morning basket on first
glance, and {place} {owner_he_she} typed {form_display} carefully,
ready to catch whatever the REPL might throw back, the way one sets
a quiet trap for whatever takes an egg in the night. {visitor_phrase},
{emo_greedy}, laughed and said no error would ever come — but {owner}
insisted on letting the runtime decide, then reading {concept_phrase}
from whatever it returned."""),

    # Visitor brushes past the warning; owner reads the stack trace.
    SubplotTemplate("""\
A small slip of paper {place} carried the form {form_display}.
{visitor} glanced at it and hurried on toward the market, certain
there was no trouble. {owner_phrase} sat down by the egg-basket,
{emo_patient}, and worked through {concept_phrase} step by step —
ready, if anything went wrong, to read the stack trace from top to
bottom and try again."""),

    # The "world outside the REPL" beat — files, streams, a careful
    # ledger of what the runtime hands back.
    SubplotTemplate("""\
Beyond the REPL the world had files, streams, and small surprises.
{owner_phrase} opened a leather ledger {place}, copying down
{concept_phrase} beside the morning's egg-tally. {visitor},
{emo_content}, watched as {owner_he_she} wrote the form {form_display}
so the runtime could carry the work the rest of the way."""),
]


def _ex(form, expected, concept, what):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what)


_PLAN_G7 = _PLAN_POOL + (
    "I wrap the form in try/catch and let the REPL handle the error.",
    "I use ex-info to attach data to the error.",
    "I let the REPL read the file or stream for me.",
    "I print or tap the value for inspection, then return.",
    "I set a careful trap with try/catch the way one watches the basket.",
)


# ─────────────────────── 18 grade-7 subjects ───────────────────────


# G7-01 — throw (we wrap throw in try/catch so the form actually
# returns a value instead of bubbling up).
G7_01 = SubjectCurriculum(grade=7, subject_id="G7-01",
    subject_title="throw", fable="goose-eggs",
    examples=[
        _ex("(try (throw (Exception. \"bad\")) (catch Exception e :thrown))",
            ":thrown",
            "throwing an exception that is then caught",
            "the keyword :thrown returned after the throw is caught"),
    ], subplots=_ERR_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-02 — try/catch
G7_02 = SubjectCurriculum(grade=7, subject_id="G7-02",
    subject_title="try / catch", fable="goose-eggs",
    examples=[
        _ex("(try (/ 1 0) (catch Exception e :caught))", ":caught",
            "a division by zero wrapped in try/catch",
            "the keyword :caught returned by the catch branch"),
        _ex("(try 42 (catch Exception e :caught))", 42,
            "a try with no error — the body's value is returned",
            "the value 42 from the no-error branch"),
    ], subplots=_ERR_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-03 — try/finally
G7_03 = SubjectCurriculum(grade=7, subject_id="G7-03",
    subject_title="try / finally", fable="goose-eggs",
    examples=[
        _ex("(try 7 (finally :cleanup))", 7,
            "a try whose finally clause runs but doesn't change the value",
            "the value 7 from the body"),
        _ex("(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))",
            ":caught",
            "a finally that runs before the outer catch fires",
            "the keyword :caught (the outer catch handles the divide-by-zero)"),
    ], subplots=_ERR_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-04 — ex-info
G7_04 = SubjectCurriculum(grade=7, subject_id="G7-04",
    subject_title="ex-info", fable="goose-eggs",
    examples=[
        _ex("(try (throw (ex-info \"bad\" {:a 1})) (catch Exception e (ex-data e)))",
            {":a": 1},
            "throwing an ex-info with attached data, then reading it back",
            "the data map {:a 1} pulled from the caught ex-info"),
        _ex("(try (throw (ex-info \"x\" {:k :v})) (catch Exception e (:k (ex-data e))))",
            ":v",
            "extracting a single key from the caught ex-info's data",
            "the value :v at key :k in the ex-data"),
    ], subplots=_ERR_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-05 — nil punning
G7_05 = SubjectCurriculum(grade=7, subject_id="G7-05",
    subject_title="nil punning", fable="goose-eggs",
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
    ], subplots=_ERR_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-06 — pre/post conditions (we exercise via the {:pre [...]} on
# a defn, applied successfully).
G7_06 = SubjectCurriculum(grade=7, subject_id="G7-06",
    subject_title="pre and post conditions", fable="goose-eggs",
    examples=[
        _ex("((fn [x] {:pre [(pos? x)]} (* x 2)) 5)", 10,
            "a fn with a :pre condition that is satisfied",
            "the value returned when the precondition holds and 5 is doubled"),
        _ex("(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))",
            ":pre-failed",
            "a :pre condition that fails, caught by surrounding try",
            "the keyword :pre-failed when the pre-check rejects -1"),
    ], subplots=_ERR_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-07 — assert
G7_07 = SubjectCurriculum(grade=7, subject_id="G7-07",
    subject_title="assert", fable="goose-eggs",
    examples=[
        _ex("(do (assert (= 1 1)) :ok)", ":ok",
            "an assert that passes, followed by a return value",
            "the keyword :ok returned after the assert succeeds"),
        _ex("(try (assert (= 1 2)) (catch Throwable e :asserted))",
            ":asserted",
            "an assert that fails, caught by surrounding try",
            "the keyword :asserted when the assertion rejects (= 1 2)"),
    ], subplots=_ERR_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-08 — prn / pprint (these side-effect to *out*; we use with-out-str
# to capture and inspect).
G7_08 = SubjectCurriculum(grade=7, subject_id="G7-08",
    subject_title="prn and pprint", fable="goose-eggs",
    examples=[
        _ex("(with-out-str (prn 42))", "42\n",
            "capturing the output of (prn 42)",
            "the string \"42\\n\" produced by prn"),
        _ex("(with-out-str (prn :hare))", ":hare\n",
            "capturing prn applied to the keyword :hare",
            "the string \":hare\\n\" produced by prn"),
    ], subplots=_ERR_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-09 — tap> (returns true; we exercise that effect).
G7_09 = SubjectCurriculum(grade=7, subject_id="G7-09",
    subject_title="tap>", fable="goose-eggs",
    examples=[
        _ex("(tap> :hello)", True,
            "tapping a value into the tap pool",
            "the boolean true returned by tap>"),
        _ex("(tap> 42)", True,
            "tapping the number 42 into the tap pool",
            "the boolean true returned by tap>"),
    ], subplots=_ERR_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-10 — doc / source (REPL helpers; we exercise via a metadata
# lookup since `doc` itself prints).
G7_10 = SubjectCurriculum(grade=7, subject_id="G7-10",
    subject_title="doc and source", fable="goose-eggs",
    examples=[
        _ex("(:doc (meta '^{:doc \"adds two\"} plus))", "adds two",
            "the :doc metadata on a symbol",
            "the string \"adds two\" from the metadata"),
    ], subplots=_ERR_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-11 — Reading stack traces (we exercise via inspecting the message
# of a caught exception).
G7_11 = SubjectCurriculum(grade=7, subject_id="G7-11",
    subject_title="Reading stack traces", fable="goose-eggs",
    examples=[
        _ex("(try (throw (Exception. \"oops\")) (catch Exception e (.getMessage e)))",
            "oops",
            "extracting the message from a caught exception",
            "the string \"oops\" from the caught Exception"),
        _ex("(try (throw (ex-info \"trouble\" {})) (catch Exception e (.getMessage e)))",
            "trouble",
            "the message of a caught ex-info",
            "the string \"trouble\""),
    ], subplots=_ERR_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-12 — slurp / spit (file IO; we exercise the inverse-of-spit:
# string-shaped helpers that don't touch the filesystem).
G7_12 = SubjectCurriculum(grade=7, subject_id="G7-12",
    subject_title="slurp and spit", fable="goose-eggs",
    examples=[
        # An in-memory analogue: build a string, then read it back via
        # split / count, the way slurp-then-process works in practice.
        _ex("(count \"hare\\ntortoise\\n\")", 14,
            "the length of a multi-line string",
            "the count of characters in \"hare\\ntortoise\\n\""),
        _ex("(clojure.string/split \"a\\nb\\nc\" #\"\\n\")", ["a", "b", "c"],
            "splitting a slurped-style string on newlines",
            "the vector [\"a\" \"b\" \"c\"] of three lines"),
    ], subplots=_ERR_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-13 — line-seq (we exercise via the in-memory equivalent: a vector
# of lines).
G7_13 = SubjectCurriculum(grade=7, subject_id="G7-13",
    subject_title="line-seq", fable="goose-eggs",
    examples=[
        _ex("(count (clojure.string/split-lines \"a\\nb\\nc\"))", 3,
            "the number of lines in a small text",
            "the count of lines in \"a\\nb\\nc\""),
        _ex("(first (clojure.string/split-lines \"first\\nsecond\"))",
            "first",
            "the first line of a small text",
            "the string \"first\""),
    ], subplots=_ERR_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-14 — with-open (we exercise the macro-shape via with-out-str,
# the closest universally-available analogue).
G7_14 = SubjectCurriculum(grade=7, subject_id="G7-14",
    subject_title="with-open", fable="goose-eggs",
    examples=[
        _ex("(with-out-str (println \"hare\"))", "hare\n",
            "a resource-scoped capture of println output",
            "the string \"hare\\n\" from the scoped block"),
    ], subplots=_ERR_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-15 — *in* / *out* (we exercise *out* via with-out-str; *in* is
# harder to bind in a single form and we leave it implied).
G7_15 = SubjectCurriculum(grade=7, subject_id="G7-15",
    subject_title="*in* and *out*", fable="goose-eggs",
    examples=[
        _ex("(with-out-str (print \"x\"))", "x",
            "redirecting *out* via with-out-str and printing",
            "the string \"x\" captured from *out*"),
        _ex("(with-out-str (println))", "\n",
            "a bare println redirected through *out*",
            "the string \"\\n\""),
    ], subplots=_ERR_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-16 — edn read
G7_16 = SubjectCurriculum(grade=7, subject_id="G7-16",
    subject_title="edn read", fable="goose-eggs",
    examples=[
        _ex("(clojure.edn/read-string \"42\")", 42,
            "reading an edn integer from a string",
            "the integer 42 read from \"42\""),
        _ex("(clojure.edn/read-string \"{:a 1}\")", {":a": 1},
            "reading an edn map from a string",
            "the map {:a 1} read from \"{:a 1}\""),
        _ex("(clojure.edn/read-string \"[:hare :tortoise]\")",
            [":hare", ":tortoise"],
            "reading an edn vector of keywords",
            "the vector [:hare :tortoise]"),
    ], subplots=_ERR_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-17 — JSON roundtrip (we exercise via edn-shaped data; the actual
# JSON library availability varies, but the conceptual roundtrip is
# the same as edn).
G7_17 = SubjectCurriculum(grade=7, subject_id="G7-17",
    subject_title="JSON roundtrip", fable="goose-eggs",
    examples=[
        _ex("(clojure.edn/read-string (pr-str {:a 1 :b 2}))",
            {":a": 1, ":b": 2},
            "writing then reading back a small map",
            "the map {:a 1 :b 2} after the roundtrip"),
        _ex("(clojure.edn/read-string (pr-str [1 2 3]))", [1, 2, 3],
            "round-tripping a vector through pr-str then edn/read-string",
            "the vector [1 2 3]"),
    ], subplots=_ERR_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-18 — Shell command (host-specific; we exercise via a non-shell
# analogue that captures the same conceptual pattern: a command-name
# string and an args vector turning into a result).
G7_18 = SubjectCurriculum(grade=7, subject_id="G7-18",
    subject_title="Shell command", fable="goose-eggs",
    examples=[
        _ex("(:cmd {:cmd \"ls\" :args [\"-l\"]})", "ls",
            "the :cmd portion of a shell-call descriptor map",
            "the string \"ls\""),
        _ex("(count (:args {:cmd \"echo\" :args [\"hello\" \"world\"]}))",
            2,
            "the number of args in a shell-call descriptor",
            "the count of args"),
    ], subplots=_ERR_SUBPLOTS, plan_pool=_PLAN_G7)


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
    print(f"grade-7 goose-eggs smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
