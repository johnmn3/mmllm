"""Metaphor-bearing subplot pools for dog-shadow.

The base `_GOAL_SUBPLOTS` (in grade_1.py) is generic hound/dog banter
that uses `{goal_text}` and `{concept_phrase}` but doesn't illuminate
any particular Clojure idiom. These pools below DO illuminate specific
idioms by carrying a fable-natural metaphor drawn from the dog-shadow
fable: a dog crossing a stream with a real bone, snapping at his own
reflection, and losing what he had.

Imagery anchors (see also
`docs/clojure-pedagogy/audits/metaphor-imagery-dog-shadow.md`):

  Tier 1 (high-leverage core):
  - _POUCH_SUBPLOTS         — bone in the mouth (let-binding)
  - _RECIPE_SUBPLOTS        — nose-trail of paw-step sniffs (fn / comp)
  - _BASKET_SUBPLOTS        — bone-cache in a hollow log (collections)
  - _SIEVE_SUBPLOTS         — gap in a log over the stream (HOFs)
  - _NOTEBOOK_SUBPLOTS      — tally-scratch on a flat stone (atom / ref)
  - _ACORN_SUBPLOTS         — counting bones at the stream's edge
  - _GATE_SUBPLOTS          — conditions at the stream crossing (boolean)
  - _FORK_SUBPLOTS          — fork in the path at the bank (if / cond)
  - _ROADSIGN_SUBPLOTS      — marker stone by the stream (def / namespace)
  - _SAFETYNET_SUBPLOTS     — log-bridge test before crossing (try/catch)

  Tier 2 (substantial):
  - _SCROLL_SUBPLOTS        — message-bone with scratch-marks (IO)
  - _GUILD_SUBPLOTS         — pack agreement on signals (protocols)
  - _TOOLSHED_SUBPLOTS      — kennel-master's tools (host interop)

  Tier 3 (small but worth doing):
  - _REWRITERULE_SUBPLOTS   — scent-mark that rewrites itself (macros)
  - _SCRIBE_SUBPLOTS        — scratch-marks on bark conventions (reader)
  - _CHALKMARK_SUBPLOTS     — "bone" scratch vs. real bone (quote)
  - _RUNNERAHEAD_SUBPLOTS   — scout-dog sent ahead (agent / future)
  - _SORTINGTABLE_SUBPLOTS  — sorting bones by origin (multimethods)
  - _CARRYINGCASE_SUBPLOTS  — labeled kennel-bag (deftype / defrecord)
  - _TALLYWALK_SUBPLOTS     — walking the bone-row (reduce / count)
  - _BEADSTRING_SUBPLOTS    — string of scratch-marks (str concat)
  - _CIRCUIT_SUBPLOTS       — pacing the bank (recur / loop)

Pool sizing: 5 templates is the standard size; small families with
1-3 subjects use 3 templates. All templates use `{goal_text}` and
`{concept_phrase}` (never `{form_display}`), keeping the form-leak
design intact.

Authoring rules followed:
- pronoun case at sentence start uses `_he_she_cap` etc.
- no "and" right after `{concept_phrase}` (avoids stutters); use
  ", then submit", "; submit", or comma + new clause.
- no "write a form to {goal_text}" (avoids verb collision when
  goal_text starts with "write"); reframe as "to {goal_text},"
  + noun-clause.
- the metaphor is concretely named in every template (mouth-and-bone /
  nose-trail / hollow-log cache / log-gap / tally-scratch) so it lands
  as imagery, not as decoration.
- {hound} is the wise dog (tortoise-analog: patient evaluator);
  {dog} is the greedy dog (hare-analog: snatches at the shadow).
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import SubplotTemplate


# ─────────────────────── bone-in-the-mouth (let) ──────────────────────


_POUCH_SUBPLOTS: list[SubplotTemplate] = [

    # 1. Hound carries the bone in the mouth for one stretch of the
    #    crossing; the binding lives only as long as the form's stretch.
    SubplotTemplate("""\
{hound} stooped to pick up a bone {place}, then held it
firmly between {hound_his_her} jaws. "When I want to {goal_text},"
{hound_he_she} said around the bone, "I carry the value between
my teeth just for the stretch of crossing where I need it. The
moment the form is past, my mouth is empty again."
{hound_he_she_cap} composed {concept_phrase}, the binding held
firm in the mouth, and submitted the form. {dog_phrase}, {emo_greedy},
had already let {dog_his_her} jaws fall open at a passing
reflection — but the form, which still carried the value, came
back with the answer."""),

    # 2. Closed-jaws-as-binding: whatever's gripped is in force only while the
    #    jaws are closed. Type-neutral framing.
    SubplotTemplate("""\
{hound}, {emo_patient}, tightened {hound_his_her} grip on
the bone — the river was loud, the bridge unsteady, and a slack
jaw at the wrong moment loses everything. "Whatever I hold here
is in force only while my jaws stay closed," {hound_he_she} said,
"and only for the form that names the binding. Step past the
form's edge and the mouth is empty again." To {goal_text},
{hound_he_she} composed {concept_phrase} with the binding gripped
through that stretch. The REPL read out the
value the mouth had held."""),

    # 3. Dog drops the bone for the shadow; Hound's careful hold wins.
    SubplotTemplate("""\
{dog}, {emo_greedy}, eyed the bone in {dog_his_her} jaws
and the brighter one shimmering on the water below — sure the
shadow was the better catch. {dog_he_she_cap} snapped at it, and
the real bone fell with a splash. {hound_phrase}, {emo_patient},
held {hound_his_her} grip steady and did the careful work
instead: to {goal_text}, the binding had to be gripped only for
its own stretch, not chased after a reflection. {hound} composed
{concept_phrase}. The REPL handed back
the value the held bone — not the lost one — had carried."""),

    # 4. Substitution rule — wherever the form names the binding,
    #    the runtime reaches into the mouth.
    SubplotTemplate("""\
"Wherever the form names the binding," {hound}, {emo_patient} said,
"the runtime reaches into the mouth and pulls out what was
gripped there." {hound_he_she_cap} demonstrated by intending to
{goal_text}: each mention of the bound name, {hound} said, would
be replaced by the value from the jaws the moment the form ran.
{hound} composed {concept_phrase}, submitted the form,
and the REPL substituted as promised — the gripped value threaded
into every place the binding had been named."""),

    # 5. End-of-stretch — the mouth is empty when the form's stretch
    #    is over. (Scope ends.)
    SubplotTemplate("""\
"Watch the mouth carefully," {hound} said {place}.
"While the form's stretch runs, the bone is held and the binding
is yours." To {goal_text}, {hound_he_she} composed
{concept_phrase} with the binding gripped safely between the
teeth, then submitted the form. The REPL returned the value, and
the mouth — its work done — was empty again. {dog_phrase},
{emo_regretful}, finally admitted that the careful hold had
carried the day."""),
]


# ─────────────────────── nose-trail (fn) ─────────────────────────────


_RECIPE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. Following a nose-trail: paw-step sniffing path; the runtime
    #    walks each sniff in order. Type-neutral.
    SubplotTemplate("""\
{hound}, {emo_patient} put {hound_his_her} nose to the ground {place} and
worked out a careful sniffing-trail toward the buried bone.
"Recipes in Clojure are like a nose-trail," {hound_he_she} said:
"each sniff is a step, the steps come in order, and the last
sniff is what you serve." To {goal_text}, {hound_he_she}
laid out {concept_phrase} along the trail, submitted the form,
and the REPL followed the sniffs and handed back the value the
last step had produced."""),

    # 2. The trail-as-runnable-routine — emphasizes the call site.
    SubplotTemplate("""\
