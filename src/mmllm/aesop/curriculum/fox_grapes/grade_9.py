"""Grade 9 — state and concurrency primitives. Through fox-grapes.

The fable's moral dynamic — patient fox keeping a careful tally of
fruit-counts, updating the cluster-count atomically, while the hasty
fox just snatches without checking — maps cleanly onto the state-and-
concurrency primitives. Patient fox insists on dosync and CAS; hasty
fox wants to mutate without coordinating. The REPL settles every
dispute the same way it settles every other fox argument: by
evaluating the form and reporting what came back.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.fox_grapes.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.fox_grapes._metaphor_pools import _BASKET_SUBPLOTS, _NOTEBOOK_SUBPLOTS, _RUNNERAHEAD_SUBPLOTS


# ─────────────────────── grade-9 subplot extensions ───────────────────────
#
# State + concurrency = "things that change over time." We extend the
# shared pool with two beats: the careful-tally (patient fox's
# transactional update of the fruit-count) and the snatching-update
# (hasty fox's uncoordinated mutation that the REPL must arbitrate).

_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    # 9. The careful-tally template — patient fox updates a fruit-count
    #    the right way; hasty fox watches impatiently.
    SubplotTemplate("""\
{patient_fox_phrase} kept a small tally of state {place} — a count of
fruit that might change as the foxes worked the cluster. {patient_fox_he_she_cap}
explained that the form {form_display} captured {concept_phrase}: a
careful, ordered update. {hasty_fox_phrase}, {emo_proud}, asked the
REPL to confirm the final value."""),

    # 10. The snatching-update template — hasty fox wants to update
    #     without coordinating; patient fox insists on the right primitive.
    SubplotTemplate("""\
