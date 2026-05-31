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
from mmllm.aesop.curriculum.tortoise_hare._metaphor_pools import (
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
    subject_title="Vector literal", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="[1 2 3]",
            expected=[1,2,3],
            concept_phrase="a vector of three numbers",
            question_what="the vector",
            goal_text="create a vector containing 1, 2, and 3",
            scenario=(
                "Mossback the tortoise kept a foraging-basket with a row of "
                "pebble slots — three side by side — one for each stone she'd "
                "gathered that morning. Position mattered: first slot, second "
                "slot, third slot, left to right. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Pip the hare asked how many pebbles were in the row and "
                "what order they stood in. Mossback needed to write out the "
                "ordered row so the REPL could confirm the arrangement."
            ),
            mapping=(
                "A vector is the row of slots in the basket. Writing "
                "`[1 2 3]` lays them out in order — first, second, third — "
                "just as the basket's pebble row holds them left to right."
            ),
            resolution=(
                "the REPL handed back the row in order — exactly the "
                "arrangement Mossback had laid out."
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
                "Before the morning's foraging began, Mossback the tortoise "
                "set her basket on the path with its pebble row still empty — "
                "no pebbles, no contents, ready for whatever the meadow "
                "would yield. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Pip the hare wanted to see what an empty row looked like "
                "in the REPL, before anything was placed inside."
            ),
            mapping=(
                "`[]` is the empty pebble row — the basket's slot-rail with "
                "nothing in it. No first, no second; the row simply exists "
                "and waits."
            ),
            resolution=(
                "the REPL returned the empty row, confirming the basket "
                "was ready and nothing had been placed yet."
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
                "Mossback the tortoise had two trail-markers scratched on "
                "bark — one reading \"a\", one reading \"b\" — and tucked "
                "them into her basket's two-slot pebble row in order."
            ),
            need=(
                "She needed to write the row out so the REPL could read "
                "it back and confirm both markers sat in the right positions."
            ),
            mapping=(
                "A vector of strings is the row of slots with "
                "letter-markers tucked into each — first slot holds the "
                "first marker, second slot holds the second, left to "
                "right."
            ),
            resolution=(
                "the REPL confirmed both markers in order — the basket's "
                "row held exactly what Mossback had tucked in."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_02 = SubjectCurriculum(grade=4, subject_id="G4-02",
    subject_title="nth — vector access", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(nth [10 20 30] 0)",
            expected=10,
            concept_phrase="accessing by index",
            question_what="the value at index 0",
            goal_text="get the element at index 0 of a vector containing 10, 20, and 30",
            scenario=(
                "Mossback the tortoise's pebble row held three stones — "
                "one at the first slot, one at the second, one at the third. "
                "Each slot had a position number starting from zero."
            ),
            need=(
                "Pip the hare needed to know what sat in the very first "
                "slot — position zero — without lifting every stone out "
                "of the row."
            ),
            mapping=(
                '`nth` reaches directly into the row at the given position. Position {drawn.b} is the first slot; `nth` reads it without disturbing the others.'
            ),
            resolution=(
                "the REPL read out what the first slot held — the pebble "
                "at position zero, undisturbed."
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
                "Mossback the tortoise's three-slot pebble row sat on "
                "the path. She needed to check the last slot — the one "
                "at position two, counting from zero."
            ),
            need=(
                "Without pulling stones out in order, Pip the hare "
                "asked Mossback to jump straight to the final slot "
                "and read what was there."
            ),
            mapping=(
                '`nth` at position {drawn.b} reaches to the third slot directly. No need to pass through 0 or 1 — the row lets `nth` land exactly where told.'
            ),
            resolution=(
                "the REPL reported the stone at position two — the far "
                "end of the row, reached in one step."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_03 = SubjectCurriculum(grade=4, subject_id="G4-03",
    subject_title="conj — append to vector", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(conj [1 2] 3)",
            expected=[1,2,3],
            concept_phrase="the conj operation",
            question_what="the vector after conjing",
            goal_text="append 3 to the end of a vector containing 1 and 2",
            scenario=(
                "Mossback the tortoise had a pebble row with two stones "
                "already in place. A third stone arrived from the path. "
                "The original row sat untouched — she needed a fresh row "
                "that included all three. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "Pip the hare wanted the new arrangement: the original "
                "two stones followed by the newcomer at the end, as a "
                "fresh row."
            ),
            mapping=(
                "`conj` drops a new stone at the end of the pebble row "
                "and returns a fresh row. The original two-stone row is "
                "unchanged; the new row carries all three in order."
            ),
            resolution=(
                "the REPL handed back the fresh row — all three pebbles "
                "in order, the newcomer settled at the end."
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
                "Mossback the tortoise set an empty pebble row on the "
                "path — no stones yet. Pip the hare left a label-stone "
                "marked :hare at the roadside, waiting to be placed. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "The label-stone needed a home. Mossback wanted a fresh "
                "row that contained just the :hare stone, starting from "
                "the empty row."
            ),
            mapping=(
                "`conj` on an empty row produces a fresh one-slot row "
                "with the new stone at its single position. The empty "
                "row contributes the structure; `:hare` fills it."
            ),
            resolution=(
                "the REPL returned the one-element row — the :hare stone "
                "in its place, the empty row still empty beside it."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_04 = SubjectCurriculum(grade=4, subject_id="G4-04",
    subject_title="List literal", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="'(1 2 3)",
            expected=[1,2,3],
            concept_phrase="a list literal",
            question_what="the list of three numbers",
            goal_text="create a list containing 1, 2, and 3",
            scenario=(
                "Three animals stood in a procession on the path, "
                "tail-to-paw in single file. Mossback the tortoise wrote "
                "them down in order — a list, not a row of slots but a "
                "chain each member knew its neighbor. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Pip the hare wanted to see the procession captured in "
                "the REPL — three members, in file, just as they stood."
            ),
            mapping=(
                "A list literal uses the apostrophe-quote mark — telling "
                "the runtime not to evaluate the parens as a call but to "
                "treat them as a procession walking left to right."
            ),
            resolution=(
                "the REPL returned the three-member procession — head "
                "at the front, last member at the tail, in order."
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
                "The path was quiet. No procession had formed yet. "
                "Mossback the tortoise wrote out the empty marching order "
                "— a list with no members — to show the REPL what "
                "nothing-in-file looks like. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Pip the hare needed proof that an empty procession "
                "was a value the REPL could hold and hand back."
            ),
            mapping=(
                "`'()` is the empty list — the quote keeps the parentheses "
                "from being read as a call; the empty interior means no "
                "members stand in line."
            ),
            resolution=(
                "the REPL handed back the empty procession — a list "
                "with nothing inside, confirmed and ready."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_05 = SubjectCurriculum(grade=4, subject_id="G4-05",
    subject_title="cons — prepend to seq", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(cons 0 '(1 2 3))",
            expected=[0,1,2,3],
            concept_phrase="the cons operation",
            question_what="the seq after cons'ing",
            goal_text="prepend 0 to the front of a list containing 1, 2, and 3",
            scenario=(
                'Three animals — numbered 1, 2, 3 — stood in procession on the path. A latecomer marked {drawn.a} arrived and needed to take the lead position at the very front of the line.'
            ),
            need=(
                "Mossback the tortoise needed a new procession with the "
                "latecomer at the head. The original three-member list "
                "should remain as it was — a fresh sequence was wanted."
            ),
            mapping=(
                "`cons` places a new leader at the head of an existing "
                "sequence and returns a fresh seq. The new head joins "
                "the front; the rest of the procession follows behind."
            ),
            resolution=(
                "the REPL returned the fresh procession — the new leader "
                "at the front, followed by the original three members "
                "in their existing order."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_06 = SubjectCurriculum(grade=4, subject_id="G4-06",
    subject_title="Map literal", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="{:hare 1 :tortoise 2}",
            expected={":hare": 1, ":tortoise": 2},
            concept_phrase="a map literal",
            question_what="the map with two entries",
            goal_text="create a map binding the keyword :hare to 1 and :tortoise to 2",
            scenario=(
                "Mossback the tortoise's foraging-basket had two labeled "
                "pouches — one stitched with the tag :hare and one with "
                ":tortoise. Each pouch held a tally of the day's findings "
                "for that racer. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Pip the hare wanted the basket written out so the REPL "
                "could read both labels and their tallies at once, as a "
                "single collection."
            ),
            mapping=(
                "A map literal pairs each label with its value inside "
                "curly braces. `:hare` names one pouch; its tally sits "
                "beside it. `:tortoise` names the other pouch; its tally "
                "follows."
            ),
            resolution=(
                "the REPL returned the basket holding both labeled "
                "pouches with their tallies — the two-entry map, just "
                "as Mossback had laid it out."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_07 = SubjectCurriculum(grade=4, subject_id="G4-07",
    subject_title="get — map lookup", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(get {:a 1 :b 2} :a)",
            expected=1,
            concept_phrase="map lookup",
            question_what="the value at :a",
            goal_text="look up the value at key :a in a map binding :a to 1 and :b to 2",
            scenario=(
                "Mossback the tortoise's basket had two pouches — one "
                "labeled :a and one labeled :b — each holding a count "
                "from the morning's foraging. The basket sat on the path, "
                "its contents undisturbed. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "Pip the hare needed to know only what pouch :a held, "
                "without pulling out :b or disturbing anything else."
            ),
            mapping=(
                "`get` reaches into the basket by label. Giving it `:a` "
                "pulls just that pouch's contents — the count stored "
                "under :a — and leaves :b exactly where it is."
            ),
            resolution=(
                "the REPL returned the count from pouch :a — one "
                "lookup, one pouch, the right answer."
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
                "Mossback the tortoise's basket had one pouch — labeled "
                ":a. Pip the hare asked for the contents of a pouch "
                "labeled :missing, which had never been stitched into "
                "the basket at all. The values drawn fresh were {drawn.a}, {drawn.b}, and {drawn.c}."
            ),
            need=(
                "Rather than failing with an error, Mossback wanted the "
                "lookup to hand back a safe stand-in — the keyword "
                ":default — whenever a label was absent."
            ),
            mapping=(
                "`get` accepts a third argument as the fallback. When "
                "the label is not in the basket, `get` returns that "
                "fallback instead of nothing, keeping the operation "
                "safe."
            ),
            resolution=(
                "the REPL returned the fallback keyword — the basket had "
                "no :missing pouch, so the safe stand-in came back "
                "as intended."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_08 = SubjectCurriculum(grade=4, subject_id="G4-08",
    subject_title="assoc — map update", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(assoc {:a 1} :b 2)",
            expected={":a": 1, ":b": 2},
            concept_phrase="the assoc operation",
            question_what="the basket after associating value 2 with the :b compartment",
            goal_text="associate value 2 with the :b compartment of a basket already binding :a to 1",
            scenario=(
                "Mossback the tortoise's foraging-basket had compartments "
                "stitched into its sides — an open area at the top, plus "
                "named pouches :a and :b. Pouch :a already held 1 acorn "
                "from the morning's gathering."
            ),
            need=(
                "Pip the hare arrived from the orchard with {drawn.c} more acorns. Mossback decided they belonged in pouch :b — and pouch :a's acorn should stay exactly where it was."
            ),
            mapping=(
                "`assoc` associates a value with a named compartment of the basket. The basket's shape stays the same — :a still holds its 1, and :b now holds the new {drawn.c} — exactly as the foraging called for."
            ),
            resolution=(
                "the basket carried both — 1 in :a, {drawn.c} in :b — ready for the rest of the day's gathering."
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
                "Mossback the tortoise's basket had a single pouch labeled "
                ":a, holding an old count from an earlier foray. A recount "
                "had produced a much larger figure that needed to replace "
                "the original. The values drawn fresh were {drawn.a}, {drawn.b}, and {drawn.c}."
            ),
            need=(
                "Pip the hare needed the basket updated so pouch :a "
                "reflected the new count — a fresh basket with the "
                "corrected value, leaving the old one untouched."
            ),
            mapping=(
                "`assoc` on an existing key replaces its value with the "
                "new one. The fresh basket carries pouch :a with the "
                "updated figure; the old basket keeps its original count."
            ),
            resolution=(
                "the REPL returned the fresh basket — pouch :a now "
                "holding the corrected figure, the update complete."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_09 = SubjectCurriculum(grade=4, subject_id="G4-09",
    subject_title="dissoc — map remove key", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(dissoc {:a 1 :b 2} :a)",
            expected={":b": 2},
            concept_phrase="the dissoc operation",
            question_what="the map after using dissoc to remove a key",
            goal_text="remove the key :a from a map binding :a to 1 and :b to 2",
            scenario=(
                "Mossback the tortoise's basket had two pouches — :a and "
                ":b — each stitched in from the morning's arrangement. "
                "The foray for :a was complete; that pouch had served "
                "its purpose. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "Pip the hare needed a fresh basket that held only :b "
                "— the :a pouch should be gone from the new arrangement, "
                "though the original basket would remain as it was."
            ),
            mapping=(
                "`dissoc` removes a named pouch from the basket and "
                "returns a fresh basket without it. The original keeps "
                "both pouches; only the fresh one has :a removed."
            ),
            resolution=(
                "the REPL returned the fresh basket — only :b remaining, "
                ":a cleanly removed from the new arrangement."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_10 = SubjectCurriculum(grade=4, subject_id="G4-10",
    subject_title="keys and vals", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(count (keys {:a 1 :b 2 :c 3}))",
            expected=3,
            concept_phrase="counting keys in a map",
            question_what="the number of keys in the map",
            goal_text="count how many keys are in a map binding :a, :b, and :c",
            scenario=(
                "Mossback the tortoise's basket had three labeled pouches "
                "— :a, :b, and :c — each holding a different count. She "
                "needed to know at a glance how many distinct labels the "
                "basket carried. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Pip the hare asked: not what's in each pouch, just how "
                "many pouches have a label. Mossback wanted the count of "
                "labels only."
            ),
            mapping=(
                "`keys` lists all the pouch labels from the basket. "
                "`count` then tallies how many labels came back — one "
                "per pouch, no contents involved."
            ),
            resolution=(
                "the REPL returned the count of labels — confirming how "
                "many named pouches the basket held."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_11 = SubjectCurriculum(grade=4, subject_id="G4-11",
    subject_title="Set literal", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(count #{1 2 3})",
            expected=3,
            concept_phrase="the size of a set",
            question_what="the size of the set",
            goal_text="count the elements in a set containing 1, 2, and 3",
            scenario=(
                "Mossback the tortoise kept a unique-kinds basket — a "
                "basket where each kind of nut appeared only once. Three "
                "different kinds sat inside: no duplicates, no repeats. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Pip the hare wanted to know how many distinct kinds "
                "the basket held. Mossback needed the count of unique "
                "members."
            ),
            mapping=(
                "`#{1 2 3}` is the set — the unique-kinds basket. "
                "`count` tallies how many distinct members it holds. "
                "Three kinds, three to count."
            ),
            resolution=(
                "the REPL returned the count of distinct kinds — "
                "three unique members, none repeated."
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
                'Mossback the tortoise wrote a set with the same kind listed three times over. The unique-kinds basket, by its rule, would keep only one of any kind no matter how many were offered. The value drawn fresh was 1.'
            ),
            need=(
                "Pip the hare expected the basket to stay true to its "
                "rule. Mossback needed to show that the count would "
                "reflect uniqueness, not the raw number of offerings."
            ),
            mapping=(
                "A set collapses duplicates — three offerings of the "
                "same kind become one. `count` on the result gives the "
                "number of distinct kinds actually kept."
            ),
            resolution=(
                "the REPL returned a count of one — the unique-kinds "
                "basket held only a single kind, as its rule required."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_12 = SubjectCurriculum(grade=4, subject_id="G4-12",
    subject_title="Set membership", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(contains? #{1 2 3} 2)",
            expected=True,
            concept_phrase="testing set membership",
            question_what="whether an element is in the set using contains?",
            goal_text="check whether 2 is a member of a set containing 1, 2, and 3",
            scenario=(
                "Mossback the tortoise's unique-kinds basket held three kinds — kinds 1, {drawn.b}, and 3. Pip the hare arrived with kind {drawn.b} and wanted to know if it was already present before adding a duplicate."
            ),
            need=(
                "Mossback needed a yes-or-no answer: is kind {drawn.b} already in the basket? The basket's rule depended on knowing this first."
            ),
            mapping=(
                "`contains?` asks the unique-kinds basket whether a "
                "specific kind is present. The basket checks its "
                "contents and returns true or false — no modification, "
                "just a membership query."
            ),
            resolution=(
                "the REPL confirmed the kind was already present — "
                "membership verified, no rummaging required."
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
                "Mossback the tortoise's unique-kinds basket held three kinds. Pip the hare arrived with kind {drawn.b} and asked whether that kind was already somewhere inside before claiming it was new."
            ),
            need=(
                'Before declaring kind {drawn.b} novel, Mossback needed to check the basket and confirm it truly was absent — not just assumed to be.'
            ),
            mapping=(
                "`contains?` checks the basket for the given kind. If "
                "the kind is not there, it returns false — a clear "
                "signal the kind has not been seen yet."
            ),
            resolution=(
                "the REPL signalled the kind's absence from the basket — "
                "if added, it would be genuinely new, no duplicate."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_13 = SubjectCurriculum(grade=4, subject_id="G4-13",
    subject_title="count — universal", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(count [1 2 3 4 5])",
            expected=5,
            concept_phrase="the count of a collection",
            question_what="the number of elements in the collection",
            goal_text="count the elements in the vector [1 2 3 4 5]",
            scenario=(
                "Mossback the tortoise's pebble row held five stones "
                "laid out in order. She had lost track of the total and "
                "needed the REPL to confirm the count without her "
                "counting by hand. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Pip the hare wagered the row had more than four stones. "
                "Mossback needed the exact tally to settle it."
            ),
            mapping=(
                "`count` works over any collection — it simply tallies "
                "how many elements are present. On a vector it counts "
                "the slots; here, five slots filled."
            ),
            resolution=(
                "the REPL returned the tally — confirming the row's "
                "length and settling the wager."
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
                "Mossback the tortoise's basket had labeled pouches — "
                "she had stitched in pouches over many forays and could "
                "no longer remember exactly how many entries the current "
                "basket held."
            ),
            need=(
                "Pip the hare wanted to know: how many pouch-and-label "
                "pairs are in the basket right now? Not what's inside "
                "each — just how many pairs exist."
            ),
            mapping=(
                "`count` on a map tallies the number of key-value pairs "
                "— each label paired with its contents counts as one "
                "entry."
            ),
            resolution=(
                'the REPL returned the pair count — confirming how many distinct label-and-contents pairs the basket held (with `:a` as the input value).'
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
                "Mossback the tortoise's unique-kinds basket held several "
                "keyword stones. She needed to know how many distinct kinds "
                "were present — `count` would give that without listing "
                "each one. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Pip the hare asked for the total number of unique members "
                "in the set. Mossback needed the tally, not the list."
            ),
            mapping=(
                "`count` on a set returns the number of distinct members "
                "it holds. Three keyword stones, three to count."
            ),
            resolution=(
                "the REPL returned the count of unique members — "
                "three keyword kinds confirmed."
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
                'Mossback the {drawn.a} had scratched her name — "{drawn.a}" — into a bark chip. Pip the hare claimed the name was shorter than it looked; Mossback was certain it was longer.'
            ),
            need=(
                "They needed the REPL to count every letter in the name "
                "so neither had to count on their claws."
            ),
            mapping=(
                '`count` works on strings too — it treats each character as a member of the collection and tallies them. "{drawn.a}" has one character per letter.'
            ),
            resolution=(
                "the REPL returned the character count — the full "
                "length of the name, settling the dispute."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_14 = SubjectCurriculum(grade=4, subject_id="G4-14",
    subject_title="empty?", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(empty? [])",
            expected=True,
            concept_phrase="checking if a collection is empty",
            question_what="whether the collection is empty",
            goal_text="test whether an empty vector is empty",
            scenario=(
                "Mossback the tortoise set her pebble row on the path "
                "before the foray began. No stones had been placed yet "
                "— the row was bare. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Pip the hare needed to confirm the row was truly empty "
                "before starting to place stones — a yes-or-no check "
                "before the foray."
            ),
            mapping=(
                "`empty?` asks whether a collection holds nothing. An "
                "empty vector has no slots filled; the answer is true."
            ),
            resolution=(
                "the REPL confirmed the row was empty — no stones, "
                "nothing inside, ready to begin."
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
                "Mossback the tortoise's pebble row had one stone in "
                "its first slot — placed earlier in the morning. The "
                "row was not bare, but Pip the hare was unsure. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Pip the hare needed to know whether the row was still "
                "empty. Mossback wanted the REPL to settle it with a "
                "direct check."
            ),
            mapping=(
                "`empty?` on a non-empty collection returns false — "
                "even one element means the collection is occupied. "
                "One stone fills the row."
            ),
            resolution=(
                "the REPL signalled the row's non-empty state — even "
                "one stone is enough to settle the question."
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
                'Mossback the tortoise picked up a blank bark chip {drawn.a}—{drawn.a} nothing scratched on it, not a single letter. Pip the hare wanted to confirm it was truly blank before writing on it.'
            ),
            need=(
                'They needed the REPL to verify the bark chip held no characters at all {drawn.a}—{drawn.a} an empty-string check before committing any marks.'
            ),
            mapping=(
                '{drawn.a}`empty?{drawn.a}` works on strings as collections of characters. A string with no characters is empty; the answer is true.'
            ),
            resolution=(
                'the REPL confirmed the bark chip was blank {drawn.a}—{drawn.a} no characters, empty string, safe to write on.'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_15 = SubjectCurriculum(grade=4, subject_id="G4-15",
    subject_title="first, rest, last", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(first [10 20 30])",
            expected=10,
            concept_phrase="getting the first element",
            question_what="the first element",
            goal_text="get the first element of a vector containing 10, 20, and 30",
            scenario=(
                "Mossback the tortoise's pebble row held three stones "
                "in order. The first stone — the one at the head of "
                "the row — was the one she needed to read without "
                "disturbing the rest. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Pip the hare needed only the leading stone. Mossback "
                "wanted to read it directly without stepping through "
                "the whole row."
            ),
            mapping=(
                "`first` reaches to the very front of a collection and "
                "returns what is there — the head stone — leaving "
                "the rest of the row untouched."
            ),
            resolution=(
                "the REPL returned the leading stone — the head of the "
                "row, read in one step."
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
                "Mossback the tortoise's pebble row held three stones. "
                "The final stone — at the far end of the row — was the "
                "one she needed, without stepping through the others. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Pip the hare needed only the trailing stone. Mossback "
                "wanted to jump straight to the end of the row and "
                "read it."
            ),
            mapping=(
                "`last` reaches to the tail of a collection and returns "
                "what is there — the final stone — without reading "
                "everything before it."
            ),
            resolution=(
                "the REPL returned the trailing stone — the far end of "
                "the row, reached directly."
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
                "Mossback the tortoise's pebble row had three stones. "
                "The leading stone had been claimed — she wanted to "
                "know how many remained in the row after the head "
                "was gone. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Pip the hare needed the count of the tail — the stones "
                "left after setting the first aside — without listing "
                "them individually."
            ),
            mapping=(
                "`rest` returns the collection without its first element. "
                "`count` then tallies the tail. Two stones remain once "
                "the head is removed."
            ),
            resolution=(
                "the REPL returned the count of the remaining stones — "
                "the tail's length, the head already gone."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_16 = SubjectCurriculum(grade=4, subject_id="G4-16",
    subject_title="into and conj on collections", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(into [] '(1 2 3))",
            expected=[1,2,3],
            concept_phrase="building a vector from a list",
            question_what="the vector built from a list",
            goal_text="convert a list containing 1, 2, and 3 into a vector",
            scenario=(
                "Mossback the tortoise had a procession of three animals "
                "walking tail-to-paw, and an empty pebble row waiting "
                "below a sieve. She needed to pour the procession through "
                "so the row would collect them in order. The values drawn fresh were {drawn.a} and {drawn.b}."
            ),
            need=(
                "Pip the hare wanted the members as an ordered row, not "
                "a procession. The sieve would let each one fall into "
                "the waiting row."
            ),
            mapping=(
                "`into` pours one collection into another through the "
                "sieve. An empty vector is the receiver; the list is "
                "the source. Each element falls in and the row fills "
                "in order."
            ),
            resolution=(
                "the REPL returned the filled row — all three members "
                "poured from the procession into the ordered vector."
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
                "Mossback the tortoise's pebble row had four stones, but one kind appeared twice. She held an empty unique-kinds basket below the sieve, ready to catch only what was genuinely new. The values drawn fresh were 1 and 2."
            ),
            need=(
                "Pip the hare wanted the unique kinds only — no repeats. "
                "Pouring through the unique-kinds basket would drop any "
                "duplicate on the first pass."
            ),
            mapping=(
                "`into` with an empty set as receiver acts as the sieve "
                "for uniqueness. Each element from the vector is poured "
                "through; duplicates are absorbed, unique kinds land."
            ),
            resolution=(
                'the REPL returned the unique-kinds basket — only the distinct members inside, duplicates sieved away (with `3` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G4)


G4_17 = SubjectCurriculum(grade=4, subject_id="G4-17",
    subject_title="Immutability — assoc returns new", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(let [m {:a 1}] (assoc m :a 99) m)",
            expected={":a": 1},
            concept_phrase="immutability of maps",
            question_what="the original map after assoc",
            goal_text="demonstrate that assoc returns a new map without modifying the original",
            scenario=(
                "Mossback the tortoise's basket had a single pouch :a "
                "inside. She set the basket on the path and bound it "
                "to the name m. Then `assoc` produced a fresh basket "
                "with an updated pouch — but Mossback asked for m, "
                "not the fresh one. The values drawn fresh were {drawn.a}, {drawn.b}, and {drawn.c}."
            ),
            need=(
                "Pip the hare expected the original basket to have "
                "changed. Mossback wanted to show it had not — the "
                "original sat exactly as placed."
            ),
            mapping=(
                "`assoc` returns a new basket; it never touches the "
                "original. The binding m still points to the first "
                "basket — unchanged, its pouch holding the same value "
                "as before."
            ),
            resolution=(
                "the REPL returned the original basket — pouch :a "
                "still holding what was there at the start, the "
                "update having gone into the fresh basket alone."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_18 = SubjectCurriculum(grade=4, subject_id="G4-18",
    subject_title="Equality of vectors and lists", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(= [1 2 3] '(1 2 3))",
            expected=True,
            concept_phrase="testing equality of different collection types",
            question_what="whether vector and list are equal",
            goal_text="test whether a vector with elements 1, 2, 3 equals a list with the same elements",
            scenario=(
                "Mossback the tortoise held two arrangements of the same "
                "three members — one laid out in a pebble row, the other "
                "walking in a procession. Pip the hare thought the two "
                "were different because their containers differed. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Mossback needed the REPL to judge whether content "
                "equality mattered more than container shape — whether "
                "the two arrangements were the same as sequences."
            ),
            mapping=(
                "`=` on collections compares element by element. A "
                "vector and a list with the same members in the same "
                "order are equal as sequences — the container shape "
                "does not break equality."
            ),
            resolution=(
                "the REPL confirmed equality as sequences — the two "
                "arrangements held the same members in the same order."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_19 = SubjectCurriculum(grade=4, subject_id="G4-19",
    subject_title="range and seq", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(count (range 5))",
            expected=5,
            concept_phrase="counting elements in a range",
            question_what="the count of range 0..4",
            goal_text="count how many numbers are generated by a range from 0 to 4",
            scenario=(
                "Mossback the tortoise needed to mark out a stretch of "
                "path with numbered milestones starting from zero. She "
                "asked `range` to generate the milestone numbers and "
                "then needed to know how many milestones would appear. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "Pip the hare needed the count before laying stones — "
                "how many milestones would `range` produce for a span "
                "of five?"
            ),
            mapping=(
                "`range` generates a sequence of numbers from zero up "
                "to but not including its argument. `count` tallies how "
                "many numbers that yields."
            ),
            resolution=(
                "the REPL returned the count of generated milestones — "
                "confirming how many the range would produce."
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
                "Mossback the tortoise's path stretched from milestone "
                "one all the way toward milestone one hundred, exclusive. "
                "She needed to confirm which milestone sat at the very "
                "start of that long stretch."
            ),
            need=(
                "Pip the hare could see the far end of the path but "
                "not the near end. Mossback needed the REPL to name "
                "the first milestone without walking the whole range."
            ),
            mapping=(
                '`range {drawn.a} {drawn.b}` generates a sequence beginning at 1. `first` reaches to the head of that sequence and returns the opening milestone.'
            ),
            resolution=(
                "the REPL returned the first milestone — the opening "
                "number of the range, the start of the long stretch."
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_20 = SubjectCurriculum(grade=4, subject_id="G4-20",
    subject_title="Collection vs sequence", fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(count (seq [1 2 3]))",
            expected=3,
            concept_phrase="creating a sequence from a vector and counting",
            question_what="the count of seq over a vector",
            goal_text="convert a vector containing 1, 2, and 3 to a sequence and count its elements",
            scenario=(
                "Mossback the tortoise had a pebble row. She wanted to "
                "treat it as a plain sequence — a general procession — "
                "rather than a positional row, then count the procession's "
                "members."
            ),
            need=(
                "Pip the hare asked: does `seq` change the count of what "
                "was in the row? Mossback needed to show that converting "
                "to a sequence and counting yields the same membership."
            ),
            mapping=(
                "`seq` converts a collection into a generic sequence. "
                "`count` then tallies the sequence's members. The row  The value drawn fresh was {drawn.a}."
                "had three elements; the sequence carries those same "
                "three."
            ),
            resolution=(
                "the REPL returned the count of the sequence — the same "
                "number of members the original row had, now held as "
                "a sequence."
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
                "Mossback the tortoise's pebble row was empty — no "
                "stones, nothing inside. Pip the hare wanted to know "
                "what `seq` would hand back when given nothing to "
                "work with. The value drawn fresh was {drawn.a}."
            ),
            need=(
                "They needed to discover: does `seq` on an empty row "
                "produce an empty sequence, or something else entirely?"
            ),
            mapping=(
                "`seq` on an empty collection returns nil — not an "
                "empty sequence, but the absence of a sequence. The "
                "distinction matters when checking whether a traversal "
                "has anything to yield."
            ),
            resolution=(
                "the REPL returned nil — the empty row yielded no "
                "sequence at all, the operation's honest answer."
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
