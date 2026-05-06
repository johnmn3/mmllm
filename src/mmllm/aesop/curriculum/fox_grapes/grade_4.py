"""Grade 4 — collections (Layer 4). Through fox-grapes.

Subplot lens: collections of fruit, clusters of grapes, baskets of plums,
figs, and rows of vines, that the foxes count, sort, and inspect. The
hasty fox dismisses the collection as not worth tallying ("probably
sour anyway"); the patient fox writes the form and lets the REPL
report the honest count or contents.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.fox_grapes.grade_1 import _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL
from mmllm.aesop.curriculum.fox_grapes._metaphor_pools import _BASKET_SUBPLOTS, _SIEVE_SUBPLOTS


_COLL_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [
    # NOTE: these two templates avoid putting both {form_display} AND a
    # "the form X" {concept_phrase} in close proximity (the duplication
    # produces ungrammatical "the form X described the form X" prose
    # when concept_phrase is "the form X" verbatim — see SKILL doc #11).
    SubplotTemplate("""\
{patient_fox_phrase} had been laying out a small collection {place} —
plums, figs, grape-clusters, whatever the orchard produced that
morning. {patient_fox} chalked {form_display} on a flat board and
asked {hasty_fox_him_her} to write the form into the REPL so they
could confirm it together."""),

    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, declared the basket of fruit too
plain to bother counting. {patient_fox_phrase} wrote {form_display}
on a slate {place}, calmly. "It's not about plain or fancy,"
{patient_fox_he_she} said. "It's about whether the runtime agrees
with what we think we're describing.\""""),
]


def _ex(form, expected, concept, what,
        goal="", scenario="", need="", mapping="", resolution="",
        tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal,
                          scenario=scenario, need=need,
                          mapping=mapping, resolution=resolution,
                          tags=tags)


_PLAN_G4 = _PLAN_POOL + (
    "I write the collection literal and let the REPL evaluate.",
    "I use the appropriate access function on the collection.",
)


