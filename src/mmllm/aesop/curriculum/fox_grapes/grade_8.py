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
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox had built a labeled crate at the press — its named compartments stamped at the time of construction.',
            need='Renard wanted to peek at one labelled slot without unpacking the rest of the crate.',
            mapping="`deftype` and `defrecord` declare a crate's shape. Constructing fills the slots; field-access reads one slot directly.",
            resolution='the named slot read back the value Renard had stamped at the press — fetched in one step.',
            tags=("story",)),
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
            "the :pace value of the Runner record",
            goal='define a Runner record with name and pace fields, construct one, and read its pace',
            scenario='Vix the fox had built a labeled fruit-crate at the warehouse — its named compartments stamped at the time of construction, each one carrying two fixed fields.',
            need='Vix had just packed a fresh crate with two slots, and now wanted to read back the value from one specific compartment without unpacking anything else.',
            mapping='`defrecord` declares a crate\'s shape with multiple named slots. Constructing the record fills those slots; the keyword-access form reads the value at one named compartment directly.',
            resolution='the labeled slot read back the value Vix had stamped at the warehouse — the crate\'s own field, fetched in one step.',
            tags=("story",)),
        _ex("(do (defrecord Runner [name pace]) (:name (->Runner \"specimen\" :steady)))",
            "specimen",
            "the :name field of a Runner record",
            "the :name value of a Runner constructed with a different label",
            goal='define a Runner record and access its name field from a constructed instance',
            scenario='Renard the fox had also built a labeled fruit-crate at the warehouse — this one with a name compartment and a pace compartment, both filled at packing time.',
            need='Renard wanted to peek at the name compartment of a packed crate without disturbing the pace compartment.',
            mapping='`defrecord` shapes the crate with named slots. Keyword-access by field name reads just that one compartment\'s value directly.',
            resolution='the name-slot read back the label Renard had stamped on the crate — one compartment, fetched cleanly.',
            tags=("story",)),
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
        _ex("(do (defprotocol Pace (speed [this])) (some? Pace))", True,
            'the defprotocol Pace, verified as defined',
            'whether the protocol var now exists',
            goal='define a Pace protocol and verify it was created',
            scenario='Sly the fox posted a new guild contract at the orchard gate — a written rule that any member who joined would have to sign up under. The contract named one shared operation that each member would implement in their own way.',
            need='Sly needed to confirm that the contract had been posted correctly, that the guild-rule itself was now solid and ready.',
            mapping='A protocol posts the rule name and the operation signature. Defining it stamps the protocol var into existence. Testing with some? confirms the var was created.',
            resolution='the protocol name stood ready on the guild\'s roster, its contract rule now available for any type to sign up under.',
            tags=("story",)),
        _ex("(do (defprotocol Greet (hail [this])) (some? Greet))", True,
            'a second protocol definition, verified as real',
            'whether a different protocol now exists',
            goal='define a Greet protocol and confirm it exists',
            scenario='Renard the fox posted a second contract at the market — a different rule with a different operation name, also expecting each member to respond in kind.',
            need='Renard wanted assurance that the second contract had been placed correctly and was ready for any member to sign.',
            mapping='Each protocol is its own independent guild contract. Defining it creates the protocol var. some? checks that the var is real.',
            resolution='the second guild contract now hung at the market, its rule available for any type to pledge under.',
            tags=("story",)),
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
            "what speed returns when applied to text",
            goal='define a Pace protocol for strings and call the speed operation',
            scenario='Vix the fox opened the guild to text-label types — any text-label could now sign the Pace contract and respond with its habit-word when asked.',
            need='Vix had signed up a text-label under the contract; now to call speed on that label and get back the habit-word it had promised.',
            mapping='extend-protocol registers a type (String) under the guild contract (Pace). The method defines what that type\'s answer to speed will be. Calling speed on a text now looks up the registered answer.',
            resolution='the text-label answered the speed query with its own habit-word, routed through the protocol\'s dispatch.',
            tags=("story",)),
        _ex("(do (defprotocol Greet (hail [this]))"
            " (extend-protocol Greet java.lang.Long (hail [_] :number))"
            " (hail 7))",
            ":number",
            "a Greet protocol extended to Long integers, then call hail on one",
            "what hail returns when applied to a number",
            goal='define a Greet protocol for integers and call hail',
            scenario='Renard the fox opened the guild to integer types — any whole number could now sign the Greet contract and respond with its own kind-word when greeted.',
            need='Renard had signed up a whole number under the contract; now to greet it and get back the kind-word it had pledged.',
            mapping='extend-protocol registers a type (Long) under a guild contract (Greet). The method defines that type\'s answer to hail. Calling hail on an integer routes through the protocol dispatch.',
            resolution='the integer answered the greeting with its registered kind-word, dispatched through the protocol.',
            tags=("story",)),
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
            "Pace extended to both String and Long; called with an integer",
            "the keyword speed returns when routed to the Long branch",
            goal='extend Pace to two types and call speed on an integer',
            scenario='Sly the fox had signed up both text-labels and whole numbers under the same Pace contract — but each type had promised a different habit-word when asked.',
            need='Sly called speed on a whole number and needed to know which habit-word would come back — the one the integer had promised.',
            mapping='extend-protocol registers two types under the same guild contract, each with its own habit-word. The dispatch looks at the argument\'s type and routes to the matching method. An integer goes to the Long branch.',
            resolution='the integer routed through its registered channel and returned the habit-word it had pledged for that type.',
            tags=("story",)),
        _ex("(do (defprotocol Pace (speed [this]))"
            " (extend-protocol Pace"
            "   java.lang.String (speed [_] :string-pace)"
            "   java.lang.Long   (speed [_] :long-pace))"
            " (speed \"x\"))",
            ":string-pace",
            "Pace extended to two types; called with a text string",
            "the keyword speed returns when routed to the String branch",
            goal='extend Pace to two types and call speed on text',
            scenario='Vix the fox had the same two-type guild — text-labels and whole numbers, each with their own habit-word. Now to call speed on a text-label instead.',
            need='Vix called speed on text and needed the habit-word that the text type had promised.',
            mapping='The protocol dispatch examines the argument\'s type. A text string routes to the String branch, returning its registered habit-word.',
            resolution='the text routed through its registered channel and returned the text-type\'s own habit-word.',
            tags=("story",)),
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
            "the keyword speed returns for a Hare record",
            goal='define a Hare record that implements the Pace protocol and call speed',
            scenario='Renard the fox had a labeled crate that also signed the Pace guild contract — the crate-type promised to answer the speed question with its own habit-word whenever anyone asked.',
            need='Renard had built one crate and packed it with a name; now to call speed on the crate and get back the habit-word it had pledged.',
            mapping='A record can implement a protocol directly. The protocol method speed is defined right in the record\'s body. When speed is called on a crate instance, it uses that inline method.',
            resolution='the crate answered speed with the habit-word it had inscribed in its contract — routed through the embedded protocol implementation.',
            tags=("story",)),
        _ex("(do (defprotocol Pace (speed [this]))"
            " (defrecord Creature [name] Pace (speed [_] :steady))"
            " (speed (->Creature \"Shell\")))",
            ":steady",
            "a defrecord Creature that implements Pace with a different habit-word",
            "the keyword speed returns for a Creature record",
            goal='define a different record that implements Pace and call speed',
            scenario='Vix the fox had a second labeled crate that also signed the Pace contract — but this crate promised a different habit-word, its own steady answer.',
            need='Vix had built this second crate and packed it; now to call speed and get back its habit-word.',
            mapping='A record implements the protocol; each method lives in the record\'s own body. When speed is called on this crate, it returns the habit-word this record had promised.',
            resolution='the second crate answered speed with its own inscribed habit-word, routed through its embedded protocol method.',
            tags=("story",)),
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
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox had set up a sorting-tray at the market — one channel per registered species, dispatched by tag.',
            need="Vix dropped a basket bearing one of the registered tags onto the tray, expecting the matching channel's habit-word back.",
            mapping='`defmulti` posts the tray and the dispatch rule; `defmethod` registers a channel for one tag. Calling routes through the matching channel.',
            resolution="the basket's tag routed it through its channel, and the tray returned that channel's habit-word.",
            tags=("story",)),
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
            "two defmethod entries on pace, called with :tortoise tag",
            "what pace returns for the tortoise channel",
            goal='define two defmethods and dispatch to one of them',
            scenario='Vix the fox had set up a sorting-tray at the market with two channels — one for each registered species. A basket bearing the first tag would drop into the first channel; the second tag routed to the second.',
            need='Vix dropped a basket bearing the second tag onto the tray, expecting the second channel\'s habit-word back.',
            mapping='defmulti posts the tray and the dispatch rule (:species tag). Each defmethod registers a channel for one tag. Calling pace with a tagged basket routes to the matching method.',
            resolution='the basket\'s tag routed it through the second channel, and the tray returned that channel\'s habit-word.',
            tags=("story",)),
        _ex("(do (defmulti pace :species)"
            " (defmethod pace :crow [_] :swift)"
            " (defmethod pace :badger [_] :slow)"
            " (defmethod pace :default [_] :unknown)"
            " (pace {:species :fox}))",
            ":unknown",
            "a multimethod with a default channel, called with an unregistered tag",
            "what pace returns when the tag matches no channel",
            goal='define a multimethod with a default fallback',
            scenario='Sly the fox had set up a sorting-tray at the market with three channels — two for specific species, one default channel for any tag the tray didn\'t recognize.',
            need='Sly dropped a basket bearing a tag no channel had registered for. The tray had to route it somewhere — to the default.',
            mapping='The default defmethod catches any dispatch value that no other method handles. When a tag matches no registered channel, the tray sends it to the default branch.',
            resolution='the unregistered tag routed to the default channel, returning the default habit-word.',
            tags=("story",)),
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
            "the string show returns when dispatching by the argument itself",
            goal='define a multimethod that dispatches on the argument itself',
            scenario='Renard the fox had set up a sorting-tray where the tag was the basket itself — not some field inside it, but the whole thing. A basket marked :hare would drop into the hare channel.',
            need='Renard dropped a :hare basket onto the tray, expecting the hare channel\'s answer back.',
            mapping='When the dispatch function is identity, the whole argument is the tag. The multimethod routes directly on the value itself, not on some extracted field.',
            resolution='the :hare basket routed through its channel and returned the answer the hare branch had registered.',
            tags=("story",)),
        _ex("(do (defprotocol Show (show [this]))"
            " (extend-protocol Show java.lang.String (show [s] (str \"str-\" s)))"
            " (show \"hare\"))",
            "str-hare",
            "a Show protocol extended to String, with a transformation on the argument",
            "the string show returns after prepending a prefix",
            goal='extend a protocol to String and apply a transformation',
            scenario='Sly the fox had a guild contract for Show — text-labels could sign it. When you asked show on a text-label, the guild would read the label and hand it back with a prefix written on.',
            need='Sly called show on a text-label and expected the label to come back with the prefix attached.',
            mapping='extend-protocol registers String under the Show contract. The method applies a transformation — prepending str-prefix. When show is called on text, the protocol\'s method transforms and returns it.',
            resolution='the text routed through the protocol and returned with the prefix inscribed.',
            tags=("story",)),
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
            "a protocol extended to String, then called on text",
            "the keyword the protocol method returns",
            goal='extend a protocol to String and call the method',
            scenario='Vix the fox had posted a guild contract IPace at the market — any text-label could sign it and pledge a habit-word. She signed up text-labels and set their word to :ran.',
            need='Vix called run on a text-label and expected back the habit-word the text had pledged.',
            mapping='extend-protocol registers String under the IPace contract. The method is defined to return :ran. Calling run on text routes through the protocol and returns the registered answer.',
            resolution='the text-label routed through its registered channel and returned the habit-word it had pledged.',
            tags=("story",)),
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
            " (name-of (->Hare \"Pip\")))", "Pip", 'the form', 'the value the form evaluates to'),
        _ex("(do (defprotocol Tagged (tag-of [this]))"
            " (defrecord Stone [t] Tagged (tag-of [this] (:t this)))"
            " (tag-of (->Stone :grey)))", ":grey", 'the form', 'the value the form evaluates to'),
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
            " [(a-op \"x\") (b-op \"x\")])", [":a-impl", ":b-impl"], 'the form', 'the value the form evaluates to'),
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
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Vix the fox had set up a sorting-tray at the market — one channel per registered species, dispatched by tag.',
            need="Vix dropped a basket bearing one of the registered tags onto the tray, expecting the matching channel's habit-word back.",
            mapping='`defmulti` posts the tray and the dispatch rule; `defmethod` registers a channel for one tag. Calling routes through the matching channel.',
            resolution="the basket's tag routed it through its channel, and the tray returned that channel's habit-word.",
            tags=("story",)),
        _ex("(isa? java.lang.Long java.lang.Number)",
            True,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Sly the fox had set up a sorting-tray at the market — one channel per registered species, dispatched by tag.',
            need="Sly dropped a basket bearing one of the registered tags onto the tray, expecting the matching channel's habit-word back.",
            mapping='`defmulti` posts the tray and the dispatch rule; `defmethod` registers a channel for one tag. Calling routes through the matching channel.',
            resolution="the basket's tag routed it through its channel, and the tray returned that channel's habit-word.",
            tags=("story",)),
        _ex("(isa? java.lang.String java.lang.Number)",
            False,
            'a form',
            'the value the form evaluates to',
            goal='evaluate this form',
            scenario='Renard the fox had set up a sorting-tray at the market — one channel per registered species, dispatched by tag.',
            need="Renard dropped a basket bearing one of the registered tags onto the tray, expecting the matching channel's habit-word back.",
            mapping='`defmulti` posts the tray and the dispatch rule; `defmethod` registers a channel for one tag. Calling routes through the matching channel.',
            resolution="the basket's tag routed it through its channel, and the tray returned that channel's habit-word.",
            tags=("story",)),
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
            " (mapv step [(->Hare) (->Tortoise)]))", [":leap", ":plod"], 'the form', 'the value the form evaluates to'),
        _ex("(do (defprotocol Sound (cry [this]))"
            " (defrecord Hare [] Sound (cry [_] :thump))"
            " (defrecord Tortoise [] Sound (cry [_] :hiss))"
            " (cry (->Tortoise)))", ":hiss", 'the form', 'the value the form evaluates to'),
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
