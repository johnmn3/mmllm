"""Grade 8 — protocols, multimethods, abstraction. Through boy-who-cried-wolf.

Subplot lens: different villagers respond to the same call differently —
the elder, the reeve, the careful neighbouring shepherd each have their
own way. This maps cleanly onto polymorphic dispatch: one named
operation, many implementations. The shepherd boasts that everyone
must hear the same alarm; the elder insists each kind of villager has
its own honest way of answering, and the REPL settles which one is
called.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.boy_wolf.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.boy_wolf._metaphor_pools import (
    _CARRYINGCASE_SUBPLOTS, _GUILD_SUBPLOTS, _SORTINGTABLE_SUBPLOTS,
)
from mmllm.aesop.curriculum.boy_wolf._goals import GOALS


# ─────────────────────── grade-8 subplot extensions ───────────────────────
#
# Polymorphism is naturally about "the same call producing different
# answers for different kinds of villagers." We extend the shared pool
# with two beats that lean into that: a meeting-of-villagers and a
# protocol-as-village-decree. The shepherd is still the cautionary
# voice; the elder is still the patient evaluator.

_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    # The meeting-of-villagers — different villagers each have their
    # own honest answer to the same named call.
    SubplotTemplate("""\
Today {place}, {elder_phrase} explained to {shepherd_phrase} that one
named call could mean different things for different kinds of villagers
— the reeve answered one way, a careful neighbouring shepherd another,
yet both could be asked the same question. The form {form_display}
captured {concept_phrase}, and {elder} suggested they hand it to the
REPL."""),

    # The protocol-as-village-decree — a written rule pinned to the
    # village board that several kinds of villagers must obey.
    SubplotTemplate("""\
