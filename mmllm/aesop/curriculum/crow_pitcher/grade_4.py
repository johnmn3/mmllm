"""Grade 4 — collections (Layer 4). Through crow-pitcher.

Subplot lens: collections of pebbles, milestones, racers, paw-prints,
plums, etc., that the characters count, sort, and manipulate.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.crow_pitcher.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL
)
from mmllm.aesop.curriculum.crow_pitcher._metaphor_pools import (
    _BASKET_SUBPLOTS, _SIEVE_SUBPLOTS,
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
    subject_title="Vector literal", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="[1 2 3]",
            expected=[1,2,3],
            concept_phrase="a vector of the numbers",
            question_what="the vector",
            goal_text="create a vector containing 1, 2, and 3",

            scenario=(
                "Korvus perched at the pitcher's rim in the garden and laid "
                "three smooth stones in a tidy row on the clay lip — each "
                "one placed deliberately, left to right, numbered by position."
            ),
            need=(
                "He needed the REPL to confirm that the ordered stone-pile "
                "held exactly those the stones in that order."
            ),
            mapping=(
                "A vector is an ordered stone-pile: square brackets open and "
                "close the pile, stones are listed left to right by position. "
                "The REPL returns the pile as it was arranged."
            ),
            resolution=(
                'The REPL returned the ordered pile, every stone confirmed in sequence (with `1` as the input value) (with `3` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="[]",
            expected=[],
            concept_phrase="an empty vector",
            question_what="the empty vector",
            goal_text="create an empty vector",

            scenario=(
                "Caw arrived at the pitcher in the orchard before any stones "
                "had been gathered. The clay lip was bare, no pile laid out, "
                "no stones waiting."
            ),
            need=(
                "She needed to show the REPL an empty stone-pile — a reserved "
                "spot on the rim holding nothing yet."
            ),
            mapping=(
                "Empty square brackets describe a stone-pile with no stones "
                "inside. The structure exists but holds nothing; the REPL "
                "returns the empty pile as written."
            ),
            resolution=(
                "The REPL returned an empty pile, confirming the reserved "
                "space held nothing at all. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='["a" "b"]',
            expected=["a","b"],
            concept_phrase="a vector of strings",
            question_what="the vector of strings",
            goal_text="create a vector containing the strings a and b",

            scenario=(
                "Sable scratched two short talon-marks on clay tiles at the "
                "hilltop pitcher — one mark for a, one for b — then slid "
                "them side by side into a small stone-pile on the rim."
            ),
            need=(
                "The question was whether the REPL would hold the scratched "
                "marks as an ordered two-stone pile with label-stones inside."
            ),
            mapping=(
                "Strings nest inside the vector as label-stones: quoted marks "
                "sit in the pile ordered left to right, just like smooth "
                "pebbles. The REPL returns the pile with both marks intact."
            ),
            resolution=(
                "The pitcher returned the two-label pile, both marks present "
                "and in order."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_02 = SubjectCurriculum(grade=4, subject_id="G4-02",
    subject_title="nth — vector access", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(nth [10 20 30] 0)",
            expected=10,
            concept_phrase="accessing by index",
            question_what="the value at index 0",
            goal_text="get the element at index 0 of a vector containing 10, 20, and 30",

            scenario=(
                "Korvus had arranged a stone-pile of three on the pitcher's "
                "rim in the meadow — ten, twenty, thirty — left to right. He "
                "needed to reach the leftmost stone without disturbing the rest."
            ),
            need=(
                "He needed to name a position number and pull exactly that "
                "stone from the pile, leaving the others untouched."
            ),
            mapping=(
                "`nth` counts from zero along the stone-pile and lifts the "
                "stone at that position. Index 0 is the leftmost stone; the "
                "pile itself is unchanged after the reach."
            ),
            resolution=(
                "The REPL lifted the leftmost stone from the pile and "
                "returned its count. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(nth [10 20 30] 2)",
            expected=30,
            concept_phrase="accessing by index",
            question_what="the value at index 2",
            goal_text="get the element at index 2 of a vector containing 10, 20, and 30",

            scenario=(
                "Caw eyed the same three-stone pile on the rim — ten, twenty, "
                "thirty. She wanted the rightmost stone, the third one, "
                "at position two counting from zero."
            ),
            need=(
                "Without knowing the count ahead of time, she needed `nth` "
                "to reach the correct position reliably."
            ),
            mapping=(
                "`nth` steps along the pile by index: zero is left, one is "
                "middle, two is right. It lifts that stone and returns it; "
                "the pile stays arranged as before."
            ),
            resolution=(
                "The REPL reached to position two and returned the rightmost stone's count (with `10` as the input value)."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_03 = SubjectCurriculum(grade=4, subject_id="G4-03",
    subject_title="conj — append to vector", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(conj [1 2] 3)",
            expected=[1,2,3],
            concept_phrase="the conj operation",
            question_what="the vector after conjing",
            goal_text="append 3 to the end of a vector containing 1 and 2",

            scenario=(
                "Sable had a two-stone pile on the pitcher's rim in the "
                "village — one and two, side by side. A third stone sat "
                "ready on the ground; the pile needed it at the right end. (with {drawn.a} folded in)"
            ),
            need=(
                "The original pile had to remain untouched; a new extended "
                "pile should come back from the REPL with the third stone added."
            ),
            mapping=(
                "`conj` places a new stone at the right end of a vector pile "
                "and returns the extended pile. The original two-stone pile "
                "is unchanged; only the new pile has the third stone."
            ),
            resolution=(
                "The REPL returned a fresh three-stone pile, original pile "
                "undisturbed beside it. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(conj [] :hare)",
            expected=[":hare"],
            concept_phrase="the conj operation",
            question_what="the vector after conjing",
            goal_text="append the keyword :hare to an empty vector",

            scenario=(
                "Korvus started with a bare rim-spot on the pitcher in the "
                "garden — an empty pile, no stones. He had one label-stone "
                "marked :hare ready to drop in."
            ),
            need=(
                "He needed `conj` to place the label-stone into the empty "
                "pile and return a one-stone pile for the REPL to confirm."
            ),
            mapping=(
                "`conj` on an empty vector creates a new one-element pile. "
                "The label-stone becomes the sole occupant; the empty spot "
                "on the rim is left as it was."
            ),
            resolution=(
                "The REPL returned a one-label pile, the keyword stone "
                "seated at the right end. (the keyword :hare)"
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_04 = SubjectCurriculum(grade=4, subject_id="G4-04",
    subject_title="List literal", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="'(1 2 3)",
            expected=[1,2,3],
            concept_phrase="a list literal",
            question_what="the list of the numbers",
            goal_text="create a list containing 1, 2, and 3",

            scenario=(
                "Caw arranged the stones in a front-to-back queue on the "
                "pitcher's edge in the market — one stone leading, then two, "
                "then three, each touching the next in a chain."
            ),
            need=(
                "She needed the REPL to read the chained queue as a list, "
                "front element reachable first, the rest trailing behind."
            ),
            mapping=(
                "A quoted list is a stone-chain: parentheses and a leading "
                "quote mark the queue. The front stone is reachable first; "
                "the REPL returns the chain in order."
            ),
            resolution=(
                'The REPL returned the three-stone chain, front to back, as a list (with `1` as the input value) (with `3` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="'()",
            expected=[],
            concept_phrase="an empty list",
            question_what="the empty list",
            goal_text="create an empty list",

            scenario=(
                "Sable traced an empty parenthesis shape in the dust at the "
                "road's edge near the pitcher — a queue marker with no stones "
                "waiting inside it."
            ),
            need=(
                "An empty queue still needed a valid list shape so later "
                "operations could treat it as a sequence."
            ),
            mapping=(
                "A quoted empty pair of parentheses is an empty stone-chain. "
                "No stones wait inside, but the chain structure is valid; the "
                "REPL returns it as an empty list."
            ),
            resolution=(
                "The REPL confirmed an empty list, the chain structure intact "
                "with nothing inside. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_05 = SubjectCurriculum(grade=4, subject_id="G4-05",
    subject_title="cons — prepend to seq", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(cons 0 '(1 2 3))",
            expected=[0,1,2,3],
            concept_phrase="the cons operation",
            question_what="the seq after cons'ing",
            goal_text="prepend 0 to the front of a list containing 1, 2, and 3",

            scenario=(
                "Korvus found a stone-chain of three at the pitcher in the "
                "orchard — the drawn counts queued up. He had a zero-stone "
                "in his talon that needed to lead the chain."
            ),
            need=(
                "The zero-stone had to become the new front without disturbing "
                "the existing chain; a new sequence should extend from it."
            ),
            mapping=(
                "`cons` places a stone at the front and returns a new sequence "
                "with that stone leading. The original three-stone chain is "
                "unchanged; the result is a four-element sequence."
            ),
            resolution=(
                "The REPL returned a new sequence with the zero-stone at the "
                "front, original chain following. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_06 = SubjectCurriculum(grade=4, subject_id="G4-06",
    subject_title="Map literal", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="{:hare 1 :tortoise 2}",
            expected={":hare": 1, ":tortoise": 2},
            concept_phrase="a map literal",
            question_what="the map with two entries",
            goal_text="create a map binding the keyword :hare to 1 and :tortoise to 2",

            scenario=(
                "Caw scratched two compartment labels into wet clay at the "
                "farm pitcher — one slot labeled :hare holding a single stone, "
                "another labeled :tortoise holding two stones."
            ),
            need=(
                "She needed the REPL to recognize the pair of label-to-count "
                "bindings as a single stone-pile map with two entries."
            ),
            mapping=(
                "Curly braces mark a map-pile: each keyword is a compartment "
                "label scratched in clay, each number is the count in that "
                "compartment. The REPL returns the labeled two-compartment pile."
            ),
            resolution=(
                "The REPL returned the map with both compartments named and "
                "filled as scratched. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_07 = SubjectCurriculum(grade=4, subject_id="G4-07",
    subject_title="get — map lookup", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(get {:a 1 :b 2} :a)",
            expected=1,
            concept_phrase="map lookup",
            question_what="the value at :a",
            goal_text="look up the value at key :a in a map binding :a to 1 and :b to 2",

            scenario=(
                "Sable had a two-compartment stone-pile at the hilltop pitcher "
                "— :a held one stone, :b held two. She needed the count from "
                "the :a compartment without disturbing the other."
            ),
            need=(
                "She needed `get` to find the :a label among the compartments "
                "and return whatever count sat there."
            ),
            mapping=(
                "`get` searches the map-pile by label and lifts the value in "
                "that compartment. It reads :a, finds it, and returns the "
                "count stored there. The pile itself is unchanged."
            ),
            resolution=(
                "The REPL returned the count from the :a compartment, "
                "the pile intact. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(get {:a 1} :missing :default)",
            expected=":default",
            concept_phrase="map lookup with default",
            question_what="the default value when key missing",
            goal_text="look up a missing key in a map, returning a default value",

            scenario=(
                "Korvus checked a single-compartment pile at the pitcher in "
                "the village — only :a labeled. He reached for :missing, which "
                "had no compartment scratched in the clay."
            ),
            need=(
                "He needed the REPL to return a fallback label-stone rather "
                "than nothing when the sought compartment did not exist."
            ),
            mapping=(
                "`get` with a third argument returns that argument when the "
                "key is absent. The fallback label-stone is returned instead "
                "of nil whenever the compartment cannot be found."
            ),
            resolution=(
                "The REPL returned the fallback label-stone, confirming the "
                "absent compartment triggered the default."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_08 = SubjectCurriculum(grade=4, subject_id="G4-08",
    subject_title="assoc — map update", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(assoc {:a 1} :b 2)",
            expected={":a": 1, ":b": 2},
            concept_phrase="the assoc operation",
            question_what="the basket after associating value 2 with the :b compartment",
            goal_text="associate value 2 with the :b compartment of a basket already binding :a to 1",

            scenario=(
                "Caw held a one-compartment stone-pile at the orchard pitcher "
                "— :a with one stone. A second compartment, :b, needed to be "
                "scratched in and filled with two stones."
            ),
            need=(
                "The original pile had to stay as it was; `assoc` should "
                "return a new pile that also had the :b compartment filled."
            ),
            mapping=(
                "`assoc` scratches a new compartment into a copy of the pile "
                "and fills it. The original pile keeps only :a; the returned "
                "new pile holds both :a and the fresh :b compartment."
            ),
            resolution=(
                "The REPL returned the extended pile with both compartments "
                "present, the original unchanged. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(assoc {:a 1} :a 99)",
            expected={":a": 99},
            concept_phrase="the assoc operation",
            question_what="the map after using assoc to change the key :a to value 99",
            goal_text="update the key :a to value 99 in a map that binds :a to 1",

            scenario=(
                "Sable noticed the :a compartment in a pile at the meadow "
                "pitcher held only one stone. The correct count was ninety-nine; "
                "the compartment needed updating in a fresh pile."
            ),
            need=(
                "She needed `assoc` to produce a new pile where :a held the "
                "corrected count, while the original pile was left as proof."
            ),
            mapping=(
                "`assoc` on an existing key replaces its value in the returned "
                "pile. The original one-stone :a compartment is unchanged; only "
                "the new pile reflects the updated count."
            ),
            resolution=(
                "The REPL returned a new pile with :a holding the updated "
                "count, original pile untouched. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_09 = SubjectCurriculum(grade=4, subject_id="G4-09",
    subject_title="dissoc — map remove key", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(dissoc {:a 1 :b 2} :a)",
            expected={":b": 2},
            concept_phrase="the dissoc operation",
            question_what="the map after using dissoc to remove a key",
            goal_text="remove the key :a from a map binding :a to 1 and :b to 2",

            scenario=(
                "Korvus had a two-compartment pile at the road pitcher — :a "
                "with one stone and :b with two. The :a compartment was no "
                "longer needed; it had to be stripped from a new copy."
            ),
            need=(
                "He needed a pile that held only :b, leaving the original "
                "two-compartment pile intact as the source."
            ),
            mapping=(
                "`dissoc` returns a new pile with the named compartment removed. "
                "The original still carries :a; only the returned pile has it "
                "stripped, leaving just :b behind."
            ),
            resolution=(
                "The REPL returned the reduced pile with only the :b "
                "compartment remaining. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_10 = SubjectCurriculum(grade=4, subject_id="G4-10",
    subject_title="keys and vals", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(count (keys {:a 1 :b 2 :c 3}))",
            expected=3,
            concept_phrase="counting keys in a map",
            question_what="the number of keys in the map",
            goal_text="count how many keys are in a map binding :a, :b, and :c",

            scenario=(
                "Caw peered at a three-compartment stone-pile on the pitcher's "
                "rim in the garden — :a, :b, and :c each scratched in. She "
                "wanted to count only the labels, not the stones inside."
            ),
            need=(
                "She needed to extract the label-list from the pile and then "
                "tally how many labels there were."
            ),
            mapping=(
                "`keys` lifts the compartment labels out of a map-pile as a "
                "sequence; `count` tallies that sequence. Together they count "
                "how many named compartments the pile holds."
            ),
            resolution=(
                "The REPL returned the tally of labels, confirming how many "
                "compartments were scratched in. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_11 = SubjectCurriculum(grade=4, subject_id="G4-11",
    subject_title="Set literal", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(count #{1 2 3})",
            expected=3,
            concept_phrase="the size of a set",
            question_what="the size of the set",
            goal_text="count the elements in a set containing 1, 2, and 3",

            scenario=(
                "Sable dropped three distinct stones into a sorting-pile at "
                "the meadow pitcher — the drawn counts, no duplicates allowed. "
                "She needed to know how many unique stones the pile held."
            ),
            need=(
                "A count of the sorting-pile would tell her whether all three "
                "distinct stones had settled in without collision."
            ),
            mapping=(
                "A set is a sorting-pile where each stone is unique. `count` "
                "tallies the unique stones present. `#{}` marks the pile; "
                "each number is a distinct stone inside it."
            ),
            resolution=(
                "The REPL returned the count of unique stones settled "
                "in the sorting-pile. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(count #{1 1 1})",
            expected=1,
            concept_phrase="the size of a set",
            question_what="the size of the set",
            goal_text="count the unique elements in a set literal with duplicate 1s",

            scenario=(
                "Korvus tried to fill the sorting-pile at the hilltop pitcher "
                "with three identical stones, each marked one. The pile's "
                "groove would only seat a stone once."
            ),
            need=(
                "He needed the REPL to confirm that duplicate stones collapse "
                "into a single entry — only one would remain."
            ),
            mapping=(
                "A set-pile rejects duplicates: when three identical stones "
                "are offered, only one settles in. `count` reflects how many "
                "unique stones actually occupy the pile."
            ),
            resolution=(
                'The REPL returned a count of one, confirming all three duplicates had collapsed to a single stone (with `1` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_12 = SubjectCurriculum(grade=4, subject_id="G4-12",
    subject_title="Set membership", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(contains? #{1 2 3} 2)",
            expected=True,
            concept_phrase="testing set membership",
            question_what="whether an element is in the set using contains?",
            goal_text="check whether 2 is a member of a set containing 1, 2, and 3",

            scenario=(
                "Caw had a three-stone sorting-pile at the farm pitcher — "
                "the drawn counts settled in their grooves. She held a stone "
                "marked two and needed to know if it already occupied a slot."
            ),
            need=(
                "Without lifting every stone, she needed `contains?` to answer "
                "whether the two-marked stone already sat in the pile."
            ),
            mapping=(
                "`contains?` checks the sorting-pile for the named stone "
                "without disturbing the pile. If the stone occupies a slot, "
                "the REPL returns true; otherwise false."
            ),
            resolution=(
                "The REPL confirmed the predicate held — confirming the two-stone was already "
                "seated in the pile. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(contains? #{1 2 3} 4)",
            expected=False,
            concept_phrase="testing set membership",
            question_what="whether an element is in the set using contains?",
            goal_text="check whether 4 is a member of a set containing 1, 2, and 3",

            scenario=(
                "Sable held a stone marked four near the same three-stone "
                "sorting-pile at the farm pitcher. No groove was carved for "
                "four; she asked whether it belonged."
            ),
            need=(
                "She needed a definitive answer before adding the stone — "
                "`contains?` would confirm absence without modifying the pile."
            ),
            mapping=(
                "`contains?` scans for the stone in the pile's grooves. When "
                "no matching groove is found the REPL returns false, telling "
                "the crow the stone has no slot."
            ),
            resolution=(
                'The REPL signalled the predicate did not hold — confirming the four-stone had no slot in the sorting-pile (with `1` as the input value) (with `3` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_13 = SubjectCurriculum(grade=4, subject_id="G4-13",
    subject_title="count — universal", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(count [1 2 3 4 5])",
            expected=5,
            concept_phrase="the count of a collection",
            question_what="the number of elements in the collection",
            goal_text="count the elements in the vector [1 2 3 4 5]",

            scenario=(
                "Korvus laid five smooth stones in a row on the pitcher rim "
                "at the market — one through five, each touching the next. "
                "He needed a quick tally before moving on."
            ),
            need=(
                "Without picking up each stone, he needed `count` to return "
                "the total occupancy of the ordered pile."
            ),
            mapping=(
                "`count` tallies every element in a collection without "
                "inspecting their values. For a vector-pile of the stones, "
                "it returns five — one per stone in the row."
            ),
            resolution=(
                "The REPL returned the stone-count of the ordered pile "
                "without lifting a single stone. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(count {:a 1 :b 2})",
            expected=2,
            concept_phrase="the count of a collection",
            question_what="the number of entries in the collection",
            goal_text="count the key-value pairs in a map",

            scenario=(
                "Caw surveyed a two-compartment map-pile at the village "
                "pitcher — :a and :b each scratched with a count inside. "
                "She wanted to know how many compartments, not how many stones."
            ),
            need=(
                "She needed `count` to tally the compartment entries rather "
                "than the stones within each compartment."
            ),
            mapping=(
                "`count` on a map-pile returns the number of key-value pairs. "
                "Each scratched compartment is one entry; the REPL counts "
                "entries, not the values stored inside them."
            ),
            resolution=(
                "The REPL returned the number of compartment entries present "
                "in the map-pile. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(count #{:a :b :c})",
            expected=3,
            concept_phrase="the count of a collection",
            question_what="the number of elements in the collection",
            goal_text="count the elements in a set containing the keywords :a, :b, and :c",

            scenario=(
                "Sable pressed three label-stones into the sorting-pile at "
                "the orchard pitcher — :a, :b, :c, each unique. She needed "
                "to confirm the pile held exactly three distinct labels."
            ),
            need=(
                "A count would verify that no duplicates had collapsed the "
                "three distinct label-stones into fewer."
            ),
            mapping=(
                "`count` on a set-pile tallies the unique stones settled in "
                "the grooves. Three distinct labels yield three; duplicates "
                "would have reduced the tally."
            ),
            resolution=(
                "The REPL returned the count of unique label-stones settled "
                "in the sorting-pile."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(count "tortoise")',
            expected=8,
            concept_phrase="the length of a string",
            question_what="the number of characters in the string",
            goal_text="count the characters in the string tortoise",

            scenario=(
                "Korvus scratched the word tortoise bead by bead on a vine "
                "at the hilltop pitcher — each letter a single bead on the "
                "string, left to right. He wanted to know the bead-count."
            ),
            need=(
                "He needed `count` to tally the beads on the string without "
                "reading each letter aloud one by one."
            ),
            mapping=(
                "`count` treats a string as a bead-string and returns the "
                "number of character-beads on it. Each letter is one bead; "
                "the REPL tallies the full string's length."
            ),
            resolution=(
                "The REPL returned the bead-count of the full word, every "
                "letter tallied. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_14 = SubjectCurriculum(grade=4, subject_id="G4-14",
    subject_title="empty?", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(empty? [])",
            expected=True,
            concept_phrase="checking if a collection is empty",
            question_what="whether the collection is empty",
            goal_text="test whether an empty vector is empty",

            scenario=(
                "Caw glanced at the pitcher rim in the garden where an empty "
                "stone-pile had been reserved — square brackets drawn in dust, "
                "no stones resting inside."
            ),
            need=(
                "She needed `empty?` to confirm the pile truly had nothing "
                "before she started adding stones."
            ),
            mapping=(
                "`empty?` checks whether a collection holds any elements. "
                "An empty vector-pile has no stones; the REPL returns true "
                "to confirm the pile is bare."
            ),
            resolution=(
                "The REPL confirmed the pile was empty, returning true "
                "for the bare vector. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(empty? [1])",
            expected=False,
            concept_phrase="checking if a collection is empty",
            question_what="whether the collection is empty",
            goal_text="test whether a vector containing 1 is empty",

            scenario=(
                "Sable spotted a vector-pile on the meadow pitcher with a "
                "single stone inside — just one pebble, no more. She asked "
                "`empty?` whether the pile held nothing."
            ),
            need=(
                "She needed the REPL to distinguish a truly empty pile from "
                "one that held even a single stone."
            ),
            mapping=(
                "`empty?` returns false when at least one element occupies "
                "the collection. One stone in the pile is enough to confirm "
                "the pile is not empty."
            ),
            resolution=(
                "The REPL signalled the predicate did not hold — the single stone sufficient to "
                "show the pile was occupied. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form='(empty? "")',
            expected=True,
            concept_phrase="checking if a string is empty",
            question_what="whether the string is empty using empty?",
            goal_text="test whether an empty string is empty",

            scenario=(
                "Korvus held a bead-string vine at the hilltop pitcher with "
                "no beads threaded — the vine knotted at both ends, empty "
                "between. He wanted `empty?` to read the bare vine."
            ),
            need=(
                "He needed confirmation the string had no character-beads "
                "before attempting to slice or join it."
            ),
            mapping=(
                "`empty?` on a string checks whether any character-beads "
                "hang on the vine. An empty string is a bare vine with zero "
                "beads; the REPL returns true."
            ),
            resolution=(
                'The REPL confirmed the predicate held — confirming the vine carried no beads at all (with `` as the input value) (with `` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_15 = SubjectCurriculum(grade=4, subject_id="G4-15",
    subject_title="first, rest, last", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(first [10 20 30])",
            expected=10,
            concept_phrase="getting the first element",
            question_what="the first element",
            goal_text="get the first element of a vector containing 10, 20, and 30",

            scenario=(
                "Caw perched beside a three-stone row on the farm pitcher — "
                "ten, twenty, thirty lined up left to right. She needed the "
                "leading stone without touching the others."
            ),
            need=(
                "She needed `first` to reach the leftmost stone and return "
                "its count while leaving the row intact."
            ),
            mapping=(
                "`first` reaches to the front of the collection and returns "
                "the element there. For a vector-pile the front is the "
                "leftmost stone; the rest of the row is untouched."
            ),
            resolution=(
                "The REPL returned the leading stone's count, the row "
                "still in place. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(last [10 20 30])",
            expected=30,
            concept_phrase="getting the last element",
            question_what="the last element",
            goal_text="get the last element of a vector containing 10, 20, and 30",

            scenario=(
                "Sable eyed the same three-stone row — ten, twenty, thirty — "
                "at the farm pitcher. The rightmost stone was the goal; she "
                "needed the trailing end without walking the whole row."
            ),
            need=(
                "She needed `last` to jump directly to the rightmost stone "
                "and return its count in one step."
            ),
            mapping=(
                "`last` reaches the end of the collection and returns the "
                "final element. For a vector-pile it is the rightmost stone; "
                "the REPL returns it without disturbing the row."
            ),
            resolution=(
                "The REPL returned the trailing stone's count, confirming "
                "the rightmost position. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(count (rest [10 20 30]))",
            expected=2,
            concept_phrase="removing the first element and counting",
            question_what="the count after removing first",
            goal_text="count the elements remaining after removing the first element from a vector with 10, 20, and 30",

            scenario=(
                "Korvus removed the leading stone from the three-stone row "
                "at the road pitcher, leaving twenty and thirty behind. He "
                "needed to know how many stones remained in the tail."
            ),
            need=(
                "He needed `rest` to drop the front stone and `count` to "
                "tally what remained in the shortened row."
            ),
            mapping=(
                "`rest` returns the collection minus its first element as a "
                "sequence; `count` tallies that sequence. One stone removed "
                "from three leaves a two-element tail."
            ),
            resolution=(
                "The REPL returned the count of the tail after the leading "
                "stone was removed. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_16 = SubjectCurriculum(grade=4, subject_id="G4-16",
    subject_title="into and conj on collections", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(into [] '(1 2 3))",
            expected=[1,2,3],
            concept_phrase="building a vector from a list",
            question_what="the vector built from a list",
            goal_text="convert a list containing 1, 2, and 3 into a vector",

            scenario=(
                "Caw had a three-stone chain queued at the market pitcher and "
                "an empty vector-pile waiting beside it. She needed to pour "
                "the chain's stones into the ordered pile."
            ),
            need=(
                "She needed `into` to transfer each stone from the chain into "
                "the vector-pile, preserving order."
            ),
            mapping=(
                "`into` pours one collection's stones into another. The chain "
                "is the source; the empty vector is the destination. Each stone "
                "lands in order, building the vector-pile from the chain."
            ),
            resolution=(
                "The REPL returned the filled vector-pile with all stones from "
                "the chain transferred in order. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(into #{} [1 2 2 3])",
            expected=[1,2,3],
            concept_phrase="building a set from a vector",
            question_what="the set built from a vector",
            goal_text="convert a vector containing duplicates into a set, keeping unique elements",

            scenario=(
                'Sable had a four-stone vector-pile at the orchard pitcher — the counts — with a duplicate two. She poured the stones toward an empty sorting-pile.'
            ),
            need=(
                "The sorting-pile would reject any duplicate, so only unique "
                "stones would remain after the pour."
            ),
            mapping=(
                "`into` pours stones into the target collection's rules. "
                "A set-pile rejects duplicates on entry; the two-stone arrives "
                "twice but only one settles, leaving three unique stones."
            ),
            resolution=(
                "The REPL returned the sorting-pile with duplicates collapsed "
                "to unique stones only. (count: 3)"
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G4)


G4_17 = SubjectCurriculum(grade=4, subject_id="G4-17",
    subject_title="Immutability — assoc returns new", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(let [m {:a 1}] (assoc m :a 99) m)",
            expected={":a": 1},
            concept_phrase="immutability of maps",
            question_what="the original map after assoc",
            goal_text="demonstrate that assoc returns a new map without modifying the original",

            scenario=(
                "Korvus tucked a one-compartment stone-pile under his wing "
                "at the village pitcher — :a holding one stone, named m. He "
                "then called `assoc` to update :a to ninety-nine in a new pile."
            ),
            need=(
                "He needed the REPL to confirm that m, the wing-cached pile, "
                "still held the original count after `assoc` had run."
            ),
            mapping=(
                "`assoc` never changes the original map-pile; it returns a "
                "brand-new pile with the update. The wing-cached m is "
                "unaffected — it still holds the original compartment count."
            ),
            resolution=(
                "The REPL returned the original pile from under the wing, "
                "unchanged by the assoc call. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_18 = SubjectCurriculum(grade=4, subject_id="G4-18",
    subject_title="Equality of vectors and lists", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(= [1 2 3] '(1 2 3))",
            expected=True,
            concept_phrase="testing equality of different collection types",
            question_what="whether vector and list are equal",
            goal_text="test whether a vector with elements 1, 2, 3 equals a list with the same elements",

            scenario=(
                "Caw laid a three-stone vector-pile beside a three-stone "
                "chain at the road pitcher — same stones, same order, "
                "different container shapes. She wondered if `=` would agree."
            ),
            need=(
                "She needed `=` to compare the contents of both containers "
                "regardless of whether one was a pile-row or a chain."
            ),
            mapping=(
                "`=` compares collections by their sequential content, not "
                "their container type. A vector and a list with identical "
                "ordered stones are considered equal in Clojure."
            ),
            resolution=(
                "The REPL confirmed the predicate held — confirming same stones same order "
                "means equality regardless of container. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_19 = SubjectCurriculum(grade=4, subject_id="G4-19",
    subject_title="range and seq", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(count (range 5))",
            expected=5,
            concept_phrase="counting elements in a range",
            question_what="the count of range 0..4",
            goal_text="count how many numbers are generated by a range from 0 to 4",

            scenario=(
                "Sable asked the pitcher in the meadow to produce a run of "
                "stones starting from zero up to but not including five. The "
                "stones would appear one by one as a lazy sequence."
            ),
            need=(
                "She needed to know how many stones the range would generate "
                "before she started placing them."
            ),
            mapping=(
                '`range` produces a lazy sequence of integers from zero; `count` walks it and tallies. {drawn.a} integers from zero through four yield a count of five.'
            ),
            resolution=(
                "The REPL returned the count of stones the range produced, "
                "one per integer generated. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(first (range 1 100))",
            expected=1,
            concept_phrase="getting the first element of a range",
            question_what="the first of range 1..99",
            goal_text="get the first element of a range starting at 1 and ending before 100",

            scenario=(
                "Korvus set the pitcher at the hilltop to pour a long run "
                "of stones from one up to ninety-nine. He needed only the "
                "very first stone without letting the whole run pour out."
            ),
            need=(
                "He needed `first` to lift just the leading stone from the "
                "lazy range without forcing all ninety-nine to generate."
            ),
            mapping=(
                "`first` on a lazy range produces only the initial element. "
                "The range starts at one; `first` lifts that stone and the "
                "rest of the sequence stays ungenerated."
            ),
            resolution=(
                "The REPL returned the first stone of the range without "
                "generating the rest. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_20 = SubjectCurriculum(grade=4, subject_id="G4-20",
    subject_title="Collection vs sequence", fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(count (seq [1 2 3]))",
            expected=3,
            concept_phrase="creating a sequence from a vector and counting",
            question_what="the count of seq over a vector",
            goal_text="convert a vector containing 1, 2, and 3 to a sequence and count its elements",

            scenario=(
                "Caw had a three-stone vector-pile at the village pitcher. "
                "She passed it through `seq` to get a chain view, then asked "
                "`count` to tally the stones in that view."
            ),
            need=(
                "She needed to confirm that converting a pile to a chain "
                "view did not lose or add any stones during the conversion."
            ),
            mapping=(
                "`seq` turns any collection into a sequential chain view. "
                "`count` then tallies the chain. The vector's stones are "
                "unchanged; the chain holds the same the elements."
            ),
            resolution=(
                "The REPL returned the count of the chain view, same as "
                "the original pile's stone total. (with {drawn.a} folded in)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(seq [])",
            expected=None,
            concept_phrase="creating a sequence from an empty vector",
            question_what="the result of seq on an empty vector",
            goal_text="convert an empty vector to a sequence",

            scenario=(
                "Sable tried to thread an empty vector-pile through `seq` "
                "at the orchard pitcher — no stones in the pile, nothing "
                "to chain into a sequence."
            ),
            need=(
                "She needed the REPL to show what `seq` returns when given "
                "a completely empty collection to chain."
            ),
            mapping=(
                "`seq` on an empty collection cannot form a chain; it returns "
                "nil to signal there is nothing to sequence. An empty pile "
                "yields no chain at all."
            ),
            resolution=(
                "The REPL returned nil, confirming no chain could form from "
                "an empty pile."
            ),
            tags=("story",),
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
    print(f"grade-4 crow-pitcher smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