"A nose-trail is only useful when it gets walked," {hound}, {emo_patient}
said, head low. "You set out the sniffs, you bring the
ingredients, the runtime does the rest." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL — taking the trail and its inputs — handed back what
the steps had produced."""),

    # 3. Last sniff is what gets served. (Body returns last form.)
    SubplotTemplate("""\
"On any nose-trail," {hound}, {emo_patient} explained, "the last sniff
is what you carry home." {hound_he_she_cap} took the goal — to
{goal_text} — and laid out the routine's paw-steps in order,
knowing that whatever the final sniff turned up was what would
come back. {hound} composed {concept_phrase}, submitted the form,
and the REPL — discarding the earlier sniffs — handed back only
the value of the last."""),

    # 4. Trails feeding into trails — chained nose-trails.
    SubplotTemplate("""\
"Trails can feed into one another," {hound}, {emo_patient} said,
sketching two paw-paths in the dirt. "What one trail turns up,
the next can take as its scent — together they make a longer
sniffing-route." To {goal_text}, {hound_he_she} composed
{concept_phrase}. The REPL — walking the
trail in order — handed back the value at the end."""),

    # 5. The Dog-skips-the-trail template.
    SubplotTemplate("""\
{dog}, {emo_greedy}, insisted {dog_he_she} could just
bound straight to the bone without bothering to follow the
sniff-trail. {hound_phrase} only smiled and lowered
{hound_his_her} nose. To {goal_text}, {hound_he_she} composed
{concept_phrase}. The REPL — running the
trail sniff by sniff — handed back the value {dog} had been
guessing at."""),
]


# ─────────────────────── bone-cache (collections) ─────────────────────


_BASKET_SUBPLOTS: list[SubplotTemplate] = [

    # 1. Bone-cache in a hollow log: pulling one bone out doesn't
    #    disturb the rest.
    SubplotTemplate("""\
{hound}, {emo_patient}, pointed to a hollow log {place},
its inside lined with bones tucked into named slots — the wood
cool, the slots solid. "Whatever I want to do with what's cached,"
{hound_he_she} said, "I read from the log, work the change, and
the cache itself stays as it was — what I get back is a fresh
arrangement, not a chewed-up original." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and let the REPL handle the cache exactly as the operation
prescribed."""),

    # 2. Slots and positions — works for tagged caches (maps),
    #    bone-rows (vectors), or kind-only piles (sets).
    SubplotTemplate("""\
"You can find what you want in a bone-cache several ways,"
{hound} said, {emo_patient}, gesturing at the hollow log:
"by the scratch above the slot, by its place in line, or by
simply asking whether it's there at all — the cache is patient,
but only one of those reaches lands the right bone." To
{goal_text}, {hound_he_she} wrote {concept_phrase} for the cache,
submitted the form, and the REPL applied the lookup or update
exactly as the form directed."""),

    # 3. Procession of bones — for ordered collections.
    SubplotTemplate("""\
A row of bones lay tucked end-to-end inside the log {place}, head
at the front, the rest trailing behind. The river ran past, and
the bones stayed in their order, each one waiting to be read.
"Many of our caches are like this row," {hound} said,
{emo_patient}. "You can grab the first bone, you can ask for the
rest, you can lay a new bone at the front of the row." To
{goal_text}, {hound_he_she} composed {concept_phrase}, submitted
the form, and the REPL ran the row exactly as the form
described."""),

    # 4. New cache from old — immutability emphasis.
    SubplotTemplate("""\
"Watch carefully," {hound} said, holding open the hollow
log. "Whatever I do to the cache, this one stays exactly as it
was — what I get back is a fresh cache with the change made,
leaving the first one untouched." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL returned a new arrangement while the original
waited, untouched. {dog_phrase}, {emo_tired}, was beginning to
see why nothing could be lost by trying."""),

    # 5. The Dog-rummages-loudly template.
    SubplotTemplate("""\
{dog} began rummaging in the bone-cache, {emo_greedy},
calling out guesses about its contents without quite checking.
"I know exactly what's in there," {dog_he_she} insisted.
{hound_phrase} shook {hound_his_her} head. To {goal_text}
properly, {hound_he_she} wrote {concept_phrase} carefully on a
flat stone. The REPL — looking into the
log the way the form told it to — handed back the answer {dog}
had been guessing at."""),
]


# ─────────────────────── log-gap (sieve / map / filter) ───────────────


_SIEVE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The general gap-in-a-log — works for transform (map),
    #    select (filter), select-counted (take/drop), or dedupe
    #    (distinct). The rule is the gap.
    SubplotTemplate("""\
{hound}, {emo_patient}, stood beside a fallen log laid
across the stream {place} — a gap chewed through its middle, the
water cool and steady beneath. "Whatever rule we choose for the
gap," {hound_he_she} said, "the bones from the near bank pass
through one at a time: some are changed, some kept, some held
back, depending on the gap." To {goal_text}, {hound_he_she}
composed {concept_phrase} as the gap's rule, ran the bones
through. The REPL returned what the
gap had let pass."""),

    # 2. The float-through-and-collect template — pour-through emphasis.
    SubplotTemplate("""\
{hound}, {emo_cautious}, balanced an empty hollow log under
the gap. "The bones come in at one end of the gap,"
{hound_he_she} said, "the gap does its work — applying the rule,
choosing or changing — and what falls into the receiving log is
the result. The receiver is patient; the gap is exact." To
{goal_text}, {hound_he_she} composed {concept_phrase}, ran the
input through. The REPL collected what
fell into the receiving log."""),

    # 3. Stacked gaps — output of one feeds the next. (comp xform.)
    SubplotTemplate("""\
{hound} laid two gapped logs above one another, the bones
that passed the first gap arriving at the second — the river
running calm beneath both. "What lands at the bottom,"
{hound_he_she} said, {emo_patient}, "has been through both rules
in order — applied as a single combined gap." To {goal_text},
{hound_he_she} composed {concept_phrase} as a stack of gaps,
ran the input through. The REPL caught
what the stack had let through."""),

    # 4. The receiver template — pour into any kind of cache.
    SubplotTemplate("""\
"You can collect the result into any kind of cache you like,"
{hound}, {emo_patient} said. "A row of bones, a unique-only pile, a sack
of any shape — the gap doesn't care; the receiver does." To
{goal_text}, {hound_he_she} composed {concept_phrase}, chose
the right empty receiver, ran the bones through the gap,
submitted the form, and the REPL packed the result into the
cache of {hound_his_her} choosing."""),

    # 5. The Dog-tries-to-shortcut-the-gap template.
    SubplotTemplate("""\
{dog} eyed the bones, {emo_greedy}, and called out a guess
about what would come out the far side of the gap without
bothering to actually run any through. {hound_phrase} shook
{hound_his_her} head and went on with the work: to {goal_text},
{hound_he_she} composed {concept_phrase} as the gap's rule, ran
the input through carefully. The REPL returned the only answer that would do — the one the gap had
actually produced."""),
]


# ─────────────────────── tally-scratch (atom / ref) ───────────────────


_NOTEBOOK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. Tally-scratch on a flat stone by the stream's edge — any dog
    #    can read it; updates are atomic.
    SubplotTemplate("""\
