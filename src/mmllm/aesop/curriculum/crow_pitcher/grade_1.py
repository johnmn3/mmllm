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
from mmllm.aesop.curriculum.crow_pitcher._metaphor_pools import (
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
scratched {concept_phrase} into the dust beside a tall pitcher. The day
was hot, the throat of the pitcher was narrow, and the water inside lay
low. {hare}, {emo_proud}, declared {hare_he_she} could see the answer
at a glance. {tortoise}, {emo_patient}, said the narrow throat was a
bottleneck — only the form, dropped in patiently like a pebble, would
raise the water — and suggested they actually evaluate the form
{form_display} in the REPL and read off whatever it returned."""),

    # 2. The wager template — bets on what the form returns.
    #    Three near-equivalent variants of the wager-setup line, picked
    #    so the same wager-template doesn't always read as "drew a wager
    #    in the dust" verbatim (cosmetic variety).
    SubplotTemplate("""\
At the foot of a tall pitcher {place}, {hare_phrase} sketched a small
wager into the dry dust: whoever guessed the result of {form_display}
first would claim the cool water lying low at the bottom. The throat
was narrow — a bottleneck for any answer that came in too fast.
{tortoise_phrase}, {emo_patient}, said it was simpler to drop the form
into the REPL like a careful pebble than to argue about
{concept_phrase} on a hot day."""),

    # 2b. wager variant — chalk on a smooth pebble
    SubplotTemplate("""\
{hare_phrase} chalked a wager on a smooth round pebble {place}: whoever
predicted the result of {form_display} would drop {hare_his_her} pebble
in the pitcher first. The water at the bottom was cool but very low,
and a wrong guess sent a pebble in for nothing. {tortoise_phrase},
{emo_patient}, said it would be simpler to drop the form into the REPL
than to bicker about {concept_phrase} while the day grew hotter."""),

    # 2c. wager variant — twig in the dust beside the pitcher
    SubplotTemplate("""\
With a twig, {hare_phrase} marked out a wager in the dust beside the
pitcher {place}: whoever guessed the result of {form_display} first
would win the right to choose the next pebble to drop. The pitcher's
rim was high, the water far below, and every wasted guess made the
shadows feel longer. {tortoise_phrase}, {emo_patient}, said it was
easier to ask the REPL about {concept_phrase} than to argue."""),

    # 3. The teacher template — Tortoise is gently correcting Hare.
    #    NOTE: drops the "from a recent sprint" tail because EMO_TIRED
    #    entries already supply their own "from X" clause; doubling
    #    produced "from sprinting from a recent sprint" awkwardness.
    SubplotTemplate("""\
{tortoise_phrase} had been trying to teach {hare_phrase} how the REPL
works. The day was hot and the water in the nearby pitcher far below
the narrow rim — a fitting backdrop for a lesson about patience.
"Look here," {tortoise_he_she} said, {emo_patient}, pointing to
{concept_phrase}. "You hand the form {form_display} to the runtime,
the runtime evaluates step by step like pebbles dropping past the
narrow throat, and you read off what it returns." {hare}, {emo_tired},
agreed to try."""),

    # 4. The audience template — small forest creatures watch and learn.
    #    NOTE: rewritten so {concept_phrase} is referenced via "pointed to"
    #    rather than "read aloud" — abstract concept_phrases like "the
    #    equality (= 1 1)" / "the predicate (zero? 0)" don't fit
    #    "read aloud" semantically (you read FORMS aloud, not types).
    SubplotTemplate("""\
A small audience of meadow birds had perched on the rim of a tall
pitcher {place} to watch {hare_phrase} attempt to outwit
{tortoise_phrase} at reading the REPL. The day was hot, the water
inside lay cool but unreachable, and the answer was plain — every
onlooker craned a head down the narrow throat to see. {tortoise},
{emo_patient}, pointed to {concept_phrase} and read out the form
aloud: {form_display}. The crowd waited to see who would correctly
write the form to submit."""),

    # 5. The race-pause template — hare pauses mid-race, tortoise catches up
    #    via careful evaluation.
    #    NOTE: uses {hare} (the name) instead of {hare_he_she_cap} for the
    #    "called it impossible" sentence — for gender="n" characters,
    #    "They called it impossible." reads as plural-subject right after
    #    a singular "Pip the hare stopped" introduction.
    SubplotTemplate("""\
Halfway to the pitcher, {hare_phrase}, {emo_proud}, stopped {place}
and refused to take another step until someone could prove what the
form {form_display} evaluated to. The day was hot, {hare_his_her}
throat dry, and the water in the pitcher's narrow throat still far
below the rim. {hare} called the answer impossible to know.
{tortoise_phrase}, {emo_patient}, walking up at {tortoise_his_her}
usual pace, simply said: "Submit {concept_phrase} to the REPL.
Whatever comes back is the answer — the water will rise pebble by
pebble.\""""),

    # 6. The notebook template — the tortoise keeps a careful ledger.
    SubplotTemplate("""\
{tortoise_phrase}, {emo_patient}, had been keeping a small leather
notebook of every form {tortoise_he_she} had successfully evaluated —
each page like a pebble in the pitcher's growing pile, raising the
ledger's water-level of known answers a little further each time.
The notebook was nearly full, the day was hot, and the answer plain
on each careful entry. {place_idx}, the next entry was
{concept_phrase}. {hare_phrase}, {emo_proud}, peered over
{tortoise_his_her} shoulder at the form {form_display} and asked
what it would come out to.""".replace("{place_idx}", "Today {place}")),

    # 7. The boast-and-rebuke template — Hare claims to know without checking.
    #    NOTE: uses {hare_him_her} (object case) for "asked X to ..."; uses
    #    comma after "said" so participle-phrase EMO_PROUD entries
    #    ("boasting at every turn", "swaggering through the underbrush")
    #    parse as adverbial — without the comma, "said boasting" reads
    #    as agrammatical.
    SubplotTemplate("""\
"There is no need to evaluate that," {hare_phrase} said, {emo_proud},
the throat dry and the water at the pitcher's bottom still out of
reach. "Anyone can see what {concept_phrase} comes to." {tortoise_phrase},
who {place} had grown used to such claims, said {emo_patient} that the
narrow throat punished hasty answers, and asked {hare_him_her} to
actually write the form {form_display} and submit it to the REPL —
just to be sure."""),

    # 8. The puzzle-on-the-path template — they find a riddle on a sign.
    SubplotTemplate("""\
A clay tag tied around the tall pitcher's neck {place} carried a
puzzle. The riddle was simple: it asked the reader to evaluate
{form_display}. The day was hot, the water at the bottom cool but
narrow-throated, and a wrong guess sent a useless pebble in.
{hare} laughed, {emo_proud}, and declared it too easy. {tortoise}
said, {emo_patient}, that the only honest way to be sure of
{concept_phrase} — and to keep the rising pile of pebbles
purposeful — was to put it in the REPL."""),
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
At the foot of the tall pitcher {place}, {hare_phrase} sketched a
small wager into the dust: whoever could produce a form whose
evaluation would {goal_text} ahead of the other would win the cool
water lying low at the bottom. The throat was narrow — a hard
bottleneck for any rushed answer. {tortoise_phrase}, {emo_patient},
said it was simpler to write {concept_phrase} carefully than to
guess at the answer while the day grew hotter."""),

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
A small audience of meadow birds had perched on the rim of the tall
pitcher {place} to watch {hare_phrase} attempt to outwit
{tortoise_phrase} at writing the right form. The challenge:
{goal_text}. The day was hot, the water below the rim cool but
unreachable, and the throat was narrow. {tortoise}, {emo_patient},
reminded the crowd that what mattered was writing {concept_phrase}
carefully, then submitting it to the REPL — not guessing aloud at
the answer while pebbles waited at hand."""),

    # 5. The race-pause template — pause mid-race for a goal-write.
    #    Fix: drop "write a form to {goal_text}"; reframe as
    #    "until someone could {goal_text} with a Clojure form".
    SubplotTemplate("""\
