"""Grade 1 — atoms + first eval, taught through the Fox-and-the-Grapes fable.

Each subject defines:
  - examples: a list of Clojure exercises (form + expected + concept_phrase)
  - subplots: 8 narrative templates that wrap any example in fable scenery
  - plan_pool: optional plan-only prefaces (never reveal the answer)

The fable's moral dynamic — rationalizing the unattainable — informs
the two named voices in every record:

  hasty_fox    — original Aesop voice. Declares the form too high or
                 not worth evaluating; the rationalizer.
  patient_fox  — corrective voice. Writes the form anyway and lets
                 the REPL settle the answer; the disciplined evaluator.

Two distinct foxes are picked per record (Renard / Vix / Sly), so the
dialectic always has two named identities. The shared 8-subplot pool
is reused across all 18 grade-1 subjects.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.fox_grapes._metaphor_pools import (
    _ACORN_SUBPLOTS,
    _CHALKMARK_SUBPLOTS,
    _GATE_SUBPLOTS,
    _SAFETYNET_SUBPLOTS,
    _SCRIBE_SUBPLOTS,
)


# ─────────────────────── shared subplot pool ───────────────────────
#
# 8 templates spanning the narrative beats of fox-grapes:
#  1. argument over a chalked form on a post (the "vine and cluster")
#  2. wager about the answer
#  2b. wager variant — board instead of post
#  2c. wager variant — twig in the dirt
#  3. teacher — patient fox demonstrating the REPL to the hasty one
#  4. small audience watches the demonstration
#  5. rationalize-and-rebuke — hasty fox declares the form not worth
#     evaluating ("probably sour anyway"); patient fox insists on
#     submitting it
#  6. ledger — patient fox keeps a notebook of evaluated forms
#  7. boast-and-rebuke — hasty fox claims to know without checking
#  8. puzzle on a sign / engraving on a gate
#
# Templates use {form_display} for the literal form (backtick-wrapped),
# {concept_phrase} for the noun-phrase ("the value 42"), and the
# fox placeholders {hasty_fox} / {patient_fox} (plus pronoun forms)
# for character/setting variation.
#
# Care taken:
#  - {hasty_fox_him_her} (object case) used after "asked X to ...".
#  - Comma before {emo_proud} when it follows "said".
#  - {hasty_fox} (the name) used in second mention to avoid singular-
#    they ambiguity for gender="n" foxes (Sly).
#  - No EMO_HUNGRY / EMO_REGRETFUL — those pools have hardcoded
#    gendered pronouns ("his stomach hollow with hunger") that
#    occasionally mismatch the chosen fox's gender. EMO_PROUD /
#    EMO_PATIENT are mostly neutral.
#  - No literal answer in any template; the answer comes from the form.

_SHARED_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The argument template — a form is chalked on a post; hasty fox
    #    dismisses it; patient fox insists they actually evaluate it.
    SubplotTemplate("""\
{hasty_fox_phrase} and {patient_fox_phrase} stopped {place} where
someone had chalked {concept_phrase} on a wooden post. {hasty_fox},
{emo_proud}, declared the form was too high a guess to bother with.
{patient_fox}, {emo_patient}, suggested they actually evaluate
{form_display} in the REPL and read off whatever it returned."""),

    # 2. The wager template — bet on the answer, drawn in the dirt.
    SubplotTemplate("""\
{hasty_fox_phrase} sketched a small wager into the dirt {place}:
whoever guessed the result of {form_display} first would claim the
next cluster of grapes. {patient_fox_phrase}, {emo_patient}, said it
was simpler to type the form into the REPL than to argue about
{concept_phrase}."""),

    # 2b. Wager variant — chalked on a board.
    SubplotTemplate("""\
{hasty_fox_phrase} chalked a wager on a flat board {place}: whoever
predicted the result of {form_display} would set the next ration of
fruit. {patient_fox_phrase}, {emo_patient}, said it would be simpler
to type the form into the REPL than to bicker over {concept_phrase}."""),

    # 2c. Wager variant — twig in the dust.
    SubplotTemplate("""\
With a twig, {hasty_fox_phrase} marked out a wager {place}: whoever
guessed the result of {form_display} first would win the right to
choose the next vine to inspect. {patient_fox_phrase}, {emo_patient},
said it was easier to ask the REPL about {concept_phrase} than to
argue."""),

    # 3. The teacher template — patient fox is demonstrating the REPL.
    #    No EMO_TIRED here: the patient-fox-explaining beat reads
    #    cleaner without the fatigue clause, and EMO_TIRED has one
    #    gendered phrase ("her legs heavy from sprinting") that's also
    #    fox-foreign anyway.
    SubplotTemplate("""\
{patient_fox_phrase} had been trying to teach {hasty_fox_phrase} how
the REPL works. "Look here," {patient_fox_he_she} said, pointing to
{concept_phrase}. "You hand the form {form_display} to the runtime,
and the runtime hands you back what it evaluates to." {hasty_fox}
agreed, this once, to try."""),

    # 4. The audience template — small orchard creatures watch.
    SubplotTemplate("""\
