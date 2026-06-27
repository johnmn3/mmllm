"""Grade 7 — error handling, debugging, IO. Through dog-shadow.

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
from mmllm.aesop.curriculum.dog_shadow.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL
)
from mmllm.aesop.curriculum.dog_shadow._metaphor_pools import (
    _SAFETYNET_SUBPLOTS, _SCROLL_SUBPLOTS, _TOOLSHED_SUBPLOTS,
)


_ERR_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    # Tortoise tries the form, catches the error, retries.
    # NOTE: {place} comma-bracketed mid-sentence (was period+place before
    # the deep-audit's LOWER_PLACE_AFTER_PERIOD check, which produced
    # "...first reading. near the meadow,..." with sentence breaking
    # mid-prep).
    SubplotTemplate("""\
{tortoise} had learned not to trust a form on first reading,
and {place} {tortoise_he_she} typed {form_display} carefully, ready
to catch whatever the REPL might throw back. {hare_phrase},
{emo_proud}, laughed and said no error would ever come — but
{tortoise} insisted on letting the runtime decide, then reading
{concept_phrase} from whatever it returned."""),

    # Hare ignores the warning; Tortoise reads the stack trace.
    SubplotTemplate("""\
A small slip of paper {place} carried {form_display}. {hare}
glanced at it and dashed on, certain there was no trouble.
{tortoise} sat down, {emo_patient}, and worked through
{concept_phrase} step by step — ready, if anything went wrong, to read
the stack trace from top to bottom and try again."""),

    # The "world outside the REPL" beat — files, streams, printing.
    SubplotTemplate("""\
