"""Grade 8 — protocols, multimethods, abstraction. Through tortoise-hare.

The fable's moral dynamic — Hare's vanity vs Tortoise's steadiness —
maps cleanly onto polymorphism: different species respond to the same
call differently. Hare boasts that "everyone runs the same way";
Tortoise insists each kind of creature has its own implementation.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.tortoise_hare.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL,
)


# ─────────────────────── grade-8 subplot extensions ───────────────────────
#
# Polymorphism is naturally about "the same call producing different
# results for different types of creatures." We extend the shared pool
# with two beats that lean into that — a meeting-of-species and a
# protocol-as-decree.

_SUBPLOTS: list[SubplotTemplate] = _GOAL_SUBPLOTS


def _ex(form, expected, concept, what, goal="", tags=()):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal, tags=tags)


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
    fable="tortoise-hare",
    examples=[
        # Without protocols, conditional dispatch on a type tag is the
        # rough equivalent. We illustrate "many shapes, one operation."
        _ex("(defn speak [k] (cond (= k :hare) \"swift\" (= k :tortoise) \"steady\" :else \"silent\"))",
            None,
            "conditional dispatch on a tag",
            "the function definition",
            goal="define a function speak that returns different strings depending on whether its argument is :hare or :tortoise"),
        _ex("(let [speak (fn [k] (cond (= k :hare) \"swift\" (= k :tortoise) \"steady\"))] (speak :tortoise))",
            "steady",
            "the result of dispatching speak on :tortoise",
            "the value returned",
            goal="call speak with :tortoise to see what it returns when dispatched"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-02 — deftype
G8_02 = SubjectCurriculum(
    grade=8, subject_id="G8-02",
    subject_title="deftype introduction",
    fable="tortoise-hare",
    examples=[
        _ex("(do (deftype Pebble [color]) (.-color (Pebble. \"grey\")))",
            "grey",
            "reading the color field of a Pebble instance",
            "the color field value after defining a type Pebble with one field color, then constructing an instance and reading the field",
            goal="define a type Pebble with a color field and then read the color field from an instance"),
        _ex("(do (deftype Stone [weight]) (.-weight (Stone. 7)))",
            7,
            "reading the weight field of a Stone instance",
            "the weight field value after defining a type Stone with one field weight, then constructing an instance and reading the field",
            goal="define a type Stone with a weight field and then read the weight field from an instance"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-03 — defrecord
G8_03 = SubjectCurriculum(
    grade=8, subject_id="G8-03",
    subject_title="defrecord introduction",
    fable="tortoise-hare",
    examples=[
        _ex("(do (defrecord Runner [name pace]) (:pace (->Runner \"Alice\" :slow)))",
            ":slow",
            "reading the pace field from a Runner record",
            "the pace field value after defining a record Runner with two fields name and pace, then creating an instance and reading the pace field",
            goal="define a record type named Runner with two fields, then retrieve one field from an instance"),
        _ex("(do (defrecord Runner [name pace]) (:name (->Runner \"Bob\" :moderate)))",
            "Bob",
            "reading the name field from a Runner record",
            "the name field value after defining a record Runner with two fields name and pace, then creating an instance and reading the name field",
            goal="define a record type named Runner with two fields, then retrieve another field from an instance"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-04 — defprotocol
G8_04 = SubjectCurriculum(
    grade=8, subject_id="G8-04",
    subject_title="Protocol definition",
    fable="tortoise-hare",
    examples=[
        # Defining a protocol returns the protocol var; we use an
        # ancillary call that demonstrates it was defined.
        _ex("(do (defprotocol Pace (speed [this])) (some? Pace))",
            True,
            "a protocol definition",
            "whether the protocol var Pace is truthy after defining a protocol named Pace with one method speed taking a single argument this",
            goal="define a protocol named Pace with one method speed that takes a single argument this"),
        _ex("(do (defprotocol Greet (hail [this])) (some? Greet))",
            True,
            "a protocol definition",
            "whether the protocol var Greet is truthy after defining a protocol named Greet with one method hail taking a single argument this",
            goal="define a protocol named Greet with one method hail that takes a single argument this"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-05 — extend-protocol
G8_05 = SubjectCurriculum(
    grade=8, subject_id="G8-05",
    subject_title="Protocol extension",
    fable="tortoise-hare",
    examples=[
        _ex("(do (defprotocol Pace (speed [this]))"
            " (extend-protocol Pace java.lang.String (speed [_] \"swift\"))"
            " (speed \"hare\"))",
            "swift",
            "calling a protocol method on a string",
            "the value returned after defining protocol Pace with method speed, extending it to String with an implementation, then calling speed on a string",
            goal="define a protocol named Pace with one method speed, extend it to String type with an implementation, then call speed on a string"),
        _ex("(do (defprotocol Greet (hail [this]))"
            " (extend-protocol Greet java.lang.Long (hail [_] :number))"
            " (hail 7))",
            ":number",
            "calling a protocol method on a number",
            "the value returned after defining protocol Greet with method hail, extending it to Long with an implementation, then calling hail on a number",
            goal="define a protocol named Greet with one method hail, extend it to Long type with an implementation, then call hail on a number"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-06 — Protocol method dispatch
G8_06 = SubjectCurriculum(
    grade=8, subject_id="G8-06",
    subject_title="Protocol method dispatch",
    fable="tortoise-hare",
    examples=[
        _ex("(do (defprotocol Pace (speed [this]))"
            " (extend-protocol Pace"
            "   java.lang.String (speed [_] :string-pace)"
            "   java.lang.Long   (speed [_] :long-pace))"
            " (speed 42))",
            ":long-pace",
            "protocol dispatch on an integer",
            "the value returned after defining protocol Pace with method speed, extending it to both String and Long types with different implementations, then calling speed on the number 42",
            goal="define a protocol Pace with method speed, extend it to both String and Long types with different implementations, then call speed on the number 42"),
        _ex("(do (defprotocol Pace (speed [this]))"
            " (extend-protocol Pace"
            "   java.lang.String (speed [_] :string-pace)"
            "   java.lang.Long   (speed [_] :long-pace))"
            " (speed \"x\"))",
            ":string-pace",
            "protocol dispatch on a string",
            "the value returned after defining protocol Pace with method speed, extending it to both String and Long types with different implementations, then calling speed on a string",
            goal="define a protocol Pace with method speed, extend it to both String and Long types with different implementations, then call speed on a string"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-07 — Record + Protocol
G8_07 = SubjectCurriculum(
    grade=8, subject_id="G8-07",
    subject_title="Record implementing protocol",
    fable="tortoise-hare",
    examples=[
        _ex("(do (defprotocol Pace (speed [this]))"
            " (defrecord Hare [name] Pace (speed [_] :swift))"
            " (speed (->Hare \"Pip\")))",
            ":swift",
            "calling a protocol method on a record instance",
            "the value returned after defining protocol Pace with method speed, defining record Hare with one field name that implements Pace, then calling speed on a Hare instance",
            goal="define a protocol Pace with method speed, define a record Hare that implements Pace, then call speed on a Hare instance"),
        _ex("(do (defprotocol Pace (speed [this]))"
            " (defrecord Tortoise [name] Pace (speed [_] :steady))"
            " (speed (->Tortoise \"Shelly\")))",
            ":steady",
            "calling a protocol method on a record instance",
            "the value returned after defining protocol Pace with method speed, defining record Tortoise with one field name that implements Pace, then calling speed on a Tortoise instance",
            goal="define a protocol Pace with method speed, define a record Tortoise that implements Pace, then call speed on a Tortoise instance"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-08 — defmulti
G8_08 = SubjectCurriculum(
    grade=8, subject_id="G8-08",
    subject_title="Multimethod defmulti",
    fable="tortoise-hare",
    examples=[
        _ex("(do (defmulti pace :species)"
            " (defmethod pace :hare [_] :swift)"
            " (pace {:species :hare}))",
            ":swift",
            "calling a multimethod with a specific dispatch value",
            "the value returned after defining multimethod pace that dispatches on :species, adding a method for :hare, then calling pace with a map",
            goal="define a multimethod pace that dispatches on the :species key, add a method for :hare, then call pace with a map"),
        _ex("(do (defmulti tag :kind)"
            " (defmethod tag :stone [_] :hard)"
            " (tag {:kind :stone}))",
            ":hard",
            "calling a multimethod with a specific dispatch value",
            "the value returned after defining multimethod tag that dispatches on :kind, adding a method for :stone, then calling tag with a map",
            goal="define a multimethod tag that dispatches on the :kind key, add a method for :stone, then call tag with a map"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-09 — defmethod
G8_09 = SubjectCurriculum(
    grade=8, subject_id="G8-09",
    subject_title="Multimethod defmethod",
    fable="tortoise-hare",
    examples=[
        _ex("(do (defmulti pace :species)"
            " (defmethod pace :hare [_] :swift)"
            " (defmethod pace :tortoise [_] :steady)"
            " (pace {:species :tortoise}))",
            ":steady",
            "calling a multimethod with multiple methods",
            "the value returned after defining multimethod pace that dispatches on :species with methods for both :hare and :tortoise, then calling pace with a map",
            goal="define a multimethod pace that dispatches on :species with methods for both :hare and :tortoise, then call pace with {:species :tortoise}"),
        _ex("(do (defmulti pace :species)"
            " (defmethod pace :hare [_] :swift)"
            " (defmethod pace :tortoise [_] :steady)"
            " (defmethod pace :default [_] :unknown)"
            " (pace {:species :owl}))",
            ":unknown",
            "calling a multimethod with a default fallback",
            "the value returned after defining multimethod pace with methods for :hare, :tortoise, and :default, then calling pace with a dispatch value that doesn't match",
            goal="define a multimethod pace with methods for :hare and :tortoise plus a :default fallback, then call pace with a dispatch value that doesn't match"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-10 — Multimethod vs protocol
G8_10 = SubjectCurriculum(
    grade=8, subject_id="G8-10",
    subject_title="Multimethod vs protocol",
    fable="tortoise-hare",
    examples=[
        # Both can implement the same dispatching idea.
        _ex("(do (defmulti show identity)"
            " (defmethod show :rabbit [_] \"quick\")"
            " (show :rabbit))",
            "quick",
            "dispatching via multimethod",
            "the value returned after defining multimethod show that dispatches on identity, adding a method for :rabbit, then calling show with :rabbit",
            goal="define a multimethod show that dispatches on identity with a method for one specific value, then call it"),
        _ex("(do (defprotocol Show (show [this]))"
            " (extend-protocol Show java.lang.String (show [s] (str \"str-\" s)))"
            " (show \"hare\"))",
            "str-hare",
            "dispatching via protocol",
            "the value returned after defining protocol Show with method show, extending it to String with an implementation, then calling show on a string",
            goal="define a protocol Show with method show, extend it to String type, then call show on a string"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-11 — Protocol vs interface
G8_11 = SubjectCurriculum(
    grade=8, subject_id="G8-11",
    subject_title="Protocol vs Java interface",
    fable="tortoise-hare",
    examples=[
        # We illustrate a protocol acting as the Clojure-side analog of
        # a Java interface — the same dispatching shape, but defined
        # purely in Clojure.
        _ex("(do (defprotocol IPace (run [this]))"
            " (extend-protocol IPace java.lang.String (run [_] :ran))"
            " (run \"hare\"))",
            ":ran",
            "calling a protocol method on a string",
            "the value returned after defining protocol IPace with method run, extending it to String with an implementation, then calling run on a string",
            goal="define a protocol IPace with method run, extend it to String type, then call run on a string"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-12 — extend-type
G8_12 = SubjectCurriculum(
    grade=8, subject_id="G8-12",
    subject_title="extend-type on built-in types",
    fable="tortoise-hare",
    examples=[
        _ex("(do (defprotocol Pace (speed [this]))"
            " (extend-type java.lang.Long Pace (speed [_] :number-pace))"
            " (speed 5))",
            ":number-pace",
            "attaching a protocol to a built-in type via extend-type",
            "the value returned after defining protocol Pace with method speed, using extend-type to attach it to Long type with an implementation, then calling speed on a number",
            goal="define a protocol Pace with method speed, use extend-type to attach it to Long type, then call speed on a number"),
        _ex("(do (defprotocol Pace (speed [this]))"
            " (extend-type java.lang.String Pace (speed [_] :string-pace))"
            " (speed \"hare\"))",
            ":string-pace",
            "attaching a protocol to a built-in type via extend-type",
            "the value returned after defining protocol Pace with method speed, using extend-type to attach it to String type with an implementation, then calling speed on a string",
            goal="define a protocol Pace with method speed, use extend-type to attach it to String type, then call speed on a string"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-13 — this-style vs fn-style
G8_13 = SubjectCurriculum(
    grade=8, subject_id="G8-13",
    subject_title="this-style vs fn-style",
    fable="tortoise-hare",
    examples=[
        # The first arg is conventionally `this` in protocol method
        # bodies — illustrate by capturing the field via this.
        _ex("(do (defprotocol Named (name-of [this]))"
            " (defrecord Hare [n] Named (name-of [this] (:n this)))"
            " (name-of (->Hare \"Zephyr\")))",
            "Zephyr",
            "using this to access a field in a protocol method",
            "the value returned after defining protocol Named with method name-of, defining record Hare with field n that uses this to access the field in the implementation, then calling name-of on a Hare instance",
            goal="define a protocol Named with method name-of, define a record that uses this to access a field, then call the method"),
        _ex("(do (defprotocol Tagged (tag-of [this]))"
            " (defrecord Stone [t] Tagged (tag-of [this] (:t this)))"
            " (tag-of (->Stone :grey)))",
            ":grey",
            "using this to access a field in a protocol method",
            "the value returned after defining protocol Tagged with method tag-of, defining record Stone with field t that uses this to access the field in the implementation, then calling tag-of on a Stone instance",
            goal="define a protocol Tagged with method tag-of, define a record Stone that implements it by accessing a field via this, then call the method"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-14 — No protocol inheritance
G8_14 = SubjectCurriculum(
    grade=8, subject_id="G8-14",
    subject_title="Protocols don't inherit",
    fable="tortoise-hare",
    examples=[
        # We illustrate the single-protocol-only nature: each protocol
        # is its own dispatching surface.
        _ex("(do (defprotocol A (a-op [this]))"
            " (defprotocol B (b-op [this]))"
            " (extend-protocol A java.lang.String (a-op [_] :a-impl))"
            " (extend-protocol B java.lang.String (b-op [_] :b-impl))"
            " [(a-op \"x\") (b-op \"x\")])",
            [":a-impl", ":b-impl"],
            "calling methods from two independent protocols",
            "the vector of results after defining protocols A and B with methods a-op and b-op, extending both to String independently, then calling both methods on the string \"x\"",
            goal="define two protocols A and B, each with a method, extend both to String type independently, then call both methods"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-15 — derive / isa
G8_15 = SubjectCurriculum(
    grade=8, subject_id="G8-15",
    subject_title="derive and isa? — multimethod hierarchy",
    fable="tortoise-hare",
    examples=[
        _ex("(do (derive ::hare ::runner) (isa? ::hare ::runner))",
            True,
            "checking type hierarchy after derive",
            "whether the relationship holds after establishing with derive that ::hare is a type of ::runner, then checking with isa?",
            goal="establish a type relationship where ::hare is a type of ::runner, then check it"),
        _ex("(isa? java.lang.Long java.lang.Number)",
            True,
            "checking Java type hierarchy",
            "whether Long is a type of Number in Java's type hierarchy",
            goal="check whether Long is a type of Number in Java's type system"),
        _ex("(isa? java.lang.String java.lang.Number)",
            False,
            "checking Java type hierarchy",
            "whether String is a type of Number in Java's type hierarchy",
            goal="check whether String is a type of Number in Java's type system"),
    ],
    subplots=_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-16 — Abstract design with protocols
G8_16 = SubjectCurriculum(
    grade=8, subject_id="G8-16",
    subject_title="Abstract design with protocols",
    fable="tortoise-hare",
    examples=[
        # A small "many implementations behind one protocol" example.
        _ex("(do (defprotocol Move (step [this]))"
            " (defrecord Hare [] Move (step [_] :leap))"
            " (defrecord Tortoise [] Move (step [_] :plod))"
            " (mapv step [(->Hare) (->Tortoise)]))",
            [":leap", ":plod"],
            "calling a polymorphic method on multiple record types",
            "the vector of results after defining protocol Move with method step, defining records Hare and Tortoise that both implement Move, then calling step via mapv on both instances",
            goal="define a protocol Move with method step, define two record types Hare and Tortoise that each implement it, then call the method on both instances"),
        _ex("(do (defprotocol Sound (cry [this]))"
            " (defrecord Hare [] Sound (cry [_] :thump))"
            " (defrecord Tortoise [] Sound (cry [_] :hiss))"
            " (cry (->Tortoise)))",
            ":hiss",
            "calling a polymorphic method on a record instance",
            "the value returned after defining protocol Sound with method cry, defining records Hare and Tortoise that both implement Sound, then calling cry on a Tortoise instance",
            goal="define a protocol Sound with method cry, define two record types that implement it, then call the method on a Tortoise instance"),
    ],
    subplots=_SUBPLOTS,
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
    print(f"grade-8 tortoise-hare smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
