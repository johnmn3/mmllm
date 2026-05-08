"""Grade 7 — error handling, debugging, IO. Through tortoise-hare.

Subplot lens: Tortoise tries the form, the REPL pushes back, Tortoise
catches the trouble and tries again. Hare prefers to ignore the
warning and dash on. The fable's vanity-vs-steadiness fits errors
naturally — Tortoise reads the stack trace; Hare insists nothing is
wrong.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.tortoise_hare.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL
)
from mmllm.aesop.curriculum.tortoise_hare._metaphor_pools import (
    _SAFETYNET_SUBPLOTS, _SCROLL_SUBPLOTS, _TOOLSHED_SUBPLOTS,
)


_ERR_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    # Tortoise tries the form, catches the error, retries.
    # NOTE: {place} comma-bracketed mid-sentence (was period+place before
    # the deep-audit's LOWER_PLACE_AFTER_PERIOD check, which produced
    # "...first reading. near the meadow,..." with sentence breaking
    # mid-prep).
    SubplotTemplate("""\
{tortoise_phrase} had learned not to trust a form on first reading,
and {place} {tortoise_he_she} typed {form_display} carefully, ready
to catch whatever the REPL might throw back. {hare_phrase},
{emo_proud}, laughed and said no error would ever come — but
{tortoise} insisted on letting the runtime decide, then reading
{concept_phrase} from whatever it returned."""),

    # Hare ignores the warning; Tortoise reads the stack trace.
    SubplotTemplate("""\
A small slip of paper {place} carried the form {form_display}. {hare}
glanced at it and dashed on, certain there was no trouble.
{tortoise_phrase} sat down, {emo_patient}, and worked through
{concept_phrase} step by step — ready, if anything went wrong, to read
the stack trace from top to bottom and try again."""),

    # The "world outside the REPL" beat — files, streams, printing.
    SubplotTemplate("""\