Beyond the REPL the world had files, streams, and surprises.
{tortoise} opened a small notebook {place}, copying down
{concept_phrase}. {hare}, {emo_tired}, watched as {tortoise_he_she}
wrote {form_display} so the runtime could carry the work the
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
    subject_title="throw", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(try (throw (Exception. \"bad\")) (catch Exception e -1))",
            expected=-1,
            concept_phrase="the exception handler returning a value after catching",
            question_what="what the catch clause returns after catching the Exception",
            goal_text="throw an Exception and catch it, returning a numeric code",
            scenario=(
                "Rex the hound approached the log-bridge at the stream's edge, testing it carefully before crossing. He tapped once, and a crack split the wood—a bad break. But he had prepared for trouble."           ),
            need=(
                'He needed to know what the REPL would give back if the timber '
                'failed. The answer would be a code—a mark he could read—not '
                'the raw crash itself.'
            ),
            mapping=(
                'The log-bridge is the try block, the break is the Exception, '
                'the catch is his ready paw set to receive the error, and the '
                'code -1 is what he carries back across.'
            ),
            resolution=(
                'The REPL threw the trouble, his catch-paw accepted it, and he '
                'walked safe to the far bank holding the verdict in his mouth.'
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-02 — try/catch
G7_02 = SubjectCurriculum(grade=7, subject_id="G7-02",
    subject_title="try / catch", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(try (/ 1 0) (catch Exception e -1))",
            expected=-1,
            concept_phrase="the handler for a division-by-zero error",
            question_what="the value the catch arm returns when the divide-by-zero throw is caught",
            goal_text="attempt to divide 1 by 0; when the runtime throws, catch the Exception and return -1 from the catch arm",
            scenario=(
                'Bell the hound had seen the snare before. A trap that '
                'divided bones by paw-counts: 1 bone split into 0 chunks. '
                'The math would snap. She knew the REPL would object.'
            ),
            need=(
                'She wanted to catch the objection and walk on with a marked '
                'result—the code -1 in her jaws—instead of being thrown by '
                'the trap.'
            ),
            mapping=(
                'The snare is the try block, the division is the bad math, '
                'the catch is her jaw ready for the thrown error, and -1 is '
                'the safe mark she carries back.'
            ),
            resolution=(
                'The REPL caught the division-by-zero, her paw intercepted it, '
                'and she received the -1 without crashing.'
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
                'Patch the hound examined a flat stone near the pond, counting '
                'the bones laid upon it. 42 bones, solid and real. They had '
                'prepared a catch-clause just in case, but the count was sound.'
            ),
            need=(
                'They wanted to run the form in a protected block, ready to '
                'catch any trouble. Yet they also wanted the real count to '
                'come back true when nothing went wrong.'
            ),
            mapping=(
                'The stone is the try block, the count is the safe evaluation, '
                'the catch-clause waits at the bank for an error that may '
                'never come, and the result is the count itself.'
            ),
            resolution=(
                'The REPL evaluated the form, no error arose, and the catch '
                'was not needed. The count came back whole — caught.'
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-03 — try/finally
G7_03 = SubjectCurriculum(grade=7, subject_id="G7-03",
    subject_title="try / finally", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(try 7 (finally (prn :cleanup)))",
            expected=7,
            concept_phrase="a try block with a finally clause that performs cleanup",
            question_what="what the try block returns when finally runs",
            goal_text="evaluate a number in a try block, then run a finally clause for cleanup",
            scenario=(
                "Rex had carried 7 bones down from the high bank at the stream's edge, crossing the shallow ford. The crossing had worked. Yet there was always a finally—a cleanup that must come after, no matter the crossing's result."
            ),
            need=(
                'He needed the count 7 to come back safe, and he also needed '
                'to mark the cleanup point so the REPL would know: print the '
                'marker :cleanup before closing.'
            ),
            mapping=(
                'The ford is the try block, the count 7 is the value from the '
                'crossing, the finally is the mark that prints—the grooming '
                'that always happens after the form—regardless of the outcome.'
            ),
            resolution=(
                'The REPL gave back the 7, then ran the cleanup mark, then '
                'returned cleanup. The crossing was complete and tidy.'
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
                'Patch had nested two bridges—one inside the other—at the stream. '
                'The inner bridge had a division trap. A finally mark would '
                'fire :ran before the outer catch could receive the trouble.'
            ),
            need=(
                'The inner finally had to run first—a cleanup ritual—then the '
                'outer catch would receive the error and hand back the code -1 '
                'as the final result.'
            ),
            mapping=(
                'The inner bridge is the try block with the bad math; its '
                'finally is the mark that prints. The outer bridge catches the '
                'error. The finally always runs, even in the presence of error.'
            ),
            resolution=(
                'The REPL hit the division-by-zero, fired the inner finally, '
                'then the outer catch took the error, handing back -1 to Patch — ran.'
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-04 — ex-info
G7_04 = SubjectCurriculum(grade=7, subject_id="G7-04",
    subject_title="ex-info", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(try (throw (ex-info \"bad\" {:a 1})) (catch Exception e (ex-data e)))",
            expected={":a": 1},
            concept_phrase="the data map from a caught ex-info",
            question_what="what data map is attached to the ex-info",
            goal_text="throw an ex-info with attached data and extract the data map from the caught exception",
            scenario=(
                'Rex had found a bone with a scratch on it—a message-bone. '
                'The message said "bad" but carried data in a bundle: '
                '{:a 1}. He prepared to catch it and read the bundle.'
            ),
            need=(
                'He wanted to throw the marked bone so the catch would snatch '
                'it, then extract the data-bundle attached to the message so '
                'he could read what was wrapped there.'
            ),
            mapping=(
                'The message-bone is the ex-info, the scratch is the message '
                '"bad", the data bundle is the map, the catch is his ready jaw, '
                'and ex-data is the sniff that reads the bundle.'
            ),
            resolution=(
                'The REPL threw the message-bone, Rex caught it, and his sniff '
                'extracted the data. The bundle came free.'
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
                'Bell had a message-bone marked "x", with a small bag '
                'attached: {:k :v}. She needed to catch it, sniff the bag, '
                'then find the item stored at key :k.'
            ),
            need=(
                'She wanted to throw the marked bone and catch it, then reach '
                'into the bag and pull out the value at :k. That value :v '
                'was what she sought.'
            ),
            mapping=(
                'The message-bone is the ex-info, its bag is the data map, '
                'the key :k is a slot in the bag, the value :v is what lies '
                'there, and the catch extracts and reads it.'
            ),
            resolution=(
                'The REPL threw the bone, Bell caught it, opened the bag, '
                'and found :v at the key she wanted.'
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-05 — nil punning
G7_05 = SubjectCurriculum(grade=7, subject_id="G7-05",
    subject_title="nil punning", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(some? nil)",
            expected=False,
            concept_phrase="whether nil is considered some",
            question_what="the result of testing if nil is some",
            goal_text="test whether nil is considered some",
            scenario=(
                'Patch the hound stood at an empty spot at the stream\'s edge where a bone should have been. Nothing. The REPL called it nil. The test would ask: is nothing "some"?'
            ),
            need=(
                'Patch wanted to know if nil counted as something real. The '
                'verdict would be false—nothing is not something.'
            ),
            mapping=(
                'The empty spot is nil, the test some? is the hound sniffing '
                'to check if a real bone lies there, and the verdict is what '
                'the air tells.'
            ),
            resolution=(
                'The REPL sniffed the empty air and reported false. No bone, '
                'no something, just nil.'
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
                'Rex found a flat stone carved with a zero. Just a mark, '
                'but real—carved there on the rock. He asked: is this mark '
                '"some"? Is zero a thing?'
            ),
            need=(
                'He wanted to know if the zero-mark counted as something '
                'concrete. The answer would be true—even zero is a real value, '
                'not nothing.'
            ),
            mapping=(
                'The zero-mark is the number 0, the test is the sniff that '
                'checks if a real value lies there, and true means something '
                'real was found.'
            ),
            resolution=(
                'The REPL checked and found zero is indeed some—a real number '
                'on the stone — 0.'
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
                "Bell stood at the empty cache at the stream's edge. No bones lay in the hollow log. She asked the REPL: what is the first bone here?"
            ),
            need=(
                'She wanted to know what the first element would be from an '
                'empty place. The REPL would answer: none.'
            ),
            mapping=(
                'The empty cache is nil, the first-finding is the sniff into '
                'the hollow log, and the result is nil—nothing to find.'
            ),
            resolution=(
                'The REPL sniffed the empty log and returned nothing. There '
                'was no first bone.'
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
                'Patch tallied the bone-row. The tally-stone lay bare, no marks '
                'upon it. She asked the REPL: how many bones are in nil?'
            ),
            need=(
                'She wanted the count of elements from nothing. The running '
                'total would be zero—the REPL would confirm no bones were '
                'there.'
            ),
            mapping=(
                'Nil is the empty bone-row, the count is the tally-scratch on '
                'the stone, and zero is the running total when no bones have '
                'been added.'
            ),
            resolution=(
                'The REPL counted the empty row and returned zero. The tallying '
                'was done.'
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-06 — pre/post conditions (we exercise via the {:pre [...]} on
# a defn, applied successfully).
G7_06 = SubjectCurriculum(grade=7, subject_id="G7-06",
    subject_title="pre and post conditions", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="((fn [x] {:pre [(pos? x)]} (* x 2)) 5)",
            expected=10,
            concept_phrase="the result of a function call that satisfies its precondition",
            question_what="what the function returns when the precondition holds",
            goal_text="call a function with a positive precondition on a positive number, doubling it",
            scenario=(
                'Rex the hound had a nose-trail that required positive bones '
                'to work. The recipe said: {:pre [(pos? x)]}. He would sniff '
                'the number 5 into the form.'
            ),
            need=(
                'He needed the form to check: is 5 truly positive? Only then '
                'would the recipe run, doubling it to get the running total.'
            ),
            mapping=(
                'The nose-trail is the function, the precondition {:pre [...]} '
                'is the guard-point before the first step, and the doubled '
                'result 10 is what comes back when the guard passes.'
            ),
            resolution=(
                'The REPL checked the precondition—5 is positive—so the recipe '
                'ran, doubling to 10. The hound had the pre.'
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
                'Bell had a nose-trail with a guard: {:pre [(pos? x)]}. It '
                'demanded positive bones. She would try the form with -1, which '
                'violated the guard.'
            ),
            need=(
                'The precondition would fail—-1 is not positive. She had '
                'wrapped the call in a catch to handle the failure and return '
                'the code 0 instead of crashing.'
            ),
            mapping=(
                'The nose-trail is the guarded function, the precondition is '
                'the checkpoint, the bad input -1 violates the guard, the catch '
                'is the safety net, and 0 is the code she receives.'
            ),
            resolution=(
                'The REPL checked the precondition, found -1 was not positive, '
                'threw the error, and Bell caught it, receiving 0 — pre.'
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-07 — assert
G7_07 = SubjectCurriculum(grade=7, subject_id="G7-07",
    subject_title="assert", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(do (assert (= 1 1)) 1)",
            expected=1,
            concept_phrase="the result when an assertion passes",
            question_what="what is returned after the assertion succeeds",
            goal_text="assert that 1 equals 1, then return a numeric code",
            scenario=(
                'Patch the hound had scratched two marks on the rock and stood '
                'back to look. Both marks were the same—1 equals 1. The assert '
                'would check this truth.'
            ),
            need=(
                'She wanted the REPL to verify the equality. If true, the form '
                'would hand back the code 1. If false, it would throw.'
            ),
            mapping=(
                'The two scratched marks are the operands being compared, the '
                'equality test is the sniff that confirms they match, and the '
                'assert is the guard that says "they must match or fail."'
            ),
            resolution=(
                'The REPL checked: 1 equals 1? Yes. The assert passed, and '
                'Patch received the code 1 — 1.'
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
                'Rex had scratched two marks on the stone: 1 and 2. They were '
                'different. The assert would check if they matched—they did not. '
                'He had wrapped it in a try/catch.'
            ),
            need=(
                'He wanted the REPL to verify the equality. Since 1 does not '
                'equal 2, the assert would throw, and his catch would receive '
                'the code 0.'
            ),
            mapping=(
                'The two marks are the operands, the assert is the test that '
                'demands they match, the try wraps the test, the catch waits '
                'for failure, and 0 is the code for "assertion failed."'
            ),
            resolution=(
                'The REPL checked: 1 equals 2? No. The assert threw, the catch '
                'received it, and Rex got the code 0 — 0.'
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-08 — prn / pprint (these side-effect to *out*; we use with-out-str
# to capture and inspect).
G7_08 = SubjectCurriculum(grade=7, subject_id="G7-08",
    subject_title="prn and pprint", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(with-out-str (prn 42))",
            expected="42\n",
            concept_phrase="the output captured from printing a number",
            question_what="what string is produced when printing the number 42",
            goal_text="print the number 42 and capture the output string",
            scenario=(
                'Bell had a message-bone with a number scratched on it: 42. '
                'She wanted to send it from her bank to the far side. The prn '
                'would scratch the mark into the message.'
            ),
            need=(
                'She needed to capture what the scratch would produce—the '
                'number 42 plus a newline—so she could read it back as a '
                'complete message-string.'
            ),
            mapping=(
                'The message-bone is the form, the number 42 is the value '
                'being printed, prn is the scratching act, the newline is the '
                'final mark, and the captured string is the message carried '
                'across the bank.'
            ),
            resolution=(
                'The REPL scratched 42 and the newline onto the message-bone, '
                'then Bell captured the scratch-marks as a string to carry — 42.'
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
                "Patch held a message-bone at the stream's edge with a keyword scratched on it: :hare. She wanted to print it and capture the exact scratches as a carried message."
            ),
            need=(
                'She needed to know what the scratches would be when prn wrote '
                'the keyword. The output would be :hare with a newline-mark '
                'at the end.'
            ),
            mapping=(
                'The message-bone is the form, the keyword :hare is the mark '
                'being printed, prn is the scratching motion, and the captured '
                'string is the completed message.'
            ),
            resolution=(
                'The REPL scratched :hare and the newline, Patch captured the '
                'marks as a message-string, ready to carry it onward — hare.'
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-09 — tap> (returns true; we exercise that effect).
G7_09 = SubjectCurriculum(grade=7, subject_id="G7-09",
    subject_title="tap>", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(tap> :hello)",
            expected=True,
            concept_phrase="the result of tapping a keyword into the tap pool",
            question_what="what tap> returns when sending a value",
            goal_text="send a keyword into the tap pool",
            scenario=(
                "Rex stood at the stream's edge at the stream's edge, holding a message-bone. The keyword :hello was scratched on it. He wanted to tap it into the pool—send it for inspection."           ),
            need=(
                'He needed to know if the tap> would succeed. The REPL would '
                'confirm true—the message reached the pool.'
            ),
            mapping=(
                'The message-bone is the keyword value, tap> is the action of '
                'tapping it into the stream, the pool is the inspection-stream, '
                'and true confirms the message arrived.'
            ),
            resolution=(
                'The REPL tapped the message :hello into the pool and confirmed '
                'true. Rex had sent the signal — hello.'
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
                'Bell held a message-bone with a number scratched on it: 42. '
                'She stood at the bank and wanted to tap it into the pool for '
                'inspection.'
            ),
            need=(
                'She needed to confirm the tapping would succeed. When tap> ran, '
                'the REPL would answer true—the number had entered the pool.'
            ),
            mapping=(
                'The message-bone is the number 42, tap> is the tapping action, '
                'the pool is the inspection-stream, and true confirms success.'
            ),
            resolution=(
                'The REPL tapped the number 42 into the pool and returned the verdict. '
                'The message was received — 42.'
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-10 — doc / source (REPL helpers; we exercise via a metadata
# lookup since `doc` itself prints).
G7_10 = SubjectCurriculum(grade=7, subject_id="G7-10",
    subject_title="doc and source", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(:doc (meta '^{:doc \"adds two\"} plus))",
            expected="adds two",
            concept_phrase="the documentation string from a symbol's metadata",
            question_what="what documentation string is attached to a symbol",
            goal_text="extract the :doc metadata value from a symbol",
            scenario=(
                'Patch found a message-bone marked "plus" at the stone at the stream\'s edge. The bone carried metadata—extra scratch-marks that said what the symbol meant. She wanted to read that documentation.'
            ),
            need=(
                "She needed to extract the doc-string from the symbol's metadata. "
                'The REPL would sniff the scratch-marks and hand back the recorded '
                'meaning.'
            ),
            mapping=(
                'The message-bone is the symbol, the metadata is the extra '
                'scratch-marks, the :doc key is the label for the explanation, '
                'and the doc value is the documentation she sought.'
            ),
            resolution=(
                'The REPL read the metadata, found the :doc mark, and returned '
                'the documentation string. Patch understood what the symbol did — doc.'
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-11 — Reading stack traces (we exercise via inspecting the message
# of a caught exception).
G7_11 = SubjectCurriculum(grade=7, subject_id="G7-11",
    subject_title="Reading stack traces", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(try (throw (Exception. \"oops\")) (catch Exception e (.getMessage e)))",
            expected="oops",
            concept_phrase="the message extracted from a caught Exception",
            question_what="what message is inside the caught Exception",
            goal_text="throw an Exception with a message and extract the message from the caught exception",
            scenario=(
                'Rex found a broken log-bridge with a message bone attached at '
                'the stream. He prepared to catch it and sniff the message.'
            ),
            need=(
                'He wanted to throw the bone and catch it, then read the message '
                'that was written on the bone — whatever the carved word was.'
            ),
            mapping=(
                'The broken log is the Exception, the message bone is the error '
                'object, the carved word is the mark on the bone, and .getMessage '
                'is the sniff that reads the mark.'
            ),
            resolution=(
                'The REPL threw the bone, Rex caught it, and his sniff extracted the message the bone had carried (with `oops` as the input value).'
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
                'Bell found a message-bone marked "trouble" at the bank. The bone '
                'carried no extra data—just the message. She would catch it and '
                'read the scratch.'
            ),
            need=(
                'She wanted to throw the bone, catch it, and extract the message '
                'that was scratched on it: "trouble".'
            ),
            mapping=(
                'The message-bone is the ex-info, "trouble" is the scratch-mark, '
                'the empty bundle {} holds no extra data, and .getMessage is the '
                'sniff that reads the main mark.'
            ),
            resolution=(
                'The REPL threw the message-bone, Bell caught it, and her sniff '
                'extracted the message: "trouble".'
            ),
            tags=("story",),
        ),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-12 — slurp / spit (file IO; we exercise the inverse-of-spit:
# string-shaped helpers that don't touch the filesystem).
G7_12 = SubjectCurriculum(grade=7, subject_id="G7-12",
    subject_title="slurp and spit", fable="dog-shadow",
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
                'Patch held a message-bone carved with two lines: a word, a '
                'newline-mark, another word, and a final newline-mark. She wanted '
                'to count every scratch.'
            ),
            need=(
                'She needed the precise count of characters—including the newline '
                "marks themselves—to know the message's true length."
            ),
            mapping=(
                'The message-bone is the multi-line string, each character is a '
                'scratch, the newline-marks are carved into the bone, and the '
                'count is the running total of all marks and spaces.'
            ),
            resolution=(
                'The REPL counted every scratch on the bone: 14 marks in all, '
                'including the newlines. The message was fully measured — hare\ntortoise\n.'
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
                'Rex found a message-bone at the stream\'s edge carved with three letters separated by newline-marks: "a\\nb\\nc". He wanted to split the message at each newline and read the pieces.'
            ),
            need=(
                'He needed to break the message into individual lines. The split '
                'would cut at each newline-mark and give back a vector of the '
                'separate pieces.'
            ),
            mapping=(
                'The message-bone is the string, the newline-marks are the '
                'break-points, the split is the cutting action, and the vector of '
                'lines is what he received.'
            ),
            resolution=(
                'The REPL split the message at each newline and handed back a '
                'vector: ["a", "b", "c"]. The message was parsed into lines.'
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-13 — line-seq (we exercise via the in-memory equivalent: a vector
# of lines).
G7_13 = SubjectCurriculum(grade=7, subject_id="G7-13",
    subject_title="line-seq", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(count (clojure.string/split-lines \"a\\nb\\nc\"))",
            expected=3,
            concept_phrase="the number of lines in a multi-line string",
            question_what="how many lines are in the text",
            goal_text="count the lines in a multi-line string",
            scenario=(
                'Bell held a message-bone carved with three lines. She split it '
                'into a vector of line-bones and wanted to count how many '
                'line-pieces she held.'
            ),
            need=(
                'She needed the running total of lines. The REPL would split the '
                'message and give back the count of separate lines.'
            ),
            mapping=(
                'The message-bone is the multi-line string, split-lines is the '
                'cutting into pieces, each piece is a line, and the count is the '
                'running total of line-bones in the vector.'
            ),
            resolution=(
                'The REPL split the message into lines and counted them: 3 lines in all. Bell held the precise tally (with `a\\nb\\nc` as the input value).'
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
                'Patch found a message-bone with two lines carved on it. She split '
                'it into separate line-bones and wanted to take the opening piece '
                'to read it.'
            ),
            need=(
                'She needed the initial line from the vector of lines. The REPL '
                'would split the message and hand back the opening line.'
            ),
            mapping=(
                'The message-bone is the multi-line string, split-lines is the '
                'cutting action, the leading line-bone is what she seeks, and the '
                'result is the mark on that opening piece.'
            ),
            resolution=(
                'The REPL split the message into lines and handed Patch the opening line. She could now read it (with `first\\nsecond` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-14 — with-open (we exercise the macro-shape via with-out-str,
# the closest universally-available analogue).
G7_14 = SubjectCurriculum(grade=7, subject_id="G7-14",
    subject_title="with-open", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(with-out-str (println \"hare\"))",
            expected="hare\n",
            concept_phrase="the output captured from a resource-scoped block",
            question_what="what output is captured within the scope",
            goal_text="capture the output of printing within a resource-scoped block",
            scenario=(
                'Rex held a message-bone at the stream\'s edge and wanted to send a word to the far bank. He would carve "hare" into the bone and send it, but first he needed to capture the exact scratches it would produce.'
            ),
            need=(
                'He wanted to write the word and collect the marks it made—the '
                'newline and all—within a scope that kept them safe. The '
                'resource-block would hold the message until he was ready.'
            ),
            mapping=(
                'The message-bone is the form, the println is the scratching '
                'act, the resource-scope is the protected boundary, and the '
                'captured marks form the completed message he carries.'
            ),
            resolution=(
                'The REPL scratched "hare" and the newline within the scope, '
                'captured the marks on the message-bone, and handed them to Rex '
                'to carry across.'
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-15 — *in* / *out* (we exercise *out* via with-out-str; *in* is
# harder to bind in a single form and we leave it implied).
G7_15 = SubjectCurriculum(grade=7, subject_id="G7-15",
    subject_title="*in* and *out*", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(with-out-str (print \"x\"))",
            expected="x",
            concept_phrase="the output captured by redirecting the output stream",
            question_what="what is captured when output is redirected",
            goal_text="redirect the output stream and capture what is printed",
            scenario=(
                'Bell found a message-bone at the stream and wanted to redirect '
                'its output. She wrote "x" on the bone and needed to capture '
                'exactly what the print would show.'
            ),
            need=(
                'She wanted to print the mark and collect it—no newline, just '
                'the letter itself. The output stream would be redirected into '
                'a message she could read.'
            ),
            mapping=(
                'The message-bone is the form, the redirected stream is the '
                'path from the print-act to the capture, the letter "x" is '
                'what print writes, and the captured message is what she '
                'receives.'
            ),
            resolution=(
                'The REPL redirected the output, printed "x", and Bell caught '
                'the mark on her message-bone. The single letter was hers to '
                'carry.'
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
                "Patch stood at the bank at the stream's edge with a bare println form. No word, no number—just the bare line-ending mark. She redirected the output to see what the bare println would produce."
            ),
            need=(
                'She needed to capture what println gives when called with no '
                'arguments—just the newline-mark itself. The stream would be '
                'redirected to collect it.'
            ),
            mapping=(
                'The message-bone is the form, the redirected stream is the '
                'capture-boundary, the bare println is the act that writes a '
                'newline, and the captured message is the single mark alone.'
            ),
            resolution=(
                'The REPL redirected the output, ran the bare println, and '
                'captured the newline mark. Patch held the mark on her message-bone.'
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-16 — edn read
G7_16 = SubjectCurriculum(grade=7, subject_id="G7-16",
    subject_title="edn read", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(clojure.edn/read-string \"42\")",
            expected=42,
            concept_phrase="the integer parsed from an edn string",
            question_what="what integer is read from the string",
            goal_text="parse an edn integer from a string",
            scenario=(
                'Rex found a message-bone carved with the scratch "42". The bone '
                'held the marks, but he needed to parse them into a real number '
                'the REPL could use.'
            ),
            need=(
                'He wanted to read the message-string and turn it into living '
                'data. The edn parser would sniff the scratches and hand back the '
                'integer 42.'
            ),
            mapping=(
                'The message-bone is the string, the scratches are the marks for '
                '42, the edn parser is the sniff that reads the marks, and the '
                'integer is what comes back alive.'
            ),
            resolution=(
                'The REPL sniffed the message-bone, recognized the edn form, and '
                'handed Rex the integer 42. The scratch had become real data.'
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
                "Bell held a message-bone at the stream's edge carved with the marks for a map: {:a 1}. The bone had the scratches, but she needed the REPL to parse them into a living map she could use."
            ),
            need=(
                'She wanted to turn the message-string into structured data. The '
                'edn parser would read the marks and hand her the parsed map.'
            ),
            mapping=(
                'The message-bone is the string, the key-and-value marks are the '
                'scratches, the edn parser is the sniff, and the parsed map is '
                'what comes back as real data.'
            ),
            resolution=(
                'The REPL parsed the message-bone, recognized the edn form, and '
                'handed Bell the map. The scratches had become living structure.'
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
                'Patch found a message-bone inscribed with the marks for a '
                'vector of keywords: [:hare :tortoise]. The scratches lay on '
                'the bone, but she needed to parse them into a vector the REPL '
                'could work with.'
            ),
            need=(
                'She wanted the message-string turned into a vector of real '
                'keywords. The edn parser would sniff the scratches and hand '
                'back the parsed vector.'
            ),
            mapping=(
                'The message-bone is the string, the keyword marks and brackets '
                'are the scratches, the edn parser is the sniff, and the vector '
                'is what comes back as real data.'
            ),
            resolution=(
                'The REPL parsed the message-bone, recognized the edn form, and '
                'handed Patch the vector. The scratches became living structure.'
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-17 — JSON roundtrip (we exercise via edn-shaped data; the actual
# JSON library availability varies, but the conceptual roundtrip is
# the same as edn).
G7_17 = SubjectCurriculum(grade=7, subject_id="G7-17",
    subject_title="JSON roundtrip", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(clojure.edn/read-string (pr-str {:a 1 :b 2}))",
            expected={":a": 1, ":b": 2},
            concept_phrase="the map after writing and reading back via edn",
            question_what="what map is recovered from the roundtrip",
            goal_text="serialize a map to a string with pr-str and read it back into data with clojure.edn/read-string",
            scenario=(
                'Rex held a map in his jaws and wanted to send it to the far '
                'bank as a message-bone. He would use pr-str to scratch the map '
                'into marks, then parse it back into a map on arrival.'
            ),
            need=(
                'He needed to write the map to a string, then read it back into '
                'a living map. The roundtrip—write then read—would preserve the '
                'structure through the journey.'
            ),
            mapping=(
                'The map in the jaws is the data, pr-str is the scratch-making, '
                'the message-bone is the string, and edn/read-string is the '
                'sniff that brings it back to life.'
            ),
            resolution=(
                'The REPL scratched the map as a string, then sniffed the marks and handed Rex the parsed map. The roundtrip was complete — b (with `:a` as the input value).'
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
                "Bell held a vector of numbers at the stream's edge and wanted to carry it across the stream. She would write it to a message-bone with pr-str, then parse it back on the far side."
            ),
            need=(
                'She needed to turn the vector into scratches that could travel, '
                'then turn them back into a vector when she arrived. The write-'
                'then-read would carry the structure safely.'
            ),
            mapping=(
                'The vector in her grip is the data, pr-str is the scratching, '
                'the message-bone is the string, and edn/read-string is the '
                'sniff that restores it.'
            ),
            resolution=(
                'The REPL scratched the vector as marks on the message-bone, '
                'then sniffed the scratches and handed Bell the vector back. '
                'The roundtrip carried it across whole — 3.'
            ),
            tags=("story",),
        ),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-18 — Shell command (host-specific; we exercise via a non-shell
# analogue that captures the same conceptual pattern: a command-name
# string and an args vector turning into a result).
G7_18 = SubjectCurriculum(grade=7, subject_id="G7-18",
    subject_title="Shell command", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(:cmd {:cmd \"ls\" :args [\"-l\"]})",
            expected="ls",
            concept_phrase="the command string from a shell-call descriptor",
            question_what="what command string is in the descriptor",
            goal_text="extract the command name from a shell-call descriptor map",
            scenario=(
                'Patch the hound had borrowed a tool-bag from the kennel-master. '
                'The bag held a map with named slots: one for :cmd "ls" and one '
                'for :args. She wanted to read just the command-name slot.'
            ),
            need=(
                'She needed to extract the command string from the labeled '
                'compartment. The tool-slot :cmd held "ls", and she needed the '
                'REPL to pull just that string.'
            ),
            mapping=(
                'The tool-bag is the map, the named compartments are the keys, '
                'the command string is what lies at :cmd, and reading it is the '
                'lookup from the labeled slot.'
            ),
            resolution=(
                'The REPL opened the tool-bag, found the :cmd compartment, and '
                'handed Patch "ls". The command was in her jaws.'
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
                'Rex borrowed a second tool-bag from the kennel-master. It held '
                'a map with :cmd "echo" and :args containing a vector of '
                'argument-strings. He wanted to count how many arguments were '
                'stashed in that compartment.'
            ),
            need=(
                'He needed to open the :args slot and count the vector inside. '
                'The tool-bag would reveal the argument-count for the shell '
                'call.'
            ),
            mapping=(
                'The tool-bag is the map, :args is a named compartment, the '
                'vector inside is the list of arguments, and counting gives '
                'the tally.'
            ),
            resolution=(
                'The REPL opened the tool-bag, pulled the vector from :args, '
                'and counted two arguments. Rex had the cmd he needed.'
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
    print(f"grade-7 dog-shadow smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