A flat stone sat at the stream's edge, its surface scratched with
a running tally of cached bones. Any dog could trot up, read the
count, or — carefully — update it. "Atoms are like this tally,"
{hound}, {emo_patient} said. "You can deref to read; you can swap! to
write atomically, no matter who else is sniffing." To
{goal_text}, {hound_he_she} composed {concept_phrase}, submitted
the form, and let the REPL work the tally exactly as the form
prescribed."""),

    # 2. Atomic swap — read, apply, write, all in one motion.
    SubplotTemplate("""\
"When I want to update the tally," {hound}, {emo_patient} said, "I don't
pick the stone up and walk away — I read the scratch, apply the
change, and scratch the new count back, all in a single motion.
If two dogs arrive at once, the runtime makes sure only one of us
goes through at a time." To {goal_text}, {hound_he_she}
composed {concept_phrase} for the tally, submitted the form, and
the REPL applied the update atomically."""),

    # 3. The tally-stays-on-the-stone template.
    SubplotTemplate("""\
"The tally stays scratched into the stone," {hound}, {emo_patient} said,
"so any dog who comes by can read what's there right now. The
count changes only when one of us scratches a new one — and only
as the runtime allows." To {goal_text}, {hound_he_she}
composed {concept_phrase}. The REPL —
reading or scratching the tally as the form prescribed — handed
back the value the stone had carried."""),

    # 4. The shared-state template — coordinated updates.
    SubplotTemplate("""\
"Many dogs can come and go past the stone," {hound}, {emo_patient} said,
"and each one's read or scratch must agree with the others. The
runtime sees to that — no two writers stomp on each other's
work." To {goal_text}, {hound_he_she} composed
{concept_phrase}. The REPL — coordinating
each access cleanly — handed back what the tally now said."""),

    # 5. The Dog-snatches-at-the-stone template.
    SubplotTemplate("""\
{dog}, {emo_greedy}, swiped a paw across the tally-stone,
trying to scratch an answer over the count. {hound_phrase} caught
{dog_him_her} firmly: tallies shared by all the pack need careful
updates, not snatches. To {goal_text}, {hound_he_she} composed
{concept_phrase}. The REPL — applying the
update the runtime's careful way — handed back the value the
stone now held."""),
]


# ─────────────────────── counting-bones (numbers) ─────────────────────


_ACORN_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The counting-bones template — generic arithmetic frame.
    SubplotTemplate("""\
{hound}, {emo_patient} laid bones out on a flat stone {place}, sorting
them into small piles. "Numbers in Clojure are just like bones
in piles," {hound_he_she} said: "you can count them, you can
add two piles together, you can divide one pile among several."
To {goal_text}, {hound_he_she} composed {concept_phrase},
submitted the form, and let the REPL hand back the count of
whatever the operation had produced."""),

    # 2. The pile-grows-or-shrinks template — for inc/dec, +/-.
    SubplotTemplate("""\
"Watch the pile," {hound} said, {emo_patient}, gesturing
at a small heap of bones beside the river. "Every operation
either adds, takes away, or combines what's already there — the
pile grows or shrinks by exactly what you say, and the river
neither rushes nor stops the count." To {goal_text},
{hound_he_she} composed {concept_phrase} and submitted it. The
runtime handed back the count, the river running steady beside
the heap."""),

    # 3. The careful-arrangement template.
    SubplotTemplate("""\
{hound}, {emo_patient}, arranged a small heap of bones
{place}, careful with the count — the bridge's shadow long across
the water, every bone weighing what it weighed. "Numbers in
Clojure don't fudge," {hound_he_she} said. "Whatever you do —
adding, subtracting, dividing into piles with leftovers,
comparing two heaps — the runtime gets it exactly right, every
time. A reflection lies; a tally does not." To {goal_text},
{hound_he_she} composed {concept_phrase} and submitted it. The
runtime handed back the count, the bridge-shadow steady on the
water beside the bones."""),

    # 4. The Dog-eyeballs-the-pile template.
    SubplotTemplate("""\
{dog} eyed the pile, {emo_greedy}, and called out a guess
about how many bones were there without bothering to count.
{hound_phrase} simply began counting — to {goal_text} required no
eyeballing, only the form. {hound_he_she_cap} composed
{concept_phrase} and submitted it. The runtime returned the
count the patient way, the bridge-shadow long across the water."""),

    # 5. The exact-count template.
    SubplotTemplate("""\
"Whatever the pile looks like after the operation,"
{hound}, {emo_patient} said, "the runtime gives the exact count — small
or large, fraction or whole, the answer is precise." To
{goal_text}, {hound_he_she} composed {concept_phrase},
submitted the form, and the REPL handed back the value, exactly
as the operation had produced it."""),
]


# ─────────────────────── stream-crossing-conditions (boolean) ─────────


_GATE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The crossing-conditions template — generic for any boolean.
    SubplotTemplate("""\
{hound}, {emo_cautious}, paused at the stream's edge
{place}, weighing the crossing. The water was quick today, the
ledge slick. "Boolean forms in Clojure are like the conditions
for a crossing," {hound_he_she} said: "the runtime checks the
value, opens or closes the way, and what comes back is the
verdict — not a guess at the surface." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL returned whatever the conditions had decided."""),

    # 2. The truthy/falsey-rules template.
    SubplotTemplate("""\
"Only two things in Clojure close the crossing," {hound}
said, {emo_patient}: "nil and false. Everything else — zero, the
empty string, an empty list — opens it. The verdict follows that
rule exactly, the way a steady current keeps its line." To
{goal_text}, {hound_he_she} composed {concept_phrase},
{concept_phrase}. The REPL returned the
value the crossing had passed, true or false."""),

    # 3. The boolean-verdict template.
    SubplotTemplate("""\
"You can't tell whether the crossing will be open by guessing,"
{hound}, {emo_patient} said. "You bring the value to the bank, the
runtime checks it, and the conditions give the only answer that
matters." To {goal_text}, {hound_he_she} composed
{concept_phrase}. The REPL settled the
matter — the conditions had spoken exactly as the rule said."""),

    # 4. The Dog-leaps-without-checking template.
    SubplotTemplate("""\
{dog} sprinted toward the stream {place}, {emo_greedy},
certain the way would be open for {dog_him_her}. {hound_phrase}
slowed and watched: the only way to know whether the crossing
held was to actually carry the value to it. To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL settled the matter — the conditions had ruled
exactly as the form said, regardless of {dog}'s guess."""),

    # 5. The decisive-condition template — and/or carry the value.
    SubplotTemplate("""\
"The condition carries the value through, not just a yes or a
no," {hound}, {emo_patient} said. "Whatever the verdict, that's what the
runtime hands back — sometimes a strict true or false, sometimes
the very value that passed the test." To {goal_text},
{hound} composed {concept_phrase}, submitted the form,
and the REPL returned the value the conditions had carried
through."""),
]


