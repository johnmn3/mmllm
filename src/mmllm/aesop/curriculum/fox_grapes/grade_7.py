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
        _ex("(try (throw (Exception. \"bad\")) (catch Exception e :thrown))", ":thrown", 'the form', 'the value the form evaluates to',
            goal="signal an error and catch what the REPL hands back",
            scenario="Renard the fox reached for a rotten berry from a high trellis, knowing it might fall badly. He held a catching-cloth tight below.",
            need="When the berry dropped (as he suspected it would), the cloth had to catch the falling fruit and name what fell.",
            mapping="throw creates the falling error; catch is the cloth's grip. The cloth holds the name the catcher-clause specifies, not the error itself.",
            resolution="the catching-cloth held firm — the keyword the catch-arm promised came back, the error safely named.",
            tags=()),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-02 — try/catch
G7_02 = SubjectCurriculum(grade=7, subject_id="G7-02",
    subject_title="try / catch", fable="fox-grapes",
    examples=[
        _ex("(try (/ 1 0) (catch Exception e :caught))", ":caught", 'the form', 'the value the form evaluates to',
            goal="attempt a division and let the cloth catch the stumble",
            scenario="Vix the fox tried to split one berry evenly among zero mouths — a task that makes no sense. The catching-cloth swayed below.",
            need="When the division failed (as dividing by zero must), the cloth had to catch the error and return what the catcher specified.",
            mapping="try opens the stretch; the division attempt happens inside. If the division stumbles, the catch-arm's value is what comes back. If it succeeds, catch is skipped.",
            resolution="the impossible division fell into the cloth — the catcher's keyword came back, the error caught and named cleanly.",
            tags=()),
        _ex("(try 42 (catch Exception e :caught))", 42, 'the form', 'the value the form evaluates to',
            goal="evaluate a form that holds no error, letting it pass cleanly through the cloth",
            scenario="Sly the fox reached for 42 berries from a full basket, knowing the count was safe. A catching-cloth hung loosely below.",
            need="With no error to catch, the value had to pass cleanly through the cloth to Sly's slate.",
            mapping="try wraps the form; 42 evaluates with no stumble. The catch-arm stays unrun because no error fell. The cloth lets the good fruit pass.",
            resolution="42 passed through the cloth untroubled — the form's value came back, the cloth's safety structure left untested but ready.",
            tags=()),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-03 — try/finally
G7_03 = SubjectCurriculum(grade=7, subject_id="G7-03",
    subject_title="try / finally", fable="fox-grapes",
    examples=[
        _ex("(try 7 (finally :cleanup))", 7, 'the form', 'the value the form evaluates to',
            goal="return a value from a try block while the finally-clause runs its housekeeping",
            scenario="Renard counted 7 berries into a small basket. He had tied a cleanup-knot to his sleeve to tighten before setting the basket down.",
            need="The 7 berries had to reach the slate, but the cleanup-knot had to be pulled regardless of whether the count was right.",
            mapping="try evaluates the body; finally runs its cleanup-form no matter what. The body's value is what comes back to the slate. Finally doesn't change the answer.",
            resolution="7 berries reached the slate cleanly, and the cleanup-knot was pulled as promised — both happened in order.",
            tags=()),
        _ex("(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))", ":caught", 'the form', 'the value the form evaluates to',
            goal="catch an error from a nested try whose finally has already run",
            scenario="Vix tried to split one berry by zero inside a nested try-catch. The inner cloth had a cleanup-knot attached; the outer cloth stood ready to catch any falling error.",
            need="The inner division would fail, its finally would run, and the outer catch had to catch what fell through.",
            mapping="The inner try's finally runs even when an error occurs. The error then propagates to the outer catch. Finally executes; catch then handles the error.",
            resolution="the inner cleanup ran its course, the error fell through to the outer cloth, and the catcher's keyword came back.",
            tags=()),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-04 — ex-info
G7_04 = SubjectCurriculum(grade=7, subject_id="G7-04",
    subject_title="ex-info", fable="fox-grapes",
    examples=[
        _ex("(try (throw (ex-info \"bad\" {:a 1})) (catch Exception e (ex-data e)))", {":a": 1}, 'the form', 'the value the form evaluates to',
            goal="throw an error labeled with data, then extract the data from what the cloth caught",
            scenario="Sly the fox spotted a bad berry and marked a small slate tile with its flaw-notes before tossing it into the cloth below.",
            need="The cloth had to catch the berry and return the flaw-notes, not the berry itself, so Sly could read what went wrong.",
            mapping="ex-info attaches a data-map to the error. The cloth catches the error. ex-data extracts the map. The catch-arm can read what ex-data pulls out.",
            resolution="the cloth held the error, ex-data revealed the flaw-notes inside, and the map came back to be read.",
            tags=()),
        _ex("(try (throw (ex-info \"x\" {:k :v})) (catch Exception e (:k (ex-data e))))", ":v", 'the form', 'the value the form evaluates to',
            goal="catch an error, extract its data-map, and pull one named value from it",
            scenario="Vix threw a marked pebble into the cloth with a small tag {:k :v} attached. She needed to read just the :v part of what she'd written.",
            need="From the caught error's data, Vix had to extract the field labeled :k and pass back its value.",
            mapping="ex-data reads the map from the caught error. Keywords can index into the map like a basket. The :k lookup returns the value :v.",
            resolution="the pebble landed in the cloth, its data read, the :k field extracted, and :v came back to the slate.",
            tags=()),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-05 — nil punning
G7_05 = SubjectCurriculum(grade=7, subject_id="G7-05",
    subject_title="nil punning", fable="fox-grapes",
    examples=[
        _ex("(some? nil)", False, 'the form', 'the value the form evaluates to',
            goal="test whether nil is something (it is not)",
            scenario="Renard opened an empty pouch and asked if anything was inside. The pouch held nothing — not even zero berries, but true absence.",
            need="The REPL had to say no, the pouch held nothing, a definite false answer to the question of somethingness.",
            mapping="some? returns false only for nil. An empty thing is still a thing; nil is the absence of a thing. The test distinguishes them.",
            resolution="the REPL confirmed — nil is not something; false came back, the question settled.",
            tags=()),
        _ex("(some? 0)", True, 'the form', 'the value the form evaluates to',
            goal="test whether zero is something (it is)",
            scenario="Sly held a slate marked with 0. He asked the REPL if zero was a real value. The slate was there, the mark was there — zero existed.",
            need="The REPL had to say yes, zero is a value, not absence. A true answer to the question of somethingness.",
            mapping="some? returns true for anything except nil. Zero is a value, so some? says true. Only nil fails the test.",
            resolution="the REPL confirmed — zero is something; true came back, the question settled.",
            tags=()),
        _ex("(first nil)", None, 'the form', 'the value the form evaluates to',
            goal="ask for the first element of nil (which has no elements)",
            scenario="Vix asked for the head of a procession that didn't exist — nil, not an empty basket, but no procession at all.",
            need="The REPL had to say: there is no first, because there's no procession to have a first. Nil back in answer.",
            mapping="first expects a sequence; nil is not a sequence. first of nil returns nil, the null answer to a null input.",
            resolution="there was no procession, so there was no first; nil came back, the answer exact.",
            tags=()),
        _ex("(count nil)", 0, 'the form', 'the value the form evaluates to',
            goal="count the size of nil (which has no size)",
            scenario="Renard asked how many berries were in a pouch that didn't exist — not an empty pouch, but no pouch at all.",
            need="The REPL had to say: zero. Not because nil is a basket of zero berries, but because nil has zero parts.",
            mapping="count treats nil as size zero. count of nil returns 0. This is convenient: nil is handled like an empty collection.",
            resolution="the nonexistent pouch held zero berries; 0 came back, the count correct.",
            tags=()),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-06 — pre/post conditions (we exercise via the {:pre [...]} on
# a defn, applied successfully).
G7_06 = SubjectCurriculum(grade=7, subject_id="G7-06",
    subject_title="pre and post conditions", fable="fox-grapes",
    examples=[
        _ex("((fn [x] {:pre [(pos? x)]} (* x 2)) 5)", 10, 'the form', 'the value the form evaluates to',
            goal="double a value, with a guard that insists the input is positive",
            scenario="Sly the fox set up a recipe that doubled any input, but first checked: is the input positive? A guard-rule stood at the door.",
            need="When 5 walked in (a positive number), the guard nodded, the doubling happened, and 10 came back.",
            mapping="The {:pre [...]} clause is a guard that runs before the recipe's body. If the guard-rule fails, an error falls. If it passes, the body runs.",
            resolution="5 passed the guard, was doubled, and 10 reached the slate — the recipe worked as designed.",
            tags=()),
        _ex("(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))", ":pre-failed", 'the form', 'the value the form evaluates to',
            goal="try to pass a negative number to a recipe with a guard requiring positive input",
            scenario="Vix tried the same recipe with -1 (a negative number). The guard-rule stood ready at the door, expecting positive.",
            need="When -1 approached the door, the guard-rule failed. The recipe never ran. The cloth caught the broken guard as an error.",
            mapping="The pre-guard checks before the body runs. If it fails, an error is thrown into the catching-cloth. The catcher can name what fell.",
            resolution="the guard blocked the negative input, an error fell, the cloth caught it, and the catcher's name came back.",
            tags=()),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-07 — assert
G7_07 = SubjectCurriculum(grade=7, subject_id="G7-07",
    subject_title="assert", fable="fox-grapes",
    examples=[
        _ex("(do (assert (= 1 1)) :ok)", ":ok", 'the form', 'the value the form evaluates to',
            goal="check that 1 equals 1, then continue with the next form",
            scenario="Renard checked his counting: is 1 truly equal to 1? Yes. He nodded and moved to the next task, marking :ok on his slate.",
            need="The assertion had to pass (1 does equal 1), so the form continued to the next line and :ok was reached.",
            mapping="assert checks a condition. If true, it continues silently. If false, it throws an error. Here, equality holds, so the do proceeds.",
            resolution="the assertion passed, the form continued undisturbed, and :ok reached the slate.",
            tags=()),
        _ex("(try (assert (= 1 2)) (catch Throwable e :asserted))", ":asserted", 'the form', 'the value the form evaluates to',
            goal="test an assertion that fails, catch the resulting error",
            scenario="Vix checked: does 1 equal 2? No. She'd written that very check inside a cloth ready to catch the error.",
            need="The false assertion would throw an error; the cloth had to catch it and return what the catcher specified.",
            mapping="assert checks the condition. If false, it throws a Throwable into the cloth. catch grisp what fell and returns the catcher-form.",
            resolution="the false assertion threw an error into the cloth; the catcher caught it and :asserted came back.",
            tags=()),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-08 — prn / pprint (these side-effect to *out*; we use with-out-str
# to capture and inspect).
G7_08 = SubjectCurriculum(grade=7, subject_id="G7-08",
    subject_title="prn and pprint", fable="fox-grapes",
    examples=[
        _ex("(with-out-str (prn 42))", "42\n", 'the form', 'the value the form evaluates to',
            goal="capture what prn writes when printing the number 42",
            scenario="Sly opened a small parchment-scroll and told prn to write 42 onto the page. The scroll trapped the writing inside, word for word.",
            need="With nothing leaking to the outside world, the scroll had to hold exactly what prn had written: the number and the line-break.",
            mapping="prn writes a value to output and adds a newline. with-out-str wraps that output, capturing it as a string. The string is what comes back.",
            resolution="the scroll held prn's work — the digits 42 and the line-break that follows — trapped and readable.",
            tags=()),
        _ex("(with-out-str (prn :fox))", ":fox\n",
            "capturing prn applied to the keyword :fox",
            "the string \":fox\\n\" produced by prn",
            goal="capture what prn writes when printing the keyword :fox",
            scenario="Vix opened a fresh parchment-scroll and told prn to write a keyword onto the page. The scroll trapped every character inside.",
            need="With nothing escaping to the outside, the scroll had to hold exactly what prn had written: the keyword text and the line-break.",
            mapping="prn writes its argument to output in readable form. with-out-str intercepts that output and returns it as a string. The form returns the captured text.",
            resolution="the scroll held prn's writing — the keyword and the newline that follows — trapped and intact.",
            tags=()),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-09 — tap> (returns true; we exercise that effect).
G7_09 = SubjectCurriculum(grade=7, subject_id="G7-09",
    subject_title="tap>", fable="fox-grapes",
    examples=[
        _ex("(tap> :hello)", True, 'the form', 'the value the form evaluates to'),
        _ex("(tap> 42)", True, 'the form', 'the value the form evaluates to'),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-10 — doc / source (REPL helpers; we exercise via a metadata
# lookup since `doc` itself prints).
G7_10 = SubjectCurriculum(grade=7, subject_id="G7-10",
    subject_title="doc and source", fable="fox-grapes",
    examples=[
        _ex("(:doc (meta '^{:doc \"adds two\"} plus))", "adds two", 'the form', 'the value the form evaluates to'),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-11 — Reading stack traces (we exercise via inspecting the message
# of a caught exception).
G7_11 = SubjectCurriculum(grade=7, subject_id="G7-11",
    subject_title="Reading stack traces", fable="fox-grapes",
    examples=[
        _ex("(try (throw (Exception. \"oops\")) (catch Exception e (.getMessage e)))", "oops", 'the form', 'the value the form evaluates to'),
        _ex("(try (throw (ex-info \"trouble\" {})) (catch Exception e (.getMessage e)))", "trouble", 'the form', 'the value the form evaluates to'),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-12 — slurp / spit (file IO; we exercise the inverse-of-spit:
# string-shaped helpers that don't touch the filesystem).
G7_12 = SubjectCurriculum(grade=7, subject_id="G7-12",
    subject_title="slurp and spit", fable="fox-grapes",
    examples=[
        # An in-memory analogue: build a string, then read it back via
        # split / count, the way slurp-then-process works in practice.
        _ex("(count \"hare\\ntortoise\\n\")", 14, 'the form', 'the value the form evaluates to'),
        _ex("(clojure.string/split \"a\\nb\\nc\" #\"\\n\")", ["a", "b", "c"], 'the form', 'the value the form evaluates to'),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-13 — line-seq (we exercise via the in-memory equivalent: a vector
# of lines).
G7_13 = SubjectCurriculum(grade=7, subject_id="G7-13",
    subject_title="line-seq", fable="fox-grapes",
    examples=[
        _ex("(count (clojure.string/split-lines \"a\\nb\\nc\"))", 3, 'the form', 'the value the form evaluates to'),
        _ex("(first (clojure.string/split-lines \"first\\nsecond\"))", "first", 'the form', 'the value the form evaluates to'),
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
        _ex("(with-out-str (print \"x\"))", "x", 'the form', 'the value the form evaluates to'),
        _ex("(with-out-str (println))", "\n", 'the form', 'the value the form evaluates to'),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-16 — edn read
G7_16 = SubjectCurriculum(grade=7, subject_id="G7-16",
    subject_title="edn read", fable="fox-grapes",
    examples=[
        _ex("(clojure.edn/read-string \"42\")", 42, 'the form', 'the value the form evaluates to'),
        _ex("(clojure.edn/read-string \"{:a 1}\")", {":a": 1}, 'the form', 'the value the form evaluates to'),
        _ex("(clojure.edn/read-string \"[:fox :grapes]\")", [":fox", ":grapes"], 'the form', 'the value the form evaluates to'),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-17 — JSON roundtrip (we exercise via edn-shaped data; the actual
# JSON library availability varies, but the conceptual roundtrip is
# the same as edn).
G7_17 = SubjectCurriculum(grade=7, subject_id="G7-17",
    subject_title="JSON roundtrip", fable="fox-grapes",
    examples=[
        _ex("(clojure.edn/read-string (pr-str {:a 1 :b 2}))", {":a": 1, ":b": 2}, 'the form', 'the value the form evaluates to'),
        _ex("(clojure.edn/read-string (pr-str [1 2 3]))", [1, 2, 3], 'the form', 'the value the form evaluates to'),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-18 — Shell command (host-specific; we exercise via a non-shell
# analogue that captures the same conceptual pattern: a command-name
# string and an args vector turning into a result).
G7_18 = SubjectCurriculum(grade=7, subject_id="G7-18",
    subject_title="Shell command", fable="fox-grapes",
    examples=[
        _ex("(:cmd {:cmd \"ls\" :args [\"-l\"]})", "ls", 'the form', 'the value the form evaluates to'),
        _ex("(count (:args {:cmd \"echo\" :args [\"hello\" \"world\"]}))", 2, 'the form', 'the value the form evaluates to'),
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
