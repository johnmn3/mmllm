"""Grade 4 — collections (Layer 4). Through ant-grasshopper.

Subplot lens: collections of grains, acorns, seeds, kernels, breadcrumbs
that the Ant counts, sorts, and stockpiles for the coming winter.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.ant_grasshopper.grade_1 import _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL


_COLL_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [
    # NOTE: these two templates avoid putting both {form_display} AND a
    # "the form X" {concept_phrase} in close proximity (the duplication
    # produces ungrammatical "the form X described the form X" prose
    # when concept_phrase is "the form X" verbatim — see SKILL doc #11).
    SubplotTemplate("""\
{ant_phrase} had been laying out a small collection {place} —
grains, acorns, seeds, whatever the day's foraging produced. {ant}
wrote {form_display} on a slate and asked {grasshopper_phrase} to write
the form into the REPL so they could confirm it together."""),

    SubplotTemplate("""\
{grasshopper_phrase}, {emo_proud}, declared the collection plain. {ant_phrase}
wrote {form_display} on a slate {place}, calmly. "It's not about plain
or fancy," {ant_he_she} said. "It's about whether the runtime
agrees with what we think we're describing.\""""),
]


def _ex(form, expected, concept, what):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what)


_PLAN_G4 = _PLAN_POOL + (
    "I write the collection literal and let the REPL evaluate.",
    "I use the appropriate access function on the collection.",
)


