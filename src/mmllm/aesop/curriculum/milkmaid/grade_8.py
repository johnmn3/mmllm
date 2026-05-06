"""Grade 8 — protocols, multimethods, abstraction. through the milkmaid fable.

The fable's moral dynamic — Milkmaid's vanity vs Farmer's steadiness —
maps cleanly onto polymorphism: different species respond to the same
call differently. Milkmaid boasts that "everyone runs the same way";
Farmer insists each kind of creature has its own implementation.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.milkmaid.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.milkmaid._metaphor_pools import (
    _CARRYINGCASE_SUBPLOTS, _GUILD_SUBPLOTS, _SORTINGTABLE_SUBPLOTS,
)


# ─────────────────────── grade-8 subplot extensions ───────────────────────
#
# Polymorphism is naturally about "the same call producing different
# results for different types of creatures." We extend the shared pool
# with two beats that lean into that — a meeting-of-species and a
# protocol-as-decree.

_SUBPLOTS: list[SubplotTemplate] = _GOAL_SUBPLOTS


def _ex(form, expected, concept, what, goal=""):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what,
                          goal_text=goal)


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
    fable="milkmaid",
    examples=[
        # Without protocols, conditional dispatch on a type tag is the
        # rough equivalent. We illustrate "many shapes, one operation."
        SubjectExample(
            form="(defn speak [k] (cond (= k :hare) \"swift\" (= k :tortoise) \"steady\" :else \"silent\"))",
            expected=None,
            concept_phrase="conditional dispatch on a tag",
            question_what="the function definition",
            goal_text="define a function speak that returns different strings depending on whether its argument is :hare or :tortoise",
        ),
        SubjectExample(
            form="(let [speak (fn [k] (cond (= k :hare) \"swift\" (= k :tortoise) \"steady\"))] (speak :tortoise))",
            expected="steady",
            concept_phrase="the result of dispatching speak on :tortoise",
            question_what="the value returned",
            goal_text="call speak with :tortoise to see what it returns when dispatched",
            scenario=(
                "At the dairy guild, the guild-master had a single window for all "
                "comers. She called out to each farmer in turn: 'What is your pace?' "
                "The hare's guild-card answered one way; the tortoise's answered "
                "another."
            ),
            need=(
                "The farmer needed a single dispatch window — one function name, "
                "`speak`, that routed each caller to the right answer based on their "
                "guild-card stamp."
            ),
            mapping=(
                "The `cond` dispatch is the guild roll-call: it reads the caller's "
                "stamp in order, tests each case, and returns the paired answer when "
                "the stamp matches. No caller walks through the wrong door."
            ),
            resolution=(
                "the REPL returned the answer belonging to the tortoise's guild-card "
                "— the dispatch had routed correctly to the right paired keyword."
            ),
            tags=("story",),
        ),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-02 — deftype
G8_02 = SubjectCurriculum(
    grade=8, subject_id="G8-02",
    subject_title="deftype introduction",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(do (deftype Pebble [color]) (.-color (Pebble. \"grey\")))",
            expected="grey",
            concept_phrase="reading the color field of a Pebble instance",
            question_what="the color field value after defining a type Pebble with one field color, then constructing an instance and reading the field",
            goal_text="define a type Pebble with a color field and then read the color field from an instance",
            scenario=(
                "The farmer designed a custom pail called Pebble — a single-slot "
                "container meant to carry one attribute, color, to market. She then "
                "hammered a Pebble pail into shape and filled the color slot."
            ),
            need=(
                "She needed to define the pail's shape (`deftype Pebble [color]`), "
                "build a concrete pail, then read back what was in the color slot "
                "— not guess what she put in."
            ),
            mapping=(
                "`deftype` is the pail mold: it names the container and its labeled "
                "slot. `Pebble.` stamps the mold into a real pail. `.-color` is the "
                "slot-reader that reaches in and retrieves the value."
            ),
            resolution=(
                "the REPL handed back the contents of the color slot — exactly what "
                "the farmer had placed there when she hammered the pail."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (deftype Stone [weight]) (.-weight (Stone. 7)))",
            expected=7,
            concept_phrase="reading the weight field of a Stone instance",
            question_what="the weight field value after defining a type Stone with one field weight, then constructing an instance and reading the field",
            goal_text="define a type Stone with a weight field and then read the weight field from an instance",
        ),
    ],
    subplots=_CARRYINGCASE_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-03 — defrecord
G8_03 = SubjectCurriculum(
    grade=8, subject_id="G8-03",
    subject_title="defrecord introduction",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form='(do (defrecord Runner [name pace]) (:pace (->Runner "Alice" :slow)))',
            expected=":slow",
            concept_phrase="reading the pace compartment of a Runner case",
            question_what="the value in the pace compartment of a freshly-built Runner case for Alice",
            goal_text="define a Runner case with two named compartments, name and pace; build a Runner case for Alice with a deliberate-pace keyword; then read the pace compartment",
        ),
        SubjectExample(
            form="(do (defrecord Runner [name pace]) (:name (->Runner \"Bob\" :moderate)))",
            expected="Bob",
            concept_phrase="reading the name compartment of a Runner case",
            question_what="the name field value after defining a record Runner with two fields name and pace, then creating an instance and reading the name field",
            goal_text="define a record type named Runner with two fields, then retrieve another field from an instance",
        ),
    ],
    subplots=_CARRYINGCASE_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-04 — defprotocol
G8_04 = SubjectCurriculum(
    grade=8, subject_id="G8-04",
    subject_title="Protocol definition",
    fable="milkmaid",
    examples=[
        # Defining a protocol returns the protocol var; we use an
        # ancillary call that demonstrates it was defined.
        SubjectExample(
            form="(do (defprotocol Pace (speed [this])) (some? Pace))",
            expected=True,
            concept_phrase="a protocol definition",
            question_what="whether the Runners' guild named Pace is real after the founding",
            goal_text="found a Runners' guild named Pace whose only requirement is a method speed taking the runner as its single argument; then check whether the guild's name is now a real thing in the runtime",
        ),
        SubjectExample(
            form="(do (defprotocol Greet (hail [this])) (some? Greet))",
            expected=True,
            concept_phrase="a protocol definition",
            question_what="whether the protocol var Greet is truthy after defining a protocol named Greet with one method hail taking a single argument this",
            goal_text="define a protocol named Greet with one method hail that takes a single argument this",
        ),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-05 — extend-protocol
G8_05 = SubjectCurriculum(
    grade=8, subject_id="G8-05",
    subject_title="Protocol extension",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form=("(do (defprotocol Pace (speed [this]))"
                  " (extend-protocol Pace java.lang.String (speed [_] \"swift\"))"
                  " (speed \"hare\"))"),
            expected="swift",
            concept_phrase="calling a protocol method on a string",
            question_what="the value returned after defining protocol Pace with method speed, extending it to String with an implementation, then calling speed on a string",
            goal_text="define a protocol named Pace with one method speed, extend it to String type with an implementation, then call speed on a string",
        ),
        SubjectExample(
            form=("(do (defprotocol Greet (hail [this]))"
                  " (extend-protocol Greet java.lang.Long (hail [_] :number))"
                  " (hail 7))"),
            expected=":number",
            concept_phrase="calling a protocol method on a number",
            question_what="the value returned after defining protocol Greet with method hail, extending it to Long with an implementation, then calling hail on a number",
            goal_text="define a protocol named Greet with one method hail, extend it to Long type with an implementation, then call hail on a number",
        ),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-06 — Protocol method dispatch
G8_06 = SubjectCurriculum(
    grade=8, subject_id="G8-06",
    subject_title="Protocol method dispatch",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form=("(do (defprotocol Pace (speed [this]))"
                  " (extend-protocol Pace"
                  "   java.lang.String (speed [_] :string-pace)"
                  "   java.lang.Long   (speed [_] :long-pace))"
                  " (speed 42))"),
            expected=":long-pace",
            concept_phrase="protocol dispatch on an integer",
            question_what="the value returned after defining protocol Pace with method speed, extending it to both String and Long types with different implementations, then calling speed on the number 42",
            goal_text="define a protocol Pace with method speed, extend it to both String and Long types with different implementations, then call speed on the number 42",
        ),
        SubjectExample(
            form=("(do (defprotocol Pace (speed [this]))"
                  " (extend-protocol Pace"
                  "   java.lang.String (speed [_] :string-pace)"
                  "   java.lang.Long   (speed [_] :long-pace))"
                  " (speed \"x\"))"),
            expected=":string-pace",
            concept_phrase="protocol dispatch on a string",
            question_what="the value returned after defining protocol Pace with method speed, extending it to both String and Long types with different implementations, then calling speed on a string",
            goal_text="define a protocol Pace with method speed, extend it to both String and Long types with different implementations, then call speed on a string",
        ),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-07 — Record + Protocol
G8_07 = SubjectCurriculum(
    grade=8, subject_id="G8-07",
    subject_title="Record implementing protocol",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form=("(do (defprotocol Pace (speed [this]))"
                  " (defrecord Milkmaid [name] Pace (speed [_] :swift))"
                  " (speed (->Milkmaid \"Pip\"))"),
            expected=":swift",
            concept_phrase="calling a protocol method on a record instance",
            question_what="the value returned after defining protocol Pace with method speed, defining record Milkmaid with one field name that implements Pace, then calling speed on a Milkmaid instance",
            goal_text="define a protocol Pace with method speed, define a record Milkmaid that implements Pace, then call speed on a Milkmaid instance",
        ),
        SubjectExample(
            form=("(do (defprotocol Pace (speed [this]))"
                  " (defrecord Farmer [name] Pace (speed [_] :steady))"
                  " (speed (->Farmer \"Shelly\"))"),
            expected=":steady",
            concept_phrase="calling a protocol method on a record instance",
            question_what="the value returned after defining protocol Pace with method speed, defining record Farmer with one field name that implements Pace, then calling speed on a Farmer instance",
            goal_text="define a protocol Pace with method speed, define a record Farmer that implements Pace, then call speed on a Farmer instance",
        ),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-08 — defmulti
G8_08 = SubjectCurriculum(
    grade=8, subject_id="G8-08",
    subject_title="Multimethod defmulti",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form='(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))',
            expected=":swift",
            concept_phrase="the multimethod and its first arm",
            question_what="the pace returned for a runner stamped :hare after the table routes to its arm",
            goal_text="declare a sorting-table named pace that reads each runner's :species stamp; add an arm for the :hare stamp returning the swift-pace keyword; then route a runner stamped :hare through the table",
            scenario=(
                "The dairy had a sorting table: each pail arrived stamped with a "
                "species-tag. The table-master had a rule: read the `:species` stamp, "
                "route the pail to the correct shelf. She nailed a placard for "
                "`:hare` to one shelf."
            ),
            need=(
                "She needed to define the table's dispatch rule (`defmulti` reading "
                "`:species`) and attach one arm (`defmethod` for `:hare`), then "
                "route a stamped pail and read where it landed."
            ),
            mapping=(
                "`defmulti` carves the sorting table, naming `pace` as the router "
                "and `:species` as the stamp to read. `defmethod` pins a placard to "
                "the `:hare` shelf. Calling `pace` with a stamped map routes the "
                "pail to the matching arm."
            ),
            resolution=(
                "the REPL returned the value the `:hare` arm had posted on its shelf "
                "— the sort had routed correctly, the pail landing exactly where "
                "the placard said."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form=("(do (defmulti tag :kind)"
                  " (defmethod tag :stone [_] :hard)"
                  " (tag {:kind :stone}))"),
            expected=":hard",
            concept_phrase="calling a multimethod with a specific dispatch value",
            question_what="the value returned when multimethod tag (dispatching on :kind) routes a map with :stone",
            goal_text="define multimethod tag dispatching on :kind, add a :stone arm, then call tag with {:kind :stone}",
        ),
    ],
    subplots=_SORTINGTABLE_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-09 — defmethod
G8_09 = SubjectCurriculum(
    grade=8, subject_id="G8-09",
    subject_title="Multimethod defmethod",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form=("(do (defmulti pace :species)"
                  " (defmethod pace :hare [_] :swift)"
                  " (defmethod pace :tortoise [_] :steady)"
                  " (pace {:species :tortoise}))"),
            expected=":steady",
            concept_phrase="calling a multimethod with multiple methods",
            question_what="the value returned after defining multimethod pace that dispatches on :species with methods for both :hare and :tortoise, then calling pace with a map",
            goal_text="define a multimethod pace that dispatches on :species with methods for both :hare and :tortoise, then call pace with {:species :tortoise}",
        ),
        SubjectExample(
            form=("(do (defmulti pace :species)"
                  " (defmethod pace :hare [_] :swift)"
                  " (defmethod pace :tortoise [_] :steady)"
                  " (defmethod pace :default [_] :unknown)"
                  " (pace {:species :owl}))"),
            expected=":unknown",
            concept_phrase="calling a multimethod with a default fallback",
            question_what="the value returned after defining multimethod pace with methods for :hare, :tortoise, and :default, then calling pace with a dispatch value that doesn't match",
            goal_text="define a multimethod pace with methods for :hare and :tortoise plus a :default fallback, then call pace with a dispatch value that doesn't match",
        ),
    ],
    subplots=_SORTINGTABLE_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-10 — Multimethod vs protocol
G8_10 = SubjectCurriculum(
    grade=8, subject_id="G8-10",
    subject_title="Multimethod vs protocol",
    fable="milkmaid",
    examples=[
        # Both can implement the same dispatching idea.
        SubjectExample(
            form=("(do (defmulti show identity)"
                  " (defmethod show :rabbit [_] \"quick\")"
                  " (show :rabbit))"),
            expected="quick",
            concept_phrase="dispatching via multimethod",
            question_what="the value returned after defining multimethod show that dispatches on identity, adding a method for :rabbit, then calling show with :rabbit",
            goal_text="define a multimethod show that dispatches on identity with a method for one specific value, then call it",
        ),
        SubjectExample(
            form=("(do (defprotocol Show (show [this]))"
                  " (extend-protocol Show java.lang.String (show [s] (str \"str-\" s)))"
                  " (show \"hare\"))"),
            expected="str-hare",
            concept_phrase="dispatching via protocol",
            question_what="the value returned after defining protocol Show with method show, extending it to String with an implementation, then calling show on a string",
            goal_text="define a protocol Show with method show, extend it to String type, then call show on a string",
        ),
    ],
    subplots=_SORTINGTABLE_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-11 — Protocol vs interface
G8_11 = SubjectCurriculum(
    grade=8, subject_id="G8-11",
    subject_title="Protocol vs Java interface",
    fable="milkmaid",
    examples=[
        # We illustrate a protocol acting as the Clojure-side analog of
        # a Java interface — the same dispatching shape, but defined
        # purely in Clojure.
        SubjectExample(
            form=("(do (defprotocol IPace (run [this]))"
                  " (extend-protocol IPace java.lang.String (run [_] :ran))"
                  " (run \"hare\"))"),
            expected=":ran",
            concept_phrase="calling a protocol method on a string",
            question_what="the value returned after defining protocol IPace with method run, extending it to String with an implementation, then calling run on a string",
            goal_text="define a protocol IPace with method run, extend it to String type, then call run on a string",
        ),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-12 — extend-type
G8_12 = SubjectCurriculum(
    grade=8, subject_id="G8-12",
    subject_title="extend-type on built-in types",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form=("(do (defprotocol Pace (speed [this]))"
                  " (extend-type java.lang.Long Pace (speed [_] :number-pace))"
                  " (speed 5))"),
            expected=":number-pace",
            concept_phrase="attaching a protocol to a built-in type via extend-type",
            question_what="the value returned when speed is called on a Long after extending Long with Pace via extend-type",
            goal_text="extend Long type with Pace protocol via extend-type, then call speed on a number",
        ),
        SubjectExample(
            form=("(do (defprotocol Pace (speed [this]))"
                  " (extend-type java.lang.String Pace (speed [_] :string-pace))"
                  " (speed \"hare\"))"),
            expected=":string-pace",
            concept_phrase="attaching a protocol to a built-in type via extend-type",
            question_what="the value returned when speed is called on a String after extending String with Pace via extend-type",
            goal_text="extend String type with Pace protocol via extend-type, then call speed on a string",
        ),
    ],
    subplots=_SORTINGTABLE_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-13 — this-style vs fn-style
G8_13 = SubjectCurriculum(
    grade=8, subject_id="G8-13",
    subject_title="this-style vs fn-style",
    fable="milkmaid",
    examples=[
        # The first arg is conventionally `this` in protocol method
        # bodies — illustrate by capturing the field via this.
        SubjectExample(
            form=("(do (defprotocol Named (name-of [this]))"
                  " (defrecord Milkmaid [n] Named (name-of [this] (:n this)))"
                  " (name-of (->Milkmaid \"Zephyr\")))"),
            expected="Zephyr",
            concept_phrase="using this to access a field in a protocol method",
            question_what="the value returned after defining protocol Named with method name-of, defining record Milkmaid with field n that uses this to access the field in the implementation, then calling name-of on a Milkmaid instance",
            goal_text="define a protocol Named with method name-of, define a record that uses this to access a field, then call the method",
        ),
        SubjectExample(
            form=("(do (defprotocol Tagged (tag-of [this]))"
                  " (defrecord Stone [t] Tagged (tag-of [this] (:t this)))"
                  " (tag-of (->Stone :grey)))"),
            expected=":grey",
            concept_phrase="using this to access a field in a protocol method",
            question_what="the value returned after defining protocol Tagged with method tag-of, defining record Stone with field t that uses this to access the field in the implementation, then calling tag-of on a Stone instance",
            goal_text="define a protocol Tagged with method tag-of, define a record Stone that implements it by accessing a field via this, then call the method",
        ),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-14 — No protocol inheritance
G8_14 = SubjectCurriculum(
    grade=8, subject_id="G8-14",
    subject_title="Protocols don't inherit",
    fable="milkmaid",
    examples=[
        # We illustrate the single-protocol-only nature: each protocol
        # is its own dispatching surface.
        SubjectExample(
            form=("(do (defprotocol A (a-op [this]))"
                  " (defprotocol B (b-op [this]))"
                  " (extend-protocol A java.lang.String (a-op [_] :a-impl))"
                  " (extend-protocol B java.lang.String (b-op [_] :b-impl))"
                  " [(a-op \"x\") (b-op \"x\")])"),
            expected=[":a-impl", ":b-impl"],
            concept_phrase="calling methods from two independent protocols",
            question_what="the vector of results after defining protocols A and B with methods a-op and b-op, extending both to String independently, then calling both methods on the string \"x\"",
            goal_text="define two protocols A and B, each with a method, extend both to String type independently, then call both methods",
        ),
    ],
    subplots=_GUILD_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-15 — derive / isa
G8_15 = SubjectCurriculum(
    grade=8, subject_id="G8-15",
    subject_title="derive and isa? — multimethod hierarchy",
    fable="milkmaid",
    examples=[
        SubjectExample(
            form="(do (derive ::hare ::runner) (isa? ::hare ::runner))",
            expected=True,
            concept_phrase="checking type hierarchy after derive",
            question_what="whether the relationship holds after establishing with derive that ::hare is a type of ::runner, then checking with isa?",
            goal_text="establish a type relationship where ::hare is a type of ::runner, then check it",
        ),
        SubjectExample(
            form="(isa? java.lang.Long java.lang.Number)",
            expected=True,
            concept_phrase="checking Java type hierarchy",
            question_what="whether Long is a type of Number in Java's type hierarchy",
            goal_text="check whether Long is a type of Number in Java's type system",
        ),
        SubjectExample(
            form="(isa? java.lang.String java.lang.Number)",
            expected=False,
            concept_phrase="checking Java type hierarchy",
            question_what="whether String is a type of Number in Java's type hierarchy",
            goal_text="check whether String is a type of Number in Java's type system",
        ),
    ],
    subplots=_SORTINGTABLE_SUBPLOTS,
    plan_pool=_PLAN_POOL_G8,
)


# G8-16 — Abstract design with protocols
G8_16 = SubjectCurriculum(
    grade=8, subject_id="G8-16",
    subject_title="Abstract design with protocols",
    fable="milkmaid",
    examples=[
        # A small "many implementations behind one protocol" example.
        SubjectExample(
            form=("(do (defprotocol Move (step [this]))"
                  " (defrecord Milkmaid [] Move (step [_] :leap))"
                  " (defrecord Farmer [] Move (step [_] :plod))"
                  " (mapv step [(->Milkmaid) (->Farmer)]))"),
            expected=[":leap", ":plod"],
            concept_phrase="calling a polymorphic method on multiple record types",
            question_what="the vector of results after defining protocol Move with method step, defining records Milkmaid and Farmer that both implement Move, then calling step via mapv on both instances",
            goal_text="define a protocol Move with method step, define two record types Milkmaid and Farmer that each implement it, then call the method on both instances",
        ),
        SubjectExample(
            form=("(do (defprotocol Sound (cry [this]))"
                  " (defrecord Milkmaid [] Sound (cry [_] :thump))"
                  " (defrecord Farmer [] Sound (cry [_] :hiss))"
                  " (cry (->Farmer)))"),
            expected=":hiss",
            concept_phrase="calling a polymorphic method on a record instance",
            question_what="the value returned after defining protocol Sound with method cry, defining records Milkmaid and Farmer that both implement Sound, then calling cry on a Farmer instance",
            goal_text="define a protocol Sound with method cry, define two record types that implement it, then call the method on a Farmer instance",
        ),
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
    print(f"grade-8 tortoise-hare smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
