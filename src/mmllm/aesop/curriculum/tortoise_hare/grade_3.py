"""Grade 3 — naming, scope, substitution. Through tortoise-hare.

The fable lens: the Tortoise's careful approach is exactly the
substitution-rule discipline. The Hare's "I just know the answer"
is what binding-by-name corrects.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.tortoise_hare.grade_1 import (
    _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.tortoise_hare._metaphor_pools import (
    _POUCH_SUBPLOTS, _RECIPE_SUBPLOTS, _ROADSIGN_SUBPLOTS, _SCRIBE_SUBPLOTS,
)

# Add naming-themed subplots: a character names a value, then references it.
# Based on _GOAL_SUBPLOTS to ensure goal-driven design.
_NAMING_SUBPLOTS: list[SubplotTemplate] = list(_GOAL_SUBPLOTS) + [
    SubplotTemplate("""\
{tortoise_phrase} kept a small ledger {place} where every meaningful
quantity got its own name. {tortoise_he_she_cap} pointed to today's
entry, which required {goal_text}. {tortoise_he_she_cap} would write
{concept_phrase} and let the REPL confirm."""),

    SubplotTemplate("""\
"The key is to name your values carefully," {tortoise} said {place}.
"To {goal_text}, you write {concept_phrase} and submit it to the REPL.
That is the discipline." {hare_phrase} nodded, {emo_tired}."""),
]


def _ex(form, expected, concept, what, goal="", tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal, tags=tags)


_PLAN_POOL_G3 = _PLAN_POOL + (
    "I bind the inputs in a let, then compute.",
    "I name the values first and then combine them.",
    "I write the let-form so the REPL can substitute.",
)


