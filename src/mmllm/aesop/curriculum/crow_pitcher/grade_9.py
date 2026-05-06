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
        ),
        SubjectExample(
            form="(let [v [1 2 3]] (conj v 4) v)",
            expected=[1, 2, 3],
            concept_phrase="binding a vector, conjoining a new element to a new vector, and returning the original",
            question_what="the original vector after conj returns a new vector",
            goal_text="bind a vector v, call conj to add 4 to a new vector, then return the unchanged v",
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
        ),
        SubjectExample(
            form="(do (def progress (atom :idle)) (reset! progress :running) @progress)",
            expected=":running",
            concept_phrase="binding an atom to progress, atomically resetting it to a new value, and dereferencing the result",
            question_what="the value after atomically resetting progress and dereferencing",
            goal_text="construct an atom holding an idle value as progress, atomically reset it to running, and dereference the result",
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
            concept_phrase="atom, swap, and deref",
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
                "1 — the tally, incremented once by the swap, read back "
                "from the clay face."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def a (atom 10)) (swap! a + 5) @a)",
            expected=15,
            concept_phrase="atom, swap, deref",
            question_what="the value returned by dereferencing a after defining a as an atom holding 10 and swapping it via + 5",
            goal_text="construct an atom holding 10, atomically swap it by applying + to 5, and dereference the result",
        ),
        SubjectExample(
            form="(do (def a (atom :start)) (reset! a :done) @a)",
            expected=":done",
            concept_phrase="atom, reset, deref",
            question_what="the value returned by dereferencing a after defining a as an atom holding a start keyword and resetting it to done",
            goal_text="construct an atom holding a start keyword, atomically reset it to a done keyword, and dereference the result",
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
            concept_phrase="atom, CAS, deref",
            question_what="the value returned by dereferencing a after defining a as an atom holding 0 and performing a successful compare-and-set to 1",
            goal_text="construct an atom holding 0, perform a compare-and-set checking for 0 and setting to 1, and dereference",
        ),
        SubjectExample(
            form="(do (def a (atom 5)) (compare-and-set! a 0 99) @a)",
            expected=5,
            concept_phrase="atom, failed CAS, deref",
            question_what="the value returned by dereferencing a after defining a as an atom holding 5 and attempting a compare-and-set that fails",
            goal_text="construct an atom holding 5, perform a compare-and-set checking for 0 and setting to 99, and dereference",
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
            concept_phrase="ref, dosync, alter, deref",
            question_what="the value returned by dereferencing r after defining a ref holding 0, performing a transactional alter via inc, and dereferencing",
            goal_text="construct a ref holding 0, perform a transactional alter by applying inc inside dosync, and dereference",
        ),
        SubjectExample(
            form="(do (def r (ref 100)) (dosync (ref-set r 7)) @r)",
            expected=7,
            concept_phrase="ref, dosync, ref-set, deref",
            question_what="the value returned by dereferencing r after defining a ref holding 100, setting it to 7 inside dosync, and dereferencing",
            goal_text="construct a ref holding 100, perform a transactional ref-set to 7 inside dosync, and dereference",
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
        ),
        SubjectExample(
            form="(do (def r (ref 10)) (dosync (alter r + 5)) @r)",
            expected=15,
            concept_phrase="ref, dosync, alter, deref",
            question_what="the value returned by dereferencing r after defining a ref holding 10, performing a transactional alter via + 5, and dereferencing",
            goal_text="construct a ref holding 10, perform a transactional alter by applying + with 5 inside dosync, and dereference",
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
            concept_phrase="atom, swap, deref",
            question_what="the value returned by dereferencing a after defining an atom holding 0, swapping it via inc, and dereferencing",
            goal_text="construct an atom holding 0, atomically swap it by applying inc, and dereference",
        ),
        SubjectExample(
            form="(do (def r (ref 0)) (dosync (alter r inc)) @r)",
            expected=1,
            concept_phrase="ref, dosync, alter, deref",
            question_what="the value returned by dereferencing r after defining a ref holding 0, altering it via inc inside dosync, and dereferencing",
            goal_text="construct a ref holding 0, perform a transactional alter by applying inc inside dosync, and dereference",
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
            concept_phrase="agent, send, await, deref",
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
                "1 — the scout returned with the incremented count, the "
                "tally settling into the pitcher's depth."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (def ag (agent 5)) (send ag + 10) (await ag) @ag)",
            expected=15,
            concept_phrase="agent, send, await, deref",
            question_what="the value returned by dereferencing ag after defining an agent holding 5, sending + 10 asynchronously, awaiting, and dereferencing",
            goal_text="construct an agent holding 5, asynchronously send + with 10 to it, await its completion, and dereference",
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
            concept_phrase="agent, send, await, deref",
            question_what="the value returned by dereferencing ag after defining an agent holding 0, using send to dispatch inc, awaiting, and dereferencing",
            goal_text="construct an agent holding 0, use send to asynchronously apply inc, await its completion, and dereference",
        ),
        SubjectExample(
            form="(do (def ag (agent 0)) (send-off ag inc) (await ag) @ag)",
            expected=1,
            concept_phrase="agent, send-off, await, deref",
            question_what="the value returned by dereferencing ag after defining an agent holding 0, using send-off to dispatch inc, awaiting, and dereferencing",
            goal_text="construct an agent holding 0, use send-off to asynchronously apply inc, await its completion, and dereference",
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
            concept_phrase="agent, double send, await, deref",
            question_what="the value returned by dereferencing ag after defining an agent holding 0, sending inc twice asynchronously, awaiting, and dereferencing",
            goal_text="construct an agent holding 0, asynchronously send inc twice, synchronize with await, and dereference",
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
            concept_phrase="future, add, deref",
            question_what="the value the messenger returns from adding 1 and 2",
            goal_text="dispatch a runner to compute the sum of 1 and 2; later, ask the runner for the answer",
        ),
        SubjectExample(
            form="@(future (* 6 7))",
            expected=42,
            concept_phrase="future, multiply, deref",
            question_what="the value returned by dereferencing a future that multiplies 6 and 7",
            goal_text="construct a future that multiplies 6 and 7, and dereference it",
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
        ),
        SubjectExample(
            form="(do (def a (atom 7)) (deref a))",
            expected=7,
            concept_phrase="constructing an atom and extracting its value using the deref function",
            question_what="the value extracted from an atom using the deref function",
            goal_text="construct an atom holding 7 and dereference it using the deref function",
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
            concept_phrase="promise, deliver, deref",
            question_what="the value returned by dereferencing a promise after defining it, delivering a keyword to it, and dereferencing",
            goal_text="construct a promise, deliver a completion keyword to it, and dereference to get the delivered value",
        ),
        SubjectExample(
            form="(do (def p (promise)) (deliver p 42) @p)",
            expected=42,
            concept_phrase="promise, deliver, deref",
            question_what="the value returned by dereferencing a promise after defining it, delivering a number to it, and dereferencing",
            goal_text="construct a promise, deliver 42 to it, and dereference to get the delivered value",
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
            concept_phrase="volatile, vswap, deref",
            question_what="the value returned by dereferencing v after defining a volatile holding 0, performing a non-transactional swap via inc, and dereferencing",
            goal_text="construct a volatile holding 0, perform a non-transactional swap by applying inc, and dereference",
        ),
        SubjectExample(
            form="(do (def v (volatile! 5)) (vreset! v 99) @v)",
            expected=99,
            concept_phrase="volatile, vreset, deref",
            question_what="the value returned by dereferencing v after defining a volatile holding 5, performing a non-transactional reset to 99, and dereferencing",
            goal_text="construct a volatile holding 5, perform a non-transactional reset to 99, and dereference",
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
            concept_phrase="dynamic var, binding, read",
            question_what="the value of the dynamic var when read inside the binding form after defining it and rebinding",
            goal_text="define a dynamic var *p* as 1, use binding to rebind it to 99, and read its value inside",
        ),
        SubjectExample(
            form="(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)",
            expected=1,
            concept_phrase="dynamic var, binding, read after",
            question_what="the value of the dynamic var when read after the binding form unwound",
            goal_text="define a dynamic var *p* as 1, use binding to rebind it to 99 inside, and read its value after binding exits",
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
            concept_phrase="lock, locking, arithmetic",
            question_what="the value returned by evaluating an addition inside a locked critical section after creating a monitor and acquiring the lock",
            goal_text="create an object to use as a monitor, acquire the lock, and evaluate an addition inside",
        ),
        SubjectExample(
            form="(do (def lock (Object.)) (locking lock 42))",
            expected=42,
            concept_phrase="lock, locking, literal",
            question_what="the literal value returned by evaluating it inside a locked critical section after creating a monitor and acquiring the lock",
            goal_text="create an object to use as a monitor, acquire the lock, and evaluate a literal inside",
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
