"""Grade 5 — control flow + higher-order intro. Through crow-pitcher."""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.crow_pitcher.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS,
    _GOAL_SUBPLOTS,
    _PLAN_POOL,
)
from mmllm.aesop.curriculum.crow_pitcher._metaphor_pools import (
    _CIRCUIT_SUBPLOTS, _FORK_SUBPLOTS, _GATE_SUBPLOTS, _RECIPE_SUBPLOTS, _SIEVE_SUBPLOTS, _TALLYWALK_SUBPLOTS,
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
    subject_title="if", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(if true :a :b)",
            expected=":a",
            concept_phrase="the conditional",
            question_what="which of :a or :b is returned",
            goal_text="choose between :a and :b based on a true condition",

            scenario=(
                "Sable perched above the pitcher's mouth at the orchard's "
                "edge, the fork-path clear below: one branch drops a stone "
                "marked :a, the other drops one marked :b. She tested "
                "the condition first."
            ),
            need=(
                "The condition was `true` — already settled. She needed to "
                "know which branch would release its stone into the pitcher."
            ),
            mapping=(
                "`if` reads the condition first: if truthy, the then-branch "
                "releases; if falsy, the else-branch releases. `true` is "
                "unmistakably truthy — the :a branch releases, :b stays back."
            ),
            resolution=(
                ":a — the then-branch released its stone, the :b stone "
                "resting where it was, the water rising one mark."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(if false :a :b)",
            expected=":b",
            concept_phrase="the conditional",
            question_what="which of :a or :b is returned",
            goal_text="choose between :a and :b based on a false condition",
        ),
        SubjectExample(
            form="(if (> 5 3) :a :b)",
            expected=":a",
            concept_phrase="the conditional",
            question_what="the if's branch",
            goal_text="choose between :a and :b based on whether 5 is greater than 3",
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_02 = SubjectCurriculum(grade=5, subject_id="G5-02",
    subject_title="if as expression", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(+ 1 (if true 10 20))",
            expected=11,
            concept_phrase="the arithmetic expression with conditional",
            question_what="the result of adding 1 to the conditional value",
            goal_text="add 1 to the result of choosing between 10 and 20 based on a true condition",
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_03 = SubjectCurriculum(grade=5, subject_id="G5-03",
    subject_title="when", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(when true :yes)",
            expected=":yes",
            concept_phrase="the when conditional",
            question_what="the value when the condition is true",
            goal_text="evaluate a when form with a true condition",
        ),
        SubjectExample(
            form="(when false :yes)",
            expected=None,
            concept_phrase="the when conditional",
            question_what="the value when the condition is false",
            goal_text="evaluate a when form with a false condition",
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_04 = SubjectCurriculum(grade=5, subject_id="G5-04",
    subject_title="cond", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(cond (= 1 2) :a (= 1 1) :b :else :c)",
            expected=":b",
            concept_phrase="the multi-clause conditional",
            question_what="the value of the first arm whose stone reads true",
            goal_text="walk three condition-stones in order, taking the arm whose stone first reads true",
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_05 = SubjectCurriculum(grade=5, subject_id="G5-05",
    subject_title="cond — :else", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(cond false :a false :b :else :c)",
            expected=":c",
            concept_phrase="the cond with default clause",
            question_what="the default value when no clauses match",
            goal_text="fall through all false conditions and return the default value",
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_06 = SubjectCurriculum(grade=5, subject_id="G5-06",
    subject_title="case", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(case 2 1 :one 2 :two 3 :three :default)",
            expected=":two",
            concept_phrase="the case statement",
            question_what="the matched branch",
            goal_text="match the value 2 against clauses and return the corresponding value",
        ),
        SubjectExample(
            form="(case 99 1 :one 2 :two :default)",
            expected=":default",
            concept_phrase="the case statement with default",
            question_what="the default branch",
            goal_text="match the value 99 against clauses and return the default when no match is found",
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_07 = SubjectCurriculum(grade=5, subject_id="G5-07",
    subject_title="and / or as control flow", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(and 1 2 3)",
            expected=3,
            concept_phrase="the and conjunction",
            question_what="the last truthy value",
            goal_text="return the last value when all values are truthy",
        ),
        SubjectExample(
            form="(or nil false :found)",
            expected=":found",
            concept_phrase="the or disjunction",
            question_what="the first truthy value",
            goal_text="return the first truthy value from a sequence of values",
        ),
    ], subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_08 = SubjectCurriculum(grade=5, subject_id="G5-08",
    subject_title="not", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(not (> 1 2))",
            expected=True,
            concept_phrase="the negation",
            question_what="the negated comparison",
            goal_text="negate the result of checking whether 1 is greater than 2",
        ),
    ], subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_09 = SubjectCurriculum(grade=5, subject_id="G5-09",
    subject_title="fn as value", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="((fn [f x] (f (f x))) inc 5)",
            expected=7,
            concept_phrase="applying a function twice",
            question_what="the result of inc applied twice",
            goal_text="apply the inc function twice to 5",
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_10 = SubjectCurriculum(grade=5, subject_id="G5-10",
    subject_title="map", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(map inc [1 2 3])",
            expected=[2,3,4],
            concept_phrase="mapping increment over a vector",
            question_what="the sequence produced by passing the vector containing 1, 2, and 3 through the inc-sieve",
            goal_text="pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collecting each transformed element",
        ),
        SubjectExample(
            form="(map #(* % %) [1 2 3 4])",
            expected=[1,4,9,16],
            concept_phrase="mapping a squaring operation over a vector",
            question_what="the sequence produced by mapping a squaring rule over the vector containing 1, 2, 3, and 4",
            goal_text="apply a squaring operation to each element of the vector containing 1, 2, 3, and 4, returning a sequence",
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_11 = SubjectCurriculum(grade=5, subject_id="G5-11",
    subject_title="filter", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(filter even? [1 2 3 4])",
            expected=[2,4],
            concept_phrase="filtering even elements from a vector",
            question_what="the sequence produced by filtering even? over the vector containing 1, 2, 3, and 4",
            goal_text="keep the even elements from the vector containing 1, 2, 3, and 4",

            scenario=(
                "Korvus held four numbered stones over the pitcher's "
                "sorting-perch in the meadow: 1, 2, 3, 4. He would pass "
                "each stone over the test-groove before deciding which dropped."
            ),
            need=(
                "He wanted only even-numbered stones to fall into the "
                "pitcher — odd ones should stay on the rim, even ones pass through."
            ),
            mapping=(
                "`filter` applies a predicate — here `even?` — to each "
                "element in turn. Stones that pass the test drop; stones that "
                "fail remain. The result holds only the passing stones, in order."
            ),
            resolution=(
                "[2 4] — the two even stones fell through, the odd-numbered "
                "ones resting on the rim untouched."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(filter pos? [-2 -1 0 1 2])",
            expected=[1,2],
            concept_phrase="filtering positive elements from a vector",
            question_what="the sequence produced by filtering pos? over the vector containing -2, -1, 0, 1, and 2",
            goal_text="keep the positive elements from the vector containing -2, -1, 0, 1, and 2",
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_12 = SubjectCurriculum(grade=5, subject_id="G5-12",
    subject_title="reduce", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(reduce + [1 2 3 4])",
            expected=10,
            concept_phrase="the fold operation",
            question_what="the running tally after walking 1, 2, 3, 4 with + as the combine step",
            goal_text="walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with + into the running total",
        ),
        SubjectExample(
            form="(reduce * [1 2 3 4 5])",
            expected=120,
            concept_phrase="the fold operation",
            question_what="the product produced by walking 1, 2, 3, 4, 5 with * as the combine step",
            goal_text="fold * over the vector containing 1, 2, 3, 4, and 5, computing their product",
        ),
        SubjectExample(
            form="(reduce max [3 1 4 1 5 9 2 6])",
            expected=9,
            concept_phrase="the fold operation",
            question_what="the largest pebble found by walking 3, 1, 4, 1, 5, 9, 2, 6 with max as the combine step",
            goal_text="fold max over the vector containing 3, 1, 4, 1, 5, 9, 2, and 6, finding the maximum",
        ),
    ], subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_13 = SubjectCurriculum(grade=5, subject_id="G5-13",
    subject_title="reduce with init", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(reduce + 100 [1 2 3])",
            expected=106,
            concept_phrase="the fold with initial value",
            question_what="the sum produced by walking 1, 2, 3 with + and an opening tally of 100",
            goal_text="fold + over the vector containing 1, 2, 3 starting from an initial accumulator of 100",
        ),
        SubjectExample(
            form="(reduce + 0 [])",
            expected=0,
            concept_phrase="the fold with initial value over empty sequence",
            question_what="the tally returned when walking an empty row with + and an opening tally of 0",
            goal_text="fold + over an empty sequence starting from an initial accumulator of 0",
        ),
    ], subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_14 = SubjectCurriculum(grade=5, subject_id="G5-14",
    subject_title="apply", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(apply + [1 2 3 4])",
            expected=10,
            concept_phrase="applying + to vector elements",
            question_what="the result of spreading the basket of 1, 2, 3, 4 as ingredients into +",
            goal_text="apply + to the elements of the vector containing 1, 2, 3, and 4",
        ),
        SubjectExample(
            form="(apply max [3 1 4 1 5])",
            expected=5,
            concept_phrase="applying max to vector elements",
            question_what="the largest count found after spreading the basket of 3, 1, 4, 1, 5 into max",
            goal_text="apply max to the elements of the vector containing 3, 1, 4, 1, and 5",
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_15 = SubjectCurriculum(grade=5, subject_id="G5-15",
    subject_title="comp", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="((comp inc inc) 5)",
            expected=7,
            concept_phrase="composing inc twice",
            question_what="the result of chaining two inc recipe-cards and applying them to 5",
            goal_text="compose two inc functions and apply them to 5",
        ),
        SubjectExample(
            form="((comp str inc) 9)",
            expected="10",
            concept_phrase="composing str and inc",
            question_what="the result of chaining the str and inc recipe-cards and applying them to 9",
            goal_text="compose str and inc functions and apply them to 9",
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_16 = SubjectCurriculum(grade=5, subject_id="G5-16",
    subject_title="partial", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="((partial + 10) 5)",
            expected=15,
            concept_phrase="partial application of +",
            question_what="the result of applying the half-loaded + card pre-filled with 10 to the count 5",
            goal_text="apply + with 10 as the first argument and 5 as the second",
        ),
        SubjectExample(
            form="(map (partial * 3) [1 2 3])",
            expected=[3,6,9],
            concept_phrase="mapping partial multiplication over a vector",
            question_what="the sequence produced by mapping the half-loaded * card pre-filled with 3 over the vector containing 1, 2, and 3",
            goal_text="apply a partially applied multiplication to each element of the vector containing 1, 2, and 3",
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_17 = SubjectCurriculum(grade=5, subject_id="G5-17",
    subject_title="juxt", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="((juxt inc dec) 5)",
            expected=[6,4],
            concept_phrase="juxtaposing inc and dec",
            question_what="the pair of results produced by asking both the inc and dec recipe-cards about 5",
            goal_text="apply both inc and dec functions to 5 and return both results as a vector",
        ),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_18 = SubjectCurriculum(grade=5, subject_id="G5-18",
    subject_title="some", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(some even? [1 3 5 8 7])",
            expected=True,
            concept_phrase="checking if any element satisfies a predicate",
            question_what="whether any pebble in 1, 3, 5, 8, 7 passes the even? sieve",
            goal_text="check if any element in the vector containing 1, 3, 5, 8, and 7 is even",
        ),
        SubjectExample(
            form="(some neg? [1 2 3])",
            expected=None,
            concept_phrase="checking if any element satisfies a predicate",
            question_what="whether any pebble in 1, 2, 3 passes the neg? sieve",
            goal_text="check if any element in the vector containing 1, 2, and 3 is negative",
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_19 = SubjectCurriculum(grade=5, subject_id="G5-19",
    subject_title="every?", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(every? pos? [1 2 3])",
            expected=True,
            concept_phrase="checking if all elements satisfy a predicate",
            question_what="whether every pebble in 1, 2, 3 passes the pos? sieve",
            goal_text="check if all elements in the vector containing 1, 2, and 3 are positive",
        ),
        SubjectExample(
            form="(every? even? [1 2 3])",
            expected=False,
            concept_phrase="checking if all elements satisfy a predicate",
            question_what="whether every pebble in 1, 2, 3 passes the even? sieve",
            goal_text="check if all elements in the vector containing 1, 2, and 3 are even",
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_20 = SubjectCurriculum(grade=5, subject_id="G5-20",
    subject_title="take and drop", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(take 3 [10 20 30 40 50])",
            expected=[10,20,30],
            concept_phrase="taking elements from a sequence",
            question_what="the sequence produced by taking 3 elements from the row of 10, 20, 30, 40, 50",
            goal_text="take the first 3 elements from the vector containing 10, 20, 30, 40, and 50",
        ),
        SubjectExample(
            form="(drop 2 [10 20 30 40 50])",
            expected=[30,40,50],
            concept_phrase="dropping elements from a sequence",
            question_what="the sequence produced by dropping 2 elements from the row of 10, 20, 30, 40, 50",
            goal_text="drop the first 2 elements from the vector containing 10, 20, 30, 40, and 50",
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_21 = SubjectCurriculum(grade=5, subject_id="G5-21",
    subject_title="distinct and sort", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(distinct [1 1 2 3 3 4])",
            expected=[1,2,3,4],
            concept_phrase="removing duplicates from a sequence",
            question_what="the sequence produced by passing 1, 1, 2, 3, 3, 4 through the dedup-sieve",
            goal_text="remove duplicate elements from the vector containing 1, 1, 2, 3, 3, and 4",
        ),
        SubjectExample(
            form="(sort [3 1 2])",
            expected=[1,2,3],
            concept_phrase="sorting a sequence",
            question_what="the sequence produced by sorting the row of 3, 1, 2 into ascending order",
            goal_text="sort the vector containing 3, 1, and 2 in ascending order",
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_22 = SubjectCurriculum(grade=5, subject_id="G5-22",
    subject_title="recur — first taste", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))",
            expected=120,
            concept_phrase="a factorial computation via loop and recur",
            question_what="the factorial of 5 computed by walking a circuit",
            goal_text="walk a small circuit five times, multiplying a running tally by the current step each lap, until the step counter reaches zero",

            scenario=(
                "Caw stood at the pitcher's rim in the hilltop field, a "
                "circuit chalked beneath her feet: start with n=5 and "
                "accumulator=1. Each lap, multiply the accumulator by n, "
                "step n down by one — loop without lifting from the rim."
            ),
            need=(
                "She needed to run the circuit until n hit zero, then read "
                "the final accumulated count as the answer."
            ),
            mapping=(
                "`loop` opens the circuit with initial bindings. `recur` "
                "loops back to the top without growing the call stack — no "
                "new flight, just another lap. When the zero-check passes "
                "`acc` is returned as the result."
            ),
            resolution=(
                "120 — five laps, the accumulator multiplied each pass, "
                "the final product surfacing when n hit zero."
            ),
            tags=("story",),
        ),
    ], subplots=_CIRCUIT_SUBPLOTS, plan_pool=_PLAN_G5)


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
    print(f"grade-5 crow-pitcher smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
