"""Grade 1 — atoms + first eval, taught through the Tortoise-and-Hare fable.

Each subject defines:
  - examples: a list of Clojure exercises (form + expected + concept_phrase)
  - subplots: 6+ narrative templates that wrap any example in fable scenery
  - plan_pool: optional plan-only prefaces (never reveal the answer)

Coverage per subject (per fable):
   examples × narrative variants ≈ 5-15 × 200-2000 distinct records.

The fable's moral dynamic — vanity vs. steadiness — informs the
characters' attitudes toward each form: Hare is the boastful, hasty
guesser; Tortoise is the patient evaluator. Subjects bring this out
differently (e.g., G1-15 equality is an argument the two settle by
reading the form; G1-13 first-arithmetic is a wager about the answer).
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.tortoise_hare._metaphor_pools import (
    _ACORN_SUBPLOTS, _CHALKMARK_SUBPLOTS, _GATE_SUBPLOTS, _SAFETYNET_SUBPLOTS, _SCRIBE_SUBPLOTS,
)


# ─────────────────────── shared subplot pool ───────────────────────
#
# These 8 templates work across most grade-1 subjects. Each subject
# either uses this pool directly or extends it with subject-specific
# templates (e.g., G1-15 equality has its own "argument" templates).
#
# Templates use `{form_display}` for the literal form being evaluated,
# `{concept_phrase}` for the noun-phrase ("the value 42"), and
# fable placeholders for character/location/emotion variation.

_SHARED_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The argument template — Hare boasts an answer, Tortoise insists
    #    they evaluate it carefully. The student writes the form.
    SubplotTemplate("""\
{hare_phrase} and {tortoise_phrase} stopped {place} where someone had
written {concept_phrase} on a flat stone. {hare}, {emo_proud}, declared
that {hare_he_she} could see the answer at a glance. {tortoise},
{emo_patient}, suggested they actually evaluate the form {form_display}
in the REPL and read off whatever it returned."""),

    # 2. The wager template — bets on what the form returns.
    #    Three near-equivalent variants of the wager-setup line, picked
    #    so the same wager-template doesn't always read as "drew a wager
    #    in the dust" verbatim (cosmetic variety).
    SubplotTemplate("""\
At a moss-covered milestone {place}, {hare_phrase} sketched a small
wager into the path: whoever guessed the result of {form_display}
first would win the right to set the next race. {tortoise_phrase},
{emo_patient}, said it was simpler to type the form into the REPL
than to argue about {concept_phrase}."""),

    # 2b. wager variant — chalk on stone
    SubplotTemplate("""\
{hare_phrase} chalked a wager on a flat stone {place}: whoever
predicted the result of {form_display} would set the next race's
distance. {tortoise_phrase}, {emo_patient}, said it would be simpler
to type the form into the REPL than to bicker about {concept_phrase}."""),

    # 2c. wager variant — twig in the path
    SubplotTemplate("""\
With a twig, {hare_phrase} marked out a wager {place}: whoever
guessed the result of {form_display} first would win the right to
choose the next contest. {tortoise_phrase}, {emo_patient}, said it
was easier to ask the REPL about {concept_phrase} than to argue."""),

    # 3. The teacher template — Tortoise is gently correcting Hare.
    #    NOTE: drops the "from a recent sprint" tail because EMO_TIRED
    #    entries already supply their own "from X" clause; doubling
    #    produced "from sprinting from a recent sprint" awkwardness.
    SubplotTemplate("""\
{tortoise_phrase} had been trying to teach {hare_phrase} how the REPL
works. "Look here," {tortoise_he_she} said, pointing to
{concept_phrase}. "You hand the form {form_display} to the runtime, and
the runtime hands you back what it evaluates to." {hare}, {emo_tired},
agreed to try."""),

    # 4. The audience template — small forest creatures watch and learn.
    #    NOTE: rewritten so {concept_phrase} is referenced via "pointed to"
    #    rather than "read aloud" — abstract concept_phrases like "the
    #    equality (= 1 1)" / "the predicate (zero? 0)" don't fit
    #    "read aloud" semantically (you read FORMS aloud, not types).
    SubplotTemplate("""\
A small audience of forest creatures had gathered {place} to watch
{hare_phrase} attempt to outwit {tortoise_phrase} at reading the REPL.
{tortoise}, {emo_patient}, pointed to {concept_phrase} and read out the
form aloud: {form_display}. The crowd waited to see who would correctly
write the form to submit."""),

    # 5. The race-pause template — hare pauses mid-race, tortoise catches up
    #    via careful evaluation.
    #    NOTE: uses {hare} (the name) instead of {hare_he_she_cap} for the
    #    "called it impossible" sentence — for gender="n" characters,
    #    "They called it impossible." reads as plural-subject right after
    #    a singular "Pip the hare stopped" introduction.
    SubplotTemplate("""\
Halfway through the race, {hare_phrase}, {emo_proud}, stopped {place}
and refused to continue until someone could prove what the form
{form_display} evaluated to. {hare} called it impossible.
{tortoise_phrase}, walking up at her usual pace, simply said: "Submit
{concept_phrase} to the REPL. Whatever comes back is the answer.\""""),

    # 6. The notebook template — the tortoise keeps a careful ledger.
    SubplotTemplate("""\
{tortoise_phrase}, {emo_patient}, had been keeping a small leather
notebook of every form {tortoise_he_she} had successfully evaluated.
{place_idx}, the next entry was {concept_phrase}. {hare_phrase} peered
over {tortoise_his_her} shoulder at the form {form_display} and asked
what it would come out to.""".replace("{place_idx}", "Today {place}")),

    # 7. The boast-and-rebuke template — Hare claims to know without checking.
    #    NOTE: uses {hare_him_her} (object case) for "asked X to ..."; uses
    #    comma after "said" so participle-phrase EMO_PROUD entries
    #    ("boasting at every turn", "swaggering through the underbrush")
    #    parse as adverbial — without the comma, "said boasting" reads
    #    as agrammatical.
    SubplotTemplate("""\
