"""Grade 1 — atoms + first eval, taught through the Boy-who-cried-Wolf fable.

Each subject defines:
  - examples: a list of Clojure exercises (form + expected + concept_phrase)
  - subplots: 6+ narrative templates that wrap any example in fable scenery
  - plan_pool: optional plan-only prefaces (never reveal the answer)

Coverage per subject (per fable):
   examples × narrative variants ≈ 5-15 × 200-2000 distinct records.

The fable's moral dynamic — lying erodes trust — informs every record's
character attitudes. The shepherd is the eager guesser whose claims are
no longer believed; the elder / villager is the patient evaluator who
insists on actually submitting the form to the REPL. Subjects bring
this out differently (e.g., G1-15 equality is settled by the village
slate; G1-13 first-arithmetic is a wager the elder refuses to take
without the REPL).

Other grade modules import `_SHARED_SUBPLOTS` and `_PLAN_POOL` from this
file as their base, then layer on grade-specific extensions where
needed (e.g., a "ledger of bindings" beat for G3, a "trust-as-namespace"
beat for G6).

This module also exports boy-wolf-specific BW_EMO_* pools that the
generator uses in place of `mmllm.aesop.fables.EMO_*` whenever
fable="boy-wolf". The shared fables.EMO pools have hard-coded gender
pronouns ("her legs heavy from sprinting", "her eyes always on the
path", "his heart sinking", "her hands trembling") that produce
ungrammatical text when the bound character is male / gender-neutral
(boy-wolf shepherds Tom and Will are male; Pat is gender-neutral).
The shared pool also carries tortoise-hare race imagery ("as if the
race were already won", "swaggering through the underbrush", "her
legs heavy from sprinting") that doesn't fit the boy-wolf valley
setting where the dramatic action is shouting alarms, not running
races. The BW_EMO_* pools below are gender-neutral and fable-flavored.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.boy_wolf._metaphor_pools import (
    _ACORN_SUBPLOTS, _CHALKMARK_SUBPLOTS, _GATE_SUBPLOTS, _SAFETYNET_SUBPLOTS, _SCRIBE_SUBPLOTS,
)
from mmllm.aesop.curriculum.boy_wolf._goals import GOALS


# ─────────────────────── boy-wolf-specific EMO pools ───────────────────────
#
# Gender-neutral (no possessive "her"/"his"/"their" baked in). Imagery
# fits the boy-wolf valley setting (shouting from the hill, the village
# slate, false alarms, the elder's patience) — no race / sprint /
# underbrush leakage from tortoise-hare.

BW_EMO_PROUD: tuple[str, ...] = (
    "with a smug grin",
    "puffed up with pride",
    "as if the village would always believe",
    "with great whoops of laughter",
    "boasting at every turn",
    "with the swagger of an unrepentant fibber",
    "sounding sure of every word",
    "talking past the elder's warning",
)

BW_EMO_PATIENT: tuple[str, ...] = (
    "without complaint",
    "saying very little",
    "with steady, careful steps",
    "with eyes always on the slate",
    "untroubled by what others thought",
    "stepping deliberately",
    "letting the runtime have the last word",
    "with the calm of a long watch well kept",
)

BW_EMO_TIRED: tuple[str, ...] = (
    "drowsy from the warm sun",
    "weary from the morning's effort",
    "lulled by the gentle wind",
    "weary from the long watch",
    "yawning at the soft moss",
    "tired from a season of misplaced cries",
    "worn from too many false starts",
)

BW_EMO_REGRETFUL: tuple[str, ...] = (
    "with the heart of someone who had cried wolf once too often",
    "wishing for more careful counting",
    "regretting every careless step",
    "wondering how it had come to this",
    "remembering a season of false alarms",
    "carrying the weight of yesterday's wrong claims",
)

BW_EMO_DESPERATE: tuple[str, ...] = (
    "with growing alarm",
    "wide-eyed with fear",
    "in a panic",
    "voice still hoarse from yesterday's false alarm",
    "calling out without confidence anyone would come",
    "with the fear of a watch that no one trusts",
)


# ─────────────────────── shared subplot pool ───────────────────────
#
# Eight templates work across most grade-1 subjects. Each subject either
# uses this pool directly or extends it with subject-specific templates.
#
# Templates use `{form_display}` for the literal form being evaluated,
# `{concept_phrase}` for the noun-phrase ("the value 42"), and
# fable-specific placeholders for character/location/emotion variation.
#
# IMPORTANT (boy-wolf-specific): the SHEPHERD is the cautionary
# character, NOT a corrective voice. So "the shepherd insisted they
# evaluate the form" is wrong for boy-wolf — that line belongs to the
# elder / villager. Boy-wolf templates flip the polarity from
# tortoise-hare: the SHEPHERD claims-without-checking; the VILLAGER /
# ELDER insists on the runtime.

_SHARED_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The false-claim template — shepherd announces an answer they
    #    haven't actually evaluated; the elder insists they submit the
    #    form. Direct echo of the fable's "false alarm" beat translated
    #    to the REPL.
    SubplotTemplate("""\
{shepherd_phrase} called down from a stone {place} where someone had
chalked {concept_phrase} on a flat board. {shepherd}, {emo_proud},
declared {shepherd_he_she} already knew what would come back. {elder},
{emo_patient}, asked {shepherd_him_her} to actually submit the form
{form_display} to the REPL — the village had stopped trusting answers
that weren't checked."""),

    # 2. The trust-ledger template — the village elder keeps a written
    #    tally of which claims were verified vs. just-guessed. Today's
    #    entry is the form. (Boy-wolf-flavored ledger beat — analogous
    #    to tortoise-hare's "wager" without the wager's gambling tone.)
    SubplotTemplate("""\
The elder of the village kept a small slate {place}, with a tally of
forms the shepherds had honestly submitted versus forms they had only
guessed at. The next line was {concept_phrase}. {elder_phrase} read
out the form {form_display} so {shepherd_phrase} could write it
properly into the REPL and earn an honest mark on the slate."""),

    # 2b. Trust-ledger variant — slate kept on a stone at the village edge.
    SubplotTemplate("""\
A small slate sat on a flat stone {place}; on it the reeve recorded
each form a shepherd had submitted to the REPL alongside each claim
made without checking. Today the form was {form_display}, and the page
heading read {concept_phrase}. {elder} nodded at {shepherd_phrase} to
write the form properly so the slate would carry an honest entry."""),

    # 2c. Trust-ledger variant — the elder's pocket notebook.
    SubplotTemplate("""\
{elder_phrase} kept a small leather notebook of every form the shepherds
of the valley had actually evaluated. Today {place} the next entry was
{concept_phrase}. {shepherd_phrase} peered over {elder_his_her} shoulder
at the form {form_display} and was asked, gently, to be the one to
submit it."""),

    # 3. The careful-villager template — a villager (the corrective
    #    voice) gently teaches the shepherd how the REPL works using
    #    this form. Echoes the fable's "boy's mother explains the rule"
    #    beat. Comma after "said" handles participle-style EMO_PATIENT.
    SubplotTemplate("""\
{elder_phrase} had been trying to teach {shepherd_phrase} how the REPL
works. "Look here," {elder_he_she} said, pointing to {concept_phrase}.
"You hand the form {form_display} to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
{shepherd}, {emo_tired}, agreed to try."""),

    # 4. The audience template — small village crowd watches the
    #    shepherd attempt to predict, then the elder insists on a real
    #    submission. NOTE: uses "pointed to" rather than "read aloud"
    #    so abstract concept_phrases ("the equality (= 1 1)") fit.
    SubplotTemplate("""\
A small crowd of villagers had gathered {place} to watch
{shepherd_phrase} attempt to predict, off the cuff, what the REPL would
return. {elder_phrase} pointed to {concept_phrase} and read out the
form aloud: {form_display}. The villagers waited, patient but
unimpressed, to see who would submit the form properly."""),

    # 5. The waiting-for-help template — the fable's signature beat
    #    repurposed: the shepherd's claim hangs in the air; nobody
    #    answers until the form is actually evaluated.
    #
    #    NOTE (boy-wolf polish, hand-audit pass): the original template
    #    had three issues that hand-audit caught: (a) "refusing to
    #    descend" presumes elevation, but {place} ranges over flat
    #    locations (meadow / road / orchard) — replaced with "refusing
    #    to come back to the flock"; (b) "{shepherd} insisted
    #    {shepherd_he_she} already knew the answer" rendered "Pat
    #    insisted they already knew" for n-gender shepherds (pitfall
    #    #19) — replaced with name-only construction; (c) "Submit
    #    {concept_phrase} to the REPL" failed for abstract concept
    #    phrases ("Submit the cond form to the REPL") — replaced with
    #    "Submit the form" plus {form_display}.
    SubplotTemplate("""\
Halfway through the morning watch, {shepherd_phrase} called out
{place}, demanding a verdict on the form {form_display} and refusing
to come back to the flock until somebody confirmed it. {shepherd} was
sure of the answer already. {elder_phrase}, walking up at an unhurried
pace, simply said: "Submit the form. Whatever comes back is the
answer.\""""),

    # 6. The reckoning-at-week's-end template — the reeve walks the
    #    meadow on Saturday and reviews the week's forms. Boy-wolf
    #    "end-of-week reckoning" beat from the fable.
    #
    #    NOTE (boy-wolf polish, hand-audit pass): the original closing
    #    "{shepherd_phrase}, who, {emo_tired}, agreed..." had a
    #    redundant relative-clause `who,` followed by a participial
    #    phrase from EMO_TIRED — `who` opens a relative clause
    #    expecting a finite verb, but the participle isn't one, so the
    #    sentence reads "Tom, who, weary from sprinting, agreed" — a
    #    broken double-comma sequence. Drop the `who,` to leave a clean
    #    appositive participle.
    SubplotTemplate("""\
Each Saturday, the reeve walked up to the meadow and reviewed which
forms the shepherds had actually submitted to the REPL during the week.
This week, the next form on the page was {form_display}, and the line
above it read {concept_phrase}. {elder_phrase} handed the page to
{shepherd_phrase}, {emo_tired}, who agreed to write it out properly."""),

    # 7. The boast-and-rebuke template — shepherd claims the answer
    #    without checking; villager insists on actual evaluation. Uses
    #    {shepherd_him_her} (object case) for "asked X to ..."; comma
    #    after "said" so participle EMO_PROUD entries parse as
    #    adverbial.
    SubplotTemplate("""\
"There is no need to evaluate that," {shepherd_phrase} said, {emo_proud}.
"Anyone can see what {concept_phrase} comes to." {elder_phrase}, who
{place} had heard such claims many times, asked {shepherd_him_her} to
actually write the form {form_display} and submit it to the REPL —
just to be sure."""),

    # 8. The puzzle-on-the-village-board template — a sign / scrap of
    #    parchment in the village square poses the form as a riddle.
    SubplotTemplate("""\
A wooden notice nailed to a post {place} carried a small puzzle. The
riddle simply asked the reader to evaluate {form_display}. {shepherd}
laughed, {emo_proud}, and declared it too easy to bother with.
{elder_phrase} said, patiently, that the only way to be certain of
{concept_phrase} was to put it in the REPL."""),
]


