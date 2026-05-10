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
from mmllm.aesop.curriculum.boy_wolf._goals import GOALS, get_goal


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
        goal_text=goal if goal is not None else get_goal(form, concept, what),
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
            "the form that defines speak via cond",
            scenario=(
                "Carol had called a meeting of the shepherds' fellowship "
                "on the watchhouse green — sheep-shepherd, goat-shepherd, "
                "geese-keeper, all gathered. Each kind of keeper had "
                "their own way of raising an alarm: a horn, a bell, a "
                "smoke-signal."
            ),
            need=(
                "The fellowship needed a single named call — `speak` — "
                "that any keeper could be asked. Each kind of keeper "
                "would answer in their own way, but the call would mean "
                "the same thing to all of them."
            ),
                mapping=(
                "Polymorphism by `cond` is the fellowship pattern in "
                "miniature: one named function, many internal arms — "
                "one for each kind of caller. The runtime checks the "
                "tag and runs the matching arm; the call site doesn't "
                "have to know which keeper showed up."
            ),
            resolution=(
                'the function was posted to the fellowship roll — a single name the watchhouse could call, with each kind of keeper answering in their own honest voice.'
            )),
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
            "the color field of a Lantern instance",
            scenario=(
                "Carol had ordered a small wooden tally-box from the "
                "village cooper — pigeon-holes inside for tallying "
                "different kinds of equipment. The first kind to track "
                "was lanterns, with one slot per box for the lantern's "
                "color."
            ),
            need=(
                "The village wanted a uniform tally-box shape so any "
                "shepherd could lift the lid, find the same labeled "
                "slots in the same order, and read off the values "
                "without having to learn each box's quirks."
            ),
                mapping=(
                "`deftype` is the cooper's plan for a tally-box: a name "
                "and a list of labeled slots. `Lantern.` constructs an "
                "instance with values in those slots; `.-color` reaches "
                "into the slot named `color` and reads it back."
            ),
            resolution=(
                "the tally-box yielded the lantern's color cleanly — the cooper's plan and the townsfolk's uniform readout, exactly as designed."
            )),
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
            "the :post value of the Watcher record",
            scenario=(
                "Carol had ordered a tally-box for tracking village "
                "watchers. Each watcher wore a name tag and carried a "
                "badge marking their post — hilltop, fold, village-gate, "
                "each name paired with a post."
            ),
            need=(
                "The village needed a box shape that held both the "
                "watcher's name and their assigned post, in a fixed order, "
                "so any shepherd could read it the same way."
            ),
            mapping=(
                "`defrecord` is the box blueprint: a name and a list of "
                "field names. The constructor `->Watcher` fills the fields; "
                "keyword lookup like `:post` reaches into the box and reads "
                "that slot back."
            ),
            resolution=(
                "the tally-box gave up the watcher's post cleanly — the record's shape meant every reader found the same slot in the same place."
            )),
        _ex("(do (defrecord Watcher [name post]) (:name (->Watcher \"elder\" :village)))",
            "elder",
            "the :name field of a Watcher record",
            "the :name value of the Watcher constructed with \"elder\"",
            scenario=(
                "At the fold's record-shelf, Tom kept tally-boxes for "
                "each watcher: a box for an elder at the village-gate, "
                "another for a careful shepherd at the hilltop."
            ),
            need=(
                "To know who was watching, Tom needed to read the name "
                "field from each box in the same way — a uniform shape "
                "meant no guessing."
            ),
            mapping=(
                "The record holds both name and post; `:name` is the "
                "keyword that reads the name slot. The constructor puts "
                "values in order; the lookup fetches by the slot label."
            ),
            resolution=(
                'the name came back correctly — "elder" — exactly as it was written into the box\'s name slot.'
            )),
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
            "whether the Alarm protocol was defined (a non-nil truthy value)",
            scenario=(
                "At the shepherds' fellowship meeting, Carol announced "
                "that all keepers must pledge to answer the named call "
                "\"Alarm\" with their own honest method — a horn, a bell, "
                "smoke. The pledge was posted on the board."
            ),
            need=(
                "The fellowship needed to declare a contract — a single "
                "named call that each kind of keeper could implement their "
                "own way, no matter their tool."
            ),
            mapping=(
                "`defprotocol` posts the named call and its signature "
                "(here, `sound` takes `this`). It doesn't say what the "
                "method does — just that it exists, and any keeper who "
                "implements it must have a `sound` method."
            ),
            resolution=(
                "the Alarm protocol was posted and established — a non-nil truthy value confirming the fellowship's pledge was written."
            )),
        _ex("(do (defprotocol Greet (hail [this])) (some? Greet))",
            True,
            "a defprotocol Greet with one method hail",
            "whether Greet has been established",
            scenario=(
                "Carol drafted a new rule for the watchers: a greeting "
                "protocol so any watchkeeper could greet a visitor their "
                "own way — formal, friendly, or stern."
            ),
            need=(
                "The rule had to declare the call `hail` as a method any "
                "watcher could implement. The rule itself was just a "
                "promise, not the implementations."
            ),
            mapping=(
                "Like a drill-card pinned to the watchhouse wall, "
                "`defprotocol Greet` announces the named method signature. "
                "It says 'hail exists' without saying what each keeper does."
            ),
            resolution=(
                'the protocol was posted and truthy — the contract was established, waiting for keepers to pledge their own honest greeting.'
            )),
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
            "what sound returns when applied to \"wolf\"",
            scenario=(
                "The fellowship had posted the Alarm protocol. Tom, a "
                "shepherd keeper, stepped forward to pledge his way: the "
                "word \"wolf\" would trigger the sound \"howl\" — his "
                "honest alarm."
            ),
            need=(
                "The Alarm protocol needed real implementations. Tom's "
                "pledge said: when the keepers' fellowship asks \"Alarm\", "
                "I, a String word-keeper, will answer with my sound."
            ),
            mapping=(
                "`extend-protocol` adds Tom's implementation to the "
                "Alarm fellowship for the String type. When `sound` is "
                "called on a String, Tom's method runs and returns the "
                "sound. The `cond`-like dispatch picks Tom."
            ),
            resolution=(
                'Tom\'s pledge was recorded. When the shepherds called `sound "wolf"`, the fellowship matched String and ran Tom\'s honest cry: "howl".'
            )),
        _ex("(do (defprotocol Greet (hail [this]))"
            " (extend-protocol Greet java.lang.Long (hail [_] :number))"
            " (hail 7))",
            ":number",
            "a Greet protocol extended to Long, then call hail on 7",
            "the keyword hail returns for the number 7",
            scenario=(
                "Carol had posted a Greet protocol at the fold-gate. A "
                "number-keeper — a tender of the tally-sticks — offered "
                "their pledge: any number greeting would return the keyword "
                "`:number`."
            ),
            need=(
                "The Greet protocol needed an implementation for numbers. "
                "The number-keeper's honest way was to reply with their own "
                "kind of greeting."
            ),
            mapping=(
                "`extend-protocol Greet java.lang.Long` adds the "
                "number-keeper's implementation. Now when `hail` is called "
                "on a Long like 7, the fellowship knows to ask the "
                "number-keeper's method, and the verdict is `:number`."
            ),
            resolution=(
                "the number-keeper's pledge was recorded, and the fellowship's dispatch routed `hail 7` to them, returning their honest greeting: `:number`."
            )),
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
            "the keyword sound returns for the integer 42",
            scenario=(
                "At the fellowship meeting, both the word-keeper and the "
                "number-keeper had pledged their Alarm implementations. "
                "Tom, testing the system, called the sound on the number "
                "42 and waited to see which keeper answered."
            ),
            need=(
                "The Alarm protocol needed to pick the right keeper based "
                "on what kind of thing was calling — a number gets the "
                "number-keeper's implementation, a word gets the "
                "word-keeper's."
            ),
            mapping=(
                "The protocol dispatch reads the type of the argument and "
                "routes to the matching extended implementation. `42` is a "
                "Long, so the `java.lang.Long` arm runs, returning the "
                "long-keeper's verdict."
            ),
            resolution=(
                "the fellowship read the type, routed to the right keeper, and returned the long-keeper's honest alarm — the verdict."
            )),
        _ex("(do (defprotocol Alarm (sound [this]))"
            " (extend-protocol Alarm"
            "   java.lang.String (sound [_] :string-alarm)"
            "   java.lang.Long   (sound [_] :long-alarm))"
            " (sound \"x\"))",
            ":string-alarm",
            "Alarm dispatched on a string argument",
            "the keyword sound returns for the string \"x\"",
            scenario=(
                "The same fellowship, same protocol, now called sound on "
                "the word \"x\" instead. The fellowship had to pick the "
                "other keeper this time."
            ),
            need=(
                "The protocol dispatch had to be smart enough to check the "
                "incoming type: word gets word-keeper, number gets "
                "number-keeper."
            ),
            mapping=(
                "`sound \"x\"` passes a String, so the dispatch picks the "
                "`java.lang.String` arm, running the word-keeper's "
                "implementation."
            ),
            resolution=(
                'the fellowship routed to the word-keeper, and their honest alarm came back — the string-alarm verdict.'           )),
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
            "the keyword sound returns for a Shepherd record",
            scenario=(
                "Carol defined a tally-box shape called Shepherd — a box "
                "with a name slot. She also declared: any Shepherd box "
                "that lives in the world must implement the Alarm protocol "
                "with its own honest sound."
            ),
            need=(
                "The village wanted a shape — Shepherd — and a promise "
                "that every Shepherd, when asked to sound the alarm, would "
                "answer with a cry. The record held the data; the "
                "protocol held the behavior."
            ),
            mapping=(
                "`defrecord Shepherd [name] Alarm (sound [_] :cry)` is "
                "both: the box shape and the implementation in one. When "
                "a Shepherd instance is asked to sound, the protocol "
                "routes to `:cry`."
            ),
            resolution=(
                'the tally-box was born and registered — a Shepherd instance could now answer the Alarm call with its own honest sound.'
            )),
        _ex("(do (defprotocol Alarm (sound [this]))"
            " (defrecord Elder [name] Alarm (sound [_] :measured))"
            " (sound (->Elder \"Mira\")))",
            ":measured",
            "an Elder record implementing Alarm with sound -> :measured",
            "the keyword sound returns for an Elder record",
            scenario=(
                "Carol designed another tally-box shape: Elder, with a "
                "name slot. She declared: Elder boxes also implement "
                "Alarm, but with their own measured sound — not a cry, but "
                "a careful answer."
            ),
            need=(
                "Two kinds of people, two kinds of boxes — Shepherd and "
                "Elder. Both must answer Alarm, but each with their own "
                "honest way. The record defines the shape; the protocol "
                "method defines the answer."
            ),
            mapping=(
                "`defrecord Elder [name] Alarm (sound [_] :measured)` "
                "defines both shape and behavior. The Elder box will sound "
                "with `:measured`, not a cry."
            ),
            resolution=(
                'the Elder box was made and pledged. When asked to sound, it returns its honest, measured answer — the verdict.'           )),
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
            "what reply returns for {:role :shepherd}",
            scenario=(
                "At the fold-gate, Carol had set up a brand-sorting "
                "gate. Each animal that arrived wore a brand on its ear "
                "— `:shepherd` for the meadow folk's working sheep, "
                "`:lantern-bearer` for the night-watch goats — and the "
                "gate routed each to the right pen."
            ),
            need=(
                "Tom needed a uniform call — `reply` — that worked for "
                "any branded animal, with the gate doing the routing. "
                "Branding was the dispatch key; the right pen was the "
                "method."
            ),
                mapping=(
                "`defmulti` posts the dispatch rule (here, look at "
                "`:role` on the arriving map) and `defmethod` registers "
                "what to do for each brand. The gate reads the brand "
                "and routes to the matching method."
            ),
            resolution=(
                'the gate read the brand, called the right method, and the runtime returned the verdict — `:cry` for the shepherd-branded entry — the routing complete.'           )),
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
            "what reply returns for {:role :elder}",
            scenario=(
                "At the fold-gate, Carol had posted a brand-sorting rule "
                "called `reply`. It read the `:role` brand and routed each "
                "branded animal to the right pen. Two shepherds had arrived "
                "— one marked `:shepherd`, one marked `:elder`."
            ),
            need=(
                "The gate needed multiple methods so each role got its own "
                "answer. The `:shepherd` pen and the `:elder` pen held "
                "different routines — a cry versus a measured response."
            ),
            mapping=(
                "`defmulti` posts the dispatcher; `defmethod` registers "
                "each implementation. The gate reads the `:role` brand and "
                "routes to the matching method."
            ),
            resolution=(
                'the gate read `:elder`, routed to the second method, and returned the verdict: `:measured`.'
            )),
        _ex("(do (defmulti reply :role)"
            " (defmethod reply :shepherd [_] :cry)"
            " (defmethod reply :elder    [_] :measured)"
            " (defmethod reply :default  [_] :unknown)"
            " (reply {:role :stranger}))",
            ":unknown",
            "a :default fallback method on reply, called with an unknown role",
            "what reply returns for {:role :stranger} when :default falls through",
            scenario=(
                "The fold-gate had two pens ready — one for `:shepherd`, "
                "one for `:elder`. Then a stranger arrived with a brand "
                "the gate had never seen: `:stranger`. Carol had posted a "
                "`:default` pen as a catch-all."
            ),
            need=(
                "The gate needed a fallback for unexpected brands. Any "
                "animal that didn't match `:shepherd` or `:elder` would "
                "fall through to `:default` and get the unknown verdict."
            ),
            mapping=(
                "When `reply` receives a map with an unrecognized `:role`, "
                "the dispatcher tries the registered methods in order. "
                "Finding none, it uses the `:default` method as the catch-all."
            ),
            resolution=(
                'the gate found no match for `:stranger`, fell through to `:default`, and returned the verdict: `:unknown`.'
            )),
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
            "the string show returns for :wolf",
            scenario=(
                "Tom was testing two ways to build a dispatch gate at the "
                "fold. The first way: a brand-sorting gate that read the "
                "incoming value itself as the brand."
            ),
            need=(
                "Tom wanted a gate that could route based on what the "
                "caller sent — a `:wolf` keyword would get one answer, "
                "something else would get another."
            ),
            mapping=(
                "`defmulti show identity` tells the gate to read the "
                "incoming value as the dispatch key. `:wolf` becomes the "
                "brand; the matching `defmethod` runs."
            ),
            resolution=(
                'the gate read `:wolf`, routed to the matching method, and returned the verdict: "howl".'
            )),
        _ex("(do (defprotocol Show (show [this]))"
            " (extend-protocol Show java.lang.String (show [s] (str \"str-\" s)))"
            " (show \"wolf\"))",
            "str-wolf",
            "a Show protocol extended to String, called with \"wolf\"",
            "the string show returns for \"wolf\" via protocol",
            scenario=(
                "Carol preferred the second way: a fellowship protocol. "
                "Instead of a gate that reads the value itself, she posted "
                "a named call that any type could answer in its own way."
            ),
            need=(
                "Carol wanted a protocol where any String could implement "
                "its own honest show method, without having to list every "
                "possible String in advance."
            ),
            mapping=(
                "`defprotocol Show` is the fellowship pledge; "
                "`extend-protocol` adds the String keeper's implementation. "
                "The dispatch reads the type of the argument, not the value."
            ),
            resolution=(
                'the protocol routed to the String keeper, who returned the verdict: "str-wolf" — the value with the keeper\'s honest prefix.'
            )),
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
            "the keyword raise returns for \"wolf\" via the protocol",
            scenario=(
                "Carol was explaining to the shepherds' fellowship that "
                "Clojure had its own way to write the same kind of contract "
                "that other villages used Java interfaces for. The "
                "fellowship could pledge to `IAlarm` just as truly."
            ),
            need=(
                "The village wanted to know that a protocol was just as "
                "binding as an interface — a way to declare that any String "
                "must have an `raise` method."
            ),
            mapping=(
                "`defprotocol IAlarm` is Clojure's way of saying what a "
                "Java interface says: here's a contract. "
                "`extend-protocol` binds the String keeper to that "
                "contract, just as a class would implement an interface."
            ),
            resolution=(
                'the fellowship saw that the protocol was as solid as any Java contract. When `raise` was called on "wolf", the String keeper answered with the verdict: `:raised`.'
            )),
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
            "the keyword sound returns for 5",
            scenario=(
                "Carol had declared the Alarm protocol. Now she used a "
                "different tool — `extend-type` — to teach the number 5 "
                "and all its kind (Long) how to answer the call."
            ),
            need=(
                "Built-in types like Long couldn't be redefined with "
                "`defrecord`. Carol needed a way to add the Alarm behavior "
                "to numbers without redefining them."
            ),
            mapping=(
                "`extend-type java.lang.Long Alarm` grafts the protocol "
                "onto the built-in type. It's like saying: all Longs now "
                "pledge to Alarm, with this honest method."
            ),
            resolution=(
                "the number 5 was taught the Alarm protocol. When asked to sound, it returned the number-keeper's verdict: `:number-alarm`."
            )),
        _ex("(do (defprotocol Alarm (sound [this]))"
            " (extend-type java.lang.String Alarm (sound [_] :string-alarm))"
            " (sound \"wolf\"))",
            ":string-alarm",
            "extend-type attaching Alarm to String",
            "the keyword sound returns for \"wolf\" via extend-type",
            scenario=(
                "Carol used the same `extend-type` tool for String. The "
                "word \"wolf\" and all strings like it could now answer "
                "Alarm."
            ),
            need=(
                "Strings are built-in; Carol couldn't redefine them. She "
                "needed to add the Alarm protocol to them without touching "
                "their core definition."
            ),
            mapping=(
                "`extend-type java.lang.String Alarm` patches the "
                "protocol onto strings. The word \"wolf\" becomes a pledge "
                "to the Alarm fellowship."
            ),
            resolution=(
                'the string "wolf" answered Alarm with its honest voice — the verdict: `:string-alarm`.'
            )),
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
            "the name returned by name-of for a Shepherd record",
            scenario=(
                "Carol had a Shepherd tally-box with a name slot. When she "
                "asked the box to tell her its name via the `name-of` "
                "method, the box could refer to itself as `this` and pull "
                "its own name out."
            ),
            need=(
                "A protocol method needs to read data from the object it "
                "lives in. The convention is to call the object `this` so "
                "the method can ask `:n this` and get the name field back."
            ),
            mapping=(
                "`(name-of [this] (:n this))` is the method body: it takes "
                "`this` as the Shepherd box and returns `:n` — the "
                "name-slot value."
            ),
            resolution=(
                'the Shepherd box answered with its own honest name — "Pip" — read from its slot by `this`.'           )),
        _ex("(do (defprotocol Tagged (tag-of [this]))"
            " (defrecord Lantern [t] Tagged (tag-of [this] (:t this)))"
            " (tag-of (->Lantern :amber)))",
            ":amber",
            "a Tagged protocol method that pulls :t off this",
            "the :t value via tag-of for a Lantern",
            scenario=(
                "Carol had a Lantern tally-box with a tag slot (:amber, "
                ":red, etc.). The box's `tag-of` method used `this` to "
                "read its own tag."
            ),
            need=(
                "The protocol method needed to access the Lantern box's "
                "internal data. Using `this` as a convention made it clear "
                "that we're asking the box for its own slot."
            ),
            mapping=(
                "`(tag-of [this] (:t this))` reads the `:t` slot from "
                "`this` — the Lantern box calling the method."
            ),
            resolution=(
                'the Lantern returned its tag — the verdict: `:amber`, read directly from its own slot via `this`.'
            )),
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
            "the pair [a-op b-op] when each protocol is used independently",
            scenario=(
                "Carol had established two separate protocols for different kinds of work."
            ),
            need=(
                "Protocols don't inherit or chain — each is independent."
            ),
            mapping=(
                "`extend-protocol` adds pledges independently to a type."
            ),
            resolution=(
                'Each protocol routed to its own method independently.'
            )),
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
            "whether ::shepherd isa? ::villager after derive",
            scenario=(
                "Carol was building a hierarchy of roles at the townsfolk. "
                "She declared that a shepherd was a kind of villager — all "
                "shepherds counted as villagers for certain rules."
            ),
            need=(
                "The multimethod dispatch needed to know family trees. If a "
                "method was written for `:villager`, it should also apply to "
                "`:shepherd` — a more specific kind."
            ),
            mapping=(
                "`derive` declares the relationship; `isa?` tests it. After "
                "`(derive ::shepherd ::villager)`, the check `(isa? "
                "::shepherd ::villager)` returns true — shepherd is a "
                "villager."
            ),
            resolution=(
                'the hierarchy was posted. The verdict confirmed that a shepherd now counted as a villager for dispatch purposes.'
            )),
        _ex("(isa? java.lang.Long java.lang.Number)",
            True,
            "the predicate (isa? Long Number)",
            "whether Long isa? Number",
            scenario=(
                "Carol was teaching the valley that Java's own type system "
                "had hierarchies built in. A Long (whole number) was a kind "
                "of Number."
            ),
            need=(
                "The multimethod needed to know that built-in Java types "
                "also had family trees. Long is always a kind of Number in "
                "Java."
            ),
            mapping=(
                "`isa?` checks the relationship. Java already knows the built-in type hierarchy."
            ),
            resolution=(
                'the verdict confirmed the hierarchy: Long is indeed a kind of Number.'
            )),
        _ex("(isa? java.lang.String java.lang.Number)",
            False,
            "the predicate (isa? String Number)",
            "whether String isa? Number",
            scenario=(
                "Tom asked whether a String was also a kind of Number. Carol "
                "said no — they're unrelated types in Java's hierarchy."
            ),
            need=(
                "Dispatch needed to know when types are not related, so that "
                "a method written for Number wouldn't accidentally match "
                "Strings."
            ),
            mapping=(
                "`isa?` checks whether String is-a Number. Java says no — "
                "they're independent type families."
            ),
            resolution=(
                'the verdict came back false: String and Number are not related in the hierarchy.'
            )),
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
            "the pair of look results for a Shepherd and an Elder",
            scenario=(
                "Carol designed a Watch protocol that any watcher could "
                "implement. Two kinds of watchers showed up: Shepherd boxes "
                "and Elder boxes, each with their own honest watch-method."
            ),
            need=(
                "The village needed one named call — `look` — that worked "
                "for any watcher, each answering their own way. A Shepherd "
                "scans the whole pasture; an Elder verifies one spot."
            ),
            mapping=(
                "The protocol declares the contract; `defrecord` binds two "
                "implementations to it. `mapv look` applies the call to a "
                "list of watchers, and each gives their own honest answer."
            ),
            resolution=(
                'both watchers answered the `look` call in their own voices: the Shepherd with `:scan`, the Elder with `:verify` — polymorphism working as designed.'
            )),
        _ex("(do (defprotocol Sound (cry [this]))"
            " (defrecord Shepherd [] Sound (cry [_] :alarm))"
            " (defrecord Elder [] Sound (cry [_] :calm))"
            " (cry (->Elder)))",
            ":calm",
            "a Sound protocol with two implementations, called on an Elder",
            "the keyword cry returns for an Elder",
            scenario=(
                "Carol had a Sound protocol. Shepherds cried out alarms when "
                "danger came; Elders stayed calm and measured. Two tally-boxes, "
                "two pledges."
            ),
            need=(
                "One named method `cry` that both kinds answered, but each "
                "with their own nature: the Shepherd alarmed, the Elder "
                "composed."
            ),
            mapping=(
                "The Sound protocol is the fellowship's pledge. Both "
                "Shepherd and Elder records implement it with their own "
                "honest methods. When `cry` is called on an Elder, the "
                "protocol routes to Elder's method."
            ),
            resolution=(
                "the Elder answered with its own measured verdict: `:calm` — the honest response of an elder's voice."
            )),
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