# ─────────────────────── fork-at-the-bank (if / cond / case) ──────────


_FORK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The fork-at-the-bank template — generic; the path branches
    #    and the condition decides which arm runs.
    SubplotTemplate("""\
The path forked at the bank {place}, with one or more arms
branching off — upstream, downstream, or back into the trees —
each arm marked with a condition. "Branching forms in Clojure
are forks like this," {hound}, {emo_patient} said. "The runtime checks
the condition, takes the matching arm, and only that arm's value
comes back." To {goal_text}, {hound_he_she} composed
{concept_phrase}. The REPL — having
taken the right arm — handed back its value."""),

    # 2. The crossroads template — applies to cond / case.
    SubplotTemplate("""\
The path {place} opened into a fork of three or four arms, each
marked by a small condition-stone. "Branching forms work like
this," {hound}, {emo_patient} said: "the dog walks past the stones in
order, takes the first arm whose stone says true, and the value
of that arm is what comes back." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL took the right arm and returned its value."""),

    # 3. The unrun-arm template — branches not taken don't run.
    SubplotTemplate("""\
"What's important about a fork," {hound}, {emo_patient} said, "is that
the arm not taken doesn't run at all. The runtime checks the
condition, walks the right arm, and the unrun arm is just left
behind." To {goal_text}, {hound_he_she} composed
{concept_phrase}. The REPL — running
only what was needed — handed back the value of the chosen
arm."""),

    # 4. The Dog-tries-to-skip-the-condition template.
    SubplotTemplate("""\
{dog}, {emo_greedy}, called out which arm of the fork
{dog_he_she} was sure the runtime would take, without bothering
to check the condition. {hound_phrase} only smiled: the only
way to know is to evaluate the condition. To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL — checking the condition properly — returned the
value of the arm the form actually ran."""),

    # 5. The one-form-decides template.
    SubplotTemplate("""\
"It isn't the dog who picks the arm," {hound}, {emo_patient} said, "it's
the condition. Whatever the condition evaluates to, that
decides." To {goal_text}, {hound_he_she} composed
{concept_phrase}. The REPL — letting the
condition decide — handed back the value of the arm the
condition had pointed at."""),
]


# ─────────────────────── marker-stone (def / namespace) ───────────────


_ROADSIGN_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The marker-stone-by-the-stream template — `def`.
    SubplotTemplate("""\
{hound}, {emo_patient} chose a flat stone {place} and scratched a fresh
name into its surface. "A def is a marker stone by the stream,"
{hound_he_she} said. "Any dog passing reads the scratch, learns
where the bone is buried, and can find it later by the name
alone." To {goal_text}, {hound_he_she} composed
{concept_phrase}. The REPL set the
stone — the name now bound to its value for any later dog along
the bank."""),

    # 2. The stones-stay-where-set template.
    SubplotTemplate("""\
"The good thing about a marker stone," {hound}, {emo_patient} said, "is
that it stays where you set it. The next dog along the bank
reads the freshest scratch — whatever the latest mark says." To
{goal_text}, {hound_he_she} composed {concept_phrase},
submitted the form, and the REPL — reading the markers as the
form directed — returned the value the bank had recorded."""),

    # 3. The bone-cache-of-the-pack template — namespaces / require.
    SubplotTemplate("""\
A small set of marker stones stood in a half-circle {place}, each
stone carrying the names for one stretch of riverbank. "Names
live in groups," {hound}, {emo_patient} said: "to use a name from a
stretch you didn't dig, you make sure that stretch's stones are
where the runtime can find them." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL — finding the right name on the right stone —
returned the value the form had asked for."""),

    # 4. The careful-naming template.
    SubplotTemplate("""\
"Naming is half the art," {hound}, {emo_patient} said, scratching a
careful sign into a fresh stone. "A clear name on the bank tells
every later dog what to expect; a careless one leads them to
the wrong bone." To {goal_text}, {hound_he_she} composed
{concept_phrase} with the right name in mind, submitted the form,
and the REPL — reading the name exactly — returned the value the
stone had promised."""),

    # 5. The Dog-misreads-the-marker template.
    SubplotTemplate("""\
{dog}, {emo_greedy}, glanced at the marker stone {place}
and called out what {dog_he_she} thought it said without slowing.
{hound_phrase} stopped and read carefully. To {goal_text}, the
scratch had to be read exactly: {hound_he_she} composed
{concept_phrase}. The REPL — reading
literally — returned the right value, while {dog}'s guess fell
short."""),
]


# ─────────────────────── log-bridge-test (try / catch) ────────────────


_SAFETYNET_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The log-bridge test before crossing — `try`/`catch`.
    SubplotTemplate("""\
{hound}, {emo_patient} stepped onto a fallen log spanning the stream
{place}, testing its hold paw by paw before trusting full weight.
"If the log gives, I retreat to the bank; the run doesn't end,
only the path bends." To {goal_text}, {hound_he_she}
composed {concept_phrase}. The REPL —
log tested in advance — caught any trouble and returned the
value the catch-arm had specified, the run continuing the patient
way."""),

    # 2. The practice-bank template — REPL safety; nil punning.
    SubplotTemplate("""\
"This is the practice bank," {hound}, {emo_patient} said {place},
gesturing wide. "A stumble here costs nothing. Try a form, see
what comes back, fix it, try again. The REPL is forgiving in a
way that a real crossing is not." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL returned the value — even if the form had been
close to a mis-step."""),

    # 3. The slip-and-recovery template.
    SubplotTemplate("""\
"What matters when something goes wrong," {hound}, {emo_patient} said,
"is that the run can continue — the runtime catches the slip,
takes the recovery path, and the answer comes back even when
something inside the form went off the bank." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the
form, and the REPL — handling the slip cleanly — returned the
value the recovery path had produced."""),

    # 4. The check-and-continue template.
    SubplotTemplate("""\
"There's a discipline to crossing safely," {hound}, {emo_patient} said,
"and it starts with checking — making sure the form does what it
claims, catching what could go wrong before it does." To
{goal_text}, {hound_he_she} composed {concept_phrase},
submitted the form, and the REPL — applying whatever check or
catch the form had asked for — returned the value the discipline
had earned."""),

    # 5. The Dog-tries-the-leap template.
    SubplotTemplate("""\
{dog} eyed the log-bridge {place}, {emo_greedy}, certain
{dog_he_she} could bound across without testing. {hound_phrase}
shook {hound_his_her} head and tested the log carefully. To
{goal_text} required no daring, only the test:
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL — catching anything that fell — returned the answer
the safety design had earned."""),
]


# ─────────────────────── message-bone (IO / metadata) ─────────────────