_PLAN_POOL: tuple[str, ...] = (
    "I write the form and let the REPL evaluate it.",
    "I submit the form to the REPL via the eval tool.",
    "I let the REPL do the evaluation.",
    "I express the form as Clojure source.",
    # Concept-specific plans — picked occasionally to break up the
    # generic ones and give the model concept-tied reasoning patterns.
    "I read the form and submit it directly.",
    "I write the literal value as Clojure source.",
    "I let the runtime decide what the form evaluates to.",
)


# ─────────────────────── helpers for examples ───────────────────────


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


# ─────────────────────── 18 grade-1 subjects ───────────────────────


# G1-01 — Eval as substitution
G1_01 = SubjectCurriculum(
    grade=1, subject_id="G1-01",
    subject_title="Eval as substitution",
    fable="boy-wolf",
    examples=[
        _ex("42",                  42,    "the value 42",
            "the value of 42"),
        _ex("0",                   0,     "the value 0",
            "the value of 0"),
        _ex("(+ 1 2)",             3,     "the form (+ 1 2)",
            "the result of (+ 1 2)"),
        _ex("(* 4 5)",             20,    "the form (* 4 5)",
            "the result of (* 4 5)"),
        _ex("(- 10 (+ 2 3))",      5,     "the nested form (- 10 (+ 2 3))",
            "the result of (- 10 (+ 2 3))"),
        _ex("(+ 1 (* 2 3))",       7,     "the form (+ 1 (* 2 3))",
            "the result of (+ 1 (* 2 3))"),
        _ex("\"hello\"",          "hello","the string \"hello\"",
            "the value of \"hello\""),
        _ex("nil",                None,   "the literal nil",
            "the value of nil"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-02 — Numbers (integers)
G1_02 = SubjectCurriculum(
    grade=1, subject_id="G1-02",
    subject_title="Integer numbers",
    fable="boy-wolf",
    examples=[
        _ex("7",     7,    "the integer 7",       "the value of the integer 7"),
        _ex("-3",   -3,    "the integer -3",      "the value of the integer -3"),
        _ex("0",     0,    "the integer 0",       "the value of zero"),
        _ex("100",   100,  "the integer 100",     "the value of one hundred"),
        _ex("-25",  -25,   "the integer -25",     "the value of negative twenty-five"),
        _ex("12345", 12345,"the integer 12345",   "the value of 12345"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-03 — Numbers (ratios)
G1_03 = SubjectCurriculum(
    grade=1, subject_id="G1-03",
    subject_title="Ratios",
    fable="boy-wolf",
    examples=[
        # Ratios like 1/2 evaluate to themselves in Clojure (exact rational).
        # In Python expected we represent them as the form string.
        _ex("1/2",   "1/2", "the ratio 1/2",   "the value of the ratio 1/2"),
        _ex("3/4",   "3/4", "the ratio 3/4",   "the value of three-quarters"),
        _ex("(+ 1/2 1/4)", "3/4",
            "the form (+ 1/2 1/4)",
            "the value of (+ 1/2 1/4)"),
        _ex("(* 2 1/2)", 1,
            "the form (* 2 1/2)",
            "the value of (* 2 1/2)"),
        _ex("(- 1 1/3)", "2/3",
            "the form (- 1 1/3)",
            "the value of (- 1 1/3)"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-04 — Strings
G1_04 = SubjectCurriculum(
    grade=1, subject_id="G1-04",
    subject_title="Strings",
    fable="boy-wolf",
    examples=[
        _ex('"hello"',    "hello",    'the string "hello"',
            'the value of "hello"'),
        _ex('"flock"',    "flock",    'the string "flock"',
            'the value of "flock"'),
        _ex('"watch the meadow"', "watch the meadow",
            'the string "watch the meadow"',
            'the value of "watch the meadow"'),
        _ex('""',         "",         'the empty string',
            'the value of the empty string'),
        _ex('"42"',       "42",       'the string "42"',
            'the value of the string "42"'),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-05 — Booleans
G1_05 = SubjectCurriculum(
    grade=1, subject_id="G1-05",
    subject_title="Booleans",
    fable="boy-wolf",
    examples=[
        _ex("true",  True,  "the literal true",  "the value of true"),
        _ex("false", False, "the literal false", "the value of false"),
        _ex("(= 1 1)", True,
            "the equality (= 1 1)",
            "the value of (= 1 1)"),
        _ex("(= 1 2)", False,
            "the equality (= 1 2)",
            "the value of (= 1 2)"),
        _ex("(< 3 5)", True,
            "the comparison (< 3 5)",
            "the value of (< 3 5)"),
        _ex("(> 3 5)", False,
            "the comparison (> 3 5)",
            "the value of (> 3 5)"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-06 — nil
G1_06 = SubjectCurriculum(
    grade=1, subject_id="G1-06",
    subject_title="nil",
    fable="boy-wolf",
    examples=[
        _ex("nil", None, "the literal nil",
            "the value of nil"),
        _ex("(nil? nil)", True,
            "the predicate (nil? nil)",
            "whether nil is nil"),
        _ex("(nil? 0)", False,
            "the predicate (nil? 0)",
            "whether 0 is nil"),
        _ex("(nil? false)", False,
            "the predicate (nil? false)",
            "whether false is nil"),
        _ex("(= nil nil)", True,
            "the equality (= nil nil)",
            "the value of (= nil nil)"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-07 — Keywords (boy-wolf themed)
G1_07 = SubjectCurriculum(
    grade=1, subject_id="G1-07",
    subject_title="Keywords",
    fable="boy-wolf",
    examples=[
        _ex(":wolf",    ":wolf",    "the keyword :wolf",
            "the value of :wolf"),
        _ex(":flock",   ":flock",   "the keyword :flock",
            "the value of :flock"),
        _ex(":alarm",   ":alarm",   "the keyword :alarm",
            "the value of :alarm"),
        _ex("(keyword? :wolf)", True,
            "the predicate (keyword? :wolf)",
            "whether :wolf is a keyword"),
        _ex("(= :wolf :wolf)", True,
            "the equality of two :wolf keywords",
            "whether :wolf equals :wolf"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-08 — Characters
G1_08 = SubjectCurriculum(
    grade=1, subject_id="G1-08",
    subject_title="Characters",
    fable="boy-wolf",
    examples=[
        _ex("\\w",      "w",     "the character \\w",
            "the value of \\w"),
        _ex("\\space",  " ",     "the character \\space",
            "the value of \\space"),
        _ex("\\T",      "T",     "the character \\T",
            "the value of \\T"),
        _ex("(char? \\w)", True,
            "the predicate (char? \\w)",
            "whether \\w is a character"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-09 — Symbols vs values
G1_09 = SubjectCurriculum(
    grade=1, subject_id="G1-09",
    subject_title="Symbols vs values",
    fable="boy-wolf",
    examples=[
        _ex("(symbol? 'wolf)", True,
            "the predicate (symbol? 'wolf)",
            "whether 'wolf is a symbol",
            scenario=(
                "Tom had chalked the word `wolf` on the watchhouse slate "
                "as a label for the south-flock pen. Carol stood beside "
                "him with a carved tag from a sheep tagged `wolf` — the "
                "actual animal the chalk mark named."
            ),
            need=(
                "The argument that morning was about which `wolf` the "
                "village should pay attention to. Without distinguishing "
                "the chalk mark from the sheep it pointed at, the "
                "village's notes would mix names with the things named."
            ),
            mapping=(
                "`symbol?` asks whether something is a chalk mark — a "
                "name standing in for a value — rather than the value "
                "itself. The quoted `'wolf` is the chalk mark; the "
                "actual sheep would be a different value."
            ),
            resolution=(
                "the predicate confirmed the chalk mark for what it was "
                "— a name, not a sheep — and the village's records "
                "stayed straight."
            )),
        _ex("(symbol? 42)", False,
            "the predicate (symbol? 42)",
            "whether 42 is a symbol"),
        _ex("(symbol? 42)", False,
            "the predicate (symbol? 42)",
            "whether 42 is a symbol"),
        _ex("'wolf", "wolf",
            "the quoted symbol 'wolf",
            "the value of 'wolf"),
        _ex("(= 'wolf 'wolf)", True,
            "the equality of two 'wolf symbols",
            "whether 'wolf equals 'wolf"),
    ],
    subplots=_CHALKMARK_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-10 — Comments
G1_10 = SubjectCurriculum(
    grade=1, subject_id="G1-10",
    subject_title="Comments",
    fable="boy-wolf",
    examples=[
        # Comments are stripped by the reader; what remains evaluates.
        _ex("(+ 1 2) ; sum of one and two", 3,
            "the form (+ 1 2) followed by a comment",
            "the result of (+ 1 2) ignoring the comment",
            scenario=(
                "Carol kept the watchhouse slate. Today she had chalked "
                "an addition on it, and to the right of the form she had "
                "drawn a single dashed line followed by `sum of one and "
                "two` in smaller chalk — annotation only, for the next "
                "shepherd's eye."
            ),
            need=(
                "Tom had been writing notes between forms and worried "
                "the runtime might somehow mix the annotations into the "
                "calculation. He needed to know which marks the runtime "
                "honored and which it skipped."
            ),
            mapping=(
                "A single semicolon `;` is the slate's ignore-from-here "
                "mark. Everything to the right of it is annotation — "
                "the reader skips it; the runtime never sees it. The "
                "form's value comes from what stays on the slate before "
                "the dash."
            ),
            resolution=(
                "the value came back as if the dashed annotation weren't "
                "there at all — exactly as the slate's conventions "
                "promised."
            )),
        _ex("42 ;; the answer", 42,
            "the literal 42 with a trailing comment",
            "the value of 42"),
    ],
    subplots=_SCRIBE_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-11 — Whitespace
G1_11 = SubjectCurriculum(
    grade=1, subject_id="G1-11",
    subject_title="Whitespace doesn't matter",
    fable="boy-wolf",
    examples=[
        _ex("(+    1    2)", 3,
            "the form (+ 1 2) with extra spaces",
            "the result of the form"),
        _ex("(+\n  1\n  2)", 3,
            "the form (+ 1 2) split across lines",
            "the result of the form"),
    ],
    subplots=_SCRIBE_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-12 — Parens as syntax
G1_12 = SubjectCurriculum(
    grade=1, subject_id="G1-12",
    subject_title="Parens group; they don't multiply",
    fable="boy-wolf",
    examples=[
        _ex("(+ 2 3)", 5,
            "the form (+ 2 3)",
            "the result of (+ 2 3)"),
        _ex("(* (+ 1 2) 3)", 9,
            "the form (* (+ 1 2) 3)",
            "the result of (* (+ 1 2) 3)"),
    ],
    subplots=_SCRIBE_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-13 — First arithmetic call
G1_13 = SubjectCurriculum(
    grade=1, subject_id="G1-13",
    subject_title="First arithmetic call",
    fable="boy-wolf",
    examples=[
        _ex("(+ 1 2)",  3,    "the form (+ 1 2)",    "the result of (+ 1 2)",
            scenario=(
                "At dawn, Tom had brought 1 lamb back from the south "
                "pasture and Carol had brought 2 from the north. They "
                "stood at the fold counting together, the village's "
                "morning record waiting on them."
            ),
            need=(
                "The combined morning tally needed to settle correctly "
                "before the day's work could begin — the village's "
                "records depended on exact arithmetic, no boasting and "
                "no fudging."
            ),
            mapping=(
                "`+` adds its operands one after another and gives back "
                "the running total. With 1 lamb from one side and 2 "
                "from the other, the runtime carries the sum exactly — "
                "no shouting required."
            ),
            resolution=(
                "the count came back as 3 lambs — the morning's flock "
                "confirmed by the runtime, not by Tom's memory."
            )),
        _ex("(- 5 3)",  2,    "the form (- 5 3)",    "the result of (- 5 3)"),
        _ex("(* 4 5)",  20,   "the form (* 4 5)",    "the result of (* 4 5)"),
        _ex("(/ 10 2)", 5,    "the form (/ 10 2)",   "the result of (/ 10 2)"),
        _ex("(+ 7 8)",  15,   "the form (+ 7 8)",    "the result of (+ 7 8)"),
        _ex("(- 20 7)", 13,   "the form (- 20 7)",   "the result of (- 20 7)"),
    ],
    subplots=_ACORN_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-14 — Nested call evaluation
G1_14 = SubjectCurriculum(
    grade=1, subject_id="G1-14",
    subject_title="Nested call evaluation",
    fable="boy-wolf",
    examples=[
        _ex("(+ 1 (* 2 3))",       7,
            "the nested form (+ 1 (* 2 3))",
            "the result of (+ 1 (* 2 3))"),
        _ex("(* (+ 1 2) (+ 3 4))", 21,
            "the nested form (* (+ 1 2) (+ 3 4))",
            "the result of (* (+ 1 2) (+ 3 4))"),
        _ex("(- 100 (* 5 5))",     75,
            "the nested form (- 100 (* 5 5))",
            "the result of (- 100 (* 5 5))"),
        _ex("(+ (* 2 3) (* 4 5))", 26,
            "the sum of two products",
            "the result of (+ (* 2 3) (* 4 5))"),
    ],
    subplots=_ACORN_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-15 — Equality
# Boy-wolf reading: village settles a dispute by checking equality, not
# by trusting the shepherd's claim. Same Clojure exercise as
# tortoise-hare, with thematic keyword swaps where they appear.
G1_15 = SubjectCurriculum(
    grade=1, subject_id="G1-15",
    subject_title="Equality",
    fable="boy-wolf",
    examples=[
        _ex("(= 1 1)",          True,  "the equality (= 1 1)",
            "the value of (= 1 1)",
            scenario=(
                "At the first fold-gate of the morning, Carol had two "
                "tally-marks carved into the post: one from yesterday's "
                "evening count, one from this morning's. Tom claimed "
                "the two had to differ — sheep, after all, never sat "
                "still."
            ),
            need=(
                "Before the flock could pass through the gate and begin "
                "the day's grazing, the gate had to confirm whether the "
                "two marks agreed. A mistaken pass would corrupt the "
                "village ledger."
            ),
            mapping=(
                "`=` compares its operands and answers whether they are "
                "the same. With both marks reading 1, the gate's "
                "predicate carries the comparison and returns the "
                "verdict — no opinion required."
            ),
            resolution=(
                "the gate opened — `=` returned true — and the village's "
                "count for the morning held without dispute."
            )),
        _ex("(= 1 2)",          False, "the equality (= 1 2)",
            "the value of (= 1 2)"),
        _ex("(= \"a\" \"a\")",  True,  "the equality (= \"a\" \"a\")",
            "the value of (= \"a\" \"a\")"),
        _ex("(= :wolf :wolf)",  True,  "the equality (= :wolf :wolf)",
            "the value of (= :wolf :wolf)"),
        _ex("(= :wolf :flock)", False,
            "the equality (= :wolf :flock)",
            "the value of (= :wolf :flock)"),
        _ex("(= 1 1 1 1)",      True,
            "the multi-arg equality (= 1 1 1 1)",
            "the value of (= 1 1 1 1)"),
    ],
    subplots=_GATE_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-16 — Numeric predicates
G1_16 = SubjectCurriculum(
    grade=1, subject_id="G1-16",
    subject_title="Numeric predicates",
    fable="boy-wolf",
    examples=[
        _ex("(zero? 0)",  True,  "the predicate (zero? 0)",
            "whether 0 is zero"),
        _ex("(zero? 5)",  False, "the predicate (zero? 5)",
            "whether 5 is zero"),
        _ex("(pos? 7)",   True,  "the predicate (pos? 7)",
            "whether 7 is positive"),
        _ex("(pos? -2)",  False, "the predicate (pos? -2)",
            "whether -2 is positive"),
        _ex("(neg? -3)",  True,  "the predicate (neg? -3)",
            "whether -3 is negative"),
        _ex("(neg? 4)",   False, "the predicate (neg? 4)",
            "whether 4 is negative"),
    ],
    subplots=_ACORN_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-17 — Printing vs returning
G1_17 = SubjectCurriculum(
    grade=1, subject_id="G1-17",
    subject_title="Printing vs returning",
    fable="boy-wolf",
    examples=[
        _ex("42", 42,
            "the value 42",
            "the value of 42"),
        _ex("(+ 1 2)", 3,
            "the form (+ 1 2)",
            "the result of (+ 1 2)"),
    ],
    subplots=_SCRIBE_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-18 — Errors are safe in the REPL
G1_18 = SubjectCurriculum(
    grade=1, subject_id="G1-18",
    subject_title="Errors are safe in the REPL",
    fable="boy-wolf",
    examples=[
        _ex("(+ 1 2)", 3,
            "the form (+ 1 2)",
            "the result of (+ 1 2)",
            scenario=(
                "Tom hesitated at the practice-pen behind the watchhouse "
                "— the small enclosure where new shepherds drilled the "
                "alarm-protocol. Carol had set out a slate and a piece "
                "of chalk, ready to demonstrate."
            ),
            need=(
                "Tom was anxious about writing a wrong form. Carol "
                "explained that this pen was for that exact purpose: to "
                "make a careless try cost nothing, so the shepherd could "
                "experiment before the day's real watch began."
            ),
            mapping=(
                "The REPL acts the way the practice-pen acts. A wrong "
                "form, a typo, a missing paren — anything tried inside "
                "is safely walked back. The runtime catches mistakes "
                "instead of letting them spill out into the village."
            ),
            resolution=(
                "Tom wrote the form, the runtime returned its value "
                "cleanly, and Carol nodded — the pen had served its "
                "purpose; he could try again any time."
            )),
        _ex("(* 7 6)", 42,
            "the form (* 7 6)",
            "the result of (* 7 6)"),
    ],
    subplots=_SAFETYNET_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# ─────────────────────── registry ───────────────────────


SUBJECTS: dict[str, SubjectCurriculum] = {
    s.subject_id: s for s in (
        G1_01, G1_02, G1_03, G1_04, G1_05, G1_06, G1_07, G1_08, G1_09,
        G1_10, G1_11, G1_12, G1_13, G1_14, G1_15, G1_16, G1_17, G1_18,
    )
}


def smoke_test() -> None:
    """Generate one record from each subject; verify shape."""
    from mmllm.aesop.curriculum.generator import generate_subject

    for sid, sub in SUBJECTS.items():
        recs = generate_subject(sub, n_per_example=1, seed=0)
        assert recs, f"no records for {sid}"
        for r in recs:
            assert r.tool_calls, f"no tool_calls for {sid}"
            assert r.tool_calls[0]["name"] == "eval"
            assert r.user_msg
            assert r.assistant_msg
    print(f"grade-1 boy-wolf smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
