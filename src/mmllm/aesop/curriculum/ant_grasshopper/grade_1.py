"""Grade 1 — atoms + first eval, taught through the Ant-and-the-Grasshopper fable.

Each subject defines:
  - examples: a list of Clojure exercises (form + expected + concept_phrase)
  - subplots: 8 narrative templates that wrap any example in fable scenery
  - plan_pool: optional plan-only prefaces (never reveal the answer)

Coverage per subject (per fable):
   examples × narrative variants ≈ 5-15 × 200-2000 distinct records.

The fable's moral dynamic — prudence vs. idleness — informs the
characters' attitudes toward each form: Grasshopper is the carefree
skipper who claims to know the answer at a glance; Ant is the patient
evaluator who submits the form and reads off the REPL's reply. Same
structural lesson as tortoise-hare's vanity-vs-steadiness — patient
evaluation beats hasty guessing — but the imagery throughout is
ant-grasshopper: meadows, stockpiles, day-by-day counting, the coming
of winter as the moral horizon.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)


# ─────────────────────── shared subplot pool ───────────────────────
#
# These 8 templates work across most grade-1 subjects. Each subject
# either uses this pool directly or extends it with subject-specific
# templates. Templates use `{form_display}` for the literal form being
# evaluated, `{concept_phrase}` for the noun-phrase ("the value 42"),
# and fable placeholders for character/location/emotion variation.
#
# Audit-doc lessons applied up front:
#   - {ant_him_her} / {grasshopper_him_her} (object case) for "asked X to ..."
#   - comma after "said" before any EMO_PROUD pick (SAID_PARTICIPLE)
#   - no co-located {form_display} + "the form X" concept_phrase strings
#     (SKILL doc #11) — concepts here use noun-phrase wrappers
#   - {ant} (the name) instead of pronoun for sentences immediately
#     following a singular setup (singular-they ambiguity)

_SHARED_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The argument template — Grasshopper boasts an answer; Ant
    #    insists they actually evaluate the form. The student writes
    #    the form for the REPL.
    SubplotTemplate("""\
{ant_phrase} and {grasshopper_phrase} stopped {place} where someone had
written {concept_phrase} on a flat stone. {grasshopper}, {emo_proud},
declared that {grasshopper_he_she} could see the answer at a glance.
{ant}, {emo_patient}, suggested they actually evaluate the form
{form_display} in the REPL and read off whatever it returned."""),

    # 2. The wager / stockpile-tally template — variants of the same
    #    "wager etched / chalked / scratched" beat so the wager doesn't
    #    always read identically.
    #    NOTE: avoid the prefix "at the edge of a stockpile {place}" —
    #    {place} carries its own preposition, producing pitfall-#21
    #    DOUBLE_PREP stacks like "at the edge of a stockpile at the
    #    edge of the orchard". "Beside a small stockpile" lets {place}
    #    stand alone without competing prepositions.
    SubplotTemplate("""\
Beside a small stockpile {place}, {grasshopper_phrase} sketched a
small wager into the dust: whoever guessed the result of {form_display}
first would win the right to set the next day's count.
{ant_phrase}, {emo_patient}, said it was simpler to type the form into
the REPL than to argue about {concept_phrase}."""),

    # 2b. wager variant — chalk on a slate
    SubplotTemplate("""\
{grasshopper_phrase} chalked a wager on a flat slate {place}: whoever
predicted the result of {form_display} first would set the next day's
ration. {ant_phrase}, {emo_patient}, said it would be simpler to type
the form into the REPL than to bicker about {concept_phrase}."""),

    # 2c. wager variant — twig in the soil
    SubplotTemplate("""\
With a twig, {grasshopper_phrase} marked out a wager {place}: whoever
guessed the result of {form_display} first would win the right to
choose the next song. {ant_phrase}, {emo_patient}, said it was easier
to ask the REPL about {concept_phrase} than to argue."""),

    # 3. The teacher template — Ant is gently teaching Grasshopper how
    #    the REPL works. NOTE: drops any "from a recent X" tail to avoid
    #    DOUBLE_FROM with EMO_TIRED entries that include "from ...".
    SubplotTemplate("""\
{ant_phrase} had been trying to teach {grasshopper_phrase} how the REPL
works. "Look here," {ant_he_she} said, pointing to {concept_phrase}.
"You hand the form {form_display} to the runtime, and the runtime hands
you back what it evaluates to." {grasshopper}, {emo_tired}, agreed to
try."""),

    # 4. The audience template — small meadow creatures gather to
    #    watch the demonstration. NOTE: uses "pointed to" rather than
    #    "read aloud" — abstract concept_phrases like "the predicate
    #    (zero? 0)" don't fit "read aloud" semantically.
    SubplotTemplate("""\
