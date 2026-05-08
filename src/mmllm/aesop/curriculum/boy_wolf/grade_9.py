"""Grade 9 — state and concurrency primitives. Through boy-who-cried-wolf.

Subplot lens: the elder's careful transactional ledger updates versus
the shepherd's racing-uncoordinated mutations. The village trust
ledger is the canonical state — a CAS-protected counter of honest
calls. The elder insists on dosync and the proper update primitive;
the shepherd wants to scribble the new value and move on. The REPL
settles every dispute.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.boy_wolf.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.boy_wolf._metaphor_pools import (
    _BASKET_SUBPLOTS, _NOTEBOOK_SUBPLOTS, _RUNNERAHEAD_SUBPLOTS,
)
from mmllm.aesop.curriculum.boy_wolf._goals import GOALS, get_goal


# ─────────────────────── grade-9 subplot extensions ───────────────────────
#
# State + concurrency = "things that change over time." We extend the
# shared pool with two beats: the careful-ledger (elder's transactional
# update of the village trust counter) and the racing-mutation (the
# shepherd wants to scribble the new value, the elder insists on the
# right primitive).

_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    # 9. The careful-ledger template — elder updates the watchhouse trust
    #    counter the right way; shepherd watches impatiently.
    SubplotTemplate("""\
{elder_phrase} kept a small ledger of state {place} — a value that
might change as the day went on, recording how many forms had been
honestly evaluated. {elder_he_she_cap} explained that the form
{form_display} captured {concept_phrase}: a careful, ordered update.
{shepherd_phrase}, {emo_proud}, asked the REPL to confirm the final
value."""),

    # 10. The racing-mutation template — shepherd wants to update without
    #     coordinating; elder insists on the right primitive.
    SubplotTemplate("""\
