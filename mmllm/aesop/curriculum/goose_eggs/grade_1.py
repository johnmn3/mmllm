"""Grade 1 — atoms + first eval, taught through the Goose-Eggs fable.

Each subject defines:
  - examples: a list of Clojure exercises (form + expected + concept_phrase)
  - subplots: 8 narrative templates that wrap any example in fable scenery
  - plan_pool: optional plan-only prefaces (never reveal the answer)

Coverage per subject (per fable):
   examples × narrative variants ≈ 5-15 × 200-2000 distinct records.

The fable's moral dynamic — greed vs. patience — informs the
characters' attitudes toward each form: the impatient {visitor}
wants the answer at once and tries to guess; the patient {owner}
submits the form to the REPL and reads back what it returns. The
{goose} stands quietly in the background, laying one egg per
morning — the same one-form-one-value cadence the REPL uses.
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
#
# Cast aliases: {owner} = the patient evaluator (tortoise-analog),
# {visitor} = the impatient guesser (hare-analog), {goose} = the
# value-yielding bird whose one-egg-per-morning rhythm parallels
# eval's one-form-one-value rhythm.

_SHARED_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The argument — visitor declares they know without evaluating;
    #    owner insists they actually submit the form to the REPL.
    SubplotTemplate("""\
{owner_phrase} and {visitor_phrase} stood {place} where someone had
scratched {concept_phrase} into a smooth slate by the egg-basket.
{visitor}, {emo_proud}, declared the answer was obvious — no need to
evaluate anything. {owner_phrase}, {emo_patient}, suggested they
actually submit the form {form_display} to the REPL, the way
{goose_phrase} laid one egg at a time: one form, one returned value."""),

    # 2. The wager — chalked on a market stall; bets on the form's result.
    SubplotTemplate("""\
At a small stall {place}, someone had chalked a wager: whoever
predicted the result of {form_display} first would set the asking
price for the morning's eggs. {owner_phrase}, {emo_patient}, said it
was easier to type the form into the REPL than to argue about
{concept_phrase} — {goose_phrase} was about to lay another egg
anyway, and the morning would not wait for guessing."""),

    # 2b. Wager variant — coins on a wooden table.
    # NOTE: was "the kitchen table" — when {place} resolved to
    # "in the kitchen" / "deep inside the kitchen" the rendered text
    # read "kitchen table in the kitchen" (DOUBLED_PLACE bug).
    # "Wooden table" composes with any {place} resolution.
    SubplotTemplate("""\
A row of three coins sat on a wooden table {place}, set out as a
wager between {visitor_phrase} and {owner_phrase}. The bet was
simple: predict what {form_display} would return. {visitor},
{emo_greedy}, was certain about the answer. {owner_phrase} asked
{visitor_him_her}, {emo_patient}, to actually write the form into the
REPL — {concept_phrase} would be settled the moment the runtime
answered, not before."""),

    # 2c. Wager variant — eggs as the stake.
    SubplotTemplate("""\
{visitor_phrase} offered a small basket of eggs as a wager {place}:
whoever guessed the result of {form_display} first would keep them.
{owner_phrase}, {emo_patient}, said it would be simpler to type the
form into the REPL than to bicker about {concept_phrase}; the eggs,
after all, would still be there once {goose_phrase} laid the next
one."""),

    # 3. The teacher — owner explains REPL using the form, draws on the
    #    one-egg-at-a-time analogy throughout.
    SubplotTemplate("""\
{owner_phrase} had been trying to teach {visitor_phrase} how the REPL
works. "Here," {owner_he_she} said, pointing to {concept_phrase}.
"You hand the form {form_display} to the runtime, and the runtime
hands you back exactly what it evaluates to. One form, one return —
the way {goose_phrase} gives one egg each morning, no more, no less.\""""),

    # 4. The audience — neighbors gather to watch the demonstration.
    SubplotTemplate("""\
A small audience of neighbors had gathered {place} to watch
{visitor_phrase} attempt to outguess {owner_phrase} at reading the
REPL. {owner} pointed to {concept_phrase} and read out the form
aloud: {form_display}. The crowd waited to see who would correctly
write the form to submit; {goose_phrase} watched too, untroubled by
the noise."""),

    # 5. The market-pause — visitor pauses on the morning errand with eggs.
    #    NOTE: uses {visitor} (the name) instead of {visitor_he_she_cap}
    #    in the second sentence — for gender="n" characters, "They called
    #    it impossible." reads as plural-subject right after the
    #    singular setup. {place} carries its own preposition, so it goes
    #    after the verb (`stopped {place}`), not after a verb that
    #    requires its own preposition (`to {place}` would double-up).
    SubplotTemplate("""\