"There is no need to evaluate that," {hare_phrase} said, {emo_proud}.
"Anyone can see what {concept_phrase} comes to." {tortoise_phrase}, who
{place} had grown used to such claims, asked {hare_him_her} to actually
write the form {form_display} and submit it to the REPL — just to be
sure."""),

    # 8. The puzzle-on-the-path template — they find a riddle on a sign.
    SubplotTemplate("""\
A wooden sign nailed to a tree {place} carried a puzzle. The riddle
was simple: it asked the reader to evaluate {form_display}. {hare}
laughed, {emo_proud}, and declared it too easy. {tortoise} said
patiently that the only way to be sure of {concept_phrase} was to put
it in the REPL."""),
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


# ─────────────────────── goal-style subplots ───────────────────────
#
# Used by NON-ATOM subjects (G1-09 onward + G2..G12). These templates
# describe the GOAL of the form ({goal_text}) and reference the
# operation abstractly via {concept_phrase}, but NEVER show the literal
# form. The model must produce the form from the goal — it cannot
# copy-from-prompt because the form isn't there.
#
# Atom subjects (G1-01..08) keep using _SHARED_SUBPLOTS, which DO show
# the form via {form_display}, because for atoms the form IS the
# answer (a literal evaluates to itself); copying-it-out IS the lesson.
_GOAL_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The argument template — characters debate; goal-driven.
    #    Fix: comma after concept_phrase to break "and" stutter when
    #    concept_phrase ends in "and"/"or"/"not".
    SubplotTemplate("""\
{hare_phrase} and {tortoise_phrase} stopped {place} to settle a small
puzzle. {hare} wanted to {goal_text}. {hare}, {emo_proud}, declared
that {hare_he_she} could write the form for it without thinking.
{tortoise}, {emo_patient}, suggested {hare_he_she} actually write
{concept_phrase} carefully — and then let the REPL confirm what
the value really was."""),

    # 2. The wager template — bet on writing the right form.
    #    Fix: drop "write a form to" verb-on-verb collision; use
    #    "produce a form whose evaluation would" (noun-clause framing).
    SubplotTemplate("""\
At a moss-covered milestone {place}, {hare_phrase} sketched a small
wager into the path: whoever could produce a form whose evaluation
would {goal_text} ahead of the other would win the right to set
the next race. {tortoise_phrase}, {emo_patient}, said it was
simpler to write {concept_phrase} carefully than to guess at the
answer."""),

    # 3. The teacher template — Tortoise teaches goal → form.
    #    Fix: "; submit that to the REPL" instead of "and submit it".
    SubplotTemplate("""\
{tortoise_phrase} had been teaching {hare_phrase} how to translate a
goal into a Clojure form. "If you want to {goal_text}," {tortoise_he_she}
said, "you write {concept_phrase}; submit that to the REPL, and it
hands you back the value." {hare}, {emo_tired}, agreed to try
writing it."""),

    # 4. The audience template — onlookers wait to see the form written.
    SubplotTemplate("""\
A small audience of forest creatures had gathered {place} to watch
{hare_phrase} attempt to outwit {tortoise_phrase} at writing the
right form. The challenge: {goal_text}. {tortoise}, {emo_patient},
reminded the crowd that what mattered was writing {concept_phrase}
carefully, then submitting it to the REPL — not guessing aloud at
the answer."""),

    # 5. The race-pause template — pause mid-race for a goal-write.
    #    Fix: drop "write a form to {goal_text}"; reframe as
    #    "until someone could {goal_text} with a Clojure form".
    SubplotTemplate("""\
Halfway through the race, {hare_phrase}, {emo_proud}, stopped {place}
and refused to continue until someone could {goal_text} with a Clojure
form. {hare} called the goal impossible. {tortoise_phrase}, walking up
at {tortoise_his_her} usual pace, simply said: "Compose
{concept_phrase}; submit it. Whatever comes back is the answer.\""""),

    # 6. The notebook template — Tortoise records goal/form pairs.
    SubplotTemplate("""\
{tortoise_phrase}, {emo_patient}, kept a small leather notebook of
every goal {tortoise_he_she} had translated into a Clojure form.
Today {place}, the next entry was a goal: {goal_text}. {tortoise} sat
with pen in hand, ready to compose {concept_phrase}, then let the
REPL confirm the value."""),

    # 7. The boast-and-rebuke template — Hare boasts; Tortoise asks
    #    for the actual form. Fix: "To X is something anyone could
    #    write" → "anyone could do that" (drops verb-collision when
    #    goal_text starts with a "write/compose" verb).
    SubplotTemplate("""\
"There is no challenge here," {hare_phrase} said, {emo_proud}.
"Anyone could {goal_text} without thinking." {tortoise_phrase},
who {place} had grown used to such claims, asked {hare_him_her} to
actually write {concept_phrase}, then submit it to the REPL —
just to be sure."""),

    # 8. The puzzle-on-the-path template — a sign poses the goal.
    SubplotTemplate("""\
A wooden sign nailed to a tree {place} carried a small puzzle. The
challenge was simple: {goal_text}. {hare} laughed, {emo_proud}, and
declared it too easy. {tortoise} said patiently that the only way
to be sure of {concept_phrase} was to write the form and put it
in the REPL — not to guess at the value from the goal alone."""),

    # 9. The Hare-stumbles template — Hare's hurry betrays him; the
    #    Tortoise's careful form returns the value first. Delivers
    #    the fable's moral (vanity vs. steadiness) directly.
    SubplotTemplate("""\
"This is nothing," {hare_phrase} scoffed, {emo_proud}. "I can
{goal_text} in my sleep." {hare} grabbed a stick and dashed off a
few characters in the dust — but a paren went missing, an operand
fell out of place, and the form did not even read as Clojure.
{tortoise_phrase}, {emo_patient}, had already written
{concept_phrase} on a flat stone, neat and unhurried, and
submitted it to the REPL. The value came back as quietly as
{tortoise_he_she} had written. The hares of the meadow looked
between the two slates: only {tortoise_his_her} had run."""),

    # 10. The race-against-the-REPL template — wager on speed-of-
    #     answering, Tortoise's careful path wins. Moral lands.
    SubplotTemplate("""\
