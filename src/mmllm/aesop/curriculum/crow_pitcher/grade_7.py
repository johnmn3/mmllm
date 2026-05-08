"""Grade 7 — error handling, debugging, IO. Through crow-pitcher.

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
from mmllm.aesop.curriculum.crow_pitcher.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL
)
from mmllm.aesop.curriculum.crow_pitcher._metaphor_pools import (
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
    subject_title="throw", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(try (throw (Exception. \"bad\")) (catch Exception e -1))",
            expected=-1,
            concept_phrase="the exception handler returning a value after catching",
            question_what="what the catch clause returns after catching the Exception",
            goal_text="throw an Exception and catch it, returning a numeric code",
            scenario=(
                "Sable perched at the garden pitcher and lobbed a stone labeled "
                "\"bad\" hard into the water. Korvus had laid the soft moss pad "
                "beneath so any thrown stone would be caught before it struck "
                "the ground."
            ),
            need=(
                "Sable needed the thrown form intercepted and a safe fallback "
                "value returned rather than a crash left unresolved."
            ),
            mapping=(
                "`throw` hurls the Exception into the air. The wrapping `catch` "
                "— the moss pad — intercepts it and returns the handler's value. "
                "The dangerous stone lands softly; the fallback rises in its place."
            ),
            resolution=(
                "The moss caught the hurled stone and the handler's fallback "
                "value surfaced to beak-reach. (count: -1)"
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-02 — try/catch
G7_02 = SubjectCurriculum(grade=7, subject_id="G7-02",
    subject_title="try / catch", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(try (/ 1 0) (catch Exception e -1))",
            expected=-1,
            concept_phrase="the handler for a division-by-zero error",
            question_what="the value the catch arm returns when the divide-by-zero throw is caught",
            goal_text="attempt to divide 1 by 0; when the runtime throws, catch the Exception and return -1 from the catch arm",

            scenario=(
                "Caw leaned over the pitcher with a risky stone in her talon "
                "— a division of one stone across zero, a form the REPL would "
                "refuse. Korvus had laid a soft moss pad below to catch "
                "any falling stone safely."
            ),
            need=(
                "She wanted the risky form tried; if the stone fell badly, "
                "she needed the moss to return -1 instead of letting the "
                "crash stand unresolved."
            ),
            mapping=(
                "`try` attempts the body. If an exception is thrown, `catch` "
                "intercepts it — the moss catches the stone — and the handler "
                "returns the fallback. The crash is absorbed; the fallback surfaces."
            ),
            resolution=(
                "The division failed, the moss caught the throw, and the "
                "handler's fallback stone rose to beak-reach."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(try 42 (catch Exception e :caught))",
            expected=42,
            concept_phrase="a try block with no error",
            question_what="what the try block returns when no error occurs",
            goal_text="evaluate a number in a try block when no error is thrown",
            scenario=(
                "Sable dropped a smooth numbered stone into the pitcher under "
                "the moss pad at the garden. The stone landed cleanly — no "
                "crack, no splash, nothing for the moss to catch."
            ),
            need=(
                "Sable needed to confirm the try body's value surfaces "
                "unchanged when no error is thrown at all."
            ),
            mapping=(
                "When `try` runs without an exception, the `catch` arm is "
                "never reached. The body's value — the numbered stone — "
                "simply rises to the rim as-is."
            ),
            resolution=(
                "No error came; the try body's stone rose to the rim "
                "untouched by the moss. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-03 — try/finally
G7_03 = SubjectCurriculum(grade=7, subject_id="G7-03",
    subject_title="try / finally", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(try 7 (finally (prn :cleanup)))",
            expected=7,
            concept_phrase="a try block with a finally clause that performs cleanup",
            question_what="what the try block returns when finally runs",
            goal_text="evaluate a number in a try block, then run a finally clause for cleanup",
            scenario=(
                "Caw dropped a numbered stone into the orchard pitcher. Korvus "
                "insisted on a cleanup sweep of the moss pad after every drop, "
                "whether or not anything went wrong with the stone."
            ),
            need=(
                "Caw needed to know the stone's value while Korvus ran the "
                "cleanup sweep regardless of outcome."
            ),
            mapping=(
                "`finally` runs after the `try` body no matter what — the "
                "cleanup sweep happens whether the stone lands cleanly or not. "
                "The try body's value is still what surfaces to the beak."
            ),
            resolution=(
                "The cleanup swept the moss pad and the try body's stone value "
                "rose to the rim — both the value and the side-effect resolved. (count: 7)"
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
                "Sable nested two moss pads at the hilltop pitcher: an inner "
                "pad with a cleanup flag, and an outer pad ready to intercept "
                "any stone that slipped through after a bad division."
            ),
            need=(
                "Sable needed the inner cleanup to run first, then the outer "
                "pad to catch the failing stone and return a safe value."
            ),
            mapping=(
                "The inner `finally` sweeps before the exception escapes. The "
                "outer `catch` intercepts it and returns the handler's fallback. "
                "Both pads activate in order; the outer value is what surfaces."
            ),
            resolution=(
                "The inner cleanup ran, the outer moss caught the bad stone, "
                "and the fallback value rose to beak-reach. (count: -1)"
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-04 — ex-info
G7_04 = SubjectCurriculum(grade=7, subject_id="G7-04",
    subject_title="ex-info", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(try (throw (ex-info \"bad\" {:a 1})) (catch Exception e (ex-data e)))",
            expected={":a": 1},
            concept_phrase="the data map from a caught ex-info",
            question_what="what data map is attached to the ex-info",
            goal_text="throw an ex-info with attached data and extract the data map from the caught exception",
            scenario=(
                "Korvus hurled a specially carved stone into the meadow pitcher "
                "— not just labeled \"bad\" but also carrying a small engraved "
                "data pouch on its side. The moss pad caught it cleanly."
            ),
            need=(
                "He needed the moss to hand back not just a fallback value but "
                "the data pouch fastened to the caught stone."
            ),
            mapping=(
                "`ex-info` attaches a map to the exception stone. After `catch` "
                "intercepts it, `ex-data` lifts off the engraved pouch. The map "
                "inside is what the handler returns."
            ),
            resolution=(
                "The moss delivered the caught stone's engraved data pouch "
                "to Korvus's waiting talon. (the keyword :a)"
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
                "Caw flung a labeled stone with a small pouch of notations into "
                "the village pitcher. The moss caught it; she then pried open "
                "the pouch and looked for the mark under a specific key."
            ),
            need=(
                "Caw needed to reach into the caught stone's pouch and pull out "
                "only the value stored at the key she cared about."
            ),
            mapping=(
                "`ex-data` lifts the entire pouch off the caught exception. "
                "Applying the key to that map — `(:k ...)` — extracts the single "
                "engraved value at that slot."
            ),
            resolution=(
                "The pouch opened and the value at the chosen key rose "
                "to beak-reach."
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-05 — nil punning
G7_05 = SubjectCurriculum(grade=7, subject_id="G7-05",
    subject_title="nil punning", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(some? nil)",
            expected=False,
            concept_phrase="whether nil is considered some",
            question_what="the result of testing if nil is some",
            goal_text="test whether nil is considered some",
            scenario=(
                "Sable peered into the garden pitcher and found nothing — no "
                "stone, no pebble, just empty water. A small moss-pad gate "
                "stood ready to check whether anything real was present."
            ),
            need=(
                "Sable needed the gate to decide whether the empty pitcher "
                "counted as some-thing or no-thing."
            ),
            mapping=(
                "`some?` checks for the presence of a real value. Nil — the "
                "empty pitcher — holds nothing, so the gate closes: the answer "
                "is false. Absence is not some."
            ),
            resolution=(
                "The moss-pad gate closed on the empty pitcher and false "
                "rose to the rim."
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
                "Korvus dropped a flat zero-marked stone into the orchard "
                "pitcher. The moss-pad gate waited to see whether a zero stone "
                "counted as something real present at the pitcher."
            ),
            need=(
                "He needed to know whether a zero-marked stone — not an "
                "empty slot — would pass the some-thing test."
            ),
            mapping=(
                "`some?` returns true for any non-nil value. A zero stone is "
                "still a stone — it occupies the pitcher — so the gate opens: "
                "zero is some."
            ),
            resolution=(
                'The gate swung open on the zero stone and true rose to the rim (with `0` as the input value).'
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
                "Caw reached into the hilltop pitcher to pull the first pebble "
                "from an empty collection. She found no pebbles, no water — "
                "only nil waited at the bottom."
            ),
            need=(
                "She needed to know what first returns when the collection "
                "itself is nil, not just empty."
            ),
            mapping=(
                "`first` on nil punts gracefully: nil is treated as an empty "
                "sequence, so the first element is nothing — nil itself floats "
                "back up undisturbed."
            ),
            resolution=(
                "Caw's talon found nothing and nil drifted back up "
                "to the rim."
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
                "Sable stood at the farm pitcher counting pebbles in a nil "
                "collection. No pebbles sat inside — the pitcher held only "
                "the empty nil, yet the count had to be settled."
            ),
            need=(
                "Sable needed a definite tally from the nil collection, not "
                "an error or a crash."
            ),
            mapping=(
                "`count` on nil is nil punning in action: nil is treated as "
                "an empty sequence. The tally returns cleanly with no crash; "
                "zero marks appear on the pitcher face."
            ),
            resolution=(
                "The tally scratched zero marks on the pitcher face and "
                "the count rose safely to the rim."
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-06 — pre/post conditions (we exercise via the {:pre [...]} on
# a defn, applied successfully).
G7_06 = SubjectCurriculum(grade=7, subject_id="G7-06",
    subject_title="pre and post conditions", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="((fn [x] {:pre [(pos? x)]} (* x 2)) 5)",
            expected=10,
            concept_phrase="the result of a function call that satisfies its precondition",
            question_what="what the function returns when the precondition holds",
            goal_text="call a function with a positive precondition on a positive number, doubling it",
            scenario=(
                "Korvus set a gate stone at the village pitcher: only positive "
                "pebbles may enter and be doubled. He dropped a clearly "
                "positive pebble in and watched the gate swing open."
            ),
            need=(
                "He needed to confirm the gate passed the good pebble and "
                "returned the doubled result without triggering the guard."
            ),
            mapping=(
                "`{:pre [(pos? x)]}` is the gate stone. A positive input "
                "passes the check; the body runs and returns the doubled "
                "value. No guard fires; the result surfaces cleanly."
            ),
            resolution=(
                "The gate opened, the body ran, and the doubled result "
                "rose to the rim."
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
                "Caw shoved a negative pebble toward the same gate at the "
                "village pitcher. The gate stone blocked it at once; the moss "
                "pad beneath caught the resulting crash."
            ),
            need=(
                "She needed to know what the outer moss pad returned when "
                "the gate rejected her pebble and threw an error."
            ),
            mapping=(
                "The precondition gate fires and throws. The outer `catch` "
                "— the moss pad — intercepts the error and returns the "
                "handler's safe fallback value."
            ),
            resolution=(
                "The gate slammed, the moss caught the crash, and the "
                "handler's fallback rose to the rim. (count: -1)"
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-07 — assert
G7_07 = SubjectCurriculum(grade=7, subject_id="G7-07",
    subject_title="assert", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(do (assert (= 1 1)) 1)",
            expected=1,
            concept_phrase="the result when an assertion passes",
            question_what="what is returned after the assertion succeeds",
            goal_text="assert that 1 equals 1, then return a numeric code",
            scenario=(
                "Sable pressed a verify-stone against the meadow pitcher to "
                "confirm two identical pebbles matched. The stone glowed "
                "green — they matched — and Sable moved on to the next form."
            ),
            need=(
                "Sable needed the assertion to pass silently so the subsequent "
                "numeric stone could surface as the result."
            ),
            mapping=(
                "`assert` checks the condition — the verify-stone press. When "
                "the condition holds, it returns nil silently and the `do` "
                "block's final form is what surfaces."
            ),
            resolution=(
                'The verify-stone passed without complaint and the final numeric stone rose to the rim (with `1` as the input value).'
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
                "Korvus pressed a verify-stone against the road pitcher "
                "comparing two pebbles that did not match. The stone cracked; "
                "the moss pad beneath caught the falling shards."
            ),
            need=(
                "He needed the moss to intercept the assertion failure and "
                "return a numeric fallback instead of crashing."
            ),
            mapping=(
                "`assert` throws when the condition is false — the verify-stone "
                "cracks. The `catch Throwable` moss catches the shards and "
                "returns the handler's numeric fallback."
            ),
            resolution=(
                "The verify-stone cracked, the moss caught it, and the "
                "fallback number rose to the rim. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-08 — prn / pprint (these side-effect to *out*; we use with-out-str
# to capture and inspect).
G7_08 = SubjectCurriculum(grade=7, subject_id="G7-08",
    subject_title="prn and pprint", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(with-out-str (prn 42))",
            expected="42\n",
            concept_phrase="the output captured from printing a number",
            question_what="what string is produced when printing the number 42",
            goal_text="print the number 42 and capture the output string",
            scenario=(
                "Caw scratched a number onto a flat stone at the garden "
                "pitcher, then held the stone up to inspect the inscribed "
                "mark and newline groove left by the talon."
            ),
            need=(
                "She needed to capture the entire inscription — numeral and "
                "trailing groove — as a readable string from the stone's face."
            ),
            mapping=(
                "`prn` inscribes the value onto the output stream like a talon "
                "scratching a flat stone. `with-out-str` gathers the scratches "
                "into a string, newline groove included."
            ),
            resolution=(
                "The number and its trailing groove were gathered into a "
                "string and returned to the rim. (count: 42)"
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
                "Sable scratched a keyword label onto a flat stone at the "
                "orchard pitcher, then wrapped the output to read back the "
                "inscribed label exactly as the talon had left it."
            ),
            need=(
                "Sable needed the keyword inscription plus its trailing "
                "groove captured as a single string from the stone."
            ),
            mapping=(
                "`prn` writes the keyword to the stream, talon-mark and "
                "trailing newline groove alike. `with-out-str` collects "
                "every mark into the returned string."
            ),
            resolution=(
                'The keyword label and its groove were gathered into a string at the rim (with `hare` as the input value) (with `:hare` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-09 — tap> (returns true; we exercise that effect).
G7_09 = SubjectCurriculum(grade=7, subject_id="G7-09",
    subject_title="tap>", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(tap> :hello)",
            expected=True,
            concept_phrase="the result of tapping a keyword into the tap pool",
            question_what="what tap> returns when sending a value",
            goal_text="send a keyword into the tap pool",
            scenario=(
                "Korvus tapped a keyword pebble into the inspection basin "
                "at the village pitcher, sending it along to any waiting "
                "observers without stopping the main flow."
            ),
            need=(
                "He needed to confirm the tap delivery succeeded while the "
                "main form continued without interruption."
            ),
            mapping=(
                "`tap>` sends the value to registered tap listeners — a pebble "
                "diverted to an observer basin. It always returns true to signal "
                "the delivery was attempted, leaving the stream undisturbed."
            ),
            resolution=(
                'The pebble reached the observer basin and true rose to the rim (with `hello` as the input value) (with `:hello` as the input value).'
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
                "Caw diverted a numbered stone into the inspection basin "
                "at the hilltop pitcher. The basin accepted the stone; "
                "the pitcher's main water level was unaffected."
            ),
            need=(
                "She needed the tap to confirm successful delivery so she "
                "could trust the basin had received the stone."
            ),
            mapping=(
                "`tap>` routes the value aside for inspection without altering "
                "the main flow. The always-true return is the delivery receipt "
                "stamped on the stone's side."
            ),
            resolution=(
                "The numbered stone reached the basin and the delivery "
                "receipt — true — rose to the rim. (count: 42)"
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-10 — doc / source (REPL helpers; we exercise via a metadata
# lookup since `doc` itself prints).
G7_10 = SubjectCurriculum(grade=7, subject_id="G7-10",
    subject_title="doc and source", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(:doc (meta '^{:doc \"adds two\"} plus))",
            expected="adds two",
            concept_phrase="the documentation string from a symbol's metadata",
            question_what="what documentation string is attached to a symbol",
            goal_text="extract the :doc metadata value from a symbol",
            scenario=(
                "Sable found a carved stone at the meadow pitcher with a small "
                "side-note engraved beneath the name mark — a doc notation "
                "scratched in by whoever first inscribed the symbol."
            ),
            need=(
                "Sable needed to lift only the doc side-note off the stone's "
                "metadata face, ignoring all other engraved marks."
            ),
            mapping=(
                "`meta` reads the side-notations carved on the symbol stone. "
                "The `:doc` key extracts just the documentation groove — the "
                "brief inscription explaining the symbol's purpose."
            ),
            resolution=(
                "The doc notation lifted cleanly off the stone's face "
                "and rose to the rim. (the keyword :doc)"
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-11 — Reading stack traces (we exercise via inspecting the message
# of a caught exception).
G7_11 = SubjectCurriculum(grade=7, subject_id="G7-11",
    subject_title="Reading stack traces", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(try (throw (Exception. \"oops\")) (catch Exception e (.getMessage e)))",
            expected="oops",
            concept_phrase="the message extracted from a caught Exception",
            question_what="what message is inside the caught Exception",
            goal_text="throw an Exception with a message and extract the message from the caught exception",
            scenario=(
                "Korvus hurled a labeled stone into the farm pitcher. The moss "
                "caught it; Korvus then read the label scratched on the stone's "
                "surface to understand what went wrong."
            ),
            need=(
                "He needed to read the message label carved onto the caught "
                "exception stone rather than just discard it."
            ),
            mapping=(
                "The `catch` block intercepts the thrown stone. `.getMessage` "
                "reads the label engraved on its surface — the stack-trace's "
                "top line, the short message of the exception."
            ),
            resolution=(
                "The label inscribed on the caught stone rose to Korvus's beak as the returned message (with `oops` as the input value)."
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
                "Caw flung an ex-info stone bearing an engraved message label "
                "into the road pitcher. The moss caught it; she bent to read "
                "the label scratched across its top."
            ),
            need=(
                "Caw needed to lift the message label off the ex-info stone "
                "so she could report back what the stone said happened."
            ),
            mapping=(
                "`ex-info` carves a message onto the thrown stone alongside "
                "its data pouch. `.getMessage` reads only the surface label — "
                "the same top line a stack trace would show first."
            ),
            resolution=(
                "The surface label of the caught ex-info stone rose to Caw's beak as the message (with `trouble` as the input value)."
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-12 — slurp / spit (file IO; we exercise the inverse-of-spit:
# string-shaped helpers that don't touch the filesystem).
G7_12 = SubjectCurriculum(grade=7, subject_id="G7-12",
    subject_title="slurp and spit", fable="crow-pitcher",
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
                "Sable unrolled a flat scroll at the orchard pitcher showing "
                "two rows of talon-marks: one short word and one longer word, "
                "each ending with a newline groove scratched across the stone."
            ),
            need=(
                "Sable needed the total count of every mark on the scroll, "
                "including the newline grooves at each row's end."
            ),
            mapping=(
                "`count` on a string tallies every character — talon-marks "
                "and grooves alike. Each letter is one mark; each newline "
                "groove is one more mark in the tally."
            ),
            resolution=(
                'Every mark and groove on the scroll was tallied and the count rose to the rim. (a\nb\nc) (with `hare\ntortoise\n` as the input value)'
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
                "Korvus had a flat stone in the meadow with three short marks "
                "scratched in rows — a, then a newline-groove, b, then another "
                "groove, c. The scroll was complete; he needed to read "
                "the rows apart."
            ),
            need=(
                "He wanted to split the inscribed stone's content at each "
                "line-groove, lifting each row as a separate pebble in a "
                "new sequence."
            ),
            mapping=(
                "`clojure.string/split` reads the inscription and divides it "
                "wherever the pattern matches — here `#\"\\n\"`, the newline "
                "mark. Each stretch between grooves becomes its own pebble "
                "in the returned vector."
            ),
            resolution=(
                '[\"a\" \"b\" \"c\"] — the pebbles lifted, each row of the '
                "inscription a separate bead in the result. (a\nb\nc)"
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-13 — line-seq (we exercise via the in-memory equivalent: a vector
# of lines).
G7_13 = SubjectCurriculum(grade=7, subject_id="G7-13",
    subject_title="line-seq", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(count (clojure.string/split-lines \"a\\nb\\nc\"))",
            expected=3,
            concept_phrase="the number of lines in a multi-line string",
            question_what="how many lines are in the text",
            goal_text="count the lines in a multi-line string",
            scenario=(
                "Korvus unrolled a scroll at the hilltop pitcher showing rows "
                "of talon-marks divided by newline grooves. He needed to count "
                "how many distinct rows the scroll contained."
            ),
            need=(
                "He needed the row tally after splitting the scroll at each "
                "newline groove, not a character count."
            ),
            mapping=(
                "`split-lines` separates the scroll at every newline groove, "
                "lifting each row as a pebble. `count` then tallies the "
                "resulting pebbles to give the row count."
            ),
            resolution=(
                'The rows were split and tallied; the row count rose to the rim (with `a\\nb\\nc` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(first (clojure.string/split-lines \"alpha\\nbeta\"))",
            expected="alpha",
            concept_phrase="the initial line from splitting a multi-line string",
            question_what="what the initial line is",
            goal_text="get the initial line from splitting a multi-line string",
            scenario=(
                "Caw unrolled a two-row scroll at the meadow pitcher. She "
                "split it at the newline groove and reached for only the "
                "topmost row-pebble, ignoring the rest."
            ),
            need=(
                "She needed only the leading row lifted from the scroll, "
                "exactly as the talon had inscribed it."
            ),
            mapping=(
                "`split-lines` splits the scroll into row-pebbles; `first` "
                "picks up only the topmost one. The initial row surfaces "
                "as-is, inscription preserved."
            ),
            resolution=(
                "The topmost row-pebble lifted from the split scroll rose to Caw's beak. (with alpha\\nbeta folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-14 — with-open (we exercise the macro-shape via with-out-str,
# the closest universally-available analogue).
G7_14 = SubjectCurriculum(grade=7, subject_id="G7-14",
    subject_title="with-open", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(with-out-str (println \"hare\"))",
            expected="hare\n",
            concept_phrase="the output captured from a resource-scoped block",
            question_what="what output is captured within the scope",
            goal_text="capture the output of printing within a resource-scoped block",
            scenario=(
                "Sable opened a scoped flat stone at the village pitcher, "
                "scratched a label onto it, then sealed the scope. Whatever "
                "the talon wrote inside would be captured and returned."
            ),
            need=(
                "Sable needed the inscription made inside the scope gathered "
                "into a string — label and trailing groove both included."
            ),
            mapping=(
                "`with-out-str` opens a scoped capture, like sealing a flat "
                "stone's surface. `println` scratches inside the scope; when "
                "the scope closes, every mark is returned as a string."
            ),
            resolution=(
                "The scope closed, gathering the label and groove into "
                "a string at the rim. (the keyword :hare)"
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-15 — *in* / *out* (we exercise *out* via with-out-str; *in* is
# harder to bind in a single form and we leave it implied).
G7_15 = SubjectCurriculum(grade=7, subject_id="G7-15",
    subject_title="*in* and *out*", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(with-out-str (print \"x\"))",
            expected="x",
            concept_phrase="the output captured by redirecting the output stream",
            question_what="what is captured when output is redirected",
            goal_text="redirect the output stream and capture what is printed",
            scenario=(
                "Korvus redirected the pitcher's output spout into a small "
                "collecting basin at the farm, then scratched a single mark "
                "through the spout to see what the basin caught."
            ),
            need=(
                "He needed to confirm exactly what character landed in the "
                "basin when the spout was redirected — no trailing groove."
            ),
            mapping=(
                "`*out*` is the pitcher's output spout; `with-out-str` "
                "redirects it into a capture basin. `print` scratches the "
                "mark without a trailing groove; the basin returns it bare."
            ),
            resolution=(
                "The basin caught the single mark and returned it "
                "to the rim without a trailing groove."
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
                "Caw redirected the orchard pitcher's spout and called a bare "
                "print-line through it — no label, just the action. The "
                "collecting basin waited to see what arrived."
            ),
            need=(
                "She needed to know what a bare print-line deposits in the "
                "basin when there is nothing to inscribe but the groove itself."
            ),
            mapping=(
                "A bare `println` with no arguments writes only the newline "
                "groove to the stream. The `with-out-str` basin catches that "
                "single groove and returns it as the captured string."
            ),
            resolution=(
                "The basin caught only the newline groove and returned "
                "it to the rim."
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-16 — edn read
G7_16 = SubjectCurriculum(grade=7, subject_id="G7-16",
    subject_title="edn read", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(clojure.edn/read-string \"42\")",
            expected=42,
            concept_phrase="the integer parsed from an edn string",
            question_what="what integer is read from the string",
            goal_text="parse an edn integer from a string",
            scenario=(
                "Sable found a flat scroll at the hilltop pitcher bearing a "
                "numeral mark scratched in edn notation. The scroll's text "
                "held the number as a string of talon-marks."
            ),
            need=(
                "Sable needed to read the scroll's talon-marks as a real "
                "integer value, not as a string of characters."
            ),
            mapping=(
                "`clojure.edn/read-string` reads the talon-marks on the scroll "
                "and converts them to their data value. A numeral string "
                "becomes the integer it inscribes."
            ),
            resolution=(
                'The numeral marks on the scroll were read as an integer and rose to the rim (with `42` as the input value).'
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
                "Korvus unrolled a scroll at the garden pitcher inscribed with "
                "a map notation — a curly-braced set of key-value marks "
                "scratched in edn. He needed the live map, not the text."
            ),
            need=(
                "He needed to parse the scroll's inscription back into a real "
                "map structure usable inside the REPL."
            ),
            mapping=(
                "`clojure.edn/read-string` reads the inscription and "
                "reconstitutes the map it describes. The curly marks become "
                "a real key-value structure at the pitcher."
            ),
            resolution=(
                "The map inscription was read back into a live map "
                "and rose to Korvus's beak. (the keyword :a)"
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
                "Caw unrolled a scroll at the road pitcher marked with a "
                "bracket-wrapped list of keyword labels scratched in edn. She "
                "needed the live vector, not the raw inscription."
            ),
            need=(
                "She needed to parse the keyword list on the scroll back into "
                "a real vector structure ready for use."
            ),
            mapping=(
                "`clojure.edn/read-string` reads the bracket marks and keyword "
                "labels, reconstituting them as a live vector. The inscription "
                "becomes data the REPL can traverse."
            ),
            resolution=(
                "The bracket inscription was parsed into a live vector "
                "and rose to Caw's beak. (the keyword :hare)"
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-17 — JSON roundtrip (we exercise via edn-shaped data; the actual
# JSON library availability varies, but the conceptual roundtrip is
# the same as edn).
G7_17 = SubjectCurriculum(grade=7, subject_id="G7-17",
    subject_title="JSON roundtrip", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(clojure.edn/read-string (pr-str {:a 1 :b 2}))",
            expected={":a": 1, ":b": 2},
            concept_phrase="the map after writing and reading back via edn",
            question_what="what map is recovered from the roundtrip",
            goal_text="serialize a map to a string with pr-str and read it back into data with clojure.edn/read-string",
            scenario=(
                "Sable scratched a map onto a flat scroll at the village "
                "pitcher using pr-str, rolled it up, then unrolled and read "
                "it back with the edn reader to recover the live data."
            ),
            need=(
                "Sable needed to confirm the map survived the roundtrip — "
                "inscribed to scroll and read back as identical live data."
            ),
            mapping=(
                "`pr-str` inscribes the map as a text scroll; "
                "`clojure.edn/read-string` reads the scroll back into live "
                "data. The roundtrip preserves every key-value pair."
            ),
            resolution=(
                'The scroll was read back and the recovered map rose to the rim intact (with `:a` as the input value).'
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
                "Korvus inscribed a sequence of numbered stones onto a flat "
                "scroll at the orchard pitcher with pr-str, then unrolled it "
                "and read it back with the edn reader."
            ),
            need=(
                "He needed to confirm the vector of numbers survived the "
                "scroll-and-read roundtrip as identical live data."
            ),
            mapping=(
                "`pr-str` serializes the vector to a scroll; "
                "`clojure.edn/read-string` reads the scroll back to live data. "
                "Each numbered stone is recovered in its original order."
            ),
            resolution=(
                "The scroll was read back and the vector of numbered "
                "stones rose to Korvus's beak intact. (count: 3)"
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-18 — Shell command (host-specific; we exercise via a non-shell
# analogue that captures the same conceptual pattern: a command-name
# string and an args vector turning into a result).
G7_18 = SubjectCurriculum(grade=7, subject_id="G7-18",
    subject_title="Shell command", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(:cmd {:cmd \"ls\" :args [\"-l\"]})",
            expected="ls",
            concept_phrase="the command string from a shell-call descriptor",
            question_what="what command string is in the descriptor",
            goal_text="extract the command name from a shell-call descriptor map",
            scenario=(
                "Caw borrowed a toolshed descriptor stone from the market "
                "pitcher — a map with a command slot and an arguments slot "
                "carved on its face. She reached for only the command slot."
            ),
            need=(
                "She needed to pull the command name from the descriptor stone "
                "without touching the arguments slot beside it."
            ),
            mapping=(
                "The descriptor map is the toolshed borrowing note. `:cmd` is "
                "the slot that names which tool to fetch. Applying the key "
                "extracts just the tool name inscribed there."
            ),
            resolution=(
                "The command name inscribed in the descriptor slot rose "
                "to Caw's beak."
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
                "Sable pulled a toolshed descriptor stone from the farm "
                "pitcher and looked at the arguments slot — a small bracket "
                "of engraved labels. The count of labels was what mattered."
            ),
            need=(
                "Sable needed to tally how many argument labels were engraved "
                "in the descriptor stone's args slot."
            ),
            mapping=(
                "`:args` extracts the argument vector from the descriptor map. "
                "`count` tallies the engraved labels inside that bracket — each "
                "argument is one mark in the tally."
            ),
            resolution=(
                "The argument labels were tallied and the count rose "
                "to Sable's beak. (with {drawn.a} folded in)"
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
    print(f"grade-7 crow-pitcher smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
