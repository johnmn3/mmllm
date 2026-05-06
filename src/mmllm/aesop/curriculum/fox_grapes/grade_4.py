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
        _ex("[1 2 3]", [1,2,3], 'the form', 'the value the form evaluates to',
            goal='arrange three harvest-baskets in a row',
            scenario='Renard the fox had three woven baskets of grapes from the morning vineyard, each holding a different weight of clusters.',
            need='He wanted to record all three weights in sequence, binding them together in a single tray-form so the ledger would show the complete harvest-row.',
            mapping='A vector form squares-brackets three values into a single ordered collection. Each number slots into its position; the vector keeps the row intact.',
            resolution='the REPL accepted all three weights in their order, lined up on the page exactly as Renard had arranged them on the path.',
            tags=("story",)),
        _ex("[]", [], 'the form', 'the value the form evaluates to',
            goal='declare an empty vine-tray for tomorrow\'s pickings',
            scenario='Vix the fox stood at the orchard gate before the day\'s work, holding a fresh woven tray with no clusters yet.',
            need='She wanted to write the form showing the empty tray—a container ready to receive but holding nothing, to start the harvest-count from zero.',
            mapping='An empty vector form creates a collection with zero slots. The tray itself exists; the row is just not filled.',
            resolution='the REPL confirmed the empty row, marking the ledger\'s starting point before the first grape went into the tray.',
            tags=("story",)),
        _ex("[\"a\" \"b\"]", ["a","b"], 'the form', 'the value the form evaluates to',
            goal='catalog two vine-tags from the left and right terraces',
            scenario='Sly the fox kept records of which vine-section each basket had come from, labeling each with a tag-mark: one for the left terrace, one for the right.',
            need='To organize the inventory, Sly needed to pair the two location-tags into a single ordered row so the sorting-table would know which baskets belonged together.',
            mapping='A vector of two strings binds each label into its position. The vector form names the row; the REPL keeps the sequence intact.',
            resolution='the tray now showed both location-tags lined up in order, ready for Sly to match baskets to their vine-sections.',
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_02 = SubjectCurriculum(grade=4, subject_id="G4-02",
    subject_title="nth — vector access", fable="fox-grapes",
    examples=[
        _ex("(nth [10 20 30] 0)", 10, 'the form', 'the value the form evaluates to',
            goal='fetch the first harvest-count from a row of three morning tallies',
            scenario='Renard lined three baskets on the trellis edge—one with its morning tally, two more added after lunch. Each position held a distinct count.',
            need='The first tally was what mattered for the morning bonus. Renard needed to pluck just that one count from position zero without touching the others.',
            mapping='nth reaches into a vector by its position number (0 for first, 1 for second, etc.). Position zero is always the head; the vector stays on the trellis unchanged.',
            resolution='the first count—exactly the morning\'s weight—came back to Renard\'s ledger.',
            tags=("story",)),
        _ex("(nth [10 20 30] 2)", 30, 'the form', 'the value the form evaluates to',
            goal='pull the last-tallied basket\'s weight from a three-basket row',
            scenario='Vix had three baskets on the path, each with its own weight-count in sequence. The last basket held the afternoon\'s largest gathering.',
            need='Vix wanted to confirm the final weight by naming its position in the row, skipping the first two to reach the tally she needed.',
            mapping='nth with position 2 (the third slot, since counting starts at 0) extracts the third value from the vector. The vector itself rests on the path, untouched.',
            resolution='the afternoon\'s largest weight—position 2\'s value—sat on Vix\'s ledger, verified.',
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_03 = SubjectCurriculum(grade=4, subject_id="G4-03",
    subject_title="conj — append to vector", fable="fox-grapes",
    examples=[
        _ex("(conj [1 2] 3)", [1,2,3], 'the form', 'the value the form evaluates to',
            goal='add a third weight to a two-basket tray to complete the harvest row',
            scenario='Sly had a tray on the trellis with two basket-weights already tallied. A final, smaller basket arrived from the hidden corner of the orchard.',
            need='Sly needed the tray to hold all three weights in order, the new one appended to the end so the row grew without losing what was already there.',
            mapping='conj (conjoin) adds a value to the end of a vector, returning a new tray with the item in its tail position. The old tray remains on the trellis.',
            resolution='the tray now held all three weights in their proper sequence—the original two plus the newcomer, ready for the final ledger entry.',
            tags=("story",)),
        _ex("(conj [] :fox)", [":fox"], 'the form', 'the value the form evaluates to',
            goal='add a single fox-marker to an empty collection-tray',
            scenario='Renard had just gathered an empty tray for a new sorting task. He wanted to mark the very first entry—his own identifier as the gatherer.',
            need='The tray needed to hold his marker :fox alone, the first and only item in a new row, so the ledger would record which fox had begun this particular count.',
            mapping='conj on an empty vector adds the first item to an otherwise bare tray. The vector form creates a one-slot row with the marker in place.',
            resolution='the tray carried the :fox marker as its sole resident, marking Renard as the row\'s author and first entry.',
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_04 = SubjectCurriculum(grade=4, subject_id="G4-04",
    subject_title="List literal", fable="fox-grapes",
    examples=[
        _ex("'(1 2 3)", [1,2,3], 'the form', 'the value the form evaluates to',
            goal='record a procession of three weights as a linked vine-strand',
            scenario='Vix kept her tallies as a long vine-strand rather than a stiff tray—three weights linked head-to-tail like grapes bunched on a single tendril.',
            need='To write down the complete vine-strand, she quoted it so the REPL would treat the numbers as a ready-made sequence, not instructions to evaluate.',
            mapping='A quoted list form creates a procession where each item points to the next. The quote stops evaluation; the list itself becomes the value.',
            resolution='the REPL accepted the three weights as a linked sequence, Vix\'s vine-strand complete and recorded without further ceremony.',
            tags=("story",)),
        _ex("'()", [], 'the form', 'the value the form evaluates to',
            goal='declare an empty vine-strand before adding the day\'s first weight',
            scenario='Renard prepared a new vine-strand for a special sorting task, beginning with no links, no weights—just the empty structure.',
            need='He wanted to quote the empty strand so it would exist as a literal value ready to accept items later, without the REPL trying to evaluate it as code.',
            mapping='A quoted empty list form creates a procession with no links. The quote marks it as data; it evaluates to an empty sequence.',
            resolution='the vine-strand sat ready—empty but present—waiting for the first weight to be joined to it.',
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_05 = SubjectCurriculum(grade=4, subject_id="G4-05",
    subject_title="cons — prepend to seq", fable="fox-grapes",
    examples=[
        _ex("(cons 0 '(1 2 3))", [0,1,2,3], 'the form', 'the value the form evaluates to',
            goal='splice a zero-weight baseline to the head of an existing three-weight vine-strand',
            scenario='Sly had recorded a vine-strand of three afternoon weights. The morning, he realized, had included a baseline check—a zero-weight tare—that belonged at the front.',
            need='Rather than rewrite the strand, Sly wanted to prepend the zero to the head, linking it so the strand would now start with the tare and flow through all the weights.',
            mapping='cons (construct) links a new head to an existing sequence. The new value becomes the first item; the old strand remains the tail, forming one longer procession.',
            resolution='the vine-strand now started with the zero-weight baseline, followed by all three afternoon weights in their original order.',
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_06 = SubjectCurriculum(grade=4, subject_id="G4-06",
    subject_title="Map literal", fable="fox-grapes",
    examples=[
        _ex("{:fox 1 :grapes 2}", {":fox": 1, ":grapes": 2}, 'the form', 'the value the form evaluates to',
            goal='build a tray with named compartments—one labeled :fox for my own take, one labeled :grapes for the co-op share',
            scenario='Renard stood at the end of the harvest day with a decision: how to split the day\'s tallies between his personal ledger and the orchard co-op record.',
            need='He needed a tray with two named slots, :fox holding his count and :grapes holding the co-op\'s allocation. Each label pointed to its own tally.',
            mapping='A map literal creates a tray where keys name slots and values hold the tallies. The curly braces form the tray structure; the colon-prefixed names become the labels.',
            resolution='the tray sat ready with both compartments filled—:fox housing his own count of 1, :grapes holding the co-op\'s share of 2.',
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_07 = SubjectCurriculum(grade=4, subject_id="G4-07",
    subject_title="get — map lookup", fable="fox-grapes",
    examples=[
        _ex("(get {:a 1 :b 2} :a)", 1, 'the form', 'the value the form evaluates to',
            goal='fetch the tally from the :a compartment of a two-slot tray',
            scenario='Vix held a vine-tray with two named slots: :a containing a specific morning count, :b holding an afternoon total. She needed just one.',
            need='Without knowing which compartment held which weight, Vix used the :a label to point directly to the right slot and extract its tally.',
            mapping='get takes a map and a key, reaching into the named compartment and pulling out its value. The tray stays on the trellis; only the value emerges.',
            resolution='the :a compartment\'s value—exactly 1—came back to Vix on her ledger.',
            tags=("story",)),
        _ex("(get {:a 1} :missing :default)", ":default", 'the form', 'the value the form evaluates to',
            goal='look for a :missing label in the tray, but return a fallback tally if it doesn\'t exist',
            scenario='Sly carried a tray with one compartment labeled :a. A counting task asked for :missing, a label that had never been written into the tray.',
            need='Rather than crash or guess, Sly wanted to safely ask for :missing and get a :default placeholder back—proof that the label wasn\'t there.',
            mapping='get with three arguments (map, key, default) searches for a key; if absent, it returns the default value instead of nil.',
            resolution='the :missing label wasn\'t in the tray, so get returned :default as the answer, a safe fallback for labels that don\'t exist.',
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_08 = SubjectCurriculum(grade=4, subject_id="G4-08",
    subject_title="assoc — map update", fable="fox-grapes",
    examples=[
        _ex("(assoc {:a 1} :b 2)", {":a": 1, ":b": 2}, 'the form', 'the value the form evaluates to',
            goal='add a new compartment :b to a one-slot tray while keeping :a intact',
            scenario='Renard had a tray with a single slot :a holding its morning tally. At midday, he had counted a new group of grapes and needed a :b slot.',
            need='Rather than rebuild the tray, Renard wanted to assoc (associate) the new label and value into the existing tray, keeping :a\'s weight unchanged.',
            mapping='assoc takes a map, adds or updates a key-value pair, and returns a fresh tray with both old and new compartments. The original tray rests on the trellis untouched.',
            resolution='the new tray held both :a with its original 1 and :b with the new 2, all in one container ready for the ledger.',
            tags=("story",)),
        _ex("(assoc {:a 1} :a 99)", {":a": 99}, 'the form', 'the value the form evaluates to',
            goal='update the :a compartment\'s tally from an old count to a corrected weight',
            scenario='Vix discovered her :a count had been wrong—she\'d miscounted the morning baskets. A recount gave her 99 instead of the original 1.',
            need='She wanted to replace the old tally with the corrected 99 in the :a slot, fixing the tray\'s record without losing the compartment itself.',
            mapping='assoc with an existing key replaces the old value with the new one. The tray\'s structure stays the same; only the value in that compartment changes.',
            resolution='the :a compartment now held the corrected weight 99, Vix\'s error fixed and the tray ready for the official ledger again.',
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_09 = SubjectCurriculum(grade=4, subject_id="G4-09",
    subject_title="dissoc — map remove key", fable="fox-grapes",
    examples=[
        _ex("(dissoc {:a 1 :b 2} :a)", {":b": 2}, 'the form', 'the value the form evaluates to',
            goal='remove the :a compartment from a two-slot tray, keeping :b\'s tally intact',
            scenario='Sly held a tray with two compartments: :a held a count of 1, :b held a count of 2. A mistake in how :a was gathered meant that slot needed to go.',
            need='Rather than discard the whole tray, Sly wanted to dissociate (remove) the :a label and its value, leaving :b alone and unharmed.',
            mapping='dissoc removes a key from a map, returning a fresh tray without that compartment. The original tray stays on the trellis; the new one has fewer slots.',
            resolution='the returned tray held only :b with its value of 2. The :a compartment was gone, and the ledger could proceed with a cleaner record.',
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_10 = SubjectCurriculum(grade=4, subject_id="G4-10",
    subject_title="keys and vals", fable="fox-grapes",
    examples=[
        _ex("(count (keys {:a 1 :b 2 :c 3}))", 3, 'the form', 'the value the form evaluates to',
            goal='count how many named compartments are stitched into a three-slot tray',
            scenario='Renard finished a complex sorting task with a tray bearing three compartment labels: :a for the home share, :b for the co-op, :c for trade.',
            need='To verify the tray was complete, Renard wanted to count the labels themselves—not the tallies inside, but how many slots existed.',
            mapping='keys extracts all the label-names from a map into a sequence; count tallies how many labels are present. The tray stays in place; only the label-count emerges.',
            resolution='the REPL counted three labels, confirming that all three compartments—:a, :b, :c—were present and accounted for.',
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_11 = SubjectCurriculum(grade=4, subject_id="G4-11",
    subject_title="Set literal", fable="fox-grapes",
    examples=[
        _ex("(count #{1 2 3})", 3, 'the form', 'the value the form evaluates to',
            goal='count distinct varieties in a set of three different grape types',
            scenario='Vix gathered three distinct grape varieties for the pressing house: variety 1 from the north field, 2 from the west, 3 from the south slope.',
            need='The head presser wanted to know how many unique types were in the batch. A set keeps only distinct items; counting them would give the variety count.',
            mapping='A set form (curly braces with a hash) holds only unique values—duplicates are silently merged. count on a set yields the number of distinct items.',
            resolution='the set held all three distinct varieties, and count returned 3, confirming the batch was genuinely mixed.',
            tags=("story",)),
        _ex("(count #{1 1 1})", 1, 'the form', 'the value the form evaluates to',
            goal='confirm that three identical weight-entries collapse into a single unique item in a set',
            scenario='Sly recorded three identical weight measurements from the same vine cluster—1, 1, 1—trying to put them all into a set to verify they were truly the same.',
            need='The test was to see whether the set would keep all three or merge them into one. A set admits no duplicates, only the unique value.',
            mapping='A set automatically deduplicates entries. When all three values are identical, the set holds only one; count reveals this collapse.',
            resolution='the set contained only one distinct value (the number 1), and count returned 1, proving that identical entries merge in a set.',
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_12 = SubjectCurriculum(grade=4, subject_id="G4-12",
    subject_title="Set membership", fable="fox-grapes",
    examples=[
        _ex("(contains? #{1 2 3} 2)", True, 'the form', 'the value the form evaluates to',
            goal='verify that variety 2 is part of a three-variety set',
            scenario='Renard held a set of three distinct grape varieties: 1, 2, 3. A customer asked whether variety 2 was in the batch.',
            need='Rather than search by hand, Renard wanted to ask the set directly: does it contain the value 2? The answer would be a simple yes or no.',
            mapping='contains? checks whether a set holds a specific value. The set stays intact; the result is a true or false answer.',
            resolution='the set did contain variety 2, and contains? returned true, so Renard could confirm it to the customer.',
            tags=("story",)),
        _ex("(contains? #{1 2 3} 4)", False, 'the form', 'the value the form evaluates to',
            goal='confirm that variety 4 is NOT in a set of varieties 1, 2, and 3',
            scenario='Vix held a set containing three varieties. A supplier offered to deliver variety 4, but Vix wanted to check if she already had it.',
            need='Using contains?, she could ask whether 4 was already in her set. If not, she could safely order it without doubling up.',
            mapping='contains? searches a set for a value. If the value isn\'t present, it returns false. The set is unchanged; only the membership answer emerges.',
            resolution='variety 4 was not in the set, so contains? returned false. Vix knew it was safe to add the new variety to her supply.',
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_13 = SubjectCurriculum(grade=4, subject_id="G4-13",
    subject_title="count — universal", fable="fox-grapes",
    examples=[
        _ex("(count [1 2 3 4 5])", 5, 'the form', 'the value the form evaluates to',
            goal='count five distinct basket-weights arranged in a row-vector',
            scenario='Sly lined five baskets on the trellis, each with a different weight. He wanted to verify that all five baskets were accounted for.',
            need='count would tally the items in the vector quickly, giving him a number to match against his physical row of baskets.',
            mapping='count works on any collection, including vectors. It returns the number of items in order, one for each slot.',
            resolution='count returned 5, confirming all five baskets were recorded in the vector.',
            tags=("story",)),
        _ex("(count {:a 1 :b 2})", 2, 'the form', 'the value the form evaluates to',
            goal='count how many key-value pairs are stored in a two-compartment tray',
            scenario='Renard held a map with two compartments: :a and :b. He needed a quick way to verify both slots were filled.',
            need='count on a map counts the number of key-value pairs (the number of compartments). This works as a sanity check on the tray\'s structure.',
            mapping='count on a map returns the number of entries (keys). Each compartment counts as one, regardless of its value.',
            resolution='count returned 2, confirming both :a and :b slots were present with their values.',
            tags=("story",)),
        _ex("(count #{:a :b :c})", 3, 'the form', 'the value the form evaluates to',
            goal='count three distinct variety-names in a set',
            scenario='Vix cataloged three distinct grape varieties as keywords in a set: :a, :b, :c. She wanted a single count to confirm variety of her stock.',
            need='count on a set returns the number of distinct items. Sets deduplicate, so this count is always exact for unique values.',
            mapping='count on a set returns the number of unique items it holds. Duplicates are merged, so the count reflects only the distinct members.',
            resolution='count returned 3, confirming three unique varieties were in Vix\'s catalog.',
            tags=("story",)),
        _ex("(count \"grapes\")", 6, 'the form', 'the value the form evaluates to',
            goal='count the characters (letters) in the word "grapes" to verify its written length',
            scenario='Renard was labeling a container and wanted to confirm the character count in the word "grapes" for spacing the label text.',
            need='count on a string returns the number of characters, one for each letter including any spaces or punctuation.',
            mapping='count on a string returns its length—the number of characters it contains. Each character is one item in the string.',
            resolution='count returned 6, confirming "grapes" has exactly six letters for Renard\'s label layout.',
            tags=("story",)),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_14 = SubjectCurriculum(grade=4, subject_id="G4-14",
    subject_title="empty?", fable="fox-grapes",
    examples=[
        _ex("(empty? [])", True, 'the form', 'the value the form evaluates to'),
        _ex("(empty? [1])", False, 'the form', 'the value the form evaluates to'),
        _ex("(empty? \"\")", True, 'the form', 'the value the form evaluates to'),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_15 = SubjectCurriculum(grade=4, subject_id="G4-15",
    subject_title="first, rest, last", fable="fox-grapes",
    examples=[
        _ex("(first [10 20 30])", 10, 'the form', 'the value the form evaluates to'),
        _ex("(last  [10 20 30])", 30, 'the form', 'the value the form evaluates to'),
        _ex("(count (rest [10 20 30]))", 2, 'the form', 'the value the form evaluates to'),
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
        _ex("(into #{} [1 2 2 3])", [1,2,3], 'the form', 'the value the form evaluates to'),
    ], subplots=_SIEVE_SUBPLOTS, plan_pool=_PLAN_G4)


G4_17 = SubjectCurriculum(grade=4, subject_id="G4-17",
    subject_title="Immutability — assoc returns new", fable="fox-grapes",
    examples=[
        _ex("(let [m {:a 1}] (assoc m :a 99) m)", {":a": 1}, 'the form', 'the value the form evaluates to'),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_18 = SubjectCurriculum(grade=4, subject_id="G4-18",
    subject_title="Equality of vectors and lists", fable="fox-grapes",
    examples=[
        _ex("(= [1 2 3] '(1 2 3))", True, 'the form', 'the value the form evaluates to'),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_19 = SubjectCurriculum(grade=4, subject_id="G4-19",
    subject_title="range and seq", fable="fox-grapes",
    examples=[
        _ex("(count (range 5))", 5, 'the form', 'the value the form evaluates to'),
        _ex("(first (range 1 100))", 1, 'the form', 'the value the form evaluates to'),
    ], subplots=_BASKET_SUBPLOTS, plan_pool=_PLAN_G4)


G4_20 = SubjectCurriculum(grade=4, subject_id="G4-20",
    subject_title="Collection vs sequence", fable="fox-grapes",
    examples=[
        _ex("(count (seq [1 2 3]))", 3, 'the form', 'the value the form evaluates to'),
        _ex("(seq [])", None, 'the form', 'the value the form evaluates to'),
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
