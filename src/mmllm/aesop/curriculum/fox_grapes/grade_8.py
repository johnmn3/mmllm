"""Grade 8 — protocols, multimethods, abstraction. Through fox-grapes.

The fable's moral dynamic — the hasty fox's rationalizing vs the
patient fox's disciplined evaluation — maps cleanly onto polymorphism:
different fruits respond to the same reach differently. The hasty fox
boasts that "every cluster yields the same way"; the patient fox
insists each kind of fruit, each orchard, has its own implementation
of the shared rule. One named operation; many honest answers, one per
species of fruit.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.fox_grapes.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.fox_grapes._metaphor_pools import _CARRYINGCASE_SUBPLOTS, _GUILD_SUBPLOTS, _SORTINGTABLE_SUBPLOTS


# ─────────────────────── grade-8 subplot extensions ───────────────────────
#
# Polymorphism is naturally about "the same call producing different
# results for different kinds." We extend the shared pool with two
# beats that lean into that — an assembly-of-fruits and a rule-pinned-
# to-an-orchard-gate.

_SUBPLOTS: list[SubplotTemplate] = list(_G1_SUBPLOTS) + [

    # 9. The assembly-of-fruits template — different fruits respond to
    #    the same reach in their own way.
    SubplotTemplate("""\
{place_idx}, {patient_fox_phrase} explained to {hasty_fox_phrase} that
one named operation could mean different things for different kinds of
fruit — a grape's yield was not a fig's yield, yet both could be asked
the same question. The form {form_display} captured {concept_phrase},
and {patient_fox} suggested they hand it to the REPL.""".replace(
        "{place_idx}", "Today {place}")),

    # 10. The rule-on-the-orchard-gate template — a written rule of
    #     behavior that several kinds of fruit must obey.
    SubplotTemplate("""\