G3_01 = SubjectCurriculum(grade=3, subject_id="G3-01",
    subject_title="def — top-level binding", fable="tortoise-hare",
    examples=[
        _ex("(do (def x 42) x)", 42, "the top-level binding and lookup",
            "the value of x after using def to bind x to 42",
            goal="bind x to 42 and return it"),
        _ex("(do (def y 7) y)",  7,  "the top-level binding",
            "the value of y after using def to bind y to 7",
            goal="bind y to 7 and return it"),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_02 = SubjectCurriculum(grade=3, subject_id="G3-02",
    subject_title="def — redefinition", fable="tortoise-hare",
    examples=[
        _ex("(do (def x 1) (def x 99) x)", 99,
            "the redefined binding",
            "the value of x after redefining it with def from 1 to 99",
            goal="bind x to 1, then redefine it as 99 and return it"),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_03 = SubjectCurriculum(grade=3, subject_id="G3-03",
    subject_title="let — local binding", fable="tortoise-hare",
    examples=[
        _ex("(let [x 3] (+ x 1))", 4, "the local binding and addition",
            "adding 1 to x after binding x locally to 3 via let",
            goal="bind x to 3 and add 1 to it"),
        _ex("(let [n 10] (* n n))", 100, "the local binding and multiplication",
            "multiplying n by itself after binding n locally to 10 via let",
            goal="bind n to 10 and compute n squared"),
        _ex("(let [a 5] a)", 5, "the local binding and lookup",
            "the value of a after binding it locally to 5 via let",
            goal="bind a to 5 and return it"),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_04 = SubjectCurriculum(grade=3, subject_id="G3-04",
    subject_title="let — multi-binding", fable="tortoise-hare",
    examples=[
        _ex("(let [a 1 b 2] (+ a b))", 3,
            "the multi-binding and addition",
            "adding a and b after binding both via let to 1 and 2",
            goal="bind a to 1 and b to 2, then add them"),
        _ex("(let [x 5 y 3] (- x y))", 2,
            "the multi-binding and subtraction",
            "subtracting y from x after binding via let to 5 and 3",
            goal="bind x to 5 and y to 3, then subtract y from x"),
        _ex("(let [a 2 b 3 c 4] (+ a b c))", 9,
            "the three-binding sum",
            "adding a, b, and c after binding via let to 2, 3, and 4",
            goal="bind a to 2, b to 3, c to 4, and add them"),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_05 = SubjectCurriculum(grade=3, subject_id="G3-05",
    subject_title="let — shadowing outer def", fable="tortoise-hare",
    examples=[
        _ex("(do (def x 10) (let [x 99] x))", 99,
            "the inner binding shadowing the outer",
            "the value of x inside the let scope where it shadows the def binding",
            goal="define x at the top level, then shadow it locally and return the inner value"),
        _ex("(do (def x 10) (let [x 99] x) x)", 10,
            "the outer binding after the let scope",
            "the value of x in the outer scope after the let scope ends",
            goal="define x, shadow it in a let, then look up x again in the outer scope"),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_06 = SubjectCurriculum(grade=3, subject_id="G3-06",
    subject_title="let — binding can reference prior", fable="tortoise-hare",
    examples=[
        _ex("(let [a 5 b (* a 2)] b)", 10,
            "the sequential binding where later refers to earlier",
            "the value of b, bound to twice a via let, after a is bound to 5",
            goal="bind a to 5, then bind b to twice a, and return b"),
        _ex("(let [a 3 b (+ a 1) c (* b 2)] c)", 8,
            "the chained bindings with sequential references",
            "the value of c, bound via let to twice b, after a is 3 and b is a+1",
            goal="bind a to 3, b to a+1, c to 2*b, and return c"),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_07 = SubjectCurriculum(grade=3, subject_id="G3-07",
    subject_title="fn — anonymous function", fable="tortoise-hare",
    examples=[
        _ex("((fn [x] (+ x 1)) 4)", 5,
            "the anonymous function call",
            "the result of applying an anonymous fn that adds 1 to its argument to the value 4",
            goal="create an anonymous function that adds 1 to its argument and apply it to 4"),
        _ex("((fn [a b] (* a b)) 3 4)", 12,
            "the two-argument anonymous function call",
            "the result of applying an anonymous fn with two parameters that multiplies them to 3 and 4",
            goal="create an anonymous function that multiplies its two arguments and apply it to 3 and 4"),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_08 = SubjectCurriculum(grade=3, subject_id="G3-08",
    subject_title="fn — multi-arg", fable="tortoise-hare",
    examples=[
        _ex("((fn [a b c] (+ a b c)) 1 2 3)", 6,
            "the three-argument anonymous function call",
            "the result of applying an anonymous fn with three parameters that adds them to 1, 2, and 3",
            goal="create an anonymous function with three parameters that adds them and apply it to 1, 2, and 3"),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_09 = SubjectCurriculum(grade=3, subject_id="G3-09",
    subject_title="defn — shorthand", fable="tortoise-hare",
    examples=[
        _ex("(do (defn dbl [x] (* x 2)) (dbl 5))", 10,
            "the function definition and call",
            "the result of calling the function dbl, defined via defn to multiply its argument by 2, with 5",
            goal="define a function dbl that doubles its argument, then call it with 5"),
        _ex("(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))", 6,
            "the multi-argument function definition and call",
            "the result of calling the function add3, defined via defn to add three arguments, with 1, 2, and 3",
            goal="define a function add3 that adds three arguments, then call it with 1, 2, and 3"),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_10 = SubjectCurriculum(grade=3, subject_id="G3-10",
    subject_title="anonymous shorthand #()", fable="tortoise-hare",
    examples=[
        _ex("(#(+ % 1) 5)", 6,
            "the shorthand function syntax",
            "the result of using the #() shorthand to create a function that adds 1 to its argument and applying it to 5",
            goal="use the shorthand syntax to create a function that adds 1 to its argument and apply it to 5"),
        _ex("(#(* %1 %2) 3 4)", 12,
            "the multi-argument shorthand syntax",
            "the result of using the #() shorthand to create a function that multiplies two arguments and applying it to 3 and 4",
            goal="use the shorthand syntax to create a function that multiplies two arguments and apply it to 3 and 4"),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_11 = SubjectCurriculum(grade=3, subject_id="G3-11",
    subject_title="Substitution rule", fable="tortoise-hare",
    examples=[
        _ex("(let [a 7] (+ a a))", 14,
            "the binding referenced multiple times",
            "the result of adding a to itself after binding a locally to 7 via let",
            goal="bind a to 7 and add a to itself"),
        _ex("((fn [x] (* x x)) 6)", 36,
            "the function call with self-multiplication",
            "the result of applying an anonymous fn that multiplies its argument by itself to 6",
            goal="apply a function that squares its argument to 6"),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_12 = SubjectCurriculum(grade=3, subject_id="G3-12",
    subject_title="Scope vs namespace", fable="tortoise-hare",
    examples=[
        _ex("(do (def g 5) (let [g 99] (+ g 1)))", 100,
            "the scope shadowing and computation",
            "the result of adding 1 to g, computed inside a let where g is locally bound to 99, shadowing the top-level def",
            goal="define g at the top level, shadow it in a let with a different value, and compute g+1 inside the let"),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_13 = SubjectCurriculum(grade=3, subject_id="G3-13",
    subject_title="fn body returns last form", fable="tortoise-hare",
    examples=[
        _ex("((fn [x] x x x 99) 1)", 99,
            "the function body with multiple expressions",
            "the result of applying an anonymous fn where the body contains multiple expressions but only the last one is returned, applied to 1",
            goal="create an anonymous function with multiple forms in its body but return only the last one"),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_14 = SubjectCurriculum(grade=3, subject_id="G3-14",
    subject_title="do form", fable="tortoise-hare",
    examples=[
        _ex("(do 1 2 3)", 3,
            "the do form with multiple values",
            "the final value evaluated by do from the sequence",
            goal="evaluate a sequence of values and return the last one"),
        _ex("(do (+ 1 1) (+ 2 2) (+ 3 3))", 6,
            "the do form with multiple expressions",
            "the final result evaluated by do from the sequence of expressions",
            goal="evaluate three arithmetic expressions in sequence and return the result of the last one"),
    ], subplots=_SCRIBE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_15 = SubjectCurriculum(grade=3, subject_id="G3-15",
    subject_title="Side-effects in body", fable="tortoise-hare",
    examples=[
        _ex("(do (println \"hi\") 42)", 42,
            "the do form with side-effects and final return",
            "the final value evaluated by do, ignoring the intermediate println side-effect",
            goal="execute a print statement for side-effects, then return a different value"),
    ], subplots=_RECIPE_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_16 = SubjectCurriculum(grade=3, subject_id="G3-16",
    subject_title="Name collision: namespace vs let", fable="tortoise-hare",
    examples=[
        _ex("(let [+ 99] +)", 99,
            "the shadowed operator binding",
            "the value locally bound to the + operator via let",
            goal="shadow the plus operator with a local binding and return the bound value"),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_17 = SubjectCurriculum(grade=3, subject_id="G3-17",
    subject_title="Naming conventions (kebab-case)", fable="tortoise-hare",
    examples=[
        _ex("(let [hare-speed 4 tortoise-speed 1] (- hare-speed tortoise-speed))", 3,
            "the kebab-case naming and subtraction",
            "the result of subtracting tortoise-speed from hare-speed after binding both via let",
            goal="bind hare-speed to 4 and tortoise-speed to 1, then compute their difference"),
    ], subplots=_ROADSIGN_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_18 = SubjectCurriculum(grade=3, subject_id="G3-18",
    subject_title="When to name vs inline", fable="tortoise-hare",
    examples=[
        _ex("(let [n 5] (* n n n))", 125,
            "the named binding used multiple times",
            "the result of multiplying n by itself three times after binding n locally to 5 via let",
            goal="bind n to 5 and compute n cubed"),
        _ex("(* 5 5 5)", 125,
            "the inline multiplication without binding",
            "the result of multiplying 5 by itself three times without any binding",
            goal="compute 5 cubed using direct values"),
    ], subplots=_POUCH_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


SUBJECTS: dict[str, SubjectCurriculum] = {
    s.subject_id: s for s in (
        G3_01, G3_02, G3_03, G3_04, G3_05, G3_06, G3_07, G3_08, G3_09,
        G3_10, G3_11, G3_12, G3_13, G3_14, G3_15, G3_16, G3_17, G3_18,
    )
}


def smoke_test() -> None:
    from mmllm.aesop.curriculum.generator import generate_subject
    for sid, sub in SUBJECTS.items():
        recs = generate_subject(sub, n_per_example=1, seed=0)
        for r in recs: assert r.tool_calls[0]["name"] == "eval"
    print(f"grade-3 tortoise-hare smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
