"""Grade 4 — collections (Layer 4). through the milkmaid fable.

Subplot lens: collections of pebbles, milestones, racers, paw-prints,
plums, etc., that the characters count, sort, and manipulate.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.milkmaid.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL
)
from mmllm.aesop.curriculum.milkmaid._metaphor_pools import (
    _BASKET_SUBPLOTS, _SIEVE_SUBPLOTS,
)


_COLL_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [
    # NOTE: these two templates avoid putting both {form_display} AND a
    # "the form X" {concept_phrase} in close proximity (the duplication
    # produces ungrammatical "the form X described the form X" prose
    # when concept_phrase is "the form X" verbatim — see SKILL doc #11).
    SubplotTemplate("""\
{farmer_phrase} had been laying out a small collection {place} —
pebbles, milestones, paw-prints, whatever the day produced. {farmer}
wrote {form_display} on a slate and asked {milkmaid_phrase} to write the
form into the REPL so they could confirm it together."""),

    SubplotTemplate("""\
{milkmaid_phrase}, {emo_proud}, declared the collection plain. {farmer_phrase}
wrote {form_display} on a slate {place}, calmly. "It's not about plain
or fancy," {farmer_he_she} said. "It's about whether the runtime
agrees with what we think we're describing.\""""),
]


def _ex(form, expected, concept, what, goal=""):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal)


_PLAN_G4 = _PLAN_POOL + (
    "I write the collection literal and let the REPL evaluate.",
    "I use the appropriate access function on the collection.",
)


