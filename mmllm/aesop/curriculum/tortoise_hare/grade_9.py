"""Grade 9 — state and concurrency primitives. Through tortoise-hare.

The fable's moral dynamic — Tortoise's careful, transactional updates
versus Hare's racing-without-coordination — maps cleanly onto the
state-and-concurrency primitives. Tortoise insists on dosync and CAS;
Hare wants to mutate without checking. The REPL settles every dispute.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.tortoise_hare.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.tortoise_hare._metaphor_pools import (
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
    fable="tortoise-hare",
    examples=[
        # `assoc` returns a new map; the original is unchanged.
        SubjectExample(
            form="(let [m {:a 1}] (assoc m :b 2) m)",
            expected={":a": 1},
            concept_phrase="binding a map, adding an entry to a new map, and returning the original",
            question_what="the original map after assoc returns a new map",
            goal_text="bind a map m, call assoc to add :b 2 to a new map, then return the unchanged m",
            scenario=(
                "Mossback the tortoise set her woven basket on the path, "
                "its single compartment :a holding one acorn gathered that "
                "morning. Pip the hare called out that she should tuck a "
                "second acorn into a new compartment :b. The values drawn fresh were {drawn.a}, {drawn.b}, and {drawn.c}."
            ),
            need=(
                "Mossback needed a fresh basket with both compartments — "
                "but she also needed the original basket to stay exactly "
                "as it was, :a and its acorn untouched."
            ),
            mapping=(
                "`assoc` builds a brand-new basket with the added "
                "compartment; the original basket `m` on the path stays "
                "unchanged. Returning `m` at the end confirms the "
                "original is unmodified."
            ),
            resolution=(
                "The original basket came back with only :a intact, "
                "proof that `assoc` never disturbs the basket it was "
                "handed."
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
                "Three smooth stones sat in a row on the meadow path — "
                "Mossback's tally-stones for the morning's laps. Pip "
                "suggested adding a fourth stone to mark an extra stretch, "
                "but Mossback wanted her original row kept exactly as it "
                "stood."
            ),
            need=(
                "Mossback needed proof that `conj` would produce a new "
                "row of four without disturbing the original three-stone "
                "row she had placed."
            ),
            mapping=(
                "`conj` adds the element to a brand-new vector; the "
                "original vector `v` is never touched. Returning `v` "
                "after `conj` confirms the original row is unchanged."
            ),
            resolution=(
                'The original three-stone row came back untouched — exactly as Mossback had placed it at the start (with `1` as the input value) (with `3` as the input value).'
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
    fable="tortoise-hare",
    examples=[
        # The minimal "place that needs identity over time" example.
        SubjectExample(
            form="(do (def counter (atom 0)) (swap! counter inc) @counter)",
            expected=1,
            concept_phrase="binding an atom to counter, atomically incrementing it, and dereferencing the result",
            question_what="the value after atomically swapping counter with inc and dereferencing",
            goal_text="construct an atom holding 0 as counter, atomically swap it by applying inc, and dereference the result",
            scenario=(
                "The meadow's berry-tally notebook sat open on the tree "
                "stump. Before any forager had returned, the page read "
                "zero. Mossback the tortoise was first back, one berry in "
                "her pouch. The value at the heart of the form was 0."
            ),
            need=(
                "The notebook needed to hold a running count that "
                "persisted between foragers' visits — a plain value "
                "cannot do that. Mossback needed to add her berry to "
                "whatever the page currently said."
            ),
            mapping=(
                "An `atom` is the notebook — a place that has identity "
                "over time. `swap!` atomically reads the page, applies "
                "`inc`, and writes the new tally back. `@counter` reads "
                "the page after the update."
            ),
            resolution=(
                "Mossback read the page and confirmed the tally had "
                "advanced by exactly her one contribution."
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
                "Mossback kept a small notebook on the stump to track "
                "the race's status. Before the starting horn, the page "
                "read the idle word. The horn sounded and the race began. The form's keyword to weigh was :idle."
            ),
            need=(
                "The status needed to change from idle to running the "
                "moment the race started — and the whole meadow shared "
                "that one page, so the update had to be authoritative."
            ),
            mapping=(
                "`reset!` replaces the atom's page with a new value "
                "outright, without reading the old one first. "
                "`@progress` reads the page to confirm the new status "
                "is in place."
            ),
            resolution=(
                "The page confirmed the running status — every forager "
                "glancing at the stump would now see the race was "
                "under way."
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(do (def a (atom 0)) (swap! a inc) @a)",
            expected=1,
            concept_phrase="the atom updated through a swap and read by deref",
            question_what="the running tally on the page after one foraging contribution",
            goal_text="set up a shared notebook starting at 0, atomically add one to its page, then read the page",
            scenario=(
                "The forest's berry-tally lived on a notebook open on "
                "the tree stump in the middle of the meadow. Anyone "
                "returning from foraging walked up, read the running "
                "total, and added their own count."
            ),
            need=(
                "Today's tally page started at 0 — no one had foraged "
                "yet. Mossback the tortoise's first handful was a "
                "single berry, and she wanted the page to reflect it."
            ),
            mapping=(
                "An `atom` is the notebook on the stump, named here "
                "`a`. `swap!` reads the current page, applies a "
                "function (here `inc`, adding one), and writes the new "
                "page back — all atomically. `@a` dereferences to read "
                "the page."
            ),
            resolution=(
                "Mossback dereferenced the page and read the new "
                "tally — one berry, exactly her contribution."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def a (atom 10)) (swap! a + 5) @a)",
            expected=15,
            concept_phrase="the atom whose value swap updates and deref reads",
            question_what="the value returned by dereferencing a after defining a as an atom holding 10 and swapping it via + 5",
            goal_text="construct an atom holding 10, atomically swap it by applying + to 5, and dereference the result",
            scenario=(
                "Ten acorns were already tallied on the notebook at the "
                "stump when Pip the hare arrived from the orchard with "
                "five more. The page needed updating before any other "
                "forager added to it."
            ),
            need=(
                "Pip needed to add her five to whatever the page "
                "currently showed — atomically, so no other forager's "
                "update could slip between her read and her write."
            ),
            mapping=(
                "`swap!` reads the atom's current value, applies `+` "
                "with the extra argument `5`, and writes the sum back "
                "as the new page — all in one atomic step. `@a` reads "
                "the resulting tally."
            ),
            resolution=(
                "The page showed the combined tally — the original ten "
                "plus Pip's five, exactly as the foraging records "
                "required."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def a (atom :start)) (reset! a :done) @a)",
            expected=":done",
            concept_phrase="the atom whose value reset replaces and deref reads",
            question_what="the value returned by dereferencing a after defining a as an atom holding a start keyword and resetting it to done",
            goal_text="construct an atom holding a start keyword, atomically reset it to a done keyword, and dereference the result",
            scenario=(
                "The notebook on the stump tracked whether the morning "
                "task was still open or complete. The page had been "
                "marked with the start word when foraging began. "
                "Mossback returned from the last patch with a full "
                "pouch."
            ),
            need=(
                "With all foraging finished, the page needed to change "
                "from its start marking to the done marking — replacing "
                "the old value entirely, not modifying it."
            ),
            mapping=(
                "`reset!` sets the atom's page to a new value "
                "unconditionally, bypassing any read of the old one. "
                "`@a` confirms the page now carries the done status."
            ),
            resolution=(
                'The page read the done marking — the morning task was officially closed on the shared notebook (with `:start` as the input value).'
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
    fable="tortoise-hare",
    examples=[
        # `compare-and-set!` succeeds when current matches expected.
        SubjectExample(
            form="(do (def a (atom 0)) (compare-and-set! a 0 1) @a)",
            expected=1,
            concept_phrase="the atom whose value compare-and-set updates and deref reads",
            question_what="the value returned by dereferencing a after defining a as an atom holding 0 and performing a successful compare-and-set to 1",
            goal_text="construct an atom holding 0, perform a compare-and-set checking for 0 and setting to 1, and dereference",
            scenario=(
                "The notebook on the stump held zero. Mossback had "
                "glanced at the page a moment before and was ready "
                "to write only if it still said zero. The value at the heart of the form was 0. The value at the heart of the form was 5."
            ),
            need=(
                "Mossback would update the page only if no other "
                "forager had changed it since she last looked."
            ),
            mapping=(
                "`compare-and-set!` checks the atom's page against "
                "the expected value; if they match, it writes the new "
                "value atomically. Here the page still said zero, so "
                "the update lands. `@a` reads the result."
            ),
            resolution=(
                "The page advanced to the new tally — the condition "
                "held, and the compare-and-set succeeded."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def a (atom 5)) (compare-and-set! a 0 99) @a)",
            expected=5,
            concept_phrase="the atom whose compare-and-set leaves the value untouched and deref reads",
            question_what="the value returned by dereferencing a after defining a as an atom holding 5 and attempting a compare-and-set that fails",
            goal_text="construct an atom holding 5, perform a compare-and-set checking for 0 and setting to 99, and dereference",
            scenario=(
                "The notebook held a tally of five — another forager "
                "had been there since Pip last looked. Pip had seen "
                "zero earlier and tried to update only if it still "
                "said zero."
            ),
            need=(
                "Pip's update was guarded: she would write the new "
                "value only if the page matched what she had seen. "
                "It did not — the page had moved on."
            ),
            mapping=(
                "`compare-and-set!` finds the atom's page does not "
                "match the expected value, so it leaves the page "
                "unchanged and returns `false`. `@a` confirms the "
                "original tally is still there."
            ),
            resolution=(
                "The page stayed at the original tally — the stale check protected the notebook from Pip's outdated write (with `5` as the input value)."
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
    fable="tortoise-hare",
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
                "Mossback tied a small bell to the corner of the "
                "notebook on the stump. Whenever a forager changed the "
                "tally page, the bell rang and a scribe noted the new "
                "value in a separate log notebook on the same stump. The form's keyword to weigh was :w."
            ),
            need=(
                "The head forager wanted an audit trail — every new "
                "value the main notebook took on should appear in the "
                "log, in order, so changes could be reviewed later."
            ),
            mapping=(
                "`add-watch` attaches a listener function to the atom; "
                "the listener receives the new value each time `swap!` "
                "changes the page and conjoins it to the log atom. "
                "`@log` reads the log notebook."
            ),
            resolution=(
                "The log held exactly one entry — the new tally after "
                "the single `swap!` — confirming the bell had rung and "
                "the scribe had written."
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
    fable="tortoise-hare",
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
                "The head forager appointed a referee to stand at the "
                "stump. Before any forager could change the tally "
                "notebook, the referee checked that the incoming value "
                "was a number — no words or symbols would be allowed on "
                "the page."
            ),
            need=(
                "Without the referee, a careless forager could write "
                "a nonsense entry. The validator ensured only numeric "
                "tallies would ever land on the page. The value at the heart of the form was 0."
            ),
            mapping=(
                "`set-validator!` installs a predicate on the atom; "
                "every proposed new value is tested by `number?` before "
                "the write is committed. A valid `inc` result passes, "
                "and the page updates. `@a` reads the validated tally."
            ),
            resolution=(
                "The page advanced to the incremented tally — the "
                "referee waved it through, and the notebook remained "
                "trustworthy."
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
    fable="tortoise-hare",
    examples=[
        # Refs require dosync to update.
        SubjectExample(
            form="(do (def r (ref 0)) (dosync (alter r inc)) @r)",
            expected=1,
            concept_phrase="the ref altered inside a transaction and read by deref",
            question_what="the value returned by dereferencing r after defining a ref holding 0, performing a transactional alter via inc, and dereferencing",
            goal_text="construct a ref holding 0, perform a transactional alter by applying inc inside dosync, and dereference",
            scenario=(
                "The ref notebook required any change to be made "
                "inside a fenced transaction zone. Mossback "
                "approached the stump to add one to the tally. The value at the heart of the form was 0."
            ),
            need=(
                "The transaction fence guaranteed that if anything "
                "went wrong mid-update the whole change would roll "
                "back. Mossback needed the page incremented safely "
                "within that guarantee."
            ),
            mapping=(
                "`ref` is the transactionally-protected notebook. "
                "`dosync` opens the transaction fence. `alter` reads "
                "the current page, applies `inc`, and writes the "
                "result — all inside the transaction. `@r` reads "
                "the final page."
            ),
            resolution=(
                "The page reflected the incremented tally — the "
                "transaction completed cleanly and the fence came "
                "down."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def r (ref 100)) (dosync (ref-set r 7)) @r)",
            expected=7,
            concept_phrase="the ref whose value ref-set replaces inside a transaction and deref reads",
            question_what="the value returned by dereferencing r after defining a ref holding 100, setting it to 7 inside dosync, and dereferencing",
            goal_text="construct a ref holding 100, perform a transactional ref-set to 7 inside dosync, and dereference",
            scenario=(
                "The ref notebook had held a large tally from a "
                "previous season's count. At the start of a new "
                "accounting period the head forager decided to "
                "overwrite the page entirely with a fresh small number, "
                "ignoring what was there before. The value at the heart of the form was 100."
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
                "the transaction."
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
    fable="tortoise-hare",
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
                "Two ref notebooks sat side by side on the stump — "
                "one tracking morning berries, one tracking afternoon "
                "berries. Mossback needed to increment both in a single "
                "accounting step so the two tallies would never be "
                "out of sync with each other. The value at the heart of the form was 1."
            ),
            need=(
                "If Mossback updated one notebook and something "
                "failed before the second, the records would be "
                "inconsistent. Both needed to advance together or "
                "not at all."
            ),
            mapping=(
                "`dosync` opens one transaction fence around both "
                "notebooks. Each `alter` increments its ref inside that "
                "fence. If the transaction commits, both pages advance; "
                "if it retries, both revert. `[@a @b]` reads both "
                "after the commit."
            ),
            resolution=(
                "Both pages showed their incremented tallies — the "
                "coordinated transaction kept the two notebooks "
                "perfectly in step."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def r (ref 10)) (dosync (alter r + 5)) @r)",
            expected=15,
            concept_phrase="the ref altered inside a transaction and read by deref",
            question_what="the value returned by dereferencing r after defining a ref holding 10, performing a transactional alter via + 5, and dereferencing",
            goal_text="construct a ref holding 10, perform a transactional alter by applying + with 5 inside dosync, and dereference",
            scenario=(
                "The ref notebook on the stump showed a tally of ten "
                "from the morning round. Pip the hare arrived with "
                "five more berries and needed to add them to the page "
                "inside the transaction fence."
            ),
            need=(
                "Pip's addition had to be atomic and transactional — "
                "the fence ensured that her read-then-write of the page "
                "would not conflict with any concurrent update."
            ),
            mapping=(
                "`dosync` opens the transaction. `alter` reads the "
                "ref's current tally, applies `+` with the extra "
                "argument `5`, and writes the sum back — all within "
                "the transaction. `@r` reads the committed page."
            ),
            resolution=(
                "The page showed the combined tally — ten plus five, "
                "committed cleanly by the transaction."
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
    fable="tortoise-hare",
    examples=[
        # The same operation expressed both ways.
        SubjectExample(
            form="(do (def a (atom 0)) (swap! a inc) @a)",
            expected=1,
            concept_phrase="the atom whose value swap updates and deref reads",
            question_what="the value returned by dereferencing a after defining an atom holding 0, swapping it via inc, and dereferencing",
            goal_text="construct an atom holding 0, atomically swap it by applying inc, and dereference",
            scenario=(
                "Mossback reached the stump with a single berry. She "
                "chose the lighter notebook — the atom — because only "
                "one forager updated the tally at a time, and no "
                "coordinated multi-notebook transaction was needed. The value at the heart of the form was 0."
            ),
            need=(
                "A single atomic page-update was all the task required. "
                "The atom's `swap!` would handle the read-modify-write "
                "in one step without the overhead of a dosync fence."
            ),
            mapping=(
                "`atom` gives a single notebook with `swap!` for "
                "atomic single-step updates. No transaction fence is "
                "needed. `@a` reads the result."
            ),
            resolution=(
                "The page advanced by one — the atom handled the "
                "single-notebook update cleanly and efficiently."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def r (ref 0)) (dosync (alter r inc)) @r)",
            expected=1,
            concept_phrase="the ref altered inside a transaction and read by deref",
            question_what="the value returned by dereferencing r after defining a ref holding 0, altering it via inc inside dosync, and dereferencing",
            goal_text="construct a ref holding 0, perform a transactional alter by applying inc inside dosync, and dereference",
            scenario=(
                "Mossback reached the stump with the same single "
                "berry, but this time the task was part of a larger "
                "coordinated accounting that spanned several notebooks. "
                "She chose the ref — the transactionally-protected "
                "notebook — for the update. The value at the heart of the form was 0."
            ),
            need=(
                "When multiple notebooks had to move together, the ref "
                "inside a `dosync` fence was the right tool — it "
                "guaranteed all-or-nothing across all the notebooks in "
                "the transaction."
            ),
            mapping=(
                "`ref` is the transactionally-protected notebook; "
                "`dosync` opens the fence; `alter` increments the "
                "page inside that fence. `@r` reads the committed "
                "tally."
            ),
            resolution=(
                "The page advanced by one — the ref's transaction "
                "committed, proving the same increment works through "
                "both the atom and the ref path."
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
    fable="tortoise-hare",
    examples=[
        # send is async — we await before reading.
        SubjectExample(
            form="(do (def ag (agent 0)) (send ag inc) (await ag) @ag)",
            expected=1,
            concept_phrase="the agent updated by send, awaited, and read by deref",
            question_what="the value returned by dereferencing ag after defining an agent holding 0, sending inc asynchronously, awaiting, and dereferencing",
            goal_text="construct an agent holding 0, asynchronously send inc to it, await its completion, and dereference",
            scenario=(
                "Mossback held a tally-scroll starting at zero. She "
                "dispatched a messenger to carry an increment task "
                "down the road, freeing her to carry on with other "
                "work while the messenger ran. The value at the heart of the form was 0."
            ),
            need=(
                "When Mossback eventually wanted the updated tally, she "
                "needed a way to wait for the messenger to finish — "
                "and then read whatever the messenger had written on "
                "the scroll."
            ),
            mapping=(
                "`agent` is the tally-scroll in the messenger's care. "
                "`send` dispatches `inc` to the messenger asynchronously. "
                "`await` waits until the messenger's queue is empty. "
                "`@ag` reads the scroll."
            ),
            resolution=(
                "The scroll showed the incremented tally — the "
                "messenger had finished, and Mossback collected the "
                "result on her return."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)",
            expected=15,
            concept_phrase="the agent updated by send, awaited, and read by deref",
            question_what="the value returned by dereferencing ag after defining an agent holding 5, sending + 10 asynchronously, awaiting, and dereferencing",
            goal_text="construct an agent holding 5, asynchronously send + with 10 to it, await its completion, and dereference",
            scenario=(
                "A messenger carried a tally-scroll already marked with "
                "a starting count. Mossback sent the messenger ahead "
                "with instructions to add ten more to the scroll while "
                "she finished packing her foraging kit."
            ),
            need=(
                "Mossback needed the messenger's addition complete "
                "before she read the scroll. She would wait at the "
                "crossroads until the messenger caught up."
            ),
            mapping=(
                "`send` dispatches `+` with the extra argument `10` "
                "to the agent asynchronously. `await` blocks until "
                "the messenger's action lands. `@ag` reads the updated "
                "scroll."
            ),
            resolution=(
                "The scroll showed the combined tally — the starting "
                "count plus ten, exactly as the messenger had been "
                "instructed."
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(do (def ag (agent 0)) (send ag inc) (await ag) @ag)",
            expected=1,
            concept_phrase="the agent updated by send, awaited, and read by deref",
            question_what="the value returned by dereferencing ag after defining an agent holding 0, using send to dispatch inc, awaiting, and dereferencing",
            goal_text="construct an agent holding 0, use send to asynchronously apply inc, await its completion, and dereference",
            scenario=(
                "Mossback needed a quick errand done on a shared-pool "
                "runner — the kind reserved for short, fast tasks that "
                "would not block the pool. She dispatched the messenger "
                "with `send` to increment the scroll. The value at the heart of the form was 0."
            ),
            need=(
                "The `send` path uses a bounded thread pool suitable "
                "for CPU-light work. Mossback needed the increment to "
                "land before she read the scroll."
            ),
            mapping=(
                "`send` dispatches the function to the agent on the "
                "shared CPU pool — right for fast, non-blocking work. "
                "`await` waits for delivery. `@ag` reads the result."
            ),
            resolution=(
                "The scroll showed the incremented tally — the `send` "
                "messenger returned promptly from the shared pool."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)",
            expected=1,
            concept_phrase="the agent updated by send-off on a blocking thread, awaited, and read by deref",
            question_what="the value returned by dereferencing ag after defining an agent holding 0, using send-off to dispatch inc, awaiting, and dereferencing",
            goal_text="construct an agent holding 0, use send-off to asynchronously apply inc, await its completion, and dereference",
            scenario=(
                "For an errand that might involve waiting — perhaps "
                "pausing at the river, or resting in the sun — Mossback "
                "chose `send-off`, which dispatches the messenger on "
                "an expandable pool that can block without starving "
                "the fast runners. The value at the heart of the form was 0."
            ),
            need=(
                "The task might park for a moment. Using `send` on a "
                "potentially-blocking errand would tie up a shared-pool "
                "thread; `send-off` was the right choice."
            ),
            mapping=(
                "`send-off` dispatches to the unbounded I/O-friendly "
                "pool — right for potentially-blocking work. `await` "
                "waits. `@ag` reads the result once the runner "
                "returns."
            ),
            resolution=(
                "The scroll showed the incremented tally — the "
                "`send-off` messenger completed without blocking the "
                "fast-runner pool."
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)",
            expected=2,
            concept_phrase="the agent updated twice by send, awaited, and read by deref",
            question_what="the value returned by dereferencing ag after defining an agent holding 0, sending inc twice asynchronously, awaiting, and dereferencing",
            goal_text="construct an agent holding 0, asynchronously send inc twice, synchronize with await, and dereference",
            scenario=(
                "Mossback sent two messengers down the road in quick "
                "succession, each carrying an increment task for the "
                "same tally-scroll. The second messenger would wait "
                "for the first to finish before applying its own "
                "increment. The value at the heart of the form was 0."
            ),
            need=(
                "Both increments had to land before Mossback read "
                "the scroll. She called `await` at the crossroads to "
                "block until the last messenger's queue was fully "
                "drained."
            ),
            mapping=(
                "Two `send` calls queue two sequential increments on "
                "the agent. `await` blocks until all queued actions "
                "complete. `@ag` reads the final scroll value after "
                "both increments."
            ),
            resolution=(
                "The scroll showed the tally advanced by two — both "
                "messengers had returned and the await had confirmed "
                "the queue was clear."
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="@(future (+ 1 2))",
            expected=3,
            concept_phrase="the future computing the sum and read by deref",
            question_what="the value the messenger returns from adding 1 and 2",
            goal_text="dispatch a runner to compute the sum of 1 and 2; later, ask the runner for the answer",
            scenario=(
                "Mossback the tortoise dispatched a young messenger "
                "down the road to compute the sum of 1 and 2 while she "
                "carried on with her own work."
            ),
            need=(
                "When she eventually wanted the messenger's answer, "
                "she'd need a way to ask for it — and to wait if the "
                "messenger hadn't quite returned yet."
            ),
            mapping=(
                "`future` sends the work down the road as a "
                "runner-sent-ahead. `@` (deref) asks for the runner's "
                "answer when needed; if the runner is still running, "
                "the runtime waits until they return."
            ),
            resolution=(
                "the messenger had finished by the time Mossback "
                "dereferenced — the answer came back cleanly, exactly "
                "the sum the runner had computed."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="@(future (* 6 7))",
            expected=42,
            concept_phrase="the future computing the product and read by deref",
            question_what="the value returned by dereferencing a future that multiplies 6 and 7",
            goal_text="construct a future that multiplies 6 and 7, and dereference it",
            scenario=(
                "Pip the hare dispatched a runner ahead to compute "
                "the product of two numbers — how many acorns in six "
                "groups of seven — while Pip herself carried on "
                "gathering at the near patch."
            ),
            need=(
                "Pip needed the multiplication result before sorting "
                "the acorns into baskets. She would wait at the "
                "sorting-stone for the runner to return with the "
                "answer."
            ),
            mapping=(
                "`future` sends `(* 6 7)` down the road as a "
                "runner-sent-ahead, computing on a background thread. "
                "`@` dereferences the future, waiting if the runner "
                "has not yet returned, then returning the result."
            ),
            resolution=(
                "The runner returned with the product — the exact "
                "count Pip needed to divide the baskets evenly."
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(do (def a (atom 7)) @a)",
            expected=7,
            concept_phrase="constructing an atom and extracting its value using the @ shorthand",
            question_what="the value extracted from an atom using @",
            goal_text="construct an atom holding 7 and dereference it using @",
            scenario=(
                "The notebook on the stump had a page already written "
                "by the morning's foragers. Mossback the tortoise "
                "wanted to glance at the page without changing anything "
                "— just read what was there. The value at the heart of the form was 7."
            ),
            need=(
                "Mossback needed only to look at the current page. "
                "The `@` shorthand was the quickest way to peek at "
                "the notebook without any transaction or swap."
            ),
            mapping=(
                "`@a` is the shorthand for `(deref a)` — it reads the "
                "notebook's current page and returns the value there. "
                "No update, no swap, just a look at the page."
            ),
            resolution=(
                "The page showed the tally exactly as the foragers "
                "had written it — the deref confirmed the notebook's "
                "current state."
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
                "Mossback wanted to read the notebook page using the "
                "long-form name — writing out `deref` in full rather "
                "than using the `@` shorthand, for clarity in her "
                "notes."
            ),
            need=(
                "The result was the same whichever form she used. "
                "She needed the page's value, and `deref` named the "
                "operation explicitly for readers of her notebook."
            ),
            mapping=(
                "`deref` is the function form of the `@` reader "
                "shorthand — both read the atom's current page. "
                "Using `deref` by name makes the operation's intent "
                "explicit in the code."
            ),
            resolution=(
                'The page value came back unchanged — `deref` and `@` are two spellings of the same peek at the notebook (with `7` as the input value).'
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(do (def p (promise)) (deliver p :done) @p)",
            expected=":done",
            concept_phrase="the promise fulfilled by deliver and read by deref",
            question_what="the value returned by dereferencing a promise after defining it, delivering a keyword to it, and dereferencing",
            goal_text="construct a promise, deliver a completion keyword to it, and dereference to get the delivered value",
            scenario=(
                "Mossback sent a sealed scroll ahead of the race — a "
                "promise that a result would arrive before anyone tried "
                "to read it. The scroll was empty when it left her "
                "paws, waiting to be filled. The form's keyword to weigh was :done."
            ),
            need=(
                "When the task finished, someone needed to unseal the "
                "scroll and write the result inside. Any reader who "
                "arrived before that moment would simply wait."
            ),
            mapping=(
                "`promise` creates the sealed scroll — an unfulfilled "
                "placeholder. `deliver` opens the seal and writes the "
                "value once. `@p` reads the scroll, blocking if "
                "delivery has not happened yet."
            ),
            resolution=(
                "The scroll opened to the delivered keyword — the "
                "promise had been kept and the reader received the "
                "answer."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def p (promise)) (deliver p 42) @p)",
            expected=42,
            concept_phrase="the promise fulfilled by deliver and read by deref",
            question_what="the value returned by dereferencing a promise after defining it, delivering a number to it, and dereferencing",
            goal_text="construct a promise, deliver 42 to it, and dereference to get the delivered value",
            scenario=(
                "Pip the hare created a sealed scroll before setting "
                "off to count the orchard's acorns. She promised "
                "Mossback the total would be written on the scroll "
                "when she returned. Mossback waited at the stump. The value at the heart of the form was 42."
            ),
            need=(
                "Mossback needed to read the scroll only after Pip "
                "had delivered the count. The promise guaranteed "
                "the scroll would block any reader until Pip wrote "
                "on it."
            ),
            mapping=(
                "`promise` is the sealed scroll. `deliver` writes the "
                "count onto the scroll — it can only happen once. "
                "`@p` reads the scroll, returning the delivered value "
                "the moment it is available."
            ),
            resolution=(
                "The scroll opened to the delivered count — Pip's "
                "promise was fulfilled and Mossback read the answer "
                "without having to ask again."
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(do (def v (volatile! 0)) (vswap! v inc) @v)",
            expected=1,
            concept_phrase="the volatile updated through vswap and read by deref",
            question_what="the value returned by dereferencing v after defining a volatile holding 0, performing a non-transactional swap via inc, and dereferencing",
            goal_text="construct a volatile holding 0, perform a non-transactional swap by applying inc, and dereference",
            scenario=(
                "For a quick-and-dirty tally used only within one "
                "runner's stretch of road — never shared across "
                "threads — Mossback reached for the lightweight "
                "notebook: the volatile. No transaction fence, no "
                "atomic retry, just a fast local update. The value at the heart of the form was 0."
            ),
            need=(
                "The atom's overhead was unnecessary when only one "
                "runner would ever touch this page. Mossback needed "
                "the increment to land without the cost of full "
                "atomicity."
            ),
            mapping=(
                "`volatile!` creates the lightweight notebook — "
                "visible across threads for visibility but offering "
                "no atomic compare-and-swap guarantee. `vswap!` "
                "increments the page directly. `@v` reads the result."
            ),
            resolution=(
                "The page showed the incremented tally — the volatile "
                "updated quickly, exactly right for single-threaded "
                "local use."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def v (volatile! 5)) (vreset! v 99) @v)",
            expected=99,
            concept_phrase="the volatile whose value vreset replaces and deref reads",
            question_what="the value returned by dereferencing v after defining a volatile holding 5, performing a non-transactional reset to 99, and dereferencing",
            goal_text="construct a volatile holding 5, perform a non-transactional reset to 99, and dereference",
            scenario=(
                "Mossback's local volatile notebook held a small "
                "interim count from the first half of the path. At "
                "the midpoint she decided to restart the count from "
                "scratch with a large new value, overwriting the "
                "old page entirely. The value at the heart of the form was 5."
            ),
            need=(
                "She needed to replace the page outright — not add "
                "to it. `vreset!` was the direct overwrite for the "
                "volatile, with no transaction overhead needed."
            ),
            mapping=(
                "`vreset!` sets the volatile's page directly to the "
                "given value, discarding the old one — the volatile "
                "equivalent of `reset!` on an atom. `@v` reads the "
                "new page."
            ),
            resolution=(
                "The page showed the large replacement value — the "
                "volatile's overwrite landed immediately, and the "
                "old interim count was gone."
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))",
            expected=99,
            concept_phrase="the dynamic var whose value binding rebinds and the body reads",
            question_what="the value of the dynamic var when read inside the binding form after defining it and rebinding",
            goal_text="define a dynamic var *p* as 1, use binding to rebind it to 99, and read its value inside",
            scenario=(
                "Every runner on the path shared the same posted "
                "default from the road-sign — a dynamic var that any "
                "runner could temporarily shadow with a personal "
                "handbook for one stretch of road. Mossback opened "
                "her personal handbook, overriding the default for "
                "the duration of her stretch."
            ),
            need=(
                "Inside her stretch Mossback needed her own value, "
                "not the meadow's shared default. The `binding` form "
                "gave her a private page for exactly that stretch."
            ),
            mapping=(
                "`def ^:dynamic` establishes the shared default on "
                "the road-sign. `binding` opens a personal handbook "
                "for this thread, shadowing the default with the new "
                "value. Reading `*p*` inside returns the personal "
                "handbook's page."
            ),
            resolution=(
                "The personal handbook's page came back — the binding "
                "form's override was in force for exactly the stretch "
                "it covered."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)",
            expected=1,
            concept_phrase="the dynamic var whose binding rebind ends with the body, leaving the original visible afterward",
            question_what="the value of the dynamic var when read after the binding form unwound",
            goal_text="define a dynamic var *p* as 1, use binding to rebind it to 99 inside, and read its value after binding exits",
            scenario=(
                "Mossback's personal handbook was open only for her "
                "stretch of the road. Once she finished that stretch "
                "and closed the handbook, any runner reading the "
                "road-sign again would see the original shared "
                "default."
            ),
            need=(
                "After the `binding` form exited, the road-sign should "
                "revert to the global default — Mossback's private "
                "override must not leak beyond her stretch."
            ),
            mapping=(
                "When the `binding` form exits, the thread's personal "
                "handbook is closed and the dynamic var reverts to "
                "the root binding established by `def`. Reading "
                "`*p*` outside the form returns the shared default."
            ),
            resolution=(
                "The road-sign showed the original default — the binding's scope ended cleanly, leaving the shared value untouched (with `99` as the input value)."
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
    fable="tortoise-hare",
    examples=[
        # `locking` takes a monitor and a body; we use a simple body.
        SubjectExample(
            form="(do (def lock (Object.)) (locking lock (+ 1 2)))",
            expected=3,
            concept_phrase="the arithmetic guarded by a locking block on a lock object",
            question_what="the value returned by evaluating an addition inside a locked critical section after creating a monitor and acquiring the lock",
            goal_text="create an object to use as a monitor, acquire the lock, and evaluate an addition inside",
            scenario=(
                "Mossback built a fence around the notebook on the "
                "stump — the last-resort guard for when atom and ref "
                "were not enough. Only the runner holding the fence-key "
                "could enter the critical section at a time. The value at the heart of the form was 1."
            ),
            need=(
                "A body of work needed exclusive access — no other "
                "runner could enter until the current one left. "
                "Mossback acquired the fence-key before computing "
                "inside."
            ),
            mapping=(
                "`(Object.)` creates the fence-key object — the JVM "
                "monitor. `locking` acquires the monitor, evaluates "
                "the body exclusively, then releases the key. The "
                "body's return value is the form's result."
            ),
            resolution=(
                "The addition's result came back cleanly — the "
                "critical section executed without interruption, and "
                "the fence was released when Mossback stepped out."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def lock (Object.)) (locking lock 42))",
            expected=42,
            concept_phrase="the literal returned from a locking block on a lock object",
            question_what="the literal value returned by evaluating it inside a locked critical section after creating a monitor and acquiring the lock",
            goal_text="create an object to use as a monitor, acquire the lock, and evaluate a literal inside",
            scenario=(
                "Pip the hare wanted to understand the locking fence "
                "by using the simplest possible body — a bare value "
                "that needed no computation. She grabbed the fence-key "
                "and stepped inside just long enough to read the "
                "value off the page. The value at the heart of the form was 42."
            ),
            need=(
                "Even a trivial body inside `locking` demonstrates "
                "the exclusion guarantee. Pip needed to show that the "
                "lock acquired and released correctly around any "
                "expression."
            ),
            mapping=(
                "`locking` acquires the monitor on the fence-key "
                "object, evaluates the body — here a bare literal — "
                "and returns it while holding exclusive access. The "
                "lock releases when the body exits."
            ),
            resolution=(
                "The literal value came back — the fence worked "
                "correctly even with the simplest body, confirming "
                "the lock acquired and released as expected."
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
    print(f"grade-9 tortoise-hare smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
