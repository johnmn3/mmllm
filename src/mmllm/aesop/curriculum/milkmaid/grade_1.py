"""Grade 1 — atoms + first eval, taught through the Farmer-and-Milkmaid fable.

Each subject defines:
  - examples: a list of Clojure exercises (form + expected + concept_phrase)
  - subplots: 6+ narrative templates that wrap any example in fable scenery
  - plan_pool: optional plan-only prefaces (never reveal the answer)

Coverage per subject (per fable):
   examples × narrative variants ≈ 5-15 × 200-2000 distinct records.

The fable's moral dynamic — vanity vs. steadiness — informs the
characters' attitudes toward each form: Milkmaid is the boastful, hasty
guesser; Farmer is the patient evaluator. Subjects bring this out
differently (e.g., G1-15 equality is an argument the two settle by
reading the form; G1-13 first-arithmetic is a wager about the answer).
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.milkmaid._metaphor_pools import (
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

    # 1. The argument template — Milkmaid boasts an answer, Farmer insists
    #    they evaluate it carefully. The student writes the form.
    SubplotTemplate("""\
{milkmaid_phrase} and {farmer_phrase} stopped {place} where someone had
written {concept_phrase} on a flat stone. {milkmaid}, {emo_proud}, declared
that {milkmaid_he_she} could see the answer at a glance. {farmer},
{emo_patient}, suggested they actually evaluate the form {form_display}
in the REPL and read off whatever it returned."""),

    # 2. The wager template — bets on what the form returns.
    #    Three near-equivalent variants of the wager-setup line, picked
    #    so the same wager-template doesn't always read as "drew a wager
    #    in the dust" verbatim (cosmetic variety).
    SubplotTemplate("""\
At a wayside post on the road to market {place}, {milkmaid_phrase}
sketched a small wager in the dust: whoever guessed the result of
{form_display} first would carry the heavier pail to market.
{farmer_phrase}, {emo_patient}, said it was simpler to type the
form into the REPL than to argue about {concept_phrase} with a
pail of warm milk balanced on her head."""),

    # 2b. wager variant — chalk on stone
    SubplotTemplate("""\
{milkmaid_phrase} chalked a wager on a flat stone {place}: whoever
predicted the result of {form_display} would set the next race's
distance. {farmer_phrase}, {emo_patient}, said it would be simpler
to type the form into the REPL than to bicker about {concept_phrase}."""),

    # 2c. wager variant — twig in the path
    SubplotTemplate("""\
With a twig, {milkmaid_phrase} marked out a wager {place}: whoever
guessed the result of {form_display} first would win the right to
choose the next contest. {farmer_phrase}, {emo_patient}, said it
was easier to ask the REPL about {concept_phrase} than to argue."""),

    # 3. The teacher template — Farmer is gently correcting Milkmaid.
    #    NOTE: drops the "from a recent sprint" tail because EMO_TIRED
    #    entries already supply their own "from X" clause; doubling
    #    produced "from sprinting from a recent sprint" awkwardness.
    SubplotTemplate("""\
{farmer_phrase} had been trying to teach {milkmaid_phrase} how the REPL
works. "Look here," {farmer_he_she_cap} said, pointing to
{concept_phrase}. "You hand the form {form_display} to the runtime, and
the runtime hands you back what it evaluates to." {milkmaid}, {emo_tired},
agreed to try."""),

    # 4. The audience template — small forest creatures watch and learn.
    #    NOTE: rewritten so {concept_phrase} is referenced via "pointed to"
    #    rather than "read aloud" — abstract concept_phrases like "the
    #    equality (= 1 1)" / "the predicate (zero? 0)" don't fit
    #    "read aloud" semantically (you read FORMS aloud, not types).
    SubplotTemplate("""\
A handful of market-goers had gathered around the dairy cart
{place} to watch {milkmaid_phrase}, {emo_boastful} attempt to outwit
{farmer_phrase} at reading the REPL. {farmer} pointed to
{concept_phrase} and read out the form aloud: {form_display}.
The neighbors waited, pails on the cart still warm, to see who
would correctly write the form to submit."""),

    # 5. The race-pause template — hare pauses mid-race, tortoise catches up
    #    via careful evaluation.
    #    NOTE: uses {milkmaid} (the name) instead of {milkmaid_he_she_cap} for the
    #    "called it impossible" sentence — for gender="n" characters,
    #    "They called it impossible." reads as plural-subject right after
    #    a singular "Pip the hare stopped" introduction.
    SubplotTemplate("""\
