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
        _ex("(symbol? 42)",
            False,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox had chalked a tag onto a vine-post — the name, not the cluster behind it.',
            need="Renard wanted to ask the form a question about the tag's nature, not about what the tag named.",
            mapping='`quote` sets a token aside as a name, not a value to evaluate. Symbol predicates ask of any token: is this one of those name-tokens?',
            resolution='the form returned the verdict the predicate had asked of the tag — name or value, drawn cleanly.',
            tags=("story",)),
        _ex("'fox", "fox",
            "the quoted symbol 'fox",
            "the value of 'fox"),
        _ex("(= 'fox 'fox)",
            True,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox had chalked a tag onto a vine-post — the name, not the cluster behind it.',
            need="Vix wanted to ask the form a question about the tag's nature, not about what the tag named.",
            mapping='`quote` sets a token aside as a name, not a value to evaluate. Symbol predicates ask of any token: is this one of those name-tokens?',
            resolution='the form returned the verdict the predicate had asked of the tag — name or value, drawn cleanly.',
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
        _ex("42 ;; the answer",
            42,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox wrote a fresh entry in the leather ledger — marginalia, whitespace, and a form, all set out by scribe's conventions.",
            need="Sly wanted the form's value, with the marginalia preserved for the next reader.",
            mapping='Comments, whitespace, and reader macros are scribe conventions: the runtime ignores them, but the reader uses them for context.',
            resolution='the form returned its honest value, and the marginalia stayed in the ledger margin for the next reader.',
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
        _ex("(+    1    2)",
            3,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox wrote a fresh entry in the leather ledger — marginalia, whitespace, and a form, all set out by scribe's conventions.",
            need="Renard wanted the form's value, with the marginalia preserved for the next reader.",
            mapping='Comments, whitespace, and reader macros are scribe conventions: the runtime ignores them, but the reader uses them for context.',
            resolution='the form returned its honest value, and the marginalia stayed in the ledger margin for the next reader.',
            tags=("story",)),
        _ex("(+\n  1\n  2)",
            3,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox wrote a fresh entry in the leather ledger — marginalia, whitespace, and a form, all set out by scribe's conventions.",
            need="Vix wanted the form's value, with the marginalia preserved for the next reader.",
            mapping='Comments, whitespace, and reader macros are scribe conventions: the runtime ignores them, but the reader uses them for context.',
            resolution='the form returned its honest value, and the marginalia stayed in the ledger margin for the next reader.',
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
        _ex("(+ 2 3)",
            5,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox wrote a fresh entry in the leather ledger — marginalia, whitespace, and a form, all set out by scribe's conventions.",
            need="Sly wanted the form's value, with the marginalia preserved for the next reader.",
            mapping='Comments, whitespace, and reader macros are scribe conventions: the runtime ignores them, but the reader uses them for context.',
            resolution='the form returned its honest value, and the marginalia stayed in the ledger margin for the next reader.',
            tags=("story",)),
        _ex("(* (+ 1 2) 3)",
            9,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox wrote a fresh entry in the leather ledger — marginalia, whitespace, and a form, all set out by scribe's conventions.",
            need="Renard wanted the form's value, with the marginalia preserved for the next reader.",
            mapping='Comments, whitespace, and reader macros are scribe conventions: the runtime ignores them, but the reader uses them for context.',
            resolution='the form returned its honest value, and the marginalia stayed in the ledger margin for the next reader.',
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
        _ex("(- 5 3)",
            2,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox tallied small heaps of clusters on a slate at the press.',
            need="Vix wanted the slate's running total — what the form's arithmetic would produce for that day's heaps.",
            mapping='Arithmetic in Clojure is the slate-tally: the form names the operation, the args are the heaps, and the REPL counts out the result.',
            resolution="the slate held the value the form's tally produced, ready to be posted to the day's harvest log.",
            tags=("story",)),
        _ex("(* 4 5)",
            20,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox tallied small heaps of clusters on a slate at the press.',
            need="Sly wanted the slate's running total — what the form's arithmetic would produce for that day's heaps.",
            mapping='Arithmetic in Clojure is the slate-tally: the form names the operation, the args are the heaps, and the REPL counts out the result.',
            resolution="the slate held the value the form's tally produced, ready to be posted to the day's harvest log.",
            tags=("story",)),
        _ex("(/ 10 2)",
            5,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox tallied small heaps of clusters on a slate at the press.',
            need="Renard wanted the slate's running total — what the form's arithmetic would produce for that day's heaps.",
            mapping='Arithmetic in Clojure is the slate-tally: the form names the operation, the args are the heaps, and the REPL counts out the result.',
            resolution="the slate held the value the form's tally produced, ready to be posted to the day's harvest log.",
            tags=("story",)),
        _ex("(+ 7 8)",
            15,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox tallied small heaps of clusters on a slate at the press.',
            need="Vix wanted the slate's running total — what the form's arithmetic would produce for that day's heaps.",
            mapping='Arithmetic in Clojure is the slate-tally: the form names the operation, the args are the heaps, and the REPL counts out the result.',
            resolution="the slate held the value the form's tally produced, ready to be posted to the day's harvest log.",
            tags=("story",)),
        _ex("(- 20 7)",
            13,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox tallied small heaps of clusters on a slate at the press.',
            need="Sly wanted the slate's running total — what the form's arithmetic would produce for that day's heaps.",
            mapping='Arithmetic in Clojure is the slate-tally: the form names the operation, the args are the heaps, and the REPL counts out the result.',
            resolution="the slate held the value the form's tally produced, ready to be posted to the day's harvest log.",
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
        _ex("(+ 1 (* 2 3))",
            7,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox tallied small heaps of clusters on a slate at the press.',
            need="Renard wanted the slate's running total — what the form's arithmetic would produce for that day's heaps.",
            mapping='Arithmetic in Clojure is the slate-tally: the form names the operation, the args are the heaps, and the REPL counts out the result.',
            resolution="the slate held the value the form's tally produced, ready to be posted to the day's harvest log.",
            tags=("story",)),
        _ex("(* (+ 1 2) (+ 3 4))",
            21,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox tallied small heaps of clusters on a slate at the press.',
            need="Vix wanted the slate's running total — what the form's arithmetic would produce for that day's heaps.",
            mapping='Arithmetic in Clojure is the slate-tally: the form names the operation, the args are the heaps, and the REPL counts out the result.',
            resolution="the slate held the value the form's tally produced, ready to be posted to the day's harvest log.",
            tags=("story",)),
        _ex("(- 100 (* 5 5))",
            75,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox tallied small heaps of clusters on a slate at the press.',
            need="Sly wanted the slate's running total — what the form's arithmetic would produce for that day's heaps.",
            mapping='Arithmetic in Clojure is the slate-tally: the form names the operation, the args are the heaps, and the REPL counts out the result.',
            resolution="the slate held the value the form's tally produced, ready to be posted to the day's harvest log.",
            tags=("story",)),
        _ex("(+ (* 2 3) (* 4 5))",
            26,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox tallied small heaps of clusters on a slate at the press.',
            need="Renard wanted the slate's running total — what the form's arithmetic would produce for that day's heaps.",
            mapping='Arithmetic in Clojure is the slate-tally: the form names the operation, the args are the heaps, and the REPL counts out the result.',
            resolution="the slate held the value the form's tally produced, ready to be posted to the day's harvest log.",
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
        _ex("(= 1 2)",
            False,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox stood at the orchard gate. Its latches lifted only when the form's verdict said so.",
            need="Vix needed the latches' yes-or-no answer for the form's question — open or closed, nothing in between.",
            mapping="Boolean predicates decide the latches' fate. `and` requires every latch lifted; `or` lets either open the gate; the verdict is the latch's state, not the values it weighed.",
            resolution="the latches gave their verdict, and the gate's response matched the form's honest predicate.",
            tags=("story",)),
        _ex("(= \"a\" \"a\")",
            True,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox stood at the orchard gate. Its latches lifted only when the form's verdict said so.",
            need="Sly needed the latches' yes-or-no answer for the form's question — open or closed, nothing in between.",
            mapping="Boolean predicates decide the latches' fate. `and` requires every latch lifted; `or` lets either open the gate; the verdict is the latch's state, not the values it weighed.",
            resolution="the latches gave their verdict, and the gate's response matched the form's honest predicate.",
            tags=("story",)),
        _ex("(= :fox :fox)",
            True,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox stood at the orchard gate. Its latches lifted only when the form's verdict said so.",
            need="Renard needed the latches' yes-or-no answer for the form's question — open or closed, nothing in between.",
            mapping="Boolean predicates decide the latches' fate. `and` requires every latch lifted; `or` lets either open the gate; the verdict is the latch's state, not the values it weighed.",
            resolution="the latches gave their verdict, and the gate's response matched the form's honest predicate.",
            tags=("story",)),
        _ex("(= :fox :grapes)",
            False,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox stood at the orchard gate. Its latches lifted only when the form's verdict said so.",
            need="Vix needed the latches' yes-or-no answer for the form's question — open or closed, nothing in between.",
            mapping="Boolean predicates decide the latches' fate. `and` requires every latch lifted; `or` lets either open the gate; the verdict is the latch's state, not the values it weighed.",
            resolution="the latches gave their verdict, and the gate's response matched the form's honest predicate.",
            tags=("story",)),
        _ex("(= 1 1 1 1)",
            True,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox stood at the orchard gate. Its latches lifted only when the form's verdict said so.",
            need="Sly needed the latches' yes-or-no answer for the form's question — open or closed, nothing in between.",
            mapping="Boolean predicates decide the latches' fate. `and` requires every latch lifted; `or` lets either open the gate; the verdict is the latch's state, not the values it weighed.",
            resolution="the latches gave their verdict, and the gate's response matched the form's honest predicate.",
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
        _ex("(zero? 0)",
            True,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox tallied small heaps of clusters on a slate at the press.',
            need="Renard wanted the slate's running total — what the form's arithmetic would produce for that day's heaps.",
            mapping='Arithmetic in Clojure is the slate-tally: the form names the operation, the args are the heaps, and the REPL counts out the result.',
            resolution="the slate held the value the form's tally produced, ready to be posted to the day's harvest log.",
            tags=("story",)),
        _ex("(zero? 5)",
            False,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox tallied small heaps of clusters on a slate at the press.',
            need="Vix wanted the slate's running total — what the form's arithmetic would produce for that day's heaps.",
            mapping='Arithmetic in Clojure is the slate-tally: the form names the operation, the args are the heaps, and the REPL counts out the result.',
            resolution="the slate held the value the form's tally produced, ready to be posted to the day's harvest log.",
            tags=("story",)),
        _ex("(pos? 7)",
            True,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox tallied small heaps of clusters on a slate at the press.',
            need="Sly wanted the slate's running total — what the form's arithmetic would produce for that day's heaps.",
            mapping='Arithmetic in Clojure is the slate-tally: the form names the operation, the args are the heaps, and the REPL counts out the result.',
            resolution="the slate held the value the form's tally produced, ready to be posted to the day's harvest log.",
            tags=("story",)),
        _ex("(pos? -2)",
            False,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox tallied small heaps of clusters on a slate at the press.',
            need="Renard wanted the slate's running total — what the form's arithmetic would produce for that day's heaps.",
            mapping='Arithmetic in Clojure is the slate-tally: the form names the operation, the args are the heaps, and the REPL counts out the result.',
            resolution="the slate held the value the form's tally produced, ready to be posted to the day's harvest log.",
            tags=("story",)),
        _ex("(neg? -3)",
            True,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox tallied small heaps of clusters on a slate at the press.',
            need="Vix wanted the slate's running total — what the form's arithmetic would produce for that day's heaps.",
            mapping='Arithmetic in Clojure is the slate-tally: the form names the operation, the args are the heaps, and the REPL counts out the result.',
            resolution="the slate held the value the form's tally produced, ready to be posted to the day's harvest log.",
            tags=("story",)),
        _ex("(neg? 4)",
            False,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox tallied small heaps of clusters on a slate at the press.',
            need="Sly wanted the slate's running total — what the form's arithmetic would produce for that day's heaps.",
            mapping='Arithmetic in Clojure is the slate-tally: the form names the operation, the args are the heaps, and the REPL counts out the result.',
            resolution="the slate held the value the form's tally produced, ready to be posted to the day's harvest log.",
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
        _ex("42",
            42,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox wrote a fresh entry in the leather ledger — marginalia, whitespace, and a form, all set out by scribe's conventions.",
            need="Renard wanted the form's value, with the marginalia preserved for the next reader.",
            mapping='Comments, whitespace, and reader macros are scribe conventions: the runtime ignores them, but the reader uses them for context.',
            resolution='the form returned its honest value, and the marginalia stayed in the ledger margin for the next reader.',
            tags=("story",)),
        _ex("(+ 1 2)",
            3,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox wrote a fresh entry in the leather ledger — marginalia, whitespace, and a form, all set out by scribe's conventions.",
            need="Vix wanted the form's value, with the marginalia preserved for the next reader.",
            mapping='Comments, whitespace, and reader macros are scribe conventions: the runtime ignores them, but the reader uses them for context.',
            resolution='the form returned its honest value, and the marginalia stayed in the ledger margin for the next reader.',
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
        _ex("(* 7 6)",
            42,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox had strung a catching-cloth between two orchard trees.',
            need='Sly wanted to evaluate a form and trust the cloth: errors caught, healthy values passed through.',
            mapping="`try`/`catch` is the catching-cloth: errors thrown are caught by the form's catch-clause, while healthy values pass through unchanged.",
            resolution="the form passed through the cloth — caught if it threw, returned if it didn't — and the slate held whatever came out.",
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
