"""Grade 8 — protocols, multimethods, abstraction. Through dog-shadow.

The fable's moral dynamic — Hare's vanity vs Tortoise's steadiness —
maps cleanly onto polymorphism: different species respond to the same
call differently. Hare boasts that "everyone runs the same way";
Tortoise insists each kind of creature has its own implementation.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import (
    SubjectCurriculum, SubjectExample, SubplotTemplate,
)
from mmllm.aesop.curriculum.dog_shadow.grade_1 import (
    _SHARED_SUBPLOTS as _G1_SUBPLOTS, _GOAL_SUBPLOTS, _PLAN_POOL,
)
from mmllm.aesop.curriculum.dog_shadow._metaphor_pools import (
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
    fable="dog-shadow",
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
                'Bell the hound scratched a small set of pack-signals into '
                'a flat stone near the pond: every breed in the pack would '
                'honor the same call but answer in its own voice. She named '
                'the call speak.'
            ),
            need=(
                'When the call went out, the runtime would dispatch by the '
                "dog's breed — :hare or :tortoise — and each breed would "
                'give back its own characteristic phrase, no two alike.'
            ),
            mapping=(
                "The pack agreement is the function's shape, the call's "
                "name is speak, the dog's breed is the dispatch key, and "
                "each breed's voice is the answer associated with its key."
            ),
            resolution=(
                'The REPL set the agreement on the bank and the function '
                'value came back. Any later call to speak with a known '
                "breed would now produce that breed's characteristic "
                'phrase — hare — hare.'
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
                'Bell the hound held a local signal-set in her mind, ready '
                'to use just for the next call. She gripped the packed '
                'signals between her jaws — the speak-agreement with its '
                'two breed routes — :hare and :tortoise — each with its '
                'own response.'
            ),
            need=(
                'She wanted to dispatch the signal with a specific breed '
                'key and fetch back the answer without remembering the '
                'signals after the call was done.'
            ),
            mapping=(
                'The closed jaws are the let, the local signal-set is the '
                'fn, the breed key :tortoise is the dispatch input, and '
                'the answer is what the pack-signal returns.'
            ),
            resolution=(
                'The REPL held the signals in force, routed by the key, '
                'and handed back the characteristic answer. Past the call, '
                'Bell\'s mind was empty — the local binding had served its '
                'stretch and was gone — hare.'
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
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(do (deftype Pebble [color]) (.-color (Pebble. \"grey\")))",
            expected="grey",
            concept_phrase="reading the color field of a Pebble instance",
            question_what="the color field value after defining a type Pebble with one field color, then constructing an instance and reading the field",
            goal_text="define a type Pebble with a color field and then read the color field from an instance",
            scenario=(
                'Bell the hound carved a small kennel-bag with a single '
                'labeled compartment — one slot, marked color — and slipped '
                "a stone of a particular shade into the slot. The bag's "
                'outside bore the kind-stamp Pebble.'
            ),
            need=(
                "She wanted to read the slot's contents back — exactly the "
                "shade the stone bore — by the slot's name, with the "
                'runtime fetching the field cleanly from the bag she had '
                'just constructed.'
            ),
            mapping=(
                'The bag is the deftype, its labeled compartment is the '
                'field, the kind-stamp is the type name, and field-access '
                'is asking the bag for the slot by name.'
            ),
            resolution=(
                'The REPL constructed the bag, fetched the named compartment, and handed back the shade the stone had borne. The bag itself kept its kind-stamp on the outside for any later read (with `grey` as the input value).'
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
                'Bell the hound carved a labeled kennel-bag with one '
                'compartment marked weight — a slot for holding the heft '
                'of a stone. She slipped a stone of weight 7 into the '
                'compartment and sealed the bag with the kind-stamp Stone.'
            ),
            need=(
                'She wanted to fetch back the heft by its slot name, with '
                'the runtime reaching straight into the bag\'s compartment '
                'and pulling out the number it held.'
            ),
            mapping=(
                'The bag is the deftype, its labeled compartment is the '
                'field, the kind-stamp is the type name, and the heft is '
                'what the field stores.'
            ),
            resolution=(
                'The REPL constructed the bag, read the named compartment, '
                'and handed back the precise weight the stone had borne. '
                'The bag itself kept its kind-stamp for any later read — 7.'
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
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form='(do (defrecord Runner [name pace]) (:pace (->Runner "Alice" :slow)))',
            expected=":slow",
            concept_phrase="reading the pace compartment of a Runner case",
            question_what="the value in the pace compartment of a freshly-built Runner case for Alice",
            goal_text="define a Runner case with two named compartments, name and pace; build a Runner case for Alice with a deliberate-pace keyword; then read the pace compartment",
            scenario=(
                'Bell the hound crafted a labeled kennel-bag for tracking '
                'runners. The bag had two named compartments — one for a '
                'runner\'s name, one for the runner\'s pace-style. She '
                'slipped "Alice" and :slow into the slots and sealed it '
                'with the case-type Runner.'
            ),
            need=(
                'She wanted to read back the pace-style by its compartment '
                'name without disturbing the other field. The runtime would '
                'fetch the second slot cleanly.'
            ),
            mapping=(
                'The bag is the defrecord, its two slots are the fields, '
                'the type-marker is the case name, and the pace-value is '
                'what the second field holds.'
            ),
            resolution=(
                'The REPL built the bag, read the named compartment, and '
                'handed back the pace-style. The bag kept both slots '
                'intact — pulling one didn\'t disturb the other — pace.'
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
                'Bell the hound made a second bag with two labeled slots '
                '— one for a runner\'s name, one for pace-style. She '
                'packed "Bob" and :moderate into the compartments and '
                'sealed it with the Runner marker.'
            ),
            need=(
                'She wanted to extract the name from the first compartment '
                'and hold just that value in her paws, leaving the '
                'pace-style undisturbed in its slot.'
            ),
            mapping=(
                'The bag is the defrecord, its two compartments are the '
                'fields, the name is the first slot\'s value, and reading '
                'by name is how the runtime fetches the right compartment.'
            ),
            resolution=(
                'The REPL built the bag, read the name-slot by its label, '
                'and handed back the name. The second slot stood ready for '
                'later reads — name.'
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
    fable="dog-shadow",
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
                'Bell the hound carved a pack agreement on a flat stone at the '
                'bank. All members would honor a single call — speed — each '
                'answering in its own way.'
            ),
            need=(
                'The pack needed proof that the guild agreement was real in '
                'the runtime.'
            ),
            mapping=(
                'The flat stone is the defprotocol, Pace is the guild name, '
                'and the protocol var is the guild\'s realness.'
            ),
            resolution=(
                'The REPL set the agreement and handed back the guild as '
                'proof. The agreement was real and ready.'
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
                'Patch the hound gathered the pack at the bank near the '
                'pond and announced a new guild: every member would answer '
                'to a single call named Greet. The only requirement was '
                'that each member could hail in response.'
            ),
            need=(
                'The pack needed the guild itself to exist as a binding in '
                'the runtime — proof that the agreement had been struck and '
                'was ready for any member to join.'
            ),
            mapping=(
                'The guild agreement is the defprotocol, the call-name is '
                'Greet, the method requirement is hail, and the guild\'s '
                'realness is the protocol var itself.'
            ),
            resolution=(
                'The REPL set the guild agreement on the bank. The '
                'protocol var came back as true — the agreement was real '
                'and binding, ready for any member to implement it.'
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
    fable="dog-shadow",
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
                'Bell set up the Pace guild and pressed its mark onto the '
                'text-pack. Any text at the speed call would answer with its '
                'own characteristic word.'
            ),
            need=(
                'When text arrived, the guild mark would route to the String '
                'implementation.'
            ),
            mapping=(
                'The guild is the defprotocol, the text-pack is the marked '
                'type, and the method is what answers the call.'
            ),
            resolution=(
                'The REPL marked the text-pack and called speed on text. The text answered, proving the extension was live (with `swift` as the input value).'
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
                'Rex the hound founded the Greet guild and pressed its mark onto the '
                'number-pack.'
            ),
            need=(
                'When a number met the hail call, the runtime would recognize the '
                'guild-mark and route to the implementation.'
            ),
            mapping=(
                'The guild is the defprotocol, the number-pack is the type, the mark '
                'is the extend-protocol, and the number-voice is the method.'
            ),
            resolution=(
                'The REPL stamped the mark on the number-type, then dispatched a number to hail. The number answered in its own voice (with `7` as the input value).'
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
    fable="dog-shadow",
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
                'Bell the hound carved a guild agreement named Pace with a '
                'speed method. She marked both the String-breed and the '
                'Long-breed with the guild mark — each with a different '
                'speed-answer ready.'
            ),
            need=(
                'When a number arrived, the runtime would read its breed, '
                'recognize the mark, and route to the Long-breed\'s '
                'speed-answer.'
            ),
            mapping=(
                'The guild is the defprotocol, the two breeds are the types '
                'being extended, the marks are the extend-protocol clauses, '
                'and each breed\'s answer is its speed implementation.'
            ),
            resolution=(
                "The REPL set the guild and both marks, then dispatched a number. The Long-breed's speed-answer came back, proving the protocol routed correctly (with `42` as the input value)."
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
                'Patch the hound set the same Pace guild and marked both the '
                'String-breed and the Long-breed — each with its own '
                'distinctive speed-call ready to give back.'
            ),
            need=(
                'When a text-pack arrived at the speed call, the runtime '
                'would check its breed-mark and route to the String '
                'implementation.'
            ),
            mapping=(
                'The guild is the protocol, the two types are String and '
                'Long, the marks are the extend-protocol stamps, and the '
                'String-answer is what the String-breed returns.'
            ),
            resolution=(
                "The REPL dispatched a text-pack to the speed call. The String-breed's implementation fired, and the text-answer came back (with `:string-pace` as the input value)."
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
    fable="dog-shadow",
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
                'Bell the hound set up a guild called Pace with a speed '
                'requirement. She then made a record case for the Hare breed '
                '— a bag with a name slot — and marked it to honor the '
                'guild agreement.'
            ),
            need=(
                'When a Hare instance crossed the stream, the speed call '
                'would recognize the guild mark on the record and route to '
                'the Hare\'s speed-answer.'
            ),
            mapping=(
                'The guild is the defprotocol, the bag-case is the '
                'defrecord, the guild mark is the protocol implementation, '
                'and the speed-word is what the record returns.'
            ),
            resolution=(
                "The REPL built the record case with the guild mark, then called speed on a Hare. The guild routed to the Hare's implementation, and the breed's word came back (with `swift` as the input value) (with `:swift` as the input value)."
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
                'Rex the hound created the Pace guild. He built a record case for '
                'Tortoise and sealed it with the guild mark.'
            ),
            need=(
                'When a Tortoise arrived at the speed call, the runtime would route '
                'to the answer.'
            ),
            mapping=(
                'The guild is the defprotocol, the Tortoise bag is the defrecord, '
                'the mark is the protocol implementation.'
            ),
            resolution=(
                'The REPL built the Tortoise case with the mark, then called speed. The steady-answer came back (with `:steady` as the input value).'
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
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form='(do (defmulti pace :species) (defmethod pace :hare [_] :swift) (pace {:species :hare}))',
            expected=":swift",
            concept_phrase="the multimethod and its first arm",
            question_what="the pace returned for a runner stamped :hare after the table routes to its arm",
            goal_text="declare a sorting-table named pace that reads each runner's :species stamp; add an arm for the :hare stamp returning the swift-pace keyword; then route a runner stamped :hare through the table",
            scenario=(
                'A flat stone sat at the bank near the pond. Bell the hound '
                'chose the species stamp as the dispatch key and added one '
                'pile for the hare breed with its own pace-word.'
            ),
            need=(
                'When a runner of a known breed arrived, the stone would '
                "route the runner to the matching pile and that pile's "
                'pace-word would come back.'
            ),
            mapping=(
                'The sorting-stone is the multimethod, the species stamp is '
                "the dispatch key, each breed's pile is a defmethod, and "
                'the pace-word is what the runtime returns.'
            ),
            resolution=(
                'The REPL read the species, picked the matching pile, and handed back its pace-word. The stone stood ready for any later breed — hare (with `:species` as the input value).'
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
                'Patch the hound carved a second sorting-stone at the bank, '
                'choosing :kind as the dispatch key. He added a pile for '
                'bones tagged :stone, each bearing the hard-quality marker.'
            ),
            need=(
                'When a bone-bundle arrived with a :stone tag, the stone '
                'would read the tag and route to the stone-pile\'s quality.'
            ),
            mapping=(
                'The sorting-stone is the defmulti, the dispatch key is '
                ':kind, each pile is a defmethod, and the quality-word is '
                'what the pile returns.'
            ),
            resolution=(
                'The REPL set the sorting-stone and the stone-pile, then '
                'routed a tagged bundle through. The stone read the :stone '
                'tag and handed back the hard-quality word.'
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
    fable="dog-shadow",
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
                'Bell the hound carved a sorting-stone for runners, using '
                ':species as the dispatch key. She added two piles — one for '
                ':hare runners with the swift-word, one for :tortoise '
                'runners with the steady-word.'
            ),
            need=(
                'When a runner stamped :tortoise arrived, the stone would '
                'read the stamp, route to the tortoise-pile, and hand back '
                'the steady-answer.'
            ),
            mapping=(
                'The sorting-stone is the defmulti, the :species key is the '
                'dispatch mark, each breed\'s pile is a defmethod, and the '
                'pace-word is what returns.'
            ),
            resolution=(
                'The REPL set the stone and both piles, then routed a '
                ':tortoise runner through. The stone read the stamp and '
                'handed back the steady-word.'
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
                'Rex the hound set up the same sorting-stone but added a '
                'third pile marked :default — for any runner whose breed '
                'wasn\'t known, the stone would return unknown.'
            ),
            need=(
                'When a runner arrived with an unexpected breed-stamp like '
                ':owl, the stone would search for its pile. Finding none, it '
                'would route to the default-pile instead.'
            ),
            mapping=(
                'The sorting-stone is the defmulti, :species is the dispatch '
                'key, the :hare and :tortoise piles are defmethods, and the '
                ':default pile catches unknown runners.'
            ),
            resolution=(
                'The REPL set the stone and all three piles, then routed an '
                ':owl runner through. The stone found no :owl pile, so it '
                'routed to :default and handed back the unknown-word.'
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
    fable="dog-shadow",
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
                'Bell the hound built a sorting-stone using identity as the '
                'dispatch rule — every value would be routed by what it is, '
                'exactly. She added one pile for the :rabbit tag with that '
                'pile\'s own characteristic word.'
            ),
            need=(
                'When the :rabbit value arrived, the stone would recognize '
                'it and hand back that matching pile\'s answer.'
            ),
            mapping=(
                'The sorting-stone is the defmulti, the dispatch rule is '
                'identity, the pile is the defmethod, and the pile\'s word '
                'is what the runtime returns.'
            ),
            resolution=(
                'The REPL set the stone and the :rabbit pile, then routed '
                'the :rabbit value through. The stone recognized the exact '
                'value and handed back the matching pile\'s word.'
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
                'Patch the hound founded a guild called Show with a show '
                'requirement. She marked the String-pack with the guild mark '
                'and gave it a special show-answer that prefixed each pack.'
            ),
            need=(
                'When a text-pack arrived at the show call, the guild mark '
                'would route it to the String implementation, which would '
                'wrap it.'
            ),
            mapping=(
                'The guild is the defprotocol, the String-pack is the type '
                'being extended, the mark is the extend-protocol, and the '
                'wrapped answer is what returns.'
            ),
            resolution=(
                'The REPL set the guild and marked the String-pack, then '
                'called show on "hare". The guild routed to the String '
                'implementation, which wrapped it and returned the wrapped '
                'word.'
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
    fable="dog-shadow",
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
                'Bell the hound carved a guild called IPace — its run method '
                'would be the agreement between all members. She pressed the '
                'guild\'s mark onto the String-breed and gave it a run-answer.'
            ),
            need=(
                'When a text-pack arrived at the run call, the mark would '
                'route it to the String implementation, which would say it '
                'had run.'
            ),
            mapping=(
                'The guild is the defprotocol, the String-breed is the type '
                'marked, the mark is the extend-protocol, and the run-word '
                'is what returns.'
            ),
            resolution=(
                'The REPL set the guild and marked the String-breed, then '
                'called run on "hare". The String implementation answered, '
                'and the run-word came back.'
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
    fable="dog-shadow",
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
                'Rex the hound crafted a guild called Pace with a speed '
                'requirement. He used a different marking method — extend-type '
                '— to stamp the Long number-breed directly, giving it a '
                'number-pace answer.'
            ),
            need=(
                'When a number arrived at the speed call, the marking would '
                'route it to the number-breed\'s implementation.'
            ),
            mapping=(
                'The guild is the defprotocol, the Long-breed is the type '
                'marked, the extend-type is the alternate marking method, '
                'and the pace-word is what returns.'
            ),
            resolution=(
                'The REPL set the guild and stamped the Long-breed with '
                'extend-type, then called speed on 5. The number answered '
                'with its pace-word.'
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
                'Patch the hound set the same Pace guild and used extend-type '
                'to mark the String text-breed. Each text-pack would now '
                'honor the speed requirement with a text-answer.'
            ),
            need=(
                'When a text-pack met the speed call, the extend-type mark '
                'would route it to the String implementation.'
            ),
            mapping=(
                'The guild is the defprotocol, the String-breed is marked '
                'via extend-type, the mark is the connection to the guild, '
                'and the text-answer is what returns.'
            ),
            resolution=(
                'The REPL set the guild and marked the String-breed, then '
                'called speed on "hare". The String implementation fired, and '
                'the text-pace-word came back.'
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
    fable="dog-shadow",
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
                'Rex carved a Named guild with a record case for runners. The '
                'case had one field, n, and bore the guild mark.'
            ),
            need=(
                'When a runner arrived at name-of, the guild routed to the '
                'record\'s body, where this meant the runner itself.'
            ),
            mapping=(
                'The guild is the defprotocol, the record is the defrecord, '
                'this points to the current record, and the field value '
                'returns.'
            ),
            resolution=(
                'The REPL built the Hare, called name-of, and this let the method read the n field from the record. The name came back (with `:n` as the input value).'
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
                'Bell founded a guild called Tagged with a tag-of requirement. '
                'She made a record case for stones with a t field.'
            ),
            need=(
                'When a Stone arrived at tag-of, the guild would route to the '
                'record\'s body, where this was the stone itself.'
            ),
            mapping=(
                'The guild is the defprotocol, the Stone bag is the defrecord, '
                'this is a reference to the current record instance.'
            ),
            resolution=(
                'The REPL built a Stone with a tag in the t field, then called tag-of. The guild routed to the body and returned the stored tag (with `:t` as the input value).'
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
    fable="dog-shadow",
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
                'Bell the hound founded two separate guilds: A with an a-op '
                'requirement, and B with a b-op requirement. She marked the '
                'String-pack independently with both guild marks — each mark '
                'held its own implementation, and the marks didn\'t interfere.'
            ),
            need=(
                'When a text-pack arrived, it could answer to either guild '
                'separately. Calling a-op would use the A-mark\'s answer, and '
                'calling b-op would use B-mark\'s answer.'
            ),
            mapping=(
                'The two guilds are the two defprotocols, the String-pack is '
                'marked twice — once for each guild, the marks are '
                'independent, and each returns its own implementation.'
            ),
            resolution=(
                'The REPL set both guilds and marked the String-pack twice, then called both methods on "x". The String answered to both guilds independently, and the vector came back with both answers (with `:a-impl` as the input value).'
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
    fable="dog-shadow",
    examples=[
        SubjectExample(
            form="(do (derive ::hare ::runner) (isa? ::hare ::runner))",
            expected=True,
            concept_phrase="checking type hierarchy after derive",
            question_what="whether the relationship holds after establishing with derive that ::hare is a type of ::runner, then checking with isa?",
            goal_text="establish a type relationship where ::hare is a type of ::runner, then check it",
            scenario=(
                'Bell the hound scratched two related names on the sorting-stone '
                'near the pond: ::hare and ::runner. She used derive to mark '
                '::hare as a kind of ::runner — linking them in the stone\'s '
                'hierarchy.'
            ),
            need=(
                'She wanted to verify the link was real. The isa? question '
                'would ask whether ::hare was a type of ::runner — the '
                'verdict would prove the hierarchy was set.'
            ),
            mapping=(
                'The two names are the keywords, derive is the linking mark, '
                'isa? is the verification question, and the verdict is the '
                'relationship itself.'
            ),
            resolution=(
                'The REPL carved the hierarchy link and answered the isa? '
                'question. The verdict came back with the verdict — ::hare was confirmed '
                'as a type of ::runner — runner.'
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
                'Rex the hound was reading the breeding records at the bank. '
                'He asked the isa? question: is the Long-breed a kind of '
                'Number-pack? The Java record would answer by checking the '
                'breed\'s ancestry.'
            ),
            need=(
                'To know whether Long traced back to Number in the family '
                'tree, the runtime would consult the type hierarchy.'
            ),
            mapping=(
                'The isa? question is the method call, the Long-breed is the '
                'first argument, the Number-ancestry is the second, and the '
                'verdict is true or false.'
            ),
            resolution=(
                'The REPL checked the breeding records and found that Long '
                'did indeed trace back to Number. The verdict came back with the verdict.'
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
                'Patch the hound asked a second isa? question at the bank: '
                'is the String-pack a kind of Number? The Java records would '
                'show if there was any family connection.'
            ),
            need=(
                'To know whether String and Number shared ancestry, the '
                'runtime would search the breeding records.'
            ),
            mapping=(
                'The isa? question is the method, the String-pack is the '
                'first argument, the Number-family is the second, and the '
                'verdict tells whether they\'re related.'
            ),
            resolution=(
                'The REPL searched the Java hierarchy and found no ancestor '
                'connection between String and Number. The verdict came back '
                'false.'
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
    fable="dog-shadow",
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
                'Patch carved a Move guild and built two record cases — one '
                'for swift runners, one for steady — each marking the guild.'
            ),
            need=(
                'When both runners met the step call, each would answer by its '
                'own movement.'
            ),
            mapping=(
                'The guild is the defprotocol, the records are the defrecords, '
                'the marks are implementations, and each breed\'s movement is '
                'what step returns.'
            ),
            resolution=(
                'The REPL set the guild and both records, called step on both via mapv. The guild routed each to its implementation (with `leap` as the input value) (with `:leap` as the input value).'
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
                'Bell carved a guild called Sound. She built two record cases: '
                'Hare with thump-sound, Tortoise with hiss-sound.'
            ),
            need=(
                'When a Tortoise arrived at cry, the guild would route to the '
                'Tortoise case\'s answer.'
            ),
            mapping=(
                'The guild is the defprotocol, the record cases are defrecords, '
                'and each breed\'s sound is what returns.'
            ),
            resolution=(
                'The REPL set the guild and both cases, then called cry on Tortoise. The hiss-sound came back (with `:thump` as the input value).'
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
    print(f"grade-8 dog-shadow smoke OK: {len(SUBJECTS)} subjects, "
          f"{sum(len(s.examples) for s in SUBJECTS.values())} examples total")


if __name__ == "__main__":
    smoke_test()