G4_01 = SubjectCurriculum(grade=4, subject_id="G4-01",
    subject_title="Vector literal", fable="milkmaid",
    examples=[
        SubjectExample(
            form="[1 2 3]",
            expected=[1,2,3],
            concept_phrase="a vector of three numbers",
            question_what="the vector",
            goal_text="create a vector containing 1, 2, and 3",
            scenario=(
                "The milkmaid set out a market-basket with three numbered compartments "
                "— each slot labeled to carry a different grade of dairy to market "
                "without mixing."
            ),
            need=(
                "She needed a literal sequence: three ordered slots holding the "
                "numbers 1, 2, and 3, ready to be carried as a single bundle "
                "without any slot bleeding into the next."
            ),
            mapping=(
                "A vector is the market-basket: `[1 2 3]` is three compartments in "
                "order, each holding exactly what was placed there. The runtime "
                "hands it back intact — no rearranging, no combining."
            ),
            resolution=(
                "the REPL handed back the three-compartment basket, items sitting "
                "exactly where placed — the market-basket arriving at the buyer's "
                "door unopened."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="[]",
            expected=[],
            concept_phrase="an empty vector",
            question_what="the empty vector",
            goal_text="create an empty vector",
        ),
        SubjectExample(
            form='["a" "b"]',
            expected=["a","b"],
            concept_phrase="a vector of strings",
            question_what="the vector of strings",
            goal_text="create a vector containing the strings a and b",
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_02 = SubjectCurriculum(grade=4, subject_id="G4-02",
    subject_title="nth — vector access", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(nth [10 20 30] 0)",
            expected=10,
            concept_phrase="accessing by index",
            question_what="the value at index 0",
            goal_text="get the element at index 0 of a vector containing 10, 20, and 30",
        ),
        SubjectExample(
            form="(nth [10 20 30] 2)",
            expected=30,
            concept_phrase="accessing by index",
            question_what="the value at index 2",
            goal_text="get the element at index 2 of a vector containing 10, 20, and 30",
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_03 = SubjectCurriculum(grade=4, subject_id="G4-03",
    subject_title="conj — append to vector", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(conj [1 2] 3)",
            expected=[1,2,3],
            concept_phrase="the conj operation",
            question_what="the vector after conjing",
            goal_text="append 3 to the end of a vector containing 1 and 2",
        ),
        SubjectExample(
            form="(conj [] :hare)",
            expected=[":hare"],
            concept_phrase="the conj operation",
            question_what="the vector after conjing",
            goal_text="append the keyword :hare to an empty vector",
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_04 = SubjectCurriculum(grade=4, subject_id="G4-04",
    subject_title="List literal", fable="milkmaid",
    examples=[
        SubjectExample(
            form="'(1 2 3)",
            expected=[1,2,3],
            concept_phrase="a list literal",
            question_what="the list of three numbers",
            goal_text="create a list containing 1, 2, and 3",
        ),
        SubjectExample(
            form="'()",
            expected=[],
            concept_phrase="an empty list",
            question_what="the empty list",
            goal_text="create an empty list",
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_05 = SubjectCurriculum(grade=4, subject_id="G4-05",
    subject_title="cons — prepend to seq", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(cons 0 '(1 2 3))",
            expected=[0,1,2,3],
            concept_phrase="the cons operation",
            question_what="the seq after cons'ing",
            goal_text="prepend 0 to the front of a list containing 1, 2, and 3",
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_06 = SubjectCurriculum(grade=4, subject_id="G4-06",
    subject_title="Map literal", fable="milkmaid",
    examples=[
        SubjectExample(
            form="{:hare 1 :tortoise 2}",
            expected={":hare": 1, ":tortoise": 2},
            concept_phrase="a map literal",
            question_what="the map with two entries",
            goal_text="create a map binding the keyword :hare to 1 and :tortoise to 2",
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_07 = SubjectCurriculum(grade=4, subject_id="G4-07",
    subject_title="get — map lookup", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(get {:a 1 :b 2} :a)",
            expected=1,
            concept_phrase="map lookup",
            question_what="the value at :a",
            goal_text="look up the value at key :a in a map binding :a to 1 and :b to 2",
        ),
        SubjectExample(
            form="(get {:a 1} :missing :default)",
            expected=":default",
            concept_phrase="map lookup with default",
            question_what="the default value when key missing",
            goal_text="look up a missing key in a map, returning a default value",
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_08 = SubjectCurriculum(grade=4, subject_id="G4-08",
    subject_title="assoc — map update", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(assoc {:a 1} :b 2)",
            expected={":a": 1, ":b": 2},
            concept_phrase="the assoc operation",
            question_what="the basket after associating value 2 with the :b compartment",
            goal_text="associate value 2 with the :b compartment of a basket already binding :a to 1",
        ),
        SubjectExample(
            form="(assoc {:a 1} :a 99)",
            expected={":a": 99},
            concept_phrase="the assoc operation",
            question_what="the map after using assoc to change the key :a to value 99",
            goal_text="update the key :a to value 99 in a map that binds :a to 1",
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_09 = SubjectCurriculum(grade=4, subject_id="G4-09",
    subject_title="dissoc — map remove key", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(dissoc {:a 1 :b 2} :a)",
            expected={":b": 2},
            concept_phrase="the dissoc operation",
            question_what="the map after using dissoc to remove a key",
            goal_text="remove the key :a from a map binding :a to 1 and :b to 2",
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_10 = SubjectCurriculum(grade=4, subject_id="G4-10",
    subject_title="keys and vals", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(count (keys {:a 1 :b 2 :c 3}))",
            expected=3,
            concept_phrase="counting keys in a map",
            question_what="the number of keys in the map",
            goal_text="count how many keys are in a map binding :a, :b, and :c",
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_11 = SubjectCurriculum(grade=4, subject_id="G4-11",
    subject_title="Set literal", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(count #{1 2 3})",
            expected=3,
            concept_phrase="the size of a set",
            question_what="the size of the set",
            goal_text="count the elements in a set containing 1, 2, and 3",
        ),
        SubjectExample(
            form="(count #{1 1 1})",
            expected=1,
            concept_phrase="the size of a set",
            question_what="the size of the set",
            goal_text="count the unique elements in a set literal with duplicate 1s",
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_12 = SubjectCurriculum(grade=4, subject_id="G4-12",
    subject_title="Set membership", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(contains? #{1 2 3} 2)",
            expected=True,
            concept_phrase="testing set membership",
            question_what="whether an element is in the set using contains?",
            goal_text="check whether 2 is a member of a set containing 1, 2, and 3",
        ),
        SubjectExample(
            form="(contains? #{1 2 3} 4)",
            expected=False,
            concept_phrase="testing set membership",
            question_what="whether an element is in the set using contains?",
            goal_text="check whether 4 is a member of a set containing 1, 2, and 3",
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_13 = SubjectCurriculum(grade=4, subject_id="G4-13",
    subject_title="count — universal", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(count [1 2 3 4 5])",
            expected=5,
            concept_phrase="the count of a collection",
            question_what="the number of elements in the collection",
            goal_text="count the elements in a vector containing 1, 2, 3, 4, and 5",
        ),
        SubjectExample(
            form="(count {:a 1 :b 2})",
            expected=2,
            concept_phrase="the count of a collection",
            question_what="the number of entries in the collection",
            goal_text="count the key-value pairs in a map",
        ),
        SubjectExample(
            form="(count #{:a :b :c})",
            expected=3,
            concept_phrase="the count of a collection",
            question_what="the number of elements in the collection",
            goal_text="count the elements in a set containing the keywords :a, :b, and :c",
        ),
        SubjectExample(
            form='(count "tortoise")',
            expected=8,
            concept_phrase="the length of a string",
            question_what="the number of characters in the string",
            goal_text="count the characters in the string tortoise",
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_14 = SubjectCurriculum(grade=4, subject_id="G4-14",
    subject_title="empty?", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(empty? [])",
            expected=True,
            concept_phrase="checking if a collection is empty",
            question_what="whether the collection is empty",
            goal_text="test whether an empty vector is empty",
        ),
        SubjectExample(
            form="(empty? [1])",
            expected=False,
            concept_phrase="checking if a collection is empty",
            question_what="whether the collection is empty",
            goal_text="test whether a vector containing 1 is empty",
        ),
        SubjectExample(
            form='(empty? "")',
            expected=True,
            concept_phrase="checking if a string is empty",
            question_what="whether the string is empty using empty?",
            goal_text="test whether an empty string is empty",
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_15 = SubjectCurriculum(grade=4, subject_id="G4-15",
    subject_title="first, rest, last", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(first [10 20 30])",
            expected=10,
            concept_phrase="getting the first element",
            question_what="the first element",
            goal_text="get the first element of a vector containing 10, 20, and 30",
        ),
        SubjectExample(
            form="(last [10 20 30])",
            expected=30,
            concept_phrase="getting the last element",
            question_what="the last element",
            goal_text="get the last element of a vector containing 10, 20, and 30",
        ),
        SubjectExample(
            form="(count (rest [10 20 30]))",
            expected=2,
            concept_phrase="removing the first element and counting",
            question_what="the count after removing first",
            goal_text="count the elements remaining after removing the first element from a vector with 10, 20, and 30",
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_16 = SubjectCurriculum(grade=4, subject_id="G4-16",
    subject_title="into and conj on collections", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(into [] '(1 2 3))",
            expected=[1,2,3],
            concept_phrase="building a vector from a list",
            question_what="the vector built from a list",
            goal_text="convert a list containing 1, 2, and 3 into a vector",
            scenario=(
                "The milkmaid set the milk-strainer over a fresh pail and poured the "
                "contents of a market list — three elements in order — through the "
                "strainer's mesh into a fresh vector-shaped container."
            ),
            need=(
                "She needed to pass the list through the strainer rule into a fresh "
                "vector — each element flowing through in sequence, nothing lost, "
                "nothing added."
            ),
            mapping=(
                "`into` is the milk-strainer over the pail: it pours each element of "
                "the source collection through the rule and collects them into the "
                "target container in order."
            ),
            resolution=(
                "the REPL returned the fresh vector with all three elements — the "
                "list had passed through the strainer and arrived in its new shape, "
                "intact."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(into #{} [1 2 2 3])",
            expected=[1,2,3],
            concept_phrase="building a set from a vector",
            question_what="the set built from a vector",
            goal_text="convert a vector containing duplicates into a set, keeping unique elements",
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G4)


G4_17 = SubjectCurriculum(grade=4, subject_id="G4-17",
    subject_title="Immutability — assoc returns new", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(let [m {:a 1}] (assoc m :a 99) m)",
            expected={":a": 1},
            concept_phrase="immutability of maps",
            question_what="the original map after assoc",
            goal_text="demonstrate that assoc returns a new map without modifying the original",
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_18 = SubjectCurriculum(grade=4, subject_id="G4-18",
    subject_title="Equality of vectors and lists", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(= [1 2 3] '(1 2 3))",
            expected=True,
            concept_phrase="testing equality of different collection types",
            question_what="whether vector and list are equal",
            goal_text="test whether a vector with elements 1, 2, 3 equals a list with the same elements",
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_19 = SubjectCurriculum(grade=4, subject_id="G4-19",
    subject_title="range and seq", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(count (range 5))",
            expected=5,
            concept_phrase="counting elements in a range",
            question_what="the count of range 0..4",
            goal_text="count how many numbers are generated by a range from 0 to 4",
        ),
        SubjectExample(
            form="(first (range 1 100))",
            expected=1,
            concept_phrase="getting the first element of a range",
            question_what="the first of range 1..99",
            goal_text="get the first element of a range starting at 1 and ending before 100",
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_20 = SubjectCurriculum(grade=4, subject_id="G4-20",
    subject_title="Collection vs sequence", fable="milkmaid",
    examples=[
        SubjectExample(
            form="(count (seq [1 2 3]))",
            expected=3,
            concept_phrase="creating a sequence from a vector and counting",
            question_what="the count of seq over a vector",
            goal_text="convert a vector containing 1, 2, and 3 to a sequence and count its elements",
        ),
        SubjectExample(
            form="(seq [])",
            expected=None,
            concept_phrase="creating a sequence from an empty vector",
            question_what="the result of seq on an empty vector",
            goal_text="convert an empty vector to a sequence",
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


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