A small audience of meadow creatures had gathered {place} to watch
{grasshopper_phrase} attempt to outwit {ant_phrase} at reading the
REPL. {ant} pointed to {concept_phrase} and read the form aloud:
{form_display}. The crowd waited to see who would correctly write the
form to submit."""),

    # 5. The day's-work-pause template — Grasshopper interrupts the
    #    Ant's stockpiling work to dispute a value; Ant settles it via
    #    careful evaluation.
    #    NOTE: uses {ant} (the name) instead of {ant_he_she_cap} for
    #    the "called it impossible" sentence — for gender="n" Ants,
    #    "They called it impossible." reads as plural-subject right
    #    after a singular "Bit the ant stopped" introduction.
    SubplotTemplate("""\
Halfway through the morning's work, {grasshopper_phrase} blocked
{ant_phrase}'s path {place} and refused to step aside until someone
could prove what the form {form_display} evaluated to. {grasshopper}
called it impossible. {ant_phrase}, walking up at {ant_his_her} usual
pace, simply said: "Submit {concept_phrase} to the REPL. Whatever comes
back is the answer.\""""),

    # 6. The notebook / stockpile-ledger template — Ant keeps a careful
    #    ledger of every form already evaluated.
    SubplotTemplate("""\
{ant_phrase} had been keeping a small leather notebook of every form
{ant_he_she} had successfully evaluated. {place_idx}, the next entry
was {concept_phrase}. {grasshopper_phrase} peered over
{ant_his_her} shoulder at the form {form_display} and asked what it
would come out to.""".replace("{place_idx}", "Today {place}")),

    # 7. The boast-and-rebuke template — Grasshopper claims to know the
    #    answer without checking; Ant insists on actually evaluating.
    #    NOTE: uses {grasshopper_him_her} (object case) for "asked X to
    #    actually..."; uses comma after "said" so participle-phrase
    #    EMO_PROUD entries ("boasting at every turn", "puffed up with
    #    pride") parse as adverbial.
    SubplotTemplate("""\
"There is no need to evaluate that," {grasshopper_phrase} said,
{emo_proud}. "Anyone can see what {concept_phrase} comes to."
{ant_phrase}, who {place} had grown used to such claims, asked
{grasshopper_him_her} to actually write the form {form_display} and
submit it to the REPL — just to be sure."""),

    # 8. The sign-on-the-path template — they find a riddle on a sign
    #    nailed to a stalk or a wooden post.
    SubplotTemplate("""\