_SCROLL_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The message-bone template — reading and writing.
    SubplotTemplate("""\
{hound}, {emo_patient} unearthed a long bone {place}, scratching marks
along its length with a sharp claw. "The world outside the REPL
is message-bones," {hound_he_she} said: "you read what they
say, you scratch what you want to keep, and the runtime carries
the marks back and forth." To {goal_text}, {hound_he_she}
composed {concept_phrase}. The REPL handed back what the bone had said, or what the writing had
committed."""),

    # 2. The reading-and-writing template — slurp / spit.
    SubplotTemplate("""\
"Reading and scratching message-bones is just like reading and
writing forms," {hound}, {emo_patient} said. "You ask the runtime for
what's on the bone, you scratch what you want recorded, and the
work goes both ways through one claw." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the
form, and the REPL handed back what the bone had said — or what
the writing had committed."""),

    # 3. The careful-handling template.
    SubplotTemplate("""\
"The world outside the REPL is bigger than the REPL,"
{hound}, {emo_patient} said, "and a message-bone out there has its own
discipline — pick it up carefully, handle it with care, set it
back when you're done." To {goal_text}, {hound_he_she}
composed {concept_phrase}. The REPL —
handling the bone the runtime's careful way — returned the value
the work had produced."""),

    # 4. The Dog-tries-to-shortcut-the-bone template.
    SubplotTemplate("""\
{dog}, {emo_greedy}, claimed the message-bone said exactly
what {dog_he_she} expected and didn't bother to actually read.
{hound_phrase} brought it close and read carefully. To
{goal_text} required the bone's actual marks — {hound_he_she}
composed {concept_phrase}. The REPL —
reading the bone faithfully — returned the value the marks had
held."""),

    # 5. The two-banks template — inside-the-REPL and outside-the-REPL.
    SubplotTemplate("""\
"There's the bank inside the REPL," {hound}, {emo_patient} said, "and
the bank outside it. Message-bones are how the two meet — a
value crosses out and becomes scratches on a bone, or scratches
on a bone cross in and become a value again." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL — bridging the two banks — handed back the value
the work had carried."""),
]


# ─────────────────────── pack-agreement (protocols) ───────────────────


_GUILD_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The founding-the-pack-agreement template — `defprotocol`.
    SubplotTemplate("""\
{hound}, {emo_patient} scratched a small set of signs into a flat stone
{place}: signals that any dog of any breed could honor.
"A protocol is a pack agreement," {hound_he_she} said. "It lists
what every member must be able to signal — the methods. Any dog
that learns the signals may join the pack." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL — agreement set — handed back the pack's record."""),

    # 2. The same-call-many-breeds template.
    SubplotTemplate("""\
"What makes a pack agreement useful," {hound}, {emo_patient} said, "is
that the call is the same for every member, but each breed
answers in its own way. The runtime looks up which breed the
dog is, then runs that breed's answer." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL — dispatching to the right breed — returned the
breed-specific value."""),

    # 3. The pack-ledger template.
    SubplotTemplate("""\
{hound}, {emo_patient} held up the pack ledger — a slab of bark
scratched with breed-by-breed entries. "Membership is in this
record," {hound_he_she} said: "the breed, the signals they
honor, and the actual answers each breed gives. The runtime
reads from the ledger whenever the call goes out." To
{goal_text}, {hound_he_she} composed {concept_phrase},
submitted the form, and the REPL — checking the ledger as it
ran — returned the right answer."""),

    # 4. The boundaries-of-the-pack template.
    SubplotTemplate("""\
"Each pack has its own agreement," {hound}, {emo_patient} said.
"Belonging to the Bone-Sniffers' pack doesn't mean belonging to
the River-Crossers' pack — the runtime checks each separately,
and only the right pack's answer comes back." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL — respecting which pack was being called — returned
the right value."""),

    # 5. The Dog-claims-membership template.
    SubplotTemplate("""\
{dog}, {emo_greedy}, declared that {dog_he_she} could of
course honor whatever the pack's signal demanded — even though
the breed had never learned the call. {hound_phrase} only smiled
and asked for the actual response. To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL — checking the ledger first — returned the right
answer based on who had actually joined."""),
]


# ─────────────────────── kennel-master's-tools (host interop) ─────────


_TOOLSHED_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The borrowed-tool template — `.method` syntax.
    SubplotTemplate("""\
{hound}, {emo_patient} padded over to the kennel-master's shed {place}
and pulled down a tool the dogs hadn't carved themselves — a
leash, a bowl, a collar. "These aren't ours," {hound_he_she}
said, "but we can call their methods directly: dot-prefix on the
tool, or slash for standard-issue." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL — calling into the kennel-master's tool — handed
back what its method had returned."""),

    # 2. The labeled-toolshed template.
    SubplotTemplate("""\
"Each tool in the kennel-master's shed has its own label,"
{hound}, {emo_patient} said, "and the right way to call it depends on
which kind of tool it is — some held by a single dog, some
standard-issue called by the shed's name." To {goal_text},
{hound_he_she} composed {concept_phrase} using the right
calling convention. The REPL — invoking
the host tool by its label — returned the value the host had
computed."""),

    # 3. The careful-handling template.
    SubplotTemplate("""\
"Kennel-master's tools work, but they need careful handling,"
{hound}, {emo_patient} said. "Their labels are different, their calling
conventions are different, and the runtime has to bridge between
the dogs' world and the human's every time." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL — making the bridge cleanly — handed back the value
the foreign tool had produced."""),

    # 4. The two-worlds template — dogs' world and humans' world.
    SubplotTemplate("""\
"There's the pack's own kit," {hound}, {emo_patient} said, "and there's
the kennel-master's. The runtime moves a value across the
boundary, calls the human-side tool, and brings the result back
into the pack." To {goal_text}, {hound_he_she} composed
{concept_phrase}. The REPL — bridging
the two sheds — returned the value cleanly."""),

    # 5. The Dog-grabs-the-wrong-tool template.
    SubplotTemplate("""\
{dog}, {emo_greedy}, snatched at the kennel-master's
shed without checking which tool was which. The wrong tool, of
course, made an awful clatter. {hound_phrase} sighed and walked
over: to {goal_text} required reading the shed's labels
carefully. {hound_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — calling the right host method
by name — returned the value cleanly while {dog} watched,
chastened."""),
]


# ─────────────────────── scent-mark-rewrite (macros) ──────────────────


_REWRITERULE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The rewriting-scent-mark template — `defmacro` introduction.
    SubplotTemplate("""\
{hound}, {emo_patient} crouched at a scratch in the bark {place}, paw
poised. "A macro," {hound_he_she} said, "is a rule that rewrites
a scent-mark before the pack ever follows it. You set the rule
once, and any mark that uses it gets rewritten on the way to the
trail." To {goal_text}, {hound_he_she} composed
{concept_phrase}. The REPL — first
rewriting, then evaluating — returned the value the rewritten
mark yielded."""),

    # 2. The rule-shapes-the-form template.
    SubplotTemplate("""\
"Here's the difference between a rule and a trail,"
{hound}, {emo_patient} said. "A trail takes ingredients and finds a
bone. A rule takes a *form* and makes a different *form* — only
then does the runtime get to evaluate it." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the
form, and the REPL — applying the rule to the form first, then
evaluating — handed back the value the rewritten form had
produced."""),

    # 3. The runtime-applies-the-rule template.
    SubplotTemplate("""\
"The order matters," {hound}, {emo_patient} said. "When a rule is
involved, the runtime first walks through the form and applies
the rule wherever it sees one — and only then does it evaluate
the result." To {goal_text}, {hound_he_she} composed
{concept_phrase}. The REPL — rewriting
first, evaluating second — returned the final value."""),

    # 4. The Dog-claims-no-rule-needed template.
    SubplotTemplate("""\
{dog}, {emo_greedy}, insisted that no rule was needed —
{dog_he_she} could write the form directly. {hound_phrase}
allowed that sometimes that's true, but the rule shines when
many forms need the same rewriting. To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL — handling the rule's rewrite the rule's way —
returned the value the form had produced."""),

    # 5. The Dog-tries-to-skip-the-rule template.
    SubplotTemplate("""\
{dog}, {emo_greedy}, insisted that the rule was
unnecessary — {dog_he_she} could scratch the rewritten mark
directly. {hound_phrase} only smiled: a hand-rewritten mark is
fine once, but the rule pays off when many marks need rewriting
the same way. To {goal_text}, {hound_he_she} composed
{concept_phrase}. The REPL — running the
rule the rule's way — returned the value the rewritten form
yielded."""),
]


