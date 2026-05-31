"""Grade 4 — collections (Layer 4). Through the Boy-who-cried-Wolf
fable.

Subplot lens: pebbles in a basket, sheep counted at sundown, marks on
the elder's slate, names in the village ledger — collections of small
things the elder lays out so the shepherd can write the form that
manipulates them. Polarity preserved: the elder lays things out and
asks for the form; the shepherd writes it (no boasting required, just
the runtime).
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.boy_wolf.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.boy_wolf._metaphor_pools import (
    _BASKET_SUBPLOTS, _SIEVE_SUBPLOTS,
)
from mmllm.aesop.curriculum.boy_wolf._goals import GOALS, get_goal


# NOTE: these templates avoid putting both {form_display} AND a "the
# form X" {concept_phrase} in close proximity (the duplication produces
# ungrammatical "the form X described the form X" prose when
# concept_phrase is "the form X" verbatim — see SKILL doc #11).
_COLL_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [
    SubplotTemplate("""\
{elder_phrase} had been laying out a small collection {place} —
pebbles, sheep counted at sundown, marks on the slate, whatever the
day produced. {elder} wrote {form_display} on a flat board and asked
{shepherd_phrase} to write the form into the REPL so the watchhouse could
confirm it together."""),

    # NOTE (boy-wolf polish, hand-audit pass): the second quoted
    # utterance was missing its closing `\"`. Closed below.
    SubplotTemplate("""\
{shepherd_phrase}, {emo_proud}, declared the collection plain.
{elder_phrase} wrote {form_display} on a slate {place}, calmly. "It's
not about plain or fancy," {elder_he_she} said. "It's about whether
the runtime agrees with what we think we're describing.\""""),
]


def _ex(form, expected, concept, what, goal=None,
        scenario="", need="", mapping="", resolution="",
        tags=()):
    canon = GOALS.get(form, {})
    if all([scenario, need, mapping, resolution]) and "story" not in tags:
        tags = tuple(tags) + ("story",)
    return SubjectExample(
        form=form, expected=expected,
        concept_phrase=canon.get("concept", concept),
        question_what=canon.get("what", what),
        goal_text=goal if goal is not None else get_goal(form, concept, what),
        scenario=scenario, need=need, mapping=mapping, resolution=resolution,
        tags=tags,
    )
_PLAN_G4 = _PLAN_POOL + (
    "I write the collection literal and let the REPL evaluate.",
    "I use the appropriate access function on the collection.",
)