A small audience of orchard creatures had gathered {place} to watch
{hasty_fox_phrase} attempt to outwit {patient_fox_phrase} at reading
the REPL. {patient_fox} pointed to {concept_phrase} and read the
form aloud: {form_display}. The crowd waited to see who would
correctly write the form to submit."""),

    # 5. The rationalize-and-rebuke template — the canonical fox-grapes
    #    moment. Hasty fox declares the form not worth evaluating
    #    ("probably sour anyway"); patient fox insists on submitting it.
    SubplotTemplate("""\
Halfway across a kitchen garden, {hasty_fox_phrase} stopped {place}
and refused to evaluate the form {form_display} at all — the answer,
{hasty_fox} insisted, was probably sour anyway. {patient_fox_phrase},
padding up at a steady pace, simply said: "Submit {concept_phrase} to
the REPL. Whatever comes back is the honest answer.\""""),

    # 6. The notebook template — patient fox's careful ledger.
    SubplotTemplate("""\
{patient_fox_phrase} had been keeping a small leather notebook of
every form {patient_fox_he_she} had successfully evaluated. Today
{place}, the next entry was {concept_phrase}. {hasty_fox_phrase}
peered over {patient_fox_his_her} shoulder at the form {form_display}
and asked what it would come out to."""),

    # 7. The boast-and-rebuke template — hasty fox dismisses the form
    #    without checking; patient fox insists on actual evaluation.
    #    NOTE: comma before {emo_proud} so participle EMO entries
    #    ("boasting at every turn") parse as adverbial. Object case
    #    {hasty_fox_him_her} for "asked X to actually write".
    SubplotTemplate("""\
"There is no need to evaluate that," {hasty_fox_phrase} said,
{emo_proud}. "The cluster is too high anyway, and {concept_phrase} is
clearly not worth the effort." {patient_fox_phrase}, who {place} had
grown used to such excuses, asked {hasty_fox_him_her} to actually
write the form {form_display} and submit it to the REPL — just to
be sure."""),

    # 8. The puzzle-on-the-gate template — a riddle pinned to an orchard
    #    gate poses the form. Uses {hasty_fox} (the name) instead of
    #    {hasty_fox_him_her} in "called the puzzle ... easy" so gender=n
    #    foxes don't read as plural.
    SubplotTemplate("""\
A wooden sign nailed to an orchard gate {place} carried a puzzle.
The riddle was simple: it asked the reader to evaluate {form_display}.
{hasty_fox} laughed, {emo_proud}, and declared the puzzle far too
easy. {patient_fox} said patiently that the only way to be sure of
{concept_phrase} was to put it in the REPL."""),
]


# Goal-driven mirror of _SHARED_SUBPLOTS: same 8 fox-grapes beats
# (post, wager×3, teacher, audience, rationalize-and-rebuke, ledger,
# boast-and-rebuke, puzzle-on-gate), but uses {goal_text} instead of
# {form_display} so the form is NOT shown — the model translates the
# goal into a Clojure form. Used by abstract subjects (G11-01,
# G12-12, etc.) whose form is a placeholder `(do "..." :studied)` and
# whose narrative carries the lesson.
_GOAL_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The post-and-debate template — goal-driven argument.
    SubplotTemplate("""\
{hasty_fox_phrase} and {patient_fox_phrase} stopped {place} where a
goal had been chalked on a wooden post: to {goal_text}. {hasty_fox},
{emo_proud}, declared {hasty_fox_he_she} could shout the answer
without bothering to write a form. {patient_fox}, {emo_patient},
suggested {hasty_fox_he_she} actually compose {concept_phrase} and
let the REPL confirm what the value really was."""),

    # 2. Wager — dirt.
    SubplotTemplate("""\
{hasty_fox_phrase} sketched a small wager into the dirt {place}:
whoever could compose a Clojure form whose evaluation would
{goal_text} ahead of the other would claim the next cluster of
grapes. {patient_fox_phrase}, {emo_patient}, said it was simpler to
write {concept_phrase} carefully than to guess at the answer."""),

    # 2b. Wager — board.
    SubplotTemplate("""\
{hasty_fox_phrase} chalked a wager on a flat board {place}: whoever
could produce a form whose evaluation would {goal_text} would set
the next ration of fruit. {patient_fox_phrase}, {emo_patient}, said
it would be simpler to write {concept_phrase} carefully than to
bicker over the value."""),

    # 2c. Wager — twig.
    SubplotTemplate("""\
With a twig, {hasty_fox_phrase} marked out a wager {place}: whoever
could write a form to {goal_text} first would win the right to
choose the next vine to inspect. {patient_fox_phrase}, {emo_patient},
said it was easier to compose {concept_phrase} than to argue."""),

    # 3. The teacher template — patient fox teaches goal → form.
    SubplotTemplate("""\
{patient_fox_phrase} had been teaching {hasty_fox_phrase} how to
translate a goal into a Clojure form. "If you want to {goal_text},"
{patient_fox_he_she} said, "you compose {concept_phrase}; submit
that to the REPL, and it hands you back the value." {hasty_fox}
agreed, this once, to try writing it."""),

    # 4. The audience template — orchard creatures watch.
    SubplotTemplate("""\
A small audience of orchard creatures had gathered {place} to watch
{hasty_fox_phrase} attempt to outwit {patient_fox_phrase} at writing
the right form. The challenge: to {goal_text}. {patient_fox} reminded
the crowd that what mattered was composing {concept_phrase} carefully,
then submitting it to the REPL — not guessing at the answer."""),

    # 5. The rationalize-and-rebuke template — canonical Aesop beat.
    SubplotTemplate("""\
