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
from mmllm.aesop.curriculum.boy_wolf._goals import GOALS, get_goal


# ─────────────────────── boy-wolf-specific EMO pools ───────────────────────
#
# Gender-neutral (no possessive "her"/"his"/"their" baked in). Imagery
# fits the boy-wolf valley setting (shouting from the hill, the watchhouse
# slate, false alarms, the elder's patience) — no race / sprint /
# underbrush leakage from tortoise-hare.

BW_EMO_PROUD: tuple[str, ...] = (
    "with a smug grin",
    "puffed up with pride",
    "as if the watchhouse would always believe",
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
{emo_patient}, asked {shepherd_him_her} to actually submit
{form_display} to the REPL — the townsfolk had stopped trusting answers
that weren't checked."""),

    # 2. The trust-ledger template — the village elder keeps a written
    #    tally of which claims were verified vs. just-guessed. Today's
    #    entry is the form. (Boy-wolf-flavored ledger beat — analogous
    #    to tortoise-hare's "wager" without the wager's gambling tone.)
    SubplotTemplate("""\
The elder of the meadow folk kept a small slate {place}, {emo_patient},
with a tally of expressions the shepherds had directly submitted versus
ones they had only guessed at. The valley was long and the
shepherds many; the slate kept what speech could not. The next
line was {concept_phrase}.
{elder_phrase} read aloud {form_display} so {shepherd_phrase}
could write it properly into the REPL and earn a clean mark on
the slate."""),

    # 2b. Trust-ledger variant — slate kept on a stone at the townsfolk edge.
    SubplotTemplate("""\
A small slate sat on a flat stone {place}; the day was long and the
slate filled slowly, mark by mark. On it the reeve recorded each
expression a shepherd had submitted to the REPL alongside each claim
made without checking. Today's entry was {form_display}, and the page
heading read {concept_phrase}. {elder}, {emo_patient}, nodded at
{shepherd_phrase} to write it properly so the slate would
carry a verified entry."""),

    # 2c. Trust-ledger variant — the elder's pocket notebook.
    SubplotTemplate("""\
{elder_phrase}, {emo_patient}, kept a small slate-pocket of
every expression the shepherds of the valley had actually evaluated —
each entry slow as the rising sun, the page-count climbing only
when the REPL had spoken. Today {place} the next entry was
{concept_phrase}. {shepherd_phrase} peered over {elder_his_her}
shoulder at {form_display} and was asked, gently, to be
the one to submit it."""),

    # 3. The careful-villager template — a villager (the corrective
    #    voice) gently teaches the shepherd how the REPL works using
    #    this form. Echoes the fable's "boy's mother explains the rule"
    #    beat. Comma after "said" handles participle-style EMO_PATIENT.
    SubplotTemplate("""\
{elder_phrase} had been trying to teach {shepherd_phrase} how the REPL
works. "Look here," {elder_he_she} said, pointing to {concept_phrase}.
"You hand {form_display} to the runtime, and the runtime hands
you back what it evaluates to. That is the only voice we trust now."
{shepherd}, {emo_tired}, agreed to try."""),

    # 4. The audience template — small village crowd watches the
    #    shepherd attempt to predict, then the elder insists on a real
    #    submission. NOTE: uses "pointed to" rather than "read aloud"
    #    so abstract concept_phrases ("the equality (= 1 1)") fit.
    SubplotTemplate("""\
A small crowd of villagers had gathered {place} to watch
{shepherd_phrase} attempt to predict, off the cuff, what the REPL
would return. The lookout was high and the day was clear; from the
slope the slate was easy to read, and so was a wrong claim.
{elder_phrase}, {emo_patient}, pointed to {concept_phrase} and read
it out aloud: {form_display}. The villagers waited, patient
but unimpressed, to see who would submit the expression properly."""),

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
Halfway through the morning watch, {shepherd_phrase}, {emo_proud},
called out {place}, demanding a verdict on {form_display}
and refusing to come back to the flock until somebody confirmed it.
The pasture was wide and the sheep were restless; the longer the
shepherd argued, the further the flock drifted. {shepherd} was sure
of the answer already. {elder_phrase}, {emo_patient}, walked up at
an unhurried pace and simply said: "Submit it. Whatever comes
back is the answer.\""""),

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
actually write {form_display} and submit it to the REPL —
just to be sure."""),

    # 8. The puzzle-on-the-village-board template — a sign / scrap of
    #    parchment in the valley square poses the form as a riddle.
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
        goal_text=goal if goal is not None else get_goal(form, concept, what),
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
        _ex("(+ 1 2)",             3,     "the expression (+ 1 2)",
            "the result of (+ 1 2)"),
        _ex("(* 4 5)",             20,    "the expression (* 4 5)",
            "the result of (* 4 5)"),
        _ex("(- 10 (+ 2 3))",      5,     "the nested expression (- 10 (+ 2 3))",
            "the result of (- 10 (+ 2 3))"),
        _ex("(+ 1 (* 2 3))",       7,     "the expression (+ 1 (* 2 3))",
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
            "the expression (+ 1/2 1/4)",
            "the value of (+ 1/2 1/4)"),
        _ex("(* 2 1/2)", 1,
            "the expression (* 2 1/2)",
            "the value of (* 2 1/2)"),
        _ex("(- 1 1/3)", "2/3",
            "the expression (- 1 1/3)",
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
                "Tom had chalked a label on the slate for a flock pen. "
                "Carol stood with a carved tag from the live sheep itself."
            ),
            need=(
                "The village's notes must not mix chalk marks with the "
                "things they name. Tom had to tell them apart."
            ),
            mapping=(
                "`symbol?` asks whether something is a chalk mark — a "
                "name standing in for a value. The quoted form is the mark."
            ),
            resolution=(
                'the predicate returned true — it was a chalk mark, a name, not the thing itself. The records stayed straight (with `wolf` as the input value).'
            )),
        _ex("(symbol? 42)", False,
            "the predicate (symbol? 42)",
            "whether 42 is a symbol",
            scenario=(
                "Carol had chalked a tally-mark on the watchhouse slate — "
                "the number 42. Tom held a wooden tally-stick carved with "
                "notches. 'Are they the same thing?' he asked."
            ),
            need=(
                "The village's count book must stay clear: marks on the "
                "slate versus the carved sticks must not be confused. "
                "Tom needed to know whether a mark and a stick were the "
                "same thing."
            ),
            mapping=(
                "`symbol?` returns false for numbers. The chalk mark "
                "'42 is a name, a symbol; but the number 42 itself is "
                "the actual count. The predicate draws that line — mark "
                "versus meaning."
            ),
            resolution=(
                "the predicate said no — the number and the name were not the same, keeping the village's records straight. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record."           )),
        _ex("'wolf", "wolf",
            "the quoted symbol 'wolf",
            "the value of 'wolf",
            scenario=(
                "At the fold-gate, Carol pointed to a chalk mark on the "
                "slate — a name for a pen. Tom carried a sheep tagged for "
                "that pen."
            ),
            need=(
                "The shepherds must trust which is the name and which is "
                "the thing named. Tom had to confirm that the quoted mark "
                "gave back the symbol itself."
            ),
            mapping=(
                "The quote `'` stops substitution: the runtime sees the "
                "chalk mark as a symbol — a name — rather than trying to "
                "look up what that name refers to."
            ),
            resolution=(
                'the runtime returned the symbol itself, exactly the chalk mark, with no further substitution (with `wolf` as the input value).'
            )),
        _ex("(= 'wolf 'wolf)", True,
            "the equality of two 'wolf symbols",
            "whether 'wolf equals 'wolf",
            scenario=(
                "Carol had written `wolf` twice on the watchhouse slate "
                "— once in the morning tally, once in the evening. Tom "
                "wondered if the two marks were the same."
            ),
            need=(
                "The village's morning and evening counts must agree on "
                "which pen is which. Clarity on symbol equality keeps the "
                "ledger sound."
            ),
            mapping=(
                "`=` compares symbols by their chalk-mark form. Two "
                "identical marks written in the same hand are equal — "
                "the symbol `wolf` equals the symbol `wolf` exactly."
            ),
            resolution=(
                'the predicate returned true — the two marks on the slate were the same chalk line, nothing more nor less.'
            )),
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
            "the expression (+ 1 2) followed by a comment",
            "the result of (+ 1 2) ignoring the comment",
            scenario=(
                "Carol had chalked an addition on the slate with a dashed "
                "line and notes in smaller chalk to the right — annotation "
                "only, for the next shepherd's eye."
            ),
            need=(
                "Tom worried the runtime might mix annotations into the "
                "calculation. He needed to know which marks the runtime "
                "honored and which it skipped."
            ),
            mapping=(
                "A single semicolon `;` is the slate's ignore-from-here "
                "mark. Everything to the right is annotation — the reader "
                "skips it; the runtime never sees it."
            ),
            resolution=(
                "the value came back as if the dashed annotation weren't there at all — exactly as the slate's conventions promised. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last."         )),
        _ex("42 ;; the answer", 42,
            "the literal 42 with a trailing comment",
            "the value of 42",
            scenario=(
                "Carol had written a value on the slate, then added a double "
                "dash and human words to explain it. Tom peered at the full "
                "line, confused about what the runtime would see."
            ),
            need=(
                "Tom had to trust the slate's convention: only the form "
                "matters to the runtime, never the human marks that follow "
                "the dash."
            ),
            mapping=(
                "A double semicolon `;;` marks everything after it as "
                "reader-ignored — true annotation. The runtime sees only "
                "what comes before; the dash-mark seals off the rest."
            ),
            resolution=(
                "the value came back — the runtime had skipped the dashed remark entirely, honoring the slate's reading rule. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand."           )),
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
            "the expression (+ 1 2) with extra spaces",
            "the result of the form",
            scenario=(
                "Carol had written the form on the slate with extra space "
                "between the symbols — to give Tom room to read each part "
                "carefully. Tom worried the gaps might break the form."
            ),
            need=(
                "The shepherd's eye must trust the blank spaces: they guide "
                "reading but mean nothing to the runtime."
            ),
            mapping=(
                "The reader strips whitespace — spaces, tabs, blank lines — "
                "before the runtime sees the form. Extra gaps are chalk "
                "marks for the human reader only; the runtime sees the "
                "structure, not the formatting."
            ),
            resolution=(
                'the form evaluated to the sum, indifferent to the spacing — the runtime had seen only the operator and operands, nothing more. Tom chalked {drawn.a} on the watchhouse notice, and the morning record stood for the next shepherd to read.'           )),
        _ex("(+\n  1\n  2)", 3,
            "the expression (+ 1 2) split across lines",
            "the result of the form",
            scenario=(
                "Carol had chalk-written an addition in a tall column on the "
                "slate — operator at the top, each operand below on its own "
                "row. Tom asked if splitting it into rows might change the "
                "meaning."
            ),
            need=(
                "The form must stay readable on a narrow slate. Tom had to "
                "trust that line breaks, like spaces, left the form's "
                "meaning untouched."
            ),
            mapping=(
                "Newlines are whitespace: the reader strips them before "
                "sending the form to the runtime. A column layout and a "
                "line layout express the same arithmetic — the structure "
                "is what counts, not the layout."
            ),
            resolution=(
                "the call returned its sum, exact as if written in a single line — the slate's vertical layout had been invisible to the runtime. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain."           )),
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
            "the expression (+ 2 3)",
            "the result of (+ 2 3)",
            scenario=(
                "Carol had written parentheses on the watchhouse slate — "
                "an outer pair with the arithmetic operators inside. Tom "
                "watched and asked what the curved brackets meant."
            ),
            need=(
                "Tom needed to know that parentheses are only syntax — "
                "grouping marks, not a multiplication signal."
            ),
            mapping=(
                "Parentheses `( )` tell the reader and runtime how to "
                "parse the form. They group the operator with its "
                "operands. The first element inside becomes the function; "
                "the rest become arguments. No implicit multiplication."
            ),
            resolution=(
                'the call returned the sum — the runtime had grouped the symbols correctly without treating the parens as an operation themselves. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'           )),
        _ex("(* (+ 1 2) 3)", 9,
            "the expression (* (+ 1 2) 3)",
            "the result of (* (+ 1 2) 3)",
            scenario=(
                "Carol had nested parentheses on the slate — one pair of "
                "brackets holding an addition, the whole thing an argument "
                "to a multiplication. Tom squinted at the layers."
            ),
            need=(
                "Nested parentheses must be resolved from inside out. Tom "
                "had to trust the runtime's careful unpacking of the "
                "brackets."
            ),
            mapping=(
                "When parentheses nest, the runtime evaluates the innermost "
                "first — the inner sum becomes a single value, then that "
                "value multiplies with the outer argument. Parens are "
                "grouping brackets only; nesting shows order, never "
                "multiplication."
            ),
            resolution=(
                'the runtime returned the product — it had evaluated the inner form first, then used that result in the outer multiplication. Parens had grouped, not multiplied. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'           )),
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
        _ex("(+ 1 2)",  3,    "the expression (+ 1 2)",    "the result of (+ 1 2)",
            scenario=(
                "At dawn, Tom had brought lambs back from the south "
                "pasture and Carol had brought lambs from the north. They "
                "stood at the fold counting together, the meadow folk's "
                "morning record waiting on them."
            ),
            need=(
                "The combined morning tally needed to settle correctly "
                "before the day's work could begin — the townsfolk's "
                "records depended on exact arithmetic, no boasting and "
                "no fudging."
            ),
            mapping=(
                "`+` adds its operands one after another and gives back "
                "the running total. The runtime carries the sum exactly "
                "— no shouting required."
            ),
            resolution=(
                "the count came back — the morning's flock confirmed by the runtime, not by Tom's memory. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear."           )),
        _ex("(- 5 3)",  2,    "the expression (- 5 3)",    "the result of (- 5 3)",
            scenario=(
                "Tom had watched some sheep leave the fold that morning and "
                "some return by noon. Carol chalked the question on the "
                "slate: how many were still grazing?"
            ),
            need=(
                "The village's grazing count had to be exact before the "
                "afternoon watch. No guessing on the flock."
            ),
            mapping=(
                "`-` subtracts: the starting count minus those returned "
                "gives the sheep still away. The runtime computes the exact "
                "remainder."
            ),
            resolution=(
                "the result came back — the exact number of sheep still grazing, confirmed by arithmetic not by Tom's memory. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record."           )),
        _ex("(* 4 5)",  20,   "the expression (* 4 5)",    "the result of (* 4 5)",
            scenario=(
                "Carol had several small baskets of wool, each holding the "
                "same count of fleeces. Tom tried to count them all at once "
                "but lost track. Carol chalked the multiplication."
            ),
            need=(
                "The village's morning wool-tally had to be final. Tom's "
                "eyeball count could not match the ledger."
            ),
            mapping=(
                "`*` multiplies: groups of items, combined. The runtime "
                "compounds the count exactly, no fumbling."
            ),
            resolution=(
                'the result came back — the total fleeces, exact as any careful basket count would yield. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'           )),
        _ex("(/ 10 2)", 5,    "the expression (/ 10 2)",   "the result of (/ 10 2)",
            scenario=(
                "Carol had coins paid for wool. She and Tom had agreed to "
                "split them evenly. Carol wrote the division on the slate."
            ),
            need=(
                "The split had to be fair and final, no haggling once the "
                "slate was written."
            ),
            mapping=(
                "`/` divides: the total coins split into equal shares. The "
                "runtime computes each shepherd's fair portion exactly."
            ),
            resolution=(
                "the result came back — each shepherd's coins, arithmetic settling what trust could not. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand."           )),
        _ex("(+ 7 8)",  15,   "the expression (+ 7 8)",    "the result of (+ 7 8)",
            scenario=(
                "Tom brought lambs from the north pen, Carol brought lambs "
                "from the south. Together they needed the total for the "
                "morning record."
            ),
            need=(
                "The day's first count had to lock in before the flock "
                "left for pasture. Arithmetic, not eyeballing."
            ),
            mapping=(
                "`+` adds: the operands combined, the morning tally. The "
                "runtime carries each number faithfully and returns the "
                "sum."
            ),
            resolution=(
                "the count came back — the morning's full flock, confirmed by the runtime and entered in the ledger. Tom chalked {drawn.a} on the village notice, and the morning record stood for the next shepherd to read."           )),
        _ex("(- 20 7)", 13,   "the expression (- 20 7)",   "the result of (- 20 7)",
            scenario=(
                "Carol had many fleeces sorted for the week's market. By "
                "noon some had been claimed by shepherds. She wrote the "
                "subtraction to see what remained."
            ),
            need=(
                "The unsold count had to be ready before the market-runner "
                "came by. No penciling and erasing on the real ledger."
            ),
            mapping=(
                "`-` removes: the original count minus those claimed, "
                "equals what stays. The runtime computes the remaining "
                "tally exactly."
            ),
            resolution=(
                'the result came back — the fleeces still waiting, exact and ready for the market count. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'           )),
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
            "the nested expression (+ 1 (* 2 3))",
            "the result of (+ 1 (* 2 3))",
            scenario=(
                "Carol had written a nested form on the slate showing the "
                "morning count: some from one pen, plus groups from "
                "another pen. Tom squinted at the nested layers."
            ),
            need=(
                "The morning's full count had to be exact. Nested "
                "arithmetic had to be unpacked in the right order."
            ),
            mapping=(
                "The runtime works from the inside out: the inner "
                "multiplication resolves first, becoming a single value, "
                "then that value adds to the outer operand. Inner forms "
                "resolve first; their results feed the outer operation."
            ),
            resolution=(
                'the result came back — the runtime had nested the arithmetic perfectly, giving the total flock for the ledger. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'           )),
        _ex("(* (+ 1 2) (+ 3 4))", 21,
            "the nested expression (* (+ 1 2) (+ 3 4))",
            "the result of (* (+ 1 2) (+ 3 4))",
            scenario=(
                "Carol had chalked two addition problems side by side, then "
                "asked what it would mean to multiply them together."
            ),
            need=(
                "Tom had to trust that each inner sum would be calculated "
                "first, then the two results multiplied for the final tally."
            ),
            mapping=(
                "Both inner forms evaluate first, each becoming a single "
                "value. Then those two results become arguments to `*`. "
                "Inside resolves before outside."
            ),
            resolution=(
                'the call returned the product — the runtime had nested the order perfectly, each sum resolved before the multiplication. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'           )),
        _ex("(- 100 (* 5 5))",     75,
            "the nested expression (- 100 (* 5 5))",
            "the result of (- 100 (* 5 5))",
            scenario=(
                "Carol had a tally of coins. Tom wondered how many "
                "would remain after paying shepherds equally by weight. "
                "Carol chalked the nested form."
            ),
            need=(
                "The payment calculation had to be exact: first the total "
                "owed, then the remainder. Nesting made it clear."
            ),
            mapping=(
                "The inner form multiplies to give the total owed. Then "
                "the outer subtraction subtracts that total from the "
                "starting amount. Inside evaluates first."
            ),
            resolution=(
                'the result came back — the coins left after the payment, the nesting having clarified the order. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'           )),
        _ex("(+ (* 2 3) (* 4 5))", 26,
            "the sum of two products",
            "the result of (+ (* 2 3) (* 4 5))",
            scenario=(
                "Carol had two groups of fleeces: several baskets with the "
                "same count in each group. She chalked both products side "
                "by side, then their sum."
            ),
            need=(
                "The village's fleece inventory had to account for both "
                "groups. Nested nesting showed the full picture."
            ),
            mapping=(
                "Each multiplication resolves first, becoming a single value. "
                "Then those two values become arguments to `+`. Inner forms "
                "resolve first; their results feed the outer addition."
            ),
            resolution=(
                'the result came back — the total fleeces from both groups, nesting having kept each count separate until the final tally. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'           )),
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
                "the gate opened — `=` returned true — and the meadow folk's count for the morning held without dispute. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last."         )),
        _ex("(= 1 2)",          False, "the equality (= 1 2)",
            "the value of (= 1 2)",
            scenario=(
                "Carol had two tally-marks on a stone by the fold: one "
                "from the morning count, one from midday. Tom claimed they "
                "must differ because sheep move. Carol wrote them side by "
                "side to test."
            ),
            need=(
                "Before the afternoon watch, the fold's gate needed to "
                "know: are the counts the same or different? The gate "
                "depends on that answer."
            ),
            mapping=(
                "`=` compares each operand: does 1 equal 2? No. The "
                "runtime's verdict is false — they are not the same."
            ),
            resolution=(
                'the gate returned false — the counts differed, and the valley would note which pen had gained or lost sheep. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'           )),
        _ex("(= \"a\" \"a\")",  True,  "the equality (= \"a\" \"a\")",
            "the value of (= \"a\" \"a\")",
            scenario=(
                "Carol had written the letter `a` on the slate twice — "
                "once in the morning lesson, once in the afternoon. Tom "
                "wondered if the two marks were truly the same mark."
            ),
            need=(
                "The elder's teaching depended on stable symbols. Carol "
                "had to show that the same chalk mark, written twice, was "
                "indeed the same mark."
            ),
            mapping=(
                "`=` compares strings: does \"a\" equal \"a\"? Yes. The "
                "runtime returns true — both are the same string."
            ),
            resolution=(
                "the predicate returned true — the chalk marks matched letter for letter, confirming Carol's careful writing. Tom chalked {drawn.a} on the valley notice, and the morning record stood for the next shepherd to read."           )),
        _ex("(= :wolf :wolf)",  True,  "the equality (= :wolf :wolf)",
            "the value of (= :wolf :wolf)",
            scenario=(
                "The watchhouse had two drill-cards, each marked `:wolf` "
                "at the top — the name of the alarm to sound when a wolf "
                "was spotted. Tom wanted to be sure both cards named the "
                "same alarm."
            ),
            need=(
                "The alarm system depends on all shepherds hearing the "
                "same name. Tom had to trust that the keyword :wolf meant "
                "the same thing on both cards."
            ),
            mapping=(
                "`=` compares keywords: does :wolf equal :wolf? Yes. The "
                "runtime returns true — the same keyword appears twice."
            ),
            resolution=(
                'the predicate returned true — both cards carried the same alarm-name, and the system stayed consistent. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'           )),
        _ex("(= :wolf :flock)", False,
            "the equality (= :wolf :flock)",
            "the value of (= :wolf :flock)",
            scenario=(
                "Carol had written :wolf and :flock on two separate slate "
                "tiles — one naming the alarm for danger, one naming the "
                "call to gather. Tom had to be sure the runtime could tell "
                "them apart."
            ),
            need=(
                "The shepherds' signals must not be confused. One false "
                "equivalence and the village would be in chaos."
            ),
            mapping=(
                "`=` compares keywords: does :wolf equal :flock? No. The "
                "runtime returns false — they are different names."
            ),
            resolution=(
                'the predicate returned false — the two keywords were distinct, keeping the alarm system clear and separate. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'           )),
        _ex("(= 1 1 1 1)",      True,
            "the multi-arg equality (= 1 1 1 1)",
            "the value of (= 1 1 1 1)",
            scenario=(
                'Carol had the stones at the fold, each notched once — the morning count from four separate shepherds. They all agreed on the same tally. Carol wrote the multi-arg equality test.'
            ),
            need=(
                "Before the day's work began, all the counts had to agree. If they matched, the flock was accounted for and the village could proceed."
            ),
            mapping=(
                "`=` with multiple arguments checks if all are the same. "
                "Does 1 equal 1? And does that 1 equal the next 1? And so "
                "on? Yes to all. The runtime returns true."
            ),
            resolution=(
                "the predicate returned true — all four counts agreed, and the morning's record locked in with the watchhouse ledger. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement."           )),
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
            "whether 0 is zero",
            scenario=(
                "At the fold-gate, Carol had a tally-mark: 0. Tom asked "
                "if the gates should stay open for no sheep, as though "
                "no sheep had come."
            ),
            need=(
                "The gate's logic had to distinguish zero (no sheep) from "
                "any other count. Clarity on what zero meant kept the "
                "system fair."
            ),
            mapping=(
                "`zero?` tests whether the number is exactly zero. On 0, "
                "the predicate returns true — confirming that zero means "
                "nothing at the fold."
            ),
            resolution=(
                "the predicate returned true — the count was zero, and the gate's rule for an empty flock was confirmed. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear."           )),
        _ex("(zero? 5)",  False, "the predicate (zero? 5)",
            "whether 5 is zero",
            scenario=(
                "Carol pointed to a tally of 5 sheep. Tom wondered if the "
                "predicate `zero?` would mistake the count for nothing. "
                "Carol wrote the test."
            ),
            need=(
                "Tom had to trust that `zero?` would correctly reject any "
                "count that was not zero."
            ),
            mapping=(
                "`zero?` tests whether the number is exactly zero. On 5, "
                "the predicate returns false — 5 is not zero."
            ),
            resolution=(
                "the predicate returned false — the count was real, and the fold's gate would open for the 5 sheep to pass. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record."           )),
        _ex("(pos? 7)",   True,  "the predicate (pos? 7)",
            "whether 7 is positive",
            scenario=(
                "Carol had tracked the flock's change from morning to "
                "afternoon: +7 sheep had returned. Tom asked if the "
                "predicate could confirm that the change was positive."
            ),
            need=(
                "The village's ledger recorded gains and losses. `pos?` "
                "had to show that the flock had grown."
            ),
            mapping=(
                "`pos?` tests whether a number is greater than zero. On 7, "
                "the predicate returns true — a gain of 7 sheep is positive."
            ),
            resolution=(
                "the predicate returned true — the change was confirmed as positive, and the afternoon's gain was entered in the ledger. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last."           )),
        _ex("(pos? -2)",  False, "the predicate (pos? -2)",
            "whether -2 is positive",
            scenario=(
                "Tom had counted 2 fewer sheep at the afternoon fold than "
                "at morning. Carol wanted the predicate to confirm that -2 "
                "was not a positive change."
            ),
            need=(
                "The village had to track losses as losses. `pos?` had to "
                "reject negative numbers clearly."
            ),
            mapping=(
                "`pos?` tests whether a number is greater than zero. On -2, "
                "the predicate returns false — a loss is not positive."
            ),
            resolution=(
                'the predicate returned false — the change was confirmed as negative, and the loss was recorded as such. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'           )),
        _ex("(neg? -3)",  True,  "the predicate (neg? -3)",
            "whether -3 is negative",
            scenario=(
                "Carol had a record: -3 fleeces sold this week (a shortage). "
                "Tom wondered if `neg?` would confirm the negative change."
            ),
            need=(
                "The wool-ledger had to mark shortages clearly. `neg?` had "
                "to confirm that -3 was indeed negative."
            ),
            mapping=(
                "`neg?` tests whether a number is less than zero. On -3, "
                "the predicate returns true — the shortage is negative."
            ),
            resolution=(
                'the predicate returned true — the shortage was confirmed as negative, and the watchhouse would plan accordingly. Tom chalked {drawn.a} on the townsfolk notice, and the morning record stood for the next shepherd to read.'           )),
        _ex("(neg? 4)",   False, "the predicate (neg? 4)",
            "whether 4 is negative",
            scenario=(
                "Carol had tallied a gain of 4 fleeces. Tom asked if `neg?` "
                "would mistakenly mark the gain as negative."
            ),
            need=(
                "Gains and losses had to stay distinct. Tom had to trust "
                "that `neg?` would correctly reject positive numbers."
            ),
            mapping=(
                "`neg?` tests whether a number is less than zero. On 4, "
                "the predicate returns false — a gain is not negative."
            ),
            resolution=(
                'the predicate returned false — the gain was not negative, and the wool-ledger would show a positive entry. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'           )),
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
            "the value of 42",
            scenario=(
                "Carol had chalked a number on the watchhouse slate. Tom "
                "peered at it and asked whether that mark on the stone was "
                "the value itself or just a record."
            ),
            need=(
                "Tom had to understand that the runtime's return value is "
                "separate from any mark on the slate. The chalk mark shows "
                "the form; the REPL's response is the value."
            ),
            mapping=(
                "When the form is a literal number, the REPL evaluates it "
                "and returns that number. The value is what the runtime "
                "gives back — not a mark on the slate, but the answer itself."
            ),
            resolution=(
                'the REPL returned the value — not a mark, but the answer. Tom could carry that forward; the slate was just a record. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'           )),
        _ex("(+ 1 2)", 3,
            "the expression (+ 1 2)",
            "the result of (+ 1 2)",
            scenario=(
                "Carol had chalked an addition on the slate and asked Tom "
                "to read what the REPL would return. Tom confused the chalk "
                "mark for the answer."
            ),
            need=(
                "Tom had to separate the form written from the result the "
                "REPL computes. Chalk on slate, value in return — two "
                "different things."
            ),
            mapping=(
                "When the form is an addition, the REPL evaluates it and "
                "returns the sum. The returned value is the arithmetic "
                "result, not the form itself."
            ),
            resolution=(
                'the REPL returned the sum — the computed result, not the form that had been written. Tom had learned the distinction. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'           )),
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
            "the expression (+ 1 2)",
            "the result of (+ 1 2)",
            scenario=(
                "Tom hesitated at the practice-pen behind the watchhouse. "
                "Carol had set out a slate and chalk to demonstrate."
            ),
            need=(
                "Tom was anxious about errors. Carol explained the pen "
                "made careless tries cost nothing — a place to experiment."
            ),
            mapping=(
                "The REPL in the practice-pen is safe. A wrong form, "
                "a typo, anything tried inside is safely walked back."
            ),
            resolution=(
                'Tom wrote it, the runtime returned its value cleanly, and the pen had served its purpose. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'
            )),
        _ex("(* 7 6)", 42,
            "the expression (* 7 6)",
            "the result of (* 7 6)",
            scenario=(
                "Tom was trying again inside the practice-pen — a "
                "multiplication this time. Carol watched as Tom wrote it."
            ),
            need=(
                "The pen's purpose was to let Tom experiment without fear. "
                "Any form would either work or fail safely, no cost to either."
            ),
            mapping=(
                "The REPL in the practice-pen works just as in the real watch. "
                "The runtime returns the answer or an error that teaches."
            ),
            resolution=(
                'the call returned the product — the pen had served its purpose as a safe place to try and learn. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'           )),
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
