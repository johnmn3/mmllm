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
            "the value bound to x",
            goal="bind x to 42 and return it"),
        _ex("(do (def y 7) y)",  7,  "the top-level binding",
            "the value bound to y",
            goal="bind y to 7 and return it"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_02 = SubjectCurriculum(grade=3, subject_id="G3-02",
    subject_title="def — redefinition", fable="tortoise-hare",
    examples=[
        _ex("(do (def x 1) (def x 99) x)", 99,
            "the redefined binding",
            "the final value of x after two def calls",
            goal="bind x to 1, then redefine it as 99 and return it"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_03 = SubjectCurriculum(grade=3, subject_id="G3-03",
    subject_title="let — local binding", fable="tortoise-hare",
    examples=[
        _ex("(let [x 3] (+ x 1))", 4, "the local binding and addition",
            "the result of adding 1 to the bound x",
            goal="bind x to 3 and add 1 to it"),
        _ex("(let [n 10] (* n n))", 100, "the local binding and multiplication",
            "the result of multiplying the bound n by itself",
            goal="bind n to 10 and compute n squared"),
        _ex("(let [a 5] a)", 5, "the local binding and lookup",
            "the value of the bound variable",
            goal="bind a to 5 and return it"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_04 = SubjectCurriculum(grade=3, subject_id="G3-04",
    subject_title="let — multi-binding", fable="tortoise-hare",
    examples=[
        _ex("(let [a 1 b 2] (+ a b))", 3,
            "the multi-binding and addition",
            "the result of adding the two bound variables",
            goal="bind a to 1 and b to 2, then add them"),
        _ex("(let [x 5 y 3] (- x y))", 2,
            "the multi-binding and subtraction",
            "the result of subtracting the second from the first",
            goal="bind x to 5 and y to 3, then subtract y from x"),
        _ex("(let [a 2 b 3 c 4] (+ a b c))", 9,
            "the three-binding sum",
            "the sum of the three bound variables",
            goal="bind a to 2, b to 3, c to 4, and add them"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_05 = SubjectCurriculum(grade=3, subject_id="G3-05",
    subject_title="let — shadowing outer def", fable="tortoise-hare",
    examples=[
        _ex("(do (def x 10) (let [x 99] x))", 99,
            "the inner binding shadowing the outer",
            "the value inside the let scope",
            goal="define x at the top level, then shadow it locally and return the inner value"),
        _ex("(do (def x 10) (let [x 99] x) x)", 10,
            "the outer binding after the let scope",
            "the original value after the let returns",
            goal="define x, shadow it in a let, then look up x again in the outer scope"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_06 = SubjectCurriculum(grade=3, subject_id="G3-06",
    subject_title="let — binding can reference prior", fable="tortoise-hare",
    examples=[
        _ex("(let [a 5 b (* a 2)] b)", 10,
            "the sequential binding where later refers to earlier",
            "the value of the second binding which uses the first",
            goal="bind a to 5, then bind b to twice a, and return b"),
        _ex("(let [a 3 b (+ a 1) c (* b 2)] c)", 8,
            "the chained bindings with sequential references",
            "the result of the final binding that depends on the prior two",
            goal="bind a to 3, b to a+1, c to 2*b, and return c"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_07 = SubjectCurriculum(grade=3, subject_id="G3-07",
    subject_title="fn — anonymous function", fable="tortoise-hare",
    examples=[
        _ex("((fn [x] (+ x 1)) 4)", 5,
            "the anonymous function call",
            "the result of applying the function to 4",
            goal="create an anonymous function that adds 1 to its argument and apply it to 4"),
        _ex("((fn [a b] (* a b)) 3 4)", 12,
            "the two-argument anonymous function call",
            "the result of applying the function to 3 and 4",
            goal="create an anonymous function that multiplies its two arguments and apply it to 3 and 4"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_08 = SubjectCurriculum(grade=3, subject_id="G3-08",
    subject_title="fn — multi-arg", fable="tortoise-hare",
    examples=[
        _ex("((fn [a b c] (+ a b c)) 1 2 3)", 6,
            "the three-argument anonymous function call",
            "the sum of the three arguments",
            goal="create an anonymous function with three parameters that adds them and apply it to 1, 2, and 3"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_09 = SubjectCurriculum(grade=3, subject_id="G3-09",
    subject_title="defn — shorthand", fable="tortoise-hare",
    examples=[
        _ex("(do (defn dbl [x] (* x 2)) (dbl 5))", 10,
            "the function definition and call",
            "the result of doubling 5",
            goal="define a function dbl that doubles its argument, then call it with 5"),
        _ex("(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))", 6,
            "the multi-argument function definition and call",
            "the sum of the three arguments",
            goal="define a function add3 that adds three arguments, then call it with 1, 2, and 3"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_10 = SubjectCurriculum(grade=3, subject_id="G3-10",
    subject_title="anonymous shorthand #()", fable="tortoise-hare",
    examples=[
        _ex("(#(+ % 1) 5)", 6,
            "the shorthand function syntax",
            "the result of the shorthand applied to 5",
            goal="use the shorthand syntax to create a function that adds 1 to its argument and apply it to 5"),
        _ex("(#(* %1 %2) 3 4)", 12,
            "the multi-argument shorthand syntax",
            "the result of the shorthand applied to two arguments",
            goal="use the shorthand syntax to create a function that multiplies two arguments and apply it to 3 and 4"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_11 = SubjectCurriculum(grade=3, subject_id="G3-11",
    subject_title="Substitution rule", fable="tortoise-hare",
    examples=[
        _ex("(let [a 7] (+ a a))", 14,
            "the binding referenced multiple times",
            "the result of adding a to itself",
            goal="bind a to 7 and add a to itself"),
        _ex("((fn [x] (* x x)) 6)", 36,
            "the function call with self-multiplication",
            "the result of multiplying the argument by itself",
            goal="apply a function that squares its argument to 6"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_12 = SubjectCurriculum(grade=3, subject_id="G3-12",
    subject_title="Scope vs namespace", fable="tortoise-hare",
    examples=[
        _ex("(do (def g 5) (let [g 99] (+ g 1)))", 100,
            "the scope shadowing and computation",
            "the result computed inside the let where g is locally 99",
            goal="define g at the top level, shadow it in a let with a different value, and compute g+1 inside the let"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_13 = SubjectCurriculum(grade=3, subject_id="G3-13",
    subject_title="fn body returns last form", fable="tortoise-hare",
    examples=[
        _ex("((fn [x] x x x 99) 1)", 99,
            "the function body with multiple expressions",
            "the final value returned by the function",
            goal="create an anonymous function with multiple forms in its body but return only the last one"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_14 = SubjectCurriculum(grade=3, subject_id="G3-14",
    subject_title="do form", fable="tortoise-hare",
    examples=[
        _ex("(do 1 2 3)", 3,
            "the do form with multiple values",
            "the final value from the sequence",
            goal="evaluate a sequence of values and return the last one"),
        _ex("(do (+ 1 1) (+ 2 2) (+ 3 3))", 6,
            "the do form with multiple expressions",
            "the result of the final expression",
            goal="evaluate three arithmetic expressions in sequence and return the result of the last one"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_15 = SubjectCurriculum(grade=3, subject_id="G3-15",
    subject_title="Side-effects in body", fable="tortoise-hare",
    examples=[
        _ex("(do (println \"hi\") 42)", 42,
            "the do form with side-effects and final return",
            "the value returned after the side-effects",
            goal="execute a print statement for side-effects, then return a different value"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_16 = SubjectCurriculum(grade=3, subject_id="G3-16",
    subject_title="Name collision: namespace vs let", fable="tortoise-hare",
    examples=[
        _ex("(let [+ 99] +)", 99,
            "the shadowed operator binding",
            "the locally bound value of the operator",
            goal="shadow the plus operator with a local binding and return the bound value"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_17 = SubjectCurriculum(grade=3, subject_id="G3-17",
    subject_title="Naming conventions (kebab-case)", fable="tortoise-hare",
    examples=[
        _ex("(let [hare-speed 4 tortoise-speed 1] (- hare-speed tortoise-speed))", 3,
            "the kebab-case naming and subtraction",
            "the difference between the two bound values",
            goal="bind hare-speed to 4 and tortoise-speed to 1, then compute their difference"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_18 = SubjectCurriculum(grade=3, subject_id="G3-18",
    subject_title="When to name vs inline", fable="tortoise-hare",
    examples=[
        _ex("(let [n 5] (* n n n))", 125,
            "the named binding used multiple times",
            "the cube of the bound value",
            goal="bind n to 5 and compute n cubed"),
        _ex("(* 5 5 5)", 125,
            "the inline multiplication without binding",
            "the cube of 5 without naming",
            goal="compute 5 cubed using direct values"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


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
