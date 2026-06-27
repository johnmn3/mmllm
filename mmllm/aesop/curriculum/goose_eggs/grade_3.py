"""Grade 3 — naming, scope, substitution. Through the goose-eggs fable.

The fable lens: the patient {owner} keeps a careful ledger of named
quantities — every binding gets a name, just as every egg from
{goose} gets a tally mark. The greedy {visitor} wants to skip the
naming and shout the answer; {owner} insists on writing the let-form
and letting the REPL substitute, the way one egg per morning is
counted, never guessed.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.goose_eggs.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)

# Add naming-themed subplots: the goose-eggs ledger metaphor maps
# directly onto bindings — every meaningful quantity gets its own
# name, the way every egg gets its own tally mark.
_NAMING_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    # Ledger of named quantities — bindings as tally entries.
    SubplotTemplate("""\
{owner_phrase} kept a small leather ledger {place} where every
quantity that mattered got its own name, the same way each egg from
{goose_phrase} got its own tally mark in the column beside it.
{owner_he_she_cap} pointed to today's entry: {concept_phrase}. The
form {form_display} would settle it once {visitor_phrase} agreed to
look at the binding rather than guess at the answer."""),

    # Naming over the kitchen table — coins counted, names assigned.
    SubplotTemplate("""\
"You can call it whatever you like," {owner_phrase} said {place},
"but the form is what the REPL reads." {owner_he_she_cap} drew the
binding for {visitor_phrase}: the form {form_display} captured
{concept_phrase}, and the runtime would do the substitution itself —
one named value at a time, the way {goose} laid one egg each
morning."""),

    # Market trip — names on the basket, the patient way to total up.
    SubplotTemplate("""\
