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
wrote {form_display} on a slate and asked {milkmaid_phrase}, {emo_boastful} to write the
form into the REPL so they could confirm it together."""),

    SubplotTemplate("""\
{milkmaid_phrase}, {emo_proud}, declared the collection plain. {farmer_phrase}
wrote {form_display} on a slate {place}, calmly. "It's not about plain
or fancy," {farmer_he_she_cap} said. "It's about whether the runtime
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
            concept_phrase="a vector of several numbers",
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
                "The REPL handed back the three-compartment basket, items sitting "
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
            scenario=(
                "The milkmaid set down a market-basket frame — the wood and weave ready, "
                "but no compartments yet, no slots holding anything."
            ),
            need=(
                "She needed to represent an empty collection: a basket that existed as a container "
                "but held nothing inside, ready to be filled."
            ),
            mapping=(
                "An empty vector literal is the frame itself: `[]` is a vector with zero compartments, "
                "a structure that exists but carries no items."
            ),
            resolution=(
                "The REPL handed back an empty basket — the frame intact, the slots all bare, "
                "nothing inside but the promise of space."
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
                "The milkmaid reached for the market-basket and placed two labeled jars inside: "
                "one compartment held a string marked 'a', another held a string marked 'b'."
            ),
            need=(
                "She needed a literal sequence of two strings — ordered, distinct, sitting in "
                "their own compartments of the same basket."
            ),
            mapping=(
                "A vector of strings is the basket holding string values: two compartments, "
                "each holding exactly one string, in the order they were placed."
            ),
            resolution=(
                "The REPL handed back the two-compartment basket — the strings 'a' and 'b' sitting "
                "exactly where they belonged, untouched and ordered."
            ),
            tags=("story",),
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
            scenario=(
                "The milkmaid stood before a market-basket with three compartments, each holding a "
                "different price of dairy: the first held butter at 10 coins, the second skim at 20 coins, "
                "the third cream at 30 coins."
            ),
            need=(
                "She needed to look into the first compartment without opening the others, to see "
                "exactly what price sat at position zero."
            ),
            mapping=(
                "The `nth` function is reaching into the basket at a specific compartment: "
                "`(nth [10 20 30] 0)` reaches into position 0 and pulls out what sits there."
            ),
            resolution=(
                "The REPL handed back the value 10 — the exact price that sat in the "
                "first compartment, untouched and clear."
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
                "The market-basket still held three compartments of dairy prices: butter at position zero, "
                "skim at position one, cream at position two."
            ),
            need=(
                "She needed to reach into the third compartment — the one at position 2 — and see "
                "what price the cream commanded."
            ),
            mapping=(
                "`nth` is the hand reaching into a numbered compartment: `(nth [10 20 30] 2)` reaches "
                "past the first two slots to the third one and pulls out its value."
            ),
            resolution=(
                "The REPL handed back 30 — the cream price sitting exactly at position 2 of the basket."
            ),
            tags=("story",),
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
            scenario=(
                "The milkmaid carried a market-basket holding two items: the number 1 in the first compartment, "
                "the number 2 in the second. She paused at the roadside, thinking to add one more item."
            ),
            need=(
                "She needed to add the number 3 to the end without disturbing the original two items — "
                "a fresh basket with one more compartment, the new item safely tucked at the end."
            ),
            mapping=(
                "The `conj` operation is reaching into the basket and adding a new compartment: "
                "the form creates a new basket with all several items, the 3 now at the end."
            ),
            resolution=(
                "The REPL handed back a new basket with three compartments: 1, 2, and 3 — the original "
                "two items untouched, the new one added at the end."
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
                "The milkmaid set down an empty market-basket — no compartments yet, just the frame waiting "
                "to be filled. She thought of the hare, fast and proud, and decided to mark the basket with "
                "the keyword :hare."
            ),
            need=(
                "She needed to add the keyword :hare to the empty basket, creating a new basket with one "
                "compartment holding that keyword."
            ),
            mapping=(
                "`conj` adds to even an empty basket: `(conj [] :hare)` takes the empty frame and creates "
                "a fresh basket with exactly one compartment, holding the keyword :hare."
            ),
            resolution=(
                "The REPL handed back a basket with one compartment — the keyword :hare sitting alone in "
                "the first and only slot."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_04 = SubjectCurriculum(grade=4, subject_id="G4-04",
    subject_title="List literal", fable="milkmaid",
    examples=[
        SubjectExample(
            form="'(1 2 3)",
            expected=[1,2,3],
            concept_phrase="a list literal",
            question_what="the list oseveral numbersrs",
            goal_text="create a list containing 1, 2, and 3",
            scenario=(
                "The milkmaid spoke aloud her shopping list to herself as she walked the market road: one butter, "
                "two creams, three wheels of cheese. She muttered the list in order, each item marked in her mind."
            ),
            need=(
                "She needed to capture this list as a complete ordered sequence several itemsms in the exact order "
                "she had spoken them, bound together as a single whole."
            ),
            mapping=(
                "A list literal is the milkmaid's spoken list captured in form: a quoted listseveral itemstems in order, "
                "a sequence bound together by quoting, ready to be carried as one bundle."
            ),
            resolution=(
                "The REPL handed back the list witseveral items items in order — the sequence the milkmaid had spoken "
                "now captured as a data structure, unchanged — 3."
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
                "The milkmaid had finished her market day and spoken all her items into a list. Now she stood in the "
                "town square with nothing left to say — no items to mark, no list to recite."
            ),
            need=(
                "She needed to represent that emptiness: an ordered sequence with no items at all, a list frame "
                "that was open and bare."
            ),
            mapping=(
                "An empty list literal is silence itself: `'()` is a list with nothing in it — a sequence bound by "
                "quotes but holding zero items."
            ),
            resolution=(
                "The REPL handed back an empty list — the bare frame, the silence, the list that held nothing."
            ),
            tags=("story",),
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
            scenario=(
                'The milkmaid had spoken a list aloud: the counts. But then she realized she had forgotten the starting point — the zero from which the count should begin. She needed to add it to the front.'
            ),
            need=(
                'She needed to place the 0 at the very beginning of the list, so the sequence would read: zero, the counts — as if she had spoken them in the correct order from the start.'
            ),
            mapping=(
                "The `cons` operation is reaching to the front of the list and adding an item there: "
                "the cons form creates a new list with 0 at the head and the rest following in order."
            ),
            resolution=(
                'The REPL handed back a list of several items in order — zero at the front, then the counts flowing behind it, exactly as she had meant to speak them — 3.'
            ),
            tags=("story",),
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
            scenario=(
                "The milkmaid stood at the village square, watching a race between a hare and a tortoise. "
                "The hare had won once, but the tortoise had persisted. She wanted to mark their victories in a ledger."
            ),
            need=(
                "She needed a way to bind each name to its count: the hare to 1, the tortoise to 2, keeping them "
                "together in one record that matched names to numbers."
            ),
            mapping=(
                "A map literal is the ledger: `{:hare 1 :tortoise 2}` binds each keyword to a value. The map is a "
                "market-basket with labeled compartments — one for the hare's score, one for the tortoise's."
            ),
            resolution=(
                "The REPL handed back the map with both bindings intact — the hare bound to 1, the tortoise to 2, "
                "their rivalry recorded in the basket's labeled slots."
            ),
            tags=("story",),
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
            scenario=(
                "The milkmaid carried a market-basket with two labeled compartments: one marked :a held the value 1, "
                "another marked :b held the value 2. She arrived at the buyer's stall wanting to know what sat in "
                "the :a compartment."
            ),
            need=(
                "She needed to look into the labeled slot without opening the entire basket, reaching only for the "
                "compartment marked :a and pulling out what sat inside."
            ),
            mapping=(
                "The `get` function is looking into a labeled compartment: the lookup form reaches for the "
                "slot labeled :a and returns what is bound there."
            ),
            resolution=(
                "The REPL handed back the value 1 — what the :a label had pointed to all along, now in her hand."
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
                "The milkmaid carried a basket with only one labeled compartment: :a held the value 1. But when she "
                "arrived at the stall, the buyer asked about a label called :missing, which had no compartment."
            ),
            need=(
                "She needed to reach for :missing, find nothing, but have a backup answer ready — a default value to "
                "hand over when the label did not exist in the basket."
            ),
            mapping=(
                "`get` with a default is a safe reach: the lookup form searches for the absent label, finds "
                "nothing, and hands back the prepared default value instead — a promise kept even when the label is absent."
            ),
            resolution=(
                "The REPL handed back the fallback keyword — the prepared default answer, proving that a missing label need not "
                "crash the form, only return what the milkmaid had prepared."
            ),
            tags=("story",),
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
            scenario=(
                "The milkmaid held a market-basket with one labeled compartment: :a held the value 1. She stood at the "
                "buyer's stall, ready to add a second compartment labeled :b to hold the value 2."
            ),
            need=(
                "She needed a new basket keeping the original :a binding while adding a fresh :b compartment. "
                "The old basket would remain untouched; a new one would carry both bindings."
            ),
            mapping=(
                "The `assoc` operation builds a new basket: the assoc form takes the original basket and creates "
                "a fresh one with the :a binding intact and a new :b compartment added. The old basket stays as it was."
            ),
            resolution=(
                "The REPL handed back a new basket with both bindings — :a still pointing to 1, :b now pointing to 2, "
                "the original basket sitting untouched behind."
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
                "The milkmaid's first basket had been marked :a and held the value 1. But after the day's business, "
                "she needed the :a compartment to hold a new value instead — 99, a much larger prize."
            ),
            need=(
                "She needed to change the binding without destroying the basket itself. A new basket would emerge with "
                "the same label :a but a different value inside — 99 where 1 had been."
            ),
            mapping=(
                "`assoc` can change a binding too: the form takes the original basket and creates a fresh "
                "one where :a now points to 99. The label stays; the value changes. The old basket remains, untouched."
            ),
            resolution=(
                "The REPL handed back a new basket with :a now binding to 99 — the label unchanged, the compartment's "
                "contents transformed. The original basket, still holding 1, sat safely behind."
            ),
            tags=("story",),
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
            scenario=(
                "The milkmaid's market-basket held two labeled compartments: one marked :a held 1, another marked :b "
                "held 2. But the buyer no longer needed the :a label — the milkmaid decided to leave that compartment out."
            ),
            need=(
                "She needed to create a fresh basket that dropped the :a compartment entirely while keeping the :b binding "
                "intact. The new basket would have only one label, only one binding."
            ),
            mapping=(
                "The `dissoc` operation removes a compartment: the form creates a new basket with :a's "
                "label and binding stripped away. The :b binding stays. The old basket remains, still holding both labels."
            ),
            resolution=(
                "The REPL handed back a new basket with only the :b binding — the :a label and its value 1 gone, "
                "leaving only what the milkmaid intended to keep."
            ),
            tags=("story",),
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
            scenario=(
                "The milkmaid stood before a market-basket that the farmer had labeled with three distinct tags: :a, :b, "
                "and :c. Each label marked a different compartment inside. She wondered: how many labels in all?"
            ),
            need=(
                "She needed to read all the labels on the outside of the basket without opening it, count them, and report "
                "how many there were. The labels themselves mattered, not what sat inside."
            ),
            mapping=(
                "The `keys` function reads the labels: it pulls all the label-names from the basket as a separate list. "
                "Then `count` tallies them. The form `(count (keys {:a 1 :b 2 :c 3}))` counts the labels: :a, :b, :c — three."
            ),
            resolution=(
                "The REPL handed back the number 3 — the count of distinct labels on the basket, the three compartments that "
                "the farmer had marked."
            ),
            tags=("story",),
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
            scenario=(
                "The milkmaid carried three distinct prices in her mind: 1 coin for butter, 2 coins for skim, 3 coins for "
                "cream. These were all the unique prices at the market — no duplicates, all different."
            ),
            need=(
                "She needed a collection that guaranteed no repeats — a way to hold these three distinct values and know "
                "that if someone tried to add 1 again, the collection would reject the duplicate and stay at three unique items."
            ),
            mapping=(
                "A set literal is uniqueness itself: `#{1 2 3}` holds three distinct items. A set never keeps duplicates — it "
                "is a market-basket that refuses to let the same price be recorded twice."
            ),
            resolution=(
                "The REPL handed back a set with three unique elements — count it, and the answer is 3. Uniqueness enforced, "
                "duplication rejected."
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
                "The milkmaid tried to record the price 1 three times over — once as she heard it, once as she wrote it down, "
                "once as she repeated it aloud. But the set refused to store the duplicate."
            ),
            need=(
                "She needed to understand that a set, by its nature, holds only unique items. Try to add 1 three times, and the "
                "set remains a set of one — the single value 1, alone, the others rejected as redundant."
            ),
            mapping=(
                "A set collapses duplicates: `#{1 1 1}` is a set that will not permit the same item three times. The set sees 1 "
                "once and ignores the rest. Count the unique elements, and the answer is 1 — just the single distinct value."
            ),
            resolution=(
                "The REPL handed back a set with one unique element — the number 1, stripped of its duplicates. Count it: 1."
            ),
            tags=("story",),
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
            scenario=(
                "The milkmaid had gathered the distinct prices at the market: 1 coin, 2 coins, 3 coins. These were the prices "
                "she knew. A buyer approached and asked: does this market carry milk for 2 coins?"
            ),
            need=(
                "She needed to check whether 2 belonged to the set of known prices without opening the entire set. A yes-or-no "
                "answer would suffice: the price 2 was or was not in her set."
            ),
            mapping=(
                "The `contains?` function asks: is this item in the set? `(contains? #{1 2 3} 2)` asks whether 2 belongs. The "
                "set answers true — yes, 2 is among the three prices."
            ),
            resolution=(
                "The REPL handed back true — the price 2 existed in the milkmaid's set of prices. The buyer could find milk at "
                "that rate."
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
                "The milkmaid's set of known prices still held 1, 2, and 3 coins. Another buyer came asking: does the market "
                "have milk for 4 coins?"
            ),
            need=(
                "She needed to check whether 4 was in her known set. But 4 did not belong — the market had no such price. A "
                "no-or-false answer was the honest reply."
            ),
            mapping=(
                "`contains?` searches the set: the form asks if 4 belongs to the set of 1, 2, and 3. The set "
                "answers false — 4 is not among the known prices."
            ),
            resolution=(
                "The REPL handed back false — the price 4 did not exist in the milkmaid's set. She would have to say no to the buyer."
            ),
            tags=("story",),
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
            goal_text="count the elements in a vector containing these numbers",
            scenario=(
                "The milkmaid stood before a market-basket with five compartments, each numbered: "
                "1, 2, 3, 4, 5. She wondered how many slots the basket held in total."
            ),
            need=(
                "She needed to know the total number of compartments — not what sat inside them, "
                "but the count of slots themselves."
            ),
            mapping=(
                "The `count` function tallies the compartments: applied to a five-element vector, it counts "
                "the slots in the basket and returns the total number of items."
            ),
            resolution=(
                "The REPL handed back the number 5 — the exact count of compartments in the basket, "
                "no more, no less."
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
                "The milkmaid's ledger held two labeled entries: one marked :a bound to the value 1, "
                "another marked :b bound to the value 2."
            ),
            need=(
                "She needed to count how many bindings the ledger held — how many labeled compartments "
                "existed in total."
            ),
            mapping=(
                "The `count` function tallies the bindings: applied to a two-entry map, it counts the "
                "labeled compartments and returns the total number of entries."
            ),
            resolution=(
                "The REPL handed back 2 — the count of key-value pairs in the map."
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
                "The milkmaid held a set of three distinct prices she had heard that day: :a, :b, and :c — "
                "each unique, none repeated."
            ),
            need=(
                "She needed to count how many unique prices the set held — the total of distinct items "
                "without regard to their value."
            ),
            mapping=(
                "The `count` function tallies unique elements: applied to a three-element set, it counts "
                "the distinct items and returns the total."
            ),
            resolution=(
                "The REPL handed back 3 — the count of unique elements in the set."
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
                "The milkmaid had learned the tale of the tortoise — a creature slow and steady, "
                "whose name carried eight letters: t-o-r-t-o-i-s-e."
            ),
            need=(
                "She needed to count how many letters made up the word 'tortoise' — the total "
                "length of the string character by character."
            ),
            mapping=(
                "The `count` function tallies string characters: `(count \"tortoise\")` counts each "
                "letter in the sequence and returns eight."
            ),
            resolution=(
                "The REPL handed back 8 — the length of the string, one character at a time."
            ),
            tags=("story",),
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
            scenario=(
                "The milkmaid looked at a market-basket she had set down — it was just the frame, "
                "no compartments, no items inside. She wondered: is this basket empty?"
            ),
            need=(
                "She needed a yes-or-no answer: does the basket hold nothing? Is it truly bare?"
            ),
            mapping=(
                "The `empty?` function checks if a collection has no items: the form asks whether "
                "the basket is void, and the answer is true."
            ),
            resolution=(
                "The REPL handed back true — the basket was indeed empty, confirmed."
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
                "The milkmaid now looked at a different basket — this one held the number 1 in "
                "its first compartment. She asked: is this basket empty?"
            ),
            need=(
                "She needed to verify: does the basket hold anything? Is there at least one item inside?"
            ),
            mapping=(
                "The `empty?` function checks if a collection has items: the form asks whether "
                "the basket is void — but it holds 1, so the answer is false."
            ),
            resolution=(
                "The REPL handed back false — the basket held the number 1, so it was not empty."
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
                "The milkmaid spoke no words — her lips were sealed, her breath held silent. "
                "She wondered: is this empty string truly bare?"
            ),
            need=(
                "She needed to check whether the string held no characters — whether silence itself "
                "was emptiness."
            ),
            mapping=(
                "The `empty?` function checks strings too: applied to a string with zero characters, it "
                "asks whether that string is void, and the answer is true."
            ),
            resolution=(
                'The REPL handed back true — the empty string was indeed empty, confirmed (with `` as the input value) (with `` as the input value).'
            ),
            tags=("story",),
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
            scenario=(
                "The milkmaid held a market-basket with three compartments: the first held 10, "
                "the second held 20, the third held 30. She reached toward the basket, thinking "
                "of the very first compartment."
            ),
            need=(
                "She needed to pull out only the item from the first slot, leaving the rest untouched "
                "in the basket."
            ),
            mapping=(
                "The `first` function reaches into the basket at the beginning: `(first [10 20 30])` "
                "pulls the value from the first compartment and returns it."
            ),
            resolution=(
                "The REPL handed back 10 — the item that sat in the very first slot."
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
                "The milkmaid still held the market-basket with three compartments: first 10, second 20, "
                "third 30. Now she turned her thoughts to the very end — the final compartment."
            ),
            need=(
                "She needed to reach to the back of the basket and pull out the item in the last slot, "
                "the rightmost compartment."
            ),
            mapping=(
                "The `last` function reaches to the end: applied to a three-item basket, it reaches past all "
                "the middle slots and returns what sits in the final compartment."
            ),
            resolution=(
                "The REPL handed back 30 — the item that occupied the very last slot."
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
                "The milkmaid held her three-compartment basket: 10, 20, 30. She plucked out the "
                "first item (10), leaving 20 and 30. Now she wondered: how many compartments remain?"
            ),
            need=(
                "She needed to count the items left after removing the first — the tail of the basket "
                "now held two compartments instead of three."
            ),
            mapping=(
                "The `rest` function removes the first, leaving the rest: `(rest [10 20 30])` creates "
                "a new sequence with just 20 and 30. Then `count` tallies the remainder."
            ),
            resolution=(
                "The REPL handed back 2 — the count of items remaining after the first had been removed."
            ),
            tags=("story",),
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
                "contents of a market list — several elements in order — through the "
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
                "The REPL returned the fresh vector with alseveral elementsts — the "
                "list had passed through the strainer and arrived in its new shape, "
                "intact — 3."
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
                "The milkmaid held a basket wiseveral itemsems: 1, 2, 2, 3 — but two of them were the same price. "
                "She held a milk-strainer over an empty set-pail, preparing to pour the basket's contents through."
            ),
            need=(
                "She needed to pass the vector through the strainer rule, which would reject the duplicate 2 and "
                "allow only unique prices through to the fresh pail."
            ),
            mapping=(
                "The `into` function with a set as target pours through a uniqueness-strainer: the form "
                "pours each element into the set, which rejects duplicates."
            ),
            resolution=(
                "The REPL handed back a set with three unique elements — the duplicate 2 had been strained out, leaving "
                "only 1, 2, and 3 as distinct prices."
            ),
            tags=("story",),
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
            scenario=(
                "The milkmaid held her original market-basket with the compartment labeled :a holding "
                "the value 1. She called assoc to create a new basket with :a bound to 99 instead. But then "
                "she looked back at the first basket."
            ),
            need=(
                "She needed proof that the original basket had never changed — that assoc had created "
                "a fresh one, leaving the old one untouched."
            ),
            mapping=(
                "Immutability means assoc creates a new basket: `(assoc m :a 99)` builds a fresh basket "
                "with the new binding, but the original `m` stays as it was."
            ),
            resolution=(
                "The REPL handed back the original map still binding :a to 1 — untouched, unchanged, "
                "proof that a new creation had been made instead."
            ),
            tags=("story",),
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
            scenario=(
                "The milkmaid carried two baskets down the market road: one was a market-basket with "
                "compartments holding 1, 2, and 3. The other was a list she had spoken aloud in the same order. "
                "She wondered: are they the same?"
            ),
            need=(
                "She needed to know whether the contents and order were identical, regardless of whether "
                "one was a compartmented basket and the other a spoken list."
            ),
            mapping=(
                "Equality checks the contents, not the container type: `(= [1 2 3] '(1 2 3))` compares the "
                "sequences — both hold the same items in the same order, so they are equal."
            ),
            resolution=(
                "The REPL handed back true — the baskets held the same truth, even though their shapes differed."
            ),
            tags=("story",),
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
            scenario=(
                "The milkmaid walked the market road, counting off each milestone: 0, 1, 2, 3, 4. "
                "The range created a virtual basket with each number in order. She wondered: how many milestones "
                "had she passed?"
            ),
            need=(
                "She needed to count the numbers the range generated — from 0 up to but not including 5, "
                "a total count of the milestone sequence."
            ),
            mapping=(
                "The `range` function generates a sequence of numbers, and `count` tallies them: "
                "`(count (range 5))` generates 0 through 4 and counts the items — five milestones."
            ),
            resolution=(
                "The REPL handed back 5 — the number of integers in the range from 0 to 4, inclusive."
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
                "The milkmaid set out on a long road from milestone 1 to 99. The range generated "
                "a virtual basket of all the milestones: 1, 2, 3, ... up to 99. She stood at the beginning."
            ),
            need=(
                "She needed to know what the first milestone was — the very start of the long journey, "
                "where the range began."
            ),
            mapping=(
                "The `first` function reaches to the beginning: applied to a range starting at 1 and stopping before 100, "
                "it generates the sequence and pulls the first item from it."
            ),
            resolution=(
                "The REPL handed back 1 — the first milestone, where the range began its count."
            ),
            tags=("story",),
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
            scenario=(
                "The milkmaid held a market-basket with three compartments: 1, 2, and 3. She applied "
                "the seq function to treat the basket as a flowing stream — a sequence ready to pour through "
                "a strainer. Now she wondered: how many items flowed?"
            ),
            need=(
                "She needed to count the items in the resulting sequence — to tally the stream as it "
                "flowed from the basket."
            ),
            mapping=(
                "The `seq` function views the basket as a sequence: `(seq [1 2 3])` creates a lazy sequence "
                "from the vector. Then `count` tallies the items."
            ),
            resolution=(
                "The REPL handed back 3 — the count of elements in the sequence, the same as the basket's compartments."
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
                "The milkmaid held an empty basket — just the frame, no compartments. She applied the seq function "
                "to turn it into a stream. But there was nothing to flow."
            ),
            need=(
                "She needed to understand what happens when a sequence is asked to flow from an empty source — "
                "what does the runtime return?"
            ),
            mapping=(
                "The `seq` function on an empty collection returns nil: applied to an empty vector, it tries to create "
                "a sequence from nothing, and the result is empty — no stream at all."
            ),
            resolution=(
                "The REPL handed back nil — no sequence could flow from an empty basket, so the runtime returned nothing."
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
    print(f"grade-4 tortoise-hare smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
