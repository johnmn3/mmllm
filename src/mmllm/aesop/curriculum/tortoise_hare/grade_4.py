"""Grade 4 — collections (Layer 4). Through tortoise-hare.

Subplot lens: collections of pebbles, milestones, racers, paw-prints,
plums, etc., that the characters count, sort, and manipulate.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.tortoise_hare.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL
)


_COLL_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [
    # NOTE: these two templates avoid putting both {form_display} AND a
    # "the form X" {concept_phrase} in close proximity (the duplication
    # produces ungrammatical "the form X described the form X" prose
    # when concept_phrase is "the form X" verbatim — see SKILL doc #11).
    SubplotTemplate("""\
{tortoise_phrase} had been laying out a small collection {place} —
pebbles, milestones, paw-prints, whatever the day produced. {tortoise}
wrote {form_display} on a slate and asked {hare_phrase} to write the
form into the REPL so they could confirm it together."""),

    SubplotTemplate("""\
{hare_phrase}, {emo_proud}, declared the collection plain. {tortoise_phrase}
wrote {form_display} on a slate {place}, calmly. "It's not about plain
or fancy," {tortoise_he_she} said. "It's about whether the runtime
agrees with what we think we're describing.\""""),
]


def _ex(form, expected, concept, what, goal="", tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal, tags=tags)


_PLAN_G4 = _PLAN_POOL + (
    "I write the collection literal and let the REPL evaluate.",
    "I use the appropriate access function on the collection.",
)


