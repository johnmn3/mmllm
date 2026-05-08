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
from mmllm.aesop.curriculum.dog_shadow._metaphor_pools import (
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
{hare} and {tortoise_phrase} paused on the river bank where
someone had scratched {concept_phrase} into the wet sand. The water
ran clear and the bridge cast a long, trembling shadow.
{hare}, {emo_proud}, said the answer was plain — anyone could see
it on the surface. {tortoise}, {emo_patient}, said the surface only
shows what the surface shows: the form {form_display}, dropped into
the REPL, would tell what the value really was."""),

    # 2. The wager template — bets on what the form returns.
    SubplotTemplate("""\
By a flat stone at the stream's edge {place}, {hare} scratched
a small wager: whoever guessed the result of {form_display} first
would carry the bone home. The water ran past, indifferent.
{tortoise_phrase}, {emo_patient}, said it was simpler to drop the
form into the REPL than to argue at the bank — a guess at a
reflection costs more than reading the real bone."""),

    # 2b. wager variant — chalk on stone
    SubplotTemplate("""\
{hare} chalked a wager on a flat stone {place}: whoever
predicted the result of {form_display} would set who crossed the
bridge first. {tortoise_phrase}, {emo_patient}, said it would be
simpler to type the form into the REPL than to bicker at the
water's edge over {concept_phrase}."""),

    # 2c. wager variant — twig in the path
    SubplotTemplate("""\
With a twig, {hare} marked a wager into the wet sand {place}:
whoever guessed the result of {form_display} first would choose
which bone to carry. {tortoise_phrase}, {emo_patient}, said it was
easier to ask the REPL about {concept_phrase} than to argue with
a reflection that gave nothing back."""),

    # 3. The teacher template — Hound is gently correcting the greedy dog.
    SubplotTemplate("""\
{tortoise} had been showing {hare_phrase} how the REPL works,
the stream cool against their paws and the bridge's shadow long.
"Look here," {tortoise_he_she} said, pointing to {concept_phrase}.
"You hand the form {form_display} to the runtime — the runtime is
the stream's honest reading, not the surface guess — and it gives
back what the form really is." {hare}, {emo_tired}, agreed to try."""),

    # 4. The audience template — small stream-side creatures watch.
    SubplotTemplate("""\
A few stream-side creatures had gathered on the bank {place} to
watch {hare} attempt to outwit {tortoise_phrase} at reading
the REPL. The water moved on, the bridge held its shadow, and
{tortoise}, {emo_patient}, pointed to {concept_phrase} and read the
form aloud: {form_display}. The crowd waited to see who would
correctly write the form to submit."""),

    # 5. The race-pause / bone-pause template — hare pauses; tortoise
    #    catches up by careful reading.
    SubplotTemplate("""\
Halfway across the bridge, {hare} stopped {place} and refused
to take another step until someone could prove what the form
{form_display} evaluated to. The reflection below glittered.
{hare} called the answer impossible to know. {tortoise_phrase},
{emo_patient}, walking up at {tortoise_his_her} usual pace, simply
said: "Submit {concept_phrase} to the REPL. The water shows a
shadow; the form shows the bone.\""""),

    # 6. The notebook template — the hound keeps a careful tally on bark.
    SubplotTemplate("""\
{tortoise}, {emo_patient}, had been keeping a small
bark-scratch tally of every form {tortoise_he_she} had successfully
evaluated — each new mark deepening the line and crowding out the
day's wishful guesses. {place_idx}, the next entry was
{concept_phrase}. {hare_phrase} peered over {tortoise_his_her}
shoulder at the form {form_display} and asked what it would come
out to.""".replace("{place_idx}", "Today {place}")),

    # 7. The boast-and-rebuke template — the greedy dog claims to know;
    #    the hound asks for the actual form.
    SubplotTemplate("""\
"There is no need to evaluate that," {hare} said, {emo_proud},
the bone clamped tight in {hare_his_her} jaws. "Anyone can see what
{concept_phrase} comes to." {tortoise_phrase}, who {place} had grown
used to such claims, asked {hare_him_her} to actually write the
form {form_display} and submit it to the REPL — a reflection
sounds confident but does not eat."""),

    # 8. The puzzle-on-the-bridge template — they find a riddle scratched
    #    on the bridge plank.
    SubplotTemplate("""\
A puzzle was scratched onto the bridge plank {place}. The riddle
was simple: it asked the reader to evaluate {form_display}.
{hare} laughed, {emo_proud}, and declared it too easy. {tortoise}
said, {emo_patient}, that the only way to be sure of
{concept_phrase} was to put it in the REPL — the bridge's shadow
shifts, but the form's value does not."""),
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
{hare} and {tortoise_phrase} stopped {place} to settle a small
puzzle. {hare} wanted to {goal_text}. {hare}, {emo_proud}, declared
that {hare_he_she} could write the form for it without thinking.
{tortoise}, {emo_patient}, suggested {hare_he_she} actually write
{concept_phrase} carefully — and then let the REPL confirm what
the value really was."""),

    # 2. The wager template — bet on writing the right form.
    #    Fix: drop "write a form to" verb-on-verb collision; use
    #    "produce a form whose evaluation would" (noun-clause framing).
    SubplotTemplate("""\
By a flat stone at the stream's edge {place}, {hare} scratched
a wager: whoever could produce a form whose evaluation would
{goal_text} ahead of the other would carry the bone home.
{tortoise_phrase}, {emo_patient}, said it was simpler to write
{concept_phrase} carefully than to guess at the answer like a dog
snapping at a reflection."""),

    # 3. The teacher template — Hound teaches the greedy dog goal → form.
    SubplotTemplate("""\
{tortoise} had been showing {hare_phrase} how to translate a
goal into a Clojure form, the bridge's shadow long across the water.
"If you want to {goal_text}," {tortoise_he_she} said, "you write
{concept_phrase}; submit that to the REPL — the runtime is the
honest reading of the bone, not a guess at the reflection." {hare},
{emo_tired}, agreed to try writing it."""),

    # 4. The audience template — onlookers wait by the bank.
    SubplotTemplate("""\
A few stream-side creatures had gathered on the bank {place} to
watch {hare} attempt to outwit {tortoise_phrase}, {emo_patient} at writing
the right form. The challenge: {goal_text}. {tortoise} reminded
the bank that what mattered was writing {concept_phrase} carefully,
then submitting it to the REPL — not snapping at a guess that
glittered on the water."""),

    # 5. The bridge-pause template — pause mid-bridge for a goal-write.
    SubplotTemplate("""\
Halfway across the bridge, {hare} stopped {place} and refused
to take another step until someone could {goal_text} with a
Clojure form. The reflection wavered below. {hare} called the goal
impossible. {tortoise_phrase}, {emo_patient}, walking up at {tortoise_his_her}
usual pace, simply said: "Compose {concept_phrase}; submit it.
Whatever comes back is the answer.\""""),

    # 6. The bark-tally template — Hound records goal/form pairs.
    SubplotTemplate("""\
{tortoise}, {emo_patient} kept a small bark-scratch tally of every goal
{tortoise_he_she} had translated into a Clojure form, the deepest
marks scoring out the day's wishful guesses. Today {place}, the
next entry was a goal: {goal_text}. {tortoise} stood ready to
compose {concept_phrase}, then let the REPL confirm the value."""),

    # 7. The boast-and-rebuke template.
    SubplotTemplate("""\
"There is no challenge here," {hare} said, {emo_proud},
the bone clamped tight in {hare_his_her} jaws. "Anyone could
{goal_text} without thinking." {tortoise_phrase}, who {place} had
grown used to such claims, asked {hare_him_her} to actually write
{concept_phrase}, then submit it to the REPL — a reflection looks
generous, but only the form delivers."""),

    # 8. The puzzle-on-the-bridge template.
    SubplotTemplate("""\
A small puzzle was scratched onto the bridge plank {place}. The
challenge was simple: {goal_text}. {hare} laughed, {emo_proud},
and declared it too easy. {tortoise} said, {emo_patient}, that
the only way to be sure of {concept_phrase} was to write the form
and put it in the REPL — guessing from the surface gives only
the surface back."""),

    # 9. The dog-stumbles template — dog's hurry betrays him; the
    #    hound's careful form returns the value first.
    SubplotTemplate("""\
"This is nothing," {hare} scoffed, {emo_proud}, the bone
heavy in {hare_his_her} jaws. "I can {goal_text} in my sleep."
{hare} dropped the bone reaching for the reflection — but a paren
went missing in {hare_his_her} hurry, an operand fell out of
place, and the form did not even read as Clojure.
{tortoise_phrase}, {emo_patient}, had already written
{concept_phrase} on a flat stone, neat and unhurried, and
submitted it to the REPL. The value came back as quietly as
{tortoise_he_she} had written. {hare} stared at the empty water
where the real bone had sunk."""),

    # 10. The race-against-the-REPL template.
    SubplotTemplate("""\
A wager was set {place}: produce the value before the next ripple
crossed the pond. {hare} bolted into a flurry of guesses,
calling out numbers and second-guessing {hare_him_her}self about
whether the goal was to {goal_text} or something close to it.
{tortoise_phrase}, {emo_patient}, who had simply walked to a flat stone and
begun to write {concept_phrase}, finished the form, submitted it,
and read the value off the REPL while {hare} was still arguing
with {hare_his_her} own reflection. The race, like every other,
went to the steady hand."""),

    # 11. The wrong-guess-then-form template.
    SubplotTemplate("""\
{hare} squinted at the goal — to {goal_text} — and blurted
out a confident guess, {emo_proud}, as though the loudness of a
guess could make it true. {tortoise_phrase} did not argue.
{tortoise_he_she_cap} simply wrote {concept_phrase} on a flat
stone by the bridge, submitted it to the REPL, and held up the
value the runtime returned. The crowd compared the two: the
hare's guess shimmered like a reflection; the form's value held
firm."""),

    # 12. The patient-explanation template.
    SubplotTemplate("""\
"You always insist on writing it out," {hare} complained,
{emo_proud}. "I can see the answer from here." {tortoise_phrase}
shook {tortoise_his_her} head slowly, the river running on past.
"To {goal_text}, the eye is no help — only the form is. The
reflection moves; the form does not. Watch." {tortoise_he_she_cap}
wrote {concept_phrase} in careful strokes, submitted it to the
REPL, and let the returned value speak for itself. {hare},
{emo_tired}, admitted that this time, again, the patient way had
carried the day."""),
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
    fable="dog-shadow",
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
    fable="dog-shadow",
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
    fable="dog-shadow",
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
    fable="dog-shadow",
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
    fable="dog-shadow",
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
    fable="dog-shadow",
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
    fable="dog-shadow",
    examples=[
        _ex(":hare",    ":hare",    "the literal keyword",
            "the value of the keyword"),
        _ex(":tortoise",":tortoise", "the literal keyword",
            "the value of the keyword"),
        _ex(":winner",   ":winner", "the literal keyword",
            "the value of the keyword"),
        _ex("(keyword? :hare)", True,
            "the keyword? predicate on a literal keyword",
            "whether the literal keyword is a keyword"),
        _ex("(= :hare :hare)", True,
            "the equality of two identical keywords",
            "whether two identical keywords are equal"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-08 — Characters
G1_08 = SubjectCurriculum(
    grade=1, subject_id="G1-08",
    subject_title="Characters",
    fable="dog-shadow",
    examples=[
        _ex("\\h",      "h",     "the literal character",
            "the value of the character"),
        _ex("\\space",  " ",     "the named character literal for a space",
            "the value of the space character"),
        _ex("\\T",      "T",     "the literal character",
            "the value of the character"),
        _ex("(char? \\h)", True,
            "the char? predicate on a literal character",
            "whether the literal character is a character"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-09 — Symbols vs values
# (NON-ATOM: uses _GOAL_SUBPLOTS — model writes the form from the goal.)
G1_09 = SubjectCurriculum(
    grade=1, subject_id="G1-09",
    subject_title="Symbols vs values",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(symbol? 'hare)",
            expected=True,
            concept_phrase="the symbol-predicate on a quoted name",
            question_what="whether a quoted name is a symbol",
            goal_text="ask whether a quoted name is a symbol, using the symbol? predicate",
            scenario=(
                'Bell the hound pointed at a name scratched into a piece of '
                'bark — the mark, not what it pointed to. The reflection in '
                'the stream had looked like a bone, but the scratch that '
                'says bone is not the bone either; the same kind of '
                'distinction was at work here.'
            ),
            need=(
                "She wanted only the runtime's verdict on what the scratch "
                'is — a name the dogs can quote and pass around — without '
                'resolving the scratch to whatever it might point to.'
            ),
            mapping=(
                'The scratch on the bark is the symbol, the actual bone (or '
                'whatever the name might point to) would be the value, and '
                'the predicate is the question of which kind of thing the '
                'form is talking about.'
            ),
            resolution=(
                'The REPL read the form, distinguishing scratch from bone, '
                'and handed back hare. The mark and the bone stayed '
                'two distinct things, exactly as the scratch had said.'
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
                'Patch the hound stood at the stream\'s edge, holding two '
                'objects side by side: a scratch-mark on bark and a smooth '
                'stone bearing the number 42. "This one is the symbol," '
                'Patch said, tapping the bark. "This one is the number. '
                'They are not the same kind of thing."'
            ),
            need=(
                'Patch wanted the runtime\'s verdict on the second object: '
                'was it a symbol name, or just a number the dogs might count '
                'with? The distinction mattered for reading the bark correctly.'
            ),
            mapping=(
                'The scratch is a symbol; the number is a literal value. The '
                'predicate asks only which kind of thing the form is, not what '
                'it might point to. The verdict settles the kind.'
            ),
            resolution=(
                'The REPL examined the integer and returned 42. It was not '
                'a symbol name, only a countable number. The distinction Patch '
                'had drawn held exactly — scratch and stone stayed two kinds.'
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
                'Patch the hound held a message scratched on bark — not a name '
                'to pass around, but a strand of letters. "The reader will treat '
                'this as text, not as a symbol the dogs can quote," Patch said, '
                'laying it beside a carved name-mark.'
            ),
            need=(
                'Patch wanted the runtime\'s clear judgment: was this string-text '
                'or symbol-name? The difference would matter for the next step.'
            ),
            mapping=(
                'The carved name is a symbol; the text on bark is a string. The '
                'predicate asks which kind of thing the form is. The REPL knows '
                'the difference between mark and message.'
            ),
            resolution=(
                'The REPL tested the string and returned false. It was not a '
                'symbol, only text. Patch nodded — the tortoise had settled the kind.'
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
                'Rex the hound laid two scratch-marks side by side on bark '
                'near the forest. Both marks said the same thing: hare, hare. '
                '"Are these two scratches the same name?" Rex asked. "Both '
                'point to the same word — but are they equal?"'
            ),
            need=(
                'He wanted the runtime to check the two names directly and say '
                'whether they were the same symbol. No guessing from the scratch '
                '— the REPL would read and compare them exactly.'
            ),
            mapping=(
                'Each quoted name is a symbol the dog can compare. The = predicate '
                'is the judgment of whether two symbols are identical. The verdict '
                'is true if the names match, false if they differ.'
            ),
            resolution=(
                'The REPL compared the two symbols and returned true. Both marks '
                'were the same name. The runtime had settled it perfectly — two '
                'equal scratches, and the hare to prove it.'
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
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(+ 1 2) ;; sum of one and two",
            expected=3,
            concept_phrase="the addition with a trailing comment",
            question_what="the result, ignoring the comment",
            goal_text="add 1 and 2, with a double-semicolon trailing comment",
            scenario=(
                'Bell the hound wrote a form on a clean strip of bark near the pond, '
                'then added a double-semicolon mark followed by a note in plain words. '
                '"The note is only for other dogs to read," she said. "The REPL will '
                'stop at the semicolon."'
            ),
            need=(
                'She wanted the runtime to ignore the trailing prose and hand back the '
                'value before the comment-sign. The note was pack knowledge, not code.'
            ),
            mapping=(
                'The arithmetic form is what the runtime evaluates. The double-semicolon '
                'marks where the comment begins. What comes after is skipped entirely by '
                'the reader — kept on the bark for later dogs only.'
            ),
            resolution=(
                'The REPL read the marks up to the comment-sign, evaluated the form, and '
                'handed back 2. The note stayed on the bark, untouched, waiting '
                'for the pack.'
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
                'Patch the hound scratched a number on clean bark near the pond: '
                '42, followed by a double-slash, then a short note in plain words. '
                '"The note is only for other dogs to read," Patch said. "The '
                'runtime will not see it."'
            ),
            need=(
                'Patch wanted the runtime to ignore the trailing prose and hand '
                'back the value before the double-semicolon. The note was pack '
                'knowledge, not code.'
            ),
            mapping=(
                'The number is what the runtime evaluates. The double-semicolon '
                'marks where the comment begins. What comes after is skipped '
                'entirely by the reader — kept on the bark for later dogs.'
            ),
            resolution=(
                'The REPL read the marks up to the comment-sign, evaluated the '
                'number, and handed back 42. The note stayed on the bark, '
                'untouched, waiting for the pack.'
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
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(+    1    2)",
            expected=3,
            concept_phrase="the addition with extra spacing",
            question_what="the result of an addition formatted with extra spaces",
            goal_text="add 1 and 2 in a form with extra spaces between tokens",
            scenario=(
                'Bell the hound scratched a form on bark near the meadow, but with '
                'wide gaps between the tokens where the reader normally saw them '
                'close together. "Does the spacing change what the form means?" '
                'someone asked. Bell shook her head.'
            ),
            need=(
                'She wanted the runtime to read the form the same way, gaps or not. '
                'Extra whitespace between tokens should not alter the value the REPL '
                'handed back.'
            ),
            mapping=(
                'The operator and operands are the same regardless of spacing. The '
                'reader skips over gaps between tokens. The runtime sees only the '
                'form\'s structure, not the marks between marks.'
            ),
            resolution=(
                'The REPL read the form, ignored the extra whitespace, and handed '
                'back the 2. The spacing had no effect — the form meant '
                'the same thing to the reader.'
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
                'Patch the hound marked a form on a long bark-strip at the stream\'s '
                'edge but spread the tokens across many lines, each indented neatly. '
                '"Does the layout change what the form says?" his packmate asked. '
                'Patch tapped the bark with his paw.'
            ),
            need=(
                'He wanted the runtime to read the form from top to bottom and '
                'return the same answer as if it were on one line. Line-breaks and '
                'indentation were just spacing.'
            ),
            mapping=(
                'The tokens stay the same whether on one line or spread across many. '
                'The reader follows the marks in order. The runtime reads the '
                'structure, not the layout.'
            ),
            resolution=(
                'The REPL traced the form across its lines, saw the addition, and '
                'handed back 2. The layout had changed nothing — the '
                'form meant exactly the same.'
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
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(+ 2 3)",
            expected=5,
            concept_phrase="the simple addition",
            question_what="the result of adding 2 and 3",
            goal_text="add 2 and 3",
            scenario=(
                'Rex the hound stood at the river bank and scratched a simple form on '
                'bark. The parentheses held the operator and two operands. "These marks '
                'group the tokens," he said. "They don\'t multiply anything — they just '
                'tell the reader what goes together."'
            ),
            need=(
                'He wanted the runtime to read the grouped form and return what the '
                'grouped operation produced. No hidden multiplication — the parens '
                'merely bundled the instruction.'
            ),
            mapping=(
                'The parentheses bundle the form into a procedure. The operator is '
                'the action. The operands are the inputs. The grouped structure is '
                'what the runtime evaluates.'
            ),
            resolution=(
                'The REPL read the grouped form, applied the addition, and handed '
                'back the 3. The parens had bundled the instruction '
                'exactly — nothing multiplied, only added.'
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
                'Patch the hound marked a nested form on a flat stone near the bank, '
                'with one grouped form tucked inside another. "The inner group runs '
                'first," Patch said. "Its value becomes the input to the outer group. '
                'Two operations, but they are bundled in order."'
            ),
            need=(
                'Patch wanted the runtime to evaluate the inner form, take its answer, '
                'and use it as input to the outer form. The nesting had to be read in '
                'the correct order.'
            ),
            mapping=(
                'The inner parentheses group the addition. The outer group uses that '
                'result as its first operand. The runtime evaluates inner-first by '
                'structure, not by writing order.'
            ),
            resolution=(
                'The REPL read the nested form, evaluated the inner addition, then '
                'multiplied its result by three. The answer came back correctly — the '
                'nesting had been honored exactly — 3.'
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
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(+ 1 2)",
            expected=3,
            concept_phrase="the addition",
            question_what="the sum of 1 and 2",
            goal_text="add 1 and 2",
            scenario=(
                'Bell the hound sat by a flat stone near the pond and laid '
                'out two small piles of bones — one of one bone, one of two '
                '— careful with the count.'
            ),
            need=(
                'She wanted the precise size of the heap if both piles were '
                'nudged together — small or large, the runtime would give '
                'the exact number, and that was the count she would carry '
                'forward.'
            ),
            mapping=(
                'The bones are the numbers, the piles are the operands, the '
                'act of nudging-together is +, and the count of the '
                'combined heap is what the REPL hands back.'
            ),
            resolution=(
                'The REPL added the two piles and handed back the precise '
                'count. Bell brushed the bones back into a single tidy heap '
                '— the 2 settled, no eyeballing needed.'
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
                'Rex the hound laid out {drawn.a} bones on a flat stone, then moved three to another pile. "How many are left?" he asked his packmate. "I could count the remainder, or I could let the runtime do it exactly."'
            ),
            need=(
                'He wanted the REPL to take the first heap, remove the second, and '
                'hand back the precise count without any eyeballing. The difference '
                'must be exact.'
            ),
            mapping=(
                'The bones in the first pile are the minuend. The bones in the second '
                'are the subtrahend. The subtraction operation is the taking-away. The '
                'REPL gives the exact count of what remains.'
            ),
            resolution=(
                'The REPL performed the subtraction and handed back the precise count. '
                'No counting by paw was needed — the runtime had settled the difference '
                'the patient way — 3.'
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
                'Bell the hound arranged {drawn.a} piles of bones, each pile holding {drawn.b} bones. "How many bones altogether?" she asked. "I could count every one, or I could let the runtime multiply them for me — one operation, exact answer."'
            ),
            need=(
                'She wanted the REPL to take the {drawn.a} piles of five and return the total count. The multiplication had to be exact, with no room for mis-counting.'
            ),
            mapping=(
                'The {drawn.a} piles are the multiplicand. The {drawn.b} bones per pile are the multiplier. The multiplication is the combining of equal groups. The REPL gives the precise heap-size that results.'
            ),
            resolution=(
                'The REPL performed the multiplication and handed back the precise count. The {drawn.a} piles had been combined exactly right — the runtime had not fumbled the counting — 5.'
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
                'Patch the hound looked at a heap of {drawn.a} bones and measured them into two equal piles. "How many bones in each pile?" asked a younger dog. "The runtime can tell us exactly by dividing."'
            ),
            need=(
                'Patch wanted the REPL to split the heap fairly and hand back the count '
                'per pile. The division had to be exact, with no bones left over in this '
                'case.'
            ),
            mapping=(
                'The {drawn.a} bones are the dividend. The two piles are the divisor. The division is the fair splitting. The REPL gives the count per pile — the quotient.'
            ),
            resolution=(
                'The REPL performed the division and handed back the precise count. Each pile had been measured exactly right — the runtime had split fairly — 2 (with `10` as the input value).'
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
                'Rex the hound gathered {drawn.a} bones from one bank and eight from another. "Should I count them all?" he asked. "Let the runtime add them together. It will give the exact total."'
            ),
            need=(
                'He wanted the REPL to combine the two heaps and hand back the precise '
                'count. No paw-counting needed — the runtime would settle it rightly.'
            ),
            mapping=(
                'The first heap of seven is the first addend. The second heap of eight '
                'is the second addend. The addition is their combining. The REPL gives '
                'the precise count of the combined heap.'
            ),
            resolution=(
                'The REPL added the two heaps and handed back 8. The '
                'bones had been combined exactly right — the runtime\'s answer was the '
                'one that mattered.'
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
                'Bell the hound laid out twenty bones in a careful row and moved seven '
                'to a separate pile. "The difference between the heaps is what matters," '
                'she said. "Let the runtime tell us exactly."'
            ),
            need=(
                'She wanted the REPL to perform the subtraction and hand back the '
                'precise count of what was left. The difference must be exact, with no '
                'mis-count.'
            ),
            mapping=(
                'The twenty bones are the minuend. The {drawn.b} bones moved away are the subtrahend. The subtraction is the taking-away. The REPL gives the exact count remaining.'
            ),
            resolution=(
                'The REPL performed the subtraction and handed back the precise count. '
                'The difference had been settled exactly — the runtime had not wavered — 7.'
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
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(+ 1 (* 2 3))",
            expected=7,
            concept_phrase="the nested computation",
            question_what="the sum of 1 with the product of 2 and 3",
            goal_text="add 1 to the product of 2 and 3",
            scenario=(
                'Patch the hound marked a nested form on bark near the river bank. '
                'Inside the outer addition lived a multiplication. "The inner form runs '
                'first," Patch said. "Its answer becomes food for the outer form."'
            ),
            need=(
                'Patch wanted the REPL to multiply first, then use that answer as one '
                'of the inputs to the addition. The nesting had to be read in the right '
                'order for the answer to be correct.'
            ),
            mapping=(
                'The nested multiplication is evaluated first, producing an intermediate '
                'result. That result becomes the second operand of the outer addition. '
                'The structure itself tells the runtime what to do and in what order.'
            ),
            resolution=(
                'The REPL read the nested form, multiplied two by three in the inner '
                'form, then added one to that answer. The running total came back '
                'exactly right — nesting honored, answer correct — 3.'
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
                'Rex the hound marked two nested forms side by side on a flat stone. '
                'The left nested form was an addition; the right was another. "Both '
                'run first," Rex said. "Then their two answers become the operands of '
                'the multiplication."'
            ),
            need=(
                'He wanted the REPL to evaluate both inner forms, get their two answers, '
                'and then multiply them together. The nested structure had to be honored '
                'perfectly.'
            ),
            mapping=(
                'The two nested additions are evaluated first, producing two intermediate '
                'results. Those two results become the operands of the outer '
                'multiplication. The runtime evaluates all nested forms before any outer '
                'form.'
            ),
            resolution=(
                'The REPL read the nested form, evaluated both inner additions, then '
                'multiplied their answers. The running total came back exactly right — '
                'all nested forms honored, no steps skipped — 4.'
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
                'Bell the hound held a heap of one hundred bones on one stone and '
                'watched a nested form on another. The nested multiplication would '
                'produce a heap to subtract. "The inner form gives me the count to '
                'take away," she said.'
            ),
            need=(
                'She wanted the REPL to multiply first, then use that answer as what '
                'to subtract from the hundred. The nesting had to be read in the right '
                'order.'
            ),
            mapping=(
                'The nested multiplication is evaluated first, producing the count of '
                'bones to remove. That count becomes the subtrahend of the outer '
                'subtraction. The structure itself orders the evaluation.'
            ),
            resolution=(
                'The REPL read the nested form, multiplied five by five in the inner '
                'form, then subtracted that from the hundred. The precise count of '
                'remaining bones came back exactly right — nesting honored — 5.'
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
                'Patch the hound marked a form on bark with two nested multiplications '
                'waiting to be combined. "Each inner form produces a heap," Patch said. '
                '"The outer form adds the two heaps together."'
            ),
            need=(
                'Patch wanted the REPL to evaluate both multiplications, then add their '
                'two results. The nesting had to be honored completely.'
            ),
            mapping=(
                'The two nested multiplications are evaluated first, each producing an '
                'intermediate heap. Those two heaps become the operands of the outer '
                'addition. The runtime evaluates nested forms before outer ones.'
            ),
            resolution=(
                'The REPL read the nested form, multiplied two by three and four by '
                'five separately, then added their answers. The running total came back '
                'exactly right — all nested forms honored, answer precise — 5.'
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
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(= 1 1)",
            expected=True,
            concept_phrase="the equality check",
            question_what="whether 1 equals 1",
            goal_text="test whether 1 equals 1 with =",
            scenario=(
                "Bell the hound paused at the stream's edge with a pebble "
                'in each paw and held them up side by side. The '
                'crossing-conditions of the day were simple: either the two '
                'pebbles match, or they do not.'
            ),
            need=(
                'She wanted only the verdict — does the runtime see them as '
                'equal? — without having to count or compare the pebbles by '
                "eye, so the answer would be the runtime's, not hers."
            ),
            mapping=(
                'The crossing-condition is =, the two pebbles are the '
                'operands, and the verdict — true or false — is what swings '
                'the way open or closed for the next step.'
            ),
            resolution=(
                'The REPL checked the two values, the conditions ruled, and '
                'the 1 came back. Bell trotted on, the matter settled '
                'by the runtime exactly as the rule said.'
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
                'Rex the hound held two pebbles at the stream\'s edge — one marked with '
                'the number one, the other with the number two. "Are these two pebbles '
                'the same?" he asked. "The runtime can tell me for certain."'
            ),
            need=(
                'He wanted the REPL to compare the two numbers directly and deliver the '
                'verdict without guessing. The comparison had to be exact.'
            ),
            mapping=(
                'The crossing-condition is =. The two pebbles are the operands. The '
                'verdict — true or false — is what swings the way open or closed for '
                'the next step.'
            ),
            resolution=(
                'The REPL checked the two values, saw they were not equal, and returned '
                'false. The verdict was clear — the pebbles marked different numbers — 2.'
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
                'Bell the hound marked two identical letters on two stones at the bank '
                'near the pond. "Are these two letters the same?" she asked. "The '
                'runtime can read them and settle it rightly."'
            ),
            need=(
                'She wanted the REPL to compare the two strings directly and return the '
                'verdict. The comparison had to be exact.'
            ),
            mapping=(
                'The crossing-condition is =. The two letter-strings are the operands. '
                'The verdict — true or false — is what the conditions decide.'
            ),
            resolution=(
                'The REPL checked the two strings, saw they were identical, and returned '
                'true. The verdict was clear — both stones bore the same letter exactly.'
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
                'Patch the hound scratched the same keyword on two pieces of bark. Both '
                'read :hare. "Are these two keywords the same?" Patch asked. "The '
                'runtime knows the answer without any guess."'
            ),
            need=(
                'Patch wanted the REPL to compare the two keywords and hand back the '
                'verdict directly. The comparison had to be exact.'
            ),
            mapping=(
                'The crossing-condition is =. The two keywords are the operands. The '
                'verdict — true or false — is what the conditions return.'
            ),
            resolution=(
                'The REPL checked the two keywords, saw they were identical, and returned '
                'true. The verdict was clear — both scratches bore the same symbol — hare.'
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
                'Rex the hound held two scratches side by side near the meadow — one '
                'naming :hare, the other naming :tortoise. "Are these two keywords the '
                'same?" he asked his packmate. "Let the runtime tell us."'
            ),
            need=(
                'He wanted the REPL to compare the two different keywords and return the '
                'verdict. The comparison had to be exact.'
            ),
            mapping=(
                'The crossing-condition is =. The two keywords are the operands. The '
                'verdict — true or false — is what the conditions decide.'
            ),
            resolution=(
                'The REPL checked the two keywords, saw they were different, and returned '
                'false. The verdict was clear — the two scratches named different symbols — tortoise.'
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
                'Bell the hound laid four pebbles in a row at the stream\'s edge, each '
                'marked with the number one. "Are all four of these pebbles the same?" '
                'she asked. "The runtime can check them all at once."'
            ),
            need=(
                'She wanted the REPL to compare all the numbers and return the verdict on whether they were all equal. The comparison had to be exact.'
            ),
            mapping=(
                'The crossing-condition is =. The the numbers are the operands. The verdict — true if all match, false if any differs — is what the conditions return.'
            ),
            resolution=(
                'The REPL checked all the numbers, saw they were all identical, and returned 1. The verdict was clear — all four pebbles bore the same mark.'
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
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(zero? 0)",
            expected=True,
            concept_phrase="the zero check",
            question_what="whether 0 is zero",
            goal_text="check whether 0 is zero using zero?",
            scenario=(
                'Patch the hound held a bone at the stream\'s edge, then laid it down '
                'on an empty stone. "Is this count zero?" Patch asked. "The runtime can '
                'tell me for certain."'
            ),
            need=(
                'Patch wanted the REPL to test the number and return the verdict: was it '
                'zero or not? The check had to be exact.'
            ),
            mapping=(
                'The number is the operand. The zero? predicate is the test. The verdict '
                '— true if the number is exactly zero, false otherwise — is what the '
                'REPL hands back.'
            ),
            resolution=(
                'The REPL tested the number, saw it was zero, and returned 0. The '
                'verdict was clear — the count was settled exactly.'
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
                'Bell the hound held {drawn.a} bones at the stream\'s edge and laid them on a flat stone. "Is this count zero?" she asked. "The runtime can tell me for certain."'
            ),
            need=(
                'She wanted the REPL to test the number and return the verdict: was it '
                'zero or not? The check had to be exact.'
            ),
            mapping=(
                'The bones are the number. The zero? predicate is the test. The '
                'verdict — true if zero, false if not — is what the REPL hands back.'
            ),
            resolution=(
                'The REPL tested the count, saw it was not zero, and returned 5. '
                'The verdict was clear — the bones had weight, not emptiness.'
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
                'Rex the hound marked the number seven on bark near the meadow and '
                'asked his packmate: "Is this count moving forward, or backward?" '
                '"The runtime can tell," his packmate said.'
            ),
            need=(
                'He wanted the REPL to test the number and return the verdict: was it '
                'positive or not? The test had to be exact.'
            ),
            mapping=(
                'The number is the value. The pos? predicate is the question of which '
                'direction. The verdict — true if moving forward, false if not — is '
                'what the REPL returns.'
            ),
            resolution=(
                'The REPL tested the number, saw it moved forward, and returned 7. '
                'The verdict was clear — the count was positive.'
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
                'Patch the hound held a negative number on bark near the forest and '
                'asked: "Is this count moving forward from the marker stone?" '
                '"Let the runtime check," someone said.'
            ),
            need=(
                'Patch wanted the REPL to test the number and hand back the verdict: '
                'was it positive or backward? The test had to be exact.'
            ),
            mapping=(
                'The negative number is the value. The pos? predicate asks the '
                'direction. The verdict — true if forward, false if backward — is '
                'what the runtime returns.'
            ),
            resolution=(
                'The REPL tested the negative number, saw it moved backward, and '
                'returned -2. The verdict was clear — the count was negative.'
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
                'Bell the hound marked a negative number on flat bark at the pond and '
                'asked: "Is this count moving backward from the starting point?" '
                '"The runtime can check," her packmate said.'
            ),
            need=(
                'She wanted the REPL to test the number and return the verdict: was it '
                'negative or positive? The test had to be exact.'
            ),
            mapping=(
                'The negative number is the value. The neg? predicate asks the '
                'direction. The verdict — true if backward, false if forward — is '
                'what the REPL returns.'
            ),
            resolution=(
                'The REPL tested the number, saw it moved backward, and returned -3. '
                'The verdict was clear — the count was negative.'
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
                'Rex the hound scratched the number four on bark near the river and '
                'asked: "Is this count moving backward?" "Let the runtime tell," '
                'said Patch.'
            ),
            need=(
                'He wanted the REPL to test the number and hand back the verdict: was '
                'it negative or forward-moving? The test had to be exact.'
            ),
            mapping=(
                'The positive number is the value. The neg? predicate asks the '
                'direction. The verdict — true if backward, false if forward — is '
                'what the runtime returns.'
            ),
            resolution=(
                'The REPL tested the number, saw it moved forward, and returned 4. '
                'The verdict was clear — the count was positive.'
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
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="42",
            expected=42,
            concept_phrase="the literal 42",
            question_what="the value 42 returned by the REPL",
            goal_text="submit the integer 42 so the REPL returns it",
            scenario=(
                'Bell the hound scratched the number 42 on clean bark at the stream\'s '
                'edge. "When the REPL reads this," she said, "it will return what I '
                'wrote — the value itself, not a computation."'
            ),
            need=(
                'She wanted the runtime to read the bare value and hand it back '
                'unchanged. No operation needed — the literal evaluates to itself.'
            ),
            mapping=(
                'The mark on the bark is the literal form. The reader sees the number. '
                'The REPL returns exactly what the form says.'
            ),
            resolution=(
                'The REPL read the literal and handed back 42. The number '
                'had evaluated to itself — no guessing needed.'
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
                'Patch the hound marked an arithmetic form on bark near the meadow. '
                '"When the REPL reads this," Patch said, "it will evaluate the form '
                'and return the result — not the form itself, but what it computes to."'
            ),
            need=(
                'He wanted the runtime to evaluate the operation and hand back the '
                'running total. The computation mattered — the form would compute to '
                'a value.'
            ),
            mapping=(
                'The marks on bark are the form. The REPL sees the operator and '
                'operands. The runtime evaluates and returns the result.'
            ),
            resolution=(
                'The REPL read the form, performed the addition, and handed back the '
                'running total. The computation had been settled by the runtime — 2.'
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
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(+ 1 2)",
            expected=3,
            concept_phrase="the addition",
            question_what="the result of adding 1 and 2",
            goal_text="add 1 and 2",
            scenario=(
                'Bell the hound stood at the edge of a small log spanning '
                "the stream near the pond. She tested the log's hold paw by "
                'paw before trusting full weight: a slip would not end the '
                'day, only bend it.'
            ),
            need=(
                'She wanted the running total of two small piles — added on '
                'the practice bank where a stumble cost nothing — knowing '
                'the runtime would catch any error before it crossed.'
            ),
            mapping=(
                'The log-bridge test is the safety design of the REPL '
                'itself, the form is the careful step taken on the practice '
                'bank, and what the REPL hands back is the value the '
                'careful step earned.'
            ),
            resolution=(
                'The REPL — net in place — handed back the precise count. '
                'Bell crossed safely, the arithmetic settled by the patient '
                'method, with no daring needed — 2.'
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
                'Rex the hound stood at the edge of a small log spanning the stream '
                'near the meadow. He tested the log\'s hold paw by paw: a slip would '
                'not end the day, only bend it. "The form is safe to try," he said.'
            ),
            need=(
                'He wanted the running total of two factors — multiplied on the '
                'practice bank where a stumble cost nothing — knowing the runtime '
                'would catch any error before it crossed.'
            ),
            mapping=(
                'The log-bridge test is the safety design of the REPL itself. The '
                'form is the step taken on the practice bank. What the REPL hands '
                'back is the value the careful step earned.'
            ),
            resolution=(
                'The REPL — net in place — handed back the precise product. Rex '
                'crossed safely, the arithmetic settled by the patient method, with '
                'no daring needed — 6.'
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
    print(f"grade-1 dog-shadow smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
