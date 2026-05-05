"""Grade 5 — control flow + higher-order intro. Through tortoise-hare."""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.tortoise_hare.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS,
    _GOAL_SUBPLOTS,
    _PLAN_POOL,
)




def _ex(form, expected, concept, what, goal="", tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal, tags=tags)


_PLAN_G5 = _PLAN_POOL + (
    "I use map / filter / reduce as appropriate.",
    "I write the higher-order form so the REPL can compute.",
)


G5_01 = SubjectCurriculum(grade=5, subject_id="G5-01",
    subject_title="if", fable="tortoise-hare",
    examples=[
        _ex("(if true :a :b)",  ":a", "the conditional", "which of :a or :b is returned",
            goal="choose between :a and :b based on a true condition"),
        _ex("(if false :a :b)", ":b", "the conditional", "which of :a or :b is returned",
            goal="choose between :a and :b based on a false condition"),
        _ex("(if (> 5 3) :a :b)", ":a", "the conditional", "the if's branch",
            goal="choose between :a and :b based on whether 5 is greater than 3"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_02 = SubjectCurriculum(grade=5, subject_id="G5-02",
    subject_title="if as expression", fable="tortoise-hare",
    examples=[
        _ex("(+ 1 (if true 10 20))", 11,
            "the arithmetic expression with conditional", "the result of adding 1 to the conditional value",
            goal="add 1 to the result of choosing between 10 and 20 based on a true condition"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_03 = SubjectCurriculum(grade=5, subject_id="G5-03",
    subject_title="when", fable="tortoise-hare",
    examples=[
        _ex("(when true :yes)", ":yes", "the when conditional", "the value when the condition is true",
            goal="evaluate a when form with a true condition"),
        _ex("(when false :yes)", None, "the when conditional", "the value when the condition is false",
            goal="evaluate a when form with a false condition"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_04 = SubjectCurriculum(grade=5, subject_id="G5-04",
    subject_title="cond", fable="tortoise-hare",
    examples=[
        _ex("(cond (= 1 2) :a (= 1 1) :b :else :c)", ":b",
            "the multi-clause conditional", "which clause of the cond fires",
            goal="evaluate multiple conditions in sequence and return the value from the first true clause"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_05 = SubjectCurriculum(grade=5, subject_id="G5-05",
    subject_title="cond — :else", fable="tortoise-hare",
    examples=[
        _ex("(cond false :a false :b :else :c)", ":c",
            "the cond with default clause", "the default value when no clauses match",
            goal="fall through all false conditions and return the default value"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_06 = SubjectCurriculum(grade=5, subject_id="G5-06",
    subject_title="case", fable="tortoise-hare",
    examples=[
        _ex("(case 2 1 :one 2 :two 3 :three :default)", ":two",
            "the case statement", "the matched branch",
            goal="match the value 2 against clauses and return the corresponding value"),
        _ex("(case 99 1 :one 2 :two :default)", ":default",
            "the case statement with default", "the default branch",
            goal="match the value 99 against clauses and return the default when no match is found"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_07 = SubjectCurriculum(grade=5, subject_id="G5-07",
    subject_title="and / or as control flow", fable="tortoise-hare",
    examples=[
        _ex("(and 1 2 3)", 3, "the and conjunction", "the last truthy value",
            goal="return the last value when all values are truthy"),
        _ex("(or nil false :found)", ":found", "the or disjunction", "the first truthy value",
            goal="return the first truthy value from a sequence of values"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_08 = SubjectCurriculum(grade=5, subject_id="G5-08",
    subject_title="not", fable="tortoise-hare",
    examples=[
        _ex("(not (> 1 2))", True, "the negation", "the negated comparison",
            goal="negate the result of checking whether 1 is greater than 2"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_09 = SubjectCurriculum(grade=5, subject_id="G5-09",
    subject_title="fn as value", fable="tortoise-hare",
    examples=[
        _ex("((fn [f x] (f (f x))) inc 5)", 7,
            "applying a function twice", "the result of inc applied twice",
            goal="apply the inc function twice to 5"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_10 = SubjectCurriculum(grade=5, subject_id="G5-10",
    subject_title="map", fable="tortoise-hare",
    examples=[
        _ex("(map inc [1 2 3])", [2,3,4],
            "mapping increment over a vector", "[1 2 3] each incremented",
            goal="apply inc to each element of the vector containing 1, 2, and 3, returning a sequence"),
        _ex("(map #(* % %) [1 2 3 4])", [1,4,9,16],
            "mapping a squaring operation over a vector", "[1 2 3 4] each squared",
            goal="apply a squaring operation to each element of the vector containing 1, 2, 3, and 4, returning a sequence"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_11 = SubjectCurriculum(grade=5, subject_id="G5-11",
    subject_title="filter", fable="tortoise-hare",
    examples=[
        _ex("(filter even? [1 2 3 4])", [2,4],
            "filtering even elements from a vector", "the even numbers from [1 2 3 4]",
            goal="keep the even elements from the vector containing 1, 2, 3, and 4"),
        _ex("(filter pos? [-2 -1 0 1 2])", [1,2],
            "filtering positive elements from a vector", "the positive numbers",
            goal="keep the positive elements from the vector containing -2, -1, 0, 1, and 2"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_12 = SubjectCurriculum(grade=5, subject_id="G5-12",
    subject_title="reduce", fable="tortoise-hare",
    examples=[
        _ex("(reduce + [1 2 3 4])",   10, "the fold operation", "the sum",
            goal="fold + over the vector containing 1, 2, 3, and 4, summing them"),
        _ex("(reduce * [1 2 3 4 5])", 120,"the fold operation", "5!",
            goal="fold * over the vector containing 1, 2, 3, 4, and 5, computing their product"),
        _ex("(reduce max [3 1 4 1 5 9 2 6])", 9,
            "the fold operation", "the maximum",
            goal="fold max over the vector containing 3, 1, 4, 1, 5, 9, 2, and 6, finding the maximum"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_13 = SubjectCurriculum(grade=5, subject_id="G5-13",
    subject_title="reduce with init", fable="tortoise-hare",
    examples=[
        _ex("(reduce + 100 [1 2 3])", 106,
            "the fold with initial value", "the sum starting from 100",
            goal="fold + over the vector containing 1, 2, 3 starting from an initial accumulator of 100"),
        _ex("(reduce + 0 [])", 0,
            "the fold with initial value over empty sequence", "the value when reducing over empty seq with init 0",
            goal="fold + over an empty sequence starting from an initial accumulator of 0"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_14 = SubjectCurriculum(grade=5, subject_id="G5-14",
    subject_title="apply", fable="tortoise-hare",
    examples=[
        _ex("(apply + [1 2 3 4])", 10,
            "applying + to vector elements", "the sum via apply",
            goal="apply + to the elements of the vector containing 1, 2, 3, and 4"),
        _ex("(apply max [3 1 4 1 5])", 5,
            "applying max to vector elements", "max of the vector via apply",
            goal="apply max to the elements of the vector containing 3, 1, 4, 1, and 5"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_15 = SubjectCurriculum(grade=5, subject_id="G5-15",
    subject_title="comp", fable="tortoise-hare",
    examples=[
        _ex("((comp inc inc) 5)", 7,
            "composing inc twice", "inc applied twice to 5",
            goal="compose two inc functions and apply them to 5"),
        _ex("((comp str inc) 9)", "10",
            "composing str and inc", "the string representation of 9 incremented",
            goal="compose str and inc functions and apply them to 9"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_16 = SubjectCurriculum(grade=5, subject_id="G5-16",
    subject_title="partial", fable="tortoise-hare",
    examples=[
        _ex("((partial + 10) 5)", 15,
            "partial application of +", "10 + 5",
            goal="apply + with 10 as the first argument and 5 as the second"),
        _ex("(map (partial * 3) [1 2 3])", [3,6,9],
            "mapping partial multiplication over a vector", "each element times 3",
            goal="apply a partially applied multiplication to each element of the vector containing 1, 2, and 3"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_17 = SubjectCurriculum(grade=5, subject_id="G5-17",
    subject_title="juxt", fable="tortoise-hare",
    examples=[
        _ex("((juxt inc dec) 5)", [6,4],
            "juxtaposing inc and dec", "inc and dec of 5 in parallel",
            goal="apply both inc and dec functions to 5 and return both results as a vector"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_18 = SubjectCurriculum(grade=5, subject_id="G5-18",
    subject_title="some", fable="tortoise-hare",
    examples=[
        _ex("(some even? [1 3 5 8 7])", True,
            "checking if any element satisfies a predicate", "whether any element is even",
            goal="check if any element in the vector containing 1, 3, 5, 8, and 7 is even"),
        _ex("(some neg? [1 2 3])", None,
            "checking if any element satisfies a predicate", "the value when no element is negative",
            goal="check if any element in the vector containing 1, 2, and 3 is negative"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_19 = SubjectCurriculum(grade=5, subject_id="G5-19",
    subject_title="every?", fable="tortoise-hare",
    examples=[
        _ex("(every? pos? [1 2 3])", True, "checking if all elements satisfy a predicate", "whether all are positive",
            goal="check if all elements in the vector containing 1, 2, and 3 are positive"),
        _ex("(every? even? [1 2 3])", False, "checking if all elements satisfy a predicate", "whether all are even",
            goal="check if all elements in the vector containing 1, 2, and 3 are even"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_20 = SubjectCurriculum(grade=5, subject_id="G5-20",
    subject_title="take and drop", fable="tortoise-hare",
    examples=[
        _ex("(take 3 [10 20 30 40 50])", [10,20,30],
            "taking elements from a sequence", "the first three elements",
            goal="take the first 3 elements from the vector containing 10, 20, 30, 40, and 50"),
        _ex("(drop 2 [10 20 30 40 50])", [30,40,50],
            "dropping elements from a sequence", "all but the first two",
            goal="drop the first 2 elements from the vector containing 10, 20, 30, 40, and 50"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_21 = SubjectCurriculum(grade=5, subject_id="G5-21",
    subject_title="distinct and sort", fable="tortoise-hare",
    examples=[
        _ex("(distinct [1 1 2 3 3 4])", [1,2,3,4],
            "removing duplicates from a sequence", "the deduplicated seq",
            goal="remove duplicate elements from the vector containing 1, 1, 2, 3, 3, and 4"),
        _ex("(sort [3 1 2])", [1,2,3],
            "sorting a sequence", "the sorted seq",
            goal="sort the vector containing 3, 1, and 2 in ascending order"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


G5_22 = SubjectCurriculum(grade=5, subject_id="G5-22",
    subject_title="recur — first taste", fable="tortoise-hare",
    examples=[
        _ex("(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))", 120,
            "a factorial computation via loop and recur",
            "5! computed via loop/recur",
            goal="compute the factorial of 5 using a loop and tail recursion"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G5)


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
    print(f"grade-5 tortoise-hare smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