Halfway across a kitchen garden, {hasty_fox_phrase} stopped {place}
and refused to write a form for the goal at all — the answer,
{hasty_fox} insisted, was probably sour anyway. {patient_fox_phrase},
padding up at a steady pace, simply said: "To {goal_text}, compose
{concept_phrase}; submit it. Whatever comes back is the honest
answer.\""""),

    # 6. The ledger template — patient fox's record.
    SubplotTemplate("""\
{patient_fox_phrase} had been keeping a small leather notebook of
every goal {patient_fox_he_she} had translated into a Clojure form.
Today {place}, the next entry was a goal: to {goal_text}.
{patient_fox} sat with pen in hand, ready to compose {concept_phrase}
and let the REPL confirm the value."""),

    # 7. The boast-and-rebuke template — hasty fox dismisses; patient
    #    asks for the actual form.
    SubplotTemplate("""\
"There is no challenge here," {hasty_fox_phrase} said, {emo_proud}.
"Anyone could {goal_text} without thinking." {patient_fox_phrase},
who {place} had grown used to such claims, asked {hasty_fox_him_her}
to actually compose {concept_phrase}, then submit it to the REPL —
just to be sure."""),

    # 8. The puzzle-on-the-gate template — sign poses the goal.
    SubplotTemplate("""\