A scrap of parchment, pinned to a post {place}, set out a rule that
every cluster in the orchard would have to abide by. {hasty_fox},
{emo_proud}, read it aloud: it was {concept_phrase}. {patient_fox_phrase}
said only the REPL could confirm what {form_display} actually decided."""),
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
    fable="fox-grapes",
    examples=[
        # Without protocols, conditional dispatch on a type tag is the
        # rough equivalent. We illustrate "many shapes, one operation."
        _ex("(defn speak [k] (cond (= k :hare) \"swift\" (= k :tortoise) \"steady\" :else \"silent\"))",
            None,
            'the defn that returns a habit-word per species tag',
            'the habit-word the procedure returns for a registered species tag',
            goal='define a procedure that returns a habit-word for each species tag, with a default for unrecognised tags',
            scenario="Renard the fox kept the orchard-keeper guild's roster. Each creature on the roster — sparrow, hedgehog, badger — had signed up for the same contract: when called by tag, respond with the species's own habit-word.",
            need="He needed a single procedure that took a creature's tag and read back the right habit-word — one phrase per registered tag, a default phrase otherwise.",
            mapping="A guild here is a shared interface — one entry-point name, many species-specific answers. `cond` walks the roster: the first matching tag's answer is what comes back. The guild's contract is the procedure; the species's habit-word is the answer.",
            resolution="the procedure stood ready on the guild's roster, dispatching each tag to its own habit-word, and to the default when no tag matched.",
            tags=("story",)),
        _ex("(let [speak (fn [k] (cond (= k :hare) \"swift\" (= k :tortoise) \"steady\"))] (speak :tortoise))",
            "steady",
            "speak applied to :tortoise via cond-dispatch",
            "what speak returns for :tortoise"),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-02 — deftype
G8_02 = SubjectCurriculum(
    grade=8, subject_id="G8-02",
    subject_title="deftype introduction",
    fable="fox-grapes",
    examples=[
        _ex("(do (deftype Pebble [color]) (.-color (Pebble. \"grey\")))",
            "grey",
            'the field-access on a deftype-instance',
            'the value at the named compartment of the labeled crate',
            goal='define a Pebble type with a color field, build one, and read its color',
            scenario='Renard the fox had built a labeled fruit-crate at the press with one named compartment. Each crate of his own type carried just that single field, fixed at the time of construction.',
            need='He had just packed a fresh crate, marking its slot, and now wanted to read back what was written on its label without unpacking the rest of the crate.',
            mapping="`deftype` declares a crate's shape — its named compartments. Constructing the type fills those slots; the field-access form reads the value at the named compartment directly. The shape is fixed; the slot's value is stamped at build time.",
            resolution="the label slot read back the value Renard had stamped at the press — the crate's own field, fetched in one step.",
            tags=("story",)),
        _ex("(do (deftype Stone [weight]) (.-weight (Stone. 7)))",
            7,
            "a deftype Stone with a weight field, then read its weight",
            "the weight of a Stone constructed with 7"),
    ],
    subplots=_CARRYINGCASE_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-03 — defrecord
G8_03 = SubjectCurriculum(
    grade=8, subject_id="G8-03",
    subject_title="defrecord introduction",
    fable="fox-grapes",
    examples=[
        _ex("(do (defrecord Runner [name pace]) (:pace (->Runner \"hare\" :swift)))",
            ":swift",
            "a defrecord Runner with name and pace fields, get :pace",
            "the :pace value of the Runner record"),
        _ex("(do (defrecord Runner [name pace]) (:name (->Runner \"tortoise\" :steady)))",
            "tortoise",
            "the :name field of a Runner record",
            "the :name value of the Runner constructed with \"tortoise\""),
    ],
    subplots=_CARRYINGCASE_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-04 — defprotocol
G8_04 = SubjectCurriculum(
    grade=8, subject_id="G8-04",
    subject_title="Protocol definition",
    fable="fox-grapes",
    examples=[
        # Defining a protocol returns the protocol var; we use an
        # ancillary call that demonstrates it was defined.
        _ex("(do (defprotocol Pace (speed [this])) (some? Pace))",
            True,
            "a defprotocol Pace with a single method speed",
            "whether the Pace protocol was defined (a non-nil truthy value)"),
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
    fable="fox-grapes",
    examples=[
        _ex("(do (defprotocol Pace (speed [this]))"
            " (extend-protocol Pace java.lang.String (speed [_] \"swift\"))"
            " (speed \"hare\"))",
            "swift",
            "a Pace protocol extended to String, then call speed on a string",
            "what speed returns when applied to \"hare\""),
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
    fable="fox-grapes",
    examples=[
        _ex("(do (defprotocol Pace (speed [this]))"
            " (extend-protocol Pace"
            "   java.lang.String (speed [_] :string-pace)"
            "   java.lang.Long   (speed [_] :long-pace))"
            " (speed 42))",
            ":long-pace",
            "Pace dispatched on the class of its argument; called with 42",
            "the keyword speed returns for the integer 42"),
        _ex("(do (defprotocol Pace (speed [this]))"
            " (extend-protocol Pace"
            "   java.lang.String (speed [_] :string-pace)"
            "   java.lang.Long   (speed [_] :long-pace))"
            " (speed \"x\"))",
            ":string-pace",
            "Pace dispatched on a string argument",
            "the keyword speed returns for the string \"x\""),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-07 — Record + Protocol
G8_07 = SubjectCurriculum(
    grade=8, subject_id="G8-07",
    subject_title="Record implementing protocol",
    fable="fox-grapes",
    examples=[
        _ex("(do (defprotocol Pace (speed [this]))"
            " (defrecord Hare [name] Pace (speed [_] :swift))"
            " (speed (->Hare \"Pip\")))",
            ":swift",
            "a defrecord Hare that implements Pace with speed -> :swift",
            "the keyword speed returns for a Hare record"),
        _ex("(do (defprotocol Pace (speed [this]))"
            " (defrecord Tortoise [name] Pace (speed [_] :steady))"
            " (speed (->Tortoise \"Shelly\")))",
            ":steady",
            "a Tortoise record implementing Pace with speed -> :steady",
            "the keyword speed returns for a Tortoise record"),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-08 — defmulti
G8_08 = SubjectCurriculum(
    grade=8, subject_id="G8-08",
    subject_title="Multimethod defmulti",
    fable="fox-grapes",
    examples=[
        _ex("(do (defmulti pace :species)"
            " (defmethod pace :hare [_] :swift)"
            " (pace {:species :hare}))",
            ":swift",
            'the multimethod call routed through a registered species channel',
            "the channel's habit-word for a basket bearing a registered species tag",
            goal='define a multimethod that dispatches on a :species tag, register a method for one species, then call it',
            scenario='Renard the fox set up a sorting-tray at the market. The tray dispatched each basket by the :species tag stamped on it — one channel per species, more added by anyone.',
            need='He needed to register a handler for one species, then drop a basket bearing that tag onto the tray.',
            mapping='A defmulti posts the tray and the dispatch rule. A defmethod registers a channel for one tag. Calling the multimethod reads the tag and routes through the matching channel.',
            resolution="the basket's tag routed it through the registered channel, and the tray returned that channel's habit-word.",
            tags=("story",)),
        _ex("(do (defmulti tag :kind)"
            " (defmethod tag :stone [_] :hard)"
            " (tag {:kind :stone}))",
            ":hard",
            "a defmulti tag dispatching on :kind",
            "what tag returns for {:kind :stone}"),
    ],
    subplots=_SORTINGTABLE_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-09 — defmethod
G8_09 = SubjectCurriculum(
    grade=8, subject_id="G8-09",
    subject_title="Multimethod defmethod",
    fable="fox-grapes",
    examples=[
        _ex("(do (defmulti pace :species)"
            " (defmethod pace :hare [_] :swift)"
            " (defmethod pace :tortoise [_] :steady)"
            " (pace {:species :tortoise}))",
            ":steady",
            "two defmethod entries on pace, called with :tortoise",
            "what pace returns for {:species :tortoise}"),
        _ex("(do (defmulti pace :species)"
            " (defmethod pace :hare [_] :swift)"
            " (defmethod pace :tortoise [_] :steady)"
            " (defmethod pace :default [_] :unknown)"
            " (pace {:species :owl}))",
            ":unknown",
            "a :default fallback method on pace, called with an unknown species",
            "what pace returns for {:species :owl} when :default falls through"),
    ],
    subplots=_SORTINGTABLE_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-10 — Multimethod vs protocol
G8_10 = SubjectCurriculum(
    grade=8, subject_id="G8-10",
    subject_title="Multimethod vs protocol",
    fable="fox-grapes",
    examples=[
        # Both can implement the same dispatching idea.
        _ex("(do (defmulti show identity)"
            " (defmethod show :hare [_] \"swift\")"
            " (show :hare))",
            "swift",
            "a defmulti dispatching on identity, with one method for :hare",
            "the string show returns for :hare"),
        _ex("(do (defprotocol Show (show [this]))"
            " (extend-protocol Show java.lang.String (show [s] (str \"str-\" s)))"
            " (show \"hare\"))",
            "str-hare",
            "a Show protocol extended to String, called with \"hare\"",
            "the string show returns for \"hare\" via protocol"),
    ],
    subplots=_SORTINGTABLE_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-11 — Protocol vs interface
G8_11 = SubjectCurriculum(
    grade=8, subject_id="G8-11",
    subject_title="Protocol vs Java interface",
    fable="fox-grapes",
    examples=[
        # We illustrate a protocol acting as the Clojure-side analog of
        # a Java interface — the same dispatching shape, but defined
        # purely in Clojure.
        _ex("(do (defprotocol IPace (run [this]))"
            " (extend-protocol IPace java.lang.String (run [_] :ran))"
            " (run \"hare\"))",
            ":ran",
            "an IPace protocol (Clojure analogue of a Java interface) extended to String",
            "the keyword run returns for \"hare\" via the protocol"),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-12 — extend-type
G8_12 = SubjectCurriculum(
    grade=8, subject_id="G8-12",
    subject_title="extend-type on built-in types",
    fable="fox-grapes",
    examples=[
        _ex("(do (defprotocol Pace (speed [this]))"
            " (extend-type java.lang.Long Pace (speed [_] :number-pace))"
            " (speed 5))",
            ":number-pace",
            "extend-type used to attach Pace to Long, called with 5",
            "the keyword speed returns for 5"),
        _ex("(do (defprotocol Pace (speed [this]))"
            " (extend-type java.lang.String Pace (speed [_] :string-pace))"
            " (speed \"hare\"))",
            ":string-pace",
            "extend-type attaching Pace to String",
            "the keyword speed returns for \"hare\" via extend-type"),
    ],
    subplots=_SORTINGTABLE_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-13 — this-style vs fn-style
G8_13 = SubjectCurriculum(
    grade=8, subject_id="G8-13",
    subject_title="this-style vs fn-style",
    fable="fox-grapes",
    examples=[
        # The first arg is conventionally `this` in protocol method
        # bodies — illustrate by capturing the field via this.
        _ex("(do (defprotocol Named (name-of [this]))"
            " (defrecord Hare [n] Named (name-of [this] (:n this)))"
            " (name-of (->Hare \"Pip\")))",
            "Pip",
            "a protocol method using this to read a field",
            "the name returned by name-of for a Hare record"),
        _ex("(do (defprotocol Tagged (tag-of [this]))"
            " (defrecord Stone [t] Tagged (tag-of [this] (:t this)))"
            " (tag-of (->Stone :grey)))",
            ":grey",
            "a Tagged protocol method that pulls :t off this",
            "the :t value via tag-of for a Stone"),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-14 — No protocol inheritance
G8_14 = SubjectCurriculum(
    grade=8, subject_id="G8-14",
    subject_title="Protocols don't inherit",
    fable="fox-grapes",
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
    fable="fox-grapes",
    examples=[
        _ex("(do (derive ::hare ::runner) (isa? ::hare ::runner))",
            True,
            "deriving ::hare from ::runner and asking isa?",
            "whether ::hare isa? ::runner after derive"),
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
    fable="fox-grapes",
    examples=[
        # A small "many implementations behind one protocol" example.
        _ex("(do (defprotocol Move (step [this]))"
            " (defrecord Hare [] Move (step [_] :leap))"
            " (defrecord Tortoise [] Move (step [_] :plod))"
            " (mapv step [(->Hare) (->Tortoise)]))",
            [":leap", ":plod"],
            "a Move protocol with two record implementations, mapped over instances",
            "the pair of step results for a Hare and a Tortoise"),
        _ex("(do (defprotocol Sound (cry [this]))"
            " (defrecord Hare [] Sound (cry [_] :thump))"
            " (defrecord Tortoise [] Sound (cry [_] :hiss))"
            " (cry (->Tortoise)))",
            ":hiss",
            "a Sound protocol with two implementations, called on a Tortoise",
            "the keyword cry returns for a Tortoise"),
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
    print(f"grade-8 fox-grapes smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
