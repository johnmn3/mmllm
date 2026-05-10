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
from mmllm.aesop.curriculum.tortoise_hare._metaphor_pools import (
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
    fable="tortoise-hare",
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
                "At the meadow's starting line, Mossback the tortoise "
                "noticed that hares and tortoises answered the same "
                "question — 'how do you run?' — with completely different "
                "words. Pip the hare had not yet arrived, so Mossback "
                "worked alone."
            ),
            need=(
                "She wanted a single function that, given a species tag, "
                "returned the right description — without the caller "
                "knowing which species would show up."
            ),
            mapping=(
                "`defn` names the function; `cond` tests each species tag "
                "in turn and returns the matching description. One call, "
                "many possible answers — the essence of dispatch."
            ),
            resolution=(
                'the function was defined and ready to answer any species tag with its own distinct description (with `:hare` as the input value).'
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
                "Mossback the tortoise had built a small dispatch function "
                "inside a `let` block, binding it to the name `speak`. "
                "Pip the hare watched, certain the answer would be the "
                "same for any species."
            ),
            need=(
                "Mossback needed to call the function with the tortoise "
                "tag and see which description came back — proving that "
                "the tortoise branch fired correctly."
            ),
            mapping=(
                "`let` binds the anonymous function to `speak`. Calling "
                "`speak` with the tortoise tag triggers the matching "
                "`cond` branch and returns that branch's description."
            ),
            resolution=(
                "the dispatch returned the tortoise's own description, confirming that different tags produce different answers from a single call (with `:hare` as the input value)."
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(do (deftype Pebble [color]) (.-color (Pebble. \"grey\")))",
            expected="grey",
            concept_phrase="reading the color field of a Pebble instance",
            question_what="the color field value after defining a type Pebble with one field color, then constructing an instance and reading the field",
            goal_text="define a type Pebble with a color field and then read the color field from an instance",
            scenario=(
                "Mossback the tortoise shaped a plain wooden carrying-case "
                "called a Pebble — no labels, just a single bare slot inside "
                "for color. She placed a pebble of a particular shade into "
                "the slot and sealed the case."
            ),
            need=(
                "She needed to reach inside the case and retrieve the color "
                "stored in its lone slot, to confirm the case held what she "
                "had put there."
            ),
            mapping=(
                "`deftype` declares the bare case shape with its one field. "
                "The constructor fills the field when the case is built. "
                "`.-color` reaches directly into the slot by field-name "
                "and pulls the value out."
            ),
            resolution=(
                'the field access returned the exact shade that had been placed in the case at construction time (with `grey` as the input value).'
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
                "Pip the hare found a smooth stone on the path and wanted "
                "to record its weight in a bare carrying-case. Mossback "
                "showed him that `deftype` could shape a case with a "
                "single weight slot — no labels, just direct field access. The value at the heart of the form was 7."
            ),
            need=(
                "After placing the stone's weight in the slot, Pip needed "
                "to read it back using the field-access syntax, to verify "
                "the case had stored it correctly."
            ),
            mapping=(
                "`deftype` declares the plain case. The constructor sets "
                "the `weight` field. `.-weight` reaches into the slot and "
                "returns the stored value directly."
            ),
            resolution=(
                "the field access returned the weight that had been placed "
                "in the slot, confirming the bare case held it faithfully."
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form='(do (defrecord Runner [name pace]) (:pace (->Runner "Alice" :slow)))',
            expected=":slow",
            concept_phrase="reading the pace compartment of a Runner case",
            question_what="the value in the pace compartment of a freshly-built Runner case for Alice",
            goal_text="define a Runner case with two named compartments, name and pace; build a Runner case for Alice with a deliberate-pace keyword; then read the pace compartment",
            scenario=(
                "Mossback the tortoise was outfitting the meadow's "
                "runners with carrying-cases — small wooden cases with "
                "two named compartments inside, one labeled `name` and "
                "one labeled `pace`. The case-stamp on the outside "
                "would read `Runner`."
            ),
            need=(
                "She wanted to define the Runner case-shape, then "
                "build one such case for a tortoise named Alice "
                "carrying a deliberate-pace keyword, and finally read "
                "what was in the pace compartment."
            ),
            mapping=(
                "`defrecord` declares the case-shape: stamp `Runner`, "
                "compartments [name pace]. The constructor fills both "
                "compartments in order from its arguments. "
                "`(:pace …)` reads the named compartment by its keyword."
            ),
            resolution=(
                "the case held the runner's name and the pace keyword "
                "in their compartments; reading the pace compartment "
                "returned exactly what the case had been built with."
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
                "Mossback the tortoise built a second Runner carrying-case, "
                "this time filling the name compartment for a hare and "
                "the pace compartment with a moderate-pace keyword. She "
                "wanted to prove that `defrecord` cases also act like maps."
            ),
            need=(
                "She needed to read back what was in the name compartment "
                "using keyword access — the same way she would read a "
                "key from any map — to confirm the record acted like one."
            ),
            mapping=(
                "`defrecord` creates a case that doubles as a map. "
                "Using `(:name …)` retrieves the name compartment's "
                "contents exactly as a keyword key-lookup would on a plain map."
            ),
            resolution=(
                "the keyword lookup returned the name stored in that "
                "compartment, confirming the carrying-case behaves like a map."
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
    fable="tortoise-hare",
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
                "Mossback wanted to found a Runners' guild named "
                "`Pace`. Members would have to perform `speed`, taking "
                "the runner as its argument."
            ),
            need=(
                "Before any species could sign, the guild had to be "
                "founded — and Mossback wanted to confirm the name was "
                "now real to the runtime."
            ),
            mapping=(
                "`defprotocol Pace (speed [this])` founds the guild. "
                "`(some? Pace)` then asks whether the name is non-nil."
            ),
            resolution=(
                "the council's roll, freshly inked, was looked up by "
                "name; `some?` cast through the registry — feeling for "
                "the var among many that might or might not be there — "
                "and confirmed the guild now stood entered."
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
                "Pip the hare wanted to found a second guild at the meadow "
                "— one called `Greet`, where members must perform a `hail` "
                "routine whenever another runner approached. The guild did "
                "not yet exist."
            ),
            need=(
                "Before any runner could sign the book, the guild had to "
                "be chartered. Pip needed to confirm the runtime recognized "
                "the name as real after the founding call."
            ),
            mapping=(
                "`defprotocol Greet (hail [this])` charters the guild and "
                "declares its one required routine. `(some? Greet)` asks "
                "the runtime whether the name resolves to a non-nil value."
            ),
            resolution=(
                "the runtime confirmed the guild existed — the name was "
                "non-nil and the charter was in force."
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
    fable="tortoise-hare",
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
                "Mossback the tortoise had founded the Pace guild. Now she "
                "needed to sign up String runners — any String value would "
                "be treated as a hare-type runner with its own answer to "
                "the `speed` routine."
            ),
            need=(
                "She needed to extend the Pace guild to cover the String "
                "type and then call `speed` on a String runner to verify "
                "the extension was in effect."
            ),
            mapping=(
                "`extend-protocol` signs the String type into the Pace "
                "guild, providing its `speed` implementation. Calling "
                "`speed` on a String dispatches to that implementation "
                "and returns its value."
            ),
            resolution=(
                "the guild dispatch reached the String arm and returned "
                "the description registered for that type."
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
                "Pip the hare founded the Greet guild and then wondered: "
                "could a number ever sign the book? Mossback showed him "
                "that `extend-protocol` could enroll the Long type, giving "
                "it its own `hail` routine. The form's keyword to weigh was :number."
            ),
            need=(
                "After enrolling the Long type, Pip needed to call `hail` "
                "on an integer to see which keyword the Long branch "
                "returned, confirming the dispatch worked."
            ),
            mapping=(
                "`extend-protocol Greet java.lang.Long` signs the Long "
                "type into the guild. Calling `hail` on an integer "
                "dispatches to the Long branch and returns its keyword."
            ),
            resolution=(
                "the dispatch reached the Long branch and returned the "
                "keyword registered for numeric runners."
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
    fable="tortoise-hare",
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
                "Mossback the tortoise had signed both String runners "
                "and Long runners into the Pace guild, each with its own "
                "`speed` implementation. An integer runner arrived at "
                "the starting line. The form's keyword to weigh was :string-pace."
            ),
            need=(
                "She needed to call `speed` on the integer and see which "
                "branch the guild chose — proving that the runtime "
                "dispatches to the correct type's implementation."
            ),
            mapping=(
                "`extend-protocol` registers a separate `speed` arm for "
                "each type. Calling `speed` on an integer value causes "
                "the runtime to match the Long branch and return that "
                "branch's keyword."
            ),
            resolution=(
                "the dispatch selected the Long arm and returned the "
                "keyword registered for integer runners."
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
                "After the integer runner cleared the guild's gate, a "
                "String runner arrived. Both types had signed the Pace "
                "guild's book, each with a different `speed` entry. "
                "Pip the hare watched to see which branch would fire. The form's value to weigh was \"x\"."
            ),
            need=(
                "Mossback needed to call `speed` on the String runner "
                "to confirm the dispatch selected the String branch "
                "rather than the Long one."
            ),
            mapping=(
                "Same `extend-protocol` as before, but now the argument "
                "is a String value, so the runtime matches the String "
                "arm and returns its keyword rather than the Long one."
            ),
            resolution=(
                'the dispatch selected the String arm and returned the keyword registered for string runners — different from the integer result (with `:string-pace` as the input value).'
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form=("(do (defprotocol Pace (speed [this]))"
                  " (defrecord Hare [name] Pace (speed [_] :swift))"
                  " (speed (->Hare \"Pip\"))"),
            expected=":swift",
            concept_phrase="calling a protocol method on a record instance",
            question_what="the value returned after defining protocol Pace with method speed, defining record Hare with one field name that implements Pace, then calling speed on a Hare instance",
            goal_text="define a protocol Pace with method speed, define a record Hare that implements Pace, then call speed on a Hare instance",
            scenario=(
                "Mossback the tortoise built a carrying-case — a `Hare` "
                "record with a `name` compartment — and signed it into the "
                "Pace guild directly inside `defrecord`. The form's value to weigh was \"Pip\"."
            ),
            need=(
                "She needed to call `speed` on a Hare instance to confirm "
                "that a record can implement a protocol at definition time."
            ),
            mapping=(
                "`defrecord Hare [name] Pace (speed …)` declares the case "
                "and implements the routine inline. Calling `speed` on a "
                "Hare instance dispatches to that implementation."
            ),
            resolution=(
                "the search through the guild's roll narrowed to the "
                "hare-arm waiting in the methods; the dispatcher — "
                "leaving no candidate untried — handed back the keyword "
                "that arm declared."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form=("(do (defprotocol Pace (speed [this]))"
                  " (defrecord Tortoise [name] Pace (speed [_] :steady))"
                  " (speed (->Tortoise \"Shelly\"))"),
            expected=":steady",
            concept_phrase="calling a protocol method on a record instance",
            question_what="the value returned after defining protocol Pace with method speed, defining record Tortoise with one field name that implements Pace, then calling speed on a Tortoise instance",
            goal_text="define a protocol Pace with method speed, define a record Tortoise that implements Pace, then call speed on a Tortoise instance",
            scenario=(
                "Mossback the tortoise repeated the experiment for her "
                "own kind — a `Tortoise` record with a `name` compartment "
                "that implements the Pace guild inline. Pip the hare "
                "watched, curious whether the tortoise's answer would "
                "differ from the hare's. The form's value to weigh was \"Shelly\"."
            ),
            need=(
                "She needed to call `speed` on a Tortoise instance and "
                "confirm the dispatch selected the tortoise's own "
                "implementation, not the hare's."
            ),
            mapping=(
                "Same pattern: `defrecord Tortoise [name] Pace (speed …)` "
                "embeds the guild routine in the record. The runtime "
                "dispatches `speed` to the Tortoise arm, not the Hare's."
            ),
            resolution=(
                "the call dispatched to the Tortoise record's "
                "implementation and returned the tortoise's distinct "
                "pace keyword."
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form='(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))',
            expected=":swift",
            concept_phrase="the multimethod and its first arm",
            question_what="the pace returned for a runner stamped :hare after the table routes to its arm",
            goal_text="declare a sorting-table named pace that reads each runner's :species stamp; add an arm for the :hare stamp returning the swift-pace keyword; then route a runner stamped :hare through the table",
            scenario=(
                "Mossback the tortoise set up a sorting-table at the "
                "edge of the meadow. Runners would walk up; the table "
                "would read each runner's :species stamp and route them "
                "to the matching arm."
            ),
            need=(
                "Today's first arm she added was for hares: any runner "
                "stamped :hare should be routed to an arm that returns "
                "the swift-pace keyword. Today's first runner arrived "
                "stamped :hare."
            ),
            mapping=(
                "`defmulti` declares the table and what it sorts by "
                "(`:species`). `defmethod` adds an arm for a specific "
                "stamp (`:hare`). Calling `pace` on a runner reads the "
                "stamp and routes to the matching arm."
            ),
            resolution=(
                "the table read the :hare stamp, took the matching arm, "
                "and returned the swift-pace keyword — exactly the "
                "right pace for the species."
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
                "Pip the hare carried a smooth stone to Mossback's "
                "sorting-table. The table read each item's `:kind` stamp; "
                "an arm existed only for the `:stone` stamp."
            ),
            need=(
                "Pip needed to send the stone map through the table and "
                "confirm the dispatch routed to the `:stone` arm."
            ),
            mapping=(
                "`defmulti tag :kind` sets the table to read `:kind`. "
                "`defmethod tag :stone` adds the arm for that stamp. Calling "
                "`tag` on a map with `:kind :stone` routes to that arm."
            ),
            resolution=(
                "the granary's sorting-table read the kernel's stamp and "
                "routed the map to its right shelf; the dispatcher — "
                "answering for every stamp the table had been taught — "
                "handed back the keyword the matching arm declared."
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
    fable="tortoise-hare",
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
                "Mossback extended the sorting-table with two arms: "
                "one for `:hare` and one for `:tortoise`. A tortoise "
                "runner arrived."
            ),
            need=(
                "She needed to route the tortoise runner and confirm "
                "the `:tortoise` arm fired, not the `:hare` arm."
            ),
            mapping=(
                "Two `defmethod` calls add an arm for each stamp. "
                "Calling `pace` with the tortoise map matches `:tortoise` "
                "and dispatches to that arm."
            ),
            resolution=(
                "the table chose the tortoise arm and returned the "
                "tortoise's own pace keyword."
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
                "An owl arrived at Mossback's sorting-table. No arm "
                "existed for owls. Mossback had added a `:default` "
                "arm to catch any stamp without a dedicated route."
            ),
            need=(
                "She needed to route the owl and confirm the `:default` "
                "arm caught it."
            ),
            mapping=(
                "`defmethod pace :default` is the catch-all arm. When "
                "no dedicated arm matches, the table falls through to "
                "`:default` and returns that arm's value."
            ),
            resolution=(
                "no arm matched the owl stamp; the table fell through "
                "to `:default` and returned the fallback keyword."
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
    fable="tortoise-hare",
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
                "Mossback the tortoise set up a sorting-table called "
                "`show` that reads the value itself as its own stamp "
                "— using `identity` as the dispatch function. She added "
                "one arm for the `:rabbit` stamp."
            ),
            need=(
                "She needed to send `:rabbit` through the table and see "
                "whether the identity-dispatch found the matching arm "
                "and returned the right string."
            ),
            mapping=(
                "`defmulti show identity` makes the table use the "
                "argument itself as the stamp. `defmethod show :rabbit` "
                "adds the matching arm. Calling `show` with `:rabbit` "
                "routes to that arm."
            ),
            resolution=(
                "the table dispatched correctly through identity and "
                "returned the string registered for the `:rabbit` stamp."
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
                "Pip the hare tried a guild instead of a sorting-table: "
                "he founded the Show guild, signed the String type in "
                "with its own `show` implementation, then called `show` "
                "on a string runner to see the dispatch at work. The form's value to weigh was \"str-\"."
            ),
            need=(
                "He needed to confirm that calling `show` on a String "
                "dispatched to the String arm — not to an arm added "
                "by the sorting-table approach."
            ),
            mapping=(
                "`defprotocol Show` founds the guild. `extend-protocol` "
                "signs String in with a `show` that prefixes the value. "
                "Calling `show` on a String dispatches to that arm via "
                "the guild, not a table."
            ),
            resolution=(
                "the guild dispatch returned a prefixed string, "
                "confirming the protocol arm fired and produced its "
                "own distinct result."
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
    fable="tortoise-hare",
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
                "Mossback the tortoise founded a guild named `IPace` — a "
                "Clojure-side guild working like the host world's interface. The form's value to weigh was \"hare\"."
            ),
            need=(
                "She needed to extend `IPace` to String and call `run` on "
                "a String runner to show the guild works like a Java interface."
            ),
            mapping=(
                "`defprotocol IPace (run [this])` creates the guild. "
                "`extend-protocol` signs String in, so calling `run` dispatches "
                "through the guild."
            ),
            resolution=(
                "the guild's many-armed registry held arms for many "
                "types; the runtime — moving through the candidates one "
                "by one — found the String arm waiting and returned the "
                "keyword that arm declared."
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
    fable="tortoise-hare",
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
                "Mossback wanted to teach a Long runner — from the host "
                "world — a new guild call. `extend-type` could sign the "
                "Long type in without touching its definition. The form's keyword to weigh was :number-pace."
            ),
            need=(
                "She needed to attach `speed` to Long and call it on "
                "an integer to confirm the extension took effect."
            ),
            mapping=(
                "`extend-type java.lang.Long Pace (speed …)` signs Long "
                "into the guild retroactively. Calling `speed` on a Long "
                "dispatches to this new implementation."
            ),
            resolution=(
                "the dispatch found the Long extension and returned the "
                "keyword for numeric runners."
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
                "Pip wanted to join the Pace guild as a String runner. "
                "Mossback showed him `extend-type` could sign String in "
                "after the guild was founded. The form's value to weigh was \"hare\"."
            ),
            need=(
                "After extending String, Pip needed to call `speed` "
                "on a String runner to confirm the extension was live."
            ),
            mapping=(
                "`extend-type java.lang.String Pace (speed …)` signs "
                "String in retroactively. Calling `speed` on a String "
                "dispatches to this extension, not the Long one."
            ),
            resolution=(
                "the dispatch selected the String extension and returned "
                "the keyword for string runners."
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
    fable="tortoise-hare",
    examples=[
        # The first arg is conventionally `this` in protocol method
        # bodies — illustrate by capturing the field via this.
        SubjectExample(
            form=("(do (defprotocol Named (name-of [this]))"
                  " (defrecord Hare [n] Named (name-of [this] (:n this)))"
                  " (name-of (->Hare \"Zephyr\")))"),
            expected="Zephyr",
            concept_phrase="using this to access a field in a protocol method",
            question_what="the value returned after defining protocol Named with method name-of, defining record Hare with field n that uses this to access the field in the implementation, then calling name-of on a Hare instance",
            goal_text="define a protocol Named with method name-of, define a record that uses this to access a field, then call the method",
            scenario=(
                "Mossback built a Hare carrying-case with a single "
                "field `n`. The `name-of` routine used `this` — the "
                "case itself — to read field `n`."
            ),
            need=(
                "She needed to call `name-of` on the Hare and confirm "
                "the method retrieved the stored name through `this`."
            ),
            mapping=(
                "`[this]` in the method signature binds the receiver. "
                "`(:n this)` reads the `n` field from that receiver — "
                "the case introspects itself."
            ),
            resolution=(
                "the method read field `n` through `this` and returned "
                "the name stored in the case."
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
                "Pip placed a pebble in a Stone case with field `t` "
                "for its tag. The Tagged guild's `tag-of` routine "
                "read that tag back through `this`."
            ),
            need=(
                "Pip needed to call `tag-of` on the Stone and confirm "
                "the `this`-style implementation retrieved the `t` field."
            ),
            mapping=(
                "`defrecord Stone [t] Tagged (tag-of [this] (:t this))` "
                "reads field `t` from the receiver. The case introspects "
                "itself rather than returning a constant."
            ),
            resolution=(
                "the method looked up `t` through `this` and returned "
                "the tag placed in the case at construction."
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
    fable="tortoise-hare",
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
                "Mossback the tortoise founded two separate guilds — A "
                "and B — each with its own routine. She signed the "
                "String type into both guilds independently, giving "
                "each its own implementation. Joining guild A carried "
                "no automatic membership in guild B. The form's value to weigh was \"x\"."
            ),
            need=(
                "She needed to call both `a-op` and `b-op` on the same "
                "String runner and collect the results, to prove the two "
                "guilds dispatch independently and don't inherit from "
                "each other."
            ),
            mapping=(
                "Each `extend-protocol` call signs String into one guild "
                "only. Calling `a-op` dispatches through guild A; calling "
                "`b-op` dispatches through guild B. The results come from "
                "separate implementations, not a shared inheritance."
            ),
            resolution=(
                'both calls returned their own keywords, one from each guild, confirming the protocols are fully independent (with `:a-impl` as the input value).'
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
    fable="tortoise-hare",
    examples=[
        SubjectExample(
            form="(do (derive ::hare ::runner) (isa? ::hare ::runner))",
            expected=True,
            concept_phrase="checking type hierarchy after derive",
            question_what="whether the relationship holds after establishing with derive that ::hare is a type of ::runner, then checking with isa?",
            goal_text="establish a type relationship where ::hare is a type of ::runner, then check it",
            scenario=(
                'Mossback the tortoise kept a hierarchy of stamps at the sorting-table edge. She wanted to declare that the `:hare` stamp was also a kind of `:runner` stamp — so the table could route hare-stamped runners to any arm that accepted runner-stamped ones. The values drawn fresh were ::hare and ::runner.'
            ),
            need=(
                "She needed to register the relationship with `derive` "
                "and then verify it held using `isa?`, so the table "
                "would recognize the parent-child stamp relationship."
            ),
            mapping=(
                "`derive` records the hierarchy: `:hare` is a child "
                "of `:runner`. `isa?` then queries the hierarchy and "
                "returns true if the child-parent relationship exists."
            ),
            resolution=(
                "the hierarchy confirmed the relationship — the hare "
                "stamp was recognized as a kind of runner stamp."
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
                "Pip the hare wondered whether the host world's own "
                "stamp hierarchy was visible at the sorting-table. "
                "Mossback showed him that `isa?` could also query the "
                "Java type hierarchy, not just the meadow's hand-made "
                "hierarchy."
            ),
            need=(
                "They needed to ask whether the Long stamp was a child "
                "of the Number stamp in the host hierarchy, to see if "
                "`isa?` worked across both worlds."
            ),
            mapping=(
                "`isa?` with two Java class names checks the host "
                "type hierarchy. Long extends Number in Java, so the "
                "parent-child relationship holds and `isa?` returns "
                "the affirmative."
            ),
            resolution=(
                "the hierarchy check confirmed Long is indeed a kind "
                "of Number in the host world's own stamp system."
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
                "Mossback the tortoise put the same question to the "
                "host hierarchy but swapped the types. String and Number "
                "live in different branches of the host stamp tree — "
                "no derivation connects them."
            ),
            need=(
                "She needed to ask whether the String stamp was a child "
                "of Number, to confirm `isa?` correctly returns the "
                "negative when no relationship exists."
            ),
            mapping=(
                "`isa?` with String and Number checks whether Java "
                "defines String as a subtype of Number. Because no such "
                "relationship exists in the host hierarchy, the check "
                "returns the negative result."
            ),
            resolution=(
                "the hierarchy confirmed no relationship — String is "
                "not a kind of Number, and the check returned accordingly."
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
    fable="tortoise-hare",
    examples=[
        # A small "many implementations behind one protocol" example.
        SubjectExample(
            form=("(do (defprotocol Move (step [this]))"
                  " (defrecord Hare [] Move (step [_] :leap))"
                  " (defrecord Tortoise [] Move (step [_] :plod))"
                  " (mapv step [(->Hare) (->Tortoise)]))"),
            expected=[":leap", ":plod"],
            concept_phrase="calling a polymorphic method on multiple record types",
            question_what="the vector of results after defining protocol Move with method step, defining records Hare and Tortoise that both implement Move, then calling step via mapv on both instances",
            goal_text="define a protocol Move with method step, define two record types Hare and Tortoise that each implement it, then call the method on both instances",
            scenario=(
                "Race day at the meadow. Mossback the tortoise founded "
                "the Move guild. Both a Hare and a Tortoise record signed "
                "with their own `step` implementations. The form's keyword to weigh was :leap."
            ),
            need=(
                "She needed to call `step` on each runner and collect both "
                "results to show one call dispatching to different implementations."
            ),
            mapping=(
                "`mapv step` applies `step` to each element. The runtime "
                "dispatches to each record's implementation, returning a "
                "different value per type."
            ),
            resolution=(
                "the vector held each runner's result, confirming one call "
                "produced two distinct answers."
            ),
            tags=("story",),
        ),
        SubjectExample(
            form=("(do (defprotocol Sound (cry [this]))"
                  " (defrecord Hare [] Sound (cry [_] :thump))"
                  " (defrecord Tortoise [] Sound (cry [_] :hiss))"
                  " (cry (->Tortoise)))"),
            expected=":hiss",
            concept_phrase="calling a polymorphic method on a record instance",
            question_what="the value returned after defining protocol Sound with method cry, defining records Hare and Tortoise that both implement Sound, then calling cry on a Tortoise instance",
            goal_text="define a protocol Sound with method cry, define two record types that implement it, then call the method on a Tortoise instance",
            scenario=(
                "Pip the hare and Mossback the tortoise both joined the "
                "Sound guild, each with a different `cry` routine. A "
                "single Tortoise instance waited at the gate, ready to "
                "answer when `cry` was called. The form's keyword to weigh was :thump."
            ),
            need=(
                "The caller needed to invoke `cry` on the Tortoise "
                "instance alone and confirm the dispatch chose the "
                "Tortoise's implementation, not the Hare's."
            ),
            mapping=(
                "Both records implement Sound but with different bodies. "
                "Calling `cry` on a Tortoise instance dispatches to the "
                "Tortoise arm of the guild, ignoring the Hare's arm "
                "entirely."
            ),
            resolution=(
                "the dispatch selected the Tortoise arm and returned "
                "the keyword registered for tortoise runners."
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
