"""Grade 8 — protocols, multimethods, abstraction. Through crow-pitcher.

The fable's moral dynamic — Hare's vanity vs Tortoise's steadiness —
maps cleanly onto polymorphism: different species respond to the same
call differently. Hare boasts that "everyone runs the same way";
Tortoise insists each kind of creature has its own implementation.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.crow_pitcher.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.crow_pitcher._metaphor_pools import (
    _CARRYINGCASE_SUBPLOTS, _GUILD_SUBPLOTS, _SORTINGTABLE_SUBPLOTS,
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
    fable="crow-pitcher",
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
                "Sable talon-scratched a routing rule on the pitcher's rim at the "
                "hilltop: a stone marked :hare gets one word, :tortoise gets another, "
                "everything else gets 'silent'. The rule was scratched — not yet called."
            ),
            need=(
                "She needed to record the routing rule so any stone could be "
                "handed to it later without re-scratching."
            ),
            mapping=(
                "`defn` scratches the rule permanently onto the rim. "
                "The `cond` branches encode each stone's tag and its matching word. "
                "No stone is dropped yet — the rule is simply registered."
            ),
            resolution=(
                "The pitcher acknowledged the rule was scratched and the var was registered. (the keyword :hare)"
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
                "Korvus scratched two rules on the rim at the garden: "
                "a :hare-marked stone gets one word, a :tortoise-marked stone "
                "gets another. He dropped a stone marked :tortoise into the pitcher."
            ),
            need=(
                "He needed to confirm the cond-rule returned the right word "
                "for a :tortoise-marked stone."
            ),
            mapping=(
                "The `cond` branches act as a hand-sorted routing rule — "
                "each clause checks the mark and picks the matching word. "
                "Dropping :tortoise skips the first clause and matches the second."
            ),
            resolution=(
                "The pitcher returned the word registered for the :tortoise branch. (with {drawn.a} folded in)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(do (deftype Pebble [color]) (.-color (Pebble. \"grey\")))",
            expected="grey",
            concept_phrase="reading the color field of a Pebble instance",
            question_what="the color field value after defining a type Pebble with one field color, then constructing an instance and reading the field",
            goal_text="define a type Pebble with a color field and then read the color field from an instance",

            scenario=(
                "Caw wove a bark-and-vine pouch at the orchard with a single "
                "slot called color. She packed one pebble in, marking the color "
                "slot with a talon-scratch, then held the pouch to the light."
            ),
            need=(
                "She needed to reach into the color slot and lift the "
                "marked value back out without unpacking everything."
            ),
            mapping=(
                "`deftype` weaves the pouch's shape — one named slot. "
                "Constructing `Pebble.` packs the value in. "
                "The `.-color` accessor reaches directly into the slot and lifts the value."
            ),
            resolution=(
                'The color slot answered with the value packed inside (with `grey` as the input value).'
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
                "Sable wove a pouch at the meadow with a single weight slot. "
                "A stone numbered 7 was packed in, and the pouch was set on "
                "the pitcher's rim to be read back."
            ),
            need=(
                "Sable needed to confirm the weight slot returned the number "
                "packed in at construction time."
            ),
            mapping=(
                "`deftype` shapes the pouch with a weight slot. "
                "The constructor packs the number in. "
                "`.-weight` reaches into that slot and returns the stored value without disturbing the pouch."
            ),
            resolution=(
                "The weight slot yielded the number that had been packed inside. (count: 7)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form='(do (defrecord Runner [name pace]) (:pace (->Runner "Alice" :slow)))',
            expected=":slow",
            concept_phrase="reading the pace compartment of a Runner case",
            question_what="the value in the pace compartment of a freshly-built Runner case for Alice",
            goal_text="define a Runner case with two named compartments, name and pace; build a Runner case for Alice with a deliberate-pace keyword; then read the pace compartment",

            scenario=(
                "Caw wove a bark-and-vine carrying-pouch with two named slots: "
                "one for a name-stone, one for a pace-stone. She stitched "
                "the shape onto the rim once, then packed an instance: "
                "name='Alice', pace=:slow."
            ),
            need=(
                "She needed to read back the pace slot from the packed pouch "
                "without unsealing the name slot."
            ),
            mapping=(
                "`defrecord` stitches the pouch's shape — named fields. "
                "`->Runner` packs an instance with values in order. "
                "`:pace` used as a function reaches into the correct slot "
                "and lifts the value without touching the others."
            ),
            resolution=(
                ":slow — the pace slot answered, the other slot undisturbed, "
                "the carrying-pouch intact on the rim."
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
                "Korvus stitched a Runner pouch on the pitcher's rim at the market "
                "with two slots: name and pace. He packed a new instance with a "
                "name-stone and a moderate pace, then reached for the name slot."
            ),
            need=(
                "He needed to lift only the name slot's value from the packed "
                "pouch, leaving the pace slot untouched."
            ),
            mapping=(
                "`defrecord` stitches the two-slot shape once. `->Runner` packs "
                "values in order. `:name` used as a function reaches into the "
                "correct slot and lifts just that value."
            ),
            resolution=(
                "The name slot answered with the value that had been packed in. (the keyword :name)"
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
    fable="crow-pitcher",
    examples=[
        # Defining a protocol returns the protocol var; we use an
        # ancillary call that demonstrates it was defined.
        SubjectExample(
            form="(do (defprotocol Pace (speed [this])) (some? Pace))",
            expected=True,
            concept_phrase="a protocol definition",
            question_what="whether the Runners' guild named Pace is real after the founding",
            goal_text="found a Runners' guild named Pace whose only requirement is a method speed taking the runner as its single argument; then check whether the guild's name is now a real thing in the runtime",

            scenario=(
                "Sable scratched the guild's charter onto the pitcher's rim "
                "at the village: any type wishing to answer the `speed` call "
                "must register here. The ledger was posted but no members had "
                "yet signed."
            ),
            need=(
                "Sable needed to confirm the guild's name existed in the runtime "
                "as a real thing after the charter was scratched."
            ),
            mapping=(
                "`defprotocol` posts the guild's ledger — the name and required "
                "calls are declared. `some?` checks whether the ledger var is "
                "present and truthy, confirming the guild was founded successfully."
            ),
            resolution=(
                "The pitcher confirmed the guild's ledger was real and present."
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
                "Caw scratched a new guild charter at the hilltop: the Greet "
                "guild, requiring any member to answer the `hail` call. "
                "She posted the ledger on the rim, then peered to see if it "
                "had truly taken hold."
            ),
            need=(
                "She needed to know whether the Greet guild ledger was now "
                "a real presence in the runtime after being posted."
            ),
            mapping=(
                "`defprotocol` posts the guild's charter with the required "
                "method listed. `some?` probes whether the ledger var is "
                "non-nil, confirming the guild exists."
            ),
            resolution=(
                "The pitcher returned confirmation that the ledger was present."
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form=("(do (defprotocol Pace (speed [this]))"
                  " (extend-protocol Pace java.lang.String (speed [_] \"swift\"))"
                  " (speed \"hare\"))"),
            expected="swift",
            concept_phrase="calling a protocol method on a string",
            question_what="the value returned after defining protocol Pace with method speed, extending it to String with an implementation, then calling speed on a string",
            goal_text="define a protocol named Pace with one method speed, extend it to String type with an implementation, then call speed on a string",
            scenario=(
                "Sable posted the guild ledger on the pitcher's rim at the "
                "hilltop: any stone that answered the `speed` call must return "
                "a pace. She registered String-marked stones as the first "
                "type, giving them a response of :swift."
            ),
            need=(
                "She wanted to drop a text-stone ('hare') and have it "
                "answered by the pace registered for String-type stones."
            ),
            mapping=(
                "`defprotocol` posts the guild's call. `extend-protocol` "
                "registers which type responds and how. When `speed` is "
                "called with a String, the runtime checks its type and "
                "dispatches to the registered method."
            ),
            resolution=(
                ":swift — the String arm of the guild answered, the right "
                "pace returning for the text stone."
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
                "Korvus posted the Greet guild ledger on the pitcher's rim at "
                "the road. He registered Long-marked stones as members — any "
                "numbered stone must answer the `hail` call — then dropped a "
                "stone marked 7."
            ),
            need=(
                "He needed the guild to route the numbered stone to its "
                "registered response without manual sorting."
            ),
            mapping=(
                "`defprotocol` posts the charter. `extend-protocol` signs Long "
                "into the guild with its response. Calling `hail` on the number "
                "checks the guild ledger and dispatches to the registered answer."
            ),
            resolution=(
                "The guild ledger matched the number's type and returned the registered response. (count: 7)"
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
    fable="crow-pitcher",
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

            scenario=(
                "Sable posted the Pace guild ledger at the garden with two "
                "member rows: one for text-stones, one for numbered stones, "
                "each with its own pace entry. She dropped a numbered stone "
                "marked 42 into the pitcher."
            ),
            need=(
                "She needed to confirm the guild routed the numbered stone to "
                "the Long row's registered pace, not the text row's."
            ),
            mapping=(
                "`extend-protocol` adds two rows to the ledger — String and "
                "Long each with their own pace. At dispatch, the runtime reads "
                "the stone's type and finds the matching ledger row."
            ),
            resolution=(
                "The Long row's pace returned, confirming dispatch went to the correct member row. (count: 42)"
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
            question_what="the value returned after defining protocol Pace with method speed, extending it to both String and Long types with different implementations, then calling speed on a string",
            goal_text="define a protocol Pace with method speed, extend it to both String and Long types with different implementations, then call speed on a string",

            scenario=(
                "Korvus posted the same two-row Pace ledger on the pitcher at "
                "the orchard. He dropped a text-stone marked 'x' and watched "
                "the guild sort it away from the numbered-stone row."
            ),
            need=(
                "He needed to confirm the text-stone was routed to the String "
                "row's pace, not the Long row's."
            ),
            mapping=(
                "Both rows exist on the ledger simultaneously. The runtime "
                "inspects the dropped stone's type, skips the Long row, and "
                "dispatches to the String row's registered pace."
            ),
            resolution=(
                "The String row's pace returned, proving the guild dispatched correctly. (the keyword :string-pace)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form=("(do (defprotocol Pace (speed [this]))"
                  " (defrecord Falcon [name] Pace (speed [_] :swift))"
                  " (speed (->Falcon \"Aria\"))"),
            expected=":swift",
            concept_phrase="calling a protocol method on a record instance",
            question_what="the value returned after defining protocol Pace with method speed, defining record Falcon with one field name that implements Pace, then calling speed on a Falcon instance",
            goal_text="define a protocol Pace with method speed, define a record Falcon that implements Pace, then call speed on a Falcon instance",

            scenario=(
                "Caw posted the Pace guild charter on the rim at the farm's edge, "
                "then wove a Falcon-shaped carrying-pouch with a name slot that "
                "signed the charter inline, pledging its own pace response. She "
                "packed a name-stone inside and called `speed`."
            ),
            need=(
                "She needed to confirm a Falcon-typed carrying-pouch returned its "
                "own pledged pace when the guild's `speed` call arrived."
            ),
            mapping=(
                "`defrecord` with the protocol name inline stitches the guild "
                "membership directly into the type. `speed` dispatches to the "
                "type's built-in response without consulting a separate ledger row."
            ),
            resolution=(
                "The Falcon-shaped pouch answered the `speed` call with its pledged pace. (the keyword :swift)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form=("(do (defprotocol Pace (speed [this]))"
                  " (defrecord Heron [name] Pace (speed [_] :steady))"
                  " (speed (->Heron \"Vesper\"))"),
            expected=":steady",
            concept_phrase="calling a protocol method on a record instance",
            question_what="the value returned after defining protocol Pace with method speed, defining record Heron with one field name that implements Pace, then calling speed on a Heron instance",
            goal_text="define a protocol Pace with method speed, define a record Heron that implements Pace, then call speed on a Heron instance",

            scenario=(
                "Korvus posted the Pace guild charter on the pitcher at the "
                "village, then wove a Heron-shaped carrying-pouch with a name "
                "slot that pledged the guild inline. He packed a name-stone and "
                "called `speed`."
            ),
            need=(
                "He needed to confirm the Heron-shaped pouch's own pace response "
                "was returned when `speed` was called on it."
            ),
            mapping=(
                "The record's inline protocol pledge means the method is baked "
                "into the type's own shape. Calling `speed` finds the method "
                "on the type itself and returns its result."
            ),
            resolution=(
                "The Heron-shaped pouch answered with the pace stitched into its own shape. (the keyword :steady)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form='(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))',
            expected=":swift",
            concept_phrase="the multimethod and its first arm",
            question_what="the pace returned for a runner stamped :hare after the table routes to its arm",
            goal_text="declare a sorting-table named pace that reads each runner's :species stamp; add an arm for the :hare stamp returning the swift-pace keyword; then route a runner stamped :hare through the table",

            scenario=(
                "Korvus set the sorting-lip on the pitcher's mouth at the "
                "farm's edge: stones bearing a :species mark would be routed "
                "by the matching chute. He registered a chute for the :hare stamp."
            ),
            need=(
                "He wanted to drop a stone stamped {:species :hare} and "
                "watch the lip route it automatically."
            ),
            mapping=(
                "`defmulti` installs the reading-rule — here it reads "
                ":species. `defmethod` registers what happens per reading. "
                "The dispatch is automatic at call time."
            ),
            resolution=(
                "the lip read :hare, opened the matching chute, and the "
                "registered value dropped into the pitcher."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form=("(do (defmulti tag :kind)"
                  " (defmethod tag :stone [_] :hard)"
                  " (tag {:kind :stone}))"),
            expected=":hard",
            concept_phrase="calling a multimethod with a specific dispatch value",
            question_what="the value returned after defining multimethod tag that dispatches on :kind, adding a method for :stone, then calling tag with a map",
            goal_text="define a multimethod tag that dispatches on the :kind key, add a method for :stone, then call tag with a map",

            scenario=(
                "Caw mounted a sorting-lip on the pitcher at the meadow that "
                "read a :kind stamp on each pebble. She registered one chute "
                "for pebbles stamped :stone and dropped in a pebble marked "
                "{:kind :stone}."
            ),
            need=(
                "She needed the lip to read :stone and automatically route "
                "the pebble to the registered chute."
            ),
            mapping=(
                "`defmulti` installs the lip with :kind as the reading rule. "
                "`defmethod` registers the :stone chute. Calling `tag` triggers "
                "the lip and dispatches to the matching chute automatically."
            ),
            resolution=(
                "The :stone chute opened and the registered value dropped into the pitcher."
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
    fable="crow-pitcher",
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
                "Sable set the sorting-lip on the pitcher's rim at the hilltop "
                "reading :species. She registered two chutes — one for :hare, "
                "one for :tortoise — then dropped a pebble stamped "
                "{:species :tortoise}."
            ),
            need=(
                "Sable needed the lip to skip the :hare chute and open only "
                "the :tortoise chute for the matching pebble."
            ),
            mapping=(
                "Two `defmethod` calls register two chutes on the same lip. "
                "The dispatch reads :species and routes exclusively to the "
                "matching chute, ignoring the other."
            ),
            resolution=(
                "The :tortoise chute opened and its registered pace returned."
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
                "Korvus set three chutes on the sorting-lip at the garden: "
                "one for :hare, one for :tortoise, and a catch-all at the end "
                "for anything else. He dropped a pebble stamped {:species :owl}."
            ),
            need=(
                "He needed to confirm the lip routed an unregistered stamp "
                "to the catch-all chute instead of failing."
            ),
            mapping=(
                "The `:default` chute catches every stamp with no specific "
                "registration. The lip reads :owl, finds no matching chute, "
                "and falls through to the default."
            ),
            resolution=(
                "The catch-all chute opened and the fallback value returned. (the keyword :species)"
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
    fable="crow-pitcher",
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
                "Caw mounted a sorting-lip at the road that read each pebble "
                "as its own stamp — the identity rule. She registered one chute "
                "for pebbles that were themselves :rabbit and dropped one in."
            ),
            need=(
                "She needed the identity lip to match the pebble's own value "
                "and route it to the :rabbit chute."
            ),
            mapping=(
                "`defmulti` with `identity` uses the pebble itself as the "
                "dispatch stamp. `defmethod` registers the :rabbit chute. "
                "Dropping :rabbit triggers the lip and routes to that chute."
            ),
            resolution=(
                "The :rabbit chute opened and the registered word returned."
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
                "Sable posted the Show guild ledger on the pitcher at the "
                "orchard and registered text-stones as members, each returning "
                "a prefixed label. She dropped a text-stone marked 'hare' and "
                "called `show`."
            ),
            need=(
                "She needed the guild to dispatch on the stone's type and "
                "return the text-stone's own computed label."
            ),
            mapping=(
                "`defprotocol` posts the charter. `extend-protocol` signs String "
                "into the guild with a function that builds a label from the "
                "stone. Calling `show` dispatches by type and runs that function."
            ),
            resolution=(
                "The String row's function ran and returned the constructed label."
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
    fable="crow-pitcher",
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

            scenario=(
                "Korvus scratched the IPace charter on the pitcher's rim at "
                "the village: any enrolled type must answer the `run` call. "
                "He enrolled text-stones and dropped a stone marked 'hare' "
                "to test the enrollment."
            ),
            need=(
                "He needed the guild to find the text-stone's enrollment and "
                "return the registered response for `run`."
            ),
            mapping=(
                "`defprotocol` is the charter; `extend-protocol` is enrollment. "
                "The runtime reads the stone's type, finds its ledger row, and "
                "dispatches the call to the enrolled implementation."
            ),
            resolution=(
                "The text-stone's enrolled response came back from the pitcher. (the keyword :ran)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form=("(do (defprotocol Pace (speed [this]))"
                  " (extend-type java.lang.Long Pace (speed [_] :number-pace))"
                  " (speed 5))"),
            expected=":number-pace",
            concept_phrase="attaching a protocol to a built-in type via extend-type",
            question_what="the value returned after defining protocol Pace with method speed, using extend-type to attach it to Long type with an implementation, then calling speed on a number",
            goal_text="define a protocol Pace with method speed, use extend-type to attach it to Long type, then call speed on a number",

            scenario=(
                "Caw posted the Pace charter on the pitcher at the farm's edge, "
                "then used a different form to attach Long-type stones to it: "
                "extend-type enrolls a whole type family at once. She dropped "
                "a numbered stone marked 5."
            ),
            need=(
                "She needed the Long enrollment to route the numbered stone "
                "and return the pace registered for that type."
            ),
            mapping=(
                "`extend-type` attaches the type to the protocol from the "
                "type's side — one type, multiple protocols at once. Calling "
                "`speed` checks the type ledger and dispatches to the attached method."
            ),
            resolution=(
                "The Long type's attached pace returned from the pitcher. (count: 5)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form=("(do (defprotocol Pace (speed [this]))"
                  " (extend-type java.lang.String Pace (speed [_] :string-pace))"
                  " (speed \"hare\"))"),
            expected=":string-pace",
            concept_phrase="attaching a protocol to a built-in type via extend-type",
            question_what="the value returned after defining protocol Pace with method speed, using extend-type to attach it to String type with an implementation, then calling speed on a string",
            goal_text="define a protocol Pace with method speed, use extend-type to attach it to String type, then call speed on a string",

            scenario=(
                "Sable posted the Pace charter at the market and used extend-type "
                "to attach String-type stones as members. She dropped a text-stone "
                "marked 'hare' and waited for the guild to respond."
            ),
            need=(
                "She needed the String attachment to answer the `speed` call "
                "with the pace registered for text-stones."
            ),
            mapping=(
                "`extend-type` attaches the String type to the Pace charter. "
                "When `speed` is called on a text-stone, the runtime finds "
                "the String attachment and dispatches to its pace method."
            ),
            resolution=(
                "The String attachment answered and the text-stone's pace returned. (the keyword :string-pace)"
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
    fable="crow-pitcher",
    examples=[
        # The first arg is conventionally `this` in protocol method
        # bodies — illustrate by capturing the field via this.
        SubjectExample(
            form=("(do (defprotocol Named (name-of [this]))"
                  " (defrecord Falcon [n] Named (name-of [this] (:n this)))"
                  " (name-of (->Falcon \"Zephyr\")))"),
            expected="Zephyr",
            concept_phrase="using this to access a field in a protocol method",
            question_what="the value returned after defining protocol Named with method name-of, defining record Falcon with field n that uses this to access the field in the implementation, then calling name-of on a Falcon instance",
            goal_text="define a protocol Named with method name-of, define a record that uses this to access a field, then call the method",

            scenario=(
                "Caw posted the Named guild charter at the garden pitcher. "
                "She wove a Falcon-shaped pouch with an 'n' slot pledging the "
                "guild — its method using `this` to read the slot."
            ),
            need=(
                "She needed `this` to reach into the pouch and return "
                "the n slot's value."
            ),
            mapping=(
                "Inside the method, `this` binds to the instance. "
                "`:n` on `this` lifts the slot value directly."
            ),
            resolution=(
                "The slot answered through `this` with the packed name. (the keyword :n)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form=("(do (defprotocol Tagged (tag-of [this]))"
                  " (defrecord Stone [t] Tagged (tag-of [this] (:t this)))"
                  " (tag-of (->Stone :grey)))"),
            expected=":grey",
            concept_phrase="using this to access a field in a protocol method",
            question_what="the value returned after defining protocol Tagged with method tag-of, defining record Stone with field t that uses this to access the field in the implementation, then calling tag-of on a Stone instance",
            goal_text="define a protocol Tagged with method tag-of, define a record Stone that implements it by accessing a field via this, then call the method",

            scenario=(
                "Korvus posted the Tagged guild charter at the hilltop "
                "pitcher. He wove a Stone pouch with a 't' slot pledging "
                "the guild — its method using `this` to read the slot."
            ),
            need=(
                "He needed `this` to reach through into the Stone pouch "
                "and return the t slot's value."
            ),
            mapping=(
                "`this` binds to the Stone inside the method. "
                "`:t` on `this` lifts the slot value, just like on a map."
            ),
            resolution=(
                "The slot answered through `this` with the packed mark. (the keyword :t)"
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
    fable="crow-pitcher",
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

            scenario=(
                "Sable posted two separate guild charters on the pitcher at the "
                "market — guild A requiring `a-op`, guild B requiring `b-op`. "
                "She signed text-stones into each guild separately, then dropped "
                "one text-stone and called both methods."
            ),
            need=(
                "She needed to confirm each guild's call returned its own "
                "registered response from the same text-stone."
            ),
            mapping=(
                "Two guilds share no ledger. Each `extend-protocol` registers "
                "the same String type independently in each. Calling both methods "
                "on one stone dispatches through separate ledgers, returning separate results."
            ),
            resolution=(
                "Both guilds answered independently, each returning its own registered response. (the keyword :a-impl)"
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
    fable="crow-pitcher",
    examples=[
        SubjectExample(
            form="(do (derive ::hare ::runner) (isa? ::hare ::runner))",
            expected=True,
            concept_phrase="checking type hierarchy after derive",
            question_what="whether the relationship holds after establishing with derive that ::hare is a type of ::runner, then checking with isa?",
            goal_text="establish a type relationship where ::hare is a type of ::runner, then check it",

            scenario=(
                "Korvus scratched a lineage mark on the sorting-lip at the "
                "orchard: ::hare is a kind of ::runner. He talon-pressed the "
                "relationship into the hierarchy stone, then queried whether "
                "::hare counted as ::runner."
            ),
            need=(
                "He needed to confirm the derived relationship was recorded "
                "and that `isa?` could read it back."
            ),
            mapping=(
                "`derive` writes the parent-child relationship into the global "
                "hierarchy. `isa?` checks that hierarchy, walking upward if "
                "needed, and returns whether the relationship holds."
            ),
            resolution=(
                "The hierarchy stone confirmed the derived relationship was present. (the keyword :hare)"
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
                "Caw inspected the Java lineage stones on the pitcher's rim "
                "at the meadow. She asked the hierarchy whether a Long-marked "
                "stone counted as a Number-marked stone in the built-in family tree."
            ),
            need=(
                "She needed `isa?` to walk the Java type tree and confirm "
                "Long's parentage without any explicit `derive` call."
            ),
            mapping=(
                "`isa?` reads both Clojure's derived hierarchy and Java's "
                "built-in class tree. Long extends Number in Java, so the "
                "relationship is already present."
            ),
            resolution=(
                "The hierarchy confirmed Long descends from Number in the built-in tree."
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
                "Sable inspected the Java lineage stones at the farm's edge, "
                "asking whether a text-stone marked String could count as a "
                "Number-type stone. She dropped the query into the pitcher "
                "and waited."
            ),
            need=(
                "She needed `isa?` to search the Java type tree and report "
                "whether String and Number are related at all."
            ),
            mapping=(
                "`isa?` walks the full Java type hierarchy. String and Number "
                "share no ancestor except Object, so no parent-child path "
                "connects them and the relationship is absent."
            ),
            resolution=(
                "The pitcher returned no — the type tree held no path between them."
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
    fable="crow-pitcher",
    examples=[
        # A small "many implementations behind one protocol" example.
        SubjectExample(
            form=("(do (defprotocol Move (step [this]))"
                  " (defrecord Falcon [] Move (step [_] :leap))"
                  " (defrecord Heron [] Move (step [_] :plod))"
                  " (mapv step [(->Falcon) (->Heron)]))"),
            expected=[":leap", ":plod"],
            concept_phrase="calling a polymorphic method on multiple record types",
            question_what="the vector of results after defining protocol Move with method step, defining records Falcon and Heron that both implement Move, then calling step via mapv on both instances",
            goal_text="define a protocol Move with method step, define two record types Falcon and Heron that each implement it, then call the method on both instances",

            scenario=(
                "Sable posted the Move guild charter on the pitcher's rim at "
                "the village. Two carrying-pouches — Falcon-shaped and "
                "Heron-shaped — each pledged the guild with their own `step` "
                "response. She lined both up and called `step` across the row."
            ),
            need=(
                "She needed each pouch to answer `step` with its own response "
                "and both results collected into a single row."
            ),
            mapping=(
                "One `defprotocol`, two `defrecord` types each pledging it. "
                "`mapv` sends `step` to each instance in turn; the runtime "
                "dispatches to each type's own method, collecting the results."
            ),
            resolution=(
                "The pitcher returned a pair — each pouch's own `step` response in order. (the keyword :leap)"
            ),
            tags=("story",),
        ),
        SubjectExample(
            form=("(do (defprotocol Sound (cry [this]))"
                  " (defrecord Falcon [] Sound (cry [_] :thump))"
                  " (defrecord Heron [] Sound (cry [_] :hiss))"
                  " (cry (->Heron)))"),
            expected=":hiss",
            concept_phrase="calling a polymorphic method on a record instance",
            question_what="the value returned after defining protocol Sound with method cry, defining records Falcon and Heron that both implement Sound, then calling cry on a Heron instance",
            goal_text="define a protocol Sound with method cry, define two record types that implement it, then call the method on a Heron instance",

            scenario=(
                "Korvus posted the Sound guild charter on the pitcher at the "
                "garden. Two carrying-pouches — Falcon-shaped and Heron-shaped "
                "— pledged the guild with separate `cry` responses. He picked "
                "up the Heron pouch and called `cry` on it alone."
            ),
            need=(
                "He needed only the Heron pouch's own `cry` response, "
                "not the Falcon's, despite both being guild members."
            ),
            mapping=(
                "Both types are guild members, but dispatch is per-instance. "
                "Calling `cry` on a Heron instance routes only to the "
                "Heron method, returning its registered response."
            ),
            resolution=(
                "The Heron pouch's `cry` response returned, the Falcon's untouched. (the keyword :thump)"
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
    print(f"grade-8 crow-pitcher smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