G4_01 = SubjectCurriculum(grade=4, subject_id="G4-01",
    subject_title="Vector literal", fable="boy-wolf",
    examples=[
        _ex("[1 2 3]", [1,2,3],   "the vector [1 2 3]",   "the value [1 2 3]"),
        _ex("[]",      [],         "the empty vector []",  "the empty vector",
            scenario=(
                "Carol laid out the wool-basket at the watchhouse, freshly "
                "emptied and ready. She showed Tom the basket's shape before "
                "adding a single fleece."
            ),
            need=(
                "The village wanted to describe the empty collection itself — "
                "the basket's shape and emptiness preserved as a form, not "
                "just the idea of it."
            ),
            mapping=(
                "The empty vector `[]` writes down the form of a collection "
                "with nothing inside it — the basket exists, but holds no fleeces."
            ),
            resolution=(
                "the call returned the empty vector, capturing the basket's state before the day's shearing began. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record."
            )),
        _ex("[\"a\" \"b\"]", ["a","b"], "the vector of strings", "the vector [\"a\" \"b\"]",
            scenario=(
                "Carol carved two wool-dye labels onto slate shards and laid "
                "them in a wool-basket side by side: 'a' on the left, 'b' on "
                "the right, ready to be sorted into pouches."
            ),
            need=(
                "The village needed a form that gathered the two labels in "
                "order so the dyers could read them aloud as a group."
            ),
            mapping=(
                "The vector `[\"a\" \"b\"]` writes down two strings in sequence, "
                "preserving the left-to-right order and marking them as a "
                "grouped collection the `count` form or `nth` form can address."
            ),
            resolution=(
                "the call returned the pair of strings, and the dyers read off 'a' then 'b' from the basket as the REPL had settled it."
            )),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_02 = SubjectCurriculum(grade=4, subject_id="G4-02",
    subject_title="nth — vector access", fable="boy-wolf",
    examples=[
        _ex("(nth [10 20 30] 0)", 10, "the expression (nth [10 20 30] 0)", "the value at index 0",
            scenario=(
                "Carol lined up three bundles of fleece in the basket, "
                "marking them by weight: 10 at the left, 20 in the middle, 30 at "
                "the right. Tom wanted the leftmost bundle's weight."
            ),
            need=(
                "The form needed to reach in and pull the first bundle's count "
                "without disturbing the arrangement."
            ),
            mapping=(
                "`nth` walks into the basket and counts from the left: position "
                "0 is the first item. It reaches in and returns the item at that "
                "spot without changing the basket."
            ),
            resolution=(
                'the call returned 10, the weight Carol had marked on the leftmost bundle. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
        _ex("(nth [10 20 30] 2)", 30, "the expression (nth [10 20 30] 2)", "the value at index 2",
            scenario=(
                "Carol's three bundles still lay in the basket: 10, 20, 30 from "
                "left to right. Tom now wanted the rightmost bundle's weight, "
                "the third one in the line."
            ),
            need=(
                "The form had to count over and reach the third position, "
                "starting the count from position 0 at the left."
            ),
            mapping=(
                "`nth` counts from the left starting at 0: position 0 is the "
                "first, position 1 is the second, position 2 is the third. The "
                "form walks there and returns the item."
            ),
            resolution=(
                'the call returned 30, the weight at the rightmost position in the basket. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'
            )),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_03 = SubjectCurriculum(grade=4, subject_id="G4-03",
    subject_title="conj — append to vector", fable="boy-wolf",
    examples=[
        _ex("(conj [1 2] 3)",       [1,2,3],   "the expression (conj [1 2] 3)",      "[1 2] with 3 conjed",
            scenario=(
                "Carol held a wool-basket with two fleeces already sorted: "
                "weight 1 and weight 2 tucked inside. A third fleece, weight 3, "
                "arrived at the door, fresh from shearing."
            ),
            need=(
                "The basket needed to keep both the old fleeces in order and "
                "add the new one to the end, returning a fresh basket without "
                "changing the original."
            ),
            mapping=(
                "`conj` adds an item to the end of the vector. It takes the old "
                "basket and the new fleece, returning a new arrangement with the "
                "fresh item appended, the old basket untouched."
            ),
            resolution=(
                "the call returned the new basket with three fleeces in the new arrangement, while Carol's original remained unchanged. Tom chalked {drawn.a} on the watchhouse notice, and the morning record stood for the next shepherd to read."
            )),
        _ex("(conj [] :wolf)",      [":wolf"], "the expression (conj [] :wolf)",     "the empty vector with :wolf conjed",
            scenario=(
                "Carol brought an empty wool-basket to the fold. Tom wanted "
                "to add a single marker, the keyword `:wolf`, to track which "
                "fleeces came from the wolf-shearing."
            ),
            need=(
                "The form had to write a basket with just that one marker, "
                "growing from empty to a one-item collection."
            ),
            mapping=(
                "`conj` on an empty basket `[]` with the keyword `:wolf` "
                "adds that keyword as the first and only item, growing the "
                "empty form into a one-element vector."
            ),
            resolution=(
                'the call returned a basket with one item, the marker `:wolf` nested inside, ready for the flock count. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'
            )),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_04 = SubjectCurriculum(grade=4, subject_id="G4-04",
    subject_title="List literal", fable="boy-wolf",
    examples=[
        _ex("'(1 2 3)", [1,2,3], "the list '(1 2 3)", "the list of three numbers",
            scenario=(
                "Carol strung three markers onto a cord: 1, then 2, then 3 in "
                "a row. She tied a knot at each end, creating a chain ready to "
                "pass from hand to hand at the fold."
            ),
            need=(
                "The form had to describe the cord and its markers as a "
                "sequence that could be fed through other operations."
            ),
            mapping=(
                "A quoted list writes down three numbers strung in a rope-like "
                "sequence. The apostrophe stops evaluation, keeping the numbers "
                "as a list shape instead of trying to call the first as a function."
            ),
            resolution=(
                'the call returned the list with three items in sequence, ready to be counted or passed through another form. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'
            )),
        _ex("'()",      [],       "the empty list",     "the empty list",
            scenario=(
                "Carol held an empty cord at the watchhouse, tied at both ends "
                "but with no markers strung onto it yet. She wanted to show Tom "
                "what an empty sequence looked like."
            ),
            need=(
                "The form had to express the cord itself without any items on it, "
                "so the townsfolk could understand the shape of an empty list."
            ),
            mapping=(
                "The quoted empty list `'()` describes a rope-like sequence with "
                "no items, parentheses wrapped in the quote to hold its shape."
            ),
            resolution=(
                'the call returned the empty list, and the REPL showed the cord with no markers strung. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'
            )),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_05 = SubjectCurriculum(grade=4, subject_id="G4-05",
    subject_title="cons — prepend to seq", fable="boy-wolf",
    examples=[
        _ex("(cons 0 '(1 2 3))", [0,1,2,3], "the expression (cons 0 '(1 2 3))", "the seq with 0 cons'd at the front",
            scenario=(
                "Carol held a cord with three markers: 1, 2, 3 in sequence. A new "
                "marker, 0, arrived that needed to go at the very front, before all "
                "the rest, tied on first."
            ),
            need=(
                "The form had to thread the new marker at the head of the cord "
                "and return a fresh sequence with zero now leading, the old cord "
                "unbroken behind it."
            ),
            mapping=(
                "`cons` locks the new item at the front. It takes the item and "
                "the sequence, stitching the item to the head and keeping the "
                "rest of the rope intact behind it."
            ),
            resolution=(
                'the call returned a new sequence with 0 at the front and 1, 2, 3 following — the original cord preserved, the new pattern complete. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'         )),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_06 = SubjectCurriculum(grade=4, subject_id="G4-06",
    subject_title="Map literal", fable="boy-wolf",
    examples=[
        _ex("{:wolf 1 :flock 2}", {":wolf": 1, ":flock": 2},
            "the map {:wolf 1 :flock 2}", "the map with two entries",
            scenario=(
                "Carol stitched a wool-basket with two named pouches inside: one "
                "labeled `:wolf` holding 1 fleece from the south pasture, another "
                "`:flock` holding 2 from the north morning shearing."
            ),
            need=(
                "The form had to describe the basket's internal structure — "
                "which pouch held which count — so Tom could reference them by name."
            ),
            mapping=(
                "The map `{:wolf 1 :flock 2}` writes down two key-value pairs: "
                "the key `:wolf` mapped to 1, and `:flock` mapped to 2. It freezes "
                "the basket's labeled arrangement in a form."
            ),
            resolution=(
                'the call returned the map showing both pouches and their counts, ready for the `get` form to pull from a single named pouch. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'
            )),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_07 = SubjectCurriculum(grade=4, subject_id="G4-07",
    subject_title="get — map lookup", fable="boy-wolf",
    examples=[
        _ex("(get {:a 1 :b 2} :a)", 1, "the expression (get {:a 1 :b 2} :a)", "the value at :a",
            scenario=(
                "Carol's wool-basket held two labeled pouches: `:a` with 1 fleece "
                "and `:b` with 2. Tom wanted the count from the `:a` pouch alone."
            ),
            need=(
                "The form had to reach into the basket, find the `:a` pouch by "
                "name, and return only its count without spilling the whole basket."
            ),
            mapping=(
                "`get` takes the map and the key name, reaching into the basket "
                "and pulling out the value paired with that key. With `:a` as the "
                "key, it finds the `:a` pouch and returns its contents."
            ),
            resolution=(
                'the lookup returned the result — the count from the `:a` pouch — and the rest of the basket stayed settled. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'         )),
        _ex("(get {:a 1} :missing :default)", ":default",
            "the expression (get {:a 1} :missing :default)", "the default value when key missing",
            scenario=(
                "Carol's basket held one pouch labeled `:a` with 1 fleece. Tom "
                "asked for a pouch that didn't exist in the basket."
            ),
            need=(
                "The form had to check if the pouch existed, and if not, return "
                "a safe fallback answer rather than nil."
            ),
            mapping=(
                "`get` with three arguments takes the map, the key to look for, "
                "and a fallback value. When the key isn't found in the basket, "
                "it returns the fallback instead of nil."
            ),
            resolution=(
                "the lookup returned the fallback value, signaling that the missing pouch didn't exist. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand."
            )),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_08 = SubjectCurriculum(grade=4, subject_id="G4-08",
    subject_title="assoc — map update", fable="boy-wolf",
    examples=[
        _ex("(assoc {:a 1} :b 2)", {":a": 1, ":b": 2},
            "the expression (assoc {:a 1} :b 2)", "the map after assoc'ing :b 2",
            scenario=(
                "Carol held a wool-basket with one pouch labeled `:a` holding 1 "
                "fleece. A fresh delivery brought new fleeces that needed a second "
                "pouch labeled `:b` with 2 pieces."
            ),
            need=(
                "The form had to add the new pouch to the basket and return an "
                "updated basket with both pouches, leaving the original unchanged."
            ),
            mapping=(
                "`assoc` adds or updates a key-value pair in the map. It takes the "
                "old basket, the new key `:b`, and its value 2, returning a fresh "
                "basket that holds both the original `:a` and the new `:b`."
            ),
            resolution=(
                'the call returned a new basket showing both `:a` 1 and `:b` 2, while the original single-pouch basket stood untouched. Tom chalked {drawn.a} on the village notice, and the morning record stood for the next shepherd to read.'
            )),
        _ex("(assoc {:a 1} :a 99)", {":a": 99},
            "the expression (assoc {:a 1} :a 99)", "the map after updating :a to 99",
            scenario=(
                "Carol's basket held one pouch labeled `:a` with 1 fleece. Later "
                "that day, a full recount showed 99 fleeces actually in the `:a` pouch."
            ),
            need=(
                "The form had to update the old count in the `:a` pouch to the new "
                "correct count and return a fresh basket, the original untouched."
            ),
            mapping=(
                "`assoc` with an existing key replaces the old value. It takes the "
                "map, the same key `:a`, and the new value 99, overwriting the old 1 "
                "and returning a new basket with the corrected count."
            ),
            resolution=(
                "the call returned a new basket with `:a` now paired with 99, and Carol's original basket with `:a` 1 remained as it was before. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain."
            )),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_09 = SubjectCurriculum(grade=4, subject_id="G4-09",
    subject_title="dissoc — map remove key", fable="boy-wolf",
    examples=[
        _ex("(dissoc {:a 1 :b 2} :a)", {":b": 2},
            "the expression (dissoc {:a 1 :b 2} :a)", "the map without :a",
            scenario=(
                "Carol's wool-basket held two pouches: `:a` with 1 fleece and "
                "`:b` with 2. A recount showed the `:a` pouch had been miscounted "
                "and needed to be removed from the day's ledger."
            ),
            need=(
                "The form had to remove the `:a` pouch from the basket, returning "
                "a fresh basket with only `:b` left, the original untouched."
            ),
            mapping=(
                "`dissoc` unstitches a key-value pair from the map. It takes the "
                "old basket and the key `:a`, returning a new basket with that "
                "pouch gone and only `:b` remaining."
            ),
            resolution=(
                "the call returned a new basket showing only `:b` 2, and Carol's original two-pouch basket sat unchanged. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then."
            )),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_10 = SubjectCurriculum(grade=4, subject_id="G4-10",
    subject_title="keys and vals", fable="boy-wolf",
    examples=[
        _ex("(count (keys {:a 1 :b 2 :c 3}))", 3,
            "the expression (count (keys ...))", "the number of keys in the map",
            scenario=(
                "Carol's wool-basket held three labeled pouches: `:a`, `:b`, and "
                "`:c`, each with different fleece counts. Tom wanted to know how "
                "many different pouches the basket held."
            ),
            need=(
                "The form had to pull out all the pouch labels and count them as "
                "one number — the size of the basket's structure."
            ),
            mapping=(
                "`keys` pulls all the key names from the map into a sequence. "
                "`count` then walks through that sequence and notches the tally "
                "once for each key, yielding the total number of pouches."
            ),
            resolution=(
                'the call returned 3, one notch for each pouch label `:a`, `:b`, and `:c` that the basket carried. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'
            )),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_11 = SubjectCurriculum(grade=4, subject_id="G4-11",
    subject_title="Set literal", fable="boy-wolf",
    examples=[
        _ex("(count #{1 2 3})", 3, "the count of #{1 2 3}", "the size of the set",
            scenario=(
                "Carol stood at the fold with three distinct fleece weights to "
                "sort: 1, 2, and 3 — each a different brand, each arriving once."
            ),
            need=(
                "The form had to count the unique fleece types without repeats, "
                "grouping them as a set where each weight appears only once."
            ),
            mapping=(
                "The set `#{1 2 3}` writes down three unique items. `count` walks "
                "through and notches the tally once for each, giving the total "
                "count of distinct items in the set."
            ),
            resolution=(
                'the call returned 3, one notch for each distinct fleece weight the fold had received. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'
            )),
        _ex("(count #{1 1 1})", 1, "the count of #{1 1 1}", "the size of the set",
            scenario=(
                "Carol arrived with three wool sacks that all bore the same weight "
                "mark: 1, 1, 1. She wanted to know how many distinct weights the "
                "sacks represented."
            ),
            need=(
                "The form had to treat the three identical items as a single "
                "unique type, collapsing them into one entry."
            ),
            mapping=(
                "The set `#{1 1 1}` collapses all three identical items into a "
                "single entry. `count` walks through the set and notches the tally "
                "once — the runtime's rule for sets is that duplicates vanish."
            ),
            resolution=(
                'the call returned 1, because a set holds only unique items, and all three sacks carried the same weight mark.'
            )),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_12 = SubjectCurriculum(grade=4, subject_id="G4-12",
    subject_title="Set membership", fable="boy-wolf",
    examples=[
        _ex("(contains? #{1 2 3} 2)", True, "the expression (contains? #{1 2 3} 2)", "whether 2 is in the set",
            scenario=(
                "Carol's sorting pen held three distinct fleece weights: 1, 2, and "
                "3. Tom asked if weight 2 had arrived in that morning's shearing."
            ),
            need=(
                "The form had to check whether the weight 2 sat in the set of "
                "weights Carol had collected."
            ),
            mapping=(
                "`contains?` tests membership. It takes the set and the item 2, "
                "checking if 2 sits among the unique weights. Since 2 is there, "
                "it returns true."
            ),
            resolution=(
                "the call returned true, confirming that weight 2 had indeed arrived in the morning's fleeces. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record."
            )),
        _ex("(contains? #{1 2 3} 4)", False, "the expression (contains? #{1 2 3} 4)", "whether 4 is in the set",
            scenario=(
                "Carol's set held fleeces of weight 1, 2, and 3. Tom wondered if "
                "any weight-4 fleeces had slipped into the pen unnoticed."
            ),
            need=(
                "The form had to check if the weight 4 existed among the collected "
                "items, and report false if it didn't."
            ),
            mapping=(
                "`contains?` checks the set for the item 4. Since 4 is not among "
                "the weights, it returns false — no weight-4 fleeces have "
                "arrived."
            ),
            resolution=(
                'the call returned false, confirming that the pen held no weight-4 fleeces and the count was exact. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_13 = SubjectCurriculum(grade=4, subject_id="G4-13",
    subject_title="count — universal", fable="boy-wolf",
    examples=[
        _ex("(count [1 2 3 4 5])", 5, "the count of a 5-element vector", "the count",
            scenario=(
                "Carol laid out five fleeces in a wool-basket. Each had a "
                "weight tag, but she wanted only a single number telling "
                "how many lay inside."
            ),
            need=(
                "The form had to walk through the basket and notch a tally once "
                "for each fleece, yielding the total."
            ),
            mapping=(
                "`count` works on any collection. It walks through the vector and "
                "counts each element — the runtime steps once per item until all "
                "have been tallied."
            ),
            resolution=(
                'the call returned 5, the exact number of fleeces Carol had placed in the basket. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'
            )),
        _ex("(count {:a 1 :b 2})", 2, "the count of a 2-key map", "the count",
            scenario=(
                "Carol's wool-basket held two labeled pouches: `:a` with its count "
                "and `:b` with its count. She wanted to know how many pouches sat "
                "in the basket."
            ),
            need=(
                "The form had to count the key-value pairs as single units, "
                "yielding the number of pouches."
            ),
            mapping=(
                "`count` on a map counts each key-value pair as one unit. The "
                "runtime walks through and notches the tally once per pouch, "
                "giving the basket's total structure size."
            ),
            resolution=(
                'the call returned 2, one notch for each pouch `:a` and `:b` that the basket carried. Tom chalked {drawn.a} on the meadow folk notice, and the morning record stood for the next shepherd to read.'
            )),
        _ex("(count #{:a :b :c})", 3, "the count of a 3-element set", "the count",
            scenario=(
                "Carol's sorting pen held three distinct brands of fleece: `:a`, "
                "`:b`, `:c`. She wanted to count the unique types."
            ),
            need=(
                "The form had to walk the set and count each unique brand once, "
                "yielding the total number of distinct types."
            ),
            mapping=(
                "`count` on a set counts each unique item. The runtime notches "
                "the tally once per brand, and because a set holds only uniques, "
                "the count matches the brands present."
            ),
            resolution=(
                'the call returned 3, confirming three distinct fleece brands in the pen. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain.'
            )),
        _ex("(count \"shepherd\")", 8, "the count of \"shepherd\"", "the string length",
            scenario=(
                "Carol carved the word \"shepherd\" onto a tally-stick one letter "
                "at a time. She wanted to count how many chalk marks she had made."
            ),
            need=(
                "The form had to count the individual letters in the word, "
                "returning their sum as one number."
            ),
            mapping=(
                "`count` on a string counts each character. The runtime walks "
                "through each letter of \"shepherd\" and notches the tally once "
                "per mark, building the total."
            ),
            resolution=(
                'the call returned 8, one notch for each letter: s, h, e, p, h, e, r, d. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then.'
            )),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_14 = SubjectCurriculum(grade=4, subject_id="G4-14",
    subject_title="empty?", fable="boy-wolf",
    examples=[
        _ex("(empty? [])",   True,  "the expression (empty? [])",   "whether [] is empty",
            scenario=(
                "Carol held an empty wool-basket at the watchhouse, fresh from "
                "cleaning. Tom asked if the basket held any fleeces at all."
            ),
            need=(
                "The form had to answer true if the basket contained nothing, "
                "false if it held even one item."
            ),
            mapping=(
                "`empty?` tests whether the collection has no items. For an empty "
                "vector `[]`, it returns true — the basket holds nothing."
            ),
            resolution=(
                "the call returned true, confirming the basket was completely empty and ready for the day's shearing. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement."
            )),
        _ex("(empty? [1])",  False, "the expression (empty? [1])",  "whether [1] is empty",
            scenario=(
                "Carol held the same basket, now with one fleece inside marked "
                "with weight 1. Tom asked again if the basket was empty."
            ),
            need=(
                "The form had to return false because the basket now carried "
                "at least one item."
            ),
            mapping=(
                "`empty?` checks for the absence of items. For `[1]`, which holds "
                "one fleece, it returns false — the basket is not empty."
            ),
            resolution=(
                'the call returned false, showing the basket had changed from empty to occupied. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear.'
            )),
        _ex("(empty? \"\")", True,  "the expression (empty? \"\")", "whether the empty string is empty",
            scenario=(
                "Carol erased all the chalk from her slate at the watchhouse, "
                "leaving it blank. She asked if the slate held any marks at all."
            ),
            need=(
                "The form had to test whether the empty string — the blank slate "
                "— held no characters."
            ),
            mapping=(
                "`empty?` works on strings too. An empty string `\"\"` is the "
                "blank slate, and it returns true because no chalk marks "
                "remain."
            ),
            resolution=(
                "the call returned true, confirming the slate was completely blank and ready for the day's tallies. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record."
            )),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_15 = SubjectCurriculum(grade=4, subject_id="G4-15",
    subject_title="first, rest, last", fable="boy-wolf",
    examples=[
        _ex("(first [10 20 30])", 10, "the first of the vector", "the first element",
            scenario=(
                "Carol lined three fleece bundles in the wool-basket: weights 10, "
                "20, and 30 from left to right. Tom wanted the leftmost bundle's "
                "weight — the first one."
            ),
            need=(
                "The form had to pluck the first item without disturbing the rest "
                "of the arrangement."
            ),
            mapping=(
                "`first` reaches to the left end of the vector and returns the "
                "first item. For `[10 20 30]`, it yields the leftmost item, 10."
            ),
            resolution=(
                'the call returned 10, the weight of the leftmost bundle. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
        _ex("(last  [10 20 30])", 30, "the last of the vector",  "the last element",
            scenario=(
                "Carol's basket still held the three bundles: 10, 20, 30 left to "
                "right. Tom now asked for the rightmost bundle — the last one."
            ),
            need=(
                "The form had to jump to the right end and return the last item "
                "without changing the basket."
            ),
            mapping=(
                "`last` reaches to the right end of the vector and returns the "
                "final item. For `[10 20 30]`, it yields 30."
            ),
            resolution=(
                'the call returned 30, the weight of the rightmost bundle. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'
            )),
        _ex("(count (rest [10 20 30]))", 2, "the count of (rest [10 20 30])", "the count after removing first",
            scenario=(
                "Carol's basket held three bundles: 10, 20, 30. She wanted to "
                "know how many items remained after setting the first bundle aside."
            ),
            need=(
                "The form had to remove the first item and count what was left, "
                "yielding a single number for the remainder."
            ),
            mapping=(
                "`rest` peels away the first item and returns the remaining items. "
                "`count` then tallies the leftovers — stepping through 20 and 30 "
                "and notching the count once per item, yielding 2."
            ),
            resolution=(
                'the call returned 2, confirming that after removing the first bundle, two remained in the basket. Tom chalked {drawn.a} on the townsfolk notice, and the morning record stood for the next shepherd to read.'
            )),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_16 = SubjectCurriculum(grade=4, subject_id="G4-16",
    subject_title="into and conj on collections", fable="boy-wolf",
    examples=[
        _ex("(into [] '(1 2 3))", [1,2,3],
            "the expression (into [] '(1 2 3))", "the vector built from a list",
            scenario=(
                "Carol set up the fleece-comb at the watchhouse, an empty "
                "wool-basket beneath it. Three fleeces arrived from the "
                "morning shearing, threaded onto a rough cord ready to "
                "be fed through the comb."
            ),
            need=(
                "The village wanted the fleeces moved into the basket in "
                "the order they came in, no rule applied — just a "
                "wholesale transfer from one container shape to another."
            ),
                mapping=(
                "`into` pours the source through into the destination "
                "one item at a time. With an empty vector as the basket "
                "below and a list as the cord above, the runtime carries "
                "each fleece across, preserving the order."
            ),
            resolution=(
                "the basket caught all three fleeces in the same order they had arrived — the morning's shearing settled into the day's container. The lookout returned with {drawn.a} on his slate, the valley long behind him and the count plain."           )),
        _ex("(into #{} [1 2 2 3])", [1,2,3],
            "the expression (into #{} [1 2 2 3])", "the set built from a vector (dups removed)",
            scenario=(
                "Carol held a wool-basket with four weight-tags: 1, 2, 2, 3. "
                "The second tag was a duplicate — two fleeces bore weight 2. "
                "She wanted to move them into a sorting pen that kept only unique "
                "weights."
            ),
            need=(
                "The form had to transfer the fleeces from the basket to the pen, "
                "collapsing the duplicate weight 2 into a single entry."
            ),
            mapping=(
                "`into` pours items from one collection into another. With an "
                "empty set `#{}` as the destination, the runtime carries each "
                "item from the vector across — but sets enforce uniqueness, so "
                "the second 2 collapses into the first."
            ),
            resolution=(
                "the call returned the set with three unique weights: 1, 2, 3, the duplicate resolved by the set's rule."
            )),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G4)


G4_17 = SubjectCurriculum(grade=4, subject_id="G4-17",
    subject_title="Immutability — assoc returns new", fable="boy-wolf",
    examples=[
        _ex("(let [m {:a 1}] (assoc m :a 99) m)", {":a": 1},
            "the form showing assoc returns a new map", "the original map after assoc",
            scenario=(
                "Carol held her wool-basket with one pouch `:a` containing 1 fleece. "
                "A fresh count revealed 99 fleeces actually in that pouch. She "
                "asked the REPL to update the basket, but then wanted to see if "
                "the original was still unchanged."
            ),
            need=(
                "The form had to prove that `assoc` returns a fresh basket while "
                "the original sits unchanged, showing immutability in action."
            ),
            mapping=(
                "`let` binds the original basket to `m`. `assoc` takes `m` and "
                "returns a new basket with `:a` updated to 99, but that new "
                "basket is not saved. The final reference to `m` pulls the "
                "original, confirming it still holds `:a` 1."
            ),
            resolution=(
                "the call returned 1, the original count, proving Carol's basket had not been changed by the `assoc` operation. The watchhouse warmed as the elder set {drawn.a} into the day record, the fold quiet by then."
            )),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_18 = SubjectCurriculum(grade=4, subject_id="G4-18",
    subject_title="Equality of vectors and lists", fable="boy-wolf",
    examples=[
        _ex("(= [1 2 3] '(1 2 3))", True,
            "the expression (= [1 2 3] '(1 2 3))", "whether vector and list with same elements are equal",
            scenario=(
                "Carol held two containers of fleeces: one a wool-basket `[1 2 3]` "
                "and another a cord `'(1 2 3)` with three markers strung on it. "
                "The containers looked different, but both held the same three items "
                "in the same order."
            ),
            need=(
                "The form had to check if two different container shapes held "
                "identical contents — whether the vector and list were equal in "
                "their elements despite different shapes."
            ),
            mapping=(
                "`=` compares for value equality, not container shape. The vector "
                "`[1 2 3]` and the list `'(1 2 3)` both hold the same three items "
                "in the same order, so it returns true even though one is a "
                "basket and one is a cord."
            ),
            resolution=(
                'the call returned true, confirming that despite their different containers, the basket and the cord held the same cargo. {drawn.a} stood as the answer the fold required, slate, chalk, and a steady eye all in agreement.'
            )),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_19 = SubjectCurriculum(grade=4, subject_id="G4-19",
    subject_title="range and seq", fable="boy-wolf",
    examples=[
        _ex("(count (range 5))", 5, "the count of (range 5)", "the count of range 0..4",
            scenario=(
                "Carol needed to count fleeces for five consecutive days at the "
                "fold. Rather than listing each day's number, she asked the form "
                "to generate the sequence 0, 1, 2, 3, 4."
            ),
            need=(
                'The form had to create a range of {drawn.a} numbers starting from zero and count them without typing each one.'
            ),
            mapping=(
                "`range 5` generates the sequence 0, 1, 2, 3, 4 — a lazy span. "
                "`count` then walks through the range and notches the tally once "
                "per item, yielding 5."
            ),
            resolution=(
                "the call returned 5, confirming that the range held five days' worth of counts. The pasture tally settled at {drawn.a}, and Carol closed the day slate with that one number written clear."
            )),
        _ex("(first (range 1 100))", 1, "the first of (range 1 100)", "the first of range 1..99",
            scenario=(
                "Carol needed to count fleeces from day 1 through day 99. The form "
                "could generate that range, and she wanted to see what the first "
                "number in the range would be."
            ),
            need=(
                "The form had to create the range starting at 1 and ending before "
                "100, then return the first number without listing all 99."
            ),
            mapping=(
                "`range 1 100` generates the sequence 1, 2, 3, ..., 99 — numbers "
                "starting at 1 up to but not including 100. `first` plucks the "
                "leftmost item from that range, which is 1."
            ),
            resolution=(
                'the call returned 1, the first day in the 99-day range Carol had requested. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record.'
            )),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_20 = SubjectCurriculum(grade=4, subject_id="G4-20",
    subject_title="Collection vs sequence", fable="boy-wolf",
    examples=[
        _ex("(count (seq [1 2 3]))", 3,
            "the expression (count (seq [1 2 3]))", "the count of seq over a vector",
            scenario=(
                "Carol held a wool-basket with three fleeces: 1, 2, 3. She passed "
                "the basket through a filter-funnel that would return it as a "
                "traversable sequence, then wanted to count the items."
            ),
            need=(
                "The form had to convert the basket into a sequence and then count "
                "the items flowing through, yielding the total."
            ),
            mapping=(
                "`seq` takes the collection and wraps it as a sequence view. "
                "`count` then walks through the sequence, notching the tally once "
                "per item — the three fleeces counted one by one."
            ),
            resolution=(
                'the call returned 3, confirming that the sequence held all three items from the original basket. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
        _ex("(seq [])", None,
            "the expression (seq [])", "what (seq []) returns",
            scenario=(
                "Carol held an empty wool-basket at the watchhouse. She wanted to "
                "know what happened if she passed the empty basket through the "
                "sequence-filter."
            ),
            need=(
                "The form had to describe what `seq` returns when given an empty "
                "collection — whether it returns an empty sequence or nil."
            ),
            mapping=(
                "`seq` on an empty collection `[]` returns nil — no sequence can "
                "be formed from an empty source, so the filter returns the "
                "absence of a value."
            ),
            resolution=(
                'the call returned nil, showing that an empty basket produces no sequence at all. The fold gate held tight against the count of {drawn.a}, slate cool under the elder hand.'
            )),
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
    print(f"grade-4 boy-wolf smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
