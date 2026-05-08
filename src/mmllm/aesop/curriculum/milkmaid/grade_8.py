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
            scenario=(
                "The guild-master had posted a dispatch window at the dairy hall. "
                "Every farmer carried a guild-card stamped with her kind. One "
                "function name, `speak`, would read the card and send each farmer "
                "to the correct answer."
            ),
            need=(
                "She needed to define the dispatch window — a `defn` named `speak` "
                "whose `cond` arms read each caller's stamp and return the matching "
                "reply without the guild-master deciding case-by-case."
            ),
            mapping=(
                "`defn` names the window; `cond` is the roll-call board, one row "
                "per stamp. Each `=` test reads the stamp and returns the paired "
                "response on a match. `:else` is the catch-all placard for any "
                "card not listed."
            ),
            resolution=(
                "The REPL registered the function without complaint — the dispatch "
                "window was installed and ready to route any caller who arrived "
                "with a guild-card."
            ),
            tags=("story",),
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
                "The REPL returned the answer belonging to the tortoise's guild-card — the dispatch had routed correctly to the right paired keyword (with `:hare` as the input value)."
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
                'The REPL handed back the contents of the color slot — exactly what the farmer had placed there when she hammered the pail (with `grey` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (deftype Stone [weight]) (.-weight (Stone. 7)))",
            expected=7,
            concept_phrase="reading the weight field of a Stone instance",
            question_what="the weight field value after defining a type Stone with one field weight, then constructing an instance and reading the field",
            goal_text="define a type Stone with a weight field and then read the weight field from an instance",
            scenario=(
                "The farmer had designed a pail mold called Stone — a single-slot "
                "container shaped to carry one attribute, weight, to the dairy scale. "
                "She hammered a Stone pail into shape and dropped the weight into its "
                "labeled slot."
            ),
            need=(
                "She needed to define the pail's mold (`deftype Stone [weight]`), "
                "stamp out a concrete pail, then retrieve what sat in the weight slot "
                "— not estimate what she had placed there."
            ),
            mapping=(
                "`deftype` is the pail mold: it names the container and its single "
                "labeled slot. `Stone.` stamps the mold into a real pail. `.-weight` "
                "is the slot-reader that reaches in and retrieves the stored value."
            ),
            resolution=(
                "The REPL handed back the contents of the weight slot — the number "
                "the farmer had pressed into the mold when she stamped the pail — 7."
            ),
            tags=("story",),
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
            scenario=(
                "The farmer had fashioned a new pail mold called Runner — two labeled "
                "slots, one for a name and one for a pace-stamp. She pressed a Runner "
                "pail into shape for Alice and filled both slots before carrying it "
                "to the dairy."
            ),
            need=(
                "She needed the pail mold defined (`defrecord Runner [name pace]`), "
                "a concrete pail built for Alice, and then the pace slot read back "
                "— to confirm what she had placed there."
            ),
            mapping=(
                "`defrecord` is the pail mold with two named slots. `->Runner` stamps "
                "a concrete pail. The keyword `:pace` acts as the slot-reader, reaching "
                "into the pail and retrieving whatever sits in that compartment."
            ),
            resolution=(
                "The REPL returned the keyword sitting in the pace slot — the stamp "
                "the farmer had pressed into that compartment when she built the pail."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (defrecord Runner [name pace]) (:name (->Runner \"Bob\" :moderate)))",
            expected="Bob",
            concept_phrase="reading the name compartment of a Runner case",
            question_what="the name field value after defining a record Runner with two fields name and pace, then creating an instance and reading the name field",
            goal_text="define a record type named Runner with two fields, then retrieve another field from an instance",
            scenario=(
                "The farmer stamped a second Runner pail using the same two-slot mold — "
                "name and pace side by side. She wanted to confirm that the name slot "
                "held exactly what she had pressed in when she shaped the pail."
            ),
            need=(
                "She needed to build a Runner pail with a name and then reach into "
                "the name slot to read back its contents — the farmer's record, "
                "not a guess."
            ),
            mapping=(
                "`defrecord` defines the pail mold with its labeled slots. `->Runner` "
                "stamps a concrete pail. The keyword `:name` is the slot-reader that "
                "reaches into the name compartment and retrieves the stored value."
            ),
            resolution=(
                "The REPL returned the string sitting in the name slot — whatever "
                "the farmer had placed there when she hammered the pail into shape."
            ),
            tags=("story",),
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
            goal_text="found a Pace guild with one required method speed, then confirm the guild's name exists in the runtime",
            scenario=(
                "The guild-master declared a new market guild called Pace, nailing "
                "its charter to the guild-hall door. One requirement: every member "
                "must answer `speed`. No farmer had joined yet, but the charter "
                "now existed."
            ),
            need=(
                "She needed to confirm the guild charter was real — that `Pace` "
                "now stood as a recognized thing in the runtime, not merely "
                "a plan in the guild-master's notebook."
            ),
            mapping=(
                "`defprotocol` is the guild charter: it names the guild and lists "
                "required methods. `some?` is the inspector who checks whether "
                "the charter's name is a real, non-nil value."
            ),
            resolution=(
                "The REPL confirmed the charter was real — the guild name existed "
                "as a recognized value and the inspector returned an affirmative "
                "answer."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(do (defprotocol Greet (hail [this])) (some? Greet))",
            expected=True,
            concept_phrase="a protocol definition",
            question_what="whether the protocol var Greet is truthy after defining a protocol named Greet with one method hail taking a single argument this",
            goal_text="define a protocol named Greet with one method hail that takes a single argument this",
            scenario=(
                "A second guild charter, Greet, had been posted at the market gate. "
                "The charter required one rule: every member must answer the `hail` "
                "call. The guild-master asked the inspector to confirm the charter "
                "was properly registered."
            ),
            need=(
                "She needed to post the Greet guild charter and then verify that its "
                "name was a real value in the runtime — not absent, not nil."
            ),
            mapping=(
                "`defprotocol` posts the guild charter and registers its name. `some?` "
                "is the inspector: it reads the name and answers truthy if the charter "
                "is present, falsy if the name resolves to nothing."
            ),
            resolution=(
                "The REPL returned a truthy answer — the Greet charter had been "
                "properly registered and the inspector confirmed its presence."
            ),
            tags=("story",),
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
            question_what="the value speed returns after the string farmer joins the Pace guild",
            goal_text="define a protocol named Pace with one method speed, extend it to String type with an implementation, then call speed on a string",
            scenario=(
                "The Pace guild charter had been posted. A string-variety farmer "
                "arrived and joined: she added her name to the charter's roll and "
                "declared her own method for answering the `speed` call."
            ),
            need=(
                "The guild-master needed the string farmer to join and supply her "
                "own `speed` implementation — then route the guild call to confirm "
                "the right method answered."
            ),
            mapping=(
                "`extend-protocol` is the joining ceremony: the string farmer signs "
                "the charter and registers her `speed` method. Calling `speed` on "
                "a string pail routes the call to her registered method."
            ),
            resolution=(
                "The REPL returned the answer the string farmer had registered — her method had answered the guild call, not any other member's (with `swift` as the input value)."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form=("(do (defprotocol Greet (hail [this]))"
                  " (extend-protocol Greet java.lang.Long (hail [_] :number))"
                  " (hail 7))"),
            expected=":number",
            concept_phrase="calling a protocol method on a number",
            question_what="the value returned after defining protocol Greet with method hail, extending it to Long with an implementation, then calling hail on a number",
            goal_text="define a protocol named Greet with one method hail, extend it to Long type with an implementation, then call hail on a number",
            scenario=(
                "The Greet guild charter stood at the market gate. A number-variety "
                "farmer joined the guild, signing the charter and registering her own "
                "`hail` method. The guild-master then called `hail` on a number pail "
                "to see which member answered."
            ),
            need=(
                "She needed the number farmer to join the Greet charter and supply "
                "her own `hail` implementation, then confirm the dispatch routed "
                "to her method when called with a number."
            ),
            mapping=(
                "`extend-protocol` registers the number farmer in the guild. "
                "Calling `hail` on a number pail dispatches to the number farmer's "
                "registered method — each guild member produces her own variety."
            ),
            resolution=(
                'The REPL returned the keyword the number farmer had registered — her method had answered the guild call correctly (with `7` as the input value).'
            ),
            tags=("story",),
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
            question_what="the value returned when speed dispatches to the number arm of the Pace guild",
            goal_text="define a protocol Pace with method speed, extend it to both String and Long types with different implementations, then call speed on the number 42",
            scenario=(
                "The Pace guild charter had two members: one string-variety and one "
                "number-variety, each with her own `speed` reply. The guild-master "
                "presented a number pail at the dispatch window."
            ),
            need=(
                "She needed the guild window to read the arriving pail's variety "
                "and route to the number farmer's arm, ignoring the string "
                "farmer's registered reply."
            ),
            mapping=(
                "`extend-protocol` with two type clauses signs both farmers at once. "
                "Calling `speed` on a number pail routes to the number arm — "
                "the string arm is never consulted."
            ),
            resolution=(
                'The REPL returned the keyword the number farmer had registered — dispatch had routed past the string arm to the correct guild member (with `42` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form=("(do (defprotocol Pace (speed [this]))"
                  " (extend-protocol Pace"
                  "   java.lang.String (speed [_] :string-pace)"
                  "   java.lang.Long   (speed [_] :long-pace))"
                  " (speed \"x\"))"),
            expected=":string-pace",
            concept_phrase="protocol dispatch on a string",
            question_what="the value returned when speed dispatches to the string arm of the Pace guild",
            goal_text="define a protocol Pace with method speed, extend it to both String and Long types with different implementations, then call speed on a string",
            scenario=(
                "The same two-farmer Pace guild stood ready. This time the "
                "guild-master presented a string pail at the dispatch window "
                "to see which member's arm answered."
            ),
            need=(
                "She needed the dispatch to read the string pail's variety and "
                "route to the string farmer's arm, leaving the number arm "
                "untouched."
            ),
            mapping=(
                "Calling `speed` on a string pail checks variety against the "
                "charter roll. The string arm matches; the number arm is skipped. "
                "Each member's reply belongs only to her own variety."
            ),
            resolution=(
                'The REPL returned the keyword the string farmer had placed on her charter arm — dispatch had routed to the right member and no other (with `string-pace` as the input value) (with `:string-pace` as the input value).'
            ),
            tags=("story",),
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
            question_what="the value returned when speed is called on a Milkmaid record that implements Pace",
            goal_text="define a protocol Pace with method speed, define a record Milkmaid that implements Pace, then call speed on a Milkmaid instance",
            scenario=(
                "The Pace guild charter was posted at the dairy gate. A Milkmaid "
                "pail mold joined the charter with its `speed` method declared "
                "inline. The guild-master stamped a pail and called `speed`."
            ),
            need=(
                "She needed `speed` routed to the Milkmaid mold's own inline "
                "body — confirming the record honored the guild charter and "
                "answered through its own registered method."
            ),
            mapping=(
                "`defrecord` with the protocol name inline signs the mold directly "
                "into the charter. `->Milkmaid` stamps a concrete pail. Calling "
                "`speed` dispatches to the mold's own method body."
            ),
            resolution=(
                "The REPL returned the keyword the Milkmaid mold's body declared — dispatch had routed correctly to the record's own implementation (with `swift` as the input value) (with `:swift` as the input value)."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form=("(do (defprotocol Pace (speed [this]))"
                  " (defrecord Farmer [name] Pace (speed [_] :steady))"
                  " (speed (->Farmer \"Shelly\"))"),
            expected=":steady",
            concept_phrase="calling a protocol method on a record instance",
            question_what="the value returned when speed is called on a Farmer record that implements Pace",
            goal_text="define a protocol Pace with method speed, define a record Farmer that implements Pace, then call speed on a Farmer instance",
            scenario=(
                "A Farmer pail mold joined the same Pace guild, declaring its own "
                "`speed` method inline. The guild-master stamped a Farmer pail "
                "and called `speed` to see which reply came back."
            ),
            need=(
                "She needed to confirm the Farmer mold's `speed` answered "
                "independently — that dispatch did not borrow the Milkmaid mold's "
                "reply but routed to the Farmer's own body."
            ),
            mapping=(
                "`defrecord Farmer` with `Pace` inline registers its own charter "
                "slot. `->Farmer` stamps a pail. `speed` reads the mold type and "
                "routes to the Farmer body — a separate slot from the Milkmaid's."
            ),
            resolution=(
                "The REPL returned the keyword the Farmer mold's body declared — each mold's implementation answered its own charter slot with no overlap (with `steady` as the input value) (with `:steady` as the input value)."
            ),
            tags=("story",),
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
            goal_text="build a sorting-table named pace that reads the :species stamp, add a :hare arm, then route a pail stamped :hare",
            scenario=(
                "The dairy had a sorting table: each pail arrived stamped with a "
                "species-tag. The table-master nailed a placard for `:hare` to one "
                "shelf and set the routing rule: read the `:species` stamp."
            ),
            need=(
                "She needed to define the dispatch rule (`defmulti` reading `:species`) "
                "and one arm (`defmethod` for `:hare`), then route a pail and "
                "read where it landed."
            ),
            mapping=(
                "`defmulti` carves the table with `pace` as the router and `:species` "
                "as the stamp key. `defmethod` pins the `:hare` placard. Calling "
                "`pace` with a stamped map routes the pail to the matching arm."
            ),
            resolution=(
                "The REPL returned the value the `:hare` arm had posted — the sort "
                "had routed correctly and the pail landed exactly where the placard "
                "said."
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
            scenario=(
                "The dairy's sorting table, `tag`, had one arm: a placard nailed "
                "to the `:stone` shelf, ready to receive any pail stamped with "
                "that variety. A pail arrived carrying its kind-stamp in the map "
                "under the `:kind` key."
            ),
            need=(
                "She needed the sorting table to read the pail's `:kind` stamp, "
                "find the `:stone` placard, and route the pail to the correct "
                "shelf — then confirm the shelf's declared value came back."
            ),
            mapping=(
                "`defmulti tag :kind` carves the sorting table and names the "
                "stamp to read. `defmethod tag :stone` nails a placard to the "
                "`:stone` shelf. Calling `tag` with the stamped map routes the "
                "pail to the matching arm."
            ),
            resolution=(
                "The REPL returned the keyword posted on the `:stone` shelf — "
                "the pail had been sorted correctly and the shelf's placard "
                "declared the result."
            ),
            tags=("story",),
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
            scenario=(
                "The dairy's `pace` sorting table now had two arms: one placard "
                "for the `:hare` shelf and one for the `:tortoise` shelf. A pail "
                "arrived stamped `:tortoise` under the `:species` key. The table "
                "read the stamp and consulted its placards."
            ),
            need=(
                "She needed the sort to bypass the `:hare` arm entirely and route "
                "to the `:tortoise` shelf instead — confirming that two arms "
                "operated independently, each answering only its own stamp."
            ),
            mapping=(
                "Each `defmethod` nails a placard to one shelf. When `pace` reads "
                "`:species :tortoise`, it bypasses the `:hare` placard and routes "
                "to the `:tortoise` shelf. The `:tortoise` arm's posted value "
                "is what the table returns."
            ),
            resolution=(
                "The REPL returned the keyword posted on the `:tortoise` shelf "
                "— the sort had ignored the `:hare` arm and routed the pail "
                "precisely to the matching placard."
            ),
            tags=("story",),
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
            scenario=(
                "The `pace` sorting table had three arms: one for `:hare`, one "
                "for `:tortoise`, and a catch-all placard labelled `:default`. "
                "An owl pail arrived — no species stamp the table recognised. "
                "The table-master turned to the catch-all shelf."
            ),
            need=(
                "She needed the sort to find no matching named arm and fall through "
                "to the `:default` placard, returning whatever value the fallback "
                "shelf declared — without raising an error for an unrecognised stamp."
            ),
            mapping=(
                "`defmethod pace :default` nails the catch-all placard. When "
                "the `:species` stamp matches no named arm, the sorting table "
                "routes to `:default`. That arm's posted value is what `pace` "
                "returns for any unrecognised variety."
            ),
            resolution=(
                "The REPL returned the keyword posted on the `:default` shelf "
                "— the owl pail had been safely caught by the fallback arm, "
                "with no arm error raised."
            ),
            tags=("story",),
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
            scenario=(
                "The dairy's `show` sorting table read each pail's stamp using "
                "`identity` — the pail's own value was its routing key. One arm "
                "had been nailed: a placard for the `:rabbit` shelf. A `:rabbit` "
                "pail arrived at the table."
            ),
            need=(
                "She needed to confirm that the `identity` dispatch function would "
                "route the `:rabbit` pail directly to the `:rabbit` placard "
                "— and that the placard's posted value came back as the sort's result."
            ),
            mapping=(
                "`defmulti show identity` makes the pail itself its own stamp. "
                "`defmethod show :rabbit` nails a placard for that exact value. "
                "Calling `show` on `:rabbit` reads the pail, finds the placard, "
                "and returns the arm's declared value."
            ),
            resolution=(
                "The REPL returned the string posted on the `:rabbit` shelf "
                "— `identity` dispatch had routed the pail precisely to the "
                "matching arm."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form=("(do (defprotocol Show (show [this]))"
                  " (extend-protocol Show java.lang.String (show [s] (str \"str-\" s)))"
                  " (show \"hare\"))"),
            expected="str-hare",
            concept_phrase="dispatching via protocol",
            question_what="the value returned after defining protocol Show with method show, extending it to String with an implementation, then calling show on a string",
            goal_text="define a protocol Show with method show, extend it to String type, then call show on a string",
            scenario=(
                "The Show guild charter had been posted alongside the sorting table. "
                "A string-variety farmer joined the guild, registering a `show` "
                "method that combined a prefix with the pail's own contents. "
                "The guild-master then called `show` on a string pail."
            ),
            need=(
                "She needed to confirm that the guild route — dispatching by pail "
                "variety rather than by a stamp in the map — returned the reply "
                "the string farmer's method had constructed from the pail's value."
            ),
            mapping=(
                "`extend-protocol Show` signs the string farmer into the charter. "
                "Her `show` body uses `s` (the pail itself) to build a reply with "
                "`str`. Protocol dispatch reads the pail's Java type and routes "
                "to the registered string implementation."
            ),
            resolution=(
                "The REPL returned the string the farmer's method had assembled — the prefix fused with the pail's own contents, confirming that protocol dispatch had reached the right guild member (with `str-` as the input value)."
            ),
            tags=("story",),
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
            question_what="the value returned when run is called on a string after extending IPace",
            goal_text="define a protocol IPace with method run, extend it to String type, then call run on a string",
            scenario=(
                "The guild-master drew up a charter called IPace with one rule: "
                "every member must honor `run`. A string-variety farmer joined "
                "and posted her own `run` body."
            ),
            need=(
                "She needed `run` on a string pail to route to the farmer's "
                "registered body — not raise an error for an unregistered "
                "variety."
            ),
            mapping=(
                "`defprotocol IPace` posts the charter. `extend-protocol` signs "
                "the string farmer in with her `run` body. Calling `run` on a "
                "string pail dispatches to that body — a Clojure-side interface "
                "for the guild."
            ),
            resolution=(
                "The REPL returned the keyword the string farmer's body declared — the charter was honored and dispatch routed to the registered member (with `ran` as the input value) (with `:ran` as the input value)."
            ),
            tags=("story",),
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
            scenario=(
                "The Pace guild charter had been posted, but no farmer had yet "
                "joined under the number variety. `extend-type` was used to sign "
                "the number variety directly into the charter, rather than listing "
                "it inside `extend-protocol`. A number pail then arrived at the "
                "dispatch window."
            ),
            need=(
                "She needed the `speed` call on a number pail to route to the "
                "implementation she had attached via `extend-type` — confirming "
                "that the type-first syntax signed the farmer into the charter "
                "just as effectively."
            ),
            mapping=(
                "`extend-type java.lang.Long Pace` names the type first, then "
                "the charter, then the method body — the inverse of `extend-protocol`. "
                "Calling `speed` on a number pail routes dispatch to that registered "
                "method and returns its posted value."
            ),
            resolution=(
                'The REPL returned the keyword the number-type arm had declared — the sorting-table dispatch had routed correctly to the `extend-type` implementation (with `5` as the input value).'
            ),
            tags=("story",),
        ),
        SubjectExample(
            form=("(do (defprotocol Pace (speed [this]))"
                  " (extend-type java.lang.String Pace (speed [_] :string-pace))"
                  " (speed \"hare\"))"),
            expected=":string-pace",
            concept_phrase="attaching a protocol to a built-in type via extend-type",
            question_what="the value returned when speed is called on a String after extending String with Pace via extend-type",
            goal_text="extend String type with Pace protocol via extend-type, then call speed on a string",
            scenario=(
                "This time the guild-master used `extend-type` to attach the Pace "
                "charter to the string variety, naming the type first and the "
                "charter second. A string pail arrived at the dispatch window "
                "and `speed` was called on it."
            ),
            need=(
                "She needed `speed` on a string pail to route to the implementation "
                "registered through `extend-type`, confirming that the type-first "
                "syntax worked symmetrically for the string variety."
            ),
            mapping=(
                "`extend-type java.lang.String Pace` signs the string variety into "
                "the charter with its own `speed` body. Calling `speed` on a string "
                "pail routes to that registered arm and returns the arm's declared "
                "keyword — the sorting-table's string shelf."
            ),
            resolution=(
                'The REPL returned the keyword the string-type arm had declared — dispatch had routed to the `extend-type` implementation for the string variety, not to any other shelf (with `string-pace` as the input value) (with `:string-pace` as the input value).'
            ),
            tags=("story",),
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
            question_what="the value name-of returns when this reads the n slot",
            goal_text="define a protocol Named with method name-of, define a record that uses this to access a field, then call the method",
            scenario=(
                "The Named guild required every member to answer `name-of`. A "
                "Milkmaid pail mold signed, its body using `this` to reach into "
                "the `n` slot for whatever had been pressed there."
            ),
            need=(
                "She needed `name-of` to read the pail's `n` slot — the value "
                "placed there at stamping time, retrieved through `this` rather "
                "than a hardcoded string."
            ),
            mapping=(
                "`this` in the method body is the concrete pail. `(:n this)` "
                "reaches into the `n` compartment. Guild dispatch binds `this` "
                "to the arriving pail and runs the body against it."
            ),
            resolution=(
                "The REPL returned the string from the `n` slot — `this` had "
                "retrieved what the caller placed there when stamping the pail."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form=("(do (defprotocol Tagged (tag-of [this]))"
                  " (defrecord Stone [t] Tagged (tag-of [this] (:t this)))"
                  " (tag-of (->Stone :grey)))"),
            expected=":grey",
            concept_phrase="using this to access a field in a protocol method",
            question_what="the value tag-of returns when this reads the t slot",
            goal_text="define a protocol Tagged with method tag-of, define a record Stone that implements it by accessing a field via this, then call the method",
            scenario=(
                "A Stone pail mold joined the Tagged guild. Its `tag-of` body "
                "used `this` to read the pail's `t` slot — the variety-stamp "
                "pressed there at construction time."
            ),
            need=(
                "She needed `tag-of` to retrieve the stamp from the `t` slot "
                "— the keyword placed there by the caller, read through `this` "
                "in the method body."
            ),
            mapping=(
                "`(:t this)` reads the `t` compartment: `this` is the arriving "
                "Stone pail and `:t` is the slot key. Guild dispatch binds `this` "
                "to the pail and runs the body against it."
            ),
            resolution=(
                "The REPL returned the keyword from the `t` slot — `this` had "
                "retrieved the pail's own variety-stamp as pressed at construction."
            ),
            tags=("story",),
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
            question_what="the two-element vector returned by calling both charter methods",
            goal_text="define two protocols A and B, each with a method, extend both to String type independently, then call both methods",
            scenario=(
                "Two guild charters — A and B — had been posted at the market gate. "
                "A string-variety farmer signed both independently, registering "
                "a different reply under each. Neither charter knew about the other."
            ),
            need=(
                "She needed to call both charter methods on the same string pail "
                "and confirm each charter's reply came back independently — A's "
                "dispatch and B's dispatch could not interfere."
            ),
            mapping=(
                "Each `extend-protocol` signs the farmer into one charter. Each "
                "call routes through its own guild window. The vector collects "
                "both replies — one per charter — side by side."
            ),
            resolution=(
                "The REPL returned a two-element vector, one slot per charter's dispatch — the two guild memberships had answered independently with no inheritance between them (with `:a-impl` as the input value)."
            ),
            tags=("story",),
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
            scenario=(
                "The table-master had written a new sorting rule in her ledger: "
                "any pail stamped `::hare` belongs under the `::runner` category. "
                "She used `derive` to record the lineage in the dairy's hierarchy "
                "book, then called `isa?` to confirm the relation was registered."
            ),
            need=(
                "She needed to verify that `isa?` could read the ledger and confirm "
                "the parent–child relationship — that `::hare` was now recognised "
                "as a sub-variety of `::runner` in the runtime hierarchy."
            ),
            mapping=(
                "`derive` writes the lineage into the global hierarchy: `::hare` "
                "is a child of `::runner`. `isa?` reads that same ledger and "
                "returns a truthy result if the lineage entry exists, a falsy "
                "one if it does not."
            ),
            resolution=(
                "The REPL confirmed the relationship — `isa?` returned an affirmative "
                "answer, showing the derived lineage had been recorded in the "
                "hierarchy ledger."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(isa? java.lang.Long java.lang.Number)",
            expected=True,
            concept_phrase="checking Java type hierarchy",
            question_what="whether Long is a type of Number in Java's type hierarchy",
            goal_text="check whether Long is a type of Number in Java's type system",
            scenario=(
                "The dairy's sorting hierarchy included Java's own breed-book as "
                "well as custom entries. The table-master wanted to confirm that "
                "the number-variety pail's Java lineage was readable directly: "
                "was Long a sub-variety of Number according to Java's own ledger?"
            ),
            need=(
                "She needed `isa?` to consult the Java type hierarchy — not a "
                "custom-derived entry — and confirm the inheritance relationship "
                "between two Java classes without any manual `derive` call."
            ),
            mapping=(
                "`isa?` in Clojure reads both the custom hierarchy ledger and "
                "Java's class hierarchy. Asking about `java.lang.Long` and "
                "`java.lang.Number` consults the Java side of the ledger, where "
                "the parent–child relationship is pre-recorded."
            ),
            resolution=(
                "The REPL confirmed the Java lineage — `isa?` returned an "
                "affirmative answer, showing Long was recorded as a sub-variety "
                "of Number in Java's own breed-book."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form="(isa? java.lang.String java.lang.Number)",
            expected=False,
            concept_phrase="checking Java type hierarchy",
            question_what="whether String is a type of Number in Java's type hierarchy",
            goal_text="check whether String is a type of Number in Java's type system",
            scenario=(
                "The table-master next checked a different lineage question: could "
                "a string-variety pail be sorted under the number shelf? She asked "
                "`isa?` to consult Java's breed-book for the relationship between "
                "String and Number."
            ),
            need=(
                "She needed `isa?` to return a negative answer — confirming that "
                "string-variety pails had no lineage connection to the number "
                "shelf and would not be mis-routed through a multimethod hierarchy "
                "that expected numbers."
            ),
            mapping=(
                "`isa?` reads Java's class hierarchy. String and Number occupy "
                "separate branches with no ancestor–descendant link between them. "
                "When neither the Java hierarchy nor the custom ledger records "
                "the relation, `isa?` returns a falsy result."
            ),
            resolution=(
                "The REPL returned a negative answer — `isa?` found no lineage "
                "connecting String to Number in Java's breed-book, confirming "
                "the two varieties were unrelated at the sorting table."
            ),
            tags=("story",),
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
            question_what="the two-element vector step returns for both guild molds",
            goal_text="define a protocol Move with method step, define two record types Milkmaid and Farmer that each implement it, then call the method on both instances",
            scenario=(
                "The Move guild required every member to answer `step`. Both a "
                "Milkmaid and a Farmer pail mold had signed the charter with their "
                "own `step` declarations. The guild-master called `step` on both."
            ),
            need=(
                "She needed `mapv` to walk the mixed line and confirm each mold's "
                "own `step` body answered — not one uniform reply, but each "
                "variety producing its own distinct keyword."
            ),
            mapping=(
                "`mapv` calls `step` on each pail in turn. Dispatch routes each "
                "call to the matching mold's body. The vector collects one reply "
                "per guild member, in order."
            ),
            resolution=(
                "The REPL returned a two-element vector — one keyword per mold, each guild member's implementation having answered its own charter slot in sequence (with `leap` as the input value) (with `:leap` as the input value)."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form=("(do (defprotocol Sound (cry [this]))"
                  " (defrecord Milkmaid [] Sound (cry [_] :thump))"
                  " (defrecord Farmer [] Sound (cry [_] :hiss))"
                  " (cry (->Farmer)))"),
            expected=":hiss",
            concept_phrase="calling a polymorphic method on a record instance",
            question_what="the keyword cry returns for the Farmer guild mold",
            goal_text="define a protocol Sound with method cry, define two record types that implement it, then call the method on a Farmer instance",
            scenario=(
                "The Sound guild required every member to honor `cry`. Both a "
                "Milkmaid and a Farmer mold had joined with their own `cry` "
                "bodies. The guild-master called `cry` on a Farmer pail only."
            ),
            need=(
                "She needed dispatch to route to the Farmer mold's body — not "
                "the Milkmaid's — confirming each mold's charter slot answered "
                "independently."
            ),
            mapping=(
                "`defrecord Farmer` with `Sound` inline registers the Farmer "
                "mold's charter slot. Calling `cry` routes to that body. The "
                "Milkmaid's slot sits separately and is never consulted."
            ),
            resolution=(
                "The REPL returned the keyword the Farmer mold's `cry` body declared — dispatch had routed precisely to the Farmer's charter entry, not to the Milkmaid's (with `thump` as the input value) (with `:thump` as the input value)."
            ),
            tags=("story",),
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
