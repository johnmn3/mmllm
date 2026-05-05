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
    SubplotTemplate("""\
At a moss-covered milestone {place}, {hare_phrase} drew a wager in the
dust: whoever guessed the result of {form_display} first would win the
right to set the next race. {tortoise_phrase}, {emo_patient}, said it
was simpler to type the form into the REPL than to argue about
{concept_phrase}."""),

    # 3. The teacher template — Tortoise is gently correcting Hare.
    SubplotTemplate("""\
{tortoise_phrase} had been trying to teach {hare_phrase} how the REPL
works. "Look here," {tortoise_he_she} said, pointing to
{concept_phrase}. "You hand the form {form_display} to the runtime, and
the runtime hands you back what it evaluates to." {hare}, {emo_tired}
from a recent sprint, agreed to try."""),

    # 4. The audience template — small forest creatures watch and learn.
    SubplotTemplate("""\
A small audience of forest creatures had gathered {place} to watch
{hare_phrase} attempt to outwit {tortoise_phrase} at reading the REPL.
{tortoise} read aloud {concept_phrase}: the form was {form_display}.
The crowd waited to see who would correctly write the form to submit."""),

    # 5. The race-pause template — hare pauses mid-race, tortoise catches up
    #    via careful evaluation.
    SubplotTemplate("""\
Halfway through the race, {hare_phrase} stopped {place} and refused to
continue until someone could prove what the form {form_display}
evaluated to. {hare_he_she_cap} called it impossible.
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
    #    NOTE: uses {hare_him_her} (object case) for "asked X to ...".
    SubplotTemplate("""\
"There is no need to evaluate that," {hare_phrase} said {emo_proud}.
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
    fable="tortoise-hare",
    examples=[
        _ex("42",                  42,    "the value 42",
            "the value of 42"),
        _ex("0",                   0,     "the value 0",
            "the value of the form 0"),
        _ex("(+ 1 2)",             3,     "the form (+ 1 2)",
            "the result of (+ 1 2)"),
        _ex("(* 4 5)",             20,    "the form (* 4 5)",
            "the result of (* 4 5)"),
        _ex("(- 10 (+ 2 3))",      5,     "the nested form (- 10 (+ 2 3))",
            "the result of (- 10 (+ 2 3))"),
        _ex("(+ 1 (* 2 3))",       7,     "the form (+ 1 (* 2 3))",
            "the result of (+ 1 (* 2 3))"),
        _ex("\"hello\"",          "hello","the string \"hello\"",
            "the string the form \"hello\" evaluates to"),
        _ex("nil",                None,   "the literal nil",
            "the value of the form nil"),
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
            "the sum 1/2 + 1/4",
            "the value of (+ 1/2 1/4)"),
        _ex("(* 2 1/2)", 1,
            "the product of 2 and 1/2",
            "the value of (* 2 1/2)"),
        _ex("(- 1 1/3)", "2/3",
            "1 minus 1/3",
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
            'the value of the string "42" (note: not the number 42)'),
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
            "whether 0 is nil (it isn't)"),
        _ex("(nil? false)", False,
            "the predicate (nil? false)",
            "whether false is nil (it isn't)"),
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
G1_09 = SubjectCurriculum(
    grade=1, subject_id="G1-09",
    subject_title="Symbols vs values",
    fable="tortoise-hare",
    examples=[
        _ex("(symbol? 'hare)", True,
            "the predicate (symbol? 'hare)",
            "whether 'hare is a symbol"),
        _ex("(symbol? 42)", False,
            "the predicate (symbol? 42)",
            "whether 42 is a symbol"),
        _ex("'hare", "hare",
            "the quoted symbol 'hare",
            "the value of 'hare"),
        _ex("(= 'hare 'hare)", True,
            "the equality of two 'hare symbols",
            "whether 'hare equals 'hare"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-10 — Comments (no eval — but we can ask "what does the non-comment evaluate to")
G1_10 = SubjectCurriculum(
    grade=1, subject_id="G1-10",
    subject_title="Comments",
    fable="tortoise-hare",
    examples=[
        # Comments are stripped by the reader; what remains evaluates.
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
    fable="tortoise-hare",
    examples=[
        _ex("(+    1    2)", 3,
            "the form (+ 1 2) with extra spaces",
            "the result of (+    1    2)"),
        _ex("(+\n  1\n  2)", 3,
            "the form (+ 1 2) split across lines",
            "the result of the same sum laid out vertically"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-12 — Parens as syntax
G1_12 = SubjectCurriculum(
    grade=1, subject_id="G1-12",
    subject_title="Parens group; they don't multiply",
    fable="tortoise-hare",
    examples=[
        _ex("(+ 2 3)", 5,
            "the form (+ 2 3)",
            "the result of (+ 2 3) — note the parens are syntax, not multiplication"),
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
    fable="tortoise-hare",
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
    fable="tortoise-hare",
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
    fable="tortoise-hare",
    examples=[
        _ex("(= 1 1)",          True,  "the equality (= 1 1)",
            "the value of (= 1 1)"),
        _ex("(= 1 2)",          False, "the equality (= 1 2)",
            "the value of (= 1 2)"),
        _ex("(= \"a\" \"a\")",  True,  "the equality (= \"a\" \"a\")",
            "the value of (= \"a\" \"a\")"),
        _ex("(= :hare :hare)",  True,  "the equality (= :hare :hare)",
            "the value of (= :hare :hare)"),
        _ex("(= :hare :tortoise)", False,
            "the equality (= :hare :tortoise)",
            "the value of (= :hare :tortoise)"),
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
    fable="tortoise-hare",
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
# (We can only express this via forms whose return value is what eval reports.
# The "prints to stdout" aspect is acknowledged in the concept, but the eval
# result is what matters for our tool-call training.)
G1_17 = SubjectCurriculum(
    grade=1, subject_id="G1-17",
    subject_title="Printing vs returning",
    fable="tortoise-hare",
    examples=[
        _ex("42", 42,
            "the value 42 (the REPL returns it; doesn't 'print' it)",
            "what 42 evaluates to (the return value, what the REPL displays)"),
        _ex("(+ 1 2)", 3,
            "the form (+ 1 2)",
            "what the REPL returns from (+ 1 2)"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-18 — Errors are safe in the REPL
# (We pose forms that succeed; the lesson is in the surrounding narrative.)
G1_18 = SubjectCurriculum(
    grade=1, subject_id="G1-18",
    subject_title="Errors are safe in the REPL",
    fable="tortoise-hare",
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
    print(f"grade-1 tortoise-hare smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
