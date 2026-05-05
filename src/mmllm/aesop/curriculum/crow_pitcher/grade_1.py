"""Grade 1 — atoms + first eval, taught through the Crow-and-Pitcher fable.

The fable's moral dynamic — cleverness in adversity — informs every
record. Two crows from the pool (Korvus, Caw, Sable) play the dialogue:

  - The HASTY crow is impatient; would give up, or guess at the
    answer rather than evaluate. The model's bad habit personified.
  - The CLEVER crow is methodical; drops the form into the REPL the
    way a stone goes into the pitcher — one form, one rise of the
    surface, until the beak (eval) reaches the answer. The model's
    correct discipline under eval-first.

The two roles rotate across the three crows, so the model sees Korvus
and Caw, Caw and Sable, and Sable and Korvus playing both sides
across thousands of records. Same dynamic, different surface forms.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)


# ─────────────────────── shared subplot pool ───────────────────────
#
# Eight templates that work across most grade-1 subjects. Each subject
# uses this pool directly. Higher grades extend it with grade-flavored
# beats (a ledger of bindings in G3, a basket of pebbles in G4, etc).
#
# The crow-pitcher metaphor runs through every template: drop a form
# into the REPL like a stone into the pitcher, watch the surface rise
# until eval can reach the answer. The hasty crow either skips the drop
# (just guesses) or despairs that the surface will never rise; the
# clever crow patiently drops one form at a time.
#
# Templates use `{form_display}` for the literal form being evaluated,
# `{concept_phrase}` for the noun-phrase ("the value 42"), and crow
# placeholders ({hasty}/{clever} and their variants) for character /
# location / emotion variation. EMO_* phrases are always comma-bracketed
# after "said" so participle entries don't read as agrammatical.

_SHARED_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The argument template — Hasty crow gives up; Clever insists
    #    on patient form-dropping. The student writes the form.
    SubplotTemplate("""\
{hasty_phrase} and {clever_phrase} alighted {place} on the rim of an old
pitcher where someone had scratched {concept_phrase}. {hasty},
{emo_desperate}, declared the answer beyond reach. {clever}, patient as
ever, suggested they drop the form {form_display} into the REPL the
way a stone goes into the pitcher — one form, one rise of the
surface."""),

    # 2. The wager template — bets on what the form returns.
    #    Three near-equivalent variants of the wager-setup line so the
    #    same wager-template doesn't always read as "scratched a wager
    #    along the rim" verbatim (cosmetic variety).
    SubplotTemplate("""\
At a moss-flecked pitcher {place}, {hasty_phrase} sketched a small
wager: whoever guessed the result of {form_display} first would drink
first when the water rose. {clever_phrase}, {emo_patient}, said it was
simpler to type the form into the REPL than to argue about
{concept_phrase}."""),

    # 2b. wager variant — etched along the rim
    SubplotTemplate("""\
{hasty_phrase} etched a wager along the rim of a chipped pitcher
{place}: whoever predicted the result of {form_display} first would set
the next day's foraging route. {clever_phrase}, {emo_patient}, said it
would be simpler to drop the form into the REPL than to bicker about
{concept_phrase}."""),

    # 2c. wager variant — pebble in the dust
    SubplotTemplate("""\
With a careful tap of {hasty_his_her} beak, {hasty_phrase} marked out a
wager in the dust {place}: whoever guessed the result of {form_display}
first would win the right to claim the next clear water they found.
{clever_phrase}, {emo_patient}, said it was easier to ask the REPL
about {concept_phrase} than to argue."""),

    # 3. The teacher template — Clever crow gently corrects Hasty.
    #    NOTE: drops a "from a recent flight" tail because EMO_TIRED
    #    entries already supply their own "from X" clause; doubling
    #    would produce "from sprinting from a recent flight" awkwardness.
    SubplotTemplate("""\
{clever_phrase} had been trying to teach {hasty_phrase} how the REPL
works. "Look here," {clever_he_she} said, pointing to {concept_phrase}.
"You hand the form {form_display} to the runtime, and the runtime hands
back what it evaluates to — the way water rises to meet the beak when
each stone goes in." {hasty}, {emo_thirsty}, agreed to try."""),

    # 4. The audience template — sparrows and finches watch and learn.
    #    NOTE: rewritten so {concept_phrase} is referenced via "pointed
    #    to" rather than "read aloud" — abstract concept_phrases like
    #    "the equality (= 1 1)" / "the predicate (zero? 0)" don't fit
    #    "read aloud" semantically.
    SubplotTemplate("""\
A small audience of sparrows had gathered {place} to watch
{hasty_phrase} attempt to outwit {clever_phrase} at the rim of an old
pitcher. {clever} pointed to {concept_phrase} and read out the form
aloud: {form_display}. The watching birds tilted their heads, waiting
to see who would correctly write the form to submit."""),

    # 5. The pitcher-pause template — Hasty crow despairs and stops at
    #    the pitcher's edge; Clever arrives and submits the form
    #    patiently.
    #    NOTE: uses {hasty} (the name) instead of {hasty_he_she_cap}
    #    for the "called it impossible" sentence — for gender="n"
    #    characters, "They called it impossible" reads as plural
    #    right after a singular "Sable the crow alighted" introduction.
    SubplotTemplate("""\
Halfway through a long thirsty afternoon, {hasty_phrase} alighted
{place} and refused to fly on until someone could prove what the form
{form_display} evaluated to. {hasty} called it impossible.
{clever_phrase}, gliding down at an unhurried pace, simply said: "Drop
{concept_phrase} into the REPL. Whatever rises is the answer.\""""),

    # 6. The notebook template — Clever crow keeps a careful ledger.
    #    Stone-by-stone counting is the natural beat for crow-pitcher.
    SubplotTemplate("""\
{clever_phrase} had been keeping a small leather notebook of every form
{clever_he_she} had successfully dropped into the REPL — one entry per
stone, one rise per form. Today {place}, the next entry was
{concept_phrase}. {hasty_phrase} peered over {clever_his_her} shoulder
at the form {form_display} and asked what it would come out to."""),

    # 7. The boast-and-rebuke template — Hasty claims to know without
    #    submitting.
    #    NOTE: uses {hasty_him_her} (object case) for "asked X to ...";
    #    uses comma after "said" so participle-phrase EMO_PROUD entries
    #    ("boasting at every turn", "swaggering through the underbrush")
    #    parse as adverbial — without the comma, "said boasting" reads
    #    as agrammatical.
    SubplotTemplate("""\
"There is no need to evaluate that," {hasty_phrase} said, {emo_proud}.
"Anyone with a sharp eye can see what {concept_phrase} comes to."
{clever_phrase}, who {place} had grown used to such claims, asked
{hasty_him_her} to actually write the form {form_display} and drop it
into the REPL — just to be sure."""),

    # 8. The puzzle-on-the-pitcher template — engraving on the vessel
    #    or a sign nearby poses the form as a riddle.
    SubplotTemplate("""\
A wooden sign nailed to a tree {place} carried a puzzle next to a
half-empty pitcher. The riddle was simple: it asked the reader to
evaluate {form_display}. {hasty} laughed, {emo_proud}, and declared it
too easy. {clever} said patiently that the only way to be sure of
{concept_phrase} was to drop it into the REPL."""),
]