# ─────────────────────── scratch-mark-conventions (reader) ────────────


_SCRIBE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The reading-conventions-of-the-form template.
    SubplotTemplate("""\
"There are conventions for how the runtime *reads* a form,"
{hound}, {emo_patient} said: "what counts as one mark, what's just blank
bark between marks, what gets ignored, what gets grouped
together. The dog who scratches and the runtime who reads both
follow the same conventions." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL — reading exactly by the conventions — returned
the value the form had specified."""),

    # 2. The form-is-what-the-reader-sees template.
    SubplotTemplate("""\
"A form is what the reader sees," {hound}, {emo_patient} said, "after
the conventions have been applied. Some marks count, some
don't; some shapes are expanded before the runtime even gets a
look. The form you scratch and the form the runtime evaluates
aren't always paw-print-for-paw-print the same." To
{goal_text}, {hound_he_she} composed {concept_phrase},
submitted the form, and the REPL — reading carefully — returned
the value of what the conventions had produced."""),

    # 3. The careful-writing-careful-reading template.
    SubplotTemplate("""\
{hound}, {emo_patient} smoothed a fresh strip of bark {place} and
scratched slowly, paying attention to every mark. "The form has
to be written so the reader can read it cleanly,"
{hound_he_she} said. "If the marks are right, the runtime gets
the right form; if not, not." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the
form, and the REPL — reading exactly as scratched — returned
the value cleanly."""),

    # 4. The Dog-misreads-the-form template.
    SubplotTemplate("""\
{dog}, {emo_greedy}, glanced at the form and called out
what {dog_he_she} thought it would do without paying attention
to the conventions of how it was scratched. {hound_phrase} only
shook {hound_his_her} head — the runtime reads the form exactly.
To {goal_text}, {hound_he_she} composed {concept_phrase},
submitted the form, and the REPL — reading literally — returned
the right value, while {dog}'s guess fell short."""),

    # 5. The form-as-it-is template.
    SubplotTemplate("""\
"A form is what's actually there on the bark," {hound}, {emo_patient}
said, "after the conventions of writing and reading have done
their work. The runtime sees the cleaned-up form, evaluates it,
and gives back what it computes." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the
form, and the REPL — taking the form exactly as it was — handed
back the value."""),
]


# ─────────────────────── bone-scratch-vs-bone (quote / symbols) ───────


_CHALKMARK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The mark-on-the-bark template — symbols vs values.
    SubplotTemplate("""\
{hound}, {emo_patient} pointed at a name scratched into the bark {place},
then at an actual bone lying on the path. "The mark on the bark
is the *name*; the bone is the *value*. They are not the same
thing — and Clojure lets you talk about either one. The
reflection in the stream looks like a bone, but the scratch that
says 'bone' isn't the bone either." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL — keeping the name and the value distinct —
returned the right answer."""),

    # 2. The label-the-list template — `quote` / `'`.
    SubplotTemplate("""\
"To talk about the form itself rather than evaluating it,"
{hound}, {emo_patient} said, "you mark the form with a quote-scratch in
front. Quoting tells the runtime: don't run this, just hand it
back as the shape it is." To {goal_text}, {hound_he_she}
composed {concept_phrase}. The REPL —
respecting the scratch — returned the form unevaluated."""),

    # 3. The labeling-form-vs-evaluating-it template.
    SubplotTemplate("""\
"There's a difference between *labeling* the form and
*evaluating* it," {hound}, {emo_patient} said. "Quote in any of its
shapes is the labeling — the runtime hands you back the form,
not its value, unless you say otherwise." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the
form, and the REPL — labeling exactly what the form asked for —
returned the form-as-data, exactly as the marks had directed."""),

    # 4. The Dog-confuses-name-with-value template.
    SubplotTemplate("""\
{dog}, {emo_greedy}, mistook the name on the bark for the
bone it pointed to. "It says bone, so the value must be the
bone!" {hound_phrase} only shook {hound_his_her} head: the mark
and the bone are never the same thing — no more than the
reflection in the stream is the bone in your jaws. To
{goal_text}, {hound_he_she} composed {concept_phrase}, submitted
the form, and the REPL — keeping mark and bone distinct —
returned the right answer for the goal."""),
]


# ─────────────────────── scout-dog (agent / future / promise) ─────────


_RUNNERAHEAD_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The scout-dog-sent-ahead template — future / agent.
    SubplotTemplate("""\
{hound}, {emo_patient} dispatched a young scout-dog down the long bank
{place}, work in jaws. "The scout goes ahead while we keep on
with our own business," {hound_he_she} said, "and when we need
the result we ask the scout to bring it back." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the
form, and the REPL — sending the scout, fetching the result
later — returned the value when it was ready."""),

    # 2. The eventually-returns template.
    SubplotTemplate("""\
"Once you've sent the scout ahead," {hound}, {emo_patient} said, "you
keep on with your own work. The result will be there when you
ask for it — sometimes you have to wait for the scout to be
finished, sometimes you can keep arranging things until you
need it." To {goal_text}, {hound_he_she} composed
{concept_phrase}. The REPL —
coordinating the scout the way the form prescribed — returned
the value when it was ready."""),

    # 3. The patience-of-the-Hound template.
    SubplotTemplate("""\
"The hard part isn't sending the scout," {hound}, {emo_patient} said.
"The hard part is being patient enough to wait for the answer
when it comes — not snatching too early, not giving up too soon.
The runtime makes that easier than it sounds." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the
form, and the REPL — coordinating the wait properly — returned
the scout's answer when the scout had it ready."""),

    # 4. The Hound-coordinates template.
    SubplotTemplate("""\
{hound}, {emo_patient} arranged a small relay {place}, scouts and
messengers each in their place along the banks. "The runtime
keeps track of who set out when, and when each one finishes,"
{hound_he_she} said, "so the values come back in the right
order, no matter how long each scout takes." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the
form, and the REPL — coordinating the relay — returned the right
value at the right time."""),

    # 5. The Dog-doesn't-wait template — Dog grabs before scout returns.
    SubplotTemplate("""\
{dog}, {emo_greedy}, lunged for the scout's satchel before
the scout had even returned from the far bank. {hound_phrase}
held {dog_him_her} back: a scout sent ahead must be allowed to
finish. To {goal_text}, {hound_he_she} composed
{concept_phrase}. The REPL — waiting
for the scout the patient way — returned the value when the
scout had actually delivered it."""),
]


# ─────────────────────── sorting-bones (multimethods) ─────────────────