Beyond the REPL the world had files, streams, and surprises.
{tortoise_phrase} opened a small notebook {place}, copying down
{concept_phrase}. {hare}, {emo_tired}, watched as {tortoise_he_she}
wrote the form {form_display} so the runtime could carry the work the
rest of the way."""),
]


def _ex(form, expected, concept, what, goal="", tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal, tags=tags)


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
    subject_title="throw", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(try (throw (Exception. \"bad\")) (catch Exception e -1))",
            expected=-1,
            concept_phrase="the exception handler returning a value after catching",
            question_what="what the catch clause returns after catching the Exception",
            goal_text="throw an Exception and catch it, returning a numeric code",
            scenario=(
                "Mossback the tortoise stood at the edge of the practice "
                "meadow, about to leap a narrow ditch. She knew the jump "
                "might go wrong — so she had a safety net stretched "
                "underneath before she launched. The form's value to weigh was \"bad\"."
            ),
            need=(
                "If the leap threw her sideways, the net had to catch "
                "her and hand back a placeholder so the rest of the run "
                "could continue undisturbed."
            ),
            mapping=(
                "`throw` is the failed leap; `catch` is the net that "
                "arrests the fall. Whatever the catch-arm yields is "
                "what the whole `try` form returns — the placeholder "
                "that lets the run carry on."
            ),
            resolution=(
                "the net caught her cleanly, and the form yielded the "
                "placeholder Mossback had chosen — the run continued "
                "without interruption."
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-02 — try/catch
G7_02 = SubjectCurriculum(grade=7, subject_id="G7-02",
    subject_title="try / catch", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(try (/ 1 0) (catch Exception e -1))",
            expected=-1,
            concept_phrase="the handler for a division-by-zero error",
            question_what="the value the catch arm returns when the divide-by-zero throw is caught",
            goal_text="attempt to divide 1 by 0; when the runtime throws, catch the Exception and return -1 from the catch arm",
            scenario=(
                "Mossback the tortoise was about to ask the runtime for the result of dividing {drawn.a} acorn into {drawn.b} piles — a division she knew would throw, because dividing by zero isn't a thing the runtime can do."
            ),
            need=(
                "She didn't want the throw to end the run. She wanted the form to come back with {drawn.c} as a placeholder so the rest of the work could continue."
            ),
            mapping=(
                "`try`/`catch` is a net beneath the leap. The throw "
                "still happens, but the catch-arm catches the "
                "Exception cleanly. Whatever the catch-arm returns is "
                "what the form yields — here, the placeholder -1."
            ),
            resolution=(
                'the throw happened, the catch caught it, and the form yielded {drawn.c} — the placeholder Mossback had specified.'           ),
            tags=("story",),
        ),
        SubjectExample(
            form="(try 42 (catch Exception e :caught))",
            expected=42,
            concept_phrase="a try block with no error",
            question_what="what the try block returns when no error occurs",
            goal_text="evaluate a number in a try block when no error is thrown",
            scenario=(
                "Hare had bet that the safety net would always activate "
                "— that the catch-arm was the only path a form ever "
                "took. Mossback disagreed and set up a simple trial: "
                "a plain number inside a `try`, with a catch-arm ready. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "She wanted to show Hare that when the leap goes "
                "cleanly, the net stays folded — the `try`-body's "
                "own value is what the form returns."
            ),
            mapping=(
                "`try` evaluates its body first; the catch-arm only "
                "runs if a throw happens. A smooth landing means the "
                "body's value travels straight through."
            ),
            resolution=(
                "no throw came; the body's value passed through "
                "untouched, and Hare conceded the point."
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-03 — try/finally
G7_03 = SubjectCurriculum(grade=7, subject_id="G7-03",
    subject_title="try / finally", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(try 7 (finally (prn :cleanup)))",
            expected=7,
            concept_phrase="a try block with a finally clause that performs cleanup",
            question_what="what the try block returns when finally runs",
            goal_text="evaluate a number in a try block, then run a finally clause for cleanup",
            scenario=(
                'Mossback the tortoise always folded her safety net after each practice jump, no matter how the leap went. She asked the runtime to do the same: carry out the cleanup step after the form, regardless of outcome. The values drawn fresh were 7 and :cleanup.'
            ),
            need=(
                "She needed the cleanup to run reliably while the "
                "body's value still passed through — the finally clause "
                "was housekeeping, not a replacement result."
            ),
            mapping=(
                "`finally` runs after the `try`-body, whether or not "
                "anything threw. The body's value still becomes the "
                "form's result; `finally` only side-effects."
            ),
            resolution=(
                "the cleanup ran, the body's value returned, and the "
                "practice area was tidy for the next leap."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(try (try (/ 1 0) (finally (prn :ran))) (catch Exception e -1))",
            expected=-1,
            concept_phrase="a finally clause running before an outer catch handler",
            question_what="what the outer catch handler returns after the inner finally runs",
            goal_text="evaluate a division by zero with an inner finally clause, caught by an outer handler",
            scenario=(
                'Mossback set up two nets — an inner one with a cleanup flag, and an outer one that would catch anything the inner net missed. The inner practice ditch held an impossible division. The values drawn fresh were 1, 0, :ran, and -1.'
            ),
            need=(
                "The inner net's cleanup had to run before the throw "
                "propagated outward. The outer net would then catch "
                "the throw and return the fallback placeholder."
            ),
            mapping=(
                "The inner `finally` fires before the throw escapes to "
                "the outer `catch`. The outer catch-arm then yields "
                "the placeholder — the innermost body's bad result "
                "never reaches the caller."
            ),
            resolution=(
                "the inner cleanup ran, the throw rose to the outer "
                "net, and the outer catch-arm's placeholder became the "
                "form's result."
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-04 — ex-info
G7_04 = SubjectCurriculum(grade=7, subject_id="G7-04",
    subject_title="ex-info", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(try (throw (ex-info \"bad\" {:a 1})) (catch Exception e (ex-data e)))",
            expected={":a": 1},
            concept_phrase="the data map from a caught ex-info",
            question_what="what data map is attached to the ex-info",
            goal_text="throw an ex-info with attached data and extract the data map from the caught exception",
            scenario=(
                "Mossback's alarm horn carried a data-map slip for extra context — not just a sound but a note describing what went wrong. She needed to recover that note after the catch-arm caught the alarm. The values drawn fresh were bad and :a."
            ),
            need=(
                "The slip had to come off the horn intact so she "
                "could read the data rather than guessing from "
                "the message alone."
            ),
            mapping=(
                "`ex-info` attaches a data map to the exception like a "
                "slip on the horn. `ex-data` in the catch-arm "
                "peels the slip off and returns the map."
            ),
            resolution=(
                "the data map came back — the slip's contents — "
                "giving Mossback the context she had packed."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(try (throw (ex-info \"x\" {:k :v})) (catch Exception e (:k (ex-data e))))",
            expected=":v",
            concept_phrase="a single value extracted from the caught ex-info's data",
            question_what="what value is at a specific key in the ex-info's data",
            goal_text="throw an ex-info with data, catch it, and extract the value at key :k",
            scenario=(
                "The slip of paper tied to Mossback's alarm horn had several labeled compartments. After catching the horn, she needed only the note in one specific compartment — the one labeled `:k`. The values drawn fresh were x, :k, and :v."
            ),
            need=(
                "Pulling the entire data map was more than she needed; "
                "she wanted to reach directly into the map and lift "
                "out the single value sitting at the key she cared about."
            ),
            mapping=(
                "`ex-data` returns the whole slip; applying the key "
                "`:k` to the map plucks the single value from that "
                "compartment, the way a finger finds the right pocket."
            ),
            resolution=(
                "the catch-arm returned the value from the `:k` "
                "compartment — the one note Mossback had been "
                "looking for."
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-05 — nil punning
G7_05 = SubjectCurriculum(grade=7, subject_id="G7-05",
    subject_title="nil punning", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(some? nil)",
            expected=False,
            concept_phrase="whether nil is considered some",
            question_what="the result of testing if nil is some",
            goal_text="test whether nil is considered some",
            scenario=(
                "Hare had an empty pouch — not a pouch containing "
                "something small, but a pouch containing nothing at "
                "all. Mossback wanted to know whether the runtime "
                "would call that 'something' or admit it was absent."
            ),
            need=(
                "She needed a crisp answer: does nil count as some "
                "value, or does `some?` see through the emptiness and "
                "return the negative?"
            ),
            mapping=(
                "`some?` asks whether its argument is not nil. Nil is "
                "the explicit absence of a value — not zero, not "
                "empty-string — so `some?` sees through it."
            ),
            resolution=(
                "the runtime returned the negative answer: nil is not "
                "some, and the empty pouch proved it."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(some? 0)",
            expected=True,
            concept_phrase="whether 0 is considered some",
            question_what="the result of testing if 0 is some",
            goal_text="test whether the number 0 is considered some",
            scenario=(
                "Hare insisted that zero acorns was the same as no "
                "acorns — an empty pouch and a pouch with zero were "
                "equivalent. Mossback shook her head and put the "
                "question to the runtime. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "She wanted the runtime to decide: is the number zero "
                "a real value — something present — or is it the "
                "same absence as nil?"
            ),
            mapping=(
                "`some?` returns the positive answer for any non-nil "
                "value, including zero. Zero is a number that exists; "
                "nil is the absence of any value entirely."
            ),
            resolution=(
                "the runtime confirmed zero is some — a real value — "
                "and Hare lost the argument about empty pouches."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(first nil)",
            expected=None,
            concept_phrase="the first element of nil",
            question_what="what the first element of nil is",
            goal_text="get the first element of nil",
            scenario=(
                "Hare had warned Mossback that asking for the first "
                "item in an absent collection would blow up the REPL. "
                "Mossback was not worried — she knew the runtime "
                "handled the absent collection gracefully."
            ),
            need=(
                "She needed to confirm that `first` on nil produced "
                "nothing rather than crashing, because downstream code "
                "depended on getting a safe result."
            ),
            mapping=(
                "`first` on nil returns nil — the runtime punts gently "
                "rather than throwing. This is nil punning: treating "
                "nil as an empty sequence rather than an error."
            ),
            resolution=(
                "the runtime returned absence — no crash, no alarm — "
                "and Hare's prediction was safely wrong."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(count nil)",
            expected=0,
            concept_phrase="the number of elements in nil",
            question_what="how many elements nil contains",
            goal_text="count the number of elements in nil",
            scenario=(
                "Mossback stood beside a completely absent basket — not "
                "an empty basket, but no basket at all. She asked the "
                "runtime how many items it held, expecting either a "
                "crash or a tally."
            ),
            need=(
                "She needed a numeric answer she could pass downstream, "
                "not a thrown exception, because the tally would feed "
                "into further arithmetic."
            ),
            mapping=(
                "`count` treats nil as an empty sequence and returns "
                "zero — nil punning again. The runtime never throws; "
                "it simply reports no items found."
            ),
            resolution=(
                "the runtime tallied zero items in the absent basket — "
                "a safe, arithmetic-ready result."
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-06 — pre/post conditions (we exercise via the {:pre [...]} on
# a defn, applied successfully).
G7_06 = SubjectCurriculum(grade=7, subject_id="G7-06",
    subject_title="pre and post conditions", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="((fn [x] {:pre [(pos? x)]} (* x 2)) 5)",
            expected=10,
            concept_phrase="the result of a function call that satisfies its precondition",
            question_what="what the function returns when the precondition holds",
            goal_text="call a function with a positive precondition on a positive number, doubling it",
            scenario=(
                "Before each training run, Mossback checked that the "
                "runner she was sending was fit to go — positive "
                "effort, no dead weight. She wrote a precondition "
                "fitness check into the routine itself."
            ),
            need=(
                "The routine would only run if the check passed. "
                "Sending a positive value meant the fitness gate "
                "would open and the body could execute."
            ),
            mapping=(
                "`{:pre [...]}` is the fitness check — a gate before "
                "the body. When the argument satisfies the predicate, "
                "the gate opens and the body runs normally."
            ),
            resolution=(
                "the fitness check passed, the body ran, and the "
                "doubled result came back — the run was sound."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e 0))",
            expected=0,
            concept_phrase="the result when a precondition is violated and caught",
            question_what="what the catch handler returns when the precondition fails",
            goal_text="call a function with a positive precondition on a negative number, catching the failure",
            scenario=(
                "Hare had not checked his fitness before arriving at "
                "the gate — he came with a negative value, below the "
                "threshold. The gate threw him back immediately. A "
                "safety net outside the gate was ready."
            ),
            need=(
                "The outer net needed to catch the gate's rejection "
                "and return a safe placeholder so the training session "
                "could continue with a known-good result."
            ),
            mapping=(
                "A failing `{:pre}` raises an AssertionError — the "
                "gate slams shut. An outer `try`/`catch` catches it "
                "and the catch-arm's placeholder becomes the result."
            ),
            resolution=(
                "the gate threw Hare back, the outer net caught him, "
                "and the safe placeholder became the form's result."
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-07 — assert
G7_07 = SubjectCurriculum(grade=7, subject_id="G7-07",
    subject_title="assert", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(do (assert (= 1 1)) 1)",
            expected=1,
            concept_phrase="the result when an assertion passes",
            question_what="what is returned after the assertion succeeds",
            goal_text="assert that 1 equals 1, then return a numeric code",
            scenario=(
                'Mossback always checked that the starting line was correctly marked before beginning any timed run. The assertion was her chalk-mark inspection: if the marks matched, the run could proceed. The value drawn fresh was 1.'
            ),
            need=(
                "She needed the inspection to pass silently and let the "
                "next statement execute — returning the run's starting "
                "code so the timer could begin."
            ),
            mapping=(
                "`assert` is the chalk-mark inspection: if the "
                "condition holds it returns nil silently; `do` then "
                "evaluates the next form and returns its value."
            ),
            resolution=(
                "the marks matched, the assertion passed, and the "
                "starting code came back — the run was green-lit."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(try (assert (= 1 2)) (catch Throwable e 0))",
            expected=0,
            concept_phrase="the result when an assertion fails and is caught",
            question_what="what the catch handler returns when the assertion fails",
            goal_text="assert that 1 equals 2, catch the failure, and return a numeric code",
            scenario=(
                "Hare had drawn the starting marks incorrectly — the "
                "two chalk numbers did not match. The assertion caught "
                "the mismatch immediately. A safety net was ready to "
                "catch the resulting alarm. The values drawn fresh were {drawn.a}, {drawn.b}, and {drawn.c}."
            ),
            need=(
                "The alarm had to be caught outside so the run could "
                "record a safe fallback code and continue tracking "
                "the session rather than aborting entirely."
            ),
            mapping=(
                "A failing `assert` throws an AssertionError. Wrapping "
                "it in `try`/`catch Throwable` intercepts the alarm; "
                "the catch-arm's value becomes the form's result."
            ),
            resolution=(
                "the mismatched marks triggered the alarm, the net "
                "caught it, and the fallback code was returned — the "
                "session kept its tally."
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-08 — prn / pprint (these side-effect to *out*; we use with-out-str
# to capture and inspect).
G7_08 = SubjectCurriculum(grade=7, subject_id="G7-08",
    subject_title="prn and pprint", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(with-out-str (prn 42))",
            expected="42\n",
            concept_phrase="the output captured from printing a number",
            question_what="what string is produced when printing the number 42",
            goal_text="print the number 42 and capture the output string",
            scenario=(
                "Mossback the tortoise had announced the day's acorn count in a loud voice — `prn`-style, readable by the REPL — and she wanted to capture the exact words on a scroll rather than letting them vanish into the air. The value drawn fresh was 42."
            ),
            need=(
                "She needed the announcement as a string she could "
                "inspect, store, or compare — the live output stream "
                "was too fleeting."
            ),
            mapping=(
                "`with-out-str` redirects `*out*` into a string buffer "
                "for the body's duration. `prn` writes its readable "
                "representation — number followed by a newline — into "
                "that buffer."
            ),
            resolution=(
                "the scroll held the number and its trailing "
                "newline-mark — exactly what `prn` would have "
                "announced aloud."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(with-out-str (prn :hare))",
            expected=":hare\n",
            concept_phrase="the output captured from printing a keyword",
            question_what="what string is produced when printing a keyword",
            goal_text="print the keyword :hare and capture the output string",
            scenario=(
                'Hare had shouted his own name as a keyword — colon and all — during the morning announcements. Mossback wanted to preserve the exact text of the shout on a scroll so she could check it later. The value drawn fresh was :hare.'
            ),
            need=(
                "The announcement had to be captured as a string "
                "including the colon prefix and the trailing newline, "
                "exactly as the REPL would have written it."
            ),
            mapping=(
                "`prn` writes its argument's readable representation: "
                "a keyword becomes the colon-prefixed name. "
                "`with-out-str` wraps the output in a string, "
                "newline-mark included."
            ),
            resolution=(
                "the scroll held the keyword's readable form and "
                "its trailing newline — Hare's announcement, "
                "preserved in writing."
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-09 — tap> (returns true; we exercise that effect).
G7_09 = SubjectCurriculum(grade=7, subject_id="G7-09",
    subject_title="tap>", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(tap> :hello)",
            expected=True,
            concept_phrase="the result of tapping a keyword into the tap pool",
            question_what="what tap> returns when sending a value",
            goal_text="send a keyword into the tap pool",
            scenario=(
                'Mossback the tortoise kept a quiet listener at the edge of the meadow — a watcher who would receive any value she whispered its way. She wanted to whisper a greeting without interrupting the main run. The value drawn fresh was :hello.'
            ),
            need=(
                "The whisper had to reach the listener and confirm "
                "the delivery, but the form's return value had to show "
                "that the tap itself succeeded — not the listener's work."
            ),
            mapping=(
                "`tap>` sends its value to every registered tap "
                "listener, then returns a positive confirmation. "
                "The tap is asynchronous — the main thread keeps "
                "running without waiting."
            ),
            resolution=(
                "the greeting reached the listener; `tap>` returned "
                "a positive confirmation, and the main run never "
                "paused."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(tap> 42)",
            expected=True,
            concept_phrase="the result of tapping a number into the tap pool",
            question_what="what tap> returns when sending a number",
            goal_text="send a number into the tap pool",
            scenario=(
                "During a count of the day's acorns, Mossback wanted to whisper the running tally to the listener at the meadow's edge — for observation only — without changing what the main form returned. The value drawn fresh was 42."
            ),
            need=(
                "She needed the tally to reach the listener while the "
                "form returned confirmation that the whisper "
                "was accepted, not the tally itself."
            ),
            mapping=(
                "`tap>` dispatches any value to registered listeners "
                "and returns a positive confirmation regardless of "
                "what was sent — the tally goes to the watcher, "
                "the confirmation comes back to the caller."
            ),
            resolution=(
                "the tally reached the listener; the form returned "
                "a positive confirmation, and the count continued "
                "undisturbed."
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-10 — doc / source (REPL helpers; we exercise via a metadata
# lookup since `doc` itself prints).
G7_10 = SubjectCurriculum(grade=7, subject_id="G7-10",
    subject_title="doc and source", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(:doc (meta '^{:doc \"adds two\"} plus))",
            expected="adds two",
            concept_phrase="the documentation string from a symbol's metadata",
            question_what="what documentation string is attached to a symbol",
            goal_text="extract the :doc metadata value from a symbol",
            scenario=(
                "Every routine Mossback left in the meadow had a small "
                "instruction card tied to its post — a `:doc` note "
                "explaining what the routine did. She needed to read "
                "the card for the `plus` routine."
            ),
            need=(
                "She wanted the documentation string itself, not the "
                "whole metadata map — just the readable instruction "
                "written on the card."
            ),
            mapping=(
                "`meta` retrieves the metadata map from a symbol; "
                "applying `:doc` to that map extracts the documentation "
                "string — the instruction card's text — from the "
                "`:doc` compartment."
            ),
            resolution=(
                "the instruction card's text came back, ready to "
                "be read by whoever needed to understand the routine."
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-11 — Reading stack traces (we exercise via inspecting the message
# of a caught exception).
G7_11 = SubjectCurriculum(grade=7, subject_id="G7-11",
    subject_title="Reading stack traces", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(try (throw (Exception. \"oops\")) (catch Exception e (.getMessage e)))",
            expected="oops",
            concept_phrase="the message extracted from a caught Exception",
            question_what="what message is inside the caught Exception",
            goal_text="throw an Exception with a message and extract the message from the caught exception",
            scenario=(
                "Mossback's alarm horn had sounded during a run. "
                "Rather than ignoring the alarm and dashing on like "
                "Hare, she stopped to read the message written on "
                "the horn's label — the first line of the stack trace."
            ),
            need=(
                "She needed the exact message text from the caught "
                "exception so she could understand what had gone wrong "
                "before attempting the leap again."
            ),
            mapping=(
                "`.getMessage` on the caught exception extracts the "
                "text the thrower wrote onto the alarm — like reading "
                "the label on the horn rather than just hearing it "
                "ring."
            ),
            resolution=(
                'the message text came back from the caught exception, and Mossback had the context she needed to diagnose the stumble (with `oops` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(try (throw (ex-info \"trouble\" {})) (catch Exception e (.getMessage e)))",
            expected="trouble",
            concept_phrase="the message extracted from a caught ex-info",
            question_what="what message is inside the caught ex-info",
            goal_text="throw an ex-info with a message and extract the message from the caught exception",
            scenario=(
                "This time the alarm was an `ex-info` horn — the kind "
                "that could carry both a label and a data-map slip. "
                "Mossback wanted only the label text; the data-map "
                "was empty for this alarm."
            ),
            need=(
                "She needed the label string extracted from the "
                "caught ex-info so the log could record what kind of "
                "trouble the alarm described."
            ),
            mapping=(
                "`ex-info` stores the message string as a Java "
                "Exception message; `.getMessage` reads it back "
                "regardless of whether data was also attached. "
                "The message is always on the label."
            ),
            resolution=(
                "the label text came back from the caught ex-info — "
                "the alarm's description, ready to be logged."
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-12 — slurp / spit (file IO; we exercise the inverse-of-spit:
# string-shaped helpers that don't touch the filesystem).
G7_12 = SubjectCurriculum(grade=7, subject_id="G7-12",
    subject_title="slurp and spit", fable="tortoise-hare",
    examples=[
        # An in-memory analogue: build a string, then read it back via
        # split / count, the way slurp-then-process works in practice.
        SubjectExample(
            form='(count "hare\ntortoise\n")',
            expected=14,
            concept_phrase="the character count of a multi-line string",
            question_what="the total characters in a two-line string with newline-marks at each line's end",
            goal_text="count every character in a two-line string ending each line with a newline-mark, including the marks",
            scenario=(
                "Mossback the tortoise had a small two-line message on "
                "a scroll — the word `hare` on one line, `tortoise` on "
                "the next, each line ending with a newline-mark. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "She wanted to know whether the message would fit in "
                "her message-pouch — and to know that, she needed the "
                "total character count, including the newline-marks."
            ),
            mapping=(
                "`count` on a string walks each character — visible "
                "letters and the invisible newline-marks alike — "
                "returning the total. The scroll itself is unchanged."
            ),
            resolution=(
                "the runtime tallied 14 characters: the four of `hare`, "
                "a newline, the eight of `tortoise`, and a final "
                "newline — the fit she had hoped for."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(clojure.string/split \"a\\nb\\nc\" #\"\\n\")",
            expected=["a", "b", "c"],
            concept_phrase="the vector of lines from splitting a string",
            question_what="what lines result from splitting a string on newlines",
            goal_text="split a multi-line string on newlines",
            scenario=(
                "Mossback had a scroll with three short entries, each "
                "on its own line. She wanted to process each entry "
                "separately, but the scroll handed them to her as "
                "one long string with newline-marks between them. The form's value to weigh was \"a\nb\nc\"."
            ),
            need=(
                "She needed the scroll's contents split at each "
                "newline-mark so each entry could be examined "
                "individually as its own string."
            ),
            mapping=(
                "`clojure.string/split` cuts the string at each "
                "occurrence of the pattern — here, newline-marks — "
                "and returns a vector of the pieces between them."
            ),
            resolution=(
                "the scroll's entries came back as a vector of separate strings — each line its own element, ready for individual handling (with `a\\nb\\nc` as the input value)."
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-13 — line-seq (we exercise via the in-memory equivalent: a vector
# of lines).
G7_13 = SubjectCurriculum(grade=7, subject_id="G7-13",
    subject_title="line-seq", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(count (clojure.string/split-lines \"a\\nb\\nc\"))",
            expected=3,
            concept_phrase="the number of lines in a multi-line string",
            question_what="how many lines are in the text",
            goal_text="count the lines in a multi-line string",
            scenario=(
                'Mossback had received a scroll with an unknown number of entries. Before processing she needed a line count so she could allocate the right number of pouches for the results. The value drawn fresh was a\\nb\\nc.'
            ),
            need=(
                "She wanted the total number of lines — not the lines "
                "themselves — so the count could guide the rest of "
                "the preparation."
            ),
            mapping=(
                "`split-lines` breaks the string into a sequence of "
                "lines; `count` then tallies how many the sequence "
                "contains. The two together read the scroll "
                "line-by-line in one motion."
            ),
            resolution=(
                "the tally came back — Mossback now knew how many "
                "pouches to prepare for the entries ahead."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(first (clojure.string/split-lines \"first\\nsecond\"))",
            expected="first",
            concept_phrase="the initial line from splitting a multi-line string",
            question_what="what the initial line is",
            goal_text="get the initial line from splitting a multi-line string",
            scenario=(
                "Mossback's scroll had a header line at the top — the most important entry — followed by a continuation. She needed to read only the opening line without unrolling the entire scroll. The value drawn fresh was first\\nsecond."
            ),
            need=(
                "She wanted just the header string — the opening "
                "entry — so she could check it before deciding "
                "whether to read further."
            ),
            mapping=(
                "`split-lines` breaks the string into a sequence; "
                "the head-taking function pulls only the leading "
                "element from that sequence without materialising "
                "the rest — lazy scroll-reading."
            ),
            resolution=(
                "the header string came back — Mossback had the "
                "opening line in hand without unrolling a single "
                "extra character."
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-14 — with-open (we exercise the macro-shape via with-out-str,
# the closest universally-available analogue).
G7_14 = SubjectCurriculum(grade=7, subject_id="G7-14",
    subject_title="with-open", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(with-out-str (println \"hare\"))",
            expected="hare\n",
            concept_phrase="the output captured from a resource-scoped block",
            question_what="what output is captured within the scope",
            goal_text="capture the output of printing within a resource-scoped block",
            scenario=(
                "Mossback needed to unroll a scroll, write Hare's name on it with a newline, and then roll the scroll back up cleanly — all in one scoped action. The scroll had to be handed back as a string, not left open. The value drawn fresh was hare."
            ),
            need=(
                "She needed the scroll-write scoped so the scroll was "
                "always rolled up when the block finished — and the "
                "captured contents returned as the result."
            ),
            mapping=(
                "`with-out-str` opens an output scroll, runs its body, "
                "then rolls the scroll back up and hands the contents "
                "back as a string. `println` writes the text and the "
                "newline-mark while the scroll is open."
            ),
            resolution=(
                "the scroll closed cleanly; the captured string — "
                "the name and its trailing newline-mark — was returned."
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-15 — *in* / *out* (we exercise *out* via with-out-str; *in* is
# harder to bind in a single form and we leave it implied).
G7_15 = SubjectCurriculum(grade=7, subject_id="G7-15",
    subject_title="*in* and *out*", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(with-out-str (print \"x\"))",
            expected="x",
            concept_phrase="the output captured by redirecting the output stream",
            question_what="what is captured when output is redirected",
            goal_text="redirect the output stream and capture what is printed",
            scenario=(
                'Mossback knew the meadow had a loud-voice channel — `*out*` — that every `print` call wrote to. She wanted to redirect that channel into a scroll temporarily so she could inspect what was written. The value drawn fresh was x.'
            ),
            need=(
                "She needed the redirected output as a string so the "
                "test could verify exactly what the form had announced, "
                "without relying on the live output stream."
            ),
            mapping=(
                "`with-out-str` binds `*out*` to a string writer for "
                "its scope. `print` writes its argument there without "
                "a trailing newline — the captured string is exactly "
                "what `print` produced."
            ),
            resolution=(
                "the redirected scroll held the single character "
                "Mossback had printed — the test had its string."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(with-out-str (println))",
            expected="\n",
            concept_phrase="the output captured from a bare print-line call",
            question_what="what is captured when a bare println is redirected",
            goal_text="redirect the output stream and capture what a bare println produces",
            scenario=(
                "Mossback wanted to know what a bare `println` — called "
                "without any argument — actually wrote to the output "
                "channel. Hare said nothing at all; she suspected "
                "a single newline-mark."
            ),
            need=(
                "She needed the redirect to capture whatever the bare "
                "call produced so she could compare the result to "
                "Hare's claim."
            ),
            mapping=(
                "`println` with no arguments writes only a newline-mark "
                "to `*out*`. `with-out-str` captures that newline as "
                "the returned string."
            ),
            resolution=(
                "the captured string held only the newline-mark — "
                "Mossback was right, and Hare had to concede the "
                "bare call was not silent."
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-16 — edn read
G7_16 = SubjectCurriculum(grade=7, subject_id="G7-16",
    subject_title="edn read", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(clojure.edn/read-string \"42\")",
            expected=42,
            concept_phrase="the integer parsed from an edn string",
            question_what="what integer is read from the string",
            goal_text="parse an edn integer from a string",
            scenario=(
                "Mossback received a scroll whose contents were written "
                "in EDN — the data notation the meadow uses for "
                "structured scrolls. The scroll held a single number "
                "written in plain characters. The form's value to weigh was \"42\"."
            ),
            need=(
                "She needed to convert the characters on the scroll "
                "into a real integer value the runtime could "
                "do arithmetic with — not a string."
            ),
            mapping=(
                "`clojure.edn/read-string` reads a string as EDN data. "
                "A string of digit-characters becomes the integer those "
                "digits represent — the scroll's ink becomes a number."
            ),
            resolution=(
                "the integer was read from the scroll, ready for "
                "any arithmetic Mossback had planned."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(clojure.edn/read-string \"{:a 1}\")",
            expected={":a": 1},
            concept_phrase="the map parsed from an edn string",
            question_what="what map is read from the string",
            goal_text="parse an edn map from a string",
            scenario=(
                "A scroll arrived from the supply post with a map "
                "of resource allocations written in EDN notation — "
                "curly braces, keywords, and numbers. Mossback wanted "
                "to turn the scroll's text into a live map. The form's value to weigh was \"{:a 1}\"."
            ),
            need=(
                "She needed the EDN text converted to a real Clojure "
                "map so she could look up values by key rather than "
                "parsing character-by-character herself."
            ),
            mapping=(
                "`read-string` parses the EDN text and reconstructs "
                "the data structure it describes. Curly-brace notation "
                "with keyword-value pairs becomes a Clojure map."
            ),
            resolution=(
                "the map came back from the scroll — keywords pointing "
                "to their values — ready for lookup."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(clojure.edn/read-string \"[:hare :tortoise]\")",
            expected=[":hare", ":tortoise"],
            concept_phrase="the vector parsed from an edn string",
            question_what="what vector is read from the string",
            goal_text="parse an edn vector of keywords from a string",
            scenario=(
                "The day's race roster arrived on a scroll as an EDN "
                "vector of participant keywords — square brackets, "
                "colon-prefixed names. Mossback needed it as a "
                "real vector to loop over. The form's value to weigh was \"[:hare :tortoise]\"."
            ),
            need=(
                "She needed the roster converted from its string form "
                "into an actual vector of keywords so she could call "
                "`first`, `count`, and `map` on it."
            ),
            mapping=(
                "`read-string` on a square-bracket EDN string returns "
                "a Clojure vector; each colon-prefixed word becomes "
                "a keyword. The scroll text becomes navigable data."
            ),
            resolution=(
                "the vector of participant keywords came back — "
                "the roster was live and ready for the day's planning."
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-17 — JSON roundtrip (we exercise via edn-shaped data; the actual
# JSON library availability varies, but the conceptual roundtrip is
# the same as edn).
G7_17 = SubjectCurriculum(grade=7, subject_id="G7-17",
    subject_title="JSON roundtrip", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(clojure.edn/read-string (pr-str {:a 1 :b 2}))",
            expected={":a": 1, ":b": 2},
            concept_phrase="the map after writing and reading back via edn",
            question_what="what map is recovered from the roundtrip",
            goal_text="serialize a map to a string with pr-str and read it back into data with clojure.edn/read-string",
            scenario=(
                "Mossback needed to send a resource map across the "
                "meadow — write it onto a scroll with `pr-str`, hand "
                "the scroll to a runner, then read it back from the "
                "scroll on the other side with `read-string`. The form's keyword to weigh was :a."
            ),
            need=(
                "She needed the recovered map to be identical to "
                "the original — same keys, same values — so the "
                "roundtrip was lossless."
            ),
            mapping=(
                "`pr-str` serialises the map to EDN text; "
                "`read-string` deserialises the EDN text back to a "
                "map. Together they form a write-and-read scroll "
                "roundtrip."
            ),
            resolution=(
                "the recovered map matched the original exactly — "
                "both keys and their values survived the roundtrip."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(clojure.edn/read-string (pr-str [1 2 3]))",
            expected=[1, 2, 3],
            concept_phrase="the vector after writing and reading back via edn",
            question_what="what vector is recovered from the roundtrip",
            goal_text="serialize a vector to a string with pr-str and read it back into data with clojure.edn/read-string",
            scenario=(
                "Mossback's lap-count vector — three numbers from the "
                "morning's practice — needed to be written onto a "
                "scroll, handed across the meadow, and read back "
                "as a working vector. The value at the heart of the form was 1."
            ),
            need=(
                "She needed the vector to survive the scroll journey "
                "without losing any element or changing their order "
                "on the way back."
            ),
            mapping=(
                "`pr-str` writes the vector as an EDN string; "
                "`read-string` reconstructs the vector from that "
                "string. The elements and their order are preserved "
                "through the roundtrip."
            ),
            resolution=(
                'the lap counts came back in order — the scroll journey was lossless, and the tally was intact (with `3` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-18 — Shell command (host-specific; we exercise via a non-shell
# analogue that captures the same conceptual pattern: a command-name
# string and an args vector turning into a result).
G7_18 = SubjectCurriculum(grade=7, subject_id="G7-18",
    subject_title="Shell command", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(:cmd {:cmd \"ls\" :args [\"-l\"]})",
            expected="ls",
            concept_phrase="the command string from a shell-call descriptor",
            question_what="what command string is in the descriptor",
            goal_text="extract the command name from a shell-call descriptor map",
            scenario=(
                "Mossback had borrowed a tool from the host toolshed "
                "by writing a descriptor map — a ticket with the tool's "
                "name and its arguments. Before dispatching the request "
                "she wanted to confirm the tool name on the ticket. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "She needed to read the `:cmd` field from the "
                "descriptor map so she could verify the right tool "
                "would be called before committing the request."
            ),
            mapping=(
                "The descriptor map is a ticket to the foreign toolshed. "
                "Applying `:cmd` to the map extracts the tool's name "
                "from the ticket — no dispatch yet, just inspection."
            ),
            resolution=(
                "the tool name came back from the descriptor — "
                "the ticket was correct, and the request was ready "
                "to dispatch."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(count (:args {:cmd \"echo\" :args [\"hello\" \"world\"]}))",
            expected=2,
            concept_phrase="the number of arguments in a shell-call descriptor",
            question_what="how many arguments are in the descriptor",
            goal_text="count the number of arguments in a shell-call descriptor map",
            scenario=(
                "The toolshed ticket for the echo tool had an arguments "
                "vector attached. Mossback needed to count how many "
                "arguments were packed into the ticket before "
                "dispatching it to the host. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "She wanted the argument count as a number so she "
                "could verify the ticket was fully populated before "
                "handing it to the foreign toolshed."
            ),
            mapping=(
                "`:args` extracts the arguments vector from the "
                "descriptor map; `count` tallies its elements. "
                "Together they inspect the ticket without "
                "dispatching the command."
            ),
            resolution=(
                "the argument count came back — the ticket was "
                "confirmed complete, and the dispatch could proceed."
            ),
            tags=("story",),
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