G4_01 = SubjectCurriculum(grade=4, subject_id="G4-01",
    subject_title="Vector literal", fable="fox-grapes",
    examples=[
        _ex("[1 2 3]",
            [1,2,3],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Vix reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and her parchment recorded the day's count for that label.",
            tags=("story",)),
        _ex("[]",
            [],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Sly reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and their parchment recorded the day's count for that label.",
            tags=("story",)),
        _ex("[\"a\" \"b\"]",
            ["a","b"],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Renard reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and his parchment recorded the day's count for that label.",
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_02 = SubjectCurriculum(grade=4, subject_id="G4-02",
    subject_title="nth — vector access", fable="fox-grapes",
    examples=[
        _ex("(nth [10 20 30] 0)",
            10,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Vix reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and her parchment recorded the day's count for that label.",
            tags=("story",)),
        _ex("(nth [10 20 30] 2)",
            30,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Sly reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and their parchment recorded the day's count for that label.",
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_03 = SubjectCurriculum(grade=4, subject_id="G4-03",
    subject_title="conj — append to vector", fable="fox-grapes",
    examples=[
        _ex("(conj [1 2] 3)",
            [1,2,3],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Renard reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and his parchment recorded the day's count for that label.",
            tags=("story",)),
        _ex("(conj [] :fox)",
            [":fox"],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Vix reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and her parchment recorded the day's count for that label.",
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_04 = SubjectCurriculum(grade=4, subject_id="G4-04",
    subject_title="List literal", fable="fox-grapes",
    examples=[
        _ex("'(1 2 3)",
            [1,2,3],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Sly reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and their parchment recorded the day's count for that label.",
            tags=("story",)),
        _ex("'()",
            [],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Renard reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and his parchment recorded the day's count for that label.",
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_05 = SubjectCurriculum(grade=4, subject_id="G4-05",
    subject_title="cons — prepend to seq", fable="fox-grapes",
    examples=[
        _ex("(cons 0 '(1 2 3))",
            [0,1,2,3],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Vix reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and her parchment recorded the day's count for that label.",
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_06 = SubjectCurriculum(grade=4, subject_id="G4-06",
    subject_title="Map literal", fable="fox-grapes",
    examples=[
        _ex("{:fox 1 :grapes 2}",
            {":fox": 1, ":grapes": 2},
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Sly reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and their parchment recorded the day's count for that label.",
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_07 = SubjectCurriculum(grade=4, subject_id="G4-07",
    subject_title="get — map lookup", fable="fox-grapes",
    examples=[
        _ex("(get {:a 1 :b 2} :a)",
            1,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Renard reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and his parchment recorded the day's count for that label.",
            tags=("story",)),
        _ex("(get {:a 1} :missing :default)",
            ":default",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Vix reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and her parchment recorded the day's count for that label.",
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_08 = SubjectCurriculum(grade=4, subject_id="G4-08",
    subject_title="assoc — map update", fable="fox-grapes",
    examples=[
        _ex("(assoc {:a 1} :b 2)",
            {":a": 1, ":b": 2},
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Sly reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and their parchment recorded the day's count for that label.",
            tags=("story",)),
        _ex("(assoc {:a 1} :a 99)",
            {":a": 99},
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Renard reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and his parchment recorded the day's count for that label.",
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_09 = SubjectCurriculum(grade=4, subject_id="G4-09",
    subject_title="dissoc — map remove key", fable="fox-grapes",
    examples=[
        _ex("(dissoc {:a 1 :b 2} :a)",
            {":b": 2},
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Vix reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and her parchment recorded the day's count for that label.",
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_10 = SubjectCurriculum(grade=4, subject_id="G4-10",
    subject_title="keys and vals", fable="fox-grapes",
    examples=[
        _ex("(count (keys {:a 1 :b 2 :c 3}))",
            3,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Sly reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and their parchment recorded the day's count for that label.",
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_11 = SubjectCurriculum(grade=4, subject_id="G4-11",
    subject_title="Set literal", fable="fox-grapes",
    examples=[
        _ex("(count #{1 2 3})",
            3,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Renard reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and his parchment recorded the day's count for that label.",
            tags=("story",)),
        _ex("(count #{1 1 1})",
            1,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Vix reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and her parchment recorded the day's count for that label.",
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_12 = SubjectCurriculum(grade=4, subject_id="G4-12",
    subject_title="Set membership", fable="fox-grapes",
    examples=[
        _ex("(contains? #{1 2 3} 2)",
            True,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Sly reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and their parchment recorded the day's count for that label.",
            tags=("story",)),
        _ex("(contains? #{1 2 3} 4)",
            False,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Renard reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and his parchment recorded the day's count for that label.",
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_13 = SubjectCurriculum(grade=4, subject_id="G4-13",
    subject_title="count — universal", fable="fox-grapes",
    examples=[
        _ex("(count [1 2 3 4 5])",
            5,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Vix reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and her parchment recorded the day's count for that label.",
            tags=("story",)),
        _ex("(count {:a 1 :b 2})",
            2,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Sly reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and their parchment recorded the day's count for that label.",
            tags=("story",)),
        _ex("(count #{:a :b :c})",
            3,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Renard reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and his parchment recorded the day's count for that label.",
            tags=("story",)),
        _ex("(count \"grapes\")",
            6,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Vix reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and her parchment recorded the day's count for that label.",
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_14 = SubjectCurriculum(grade=4, subject_id="G4-14",
    subject_title="empty?", fable="fox-grapes",
    examples=[
        _ex("(empty? [])",
            True,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Sly reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and their parchment recorded the day's count for that label.",
            tags=("story",)),
        _ex("(empty? [1])",
            False,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Renard reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and his parchment recorded the day's count for that label.",
            tags=("story",)),
        _ex("(empty? \"\")",
            True,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Vix reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and her parchment recorded the day's count for that label.",
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_15 = SubjectCurriculum(grade=4, subject_id="G4-15",
    subject_title="first, rest, last", fable="fox-grapes",
    examples=[
        _ex("(first [10 20 30])",
            10,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Sly reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and their parchment recorded the day's count for that label.",
            tags=("story",)),
        _ex("(last  [10 20 30])",
            30,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Renard reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and his parchment recorded the day's count for that label.",
            tags=("story",)),
        _ex("(count (rest [10 20 30]))",
            2,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Vix reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and her parchment recorded the day's count for that label.",
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_16 = SubjectCurriculum(grade=4, subject_id="G4-16",
    subject_title="into and conj on collections", fable="fox-grapes",
    examples=[
        _ex("(into [] '(1 2 3))",
            [1,2,3],
            'the pour of a list into an empty vector',
            'the new-shape collection holding the same row of values',
            goal='pour a list into an empty vector, ending up with the same items in vector form',
            scenario='Sly the fox set an empty stave-bucket below the trellis and held a sieve above it. The sieve already held three graded clusters in a row, ready to be poured through into a fresh container of a different shape.',
            need="Sly wanted the contents transferred into the new bucket without losing the row's order — every cluster from the sieve, in the same sequence, settled into the empty bucket.",
            mapping="The into form pours one collection through into another, item by item, preserving order. The list pours through the sieve and into the empty vector — the container's shape changes; the row of values does not.",
            resolution='the bucket now held the same row Sly had started with, in the new vector shape — every cluster transferred, the order intact.',
            tags=("story",)),
        _ex("(into #{} [1 2 2 3])",
            [1,2,3],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox held a grape-sieve over an empty stave-bucket, the day's harvest ready to be poured through.",
            need="Sly wanted only what the sieve's rule kept; the rest could fall back into the row, untouched by the bucket.",
            mapping='A higher-order function is a sieve: it applies one operation to every item that passes through. The shape of what falls below is set by the rule, not by the input.',
            resolution="the bucket caught what the sieve's rule had let through, exactly the row Sly had wanted to keep.",
            tags=("story",)),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G4)


G4_17 = SubjectCurriculum(grade=4, subject_id="G4-17",
    subject_title="Immutability — assoc returns new", fable="fox-grapes",
    examples=[
        _ex("(let [m {:a 1}] (assoc m :a 99) m)",
            {":a": 1},
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Renard reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and his parchment recorded the day's count for that label.",
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_18 = SubjectCurriculum(grade=4, subject_id="G4-18",
    subject_title="Equality of vectors and lists", fable="fox-grapes",
    examples=[
        _ex("(= [1 2 3] '(1 2 3))",
            True,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Vix reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and her parchment recorded the day's count for that label.",
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_19 = SubjectCurriculum(grade=4, subject_id="G4-19",
    subject_title="range and seq", fable="fox-grapes",
    examples=[
        _ex("(count (range 5))",
            5,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Sly reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and their parchment recorded the day's count for that label.",
            tags=("story",)),
        _ex("(first (range 1 100))",
            1,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Renard reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and his parchment recorded the day's count for that label.",
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_20 = SubjectCurriculum(grade=4, subject_id="G4-20",
    subject_title="Collection vs sequence", fable="fox-grapes",
    examples=[
        _ex("(count (seq [1 2 3]))",
            3,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Vix reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and her parchment recorded the day's count for that label.",
            tags=("story",)),
        _ex("(seq [])",
            None,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Sly the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Sly reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and their parchment recorded the day's count for that label.",
            tags=("story",)),
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
    print(f"grade-4 fox-grapes smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
