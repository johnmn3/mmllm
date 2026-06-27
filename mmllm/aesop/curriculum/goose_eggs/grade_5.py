"""Grade 5 — control flow + higher-order intro. Through goose-eggs."""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.goose_eggs.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)


# Grade-5 flavored extensions: the "same operation repeated cleverly"
# theme of higher-order forms maps cleanly onto the goose-eggs daily
# ritual — morning by morning the goose lays one egg, and the days
# compound into a ledger of repeated evaluations.
_HOF_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    # Daily-ritual: one operation repeated across many mornings.
    SubplotTemplate("""\
{owner_phrase} kept a long ledger {place} where every morning a single
egg was tallied, and every morning the same small operation was applied
to the row of days. The form {form_display} captured {concept_phrase}:
the same trick, repeated cleverly across the basket. {visitor_phrase},
{emo_greedy}, claimed to know what would come back without running it;
{owner_phrase}, {emo_patient}, asked {visitor_him_her} to submit the
form to the REPL — one form, one returned value, the way one morning
yielded one egg."""),

    # Market-trip: same rule applied to every coin in the purse.
    SubplotTemplate("""\
On the way to market {place}, {owner_phrase} explained to
{visitor_phrase} how a single rule could be applied to a whole basket
of eggs at once — or to every coin in a purse — without writing the
rule out for each item. The form {form_display} did exactly that for
{concept_phrase}. {visitor}, {emo_proud}, guessed the result aloud;
{owner_phrase} said, {emo_patient}, that {goose_phrase} taught a
better habit: count by submitting, not by sky-gazing."""),

    # Compounding-days: the daily-eval framing.
    SubplotTemplate("""\
"Morning by morning, the goose lays one egg, and the days compound,"
{owner_phrase} said {place}, sketching the form {form_display} into the
margin of the kitchen ledger. {concept_phrase} was, {owner_he_she}
explained, the same kind of patient compounding — one operation,
applied again and again until the REPL handed back its single, honest
answer. {visitor_phrase}, {emo_regretful} after an earlier wrong guess,
agreed this time to let the runtime decide."""),
]


def _ex(form, expected, concept, what):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what)


_PLAN_G5 = _PLAN_POOL + (
    "I use map / filter / reduce as appropriate.",
    "I write the higher-order form so the REPL can compute.",
    "I let the REPL apply the same operation across the basket.",
)