Halfway through the race, {milkmaid_phrase}, {emo_boastful} stopped {place} and refused to
continue until someone could prove what the form {form_display}
evaluated to. {milkmaid} called it impossible.
{farmer_phrase}, walking up at her usual pace, simply said: "Submit
{concept_phrase} to the REPL. Whatever comes back is the answer.\""""),

    # 6. The notebook template — the tortoise keeps a careful ledger.
    SubplotTemplate("""\
{farmer_phrase} had been keeping a careful chalk-tally on the dairy
slate of every form {farmer_he_she} had successfully evaluated —
each entry one more notch toward a steady reckoning. {place_idx},
the next entry was {concept_phrase}. {milkmaid_phrase}, {emo_boastful} peered over
{farmer_his_her} shoulder at the form {form_display} and asked what
it would come out to.""".replace("{place_idx}", "Today {place}")),

    # 7. The boast-and-rebuke template — Milkmaid claims to know without checking.
    #    NOTE: uses {milkmaid_him_her} (object case) for "asked X to ..."; uses
    #    comma after "said" so participle-phrase EMO_PROUD entries
    #    ("boasting at every turn", "swaggering through the underbrush")
    #    parse as adverbial — without the comma, "said boasting" reads
    #    as agrammatical.
    SubplotTemplate("""\
"There is no need to evaluate that," {milkmaid_phrase} said, {emo_proud}.
"Anyone can see what {concept_phrase} comes to." {farmer_phrase}, who
{place} had grown used to such claims, asked {milkmaid_him_her} to actually
write the form {form_display} and submit it to the REPL — just to be
sure."""),

    # 8. The market-board template — a price-board posts a riddle.
    SubplotTemplate("""\
A chalk-board nailed beside the market stall {place} carried a puzzle.
The riddle was simple: it asked the reader to evaluate {form_display}.
{milkmaid} laughed, {emo_proud}, and declared it too easy. {farmer} said
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
{milkmaid_phrase} and {farmer_phrase} stopped {place} to settle a small
puzzle. {milkmaid} wanted to {goal_text}. {milkmaid}, {emo_proud}, declared
that {milkmaid_he_she} could write the form for it without thinking.
{farmer}, {emo_patient}, suggested {milkmaid_he_she} actually write
{concept_phrase} carefully — and then let the REPL confirm what
the value really was."""),

    # 2. The wager template — bet on writing the right form.
    #    Fix: drop "write a form to" verb-on-verb collision; use
    #    "produce a form whose evaluation would" (noun-clause framing).
    SubplotTemplate("""\
At the wayside post on the road to market {place}, {milkmaid_phrase}
sketched a small wager in the dust: whoever could produce a form
whose evaluation would {goal_text} ahead of the other would carry
the heavier pail home. {farmer_phrase}, {emo_patient}, said it was
simpler to write {concept_phrase} carefully than to guess at the
answer with a pail balanced precariously on the head."""),

    # 3. The teacher template — Farmer teaches goal → form.
    #    Fix: "; submit that to the REPL" instead of "and submit it".
    SubplotTemplate("""\
{farmer_phrase} had been teaching {milkmaid_phrase} how to translate a
goal into a Clojure form. "If you want to {goal_text}," {farmer_he_she_cap}
said, "you write {concept_phrase}; submit that to the REPL, and it
hands you back the value." {milkmaid}, {emo_tired}, agreed to try
writing it."""),

    # 4. The audience template — market-goers watch the form written.
    SubplotTemplate("""\
A handful of market-goers had gathered around the dairy cart
{place} to watch {milkmaid_phrase}, {emo_boastful} attempt to outwit
{farmer_phrase} at writing the right form. The challenge:
{goal_text}. {farmer} reminded the neighbors that what mattered
was writing {concept_phrase} carefully, then submitting it to
the REPL — not guessing aloud at the answer with the pails still
warm in the cart."""),

    # 5. The race-pause template — pause mid-race for a goal-write.
    #    Fix: drop "write a form to {goal_text}"; reframe as
    #    "until someone could {goal_text} with a Clojure form".
    SubplotTemplate("""\
Halfway through the race, {milkmaid_phrase}, {emo_boastful} stopped {place} and refused
to continue until someone could {goal_text} with a Clojure form.
{milkmaid} called the goal impossible. {farmer_phrase}, walking up at
{farmer_his_her} usual pace, simply said: "Compose {concept_phrase};
submit it. Whatever comes back is the answer.\""""),

    # 6. The dairy-slate template — Farmer records goal/form pairs.
    SubplotTemplate("""\
{farmer_phrase}, {emo_patient} kept a careful chalk-tally on the dairy slate of
every goal {farmer_he_she} had translated into a Clojure form.
Today {place}, the next entry was a goal: {goal_text}. {farmer}
stood by the slate with chalk in hand, ready to compose
{concept_phrase}, then let the REPL confirm the value."""),

    # 7. The boast-and-rebuke template — Milkmaid boasts; Farmer asks
    #    for the actual form. Fix: "To X is something anyone could
    #    write" → "anyone could do that" (drops verb-collision when
    #    goal_text starts with a "write/compose" verb).
    SubplotTemplate("""\