Halfway through the morning errand, {visitor_phrase} stopped {place}
with a basket of eggs and refused to move on until someone could
prove what the form {form_display} evaluated to. {visitor} called it
impossible. {owner_phrase}, walking up at an unhurried pace, simply
said: "Submit {concept_phrase} to the REPL. Whatever comes back is
the answer." {goose_phrase} watched the basket, calm as ever."""),

    # 6. The ledger — owner keeps a careful written record.
    SubplotTemplate("""\
{owner_phrase} had been keeping a small leather ledger of every form
{owner_he_she} had successfully evaluated, the same way the eggs from
{goose_phrase} were tallied in another column. Today {place}, the
next entry was {concept_phrase}. {visitor_phrase} peered over
{owner_his_her} shoulder at the form {form_display} and asked what
it would come out to."""),

    # 7. The boast-and-rebuke — visitor claims to know without checking.
    #    NOTE: uses {visitor_him_her} (object case) for "asked X to ...";
    #    uses comma after "said" so participle EMO_PROUD entries parse
    #    as adverbial.
    SubplotTemplate("""\
"There is no need to evaluate that," {visitor_phrase} said, {emo_proud}.
"Anyone with eyes can see what {concept_phrase} comes to."
{owner_phrase}, who {place} had grown used to such claims, asked
{visitor_him_her} to actually write the form {form_display} and
submit it to the REPL — just to be sure, the way one counts eggs
one by one rather than guessing the day's total at a glance."""),

    # 8. The notice on the village post — a riddle posted publicly.
    SubplotTemplate("""\
A small wooden notice nailed to a post {place} carried a puzzle for
the village. The riddle asked the reader to evaluate {form_display}.
{visitor} laughed, {emo_proud}, and declared it too easy.
{owner_phrase} said, {emo_patient}, that the only honest way to know
{concept_phrase} was to put it in the REPL — the way an honest
egg-count was settled by going to the basket and counting, never
by sky-gazing."""),
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
    # Goose-eggs flavored plans — the patience-vs-greed framing.
    "I let the runtime hand back one value, the way the goose gives one egg.",
    "I submit the form patiently and read whatever comes back.",
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
    fable="goose-eggs",
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
    fable="goose-eggs",
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
    fable="goose-eggs",
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
    fable="goose-eggs",
    examples=[
        _ex('"hello"',    "hello",    'the string "hello"',
            'the value of "hello"'),
        _ex('"egg"',      "egg",      'the string "egg"',
            'the value of "egg"'),
        _ex('"golden egg"', "golden egg",
            'the string "golden egg"',
            'the value of "golden egg"'),
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
    fable="goose-eggs",
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
    fable="goose-eggs",
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
    fable="goose-eggs",
    examples=[
        _ex(":egg",     ":egg",     "the keyword :egg",
            "the value of :egg"),
        _ex(":goose",   ":goose",   "the keyword :goose",
            "the value of :goose"),
        _ex(":gold",    ":gold",    "the keyword :gold",
            "the value of :gold"),
        _ex("(keyword? :egg)", True,
            "the predicate (keyword? :egg)",
            "whether :egg is a keyword"),
        _ex("(= :egg :egg)", True,
            "the equality of two :egg keywords",
            "whether :egg equals :egg"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-08 — Characters
G1_08 = SubjectCurriculum(
    grade=1, subject_id="G1-08",
    subject_title="Characters",
    fable="goose-eggs",
    examples=[
        _ex("\\g",      "g",     "the character \\g",
            "the value of \\g"),
        _ex("\\space",  " ",     "the character \\space",
            "the value of \\space"),
        _ex("\\E",      "E",     "the character \\E",
            "the value of \\E"),
        _ex("(char? \\g)", True,
            "the predicate (char? \\g)",
            "whether \\g is a character"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-09 — Symbols vs values
G1_09 = SubjectCurriculum(
    grade=1, subject_id="G1-09",
    subject_title="Symbols vs values",
    fable="goose-eggs",
    examples=[
        _ex("(symbol? 'goose)", True,
            "the predicate (symbol? 'goose)",
            "whether 'goose is a symbol"),
        _ex("(symbol? 42)", False,
            "the predicate (symbol? 42)",
            "whether 42 is a symbol"),
        _ex("'goose", "goose",
            "the quoted symbol 'goose",
            "the value of 'goose"),
        _ex("(= 'goose 'goose)", True,
            "the equality of two 'goose symbols",
            "whether 'goose equals 'goose"),
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)


# G1-10 — Comments
G1_10 = SubjectCurriculum(
    grade=1, subject_id="G1-10",
    subject_title="Comments",
    fable="goose-eggs",
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
    fable="goose-eggs",
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
    fable="goose-eggs",
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
    fable="goose-eggs",
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
    fable="goose-eggs",
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
    fable="goose-eggs",
    examples=[
        _ex("(= 1 1)",          True,  "the equality (= 1 1)",
            "the value of (= 1 1)"),
        _ex("(= 1 2)",          False, "the equality (= 1 2)",
            "the value of (= 1 2)"),
        _ex("(= \"a\" \"a\")",  True,  "the equality (= \"a\" \"a\")",
            "the value of (= \"a\" \"a\")"),
        _ex("(= :gold :gold)",  True,  "the equality (= :gold :gold)",
            "the value of (= :gold :gold)"),
        _ex("(= :gold :silver)", False,
            "the equality (= :gold :silver)",
            "the value of (= :gold :silver)"),
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
    fable="goose-eggs",
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
    fable="goose-eggs",
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
    fable="goose-eggs",
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
    print(f"grade-1 goose-eggs smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