A wooden sign nailed to a stalk {place} carried a puzzle. The riddle
was simple: it asked the reader to evaluate {form_display}. {grasshopper}
laughed, {emo_proud}, and declared it too easy. {ant} said patiently
that the only way to be sure of {concept_phrase} was to put it in the
REPL."""),
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


def _ex(form: str, expected, concept: str, what: str,
        tags: tuple[str, ...] = ()) -> SubjectExample:
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          tags=tags)


# ─────────────────────── 18 grade-1 subjects ───────────────────────


# G1-01 — Eval as substitution
G1_01 = SubjectCurriculum(
    grade=1, subject_id="G1-01",
    subject_title="Eval as substitution",
    fable="ant-grasshopper",
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
    fable="ant-grasshopper",
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
    fable="ant-grasshopper",
    examples=[
        # Note: ratios like 1/2 evaluate to themselves in Clojure (exact rational).
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
    fable="ant-grasshopper",
    examples=[
        _ex('"hello"',    "hello",    'the string "hello"',
            'the value of "hello"'),
        _ex('"grain"',    "grain",    'the string "grain"',
            'the value of "grain"'),
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
    fable="ant-grasshopper",
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
    fable="ant-grasshopper",
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
    fable="ant-grasshopper",
    examples=[
        _ex(":ant",         ":ant",         "the keyword :ant",
            "the value of :ant"),
        _ex(":grasshopper", ":grasshopper", "the keyword :grasshopper",
            "the value of :grasshopper"),
        _ex(":winter",      ":winter",      "the keyword :winter",
            "the value of :winter"),
        _ex("(keyword? :ant)", True,
            "the predicate (keyword? :ant)",
            "whether :ant is a keyword"),
        _ex("(= :ant :ant)", True,
            "the equality of two :ant keywords",
            "whether :ant equals :ant"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-08 — Characters
G1_08 = SubjectCurriculum(
    grade=1, subject_id="G1-08",
    subject_title="Characters",
    fable="ant-grasshopper",
    examples=[
        _ex("\\a",      "a",     "the character \\a",
            "the value of \\a"),
        _ex("\\space",  " ",     "the character \\space",
            "the value of \\space"),
        _ex("\\G",      "G",     "the character \\G",
            "the value of \\G"),
        _ex("(char? \\a)", True,
            "the predicate (char? \\a)",
            "whether \\a is a character"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-09 — Symbols vs values
G1_09 = SubjectCurriculum(
    grade=1, subject_id="G1-09",
    subject_title="Symbols vs values",
    fable="ant-grasshopper",
    examples=[
        _ex("(symbol? 'ant)", True,
            "the predicate (symbol? 'ant)",
            "whether 'ant is a symbol"),
        _ex("(symbol? 42)", False,
            "the predicate (symbol? 42)",
            "whether 42 is a symbol"),
        _ex("'ant", "ant",
            "the quoted symbol 'ant",
            "the value of 'ant"),
        _ex("(= 'ant 'ant)", True,
            "the equality of two 'ant symbols",
            "whether 'ant equals 'ant"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-10 — Comments
G1_10 = SubjectCurriculum(
    grade=1, subject_id="G1-10",
    subject_title="Comments",
    fable="ant-grasshopper",
    examples=[
        _ex("(+ 1 2) ; sum of one and two", 3,
            "the form with a trailing comment",
            "the result of (+ 1 2) ignoring the comment"),
        _ex("42 ;; the answer", 42,
            "the literal with a trailing comment",
            "the value of 42"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-11 — Whitespace
G1_11 = SubjectCurriculum(
    grade=1, subject_id="G1-11",
    subject_title="Whitespace doesn't matter",
    fable="ant-grasshopper",
    examples=[
        _ex("(+    1    2)", 3,
            "the spaced-out form",
            "the result of the form"),
        _ex("(+\n  1\n  2)", 3,
            "the line-broken form",
            "the result of the form"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-12 — Parens as syntax
G1_12 = SubjectCurriculum(
    grade=1, subject_id="G1-12",
    subject_title="Parens group; they don't multiply",
    fable="ant-grasshopper",
    examples=[
        _ex("(+ 2 3)", 5,
            "the form (+ 2 3)",
            "the result of (+ 2 3)"),
        _ex("(* (+ 1 2) 3)", 9,
            "the form (* (+ 1 2) 3)",
            "the result of (* (+ 1 2) 3)"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-13 — First arithmetic call
G1_13 = SubjectCurriculum(
    grade=1, subject_id="G1-13",
    subject_title="First arithmetic call",
    fable="ant-grasshopper",
    examples=[
        _ex("(+ 1 2)",  3,    "the form (+ 1 2)",    "the result of (+ 1 2)"),
        _ex("(- 5 3)",  2,    "the form (- 5 3)",    "the result of (- 5 3)"),
        _ex("(* 4 5)",  20,   "the form (* 4 5)",    "the result of (* 4 5)"),
        _ex("(/ 10 2)", 5,    "the form (/ 10 2)",   "the result of (/ 10 2)"),
        _ex("(+ 7 8)",  15,   "the form (+ 7 8)",    "the result of (+ 7 8)"),
        _ex("(- 20 7)", 13,   "the form (- 20 7)",   "the result of (- 20 7)"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-14 — Nested call evaluation
G1_14 = SubjectCurriculum(
    grade=1, subject_id="G1-14",
    subject_title="Nested call evaluation",
    fable="ant-grasshopper",
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
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-15 — Equality
G1_15 = SubjectCurriculum(
    grade=1, subject_id="G1-15",
    subject_title="Equality",
    fable="ant-grasshopper",
    examples=[
        _ex("(= 1 1)",          True,  "the equality (= 1 1)",
            "the value of (= 1 1)"),
        _ex("(= 1 2)",          False, "the equality (= 1 2)",
            "the value of (= 1 2)"),
        _ex("(= \"a\" \"a\")",  True,  "the equality (= \"a\" \"a\")",
            "the value of (= \"a\" \"a\")"),
        _ex("(= :ant :ant)",    True,  "the equality (= :ant :ant)",
            "the value of (= :ant :ant)"),
        _ex("(= :ant :grasshopper)", False,
            "the equality (= :ant :grasshopper)",
            "the value of (= :ant :grasshopper)"),
        _ex("(= 1 1 1 1)",      True,
            "the multi-arg equality (= 1 1 1 1)",
            "the value of (= 1 1 1 1)"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-16 — Numeric predicates
G1_16 = SubjectCurriculum(
    grade=1, subject_id="G1-16",
    subject_title="Numeric predicates",
    fable="ant-grasshopper",
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
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-17 — Printing vs returning
G1_17 = SubjectCurriculum(
    grade=1, subject_id="G1-17",
    subject_title="Printing vs returning",
    fable="ant-grasshopper",
    examples=[
        _ex("42", 42,
            "the value 42",
            "the value of 42"),
        _ex("(+ 1 2)", 3,
            "the form (+ 1 2)",
            "the result of (+ 1 2)"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-18 — Errors are safe in the REPL
G1_18 = SubjectCurriculum(
    grade=1, subject_id="G1-18",
    subject_title="Errors are safe in the REPL",
    fable="ant-grasshopper",
    examples=[
        _ex("(+ 1 2)", 3,
            "the form (+ 1 2)",
            "the result of (+ 1 2)"),
        _ex("(* 7 6)", 42,
            "the form (* 7 6)",
            "the result of (* 7 6)"),
    ],
    subplots=_SHARED_SUBPLOTS,
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
    print(f"grade-1 ant-grasshopper smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