A scrap of parchment, pinned to the village board {place}, set out a
rule that every honest villager would have to abide by. {shepherd},
{emo_proud}, read it aloud: it was {concept_phrase}. {elder_phrase}
said only the REPL could confirm what {form_display} actually
decided."""),
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
        goal_text=goal if goal is not None else canon.get("goal", ""),
        scenario=scenario, need=need, mapping=mapping, resolution=resolution,
        tags=tags,
    )
_PLAN_POOL_G8: tuple[str, ...] = _PLAN_POOL + (
    "I define the protocol or type, then exercise it.",
    "I wrap the definition and the call together in a do block.",
    "I let the polymorphic dispatch pick the right implementation.",
)


# ─────────────────────── 16 grade-8 subjects ───────────────────────


# G8-01 — Why polymorphism
G8_01 = SubjectCurriculum(
    grade=8, subject_id="G8-01",
    subject_title="Why polymorphism",
    fable="boy-wolf",
    examples=[
        # Without protocols, conditional dispatch on a type tag is the
        # rough equivalent. We illustrate "many shapes, one operation."
        _ex("(defn speak [k] (cond (= k :wolf) \"howl\" (= k :flock) \"bleat\" :else \"silent\"))",
            None,
            "a function speak that returns different strings for :wolf vs :flock",
            "the form that defines speak via cond"),
        _ex("(let [speak (fn [k] (cond (= k :wolf) \"howl\" (= k :flock) \"bleat\"))] (speak :flock))",
            "bleat",
            "speak applied to :flock via cond-dispatch",
            "what speak returns for :flock"),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-02 — deftype
G8_02 = SubjectCurriculum(
    grade=8, subject_id="G8-02",
    subject_title="deftype introduction",
    fable="boy-wolf",
    examples=[
        _ex("(do (deftype Lantern [color]) (.-color (Lantern. \"amber\")))",
            "amber",
            "a deftype Lantern with a color field, then read color of an instance",
            "the color field of a Lantern instance"),
        _ex("(do (deftype Crook [length]) (.-length (Crook. 7)))",
            7,
            "a deftype Crook with a length field, then read its length",
            "the length of a Crook constructed with 7"),
    ],
    subplots=_CARRYINGCASE_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-03 — defrecord
G8_03 = SubjectCurriculum(
    grade=8, subject_id="G8-03",
    subject_title="defrecord introduction",
    fable="boy-wolf",
    examples=[
        _ex("(do (defrecord Watcher [name post]) (:post (->Watcher \"shepherd\" :hilltop)))",
            ":hilltop",
            "a defrecord Watcher with name and post fields, get :post",
            "the :post value of the Watcher record"),
        _ex("(do (defrecord Watcher [name post]) (:name (->Watcher \"elder\" :village)))",
            "elder",
            "the :name field of a Watcher record",
            "the :name value of the Watcher constructed with \"elder\""),
    ],
    subplots=_CARRYINGCASE_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-04 — defprotocol
G8_04 = SubjectCurriculum(
    grade=8, subject_id="G8-04",
    subject_title="Protocol definition",
    fable="boy-wolf",
    examples=[
        # Defining a protocol returns the protocol var; we use an
        # ancillary call that demonstrates it was defined.
        _ex("(do (defprotocol Alarm (sound [this])) (some? Alarm))",
            True,
            "a defprotocol Alarm with a single method sound",
            "whether the Alarm protocol was defined (a non-nil truthy value)"),
        _ex("(do (defprotocol Greet (hail [this])) (some? Greet))",
            True,
            "a defprotocol Greet with one method hail",
            "whether Greet has been established"),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-05 — extend-protocol
G8_05 = SubjectCurriculum(
    grade=8, subject_id="G8-05",
    subject_title="Protocol extension",
    fable="boy-wolf",
    examples=[
        _ex("(do (defprotocol Alarm (sound [this]))"
            " (extend-protocol Alarm java.lang.String (sound [_] \"howl\"))"
            " (sound \"wolf\"))",
            "howl",
            "an Alarm protocol extended to String, then call sound on a string",
            "what sound returns when applied to \"wolf\""),
        _ex("(do (defprotocol Greet (hail [this]))"
            " (extend-protocol Greet java.lang.Long (hail [_] :number))"
            " (hail 7))",
            ":number",
            "a Greet protocol extended to Long, then call hail on 7",
            "the keyword hail returns for the number 7"),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-06 — Protocol method dispatch
G8_06 = SubjectCurriculum(
    grade=8, subject_id="G8-06",
    subject_title="Protocol method dispatch",
    fable="boy-wolf",
    examples=[
        _ex("(do (defprotocol Alarm (sound [this]))"
            " (extend-protocol Alarm"
            "   java.lang.String (sound [_] :string-alarm)"
            "   java.lang.Long   (sound [_] :long-alarm))"
            " (sound 42))",
            ":long-alarm",
            "Alarm dispatched on the class of its argument; called with 42",
            "the keyword sound returns for the integer 42"),
        _ex("(do (defprotocol Alarm (sound [this]))"
            " (extend-protocol Alarm"
            "   java.lang.String (sound [_] :string-alarm)"
            "   java.lang.Long   (sound [_] :long-alarm))"
            " (sound \"x\"))",
            ":string-alarm",
            "Alarm dispatched on a string argument",
            "the keyword sound returns for the string \"x\""),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-07 — Record + Protocol
G8_07 = SubjectCurriculum(
    grade=8, subject_id="G8-07",
    subject_title="Record implementing protocol",
    fable="boy-wolf",
    examples=[
        _ex("(do (defprotocol Alarm (sound [this]))"
            " (defrecord Shepherd [name] Alarm (sound [_] :cry))"
            " (sound (->Shepherd \"Pip\")))",
            ":cry",
            "a defrecord Shepherd that implements Alarm with sound -> :cry",
            "the keyword sound returns for a Shepherd record"),
        _ex("(do (defprotocol Alarm (sound [this]))"
            " (defrecord Elder [name] Alarm (sound [_] :measured))"
            " (sound (->Elder \"Mira\")))",
            ":measured",
            "an Elder record implementing Alarm with sound -> :measured",
            "the keyword sound returns for an Elder record"),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-08 — defmulti
G8_08 = SubjectCurriculum(
    grade=8, subject_id="G8-08",
    subject_title="Multimethod defmulti",
    fable="boy-wolf",
    examples=[
        _ex("(do (defmulti reply :role)"
            " (defmethod reply :shepherd [_] :cry)"
            " (reply {:role :shepherd}))",
            ":cry",
            "a defmulti reply that dispatches on :role, called with :shepherd",
            "what reply returns for {:role :shepherd}"),
        _ex("(do (defmulti tag :kind)"
            " (defmethod tag :lantern [_] :bright)"
            " (tag {:kind :lantern}))",
            ":bright",
            "a defmulti tag dispatching on :kind",
            "what tag returns for {:kind :lantern}"),
    ],
    subplots=_SORTINGTABLE_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-09 — defmethod
G8_09 = SubjectCurriculum(
    grade=8, subject_id="G8-09",
    subject_title="Multimethod defmethod",
    fable="boy-wolf",
    examples=[
        _ex("(do (defmulti reply :role)"
            " (defmethod reply :shepherd [_] :cry)"
            " (defmethod reply :elder    [_] :measured)"
            " (reply {:role :elder}))",
            ":measured",
            "two defmethod entries on reply, called with :elder",
            "what reply returns for {:role :elder}"),
        _ex("(do (defmulti reply :role)"
            " (defmethod reply :shepherd [_] :cry)"
            " (defmethod reply :elder    [_] :measured)"
            " (defmethod reply :default  [_] :unknown)"
            " (reply {:role :stranger}))",
            ":unknown",
            "a :default fallback method on reply, called with an unknown role",
            "what reply returns for {:role :stranger} when :default falls through"),
    ],
    subplots=_SORTINGTABLE_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-10 — Multimethod vs protocol
G8_10 = SubjectCurriculum(
    grade=8, subject_id="G8-10",
    subject_title="Multimethod vs protocol",
    fable="boy-wolf",
    examples=[
        # Both can implement the same dispatching idea.
        _ex("(do (defmulti show identity)"
            " (defmethod show :wolf [_] \"howl\")"
            " (show :wolf))",
            "howl",
            "a defmulti dispatching on identity, with one method for :wolf",
            "the string show returns for :wolf"),
        _ex("(do (defprotocol Show (show [this]))"
            " (extend-protocol Show java.lang.String (show [s] (str \"str-\" s)))"
            " (show \"wolf\"))",
            "str-wolf",
            "a Show protocol extended to String, called with \"wolf\"",
            "the string show returns for \"wolf\" via protocol"),
    ],
    subplots=_SORTINGTABLE_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-11 — Protocol vs interface
G8_11 = SubjectCurriculum(
    grade=8, subject_id="G8-11",
    subject_title="Protocol vs Java interface",
    fable="boy-wolf",
    examples=[
        # We illustrate a protocol acting as the Clojure-side analog of
        # a Java interface — the same dispatching shape, but defined
        # purely in Clojure.
        _ex("(do (defprotocol IAlarm (raise [this]))"
            " (extend-protocol IAlarm java.lang.String (raise [_] :raised))"
            " (raise \"wolf\"))",
            ":raised",
            "an IAlarm protocol (Clojure analogue of a Java interface) extended to String",
            "the keyword raise returns for \"wolf\" via the protocol"),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-12 — extend-type
G8_12 = SubjectCurriculum(
    grade=8, subject_id="G8-12",
    subject_title="extend-type on built-in types",
    fable="boy-wolf",
    examples=[
        _ex("(do (defprotocol Alarm (sound [this]))"
            " (extend-type java.lang.Long Alarm (sound [_] :number-alarm))"
            " (sound 5))",
            ":number-alarm",
            "extend-type used to attach Alarm to Long, called with 5",
            "the keyword sound returns for 5"),
        _ex("(do (defprotocol Alarm (sound [this]))"
            " (extend-type java.lang.String Alarm (sound [_] :string-alarm))"
            " (sound \"wolf\"))",
            ":string-alarm",
            "extend-type attaching Alarm to String",
            "the keyword sound returns for \"wolf\" via extend-type"),
    ],
    subplots=_SORTINGTABLE_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-13 — this-style vs fn-style
G8_13 = SubjectCurriculum(
    grade=8, subject_id="G8-13",
    subject_title="this-style vs fn-style",
    fable="boy-wolf",
    examples=[
        # The first arg is conventionally `this` in protocol method
        # bodies — illustrate by capturing the field via this.
        _ex("(do (defprotocol Named (name-of [this]))"
            " (defrecord Shepherd [n] Named (name-of [this] (:n this)))"
            " (name-of (->Shepherd \"Pip\")))",
            "Pip",
            "a protocol method using this to read a field",
            "the name returned by name-of for a Shepherd record"),
        _ex("(do (defprotocol Tagged (tag-of [this]))"
            " (defrecord Lantern [t] Tagged (tag-of [this] (:t this)))"
            " (tag-of (->Lantern :amber)))",
            ":amber",
            "a Tagged protocol method that pulls :t off this",
            "the :t value via tag-of for a Lantern"),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-14 — No protocol inheritance
G8_14 = SubjectCurriculum(
    grade=8, subject_id="G8-14",
    subject_title="Protocols don't inherit",
    fable="boy-wolf",
    examples=[
        # We illustrate the single-protocol-only nature: each protocol
        # is its own dispatching surface.
        _ex("(do (defprotocol A (a-op [this]))"
            " (defprotocol B (b-op [this]))"
            " (extend-protocol A java.lang.String (a-op [_] :a-impl))"
            " (extend-protocol B java.lang.String (b-op [_] :b-impl))"
            " [(a-op \"x\") (b-op \"x\")])",
            [":a-impl", ":b-impl"],
            "two independent protocols A and B both extended to String",
            "the pair [a-op b-op] when each protocol is used independently"),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-15 — derive / isa
G8_15 = SubjectCurriculum(
    grade=8, subject_id="G8-15",
    subject_title="derive and isa? — multimethod hierarchy",
    fable="boy-wolf",
    examples=[
        _ex("(do (derive ::shepherd ::villager) (isa? ::shepherd ::villager))",
            True,
            "deriving ::shepherd from ::villager and asking isa?",
            "whether ::shepherd isa? ::villager after derive"),
        _ex("(isa? java.lang.Long java.lang.Number)",
            True,
            "the predicate (isa? Long Number)",
            "whether Long isa? Number"),
        _ex("(isa? java.lang.String java.lang.Number)",
            False,
            "the predicate (isa? String Number)",
            "whether String isa? Number"),
    ],
    subplots=_SORTINGTABLE_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-16 — Abstract design with protocols
G8_16 = SubjectCurriculum(
    grade=8, subject_id="G8-16",
    subject_title="Abstract design with protocols",
    fable="boy-wolf",
    examples=[
        # A small "many implementations behind one protocol" example.
        _ex("(do (defprotocol Watch (look [this]))"
            " (defrecord Shepherd [] Watch (look [_] :scan))"
            " (defrecord Elder [] Watch (look [_] :verify))"
            " (mapv look [(->Shepherd) (->Elder)]))",
            [":scan", ":verify"],
            "a Watch protocol with two record implementations, mapped over instances",
            "the pair of look results for a Shepherd and an Elder"),
        _ex("(do (defprotocol Sound (cry [this]))"
            " (defrecord Shepherd [] Sound (cry [_] :alarm))"
            " (defrecord Elder [] Sound (cry [_] :calm))"
            " (cry (->Elder)))",
            ":calm",
            "a Sound protocol with two implementations, called on an Elder",
            "the keyword cry returns for an Elder"),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# ─────────────────────── registry ───────────────────────


SUBJECTS: dict[str, SubjectCurriculum] = {
    s.subject_id: s for s in (
        G8_01, G8_02, G8_03, G8_04, G8_05, G8_06, G8_07, G8_08,
        G8_09, G8_10, G8_11, G8_12, G8_13, G8_14, G8_15, G8_16,
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
    print(f"grade-8 boy-wolf smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