"Why bother with all this?" {hasty_fox_phrase} demanded {place}.
"{hasty_fox_he_she_cap} could just snatch and write the new value!"
{patient_fox_phrase}, {emo_patient}, sketched out {concept_phrase}
instead and showed the form {form_display}: the proper way for the
runtime to manage change. They agreed to submit it to the REPL."""),
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
    fable="fox-grapes",
    examples=[
        # `assoc` returns a new map; the original is unchanged.
        _ex("(let [m {:a 1}] (assoc m :b 2) m)",
            {":a": 1},
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Renard the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Renard reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and his parchment recorded the day's count for that label.",
            tags=("story",)),
        _ex("(let [v [1 2 3]] (conj v 4) v)",
            [1, 2, 3],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario="Vix the fox laid out a vine-tray with named compartments at the press, the day's pickings sorted by their labels.",
            need='Vix reached into the right slot to read what the tray held there, leaving the rest untouched.',
            mapping="A collection in Clojure is a labeled tray. Looking up by key reads the value at that slot; the tray's other slots stay closed.",
            resolution="the slot yielded its value, and her parchment recorded the day's count for that label.",
            tags=("story",)),
    ],
    subplots=_BASKET_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-02 — Why state at all
G9_02 = SubjectCurriculum(
    grade=9, subject_id="G9-02",
    subject_title="Why state at all",
    fable="fox-grapes",
    examples=[
        # The minimal "place that needs identity over time" example.
        _ex("(do (def counter (atom 0)) (swap! counter inc) @counter)",
            1,
            "the atom's value after one atomic increment stroke",
            "the ledger page's tally after the atomic increment stroke",
            goal='create an atom holding 0, increment it, then read its value',
            scenario='Vix the fox kept a leather ledger on the orchard wall. One page tracked a running tally that any fox could update, but only by crossing out the old number and writing the new one in a single, careful stroke.',
            need='She wanted the tally moved one step forward — the old value replaced by old-plus-one — then she would read off whatever number now stood on the page.',
            mapping="An atom is the ledger's mutable page; the swap form is the atomic stroke — applying the increment to the old value and writing the new one in one indivisible move. The deref form peeks at the current page without changing it.",
            resolution="the page now read the post-stroke tally — the old number advanced by one, the ledger's record honest and current.",
            tags=("story",)),
        _ex("(do (def progress (atom :idle)) (reset! progress :running) @progress)",
            ":running",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Sly wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-03 — Atom introduction
G9_03 = SubjectCurriculum(
    grade=9, subject_id="G9-03",
    subject_title="Atom introduction",
    fable="fox-grapes",
    examples=[
        _ex("(do (def a (atom 0)) (swap! a inc) @a)",
            1,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Renard wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
        _ex("(do (def a (atom 10)) (swap! a + 5) @a)",
            15,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Vix wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
        _ex("(do (def a (atom :start)) (reset! a :done) @a)",
            ":done",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Sly wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-04 — Atom CAS semantics
G9_04 = SubjectCurriculum(
    grade=9, subject_id="G9-04",
    subject_title="Atom CAS semantics",
    fable="fox-grapes",
    examples=[
        # `compare-and-set!` succeeds when current matches expected.
        _ex("(do (def a (atom 0)) (compare-and-set! a 0 1) @a)",
            1,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Renard wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
        _ex("(do (def a (atom 5)) (compare-and-set! a 0 99) @a)",
            5,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Vix wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-05 — Watch on atom
G9_05 = SubjectCurriculum(
    grade=9, subject_id="G9-05",
    subject_title="Watch on atom",
    fable="fox-grapes",
    examples=[
        # A watch can record into another atom each time the watched atom
        # changes; we read the recording atom at the end.
        _ex("(do (def a (atom 0))"
            " (def log (atom []))"
            " (add-watch a :w (fn [_ _ _ n] (swap! log conj n)))"
            " (swap! a inc)"
            " @log)",
            [1],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Sly wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-06 — Validator on atom
G9_06 = SubjectCurriculum(
    grade=9, subject_id="G9-06",
    subject_title="Validator on atom",
    fable="fox-grapes",
    examples=[
        # A validator gates updates; we set one then read the value.
        _ex("(do (def a (atom 0))"
            " (set-validator! a number?)"
            " (swap! a inc)"
            " @a)",
            1,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Renard wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-07 — Ref introduction
G9_07 = SubjectCurriculum(
    grade=9, subject_id="G9-07",
    subject_title="Ref introduction",
    fable="fox-grapes",
    examples=[
        # Refs require dosync to update.
        _ex("(do (def r (ref 0)) (dosync (alter r inc)) @r)",
            1,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Vix wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
        _ex("(do (def r (ref 100)) (dosync (ref-set r 7)) @r)",
            7,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Sly wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-08 — dosync / alter
G9_08 = SubjectCurriculum(
    grade=9, subject_id="G9-08",
    subject_title="dosync and alter",
    fable="fox-grapes",
    examples=[
        # Two refs altered atomically inside one dosync.
        _ex("(do (def a (ref 1)) (def b (ref 2))"
            " (dosync (alter a inc) (alter b inc))"
            " [@a @b])",
            [2, 3],
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Renard wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
        _ex("(do (def r (ref 10)) (dosync (alter r + 5)) @r)",
            15,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Vix wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-09 — Ref vs atom
G9_09 = SubjectCurriculum(
    grade=9, subject_id="G9-09",
    subject_title="Ref vs atom",
    fable="fox-grapes",
    examples=[
        # The same operation expressed both ways.
        _ex("(do (def a (atom 0)) (swap! a inc) @a)",
            1,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Sly wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
        _ex("(do (def r (ref 0)) (dosync (alter r inc)) @r)",
            1,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Renard wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-10 — Agent introduction
G9_10 = SubjectCurriculum(
    grade=9, subject_id="G9-10",
    subject_title="Agent introduction",
    fable="fox-grapes",
    examples=[
        # send is async — we await before reading.
        _ex("(do (def ag (agent 0)) (send ag inc) (await ag) @ag)",
            1,
            "the agent's value after a send-and-await increment",
            "the slate's tally after the runner has returned with the new value",
            goal='create an agent at 0, send an increment, wait for completion, read the value',
            scenario="Vix the fox sent a swift runner ahead to the market with a small slate. The runner would advance the slate's tally by one and return.",
            need="She needed the slate updated by the runner's pace, with a guarantee that by the time she read it, the runner had finished.",
            mapping="An agent is the slate the runner carries; the send form dispatches the work; the await form waits for return; the deref reads the slate's value.",
            resolution='by the time Vix arrived, the runner had returned, and the slate showed one more than it had started with.',
            tags=("story",)),
        _ex("(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)",
            15,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox sent a swift runner ahead to the market with a small slate.',
            need="Vix needed the slate updated at the runner's pace, with a guarantee that by the time it was read, the runner had finished.",
            mapping="Agents and futures dispatch work to a runner; await ties the runner's return back. The deref reads the slate's current value once the runner has settled.",
            resolution="the runner returned, the slate showed the form's post-update value, and the value was honest.",
            tags=("story",)),
    ],
    subplots=_RUNNERAHEAD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-11 — send / send-off
G9_11 = SubjectCurriculum(
    grade=9, subject_id="G9-11",
    subject_title="send and send-off",
    fable="fox-grapes",
    examples=[
        _ex("(do (def ag (agent 0)) (send ag inc) (await ag) @ag)",
            1,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox sent a swift runner ahead to the market with a small slate.',
            need="Sly needed the slate updated at the runner's pace, with a guarantee that by the time it was read, the runner had finished.",
            mapping="Agents and futures dispatch work to a runner; await ties the runner's return back. The deref reads the slate's current value once the runner has settled.",
            resolution="the runner returned, the slate showed the form's post-update value, and the value was honest.",
            tags=("story",)),
        _ex("(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)",
            1,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox sent a swift runner ahead to the market with a small slate.',
            need="Renard needed the slate updated at the runner's pace, with a guarantee that by the time it was read, the runner had finished.",
            mapping="Agents and futures dispatch work to a runner; await ties the runner's return back. The deref reads the slate's current value once the runner has settled.",
            resolution="the runner returned, the slate showed the form's post-update value, and the value was honest.",
            tags=("story",)),
    ],
    subplots=_RUNNERAHEAD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-12 — await
G9_12 = SubjectCurriculum(
    grade=9, subject_id="G9-12",
    subject_title="await — synchronizing on agents",
    fable="fox-grapes",
    examples=[
        _ex("(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)",
            2,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox sent a swift runner ahead to the market with a small slate.',
            need="Vix needed the slate updated at the runner's pace, with a guarantee that by the time it was read, the runner had finished.",
            mapping="Agents and futures dispatch work to a runner; await ties the runner's return back. The deref reads the slate's current value once the runner has settled.",
            resolution="the runner returned, the slate showed the form's post-update value, and the value was honest.",
            tags=("story",)),
    ],
    subplots=_RUNNERAHEAD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-13 — future
G9_13 = SubjectCurriculum(
    grade=9, subject_id="G9-13",
    subject_title="future introduction",
    fable="fox-grapes",
    examples=[
        _ex("@(future (+ 1 2))",
            3,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox sent a swift runner ahead to the market with a small slate.',
            need="Sly needed the slate updated at the runner's pace, with a guarantee that by the time it was read, the runner had finished.",
            mapping="Agents and futures dispatch work to a runner; await ties the runner's return back. The deref reads the slate's current value once the runner has settled.",
            resolution="the runner returned, the slate showed the form's post-update value, and the value was honest.",
            tags=("story",)),
        _ex("@(future (* 6 7))",
            42,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox sent a swift runner ahead to the market with a small slate.',
            need="Renard needed the slate updated at the runner's pace, with a guarantee that by the time it was read, the runner had finished.",
            mapping="Agents and futures dispatch work to a runner; await ties the runner's return back. The deref reads the slate's current value once the runner has settled.",
            resolution="the runner returned, the slate showed the form's post-update value, and the value was honest.",
            tags=("story",)),
    ],
    subplots=_RUNNERAHEAD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-14 — deref @
G9_14 = SubjectCurriculum(
    grade=9, subject_id="G9-14",
    subject_title="deref @ shorthand",
    fable="fox-grapes",
    examples=[
        _ex("(do (def a (atom 7)) @a)",
            7,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Vix wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
        _ex("(do (def a (atom 7)) (deref a))",
            7,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Sly wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-15 — promise
G9_15 = SubjectCurriculum(
    grade=9, subject_id="G9-15",
    subject_title="promise — deliver and deref",
    fable="fox-grapes",
    examples=[
        _ex("(do (def p (promise)) (deliver p :done) @p)",
            ":done",
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox sent a swift runner ahead to the market with a small slate.',
            need="Renard needed the slate updated at the runner's pace, with a guarantee that by the time it was read, the runner had finished.",
            mapping="Agents and futures dispatch work to a runner; await ties the runner's return back. The deref reads the slate's current value once the runner has settled.",
            resolution="the runner returned, the slate showed the form's post-update value, and the value was honest.",
            tags=("story",)),
        _ex("(do (def p (promise)) (deliver p 42) @p)",
            42,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox sent a swift runner ahead to the market with a small slate.',
            need="Vix needed the slate updated at the runner's pace, with a guarantee that by the time it was read, the runner had finished.",
            mapping="Agents and futures dispatch work to a runner; await ties the runner's return back. The deref reads the slate's current value once the runner has settled.",
            resolution="the runner returned, the slate showed the form's post-update value, and the value was honest.",
            tags=("story",)),
    ],
    subplots=_RUNNERAHEAD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-16 — volatile
G9_16 = SubjectCurriculum(
    grade=9, subject_id="G9-16",
    subject_title="volatile — when STM is too heavy",
    fable="fox-grapes",
    examples=[
        _ex("(do (def v (volatile! 0)) (vswap! v inc) @v)",
            1,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Sly wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
        _ex("(do (def v (volatile! 5)) (vreset! v 99) @v)",
            99,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Renard wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-17 — thread-local binding
G9_17 = SubjectCurriculum(
    grade=9, subject_id="G9-17",
    subject_title="binding — thread-local",
    fable="fox-grapes",
    examples=[
        _ex("(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))",
            99,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Vix wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
        _ex("(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)",
            1,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Sly wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
    ],
    subplots=_NOTEBOOK_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-18 — locking
G9_18 = SubjectCurriculum(
    grade=9, subject_id="G9-18",
    subject_title="locking — last resort",
    fable="fox-grapes",
    examples=[
        # `locking` takes a monitor and a body; we use a simple body.
        _ex("(do (def lock (Object.)) (locking lock (+ 1 2)))",
            3,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Renard wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
        _ex("(do (def lock (Object.)) (locking lock 42))",
            42,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox kept a leather ledger on the wall. One page tracked a running tally any fox could update by an atomic stroke.',
            need="Vix wanted the page advanced by the form's update, then read off whatever number the ledger now held.",
            mapping='An atom is a mutable page; `swap!` is the atomic stroke; the deref reads the current page without changing it. The update happens in one indivisible move.',
            resolution="the ledger's page now read the value the stroke had written, honest and current to the form's update.",
            tags=("story",)),
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
    print(f"grade-9 fox-grapes smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