The wager was set {place}: produce the value before the breeze had
turned the next leaf. {hare_phrase}, {emo_proud}, bolted into a flurry
of guesses. {hare_he_she_cap} called out numbers and second-guessed
{hare_him_her}self about whether the goal was to {goal_text}.
{tortoise_phrase}, {emo_patient}, simply walked to the slate.
{tortoise_he_she_cap} wrote {concept_phrase} and finished the form.
The REPL handed back the value while {hare} was still arguing with
the breeze. The race went to the steady hand."""),

    # 11. The wrong-guess-then-form template — Hare blurts a guess at
    #     the answer (deliberately abstract — no actual value leaks),
    #     Tortoise patiently writes the form. The point: the form
    #     beats the guess.
    SubplotTemplate("""\
{hare_phrase} squinted at the goal — to {goal_text} — and blurted
out a confident guess, {emo_proud}, as though loudness were the
same as correctness. {tortoise_phrase} did not argue.
{tortoise_he_she_cap} simply wrote {concept_phrase} on the path,
submitted it to the REPL, and held up the value the runtime
returned. The crowd compared the two, and the hare's guess was
found wanting against the form that had actually run."""),

    # 12. The patient-explanation template — Tortoise teaches, Hare
    #     resists, the lesson takes hold by the end. Slower beat,
    #     longer narrative; lets the moral breathe.
    SubplotTemplate("""\
