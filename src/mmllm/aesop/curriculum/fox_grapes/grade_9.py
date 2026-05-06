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
        _ex("(let [m {:a 1}] (assoc m :b 2) m)", {":a": 1}, 'the form', 'the value the form evaluates to',
            goal='return the original map unchanged after associating a new key',
            scenario='Renard the fox carried a vine-tray with one labeled slot :a holding tally 1.',
            need='A visitor offered Renard a new berry-count 2 for slot :b. Renard wanted to honor the gift and also keep slot :a untouched.',
            mapping='The assoc operation creates a fresh tray with both slots—:a and :b—without changing the original tray Renard carried.',
            resolution='when Renard reached for the original tray at the end, it still held only :a with 1, exactly as it had started.',
            tags=("story",)),
        _ex("(let [v [1 2 3]] (conj v 4) v)", [1, 2, 3], 'the form', 'the value the form evaluates to',
            goal='add a value to a sequence without altering the original',
            scenario='Vix the fox had a vine-tray holding three berry-counts: 1, 2, 3 in order.',
            need='A fourth berry arrived and Vix wanted to append it to the tray. But the original tray had to stay as it was for the ledger.',
            mapping='The conj operation adds the new value to a fresh tray without touching the original. The original remains 1, 2, 3.',
            resolution='when Vix returned to the original tray, it still read 1, 2, 3—unchanged and ready for the evening tally.',
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
        _ex("(do (def progress (atom :idle)) (reset! progress :running) @progress)", ":running", 'the form', 'the value the form evaluates to',
            goal='change a mutable state from idle to running and read the new value',
            scenario='Sly the fox kept a leather ledger page marking the foraging-run state: either :idle or :running.',
            need='When work began, Sly needed to flip the state from :idle to :running, then check what the page now showed.',
            mapping='An atom holds the state keyword. The reset! form overwrites the entire page in one stroke. The deref reads the current marking.',
            resolution='the page now marked :running, showing the foraging work had begun.',
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
        _ex("(do (def a (atom 0)) (swap! a inc) @a)", 1, 'the form', 'the value the form evaluates to',
            goal='start with 0 on a ledger page, increment it once, and read the result',
            scenario='Renard the fox marked a ledger page with the number 0 to count berries picked.',
            need='Each berry picked should add 1 to the tally. Renard needed to stroke the first increment and see the result.',
            mapping='An atom is the ledger page. The swap! form reads the old number, applies the increment function, and writes the new number back—all in one stroke.',
            resolution='the page now showed 1, the first berry recorded.',
            tags=("story",)),
        _ex("(do (def a (atom 10)) (swap! a + 5) @a)", 15, 'the form', 'the value the form evaluates to',
            goal='start with 10, add 5 atomically, and read the result',
            scenario='Vix the fox had a ledger page showing 10—the morning harvest count.',
            need='An afternoon haul brought 5 more grapes. Vix needed to add them to the page and see the new total.',
            mapping='The swap! form takes the old value 10, applies the addition with 5, and writes the new sum back.',
            resolution='the page now read 15, the day's full harvest marked.',
            tags=("story",)),
        _ex("(do (def a (atom :start)) (reset! a :done) @a)", ":done", 'the form', 'the value the form evaluates to',
            goal='replace a state value on a page from :start to :done',
            scenario='Sly the fox marked a ledger page with :start to show the foraging-run had not begun.',
            need='When the run completed, Sly needed to replace :start with :done on the same page.',
            mapping='The reset! form erases the old marker entirely and writes a fresh new marker in one indivisible stroke.',
            resolution='the page now showed :done, declaring the day's foraging complete.',
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
        _ex("(do (def a (atom 0)) (compare-and-set! a 0 1) @a)", 1, 'the form', 'the value the form evaluates to',
            goal='change the ledger page only if it currently holds 0',
            scenario='Renard the fox kept a ledger page showing 0 berries. He wanted to advance it to 1, but only if no other fox had changed the page since he last looked.',
            need='Renard needed a guarantee: "If the page still reads 0 when I stroke, change it to 1; if not, leave it alone."',
            mapping='The compare-and-set! form checks the old value matches what you expect, and only then writes the new value—a safe atomic swap.',
            resolution='since the page held 0 as expected, it now held 1.',
            tags=("story",)),
        _ex("(do (def a (atom 5)) (compare-and-set! a 0 99) @a)", 5, 'the form', 'the value the form evaluates to',
            goal='attempt to change the page only if it reads 0, but it reads 5 instead',
            scenario='Vix the fox checked a ledger page thinking it showed 0, but it actually showed 5.',
            need='Vix wanted to update it only if it was 0. If it had changed to something else, she needed to leave it untouched.',
            mapping='The compare-and-set! form checks: "Is it 0?" It is not—it is 5—so the operation fails and the page stays exactly as it was.',
            resolution='the page remained 5, unchanged, because the condition was not met.',
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
            " @log)", [1], 'the form', 'the value the form evaluates to',
            goal='watch a ledger page and record every value it becomes',
            scenario='Renard the fox kept a ledger page at 0 and a separate log-tray to record each new value the page would take.',
            need='Whenever the page changed, Renard wanted the new value automatically appended to the log-tray so no change went unnoticed.',
            mapping='The add-watch form sets a guardian at the ledger page; when the page changes, the guardian records the new value into the log-tray. When we read the log-tray, it holds all the values the page became.',
            resolution='after the page was incremented to 1, the log-tray held a record of that new value.',
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
            " @a)", 1, 'the form', 'the value the form evaluates to',
            goal='protect a ledger page with a rule that only numbers are allowed',
            scenario='Vix the fox kept a ledger page showing 0 berries. She wanted to ensure no other fox could write non-numeric marks on the page by accident.',
            need='Vix set a rule: "Only numbers may be written here." Then she incremented the page and read the result.',
            mapping='The set-validator! form installs a guardian at the page. The guardian checks every new value: if it passes the check (is a number?), the stroke succeeds; if not, it fails.',
            resolution='because 1 passed the number? check, the page advanced to 1.',
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
        _ex("(do (def r (ref 0)) (dosync (alter r inc)) @r)", 1, 'the form', 'the value the form evaluates to',
            goal='increment a transactional ledger page inside a dosync block',
            scenario='Renard the fox kept a transactional ledger page holding 0—a page that could only be safely changed within a synchronized session.',
            need='Renard needed to increment the page, but the rule was strict: all edits must happen inside a dosync block so the runtime could mediate conflicts.',
            mapping='A ref is the transactional ledger page. The dosync form opens a transaction. The alter form reads the old value, applies the increment, and writes it back—all atomically within the dosync.',
            resolution='after the synchronized transaction, the page held 1.',
            tags=("story",)),
        _ex("(do (def r (ref 100)) (dosync (ref-set r 7)) @r)", 7, 'the form', 'the value the form evaluates to',
            goal='replace a transactional page value with a new one',
            scenario='Sly the fox had a transactional ledger page showing 100—a harvest tally from the previous season.',
            need='A new season began with a fresh count, and Sly needed to reset the page to 7 within a dosync transaction.',
            mapping='The dosync opens the transaction. The ref-set form replaces the entire page value atomically.',
            resolution='the page now showed 7, the new season tally recorded.',
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
            " [@a @b])", [2, 3], 'the form', 'the value the form evaluates to',
            goal='increment two transactional pages together in a single dosync',
            scenario='Renard the fox kept two ledger pages: one showing 1 (green grapes), one showing 2 (ripe grapes). Both needed to advance when a new harvest arrived.',
            need='Renard had to update both pages in one atomic transaction—if one succeeded and the other failed, the ledger would be inconsistent.',
            mapping='The dosync opens one transaction covering both alters. Each alter reads, increments, and writes atomically. Both finish together, or both roll back.',
            resolution='both pages advanced together: the first to 2, the second to 3, the ledger balanced.',
            tags=("story",)),
        _ex("(do (def r (ref 10)) (dosync (alter r + 5)) @r)", 15, 'the form', 'the value the form evaluates to',
            goal='add a value to a transactional page within a dosync',
            scenario='Vix the fox had a transactional ledger page showing 10 berries from the morning harvest.',
            need='An afternoon foraging brought 5 more berries. Vix needed to add them within a dosync to keep the ledger consistent.',
            mapping='The dosync opens the transaction. The alter reads 10, applies the addition with 5, and writes the result atomically.',
            resolution='the page now showed 15, the morning and afternoon harvests combined.',
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
        _ex("(do (def a (atom 0)) (swap! a inc) @a)", 1, 'the form', 'the value the form evaluates to'),
        _ex("(do (def r (ref 0)) (dosync (alter r inc)) @r)", 1, 'the form', 'the value the form evaluates to'),
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
        _ex("(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)", 15, 'the form', 'the value the form evaluates to'),
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
        _ex("(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)", 1, 'the form', 'the value the form evaluates to'),
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
        _ex("(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)", 2, 'the form', 'the value the form evaluates to'),
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
        _ex("@(future (* 6 7))", 42, 'the form', 'the value the form evaluates to'),
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
        _ex("(do (def a (atom 7)) @a)", 7, 'the form', 'the value the form evaluates to'),
        _ex("(do (def a (atom 7)) (deref a))", 7, 'the form', 'the value the form evaluates to'),
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
        _ex("(do (def p (promise)) (deliver p :done) @p)", ":done", 'the form', 'the value the form evaluates to'),
        _ex("(do (def p (promise)) (deliver p 42) @p)", 42, 'the form', 'the value the form evaluates to'),
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
        _ex("(do (def v (volatile! 0)) (vswap! v inc) @v)", 1, 'the form', 'the value the form evaluates to'),
        _ex("(do (def v (volatile! 5)) (vreset! v 99) @v)", 99, 'the form', 'the value the form evaluates to'),
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
        _ex("(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))", 99, 'the form', 'the value the form evaluates to'),
        _ex("(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)", 1, 'the form', 'the value the form evaluates to'),
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
        _ex("(do (def lock (Object.)) (locking lock (+ 1 2)))", 3, 'the form', 'the value the form evaluates to'),
        _ex("(do (def lock (Object.)) (locking lock 42))", 42, 'the form', 'the value the form evaluates to'),
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