A wooden sign nailed to an orchard gate {place} carried a small
puzzle. The challenge was simple: to {goal_text}. {hasty_fox}
laughed, {emo_proud}, and declared it too easy. {patient_fox} said
patiently that the only way to be sure of the answer was to compose
{concept_phrase} and put it in the REPL."""),
]


_PLAN_POOL: tuple[str, ...] = (
    "I write the form and let the REPL evaluate it.",
    "I submit the form to the REPL via the eval tool.",
    "I let the REPL settle what the form evaluates to.",
    "I write the form rather than guess at the value.",
    "I express the form as Clojure source.",
    "I read the form and submit it directly.",
    "I let the runtime decide what the form evaluates to.",
)


# ─────────────────────── helpers for examples ───────────────────────


def _ex(form, expected, concept, what,
        goal="", scenario="", need="", mapping="", resolution="",
        tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal,
                          scenario=scenario, need=need,
                          mapping=mapping, resolution=resolution,
                          tags=tags)


# ─────────────────────── 18 grade-1 subjects ───────────────────────


# G1-01 — Eval as substitution
G1_01 = SubjectCurriculum(
    grade=1, subject_id="G1-01",
    subject_title="Eval as substitution",
    fable="fox-grapes",
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
        _ex("\"grapes\"",         "grapes","the string \"grapes\"",
            "the value of \"grapes\""),
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
    fable="fox-grapes",
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
    fable="fox-grapes",
    examples=[
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
    fable="fox-grapes",
    examples=[
        _ex('"grapes"',   "grapes",   'the string "grapes"',
            'the value of "grapes"'),
        _ex('"orchard"',  "orchard",  'the string "orchard"',
            'the value of "orchard"'),
        _ex('"too high"', "too high",
            'the string "too high"',
            'the value of "too high"'),
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
    fable="fox-grapes",
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
    fable="fox-grapes",
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


# G1-07 — Keywords
G1_07 = SubjectCurriculum(
    grade=1, subject_id="G1-07",
    subject_title="Keywords",
    fable="fox-grapes",
    examples=[
        _ex(":fox",      ":fox",     "the keyword :fox",
            "the value of :fox"),
        _ex(":grapes",   ":grapes",  "the keyword :grapes",
            "the value of :grapes"),
        _ex(":sour",     ":sour",    "the keyword :sour",
            "the value of :sour"),
        _ex("(keyword? :fox)", True,
            "the predicate (keyword? :fox)",
            "whether :fox is a keyword"),
        _ex("(= :fox :fox)", True,
            "the equality of two :fox keywords",
            "whether :fox equals :fox"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-08 — Characters
G1_08 = SubjectCurriculum(
    grade=1, subject_id="G1-08",
    subject_title="Characters",
    fable="fox-grapes",
    examples=[
        _ex("\\f",      "f",     "the character \\f",
            "the value of \\f"),
        _ex("\\space",  " ",     "the character \\space",
            "the value of \\space"),
        _ex("\\G",      "G",     "the character \\G",
            "the value of \\G"),
        _ex("(char? \\f)", True,
            "the predicate (char? \\f)",
            "whether \\f is a character"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-09 — Symbols vs values
G1_09 = SubjectCurriculum(
    grade=1, subject_id="G1-09",
    subject_title="Symbols vs values",
    fable="fox-grapes",
    examples=[
        _ex("(symbol? 'fox)",
            True,
            'the predicate that asks if a quoted name is a symbol',
            'whether a quoted name is a symbol',
            goal='ask whether a quoted name is a symbol, using the symbol? predicate',
            scenario='Vix the fox had been chalking name-tags onto the vine-posts all morning: each tag a quoted token, each post a real cluster the tag stood for. The chalked tag at the head of the row was a name, written but not yet read by anyone.',
            need='Vix wanted to know whether the chalked tag was the *kind of thing* a name is — a symbol — rather than a number or a string. The predicate would say so.',
            mapping='A quoted token is a symbol — a name standing for something, not the thing itself. The symbol? predicate asks of any value: is this one of those name-tokens? The chalk tag is the symbol; the cluster behind it is what the tag names.',
            resolution='the predicate confirmed what the chalk had drawn — a name, not a value — and Vix moved on to tag the next vine.',
            tags=("story",)),
        _ex("(symbol? 42)", False,
            'the predicate asking if a number is a symbol',
            'whether a bare number is a symbol',
            goal='ask whether a number is a symbol using symbol?',
            scenario='Vix had written the numeral 42 in chalk on a post — not a quoted name, just a tally-mark. She wondered if the chalk-mark itself could ever be a symbol.',
            need='Vix wanted to test whether this bare number held the nature of a name. The predicate would give a yes-or-no answer.',
            mapping='A bare number like 42 is never a symbol — it is itself a value. The symbol? predicate says no for numbers, yes only for quoted names.',
            resolution='the predicate answered no — the tally-mark was a number, not a name-token like a chalk tag.',
            tags=("story",)),
        _ex("'fox", "fox",
            "the quoted symbol fox — a name without evaluation",
            "the value the quoted name fox evaluates to",
            goal='quote the name fox to get a symbol',
            scenario='Sly chalked a name-tag on the post — the word fox, quoted to stand as itself. The chalk-mark was the symbol; behind it lay the real grapes.',
            need='Sly wanted to preserve the name as a symbol, not read what the name stood for. The quote-mark made the difference.',
            mapping='Quoting a name creates a symbol — a name-token that stands for itself rather than what it names. The chalk tag is the symbol; the cluster behind it is the value the symbol refers to.',
            resolution='the quoted name stood on the post — a symbol fox, untouched by the REPL, ready to label the next vine.',
            tags=("story",)),
        _ex("(= 'fox 'fox)", True,
            'the equality test of two quoted symbols',
            'whether two identical quoted names are equal',
            goal='test whether two quoted fox names are equal',
            scenario='Vix found two chalk-marks side by side on a fencepost — each one chalked with the name fox. She wondered if the two tags named the same thing.',
            need='Vix needed a yes-or-no answer: do these two identical chalk-marks stand for the same symbol? The equality test would settle it.',
            mapping='Equality checks whether two symbols are identical — the same name-token. Two chalk tags marked with the same word are the same symbol.',
            resolution='the predicate confirmed yes — both chalk-marks bore the same name, so the two symbols matched exactly.',
            tags=("story",)),
    ],
    subplots=_CHALKMARK_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-10 — Comments
G1_10 = SubjectCurriculum(
    grade=1, subject_id="G1-10",
    subject_title="Comments",
    fable="fox-grapes",
    examples=[
        _ex("(+ 1 2) ; sum of one and two",
            3,
            'an addition form followed by a single-semicolon margin comment',
            'the value of an addition form whose right-margin comment is dropped',
            goal='add 1 and 2, with a single-semicolon trailing comment',
            scenario="Renard the fox wrote a fresh entry in the leather ledger: the day's first tally form, with a thin marginalia note spelling out what the form did.",
            need="Renard wanted the form's value but also wanted the marginalia preserved. The note must not change what the form evaluates to.",
            mapping="A single-semicolon comment is a scribe's marginalia: text the runtime ignores. The semicolon and what follows are dropped before evaluation.",
            resolution='the form returned its honest sum, and the marginalia stayed in the margin — visible to the reader, invisible to the runtime.',
            tags=("story",)),
        _ex("42 ;; the answer", 42,
            'a bare number with a trailing comment',
            'the value of a number whose margin comment is dropped',
            goal='write a number with a trailing comment',
            scenario='Renard jotted the tally 42 in the ledger, then scribbled a margin note: ; the answer. The ink held both.',
            need='Renard wanted the number read and the comment preserved in the margin. The note was for readers, not the runtime.',
            mapping='A double-semicolon comment is marginalia — text dropped before the form evaluates. The semicolon and what follows are invisible to the runtime.',
            resolution='the form returned its honest value, and the marginalia stayed in the margin — readers could see the note, the runtime never knew it was there.',
            tags=("story",)),
    ],
    subplots=_SCRIBE_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-11 — Whitespace
G1_11 = SubjectCurriculum(
    grade=1, subject_id="G1-11",
    subject_title="Whitespace doesn't matter",
    fable="fox-grapes",
    examples=[
        _ex("(+    1    2)", 3,
            'the form with extra spaces inside',
            'the result when spaces between parts do not matter',
            goal='add 1 and 2 with spaces between the parts',
            scenario='Renard scratched the addition form on a slate with gaps between the numbers — extra space after the plus, extra space between the 1 and the 2. The form sprawled across the slate.',
            need='Renard wondered if the REPL could read a form with irregular spacing. Would the extra blanks break the arithmetic?',
            mapping='Whitespace is transparent to the reader — the REPL skips all blank space between parts. The form reads the same whether tightly packed or spread wide.',
            resolution='the REPL read past the gaps and returned the honest sum — spacing was invisible to the evaluator.',
            tags=("story",)),
        _ex("(+\n  1\n  2)", 3,
            'the form with newlines between parts',
            'the result when line breaks between parts do not matter',
            goal='add 1 and 2 with line breaks between the parts',
            scenario='Sly copied the addition form into the ledger — one part per line, indented like a recipe card. The form stretched down the page.',
            need='Sly wanted to know if the REPL would follow the form across line breaks. Did newlines count as a break in the command?',
            mapping='Newlines are whitespace too — the REPL treats them like spaces. A form split across lines reads the same as one written tight.',
            resolution='the REPL read through the newlines and indentation, returning the true sum as if the form had been written on one line.',
            tags=("story",)),
    ],
    subplots=_SCRIBE_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-12 — Parens as syntax
G1_12 = SubjectCurriculum(
    grade=1, subject_id="G1-12",
    subject_title="Parens group; they don't multiply",
    fable="fox-grapes",
    examples=[
        _ex("(+ 2 3)", 5,
            'a simple addition form with parens for grouping',
            'the result of adding 2 and 3 when parens mark the form',
            goal='add 2 and 3 with parens to group the operation',
            scenario='Renard wrote the sum on the ledger page: two clusters plus three more, enclosed in parens to mark where the form begins and ends.',
            need='Renard wanted the REPL to read the parens as grouping symbols, not as multiplying the result. The parens should say "here is a form" — nothing more.',
            mapping='Parentheses in Clojure group a form — they say "evaluate this thing as one unit." They do not multiply; they just mark the boundary.',
            resolution='the REPL read the parens as grouping, computed the sum of two plus three, and returned the total.',
            tags=("story",)),
        _ex("(* (+ 1 2) 3)", 9,
            'a multiplication form with a nested addition',
            'the result of multiplying the sum of 1 and 2 by 3',
            goal='multiply the result of adding 1 and 2 by 3',
            scenario='Vix chalked a nested form on the post: inside the outer parens sat another set, with 1 and 2 to be added first, then the result multiplied by 3. The form nested like boxes.',
            need='Vix wondered if the REPL would follow the nesting — first add the inner numbers, then multiply the outcome. Would the inner parens be evaluated before the outer operation?',
            mapping='Inner parens are evaluated first. The addition inside is a subform; its result becomes the first argument to the multiplication outside.',
            resolution='the REPL read the nested form, added 1 and 2 to get an intermediate, then multiplied that intermediate by 3 to get the final result.',
            tags=("story",)),
    ],
    subplots=_SCRIBE_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-13 — First arithmetic call
# Examples are framed in body-stand + jump-height arithmetic that fits
# fox-grapes' canonical "how high can I reach?" math, but the
# concept_phrase / question_what stay neutral so the same subplots
# render cleanly across all examples.
G1_13 = SubjectCurriculum(
    grade=1, subject_id="G1-13",
    subject_title="First arithmetic call",
    fable="fox-grapes",
    examples=[
        _ex("(+ 1 2)",
            3,
            'the addition of one and two',
            'the running total of one cluster plus two clusters',
            goal='add 1 and 2',
            scenario='Renard the fox had been picking grapes along the trellis all morning, tallying his haul on a small slate. After one vine he had marked one cluster; after the next, two more clusters lay in his vine-tray.',
            need='Now Renard wanted the running total — the count of clusters from the first vine added to the count from the second.',
            mapping="Adding clusters to clusters is what `+` does for numbers: the first vine's count is the first arg, the second vine's count is the second, and the addition form reads off the total. The form names the operation; the REPL does the counting.",
            resolution="the slate's running total stood at one plus two clusters — exactly the haul Renard had laid in the press.",
            tags=("story",)),
        _ex("(- 5 3)", 2,
            'the subtraction of 3 from 5',
            'the difference when 3 clusters are crossed off a slate of 5',
            goal='subtract 3 from 5',
            scenario='Renard had tallied five clusters on a slate that morning. By afternoon, he had given three of those clusters to Sly. On the slate, he crossed out the three marks.',
            need='Now Renard wanted to know the count of clusters that remained on his slate after the three were crossed out.',
            mapping='Subtraction takes a starting count and removes a portion. The first number is what you start with, the second is what leaves. The difference is what stays.',
            resolution='after crossing out the three, the slate showed the remaining clusters — exactly what the difference gave him.',
            tags=("story",)),
        _ex("(* 4 5)", 20,
            'the multiplication of 4 rows by 5 vines per row',
            'the total cluster count in 4 rows of 5 vines each',
            goal='multiply 4 rows by 5 vines per row',
            scenario='Vix stood in the orchard viewing a grid of vines: four rows, each row holding five vines heavy with clusters. She wanted one number for the whole grid.',
            need='Vix needed a count of all the vines in the grid — not row by row, but the whole total. Multiplication would give her the answer.',
            mapping='Multiplication counts equal groups. Four rows times five vines per row means four repeated copies of five — the total number of vines.',
            resolution='the multiplication gave her the count: each of the four rows multiplied by the five vines in each one, all the vines in the grid at once.',
            tags=("story",)),
        _ex("(/ 10 2)", 5,
            'the division of 10 clusters into groups of 2',
            'the number of baskets when 10 clusters are split equally into 2 baskets',
            goal='divide 10 clusters equally into 2 baskets',
            scenario='Sly had picked ten clusters this morning. Now she wanted to split them equally between two baskets — five in each. She asked the REPL to confirm the count per basket.',
            need='Sly needed to know how many clusters went into each basket when ten were split evenly in half.',
            mapping='Division splits a total into equal parts. The first number is the total, the second is the number of parts. The result is how much goes in each part.',
            resolution='the division confirmed her count — ten clusters split evenly into two gave five per basket, just as she had apportioned them.',
            tags=("story",)),
        _ex("(+ 7 8)", 15,
            'the addition of 7 clusters and 8 clusters',
            'the total when seven clusters from one vine are added to eight from another',
            goal='add 7 and 8',
            scenario='Renard gathered seven clusters from the north trellis and eight from the south. He poured both hauls onto a slate and wanted one number for the combined heap.',
            need='Renard wanted the running total — how many clusters lay on his slate once both hauls were added together.',
            mapping="Addition combines two counts into one sum. The first vine's count plus the second vine's count gives the total haul.",
            resolution='the slate showed the combined total — seven plus eight clusters — exactly the full harvest Renard had gathered.',
            tags=("story",)),
        _ex("(- 20 7)", 13,
            'the subtraction of 7 from a count of 20',
            'the remainder when 7 clusters are removed from 20',
            goal='subtract 7 from 20',
            scenario="Renard tallied twenty clusters in his ledger from the morning's work. By evening, he had shared seven with a friend. He crossed off the seven to see what remained.",
            need='Renard wanted to know the count of clusters left after the seven had been given away.',
            mapping='Subtraction removes one count from another. The first number is the starting total, the second is how much is taken away. The result is what is left.',
            resolution='after crossing out the seven, his ledger showed the remaining count — exactly what subtraction had calculated.',
            tags=("story",)),
    ],
    subplots=_ACORN_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-14 — Nested call evaluation
G1_14 = SubjectCurriculum(
    grade=1, subject_id="G1-14",
    subject_title="Nested call evaluation",
    fable="fox-grapes",
    examples=[
        _ex("(+ 1 (* 2 3))", 7,
            'an addition with a nested multiplication',
            'the result when one cluster is added to the product of 2 and 3',
            goal='add 1 to the product of 2 times 3',
            scenario='Renard held one cluster in his left claw. In his right, he held two rows of three clusters each — a nested group he had arranged. He wanted the total across both.',
            need='Renard needed the REPL to first compute the inner multiplication, then add his single cluster to that product.',
            mapping='Nested forms evaluate inside-out. The inner multiplication produces a value, which becomes the second argument to the addition outside.',
            resolution='the REPL computed the product of the nested pair, added the single cluster to it, and returned the total.',
            tags=("story",)),
        _ex("(* (+ 1 2) (+ 3 4))", 21,
            'a multiplication of two nested sums',
            'the product of the sum 1+2 and the sum 3+4',
            goal='multiply the sum of 1 and 2 by the sum of 3 and 4',
            scenario='Vix arranged grapes in two groups: the first group was one cluster plus two more (three total), the second group was three plus four (seven total). She wanted to know the product of these two group-sizes.',
            need='Vix needed both inner sums to be computed first, then their results multiplied together.',
            mapping='Each nested form is evaluated independently, producing a value. The outer multiplication uses those two values as its arguments.',
            resolution='the REPL computed the first sum, computed the second sum separately, then multiplied the two results to give the final total.',
            tags=("story",)),
        _ex("(- 100 (* 5 5))", 75,
            'a subtraction with a nested multiplication',
            'the difference when 5×5 is subtracted from 100',
            goal='subtract the product of 5 times 5 from 100',
            scenario='Sly started with a tally of one hundred clusters on her slate. Then she crossed out a block: five rows of five vines each. She wanted to know what remained.',
            need='Sly needed the REPL to first calculate the inner product, then subtract it from her starting count of one hundred.',
            mapping='The inner multiplication gives a value that becomes the subtracted amount. Subtraction takes the outer first value and removes the nested result.',
            resolution='the REPL computed the inner product, subtracted it from one hundred, and returned what Sly had left on her slate.',
            tags=("story",)),
        _ex("(+ (* 2 3) (* 4 5))", 26,
            'an addition of two nested products',
            'the sum of 2×3 and 4×5',
            goal='add the product 2×3 to the product 4×5',
            scenario='Renard held two blocks of vines: the first block was 2 rows of 3 vines each, the second was 4 rows of 5 vines each. He wanted one number for all the vines in both blocks combined.',
            need='Renard needed both products computed separately, then their results added to give the total vine count across both blocks.',
            mapping='Each nested form is computed to a value. The outer addition uses those two values as its arguments, summing them.',
            resolution='the REPL computed the first product, computed the second product independently, then added both results to give the total.',
            tags=("story",)),
    ],
    subplots=_ACORN_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-15 — Equality
G1_15 = SubjectCurriculum(
    grade=1, subject_id="G1-15",
    subject_title="Equality",
    fable="fox-grapes",
    examples=[
        _ex("(= 1 1)",
            True,
            'the equality test that weighs 1 against 1',
            "whether the equality predicate's pans balance for 1 and 1",
            goal='test whether 1 equals 1 with =',
            scenario="Vix the fox stopped at the orchard's outer gate. The gate bore a single latch this morning, and the latch's catch was a question: would the two pebbles she carried weigh the same?",
            need='She needed a yes-or-no verdict — the latch lifts when the pebbles match, stays shut when they do not. The gate would open or stay closed, nothing in between.',
            mapping="The equality predicate weighs values against each other and reports a verdict. The gate's latch lifts when the pans balance, does not lift when they do not. The verdict is the latch's state, not the pebbles.",
            resolution="the pans balanced, the latch lifted, and the gate swung open — Vix's verdict was the honest one the scale gave her.",
            tags=("story",)),
        _ex("(= 1 2)", False,
            'the equality test of 1 against 2',
            'whether one pebble weighs the same as two',
            goal='test whether 1 equals 2',
            scenario="Vix held one pebble in her left claw and two in her right. She set them on the orchard gate's scale to see if they balanced.",
            need='Vix needed a yes-or-no answer: do these two weights match? The equality test would tip the scale or leave it level.',
            mapping='Equality asks whether two values are identical. The scale tips down on the heavier side; the verdict is no when they do not balance.',
            resolution='the scale tipped — one pebble does not weigh the same as two — and the equality verdict was false.',
            tags=("story",)),
        _ex("(= \"a\" \"a\")", True,
            'the equality test of two identical strings',
            'whether two strings both containing "a" are equal',
            goal='test whether two copies of the string "a" are equal',
            scenario='Renard chalked the letter a on one vine-post, then chalked the same letter a on another post nearby. He wondered if the two chalk-marks stood for the same thing.',
            need='Renard wanted to know if these two identical chalk-letters were truly the same. The equality test would confirm it.',
            mapping='Equality checks whether two strings are identical — same characters in the same order. Two chalk-marks bearing the same letter are the same string.',
            resolution='the predicate confirmed yes — both chalk-marks bore the letter a, so the two strings matched exactly.',
            tags=("story",)),
        _ex("(= :fox :fox)", True,
            'the equality test of two identical keywords',
            'whether two :fox keywords are equal',
            goal='test whether two :fox keywords are the same',
            scenario='Sly hung two tags on the orchard fence: each tag bore the keyword :fox. She asked whether the two tags were truly identical.',
            need='Sly wanted a yes-or-no answer: are these two keyword-tokens the same thing? Equality would settle it.',
            mapping='Equality checks whether two keywords are identical — the same keyword name. Two tags marked :fox are the same keyword.',
            resolution='the equality test confirmed yes — both tags bore the keyword :fox, so they were identical.',
            tags=("story",)),
        _ex("(= :fox :grapes)", False,
            'the equality test of two different keywords',
            'whether :fox and :grapes are the same keyword',
            goal='test whether :fox and :grapes are equal',
            scenario='Vix held two tags side by side: one marked :fox, the other marked :grapes. She wondered if these different keywords could somehow be considered the same.',
            need='Vix wanted the REPL to compare the two distinct keywords. Would they match or differ?',
            mapping='Equality checks whether keywords match. Two different keyword names are never equal — :fox and :grapes are different.',
            resolution='the equality test said no — the two keywords were different, so the verdict was false.',
            tags=("story",)),
        _ex("(= 1 1 1 1)", True,
            'the equality test of four identical numbers',
            'whether all four 1s in the form are equal to each other',
            goal='test whether 1 equals 1 equals 1 equals 1',
            scenario='Renard placed four pebbles on the scale, one at a time — each pebble the same weight, each marked with the number 1. He asked whether all four matched.',
            need='Renard wanted to know if all four pebbles balanced perfectly. The multi-arity equality test would check them all at once.',
            mapping='Equality can test many values at once. All pebbles match means the verdict is yes; if any differ, the verdict is no.',
            resolution='the equality test confirmed that all four pebbles balanced perfectly — each was the same weight, so the verdict was true.',
            tags=("story",)),
    ],
    subplots=_GATE_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-16 — Numeric predicates
G1_16 = SubjectCurriculum(
    grade=1, subject_id="G1-16",
    subject_title="Numeric predicates",
    fable="fox-grapes",
    examples=[
        _ex("(zero? 0)", True,
            'the predicate asking if 0 is zero',
            'whether the number 0 counts as zero',
            goal='ask whether 0 is zero using zero?',
            scenario='Renard had an empty slate — no clusters marked, no tally written. He asked the REPL whether his slate truly held zero.',
            need='Renard wanted to confirm that an empty count was indeed zero. The zero? predicate would say yes or no.',
            mapping='The zero? predicate checks if a number equals zero. Zero on a slate means no clusters at all — the null count.',
            resolution='the predicate confirmed yes — the empty slate was zero, exactly as the REPL determined.',
            tags=("story",)),
        _ex("(zero? 5)", False,
            'the predicate asking if 5 is zero',
            'whether the number 5 counts as zero',
            goal='ask whether 5 is zero using zero?',
            scenario='Vix tallied five clusters on her slate. She wondered aloud if this count of five could somehow be considered zero.',
            need='Vix wanted the zero? predicate to check whether five clusters amounted to nothing at all.',
            mapping='The zero? predicate returns yes only for the number zero itself. Any other count, including 5, is not zero.',
            resolution='the predicate said no — five clusters are definitely not zero.',
            tags=("story",)),
        _ex("(pos? 7)", True,
            'the predicate asking if 7 is positive',
            'whether the number 7 is greater than zero',
            goal='ask whether 7 is positive using pos?',
            scenario='Sly counted seven clusters in her basket. She wondered if this count was positive — more than nothing, a real harvest.',
            need='Sly wanted the pos? predicate to confirm that seven was indeed above zero.',
            mapping='The pos? predicate checks if a number is greater than zero. Seven clusters is a positive count — a real yield.',
            resolution='the predicate confirmed yes — seven is positive, well above the null point.',
            tags=("story",)),
        _ex("(pos? -2)", False,
            'the predicate asking if -2 is positive',
            'whether the number -2 is greater than zero',
            goal='ask whether -2 is positive using pos?',
            scenario='Renard chalked a debt on the ledger: minus two clusters, a count he owed. He wondered if negative two could be called positive.',
            need='Renard asked the pos? predicate whether a negative count could ever be positive.',
            mapping='The pos? predicate checks if a number is greater than zero. Negative numbers are below zero, never positive.',
            resolution='the predicate said no — negative two is not positive.',
            tags=("story",)),
        _ex("(neg? -3)", True,
            'the predicate asking if -3 is negative',
            'whether the number -3 is less than zero',
            goal='ask whether -3 is negative using neg?',
            scenario='Vix recorded a loss in her ledger: minus three clusters, a debt owed. She asked if negative three was indeed a negative number.',
            need='Vix wanted the neg? predicate to confirm that a debt was truly negative.',
            mapping='The neg? predicate checks if a number is less than zero. Minus three is below the null point — a true negative.',
            resolution='the predicate confirmed yes — negative three is indeed negative.',
            tags=("story",)),
        _ex("(neg? 4)", False,
            'the predicate asking if 4 is negative',
            'whether the number 4 is less than zero',
            goal='ask whether 4 is negative using neg?',
            scenario='Sly tallied four clusters as a gain. She wondered aloud if this positive count could somehow be negative.',
            need='Sly asked the neg? predicate whether a gain could ever count as negative.',
            mapping='The neg? predicate returns yes only for numbers less than zero. Four is above zero, never negative.',
            resolution='the predicate said no — four is not negative.',
            tags=("story",)),
    ],
    subplots=_ACORN_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-17 — Printing vs returning
G1_17 = SubjectCurriculum(
    grade=1, subject_id="G1-17",
    subject_title="Printing vs returning",
    fable="fox-grapes",
    examples=[
        _ex("42", 42,
            'a bare number submitted to the REPL',
            'the value the REPL returns when given a bare number',
            goal='submit the number 42 to the REPL and see what it returns',
            scenario='Renard typed 42 at the REPL prompt. The form was just a number — no operation, no parens, nothing to compute.',
            need='Renard wanted to know: would the REPL print the number, return the number, or both? What exactly did the REPL hand back?',
            mapping='The REPL evaluates a bare number to itself and returns that value. Print and return are different — the return is what the REPL hands to the next operation.',
            resolution='the REPL returned the value 42 — that is what it hands to the system, whether it also prints to the screen or not.',
            tags=("story",)),
        _ex("(+ 1 2)", 3,
            'an addition form submitted to the REPL',
            'the value the REPL returns when it evaluates the sum',
            goal='submit the addition form 1+2 to the REPL and see what it returns',
            scenario='Sly typed the addition at the REPL prompt. The form was a complete operation — plus with two arguments — ready to evaluate.',
            need='Sly wanted to know what value the REPL would return once it computed the sum. Print and return are different.',
            mapping='The REPL evaluates a form to a result and returns that value. Print (what appears on screen) is separate from return (what the REPL hands forward).',
            resolution='the REPL returned the computed sum — the value it handed back after evaluation, distinct from anything it may have printed.',
            tags=("story",)),
    ],
    subplots=_SCRIBE_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-18 — Errors are safe in the REPL
G1_18 = SubjectCurriculum(
    grade=1, subject_id="G1-18",
    subject_title="Errors are safe in the REPL",
    fable="fox-grapes",
    examples=[
        _ex("(+ 1 2)",
            3,
            "a clean addition form evaluated under the REPL's safety",
            'the value the catching-cloth lets pass for a clean addition',
            goal='add 1 and 2 — and watch the REPL handle the form safely either way',
            scenario='Sly the fox had strung a catching-cloth between two orchard trees. Whatever fell into the cloth — fruit, twig, surprise — would land softly; nothing splattered on the path.',
            need='Sly wanted to evaluate a form and trust the cloth: if the form raised an error, the cloth would catch it; if it returned a value, the cloth let it pass through to the slate.',
            mapping="The REPL's evaluation runs under the catching-cloth: errors are caught and reported, healthy values pass through. Clean forms simply return their value; bad ones land in the cloth without splattering. The cloth is the REPL's safety; the value is the REPL's report.",
            resolution="the form passed cleanly through the cloth — no error to catch, just the honest sum landing on Sly's slate.",
            tags=("story",)),
        _ex("(* 7 6)", 42,
            'a multiplication form evaluated safely in the REPL',
            'the value the catching-cloth lets pass for a clean multiplication',
            goal='multiply 7 by 6 under the REPL safety net',
            scenario='Sly stretched a catching-cloth between two orchard trees and typed the multiplication form underneath it. Whatever fell into the cloth would land softly.',
            need='Sly wanted to evaluate the form and trust the cloth: if it failed, the cloth caught the error; if it succeeded, the cloth let the value pass.',
            mapping="The REPL's evaluation runs under the catching-cloth: errors are caught, healthy values pass through. Clean forms simply return their result; the cloth is the REPL's safety.",
            resolution="the form evaluated cleanly — no error for the cloth to catch, just the honest product landing on Sly's slate.",
            tags=("story",)),
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
    print(f"grade-1 fox-grapes smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
