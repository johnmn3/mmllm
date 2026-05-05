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
        _ex("(symbol? 'fox)", True,
            "the predicate (symbol? 'fox)",
            "whether 'fox is a symbol"),
        _ex("(symbol? 42)", False,
            "the predicate (symbol? 42)",
            "whether 42 is a symbol"),
        _ex("'fox", "fox",
            "the quoted symbol 'fox",
            "the value of 'fox"),
        _ex("(= 'fox 'fox)", True,
            "the equality of two 'fox symbols",
            "whether 'fox equals 'fox"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-10 — Comments
G1_10 = SubjectCurriculum(
    grade=1, subject_id="G1-10",
    subject_title="Comments",
    fable="fox-grapes",
    examples=[
        _ex("(+ 1 2) ; sum of one and two", 3,
            "the form (+ 1 2) followed by a comment",
            "the result of (+ 1 2) ignoring the comment"),
        _ex("42 ;; the answer", 42,
            "the literal 42 with a trailing comment",
            "the value of 42"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-11 — Whitespace
G1_11 = SubjectCurriculum(
    grade=1, subject_id="G1-11",
    subject_title="Whitespace doesn't matter",
    fable="fox-grapes",
    examples=[
        _ex("(+    1    2)", 3,
            "the form (+ 1 2) with extra spaces",
            "the result of the form"),
        _ex("(+\n  1\n  2)", 3,
            "the form (+ 1 2) split across lines",
            "the result of the form"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-12 — Parens as syntax
G1_12 = SubjectCurriculum(
    grade=1, subject_id="G1-12",
    subject_title="Parens group; they don't multiply",
    fable="fox-grapes",
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
# Examples are framed in body-stand + jump-height arithmetic that fits
# fox-grapes' canonical "how high can I reach?" math, but the
# concept_phrase / question_what stay neutral so the same subplots
# render cleanly across all examples.
G1_13 = SubjectCurriculum(
    grade=1, subject_id="G1-13",
    subject_title="First arithmetic call",
    fable="fox-grapes",
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
    fable="fox-grapes",
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
    fable="fox-grapes",
    examples=[
        _ex("(= 1 1)",          True,  "the equality (= 1 1)",
            "the value of (= 1 1)"),
        _ex("(= 1 2)",          False, "the equality (= 1 2)",
            "the value of (= 1 2)"),
        _ex("(= \"a\" \"a\")",  True,  "the equality (= \"a\" \"a\")",
            "the value of (= \"a\" \"a\")"),
        _ex("(= :fox :fox)",    True,  "the equality (= :fox :fox)",
            "the value of (= :fox :fox)"),
        _ex("(= :fox :grapes)", False,
            "the equality (= :fox :grapes)",
            "the value of (= :fox :grapes)"),
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
    fable="fox-grapes",
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
    fable="fox-grapes",
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
    fable="fox-grapes",
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
    print(f"grade-1 fox-grapes smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