"You always insist on writing it out," {hare_phrase} complained,
{emo_proud}. "I can see the answer from here." {tortoise_phrase}
shook {tortoise_his_her} head slowly. "To {goal_text}, the eye is
no help — only the form is. Watch." {tortoise_he_she_cap} wrote
{concept_phrase} in careful strokes, submitted it to the REPL,
and let the returned value speak for itself. {hare}, {emo_tired},
admitted that this time, again, the patient way had carried the
day."""),
]


# ─────────────────────── helpers for examples ───────────────────────


def _ex(form: str, expected, concept: str, what: str,
        goal: str = "",
        tags: tuple[str, ...] = ()) -> SubjectExample:
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal, tags=tags)


# ─────────────────────── 18 grade-1 subjects ───────────────────────


# G1-01 — Eval as substitution. ATOM SUBJECT: form IS the answer; the
# lesson is "values evaluate to themselves." Trimmed application
# examples — those live in G1-13 (first arithmetic) and G1-14 (nested).
G1_01 = SubjectCurriculum(
    grade=1, subject_id="G1-01",
    subject_title="Eval as substitution",
    fable="tortoise-hare",
    examples=[
        _ex("42",                  42,    "the value 42",
            "the value of 42"),
        _ex("0",                   0,     "the value 0",
            "the value of 0"),
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
    fable="tortoise-hare",
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
    fable="tortoise-hare",
    examples=[
        # Note: ratios like 1/2 evaluate to themselves in Clojure (exact rational).
        # In Python expected we represent as the form string since basilisp's
        # eval result is the canonical ratio. For training, the model writes
        # the literal form and the runtime reproduces it.
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
    fable="tortoise-hare",
    examples=[
        _ex('"hello"',    "hello",    'the string "hello"',
            'the value of "hello"'),
        _ex('"race"',     "race",     'the string "race"',
            'the value of "race"'),
        _ex('"slow and steady"', "slow and steady",
            'the string "slow and steady"',
            'the value of "slow and steady"'),
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
    fable="tortoise-hare",
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
    fable="tortoise-hare",
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
    fable="tortoise-hare",
    examples=[
        _ex(":hare",    ":hare",    "the keyword :hare",
            "the value of :hare"),
        _ex(":tortoise",":tortoise", "the keyword :tortoise",
            "the value of :tortoise"),
        _ex(":winner",   ":winner", "the keyword :winner",
            "the value of :winner"),
        _ex("(keyword? :hare)", True,
            "the predicate (keyword? :hare)",
            "whether :hare is a keyword"),
        _ex("(= :hare :hare)", True,
            "the equality of two :hare keywords",
            "whether :hare equals :hare"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-08 — Characters
G1_08 = SubjectCurriculum(
    grade=1, subject_id="G1-08",
    subject_title="Characters",
    fable="tortoise-hare",
    examples=[
        _ex("\\h",      "h",     "the character \\h",
            "the value of \\h"),
        _ex("\\space",  " ",     "the character \\space",
            "the value of \\space"),
        _ex("\\T",      "T",     "the character \\T",
            "the value of \\T"),
        _ex("(char? \\h)", True,
            "the predicate (char? \\h)",
            "whether \\h is a character"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-09 — Symbols vs values
# (NON-ATOM: uses _GOAL_SUBPLOTS — model writes the form from the goal.)
G1_09 = SubjectCurriculum(
    grade=1, subject_id="G1-09",
    subject_title="Symbols vs values",
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(symbol? 'hare)",
            expected=True,
            concept_phrase="the symbol-predicate on a quoted name",
            question_what="whether a quoted name is a symbol",
            goal_text="ask whether a quoted name is a symbol, using the symbol? predicate",
            scenario=(
                "Mossback the tortoise scratched a chalk mark across a "
                "piece of bark — the name 'hare — and pointed first at "
                "the chalk mark, then at the actual bounding hare "
                "itself."
            ),
            need=(
                "She wanted to show that the chalk mark and the bounding "
                "hare are different kinds of thing — and to ask the "
                "runtime which kind the chalk mark itself was."
            ),
            mapping=(
                "Quoting (with the leading apostrophe) labels a name as "
                "a name — a symbol — rather than evaluating it. "
                "`symbol?` then asks the runtime: is this thing a "
                "chalk-mark-of-a-name?"
            ),
            resolution=(
                "the runtime confirmed: 'hare is indeed a symbol, a "
                "name and not the bounding thing the name might refer "
                "to. true came back."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(symbol? 42)",
            expected=False,
            concept_phrase="the symbol-predicate on an integer",
            question_what="whether an integer is a symbol",
            goal_text="ask whether the integer 42 is a symbol, using the symbol? predicate",
            scenario=(
                "Pip the hare picked up a stone with the number {drawn.a} scratched into it and held it beside a bark-strip labelled 'count. Shelly the tortoise needed to know which of the two was a name and which was a value."
            ),
            need=(
                "Without asking the runtime, the two risked arguing all "
                "afternoon — the stone needed to be tested, not debated."
            ),
            mapping=(
                "`symbol?` tests whether the runtime sees a chalk-mark "
                "name or the actual value it might stand for. An integer "
                "is a value — never a name — so the predicate returns "
                "the falsey verdict."
            ),
            resolution=(
                'the runtime confirmed that {drawn.a} is not a symbol: the integer is a value, not a name scratched on bark.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(symbol? "tortoise")',
            expected=False,
            concept_phrase="the symbol-predicate on a string",
            question_what="whether a string is a symbol",
            goal_text="ask whether a string of letters is a symbol, using the symbol? predicate",
            scenario=(
                'Mossback had laid two things side by side on a flat stone: a chalk mark that read \'{drawn.a}, and a piece of bark bearing the word "{drawn.a}" pressed in ink — a proper string, not a symbol.'
            ),
            need=(
                "She needed the runtime to settle which kind each was, "
                "because the two look alike to the eye yet behave "
                "entirely differently under evaluation."
            ),
            mapping=(
                "A string in double quotes is a value — a sequence of "
                "characters — not a name. `symbol?` checks for the "
                "chalk-mark kind; a string returns the falsey answer."
            ),
            resolution=(
                "the runtime distinguished them cleanly: the string was "
                "not a symbol, so the falsey verdict came back."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(= 'hare 'hare)",
            expected=True,
            concept_phrase="the equality of two quoted names",
            question_what="whether two quoted names are equal",
            goal_text="compare two quoted names for equality, using the = predicate",
            scenario=(
                "Mossback had chalk-marked the name 'hare on two "
                "separate pieces of bark. Pip insisted the two marks "
                "were the same name; Hopper the hare said they might "
                "not be, since each came from a different piece of bark."
            ),
            need=(
                "The argument could only be settled by asking the "
                "runtime whether the two chalk-marked names were equal "
                "— eye-reading alone was not enough."
            ),
            mapping=(
                "Quoting preserves both as symbols — names — rather "
                "than trying to look them up. `=` then tests whether "
                "the two names are the same name."
            ),
            resolution=(
                "the runtime confirmed that the two quoted names are "
                "identical, so the truthy verdict came back."
            ),
            tags=("story",),
        ),
    ],
    subplots=_CHALKMARK_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-10 — Comments
G1_10 = SubjectCurriculum(
    grade=1, subject_id="G1-10",
    subject_title="Comments",
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(+ 1 2) ; sum of one and two",
            expected=3,
            concept_phrase="the addition with a trailing comment",
            question_what="the result, ignoring the comment",
            goal_text="add 1 and 2, with a single-semicolon trailing comment",
            scenario=(
                "Slowpoke the tortoise had scratched an addition on "
                "the trail-stone and, beside it, added a small note "
                "after a semicolon explaining what the form computed — "
                "a scribe's marginal gloss. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "Pip the hare needed to know what the form returned, "
                "not what the note said — the note was for the reader, "
                "not the runtime."
            ),
            mapping=(
                "The scribe's convention: everything after a semicolon "
                "on the same line is a comment — the runtime skips it "
                "entirely and evaluates only what comes before."
            ),
            resolution=(
                "the runtime skipped the note and returned the sum of "
                "the two numbers, just as the form before the semicolon "
                "asked."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="42 ;; the answer",
            expected=42,
            concept_phrase="the literal with a trailing comment",
            question_what="the literal value, ignoring the comment",
            goal_text="submit the integer 42 with a double-semicolon trailing comment",
            scenario=(
                "Mossback had etched a number on a flat stone and "
                "after a double semicolon had written a scribe's "
                "note naming what the number meant — a second style "
                "of marginal annotation the scribe used for emphasis. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Bramble the hare needed the value the runtime would "
                "hand back, separate from the annotation the scribe "
                "had left alongside it."
            ),
            mapping=(
                "A double semicolon works the same way as a single "
                "one: both mark the start of a comment the runtime "
                "ignores. Only the token before the double semicolon "
                "is evaluated."
            ),
            resolution=(
                "the runtime ignored the annotation and returned the "
                "integer the stone had been etched with."
            ),
            tags=("story",),
        ),
    ],
    subplots=_SCRIBE_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-11 — Whitespace
G1_11 = SubjectCurriculum(
    grade=1, subject_id="G1-11",
    subject_title="Whitespace doesn't matter",
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(+    1    2)",
            expected=3,
            concept_phrase="the addition with extra spacing",
            question_what="the result of an addition formatted with extra spaces",
            goal_text="add 1 and 2 in a form with extra spaces between tokens",
            scenario=(
                "Pip the hare had written an addition on the path-stone "
                "with wide gaps between the tokens — extra spaces where "
                "the chalk had skipped. Mossback looked it over and "
                "said the form was still readable. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "Pip needed to know whether the extra whitespace changed "
                "what the runtime would compute or whether spacing was "
                "invisible to the scribe."
            ),
            mapping=(
                "The scribe reads tokens, not gaps. Extra spaces between "
                "operator and arguments are ignored; the runtime sees "
                "the same addition regardless of how much air sits "
                "between the marks."
            ),
            resolution=(
                "the runtime returned the same sum as if the tokens had "
                "been written with a single space each — the gaps had "
                "changed nothing."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(+\n  1\n  2)",
            expected=3,
            concept_phrase="the addition split across lines",
            question_what="the result of an addition formatted across multiple lines",
            goal_text="add 1 and 2 in a form whose arguments are on separate lines",
            scenario=(
                "Shelly the tortoise had written a form across three "
                "lines on a broad leaf — the operator on the first, "
                "each argument indented on its own line below. Hopper "
                "the hare wondered whether the line-breaks would confuse "
                "the reader. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "Hopper needed to know whether the runtime read forms "
                "line by line or saw through the newlines just as it "
                "saw through extra spaces."
            ),
            mapping=(
                "The scribe treats a newline the same as a space: it "
                "separates tokens but carries no meaning. The runtime "
                "sees the same three-token call no matter how many "
                "lines the form spans."
            ),
            resolution=(
                "the runtime returned the sum of the two numbers — the "
                "line-breaks had not altered the form's meaning at all."
            ),
            tags=("story",),
        ),
    ],
    subplots=_SCRIBE_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-12 — Parens group; they don't multiply
G1_12 = SubjectCurriculum(
    grade=1, subject_id="G1-12",
    subject_title="Parens group; they don't multiply",
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(+ 2 3)",
            expected=5,
            concept_phrase="the simple addition",
            question_what="the result of adding 2 and 3",
            goal_text="add 2 and 3",
            scenario=(
                'Mossback the tortoise chalked a small expression on the path: the plus-mark, then {drawn.a}, then {drawn.b}, all wrapped in a single set of parens. Pip the hare paused — was the answer 6 (parens means multiply, surely?), or maybe 23?'
            ),
            need=(
                "Mossback wanted to show that the parens are fence-posts, "
                "not multiplication: they mark which tokens belong "
                "together as one form, nothing more."
            ),
            mapping=(
                'Parens in Clojure group: the first token inside is the operator (`+`), the rest are arguments ({drawn.a}, {drawn.b}). The runtime applies + to {drawn.a} and {drawn.b} — the parens themselves do no math.'
            ),
            resolution=(
                'the runtime applied + to {drawn.a} and {drawn.b} and returned the result — not 6, not 23, just the sum the form had asked for.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* (+ 1 2) 3)",
            expected=9,
            concept_phrase="the nested multiplication",
            question_what="the result of multiplying a nested sum by 3",
            goal_text="multiply the sum of 1 and 2 by 3",
            scenario=(
                'Mossback chalked two nested fences on the path: an inner fence holding the plus-mark, {drawn.a}, and {drawn.b}, and an outer fence holding the star-mark, the inner fence, and 3. Pip counted the parens and declared the result must be enormous.'
            ),
            need=(
                "Mossback needed to show that each set of parens is "
                "its own fence-post group — the inner one resolves "
                "first, then the outer one takes that result as its "
                "argument."
            ),
            mapping=(
                'Inner parens group first: `(+ {drawn.a} {drawn.b})` resolves to its sum. The outer parens then group `*`, that sum, and {drawn.c} — multiplying them together. The fence-posts mark order, not multiplication.'
            ),
            resolution=(
                "the runtime resolved the inner group first, then "
                "applied the outer operator, returning the final "
                "product — exactly what the nested fences prescribed."
            ),
            tags=("story",),
        ),
    ],
    subplots=_SCRIBE_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-13 — First arithmetic call
G1_13 = SubjectCurriculum(
    grade=1, subject_id="G1-13",
    subject_title="First arithmetic call",
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(+ 1 2)",
            expected=3,
            concept_phrase="the addition",
            question_what="the sum of 1 and 2",
            goal_text="add 1 and 2",
            scenario=(
                "Mossback had sorted this morning's acorns into two small heaps beside the trail — one heap of {drawn.a} and another of 2."
            ),
            need=(
                "She needed the running total before deciding whether "
                "to carry them all or leave some behind."
            ),
            mapping=(
                "`+` is the counting-together operator: the two heap "
                "sizes are its arguments, and the runtime combines "
                "them into a single count."
            ),
            resolution=(
                "the runtime returned the combined count — the two "
                "heaps tallied into one."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(- 5 3)",
            expected=2,
            concept_phrase="the subtraction",
            question_what="the difference of 5 and 3",
            goal_text="subtract 3 from 5",
            scenario=(
                'Pip the hare had counted {drawn.a} acorns set aside for the midday rest. Hopper had already taken {drawn.b} to his side of the log before Pip noticed.'
            ),
            need=(
                "Pip needed to know how many remained so he could "
                "decide whether the rest was worth stopping for."
            ),
            mapping=(
                "`-` takes the starting heap and removes the given "
                "count; the result is what remains after the "
                "subtraction."
            ),
            resolution=(
                "the runtime returned the remainder — the acorns left "
                "after Hopper's share had been removed."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 4 5)",
            expected=20,
            concept_phrase="the multiplication",
            question_what="the product of 4 and 5",
            goal_text="multiply 4 by 5",
            scenario=(
                "Shelly the tortoise had arranged her acorn-gathering in {drawn.a} equal rows of {drawn.b} acorns each along the meadow's edge, each row the same size."
            ),
            need=(
                "She needed the full count of acorns without adding "
                "row by row — the repeated-addition shortcut was the "
                "quickest path."
            ),
            mapping=(
                '`*` computes the repeated sum: {drawn.a} rows of {drawn.b} is the same as adding {drawn.b} four times. The runtime returns that total directly.'
            ),
            resolution=(
                "the runtime returned the total count across all "
                "rows — the full morning's harvest in one number."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(/ 10 2)",
            expected=5,
            concept_phrase="the division",
            question_what="the quotient of 10 and 2",
            goal_text="divide 10 by 2",
            scenario=(
                'Mossback and Pip had gathered a shared heap of {drawn.a} acorns. They agreed to split the heap into {drawn.b} equal shares, one for each of them.'
            ),
            need=(
                "Mossback needed to know exactly how many acorns each "
                "share would hold so the split was fair."
            ),
            mapping=(
                "`/` divides the heap into equal portions: the "
                "dividend is the total heap, the divisor is the number "
                "of shares, and the runtime returns each share's size."
            ),
            resolution=(
                "the runtime returned each share's count — the heap "
                "divided cleanly between the two."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(+ 7 8)",
            expected=15,
            concept_phrase="the addition",
            question_what="the sum of 7 and 8",
            goal_text="add 7 and 8",
            scenario=(
                'Bramble the hare had counted {drawn.a} acorns beneath the oak and {drawn.b} more under the elm. Both heaps sat in separate leaf-cups at the edge of the path.'
            ),
            need=(
                "Bramble needed the combined count to report back to "
                "Shelly, who was tallying the morning's whole haul."
            ),
            mapping=(
                "`+` combines the two heap sizes into a single total; "
                "each argument is one leaf-cup's count, and the "
                "runtime adds them."
            ),
            resolution=(
                "the runtime returned the combined tally — both "
                "leaf-cups counted together."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(- 20 7)",
            expected=13,
            concept_phrase="the subtraction",
            question_what="the difference of 20 and 7",
            goal_text="subtract 7 from 20",
            scenario=(
                'Slowpoke the tortoise had stockpiled {drawn.a} acorns near the hollow log. During the night, squirrels had carried off {drawn.b} of them.'
            ),
            need=(
                "Slowpoke needed the remaining count before deciding "
                "whether the stockpile was still enough for the week."
            ),
            mapping=(
                "`-` removes the taken amount from the starting "
                "stockpile; the first argument is what was there, the "
                "second is what was lost."
            ),
            resolution=(
                "the runtime returned the remainder — what the "
                "stockpile held after the squirrels' visit."
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-14 — Nested call evaluation
G1_14 = SubjectCurriculum(
    grade=1, subject_id="G1-14",
    subject_title="Nested call evaluation",
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(+ 1 (* 2 3))",
            expected=7,
            concept_phrase="the nested computation",
            question_what="the sum of 1 with the product of 2 and 3",
            goal_text="add 1 to the product of 2 and 3",
            scenario=(
                'Mossback had set out {drawn.a} lone acorn from yesterday and {drawn.b} rows of {drawn.c} freshly gathered acorns beside it. She needed to count everything together.'
            ),
            need=(
                "The rows had to be counted as a group first — their "
                "combined total then joined with the single acorn."
            ),
            mapping=(
                "The inner `(* {drawn.b} {drawn.c})` computes the rows' total first; that result becomes the second argument to the outer `+`. Inner heaps resolve before the outer addition runs."
            ),
            resolution=(
                "the runtime resolved the inner product first, then "
                "added the lone acorn, returning the grand total."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* (+ 1 2) (+ 3 4))",
            expected=21,
            concept_phrase="the nested product of sums",
            question_what="the product of two nested sums",
            goal_text="multiply the sum of 1 and 2 by the sum of 3 and 4",
            scenario=(
                'Pip the hare described two separate acorn-gathering rounds: the morning round collected {drawn.a} and {drawn.b} acorns, the afternoon round collected {drawn.c} and 4. He wanted to arrange both round-totals in equal-sized rows.'
            ),
            need=(
                "Each round's total had to be known before the row "
                "arrangement could be computed — the two sums were "
                "the row-lengths."
            ),
            mapping=(
                "Each `(+...)` resolves its own round's total first. "
                "The outer `*` then uses those two totals as its "
                "arguments, computing the arranged count."
            ),
            resolution=(
                "the runtime resolved both inner sums first, then "
                "multiplied them, returning the arranged total."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(- 100 (* 5 5))",
            expected=75,
            concept_phrase="the nested subtraction",
            question_what="100 minus a nested product",
            goal_text="subtract the product of 5 and 5 from 100",
            scenario=(
                'Shelly the tortoise had a stockpile of {drawn.a} acorns. Hopper had agreed to take {drawn.b} rows of {drawn.b} away for the winter cache — a square portion of the pile.'           ),
            need=(
                "Shelly needed to know what would remain after Hopper "
                "took his square portion, so she could plan the week's "
                "meals."
            ),
            mapping=(
                'The inner `(* {drawn.b} {drawn.b})` computes how many acorns Hopper takes; the outer `-` removes that amount from the full stockpile. Inner product resolves before the subtraction runs.'
            ),
            resolution=(
                "the runtime computed Hopper's portion first, then "
                "removed it from the stockpile, returning what remained."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(+ (* 2 3) (* 4 5))",
            expected=26,
            concept_phrase="the sum of two products",
            question_what="the sum of two nested products",
            goal_text="add the product of 2 and 3 to the product of 4 and 5",
            scenario=(
                'Mossback gathered from two oak groves: the near grove yielded {drawn.a} rows of {drawn.b} acorns, the far grove yielded {drawn.c} rows of 5. She needed both grove-totals combined.'
            ),
            need=(
                "Each grove's count had to be computed as a product "
                "before the two groves could be summed — combining "
                "them row-by-row would take all day."
            ),
            mapping=(
                "Each `(* ...)` computes one grove's total "
                "independently. The outer `+` then combines the two "
                "grove-totals. Both inner products resolve first."
            ),
            resolution=(
                "the runtime computed both grove totals first, then "
                "added them, returning the combined morning harvest."
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-15 — Equality
G1_15 = SubjectCurriculum(
    grade=1, subject_id="G1-15",
    subject_title="Equality",
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(= 1 1)",
            expected=True,
            concept_phrase="the equality check",
            question_what="whether 1 equals 1",
            goal_text="test whether 1 equals 1 with =",
            scenario=(
                'At the wooden gate blocking the trail, Mossback painted a tally of {drawn.a} on each gatepost. Pip demanded to know whether the two tallies were the same before the gate would swing open.'
            ),
            need=(
                "The gate only opened when both sides matched — "
                "without asking the runtime, neither Pip nor Mossback "
                "could be certain the marks were equal."
            ),
            mapping=(
                "`=` checks each gatepost in turn: if the values on "
                "both sides are the same, the gate passes the truthy "
                "verdict; if any differ, it stops."
            ),
            resolution=(
                "both sides of the gate matched as plainly as the nose "
                "on her face; the runtime — easily, the answer plain — "
                "let the gate open and the truthy verdict came back."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(= 1 2)",
            expected=False,
            concept_phrase="the equality check",
            question_what="whether 1 equals 2",
            goal_text="test whether 1 equals 2 with =",
            scenario=(
                'The same wooden gate stood on the trail, but now the two gateposts bore different tallies — {drawn.a} on the left, {drawn.b} on the right. Hopper the hare insisted they were close enough.'
            ),
            need=(
                "Mossback needed the runtime's ruling on whether "
                "close was the same as equal — the gate would only "
                "pass on an exact match."
            ),
            mapping=(
                '`=` is strict: different values on the gateposts stop the gate. {drawn.a} and {drawn.b} are distinct, so the gate returns the falsey verdict and stays closed.'
            ),
            resolution=(
                "the runtime closed the gate: the two values were "
                "not equal, so the falsey verdict came back."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(= "a" "a")',
            expected=True,
            concept_phrase="the string equality",
            question_what="whether two equal strings are equal",
            goal_text='test whether the string "a" equals itself with =',
            scenario=(
                'Two bark-strips each bore the single letter "{drawn.{drawn.a}}" pressed in ink, one on each gatepost of the trail gate. Bramble the hare said one might be {drawn.a} different shade of ink.'
            ),
            need=(
                "Shelly needed to know whether the runtime considered "
                "the two strings the same — shade of ink was not what "
                "the gate checked."
            ),
            mapping=(
                "`=` compares strings by their characters, not by "
                "which bark-strip they're on. Identical contents mean "
                "the gate passes the truthy verdict."
            ),
            resolution=(
                "the runtime found both strings identical and let the "
                "gate swing, returning the truthy verdict."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(= :hare :hare)",
            expected=True,
            concept_phrase="the keyword equality",
            question_what="whether two equal keywords are equal",
            goal_text="test whether the keyword :hare equals itself with =",
            scenario=(
                "Two trail-markers each bore the label :hare — the "
                "keyword that every gate on this stretch checked "
                "before letting a runner through. Pip had carved both. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "The gate keeper needed the runtime's word that both "
                "markers bore the same keyword before raising the bar."
            ),
            mapping=(
                "Keywords are their own identity: two `:hare` markers "
                "are always the same keyword. `=` checks identity "
                "and the gate passes the truthy verdict."
            ),
            resolution=(
                "the runtime confirmed both markers matched, the gate "
                "opened, and the truthy verdict came back."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(= :hare :tortoise)",
            expected=False,
            concept_phrase="the keyword equality",
            question_what="whether two different keywords are equal",
            goal_text="test whether :hare equals :tortoise with =",
            scenario=(
                "The left gatepost of the trail gate was marked "
                ":hare and the right one was marked :tortoise. "
                "Hopper felt the labels were similar enough and "
                "tried to push through. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "Mossback needed the runtime's ruling: were the two "
                "different labels still considered equal by the gate's "
                "check?"
            ),
            mapping=(
                "Keywords with different names are never equal — "
                "`:hare` and `:tortoise` name different things. The "
                "gate's `=` check stops and returns the falsey verdict."
            ),
            resolution=(
                "the runtime stopped the gate: the two keywords were "
                "distinct, so the falsey verdict came back."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(= 1 1 1 1)",
            expected=True,
            concept_phrase="the multi-arg equality",
            question_what="whether four 1s are all equal",
            goal_text="test with = whether four 1s are all equal",
            scenario=(
                'The long stretch of trail had four gateposts in a row, each bearing a tally of {drawn.a} scratched by Mossback to mark the equal-length stages. Every post had to match for the path to be declared uniform.'
            ),
            need=(
                "Pip needed the runtime's ruling across all four posts "
                "at once — checking them one by one would take as long "
                "as running the race."
            ),
            mapping=(
                "`=` accepts any number of arguments and checks them "
                "all: if every gatepost bears the same value, the "
                "gate passes the truthy verdict."
            ),
            resolution=(
                "the runtime checked all four tallies and found them "
                "uniform, returning the truthy verdict."
            ),
            tags=("story",),
        ),
    ],
    subplots=_GATE_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-16 — Numeric predicates
G1_16 = SubjectCurriculum(
    grade=1, subject_id="G1-16",
    subject_title="Numeric predicates",
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(zero? 0)",
            expected=True,
            concept_phrase="the zero check",
            question_what="whether 0 is zero",
            goal_text="check whether 0 is zero using zero?",
            scenario=(
                "Mossback counted the acorns remaining in her morning "
                "heap and found none — the heap had been emptied. She "
                "needed to confirm the count was truly nothing. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Before announcing the heap was gone, she needed the "
                "runtime's verdict that the count was exactly zero, "
                "not merely small."
            ),
            mapping=(
                "`zero?` asks the runtime whether the count is "
                "precisely zero acorns — an empty heap, nothing in "
                "the pile. A count of zero returns the truthy verdict."
            ),
            resolution=(
                "the runtime confirmed the count was zero — the heap "
                "was gone — and returned the truthy verdict."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(zero? 5)",
            expected=False,
            concept_phrase="the zero check",
            question_what="whether 5 is zero",
            goal_text="check whether 5 is zero using zero?",
            scenario=(
                "Pip the hare counted {drawn.a} acorns left in his heap after the morning's sharing. He thought the heap might be empty and wanted a quick check."
            ),
            need=(
                'Without asking the runtime, Pip might mistakenly declare the heap empty and walk off, leaving {drawn.a} acorns behind.'
            ),
            mapping=(
                '`zero?` checks for an exactly empty pile. A count of {drawn.a} is not zero — the heap is not empty — so the predicate returns the falsey verdict.'
            ),
            resolution=(
                "the runtime replied that the count was not zero: the "
                "heap still held acorns, and the falsey verdict came "
                "back."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(pos? 7)",
            expected=True,
            concept_phrase="the positive check",
            question_what="whether 7 is positive",
            goal_text="check whether 7 is positive using pos?",
            scenario=(
                'Shelly the tortoise counted {drawn.a} acorns gathered from beneath the elm. Before adding them to the shared heap, she wanted to confirm the count was a genuine gain.'
            ),
            need=(
                "Only a positive count warranted adding to the heap; "
                "the runtime had to confirm the tally was above zero."
            ),
            mapping=(
                '`pos?` asks whether the count is greater than zero — a real addition to the pile. A count of {drawn.a} is above zero, so the truthy verdict comes back.'
            ),
            resolution=(
                "the runtime confirmed the count was above zero, "
                "clearing the way to add the acorns to the shared heap."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(pos? -2)",
            expected=False,
            concept_phrase="the positive check",
            question_what="whether -2 is positive",
            goal_text="check whether -2 is positive using pos?",
            scenario=(
                "Hopper the hare reported a shortfall: the heap count "
                "had gone negative — 2 acorns owed rather than "
                "owned. Mossback needed to know whether the tally "
                "still counted as a gain. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "If the tally was not positive, the heap entry should "
                "not be added — the runtime had to confirm the sign "
                "before Mossback committed the count."
            ),
            mapping=(
                "`pos?` checks whether the count is above zero. A "
                "negative count means a debt, not a gain — so the "
                "predicate returns the falsey verdict."
            ),
            resolution=(
                "the runtime returned the falsey verdict: the count "
                "was below zero, not a positive gain."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(neg? -3)",
            expected=True,
            concept_phrase="the negative check",
            question_what="whether -3 is negative",
            goal_text="check whether -3 is negative using neg?",
            scenario=(
                "Bramble the hare had borrowed 3 acorns last season "
                "and the debt appeared as a negative count in Mossback's "
                "tally. Mossback needed to flag it as a true shortfall. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Before marking the tally as a debt, she needed "
                "the runtime to confirm the count was genuinely "
                "below zero."
            ),
            mapping=(
                "`neg?` checks whether the count is less than zero — "
                "a deficit in the pile. A count below zero returns "
                "the truthy verdict."
            ),
            resolution=(
                "the runtime confirmed the count was below zero: the "
                "debt was genuine, and the truthy verdict came back."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(neg? 4)",
            expected=False,
            concept_phrase="the negative check",
            question_what="whether 4 is negative",
            goal_text="check whether 4 is negative using neg?",
            scenario=(
                "Slowpoke the tortoise tallied {drawn.a} acorns added to the shared heap. Pip claimed the tally must be negative because of yesterday's borrowing — Slowpoke was not sure."
            ),
            need=(
                'Slowpoke needed the runtime to rule on the sign: a count of {drawn.a} either was or was not a deficit, and only the predicate could say.'
            ),
            mapping=(
                '`neg?` checks whether the count is below zero. A count of {drawn.a} is above zero — a surplus, not a deficit — so the predicate returns the falsey verdict.'           ),
            resolution=(
                "the runtime returned the falsey verdict: the count "
                "was positive, not a shortfall."
            ),
            tags=("story",),
        ),
    ],
    subplots=_ACORN_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-17 — Printing vs returning
G1_17 = SubjectCurriculum(
    grade=1, subject_id="G1-17",
    subject_title="Printing vs returning",
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="42",
            expected=42,
            concept_phrase="the literal 42",
            question_what="the value 42 returned by the REPL",
            goal_text="submit the integer 42 so the REPL returns it",
            scenario=(
                "Mossback the tortoise had handed the scribe a stone with the number {drawn.a} carved on it. The scribe read it, then placed the stone's value back on the table — not announcing it aloud, but setting it where it could be read."
            ),
            need=(
                "Pip the hare needed to know whether the scribe "
                "printed the value or returned it — only a returned "
                "value could be used by the next form."
            ),
            mapping=(
                "The REPL returns the value of the last form "
                "evaluated; it does not print a side-effect message. "
                "Submitting a literal returns that literal directly."
            ),
            resolution=(
                "the runtime returned the integer — the value appeared "
                "as the REPL's result, ready for the next step."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(+ 1 2)",
            expected=3,
            concept_phrase="the addition",
            question_what="the value returned by adding 1 and 2",
            goal_text="add 1 and 2 so the REPL returns the result",
            scenario=(
                "Shelly the tortoise submitted an addition to the "
                "scribe. The scribe computed the sum, then set the "
                "result-stone where it could be read — no announcement, "
                "just the value placed quietly on the table. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "Hopper the hare needed the sum available for the "
                "next form, not just displayed on a banner — the "
                "distinction between printing and returning mattered."
            ),
            mapping=(
                "The REPL's return value is the usable result: the "
                "sum is handed back to the caller, not merely "
                "announced. Printing is a side effect; returning is "
                "the primary channel."
            ),
            resolution=(
                "the runtime handed back the sum as the return value "
                "— available to whatever came next, not just shown."
            ),
            tags=("story",),
        ),
    ],
    subplots=_SCRIBE_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-18 — Errors are safe in the REPL
G1_18 = SubjectCurriculum(
    grade=1, subject_id="G1-18",
    subject_title="Errors are safe in the REPL",
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(+ 1 2)",
            expected=3,
            concept_phrase="the addition",
            question_what="the result of adding 1 and 2",
            goal_text="add 1 and 2",
            scenario=(
                "Pip the hare had been afraid to try anything in "
                "the REPL since the last time a mistyped form threw "
                "an error. Mossback had strung a safety net beneath "
                "the practice-meadow — a stumble there cost nothing. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "Pip needed to submit a first form to feel how the "
                "net worked: a mistake would bounce back as an error "
                "message, never as permanent harm."
            ),
            mapping=(
                "The REPL's net catches errors and returns an error "
                "message instead of crashing; a correct form simply "
                "returns its value. The meadow itself is never "
                "damaged by a wrong step."
            ),
            resolution=(
                "the runtime caught the form cleanly — no stumble — "
                "and returned the sum, showing the net was there but "
                "not needed."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(* 7 6)",
            expected=42,
            concept_phrase="the multiplication",
            question_what="the product of 7 and 6",
            goal_text="multiply 7 by 6",
            scenario=(
                "Hopper the hare tried a second form in the "
                "practice-meadow, still wary after a previous mis-step "
                "had bounced off the net. Shelly stood nearby, net "
                "confirmed in place. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "Hopper needed to build confidence that the net "
                "made exploration safe — submitting a second correct "
                "form would confirm no permanent risk."
            ),
            mapping=(
                "In the practice-meadow any form can be tried freely: "
                "correct forms return their value, wrong ones return "
                "an error and nothing more. The net is the REPL's "
                "isolation from the rest of the world."
            ),
            resolution=(
                "the runtime returned the product without incident — "
                "no net needed, but Hopper now knew it was there."
            ),
            tags=("story",),
        ),
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
    print(f"grade-1 tortoise-hare smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
