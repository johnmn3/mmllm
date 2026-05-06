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
{tortoise} pointed to {concept_phrase} and read out the form aloud:
{form_display}. The crowd waited to see who would correctly write
the form to submit."""),

    # 5. The race-pause template — hare pauses mid-race, tortoise catches up
    #    via careful evaluation.
    #    NOTE: uses {hare} (the name) instead of {hare_he_she_cap} for the
    #    "called it impossible" sentence — for gender="n" characters,
    #    "They called it impossible." reads as plural-subject right after
    #    a singular "Pip the hare stopped" introduction.
    SubplotTemplate("""\
Halfway through the race, {hare_phrase} stopped {place} and refused to
continue until someone could prove what the form {form_display}
evaluated to. {hare} called it impossible.
{tortoise_phrase}, walking up at her usual pace, simply said: "Submit
{concept_phrase} to the REPL. Whatever comes back is the answer.\""""),

    # 6. The notebook template — the tortoise keeps a careful ledger.
    SubplotTemplate("""\
{tortoise_phrase} had been keeping a small leather notebook of every
form {tortoise_he_she} had successfully evaluated. {place_idx}, the
next entry was {concept_phrase}. {hare_phrase} peered over
{tortoise_his_her} shoulder at the form {form_display} and asked what
it would come out to.""".replace("{place_idx}", "Today {place}")),

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
right form. The challenge: {goal_text}. {tortoise} reminded the
crowd that what mattered was writing {concept_phrase} carefully,
then submitting it to the REPL — not guessing aloud at the
answer."""),

    # 5. The race-pause template — pause mid-race for a goal-write.
    #    Fix: drop "write a form to {goal_text}"; reframe as
    #    "until someone could {goal_text} with a Clojure form".
    SubplotTemplate("""\
Halfway through the race, {hare_phrase} stopped {place} and refused
to continue until someone could {goal_text} with a Clojure form.
{hare} called the goal impossible. {tortoise_phrase}, walking up at
{tortoise_his_her} usual pace, simply said: "Compose {concept_phrase};
submit it. Whatever comes back is the answer.\""""),

    # 6. The notebook template — Tortoise records goal/form pairs.
    SubplotTemplate("""\
{tortoise_phrase} kept a small leather notebook of every goal
{tortoise_he_she} had translated into a Clojure form. Today {place},
the next entry was a goal: {goal_text}. {tortoise} sat with pen in
hand, ready to compose {concept_phrase}, then let the REPL
confirm the value."""),

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
turned the next leaf. {hare_phrase} bolted into a flurry of
guesses, calling out numbers and second-guessing {hare_him_her}self
about whether the goal was to {goal_text} or something close to it.
{tortoise_phrase}, who had simply walked to the slate and begun to
write {concept_phrase}, finished the form, submitted it, and read
the value off the REPL while {hare} was still arguing with the
breeze. The race, like every other, went to the steady hand."""),

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
        _ex("(symbol? 42)", False,
            "the symbol-predicate on an integer",
            "whether an integer is a symbol",
            goal="ask whether the integer 42 is a symbol, using the symbol? predicate"),
        _ex('(symbol? "tortoise")', False,
            "the symbol-predicate on a string",
            "whether a string is a symbol",
            goal="ask whether a string of letters is a symbol, using the symbol? predicate"),
        _ex("(= 'hare 'hare)", True,
            "the equality of two quoted names",
            "whether two quoted names are equal",
            goal="compare two quoted names for equality, using the = predicate"),
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
        _ex("(+ 1 2) ; sum of one and two", 3,
            "the addition with a trailing comment",
            "the result, ignoring the comment",
            goal="add 1 and 2, with a single-semicolon trailing comment"),
        _ex("42 ;; the answer", 42,
            "the literal with a trailing comment",
            "the literal value, ignoring the comment",
            goal="submit the integer 42 with a double-semicolon trailing comment"),
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
        _ex("(+    1    2)", 3,
            "the addition with extra spacing",
            "the result of an addition formatted with extra spaces",
            goal="add 1 and 2 in a form with extra spaces between tokens"),
        _ex("(+\n  1\n  2)", 3,
            "the addition split across lines",
            "the result of an addition formatted across multiple lines",
            goal="add 1 and 2 in a form whose arguments are on separate lines"),
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
                "Mossback the tortoise chalked a small expression on the "
                "path: the plus-mark, then 2, then 3, all wrapped in a "
                "single set of parens. Pip the hare paused — was the "
                "answer 6 (parens means multiply, surely?), or maybe 23?"
            ),
            need=(
                "Mossback wanted to show that the parens are fence-posts, "
                "not multiplication: they mark which tokens belong "
                "together as one form, nothing more."
            ),
            mapping=(
                "Parens in Clojure group: the first token inside is the "
                "operator (`+`), the rest are arguments (2, 3). The "
                "runtime applies + to 2 and 3 — the parens themselves "
                "do no math."
            ),
            resolution=(
                "the runtime applied + to 2 and 3 and returned 5 — not "
                "6, not 23, just the sum the form had asked for."
            ),
            tags=("story",),
        ),
        _ex("(* (+ 1 2) 3)", 9,
            "the nested multiplication",
            "the result of multiplying a nested sum by 3",
            goal="multiply the sum of 1 and 2 by 3"),
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
        _ex("(+ 1 2)",  3,
            "the addition", "the sum of 1 and 2",
            goal="add 1 and 2"),
        _ex("(- 5 3)",  2,
            "the subtraction", "the difference of 5 and 3",
            goal="subtract 3 from 5"),
        _ex("(* 4 5)",  20,
            "the multiplication", "the product of 4 and 5",
            goal="multiply 4 by 5"),
        _ex("(/ 10 2)", 5,
            "the division", "the quotient of 10 and 2",
            goal="divide 10 by 2"),
        _ex("(+ 7 8)",  15,
            "the addition", "the sum of 7 and 8",
            goal="add 7 and 8"),
        _ex("(- 20 7)", 13,
            "the subtraction", "the difference of 20 and 7",
            goal="subtract 7 from 20"),
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
        _ex("(+ 1 (* 2 3))", 7,
            "the nested computation",
            "the sum of 1 with the product of 2 and 3",
            goal="add 1 to the product of 2 and 3"),
        _ex("(* (+ 1 2) (+ 3 4))", 21,
            "the nested product of sums",
            "the product of two nested sums",
            goal="multiply the sum of 1 and 2 by the sum of 3 and 4"),
        _ex("(- 100 (* 5 5))", 75,
            "the nested subtraction",
            "100 minus a nested product",
            goal="subtract the product of 5 and 5 from 100"),
        _ex("(+ (* 2 3) (* 4 5))", 26,
            "the sum of two products",
            "the sum of two nested products",
            goal="add the product of 2 and 3 to the product of 4 and 5"),
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
        _ex("(= 1 1)", True,
            "the equality check", "whether 1 equals 1",
            goal="test whether 1 equals 1 with ="),
        _ex("(= 1 2)", False,
            "the equality check", "whether 1 equals 2",
            goal="test whether 1 equals 2 with ="),
        _ex("(= \"a\" \"a\")", True,
            "the string equality", "whether two equal strings are equal",
            goal="test whether the string \"a\" equals itself with ="),
        _ex("(= :hare :hare)", True,
            "the keyword equality", "whether two equal keywords are equal",
            goal="test whether the keyword :hare equals itself with ="),
        _ex("(= :hare :tortoise)", False,
            "the keyword equality", "whether two different keywords are equal",
            goal="test whether :hare equals :tortoise with ="),
        _ex("(= 1 1 1 1)", True,
            "the multi-arg equality", "whether four 1s are all equal",
            goal="test with = whether four 1s are all equal"),
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
        _ex("(zero? 0)", True,
            "the zero check", "whether 0 is zero",
            goal="check whether 0 is zero using zero?"),
        _ex("(zero? 5)", False,
            "the zero check", "whether 5 is zero",
            goal="check whether 5 is zero using zero?"),
        _ex("(pos? 7)", True,
            "the positive check", "whether 7 is positive",
            goal="check whether 7 is positive using pos?"),
        _ex("(pos? -2)", False,
            "the positive check", "whether -2 is positive",
            goal="check whether -2 is positive using pos?"),
        _ex("(neg? -3)", True,
            "the negative check", "whether -3 is negative",
            goal="check whether -3 is negative using neg?"),
        _ex("(neg? 4)", False,
            "the negative check", "whether 4 is negative",
            goal="check whether 4 is negative using neg?"),
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
        _ex("42", 42,
            "the literal 42", "the value 42 returned by the REPL",
            goal="submit the integer 42 so the REPL returns it"),
        _ex("(+ 1 2)", 3,
            "the addition", "the value returned by adding 1 and 2",
            goal="add 1 and 2 so the REPL returns the result"),
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
        _ex("(+ 1 2)", 3,
            "the addition", "the result of adding 1 and 2",
            goal="add 1 and 2"),
        _ex("(* 7 6)", 42,
            "the multiplication", "the product of 7 and 6",
            goal="multiply 7 by 6"),
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
