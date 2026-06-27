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
from mmllm.aesop.curriculum.boy_wolf._goals import GOALS, get_goal


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
{shepherd}, {emo_proud}, said no error would ever come. The elder
let the runtime decide, then read {concept_phrase} from whatever it
returned."""),

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
wrote it {form_display} so the runtime could carry the work the
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
        goal_text=goal if goal is not None else get_goal(form, concept, what),
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
            "the keyword :thrown returned after the throw is caught",
            scenario=(
                "Tom stood at the practice-pen, nervous about what would "
                "happen if his form went wrong. Carol handed him chalk and "
                "pointed at the pen's walls: they'd caught mistakes before."
            ),
            need=(
                "The practice-pen was meant to let shepherds learn from "
                "errors without spilling them into the flock. Tom needed to "
                "know his careless throw would be caught, not cause panic."
            ),
            mapping=(
                "`throw` raises an exception; `try` surrounds it; `catch` "
                "receives it and returns a value. The catch returns a keyword "
                "instead of letting the error escape to crash the form. The "
                "practice-pen catches what was thrown."
            ),
            resolution=(
                'the form caught the error and returned the keyword, keeping the work inside the pen where mistakes stay lessons, not disasters.'
            )),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-02 — try/catch
G7_02 = SubjectCurriculum(grade=7, subject_id="G7-02",
    subject_title="try / catch", fable="boy-wolf",
    examples=[
        _ex("(try (/ 1 0) (catch Exception e :caught))", ":caught",
            "a division by zero wrapped in try/catch",
            "the keyword :caught returned by the catch branch",
            scenario=(
                "Tom was counting sheep at dusk when a strange question came "
                "to him: what was one sheep divided by zero sheep? Carol heard "
                "the question and smiled. She wrote out the form."
            ),
            need=(
                "The flock couldn't be divided by nothing — it would break the "
                "counting. Carol needed a form that caught the impossible "
                "calculation and returned a safe answer instead."
            ),
            mapping=(
                "`try` surrounds the dangerous division; `catch` waits for the "
                "error (division by zero always fails); when caught, the catch "
                "clause returns :caught instead of crashing. The pen holds it."
            ),
            resolution=(
                "the form caught the error and returned :caught, keeping the counting safe without stopping the day's watch. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record."
            )),
        _ex("(try 42 (catch Exception e :caught))", 42,
            "a try with no error — the body's value is returned",
            "the value 42 from the no-error branch",
            scenario=(
                "Carol asked Tom to write a form that tried a simple value "
                "inside the catch pen, just to prove what happens when nothing "
                "goes wrong. He chalked 42 on the slate."
            ),
            need=(
                "The practice-pen must show both paths: when the form works "
                "cleanly, and when it stumbles. Tom had to see the no-error "
                "case live."
            ),
            mapping=(
                "When `try` evaluates its body with no error, it returns the "
                "body's value directly. The `catch` clause is there, waiting, "
                "but unused. A clean form returns its own value, untouched by "
                "the pen's safety."
            ),
            resolution=(
                'the call returned 42 exactly, the catch unused because the arithmetic had posed no trouble — proving the pen only catches when needed. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'           )),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-03 — try/finally
G7_03 = SubjectCurriculum(grade=7, subject_id="G7-03",
    subject_title="try / finally", fable="boy-wolf",
    examples=[
        _ex("(try 7 (finally :cleanup))", 7,
            "a try whose finally clause runs but doesn't change the value",
            "the value 7 from the body",
            scenario=(
                "After the day's count, Carol would chalk a tally on the slate, "
                "then always wipe chalk dust from the slate's edge. The dust "
                "wiping never changed the count, but it kept the pen clean."
            ),
            need=(
                "Every routine needs cleanup — whether the form works or fails, "
                "the slate must be cleared. Carol needed the count returned, "
                "with cleanup guaranteed after."
            ),
            mapping=(
                "`try` returns the body's value (7). `finally` runs after, "
                "always, whether error or no. The cleanup code (:cleanup) "
                "runs but doesn't change what `try` hands back. Cleanup happens "
                "outside the value's path."
            ),
            resolution=(
                "the call returned 7, and the finally clause ran after — the cleanup kept the pen prepared for the next morning's watch."
            )),
        _ex("(try (try (/ 1 0) (finally :ran)) (catch Exception e :caught))",
            ":caught",
            "a finally that runs before the outer catch fires",
            "the keyword :caught (the outer catch handles the divide-by-zero)",
            scenario=(
                "Tom wrote a nested form where an inner pen had cleanup work, "
                "but the outer pen caught errors. Carol nodded: this was real "
                "practice-pen discipline — nested safety layers."
            ),
            need=(
                "The inner finally must run even when the outer catch catches, "
                "proving cleanup discipline works all the way through nesting. "
                "Tom needed to see the order of operations."
            ),
            mapping=(
                "The inner `try` fails (divide-by-zero), so its `finally` runs "
                "first (:ran executes), then the error bubbles to the outer "
                "`catch`, which catches it and returns :caught. Finally always "
                "runs first, cleanup before the catch answer."
            ),
            resolution=(
                "the call returned :caught, but the inner finally had already run, proving the pen's nested layers work as designed — cleanup first, then the outer catch."
            )),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-04 — ex-info
G7_04 = SubjectCurriculum(grade=7, subject_id="G7-04",
    subject_title="ex-info", fable="boy-wolf",
    examples=[
        _ex("(try (throw (ex-info \"bad\" {:a 1})) (catch Exception e (ex-data e)))",
            {":a": 1},
            "throwing an ex-info with attached data, then reading it back",
            "the data map {:a 1} pulled from the caught ex-info",
            scenario=(
                "Tom's careless throw caused an error, and Carol caught it. But "
                "the error carried a tag-pouch with a written description of "
                "what had gone wrong. Carol opened the pouch and read the note."
            ),
            need=(
                "A bare error message isn't enough — shepherds need details. "
                "Carol needed to know not just that Tom failed, but *what* went "
                "wrong and why, written in the error itself."
            ),
            mapping=(
                "`ex-info` creates an exception that carries a message and a "
                "data-map. When caught, `ex-data` opens the pouch and reads the "
                "attached data. The map {:a 1} was the shepherd's note inside."
            ),
            resolution=(
                "the catch opened the error's data pouch and handed back the map, giving Carol all the detail she needed to understand Tom's mistake."
            )),
        _ex("(try (throw (ex-info \"x\" {:k :v})) (catch Exception e (:k (ex-data e))))",
            ":v",
            "extracting a single key from the caught ex-info's data",
            "the value :v at key :k in the ex-data",
            scenario=(
                "The error pouch held a tally-map with multiple notes. Carol "
                "didn't need the whole pouch — she reached in, found the key "
                "labeled :k, and pulled out the value :v."
            ),
            need=(
                "When an error carries many details, a careful shepherder picks "
                "out just the piece that matters. Carol needed the specific value, "
                "not the whole error's baggage."
            ),
            mapping=(
                "`catch` receives the error. `ex-data` opens the pouch to get the "
                "map. Then indexing into the map with :k extracts just the value "
                ":v. Each layer peels back one piece."
            ),
            resolution=(
                "the call returned :v exactly — Carol had navigated the error's data layers and found the piece she needed."
            )),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-05 — nil punning
G7_05 = SubjectCurriculum(grade=7, subject_id="G7-05",
    subject_title="nil punning", fable="boy-wolf",
    examples=[
        _ex("(some? nil)", False,
            "the predicate (some? nil)",
            "whether nil counts as some?",
            scenario=(
                "Tom asked Carol: is the absence of a sheep — nothing at all — "
                "the same as having *some* sheep? Carol chalked out the predicate."
            ),
            need=(
                "The village's accounting had to be clear: nothing is not "
                "something. Nil needed to be distinct from any actual value."
            ),
            mapping=(
                "`some?` tests whether a value counts as present. Nil is "
                "absence itself — not a value, not something. The predicate "
                "returns false for nil because nil is not *some*."
            ),
            resolution=(
                'the predicate returned false — nil confirmed as absence, not as something the accountant could count.'
            )),
        _ex("(some? 0)", True,
            "the predicate (some? 0)",
            "whether 0 counts as some?",
            scenario=(
                "But Carol asked Tom the reverse: is a count of *zero* sheep "
                "something, or is it like having nothing? He needed the form."
            ),
            need=(
                "The distinction between zero (a count) and nil (no count) must "
                "be clear in the practice-pen. Zero is a real value; nil is not."
            ),
            mapping=(
                "Even though zero means empty, it's still a value — a number "
                "representing absence, not absence itself. `some?` returns true "
                "for 0 because it's a real value, even if zero sheep is an empty "
                "pen."
            ),
            resolution=(
                'the predicate returned true — zero was something countable, even if the count was empty. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'           )),
        _ex("(first nil)", None,
            "calling first on nil",
            "the value of (first nil)",
            scenario=(
                "Carol asked Tom: what is the first sheep from an empty pen? She "
                "chalked the form `(first nil)` on the slate."
            ),
            need=(
                "The code must handle empty things gracefully. Tom needed to see "
                "what the runtime returned for the first element of nothing."
            ),
            mapping=(
                "`first` on nil — the absence of a collection — returns nil. There "
                "is no first element of nothing, so the runtime returns nothing."
            ),
            resolution=(
                'the call returned nil — the first element of an empty pen was absence itself.'
            )),
        _ex("(count nil)", 0,
            "counting a nil collection",
            "the count of nil",
            scenario=(
                "Carol asked Tom to count the sheep in an empty pen. Tom was "
                "confused — how could you count nothing? Carol wrote it."
            ),
            need=(
                "Counting must always work, even when there's nothing to count. "
                "Tom needed to see what the count of nothing was."
            ),
            mapping=(
                "`count` on nil returns 0. Even though nil is absence, `count` "
                "treats it as an empty collection with a count of zero."
            ),
            resolution=(
                "the call returned 0 — counting nothing gave zero, a real value the village's ledger could record."
            )),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-06 — pre/post conditions (we exercise via the {:pre [...]} on
# a defn, applied successfully).
G7_06 = SubjectCurriculum(grade=7, subject_id="G7-06",
    subject_title="pre and post conditions", fable="boy-wolf",
    examples=[
        _ex("((fn [x] {:pre [(pos? x)]} (* x 2)) 5)", 10,
            "a fn with a :pre condition that is satisfied",
            "the value returned when the precondition holds and 5 is doubled",
            scenario=(
                "Carol wrote a drill-card on the watchhouse wall: \"Only "
                "positive counts go into this routine.\" Tom brought 5 sheep, "
                "and the drill ran perfectly."
            ),
            need=(
                "Safety comes from checking the input before work begins. The "
                "drill-card had a guard: it wouldn't run if fed a bad count."
            ),
            mapping=(
                "`:pre` is the guard at the drill's mouth. It checks `:pos?` "
                "on the input. If the check holds, the routine runs (doubling "
                "5 to 10). If it fails, the pen catches the guard's rejection."
            ),
            resolution=(
                'the call returned 10 — the guard had approved 5 as positive, and the drill ran its full course.'
            )),
        _ex("(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exception e :pre-failed))",
            ":pre-failed",
            "a :pre condition that fails, caught by surrounding try",
            "the keyword :pre-failed when the pre-check rejects -1",
            scenario=(
                "Tom tried to pass -1 sheep to Carol's drill-card. The guard "
                "at the mouth rejected him. Carol had written the drill to "
                "catch the rejection in the practice-pen."
            ),
            need=(
                "A bad input must be caught before it ruins the work. Carol's "
                "pen had a catch waiting for exactly this kind of guard failure."
            ),
            mapping=(
                "The `:pre` guard checks `:pos?` and rejects -1 (negative). The "
                "rejection bubbles as an exception, caught by the outer `try`. "
                "The catch returns :pre-failed, stopping the bad input cold."
            ),
            resolution=(
                "the form caught the guard's rejection and returned :pre-failed — the pen had protected the drill from bad shepherding."
            )),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-07 — assert
G7_07 = SubjectCurriculum(grade=7, subject_id="G7-07",
    subject_title="assert", fable="boy-wolf",
    examples=[
        _ex("(do (assert (= 1 1)) :ok)", ":ok",
            "an assert that passes, followed by a return value",
            "the keyword :ok returned after the assert succeeds",
            scenario=(
                "Carol wrote an assertion on the watchhouse slate: \"1 equals 1.\" "
                "The assertion held. She wrote :ok and handed it to Tom as proof."
            ),
            need=(
                "The practice-pen must certify that a claim is true before work "
                "continues. Carol needed the assertion to pass silently, then "
                "return the next value."
            ),
            mapping=(
                "`assert` tests a condition. If true, it does nothing and returns. "
                "Then the next form (`:ok`) runs. The assertion was a gate that "
                "let the value through cleanly when the check held."
            ),
            resolution=(
                'the call returned :ok — the assertion had passed and the next form had run without interruption.'
            )),
        _ex("(try (assert (= 1 2)) (catch Throwable e :asserted))",
            ":asserted",
            "an assert that fails, caught by surrounding try",
            "the keyword :asserted when the assertion rejects (= 1 2)",
            scenario=(
                "Carol wrote a false assertion: \"1 equals 2.\" Tom knew it would "
                "fail. The practice-pen's catch waited to catch the explosion."
            ),
            need=(
                "When an assertion fails, it must be caught cleanly by the pen, "
                "not crash the whole watch. Tom needed to see the failure held."
            ),
            mapping=(
                "`assert` on a false condition throws an exception. The pen's "
                "`catch` receives it and returns :asserted. The assertion became "
                "a gate that rejected the bad path and fed an error to safety."
            ),
            resolution=(
                "the form caught the assertion's failure and returned :asserted — the practice-pen had held the broken claim without spilling. Tom chalked {drawn.a} on the watchhouse notice, and the morning record stood for the next shepherd to read."           )),
    ], subplots=_SAFETYNET_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-08 — prn / pprint (these side-effect to *out*; we use with-out-str
# to capture and inspect).
G7_08 = SubjectCurriculum(grade=7, subject_id="G7-08",
    subject_title="prn and pprint", fable="boy-wolf",
    examples=[
        _ex("(with-out-str (prn 42))", "42\n",
            "capturing the output of (prn 42)",
            "the string \"42\\n\" produced by prn",
            scenario=(
                "Carol opened the watchhouse log-book and dipped her quill in ink. "
                "She chalked the form to capture what `prn` would write. Tom "
                "watched as she opened a scroll and caught the words."
            ),
            need=(
                "The log-book must record what the runtime prints. Carol needed "
                "to capture the printed line so it would stay on the scroll."
            ),
            mapping=(
                "`prn` writes to the scroll (output). `with-out-str` captures "
                "what was written as a string. The form `prn 42` writes \"42\\n\"; "
                "the capture catches it in the log-book as text."
            ),
            resolution=(
                'the call returned the string "42\\n" — the log-book had recorded what `prn` would have printed to the townsfolk square.'
            )),
        _ex("(with-out-str (prn :wolf))", ":wolf\n",
            "capturing prn applied to the keyword :wolf",
            "the string \":wolf\\n\" produced by prn",
            scenario=(
                "Carol wrote another line in the log-book, this time capturing "
                "what `prn` would write about the keyword :wolf. The pen caught "
                "the words as they left the quill."
            ),
            need=(
                "Each name in the village has its own log-line. Carol needed to "
                "see the exact line the runtime would print for the keyword."
            ),
            mapping=(
                "`prn` prints the keyword `:wolf` to the scroll as \":wolf\\n\". "
                "`with-out-str` captures that exact text. Keywords are printed "
                "with the colon and a newline."
            ),
            resolution=(
                'the call returned ":wolf\\n" — the log-book held the keyword as `prn` would have printed it, ready to send downhill.'
            )),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-09 — tap> (returns true; we exercise that effect).
G7_09 = SubjectCurriculum(grade=7, subject_id="G7-09",
    subject_title="tap>", fable="boy-wolf",
    examples=[
        _ex("(tap> :hello)", True,
            "tapping a value into the tap pool",
            "the boolean true returned by tap>",
            scenario=(
                "Carol kept a small pool at the watchhouse edge where she'd "
                "toss in values for Tom to inspect. She threw :hello into the "
                "pool and watched it surface."
            ),
            need=(
                "Inspection pools let shepherds peek at values without stopping "
                "the work. Carol needed the form to return true, proving the "
                "value had been tapped."
            ),
            mapping=(
                "`tap>` tosses the value into an inspection pool and returns "
                "true. The value `:hello` lands in the pool; the form confirms "
                "the toss worked by returning true."
            ),
            resolution=(
                'the call returned true — the keyword had been tapped into the pool and Carol could fish it out later for inspection.'
            )),
        _ex("(tap> 42)", True,
            "tapping the number 42 into the tap pool",
            "the boolean true",
            scenario=(
                "Tom tossed a number into Carol's pool: 42. The form confirmed "
                "the toss worked by returning true. Numbers, keywords, anything "
                "could go in the pool."
            ),
            need=(
                "The pool must accept any value and always return true to show "
                "the tap worked. Tom needed to see that the number had been "
                "caught."
            ),
            mapping=(
                "Whether the value is a keyword or a number, `tap>` always "
                "returns true. The value lands in the pool, it confirms. "
                "Numbers and keywords both tap the same way."
            ),
            resolution=(
                'the call returned true — the number had been tapped into the pool, ready for later inspection.'
            )),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-10 — doc / source (REPL helpers; we exercise via a metadata
# lookup since `doc` itself prints).
G7_10 = SubjectCurriculum(grade=7, subject_id="G7-10",
    subject_title="doc and source", fable="boy-wolf",
    examples=[
        _ex("(:doc (meta '^{:doc \"adds two\"} plus))", "adds two",
            "the :doc metadata on a symbol",
            "the string \"adds two\" from the metadata",
            scenario=(
                "Carol carved a drill-card on the watchhouse wall. Above the "
                "recipe's steps, she chalked a small note: \"adds two\". Tom "
                "asked what the note was for. Carol opened the metadata."
            ),
            need=(
                "Every drill-card needs a note explaining what it does. The log-book "
                "must record that note so shepherds know the routine's purpose."
            ),
            mapping=(
                "Metadata `:doc` holds the card's written note. `meta` opens the "
                "card to read what was chalked above. The form pulls the `:doc` "
                "string from the card's metadata."
            ),
            resolution=(
                'the call returned "adds two" — the note Carol had chalked was now written in the log-book for all shepherds to read.'
            )),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-11 — Reading stack traces (we exercise via inspecting the message
# of a caught exception).
G7_11 = SubjectCurriculum(grade=7, subject_id="G7-11",
    subject_title="Reading stack traces", fable="boy-wolf",
    examples=[
        _ex("(try (throw (Exception. \"oops\")) (catch Exception e (.getMessage e)))",
            "oops",
            "extracting the message from a caught exception",
            "the string \"oops\" from the caught Exception",
            scenario=(
                "Tom's careless throw raised an error. Carol caught it and read the message."
            ),
            need=(
                "Shepherds need the error's message to understand what went wrong."
            ),
            mapping=(
                "`throw` sends an exception with a message. `catch` receives it. `.getMessage` reads the tag."
            ),
            resolution=(
                "The form returned the error's message and Carol understood the mistake."
            )),
        _ex("(try (throw (ex-info \"trouble\" {})) (catch Exception e (.getMessage e)))",
            "trouble",
            "the message of a caught ex-info",
            "the string \"trouble\"",
            scenario=(
                "Carol threw an error and Tom caught it, reading its message."
            ),
            need=(
                "Tom needed to know that `.getMessage` works the same way on any exception."
            ),
            mapping=(
                "`ex-info` is a fancier error that carries data and a message. `.getMessage` reads it the same way."
            ),
            resolution=(
                "The form returned the ex-info's message and Tom understood the error."
            )),
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
            "the count of characters in \"wolf\\nshepherd\\n\"",
            scenario=(
                "Carol kept the meadow folk log-book. She'd read the scroll aloud: "
                "\"wolf, newline, shepherd, newline.\" Tom counted the marks "
                "and got 14."
            ),
            need=(
                "The scroll must be countable — each letter, each newline is a "
                "mark. Tom needed to see how long the log would be."
            ),
            mapping=(
                "`count` reads the string character by character. \"wolf\" is 4, "
                "newline is 1, \"shepherd\" is 8, newline is 1. Together: 4+1+8+1=14."
            ),
            resolution=(
                'the call returned 14 — the log-book was exactly that long, counted from scroll to scroll. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'           )),
        _ex("(clojure.string/split \"a\\nb\\nc\" #\"\\n\")", ["a", "b", "c"],
            "splitting a slurped-style string on newlines",
            "the vector [\"a\" \"b\" \"c\"] of three lines",
            scenario=(
                "Carol had a scroll with three lines written on it. She asked Tom "
                "to separate the lines at each newline break. Tom split the scroll "
                "into pieces."
            ),
            need=(
                "The log-book is written in lines, but processing requires each "
                "line separate. Tom had to split what Carol had written."
            ),
            mapping=(
                "`split` cuts the string at each newline marker. \"a\\nb\\nc\" "
                "becomes [\"a\", \"b\", \"c\"] — three separate lines in a vector."
            ),
            resolution=(
                'the call returned ["a", "b", "c"] — the scroll had been split into its three lines, ready for the townsfolk\'s processing.'
            )),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-13 — line-seq (we exercise via the in-memory equivalent: a vector
# of lines).
G7_13 = SubjectCurriculum(grade=7, subject_id="G7-13",
    subject_title="line-seq", fable="boy-wolf",
    examples=[
        _ex("(count (clojure.string/split-lines \"a\\nb\\nc\"))", 3,
            "the number of lines in a small text",
            "the count of lines in \"a\\nb\\nc\"",
            scenario=(
                "The village log-book had been split into lines. Carol asked Tom "
                "to count how many lines the scroll held."
            ),
            need=(
                "Before processing the log, the valley needs to know its size. "
                "Tom had to count the lines."
            ),
            mapping=(
                "`split-lines` breaks the text at newlines. \"a\\nb\\nc\" becomes "
                "[\"a\", \"b\", \"c\"]. `count` gives 3. Each line is a separate "
                "entry."
            ),
            resolution=(
                "the call returned 3 — the log held exactly three lines, ready for the morning's processing."
            )),
        _ex("(first (clojure.string/split-lines \"alpha\\nbeta\"))",
            "alpha",
            "the initial line from splitting a multi-line string",
            "what the initial line is",
            goal="get the initial line from splitting a multi-line string",
            scenario=(
                "Carol handed Tom the morning's log-book split into lines. He "
                "asked: what comes first? She split it and pointed to the top."
            ),
            need=(
                "The first entry must be read before the rest. Tom needed to "
                "reach for the first line of the split scroll."
            ),
            mapping=(
                "`split-lines` breaks the string into lines. `first` picks the head of the sequence."
            ),
            resolution=(
                'The form returned the first line of the scroll.'
            )),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-14 — with-open (we exercise the macro-shape via with-out-str,
# the closest universally-available analogue).
G7_14 = SubjectCurriculum(grade=7, subject_id="G7-14",
    subject_title="with-open", fable="boy-wolf",
    examples=[
        _ex("(with-out-str (println \"wolf\"))", "wolf\n",
            "a resource-scoped capture of println output",
            "the string \"wolf\\n\" from the scoped block",
            scenario=(
                "Carol kept a small scroll for testing. She'd write a word on it, "
                "then capture what was written. The scroll was only open for that "
                "one use."
            ),
            need=(
                "Resources like scrolls must be opened, used, and closed carefully. "
                "Carol needed the capture to happen in a scoped block."
            ),
            mapping=(
                "`with-out-str` opens a capture scope, runs the work inside "
                "(printing \"wolf\"), captures the output, and closes the scope. "
                "The string \"wolf\\n\" is the captured text."
            ),
            resolution=(
                'the call returned "wolf\\n" — the scope had held the print, captured it, and closed cleanly without spill.'
            )),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-15 — *in* / *out* (we exercise *out* via with-out-str; *in* is
# harder to bind in a single form and we leave it implied).
G7_15 = SubjectCurriculum(grade=7, subject_id="G7-15",
    subject_title="*in* and *out*", fable="boy-wolf",
    examples=[
        _ex("(with-out-str (print \"x\"))", "x",
            "redirecting *out* via with-out-str and printing",
            "the string \"x\" captured from *out*",
            scenario=(
                "Carol opened the village's writing-scroll and asked Tom to print "
                "a single letter. The scroll captured what was written."
            ),
            need=(
                "The scroll is the world's output channel. When something is printed, "
                "it goes to the scroll. Carol needed to capture that output."
            ),
            mapping=(
                "`print` sends text to *out* (the scroll). `with-out-str` redirects "
                "*out* to a capture string. The letter \"x\" was printed, then "
                "captured by the scope."
            ),
            resolution=(
                'the call returned "x" — the print had gone to the scroll, and the scroll had been captured perfectly.'
            )),
        _ex("(with-out-str (println))", "\n",
            "a bare println redirected through *out*",
            "the string \"\\n\"",
            scenario=(
                "Carol asked Tom to write a blank line on the scroll and capture it. "
                "No letters, just the newline. The scope caught it."
            ),
            need=(
                "The scroll's output channel must carry everything, even blank lines. "
                "Tom needed to prove that a bare newline was captured."
            ),
            mapping=(
                "`println` with no args prints just a newline to *out*. "
                "`with-out-str` captures what was printed. The result is \"\\n\" — "
                "a single newline, nothing more."
            ),
            resolution=(
                'the call returned "\\n" — the blank line had been printed and captured, proving the scroll holds what\'s not written too.'
            )),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-16 — edn read
G7_16 = SubjectCurriculum(grade=7, subject_id="G7-16",
    subject_title="edn read", fable="boy-wolf",
    examples=[
        _ex("(clojure.edn/read-string \"42\")", 42,
            "reading an edn integer from a string",
            "the integer 42 read from \"42\"",
            scenario=(
                "The village log-book held the number \"42\" written in chalk. Carol "
                "asked the runtime to read it and turn it back into a real number."
            ),
            need=(
                "Text on a scroll is just marks — the runtime must translate those "
                "marks back into values. Carol needed 42 the number, not \"42\" the "
                "text."
            ),
            mapping=(
                "`edn/read-string` reads the text and parses it. \"42\" as text "
                "becomes 42 as a number — a real value again, ready to calculate."
            ),
            resolution=(
                "the call returned 42 — the log-book's mark had been translated back into a live number."
            )),
        _ex("(clojure.edn/read-string \"{:a 1}\")", {":a": 1},
            "reading an edn map from a string",
            "the map {:a 1} read from \"{:a 1}\"",
            scenario=(
                "The scroll held the form of a map written in chalk. Carol needed "
                "the runtime to read that text-form and turn it into a real map."
            ),
            need=(
                "Complex data on scrolls is just characters. Carol had to translate "
                "the chalk marks back into a usable map."
            ),
            mapping=(
                "`edn/read-string` parses the text \"{:a 1}\" and returns the map "
                "{:a 1}. The characters become a data structure again."
            ),
            resolution=(
                "the call returned {:a 1} — the scroll's notation had been decoded into a live map the watchhouse could use."
            )),
        _ex("(clojure.edn/read-string \"[:wolf :flock]\")",
            [":wolf", ":flock"],
            "reading an edn vector of keywords",
            "the vector [:wolf :flock]",
            scenario=(
                "The log-book held a vector of shepherd names written as text. Carol "
                "read it back to get the actual vector."
            ),
            need=(
                "Names on scrolls are just chalk. The runtime must translate them "
                "back into the live keywords the shepherds could use."
            ),
            mapping=(
                "`edn/read-string` parses \"[:wolf :flock]\" and returns the vector "
                "[:wolf :flock]. Keywords come back as real keywords."
            ),
            resolution=(
                "the call returned [:wolf :flock] — the scroll's roster had been decoded into live keywords."
            )),
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
            "the map {:a 1 :b 2} after the roundtrip",
            scenario=(
                "Carol had a map in the REPL. She wrote it onto the scroll with "
                "`pr-str`, then asked the runtime to read it back. The map came "
                "back exactly as it was."
            ),
            need=(
                "Data must survive the journey: live value to scroll-marks to live "
                "value again. Carol needed proof the roundtrip was clean."
            ),
            mapping=(
                "`pr-str` writes the map to text on the scroll. `edn/read-string` "
                "reads it back. The map {:a 1 :b 2} goes out as characters and "
                "comes back as a live map."
            ),
            resolution=(
                'the call returned {:a 1 :b 2} — the map had survived the journey to the scroll and back, unchanged.'
            )),
        _ex("(clojure.edn/read-string (pr-str [1 2 3]))", [1, 2, 3],
            "round-tripping a vector through pr-str then edn/read-string",
            "the vector [1 2 3]",
            scenario=(
                "The vector [1 2 3] was written to the scroll and read back. Each "
                "step preserved the data cleanly."
            ),
            need=(
                "All data types must survive the roundtrip — maps, vectors, numbers. "
                "Carol needed to see that vectors worked too."
            ),
            mapping=(
                "`pr-str` turns [1 2 3] into text. `edn/read-string` parses it back. "
                "The three numbers return as a vector, unchanged."
            ),
            resolution=(
                'the call returned [1 2 3] — the vector had made the roundtrip cleanly, proving all data can survive the scroll.'
            )),
    ], subplots=_SCROLL_SUBPLOTS, plan_pool=_PLAN_G7)


# G7-18 — Shell command (host-specific; we exercise via a non-shell
# analogue that captures the same conceptual pattern: a command-name
# string and an args vector turning into a result).
G7_18 = SubjectCurriculum(grade=7, subject_id="G7-18",
    subject_title="Shell command", fable="boy-wolf",
    examples=[
        _ex("(:cmd {:cmd \"ls\" :args [\"-l\"]})", "ls",
            "the :cmd portion of a shell-call descriptor map",
            "the string \"ls\"",
            scenario=(
                "Tom visited the foreign toolshed at the meadow folk smithy. He picked "
                "up a tool labeled with a command name. Carol showed him how to "
                "read the tool's label."
            ),
            need=(
                "Foreign tools have their own labels and calling conventions. Tom "
                "had to learn how to extract the command name from the tool's "
                "descriptor."
            ),
            mapping=(
                "The tool descriptor is a map with `:cmd` as the label. The string "
                "\"ls\" is the command name. To use the foreign tool, Tom needed "
                "to read that label first."
            ),
            resolution=(
                'the call returned "ls" — Tom had read the toolshed\'s label and found the command he needed to call. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'           )),
        _ex("(count (:args {:cmd \"echo\" :args [\"hello\" \"world\"]}))",
            2,
            "the number of args in a shell-call descriptor",
            "the count of args",
            scenario=(
                "Carol showed Tom another tool in the smithy. This one carried "
                "arguments in a special pouch labeled `:args`. He counted how many "
                "arguments the tool had."
            ),
            need=(
                "Foreign tools often take arguments. Tom had to know how many "
                "arguments the tool expected."
            ),
            mapping=(
                "The descriptor holds `:args` with a vector [\"hello\" \"world\"]. "
                "`count` on that vector gives 2. The tool has two arguments."
            ),
            resolution=(
                "the call returned 2 — Tom had extracted the argument count from the foreign tool's descriptor. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement."           )),
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