_SORTINGTABLE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The sorting-bones-by-origin template — `defmulti`.
    SubplotTemplate("""\
A long flat stone sat {place}, with several piles of bones
forming around it — fish, bird, deer, each in its own pile.
"Defmulti is a sorting-stone," {hound}, {emo_patient} said. "You decide
what about each bone to look at — its shape, its smell — and
the stone routes each bone to the matching pile." To
{goal_text}, {hound_he_she} composed {concept_phrase},
submitted the form, and the REPL — reading the bone, picking the
pile — returned the value the right pile had produced."""),

    # 2. The branch-of-the-table template — `defmethod`.
    SubplotTemplate("""\
"To add a pile to the sorting-stone," {hound}, {emo_patient} said, "you
say what kind of bone the pile handles and what behavior runs
when a bone of that kind arrives." To {goal_text},
{hound_he_she} composed {concept_phrase} for the right pile,
submitted the form, and the REPL — adding the pile, dispatching
the bone — returned the pile-specific value."""),

    # 3. The runtime-reads-the-stamp template.
    SubplotTemplate("""\
"What the stone sorts by is up to you," {hound}, {emo_patient} said.
"You decide what to look at on each bone — a kind, a smell, a
size, anything. The runtime reads it, finds the matching pile,
and runs that one." To {goal_text}, {hound_he_she} composed
{concept_phrase}. The REPL — reading
what the dispatch function produced — returned the value the
right pile had given."""),

    # 4. The flexible-routing template.
    SubplotTemplate("""\
"The good thing about a sorting-stone," {hound}, {emo_patient} said,
"is that you can keep adding new piles whenever a new kind of
bone shows up. The original stone doesn't change; the runtime
just learns one more route." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the
form, and the REPL — routing through the piles cleanly —
returned the right value."""),

    # 5. The Dog-jumps-to-the-wrong-pile template.
    SubplotTemplate("""\
{dog}, {emo_greedy}, leaped onto the sorting-stone
without showing what kind of bone {dog_he_she} carried.
{hound_phrase} pointed at the edge of the stone: every bone
must show the kind the stone sorts by. To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL — reading the kind first, dispatching second —
returned the value from the correct pile."""),
]


# ─────────────────────── kennel-bag (deftype / defrecord) ────────────


_CARRYINGCASE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The labeled-compartments template — defrecord.
    SubplotTemplate("""\
{hound}, {emo_patient} held up a small kennel-bag {place}, its inside
divided into labeled compartments — one for the bone's date,
one for its size, one for its source. "Defrecord makes a bag
like this," {hound_he_she} said: "named compartments holding
specific things; a stamp on the outside saying what kind of
bag it is." To {goal_text}, {hound_he_she} composed
{concept_phrase}. The REPL —
constructing the bag, filling its compartments — returned the
value the bag held or carried."""),

    # 2. The bare-bag template — deftype.
    SubplotTemplate("""\
"A deftype is a barer bag," {hound}, {emo_patient} said. "Compartments,
a stamp — no map-like behavior unless you ask for it. Faster,
more focused, less convenient." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the
form, and the REPL — constructing the bare bag as specified —
returned the value inside."""),

    # 3. The reaching-into-the-compartment template — field access.
    SubplotTemplate("""\
"To reach into a labeled compartment," {hound}, {emo_patient} said,
"you ask for it by name. The bag knows where each compartment
is; the runtime fetches it cleanly." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the
form, and the REPL — opening the right compartment — returned
exactly what was inside."""),
]


# ─────────────────────── walking-the-bone-row (reduce / count) ────────


_TALLYWALK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The walking-the-bone-row template — reduce.
    SubplotTemplate("""\
{hound}, {emo_patient} paced the row of cached bones {place}, one paw at
a time, a flat stone in {hound_his_her} jaws for the running
tally. "Reduce is this walk," {hound_he_she} said: "at each
bone, you fold its count into the tally; at the end, the tally
is your answer." To {goal_text}, {hound_he_she} composed
{concept_phrase}. The REPL — walking
the row, carrying the tally — returned the final number."""),

    # 2. The starting-tally template — reduce with init.
    SubplotTemplate("""\
"You don't have to start the tally at zero," {hound}, {emo_patient}
said, holding up a stone already scratched with a number. "If
you start with a different value, the walk begins from there —
the combine-step folds each bone in from that starting point."
To {goal_text}, {hound_he_she} composed {concept_phrase},
submitted the form, and the REPL — starting from the given
tally, walking the row — returned the final value."""),

    # 3. The simple-count template — `count`.
    SubplotTemplate("""\
"The simplest tally-walk is just counting," {hound}, {emo_patient} said:
"step along the row, add one at every bone, no other operation.
The runtime does this for any collection — vector, list, map,
string." To {goal_text}, {hound_he_she} composed
{concept_phrase}. The REPL — walking the
row, counting the steps — returned the count."""),
]


# ─────────────────────── scratch-mark-string (str ops) ────────────────


_BEADSTRING_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The threading-marks template — `str` concat.
    SubplotTemplate("""\
{hound}, {emo_patient} held up a strip of bark covered in scratches
{place}. "Strings in Clojure are like this," {hound_he_she}
said: "a row of scratched marks, in order. Concat two strips
together, and the marks are spliced; cut a substring out, and
you get a shorter strip." To {goal_text}, {hound_he_she}
composed {concept_phrase}. The REPL —
splicing or cutting as the form said — returned the new
strip."""),

    # 2. The counting-marks template — string length / substring.
    SubplotTemplate("""\
"To count the marks, walk the strip," {hound}, {emo_patient} said.
"Want a section of marks? Cut from one position to another and
you get a smaller strip, the original untouched." To
{goal_text}, {hound_he_she} composed {concept_phrase},
submitted the form, and the REPL — counting or cutting —
returned the answer the strip had given up."""),

    # 3. The Dog-yanks-at-the-strip template.
    SubplotTemplate("""\
{dog}, {emo_greedy}, yanked at the bark-strip {place}
without bothering to count. {hound_phrase} stopped {dog_him_her}:
strings are precise — every mark in its place, every position
counted. To {goal_text}, {hound_he_she} composed
{concept_phrase}. The REPL — handling
the strip carefully — returned the right answer."""),
]


# ─────────────────────── pacing-the-bank (recur / loop) ───────────────


_CIRCUIT_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The pacing-without-growing-the-trail template — recur.
    SubplotTemplate("""\
{hound}, {emo_patient} paced back and forth along the stream bank
{place}, each pass returning to the same starting point with a
slightly different tally in jaws. "Recur is this pacing,"
{hound_he_she} said: "back to the top with new bindings, no
extra trail laid down behind us." To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the
form, and the REPL — looping without growing the call-stack —
returned the final value."""),

    # 2. The base-case template — termination.
    SubplotTemplate("""\
"Every pacing has a stopping condition," {hound}, {emo_patient} said.
"Without one, the dog walks forever. With one, the dog knows
when the passes are done and the tally is the answer." To
{goal_text}, {hound_he_she} composed {concept_phrase},
submitted the form, and the REPL — looping until the base case —
returned the value the final pass produced."""),

    # 3. The Dog-doesn't-trust-the-pacing template.
    SubplotTemplate("""\
{dog}, {emo_greedy}, distrusted the very idea of pacing:
surely you'd just walk forever? {hound_phrase} smiled patiently
— the base case is the dog's compass. To {goal_text},
{hound_he_she} composed {concept_phrase}, submitted the form,
and the REPL — looping the right number of times, then
stopping — returned the value cleanly."""),
]