G5_01 = SubjectCurriculum(grade=5, subject_id="G5-01",
    subject_title="if", fable="goose-eggs",
    examples=[
        _ex("(if true :a :b)",  ":a", "the form (if true :a :b)",  "which of :a or :b is returned"),
        _ex("(if false :a :b)", ":b", "the form (if false :a :b)", "which of :a or :b is returned"),
        _ex("(if (> 5 3) :a :b)", ":a", "the form (if (> 5 3) :a :b)", "the if's branch"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_02 = SubjectCurriculum(grade=5, subject_id="G5-02",
    subject_title="if as expression", fable="goose-eggs",
    examples=[
        _ex("(+ 1 (if true 10 20))", 11,
            "the form (+ 1 (if true 10 20))", "the result of adding 1 to the if expression"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_03 = SubjectCurriculum(grade=5, subject_id="G5-03",
    subject_title="when", fable="goose-eggs",
    examples=[
        _ex("(when true :yes)", ":yes", "the form (when true :yes)", "the value of (when true :yes)"),
        _ex("(when false :yes)", None, "the form (when false :yes)", "the value of (when false :yes)"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_04 = SubjectCurriculum(grade=5, subject_id="G5-04",
    subject_title="cond", fable="goose-eggs",
    examples=[
        _ex("(cond (= 1 2) :a (= 1 1) :b :else :c)", ":b",
            "the cond form", "which clause of the cond fires"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_05 = SubjectCurriculum(grade=5, subject_id="G5-05",
    subject_title="cond — :else", fable="goose-eggs",
    examples=[
        _ex("(cond false :a false :b :else :c)", ":c",
            "the cond falling through to :else", "the :else value"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_06 = SubjectCurriculum(grade=5, subject_id="G5-06",
    subject_title="case", fable="goose-eggs",
    examples=[
        _ex("(case 2 1 :one 2 :two 3 :three :default)", ":two",
            "the case form", "the matched branch"),
        _ex("(case 99 1 :one 2 :two :default)", ":default",
            "case falling through to default", "the default branch"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_07 = SubjectCurriculum(grade=5, subject_id="G5-07",
    subject_title="and / or as control flow", fable="goose-eggs",
    examples=[
        _ex("(and 1 2 3)", 3, "the form (and 1 2 3) returns last truthy", "the last truthy value"),
        _ex("(or nil false :found)", ":found", "the form (or nil false :found)", "the first truthy value"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_08 = SubjectCurriculum(grade=5, subject_id="G5-08",
    subject_title="not", fable="goose-eggs",
    examples=[
        _ex("(not (> 1 2))", True, "the form (not (> 1 2))", "the negated comparison"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_09 = SubjectCurriculum(grade=5, subject_id="G5-09",
    subject_title="fn as value", fable="goose-eggs",
    examples=[
        _ex("((fn [f x] (f (f x))) inc 5)", 7,
            "applying f twice to x where f is inc", "the result of inc applied twice"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_10 = SubjectCurriculum(grade=5, subject_id="G5-10",
    subject_title="map", fable="goose-eggs",
    examples=[
        _ex("(map inc [1 2 3])", [2,3,4],
            "the form (map inc [1 2 3])", "[1 2 3] each incremented"),
        _ex("(map #(* % %) [1 2 3 4])", [1,4,9,16],
            "the form (map #(* % %) [1 2 3 4])", "[1 2 3 4] each squared"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_11 = SubjectCurriculum(grade=5, subject_id="G5-11",
    subject_title="filter", fable="goose-eggs",
    examples=[
        _ex("(filter even? [1 2 3 4])", [2,4],
            "the form (filter even? [1 2 3 4])", "the even numbers from [1 2 3 4]"),
        _ex("(filter pos? [-2 -1 0 1 2])", [1,2],
            "the form (filter pos? ...)", "the positive numbers"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_12 = SubjectCurriculum(grade=5, subject_id="G5-12",
    subject_title="reduce", fable="goose-eggs",
    examples=[
        _ex("(reduce + [1 2 3 4])",   10, "the form (reduce + [1 2 3 4])", "the sum"),
        _ex("(reduce * [1 2 3 4 5])", 120,"the form (reduce * [1 2 3 4 5])", "5!"),
        _ex("(reduce max [3 1 4 1 5 9 2 6])", 9,
            "the form (reduce max [...])", "the maximum"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_13 = SubjectCurriculum(grade=5, subject_id="G5-13",
    subject_title="reduce with init", fable="goose-eggs",
    examples=[
        _ex("(reduce + 100 [1 2 3])", 106,
            "the form (reduce + 100 [1 2 3])", "100 + sum of [1 2 3]"),
        _ex("(reduce + 0 [])", 0,
            "the form (reduce + 0 [])",
            "the value when reducing over empty seq with init 0"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_14 = SubjectCurriculum(grade=5, subject_id="G5-14",
    subject_title="apply", fable="goose-eggs",
    examples=[
        _ex("(apply + [1 2 3 4])", 10,
            "the form (apply + [1 2 3 4])", "+ applied to the elements of the vector"),
        _ex("(apply max [3 1 4 1 5])", 5,
            "the form (apply max ...)", "max of the vector via apply"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_15 = SubjectCurriculum(grade=5, subject_id="G5-15",
    subject_title="comp", fable="goose-eggs",
    examples=[
        _ex("((comp inc inc) 5)", 7,
            "the form ((comp inc inc) 5)", "inc twice applied to 5"),
        _ex("((comp str inc) 9)", "10",
            "the form ((comp str inc) 9)", "inc then str of 9"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_16 = SubjectCurriculum(grade=5, subject_id="G5-16",
    subject_title="partial", fable="goose-eggs",
    examples=[
        _ex("((partial + 10) 5)", 15,
            "the form ((partial + 10) 5)", "10 + 5"),
        _ex("(map (partial * 3) [1 2 3])", [3,6,9],
            "(partial * 3) mapped over [1 2 3]", "each element times 3"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_17 = SubjectCurriculum(grade=5, subject_id="G5-17",
    subject_title="juxt", fable="goose-eggs",
    examples=[
        _ex("((juxt inc dec) 5)", [6,4],
            "the form ((juxt inc dec) 5)", "inc and dec of 5 in parallel"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_18 = SubjectCurriculum(grade=5, subject_id="G5-18",
    subject_title="some", fable="goose-eggs",
    examples=[
        _ex("(some even? [1 3 5 8 7])", True,
            "the form (some even? [...])", "whether any element is even"),
        _ex("(some neg? [1 2 3])", None,
            "the form (some neg? [1 2 3])", "the value when no element is negative (it's nil)"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_19 = SubjectCurriculum(grade=5, subject_id="G5-19",
    subject_title="every?", fable="goose-eggs",
    examples=[
        _ex("(every? pos? [1 2 3])", True, "the form (every? pos? [1 2 3])", "whether all are positive"),
        _ex("(every? even? [1 2 3])", False, "the form (every? even? [1 2 3])", "whether all are even"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_20 = SubjectCurriculum(grade=5, subject_id="G5-20",
    subject_title="take and drop", fable="goose-eggs",
    examples=[
        _ex("(take 3 [10 20 30 40 50])", [10,20,30],
            "the form (take 3 ...)", "the first three elements"),
        _ex("(drop 2 [10 20 30 40 50])", [30,40,50],
            "the form (drop 2 ...)", "all but the first two"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_21 = SubjectCurriculum(grade=5, subject_id="G5-21",
    subject_title="distinct and sort", fable="goose-eggs",
    examples=[
        _ex("(distinct [1 1 2 3 3 4])", [1,2,3,4],
            "the form (distinct [1 1 2 3 3 4])", "the deduplicated seq"),
        _ex("(sort [3 1 2])", [1,2,3],
            "the form (sort [3 1 2])", "the sorted seq"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


G5_22 = SubjectCurriculum(grade=5, subject_id="G5-22",
    subject_title="recur — first taste", fable="goose-eggs",
    examples=[
        _ex("(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))", 120,
            "a loop computing factorial of 5 via recur",
            "5! computed via loop/recur"),
    ], subplots=_HOF_SUBPLOTS, plan_pool=_PLAN_G5)


SUBJECTS = {s.subject_id: s for s in (
    G5_01, G5_02, G5_03, G5_04, G5_05, G5_06, G5_07, G5_08, G5_09, G5_10,
    G5_11, G5_12, G5_13, G5_14, G5_15, G5_16, G5_17, G5_18, G5_19, G5_20,
    G5_21, G5_22,
)}


def smoke_test() -> None:
    from mmllm.aesop.curriculum.generator import generate_subject
    for sid, sub in SUBJECTS.items():
        recs = generate_subject(sub, n_per_example=1, seed=0)
        for r in recs: assert r.tool_calls[0]["name"] == "eval"
    print(f"grade-5 goose-eggs smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
