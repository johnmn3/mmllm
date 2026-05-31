"""Grade 9 — state and concurrency primitives. Through goose-eggs.

The fable's moral dynamic — the patient {owner}'s careful, transactional
updates versus the {visitor}'s greed-driven shortcut to grab the lot at
once — maps cleanly onto the state-and-concurrency primitives. The
owner is a careful coin-counter at the chest, only updating the running
total when each egg's been tallied; the visitor wants to slam the lid
shut and pocket the chest. The REPL settles every dispute.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.goose_eggs.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)


# ─────────────────────── grade-9 subplot extensions ───────────────────────
#
# State + concurrency = "things that change over time." We extend the
# shared pool with two beats: the careful coin-counter at the chest
# (the owner's transactional update) and the greedy grab (the visitor's
# uncoordinated shortcut that the REPL must arbitrate).

_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    # 9. The careful coin-counter — owner updates the running total at
    #    the chest only after each egg's been tallied; visitor watches.
    SubplotTemplate("""\
{owner_phrase} kept a small chest of coins {place} and a running total
that changed each time another egg from {goose_phrase} was sold.
{owner_he_she_cap} explained that the form {form_display} captured
{concept_phrase}: a careful, ordered update, the way a coin only goes
into the chest after it has been counted. {visitor_phrase}, {emo_proud},
asked the REPL to confirm the final value."""),

    # 10. The greedy grab — visitor wants to seize the chest without
    #     coordinating; owner insists on the right primitive.
    SubplotTemplate("""\
"Why count one coin at a time?" {visitor_phrase} demanded {place}, eyeing
the chest. "{visitor_he_she_cap} could just take the lot at once!"
{owner_phrase}, {emo_patient}, sketched out {concept_phrase} on the
ledger instead and showed the form {form_display}: the proper way for
the runtime to manage the change as each egg of {goose_phrase} was
tallied. They agreed to submit it to the REPL."""),

    # 11. The market-trip ledger — owner reconciles the day's coin take
    #     against the egg-count on returning from market.
    SubplotTemplate("""\