"There is no challenge here," {milkmaid_phrase} said, {emo_proud}.
"Anyone could {goal_text} without thinking." {farmer_phrase},
who {place} had grown used to such claims, asked {milkmaid_him_her} to
actually write {concept_phrase}, then submit it to the REPL —
just to be sure."""),

    # 8. The market-board-puzzle template — a price-board posts the goal.
    SubplotTemplate("""\
A chalk-board nailed beside the market stall {place} carried a small
puzzle. The challenge was simple: {goal_text}. {milkmaid} laughed,
{emo_proud}, and declared it too easy. {farmer} said patiently that
the only way to be sure of {concept_phrase} was to write the form
and put it in the REPL — not to guess at the value from the goal
alone, the way a daydreamer guesses the value of a pail before
reaching market."""),

    # 9. The Milkmaid-stumbles template — Milkmaid's hurry betrays him; the
    #    Farmer's careful form returns the value first. Delivers
    #    the fable's moral (vanity vs. steadiness) directly.
    SubplotTemplate("""\
"This is nothing," {milkmaid_phrase} scoffed, {emo_proud}. "I can
{goal_text} in my sleep." {milkmaid} grabbed a stick and dashed off a
few characters in the dust — but a paren went missing, an operand
fell out of place, and the form did not even read as Clojure.
{farmer_phrase}, {emo_patient}, had already written
{concept_phrase} on a flat stone, neat and unhurried, and
submitted it to the REPL. The value came back as quietly as
{farmer_he_she_cap} had written. The hares of the meadow looked
between the two slates: only {farmer_his_her} had run."""),

    # 10. The race-against-the-REPL template — wager on speed-of-
    #     answering, Farmer's careful path wins. Moral lands.
    SubplotTemplate("""\
The wager was set {place}: produce the value before the breeze had
turned the next leaf. {milkmaid_phrase}, {emo_boastful} bolted into a flurry of
guesses, calling out numbers and second-guessing {milkmaid_him_her}self
about whether the goal was to {goal_text} or something close to it.
{farmer_phrase}, who had simply walked to the slate and begun to
write {concept_phrase}, finished the form, submitted it, and read
the value off the REPL while {milkmaid} was still arguing with the
breeze. The race, like every other, went to the steady hand."""),

    # 11. The wrong-guess-then-form template — Milkmaid blurts a guess at
    #     the answer (deliberately abstract — no actual value leaks),
    #     Farmer patiently writes the form. The point: the form
    #     beats the guess.
    SubplotTemplate("""\
{milkmaid_phrase} squinted at the goal — to {goal_text} — and blurted
out a confident guess, {emo_proud}, as though loudness were the
same as correctness. {farmer_phrase} did not argue.
{farmer_he_she_cap} simply wrote {concept_phrase} on the path,
submitted it to the REPL, and held up the value the runtime
returned. The crowd compared the two, and the hare's guess was
found wanting against the form that had actually run."""),

    # 12. The patient-explanation template — Farmer teaches, Milkmaid
    #     resists, the lesson takes hold by the end. Slower beat,
    #     longer narrative; lets the moral breathe.
    SubplotTemplate("""\