_PLAN_POOL: tuple[str, ...] = (
    "I write the form and let the REPL evaluate it.",
    "I submit the form to the REPL via the eval tool.",
    "I let the REPL do the evaluation.",
    "I express the form as Clojure source.",
    # Crow-flavored plans — picked occasionally to break up the generic
    # ones and tie the model's reasoning to the fable's metaphor.
    "I drop the form into the REPL like a stone into the pitcher.",
    "I let each form raise the surface a little closer to the answer.",
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
    fable="crow-pitcher",
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
        # Ratios like 1/2 evaluate to themselves in Clojure (exact rational).
        # The model writes the literal form; the runtime reproduces it.
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
        _ex('"thirst"',   "thirst",   'the string "thirst"',
            'the value of "thirst"'),
        _ex('"clever and patient"', "clever and patient",
            'the string "clever and patient"',
            'the value of "clever and patient"'),
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
        _ex(":crow",     ":crow",     "the keyword :crow",
            "the value of :crow"),
        _ex(":pitcher",  ":pitcher",  "the keyword :pitcher",
            "the value of :pitcher"),
        _ex(":stone",    ":stone",    "the keyword :stone",
            "the value of :stone"),
        _ex("(keyword? :crow)", True,
            "the predicate (keyword? :crow)",
            "whether :crow is a keyword"),
        _ex("(= :crow :crow)", True,
            "the equality of two :crow keywords",
            "whether :crow equals :crow"),
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
        _ex("\\c",      "c",     "the character \\c",
            "the value of \\c"),
        _ex("\\space",  " ",     "the character \\space",
            "the value of \\space"),
        _ex("\\K",      "K",     "the character \\K",
            "the value of \\K"),
        _ex("(char? \\c)", True,
            "the predicate (char? \\c)",
            "whether \\c is a character"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-09 — Symbols vs values
G1_09 = SubjectCurriculum(
    grade=1, subject_id="G1-09",
    subject_title="Symbols vs values",
    fable="crow-pitcher",
    examples=[
        _ex("(symbol? 'crow)", True,
            "the predicate (symbol? 'crow)",
            "whether 'crow is a symbol"),
        _ex("(symbol? 42)", False,
            "the predicate (symbol? 42)",
            "whether 42 is a symbol"),
        _ex("'crow", "crow",
            "the quoted symbol 'crow",
            "the value of 'crow"),
        _ex("(= 'crow 'crow)", True,
            "the equality of two 'crow symbols",
            "whether 'crow equals 'crow"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-10 — Comments (no eval — but we ask "what does the non-comment evaluate to")
G1_10 = SubjectCurriculum(
    grade=1, subject_id="G1-10",
    subject_title="Comments",
    fable="crow-pitcher",
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
    fable="crow-pitcher",
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
    fable="crow-pitcher",
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
    fable="crow-pitcher",
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
    fable="crow-pitcher",
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
    fable="crow-pitcher",
    examples=[
        _ex("(= 1 1)",          True,  "the equality (= 1 1)",
            "the value of (= 1 1)"),
        _ex("(= 1 2)",          False, "the equality (= 1 2)",
            "the value of (= 1 2)"),
        _ex("(= \"a\" \"a\")",  True,  "the equality (= \"a\" \"a\")",
            "the value of (= \"a\" \"a\")"),
        _ex("(= :crow :crow)",  True,  "the equality (= :crow :crow)",
            "the value of (= :crow :crow)"),
        _ex("(= :crow :stone)", False,
            "the equality (= :crow :stone)",
            "the value of (= :crow :stone)"),
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
    fable="crow-pitcher",
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
    fable="crow-pitcher",
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
# (We pose forms that succeed; the lesson is in the surrounding narrative.)
G1_18 = SubjectCurriculum(
    grade=1, subject_id="G1-18",
    subject_title="Errors are safe in the REPL",
    fable="crow-pitcher",
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
    print(f"grade-1 crow-pitcher smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
