"""Grade 9 — state and concurrency primitives. through the milkmaid fable.

The fable's moral dynamic — Farmer's careful, transactional updates
versus Milkmaid's racing-without-coordination — maps cleanly onto the
state-and-concurrency primitives. Farmer insists on dosync and CAS;
Milkmaid wants to mutate without checking. The REPL settles every dispute.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.milkmaid.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.milkmaid._metaphor_pools import (
    _BASKET_SUBPLOTS, _NOTEBOOK_SUBPLOTS, _RUNNERAHEAD_SUBPLOTS,
)


# ─────────────────────── grade-9 subplot pool ───────────────────────
#
# Use goal-style subplots exclusively for grade 9. State and concurrency
# primitives require the model to write the form from the goal, not copy
# from prompt — this prevents form-leak training pathology.

_SUBPLOTS: list[SubplotTemplate] = _GOAL_SUBPLOTS


def _ex(form, expected, concept, what, goal=""):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal)


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
    fable="milkmaid",
    examples=[
        # `assoc` returns a new map; the original is unchanged.
        SubjectExample(
            form="(let [m {:a 1}] (assoc m :b 2) m)",
            expected={":a": 1},
            concept_phrase="binding a map, adding an entry to a new map, and returning the original",
            question_what="the original map after assoc returns a new map",
            goal_text="bind a map m, call assoc to add :b 2 to a new map, then return the unchanged m",
            scenario=(
                "The milkmaid packed her market-basket for the morning round: one "
                "compartment held cream, neatly sealed. The farmer asked her to add "
                "a second compartment for butter without disturbing the first."
            ),
            need=(
                "She needed to produce a basket with both compartments — but the "
                "original basket had to remain exactly as it was, cream intact, in "
                "case the buyer inspected the original pail."
            ),
            mapping=(
                "`assoc` builds a new basket with the extra compartment added; the "
                "original basket is never opened or changed. Returning `m` at the "
                "end reads what the original basket still holds."
            ),
            resolution=(
                "The REPL returned the original basket unchanged — the new compartment "
                "lived only in the fresh basket, and the first pail stayed sealed — :b."
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
                "The milkmaid set three pails in a row by the dairy door and "
                "wanted to note a fourth delivery without disturbing the first "
                "three. The farmer watched to see if the original row would change."
            ),
            need=(
                "She needed to conjoin a fourth pail to the record while proving "
                "that the original row of three remained untouched — the pail "
                "count depended on reading the original row back correctly."
            ),
            mapping=(
                "`conj` produces a new row with the fourth pail appended; it never "
                "reaches into the original row. Returning `v` at the end reads the "
                "original three-pail row that was never altered."
            ),
            resolution=(
                "The REPL returned the original three-pail row — the fourth pail "
                "existed only in the new row, and the first row remained intact — 4."
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
    fable="milkmaid",
    examples=[
        # The minimal "place that needs identity over time" example.
        SubjectExample(
            form="(do (def counter (atom 0)) (swap! counter inc) @counter)",
            expected=1,
            concept_phrase="binding an atom to counter, atomically incrementing it, and dereferencing the result",
            question_what="the value after atomically swapping counter with inc and dereferencing",
            goal_text="construct an atom holding 0 as counter, atomically swap it by applying inc, and dereference the result",
            scenario=(
                "The milkmaid hung a fresh tally-slate by the dairy door with the "
                "number 0 chalked at the top — the starting count for the day's "
                "deliveries. The first pail went out; the slate needed updating."
            ),
            need=(
                "She needed to erase the old mark and chalk a new one — not replace "
                "the slate, but update it in place, as if the dairy door itself "
                "remembered."
            ),
            mapping=(
                "`atom` is the tally-slate; `swap!` is the chalk-update: it reads "
                "the current mark, applies `inc` to get the next count, and chalks "
                "the new number without replacing the slate. `@` reads what the "
                "slate says now."
            ),
            resolution=(
                "The REPL read the slate and returned the result — one delivery tallied, the "
                "slate faithfully updated after the first pail left the door."
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
                "The milkmaid chalked the day's status on the tally-slate by the "
                "dairy door: it read 'idle' while the herd was still gathered. "
                "Once the first pail was filled, the whole slate needed a fresh mark."
            ),
            need=(
                "She needed to overwrite the old chalk mark entirely — not add to "
                "it, but replace it outright — so every farmer who glanced at the "
                "slate would see the current status without confusion."
            ),
            mapping=(
                "`reset!` erases whatever the tally-slate currently says and writes "
                "the new mark in one stroke, with no regard for the old value. "
                "`@` reads what the slate says after the overwrite."
            ),
            resolution=(
                "The REPL read the slate and returned the new status — the idle "
                "mark was gone, replaced in a single chalk stroke, and the dairy "
                "door showed the current state — :running."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(do (def a (atom 0)) (swap! a inc) @a)",
            expected=1,
            concept_phrase="the atom updated with swap and read with deref",
            question_what="the running tally on the page after one foraging contribution",
            goal_text="set up a shared notebook starting at 0, atomically add one to its page, then read the page",
            scenario=(
                "The milkmaid hung a blank tally-slate by the dairy door, marked "
                "with a zero at the start of the morning. The first pail left for "
                "the market, and the slate had to record it."
            ),
            need=(
                "She needed the slate to track each pail dispatched — starting "
                "from zero and growing by one with every delivery — so any farmer "
                "passing the door could read the current count."
            ),
            mapping=(
                "`atom` is the tally-slate; `swap!` applies `inc` as a chalk-update "
                "in one unbreakable motion, reading the old mark and writing the "
                "next number. `@` reads what the slate says now."
            ),
            resolution=(
                'The REPL read the slate and returned the updated count — one pail tallied, the chalk mark correct after the first delivery (with `0` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def a (atom 10)) (swap! a + 5) @a)",
            expected=15,
            concept_phrase="the atom-swap-deref pattern",
            question_what="the value returned by dereferencing a after defining a as an atom holding 10 and swapping it via + 5",
            goal_text="construct an atom holding 10, atomically swap it by applying + to 5, and dereference the result",
            scenario=(
                "Ten pails were already tallied on the slate by the dairy door "
                "when a second batch of five arrived. The milkmaid needed to add "
                "them all to the running count in a single chalk-update."
            ),
            need=(
                "She needed the slate to absorb the new five pails without anyone "
                "reading a half-finished tally — the update had to happen in one "
                "unbroken motion from the old mark to the new one."
            ),
            mapping=(
                "`swap!` reads the current slate value, applies `+ 5` to it, and "
                "writes the result back atomically. `@` reads the updated mark "
                "after the chalk-update is complete."
            ),
            resolution=(
                "The REPL read the slate and returned the combined count — the "
                "second batch was absorbed and the tally reflected the full "
                "morning's deliveries."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def a (atom :start)) (reset! a :done) @a)",
            expected=":done",
            concept_phrase="the atom reset and read",
            question_what="the value returned by dereferencing a after defining a as an atom holding a start keyword and resetting it to done",
            goal_text="construct an atom holding a start keyword, atomically reset it to a done keyword, and dereference the result",
            scenario=(
                "The milkmaid chalked the word 'start' on the tally-slate by the "
                "dairy door to mark that the morning round had begun. When the "
                "last pail was delivered, the slate needed a fresh mark entirely."
            ),
            need=(
                "She needed to overwrite the old status word completely — not "
                "update it step by step, but replace it in a single chalk stroke "
                "so the door showed 'done' the moment the round ended."
            ),
            mapping=(
                "`reset!` ignores whatever the slate currently says and writes the "
                "new value in one stroke, replacing old mark with new. `@` reads "
                "what the slate says after the overwrite."
            ),
            resolution=(
                "The REPL read the slate and returned the new status — the round "
                "was marked complete, the old word erased and replaced in one "
                "unbroken motion — :done."
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
    fable="milkmaid",
    examples=[
        # `compare-and-set!` succeeds when current matches expected.
        SubjectExample(
            form="(do (def a (atom 0)) (compare-and-set! a 0 1) @a)",
            expected=1,
            concept_phrase="the atom with compare-and-set",
            question_what="the value returned by dereferencing a after defining a as an atom holding 0 and performing a successful compare-and-set to 1",
            goal_text="construct an atom holding 0, perform a compare-and-set checking for 0 and setting to 1, and dereference",
            scenario=(
                "The milkmaid checked the tally-slate by the dairy door: it read "
                "zero, exactly as she expected. She would update it to one — but "
                "only if no other farmer had touched the slate first."
            ),
            need=(
                "She needed to confirm the current mark matched before chalking a "
                "new value — an unsafe update on a stale mark would corrupt the tally."
            ),
            mapping=(
                "`compare-and-set!` reads the slate, checks the expected mark, and "
                "writes only when they match. `@` reads the slate after the attempt."
            ),
            resolution=(
                'The REPL read the slate and returned the updated count — the marks matched and the chalk-update succeeded (with `0` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def a (atom 5)) (compare-and-set! a 0 99) @a)",
            expected=5,
            concept_phrase="the atom with a failed compare-and-set",
            question_what="the value returned by dereferencing a after defining a as an atom holding 5 and attempting a compare-and-set that fails",
            goal_text="construct an atom holding 5, perform a compare-and-set checking for 0 and setting to 99, and dereference",
            scenario=(
                "The milkmaid arrived expecting the tally-slate to read zero, but "
                "another farmer had already marked five pails since dawn. She tried "
                "to overwrite the slate with a new number anyway."
            ),
            need=(
                "The conditional chalk-update needed to fail silently — the slate "
                "showed five, not zero, so no new mark should be written."
            ),
            mapping=(
                "`compare-and-set!` checks the slate against the expected mark; "
                "since they differ, no chalk touches it. `@` reads the original "
                "value still held there."
            ),
            resolution=(
                "The REPL read the slate and returned the original count — the "
                "failed compare left the tally exactly as the other farmer wrote it — 99."
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
    fable="milkmaid",
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
                "The milkmaid hung a tally-slate by the dairy door and nailed a "
                "log-slate beside it. She wanted every chalk-update on the first "
                "to be copied onto the second automatically."
            ),
            need=(
                "She needed a watcher pinned to the tally-slate that would conjoin "
                "each new mark onto the log-slate without her writing it twice."
            ),
            mapping=(
                "`add-watch` fires whenever `swap!` chalks a new number, conjoining "
                "it onto the log-slate. `@log` reads what the log-slate collected."
            ),
            resolution=(
                'The REPL read the log-slate and returned its collected entries — every update had been captured by the watcher (with `:w` as the input value).'
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
    fable="milkmaid",
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
                "The farmer posted a rule at the dairy door: only numbers may be "
                "chalked on the tally-slate. The milkmaid hung the slate, wrote zero "
                "as the opening mark, and then applied the daily increment."
            ),
            need=(
                "She needed the rule to guard the slate — rejecting any chalk-update "
                "that tried to write a non-number — so the tally would remain a "
                "reliable count all day."
            ),
            mapping=(
                "`set-validator!` is the door-rule pinned to the tally-slate: any "
                "`swap!` that would produce a non-number is rejected outright. "
                "`@` reads what the slate holds after the validated chalk-update."
            ),
            resolution=(
                'The REPL read the slate and returned the updated count — the chalk-update passed the door-rule, and the tally advanced safely (with `0` as the input value).'
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
    fable="milkmaid",
    examples=[
        # Refs require dosync to update.
        SubjectExample(
            form="(do (def r (ref 0)) (dosync (alter r inc)) @r)",
            expected=1,
            concept_phrase="the ref altered inside dosync",
            question_what="the value returned by dereferencing r after defining a ref holding 0, performing a transactional alter via inc, and dereferencing",
            goal_text="construct a ref holding 0, perform a transactional alter by applying inc inside dosync, and dereference",
            scenario=(
                "The farmer hung a tally-slate by the dairy door and ruled that any "
                "chalk-update must happen inside a locked transaction — no stray "
                "marks permitted."
            ),
            need=(
                "She needed to increment the count safely inside a dosync block so "
                "no other farmer could read a half-written tally."
            ),
            mapping=(
                "`ref` is the tally-slate; `dosync` is the locked window; `alter` "
                "applies `inc` inside it. `@` reads the slate after the window closes."
            ),
            resolution=(
                'The REPL read the slate and returned the updated count — the transactional chalk-update completed safely (with `0` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def r (ref 100)) (dosync (ref-set r 7)) @r)",
            expected=7,
            concept_phrase="the ref reset inside dosync",
            question_what="the value returned by dereferencing r after defining a ref holding 100, setting it to 7 inside dosync, and dereferencing",
            goal_text="construct a ref holding 100, perform a transactional ref-set to 7 inside dosync, and dereference",
            scenario=(
                "The tally-slate showed a high count from the previous week. A new "
                "delivery season began, and the farmer needed to overwrite the old "
                "total inside a locked transaction."
            ),
            need=(
                "She needed to replace the old mark outright in one locked stroke, "
                "not add to it, so every farmer would see the fresh starting count."
            ),
            mapping=(
                "`ref-set` inside `dosync` erases the slate's current mark and "
                "writes the new value in one locked motion. `@` reads the result."
            ),
            resolution=(
                "The REPL read the slate and returned the new count — the old mark "
                "was replaced in a single transactional stroke — 7."
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
    fable="milkmaid",
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
                "Two tally-slates hung by the dairy door: one for morning deliveries, "
                "one for afternoon. The farmer needed to increment both counts at "
                "exactly the same moment — no farmer could see one updated without "
                "the other."
            ),
            need=(
                "She needed both chalk-updates to happen inside a single locked "
                "transaction so no one reading the door could ever see a half-updated "
                "pair of tallies."
            ),
            mapping=(
                "`dosync` opens one locked transaction window for both slates; each "
                "`alter` inside it applies `inc` to its respective tally-slate. "
                "Both slates are updated atomically — either both advance, or neither does."
            ),
            resolution=(
                'The REPL read both slates and returned the updated pair — each tally had advanced by one inside the single coordinated transaction (with `1` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def r (ref 10)) (dosync (alter r + 5)) @r)",
            expected=15,
            concept_phrase="the ref altered inside dosync",
            question_what="the value returned by dereferencing r after defining a ref holding 10, performing a transactional alter via + 5, and dereferencing",
            goal_text="construct a ref holding 10, perform a transactional alter by applying + with 5 inside dosync, and dereference",
            scenario=(
                "The tally-slate by the dairy door showed ten pails already counted "
                "from the morning round. Five more pails arrived in the afternoon, "
                "and the farmer needed to add them inside a locked transaction."
            ),
            need=(
                "She needed to chalk the five new pails onto the existing ten in a "
                "single transactional stroke, so no other farmer would read the "
                "slate mid-update and see an incomplete total."
            ),
            mapping=(
                "`alter` inside `dosync` reads the current slate mark, applies "
                "`+ 5` to it, and writes the new total back inside the locked "
                "window. `@` reads what the slate holds after the transaction closes."
            ),
            resolution=(
                "The REPL read the slate and returned the combined count — the "
                "five afternoon pails were added safely in one locked stroke."
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
    fable="milkmaid",
    examples=[
        # The same operation expressed both ways.
        SubjectExample(
            form="(do (def a (atom 0)) (swap! a inc) @a)",
            expected=1,
            concept_phrase="the atom-swap-deref pattern",
            question_what="the value returned by dereferencing a after defining an atom holding 0, swapping it via inc, and dereferencing",
            goal_text="construct an atom holding 0, atomically swap it by applying inc, and dereference",
            scenario=(
                "The farmer had two tally-slates to choose from for recording the "
                "day's first pail. One slate worked alone without any special lock; "
                "the other required opening a locked transaction window first."
            ),
            need=(
                "She needed to see how the solo slate — the atom — handled an "
                "increment with no surrounding transaction, so she could compare "
                "it against the ref's transactional approach."
            ),
            mapping=(
                "`atom` is the solo tally-slate; `swap!` chalks the increment "
                "directly without a `dosync` wrapper — the atom handles its own "
                "internal coordination. `@` reads the slate afterward."
            ),
            resolution=(
                'The REPL read the atom slate and returned the incremented count — the solo chalk-update succeeded with no transaction required (with `0` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def r (ref 0)) (dosync (alter r inc)) @r)",
            expected=1,
            concept_phrase="the ref altered inside dosync",
            question_what="the value returned by dereferencing r after defining a ref holding 0, altering it via inc inside dosync, and dereferencing",
            goal_text="construct a ref holding 0, perform a transactional alter by applying inc inside dosync, and dereference",
            scenario=(
                "The farmer turned to the second tally-slate — the one requiring a "
                "locked transaction — to perform the same increment as the atom. "
                "She opened the dosync window and made the chalk-update inside it."
            ),
            need=(
                "She needed the transactional slate to accept the increment inside a "
                "locked window, confirming that refs can coordinate multiple slates "
                "when needed — unlike the solo atom."
            ),
            mapping=(
                "`ref` is the tally-slate requiring a transaction; `dosync` opens "
                "the locked window; `alter` applies `inc` inside it. `@` reads "
                "the slate after the window closes."
            ),
            resolution=(
                'The REPL read the ref slate and returned the same incremented count as the atom — same result, different coordination mechanism (with `0` as the input value).'
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
    fable="milkmaid",
    examples=[
        # send is async — we await before reading.
        SubjectExample(
            form="(do (def ag (agent 0)) (send ag inc) (await ag) @ag)",
            expected=1,
            concept_phrase="the agent updated with send and read after await",
            question_what="the value returned by dereferencing ag after defining an agent holding 0, sending inc asynchronously, awaiting, and dereferencing",
            goal_text="construct an agent holding 0, asynchronously send inc to it, await its completion, and dereference",
            scenario=(
                "The farmer sent a swift runner ahead to the buyer's stall with a "
                "message: 'increment the day's count when you arrive.' She didn't "
                "wait for the runner to return — she kept milking while the runner "
                "moved."
            ),
            need=(
                "She needed the runner to carry `inc` to the agent ahead; she needed "
                "to carry on with her chores; and then, when the sun reached its "
                "peak, she needed to read the runner's final answer."
            ),
            mapping=(
                "`agent` is the runner; `send` dispatches the runner with the `inc` "
                "message; `await` waits at the gate for the runner to return; `@` "
                "reads the answer the runner brought back."
            ),
            resolution=(
                "The REPL read the agent's final tally — the runner had arrived, applied `inc`, and the count was waiting when the milkmaid came to collect it (with `0` as the input value)."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)",
            expected=15,
            concept_phrase="the agent updated with send and read after await",
            question_what="the value returned by dereferencing ag after defining an agent holding 5, sending + 10 asynchronously, awaiting, and dereferencing",
            goal_text="construct an agent holding 5, asynchronously send + with 10 to it, await its completion, and dereference",
            scenario=(
                "The milkmaid sent a swift runner ahead along the market road, "
                "carrying a message: add ten more pails to the count of five already "
                "tallied. She kept milking while the runner traveled to the buyer's stall."
            ),
            need=(
                "She needed the runner to carry the addition to the agent ahead; she "
                "needed to wait at the gate for the runner to finish; and then she "
                "needed to read the runner's final tally."
            ),
            mapping=(
                "`agent` is the swift runner; `send` dispatches the runner with "
                "`+ 10`; `await` waits at the gate for the runner to return; `@` "
                "reads the total the runner brought back."
            ),
            resolution=(
                "The REPL read the agent's final count — the runner arrived, applied "
                "the addition, and the combined tally was waiting at the gate."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(do (def ag (agent 0)) (send ag inc) (await ag) @ag)",
            expected=1,
            concept_phrase="the agent updated with send and read after await",
            question_what="the value returned by dereferencing ag after defining an agent holding 0, using send to dispatch inc, awaiting, and dereferencing",
            goal_text="construct an agent holding 0, use send to asynchronously apply inc, await its completion, and dereference",
            scenario=(
                "The milkmaid stationed a runner at the dairy door with a count of "
                "zero and a quick task — add one — then dispatched the runner along "
                "the shared market road while she continued her chores."
            ),
            need=(
                "She needed the runner to carry the short task via the shared pool "
                "and wait at the gate to read the tally on return."
            ),
            mapping=(
                "`send` dispatches the agent-runner via the shared thread pool for "
                "quick tasks; `await` waits at the gate; `@` reads the result."
            ),
            resolution=(
                "The REPL read the agent's count — the runner completed the task and reported back the updated tally (with `0` as the input value)."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)",
            expected=1,
            concept_phrase="the agent with send-off awaited and read",
            question_what="the value returned by dereferencing ag after defining an agent holding 0, using send-off to dispatch inc, awaiting, and dereferencing",
            goal_text="construct an agent holding 0, use send-off to asynchronously apply inc, await its completion, and dereference",
            scenario=(
                "The milkmaid had a runner with a longer delivery task. She "
                "dispatched it along a separate road — the blocking pool — to "
                "keep the shared market road free for quick errands."
            ),
            need=(
                "She needed the runner to travel its own road without blocking "
                "short-task runners; she would wait at the gate afterward."
            ),
            mapping=(
                "`send-off` dispatches via a separate blocking pool for longer "
                "tasks, unlike `send`. `await` waits at the gate; `@` reads "
                "the result."
            ),
            resolution=(
                "The REPL read the agent's count — the runner finished along its own road and reported back the same incremented tally (with `0` as the input value)."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)",
            expected=2,
            concept_phrase="the agent receiving two sends awaited and read",
            question_what="the value returned by dereferencing ag after defining an agent holding 0, sending inc twice asynchronously, awaiting, and dereferencing",
            goal_text="construct an agent holding 0, asynchronously send inc twice, synchronize with await, and dereference",
            scenario=(
                "The milkmaid dispatched the same runner ahead twice along the "
                "market road — first with one message, then a second before the "
                "runner returned. Both messages queued up for the runner to deliver "
                "in order while she finished her morning chores."
            ),
            need=(
                "She needed to wait at the dairy gate until the runner had "
                "delivered both messages in sequence, so the tally reflected "
                "both increments before she read it."
            ),
            mapping=(
                "Each `send` queues a message for the agent-runner; the runner "
                "delivers them in order. `await` holds the milkmaid at the gate "
                "until both deliveries are done. `@` reads the final tally."
            ),
            resolution=(
                "The REPL read the agent's tally — both increments had been applied in sequence, and the count reflected both deliveries (with `0` as the input value)."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="@(future (+ 1 2))",
            expected=3,
            concept_phrase="the future computing addition then awaited",
            question_what="the value the messenger returns from adding 1 and 2",
            goal_text="dispatch a runner to compute the sum of 1 and 2; later, ask the runner for the answer",
            scenario=(
                "The milkmaid sent a runner ahead to the buyer's stall with a simple "
                "arithmetic task: add one pail to two. She kept working at the dairy "
                "door while the runner carried the computation down the market road."
            ),
            need=(
                "She needed the runner to complete the addition asynchronously and "
                "hold the result until she was ready to collect it — blocking at "
                "the gate only when she asked for the answer."
            ),
            mapping=(
                "`future` is the swift runner dispatched ahead with the computation; "
                "the runner travels while the milkmaid works. `@` waits at the gate "
                "for the runner to return and reads the answer brought back."
            ),
            resolution=(
                'The REPL read the future and returned the sum — the runner had completed the addition along the market road and reported back (with `1` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="@(future (* 6 7))",
            expected=42,
            concept_phrase="the future computing multiplication then awaited",
            question_what="the value returned by dereferencing a future that multiplies 6 and 7",
            goal_text="construct a future that multiplies 6 and 7, and dereference it",
            scenario=(
                "The milkmaid dispatched a second runner along the market road with "
                "a multiplication task: find the product of six pails by seven. "
                "The runner set off while she loaded the next delivery."
            ),
            need=(
                "She needed the runner to carry the heavier multiplication ahead "
                "and hold the result until she walked to the buyer's stall to "
                "collect it."
            ),
            mapping=(
                "`future` dispatches the runner with the multiplication task; the "
                "runner computes while the milkmaid is busy. `@` meets the runner "
                "at the stall and reads the product brought back."
            ),
            resolution=(
                "The REPL read the future and returned the product — the runner "
                "had completed the multiplication and the answer was waiting — 7."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(do (def a (atom 7)) @a)",
            expected=7,
            concept_phrase="constructing an atom and extracting its value using the @ shorthand",
            question_what="the value extracted from an atom using @",
            goal_text="construct an atom holding 7 and dereference it using @",
            scenario=(
                "The milkmaid chalked seven pails on the tally-slate by the dairy "
                "door. The farmer walked up and asked her to read the current mark "
                "off the slate — using the short chalk-reading sign, @."
            ),
            need=(
                "She needed a quick way to read the slate's current mark without "
                "a long form — just glance at the slate and report what it says now."
            ),
            mapping=(
                "`atom` is the tally-slate holding the count; `@` is the chalk-reading "
                "shorthand — a single glance at the slate that returns whatever mark "
                "is currently chalked there."
            ),
            resolution=(
                "The REPL read the slate and returned the current mark — the @ "
                "shorthand glanced at the slate and brought back what was chalked — 7."
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
                "The same tally-slate hung by the dairy door with seven chalked on "
                "it. The farmer asked for the long-form reading — using the full "
                "`deref` function call rather than the @ shorthand."
            ),
            need=(
                "She needed to demonstrate that the full `deref` call reads the "
                "slate just as the @ shorthand does — same glance, same mark, "
                "only written out in longer form."
            ),
            mapping=(
                "`deref` is the full chalk-reading call: it reads the tally-slate "
                "and returns the current mark. It is the unabbreviated form of `@` — "
                "both look at the same slate and return the same value."
            ),
            resolution=(
                "The REPL read the slate and returned the current mark — the full "
                "`deref` call reached the same answer as the @ shorthand — 7."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(do (def p (promise)) (deliver p :done) @p)",
            expected=":done",
            concept_phrase="the promise delivered and awaited",
            question_what="the value returned by dereferencing a promise after defining it, delivering a keyword to it, and dereferencing",
            goal_text="construct a promise, deliver a completion keyword to it, and dereference to get the delivered value",
            scenario=(
                "The milkmaid sent a runner ahead to the buyer's stall but gave no "
                "message yet — she would deliver the message later when she was "
                "ready. The runner waited at the stall for the word to arrive."
            ),
            need=(
                "She needed a placeholder that the runner could hold — an empty "
                "promise — until she was ready to deliver the completion signal "
                "and the runner could return with it."
            ),
            mapping=(
                "`promise` is the empty placeholder the runner holds at the stall; "
                "`deliver` sends the completion word to the waiting runner; `@` "
                "reads what the runner received after the word was delivered."
            ),
            resolution=(
                "The REPL read the promise and returned the delivered word — the "
                "runner had received the signal and brought it back to the gate — :done."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def p (promise)) (deliver p 42) @p)",
            expected=42,
            concept_phrase="the promise delivered and awaited",
            question_what="the value returned by dereferencing a promise after defining it, delivering a number to it, and dereferencing",
            goal_text="construct a promise, deliver 42 to it, and dereference to get the delivered value",
            scenario=(
                "The milkmaid gave a runner an empty promise-slip at the dairy "
                "door and sent the runner to wait at the buyer's stall. When the "
                "final pail count was known, she filled in the number and delivered "
                "it to the waiting runner."
            ),
            need=(
                "She needed the runner to block at the stall until the number "
                "arrived, then carry the filled-in count back to the dairy door "
                "so she could read the final total."
            ),
            mapping=(
                "`promise` is the empty slip the runner holds; `deliver` fills in "
                "the number and sends it to the runner. `@` waits at the gate for "
                "the runner to return and reads the number on the slip."
            ),
            resolution=(
                "The REPL read the promise and returned the delivered number — the "
                "runner received the filled slip and brought the count back — 42."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(do (def v (volatile! 0)) (vswap! v inc) @v)",
            expected=1,
            concept_phrase="the volatile updated with vswap and read",
            question_what="the value returned by dereferencing v after defining a volatile holding 0, performing a non-transactional swap via inc, and dereferencing",
            goal_text="construct a volatile holding 0, perform a non-transactional swap by applying inc, and dereference",
            scenario=(
                "The milkmaid needed a lightweight tally-slate for a single-threaded "
                "loop inside the dairy — no other farmer would touch it, so there was "
                "no need for the atom's heavier coordination overhead."
            ),
            need=(
                "She needed a slate that updated fast inside a tight loop, without "
                "the cost of full atomic coordination — a slate for her eyes only, "
                "not shared across the farmyard."
            ),
            mapping=(
                "`volatile!` is the lightweight solo tally-slate; `vswap!` chalks "
                "the increment directly with no concurrency overhead. `@` reads "
                "what the slate holds after the fast update."
            ),
            resolution=(
                'The REPL read the volatile slate and returned the updated count — the fast chalk-update completed without heavier coordination (with `0` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def v (volatile! 5)) (vreset! v 99) @v)",
            expected=99,
            concept_phrase="the volatile reset and read",
            question_what="the value returned by dereferencing v after defining a volatile holding 5, performing a non-transactional reset to 99, and dereferencing",
            goal_text="construct a volatile holding 5, perform a non-transactional reset to 99, and dereference",
            scenario=(
                "The milkmaid's lightweight tally-slate showed five from a test run. "
                "She needed to overwrite it entirely with a new starting value — "
                "not incrementally, but in a single fast stroke, with no other "
                "farmer watching."
            ),
            need=(
                "She needed a fast overwrite on the solo slate — not a read-then-"
                "update, but a plain replace — to reset it quickly inside a "
                "single-threaded context."
            ),
            mapping=(
                "`vreset!` writes the new value directly onto the volatile slate "
                "in one stroke, ignoring whatever was there before. `@` reads "
                "the new mark after the fast overwrite."
            ),
            resolution=(
                "The REPL read the volatile slate and returned the new value — the "
                "old mark was gone, replaced in a single fast stroke — 99."
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
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))",
            expected=99,
            concept_phrase="the dynamic var rebound and read",
            question_what="the value of the dynamic var when read inside the binding form after defining it and rebinding",
            goal_text="define a dynamic var *p* as 1, use binding to rebind it to 99, and read its value inside",
            scenario=(
                "The milkmaid's tally-slate showed the day's default count. For one "
                "special delivery run, she covered the slate with a private mark "
                "visible only inside that run."
            ),
            need=(
                "She needed the per-run cover to shadow the default without touching "
                "the permanent slate — farmers during the run saw the local mark."
            ),
            mapping=(
                "`binding` covers the tally-slate for the run's duration; the local "
                "mark shadows the default. Reading `*p*` inside returns the "
                "run's private value."
            ),
            resolution=(
                "The REPL read the dynamic var inside the binding and returned the "
                "temporary mark — the cover was in place — :dynamic."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)",
            expected=1,
            concept_phrase="the dynamic var rebound and read after",
            question_what="the value of the dynamic var when read after the binding form unwound",
            goal_text="define a dynamic var *p* as 1, use binding to rebind it to 99 inside, and read its value after binding exits",
            scenario=(
                "The milkmaid placed the temporary cover over the tally-slate for "
                "the special delivery run, then removed it when the run ended. "
                "Another farmer glanced at the slate afterward."
            ),
            need=(
                "She needed to confirm the permanent slate still showed the original "
                "default once the cover was lifted — not the run's private mark."
            ),
            mapping=(
                "`binding` lifts the cover when its body exits; the slate is "
                "restored exactly as it was. Reading `*p*` after exit returns the "
                "original default."
            ),
            resolution=(
                "The REPL read the dynamic var after the binding unwound and "
                "returned the default — the permanent slate was unchanged — :dynamic."
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
    fable="milkmaid",
    examples=[
        # `locking` takes a monitor and a body; we use a simple body.
        SubjectExample(
            form="(do (def lock (Object.)) (locking lock (+ 1 2)))",
            expected=3,
            concept_phrase="the lock guarding arithmetic",
            question_what="the value returned by evaluating an addition inside a locked critical section after creating a monitor and acquiring the lock",
            goal_text="create an object to use as a monitor, acquire the lock, and evaluate an addition inside",
            scenario=(
                "The milkmaid needed to tally pails at the dairy door using a raw "
                "Java-style padlock — the heaviest tool available — to guard a "
                "critical section where no other thread could enter while she worked."
            ),
            need=(
                "She needed the padlock to ensure that only one farmer at a time "
                "could perform the addition inside the critical section — a last-resort "
                "guard when lighter tools were not enough."
            ),
            mapping=(
                "`locking` is the padlock on the dairy door: it acquires the monitor, "
                "runs the addition inside the locked section, then releases. No other "
                "thread can enter while the padlock is held."
            ),
            resolution=(
                'The REPL returned the result of the addition — the critical section ran safely under the padlock, and the lock was released afterward (with `1` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def lock (Object.)) (locking lock 42))",
            expected=42,
            concept_phrase="the lock guarding a literal",
            question_what="the literal value returned by evaluating it inside a locked critical section after creating a monitor and acquiring the lock",
            goal_text="create an object to use as a monitor, acquire the lock, and evaluate a literal inside",
            scenario=(
                "The farmer showed the milkmaid the simplest possible padlocked "
                "section: just a plain value inside the lock. The padlock was real — "
                "it acquired the monitor — but the body needed no computation."
            ),
            need=(
                "She needed to see that `locking` could guard any expression — even "
                "a bare literal — and that the returned value came from the body, not "
                "from the lock itself."
            ),
            mapping=(
                "`locking` acquires the monitor and evaluates whatever is inside "
                "the critical section. The lock returns the body's value when it "
                "releases — the padlock is the guard, not the answer."
            ),
            resolution=(
                "The REPL returned the literal from inside the locked section — the "
                "padlock held, the body was evaluated, and the value came back — 42."
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