On the way back from the market {place}, {owner_phrase} unpacked the
basket and labeled each parcel before adding anything up. "Name first,
total after," {owner_he_she} told {visitor_phrase}, {emo_patient}.
The form {form_display} captured {concept_phrase} the same way: every
binding got its name before the REPL was asked for the answer."""),
]


def _ex(form, expected, concept, what, tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          tags=tags)


_PLAN_POOL_G3 = _PLAN_POOL + (
    "I bind the inputs in a let, then compute.",
    "I name the values first and then combine them.",
    "I write the let-form so the REPL can substitute.",
    "I tally each binding by name, the way eggs get tallied one by one.",
)


G3_01 = SubjectCurriculum(grade=3, subject_id="G3-01",
    subject_title="def — top-level binding", fable="goose-eggs",
    examples=[
        _ex("(do (def x 42) x)", 42, "the binding (def x 42) followed by x",
            "the value bound to x after (def x 42)"),
        _ex("(do (def y 7) y)",  7,  "the binding (def y 7)",
            "the value bound to y"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_02 = SubjectCurriculum(grade=3, subject_id="G3-02",
    subject_title="def — redefinition", fable="goose-eggs",
    examples=[
        _ex("(do (def x 1) (def x 99) x)", 99,
            "the redefined x", "the value of x after redefinition"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_03 = SubjectCurriculum(grade=3, subject_id="G3-03",
    subject_title="let — local binding", fable="goose-eggs",
    examples=[
        _ex("(let [x 3] (+ x 1))", 4, "the form (let [x 3] (+ x 1))",
            "the result of (let [x 3] (+ x 1))"),
        _ex("(let [n 10] (* n n))", 100, "the form (let [n 10] (* n n))",
            "the square of n where n is bound to 10"),
        _ex("(let [a 5] a)", 5, "the form (let [a 5] a)",
            "the value of (let [a 5] a)"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_04 = SubjectCurriculum(grade=3, subject_id="G3-04",
    subject_title="let — multi-binding", fable="goose-eggs",
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
    subject_title="let — shadowing outer def", fable="goose-eggs",
    examples=[
        _ex("(do (def x 10) (let [x 99] x))", 99,
            "an inner let shadowing the outer def",
            "the inner-let value of x"),
        _ex("(do (def x 10) (let [x 99] x) x)", 10,
            "the outer x after the inner let returns",
            "the outer x after the let scope ends"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_06 = SubjectCurriculum(grade=3, subject_id="G3-06",
    subject_title="let — binding can reference prior", fable="goose-eggs",
    examples=[
        _ex("(let [a 5 b (* a 2)] b)", 10,
            "a let where b uses a",
            "the value of b when a=5 and b is (* a 2)"),
        _ex("(let [a 3 b (+ a 1) c (* b 2)] c)", 8,
            "a let with sequential bindings",
            "the result of the chained binding c"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_07 = SubjectCurriculum(grade=3, subject_id="G3-07",
    subject_title="fn — anonymous function", fable="goose-eggs",
    examples=[
        _ex("((fn [x] (+ x 1)) 4)", 5,
            "an anonymous function applied to 4",
            "the result of applying (fn [x] (+ x 1)) to 4"),
        _ex("((fn [a b] (* a b)) 3 4)", 12,
            "a two-arg anonymous function",
            "the result of applying (fn [a b] (* a b)) to 3 and 4"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_08 = SubjectCurriculum(grade=3, subject_id="G3-08",
    subject_title="fn — multi-arg", fable="goose-eggs",
    examples=[
        _ex("((fn [a b c] (+ a b c)) 1 2 3)", 6,
            "a three-arg anonymous function",
            "the sum of a, b, c"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_09 = SubjectCurriculum(grade=3, subject_id="G3-09",
    subject_title="defn — shorthand", fable="goose-eggs",
    examples=[
        _ex("(do (defn dbl [x] (* x 2)) (dbl 5))", 10,
            "a defn that doubles its argument",
            "the doubled value (dbl 5)"),
        _ex("(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))", 6,
            "a defn with three args",
            "the result of (add3 1 2 3)"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_10 = SubjectCurriculum(grade=3, subject_id="G3-10",
    subject_title="anonymous shorthand #()", fable="goose-eggs",
    examples=[
        _ex("(#(+ % 1) 5)", 6,
            "the shorthand #(+ % 1) applied to 5",
            "the result of (#(+ % 1) 5)"),
        _ex("(#(* %1 %2) 3 4)", 12,
            "the shorthand #(* %1 %2) applied to 3 and 4",
            "the result of (#(* %1 %2) 3 4)"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_11 = SubjectCurriculum(grade=3, subject_id="G3-11",
    subject_title="Substitution rule", fable="goose-eggs",
    examples=[
        _ex("(let [a 7] (+ a a))", 14,
            "the let where a is referenced twice",
            "the result of (+ a a) when a=7"),
        _ex("((fn [x] (* x x)) 6)", 36,
            "applying square to 6",
            "the square of 6"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_12 = SubjectCurriculum(grade=3, subject_id="G3-12",
    subject_title="Scope vs namespace", fable="goose-eggs",
    examples=[
        _ex("(do (def g 5) (let [g 99] (+ g 1)))", 100,
            "an inner let masking the outer def g",
            "the value computed inside the inner scope"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_13 = SubjectCurriculum(grade=3, subject_id="G3-13",
    subject_title="fn body returns last form", fable="goose-eggs",
    examples=[
        _ex("((fn [x] x x x 99) 1)", 99,
            "a fn whose body has multiple forms; only the last is returned",
            "the value of a fn body that ends with 99"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_14 = SubjectCurriculum(grade=3, subject_id="G3-14",
    subject_title="do form", fable="goose-eggs",
    examples=[
        _ex("(do 1 2 3)", 3,
            "the do form (do 1 2 3)",
            "the value of (do 1 2 3)"),
        _ex("(do (+ 1 1) (+ 2 2) (+ 3 3))", 6,
            "a do with three forms",
            "the value of (do (+ 1 1) (+ 2 2) (+ 3 3))"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_15 = SubjectCurriculum(grade=3, subject_id="G3-15",
    subject_title="Side-effects in body", fable="goose-eggs",
    examples=[
        _ex("(do (println \"hi\") 42)", 42,
            "the form (do (println \"hi\") 42)",
            "the return value of the do (the println side-effects, but the do returns 42)"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_16 = SubjectCurriculum(grade=3, subject_id="G3-16",
    subject_title="Name collision: namespace vs let", fable="goose-eggs",
    examples=[
        _ex("(let [+ 99] +)", 99,
            "a let that shadows the + function",
            "the value bound to the (locally shadowed) +"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_17 = SubjectCurriculum(grade=3, subject_id="G3-17",
    subject_title="Naming conventions (kebab-case)", fable="goose-eggs",
    examples=[
        _ex("(let [hare-speed 4 tortoise-speed 1] (- hare-speed tortoise-speed))", 3,
            "a let with kebab-case names",
            "the difference of the two speeds"),
    ], subplots=_NAMING_SUBPLOTS, plan_pool=_PLAN_POOL_G3)


G3_18 = SubjectCurriculum(grade=3, subject_id="G3-18",
    subject_title="When to name vs inline", fable="goose-eggs",
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
    print(f"grade-3 goose-eggs smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