# ════════════════════════════════════════════════════════════════════
# STORY TEMPLATES (Phase C — story-scaffold framework)
# ════════════════════════════════════════════════════════════════════
#
# Each family gets ONE additional template that composes the example's
# `scenario` / `need` / `mapping` / `resolution` slots into a 5-act
# grounded story:
#
#   Act 1 (SETUP):       {scenario}
#   Act 2 (NEED):        {need}
#   Act 3 (MAPPING):     {mapping}
#   Act 4 (ACTION):      character composes form; supplied by template
#   Act 5 (RESOLUTION):  {resolution}
#
# These templates carry `fits_tags=("story",)` so they only fire for
# examples whose tags include "story" (i.e., examples that have all
# four story slots authored). Examples without story slots continue
# to render with the existing family templates as before.
#
# Each family's story template differs only in the metaphor-vocabulary
# of its connective prose around the {concept_phrase} action — let
# is "gripped between the teeth", basket is "for the bone-cache",
# sieve is "as the gap's rule", etc. The slots provide the specifics.


def _story(connective_prose: str) -> SubplotTemplate:
    """Build a story-scaffold template for a family.

    The template is the canonical 5-act story shape; the family
    differentiates itself only by the {connective_prose} around the
    composed/submitted action — using the family's verb (compose /
    pour / swap / grip / etc.) and its imagery vocabulary.
    """
    return SubplotTemplate(f"""\
{{scenario}} {{need}} {{mapping}}

{connective_prose} {{resolution}}""", fits_tags=("story",))


# Family-specific story templates. The connective prose for each
# uses the family's verb + imagery, so the metaphor's vocabulary
# stays consistent through the action act.

_POUCH_SUBPLOTS = _POUCH_SUBPLOTS + [
    _story(
        "{hound_he_she_cap}, {emo_patient}, composed {concept_phrase}. The runtime pulled from the mouth as the form directed:"
    ),
]

_RECIPE_SUBPLOTS = _RECIPE_SUBPLOTS + [
    _story(
        "To {goal_text}, {hound_he_she}, {emo_patient}, laid out {concept_phrase} along the nose-trail and submitted the form. It walked the trail end to end and returned:"
    ),
]

_BASKET_SUBPLOTS = _BASKET_SUBPLOTS + [
    _story(
        "{hound_he_she_cap}, {emo_patient}, composed {concept_phrase} for the bone-cache. The runtime handed back the arrangement:"
    ),
]

_SIEVE_SUBPLOTS = _SIEVE_SUBPLOTS + [
    _story(
        "{hound_he_she_cap}, {emo_patient}, composed {concept_phrase} as the gap's rule ran the input through,. The runtime caught what landed below:"
    ),
]

_NOTEBOOK_SUBPLOTS = _NOTEBOOK_SUBPLOTS + [
    _story(
        "{hound_he_she_cap}, {emo_patient}, composed {concept_phrase} for the tally-stone. The runtime applied the update at the stream's edge:"
    ),
]

_ACORN_SUBPLOTS = _ACORN_SUBPLOTS + [
    _story(
        "{hound_he_she_cap}, {emo_patient}, composed {concept_phrase} with the running tally heavy in the count. The runtime counted out the answer:"
    ),
]

_GATE_SUBPLOTS = _GATE_SUBPLOTS + [
    _story(
        "{hound_he_she_cap}, {emo_patient}, composed {concept_phrase}. The runtime let the crossing-conditions decide:"
    ),
]

_FORK_SUBPLOTS = _FORK_SUBPLOTS + [
    _story(
        "{hound_he_she_cap}, {emo_patient}, composed {concept_phrase}. The runtime took the right arm of the path:"
    ),
]

_ROADSIGN_SUBPLOTS = _ROADSIGN_SUBPLOTS + [
    _story(
        "{hound_he_she_cap}, {emo_patient}, composed {concept_phrase}. The runtime read the markers and replied:"
    ),
]

_SAFETYNET_SUBPLOTS = _SAFETYNET_SUBPLOTS + [
    _story(
        "{hound_he_she_cap}, {emo_cautious}, composed {concept_phrase}. It handed back the value:"
    ),
]

_SCROLL_SUBPLOTS = _SCROLL_SUBPLOTS + [
    _story(
        "To {goal_text}, {hound_he_she}, {emo_patient}, composed {concept_phrase} with the message-bone laid long enough to hold every word the work would carry claw to bark — completed the message-bone work:"
    ),
]

_GUILD_SUBPLOTS = _GUILD_SUBPLOTS + [
    _story(
        "{hound_he_she_cap}, {emo_patient}, composed {concept_phrase}. It dispatched cleanly:"
    ),
]

_SORTINGTABLE_SUBPLOTS = _SORTINGTABLE_SUBPLOTS + [
    _story(
        "{hound_he_she_cap}, {emo_patient}, composed {concept_phrase}. The runtime routed through the piles:"
    ),
]

_CARRYINGCASE_SUBPLOTS = _CARRYINGCASE_SUBPLOTS + [
    _story(
        "{hound_he_she_cap}, {emo_patient}, composed {concept_phrase}. It constructed the kennel-bag:"
    ),
]

_TOOLSHED_SUBPLOTS = _TOOLSHED_SUBPLOTS + [
    _story(
        "{hound_he_she_cap}, {emo_cautious}, composed {concept_phrase}. It returned:"
    ),
]

_RUNNERAHEAD_SUBPLOTS = _RUNNERAHEAD_SUBPLOTS + [
    _story(
        "{hound_he_she_cap}, {emo_patient}, composed {concept_phrase}. The runtime coordinated the scout's return:"
    ),
]

_REWRITERULE_SUBPLOTS = _REWRITERULE_SUBPLOTS + [
    _story(
        "{hound_he_she_cap}, {emo_patient}, composed {concept_phrase}. It returned:"
    ),
]

_SCRIBE_SUBPLOTS = _SCRIBE_SUBPLOTS + [
    _story(
        "{hound_he_she_cap}, {emo_cautious}, composed {concept_phrase}. It read by the conventions and returned:"
    ),
]

_CHALKMARK_SUBPLOTS = _CHALKMARK_SUBPLOTS + [
    _story(
        "{hound_he_she_cap}, {emo_patient}, composed {concept_phrase}. It returned:"
    ),
]

_TALLYWALK_SUBPLOTS = _TALLYWALK_SUBPLOTS + [
    _story(
        "{hound_he_she_cap}, {emo_patient}, composed {concept_phrase}. It walked the bone-row carrying the tally:"
    ),
]

_BEADSTRING_SUBPLOTS = _BEADSTRING_SUBPLOTS + [
    _story(
        "{hound_he_she_cap}, {emo_patient}, composed {concept_phrase}. It spliced or counted as the form said:"
    ),
]

_CIRCUIT_SUBPLOTS = _CIRCUIT_SUBPLOTS + [
    _story(
        "{hound_he_she_cap}, {emo_patient}, composed {concept_phrase}. It paced without growing the trail:"
    ),
]