G4_01 = SubjectCurriculum(grade=4, subject_id="G4-01",
    subject_title="Vector literal", fable="tortoise-hare",
    examples=[
        _ex("[1 2 3]", [1,2,3],   "a vector of three numbers",   "the vector",
            goal="create a vector containing 1, 2, and 3"),
        _ex("[]",      [],         "an empty vector",  "the empty vector",
            goal="create an empty vector"),
        _ex("[\"a\" \"b\"]", ["a","b"], "a vector of strings", "the vector of strings",
            goal="create a vector containing the strings a and b"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_02 = SubjectCurriculum(grade=4, subject_id="G4-02",
    subject_title="nth — vector access", fable="tortoise-hare",
    examples=[
        _ex("(nth [10 20 30] 0)", 10, "accessing by index", "the value at index 0",
            goal="get the element at index 0 of a vector containing 10, 20, and 30"),
        _ex("(nth [10 20 30] 2)", 30, "accessing by index", "the value at index 2",
            goal="get the element at index 2 of a vector containing 10, 20, and 30"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_03 = SubjectCurriculum(grade=4, subject_id="G4-03",
    subject_title="conj — append to vector", fable="tortoise-hare",
    examples=[
        _ex("(conj [1 2] 3)",       [1,2,3],   "the conj operation",      "the vector after conjing",
            goal="append 3 to the end of a vector containing 1 and 2"),
        _ex("(conj [] :hare)",      [":hare"], "the conj operation",     "the vector after conjing",
            goal="append the keyword :hare to an empty vector"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_04 = SubjectCurriculum(grade=4, subject_id="G4-04",
    subject_title="List literal", fable="tortoise-hare",
    examples=[
        _ex("'(1 2 3)", [1,2,3], "a list literal", "the list of three numbers",
            goal="create a list containing 1, 2, and 3"),
        _ex("'()",      [],       "an empty list",     "the empty list",
            goal="create an empty list"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_05 = SubjectCurriculum(grade=4, subject_id="G4-05",
    subject_title="cons — prepend to seq", fable="tortoise-hare",
    examples=[
        _ex("(cons 0 '(1 2 3))", [0,1,2,3], "the cons operation", "the seq after cons'ing",
            goal="prepend 0 to the front of a list containing 1, 2, and 3"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_06 = SubjectCurriculum(grade=4, subject_id="G4-06",
    subject_title="Map literal", fable="tortoise-hare",
    examples=[
        _ex("{:hare 1 :tortoise 2}", {":hare": 1, ":tortoise": 2},
            "a map literal", "the map with two entries",
            goal="create a map binding the keyword :hare to 1 and :tortoise to 2"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_07 = SubjectCurriculum(grade=4, subject_id="G4-07",
    subject_title="get — map lookup", fable="tortoise-hare",
    examples=[
        _ex("(get {:a 1 :b 2} :a)", 1, "map lookup", "the value at :a",
            goal="look up the value at key :a in a map binding :a to 1 and :b to 2"),
        _ex("(get {:a 1} :missing :default)", ":default",
            "map lookup with default", "the default value when key missing",
            goal="look up a missing key in a map, returning a default value"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_08 = SubjectCurriculum(grade=4, subject_id="G4-08",
    subject_title="assoc — map update", fable="tortoise-hare",
    examples=[
        _ex("(assoc {:a 1} :b 2)", {":a": 1, ":b": 2},
            "the assoc operation", "the map after update",
            goal="associate the key :b with value 2 onto a map binding :a to 1"),
        _ex("(assoc {:a 1} :a 99)", {":a": 99},
            "the assoc operation", "the map after update",
            goal="update the key :a to value 99 in a map that binds :a to 1"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_09 = SubjectCurriculum(grade=4, subject_id="G4-09",
    subject_title="dissoc — map remove key", fable="tortoise-hare",
    examples=[
        _ex("(dissoc {:a 1 :b 2} :a)", {":b": 2},
            "the dissoc operation", "the map without the key",
            goal="remove the key :a from a map binding :a to 1 and :b to 2"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_10 = SubjectCurriculum(grade=4, subject_id="G4-10",
    subject_title="keys and vals", fable="tortoise-hare",
    examples=[
        _ex("(count (keys {:a 1 :b 2 :c 3}))", 3,
            "counting keys in a map", "the number of keys in the map",
            goal="count how many keys are in a map binding :a, :b, and :c"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_11 = SubjectCurriculum(grade=4, subject_id="G4-11",
    subject_title="Set literal", fable="tortoise-hare",
    examples=[
        _ex("(count #{1 2 3})", 3, "the size of a set", "the size of the set",
            goal="count the elements in a set containing 1, 2, and 3"),
        _ex("(count #{1 1 1})", 1, "the size of a set", "the size of the set",
            goal="count the unique elements in a set literal with duplicate 1s"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_12 = SubjectCurriculum(grade=4, subject_id="G4-12",
    subject_title="Set membership", fable="tortoise-hare",
    examples=[
        _ex("(contains? #{1 2 3} 2)", True, "testing set membership", "whether 2 is in the set",
            goal="check whether 2 is a member of a set containing 1, 2, and 3"),
        _ex("(contains? #{1 2 3} 4)", False, "testing set membership", "whether 4 is in the set",
            goal="check whether 4 is a member of a set containing 1, 2, and 3"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_13 = SubjectCurriculum(grade=4, subject_id="G4-13",
    subject_title="count — universal", fable="tortoise-hare",
    examples=[
        _ex("(count [1 2 3 4 5])", 5, "the count of a collection", "the count",
            goal="count the elements in a vector containing 1, 2, 3, 4, and 5"),
        _ex("(count {:a 1 :b 2})", 2, "the count of a collection", "the count",
            goal="count the key-value pairs in a map"),
        _ex("(count #{:a :b :c})", 3, "the count of a collection", "the count",
            goal="count the elements in a set containing the keywords :a, :b, and :c"),
        _ex("(count \"tortoise\")", 8, "the length of a string", "the string length",
            goal="count the characters in the string tortoise"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_14 = SubjectCurriculum(grade=4, subject_id="G4-14",
    subject_title="empty?", fable="tortoise-hare",
    examples=[
        _ex("(empty? [])",   True,  "checking if a collection is empty",   "whether the vector is empty",
            goal="test whether an empty vector is empty"),
        _ex("(empty? [1])",  False, "checking if a collection is empty",  "whether the vector is empty",
            goal="test whether a vector containing 1 is empty"),
        _ex("(empty? \"\")", True,  "checking if a string is empty", "whether the string is empty",
            goal="test whether an empty string is empty"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_15 = SubjectCurriculum(grade=4, subject_id="G4-15",
    subject_title="first, rest, last", fable="tortoise-hare",
    examples=[
        _ex("(first [10 20 30])", 10, "getting the first element", "the first element",
            goal="get the first element of a vector containing 10, 20, and 30"),
        _ex("(last  [10 20 30])", 30, "getting the last element",  "the last element",
            goal="get the last element of a vector containing 10, 20, and 30"),
        _ex("(count (rest [10 20 30]))", 2, "removing the first element and counting", "the count after removing first",
            goal="count the elements remaining after removing the first element from a vector with 10, 20, and 30"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_16 = SubjectCurriculum(grade=4, subject_id="G4-16",
    subject_title="into and conj on collections", fable="tortoise-hare",
    examples=[
        _ex("(into [] '(1 2 3))", [1,2,3],
            "building a vector from a list", "the vector built from a list",
            goal="convert a list containing 1, 2, and 3 into a vector"),
        _ex("(into #{} [1 2 2 3])", [1,2,3],
            "building a set from a vector", "the set built from a vector",
            goal="convert a vector containing duplicates into a set, keeping unique elements"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_17 = SubjectCurriculum(grade=4, subject_id="G4-17",
    subject_title="Immutability — assoc returns new", fable="tortoise-hare",
    examples=[
        _ex("(let [m {:a 1}] (assoc m :a 99) m)", {":a": 1},
            "immutability of maps", "the original map after assoc",
            goal="demonstrate that assoc returns a new map without modifying the original"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_18 = SubjectCurriculum(grade=4, subject_id="G4-18",
    subject_title="Equality of vectors and lists", fable="tortoise-hare",
    examples=[
        _ex("(= [1 2 3] '(1 2 3))", True,
            "testing equality of different collection types", "whether vector and list are equal",
            goal="test whether a vector with elements 1, 2, 3 equals a list with the same elements"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_19 = SubjectCurriculum(grade=4, subject_id="G4-19",
    subject_title="range and seq", fable="tortoise-hare",
    examples=[
        _ex("(count (range 5))", 5, "counting elements in a range", "the count of range 0..4",
            goal="count how many numbers are generated by a range from 0 to 4"),
        _ex("(first (range 1 100))", 1, "getting the first element of a range", "the first of range 1..99",
            goal="get the first element of a range starting at 1 and ending before 100"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G4)


G4_20 = SubjectCurriculum(grade=4, subject_id="G4-20",
    subject_title="Collection vs sequence", fable="tortoise-hare",
    examples=[
        _ex("(count (seq [1 2 3]))", 3,
            "creating a sequence from a vector and counting", "the count of seq over a vector",
            goal="convert a vector containing 1, 2, and 3 to a sequence and count its elements"),
        _ex("(seq [])", None,
            "creating a sequence from an empty vector", "the result of seq on an empty vector",
            goal="convert an empty vector to a sequence"),
    ], subplots=_GOAL_SUBPLOTS, plan_pool=_PLAN_G4)


SUBJECTS = {s.subject_id: s for s in (
    G4_01, G4_02, G4_03, G4_04, G4_05, G4_06, G4_07, G4_08, G4_09, G4_10,
    G4_11, G4_12, G4_13, G4_14, G4_15, G4_16, G4_17, G4_18, G4_19, G4_20,
)}


def smoke_test() -> None:
    from mmllm.aesop.curriculum.generator import generate_subject
    for sid, sub in SUBJECTS.items():
        recs = generate_subject(sub, n_per_example=1, seed=0)
        for r in recs: assert r.tool_calls[0]["name"] == "eval"
    print(f"grade-4 tortoise-hare smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
