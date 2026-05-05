"""Grade 3 — naming, scope, substitution. Through ant-grasshopper.

The fable lens: the Ant's careful approach is exactly the
substitution-rule discipline. The Grasshopper's "I just know the answer"
is what binding-by-name corrects.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.ant_grasshopper.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)

# Add naming-themed subplots: an Ant labels each entry in the
# stockpile-ledger, then references the binding by name.
_NAMING_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [
    SubplotTemplate("""\
{ant_phrase} kept a small stockpile-ledger {place} where every meaningful
quantity got its own name. {ant_he_she_cap} pointed to today's
entry: {concept_phrase}. The form {form_display} would settle it once
{grasshopper_phrase} agreed to look at the binding."""),

    SubplotTemplate("""\
"You can call it whatever you like," {ant} said {place}, "but the
form is what matters." {ant_he_she_cap} drew the binding for
{grasshopper_phrase}: the form {form_display} captured {concept_phrase}, and
the REPL would do the rest."""),
]


def _ex(form, expected, concept, what, tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          tags=tags)


_PLAN_POOL_G3 = _PLAN_POOL + (
    "I bind the inputs in a let, then compute.",
    "I name the values first and then combine them.",
    "I write the let-form so the REPL can substitute.",
)


G3_01 = SubjectCurriculum(grade=3, subject_id="G3-01",
    subject_title="def — top-level binding", fable="ant-grasshopper",
    examples=[
        _ex("(do (def x 42) x)", 42, "the binding (def x 42) followed by x",
            "the value bound to x after (def x 42)"),
        _ex("(do (def y 7) y)",  7,  "the binding (def y 7)",
            "the value bound to y"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_02 = SubjectCurriculum(grade=3, subject_id="G3-02",
    subject_title="def — redefinition", fable="ant-grasshopper",
    examples=[
        _ex("(do (def x 1) (def x 99) x)", 99,
            "the redefined x", "the value of x after redefinition"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_03 = SubjectCurriculum(grade=3, subject_id="G3-03",
    subject_title="let — local binding", fable="ant-grasshopper",
    examples=[
        _ex("(let [x 3] (+ x 1))", 4, "the form (let [x 3] (+ x 1))",
            "the result of (let [x 3] (+ x 1))"),
        _ex("(let [n 10] (* n n))", 100, "the form (let [n 10] (* n n))",
            "the square of n where n is bound to 10"),
        _ex("(let [a 5] a)", 5, "the form (let [a 5] a)",
            "the value of (let [a 5] a)"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_04 = SubjectCurriculum(grade=3, subject_id="G3-04",
    subject_title="let — multi-binding", fable="ant-grasshopper",
    examples=[
        _ex("(let [a 1 b 2] (+ a b))", 3,
            "the form with two bindings",
            "the result of (let [a 1 b 2] (+ a b))"),
        _ex("(let [x 5 y 3] (- x y))", 2,
            "the form (let [x 5 y 3] (- x y))",
            "the result of (- x y) when x=5, y=3"),
        _ex("(let [a 2 b 3 c 4] (+ a b c))", 9,
            "a let with three bindings",
            "the sum of a, b, c when a=2, b=3, c=4"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_05 = SubjectCurriculum(grade=3, subject_id="G3-05",
    subject_title="let — shadowing outer def", fable="ant-grasshopper",
    examples=[
        _ex("(do (def x 10) (let [x 99] x))", 99,
            "an inner let shadowing the outer def",
            "the inner-let value of x"),
        _ex("(do (def x 10) (let [x 99] x) x)", 10,
            "the outer x after the inner let returns",
            "the outer x after the let scope ends"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_06 = SubjectCurriculum(grade=3, subject_id="G3-06",
    subject_title="let — binding can reference prior", fable="ant-grasshopper",
    examples=[
        _ex("(let [a 5 b (* a 2)] b)", 10,
            "a let where b uses a",
            "the value of b when a=5 and b is (* a 2)"),
        _ex("(let [a 3 b (+ a 1) c (* b 2)] c)", 8,
            "a let with sequential bindings",
            "the result of the chained binding c"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_07 = SubjectCurriculum(grade=3, subject_id="G3-07",
    subject_title="fn — anonymous function", fable="ant-grasshopper",
    examples=[
        _ex("((fn [x] (+ x 1)) 4)", 5,
            "an anonymous function applied to 4",
            "the result of applying (fn [x] (+ x 1)) to 4"),
        _ex("((fn [a b] (* a b)) 3 4)", 12,
            "a two-arg anonymous function",
            "the result of applying (fn [a b] (* a b)) to 3 and 4"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_08 = SubjectCurriculum(grade=3, subject_id="G3-08",
    subject_title="fn — multi-arg", fable="ant-grasshopper",
    examples=[
        _ex("((fn [a b c] (+ a b c)) 1 2 3)", 6,
            "a three-arg anonymous function",
            "the sum of a, b, c"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_09 = SubjectCurriculum(grade=3, subject_id="G3-09",
    subject_title="defn — shorthand", fable="ant-grasshopper",
    examples=[
        _ex("(do (defn dbl [x] (* x 2)) (dbl 5))", 10,
            "a defn that doubles its argument",
            "the doubled value (dbl 5)"),
        _ex("(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))", 6,
            "a defn with three args",
            "the result of (add3 1 2 3)"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_10 = SubjectCurriculum(grade=3, subject_id="G3-10",
    subject_title="anonymous shorthand #()", fable="ant-grasshopper",
    examples=[
        _ex("(#(+ % 1) 5)", 6,
            "the shorthand #(+ % 1) applied to 5",
            "the result of (#(+ % 1) 5)"),
        _ex("(#(* %1 %2) 3 4)", 12,
            "the shorthand #(* %1 %2) applied to 3 and 4",
            "the result of (#(* %1 %2) 3 4)"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_11 = SubjectCurriculum(grade=3, subject_id="G3-11",
    subject_title="Substitution rule", fable="ant-grasshopper",
    examples=[
        _ex("(let [a 7] (+ a a))", 14,
            "the let where a is referenced twice",
            "the result of (+ a a) when a=7"),
        _ex("((fn [x] (* x x)) 6)", 36,
            "applying square to 6",
            "the square of 6"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_12 = SubjectCurriculum(grade=3, subject_id="G3-12",
    subject_title="Scope vs namespace", fable="ant-grasshopper",
    examples=[
        _ex("(do (def g 5) (let [g 99] (+ g 1)))", 100,
            "the let-shadowed form (do (def g 5) (let [g 99] (+ g 1)))",
            "the value computed inside the inner scope"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_13 = SubjectCurriculum(grade=3, subject_id="G3-13",
    subject_title="fn body returns last form", fable="ant-grasshopper",
    examples=[
        _ex("((fn [x] x x x 99) 1)", 99,
            "the multi-form fn body",
            "the value of a fn body that ends with 99"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_14 = SubjectCurriculum(grade=3, subject_id="G3-14",
    subject_title="do form", fable="ant-grasshopper",
    examples=[
        _ex("(do 1 2 3)", 3,
            "the do form (do 1 2 3)",
            "the value of (do 1 2 3)"),
        _ex("(do (+ 1 1) (+ 2 2) (+ 3 3))", 6,
            "a do with three forms",
            "the value of (do (+ 1 1) (+ 2 2) (+ 3 3))"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_15 = SubjectCurriculum(grade=3, subject_id="G3-15",
    subject_title="Side-effects in body", fable="ant-grasshopper",
    examples=[
        _ex("(do (println \"hi\") 42)", 42,
            "the form (do (println \"hi\") 42)",
            "the return value of the do (the println side-effects, but the do returns 42)"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_16 = SubjectCurriculum(grade=3, subject_id="G3-16",
    subject_title="Name collision: namespace vs let", fable="ant-grasshopper",
    examples=[
        _ex("(let [+ 99] +)", 99,
            "the let-shadowed form (let [+ 99] +)",
            "the value bound to the (locally shadowed) +"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_17 = SubjectCurriculum(grade=3, subject_id="G3-17",
    subject_title="Naming conventions (kebab-case)", fable="ant-grasshopper",
    examples=[
        _ex("(let [grasshopper-pace 4 ant-pace 1] (- grasshopper-pace ant-pace))", 3,
            "a let with kebab-case names",
            "the difference of the two paces"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_18 = SubjectCurriculum(grade=3, subject_id="G3-18",
    subject_title="When to name vs inline", fable="ant-grasshopper",
    examples=[
        _ex("(let [n 5] (* n n n))", 125,
            "naming n once and using it three times",
            "n cubed where n=5"),
        _ex("(* 5 5 5)", 125,
            "the inline form (* 5 5 5)",
            "5 cubed (without binding)"),
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
    print(f"grade-3 ant-grasshopper smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
