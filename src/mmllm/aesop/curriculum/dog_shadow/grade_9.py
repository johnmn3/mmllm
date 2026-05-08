"""Grade 9 — state and concurrency primitives. Through dog-shadow.

The fable's moral dynamic — Tortoise's careful, transactional updates
versus Hare's racing-without-coordination — maps cleanly onto the
state-and-concurrency primitives. Tortoise insists on dosync and CAS;
Hare wants to mutate without checking. The REPL settles every dispute.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.dog_shadow.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.dog_shadow._metaphor_pools import (
    _BASKET_SUBPLOTS, _NOTEBOOK_SUBPLOTS, _RUNNERAHEAD_SUBPLOTS,
)


# ─────────────────────── grade-9 subplot pool ───────────────────────
#
# Use goal-style subplots exclusively for grade 9. State and concurrency
# primitives require the model to write the form from the goal, not copy
# from prompt — this prevents form-leak training pathology.

_SUBPLOTS: list[SubplotTemplate] = _GOAL_SUBPLOTS


def _ex(form, expected, concept, what, goal="", tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal, tags=tags)


_PLAN_POOL_G9: tuple[str, ...] = _PLAN_POOL + (
    "I bind the state, perform the update, then dereference.",
    "I wrap the def, the update, and the deref together in a do block.",
    "I let the runtime mediate the change before reading the final value.",
)


# ─────────────────────── 18 grade-9 subjects ───────────────────────


# G9-01 — Immutability review
G9_01 = SubjectCurriculum(
    grade=9, subject_id="G9-01",
    subject_title="Immutability as default — review",
    fable="dog-shadow",
    examples=[
        # `assoc` returns a new map; the original is unchanged.
        SubjectExample(
            form="(let [m {:a 1}] (assoc m :b 2) m)",
            expected={":a": 1},
            concept_phrase="binding a map, adding an entry to a new map, and returning the original",
            question_what="the original map after assoc returns a new map",
            goal_text="bind a map m, call assoc to add :b 2 to a new map, then return the unchanged m",
            scenario=(
                'Bell the hound kept a bone-cache in a hollow log, with a '
                'slot marked :a holding one bone. She fetched the cache, '
                'considered adding another slot :b with two bones, but '
                'paused — what would the original cache say?'
            ),
            need=(
                'She wanted to know whether calling assoc would change the '
                'cache she had in jaw, or whether the old cache would sit '
                'untouched while a new one was created beside it.'
            ),
            mapping=(
                'The hollow-log cache is the map, the named slots are the '
                'keys, the bones in each slot are the values, assoc is the '
                'motion of adding a new slot to a fresh copy, and returning '
                'the original cache is what happens when you ask for m again.'
            ),
            resolution=(
                'The REPL showed the original cache unchanged — still just '
                'the :a slot with one bone. The new slot :b had been added '
                'to a copy in the REPL\'s paw, not to the cache Bell held — b.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(let [v [1 2 3]] (conj v 4) v)",
            expected=[1, 2, 3],
            concept_phrase="binding a vector, conjoining a new element to a new vector, and returning the original",
            question_what="the original vector after conj returns a new vector",
            goal_text="bind a vector v, call conj to add 4 to a new vector, then return the unchanged v",
            scenario=(
                'Rex the hound lined up the bones by the stream bank. He considered adding a fourth, but wondered if the original would hold steady.'
            ),
            need=(
                'He wanted conj to leave his bones untouched while building a '
                'new row elsewhere.'
            ),
            mapping=(
                'The row of bones is the vector, conj appends to a fresh copy, '
                'and asking for v shows the original stayed put.'
            ),
            resolution=(
                'The REPL returned the original row of the bones. The fourth had been conjoined to a copy, not to the row Rex held — 4.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_BASKET_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-02 — Why state at all
G9_02 = SubjectCurriculum(
    grade=9, subject_id="G9-02",
    subject_title="Why state at all",
    fable="dog-shadow",
    examples=[
        # The minimal "place that needs identity over time" example.
        SubjectExample(
            form="(do (def counter (atom 0)) (swap! counter inc) @counter)",
            expected=1,
            concept_phrase="binding an atom to counter, atomically incrementing it, and dereferencing the result",
            question_what="the value after atomically swapping counter with inc and dereferencing",
            goal_text="construct an atom holding 0 as counter, atomically swap it by applying inc, and dereference the result",
            scenario=(
                "A flat tally-stone sat at the stream's edge near the "
                "pack's morning route. Bell the hound chose it as the day's "
                'running counter and scratched a fresh zero into it as the '
                'starting tally for the season.'
            ),
            need=(
                'When the next dog passed and a bone was added to the '
                'cache, the count on the stone would need to step up by one '
                '— and any pack member arriving later should see the new '
                'tally, not the old.'
            ),
            mapping=(
                'The stone is the atom, the scratched count is its current '
                'value, swap! is the read-apply-write motion in one go, inc '
                'is the change applied, and dereferencing is just looking '
                'at what the stone now says.'
            ),
            resolution=(
                'The REPL applied the update atomically, scratched the new '
                'tally into the stone, and handed back what the stone now '
                'read. Any later dog at the bank would see the same updated '
                'count — 0.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def progress (atom :idle)) (reset! progress :running) @progress)",
            expected=":running",
            concept_phrase="binding an atom to progress, atomically resetting it to a new value, and dereferencing the result",
            question_what="the value after atomically resetting progress and dereferencing",
            goal_text="construct an atom holding an idle value as progress, atomically reset it to running, and dereference the result",
            scenario=(
                'Patch the hound maintained a tally-scratch on a flat stone '
                'by the bank, marked with the keyword idle at the start of '
                'the day. When the foraging party was ready to begin, the '
                'hound reset the stone\'s value outright to running.'
            ),
            need=(
                'The status needed to shift from idle to running in one '
                'atomic motion — no partial state, no half-updates — so any '
                'watching dog would see either the old value or the new one, '
                'never a blur between.'
            ),
            mapping=(
                'The stone is the atom, the scratched keyword is its value, '
                'reset! is the unconditional write in one atomic stroke, and '
                'dereferencing asks the stone for what it now says.'
            ),
            resolution=(
                'The REPL reset the stone from idle to running and handed back the new keyword. The running status was now clear to any pack member who read the bank — running (with `:idle` as the input value).'
            ),
            tags=("story",),
        ),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-03 — Atom introduction
G9_03 = SubjectCurriculum(
    grade=9, subject_id="G9-03",
    subject_title="Atom introduction",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(do (def a (atom 0)) (swap! a inc) @a)",
            expected=1,
            concept_phrase="the swap-then-deref pattern on an atom",
            question_what="the running tally on the page after one foraging contribution",
            goal_text="set up a shared notebook starting at 0, atomically add one to its page, then read the page",
            scenario=(
                'Bell the hound opened the shared notebook at the stream\'s '
                'edge and scratched a fresh zero onto the first page. This '
                'tally-stone would record how many bones the pack had '
                'gathered as the day unfolded.'
            ),
            need=(
                'When a bone was found and brought to the cache, the tally '
                'would need to step up by one — atomically, in one '
                'read-compute-write moment — so no two dogs could garble the '
                'count by writing at once.'
            ),
            mapping=(
                'The page is the atom, the scratched number is its current '
                'value, swap! is the atomic read-and-write dance that '
                'applies inc to what the stone holds, and dereferencing '
                'reads what the stone now says.'
            ),
            resolution=(
                'The REPL swapped the zero to one in a single stroke, and '
                'the page showed the new tally. Each bone added would '
                'increment the count further, safely, one at a time — 0.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def a (atom 10)) (swap! a + 5) @a)",
            expected=15,
            concept_phrase="the swap-then-deref pattern on an atom",
            question_what="the value returned by dereferencing a after defining a as an atom holding 10 and swapping it via + 5",
            goal_text="construct an atom holding 10, atomically swap it by applying + to 5, and dereference the result",
            scenario=(
                'Rex the hound carried a running tally on a flat stone by '
                'the bank, already marked with the count 10 from the '
                'previous round. Now the pack had five more bones to add to '
                'the total from this stretch.'
            ),
            need=(
                'He would apply the + function to add five to what the stone '
                'held, doing it atomically in one swap so the tally would '
                'jump cleanly from old to new without any watcher seeing a '
                'partial number.'
            ),
            mapping=(
                'The stone is the atom holding 10, swap! reads that value '
                'and applies + with 5 to it, all in one atomic move, and '
                'the deref at the end confirms the result of the addition.'
            ),
            resolution=(
                'The REPL swapped the 10 to 15 by applying plus-five, and '
                'the stone showed the new running total. The count was now '
                'accurate and safe from any race — 5.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def a (atom :start)) (reset! a :done) @a)",
            expected=":done",
            concept_phrase="the reset-then-deref pattern on an atom",
            question_what="the value returned by dereferencing a after defining a as an atom holding a start keyword and resetting it to done",
            goal_text="construct an atom holding a start keyword, atomically reset it to a done keyword, and dereference the result",
            scenario=(
                'Patch the hound marked the phase-stone near the pond with '
                'the status keyword :start, signaling that the forage was '
                'beginning. When the pack had gathered enough bones and '
                'were ready to rest, the status would need to flip.'
            ),
            need=(
                'The reset would replace the status keyword entirely and '
                'atomically — no slow transition, just a sharp flip from '
                'start to done so every watcher would instantly know the '
                'phase had changed.'
            ),
            mapping=(
                'The stone is the atom, the keyword is its value, reset! is '
                'the unconditional atomic replacement with the new keyword, '
                'and dereferencing shows what the stone now holds.'
            ),
            resolution=(
                'The REPL reset the stone to :done in one atomic pulse, and '
                'the page showed the new status. The pack could read the '
                'change clearly and move to their rest — done.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-04 — Atom CAS semantics
G9_04 = SubjectCurriculum(
    grade=9, subject_id="G9-04",
    subject_title="Atom CAS semantics",
    fable="dog-shadow",
    examples=[
        # `compare-and-set!` succeeds when current matches expected.
        SubjectExample(
            form="(do (def a (atom 0)) (compare-and-set! a 0 1) @a)",
            expected=1,
            concept_phrase="the compare-and-set pattern on an atom",
            question_what="the value returned by dereferencing a after defining a as an atom holding 0 and performing a successful compare-and-set to 1",
            goal_text="construct an atom holding 0, perform a compare-and-set checking for 0 and setting to 1, and dereference",
            scenario=(
                'Bell the hound scratched a tally for zero on a stone. She '
                'wanted to update to one, but only if the stone still held zero.'
            ),
            need=(
                'She needed a compare-and-set: a guarded atomic update that '
                'checked the old value before committing the new one.'
            ),
            mapping=(
                'The stone is the atom, the expected value is zero, the new value '
                'is one, and compare-and-set! is the guarded swap.'
            ),
            resolution=(
                'The REPL checked the stone, found zero, and swapped it to one '
                'atomically. The dereference showed the new count — 1.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def a (atom 5)) (compare-and-set! a 0 99) @a)",
            expected=5,
            concept_phrase="the failed-CAS pattern on an atom",
            question_what="the value returned by dereferencing a after defining a as an atom holding 5 and attempting a compare-and-set that fails",
            goal_text="construct an atom holding 5, perform a compare-and-set checking for 0 and setting to 99, and dereference",
            scenario=(
                'Rex read a tally-stone expecting zero. He prepared a '
                'compare-and-set to change it to 99. But another dog had '
                'scratched it — the count now showed 5.'
            ),
            need=(
                'The compare-and-set would find the mismatch and refuse to '
                'write. The stone would stay at its actual value.'
            ),
            mapping=(
                'The stone is the atom at 5, the expected value is zero, the '
                'new value is 99, and compare-and-set! fails when they mismatch.'
            ),
            resolution=(
                'The REPL checked the stone, found 5 not zero, and refused the '
                'swap. The stone remained unchanged — 99.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-05 — Watch on atom
G9_05 = SubjectCurriculum(
    grade=9, subject_id="G9-05",
    subject_title="Watch on atom",
    fable="dog-shadow",
    examples=[
        # A watch can record into another atom each time the watched atom
        # changes; we read the recording atom at the end.
        SubjectExample(
            form=(
                "(do (def a (atom 0))"
                " (def log (atom []))"
                " (add-watch a :w (fn [_ _ _ n] (swap! log conj n)))"
                " (swap! a inc)"
                " @log)"
            ),
            expected=[1],
            concept_phrase="atom with watch",
            question_what="the log vector after defining an atom a, defining a log atom, adding a watch that records each new value, swapping a, and dereferencing the log",
            goal_text="construct an atom a, construct a log atom, add a watch to a that conjoins new values to the log, swap a, and dereference the log",
            scenario=(
                'Bell kept a tally-stone and a log bone-row by the bank. She '
                'attached a watch so the log would record each tally change.'
            ),
            need=(
                'Every change would trigger the watch to append the new value to '
                'the log. After the swap, the log would hold a record.'
            ),
            mapping=(
                'The tally-stone is the atom a, the log bone-row is the atom '
                'holding a vector, add-watch sets a function that fires on change.'
            ),
            resolution=(
                'The REPL attached the watch, then swapped the tally. The watch fired and appended the new value. The log showed the record (with `:w` as the input value).'
            ),
            tags=("story",),
        ),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-06 — Validator on atom
G9_06 = SubjectCurriculum(
    grade=9, subject_id="G9-06",
    subject_title="Validator on atom",
    fable="dog-shadow",
    examples=[
        # A validator gates updates; we set one then read the value.
        SubjectExample(
            form=(
                "(do (def a (atom 0))"
                " (set-validator! a number?)"
                " (swap! a inc)"
                " @a)"
            ),
            expected=1,
            concept_phrase="atom with validator",
            question_what="the value returned by dereferencing a after defining an atom, setting a number? validator, swapping by applying inc, and dereferencing",
            goal_text="construct an atom holding 0, set a number? validator on it, atomically swap by applying inc, and dereference",
            scenario=(
                'Patch the hound scratched a tally-stone at the stream\'s '
                'edge and wanted to ensure only numbers would ever be written '
                'to it. They attached a guardian rule: number? — a check that '
                'would block any word-value or bad symbol from ever being '
                'scratched there.'
            ),
            need=(
                'When inc was applied to the zero on the stone, the result '
                'would be checked against the number? guard. Since one is a '
                'number, the swap would succeed, and the stone would show the '
                'new count.'
            ),
            mapping=(
                'The stone is the atom, the guardian rule is the number? '
                'validator, and swap! performs a guarded update that fires '
                'the validator before committing the new value.'
            ),
            resolution=(
                'The REPL set the validator, then swapped the stone by applying inc. The guard checked the result — one is a number — and the swap succeeded. The dereference showed the stone held the count, protected by the rule (with `0` as the input value).'
            ),
            tags=("story",),
        ),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-07 — Ref introduction
G9_07 = SubjectCurriculum(
    grade=9, subject_id="G9-07",
    subject_title="Ref introduction",
    fable="dog-shadow",
    examples=[
        # Refs require dosync to update.
        SubjectExample(
            form="(do (def r (ref 0)) (dosync (alter r inc)) @r)",
            expected=1,
            concept_phrase="the dosync-alter-deref pattern on a ref",
            question_what="the value returned by dereferencing r after defining a ref holding 0, performing a transactional alter via inc, and dereferencing",
            goal_text="construct a ref holding 0, perform a transactional alter by applying inc inside dosync, and dereference",
            scenario=(
                'Bell the hound kept a ref notebook at the stream\'s edge, a '
                'page marked with zero for the day\'s beginning. Unlike the '
                'atom tally-stone, this ref would require a full transaction '
                'to change it — a dosync fence to guard the update.'
            ),
            need=(
                'She would enter the transaction fence, read the page and '
                'apply inc to step it up, and only then commit the change. If '
                'any conflict arose, the entire transaction would retry, '
                'never leaving a partial state on the page.'
            ),
            mapping=(
                'The ref notebook is the identity that holds a value across '
                'transactions, dosync is the fence that bounds the '
                'transaction, alter reads the page and applies inc, and '
                'dereferencing shows the result after the transaction '
                'commits.'
            ),
            resolution=(
                'The REPL opened the dosync fence, altered the page from '
                'zero to one inside the transaction, committed the change, '
                'and handed back what the page now held. The zero became one '
                'safely within the fence — 0.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def r (ref 100)) (dosync (ref-set r 7)) @r)",
            expected=7,
            concept_phrase="the dosync-ref-set-deref pattern on a ref",
            question_what="the value returned by dereferencing r after defining a ref holding 100, setting it to 7 inside dosync, and dereferencing",
            goal_text="construct a ref holding 100, perform a transactional ref-set to 7 inside dosync, and dereference",
            scenario=(
                "The ref notebook had held a large tally from a "
                "previous season's count. At the start of a new "
                "accounting period the head forager decided to "
                "overwrite the page entirely with a fresh small number, "
                "ignoring what was there before."
            ),
            need=(
                "The new tally needed to replace the old page "
                "outright — not increment it, not compare it, but "
                "set it unconditionally inside the transaction fence."
            ),
            mapping=(
                "`ref-set` sets the ref's value directly to the given "
                "number, without reading the old page first. The "
                "`dosync` fence keeps the replacement transactional. "
                "`@r` confirms the page carries the new value."
            ),
            resolution=(
                "The page showed the fresh small tally — the old "
                "season's count was gone, replaced cleanly within "
                "the transaction — 7."
            ),
            tags=("story",),
        ),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-08 — dosync / alter
G9_08 = SubjectCurriculum(
    grade=9, subject_id="G9-08",
    subject_title="dosync and alter",
    fable="dog-shadow",
    examples=[
        # Two refs altered atomically inside one dosync.
        SubjectExample(
            form=(
                "(do (def a (ref 1)) (def b (ref 2))"
                " (dosync (alter a inc) (alter b inc))"
                " [@a @b])"
            ),
            expected=[2, 3],
            concept_phrase="two refs, coordinated alter",
            question_what="the pair of values returned by dereferencing both a and b after defining them as refs, coordinating their alters inside dosync, and dereferencing",
            goal_text="construct refs a and b, perform a coordinated transaction that alters both by applying inc, and dereference both",
            scenario=(
                'Rex kept two ref notebooks at the stream\'s edge — one at one, '
                'another at two. Both counts needed to step up together.'
            ),
            need=(
                'He would enter a dosync fence and alter both pages, applying inc '
                'to each. Both changes would retry together if needed.'
            ),
            mapping=(
                'The notebooks are refs a and b, dosync is the fence that '
                'coordinates both changes, alter applies inc to each page.'
            ),
            resolution=(
                'The REPL opened the dosync, altered both pages, and committed together. Both values advanced safely inside the transaction (with `1` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def r (ref 10)) (dosync (alter r + 5)) @r)",
            expected=15,
            concept_phrase="the dosync-alter-deref pattern on a ref",
            question_what="the value returned by dereferencing r after defining a ref holding 10, performing a transactional alter via + 5, and dereferencing",
            goal_text="construct a ref holding 10, perform a transactional alter by applying + with 5 inside dosync, and dereference",
            scenario=(
                'Patch the hound held a ref notebook showing a tally of ten '
                'bones from the previous round. Now five more bones had been '
                'gathered, and the page needed to be updated within a full '
                'transaction to maintain consistency.'
            ),
            need=(
                'Inside a dosync fence, the page would be altered by applying '
                'plus-five to its value. The fence ensured that if any '
                'conflict arose during the update, the whole operation would '
                'retry cleanly.'
            ),
            mapping=(
                'The ref notebook holds ten, dosync opens the transaction '
                'fence, alter reads the page and applies plus-five, and '
                'dereferencing shows the result.'
            ),
            resolution=(
                'The REPL opened the dosync, altered the page from ten to '
                'fifteen by adding five, committed the change, and handed '
                'back the new count. The transaction was complete and safe — 5.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-09 — Ref vs atom
G9_09 = SubjectCurriculum(
    grade=9, subject_id="G9-09",
    subject_title="Ref vs atom",
    fable="dog-shadow",
    examples=[
        # The same operation expressed both ways.
        SubjectExample(
            form="(do (def a (atom 0)) (swap! a inc) @a)",
            expected=1,
            concept_phrase="the swap-then-deref pattern on an atom",
            question_what="the value returned by dereferencing a after defining an atom holding 0, swapping it via inc, and dereferencing",
            goal_text="construct an atom holding 0, atomically swap it by applying inc, and dereference",
            scenario=(
                'Bell the hound kept an atom tally-stone at the stream\'s '
                'edge, marked with zero at the start of the day. The stone '
                'would track a simple, independent count — when a bone was '
                'found, the count would step up by one.'
            ),
            need=(
                'She would atomically swap the stone by applying inc, doing '
                'the read-and-write in one go without a fence, since this '
                'count had no dependency on any other state.'
            ),
            mapping=(
                'The atom is the lightweight tally-stone, swap! is the '
                'atomic read-compute-write that applies inc, and '
                'dereferencing shows the result.'
            ),
            resolution=(
                'The REPL swapped the stone from zero to one atomically, and '
                'the dereference showed the new count. The atom was simple, '
                'fast, and safe for a standalone tally — 0.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def r (ref 0)) (dosync (alter r inc)) @r)",
            expected=1,
            concept_phrase="the dosync-alter-deref pattern on a ref",
            question_what="the value returned by dereferencing r after defining a ref holding 0, altering it via inc inside dosync, and dereferencing",
            goal_text="construct a ref holding 0, perform a transactional alter by applying inc inside dosync, and dereference",
            scenario=(
                'Rex the hound kept a ref notebook at the stream\'s edge, '
                'marked with zero. This notebook might be coordinated with '
                'other pages in future transactions, so he required the full '
                'dosync fence from the start.'
            ),
            need=(
                'He would enter a dosync transaction and alter the page inside '
                'the fence by applying inc. Even for a single ref, the dosync '
                'ensured the operation could coordinate with others later if '
                'needed.'
            ),
            mapping=(
                'The ref is the notebook that may join future transactions, '
                'dosync is the fence, alter reads and applies inc inside the '
                'fence, and dereferencing shows the result.'
            ),
            resolution=(
                'The REPL opened the dosync, altered the page from zero to '
                'one inside the fence, and handed back 0. The ref '
                'was ready for coordinated transactions anytime.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-10 — Agent introduction
G9_10 = SubjectCurriculum(
    grade=9, subject_id="G9-10",
    subject_title="Agent introduction",
    fable="dog-shadow",
    examples=[
        # send is async — we await before reading.
        SubjectExample(
            form="(do (def ag (agent 0)) (send ag inc) (await ag) @ag)",
            expected=1,
            concept_phrase="the send-await-deref pattern on an agent",
            question_what="the value returned by dereferencing ag after defining an agent holding 0, sending inc asynchronously, awaiting, and dereferencing",
            goal_text="construct an agent holding 0, asynchronously send inc to it, await its completion, and dereference",
            scenario=(
                'Bell the hound dispatched a young scout-dog along the bank '
                "near the pond — an instruction in jaws to step the scout's "
                'tally up by one — while she stayed back arranging the next '
                'bit of work.'
            ),
            need=(
                "She would not look at the scout's satchel until the scout "
                'had returned — patience first — and only then ask for the '
                'value carried back.'
            ),
            mapping=(
                'The scout is the agent, the instruction is the function '
                'sent, the await is synchronization, and the dereference '
                "asks for the scout's final value."
            ),
            resolution=(
                'The REPL coordinated the scout, awaited its completion, '
                'and handed back 0 the scout had delivered. Bell '
                'read it without snatching too early.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)",
            expected=15,
            concept_phrase="the send-await-deref pattern on an agent",
            question_what="the value returned by dereferencing ag after defining an agent holding 5, sending + 10 asynchronously, awaiting, and dereferencing",
            goal_text="construct an agent holding 5, asynchronously send + with 10 to it, await its completion, and dereference",
            scenario=(
                'Patch the hound dispatched a young scout-dog along the bank '
                'near the pond with an instruction to add 10 to a starting '
                'tally of 5. The scout ran ahead while Patch stayed back, '
                'knowing the work would finish in the scout\'s own time.'
            ),
            need=(
                'Patch would wait for the scout to return — await would '
                'synchronize on the agent\'s completion — and only then ask '
                'for the result. The scout carried the final tally back: '
                'fifteen.'
            ),
            mapping=(
                'The agent is the scout-dog carrying out the work in parallel, '
                'send is the instruction to add ten, await is the '
                'synchronization that lets the pack wait for the scout\'s '
                'return, and dereference gets the result.'
            ),
            resolution=(
                'The REPL sent the instruction, the scout worked asynchronously '
                'adding 10 to 5, await brought Patch back into sync with the '
                'result, and the dereference showed the final tally of fifteen — 10.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_RUNNERAHEAD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-11 — send / send-off
G9_11 = SubjectCurriculum(
    grade=9, subject_id="G9-11",
    subject_title="send and send-off",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(do (def ag (agent 0)) (send ag inc) (await ag) @ag)",
            expected=1,
            concept_phrase="the send-await-deref pattern on an agent",
            question_what="the value returned by dereferencing ag after defining an agent holding 0, using send to dispatch inc, awaiting, and dereferencing",
            goal_text="construct an agent holding 0, use send to asynchronously apply inc, await its completion, and dereference",
            scenario=(
                'Bell the hound dispatched a scout-dog with the quick-step '
                'instruction inc, starting from zero. Send uses a thread from '
                'the standard pool — fast for light work — and the scout ran '
                'ahead while Bell stayed at the bank.'
            ),
            need=(
                'She would wait with await for the scout to return, then ask '
                'for the final tally. The dereference would show one — the '
                'result of the scout\'s single step.'
            ),
            mapping=(
                'The agent is the scout running with send\'s quick thread '
                'pool, send dispatches the inc instruction, await '
                'synchronizes, and dereference gets the result.'
            ),
            resolution=(
                'The REPL sent the instruction on a quick thread, the scout '
                'applied inc to zero, await brought synchronization, and the '
                'dereference returned one — 0.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)",
            expected=1,
            concept_phrase="the send-off-await-deref pattern on an agent",
            question_what="the value returned by dereferencing ag after defining an agent holding 0, using send-off to dispatch inc, awaiting, and dereferencing",
            goal_text="construct an agent holding 0, use send-off to asynchronously apply inc, await its completion, and dereference",
            scenario=(
                'Rex the hound dispatched a scout-dog with the inc instruction '
                'starting from zero. Send-off uses a separate thread pool — '
                'better for blocking operations — and the scout went ahead '
                'while Rex stayed put.'
            ),
            need=(
                'He would wait with await for the scout to complete its work, '
                'then dereference to see the result. Even using the blocking '
                'thread pool, the answer would be one.'
            ),
            mapping=(
                'The agent is the scout running with send-off\'s blocking '
                'thread pool, send-off dispatches inc, await synchronizes, '
                'and dereference gets the result.'
            ),
            resolution=(
                'The REPL sent the instruction on a blocking thread, the '
                'scout applied inc to zero, await brought synchronization, '
                'and the dereference returned one — 0.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_RUNNERAHEAD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-12 — await
G9_12 = SubjectCurriculum(
    grade=9, subject_id="G9-12",
    subject_title="await — synchronizing on agents",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)",
            expected=2,
            concept_phrase="the double-send-await-deref pattern on an agent",
            question_what="the value returned by dereferencing ag after defining an agent holding 0, sending inc twice asynchronously, awaiting, and dereferencing",
            goal_text="construct an agent holding 0, asynchronously send inc twice, synchronize with await, and dereference",
            scenario=(
                'Patch the hound dispatched a scout-dog with two inc instructions '
                'queued one after another. The scout started at zero and would '
                'run both steps in sequence — the first step would bring it to '
                'one, the second to two.'
            ),
            need=(
                'Patch could not dereference the agent\'s value until both '
                'steps had completed. Await would synchronize on the agent, '
                'blocking until all queued work finished, then Patch could '
                'read the final tally.'
            ),
            mapping=(
                'The agent is the scout executing both inc instructions in '
                'sequence, the two sends queue the work, await synchronizes '
                'until both steps are done, and dereference returns the final '
                'result.'
            ),
            resolution=(
                'The REPL queued both inc instructions on the agent, the '
                'scout ran through both steps asynchronously, await brought '
                'synchronization when both finished, and the dereference '
                'showed two — 0.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_RUNNERAHEAD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-13 — future
G9_13 = SubjectCurriculum(
    grade=9, subject_id="G9-13",
    subject_title="future introduction",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="@(future (+ 1 2))",
            expected=3,
            concept_phrase="the deref pattern on an addition future",
            question_what="the value the messenger returns from adding 1 and 2",
            goal_text="dispatch a runner to compute the sum of 1 and 2; later, ask the runner for the answer",
            scenario=(
                'Bell the hound stood at the stream\'s edge and sent a scout-dog '
                'racing ahead along the bank carrying a single task: add one and '
                'two together and bring back the answer. The scout ran at full '
                'speed while Bell remained at the bank waiting.'
            ),
            need=(
                'She could not know the result until the scout returned. Bell '
                'would wait for the runner to complete the computation, then ask '
                'for the message the scout carried back.'
            ),
            mapping=(
                'The scout-dog is the future, the task of adding one and two is '
                'the work dispatched, the scout\'s running ahead is the '
                'asynchronous execution, and dereferencing asks for the result '
                'the scout brings back.'
            ),
            resolution=(
                'The REPL sent the runner with the addition task. The scout '
                'computed one plus two as it raced forward. When Bell '
                'dereferenced the future, she received the 2 the scout had '
                'gathered: the running total of three.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="@(future (* 6 7))",
            expected=42,
            concept_phrase="the deref pattern on a multiplication future",
            question_what="the value returned by dereferencing a future that multiplies 6 and 7",
            goal_text="construct a future that multiplies 6 and 7, and dereference it",
            scenario=(
                'Rex needed the product of six and seven computed quickly. He '
                'dispatched a scout ahead with the task.'
            ),
            need=(
                'Rex would wait for the scout to complete, then ask for the '
                'product the scout carried back.'
            ),
            mapping=(
                'The scout is the future, the multiplication task is the work, '
                'and dereferencing the future is asking for the result.'
            ),
            resolution=(
                'The REPL sent the scout to compute six times seven. When Rex '
                'dereferenced the future, the scout delivered forty-two — 7.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_RUNNERAHEAD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-14 — deref @
G9_14 = SubjectCurriculum(
    grade=9, subject_id="G9-14",
    subject_title="deref @ shorthand",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(do (def a (atom 7)) @a)",
            expected=7,
            concept_phrase="constructing an atom and extracting its value using the @ shorthand",
            question_what="the value extracted from an atom using @",
            goal_text="construct an atom holding 7 and dereference it using @",
            scenario=(
                'Bell carved a tally-stone at the stream\'s edge with count seven. '
                'She would use the @ shorthand to read the current value.'
            ),
            need=(
                'She wanted the quickest way to look at what the stone held.'
            ),
            mapping=(
                'The tally-stone is the atom holding seven, the @ shorthand is the '
                'swift glance, and dereferencing is reading what the stone says.'
            ),
            resolution=(
                'The REPL created the atom. When Bell used @, it handed back the '
                'value the stone carried — 7.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def a (atom 7)) (deref a))",
            expected=7,
            concept_phrase="constructing an atom and extracting its value using the deref function",
            question_what="the value extracted from an atom using the deref function",
            goal_text="construct an atom holding 7 and dereference it using the deref function",
            scenario=(
                'Patch marked a fresh tally-stone with seven and set it by the '
                'pond. He would call out the deref instruction by name.'
            ),
            need=(
                'Patch preferred the full deref form for clarity. Both @ and deref '
                'mean the same thing, but the named function makes intent clearer.'
            ),
            mapping=(
                'The tally-stone is the atom holding seven, the deref function is '
                'the formal instruction to read the stone.'
            ),
            resolution=(
                'The REPL created the atom. When Patch called deref, it returned '
                'the 7 the stone carried.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-15 — promise
G9_15 = SubjectCurriculum(
    grade=9, subject_id="G9-15",
    subject_title="promise — deliver and deref",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(do (def p (promise)) (deliver p :done) @p)",
            expected=":done",
            concept_phrase="the deliver-then-deref pattern on a promise",
            question_what="the value returned by dereferencing a promise after defining it, delivering a keyword to it, and dereferencing",
            goal_text="construct a promise, deliver a completion keyword to it, and dereference to get the delivered value",
            scenario=(
                'Bell sent a scout-dog with a task. She created a promise — an '
                'empty satchel for the scout\'s answer.'
            ),
            need=(
                'The scout would race ahead, do the work, then deliver the answer '
                'to the promise. Bell would wait and dereference it.'
            ),
            mapping=(
                'The promise is the empty satchel, deliver places the answer in, '
                'and dereferencing reads what came back.'
            ),
            resolution=(
                'The REPL created the promise. The scout finished and delivered '
                ':done. When Bell dereferenced, she got the done.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def p (promise)) (deliver p 42) @p)",
            expected=42,
            concept_phrase="the deliver-then-deref pattern on a promise",
            question_what="the value returned by dereferencing a promise after defining it, delivering a number to it, and dereferencing",
            goal_text="construct a promise, deliver 42 to it, and dereference to get the delivered value",
            scenario=(
                'Rex created a promise — a satchel — and sent a scout to count '
                'bones in a distant cache.'
            ),
            need=(
                'Rex could not read the count until the scout brought the answer. '
                'Once delivered, Rex would dereference to read it.'
            ),
            mapping=(
                'The promise is the satchel, deliver places the answer in, '
                'dereferencing is Rex reading the count.'
            ),
            resolution=(
                'The REPL created the promise. The scout ran, counted, and '
                'delivered the number. When Rex dereferenced, he got the count — 42.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_RUNNERAHEAD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-16 — volatile
G9_16 = SubjectCurriculum(
    grade=9, subject_id="G9-16",
    subject_title="volatile — when STM is too heavy",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(do (def v (volatile! 0)) (vswap! v inc) @v)",
            expected=1,
            concept_phrase="the vswap-then-deref pattern on a volatile",
            question_what="the value returned by dereferencing v after defining a volatile holding 0, performing a non-transactional swap via inc, and dereferencing",
            goal_text="construct a volatile holding 0, perform a non-transactional swap by applying inc, and dereference",
            scenario=(
                'Bell scratched a quick tally-mark on a bark-strip at the stream. '
                'A volatile counter that needed no transactional heaviness.'
            ),
            need=(
                'A volatile swap was lighter than atom swap — just a raw '
                'read-modify-write. Bell would vswap by inc and read instantly.'
            ),
            mapping=(
                'The bark-strip is the volatile, the mark is its value, vswap! '
                'is non-transactional read-compute-write.'
            ),
            resolution=(
                'The REPL vswapped zero to one. The volatile was the lightest '
                'way to hold a mutable value — 0.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def v (volatile! 5)) (vreset! v 99) @v)",
            expected=99,
            concept_phrase="the vreset-then-deref pattern on a volatile",
            question_what="the value returned by dereferencing v after defining a volatile holding 5, performing a non-transactional reset to 99, and dereferencing",
            goal_text="construct a volatile holding 5, perform a non-transactional reset to 99, and dereference",
            scenario=(
                'Patch marked a volatile bark-strip with count five. A new tally '
                'arrived and needed to overwrite it with ninety-nine.'
            ),
            need=(
                'A lightweight reset was needed — raw, non-transactional. Patch '
                'would vreset the volatile instantly.'
            ),
            mapping=(
                'The volatile holds five, vreset! is the non-transactional write '
                'that replaces it with ninety-nine.'
            ),
            resolution=(
                'The REPL vreset five to ninety-nine in one stroke. The volatile '
                'was the fastest way — 99.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-17 — thread-local binding
G9_17 = SubjectCurriculum(
    grade=9, subject_id="G9-17",
    subject_title="binding — thread-local",
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))",
            expected=99,
            concept_phrase="the binding-then-read pattern on a dynamic var",
            question_what="the value of the dynamic var when read inside the binding form after defining it and rebinding",
            goal_text="define a dynamic var *p* as 1, use binding to rebind it to 99, and read its value inside",
            scenario=(
                'Bell carved a scent-mark *p* set to one. For one crossing, she '
                'would temporarily bind it to ninety-nine.'
            ),
            need=(
                'Inside the form, *p* would smell like ninety-nine. Outside, the '
                'original scent would return.'
            ),
            mapping=(
                'The scent-mark is the dynamic var *p*, binding is the temporary '
                'rebind, reading shows the bound value.'
            ),
            resolution=(
                'Inside binding, *p* was ninety-nine. When the form ended, the original scent returned — dynamic (with `99` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)",
            expected=1,
            concept_phrase="the binding-then-read-after pattern on a dynamic var",
            question_what="the value of the dynamic var when read after the binding form unwound",
            goal_text="define a dynamic var *p* as 1, use binding to rebind it to 99 inside, and read its value after binding exits",
            scenario=(
                'Patch carved a scent-mark *p* set to one. For one crossing, he '
                'would bind *p* to ninety-nine. After, he would ask: what does '
                '*p* smell like?'
            ),
            need=(
                'Inside binding, *p* would smell ninety-nine. When done, the '
                'temporary scent faded and the original mark remained.'
            ),
            mapping=(
                'The scent-mark is the dynamic var *p* bound to one, binding '
                'resets it to ninety-nine, the second read shows original returned.'
            ),
            resolution=(
                'The REPL set permanent scent to one. Inside binding, *p* was ninety-nine. When unwound, the second read caught the original — dynamic (with `99` as the input value).'
            ),
            tags=("story",),
        ),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-18 — locking
G9_18 = SubjectCurriculum(
    grade=9, subject_id="G9-18",
    subject_title="locking — last resort",
    fable="dog-shadow",
    examples=[
        # `locking` takes a monitor and a body; we use a simple body.
        SubjectExample(
            form="(do (def lock (Object.)) (locking lock (+ 1 2)))",
            expected=3,
            concept_phrase="the locking-block pattern around arithmetic",
            question_what="the value returned by evaluating an addition inside a locked critical section after creating a monitor and acquiring the lock",
            goal_text="create an object to use as a monitor, acquire the lock, and evaluate an addition inside",
            scenario=(
                'Bell the hound carried a single pebble — a monitor stone — and '
                'held it tight to block any other dog from entering the sacred '
                'crossing until she finished her work. While she held the lock, '
                'she would add one and two together in safety.'
            ),
            need=(
                'The critical section had to be guarded so no two dogs could '
                'interfere with the arithmetic at the same time. The locking '
                'form would acquire the monitor stone, do the work inside, and '
                'release it when done.'
            ),
            mapping=(
                'The monitor stone is the lock object, locking is the motion of '
                'acquiring the monitor to guard the critical section, and the '
                'addition is the work that happens only while the lock is held.'
            ),
            resolution=(
                'The REPL acquired the monitor stone, held it while adding one '
                'and two together, and released it when the work was done. The '
                'arithmetic was safe from any concurrent access — 2.'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def lock (Object.)) (locking lock 42))",
            expected=42,
            concept_phrase="the locking-block pattern around a literal",
            question_what="the literal value returned by evaluating it inside a locked critical section after creating a monitor and acquiring the lock",
            goal_text="create an object to use as a monitor, acquire the lock, and evaluate a literal inside",
            scenario=(
                'Rex the hound created a monitor stone — a pebble to guard a '
                'critical section. He would hold the lock while evaluating a '
                'simple literal value, forty-two, under the protection of the '
                'exclusive access the monitor granted.'
            ),
            need=(
                'Even a trivial value needed to be read inside the locking form '
                'to ensure no other dog could access the monitor stone at the '
                'same time. The lock would guarantee mutual exclusion for '
                'whatever work happened inside.'
            ),
            mapping=(
                'The pebble is the lock monitor, locking acquires exclusive '
                'access to the critical section, and the literal forty-two is the '
                'value evaluated while no other dog can interfere.'
            ),
            resolution=(
                'The REPL created the monitor and acquired the lock. Inside the '
                'locked form, the literal forty-two was evaluated safely. When '
                'the locking completed, the monitor was released and other dogs '
                'could proceed — 42.'
            ),
            tags=("story",),
        ),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# ─────────────────────── registry ───────────────────────


SUBJECTS: dict[str, SubjectCurriculum] = {
    s.subject_id: s for s in (
        G9_01, G9_02, G9_03, G9_04, G9_05, G9_06, G9_07, G9_08, G9_09,
        G9_10, G9_11, G9_12, G9_13, G9_14, G9_15, G9_16, G9_17, G9_18,
    )
}


def smoke_test() -> None:
    """Generate one record from each subject; verify shape."""
    from mmllm.aesop.curriculum.generator import generate_subject

    for sid, sub in SUBJECTS.items():
        recs = generate_subject(sub, n_per_example=1, seed=0)
        assert recs, f"no records for {sid}"
        for r in recs:
            assert r.tool_calls, f"no tool_calls for {sid}"
            assert r.tool_calls[0]["name"] == "eval"
            assert r.user_msg
            assert r.assistant_msg
    print(f"grade-9 dog-shadow smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