G4_01 = SubjectCurriculum(grade=4, subject_id="G4-01",
    subject_title="Vector literal", fable="ant-grasshopper",
    examples=[
        _ex("[1 2 3]", [1,2,3],   "the vector [1 2 3]",   "the value [1 2 3]"),
        _ex("[]",      [],         "the empty vector []",  "the empty vector"),
        _ex("[\"a\" \"b\"]", ["a","b"], "the vector of strings", "the vector [\"a\" \"b\"]"),
    ], subplots=_COLL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_02 = SubjectCurriculum(grade=4, subject_id="G4-02",
    subject_title="nth — vector access", fable="ant-grasshopper",
    examples=[
        _ex("(nth [10 20 30] 0)", 10, "the form (nth [10 20 30] 0)", "the value at index 0"),
        _ex("(nth [10 20 30] 2)", 30, "the form (nth [10 20 30] 2)", "the value at index 2"),
    ], subplots=_COLL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_03 = SubjectCurriculum(grade=4, subject_id="G4-03",
    subject_title="conj — append to vector", fable="ant-grasshopper",
    examples=[
        _ex("(conj [1 2] 3)",       [1,2,3],   "the form (conj [1 2] 3)",      "[1 2] with 3 conjed"),
        _ex("(conj [] :ant)",       [":ant"],  "the form (conj [] :ant)",      "the empty vector with :ant conjed"),
    ], subplots=_COLL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_04 = SubjectCurriculum(grade=4, subject_id="G4-04",
    subject_title="List literal", fable="ant-grasshopper",
    examples=[
        _ex("'(1 2 3)", [1,2,3], "the list '(1 2 3)", "the list of three numbers"),
        _ex("'()",      [],       "the empty list",     "the empty list"),
    ], subplots=_COLL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_05 = SubjectCurriculum(grade=4, subject_id="G4-05",
    subject_title="cons — prepend to seq", fable="ant-grasshopper",
    examples=[
        _ex("(cons 0 '(1 2 3))", [0,1,2,3], "the form (cons 0 '(1 2 3))", "the seq with 0 cons'd at the front"),
    ], subplots=_COLL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_06 = SubjectCurriculum(grade=4, subject_id="G4-06",
    subject_title="Map literal", fable="ant-grasshopper",
    examples=[
        _ex("{:ant 1 :grasshopper 2}", {":ant": 1, ":grasshopper": 2},
            "the map {:ant 1 :grasshopper 2}", "the map with two entries"),
    ], subplots=_COLL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_07 = SubjectCurriculum(grade=4, subject_id="G4-07",
    subject_title="get — map lookup", fable="ant-grasshopper",
    examples=[
        _ex("(get {:a 1 :b 2} :a)", 1, "the form (get {:a 1 :b 2} :a)", "the value at :a"),
        _ex("(get {:a 1} :missing :default)", ":default",
            "the form (get {:a 1} :missing :default)", "the default value when key missing"),
    ], subplots=_COLL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_08 = SubjectCurriculum(grade=4, subject_id="G4-08",
    subject_title="assoc — map update", fable="ant-grasshopper",
    examples=[
        _ex("(assoc {:a 1} :b 2)", {":a": 1, ":b": 2},
            "the form (assoc {:a 1} :b 2)", "the map after assoc'ing :b 2"),
        _ex("(assoc {:a 1} :a 99)", {":a": 99},
            "the form (assoc {:a 1} :a 99)", "the map after updating :a to 99"),
    ], subplots=_COLL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_09 = SubjectCurriculum(grade=4, subject_id="G4-09",
    subject_title="dissoc — map remove key", fable="ant-grasshopper",
    examples=[
        _ex("(dissoc {:a 1 :b 2} :a)", {":b": 2},
            "the form (dissoc {:a 1 :b 2} :a)", "the map without :a"),
    ], subplots=_COLL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_10 = SubjectCurriculum(grade=4, subject_id="G4-10",
    subject_title="keys and vals", fable="ant-grasshopper",
    examples=[
        _ex("(count (keys {:a 1 :b 2 :c 3}))", 3,
            "the count of map keys", "the number of keys in the map"),
    ], subplots=_COLL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_11 = SubjectCurriculum(grade=4, subject_id="G4-11",
    subject_title="Set literal", fable="ant-grasshopper",
    examples=[
        _ex("(count #{1 2 3})", 3, "the count of #{1 2 3}", "the size of the set"),
        _ex("(count #{1 1 1})", 1, "the count of the deduped set #{1 1 1}", "the size of the set"),
    ], subplots=_COLL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_12 = SubjectCurriculum(grade=4, subject_id="G4-12",
    subject_title="Set membership", fable="ant-grasshopper",
    examples=[
        _ex("(contains? #{1 2 3} 2)", True, "the form (contains? #{1 2 3} 2)", "whether 2 is in the set"),
        _ex("(contains? #{1 2 3} 4)", False, "the form (contains? #{1 2 3} 4)", "whether 4 is in the set"),
    ], subplots=_COLL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_13 = SubjectCurriculum(grade=4, subject_id="G4-13",
    subject_title="count — universal", fable="ant-grasshopper",
    examples=[
        _ex("(count [1 2 3 4 5])", 5, "the count of a 5-element vector", "the count"),
        _ex("(count {:a 1 :b 2})", 2, "the count of a 2-key map", "the count"),
        _ex("(count #{:a :b :c})", 3, "the count of a 3-element set", "the count"),
        _ex("(count \"grasshopper\")", 11, "the count of \"grasshopper\"", "the string length"),
    ], subplots=_COLL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_14 = SubjectCurriculum(grade=4, subject_id="G4-14",
    subject_title="empty?", fable="ant-grasshopper",
    examples=[
        _ex("(empty? [])",   True,  "the form (empty? [])",   "whether [] is empty"),
        _ex("(empty? [1])",  False, "the form (empty? [1])",  "whether [1] is empty"),
        _ex("(empty? \"\")", True,  "the form (empty? \"\")", "whether the empty string is empty"),
    ], subplots=_COLL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_15 = SubjectCurriculum(grade=4, subject_id="G4-15",
    subject_title="first, rest, last", fable="ant-grasshopper",
    examples=[
        _ex("(first [10 20 30])", 10, "the first of the vector", "the first element"),
        _ex("(last  [10 20 30])", 30, "the last of the vector",  "the last element"),
        _ex("(count (rest [10 20 30]))", 2, "the count of the rest of [10 20 30]", "the count after removing first"),
    ], subplots=_COLL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_16 = SubjectCurriculum(grade=4, subject_id="G4-16",
    subject_title="into and conj on collections", fable="ant-grasshopper",
    examples=[
        _ex("(into [] '(1 2 3))", [1,2,3],
            "the form (into [] '(1 2 3))", "the vector built from a list"),
        _ex("(into #{} [1 2 2 3])", [1,2,3],
            "the form (into #{} [1 2 2 3])", "the set built from a vector (dups removed)"),
    ], subplots=_COLL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_17 = SubjectCurriculum(grade=4, subject_id="G4-17",
    subject_title="Immutability — assoc returns new", fable="ant-grasshopper",
    examples=[
        _ex("(let [m {:a 1}] (assoc m :a 99) m)", {":a": 1},
            "the form (let [m {:a 1}] (assoc m :a 99) m)", "the original map after assoc"),
    ], subplots=_COLL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_18 = SubjectCurriculum(grade=4, subject_id="G4-18",
    subject_title="Equality of vectors and lists", fable="ant-grasshopper",
    examples=[
        _ex("(= [1 2 3] '(1 2 3))", True,
            "the form (= [1 2 3] '(1 2 3))", "whether vector and list with same elements are equal"),
    ], subplots=_COLL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_19 = SubjectCurriculum(grade=4, subject_id="G4-19",
    subject_title="range and seq", fable="ant-grasshopper",
    examples=[
        _ex("(count (range 5))", 5, "the count of (range 5)", "the count of range 0..4"),
        _ex("(first (range 1 100))", 1, "the first of (range 1 100)", "the first of range 1..99"),
    ], subplots=_COLL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_20 = SubjectCurriculum(grade=4, subject_id="G4-20",
    subject_title="Collection vs sequence", fable="ant-grasshopper",
    examples=[
        _ex("(count (seq [1 2 3]))", 3,
            "the form (count (seq [1 2 3]))", "the count of seq over a vector"),
        _ex("(seq [])", None,
            "the form (seq [])", "what (seq []) returns"),
    ], subplots=_COLL_SUBPLOTS, plan_pool=_PLAN_G4)


SUBJECTS = {s.subject_id: s for s in (
    G4_01, G4_02, G4_03, G4_04, G4_05, G4_06, G4_07, G4_08, G4_09, G4_10,
    G4_11, G4_12, G4_13, G4_14, G4_15, G4_16, G4_17, G4_18, G4_19, G4_20,
)}


def smoke_test() -> None:
    from mmllm.aesop.curriculum.generator import generate_subject
    for sid, sub in SUBJECTS.items():
        recs = generate_subject(sub, n_per_example=1, seed=0)
        for r in recs: assert r.tool_calls[0]["name"] == "eval"
    print(f"grade-4 ant-grasshopper smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