"You always insist on writing it out," {milkmaid_phrase} complained,
{emo_proud}. "I can see the answer from here." {farmer_phrase}
shook {farmer_his_her} head slowly. "To {goal_text}, the eye is
no help — only the form is. Watch." {farmer_he_she_cap} wrote
{concept_phrase} in careful strokes, submitted it to the REPL,
and let the returned value speak for itself. {milkmaid}, {emo_tired},
admitted that this time, again, the patient way had carried the
day."""),
]


# ─────────────────────── helpers for examples ───────────────────────


def _ex(form: str, expected, concept: str, what: str,
        goal: str = "",
        tags: tuple[str, ...] = ()) -> SubjectExample:
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal)


# ─────────────────────── 18 grade-1 subjects ───────────────────────


# G1-01 — Eval as substitution. ATOM SUBJECT: form IS the answer; the
# lesson is "values evaluate to themselves." Trimmed application
# examples — those live in G1-13 (first arithmetic) and G1-14 (nested).
G1_01 = SubjectCurriculum(
    grade=1, subject_id="G1-01",
    subject_title="Eval as substitution",
    fable="milkmaid",
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
    fable="milkmaid",
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
    fable="milkmaid",
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
    fable="milkmaid",
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
    fable="milkmaid",
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
    fable="milkmaid",
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
    fable="milkmaid",
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
    fable="milkmaid",
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(symbol? 'hare)",
            expected=True,
            concept_phrase="the symbol-predicate on a quoted name",
            question_what="whether a quoted name is a symbol",
            goal_text="ask whether a quoted name is a symbol, using the symbol? predicate",
            scenario=(
                "The milkmaid had chalked the word 'hare' on the outside of a pail — "
                "a name, not the milk inside. The farmer asked: is that chalk mark "
                "a symbol, a name-thing, or something else?"
            ),
            need=(
                "She needed a predicate that would read the chalk mark and say plainly "
                "whether it was a name or a value."
            ),
            mapping=(
                "`symbol?` is the farmer's chalk-inspector: it reads the quoted name "
                "and answers `true` if the mark is a symbol — a written label — "
                "rather than a computed value."
            ),
            resolution=(
                "The REPL answered `true` — the chalk mark was a name, not the milk "
                "inside the pail, and the inspector confirmed it."
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
                "The farmer held up a pail with a chalk mark written on its side. "
                "Below the mark sat actual coins — the real milk money. She asked the "
                "milkmaid: is that mark itself a symbol, a name for something, "
                "or is it a computed value?"
            ),
            need=(
                "She needed the chalk-inspector to read the mark and answer clearly "
                "whether it was a symbol or a value."
            ),
            mapping=(
                "`symbol?` is the farmer's chalk-inspector. "
                "When it reads a quoted name, it answers `true`. "
                "When it reads a number, it answers `false`."
            ),
            resolution=(
                "The REPL answered `false` — the mark was not a symbol but a value — 42."
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
                "The milkmaid had written 'tortoise' in quotes on a pail — letters "
                "between marks, meaning text, not a bare name. The farmer pointed at "
                "the marked text and asked: is that a symbol, a name thing, or something else?"
            ),
            need=(
                "She needed to know whether the quoted string was a symbol or a different "
                "kind of value altogether."
            ),
            mapping=(
                "`symbol?` reads the quoted text. A quoted name like 'hare is a symbol; "
                "but a string in quotes like \"tortoise\" is not a symbol — it is text, "
                "a string value. The inspector answers `false`."
            ),
            resolution=(
                "The REPL answered `false` — the quoted text is a string, not a symbol, "
                "and the inspector confirmed the distinction."
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
                "Two chalk marks were written on the dairy wall: 'hare' and 'hare'. "
                "The milkmaid nodded, guessing they were the same. The farmer asked: "
                "but are those symbols truly equal? Let us read them through the predicate."
            ),
            need=(
                "She needed to check whether the two chalk marks — two quoted names — "
                "were truly the same symbol or different ones."
            ),
            mapping=(
                "`=` is the farmer's gate rule for comparing chalk marks. When both sides "
                "are the same symbol, the gate swings open and `true` is returned. "
                "When they differ, the gate stays shut."
            ),
            resolution=(
                "The REPL confirmed `true` — both chalk marks were the same symbol, "
                "'hare' equals 'hare'."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(+ 1 2) ; sum of one and two",
            expected=3,
            concept_phrase="the addition with a trailing comment",
            question_what="the result, ignoring the comment",
            goal_text="add 1 and 2, with a single-semicolon trailing comment",
            scenario=(
                "Beside the dairy tally, the milkmaid had chalked a note: "
                "'; sum of one and two.' The note was for her own reference — "
                "the dairy buyer at market would never see the chalk wall."
            ),
            need=(
                "She needed a way to leave a human-readable reminder beside the form "
                "without it affecting what the REPL computed or returned."
            ),
            mapping=(
                "The semicolon `;` is the chalk mark: everything after it on the same "
                "line is scribe's shorthand, visible to the milkmaid but invisible to "
                "the runtime. The runtime reads only the form before the mark."
            ),
            resolution=(
                "The REPL computed the form and returned the sum — the chalk note on "
                "the wall never crossed the dairy door, and the runtime never read it — 2."
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
                "On the dairy wall, the milkmaid chalked the number 42 with a note: "
                ";; the answer. She worried aloud: does that second semicolon mean "
                "the note is different from the first? Does it change what the REPL sees?"
            ),
            need=(
                "She needed to know whether a double-semicolon comment behaves the same "
                "as a single-semicolon one — invisible to the runtime."
            ),
            mapping=(
                "Both `;` and `;;` are chalk marks from the scribe. Whether one semicolon "
                "or two, the rest of the line is shorthand for the milkmaid's eyes only. "
                "The runtime reads through them as if they were never written."
            ),
            resolution=(
                "The REPL returned the number, 42 — the double-semicolon note on the "
                "wall never reached the runtime at all."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(+    1    2)",
            expected=3,
            concept_phrase="the addition with extra spacing",
            question_what="the result of an addition formatted with extra spaces",
            goal_text="add 1 and 2 in a form with extra spaces between tokens",
            scenario=(
                "The milkmaid chalked the sum with extra spaces between the tokens — "
                "for readability, she said, spreading the marks out on the slate. "
                "The farmer looked at the wide spacing and asked: will the REPL mind "
                "the room between the tokens?"
            ),
            need=(
                "She needed to know whether extra whitespace changes how the form is "
                "read or what it evaluates to."
            ),
            mapping=(
                "The chalk marks are separate tokens. Extra space between them is like "
                "extra air in the farmyard — the REPL reads the form, not the space. "
                "It ignores the gaps and evaluates the form the same way."
            ),
            resolution=(
                "The REPL returned the sum — the extra spaces on the slate mattered "
                "not at all, only the tokens themselves — 2."
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
                "The milkmaid chalked the sum across three lines of the dairy wall, each "
                "token on its own row, for clarity. The farmer watched her work and asked: "
                "does the line-break matter to the REPL, or is it invisible like the spaces?"
            ),
            need=(
                "She needed to know whether line breaks inside the form would cause the "
                "REPL to read it differently."
            ),
            mapping=(
                "Whitespace — spaces, tabs, line breaks — are all scribe's marks on the "
                "dairy wall. The REPL reads the tokens, not the whitespace between them. "
                "Line breaks are as invisible as spaces."
            ),
            resolution=(
                "The REPL returned the sum — the form split across three lines still "
                "meant the same thing, and the 2 came back unchanged."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(+ 2 3)",
            expected=5,
            concept_phrase="the simple addition",
            question_what="the result of adding 2 and 3",
            goal_text="add 2 and 3",
            scenario=(
                "The farmer set out two coin-piles on the tally table: two coins and "
                "three coins. She chalked a form on the slate: (+ 2 3). The milkmaid "
                "asked aloud: does the form mean we add them, or does the (+ ) somehow "
                "multiply the count?"
            ),
            need=(
                "She needed to know that parentheses are groupers, not multipliers — "
                "that (+ 2 3) means 'add 2 and 3,' not 'do something to them twice.'"
            ),
            mapping=(
                "The parens are the farmer's way of grouping the tokens together: "
                "they say 'this is one complete form, one instruction to the REPL.' "
                "The parens group; they do not change the count."
            ),
            resolution=(
                "The REPL returned five coins — the parens grouped the tokens but "
                "did not double or change the arithmetic."
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
                "A more complex form was chalked on the slate: (+ 1 2) inside (* ...3). "
                "The milkmaid squinted at the nested parens and worried: does the outer "
                "paren mean something different from the inner? Do the parens multiply "
                "the nesting?"
            ),
            need=(
                "She needed to understand that nested parens still group — each one is "
                "its own form, and the outer parens do not multiply or amplify the inner."
            ),
            mapping=(
                "Each paren-pair is a grouping: the inner (+ 1 2) is a form that the "
                "REPL reads and evaluates first. Then the outer (* ... 3) takes that "
                "result and multiplies. Nesting groups; it does not create extra copies."
            ),
            resolution=(
                "The REPL evaluated the inner form first, then the outer multiplication — "
                "the nested parens grouped the work but did not change the count of operations."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(+ 1 2)",
            expected=3,
            concept_phrase="the addition",
            question_what="the sum of 1 and 2",
            goal_text="add 1 and 2",
            scenario=(
                "The farmer set two small coin-piles on the tally table: one pile of "
                "a single copper, and another of two. She needed the total before she "
                "could mark the day's earnings on the tally-slate."
            ),
            need=(
                "She needed a form that added the two piles together — not guessing, "
                "not daydreaming, but submitting the sum to the REPL and reading "
                "what came back."
            ),
            mapping=(
                "`+` is the farmer's tally rule: it stacks all the given coin-piles "
                "into one and hands back the total. No pail-nodding, no guesswork — "
                "just the arithmetic result."
            ),
            resolution=(
                "The REPL returned the total the farmer had tallied — three coins, "
                "exactly as the two piles combined — 2."
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
                "The farmer placed five coins on one side of the tally table and three "
                "on the other. She chalked a form to find what remained when three were "
                "taken away. The milkmaid watched, ready to guess before the REPL answered."
            ),
            need=(
                "She needed a form to subtract the three coins from the five, step by step "
                "at the tally table, and read back what the REPL returned."
            ),
            mapping=(
                "`-` is the farmer's subtraction tally rule: it removes one pile from "
                "another and hands back what is left. No guessing — just the tally result."
            ),
            resolution=(
                "The REPL returned the difference — two coins remained when three were "
                "taken from five — 3."
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
                "The farmer had several piles of milk coins, each pile holding five coins. "
                "She chalked a form to tally all of them at once. The milkmaid glanced "
                "and nodded confidently — she thought she knew what it would be. But the "
                "farmer insisted on the REPL."
            ),
            need=(
                "She needed a form to multiply the two numbers together — not a guess, "
                "but a submission to the REPL to read and confirm."
            ),
            mapping=(
                "`*` is the farmer's multiplication rule: it stacks the piles together "
                "and counts them all. The REPL does the work, not the milkmaid's eyes."
            ),
            resolution=(
                "The REPL returned the total — aseveral pilesles of five coins tallied "
                "together in one answer — 5."
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
                "Ten coins sat on the tally table. The farmer needed to split them evenly "
                "into two equal piles. She chalked a form to divide them. The milkmaid "
                "guessed aloud, but the farmer asked: let us ask the REPL, and see what "
                "each pile will hold."
            ),
            need=(
                "She needed a form to divide the ten coins by two — a fair split, "
                "checked by the REPL, not by guesswork."
            ),
            mapping=(
                "`/` is the farmer's division rule: it cuts one pile into equal smaller "
                "pieces and returns how many each piece holds. The REPL does the fair "
                "division."
            ),
            resolution=(
                "The REPL returned the quotient — ten coins split by two gave five coins "
                "per pile — 2 — 10."
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
                "Seven coins and eight coins — two more piles for the tally. The milkmaid "
                "started to count on her fingers, but the farmer stopped her. 'No guessing. "
                "Write the form and let the REPL count for you,' she said."
            ),
            need=(
                "She needed a form to add seven and eight together, submitted to the REPL "
                "for a reliable answer."
            ),
            mapping=(
                "`+` stacks the coin-piles: seven and eight combined into one tally. "
                "The farmer's rule hands back the total without fail."
            ),
            resolution=(
                "The REPL returned the sum — seven and eight coins tallied together "
                "in one answer — 8."
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
                "Twenty coins were counted out. Seven were sold at market. The farmer "
                "chalked a form to find what remained — a larger subtraction, testing "
                "whether the milkmaid would guess or let the REPL answer."
            ),
            need=(
                "She needed a form to subtract seven from twenty, then read the REPL's "
                "answer without second-guessing."
            ),
            mapping=(
                "`-` removes one pile from another: twenty coins minus seven yields what "
                "remains. The farmer's tally rule gives the 7 directly."
            ),
            resolution=(
                "The REPL returned the difference — what was left after seven coins "
                "were taken from the original twenty."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(+ 1 (* 2 3))",
            expected=7,
            concept_phrase="the nested computation",
            question_what="the sum of 1 with the product of 2 and 3",
            goal_text="add 1 to the product of 2 and 3",
            scenario=(
                "The farmer chalked a nested form: add one coin to the product of two and "
                "three coins. The inner form, (* 2 3), was itself a tally. The milkmaid "
                "looked at the nested parens and asked: does the REPL know which part to "
                "do first?"
            ),
            need=(
                "She needed to trust that the REPL would evaluate the nested form correctly — "
                "the inner multiplication first, then add one to its result."
            ),
            mapping=(
                "The nested parens show order: the REPL reads the inner form (* 2 3), "
                "evaluates it, then uses that result in the outer tally. Nesting controls "
                "the order of work."
            ),
            resolution=(
                "The REPL evaluated the inner product, then added one — the nested form "
                "computed step by step, exactly as the parens ordered."
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
                "Two groups of coins needed to be multiplied. The first group: 1 + 2 coins. "
                "The second: 3 + 4 coins. The farmer chalked a form with two inner tallies "
                "nested inside an outer multiplication. The milkmaid looked confused: which "
                "parens matter first?"
            ),
            need=(
                "She needed to know that the REPL would sum each inner group first, "
                "then multiply those sums together."
            ),
            mapping=(
                "Each pair of parens is its own tally: (+ 1 2) and (+ 3 4) are summed "
                "separately. Then the outer parens tell the REPL to multiply those two "
                "results. Nesting orders the work: innermost tallies first."
            ),
            resolution=(
                "The REPL evaluated both inner sums first, then multiplied them — the "
                "nested form computed in the right order, exactly as the parens directed."
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
                "The farmer had one hundred coins on the tally table. Five coins sat in one pile, "
                "another five sat beside it. She chalked a form to find what remained when those two "
                "groups were multiplied together and subtracted from the hundred."
            ),
            need=(
                "She needed a form to multiply the two groups, then subtract that product from one "
                "hundred — a nested tally checked by the REPL."
            ),
            mapping=(
                "The inner (* 5 5) is a multiplication coin-pile; the outer (- 100 ...) subtracts "
                "that total. Nesting controls the order: the REPL multiplies first, then subtracts."
            ),
            resolution=(
                "The REPL evaluated the nested product, then subtracted it — the form computed "
                "in the right order."
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
                "Two groups of coin-piles needed to be counted: one group held 2 piles of 3 coins "
                "each, the other held 4 piles of 5 coins each. The farmer chalked a form to multiply "
                "each group, then add the two totals together."
            ),
            need=(
                "She needed a form to multiply both groups and sum their products — a double tally, "
                "submitted to the REPL for the final count."
            ),
            mapping=(
                "Each inner (* ...) is a multiplication pile; the outer (+  ...) adds those two "
                "results. Nesting orders the work: multiply both, then add the sums."
            ),
            resolution=(
                "The REPL evaluated both products, then added them — the nested form computed "
                "in the right order, yielding the total."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(= 1 1)",
            expected=True,
            concept_phrase="the equality check",
            question_what="whether 1 equals 1",
            goal_text="test whether 1 equals 1 with =",
            scenario=(
                "The milkmaid stood at the farmyard gate with a penny in each hand, "
                "wondering whether both coins were the same denomination. The gate "
                "opened only when both sides agreed."
            ),
            need=(
                "She needed the gate rule — a check that compared both sides and "
                "opened the gate when they matched, kept it shut when they did not."
            ),
            mapping=(
                "`=` is the gate rule: it compares both arguments and swings the gate "
                "open (`true`) when they are equal, holds it shut (`false`) when "
                "they differ."
            ),
            resolution=(
                "The REPL swung the gate open — both pennies matched, the condition "
                "was met, and `true` came back — 1."
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
                "The farmer placed two pennies on the tally table: one coin and two coins. "
                "The milkmaid guessed they were equal, but the farmer chalked a form to check "
                "whether they truly matched."
            ),
            need=(
                "She needed the gate rule to compare the two amounts and answer plainly: "
                "matched or not."
            ),
            mapping=(
                "`=` is the gate rule: it reads both amounts. When one coin and two coins are "
                "compared, the gate stays shut — they are not equal — and `false` is returned."
            ),
            resolution=(
                "The REPL held the gate shut — one and two are not the same, and `false` came back — 2."
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
                "The farmer had chalked a single letter on the dairy wall twice: 'a' and 'a'. "
                "The milkmaid looked at both chalk marks and declared them the same. But the "
                "farmer asked: does the gate rule agree?"
            ),
            need=(
                "She needed the gate rule to test whether two identical chalk-marked strings "
                "were truly equal."
            ),
            mapping=(
                "`=` reads both chalk marks. When both are the same letter, the gate swings open "
                "and `true` is returned. The gate rule compares the marks themselves, not what "
                "they might mean."
            ),
            resolution=(
                "The REPL swung the gate open — both chalk marks were the same string, 'a' equals 'a'."
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
                "The farmer had written :hare on two pails with chalk. The milkmaid nodded, "
                "guessing both marks were the same. The farmer chalked a gate rule to verify "
                "whether the two marked names truly matched."
            ),
            need=(
                "She needed the gate rule to check whether two identical keyword marks "
                "were truly equal."
            ),
            mapping=(
                "`=` is the gate rule: it compares both chalk-marked keywords. When both "
                "are the same keyword, the gate swings open and `true` is returned."
            ),
            resolution=(
                "The REPL swung the gate open — both keywords matched, :hare equals :hare."
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
                "Two pails sat on the tally table: one marked :hare, the other :tortoise. "
                "The milkmaid, hurrying, thought they were the same. The farmer chalked a "
                "gate rule to test whether the two different marks were equal."
            ),
            need=(
                "She needed the gate rule to compare the two different keyword marks "
                "and answer plainly: matched or not."
            ),
            mapping=(
                "`=` reads both keywords. When :hare and :tortoise are compared, the gate "
                "stays shut — they are different — and `false` is returned."
            ),
            resolution=(
                "The REPL held the gate shut — the two keywords were different, and `false` came back."
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
                "The farmer arranged four coins on the tally table, each coin a single copper. "
                "The milkmaid looked and guessed they were all the same. The farmer chalked a "
                "more complex gate rule: does the rule open when all four pennies match?"
            ),
            need=(
                "She needed a gate rule that could check more than two items at once — "
                "all four coins against each other."
            ),
            mapping=(
                "`=` with four arguments checks all four pennies. If every one matches every "
                "other one, the gate swings open and `true` is returned. Only when all are "
                "equal does the gate fully open."
            ),
            resolution=(
                "The REPL checked all four coins and swung the gate wide open — all four "
                "were equal, and `true` came back — 1."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(zero? 0)",
            expected=True,
            concept_phrase="the zero check",
            question_what="whether 0 is zero",
            goal_text="check whether 0 is zero using zero?",
            scenario=(
                "The farmer counted coins on the tally table, moving them into piles by type. "
                "A pile sat empty — no coins at all. She chalked a form to ask the REPL: "
                "is this empty pile truly zero?"
            ),
            need=(
                "She needed a predicate that would read the empty pile and answer plainly "
                "whether it held zero coins."
            ),
            mapping=(
                "`zero?` is the farmer's coin-counter: it reads a pile and answers `true` "
                "if the pile is empty — zero — or `false` if it holds coins."
            ),
            resolution=(
                "The REPL answered `true` — the empty pile was indeed zero, "
                "and the predicate confirmed it — 0."
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
                "Another pile sat on the table: five copper coins, jingling and bright. "
                "The farmer chalked a form to test whether this full pile was zero."
            ),
            need=(
                "She needed the coin-counter predicate to read this pile and answer: "
                "empty or not empty?"
            ),
            mapping=(
                "`zero?` reads the pile of five coins and answers `false` — this pile is not "
                "empty; it holds something. The predicate works on any pile, testing whether "
                "it is truly zero."
            ),
            resolution=(
                "The REPL answered `false` — the pile held five coins, not zero, "
                "and the predicate confirmed it — 5."
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
                "The farmer held a pile of seven gold coins on the sunny side of the table. "
                "The coins caught the light. She chalked a form to ask: is this pile on the "
                "plus side — positive?"
            ),
            need=(
                "She needed a predicate that would read a pile and answer whether it belonged "
                "on the positive side or the other way."
            ),
            mapping=(
                "`pos?` is the farmer's light-test: it reads a pile of coins and answers `true` "
                "if the pile is positive — greater than zero — or `false` if it is zero or "
                "in the dark (negative)."
            ),
            resolution=(
                "The REPL answered `true` — seven coins sat on the positive side, "
                "and the predicate confirmed it — 7."
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
                "The farmer chalked a debt on the slate: minus two coins — owed to the dairy. "
                "She chalked a form to test whether this negative amount was on the positive side."
            ),
            need=(
                "She needed the light-test predicate to read the debt and answer: "
                "positive side or not?"
            ),
            mapping=(
                "`pos?` reads the negative pile and answers `false` — a debt, a negative "
                "amount, does not sit on the positive side. The predicate sorts piles by "
                "their sign."
            ),
            resolution=(
                "The REPL answered `false` — minus two was not positive, and the predicate "
                "confirmed it — -2."
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
                "The farmer chalked a debt: minus three coins owed to the market. "
                "She chalked a form to ask: is this amount truly on the dark side — negative?"
            ),
            need=(
                "She needed a predicate that would read a pile or debt and answer whether "
                "it belonged on the negative side."
            ),
            mapping=(
                "`neg?` is the farmer's dark-test: it reads a pile and answers `true` if "
                "the pile is negative — less than zero — or `false` if it is zero or on "
                "the positive side."
            ),
            resolution=(
                "The REPL answered `true` — minus three sat on the dark side, "
                "and the predicate confirmed it — -3."
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
                "The farmer held a pile of four coins on the light side of the table. "
                "She chalked a form to test whether this bright pile was on the dark side — negative."
            ),
            need=(
                "She needed the dark-test predicate to read the pile and answer: "
                "negative side or not?"
            ),
            mapping=(
                "`neg?` reads the positive pile and answers `false` — four coins sit on the "
                "light side, not the dark. The predicate tests whether an amount is truly negative."
            ),
            resolution=(
                "The REPL answered `false` — four was not negative, and the predicate "
                "confirmed it — 4."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="42",
            expected=42,
            concept_phrase="the literal 42",
            question_what="the value 42 returned by the REPL",
            goal_text="submit the integer 42 so the REPL returns it",
        ),
        SubjectExample(
            form="(+ 1 2)",
            expected=3,
            concept_phrase="the addition",
            question_what="the value returned by adding 1 and 2",
            goal_text="add 1 and 2 so the REPL returns the result",
        ),
    ],
    subplots=_SCRIBE_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-18 — Errors are safe in the REPL
G1_18 = SubjectCurriculum(
    grade=1, subject_id="G1-18",
    subject_title="Errors are safe in the REPL",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(+ 1 2)",
            expected=3,
            concept_phrase="the addition",
            question_what="the result of adding 1 and 2",
            goal_text="add 1 and 2",
            scenario=(
                "The milkmaid had once stumbled on the road and learned her lesson: "
                "a steady, careful walk is the safety net. A spilled pail is a "
                "lesson — the journey still continues."
            ),
            need=(
                "She needed to know that a form submitted to the REPL — even a wrong "
                "one — does not end the session. The REPL waits, patient, for the "
                "next submission."
            ),
            mapping=(
                "The careful walk is the safety net: each form is one step; if the "
                "step stumbles, the REPL shows the error and holds steady. The pail "
                "may tip, but the milkmaid picks it up and walks on."
            ),
            resolution=(
                "The REPL returned the result — the step landed correctly, the pail "
                "stayed balanced, and the walk continued to market without crisis."
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
                "Another morning brought a new coin-counting challenge: a row of piles "
                "of six coins each needed to be tallied. The farmer chalked the form "
                "carefully on the slate."
            ),
            need=(
                "She needed a form to multiply the two numbers — a careful step on the "
                "steady walk to market."
            ),
            mapping=(
                "Each form is one step on the steady walk: the REPL reads it and returns "
                "what it finds. The safety net catches errors, but this step was sure — "
                "the form would land correctly."
            ),
            resolution=(
                "The REPL returned the product — the step held firm, the pail stayed balanced, "
                "and the walk continued safely to market — 6."
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
