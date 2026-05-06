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
from mmllm.aesop.curriculum.tortoise_hare._metaphor_pools import (
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
    subject_title="if", fable="tortoise-hare",
    examples=[
        _ex("(if true :a :b)",  ":a", "the conditional", "which of :a or :b is returned",
            goal="choose between :a and :b based on a true condition"),
        _ex("(if false :a :b)", ":b", "the conditional", "which of :a or :b is returned",
            goal="choose between :a and :b based on a false condition"),
        _ex("(if (> 5 3) :a :b)", ":a", "the conditional", "the if's branch",
            goal="choose between :a and :b based on whether 5 is greater than 3"),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_02 = SubjectCurriculum(grade=5, subject_id="G5-02",
    subject_title="if as expression", fable="tortoise-hare",
    examples=[
        _ex("(+ 1 (if true 10 20))", 11,
            "the arithmetic expression with conditional", "the result of adding 1 to the conditional value",
            goal="add 1 to the result of choosing between 10 and 20 based on a true condition"),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_03 = SubjectCurriculum(grade=5, subject_id="G5-03",
    subject_title="when", fable="tortoise-hare",
    examples=[
        _ex("(when true :yes)", ":yes", "the when conditional", "the value when the condition is true",
            goal="evaluate a when form with a true condition"),
        _ex("(when false :yes)", None, "the when conditional", "the value when the condition is false",
            goal="evaluate a when form with a false condition"),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_04 = SubjectCurriculum(grade=5, subject_id="G5-04",
    subject_title="cond", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(cond (= 1 2) :a (= 1 1) :b :else :c)",
            expected=":b",
            concept_phrase="the multi-clause conditional",
            question_what="the value of the first arm whose stone reads true",
            goal_text="walk three condition-stones in order, taking the arm whose stone first reads true",
            scenario=(
                "The trail forked into three arms, each marked by a "
                "small condition-stone — the first carved `(= 1 2)`, "
                "the second `(= 1 1)`, the third `:else`."
            ),
            need=(
                "Mossback the tortoise wanted the runtime to walk the "
                "stones in order and take the first arm whose stone "
                "read true."
            ),
            mapping=(
                "`cond` walks each (condition, value) pair in order. "
                "The first stone is false (skip), the second is true "
                "(take that arm; return its value); the third is never "
                "reached."
            ),
            resolution=(
                "the runtime took the second arm and returned :b, the "
                "value that arm carried."
            ),
            tags=("story",),
        ),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_05 = SubjectCurriculum(grade=5, subject_id="G5-05",
    subject_title="cond — :else", fable="tortoise-hare",
    examples=[
        _ex("(cond false :a false :b :else :c)", ":c",
            "the cond with default clause", "the default value when no clauses match",
            goal="fall through all false conditions and return the default value"),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_06 = SubjectCurriculum(grade=5, subject_id="G5-06",
    subject_title="case", fable="tortoise-hare",
    examples=[
        _ex("(case 2 1 :one 2 :two 3 :three :default)", ":two",
            "the case statement", "the matched branch",
            goal="match the value 2 against clauses and return the corresponding value"),
        _ex("(case 99 1 :one 2 :two :default)", ":default",
            "the case statement with default", "the default branch",
            goal="match the value 99 against clauses and return the default when no match is found"),
    ], subplots=_FORK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_07 = SubjectCurriculum(grade=5, subject_id="G5-07",
    subject_title="and / or as control flow", fable="tortoise-hare",
    examples=[
        _ex("(and 1 2 3)", 3, "the and conjunction", "the last truthy value",
            goal="return the last value when all values are truthy"),
        _ex("(or nil false :found)", ":found", "the or disjunction", "the first truthy value",
            goal="return the first truthy value from a sequence of values"),
    ], subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_08 = SubjectCurriculum(grade=5, subject_id="G5-08",
    subject_title="not", fable="tortoise-hare",
    examples=[
        _ex("(not (> 1 2))", True, "the negation", "the negated comparison",
            goal="negate the result of checking whether 1 is greater than 2"),
    ], subplots=_GATE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_09 = SubjectCurriculum(grade=5, subject_id="G5-09",
    subject_title="fn as value", fable="tortoise-hare",
    examples=[
        _ex("((fn [f x] (f (f x))) inc 5)", 7,
            "applying a function twice", "the result of inc applied twice",
            goal="apply the inc function twice to 5"),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_10 = SubjectCurriculum(grade=5, subject_id="G5-10",
    subject_title="map", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(map inc [1 2 3])",
            expected=[2,3,4],
            concept_phrase="mapping increment over a vector",
            question_what="the sequence produced by passing the vector containing 1, 2, and 3 through the inc-sieve",
            goal_text="pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collecting each transformed element",
            scenario=(
                "A row of three small acorns lay on a flat stone — "
                "the morning's first gathering, with counts of 1, 2, "
                "and 3."
            ),
            need=(
                "Each acorn was missing a single bud at the cap. "
                "Mossback the tortoise wanted to add one bud to every "
                "acorn before sending the row to market — without "
                "pulling the row apart."
            ),
                mapping=(
                "`map` is a sieve with a rule attached at its mouth. "
                "Pour the row through, and each acorn passes the rule — "
                "here, `inc`, adding one bud — coming out the other "
                "side budded by one. The shape stays a row; only the "
                "counts step up."
            ),
            resolution=(
                "what landed below the sieve was the same three acorns, "
                "each budded one more — counts of 2, 3, and 4."
            ),
            tags=("story",),
        ),
        _ex("(map #(* % %) [1 2 3 4])", [1,4,9,16],
            "mapping a squaring operation over a vector", "the sequence produced by mapping a lambda that squares its argument over the vector containing 1, 2, 3, and 4",
            goal="apply a squaring operation to each element of the vector containing 1, 2, 3, and 4, returning a sequence"),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_11 = SubjectCurriculum(grade=5, subject_id="G5-11",
    subject_title="filter", fable="tortoise-hare",
    examples=[
        _ex("(filter even? [1 2 3 4])", [2,4],
            "filtering even elements from a vector", "the sequence produced by filtering even? over the vector containing 1, 2, 3, and 4",
            goal="keep the even elements from the vector containing 1, 2, 3, and 4"),
        _ex("(filter pos? [-2 -1 0 1 2])", [1,2],
            "filtering positive elements from a vector", "the sequence produced by filtering pos? over the vector containing -2, -1, 0, 1, and 2",
            goal="keep the positive elements from the vector containing -2, -1, 0, 1, and 2"),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_12 = SubjectCurriculum(grade=5, subject_id="G5-12",
    subject_title="reduce", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(reduce + [1 2 3 4])",
            expected=10,
            concept_phrase="the fold operation",
            question_what="the running tally after walking 1, 2, 3, 4 with + as the combine step",
            goal_text="walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with + into the running total",
            scenario=(
                "A row of four small pebbles lay along the path — "
                "counts of 1, 2, 3, and 4 from four foraging trips."
            ),
            need=(
                "Mossback the tortoise wanted the grand total of the "
                "four trips. Walking the row and carrying a running "
                "tally was the patient way."
            ),
            mapping=(
                "`reduce` walks the collection from left to right "
                "carrying a tally. At each pebble, the combine "
                "function (here `+`) is applied to (tally, pebble), "
                "producing the new tally. The final tally is what "
                "comes back."
            ),
            resolution=(
                "the walk produced a tally that grew across the four "
                "pebbles, ending at the grand total of all four "
                "trips."
            ),
            tags=("story",),
        ),
        _ex("(reduce * [1 2 3 4 5])", 120,"the fold operation", "the product produced by reducing * over the vector containing 1, 2, 3, 4, and 5",
            goal="fold * over the vector containing 1, 2, 3, 4, and 5, computing their product"),
        _ex("(reduce max [3 1 4 1 5 9 2 6])", 9,
            "the fold operation", "the maximum produced by reducing max over the vector containing 3, 1, 4, 1, 5, 9, 2, and 6",
            goal="fold max over the vector containing 3, 1, 4, 1, 5, 9, 2, and 6, finding the maximum"),
    ], subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_13 = SubjectCurriculum(grade=5, subject_id="G5-13",
    subject_title="reduce with init", fable="tortoise-hare",
    examples=[
        _ex("(reduce + 100 [1 2 3])", 106,
            "the fold with initial value", "the sum produced by reducing + over the vector containing 1, 2, and 3 with an initial value of 100",
            goal="fold + over the vector containing 1, 2, 3 starting from an initial accumulator of 100"),
        _ex("(reduce + 0 [])", 0,
            "the fold with initial value over empty sequence", "the result of reducing + over an empty vector with an initial value of 0",
            goal="fold + over an empty sequence starting from an initial accumulator of 0"),
    ], subplots=_TALLYWALK_SUBPLOTS, plan_pool=_PLAN_G5)


G5_14 = SubjectCurriculum(grade=5, subject_id="G5-14",
    subject_title="apply", fable="tortoise-hare",
    examples=[
        _ex("(apply + [1 2 3 4])", 10,
            "applying + to vector elements", "the result of applying + to the elements of the vector containing 1, 2, 3, and 4",
            goal="apply + to the elements of the vector containing 1, 2, 3, and 4"),
        _ex("(apply max [3 1 4 1 5])", 5,
            "applying max to vector elements", "the result of applying max to the elements of the vector containing 3, 1, 4, 1, and 5",
            goal="apply max to the elements of the vector containing 3, 1, 4, 1, and 5"),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_15 = SubjectCurriculum(grade=5, subject_id="G5-15",
    subject_title="comp", fable="tortoise-hare",
    examples=[
        _ex("((comp inc inc) 5)", 7,
            "composing inc twice", "the result of applying the composition of inc and inc to 5",
            goal="compose two inc functions and apply them to 5"),
        _ex("((comp str inc) 9)", "10",
            "composing str and inc", "the result of applying the composition of str and inc to 9",
            goal="compose str and inc functions and apply them to 9"),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_16 = SubjectCurriculum(grade=5, subject_id="G5-16",
    subject_title="partial", fable="tortoise-hare",
    examples=[
        _ex("((partial + 10) 5)", 15,
            "partial application of +", "the result of applying a partially applied + function with first argument 10 to 5",
            goal="apply + with 10 as the first argument and 5 as the second"),
        _ex("(map (partial * 3) [1 2 3])", [3,6,9],
            "mapping partial multiplication over a vector", "the sequence produced by mapping a partially applied multiplication function with first argument 3 over the vector containing 1, 2, and 3",
            goal="apply a partially applied multiplication to each element of the vector containing 1, 2, and 3"),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_17 = SubjectCurriculum(grade=5, subject_id="G5-17",
    subject_title="juxt", fable="tortoise-hare",
    examples=[
        _ex("((juxt inc dec) 5)", [6,4],
            "juxtaposing inc and dec", "the vector produced by applying juxt to inc and dec with argument 5",
            goal="apply both inc and dec functions to 5 and return both results as a vector"),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_18 = SubjectCurriculum(grade=5, subject_id="G5-18",
    subject_title="some", fable="tortoise-hare",
    examples=[
        _ex("(some even? [1 3 5 8 7])", True,
            "checking if any element satisfies a predicate", "the result of applying some with even? to the vector containing 1, 3, 5, 8, and 7",
            goal="check if any element in the vector containing 1, 3, 5, 8, and 7 is even"),
        _ex("(some neg? [1 2 3])", None,
            "checking if any element satisfies a predicate", "the result of applying some with neg? to the vector containing 1, 2, and 3",
            goal="check if any element in the vector containing 1, 2, and 3 is negative"),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_19 = SubjectCurriculum(grade=5, subject_id="G5-19",
    subject_title="every?", fable="tortoise-hare",
    examples=[
        _ex("(every? pos? [1 2 3])", True, "checking if all elements satisfy a predicate", "the result of applying every? with pos? to the vector containing 1, 2, and 3",
            goal="check if all elements in the vector containing 1, 2, and 3 are positive"),
        _ex("(every? even? [1 2 3])", False, "checking if all elements satisfy a predicate", "the result of applying every? with even? to the vector containing 1, 2, and 3",
            goal="check if all elements in the vector containing 1, 2, and 3 are even"),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_20 = SubjectCurriculum(grade=5, subject_id="G5-20",
    subject_title="take and drop", fable="tortoise-hare",
    examples=[
        _ex("(take 3 [10 20 30 40 50])", [10,20,30],
            "taking elements from a sequence", "the sequence produced by taking 3 elements from the vector containing 10, 20, 30, 40, and 50",
            goal="take the first 3 elements from the vector containing 10, 20, 30, 40, and 50"),
        _ex("(drop 2 [10 20 30 40 50])", [30,40,50],
            "dropping elements from a sequence", "the sequence produced by dropping 2 elements from the vector containing 10, 20, 30, 40, and 50",
            goal="drop the first 2 elements from the vector containing 10, 20, 30, 40, and 50"),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_21 = SubjectCurriculum(grade=5, subject_id="G5-21",
    subject_title="distinct and sort", fable="tortoise-hare",
    examples=[
        _ex("(distinct [1 1 2 3 3 4])", [1,2,3,4],
            "removing duplicates from a sequence", "the sequence produced by applying distinct to the vector containing 1, 1, 2, 3, 3, and 4",
            goal="remove duplicate elements from the vector containing 1, 1, 2, 3, 3, and 4"),
        _ex("(sort [3 1 2])", [1,2,3],
            "sorting a sequence", "the sequence produced by applying sort to the vector containing 3, 1, and 2",
            goal="sort the vector containing 3, 1, and 2 in ascending order"),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G5)


G5_22 = SubjectCurriculum(grade=5, subject_id="G5-22",
    subject_title="recur — first taste", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n))))",
            expected=120,
            concept_phrase="a factorial computation via loop and recur",
            question_what="the factorial of 5 computed by walking a circuit",
            goal_text="walk a small circuit five times, multiplying a running tally by the current step each lap, until the step counter reaches zero",
            scenario=(
                "Mossback the tortoise wanted to compute 5! — the "
                "product 5 × 4 × 3 × 2 × 1 — without writing five "
                "separate multiplications."
            ),
            need=(
                "She'd walk a small circuit around a stone, each lap "
                "multiplying her tally by the current step, until the "
                "step counter reached zero — then return the tally."
            ),
            mapping=(
                "`loop`/`recur` is the circuit. `loop [n 5 acc 1]` "
                "starts the bindings; `recur` jumps back to the top "
                "with new bindings — `(dec n)` and `(* acc n)` — "
                "without growing the call-stack. The base case "
                "`(zero? n)` returns `acc`."
            ),
            resolution=(
                "five laps later the step counter reached zero and the "
                "tally — 5! — came back."
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
    print(f"grade-5 tortoise-hare smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