"Why bother with all this?" {shepherd_phrase} demanded {place}.
"{shepherd_he_she_cap} could just write the new value!" {elder_phrase},
{emo_patient}, sketched out {concept_phrase} instead and showed the
form {form_display}: the proper way for the runtime to manage change.
They agreed to submit it to the REPL."""),
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
    fable="boy-wolf",
    examples=[
        # `assoc` returns a new map; the original is unchanged.
        _ex("(let [m {:a 1}] (assoc m :b 2) m)",
            {":a": 1},
            "binding m, calling (assoc m :b 2), then returning m unchanged",
            "the original map after a non-mutating assoc",
            scenario=(
                "Tom tucked a fresh wool-basket on the shelf — three pouches marked "
                "for white fleece, dyed fleece, and thorn-combed scraps. He said to "
                "Carol, 'I'll add a fourth pouch here for the lambing-wool.' Carol "
                "smiled and watched the shelf."
            ),
            need=(
                "Tom wanted to mark a new kind in the basket, but the original "
                "three categories had to stay as they were — the morning's tally "
                "lived on that shelf and couldn't change retroactively."
            ),
            mapping=(
                "A map is like a named basket with labeled pouches. `assoc` hands "
                "back a fresh basket with the new pouch added, leaving the original "
                "untouched. `m` still holds the three original pouches after `assoc` "
                "runs."
            ),
            resolution=(
                "the original basket still held only its three pouches — the map m unchanged, ready for the next shepherd's count. The slate showed {drawn.a} in clear chalk, and the fold tally stood as the day record."           )),
        _ex("(let [v [1 2 3]] (conj v 4) v)",
            [1, 2, 3],
            "binding v, calling (conj v 4), then returning v unchanged",
            "the original vector after conj",
            scenario=(
                "Carol's record on the watchhouse step had to stay fixed."
            ),
            need=(
                "The morning's record couldn't shift after it was written."
            ),
            mapping=(
                "`conj` builds a new vector but doesn't rewrite the original."
            ),
            resolution=(
                'The original vector stood unchanged as the immutable record. Carol marked {drawn.a} on the watchhouse beam, the lookout high above the valley quiet at last.'
            )),
    ],
    subplots=_BASKET_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-02 — Why state at all
G9_02 = SubjectCurriculum(
    grade=9, subject_id="G9-02",
    subject_title="Why state at all",
    fable="boy-wolf",
    examples=[
        # The minimal "place that needs identity over time" example.
        _ex("(do (def counter (atom 0)) (swap! counter inc) @counter)",
            1,
            "an atom counter, incremented once, then read",
            "the value of counter after one swap! inc",
            scenario=(
                "The watchhouse slate sat on its stand inside the "
                "watchhouse, open for any shepherd to read. Carol had "
                "chalked a single tally at the top — 0 honest evaluations "
                "for the morning so far — and stepped back to begin the "
                "day's count."
            ),
            need=(
                "Each time a form was honestly evaluated, the slate's "
                "tally needed to step up by one — and only one shepherd "
                "could be writing at a time, so the watchhouse's running "
                "count would never be lost or doubled."
            ),
                mapping=(
                "An atom is exactly the watchhouse slate: a single shared "
                "tally that any shepherd can read or update, with the "
                "REPL guaranteeing the read-modify-write step is "
                "atomic. `swap!` is `read the page, apply the change, "
                "write it back`, all as one motion."
            ),
            resolution=(
                "the slate now read 1 — the morning's first honest evaluation safely tallied, ready for the next."
            )),
        _ex("(do (def progress (atom :idle)) (reset! progress :running) @progress)",
            ":running",
            "a progress atom reset to :running",
            "the value of progress after reset!",
            scenario=(
                "The watchhouse slate showed :idle at dawn. By noon, when Carol "
                "checked it, the morning watch had finished its forms. She took the "
                "chalk and erased the old mark, writing :running to show the next "
                "phase had begun."
            ),
            need=(
                "The slate's state needed to shift from one phase to another as the "
                "day progressed — one fresh tally at a time, the old erased before "
                "the new was written."
            ),
            mapping=(
                "`reset!` is the chalk erasing and rewriting in one motion. It "
                "replaces the atom's value with a new one, overwriting what came "
                "before. The atom progress now holds :running."
            ),
            resolution=(
                'the slate now read :running — the phase marker updated, the watch advancing.'
            )),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-03 — Atom introduction
G9_03 = SubjectCurriculum(
    grade=9, subject_id="G9-03",
    subject_title="Atom introduction",
    fable="boy-wolf",
    examples=[
        _ex("(do (def a (atom 0)) (swap! a inc) @a)",
            1,
            "an atom starting at 0, incremented once via swap!",
            "the value of the atom after one swap! inc",
            scenario=(
                "Tom sat at the watchhouse slate, chalk in hand. A fresh tally — 0 — "
                "marked the morning's count. Carol stepped in: 'One form evaluated.' "
                "Tom nodded and reached for the chalk to bump the count."
            ),
            need=(
                "The tally had to advance one mark at a time, each shepherd's claim "
                "checked before the count moved. Tom couldn't scribble blindly; the "
                "elder oversaw every increment."
            ),
            mapping=(
                "`swap!` reads the current tally, applies the change atomically, and "
                "writes it back all in one motion. `inc` adds one — the shepherd and "
                "the slate working as one."
            ),
            resolution=(
                'the tally rose to the new count — one honest evaluation recorded, the slate ready for the next.'
            )),
        _ex("(do (def a (atom 10)) (swap! a + 5) @a)",
            15,
            "an atom starting at 10, with (swap! a + 5)",
            "the value of the atom after swap! + 5",
            scenario=(
                "The wool-trade ledger on the slate read 10 coins from yesterday's "
                "sales. A new batch of fleece had been sold. Carol chalked the rule: "
                "'Add 5 coins to the ledger.' Tom watched as the slate's number "
                "shifted."
            ),
            need=(
                "The coin count had to jump by a known amount without losing the "
                "base number. The slate was the only record; it couldn't be erased "
                "mid-transaction."
            ),
            mapping=(
                "`swap!` with `+ 5` reads the current tally, adds 5 to it, and "
                "writes the new total back atomically. The atom a moves from 10 to "
                "the new sum in one atomic step."
            ),
            resolution=(
                'the ledger now showed 15 coins — the addition recorded, the trade complete.'
            )),
        _ex("(do (def a (atom :start)) (reset! a :done) @a)",
            ":done",
            "an atom reset! from :start to :done",
            "the value of the atom after reset!",
            scenario=(
                "The slate at the fold showed :start as Tom began sorting sheep into "
                "pens. Hours passed. Carol arrived and took the chalk, marking the "
                "slate :done — the day's work complete."
            ),
            need=(
                "The slate's state needed to flip entirely from one phase to "
                "another, wiping the old status and writing the new without "
                "intermediate confusion."
            ),
            mapping=(
                "`reset!` throws out the old value and writes a new one. No "
                "transaction needed; the atom a simply becomes :done, overwriting "
                ":start."
            ),
            resolution=(
                "the slate read :done — the day's phase marker final, the work sealed."
            )),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-04 — Atom CAS semantics
G9_04 = SubjectCurriculum(
    grade=9, subject_id="G9-04",
    subject_title="Atom CAS semantics",
    fable="boy-wolf",
    examples=[
        # `compare-and-set!` succeeds when current matches expected.
        _ex("(do (def a (atom 0)) (compare-and-set! a 0 1) @a)",
            1,
            "compare-and-set! on an atom: expected 0, set to 1",
            "the value of the atom after a successful CAS",
            scenario=(
                "Tom checked the slate's value before writing a new one."
            ),
            need=(
                "The value had to match his expectation before the write could succeed."
            ),
            mapping=(
                "`compare-and-set!` atomically updates only if the expected value matches."
            ),
            resolution=(
                'The check succeeded and the atom was updated atomically (with `0` as the input value).'
            )),
        _ex("(do (def a (atom 5)) (compare-and-set! a 0 99) @a)",
            5,
            "compare-and-set! when the expected value doesn't match",
            "the value of the atom after a CAS that does not fire",
            scenario=(
                "The slate showed 5 coins. Tom said, 'If it's 0, I'll write 99.' He "
                "reached for the chalk, but Carol stopped him: 'Look again — it's "
                "not 0. Your bet fails.'"
            ),
            need=(
                "Tom's assumption was wrong. The slate had already changed. The "
                "compare-and-set guard prevented Tom from overwriting a value he "
                "hadn't actually read."
            ),
            mapping=(
                "`compare-and-set!` returns false and leaves the atom untouched when "
                "the current value doesn't match the expected one. The atom a stays "
                "at 5 because the precondition failed."
            ),
            resolution=(
                "the slate remained at 5 — Tom's blind write was blocked, the elder's safety rule preserved."
            )),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-05 — Watch on atom
G9_05 = SubjectCurriculum(
    grade=9, subject_id="G9-05",
    subject_title="Watch on atom",
    fable="boy-wolf",
    examples=[
        # A watch can record into another atom each time the watched atom
        # changes; we read the recording atom at the end.
        _ex("(do (def a (atom 0))"
            " (def log (atom []))"
            " (add-watch a :w (fn [_ _ _ n] (swap! log conj n)))"
            " (swap! a inc)"
            " @log)",
            [1],
            "an atom with a watch that appends each new value to a log",
            "the contents of the log after one swap",
            scenario=(
                "Carol set up two slates in the watchhouse — one to track the "
                "morning's tally, and a second to log each change as it happened. "
                "'Whenever the first slate updates,' she told the watch-keeper, "
                "'write the new number here.' Tom watched as the count climbed."
            ),
            need=(
                "The village needed a second record of every state transition — not "
                "just the current value, but the history of how it had moved. The "
                "log slate grew as the tally changed."
            ),
            mapping=(
                "A watch is a function hooked to an atom. `add-watch` registers it. "
                "Each time the atom changes via `swap!`, the watch function fires and "
                "can record the new value — here appending it to the log vector."
            ),
            resolution=(
                'the log showed [1] — the history slate recorded the single honest step, a complete audit trail (with `:w` as the input value).'
            )),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-06 — Validator on atom
G9_06 = SubjectCurriculum(
    grade=9, subject_id="G9-06",
    subject_title="Validator on atom",
    fable="boy-wolf",
    examples=[
        # A validator gates updates; we set one then read the value.
        _ex("(do (def a (atom 0))"
            " (set-validator! a number?)"
            " (swap! a inc)"
            " @a)",
            1,
            "an atom with a number? validator, incremented once",
            "the value of the atom after a valid update",
            scenario=(
                "Carol chalked a rule on the watchhouse wall: 'Only numbers on the "
                "tally slate.' She installed a watchman to check every mark Tom tried "
                "to make. Tom reached for the chalk to bump the count — the watchman "
                "nodded and let the mark stand."
            ),
            need=(
                "The slate needed a guardian to prevent accidents — if Tom ever "
                "scribbled a word or symbol instead of a numeral, the townsfolk's count "
                "would corrupt. The validator caught and rejected bad writes."
            ),
            mapping=(
                "A validator is a function that checks the new value before it lands "
                "on the atom. `set-validator! a number?` ensures only numbers are "
                "allowed. `inc` returns a number, so the update succeeds."
            ),
            resolution=(
                "the tally rose safely to 1 — the watchman's check passed, the count trusted again (with `0` as the input value)."
            )),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-07 — Ref introduction
G9_07 = SubjectCurriculum(
    grade=9, subject_id="G9-07",
    subject_title="Ref introduction",
    fable="boy-wolf",
    examples=[
        # Refs require dosync to update.
        _ex("(do (def r (ref 0)) (dosync (alter r inc)) @r)",
            1,
            "a ref incremented inside a dosync transaction",
            "the value of the ref after dosync alter inc",
            scenario=(
                "Carol led Tom into the watchhouse vault, where the ledger lay under "
                "lock. 'This record is precious,' she said. 'You cannot touch it alone. "
                "We enter together, I read the page, you mark the change, I verify it, "
                "then we exit.' Tom nodded and they entered the dosync together."
            ),
            need=(
                "Multiple shepherds might try to update the ledger at the same time. "
                "The vault ensured that no two updates could collide or corrupt the "
                "count. Coordination was the cost of safety."
            ),
            mapping=(
                "A ref is a ledger held in a vault. `dosync` opens the vault and "
                "locks it. `alter` applies a change inside the transaction. When "
                "dosync exits, the vault closes and all changes are final."
            ),
            resolution=(
                "the ledger's page was locked and marked — the synchronized update complete, the count safe from collision (with `0` as the input value)."
            )),
        _ex("(do (def r (ref 100)) (dosync (ref-set r 7)) @r)",
            7,
            "a ref ref-set to 7 inside dosync",
            "the value of the ref after ref-set 7",
            scenario=(
                "The vault was open. Carol said, 'Forget the old page — write a fresh "
                "number here.' Tom took the chalk and wrote 7 directly, no formula, no "
                "reading the old value — just a clean replacement. Carol locked the "
                "vault."
            ),
            need=(
                "Sometimes the ledger needed to be completely rewritten, not adjusted. "
                "`ref-set` was the tool for wholesale replacement inside the safety of "
                "dosync."
            ),
            mapping=(
                "`ref-set` inside dosync directly overwrites the ref's value without "
                "reading the old one. The new value lands as soon as dosync commits. "
                "The ref r now holds 7."
            ),
            resolution=(
                'the ledger was rewritten — the old hundred erased, the new seven locked in.'
            )),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-08 — dosync / alter
G9_08 = SubjectCurriculum(
    grade=9, subject_id="G9-08",
    subject_title="dosync and alter",
    fable="boy-wolf",
    examples=[
        # Two refs altered atomically inside one dosync.
        _ex("(do (def a (ref 1)) (def b (ref 2))"
            " (dosync (alter a inc) (alter b inc))"
            " [@a @b])",
            [2, 3],
            "two refs each incremented inside a single dosync",
            "the pair [a b] after the coordinated transaction",
            scenario=(
                "Carol kept two ledgers that had to stay balanced when changed."
            ),
            need=(
                "Both updates had to succeed together or fail together."
            ),
            mapping=(
                "Multiple refs altered inside dosync are coordinated atomically."
            ),
            resolution=(
                'Both counts changed together in one atomic transaction (with `1` as the input value).'
            )),
        _ex("(do (def r (ref 10)) (dosync (alter r + 5)) @r)",
            15,
            "a ref altered by + 5 inside dosync",
            "the value of the ref after alter + 5",
            scenario=(
                "The vault was open. The ledger read 10 coins. Carol said, 'Five more "
                "coins came in from the fleece trade. Alter the ledger.' Tom saw the "
                "old number, applied the rule, and wrote 15. Carol locked the vault."
            ),
            need=(
                "The alteration had to read the old value, apply a transformation, "
                "and write the new one — all atomically, with no other shepherd's "
                "write sneaking in between."
            ),
            mapping=(
                "`alter` inside dosync reads the ref, applies the function (+ 5), and "
                "writes the result. All three steps are atomic. The ref r moves from "
                "10 to 15 in one transaction."
            ),
            resolution=(
                'the ledger now showed 15 — the five new coins tallied, the vault closed.'
            )),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-09 — Ref vs atom
G9_09 = SubjectCurriculum(
    grade=9, subject_id="G9-09",
    subject_title="Ref vs atom",
    fable="boy-wolf",
    examples=[
        # The same operation expressed both ways.
        _ex("(do (def a (atom 0)) (swap! a inc) @a)",
            1,
            "an atom updated via swap!",
            "the value of the atom after one swap! inc",
            scenario=(
                "Tom came to the watchhouse slate holding a tally of one honest form. "
                "The slate showed 0. Carol handed him chalk and said, 'Just write the "
                "new tally — we'll keep it simple.' Tom marked 1 and stepped back."
            ),
            need=(
                "The tally needed to update without the overhead of the vault. Atoms "
                "are simpler — one shepherd at a time, no coordination dance."
            ),
            mapping=(
                "An atom with `swap!` is the watchhouse slate: any shepherd can "
                "update it, the read-modify-write is atomic, no locks needed. The "
                "atom a is now 1."
            ),
            resolution=(
                'the slate rose to 1 — the simpler path taken, the count recorded.'           )),
        _ex("(do (def r (ref 0)) (dosync (alter r inc)) @r)",
            1,
            "a ref updated via alter inside dosync",
            "the value of the ref after one dosync alter inc",
            scenario=(
                "Tom came to the vault ledger holding a tally of one honest form. The "
                "ledger showed 0. Carol led him into the vault, they read the page "
                "together, applied the change, and Carol locked the door behind them."
            ),
            need=(
                "The vault ledger demanded coordination — multiple shepherds might "
                "access it, so the dosync dance ensured no updates collided."
            ),
            mapping=(
                "A ref with dosync and alter is the vault ledger: the vault door "
                "locks, the update happens inside, the door unlocks only when the "
                "transaction commits. The ref r is now 1."
            ),
            resolution=(
                'the ledger rose to 1 — the careful path taken, the count safe from collision.'
            )),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-10 — Agent introduction
G9_10 = SubjectCurriculum(
    grade=9, subject_id="G9-10",
    subject_title="Agent introduction",
    fable="boy-wolf",
    examples=[
        # send is async — we await before reading.
        _ex("(do (def ag (agent 0)) (send ag inc) (await ag) @ag)",
            1,
            "an agent sent inc and awaited",
            "the value of the agent after send inc and await",
            scenario=(
                "Carol called the smallest of the village children to "
                "the watchhouse step. She handed the child a folded "
                "message with a single instruction: take it to the "
                "elder at the far cottage, wait for the reply, and "
                "bring back what the elder said."
            ),
            need=(
                "The instruction couldn't be answered immediately — the "
                "child had to run, deliver, and return. The village "
                "needed to keep its work going meanwhile, then collect "
                "the runner's answer when it was ready."
            ),
                mapping=(
                "An agent is the dispatched runner. `send` hands off "
                "the message and lets the runner go; `await` waits "
                "until the runner is back at the watchhouse step; "
                "`@` reads the answer the runner brought."
            ),
            resolution=(
                "the runner returned with the elder's reply tallied into the message — 1 step further than the start, honestly delivered (with `0` as the input value)."
            )),
        _ex("(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)",
            15,
            "an agent sent (+ 10) and awaited",
            "the value of the agent after send + 10 and await",
            scenario=(
                "Carol called another runner, this one with a purse of coins. She "
                "handed the message: 'Ask the elder to add some coins to that purse.' "
                "The runner raced off, returned with the answer, and Carol counted "
                "the coins."
            ),
            need=(
                "The message needed a transformation — not just a delivery, but a "
                "formula to apply to the value. The runner would execute it and bring "
                "back the result."
            ),
            mapping=(
                "`send` with a function like `+ 10` dispatches the transformation to "
                "the agent's queue. `await` waits for all pending tasks to complete. "
                "`@` reads the final result: the agent now holds the new total."
            ),
            resolution=(
                'the runner returned with the answer — the addition computed, the message fulfilled and the purse heavier.'
            )),
    ],
    subplots=_RUNNERAHEAD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-11 — send / send-off
G9_11 = SubjectCurriculum(
    grade=9, subject_id="G9-11",
    subject_title="send and send-off",
    fable="boy-wolf",
    examples=[
        _ex("(do (def ag (agent 0)) (send ag inc) (await ag) @ag)",
            1,
            "send used on an agent, then awaited",
            "the agent's value after send inc",
            scenario=(
                "Carol sent a swift runner with a simple task — add one to the tally "
                "in the pouch. The runner moved fast, did the work, and returned. "
                "Carol waited until the runner was back, then checked the pouch."
            ),
            need=(
                "The runner could handle quick, computational work. `send` was the "
                "dispatch for short jobs that didn't block or wait for I/O."
            ),
            mapping=(
                "`send` dispatches the function to an agent's thread pool — for "
                "fast, CPU-bound operations. `await` blocks until all pending sends "
                "are done. The agent now holds 1."
            ),
            resolution=(
                'the runner returned swift and sure — the quick task complete, the pouch tallied (with `0` as the input value).'
            )),
        _ex("(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)",
            1,
            "send-off used on an agent, then awaited",
            "the agent's value after send-off inc",
            scenario=(
                "Carol sent a runner with a task that might take time — the elder "
                "might be busy. The runner had to wait and return with the answer. "
                "Carol continued working, then awaited the runner's return."
            ),
            need=(
                "The runner might need to wait for a slow operation — I/O, network, "
                "the elder's reply. `send-off` was the dispatch for long-running tasks "
                "without blocking the meadow folk."
            ),
            mapping=(
                "`send-off` dispatches to a thread that can block — for slow operations "
                "like I/O or waiting. `await` still waits for completion. The agent "
                "holds 1 after the send-off completes."
            ),
            resolution=(
                'the runner returned with the answer — patient work done, the pouch tallied (with `0` as the input value).'
            )),
    ],
    subplots=_RUNNERAHEAD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-12 — await
G9_12 = SubjectCurriculum(
    grade=9, subject_id="G9-12",
    subject_title="await — synchronizing on agents",
    fable="boy-wolf",
    examples=[
        _ex("(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)",
            2,
            "two send inc calls then await before deref",
            "the agent's value after two sends and await",
            scenario=(
                "Carol gave the runner two tasks in sequence: 'First, add one. Then, "
                "add one again. Come back when both are done.' The runner took off, "
                "completed both jobs, and returned. Carol waited until the runner was "
                "safely back at the step before asking for the result."
            ),
            need=(
                "Multiple sends could queue up in the agent's mailbox. `await` ensured "
                "all pending tasks had finished before the townsfolk tried to read the "
                "result — no race with the runner."
            ),
            mapping=(
                "Two `send` calls queue two messages in the agent's mailbox. `await` "
                "blocks the current thread until the agent has processed all queued "
                "messages. The agent now holds 2."
            ),
            resolution=(
                'the runner had done both tasks — the two increments tallied, the answer ready and certain (with `0` as the input value).'
            )),
    ],
    subplots=_RUNNERAHEAD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-13 — future
G9_13 = SubjectCurriculum(
    grade=9, subject_id="G9-13",
    subject_title="future introduction",
    fable="boy-wolf",
    examples=[
        _ex("@(future (+ 1 2))",
            3,
            "a future computing (+ 1 2), dereferenced",
            "the value of the future for (+ 1 2)",
            scenario=(
                "Carol said to Tom, 'I'm sending a runner to add two numbers in the far "
                "cottage. I'll get started on other work, and when I'm ready, I'll "
                "ask for the runner's answer.' The runner went to work, and Carol "
                "continued her tasks until she asked for the result."
            ),
            need=(
                "The village needed to compute something without waiting for the "
                "answer immediately. The runner could work in parallel while others "
                "moved forward."
            ),
            mapping=(
                "`future` sends a computation to another thread and returns immediately. "
                "`@` blocks until the computation completes and returns the result. The "
                "future computed the sum while the rest of the valley worked."
            ),
            resolution=(
                'the runner had finished and returned the sum — the answer ready and waiting (with `1` as the input value).'           )),
        _ex("@(future (* 6 7))",
            42,
            "a future computing (* 6 7), dereferenced",
            "the value of the future for (* 6 7)",
            scenario=(
                "Carol sent a runner to the mill to grind flour — a long task. She "
                "gave the formula: multiply two quantities together. Then she went "
                "about her business. When she needed the answer, she asked the runner "
                "what had been produced."
            ),
            need=(
                "Long-running operations shouldn't block the main work. The computation "
                "could happen in the background while the village kept moving."
            ),
            mapping=(
                "`future` schedules the computation on a thread pool and returns "
                "immediately with a promise. `@` waits for that promise to resolve. The "
                "future computed the product."
            ),
            resolution=(
                'the runner had finished the calculation — the product ready, the formula answered (with `6` as the input value).'
            )),
    ],
    subplots=_RUNNERAHEAD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-14 — deref @
G9_14 = SubjectCurriculum(
    grade=9, subject_id="G9-14",
    subject_title="deref @ shorthand",
    fable="boy-wolf",
    examples=[
        _ex("(do (def a (atom 7)) @a)",
            7,
            "deref via @ on an atom holding 7",
            "the value of the atom via @",
            scenario=(
                "The watchhouse slate showed 7 tallies. Tom glanced at it and asked "
                "Carol, 'What does the slate show?' She pointed: '@' is the quick sign "
                "for reading. Tom saw 7 marks."
            ),
            need=(
                "The shepherd needed a shorthand to read the slate. @ is chalk-mark "
                "shorthand for deref — faster to write, same meaning."
            ),
            mapping=(
                "`@` is shorthand syntax for `deref`. Both read the atom's current "
                "value. The @ sign lets you write fewer words but means the same thing."
            ),
            resolution=(
                'the slate was read — 7 clearly marked, the short way fast and sure.'           )),
        _ex("(do (def a (atom 7)) (deref a))",
            7,
            "deref via the function form on an atom",
            "the value of the atom via the deref function",
            scenario=(
                "The watchhouse slate showed 7 tallies. Tom asked Carol, 'What does "
                "the slate show?' She took his hand and pointed to each step: deref "
                "means 'reach inside and take out the value.' Tom saw 7 marks."
            ),
            need=(
                "The full word `deref` explained the meaning clearly — reach inside "
                "the atom and extract its value. Some shepherds preferred the explicit "
                "name."
            ),
            mapping=(
                "`deref` is the function form for reading an atom. `(deref a)` and "
                "`@a` do the same thing. The deref function returns the current value: 7."
            ),
            resolution=(
                'the slate was read the long way — 7 clearly marked, the meaning transparent.'
            )),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-15 — promise
G9_15 = SubjectCurriculum(
    grade=9, subject_id="G9-15",
    subject_title="promise — deliver and deref",
    fable="boy-wolf",
    examples=[
        _ex("(do (def p (promise)) (deliver p :done) @p)",
            ":done",
            "a promise delivered with :done, then dereffed",
            "the value of the promise after deliver",
            scenario=(
                "Carol gave Tom an empty promise envelope and later filled it."
            ),
            need=(
                "Tom needed a way to wait for a value that would arrive later."
            ),
            mapping=(
                "A promise is an empty container. `deliver` fills it, `@` reads it."
            ),
            resolution=(
                'The promise was delivered and read successfully (with `done` as the input value) (with `:done` as the input value).'
            )),
        _ex("(do (def p (promise)) (deliver p 42) @p)",
            42,
            "a promise delivered with 42",
            "the value of the promise after deliver 42",
            scenario=(
                "Carol handed Tom an empty envelope. 'This will have the count of "
                "sheep,' she said. 'Just wait.' Tom kept working. By evening, Carol "
                "slipped the tally inside. Tom opened it and smiled — the count was complete."
            ),
            need=(
                "Some answers took time. The promise let them decouple the request "
                "from the delivery — Tom could ask now and wait later without blocking."
            ),
            mapping=(
                "A promise is a future value waiting to be filled. `deliver` writes "
                "the value in. `@` reads it. The promise now holds the delivered number."
            ),
            resolution=(
                'the envelope was filled with the answer — the sheep tallied, the promise delivered (with `42` as the input value).'
            )),
    ],
    subplots=_RUNNERAHEAD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-16 — volatile
G9_16 = SubjectCurriculum(
    grade=9, subject_id="G9-16",
    subject_title="volatile — when STM is too heavy",
    fable="boy-wolf",
    examples=[
        _ex("(do (def v (volatile! 0)) (vswap! v inc) @v)",
            1,
            "a volatile! incremented via vswap!",
            "the value of the volatile after one vswap! inc",
            scenario=(
                "Tom held a small temporary tally-stick in his palm — 0 notches. As "
                "he sorted sheep through the gate, he marked one notch. The stick was "
                "just for his pocket during this task, not a record the watchhouse would "
                "ever see."
            ),
            need=(
                "The shepherd needed a fast counter for one-off work — no need for the "
                "vault's overhead, no watches or validators. Just a quick mutable "
                "counter that didn't slow him down."
            ),
            mapping=(
                "A volatile is a mutable cell lighter than an atom — no atomicity, no "
                "watches. `vswap!` swaps the value in place. It's purely local work. "
                "The volatile now holds 1."
            ),
            resolution=(
                'the stick was notched once — quick local counting done, no village record needed.'
            )),
        _ex("(do (def v (volatile! 5)) (vreset! v 99) @v)",
            99,
            "a volatile! reset via vreset!",
            "the value of the volatile after vreset! 99",
            scenario=(
                "Tom held a small stick marked 5. Suddenly he realized the count was "
                "wrong for his local work. He scratched it clean and wrote 99 instead "
                "— a fresh start just for this stretch of work."
            ),
            need=(
                "The shepherd sometimes needed to restart a local counter without "
                "ceremony. `vreset!` was the fast way — no transaction, no guarantee, "
                "just replace the value."
            ),
            mapping=(
                "`vreset!` replaces a volatile's value directly. It's fast and simple "
                "— perfect for local, thread-local work that doesn't need "
                "coordination. The volatile now holds 99."
            ),
            resolution=(
                'the stick was rewritten — 99 fresh marks, local work restarted.'           )),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-17 — thread-local binding
G9_17 = SubjectCurriculum(
    grade=9, subject_id="G9-17",
    subject_title="binding — thread-local",
    fable="boy-wolf",
    examples=[
        _ex("(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))",
            99,
            "a dynamic var *p* rebound to 99 inside binding",
            "the value of *p* inside the binding form",
            scenario=(
                "Carol posted a notice on the meadow folk board: 'Today, all messages "
                "carry a priority level of 1.' Tom was about to send an urgent "
                "message, so he entered the urgent zone (binding) and the priority "
                "became 99. While inside the zone, he sent his message with the "
                "higher priority."
            ),
            need=(
                "A thread sometimes needed to temporarily rebind a shared value "
                "without affecting other threads. The binding would apply only within "
                "its scope."
            ),
            mapping=(
                "`binding` creates a thread-local override for a dynamic variable. "
                "Inside binding's block, *p* is 99. Outside, it reverts to 1. The "
                "variable reads 99 inside the binding."
            ),
            resolution=(
                'the urgent message was sent with priority 99 — the temporary rebinding honored within its scope.'
            )),
        _ex("(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)",
            1,
            "the value of *p* AFTER the binding form exits",
            "the original value of *p* once binding has unwound",
            scenario=(
                "The urgent message was sent with priority 99. Tom exited the urgent "
                "zone (binding unwound). He checked the townsfolk notice again and saw "
                "the original priority: 1. The temporary rebinding was gone."
            ),
            need=(
                "The binding had to be temporary — once the urgent task was done, the "
                "normal priority had to return. Thread-local state, not global."
            ),
            mapping=(
                "When binding exits, the dynamic variable reverts to its original "
                "value. `*p*` inside binding was 99; `*p*` after binding is 1 again. "
                "The override is scoped."
            ),
            resolution=(
                'the priority returned to 1 — the temporary rebinding unwound, the normal state restored.'
            )),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-18 — locking
G9_18 = SubjectCurriculum(
    grade=9, subject_id="G9-18",
    subject_title="locking — last resort",
    fable="boy-wolf",
    examples=[
        # `locking` takes a monitor and a body; we use a simple body.
        _ex("(do (def lock (Object.)) (locking lock (+ 1 2)))",
            3,
            "a locking form around (+ 1 2) using a fresh Object as monitor",
            "the result of the body inside locking",
            scenario=(
                "At the narrow gate of the fold stood a lock only one shepherd could hold."
            ),
            need=(
                "A mutex-style lock serializes access so only one thread runs at a time."
            ),
            mapping=(
                "`locking` acquires a monitor, runs the body, then releases it."
            ),
            resolution=(
                'The gate was passed safely and the body was executed without interruption (with `1` as the input value).'
            )),
        _ex("(do (def lock (Object.)) (locking lock 42))",
            42,
            "a locking form whose body is just the literal 42",
            "the value the locking form returns",
            scenario=(
                "Tom approached the narrow gate with the stone marker. He grabbed it "
                "and thought about the meaning — 42. He held the stone, thought "
                "clearly, then released it and walked away with the answer."
            ),
            need=(
                "Even a simple value — no computation, just a literal — needed "
                "protection by the lock. The gate serialized access to the critical "
                "moment."
            ),
            mapping=(
                "`locking` protects the body by holding a monitor, even if the body "
                "is just a value. The body evaluates to 42 while the monitor is held. "
                "42 is returned."
            ),
            resolution=(
                'the gate was passed — the simple answer held safely, returned: 42.'           )),
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
    print(f"grade-9 boy-wolf smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