On returning from market {place}, {owner_phrase} sat down to reconcile
the day's coin take against the eggs sold from {goose_phrase}'s basket.
The form {form_display} captured {concept_phrase} — the ordered update
{owner_he_she} preferred to any hasty tally. {visitor_phrase},
{emo_greedy}, wanted the total at once, but agreed to wait while
{owner} submitted the form to the REPL."""),
]


def _ex(form, expected, concept, what):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what)


_PLAN_POOL_G9: tuple[str, ...] = _PLAN_POOL + (
    "I bind the state, perform the update, then dereference.",
    "I wrap the def, the update, and the deref together in a do block.",
    "I let the runtime mediate the change before reading the final value.",
    "I count each coin into the chest before reading the running total.",
)


# ─────────────────────── 18 grade-9 subjects ───────────────────────


# G9-01 — Immutability review
G9_01 = SubjectCurriculum(
    grade=9, subject_id="G9-01",
    subject_title="Immutability as default — review",
    fable="goose-eggs",
    examples=[
        # `assoc` returns a new map; the original is unchanged.
        _ex("(let [m {:a 1}] (assoc m :b 2) m)",
            {":a": 1},
            "binding m, calling (assoc m :b 2), then returning m unchanged",
            "the original map after a non-mutating assoc"),
        _ex("(let [v [1 2 3]] (conj v 4) v)",
            [1, 2, 3],
            "binding v, calling (conj v 4), then returning v unchanged",
            "the original vector after conj"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-02 — Why state at all
G9_02 = SubjectCurriculum(
    grade=9, subject_id="G9-02",
    subject_title="Why state at all",
    fable="goose-eggs",
    examples=[
        # The minimal "place that needs identity over time" example.
        _ex("(do (def counter (atom 0)) (swap! counter inc) @counter)",
            1,
            "an atom counter, incremented once, then read",
            "the value of counter after one swap! inc"),
        _ex("(do (def progress (atom :idle)) (reset! progress :running) @progress)",
            ":running",
            "a progress atom reset to :running",
            "the value of progress after reset!"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-03 — Atom introduction
G9_03 = SubjectCurriculum(
    grade=9, subject_id="G9-03",
    subject_title="Atom introduction",
    fable="goose-eggs",
    examples=[
        _ex("(do (def a (atom 0)) (swap! a inc) @a)",
            1,
            "an atom starting at 0, incremented once via swap!",
            "the value of the atom after one swap! inc"),
        _ex("(do (def a (atom 10)) (swap! a + 5) @a)",
            15,
            "an atom starting at 10, with (swap! a + 5)",
            "the value of the atom after swap! + 5"),
        _ex("(do (def a (atom :start)) (reset! a :done) @a)",
            ":done",
            "an atom reset! from :start to :done",
            "the value of the atom after reset!"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-04 — Atom CAS semantics
G9_04 = SubjectCurriculum(
    grade=9, subject_id="G9-04",
    subject_title="Atom CAS semantics",
    fable="goose-eggs",
    examples=[
        # `compare-and-set!` succeeds when current matches expected.
        _ex("(do (def a (atom 0)) (compare-and-set! a 0 1) @a)",
            1,
            "compare-and-set! on an atom: expected 0, set to 1",
            "the value of the atom after a successful CAS"),
        _ex("(do (def a (atom 5)) (compare-and-set! a 0 99) @a)",
            5,
            "compare-and-set! when the expected value doesn't match",
            "the value of the atom after a CAS that does not fire"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-05 — Watch on atom
G9_05 = SubjectCurriculum(
    grade=9, subject_id="G9-05",
    subject_title="Watch on atom",
    fable="goose-eggs",
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
            "the contents of the log after one swap"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-06 — Validator on atom
G9_06 = SubjectCurriculum(
    grade=9, subject_id="G9-06",
    subject_title="Validator on atom",
    fable="goose-eggs",
    examples=[
        # A validator gates updates; we set one then read the value.
        _ex("(do (def a (atom 0))"
            " (set-validator! a number?)"
            " (swap! a inc)"
            " @a)",
            1,
            "an atom with a number? validator, incremented once",
            "the value of the atom after a valid update"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-07 — Ref introduction
G9_07 = SubjectCurriculum(
    grade=9, subject_id="G9-07",
    subject_title="Ref introduction",
    fable="goose-eggs",
    examples=[
        # Refs require dosync to update.
        _ex("(do (def r (ref 0)) (dosync (alter r inc)) @r)",
            1,
            "a ref incremented inside a dosync transaction",
            "the value of the ref after dosync alter inc"),
        _ex("(do (def r (ref 100)) (dosync (ref-set r 7)) @r)",
            7,
            "a ref ref-set to 7 inside dosync",
            "the value of the ref after ref-set 7"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-08 — dosync / alter
G9_08 = SubjectCurriculum(
    grade=9, subject_id="G9-08",
    subject_title="dosync and alter",
    fable="goose-eggs",
    examples=[
        # Two refs altered atomically inside one dosync.
        _ex("(do (def a (ref 1)) (def b (ref 2))"
            " (dosync (alter a inc) (alter b inc))"
            " [@a @b])",
            [2, 3],
            "two refs each incremented inside a single dosync",
            "the pair [a b] after the coordinated transaction"),
        _ex("(do (def r (ref 10)) (dosync (alter r + 5)) @r)",
            15,
            "a ref altered by + 5 inside dosync",
            "the value of the ref after alter + 5"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-09 — Ref vs atom
G9_09 = SubjectCurriculum(
    grade=9, subject_id="G9-09",
    subject_title="Ref vs atom",
    fable="goose-eggs",
    examples=[
        # The same operation expressed both ways.
        _ex("(do (def a (atom 0)) (swap! a inc) @a)",
            1,
            "an atom updated via swap!",
            "the value of the atom after one swap! inc"),
        _ex("(do (def r (ref 0)) (dosync (alter r inc)) @r)",
            1,
            "a ref updated via alter inside dosync",
            "the value of the ref after one dosync alter inc"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-10 — Agent introduction
G9_10 = SubjectCurriculum(
    grade=9, subject_id="G9-10",
    subject_title="Agent introduction",
    fable="goose-eggs",
    examples=[
        # send is async — we await before reading.
        _ex("(do (def ag (agent 0)) (send ag inc) (await ag) @ag)",
            1,
            "an agent sent inc and awaited",
            "the value of the agent after send inc and await"),
        _ex("(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)",
            15,
            "an agent sent (+ 10) and awaited",
            "the value of the agent after send + 10 and await"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-11 — send / send-off
G9_11 = SubjectCurriculum(
    grade=9, subject_id="G9-11",
    subject_title="send and send-off",
    fable="goose-eggs",
    examples=[
        _ex("(do (def ag (agent 0)) (send ag inc) (await ag) @ag)",
            1,
            "send used on an agent, then awaited",
            "the agent's value after send inc"),
        _ex("(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)",
            1,
            "send-off used on an agent, then awaited",
            "the agent's value after send-off inc"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-12 — await
G9_12 = SubjectCurriculum(
    grade=9, subject_id="G9-12",
    subject_title="await — synchronizing on agents",
    fable="goose-eggs",
    examples=[
        _ex("(do (def ag (agent 0)) (send ag inc) (send ag inc) (await ag) @ag)",
            2,
            "two send inc calls then await before deref",
            "the agent's value after two sends and await"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-13 — future
G9_13 = SubjectCurriculum(
    grade=9, subject_id="G9-13",
    subject_title="future introduction",
    fable="goose-eggs",
    examples=[
        _ex("@(future (+ 1 2))",
            3,
            "a future computing (+ 1 2), dereferenced",
            "the value of the future for (+ 1 2)"),
        _ex("@(future (* 6 7))",
            42,
            "a future computing (* 6 7), dereferenced",
            "the value of the future for (* 6 7)"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-14 — deref @
G9_14 = SubjectCurriculum(
    grade=9, subject_id="G9-14",
    subject_title="deref @ shorthand",
    fable="goose-eggs",
    examples=[
        _ex("(do (def a (atom 7)) @a)",
            7,
            "deref via @ on an atom holding 7",
            "the value of the atom via @"),
        _ex("(do (def a (atom 7)) (deref a))",
            7,
            "deref via the function form on an atom",
            "the value of the atom via the deref function"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-15 — promise
G9_15 = SubjectCurriculum(
    grade=9, subject_id="G9-15",
    subject_title="promise — deliver and deref",
    fable="goose-eggs",
    examples=[
        _ex("(do (def p (promise)) (deliver p :done) @p)",
            ":done",
            "a promise delivered with :done, then dereffed",
            "the value of the promise after deliver"),
        _ex("(do (def p (promise)) (deliver p 42) @p)",
            42,
            "a promise delivered with 42",
            "the value of the promise after deliver 42"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-16 — volatile
G9_16 = SubjectCurriculum(
    grade=9, subject_id="G9-16",
    subject_title="volatile — when STM is too heavy",
    fable="goose-eggs",
    examples=[
        _ex("(do (def v (volatile! 0)) (vswap! v inc) @v)",
            1,
            "a volatile! incremented via vswap!",
            "the value of the volatile after one vswap! inc"),
        _ex("(do (def v (volatile! 5)) (vreset! v 99) @v)",
            99,
            "a volatile! reset via vreset!",
            "the value of the volatile after vreset! 99"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-17 — thread-local binding
G9_17 = SubjectCurriculum(
    grade=9, subject_id="G9-17",
    subject_title="binding — thread-local",
    fable="goose-eggs",
    examples=[
        _ex("(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))",
            99,
            "a dynamic var *p* rebound to 99 inside binding",
            "the value of *p* inside the binding form"),
        _ex("(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)",
            1,
            "the value of *p* AFTER the binding form exits",
            "the original value of *p* once binding has unwound"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G9,
)


# G9-18 — locking
G9_18 = SubjectCurriculum(
    grade=9, subject_id="G9-18",
    subject_title="locking — last resort",
    fable="goose-eggs",
    examples=[
        # `locking` takes a monitor and a body; we use a simple body.
        _ex("(do (def lock (Object.)) (locking lock (+ 1 2)))",
            3,
            "a locking form around (+ 1 2) using a fresh Object as monitor",
            "the result of the body inside locking"),
        _ex("(do (def lock (Object.)) (locking lock 42))",
            42,
            "a locking form whose body is just the literal 42",
            "the value the locking form returns"),
    ],
    subplots=_SUBPLOTS,
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
    print(f"grade-9 goose-eggs smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
