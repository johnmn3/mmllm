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
            scenario="Margery carried her milk pail down a steep path toward market, eager to deliver quickly.",
            need="A loose stone caught her heel. She stumbled, nearly spilling the pail. But she steadied herself and walked on, knowing that one stumble was not the end of the journey.",
            mapping="A thrown exception is a stumble on the market road. The catch clause is her quick steadying step that keeps the pail upright and lets her continue the walk—the journey doesn't end; it finds a new rhythm.",
            resolution='The form returned a recovery value, and the careful walk continued safely to the market (with `-1` as the input value).',
            tags=("story",),
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
            scenario="Lila walked carefully to the dairy, carrying a pail of cream to be divided among the neighbors.",
            need="But when she tried to share the cream equally with no neighbors present—dividing by zero—the motion made no sense. What would happen?",
            mapping="An impossible division is an error thrown at the milkmaid. The catch block is the careful handler—not a net to prevent the error, but a graceful response that lets her substitute a recovery value and continue.",
            resolution="The form caught the error and returned a recovery code, keeping the day's work from being lost (with `1` as the input value) (with `-1` as the input value).",
            tags=("story",),
        ),
        SubjectExample(
            form="(try 42 (catch Exception e :caught))",
            expected=42,
            concept_phrase="a try block with no error",
            question_what="what the try block returns when no error occurs",
            goal_text="evaluate a number in a try block when no error is thrown",
            scenario="Clara carried her pail safely down the path, with no stones to trip her and no rain to fall.",
            need="She wanted to know: if the walk goes well and no stumbles occur, what does the form return?",
            mapping="A try block with no error is an unbroken walk to market. The form evaluates the value inside, just as the milkmaid reaches her destination unchanged.",
            resolution="The form returned the number itself—42—because no error occurred to interrupt the careful walk.",
            tags=("story",),
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
            scenario="Nan reached the market gate, her pail full and ready. But before she entered, she needed to sweep and tidy her workspace.",
            need="The finally clause must run whether the journey was smooth or not—a cleanup task that happens at the end no matter what.",
            mapping="The try block is the main walk to market; the finally clause is the cleanup work that happens afterward, rain or shine, success or stumble. Neither changes what the walk achieved.",
            resolution="The form returned 7, the original value, and the cleanup task ran—both the result and the final duty completed.",
            tags=("story",),
        ),
        SubjectExample(
            form="(try (try (/ 1 0) (finally (prn :ran))) (catch Exception e -1))",
            expected=-1,
            concept_phrase="a finally clause running before an outer catch handler",
            question_what="what the outer catch handler returns after the inner finally runs",
            goal_text="evaluate a division by zero with an inner finally clause, caught by an outer handler",
            scenario="Bess carried her pail home, but at the first gate she tried an impossible sharing task—dividing by zero. The inner try stumbled.",
            need="Before the outer catch could step in and steady her, the inner cleanup must run. What order do these tasks take?",
            mapping="The inner finally always runs after its try, whether success or error. Then the outer catch catches what escapes. Cleanup happens before recovery, not instead of it.",
            resolution="The form ran the inner cleanup, then let the outer catch return -1, proving the finally always completes its task first.",
            tags=("story",),
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
            scenario="Margery stumbled on the path and her pail tumbled. But she had pinned a note to her apron with details of what went wrong—the cow's name, the time, the weather.",
            need="When she caught herself and the pail, she needed to read that attached note. What information was saved with the error?",
            mapping="An ex-info error is a stumble that carries context notes. Catching it and extracting the attached data is reading those notes to understand what happened when things went wrong.",
            resolution='The form caught the error and extracted the attached data—all the context that was saved along with the mistake (with `:a` as the input value).',
            tags=("story",),
        ),
        SubjectExample(
            form="(try (throw (ex-info \"x\" {:k :v})) (catch Exception e (:k (ex-data e))))",
            expected=":v",
            concept_phrase="a single value extracted from the caught ex-info's data",
            question_what="what value is at a specific key in the ex-info's data",
            goal_text="throw an ex-info with data, catch it, and extract the value at key :k",
            scenario="Lila's pail tipped, and she had tucked a slip with key-value pairs into her pocket—cow-id, milk-type, time-of-day.",
            need="From the scattered notes after the stumble, she needed to retrieve just one piece: the milk-type. Could she extract a single value from the attached data?",
            mapping="The catch extracts the whole data map, but then you can pull out just one value by its key name—like finding one detail in a list of notes.",
            resolution='The form retrieved the specific value attached to the chosen key, proving that errors can carry rich context and you can query what you need (with `:k` as the input value).',
            tags=("story",),
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
            scenario="Clara gazed at an empty basket that had held cream, now containing nothing—nil, a void.",
            need="Is the void something? Is nothing one of something's cousins? She wanted to test carefully.",
            mapping="Nil is the empty pail—truly empty, not a pail holding zero coins. The test some? asks: is this void a form of 'something'? It is not.",
            resolution="The form returned the verdict—nil is not considered some; it stands entirely apart.",
            tags=("story",),
        ),
        SubjectExample(
            form="(some? 0)",
            expected=True,
            concept_phrase="whether 0 is considered some",
            question_what="the result of testing if 0 is some",
            goal_text="test whether the number 0 is considered some",
            scenario="Nan held up a coin that bore no mark—zero value written on its face—and asked the farmer: is this something?",
            need="Does zero count as a value, a form of something? Or is it treated as empty?",
            mapping="Zero is a value in the pail, not nothing. The test some? checks: is this a form of 'something'? Zero is—it has weight, it exists. Nil does not.",
            resolution="The form returned the verdict—zero is something, different from nil's emptiness.",
            tags=("story",),
        ),
        SubjectExample(
            form="(first nil)",
            expected=None,
            concept_phrase="the first element of nil",
            question_what="what the first element of nil is",
            goal_text="get the first element of nil",
            scenario="Bess reached for the first cream vessel in her lineup, but they were all gone. The pail was empty—nil.",
            need="What is the first element when there are no elements at all?",
            mapping="Nil is a pail with no contents. Asking for the first cream when the pail is empty returns nil again—there is nothing to return.",
            resolution="The form returned nil because nil has no first element; it is the absence of elements entirely.",
            tags=("story",),
        ),
        SubjectExample(
            form="(count nil)",
            expected=0,
            concept_phrase="the number of elements in nil",
            question_what="how many elements nil contains",
            goal_text="count the number of elements in nil",
            scenario="Margery stood with an empty pail—not even a drop left. She wanted to count how many pails' worth remained.",
            need="How many elements are in nothing? Does nothing count as zero elements?",
            mapping="Nil is the pail with zero drops, zero coins, zero anything. Counting nil yields zero—the void tallies to the number zero.",
            resolution="The form returned zero—nil contains zero elements, not some unknown count.",
            tags=("story",),
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
            scenario="Lila handed five coins to a merchant who promised: 'I will only take positive amounts—no debts, no empty hands.'",
            need="She had five coins, which is positive. Would the merchant accept and double her wealth?",
            mapping="A precondition is the merchant's promise—'I work only with positive amounts.' Passing five, which is positive, satisfies the promise. The form proceeds and returns the doubled result.",
            resolution='The form returned 10 because the precondition was satisfied—five is positive, and the work was done (with `5` as the input value).',
            tags=("story",),
        ),
        SubjectExample(
            form="(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e 0))",
            expected=0,
            concept_phrase="the result when a precondition is violated and caught",
            question_what="what the catch handler returns when the precondition fails",
            goal_text="call a function with a positive precondition on a negative number, catching the failure",
            scenario="Clara handed negative-one coins to the same merchant, who had set the rule: 'Only positive amounts.'",
            need="She tried to break the merchant's promise. Would the form catch the violation and handle it gracefully?",
            mapping="Passing -1, which is negative, violates the precondition. The merchant refuses—an error is thrown. The outer catch catches this violation and returns a recovery value.",
            resolution="The form returned 0 because the precondition was violated, caught by the try-catch, proving that conditions are enforced at the gate.",
            tags=("story",),
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
            scenario="Nan paused at a marker stone and checked: 'Do I have one coin in my left hand and one in my right?' Yes, the assertion held.",
            need="When the assertion passes—the two coins match—what happens next? Does the journey continue?",
            mapping="An assertion is a checkpoint on the walk. If the assertion holds true, the form passes through and continues. If false, it fails and stops—a safety catch.",
            resolution="The form passed the assertion and returned the result, proving the check succeeded and the walk could continue safely.",
            tags=("story",),
        ),
        SubjectExample(
            form="(try (assert (= 1 2)) (catch Throwable e 0))",
            expected=0,
            concept_phrase="the result when an assertion fails and is caught",
            question_what="what the catch handler returns when the assertion fails",
            goal_text="assert that 1 equals 2, catch the failure, and return a numeric code",
            scenario="Bess stopped and checked: 'Do I have one coin on my left and two coins on my right, and they are equal?' No—they were clearly different.",
            need="The assertion was false. Would the error be caught, or would the walk fail?",
            mapping="A false assertion is an impossible claim on the walk. The error is thrown immediately. The outer try-catch catches this failure and returns a recovery code.",
            resolution="The form caught the failed assertion and returned 0, proving that false checks can be caught and handled safely.",
            tags=("story",),
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
            scenario="Margery wrote a note on a slip of paper: the number 42, the count of pails delivered that day.",
            need="When she wrote the note—printed it—what words appeared on the paper?",
            mapping="Printing is writing onto a market order slip. The form prn writes the value to a stream. With-out-str captures what was written, like folding the slip closed before it's mailed.",
            resolution="The form captured the printed output as a string: '42\\n'—the number, followed by a newline, exactly as it was written.",
            tags=("story",),
        ),
        SubjectExample(
            form="(with-out-str (prn :hare))",
            expected=":hare\n",
            concept_phrase="the output captured from printing a keyword",
            question_what="what string is produced when printing a keyword",
            goal_text="print the keyword :hare and capture the output string",
            scenario="Clara marked her slip with a name: :hare, the symbol of the fastest racer in the fable.",
            need="When she printed this keyword symbol, what exactly was written?",
            mapping="A keyword is a special notation on the slip. Printing it writes the keyword notation itself—the colon-name pair, just as it appears in the form.",
            resolution="The form captured ':hare\\n'—the keyword written as it appears, followed by the line break.",
            tags=("story",),
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
            scenario="Nan tapped a wooden slip against the market board, marking it with a keyword: :hello, a greeting to the morning.",
            need="When she sent the keyword into the pool, did the tap succeed? What did the form return?",
            mapping="Tapping a value into the tap pool is sending a message on a slip to an invisible reader. The form always returns true—the tap succeeds, the slip is sent.",
            resolution="The form returned the verdict, proving the keyword was successfully tapped into the pool.",
            tags=("story",),
        ),
        SubjectExample(
            form="(tap> 42)",
            expected=True,
            concept_phrase="the result of tapping a number into the tap pool",
            question_what="what tap> returns when sending a number",
            goal_text="send a number into the tap pool",
            scenario="Lila marked her slip with a number: 42, the count of pails she had delivered.",
            need="Would sending a number into the tap pool also return success?",
            mapping="The tap pool accepts any value—keyword, number, map, anything. Sending it always succeeds. Tap> returns true for every slip sent.",
            resolution="The form returned the verdict—the number 42 was tapped successfully, just as the keyword was.",
            tags=("story",),
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
            scenario="Clara found an old scroll marking the symbol 'plus' with notes written in the margins: 'adds two'.",
            need="She wanted to read the attached documentation note. What words were written in those margins?",
            mapping="A symbol's metadata is like notes written on a market slip. The :doc key holds a documentation string. Reading the metadata is unfolding the slip to see what was written there.",
            resolution="The form extracted the documentation string 'adds two' from the symbol's metadata, proving the notes were there all along.",
            tags=("story",),
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
            scenario="Bess stumbled and her pail tumbled, and she had pinned a message to her apron—the cry of a careless step.",
            need="When she caught herself, she needed to read the error message. What were the exact words?",
            mapping="An exception carries a message like a slip of paper tucked into the caught pail. Reading the message is unfolding that slip to see what the error said.",
            resolution='The form caught the exception and extracted the error message, proving errors carry human-readable notes about what went wrong (with `oops` as the input value).',
            tags=("story",),
        ),
        SubjectExample(
            form="(try (throw (ex-info \"trouble\" {})) (catch Exception e (.getMessage e)))",
            expected="trouble",
            concept_phrase="the message extracted from a caught ex-info",
            question_what="what message is inside the caught ex-info",
            goal_text="throw an ex-info with a message and extract the message from the caught exception",
            scenario="Margery's walk was interrupted by a problem, and she had labeled it with an error description.",
            need="She caught the error. Could she read the message that came with the ex-info?",
            mapping="An ex-info is a richer error—it carries both a message and data. Reading the message is still the same: unroll the slip and read what was written.",
            resolution="The form extracted the description from the ex-info's message, showing that both simple exceptions and rich ex-infos carry readable error messages (with `trouble` as the input value).",
            tags=("story",),
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
            scenario="Nan unfolded a market order slip that carried two lines: 'hare' on the first, 'tortoise' on the second, each line marked with a newline symbol.",
            need="How many characters were written on this slip—every mark, every line break, counted?",
            mapping="A multi-line string is a market slip with several lines of text. Counting the characters means tallying every letter and every newline mark, no exceptions.",
            resolution="The form counted all characters: 'hare' (4 chars) + newline (1) + 'tortoise' (8 chars) + newline (1) = 14 total (with `hare\ntortoise\n` as the input value).",
            tags=("story",),
        ),
        SubjectExample(
            form="(clojure.string/split \"a\\nb\\nc\" #\"\\n\")",
            expected=["a", "b", "c"],
            concept_phrase="the vector of lines from splitting a string",
            question_what="what lines result from splitting a string on newlines",
            goal_text="split a multi-line string on newlines",
            scenario="Clara held a long slip with letters stacked: a, then b, then c, each separated by newline marks.",
            need="If she split the slip at each newline, how many individual lines would result?",
            mapping="Splitting on newlines is tearing the market slip at each line break, creating separate pieces. Each piece becomes one line in the result vector.",
            resolution='The form split the slip at each newline and returned three separate lines: ["a" "b" "c"], each a distinct piece of the original slip (with `a\\nb\\nc` as the input value).',
            tags=("story",),
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
            scenario="Bess read a three-line order slip from the market: line one with 'a', line two with 'b', line three with 'c'.",
            need="How many lines of orders had the buyer written?",
            mapping="Splitting a slip into lines and counting them tells you how many separate instructions the slip contains. Each line is one order entry.",
            resolution='The form split the slip into three lines and counted them—three lines, three orders, no more and no less (with `a\\nb\\nc` as the input value).',
            tags=("story",),
        ),
        SubjectExample(
            form="(first (clojure.string/split-lines \"morning-delivery\\nevening-delivery\"))",
            expected="morning-delivery",
            concept_phrase="the initial line from splitting a multi-line string",
            question_what="what the opening line is",
            goal_text="get the opening line from splitting a multi-line string",
            scenario="Margery unfolded a two-line slip and read the opening line—the main order, listed at the top.",
            need="What was written on the opening line of this slip?",
            mapping="The opening line of a market slip is the primary instruction. Getting it is like looking at the top of the slip before reading further.",
            resolution="The form returned the text from the opening line—the primary order from the buyer's slip (with `morning-delivery\\nevening-delivery` as the input value).",
            tags=("story",),
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
            scenario="Margery opened her market notebook and wrote the word 'hare'—a single line, then closed it.",
            need="When she copied that line onto paper and closed the notebook, what did the writing preserve?",
            mapping="With-open is like closing a notebook after writing—the resource is sealed and the words are captured, safe until she reads them again. The output stream is the page itself.",
            resolution="The form captured the output 'hare\\n'—the word and the line break, sealed in the notebook's scope.",
            tags=("story",),
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
            scenario="Nan marked a slip with a single letter: 'x'—the signature mark on a market order.",
            need="When she redirected her marking stream to a captured notebook, what letter appeared on the page?",
            mapping="Redirecting the output stream *out* is like pointing her pen toward a paper she will keep, not just the open air. The letter flows to the page instead of vanishing.",
            resolution="The form captured 'x'—the single character written to the redirected stream, preserved on the slip.",
            tags=("story",),
        ),
        SubjectExample(
            form="(with-out-str (println))",
            expected="\n",
            concept_phrase="the output captured from a bare print-line call",
            question_what="what is captured when a bare println is redirected",
            goal_text="redirect the output stream and capture what a bare println produces",
            scenario="Lila held her pen above a slip, ready to print a line. She pressed down but wrote nothing—only the line break itself.",
            need="When she redirected that bare newline to the captured stream, what appeared?",
            mapping="A bare println writes a line break to the stream—the pen moves down to start a new line, but no words are written, only the space between lines.",
            resolution="The form captured '\\n'—the line break alone, the invisible mark that separates one line from the next.",
            tags=("story",),
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
            scenario="Clara unfolded a market slip bearing a single number: 42—the count of pails written in plain notation.",
            need="When she read the slip—parsed the edn notation—what number did she recover?",
            mapping="A market slip with a number is text waiting to be read. Parsing it is translating the written marks back into a Clojure integer, the same way a reader decodes written words.",
            resolution="The form parsed the string and returned the integer 42, proving that written numbers on a slip can be read back into data.",
            tags=("story",),
        ),
        SubjectExample(
            form="(clojure.edn/read-string \"{:a 1}\")",
            expected={":a": 1},
            concept_phrase="the map parsed from an edn string",
            question_what="what map is read from the string",
            goal_text="parse an edn map from a string",
            scenario="Bess held a market slip with a key-value pair written: :a maps to 1—a trade record in compact notation.",
            need="When she read this slip back into Clojure data, what map would it become?",
            mapping="A slip with a key-value notation is a map waiting to be parsed. Reading it recovers the map as a Clojure data structure, ready to be queried and used.",
            resolution="The form parsed the string and recovered the map {:a 1}, with the key and value intact and queryable.",
            tags=("story",),
        ),
        SubjectExample(
            form="(clojure.edn/read-string \"[:hare :tortoise]\")",
            expected=[":hare", ":tortoise"],
            concept_phrase="the vector parsed from an edn string",
            question_what="what vector is read from the string",
            goal_text="parse an edn vector of keywords from a string",
            scenario="Margery wrote a slip listing two racers: [:hare :tortoise]—the fable characters in vector notation.",
            need="When she parsed this slip from text back into Clojure data, what vector would emerge?",
            mapping="A slip with a vector of keywords is a list waiting to be understood. Parsing it turns the written notation into a living vector, ready to be counted and traversed.",
            resolution="The form parsed the string and returned the vector [:hare :tortoise], with both keywords preserved and accessible.",
            tags=("story",),
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
            scenario="Nan wrote a market record to a slip: a map {:a 1 :b 2}—two fields recorded in her ledger.",
            need="She sealed the slip in an envelope and carried it to the market. When she opened it and read it back, what map would she recover?",
            mapping="A roundtrip is writing data to a slip and reading it back. The slip preserves the structure perfectly—what goes out as a map comes back as a map, unchanged and whole.",
            resolution="The form wrote the map to a string, then read it back, recovering the complete map {:a 1 :b 2} with both keys and values intact.",
            tags=("story",),
        ),
        SubjectExample(
            form="(clojure.edn/read-string (pr-str [1 2 3]))",
            expected=[1, 2, 3],
            concept_phrase="the vector after writing and reading back via edn",
            question_what="what vector is recovered from the roundtrip",
            goal_text="serialize a vector to a string with pr-str and read it back into data with clojure.edn/read-string",
            scenario="Lila recorded three orders on a slip: [1 2 3]—three pails to deliver, in vector notation.",
            need="She mailed the slip to the market. When it arrived and was read back into data, what vector would it be?",
            mapping="Writing and reading a vector is sending a message that preserves its order and count perfectly. What leaves as a vector returns as a vector, the same sequence intact.",
            resolution="The form serialized the vector to text and read it back, recovering [1 2 3]—the several items in their original order, unchanged.",
            tags=("story",),
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
            scenario="Godfrey borrowed a neighbor's milking stool—a proven tool with a label marking what it does: 'ls', the list-maker.",
            need="From the tool's description map, could he read what command the stool represents?",
            mapping="A shell-call descriptor is a tool borrowed from the neighbor, marked with what it does. The :cmd key holds the tool's name, just as a borrowed implement is labeled with its purpose.",
            resolution="The form extracted the command string 'ls' from the descriptor, proving the tool was properly labeled and readable.",
            tags=("story",),
        ),
        SubjectExample(
            form="(count (:args {:cmd \"echo\" :args [\"hello\" \"world\"]}))",
            expected=2,
            concept_phrase="the number of arguments in a shell-call descriptor",
            question_what="how many arguments are in the descriptor",
            goal_text="count the number of arguments in a shell-call descriptor map",
            scenario="Aldric examined a neighbor's milking tool with instructions: 'echo' with two arguments: ['hello' 'world']—the stool came with a method.",
            need="He wanted to count how many arguments the tool expected. What was the count?",
            mapping="A borrowed tool carries instructions—a :cmd name and :args list. Counting the arguments tells you how many steps the tool will perform, just as counting the stool's legs tells you if it's stable.",
            resolution="The form extracted the args list and counted it—2 arguments, proving the tool came with two clear instructions.",
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