Halfway through the race, {hare_phrase}, {emo_proud}, stopped {place}
and refused to continue until someone could {goal_text} with a
Clojure form. The day was hot, {hare_his_her} throat dry, and the
nearby pitcher's water still far below the narrow rim. {hare} called
the goal impossible. {tortoise_phrase}, {emo_patient}, walking up at
{tortoise_his_her} usual pace, simply said: "Compose {concept_phrase};
submit it. Whatever comes back is the answer.\""""),

    # 6. The notebook template — Tortoise records goal/form pairs.
    SubplotTemplate("""\
{tortoise_phrase}, {emo_patient}, kept a small bark-strip ledger of
every goal {tortoise_he_she} had translated into a Clojure form —
each entry a pebble's worth of progress, the ledger's mark-count
rising slowly the way the pitcher's water rose with patient drops.
Today {place}, the next entry was a goal: {goal_text}. {tortoise}
sat with pen in hand, ready to compose {concept_phrase}, then let
the REPL confirm the value."""),

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
A clay tag tied around the tall pitcher's neck {place} carried a
small puzzle. The challenge was simple: {goal_text}. The day was
hot, the water at the pitcher's bottom cool but narrow-throated.
{hare} laughed, {emo_proud}, and declared it too easy. {tortoise}
said, {emo_patient}, that the only way to be sure of
{concept_phrase} was to write the form and put it in the REPL —
not to guess at the value from the goal alone, like a pebble flung
without aim."""),

    # 9. The Hare-stumbles template — Hare's hurry betrays him; the
    #    Tortoise's careful form returns the value first. Delivers
    #    the fable's moral (vanity vs. steadiness) directly.
    SubplotTemplate("""\
"This is nothing," {hare_phrase} scoffed, {emo_proud}, the day hot
and the throat dry. "I can {goal_text} in my sleep." {hare} grabbed
a stick and dashed off a few characters in the dust — but a paren
went missing, an operand fell out of place, and the form did not
even read as Clojure. The pitcher stood narrow and tall, the water
inside still as far below as a bad guess could leave it.
{tortoise_phrase}, {emo_patient}, had already written
{concept_phrase} on a smooth pebble, neat and unhurried, and
submitted it to the REPL. The value came back as quietly as
{tortoise_he_she} had written, and the water in the pitcher seemed
to rise a finger's width."""),

    # 10. The race-against-the-REPL template — wager on speed-of-
    #     answering, Tortoise's careful path wins. Moral lands.
    SubplotTemplate("""\
The wager was set {place}: produce the value before the breeze had
turned the next leaf. The day was hot and the pitcher's water lay
low; a wrong guess wasted the breeze and the whole pebble both.
{hare_phrase}, {emo_proud}, bolted into a flurry of guesses, calling
out numbers and second-guessing {hare_him_her}self about whether
the goal was to {goal_text} or something close to it.
{tortoise_phrase}, {emo_patient}, walked to the slate and began to
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
    fable="crow-pitcher",
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
    fable="crow-pitcher",
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
    fable="crow-pitcher",
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
    fable="crow-pitcher",
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
    fable="crow-pitcher",
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
    fable="crow-pitcher",
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
    fable="crow-pitcher",
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
    fable="crow-pitcher",
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(symbol? 'hare)",
            expected=True,
            concept_phrase="the symbol-predicate on a quoted name",
            question_what="whether a quoted name is a symbol",
            goal_text="ask whether a quoted name is a symbol, using the symbol? predicate",

            scenario=(
                "Caw held up a chalk-scratched mark — the name 'hare — and "
                "pointed first at the chalk on her talon, then at an actual hare "
                "bounding across the meadow. She set the chalk mark beside "
                "the pitcher's rim."
            ),
            need=(
                "She wanted to know whether the runtime would confirm the "
                "chalk mark as a name-thing — a symbol — not the bounding hare."
            ),
            mapping=(
                "Quoting (the leading apostrophe) wraps the name as a chalk "
                "mark, preventing evaluation. `symbol?` asks the runtime: "
                "is this a name-mark? A quoted name is a symbol — chalk, not hare."
            ),
            resolution=(
                "true — the runtime confirmed: 'hare is a chalk mark, "
                "a symbol, not the bounding creature the name might refer to."
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
                "Korvus held a smooth stone marked with the notch-count forty-two "
                "at the orchard pitcher's rim. No chalk mark — just the stone "
                "itself, solid and countable, resting in his talon."
            ),
            need=(
                "He needed the runtime to confirm whether a bare stone-count "
                "could ever be a chalk-mark name, or only ever a value."
            ),
            mapping=(
                "`symbol?` asks: is this thing a name-mark, not a value? "
                "An integer is a stone, not chalk — it carries a count, "
                "not a name. The predicate draws the line cleanly."
            ),
            resolution=(
                "The gate returned the negative verdict: a bare stone-count "
                "is no chalk mark. (with {drawn.a} folded in)"
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
                "Sable scratched a row of letters between quote-marks on the "
                "pitcher's clay at the village square: the word tortoise, "
                "enclosed, a bound sequence of characters rather than a bare name."
            ),
            need=(
                "Sable wanted to know whether the runtime would treat the "
                "quoted word as a symbol — a chalk-mark name — or merely a string."
            ),
            mapping=(
                "A string in double-quotes is a sequence of characters, not a "
                "name-mark. `symbol?` only returns the positive verdict for "
                "quoted bare names, not for enclosed letter-sequences."
            ),
            resolution=(
                "The gate closed: a quoted word-sequence is no chalk-mark name, "
                "only a string."
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
                "Caw drew two identical chalk marks on the pitcher's rim at "
                "the hilltop — each a quoted name-shape, side by side, "
                "neither one pointing at any creature below."
            ),
            need=(
                "She needed to know whether two chalk marks scratched with the "
                "same strokes would read as equal at the dual-gate check."
            ),
            mapping=(
                "`=` compares its arguments directly. Two quoted name-marks "
                "of the same shape are the same chalk-mark: the gate reads them "
                "together and confirms the match."
            ),
            resolution=(
                'The gate closed in agreement: two identical chalk marks are equal, the confirmation returned (with `hare` as the input value).'
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(+ 1 2) ; sum of one and two",
            expected=3,
            concept_phrase="the addition with a trailing comment",
            question_what="the result, ignoring the comment",
            goal_text="add 1 and 2, with a single-semicolon trailing comment",

            scenario=(
                "Korvus scratched a stone-drop form onto the pitcher's rim "
                "in the garden: `(+ 1 2)`. Beside it he pressed the finest "
                "tip of his talon to the clay and added a marginal note: "
                "`; sum of one and two` — a reader-note, not part of the drop."
            ),
            need=(
                "He wanted the form to evaluate as usual, the marginal note "
                "silent, the REPL reading only the form to the semicolon's left."
            ),
            mapping=(
                "The semicolon marks everything to its right as a scribe-note: "
                "the reader ignores it completely. Only the form before the "
                "semicolon enters the pitcher and drops as a stone."
            ),
            resolution=(
                "The sum arrived unchanged, the marginal note never "
                "entering the water, exactly as the scribe intended. (with {drawn.a} folded in)"
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
                "Sable scratched the stone-count forty-two on the garden pitcher's "
                "rim, then pressed two talon-tips side by side — a double-semicolon "
                "mark — and wrote a reader-note trailing behind it."
            ),
            need=(
                "Sable needed the pitcher to return the count alone, the "
                "double-semicolon note staying silent on the clay."
            ),
            mapping=(
                "Double-semicolon is still a semicolon mark: everything to the "
                "right is scribe-notation, invisible to the runtime. Only the "
                "value before the mark drops into the pitcher."
            ),
            resolution=(
                "The count returned unchanged, the note never entering the water, "
                "just as the double mark promised. (with {drawn.a} folded in)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(+    1    2)",
            expected=3,
            concept_phrase="the addition with extra spacing",
            question_what="the result of an addition formatted with extra spaces",
            goal_text="add 1 and 2 in a form with extra spaces between tokens",

            scenario=(
                "Korvus scratched a stone-drop form on the market pitcher's clay, "
                "pressing extra gaps between each token — wide spaces separating "
                "the operator from both stone-counts on the rim."
            ),
            need=(
                "He needed to confirm the reader would collapse the spacing and "
                "still see one clean form, not three separate marks."
            ),
            mapping=(
                "The reader discards extra whitespace between tokens; gaps are "
                "invisible after reading. The runtime receives the same clean "
                "form regardless of how wide the spaces were scratched."
            ),
            resolution=(
                "The expected sum returned, the extra spacing having vanished "
                "before the form ever reached the pitcher. (with {drawn.a} folded in)"
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
                "Caw scratched the same stone-drop form across three separate lines "
                "on the road-side pitcher: the operator on one line, each stone-count "
                "indented on its own line below."
            ),
            need=(
                "She needed the REPL to read all three lines as one form, "
                "not as separate marks, and return the single sum."
            ),
            mapping=(
                "Newlines are whitespace: the reader joins them with the spaces "
                "and hands the runtime one clean, complete form. Line breaks "
                "have no effect on what the form computes."
            ),
            resolution=(
                "The correct sum returned, the line breaks invisible to the "
                "runtime just as any other spacing would be. (with {drawn.a} folded in)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(+ 2 3)",
            expected=5,
            concept_phrase="the simple addition",
            question_what="the result of adding 2 and 3",
            goal_text="add 2 and 3",

            scenario=(
                "Sable pressed two curved talon-arcs around a stone-drop group "
                "on the meadow pitcher — open-paren, two stone-counts, close-paren — "
                "the parens hugging the stones into one grouped form."
            ),
            need=(
                "Sable needed to confirm the parens grouped the drop and did not "
                "multiply anything — that the form returned only the counted sum."
            ),
            mapping=(
                "Parens delimit a call: the first token inside is the operator, "
                "the rest are arguments. They group, they do not multiply. "
                "The runtime reads the group and applies the operator to the stones."
            ),
            resolution=(
                "The sum returned, the parens having grouped the form cleanly "
                "without adding any multiplication. (with {drawn.a} folded in)"
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
                "Korvus scratched two nested paren-groups on the orchard pitcher: "
                "an inner group summing two stones, the whole thing wrapped in "
                "an outer group that multiplied the result by a third stone."
            ),
            need=(
                "He needed the inner group to resolve first and its result to "
                "be passed as an argument to the outer multiplication."
            ),
            mapping=(
                "The reader sees two grouped forms: the inner parens are one "
                "complete call, its value becoming an argument to the outer call. "
                "Nesting is grouping all the way down; each group is one form."
            ),
            resolution=(
                "The nested product returned, the inner sum resolved before "
                "the outer multiplication ever ran. (with {drawn.a} folded in)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(+ 1 2)",
            expected=3,
            concept_phrase="the addition",
            question_what="the sum of 1 and 2",
            goal_text="add 1 and 2",

            scenario=(
                "Korvus crouched at the tall clay pitcher's rim at the farm's "
                "yard, two handfuls of smooth stones — one stone in his left "
                "talon, two in his right."
            ),
            need=(
                "He wanted to count the total stones in both talons to know "
                "how far the water would rise when both handfuls dropped together."
            ),
            mapping=(
                "`+` is the stone-count call: it totals the numbers it receives, "
                "left to right. One stone plus two stones gives a total the "
                "runtime calculates and returns as the water-level."
            ),
            resolution=(
                "The two handfuls combined, the water rising to the "
                "expected notch at beak-reach. (with {drawn.a} folded in)"
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
                "Caw stood at the farm pitcher's rim with five smooth stones "
                "in one talon and lifted three away, setting them aside on the "
                "ground before dropping the remainder into the water."
            ),
            need=(
                "She needed the runtime to return the count of what remained "
                "after the the stones were lifted away."
            ),
            mapping=(
                "`-` removes the second stone-count from the first. the stones "
                "less three gives the smaller heap; the runtime counts what's left "
                "and returns it as the water-level."
            ),
            resolution=(
                "The remaining count returned, the heap diminished by exactly "
                "the stones lifted away. (with {drawn.a} folded in)"
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
                "Korvus arranged four rows of stones on the hilltop pitcher's "
                "rim, the stones in each row, tallying how many stones he would "
                "need in total before dropping them all at once."
            ),
            need=(
                "He needed the runtime to count the total by repeating the "
                "row-count as many times as there were rows."
            ),
            mapping=(
                "`*` repeats the addition of the first count as many times as "
                "the second count says. Four rows of the stones gives the full "
                "heap; the runtime returns the exact product."
            ),
            resolution=(
                "The total stone-count returned, the full heap tallied without "
                "a single stone miscounted. (with {drawn.a} folded in)"
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
                "Sable stood at the garden pitcher's rim with the stones and "
                "two waiting spots on the clay, sorting the pile evenly into "
                "both spots before counting what each portion held."
            ),
            need=(
                "Sable needed to know how many stones would land in each even "
                "portion if the heap were split exactly in two."
            ),
            mapping=(
                "`/` divides the first stone-count into as many equal parts as "
                "the second count says. the stones split evenly into two portions "
                "gives the per-portion count the runtime returns."
            ),
            resolution=(
                "The even-split count returned, each portion holding the same "
                "number of stones. (with {drawn.a} folded in)"
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
                "Caw crouched at the orchard pitcher's rim, the stones in "
                "her left talon and eight in her right, both handfuls poised "
                "above the water."
            ),
            need=(
                "She wanted the runtime to count both handfuls as one heap and "
                "return the combined total before dropping."
            ),
            mapping=(
                "`+` sums all its stone-counts, left to right. Seven plus eight "
                "gives a single total the runtime counts precisely and returns "
                "as the water-level reading."
            ),
            resolution=(
                "The combined count returned, both handfuls measured together "
                "in a single stone-count call. (with {drawn.a} folded in)"
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
                "Korvus counted twenty smooth stones piled on the road-side "
                "pitcher's rim, then moved seven to one side, studying the "
                "smaller heap that remained before submitting the form."
            ),
            need=(
                "He needed the runtime to confirm how many stones remained "
                "after the seven were removed from the full pile."
            ),
            mapping=(
                "`-` takes the second stone-count away from the first. Twenty "
                "stones less seven leaves the remainder the runtime counts exactly "
                "and returns as the water-level."
            ),
            resolution=(
                'The remainder returned, the heap diminished and the count precise (with `20` as the input value).'
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(+ 1 (* 2 3))",
            expected=7,
            concept_phrase="the nested computation",
            question_what="the sum of 1 with the product of 2 and 3",
            goal_text="add 1 to the product of 2 and 3",

            scenario=(
                "Sable stood at the meadow pitcher's rim with one loose stone "
                "and two small groups of the stones each, the grouped stones "
                "nested inside the outer count like a bag within a bag."
            ),
            need=(
                "Sable needed the inner group to resolve first, its product "
                "becoming the second stone-count in the outer addition."
            ),
            mapping=(
                "Clojure evaluates the inner call first, its result becoming an "
                "argument for the outer call. The nested stone-count resolves to "
                "a single value, then the outer addition runs with that value."
            ),
            resolution=(
                "The outer sum returned, the inner product having resolved "
                "before the addition ever ran. (with {drawn.a} folded in)"
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
                "Korvus arranged two small heaps on the farm pitcher's rim — "
                "one of the stones summed from two groups, another of seven "
                "summed from two groups — before multiplying the resolved heaps together."
            ),
            need=(
                "He needed both inner sums to resolve into single counts "
                "before the outer multiplication could combine them."
            ),
            mapping=(
                "Both inner calls resolve to stone-counts first; the runtime "
                "then multiplies those two counts. Each nested group is evaluated "
                "before the outer operator receives its arguments."
            ),
            resolution=(
                "The product returned, both nested sums resolved and then "
                "multiplied by the outer call. (with {drawn.a} folded in)"
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
                "Caw started with a full hundred-stone pile at the hilltop "
                "pitcher's rim, a nested multiplication group waiting to resolve "
                "into the count she needed to remove."
            ),
            need=(
                "She needed the inner product to resolve first so the outer "
                "subtraction could lift exactly that many stones away."
            ),
            mapping=(
                "The nested multiplication resolves to its product first; the "
                "outer subtraction then removes that count from one hundred. "
                "Inner calls always resolve before the outer operator receives them."
            ),
            resolution=(
                "The diminished count returned, the inner product resolved "
                "and removed from the outer pile. (with {drawn.a} folded in)"
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
                "Korvus scratched two product-groups on the garden pitcher's "
                "rim — each a nested multiplication — and planned to drop their "
                "combined result into the water as one outer addition."
            ),
            need=(
                "He needed both nested products to resolve into single "
                "stone-counts before the outer addition combined them."
            ),
            mapping=(
                "Each nested multiplication resolves independently; the outer "
                "addition then sums the two resulting counts. Resolution flows "
                "from the inside out, group by group."
            ),
            resolution=(
                "The combined total returned, both inner products resolved and "
                "then added together by the outer call. (with {drawn.a} folded in)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(= 1 1)",
            expected=True,
            concept_phrase="the equality check",
            question_what="whether 1 equals 1",
            goal_text="test whether 1 equals 1 with =",

            scenario=(
                "Caw held two unmarked stones up at the pitcher's mouth in "
                "the village, one in each talon, both carrying the count 1. "
                "She set them side by side at the dual-gate check."
            ),
            need=(
                "Only if both gate-arms confirmed the same count would the "
                "form return true and the beak dip to drink."
            ),
            mapping=(
                "`=` checks whether all its arguments are equal. Both gate-arms "
                "read 1; both close together. With both gates cleared the "
                "runtime returns the confirmation: true."
            ),
            resolution=(
                "true — both gates closed in agreement, the counts identical, "
                "the confirmation dropping into the pitcher. (with {drawn.a} folded in)"
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
                "Korvus held one stone in his left talon and two in his right "
                "at the orchard pitcher's mouth, setting both at the dual-gate "
                "check side by side."
            ),
            need=(
                "He needed the gate-arms to read both counts and report whether "
                "they matched — one stone against two."
            ),
            mapping=(
                "`=` passes its arguments through the dual-gate check. One stone "
                "and two stones carry different counts; the gate-arms find no "
                "match and swing to the rejection position."
            ),
            resolution=(
                "The gate returned the negative verdict: the counts differed, "
                "the arms refusing to close together. (with {drawn.a} folded in)"
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
                "Sable scratched two identical single-letter marks — both the "
                "letter a, each enclosed in talon-arcs — at the meadow pitcher's "
                "dual-gate check, one mark per gate-arm."
            ),
            need=(
                "Sable needed the gate to confirm that two enclosed letter-marks "
                "of identical shape would count as equal at the check."
            ),
            mapping=(
                "`=` checks strings by their contents, letter by letter. "
                "Both enclosed marks hold the same single character; "
                "the gate-arms read identically and close in agreement."
            ),
            resolution=(
                "The gate confirmed agreement: the two letter-marks matched "
                "and the arms closed together. (with {drawn.a} folded in)"
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
                "Caw placed two colon-prefixed name-stones on the road-side "
                "pitcher's rim — both the keyword :hare, each identical in "
                "marking — and set them at the dual-gate check."
            ),
            need=(
                "She needed the gate to confirm whether two identical "
                "colon-prefixed name-stones would read as equal."
            ),
            mapping=(
                "Keywords are interned: every `:hare` is the same object in "
                "the runtime. The gate-arms both receive the same name-stone "
                "and close together without hesitation."
            ),
            resolution=(
                "The gate confirmed the match: both colon-prefixed name-stones "
                "were identical, the arms closing in agreement. (with {drawn.a} folded in)"
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
                "Korvus brought two differently marked colon-prefixed name-stones "
                "to the hilltop pitcher's dual-gate check — one marked :hare "
                "and one marked :tortoise."
            ),
            need=(
                "He needed the gate-arms to report whether two different "
                "name-stones carried equal identity or merely similar form."
            ),
            mapping=(
                "`=` on two differently named keywords compares their interned "
                "identity: `:hare` and `:tortoise` are distinct objects in the "
                "runtime, and the gate-arms read different marks."
            ),
            resolution=(
                "The gate returned the rejection: the two name-stones were "
                "distinct, the arms unable to close together. (with {drawn.a} folded in)"
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
                "Sable lined up four single stones at the garden pitcher's "
                "dual-gate check, each carrying the count one, presenting "
                "all four to the gate at the same time."
            ),
            need=(
                "Sable needed the gate to confirm all the stones carried "
                "identical counts — a multi-stone check, not just a pair."
            ),
            mapping=(
                "`=` accepts any number of arguments and confirms all equal. "
                "the stones each carrying the count one pass the gate-arms "
                "in sequence; every comparison matches."
            ),
            resolution=(
                "The gate confirmed unanimous agreement: all the stone-counts "
                "matched, the arms closing with each comparison. (with {drawn.a} folded in)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(zero? 0)",
            expected=True,
            concept_phrase="the zero check",
            question_what="whether 0 is zero",
            goal_text="check whether 0 is zero using zero?",

            scenario=(
                "Korvus stood at the farm pitcher's rim with an empty talon — "
                "no stones at all — and held it over the zero-notch before "
                "putting the question to the runtime."
            ),
            need=(
                "He needed the runtime to confirm whether an empty talon "
                "truly counted as the zero stone-count."
            ),
            mapping=(
                "`zero?` tests whether its stone-count argument is exactly "
                "nothing — not negative, not positive, but the empty notch. "
                "An empty talon matches the zero-notch precisely."
            ),
            resolution=(
                "The positive verdict returned: the empty talon held the zero "
                "count, confirmed by the predicate. (with {drawn.a} folded in)"
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
                "Caw held five smooth stones at the orchard pitcher's rim, "
                "talon clearly full, and put the zero-check to the runtime "
                "despite the obvious weight in her grip."
            ),
            need=(
                "She needed the runtime to report whether the stones in "
                "the talon could ever pass the empty-talon test."
            ),
            mapping=(
                "`zero?` checks for the empty notch only. the stones is a "
                "non-empty count; the predicate finds the talon occupied and "
                "returns the negative verdict without hesitation."
            ),
            resolution=(
                "The negative verdict returned: the stones is not zero, "
                "the talon far from empty. (with {drawn.a} folded in)"
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
                "Sable placed the stones above the zero-notch scratch on the "
                "meadow pitcher's rim — clearly on the positive side of the "
                "mark — and submitted the positive-check to the runtime."
            ),
            need=(
                "Sable needed the runtime to confirm whether the stones "
                "above the zero-notch satisfied the positive-side test. (with {drawn.a} folded in)"
            ),
            mapping=(
                "`pos?` checks whether the stone-count sits above the zero-notch. "
                "the stones land squarely on the positive side; "
                "the predicate confirms the verdict."
            ),
            resolution=(
                "The positive verdict returned: the stones above the notch "
                "satisfied the positive-side test."
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
                "Korvus scratched a count two notches below the zero-mark on "
                "the road-side pitcher — a below-zero stone-debt — and asked "
                "the runtime to run the positive-check on it."
            ),
            need=(
                "He needed to know whether a count sitting below the zero-mark "
                "could pass the positive-side test."
            ),
            mapping=(
                "`pos?` rejects any count at or below the zero-notch. A stone-debt "
                "sits below the mark; the predicate finds it on the wrong side "
                "and returns the negative verdict."
            ),
            resolution=(
                'The negative verdict returned: a below-zero count does not pass the positive-side test (with `-2` as the input value).'
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
                "Caw scratched a three-notch debt mark below the zero-line on "
                "the garden pitcher, three notches under the waterline, and "
                "submitted the below-zero check to the runtime."
            ),
            need=(
                "She needed the runtime to confirm that a count sitting three "
                "notches below zero would pass the negative-side test."
            ),
            mapping=(
                "`neg?` confirms any count that sits below the zero-notch. "
                "Three notches under the waterline is clearly on the negative "
                "side; the predicate returns the positive verdict."
            ),
            resolution=(
                "The positive verdict returned: a below-zero count satisfies "
                "the negative-side test. (with {drawn.a} folded in)"
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
                "Korvus held the stones clearly above the zero-notch at the "
                "market pitcher's rim and put the negative-side test to the "
                "runtime despite the count sitting in positive territory."
            ),
            need=(
                "He needed the runtime to confirm whether the stones above "
                "zero could pass the below-zero test. (with {drawn.a} folded in)"
            ),
            mapping=(
                "`neg?` only passes counts that sit below the zero-notch. "
                "the stones above the mark are on the positive side; "
                "the predicate finds the count above the line and rejects it."
            ),
            resolution=(
                "The negative verdict returned: the stones above zero do not "
                "satisfy the below-zero test."
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="42",
            expected=42,
            concept_phrase="the literal 42",
            question_what="the value 42 returned by the REPL",
            goal_text="submit the integer 42 so the REPL returns it",

            scenario=(
                "Sable scratched only the count mark onto the orchard pitcher's "
                "clay — the bare stone-count, nothing else — and watched the "
                "water to see what came back."
            ),
            need=(
                "Sable needed to confirm that the REPL returns the literal "
                "value directly, not a side-effect splash — the value rising "
                "in the water itself."
            ),
            mapping=(
                "A bare literal is both the form and the return: the reader "
                "hands it to the runtime, the runtime evaluates it to itself, "
                "and the water level rises to that value. Nothing is printed separately."
            ),
            resolution=(
                "The literal value rose in the water, returned by the REPL "
                "as the form's own value. (with {drawn.a} folded in)"
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
                "Caw scratched the stone-drop addition form on the hilltop "
                "pitcher's clay and waited at the rim, watching for the water "
                "to carry the result back — not a splash announcement, the value itself."
            ),
            need=(
                "She needed to see the result in the water level, returned "
                "by the REPL, not echoed as a separate side-effect mark beside it."
            ),
            mapping=(
                "The REPL returns the value of every form it evaluates; the "
                "return is the water rising, not a printed note beside it. "
                "The addition's result comes back through the return path alone."
            ),
            resolution=(
                "The sum rose in the water, returned directly by the REPL "
                "as the form's evaluated value. (with {drawn.a} folded in)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(+ 1 2)",
            expected=3,
            concept_phrase="the addition",
            question_what="the result of adding 1 and 2",
            goal_text="add 1 and 2",

            scenario=(
                "Sable spread a patch of soft moss on the ground beneath the "
                "garden pitcher before dropping any stone — a safety pad in "
                "place, ready to catch any mis-drop without harm."
            ),
            need=(
                "Sable needed to confirm that a well-formed stone-drop would "
                "return the correct count even with the moss in place below."
            ),
            mapping=(
                "The moss patch changes nothing when the drop succeeds: it only "
                "matters if something goes wrong. A correct addition returns its "
                "value as usual, the moss untouched and the pitcher undisturbed."
            ),
            resolution=(
                "The expected sum came back, the moss never needed, "
                "the REPL untroubled by the safety pad beneath. (with {drawn.a} folded in)"
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
                "Korvus laid a wide moss pad beneath the hilltop pitcher, "
                "then arranged seven rows of the stones on the rim, ready to "
                "drop the product-form with the safety net in place."
            ),
            need=(
                "He needed the REPL to return the full product and show that "
                "the moss pad had not disrupted any correct drop."
            ),
            mapping=(
                "A correctly formed multiplication drop needs no safety catch; "
                "the moss is there for errors, not for successes. The runtime "
                "computes the product and returns it, the pad below irrelevant."
            ),
            resolution=(
                "The full product returned, the moss untouched, the pitcher's "
                "water rising to the correct level. (with {drawn.a} folded in)"
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
    print(f"grade-1 crow-pitcher smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
