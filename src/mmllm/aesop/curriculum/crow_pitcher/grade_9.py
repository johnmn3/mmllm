"""Grade 9 — state and concurrency primitives. Through crow-pitcher.

The fable's moral dynamic — Tortoise's careful, transactional updates
versus Hare's racing-without-coordination — maps cleanly onto the
state-and-concurrency primitives. Tortoise insists on dosync and CAS;
Hare wants to mutate without checking. The REPL settles every dispute.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.crow_pitcher.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.crow_pitcher._metaphor_pools import (
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
    fable="crow-pitcher",
    examples=[
        # `assoc` returns a new map; the original is unchanged.
        SubjectExample(
            form="(let [m {:a 1}] (assoc m :b 2) m)",
            expected={":a": 1},
            concept_phrase="binding a map, adding an entry to a new map, and returning the original",
            question_what="the original map after assoc returns a new map",
            goal_text="bind a map m, call assoc to add :b 2 to a new map, then return the unchanged m",

            scenario=(
                "Korvus paused at the garden pitcher with a basket holding "
                "one stone marked :a. He dropped a second stone marked :b "
                "into a spare basket beside it, leaving his original basket "
                "untouched on the rim."
            ),
            need=(
                "He wanted to confirm his original basket still held only "
                "the first stone, unchanged after the new basket was made."
            ),
            mapping=(
                "`let` binds the map to m. `assoc` builds a brand-new map "
                "with the extra entry — it never alters m. Returning m at "
                "the end reads the original basket, which is still intact."
            ),
            resolution=(
                "The pitcher returned the original basket — proof the first "
                "stone was never disturbed. (with {drawn.a} folded in)"
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
                "Caw lined up the stones on the pitcher's rim at the "
                "orchard, then pressed a fourth stone into a fresh row "
                "beside them. Her original three-stone row stayed exactly "
                "as she had placed it."
            ),
            need=(
                "She needed to check that her original three-stone row "
                "was untouched after the new row was formed beside it."
            ),
            mapping=(
                "`conj` produces a new vector with the extra element — the "
                "original binding v is never modified. Returning v reads "
                "the old row, not the extended one."
            ),
            resolution=(
                "The pitcher showed the original three-stone row, "
                "confirming no stone had moved. (with {drawn.a} folded in)"
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
    fable="crow-pitcher",
    examples=[
        # The minimal "place that needs identity over time" example.
        SubjectExample(
            form="(do (def counter (atom 0)) (swap! counter inc) @counter)",
            expected=1,
            concept_phrase="binding an atom to counter, atomically incrementing it, and dereferencing the result",
            question_what="the value after atomically swapping counter with inc and dereferencing",
            goal_text="construct an atom holding 0 as counter, atomically swap it by applying inc, and dereference the result",

            scenario=(
                "Korvus needed a mark that would survive across visits to "
                "the hilltop pitcher. He scratched a zero on the clay face "
                "as a counter, then nudged it up by one with a single talon "
                "stroke."
            ),
            need=(
                "He needed to read the counter's current mark after the "
                "update to know how many visits were recorded."
            ),
            mapping=(
                "`atom` creates the persistent tally on the clay face. "
                "`swap!` applies inc to the current value and writes the "
                "new mark. `@counter` reads the mark back from the clay."
            ),
            resolution=(
                'The clay face showed the updated tally — one visit recorded, the counter holding its new mark (with `0` as the input value).'
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
                "Sable scratched `:idle` into the pitcher's clay face at "
                "the meadow to mark the flock's state. When the foraging "
                "run began, Sable wiped the mark away and pressed a fresh "
                "active-state keyword into the clay in its place."
            ),
            need=(
                "Sable needed to confirm the clay face now showed the "
                "fresh state after the reset took effect."
            ),
            mapping=(
                "`atom` holds the current state label on the clay. "
                "`reset!` overwrites the old mark entirely with a new "
                "value. `@progress` reads whatever mark is currently "
                "pressed into the clay."
            ),
            resolution=(
                "The clay face returned the new state label, confirming "
                "the transition had taken hold. (the keyword :idle)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(do (def a (atom 0)) (swap! a inc) @a)",
            expected=1,
            concept_phrase="the atom updated atomically via swap! and read by deref",
            question_what="the running tally on the page after one foraging contribution",
            goal_text="set up a shared notebook starting at 0, atomically add one to its page, then read the page",

            scenario=(
                "Caw scratched a fresh tally line into the pitcher's clay face "
                "at the village, starting at zero. The mark was the notebook "
                "— any crow at the pitcher could read or update it, and "
                "the mark would persist."
            ),
            need=(
                "She needed to nudge the tally up by one and then read back "
                "the new count scratched into the clay face."
            ),
            mapping=(
                "`atom` creates a mutable tally on the pitcher's face. "
                "`swap!` applies a function to the current value and "
                "writes the new mark. `@` dereferences the atom — reads "
                "the current tally from the clay."
            ),
            resolution=(
                '1 — the tally, incremented once by the swap, read back from the clay face (with `0` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def a (atom 10)) (swap! a + 5) @a)",
            expected=15,
            concept_phrase="the atom updated atomically and then read",
            question_what="the value returned by dereferencing a after defining a as an atom holding 10 and swapping it via + 5",
            goal_text="construct an atom holding 10, atomically swap it by applying + to 5, and dereference the result",

            scenario=(
                "Korvus scratched ten strokes into the pitcher's clay face "
                "at the farm to record stones already dropped. He then added "
                "five more strokes with a single talon sweep, updating the "
                "tally in one motion."
            ),
            need=(
                "He needed to read the clay face and confirm the tally "
                "reflected the full count after the addition. (count: 10)"
            ),
            mapping=(
                "`atom` holds the running count on the clay. `swap!` with "
                "`+ 5` applies addition to the current mark and writes the "
                "result back atomically. `@a` reads the updated tally."
            ),
            resolution=(
                "The pitcher returned the updated tally from the clay face, "
                "reflecting the full count after the addition."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def a (atom :start)) (reset! a :done) @a)",
            expected=":done",
            concept_phrase="the atom reset to a new value and then read",
            question_what="the value returned by dereferencing a after defining a as an atom holding a start keyword and resetting it to done",
            goal_text="construct an atom holding a start keyword, atomically reset it to a done keyword, and dereference the result",

            scenario=(
                "Sable pressed `:start` into the pitcher's clay face at "
                "the village to mark where the session stood. Once the "
                "session finished, Sable wiped the old mark and pressed "
                "`:done` firmly into the clay."
            ),
            need=(
                "Sable needed to confirm the clay face now carried the "
                "finished mark after the reset was applied."
            ),
            mapping=(
                "`atom` holds the session label on the clay face. "
                "`reset!` replaces the old mark entirely with the new "
                "keyword. `@a` reads the current mark scratched into clay."
            ),
            resolution=(
                "The pitcher returned the new label from the clay, "
                "confirming the session mark had been replaced. (the keyword :start)"
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
    fable="crow-pitcher",
    examples=[
        # `compare-and-set!` succeeds when current matches expected.
        SubjectExample(
            form="(do (def a (atom 0)) (compare-and-set! a 0 1) @a)",
            expected=1,
            concept_phrase="the atom updated via compare-and-set and read",
            question_what="the value returned by dereferencing a after defining a as an atom holding 0 and performing a successful compare-and-set to 1",
            goal_text="construct an atom holding 0, perform a compare-and-set checking for 0 and setting to 1, and dereference",

            scenario=(
                "Korvus checked the pitcher's clay face at the garden: if "
                "it still showed zero — the exact mark he expected — he "
                "would replace it with a fresh stroke of one. The mark "
                "was indeed zero, so the swap was allowed."
            ),
            need=(
                "He needed to confirm the clay now showed the new mark "
                "after the conditional swap succeeded."
            ),
            mapping=(
                "`compare-and-set!` reads the current mark, checks it "
                "against the expected value, and only writes the new mark "
                "if they match. `@a` then reads the result from the clay."
            ),
            resolution=(
                'The pitcher returned the new mark from the clay face, confirming the conditional swap had succeeded (with `0` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def a (atom 5)) (compare-and-set! a 0 99) @a)",
            expected=5,
            concept_phrase="the atom guarded by a compare-and-set whose expected value did not match",
            question_what="the value returned by dereferencing a after defining a as an atom holding 5 and attempting a compare-and-set that fails",
            goal_text="construct an atom holding 5, perform a compare-and-set checking for 0 and setting to 99, and dereference",

            scenario=(
                "Caw approached the pitcher at the orchard, expecting the "
                "clay face to read zero. But the mark already showed five "
                "— not zero — so her attempt to overwrite it with a new "
                "value was quietly refused."
            ),
            need=(
                "She needed to read the clay face and see that the original "
                "mark was preserved after the failed swap attempt."
            ),
            mapping=(
                "`compare-and-set!` checks the current mark against the "
                "expected value. Finding a mismatch, it leaves the clay "
                "unchanged. `@a` reads the original mark still scratched in."
            ),
            resolution=(
                "The pitcher returned the original mark — the clay was "
                "untouched because the comparison had failed. (count: 5)"
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
    fable="crow-pitcher",
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
                "Sable scratched a zero on the pitcher's clay face at the "
                "hilltop, then pressed a second tally beside it as a log. "
                "A sentinel rule was set: whenever the first mark changed, "
                "the new value would be copied into the log tally."
            ),
            need=(
                "After nudging the first tally up by one, Sable needed to "
                "read the log and confirm the change had been recorded."
            ),
            mapping=(
                "`add-watch` installs a sentinel on the atom: every time "
                "`swap!` writes a new mark, the watcher conjoins the new "
                "value into the log atom. `@log` reads the record."
            ),
            resolution=(
                "The pitcher returned the log tally — a single entry "
                "showing the change that the sentinel had captured. (the keyword :w)"
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
    fable="crow-pitcher",
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
                "Korvus scratched zero onto the pitcher's clay face at the "
                "village and carved a rule beside it: only number marks may "
                "ever be pressed here. Then he nudged the tally up by one "
                "— a number, so the rule allowed it."
            ),
            need=(
                "He needed to read the tally back and confirm the update "
                "had passed the rule and been recorded on the clay."
            ),
            mapping=(
                "`set-validator!` carves a rule on the atom: any proposed "
                "new value must satisfy `number?` or the update is rejected. "
                "`swap!` with `inc` passes, and `@a` reads the result."
            ),
            resolution=(
                'The pitcher returned the updated tally — the rule was satisfied and the new mark settled into the clay (with `0` as the input value).'
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
    fable="crow-pitcher",
    examples=[
        # Refs require dosync to update.
        SubjectExample(
            form="(do (def r (ref 0)) (dosync (alter r inc)) @r)",
            expected=1,
            concept_phrase="the ref altered inside a transaction and read",
            question_what="the value returned by dereferencing r after defining a ref holding 0, performing a transactional alter via inc, and dereferencing",
            goal_text="construct a ref holding 0, perform a transactional alter by applying inc inside dosync, and dereference",

            scenario=(
                "Caw placed a zero-mark in a sealed safe-box beside the "
                "pitcher at the garden. To change the mark she had to open "
                "the safe-box in one atomic transaction, nudge the tally up "
                "by one, and seal it again before reading."
            ),
            need=(
                "She needed to read the safe-box after the transaction "
                "sealed to confirm the tally had been properly updated."
            ),
            mapping=(
                "`ref` holds the tally inside the safe-box. `dosync` opens "
                "the transaction; `alter` applies `inc` to the current mark "
                "and seals the change. `@r` reads the committed tally."
            ),
            resolution=(
                'The pitcher returned the tally from inside the safe-box, showing the transaction had committed cleanly (with `0` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def r (ref 100)) (dosync (ref-set r 7)) @r)",
            expected=7,
            concept_phrase="the ref reset inside a transaction and read",
            question_what="the value returned by dereferencing r after defining a ref holding 100, setting it to 7 inside dosync, and dereferencing",
            goal_text="construct a ref holding 100, perform a transactional ref-set to 7 inside dosync, and dereference",

            scenario=(
                "Korvus found a safe-box at the farm holding a large tally. "
                "He opened a transaction, wiped the old mark entirely, and "
                "pressed a new, much smaller tally into the safe-box before "
                "sealing it shut."
            ),
            need=(
                "He needed to read the safe-box to confirm the new tally "
                "had replaced the old one after the transaction committed."
            ),
            mapping=(
                "`dosync` opens the transaction around the safe-box. "
                "`ref-set` replaces the current mark wholesale. `@r` "
                "dereferences the ref and reads the committed replacement."
            ),
            resolution=(
                "The pitcher returned the newly set tally from the safe-box, "
                "confirming the old mark was gone. (count: 100)"
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
    fable="crow-pitcher",
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
                "Sable kept two safe-boxes beside the pitcher at the hilltop "
                "— one holding a small tally, one slightly larger. She opened "
                "a single transaction and nudged both tallies up by one "
                "before sealing both boxes together."
            ),
            need=(
                "Sable needed to read both safe-boxes after the transaction "
                "and confirm each tally had advanced by exactly one."
            ),
            mapping=(
                "`dosync` wraps both `alter` calls in one atomic transaction. "
                "Either both tallies commit together or neither does. "
                "`[@a @b]` reads the pair of updated marks."
            ),
            resolution=(
                'The pitcher returned both tallies side by side, each advanced by one in the same sealed transaction (with `1` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def r (ref 10)) (dosync (alter r + 5)) @r)",
            expected=15,
            concept_phrase="the ref altered inside a transaction and read",
            question_what="the value returned by dereferencing r after defining a ref holding 10, performing a transactional alter via + 5, and dereferencing",
            goal_text="construct a ref holding 10, perform a transactional alter by applying + with 5 inside dosync, and dereference",

            scenario=(
                "Caw found a safe-box at the orchard holding a tally of ten. "
                "She opened a transaction and applied an addition of five to "
                "the existing mark, sealing the safe-box with the combined "
                "total before stepping back."
            ),
            need=(
                "She needed to read the safe-box after the transaction "
                "sealed and confirm the combined tally was recorded inside."
            ),
            mapping=(
                "`dosync` opens the transaction; `alter` with `+ 5` adds "
                "to the current mark and writes the result atomically. "
                "`@r` reads the committed total held by the safe-box."
            ),
            resolution=(
                "The pitcher returned the combined tally from the safe-box, "
                "showing the addition had committed in the transaction. (count: 10)"
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
    fable="crow-pitcher",
    examples=[
        # The same operation expressed both ways.
        SubjectExample(
            form="(do (def a (atom 0)) (swap! a inc) @a)",
            expected=1,
            concept_phrase="the atom updated atomically and then read",
            question_what="the value returned by dereferencing a after defining an atom holding 0, swapping it via inc, and dereferencing",
            goal_text="construct an atom holding 0, atomically swap it by applying inc, and dereference",

            scenario=(
                "Korvus scratched zero on the clay face of the pitcher at "
                "the meadow — open for any crow to update directly. He "
                "pressed one talon stroke to nudge the mark up by one, "
                "needing no transaction box at all."
            ),
            need=(
                "He wanted to read the clay face and confirm the mark had "
                "risen after the direct atomic swap."
            ),
            mapping=(
                "`atom` exposes the mark directly on the clay — no "
                "transaction required. `swap!` with `inc` updates it "
                "atomically. `@a` reads the mark back from the face."
            ),
            resolution=(
                'The pitcher returned the mark from the clay, updated by the direct swap without any enclosing transaction (with `0` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def r (ref 0)) (dosync (alter r inc)) @r)",
            expected=1,
            concept_phrase="the ref altered inside a transaction and read",
            question_what="the value returned by dereferencing r after defining a ref holding 0, altering it via inc inside dosync, and dereferencing",
            goal_text="construct a ref holding 0, perform a transactional alter by applying inc inside dosync, and dereference",

            scenario=(
                "Sable placed the same zero mark inside a sealed safe-box "
                "beside the pitcher at the meadow — a ref, not bare clay. "
                "To nudge the tally she had to open a full transaction, "
                "alter the mark, and seal before reading."
            ),
            need=(
                "She needed to read the safe-box after the transaction "
                "and confirm the same result as the bare-clay path."
            ),
            mapping=(
                "`ref` locks the mark inside a safe-box. `dosync` + `alter` "
                "update it transactionally — heavier than `atom` but "
                "coordinated. `@r` reads the committed mark."
            ),
            resolution=(
                'The pitcher returned the same updated mark as the atom path — identical result, different mechanism (with `0` as the input value).'
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
    fable="crow-pitcher",
    examples=[
        # send is async — we await before reading.
        SubjectExample(
            form="(do (def ag (agent 0)) (send ag inc) (await ag) @ag)",
            expected=1,
            concept_phrase="the agent sent a function asynchronously, awaited, and read",
            question_what="the value returned by dereferencing ag after defining an agent holding 0, sending inc asynchronously, awaiting, and dereferencing",
            goal_text="construct an agent holding 0, asynchronously send inc to it, await its completion, and dereference",

            scenario=(
                "Sable set a scout-crow carrying a tally of zero on the road "
                "to the far orchard. She sent the scout ahead with one "
                "instruction: increment the tally by one. Then she waited "
                "at the pitcher for the scout's return."
            ),
            need=(
                "Once the scout had done its work she wanted to read the "
                "tally the scout carried back and see how the water stood."
            ),
            mapping=(
                "`agent` creates the scout carrying a value. `send` dispatches "
                "the function asynchronously. `await` blocks until the scout "
                "returns. `@` dereferences the final tally from the agent."
            ),
            resolution=(
                "1 — the scout returned with the incremented count, the tally settling into the pitcher's depth (with `0` as the input value)."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)",
            expected=15,
            concept_phrase="the agent sent a function asynchronously, awaited, and read",
            question_what="the value returned by dereferencing ag after defining an agent holding 5, sending + 10 asynchronously, awaiting, and dereferencing",
            goal_text="construct an agent holding 5, asynchronously send + with 10 to it, await its completion, and dereference",

            scenario=(
                "Korvus dispatched a scout-crow from the hilltop carrying "
                "a tally of five, with instructions to add ten more along "
                "the road to the orchard. He waited at the pitcher until "
                "the scout returned with the combined count."
            ),
            need=(
                "He needed to read the scout's final tally after it "
                "returned to know the full combined count."
            ),
            mapping=(
                "`agent` carries the starting tally. `send` with `+ 10` "
                "dispatches the addition asynchronously. `await` holds "
                "at the pitcher until the scout lands. `@ag` reads the result."
            ),
            resolution=(
                "The pitcher returned the scout's final tally — the "
                "combined count after the addition completed on the road. (count: 5)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(do (def ag (agent 0)) (send ag inc) (await ag) @ag)",
            expected=1,
            concept_phrase="the agent sent a function asynchronously, awaited, and read",
            question_what="the value returned by dereferencing ag after defining an agent holding 0, using send to dispatch inc, awaiting, and dereferencing",
            goal_text="construct an agent holding 0, use send to asynchronously apply inc, await its completion, and dereference",

            scenario=(
                "Caw commissioned a scout-crow from the village pitcher "
                "with a tally of zero. She sent it via the short-task "
                "pool — `send` — with instructions to add one, then "
                "waited at the rim for the scout to land."
            ),
            need=(
                "After the scout returned she needed to read its tally "
                "to confirm the short-task route had updated the count."
            ),
            mapping=(
                "`send` routes the scout through the fixed thread pool — "
                "right for quick, CPU-bound tasks. `await` holds until "
                "the scout lands. `@ag` reads the tally it carried back."
            ),
            resolution=(
                "The pitcher returned the scout's tally, confirming the short-task send had completed and the count was updated (with `0` as the input value)."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)",
            expected=1,
            concept_phrase="the agent dispatched via send-off, awaited, and read",
            question_what="the value returned by dereferencing ag after defining an agent holding 0, using send-off to dispatch inc, awaiting, and dereferencing",
            goal_text="construct an agent holding 0, use send-off to asynchronously apply inc, await its completion, and dereference",

            scenario=(
                "Sable sent the same scout-crow via the long-task route "
                "— `send-off` — from the village pitcher. The scout "
                "carried a zero tally and instructions to add one, "
                "routed through the expandable thread pool."
            ),
            need=(
                "After the scout returned from the long-task route she "
                "needed to read the tally and confirm it matched expectation."
            ),
            mapping=(
                "`send-off` routes the scout through an expandable pool — "
                "right for blocking or slow tasks. `await` waits for "
                "return. `@ag` reads the tally the scout carried back."
            ),
            resolution=(
                "The pitcher returned the scout's tally — the long-task route and the short-task route yielded the same result (with `0` as the input value)."
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)",
            expected=2,
            concept_phrase="the agent sent two updates in succession, awaited, and read",
            question_what="the value returned by dereferencing ag after defining an agent holding 0, sending inc twice asynchronously, awaiting, and dereferencing",
            goal_text="construct an agent holding 0, asynchronously send inc twice, synchronize with await, and dereference",

            scenario=(
                "Korvus dispatched a scout-crow from the orchard pitcher "
                "twice in quick succession — each time with orders to "
                "add one to the tally. He waited at the rim until both "
                "missions finished before reading the result."
            ),
            need=(
                "He needed to confirm that both increments had landed on "
                "the scout's tally before he read the final count."
            ),
            mapping=(
                "Two `send` calls queue both increments on the agent. "
                "`await` blocks at the pitcher until the queue drains "
                "completely. `@ag` then reads the fully updated tally."
            ),
            resolution=(
                "The pitcher returned the scout's tally after both missions completed — both increments accounted for (with `0` as the input value)."
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="@(future (+ 1 2))",
            expected=3,
            concept_phrase="the addition wrapped in a future and dereferenced",
            question_what="the value the messenger returns from adding 1 and 2",
            goal_text="dispatch a runner to compute the sum of 1 and 2; later, ask the runner for the answer",

            scenario=(
                "Caw sent a scout-crow from the meadow pitcher with a "
                "single task: fly to the far stone and add one and two "
                "together. She waited at the rim; when the scout returned "
                "she dipped her talon to read the result."
            ),
            need=(
                "She needed to read the scout's answer once it landed — "
                "the sum it computed while away on the task."
            ),
            mapping=(
                "`future` launches the scout-crow asynchronously with the "
                "computation as its mission. `@` blocks until the scout "
                "lands and then reads the value it carries back."
            ),
            resolution=(
                "The pitcher returned the scout's computed answer — the sum delivered the moment the scout touched down (with `1` as the input value)."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="@(future (* 6 7))",
            expected=42,
            concept_phrase="the multiplication wrapped in a future and dereferenced",
            question_what="the value returned by dereferencing a future that multiplies 6 and 7",
            goal_text="construct a future that multiplies 6 and 7, and dereference it",

            scenario=(
                "Korvus sent a scout-crow from the hilltop pitcher on a "
                "longer mission: multiply six by seven in the far field. "
                "He perched at the rim and waited; the scout returned "
                "carrying the product of that calculation."
            ),
            need=(
                "He needed to read the scout's tally once it returned to "
                "learn the product it had computed in the field."
            ),
            mapping=(
                "`future` dispatches the scout with `(* 6 7)` as its task. "
                "`@` blocks at the pitcher until the scout lands and then "
                "extracts the computed product the scout carries."
            ),
            resolution=(
                "The pitcher returned the product the scout computed — "
                "the multiplication result delivered on landing. (count: 6)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(do (def a (atom 7)) @a)",
            expected=7,
            concept_phrase="constructing an atom and extracting its value using the @ shorthand",
            question_what="the value extracted from an atom using @",
            goal_text="construct an atom holding 7 and dereference it using @",

            scenario=(
                "Sable pressed seven strokes into the pitcher's clay face "
                "at the village to create a tally. She then glanced at "
                "the clay with a quick talon-tap — the `@` shorthand — "
                "to read the mark without disturbing it."
            ),
            need=(
                "She needed to confirm the clay face still held the seven "
                "strokes she had pressed in, reading it with @ shorthand."
            ),
            mapping=(
                "`atom` holds the tally on the clay face. `@a` is the "
                "shorthand talon-tap: it reads the current mark directly "
                "without altering or wrapping it in any expression."
            ),
            resolution=(
                "The pitcher returned the mark on the clay — the tally "
                "read back exactly as scratched, using the @ shorthand. (count: 7)"
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
                "Korvus pressed seven strokes into the clay face at the "
                "garden pitcher. Instead of the quick talon-tap, he recited "
                "the full `deref` call aloud — the long form of the same "
                "read — and waited for the pitcher's answer."
            ),
            need=(
                "He needed to confirm the clay face held seven strokes "
                "using the explicit `deref` function rather than `@`."
            ),
            mapping=(
                "`deref` is the explicit function form of `@`: it reads "
                "the current mark from the atom's clay face. Both forms "
                "return the same value — longhand and shorthand alike."
            ),
            resolution=(
                "The pitcher returned the same mark as the shorthand form "
                "— the seven strokes, read via the full deref call. (count: 7)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(do (def p (promise)) (deliver p :done) @p)",
            expected=":done",
            concept_phrase="the promise delivered a value and then dereferenced",
            question_what="the value returned by dereferencing a promise after defining it, delivering a keyword to it, and dereferencing",
            goal_text="construct a promise, deliver a completion keyword to it, and dereference to get the delivered value",

            scenario=(
                "Caw hung an empty sealed pouch on the pitcher's rim at "
                "the market — a promise with nothing inside yet. When her "
                "task finished she pressed a `:done` token into the pouch "
                "and sealed it, then read out what it held."
            ),
            need=(
                "She needed to open the sealed pouch and confirm the "
                "delivered token was inside after the delivery was made."
            ),
            mapping=(
                "`promise` creates the empty pouch on the rim. `deliver` "
                "presses a value in and seals it — once only. `@p` opens "
                "the pouch and reads the delivered token."
            ),
            resolution=(
                "The pitcher returned the token from the pouch — the "
                "delivered value, present and readable after sealing. (the keyword :done)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def p (promise)) (deliver p 42) @p)",
            expected=42,
            concept_phrase="the promise delivered a value and then dereferenced",
            question_what="the value returned by dereferencing a promise after defining it, delivering a number to it, and dereferencing",
            goal_text="construct a promise, deliver 42 to it, and dereference to get the delivered value",

            scenario=(
                "Sable hung an empty pouch on the pitcher's rim at the "
                "road. Once the count was complete, a stone tally was "
                "pressed into the pouch and sealed. Sable reached in "
                "with a talon-tap to read the count inside."
            ),
            need=(
                "Sable needed to read the sealed pouch and confirm the "
                "number tally was present after delivery."
            ),
            mapping=(
                "`promise` suspends reading until delivery occurs. `deliver` "
                "places the tally inside and seals the pouch permanently. "
                "`@p` unblocks and reads the delivered number."
            ),
            resolution=(
                "The pitcher returned the count from the sealed pouch — "
                "the number tally present the moment it was delivered. (count: 42)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(do (def v (volatile! 0)) (vswap! v inc) @v)",
            expected=1,
            concept_phrase="the volatile updated by vswap! and read",
            question_what="the value returned by dereferencing v after defining a volatile holding 0, performing a non-transactional swap via inc, and dereferencing",
            goal_text="construct a volatile holding 0, perform a non-transactional swap by applying inc, and dereference",

            scenario=(
                "Korvus needed a fast tally on the pitcher's clay face at "
                "the farm — no safe-box, no transaction overhead. He "
                "scratched a zero directly and swept one stroke over it "
                "with `vswap!`, updating in place without locking."
            ),
            need=(
                "He needed to read the clay face immediately after the "
                "lightweight swap and confirm the updated mark was there."
            ),
            mapping=(
                "`volatile!` creates the tally on bare clay — lighter than "
                "an atom, no CAS retry loop. `vswap!` with `inc` updates "
                "it directly. `@v` reads the mark back from the clay."
            ),
            resolution=(
                'The pitcher returned the updated mark from the clay — the lightweight swap had written it without any transaction (with `0` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def v (volatile! 5)) (vreset! v 99) @v)",
            expected=99,
            concept_phrase="the volatile reset by vreset! and read",
            question_what="the value returned by dereferencing v after defining a volatile holding 5, performing a non-transactional reset to 99, and dereferencing",
            goal_text="construct a volatile holding 5, perform a non-transactional reset to 99, and dereference",

            scenario=(
                "Caw scratched five strokes onto the clay face at the "
                "orchard, then wiped them away entirely with `vreset!` "
                "and pressed a large new number directly into the clay "
                "— no safe-box, no coordination required."
            ),
            need=(
                "She needed to read the clay face and confirm the new "
                "mark had fully replaced the old one after the reset."
            ),
            mapping=(
                "`volatile!` holds the tally on lightweight clay. `vreset!` "
                "overwrites the mark wholesale — faster than `reset!` on "
                "an atom. `@v` reads the replacement mark from the clay."
            ),
            resolution=(
                "The pitcher returned the new mark from the clay — the "
                "old strokes fully replaced by the lightweight reset. (count: 5)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))",
            expected=99,
            concept_phrase="the dynamic var rebound inside a binding form and read",
            question_what="the value of the dynamic var when read inside the binding form after defining it and rebinding",
            goal_text="define a dynamic var *p* as 1, use binding to rebind it to 99, and read its value inside",

            scenario=(
                "Sable chalked `1` on the pitcher's rim at the village as "
                "the default mark for `*p*`. Inside a sheltered alcove "
                "she re-chalked the rim to `99` for her own use, "
                "without disturbing any other crow's view of the mark."
            ),
            need=(
                "Inside the alcove she needed to read the rim and confirm "
                "it showed her local rebinding, not the global chalk."
            ),
            mapping=(
                "`^:dynamic` makes the var chalk-on-rim — rebindable per "
                "scope. `binding` re-chalks the rim locally for this "
                "thread's alcove. Reading `*p*` inside sees the local mark."
            ),
            resolution=(
                "The pitcher returned the locally chalked value — the "
                "rebinding visible inside the alcove, not the global mark. (count: 99)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)",
            expected=1,
            concept_phrase="the dynamic var rebound inside a binding form, read inside, then read again outside",
            question_what="the value of the dynamic var when read after the binding form unwound",
            goal_text="define a dynamic var *p* as 1, use binding to rebind it to 99 inside, and read its value after binding exits",

            scenario=(
                "Korvus chalked `1` on the pitcher's rim at the garden. "
                "Inside an alcove he re-chalked it to `99`, but when he "
                "stepped back out of the alcove the local chalk faded "
                "and the global mark of `1` reappeared on the rim."
            ),
            need=(
                "Outside the alcove he needed to read the rim and confirm "
                "the global mark had been restored after the binding unwound."
            ),
            mapping=(
                "`binding` re-chalks only for the duration of its body. "
                "Once the form exits, the local mark dissolves and the "
                "original global chalk is visible again. Reading `*p*` after "
                "binding sees the restored global value."
            ),
            resolution=(
                "The pitcher returned the global chalk mark — the original "
                "value restored after the binding form exited. (count: 99)"
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
    fable="crow-pitcher",
    examples=[
        # `locking` takes a monitor and a body; we use a simple body.
        SubjectExample(
            form="(do (def lock (Object.)) (locking lock (+ 1 2)))",
            expected=3,
            concept_phrase="the arithmetic evaluated inside a critical section guarded by locking",
            question_what="the value returned by evaluating an addition inside a locked critical section after creating a monitor and acquiring the lock",
            goal_text="create an object to use as a monitor, acquire the lock, and evaluate an addition inside",

            scenario=(
                "Caw placed a heavy stone at the pitcher's mouth at the "
                "market to serve as a gate. Only she could move it. She "
                "rolled the stone aside, added one and two inside the "
                "sealed section, then rolled it back."
            ),
            need=(
                "She needed to read the result of the addition computed "
                "inside the gate — the value returned from the locked body."
            ),
            mapping=(
                "`(Object.)` creates the gate-stone monitor. `locking` "
                "acquires it — blocking any other crow — and evaluates "
                "the body. The result of the body is returned on release."
            ),
            resolution=(
                'The pitcher returned the sum produced within the gate — the addition completed safely behind the locked section (with `1` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def lock (Object.)) (locking lock 42))",
            expected=42,
            concept_phrase="the literal value evaluated inside a critical section guarded by locking",
            question_what="the literal value returned by evaluating it inside a locked critical section after creating a monitor and acquiring the lock",
            goal_text="create an object to use as a monitor, acquire the lock, and evaluate a literal inside",

            scenario=(
                "Korvus planted a gate-stone at the pitcher's mouth on "
                "the road. He rolled it aside, placed a single stone "
                "tally inside the sealed section, then rolled the gate "
                "back — the tally was the body's only expression."
            ),
            need=(
                "He needed to confirm the tally literal was returned "
                "by the locked section after the gate reopened."
            ),
            mapping=(
                "`locking` acquires the monitor and evaluates its body. "
                "When the body is a literal, that literal is the return "
                "value. The gate-stone releases on exit, freeing the path."
            ),
            resolution=(
                "The pitcher returned the literal tally from inside the "
                "gate — the value present when the lock was released. (count: 42)"
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
    print(f"grade-9 crow-pitcher smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
