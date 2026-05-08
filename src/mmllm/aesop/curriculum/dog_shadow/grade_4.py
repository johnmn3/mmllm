"""Grade 4 — collections (Layer 4). Through dog-shadow.

Subplot lens: collections of pebbles, milestones, racers, paw-prints,
plums, etc., that the characters count, sort, and manipulate.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.dog_shadow.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL
)
from mmllm.aesop.curriculum.dog_shadow._metaphor_pools import (
    _BASKET_SUBPLOTS, _SIEVE_SUBPLOTS,
)


_COLL_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [
    # NOTE: these two templates avoid putting both {form_display} AND a
    # "the form X" {concept_phrase} in close proximity (the duplication
    # produces ungrammatical "the form X described the form X" prose
    # when concept_phrase is "the form X" verbatim — see SKILL doc #11).
    SubplotTemplate("""\
{tortoise}, {emo_patient} had been laying out a small collection {place} —
pebbles, milestones, paw-prints, whatever the day produced. {tortoise}
wrote {form_display} on a slate and asked {hare_phrase} to write the
form into the REPL so they could confirm it together."""),

    SubplotTemplate("""\
{hare}, {emo_proud}, declared the collection plain. {tortoise_phrase}
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
    subject_title="Vector literal", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="[1 2 3]",
            expected=[1,2,3],
            concept_phrase="a vector of three numbers",
            question_what="the vector",
            goal_text="create a vector containing 1, 2, and 3",
            scenario=(
                "Rex the hound arrived at the hollow log cache at the stream's edge and laid out three bones in a neat row — one, then two, then three. The log could hold them arranged this way."
            ),
            need=(
                'He wanted the row fixed in the hollow log so any dog could read the bones and know the exact count: the counts. The vector was the shape the cache would take.'
            ),
            mapping=(
                'The hollow log is the vector, the three bones are the '
                'elements 1, 2, 3, and the arrangement is what the form '
                'describes when written as [1 2 3].'
            ),
            resolution=(
                'The REPL set the bones in the log exactly as Rex directed, '
                'in their order, and handed back the complete row. The cache '
                'now held what the form promised — 3.'
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
                'Bell the hound stood before an empty hollow log near the '
                'stream, freshly cleaned and ready to receive bones. She had '
                'no bones to place just yet.'
            ),
            need=(
                'She wanted to confirm that the empty log itself — the cache '
                'ready and waiting — could be described as a form and '
                'recognized by the REPL.'
            ),
            mapping=(
                'The hollow log, empty and waiting, is the empty vector. '
                'The form [] names the shape itself.'
            ),
            resolution=(
                'The REPL confirmed the empty cache, handing back the '
                'emptiness Bell had shown it. No bones were there; that was '
                'the verdict.'
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
                'Patch the hound had found two stripped bark-scraps at the '
                'forest edge, one marked "a", one marked "b". They placed them '
                'carefully in the hollow log one after the other.'
            ),
            need=(
                'Patch wanted the pair of scraps to rest in the log as a '
                'single row so the scratch-marks could be read in their order.'
            ),
            mapping=(
                'The hollow log is the vector, the two bark-scraps are the '
                'string elements "a" and "b".'
            ),
            resolution=(
                'The REPL set the scraps in the log and handed back the '
                'ordered pair. Both marks were now fixed in the cache, ready '
                'to be read.'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_02 = SubjectCurriculum(grade=4, subject_id="G4-02",
    subject_title="nth — vector access", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(nth [10 20 30] 0)",
            expected=10,
            concept_phrase="accessing by index",
            question_what="the value at index 0",
            goal_text="get the element at index 0 of a vector containing 10, 20, and 30",
            scenario=(
                'Bell the hound counted three bone-heaps in the hollow log '
                'cache: a pile of 10 bones first, then 20, then 30. She '
                'wanted the very first heap to be pulled out and held up.'
            ),
            need=(
                'She asked the REPL for the bone-count at position 0 — the '
                'first slot in the cache. The position was what mattered, not '
                'the value it held.'
            ),
            mapping=(
                'The hollow log is the vector [10 20 30], the slot number 0 '
                'is the index, and the first heap of bones is what sits there.'
            ),
            resolution=(
                'The REPL stepped into the cache, found the first slot, and '
                'handed back the heap that rested there: 10 bones. The '
                'position had led true — 0.'
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
                'Rex the hound peered into the bone cache and spotted three '
                'piles: position 0 held 10, position 1 held 20, position 2 '
                'held 30. He wanted only the third heap.'
            ),
            need=(
                'He named the slot number 2 to the REPL and asked for what '
                'the log held at that third position.'
            ),
            mapping=(
                'The hollow log is [10 20 30], the index 2 names the third '
                'slot (counting from 0), and position 2 holds the heap of 30.'
            ),
            resolution=(
                'The REPL counted to the third slot in the cache and handed '
                'back the pile of 30 bones. The heap at position 2 was now '
                'in Rex\'s grasp — 2.'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_03 = SubjectCurriculum(grade=4, subject_id="G4-03",
    subject_title="conj — append to vector", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(conj [1 2] 3)",
            expected=[1,2,3],
            concept_phrase="the conj operation",
            question_what="the vector after conjing",
            goal_text="append 3 to the end of a vector containing 1 and 2",
            scenario=(
                'Patch the hound tended a hollow log cache holding two bones '
                'already: one and two. A third bone lay nearby, ready to be '
                'added to the end of the row.'
            ),
            need=(
                'Patch wanted the third bone packed into the cache so the row grew to hold the counts — without disturbing what was already there.'
            ),
            mapping=(
                'The hollow log is the vector [1 2], the new bone is 3, and '
                'appending it creates the extended cache.'
            ),
            resolution=(
                'The REPL took the new bone and slid it into the end of the log, sealing the cache so it now held the counts in order. The original cache stayed untouched; the new one was what came back — 3.'
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
                'Bell the hound found an empty hollow log by the stream and '
                'held up a special marked stone with the label ":hare" '
                'scratched into it. She was ready to place it in the cache.'
            ),
            need=(
                'She wanted to conjoin the marked stone with the empty cache '
                'so the log would hold that single marker.'
            ),
            mapping=(
                'The empty hollow log is [], the marked stone is the keyword '
                ':hare, and placing it creates the new cache.'
            ),
            resolution=(
                'The REPL received the marked stone and placed it in the empty '
                'log. The cache now held the keyword :hare and handed back the '
                'new row — hare.'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_04 = SubjectCurriculum(grade=4, subject_id="G4-04",
    subject_title="List literal", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="'(1 2 3)",
            expected=[1,2,3],
            concept_phrase="a list literal",
            question_what="the list of three numbers",
            goal_text="create a list containing 1, 2, and 3",
            scenario=(
                'Rex the hound chained three bones together in sequence — one '
                'at the front, then two, then three — so that any dog could '
                'pick up the first and the rest would follow as a linked row.'
            ),
            need=(
                'He wanted the chained bones to form a single entity that the '
                'REPL could recognize and return as a complete sequence.'
            ),
            mapping=(
                'The linked chain of bones is the list, each bone is an '
                'element, and the form spells out the chain from first to '
                'last.'
            ),
            resolution=(
                'The REPL recognized the chained form and handed back the '
                'sequence as Rex had described it: one, then two, then three, '
                'linked together — 3.'
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
                'Patch the hound picked up an empty chain by the bank, a mere '
                'collar with no bones attached, and held it up.'
            ),
            need=(
                'Patch wanted the empty chain itself to be a recognizable form '
                'that the REPL would honor as a valid sequence.'
            ),
            mapping=(
                'The empty chain, link without cargo, is the empty list. The '
                'form names that emptiness precisely.'
            ),
            resolution=(
                'The REPL saw the empty form and handed back the empty '
                'sequence. The chain without bones was itself a valid row.'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_05 = SubjectCurriculum(grade=4, subject_id="G4-05",
    subject_title="cons — prepend to seq", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(cons 0 '(1 2 3))",
            expected=[0,1,2,3],
            concept_phrase="the cons operation",
            question_what="the seq after cons'ing",
            goal_text="prepend 0 to the front of a list containing 1, 2, and 3",
            scenario=(
                'Bell the hound held a chain of three bones — the counts — linked in sequence. A fourth bone, numbered 0, lay at her feet, ready to be spliced to the front of the chain.'
            ),
            need=(
                'She wanted to attach the 0 bone to the very front of the chain so the linked row would grow to read: zero, the counts.'
            ),
            mapping=(
                'The bone numbered 0 is the value being prepended, the chain '
                '(1 2 3) is the existing sequence, and cons is the splice that '
                'binds them.'
            ),
            resolution=(
                'The REPL stitched the 0 bone to the front of the chain, '
                'creating a new linked sequence. The chain now ran from 0 at '
                'the head through 1, 2, 3 in order — 0.'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_06 = SubjectCurriculum(grade=4, subject_id="G4-06",
    subject_title="Map literal", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="{:hare 1 :tortoise 2}",
            expected={":hare": 1, ":tortoise": 2},
            concept_phrase="a map literal",
            question_what="the map with two entries",
            goal_text="create a map binding the keyword :hare to 1 and :tortoise to 2",
            scenario=(
                'Patch the hound lined up a hollow log with two named '
                'compartments: one for :hare (marked on the bark), one for '
                ':tortoise. Into the first went a single bone; into the second '
                'went two bones.'
            ),
            need=(
                'Patch wanted the labeled compartments and their bone-counts to '
                'be fixed as a single data shape that the REPL could recognize '
                'and return.'
            ),
            mapping=(
                'The hollow log is the map, the two compartment names are the '
                'keywords :hare and :tortoise, and the bone-counts are 1 and 2.'
            ),
            resolution=(
                'The REPL sealed the named compartments exactly as Patch '
                'described, binding each name to its count. The map came back '
                'with both slots in place — tortoise.'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_07 = SubjectCurriculum(grade=4, subject_id="G4-07",
    subject_title="get — map lookup", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(get {:a 1 :b 2} :a)",
            expected=1,
            concept_phrase="map lookup",
            question_what="the value at :a",
            goal_text="look up the value at key :a in a map binding :a to 1 and :b to 2",
            scenario=(
                'Rex the hound faced a hollow log cache with two named '
                'compartments — :a held 1 bone, :b held 2. He wanted to reach '
                'into the compartment named :a and pull out what it held.'
            ),
            need=(
                'He asked the REPL to find the compartment marked :a and hand '
                'back the count of bones resting there.'
            ),
            mapping=(
                'The hollow log is the map {:a 1 :b 2}, the compartment name '
                ':a is the key, and what sits inside is the value.'
            ),
            resolution=(
                'The REPL read the name :a, found the correct compartment, and '
                'handed back the bone-count it held: 1 — a.'
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
                'Bell the hound reached for a hollow log cache that held only '
                'one compartment named :a with 1 bone in it. She asked the REPL '
                'for what rested in a compartment named :missing — which did not '
                'exist — but provided a default fallback marker.'
            ),
            need=(
                'She wanted the REPL to return the fallback value if the named '
                'compartment was not found in the cache.'
            ),
            mapping=(
                'The map is {:a 1}, the missing key :missing names a '
                'compartment that is not there, and the default is the '
                'placeholder handed back when the lookup fails.'
            ),
            resolution=(
                'The REPL looked for :missing in the cache, found nothing, and '
                'returned the default marker instead. The fallback held true — default.'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_08 = SubjectCurriculum(grade=4, subject_id="G4-08",
    subject_title="assoc — map update", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(assoc {:a 1} :b 2)",
            expected={":a": 1, ":b": 2},
            concept_phrase="the assoc operation",
            question_what="the basket after associating value 2 with the :b compartment",
            goal_text="associate value 2 with the :b compartment of a basket already binding :a to 1",
            scenario=(
                'Patch the hound held a hollow log cache with one compartment '
                'named :a that held 1 bone. The cache was ready to receive a '
                'new compartment. Patch marked out a fresh section and labeled '
                'it :b, then placed 2 bones inside.'
            ),
            need=(
                'Patch wanted the REPL to take the existing cache, add the new '
                'compartment :b with its 2 bones, and return the extended cache '
                'without disturbing what :a held.'
            ),
            mapping=(
                'The original hollow log is the map {:a 1}, the new '
                'compartment name is :b, the new bone-count is 2, and assoc is '
                'the operation that adds the slot.'
            ),
            resolution=(
                'The REPL extended the cache by one compartment, placing 2 '
                'bones in the :b slot while :a kept its 1 bone. The expanded '
                'cache came back intact — b.'
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
                'Bell the hound tended a hollow log cache with one compartment '
                'marked :a that held 1 bone. She wanted to replace what was '
                'inside with a much larger heap of 99 bones.'
            ),
            need=(
                'She asked the REPL to update the :a compartment so it now '
                'held 99 instead of 1.'
            ),
            mapping=(
                'The hollow log is {:a 1}, the compartment :a is being revised, '
                'the new bone-count is 99, and assoc performs the substitution.'
            ),
            resolution=(
                'The REPL updated the cache so the :a compartment now held 99 '
                'bones. A new cache with the revised count came back, the old '
                'one left behind — a.'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_09 = SubjectCurriculum(grade=4, subject_id="G4-09",
    subject_title="dissoc — map remove key", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(dissoc {:a 1 :b 2} :a)",
            expected={":b": 2},
            concept_phrase="the dissoc operation",
            question_what="the map after using dissoc to remove a key",
            goal_text="remove the key :a from a map binding :a to 1 and :b to 2",
            scenario=(
                'Rex the hound inspected a hollow log cache holding two '
                'compartments: :a with 1 bone, :b with 2 bones. He decided the '
                ':a compartment was no longer needed and should be sealed shut.'
            ),
            need=(
                'He wanted the REPL to close off the :a compartment completely, '
                'leaving only :b with its 2 bones in the revised cache.'
            ),
            mapping=(
                'The hollow log is {:a 1 :b 2}, the key :a names the '
                'compartment to remove, and dissoc is the operation that seals '
                'it shut.'
            ),
            resolution=(
                'The REPL closed the :a compartment and sealed it from the '
                'cache, leaving only :b standing. The new cache held 2 bones '
                'in a single compartment now — a.'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_10 = SubjectCurriculum(grade=4, subject_id="G4-10",
    subject_title="keys and vals", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(count (keys {:a 1 :b 2 :c 3}))",
            expected=3,
            concept_phrase="counting keys in a map",
            question_what="the number of keys in the map",
            goal_text="count how many keys are in a map binding :a, :b, and :c",
            scenario=(
                'Bell the hound examined a hollow log cache with three labeled '
                'compartments: :a, :b, :c, each holding bones. She wanted to '
                'count only the names, not the bones themselves.'
            ),
            need=(
                'She asked the REPL to list all the compartment names and count '
                'how many existed in the cache.'
            ),
            mapping=(
                'The hollow log is the map {:a 1 :b 2 :c 3}, the keys are the '
                'three names, and the count of keys tells how many '
                'compartments there are.'
            ),
            resolution=(
                'The REPL read off the three compartment names and counted '
                'them: 3 compartments total. The verdict came back as the '
                'running tally — c.'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_11 = SubjectCurriculum(grade=4, subject_id="G4-11",
    subject_title="Set literal", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(count #{1 2 3})",
            expected=3,
            concept_phrase="the size of a set",
            question_what="the size of the set",
            goal_text="count the elements in a set containing 1, 2, and 3",
            scenario=(
                'Patch the hound held three distinct bones near the forest and '
                'wanted to treat them as a unique collection where each bone '
                'was counted only once, no matter how they were arranged.'
            ),
            need=(
                'Patch asked the REPL to count the unique bones in the set and '
                'return that precise tally.'
            ),
            mapping=(
                'The set #{1 2 3} holds three unique elements, and the count '
                'function returns how many distinct bones reside in it.'
            ),
            resolution=(
                'The REPL recognized the three unique bones and counted them: '
                '3. The tally of the set came back as the 3.'
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
                'Rex the hound picked up three bones that all looked alike — '
                'three copies of the same bone, really. He placed them in a set '
                'and wanted to know how many truly distinct bones were there.'
            ),
            need=(
                'He asked the REPL to ignore duplicates and count only the '
                'unique bone in the set.'
            ),
            mapping=(
                'The set #{1 1 1} deduplicates the three copies, leaving a '
                'single unique element. The count function returns 1.'
            ),
            resolution=(
                'The REPL examined the set, saw that all three bones were '
                'identical, and counted only 1 unique member. The running '
                'tally was 1 — 1.'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_12 = SubjectCurriculum(grade=4, subject_id="G4-12",
    subject_title="Set membership", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(contains? #{1 2 3} 2)",
            expected=True,
            concept_phrase="testing set membership",
            question_what="whether an element is in the set using contains?",
            goal_text="check whether 2 is a member of a set containing 1, 2, and 3",
            scenario=(
                'Bell the hound held a set of three bones in a hollow log: 1, 2, '
                'and 3. She wanted to test if the bone numbered 2 was among them.'
            ),
            need=(
                'She asked the REPL whether bone 2 was a member of the set, '
                'expecting a verdict of yes or no.'
            ),
            mapping=(
                'The hollow log is the set #{1 2 3}, the bone 2 is the value '
                'being checked, and contains? is the test.'
            ),
            resolution=(
                'The REPL searched the set for the bone numbered 2, found it, '
                'and returned true. The verdict was certain — 2.'
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
                'Patch the hound held a set of three bones numbered 1, 2, and 3 '
                'in a hollow log. A bone numbered 4 lay outside, and Patch asked '
                'the REPL if bone 4 belonged to the set.'
            ),
            need=(
                'He wanted to know whether the bone numbered 4 was a member of '
                'the cache, expecting the answer to be false since it had never '
                'been placed inside.'
            ),
            mapping=(
                'The set #{1 2 3} holds three bones, the bone 4 is outside the '
                'set, and contains? verifies that bone 4 is not a member.'
            ),
            resolution=(
                'The REPL searched the set and found no bone numbered 4 among '
                'them. It returned false. The bone lay beyond the cache — 4.'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_13 = SubjectCurriculum(grade=4, subject_id="G4-13",
    subject_title="count — universal", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(count [1 2 3 4 5])",
            expected=5,
            concept_phrase="the count of a collection",
            question_what="the number of elements in the collection",
            goal_text="count the elements in a vector containing 1, 2, 3, 4, and 5",
            scenario=(
                'Rex the hound laid out five bones in a hollow log arranged in '
                'a neat row: 1, 2, 3, 4, 5. He wanted the precise count of all '
                'bones in the cache.'
            ),
            need=(
                'He asked the REPL to tally the bones in the vector and return '
                'that running total.'
            ),
            mapping=(
                'The hollow log is [1 2 3 4 5], count examines the vector, and '
                'the result is the bone-count: 5.'
            ),
            resolution=(
                'The REPL counted the five bones in the cache and handed back the '
                'tally: 5. The verdict was the size of the vector — 5.'
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
                'Bell the hound inspected a hollow log with two named '
                'compartments: :a held 1 bone, :b held 2. She wanted to count '
                'the number of compartments, not the bones inside them.'
            ),
            need=(
                'She asked the REPL for the count of compartments in the map.'
            ),
            mapping=(
                'The map is {:a 1 :b 2}, count returns the number of key-value '
                'pairs, and the tally is the number of named slots.'
            ),
            resolution=(
                'The REPL tallied the compartments in the cache: 2 named slots '
                'total. The count came back as 2 — b.'
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
                'Patch the hound gathered three uniquely marked bones in a set: '
                'one marked :a, one marked :b, one marked :c. Each had its own '
                'signal stone.'
            ),
            need=(
                'Patch wanted the REPL to count all the unique signal stones in '
                'the set.'
            ),
            mapping=(
                'The set #{:a :b :c} holds three unique keywords, count tallies '
                'them, and the result is 3.'
            ),
            resolution=(
                'The REPL counted the three unique signal stones and handed back '
                'the tally: 3. Each marker was distinct and counted once — c.'
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
                'Bell the hound read a series of eight scratch-marks left on a '
                'bark-strip: t-o-r-t-o-i-s-e. She wanted to know the exact count '
                'of all the marks.'
            ),
            need=(
                'She asked the REPL to tally every scratch-mark in the string.'
            ),
            mapping=(
                'The bark-strip with scratch-marks is the string "tortoise", '
                'count tallies every mark, and the result is the total: 8.'
            ),
            resolution=(
                'The REPL counted all eight scratch-marks on the bark and handed '
                'back the tally: 8. Each mark was counted in order — tortoise.'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_14 = SubjectCurriculum(grade=4, subject_id="G4-14",
    subject_title="empty?", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(empty? [])",
            expected=True,
            concept_phrase="checking if a collection is empty",
            question_what="whether the collection is empty",
            goal_text="test whether an empty vector is empty",
            scenario=(
                'Rex the hound came upon an empty hollow log cache near the pond '
                'and wanted to ask the REPL if the cache held any bones at all.'
            ),
            need=(
                'He wanted a simple yes-or-no answer: is this cache truly empty?'
            ),
            mapping=(
                'The empty hollow log is [], and empty? is the test that checks '
                'for the absence of bones.'
            ),
            resolution=(
                'The REPL looked inside the empty cache and returned true. The '
                'verdict was certain: no bones lay within.'
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
                'Bell the hound held a hollow log with one bone resting inside '
                'and asked the REPL whether the cache was empty.'
            ),
            need=(
                'She wanted the REPL to confirm that the cache held at least one '
                'bone and was therefore not empty.'
            ),
            mapping=(
                'The hollow log is [1] with a bone inside, and empty? is the '
                'test that checks whether the cache is void.'
            ),
            resolution=(
                'The REPL looked inside and found 1 bone, so it returned false. '
                'The cache was not empty; it held bone-cargo — 1.'
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
                'Patch the hound found a clean bark-strip with no scratch-marks '
                'on it and asked the REPL if the string was void.'
            ),
            need=(
                'Patch wanted to know if the bark-strip held any marks at all.'
            ),
            mapping=(
                'The blank bark-strip is the string "", and empty? tests whether '
                'it contains any scratch-marks.'
            ),
            resolution=(
                'The REPL examined the bark-strip and found no marks, so it returned true. The string was completely empty (with `` as the input value) (with `` as the input value).'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_15 = SubjectCurriculum(grade=4, subject_id="G4-15",
    subject_title="first, rest, last", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(first [10 20 30])",
            expected=10,
            concept_phrase="getting the first element",
            question_what="the first element",
            goal_text="get the first element of a vector containing 10, 20, and 30",
            scenario=(
                'Bell the hound faced a hollow log cache holding three bone-heaps: '
                '10 in the first slot, 20 in the second, 30 in the third. She '
                'wanted the very first heap.'
            ),
            need=(
                'She asked the REPL to pull the first element from the vector and '
                'hand it to her.'
            ),
            mapping=(
                'The hollow log is [10 20 30], first grabs the bone-heap at the '
                'head, and 10 is what comes back.'
            ),
            resolution=(
                'The REPL reached to the front of the cache and pulled out the '
                'first heap: 10 bones. The verdict was the first element — 30.'
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
                'Rex the hound inspected a hollow log with three heaps: 10 in the '
                'first slot, 20 in the middle, 30 at the very end. He wanted the '
                'last heap.'
            ),
            need=(
                'He asked the REPL to pull the last element from the cache.'
            ),
            mapping=(
                'The hollow log is [10 20 30], last grabs the bone-heap at the '
                'tail, and 30 is the result.'
            ),
            resolution=(
                'The REPL reached to the back of the cache and pulled out the '
                'last heap: 30 bones. The tail held the 30.'
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
                'Patch the hound held a hollow log with three heaps: 10, 20, 30. '
                'He wanted to drop the first heap and count how many remained.'
            ),
            need=(
                'Patch asked the REPL to remove the first heap and tally what was '
                'left in the cache.'
            ),
            mapping=(
                'The hollow log is [10 20 30], rest removes the head, and count '
                'tallies what remains: 20 and 30.'
            ),
            resolution=(
                'The REPL dropped the first heap from the cache and counted the '
                'two heaps that remained: 2. The running tally of the rest was '
                'the 30.'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_16 = SubjectCurriculum(grade=4, subject_id="G4-16",
    subject_title="into and conj on collections", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(into [] '(1 2 3))",
            expected=[1,2,3],
            concept_phrase="building a vector from a list",
            question_what="the vector built from a list",
            goal_text="convert a list containing 1, 2, and 3 into a vector",
            scenario=(
                'Bell the hound balanced an empty hollow log under the '
                'gap-in-the-log spanning the stream near the pond. A small '
                'chain of bones — three of them, in order — rested at the '
                'near end, ready to pour through.'
            ),
            need=(
                'She wanted the same three bones to land in the empty '
                'receiver, in their original order, but as a row that could '
                'be read from either end rather than only from the front.'
            ),
            mapping=(
                'The gap is the transducer (here, identity since `into` '
                'carries no xform), the source is the chain of three bones, '
                'the empty receiver below the gap is the vector, and what '
                'lands in it is the result.'
            ),
            resolution=(
                'The REPL ran each bone through the gap and packed it into '
                'the receiving log. The chain above stayed as it had been; '
                'the row below now held the three bones in their original '
                'order — 3.'
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
                'Patch the hound stood at the gap-in-a-log spanning the stream near the pond, holding a row of bones: the counts. Below the gap rested an empty set-shaped cache.'
            ),
            need=(
                'Patch wanted the four bones to pass through the gap one by one, '
                'but the cache below would keep only unique bones, discarding '
                'any duplicates that fell through.'
            ),
            mapping=(
                'The gap in the log is the transducer; the row above is the source; '
                'the set below catches what passes through; the rule of the gap '
                'is uniqueness — only one copy of each bone survives.'
            ),
            resolution=(
                'The REPL fed each bone through the gap. When the second two tried to pass, the set turned it away as a duplicate. The cache filled with three unique bones: the counts — 3.'
            ),
            tags=("story",),
        ),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G4)


G4_17 = SubjectCurriculum(grade=4, subject_id="G4-17",
    subject_title="Immutability — assoc returns new", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(let [m {:a 1}] (assoc m :a 99) m)",
            expected={":a": 1},
            concept_phrase="immutability of maps",
            question_what="the original map after assoc",
            goal_text="demonstrate that assoc returns a new map without modifying the original",
            scenario=(
                'Bell the hound held a hollow log cache in her jaws with one '
                'compartment named :a holding 1 bone. The binding m locked the '
                'cache in place for just this stretch of the crossing.'
            ),
            need=(
                'She wanted to use assoc to update the :a compartment to hold 99 '
                'bones instead, but crucially: the original cache m should remain '
                'untouched after the stretch ended.'
            ),
            mapping=(
                'The hollow log held in the jaws is the map m. The assoc operation '
                'creates a new cache with the updated value, but leaves the '
                'original m unchanged. The two caches are separate things.'
            ),
            resolution=(
                'The REPL created a new cache with 99 bones in the :a slot, but '
                'when Bell consulted m at the end of the stretch, it still held '
                '1 bone. The immutable cache had never been altered — a.'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_18 = SubjectCurriculum(grade=4, subject_id="G4-18",
    subject_title="Equality of vectors and lists", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(= [1 2 3] '(1 2 3))",
            expected=True,
            concept_phrase="testing equality of different collection types",
            question_what="whether vector and list are equal",
            goal_text="test whether a vector with elements 1, 2, 3 equals a list with the same elements",
            scenario=(
                "Rex the hound held two different bone-shapes at the stream's edge: one was a rigid row in a hollow log [1 2 3], the other a linked chain '(1 2 3) with the same bones but a different build. They looked the same at first glance."
            ),
            need=(
                'He wanted to know if the REPL would say the two shapes held equal '
                'contents, even though one was built as a vector and one as a list.'
            ),
            mapping=(
                'The hollow log is the vector [1 2 3], the linked chain is the '
                "list '(1 2 3), and equality looks past the container's shape to "
                'count the contents.'
            ),
            resolution=(
                'The REPL examined both shapes, found the same bones in the same '
                'order, and returned true. Both containers held the same cargo, '
                'and the 3 was equality.'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_19 = SubjectCurriculum(grade=4, subject_id="G4-19",
    subject_title="range and seq", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(count (range 5))",
            expected=5,
            concept_phrase="counting elements in a range",
            question_what="the count of range 0..4",
            goal_text="count how many numbers are generated by a range from 0 to 4",
            scenario=(
                'Bell the hound asked the REPL to generate a range of bones from '
                '0 to 4 — not a cached row, but a virtual sequence that would be '
                'produced on demand.'
            ),
            need=(
                'She wanted to know: how many bones would the range unfold if she '
                'counted them all?'
            ),
            mapping=(
                'The range is a promise of {drawn.a} bones (0, 1, 2, 3, 4), and count consumes that promise one bone at a time, tallying the whole.'
            ),
            resolution=(
                'The REPL worked through the range, counting each bone as it was '
                'produced: 5 total. The verdict was the sum of the sequence — 5.'
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
                'Patch the hound asked the REPL for a range of bones from 1 to 99 '
                '— a virtual row that could stretch very far. The hound wanted only '
                'the very first bone from that sequence.'
            ),
            need=(
                'Patch needed the REPL to pull the first element from the range '
                'without generating all 99 bones, just the one at the head.'
            ),
            mapping=(
                'The range is a lazy promise of bones from 1 onwards, and first '
                'peeks at the head of that sequence without forcing the rest.'
            ),
            resolution=(
                'The REPL looked at the start of the range and handed back 1. No '
                'need to unfold the whole sequence — the first bone came straight '
                'away — 100.'
            ),
            tags=("story",),
        ),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_20 = SubjectCurriculum(grade=4, subject_id="G4-20",
    subject_title="Collection vs sequence", fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(count (seq [1 2 3]))",
            expected=3,
            concept_phrase="creating a sequence from a vector and counting",
            question_what="the count of seq over a vector",
            goal_text="convert a vector containing 1, 2, and 3 to a sequence and count its elements",
            scenario=(
                'Rex the hound held a rigid hollow log cache [1 2 3] in the bank '
                'near the pond. He wanted to turn it into a lazy sequence that '
                'could be stepped through one bone at a time.'
            ),
            need=(
                'He asked the REPL to convert the rigid row into a walkable '
                'sequence and then count all the bones in that sequence.'
            ),
            mapping=(
                'The hollow log is the vector [1 2 3], seq transforms it into a '
                'lazy sequence view, and count tallies how many bones unfold.'
            ),
            resolution=(
                'The REPL converted the vector into a sequence and walked it from '
                'head to tail, counting each bone: 3 total. The verdict was the '
                'size of the sequence — 3.'
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
                'Patch the hound faced an empty hollow log cache near the pond. '
                'The hound asked the REPL to convert it into a sequence, even '
                'though there were no bones to walk.'
            ),
            need=(
                'Patch wanted to know: what does seq return when the cache holds '
                'nothing at all?'
            ),
            mapping=(
                'The empty hollow log [] can be wrapped by seq, but an empty '
                'sequence has no bones to step through and no head to offer.'
            ),
            resolution=(
                'The REPL checked the empty cache and found no bones to sequence. '
                'When there is nothing to walk, seq returns null. The verdict was '
                'nil.'
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
    print(f"grade-4 dog-shadow smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples")


if __name__ == "__main__":
    smoke_test()
