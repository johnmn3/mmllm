"""Metaphor-bearing subplot pools for boy-wolf.

The base `_GOAL_SUBPLOTS` (in grade_1.py as `_SHARED_SUBPLOTS`) is
generic shepherd-vs-elder banter that uses `{goal_text}` and
`{concept_phrase}` but doesn't illuminate any particular Clojure idiom.
These pools below DO illuminate specific idioms by carrying a
boy-wolf-natural metaphor.

Family names mirror tortoise-hare's exactly (cross-fable parity); the
imagery is boy-wolf-specific. See
`docs/clojure-pedagogy/audits/metaphor-imagery-boy-wolf.md` for the
mapping.

Polarity: the SHEPHERD is the cautionary character (boasts, claims he
just *knows*); the ELDER is the corrective voice (writes the form,
lets the runtime decide). Boy-wolf templates flip the typical fable
polarity from tortoise-hare's hare/tortoise framing.

Pool sizing: 5 templates is the standard size; small families with
1-3 subjects use 3 templates. All templates use `{goal_text}` and
`{concept_phrase}` (never `{form_display}`), keeping the form-leak
design intact.

Authoring rules followed:
- Pronoun case at sentence start uses `_he_she_cap` etc.
- No "and" right after `{concept_phrase}` (avoids "the logical and
  and submit" stutters); use ", then submit", "; submit", or
  comma + new clause.
- No "write a form to {goal_text}" (avoids verb collision when
  goal_text starts with "write"); reframe as "to {goal_text},"
  + noun-clause.
- The metaphor is concretely named in every template (pouch / drill-
  card / wool-basket / fleece-comb / slate / etc.) so it lands as
  imagery, not as decoration.
- At least 2 of 5 templates carry a shepherd/elder fable beat
  (shepherd boasts/guesses → elder writes the form / lets the runtime
  decide).
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import SubplotTemplate


# ─────────────────────── goal-fallback (no metaphor) ──────────────────
#
# `_GOAL_SUBPLOTS` is the honest fallback for ~23 abstract subjects
# (host platforms, library design, build tools) where forcing a
# pastoral metaphor would be cargo-cult. It uses {goal_text} +
# {concept_phrase} (NOT {form_display}, since these are non-atom
# subjects). Carries the shepherd-vs-elder polarity but no specific
# imagery.

_GOAL_SUBPLOTS: list[SubplotTemplate] = [

    # 1. Shepherd boasts; elder asks for the form.
    SubplotTemplate("""\
{shepherd_phrase} and {elder_phrase} stopped {place} to settle a small
question. {shepherd}, {emo_proud}, declared {shepherd_he_she} could
write the form for it without thinking. {elder}, {emo_patient}, asked
{shepherd_him_her} to actually write {concept_phrase} carefully — and
then let the REPL confirm what the value really was. To {goal_text},
{elder_he_she} composed the form and submitted it."""),

    # 2. The honest-tally template — no wager, just the village's
    # standard of "claims must be checked".
    SubplotTemplate("""\
At the watchhouse notice-stone {place}, the question of the day was
posted: how to {goal_text}. {shepherd_phrase}, {emo_proud}, started
to shout an answer. The elder of the watchhouse reminded
{shepherd_him_her} that the village had stopped trusting unchecked
claims. {elder_he_she_cap} composed {concept_phrase} carefully and
submitted it so the REPL could give the townsfolk a clean
mark."""),

    # 3. Patient-elder template — the elder demonstrates the discipline.
    SubplotTemplate("""\
"To {goal_text}," {elder_phrase}, {emo_patient}, said {place}, "the village agreed
years ago: write the form, submit it, take the runtime's word." The
elder composed {concept_phrase} for {shepherd_phrase} to read,
submitted it to the REPL, and the answer came back as plain
as anything the slate had ever held."""),

    # 4. Apprentice-style template — elder shows the shepherd how.
    SubplotTemplate("""\
{elder_phrase}, {emo_patient}, had been showing {shepherd_phrase}
the way the meadow folk's careful shepherds settled questions on the
long valley road. To {goal_text}, {elder_he_she} composed
{concept_phrase} and let the REPL — steady as the watchhouse
slate, cool as the morning mist — return what the form computed.
The shepherd watched, {emo_regretful}, and started to understand."""),

    # 5. The runtime-as-judge template — village standard.
    #    Cat-J grounding: the village's rule is old and steady
    #    (old ↔ stable trust the runtime carries); the trial is
    #    long (long ↔ the form's full reduction).
    SubplotTemplate("""\
The village's rule, by long agreement {place}, was simple: a
question was answered by a form, never by a claim. To {goal_text},
the elder, {emo_patient}, composed {concept_phrase}, submitted
it, and the REPL — the only judge the valley trusted
now, slow and steady as a long evening — gave back the value.
{shepherd}, {emo_tired}, accepted the answer."""),
]


_GOAL_SUBPLOTS = _GOAL_SUBPLOTS + [
    # Story-scaffold composer. Cat-J grounding: the elder is
    # {emo_patient} (patience ↔ careful evaluation, the
    # patient/evaluator polarity), and the runtime is named "the
    # only judge that doesn't talk back" — long established trust
    # ↔ a stable runtime that returns the same value each time.
    # Story-scaffold composer (rewritten Cat-K XOE6). The earlier
    # version used "To {goal_text}, X composed …", which rendered
    # "To , X composed …" when the example had no goal_text (atom
    # subjects with story slots). The new wording uses {concept_phrase}
    # alone in the action line and threads the patience as a manner
    # adverb rather than a stitched-in phrase.
    SubplotTemplate(f"""\
{{scenario}} {{need}} {{mapping}}

{{elder_phrase}}, {{emo_patient}}, composed {{concept_phrase}} \
and submitted it. The REPL — the only judge that does not \
talk back — returned: {{resolution}}""", fits_tags=("story",)),
]


# ─────────────────────── shepherd's belt-pouch (let) ──────────────────


_POUCH_SUBPLOTS: list[SubplotTemplate] = [

    # 1. Shepherd claims he knows without checking; elder tucks the
    #    value into the pouch and carries it just for the stretch
    #    where it's needed.
    SubplotTemplate("""\
{shepherd_phrase}, {emo_proud}, claimed {shepherd_he_she} could just
shout the answer without bothering to check. {elder_phrase} only
shook {elder_his_her} head and reached for the belt-pouch. "When I
want to {goal_text}," {elder_he_she} said, "I tuck the value into
the pouch and carry it just for the stretch where I need it. By the
next milestone the pouch is empty again." {elder_he_she_cap} composed
{concept_phrase}, the binding tucked away inside the pouch, and
submitted it to the REPL. The form came back with the answer
the shepherd had not even thought to check."""),

    # 2. The pouch held for one stretch of road; whatever's tucked
    #    inside is in force only while the pouch is worn.
    #    Cat-J grounding: the road from village to pasture is long
    #    (long ↔ scope stretch), the pouch grows heavy with what's
    #    tucked (heavy ↔ accumulator); the elder's patience steadies
    #    the walk between milestones.
    SubplotTemplate("""\
{elder_phrase}, {emo_patient}, patted the heavy belt-pouch at
{elder_his_her} hip on the long road. "Whatever I tuck in here is
in force only while the pouch is worn," {elder_he_she} said, "and
only for the form that names the binding. Step past the form's
edge and the pouch is empty again." To {goal_text}, {elder_he_she}
composed {concept_phrase} with the binding tucked in for that
stretch, submitted it, and let
the REPL read out the value the pouch had held."""),

    # 3. Substitution rule — wherever the form names the binding,
    #    the runtime reaches into the pouch.
    #    Cat-J grounding: the pouch is heavy at the elder's hip
    #    (heavy ↔ accumulator value), the road from village to
    #    pasture is long (long ↔ the form's stretch of scope), the
    #    elder's patience steadies the substitution.
    SubplotTemplate("""\
"Wherever the form names the binding," {elder_phrase} explained,
{emo_patient}, on the long road from the village to the pasture,
"the runtime reaches into the heavy pouch and pulls out what was
tucked there." {elder_he_she_cap} demonstrated by intending to
{goal_text}: each mention of the bound name, {elder_he_she} said,
would be replaced by the value from the pouch the moment the
form ran. {elder_phrase} composed {concept_phrase}, submitted the
form, and the REPL substituted as promised — the pouch's value
threaded into every place the binding had been named."""),

    # 4. End-of-stretch — the pouch is empty when the form's stretch
    #    is over. (Scope ends.) Elder's careful work wins.
    #    Cat-J grounding: the road's stretch is long (long ↔ the
    #    binding's full scope); the pouch is full at the start and
    #    light at the end (full ↔ live binding, light ↔ scope ended);
    #    the elder's patience watches the cycle close.
    SubplotTemplate("""\
"Watch the pouch carefully," {elder_phrase} said, {emo_patient},
{place}. "While the form's long stretch of road runs, the pouch
is full and heavy and the binding is yours." To {goal_text},
{elder_he_she} composed {concept_phrase} with the binding tucked
safely inside, then submitted it. The REPL returned the
value, and the pouch — its work done — was light and empty
again. {shepherd_phrase}, {emo_tired}, finally admitted that the
patient pouch-walk had carried the day."""),

    # 5. The pouch holds the value for exactly one stretch; scope and
    #    temporary binding as a unified concept.
    SubplotTemplate("""\
{shepherd_phrase}, {emo_desperate}, was beginning to understand:
the belt-pouch was not magic, only careful. {elder_phrase} took the
goal — to {goal_text} — and composed {concept_phrase}, the value
tucked into the pouch for the stretch where the form lived. {elder_he_she_cap}
submitted it, and the REPL — reading the pouch as the form
told it to — handed back only what the form's scope had carried.
When the scope ended, the pouch fell away, and the value was gone."""),
]


# ─────────────────────── drill-card / watch-routine (fn) ──────────────


_RECIPE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. Shepherd claims he knows without writing; elder writes out
    #    the drill-card on the watchhouse wall.
    #    Cat-J grounding: the drill-card is laminated and well-worn
    #    (worn ↔ trusted reusable routine), the chalk is dry and
    #    cool (cool ↔ stable intermediate state through the steps).
    #    The elder's patience holds for the long write-out.
    SubplotTemplate("""\
{shepherd_phrase}, {emo_proud}, insisted {shepherd_he_she} could just
shout the answer rather than bother writing a drill-card. {elder_phrase},
{emo_patient}, only smiled and reached for the dry chalk and the
well-worn watchhouse wall. "Recipes on a drill-card are like the
routines we follow," {elder_he_she} said: "the ingredients go at the
head, the steps in order, and the last step is what gets served." To
{goal_text}, {elder_he_she} chalked out {concept_phrase} on the card,
submitted it, and the REPL followed the recipe and handed back
the value the last step had produced."""),

    # 2. The drill-card as a named watch-routine; elder composes it
    #    carefully, letting the REPL follow the steps.
    SubplotTemplate("""\
"A drill-card is only useful when it runs," {elder_phrase}, {emo_patient}, said,
holding up a slate-card from the watchhouse wall. "You write the steps,
you call the shepherds, the runtime does the rest." To {goal_text},
{elder_he_she} composed {concept_phrase} as a named routine, submitted
it, and the REPL — taking the recipe and its ingredients — handed
back what the steps had produced."""),

    # 3. Last step is what the routine serves. (Body returns last form;
    #    type-neutral and pedagogically true for all drill-cards.)
    #    Cat-K rewrite: make the "last step" rule concrete via the
    #    village's own drill-card practice. Cat-J: {emo_patient} +
    #    well-worn watchhouse wall (worn ↔ trusted reusable routine).
    SubplotTemplate("""\
"On any drill-card," {elder_phrase} said, {emo_patient}, smoothing
chalk down the well-worn watchhouse wall, "only the last step is what
the runner carries back. The earlier steps prepare the way; the last
step is the answer." To {goal_text}, {elder_he_she} chalked the
routine's steps in order and composed {concept_phrase}, submitted the
form, and the REPL — discarding earlier steps' values — handed back
only the result from the last."""),

    # 4. Drill-cards feeding into drill-cards — emphasizes the chained
    #    nature and how routines can be composed together.
    SubplotTemplate("""\
"Drill-cards can feed into one another," {elder_phrase}, {emo_patient}, said, spreading
several slates on the watchhouse step. "What one card serves, the next
can take as its ingredient — together they make a longer routine." To
{goal_text}, {elder_he_she} composed {concept_phrase} as a chain of
routines, submitted it, and the REPL — walking through the recipe
in order — handed back the value at the end."""),

    # 5. The shepherd boasts that he can guess the answer; the elder
    #    writes the drill-card carefully and the REPL proves the answer.
    SubplotTemplate("""\
{shepherd_phrase}, {emo_proud}, began calling out guesses about what the
routine would produce, certain {shepherd_he_she} knew without writing a
thing. {elder_phrase} simply kept chalking on the watchhouse wall. To
{goal_text}, {elder_he_she} composed {concept_phrase} as a careful
drill-card, submitted it, and the REPL — running the recipe step
by step — handed back the only answer that would do: the one the card
had actually produced."""),
]


# ─────────────────────── wool-basket / lambing-pen (collections) ──────


_BASKET_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The wool-basket-on-the-path template — generic; whatever the
    #    operation, the basket stays as it was, the form returns the
    #    new arrangement.
    #    Cat-J grounding: the basket is heavy with raw fleece (heavy
    #    ↔ accumulator value, fleece-full ↔ stable input); the elder's
    #    patience steadies the read; the loose-weave warmth hints at
    #    the immutability that returns a fresh arrangement.
    SubplotTemplate("""\
{elder_phrase}, {emo_patient}, pointed to a heavy wool-basket {place}.
"Whatever I want to do with what's inside," {elder_he_she} said, "I
read from the loose-weave basket, work the change, and the basket
itself stays as it was — what I get back is a fresh arrangement,
the original weight undisturbed." To {goal_text}, {elder_he_she}
composed {concept_phrase}, submitted it, and let the REPL
handle the basket exactly as the operation prescribed."""),

    # 2. The named pouches within the basket — works for tagged fleeces
    #    (maps), positional wool (vectors), or kind-only baskets (sets).
    #    The narrative is generic; goal_text says which.
    #    Cat-J grounding: the long row of pouches (long ↔ collection
    #    length); the {emo_patient} elder; the chalked names cool and
    #    steady on the pouches (cool ↔ stable lookup keys).
    SubplotTemplate("""\
"You can find what you want in a wool-basket several ways,"
{elder_phrase} said, {emo_patient}, gesturing at the long row of
woven pouches: "by the name chalked on the cool sturdy pouch, by
its place in the row, or by simply asking whether it's there at
all." To {goal_text}, {elder_he_she} wrote {concept_phrase} for
the basket, submitted it, and the REPL applied the lookup
or update exactly as the form directed — the answer surfacing
clean from the steady weave."""),

    # 3. The procession of sheep — for ordered collections (vectors,
    #    lists, seqs). Sub-template is collection-leaning but doesn't
    #    claim a specific type.
    SubplotTemplate("""\
A line of sheep had formed {place}, each one taking the next sheep's
fleece in its mouth — head at the front, the rest trailing behind. "Many
of our baskets are like this procession," {elder_phrase}, {emo_patient}, said. "You can
grab the head, you can ask for the tail, you can put a new sheep at the
front of the line." To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL marched the procession
exactly as the form described."""),

    # 4. The new-basket-from-old template — immutability emphasis;
    #    works for any collection type. The original sits untouched.
    SubplotTemplate("""\
"Watch carefully," {elder_phrase} said, holding up the original
wool-basket. "Whatever I do to it, this one sits unchanged in the fold —
what I get back is a fresh basket with the change made, leaving the first
one exactly where it was." To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL returned a new
arrangement while the original waited, untouched. {shepherd_phrase},
{emo_tired}, was beginning to see why nothing could be lost by
trying."""),

    # 5. The shepherd rummages and guesses; elder's careful basket-work
    #    wins. Generic fable beat that fits any collection operation.
    SubplotTemplate("""\
{shepherd_phrase} began rummaging in the wool-basket, {emo_proud}, calling
out guesses about its contents without quite checking. "I know exactly
what's in there," {shepherd_he_she} insisted. {elder_phrase} shook
{elder_his_her} head. To {goal_text} properly, {elder_he_she} wrote
{concept_phrase} carefully on a slate, submitted it, and the REPL —
looking into the basket the way the form told it to — handed back the
answer {shepherd} had been guessing at."""),
]


# ─────────────────────── fleece-comb / wool-screen (HOFs) ─────────────


_SIEVE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The general fleece-comb — works for transform (map),
    #    select (filter), select-counted (take/drop), or dedupe
    #    (distinct). The rule attached to the comb decides what
    #    happens to each fleece.
    #    Cat-J grounding: the comb is narrow-toothed (narrow ↔
    #    bottleneck rule — predicate filter), the heap of fleece is
    #    heavy (heavy ↔ collection size); the elder's patience tends
    #    each lock through the teeth without rushing.
    SubplotTemplate("""\
{elder_phrase}, {emo_patient}, held up a narrow-toothed fleece-comb
{place} — a routine rule attached at its teeth, the heavy heap of
fleece at the elder's feet. "Whatever rule we hang on the comb,"
{elder_he_she} said, "the wool passes through one lock at a time:
some are changed, some kept, some dropped, depending on the rule."
To {goal_text}, {elder_he_she} composed {concept_phrase} as the
comb's rule, poured the fleeces through, submitted it, and
the REPL returned what the comb had let pass."""),

    # 2. The pour-through-and-collect template — generic emphasis on
    #    the new-basket-out-the-other-side metaphor with a fleece-comb
    #    or wool-screen.
    SubplotTemplate("""\
{elder_phrase}, {emo_patient}, balanced a fleece-comb over an empty wool-basket. "The
fleeces go in at the top," {elder_he_she} said, "and the comb does its
work — applying the rule, choosing or changing — and what lands in the
basket below is the result." To {goal_text}, {elder_he_she} composed
{concept_phrase}, poured the input through, submitted it, and the
REPL collected what fell into the receiving basket."""),

    # 3. Stacked combs — output of one feeds the next. (comp xform.)
    SubplotTemplate("""\
{elder_phrase}, {emo_patient}, stacked two fleece-combs one above the other, the output
of the first feeding into the second. "What lands at the bottom,"
{elder_he_she} said, "has been through both rules in order — applied as
a single combined comb." To {goal_text}, {elder_he_she} composed
{concept_phrase} as a stack of combs, poured the input through, submitted
it, and the REPL caught what the stack let pass."""),

    # 4. The receiver template — pour into any kind of basket.
    #    (into / into with xform.)
    SubplotTemplate("""\
"You can pour the fleeces into any kind of basket you like,"
{elder_phrase}, {emo_patient}, said. "A row of locks, a unique-only pile, a bag of any
shape — the comb doesn't care; the receiver does." To {goal_text},
{elder_he_she} composed {concept_phrase}, chose the right empty
receiver, poured through the fleece-comb, submitted it, and the
REPL packed the result into the basket of {elder_his_her} choosing."""),

    # 5. The shepherd tries to guess the output without actually using
    #    the comb; elder pours through carefully and the REPL proves the
    #    answer.
    SubplotTemplate("""\
{shepherd_phrase} eyed the wool, {emo_proud}, and called out a guess
about what would come out the other side of the fleece-comb.
{elder_phrase} shook {elder_his_her} head and went on with the work.
To {goal_text}, {elder_he_she} composed {concept_phrase} as the comb's
rule and poured the input through. The REPL returned the only answer
that would do — the one the comb had actually produced."""),
]


# ─────────────────────── watchhouse slate (atom / state) ──────────────


_NOTEBOOK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. Watchhouse slate open on the table; any shepherd can read
    #    or atomically update. Elder explains the atomic write.
    #    Cat-J grounding: the slate is cool stone (cool ↔ stable
    #    intermediate state, persistent between writes), heavy under
    #    its frame (heavy ↔ accumulator the slate carries between
    #    moments). The elder's patience times the read-apply-write
    #    cycle so no other writer can step on it.
    SubplotTemplate("""\
A heavy watchhouse slate lay cool on the stone table, open for any
shepherd to read. "Atoms are like this slate," {elder_phrase} said,
{emo_patient}. "You can read the tally, or — carefully — update it
the atomic way: read the page, apply the change, write it back,
all in one motion that no other writer can step on." To
{goal_text}, {elder_he_she} composed {concept_phrase}, submitted
it, and let the REPL work the slate exactly as the form
prescribed."""),

    # 2. Atomic swap — read, apply, write, all in one motion.
    #    No race conditions.
    #    Cat-K rewrite: dialogue grounded in a real village
    #    procedure (two shepherds, one slate). Cat-J: {emo_patient}
    #    + heavy slate (heavy ↔ accumulator weight) + cool stone
    #    (cool ↔ stable persistent state).
    SubplotTemplate("""\
{elder_phrase} held the heavy slate, {emo_patient}; the cool stone
rested against {elder_his_her} forearm. "When I update the slate I
don't pick it up and walk away. I read the tally, apply the change,
and write it back — one quick motion. The REPL holds any second
writer at the threshold so the slate is never half-written." To
{goal_text}, {elder_he_she} composed {concept_phrase} for the slate,
submitted it, and the REPL applied the update atomically."""),

    # 3. The slate-and-the-stone-table — emphasizes the persistence
    #    of the slate between updates.
    SubplotTemplate("""\
"The watchhouse slate stays on the stone table," {elder_phrase}, {emo_patient}, said, "so
any shepherd who passes can read what's on the page right now. The page
changes only when someone writes — and only as the REPL allows." To
{goal_text}, {elder_he_she} composed {concept_phrase}, submitted the
form, and the REPL — reading or writing the slate as the form prescribed —
handed back the value the page had carried."""),

    # 4. The shared-tally template — generic emphasis that many shepherds
    #    can coordinate their updates on the same slate.
    SubplotTemplate("""\
"Many shepherds can come and go past the table," {elder_phrase}, {emo_patient}, said, "and
each one's read or write must agree with the others. The REPL sees to that —
no two writers stomp on each other's chalk." To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted it, and the
REPL — coordinating each access cleanly — handed back what the slate now
said."""),

    # 5. The shepherd tries to rip the page; elder updates the slate
    #    carefully. Generic fable beat applicable to any state operation.
    SubplotTemplate("""\
{shepherd_phrase}, {emo_proud}, swiped at the watchhouse slate on the table,
trying to scribble an answer over the tally. {elder_phrase} caught
{shepherd_him_her} firmly: slates shared by all the valley need careful
updates, not snatches. To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL — applying the update
the runtime's careful way — handed back the value the slate now held."""),
]


# ─────────────────────── counting sheep / fleeces (arithmetic) ────────


_ACORN_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The shepherd-guesses, elder-counts template — shepherd claims he knows
    #    by sight, elder counts carefully.
    SubplotTemplate("""{shepherd_phrase} eyed the grazing flock {place}, {emo_proud}, and called out a
guess about how many sheep were there without bothering to count. {elder_phrase}
simply began counting — to {goal_text} required no eyeballing, only the form.
{elder_he_she_cap} composed {concept_phrase}, submitted it to the REPL. The
runtime returned the count the form computed, and the slate showed the answer
the patient way."""),

    # 2. The flock-grows-or-shrinks template — for inc/dec, +/-.
    SubplotTemplate(""""Watch the flock," {elder_phrase}, {emo_patient}, said, gesturing at the grazing sheep. "Every
operation either adds a lamb, removes one, or combines what's already there —
the flock grows or shrinks by exactly what you say." To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted it, and the REPL
returned the new count, the flock settled into its new arrangement."""),

    # 3. The careful-count template — generic; the operation is whatever
    #    the form says, but the elder's care with numbers is the metaphor.
    SubplotTemplate("""{elder_phrase}, {emo_patient}, arranged the tally-stick {place}, careful with the count.
"Numbers in Clojure don't fudge," {elder_he_she} said. "Whatever you do —
adding sheep to the count, subtracting, dividing wool-weight into shares with
leftovers, comparing two flocks — the runtime gets it exactly right, every
time." To {goal_text}, {elder_he_she} composed {concept_phrase}, submitted
it. The REPL handed back the count, slate cool against the elder's
quiet hand."""),

    # 4. The shepherd-boasts-wrong template — shepherd claims answer by sight;
    #    elder counts and REPL proves shepherd wrong.
    SubplotTemplate("""{shepherd_phrase}, {emo_proud}, glanced at the flock {place} and shouted out
what {shepherd_he_she} claimed the count would be, without bothering to tally.
"I know numbers," {shepherd_he_she} insisted. {elder_phrase} simply reached for
the tally-stick and began marking carefully. To {goal_text}, {elder_he_she}
composed {concept_phrase} and submitted it. The REPL returned
the true count — which was not what {shepherd_phrase} had claimed."""),

    # 5. The exact-number template — generic; emphasizes that the REPL gives
    #    the exact count, no matter the operation.
    SubplotTemplate(""""Whatever the flock looks like after the operation," {elder_phrase}, {emo_patient}, said,
"the runtime gives the exact count — small or large, remainder or whole, the
answer is precise." To {goal_text}, {elder_he_she} composed {concept_phrase},
submitted it, and the REPL handed back the value, exactly as the operation
had produced it."""),
]


# ─────────────────────── fold-gates (and / or / falsey) ───────────────


_GATE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The shepherd-tries-to-jump template — shepherd guesses gate state,
    #    elder tests carefully.
    #    Cat-J grounding: the latched fold-gates are heavy and slow
    #    (heavy ↔ short-circuit weight, slow ↔ careful boolean-by-boolean
    #    evaluation); the elder's patience times the swing exactly.
    SubplotTemplate("""{shepherd_phrase} sprinted toward the heavy fold-gates {place}, {emo_proud}, certain
they would open for {shepherd_him_her}. {elder_phrase}, {emo_patient}, slowed
and watched the latched timber: the only way to know which way the gates would
swing was to actually bring the value to them. To {goal_text}, {elder_he_she}
composed {concept_phrase} and submitted it. The REPL — testing the gates
properly — settled the matter, the heavy gates swinging exactly as the rule
said, regardless of {shepherd_phrase}'s guess."""),

    # 2. The truthy-and-falsey-rule template — generic.
    #    Cat-K rewrite (was abstract list of values + flat closing).
    #    Now: shepherd asks a real question, elder names the rule
    #    plainly with two grounded examples, the form lands as the
    #    answer to that question. Cat-J: {emo_patient} + heavy gate
    #    timber (heavy ↔ short-circuit weight).
    SubplotTemplate(""""Why did the gate stay shut?" {shepherd_phrase} asked. {elder_phrase},
{emo_patient}, leaned on the heavy timber. "Two things and only two things
close these gates: nil and false. An empty bucket or a sleeping flock still
swings the gate open." To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL returned the verdict the
gate had carried."""),

    # 3. The first-closed-gate template — emphasizes short-circuiting.
    #    When multiple gates are chained, the first closed one stops the chain.
    #    Cat-J: {emo_patient} + heavy timber. Cat-K trim: cleaner
    #    explanation, less "the runtime checks it" filler.
    SubplotTemplate(""""You can't guess which way the gates will swing," {elder_phrase} said,
{emo_patient}, leaning on the heavy timber of the first fold-gate. "Bring
the value to the first gate. If it shuts, the chain stops there — the gates
behind it never see the value at all." To {goal_text}, {elder_he_she}
composed {concept_phrase} and submitted it. The REPL — checking
each gate in order, stopping at the first that closed — settled the matter
exactly as the rule said."""),

    # 4. The stone-gates-boast-template — shepherd claims to know gate behavior;
    #    elder evaluates the condition properly.
    SubplotTemplate("""{shepherd_phrase}, {emo_proud}, watched the fold-gates {place} and claimed to
know exactly what they would do without checking the condition. "I just know,"
{shepherd_he_she} insisted, calling out a prediction. {elder_phrase} only smiled
and reached for pen and slate. To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL — checking the gates
properly — returned the verdict the gates actually gave."""),

    # 5. The gate-carries-the-value template — generic emphasis on the REPL
    #    returning the value the gate carries, not just true or false.
    #    Cat-K rewrite: shepherd's question motivates the elder's
    #    answer; the gate-as-funnel image grounds the metaphor.
    #    Cat-J: {emo_patient} + heavy timber.
    SubplotTemplate(""""So the gate just says yes or no?" {shepherd_phrase} asked.
{elder_phrase}, {emo_patient}, shook {elder_his_her} head and tapped the heavy
timber. "Look closely. The gate carries the actual value through — sometimes
a strict yes or no, sometimes the very thing that passed the test." To
{goal_text}, {elder_he_she} composed {concept_phrase}, submitted it,
and the REPL returned the value the gates had carried
through."""),
]


# ─────────────────────── path-fork at lookout (if / cond / case) ──────


_FORK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The shepherd-shouts-the-path template — shepherd guesses which arm,
    #    elder evaluates the condition carefully.
    #    Cat-J grounding: the path-fork is steep (steep ↔ a strict
    #    branch — only one arm taken), the day is long (long ↔
    #    deliberate evaluation). The elder's patience holds the
    #    decision until the condition is read.
    SubplotTemplate("""{shepherd_phrase}, {emo_proud}, called out which arm of the steep fork at the lookout
{shepherd_he_she} was sure the runtime would take, without bothering to check
the condition. {elder_phrase}, {emo_patient}, only smiled in the long afternoon:
the only way to know is to evaluate the condition. To {goal_text}, {elder_he_she}
composed {concept_phrase} and submitted it. The REPL — checking the
condition properly — returned the value of the arm the form actually took."""),

    # 2. The crossroads-with-many-stones template — applies to `cond` / `case` /
    #    multi-arm branching. Type-neutral framing works for if (one stone),
    #    cond/case (many stones).
    SubplotTemplate("""The path {place} opened into a crossroads, each arm marked by a condition-stone.
"Branching forms work like this," {elder_phrase}, {emo_patient}, said: "the shepherd walks past
the stones in order, takes the first arm whose stone says true, and the value of
that arm is what comes back." To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL took the right arm and
returned its value."""),

    # 3. The unwalked-arm template — generic emphasis that branches not taken
    #    don't run at all.
    SubplotTemplate(""""What's important about a path-fork," {elder_phrase}, {emo_patient}, said, "is that the arm not
taken doesn't run at all. The runtime checks the condition, walks the right arm,
and the unwalked arm is just left behind." To {goal_text}, {elder_he_she}
composed {concept_phrase} and submitted it. The REPL — running only what
was needed — handed back the value of the chosen arm."""),

    # 4. The path-fork-boast template — shepherd boasts he can pick the arm
    #    without checking; elder takes the form to the lookout.
    SubplotTemplate("""{shepherd_phrase}, {emo_proud}, stood at the path-fork {place}, certain
{shepherd_he_she} could pick the right arm by sight alone. "I don't need to
check the condition," {shepherd_he_she} insisted. {elder_phrase} shook
{elder_his_her} head. To {goal_text}, {elder_he_she} composed {concept_phrase},
submitted it, and the REPL — taking the path that the condition actually
pointed to — returned the arm the fork had truly revealed."""),

    # 5. The condition-decides template — generic; emphasizes that the condition
    #    is what picks the arm, not the shepherd's hopes.
    SubplotTemplate(""""It isn't the shepherd who picks the arm," {elder_phrase}, {emo_patient}, said, "it's the
condition. Whatever the condition evaluates to, that decides." To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted it, and the REPL
— letting the condition decide — handed back the value of the arm the condition
had pointed at."""),
]


# ─────────────────────── village notice-post (def / namespace) ────────


_ROADSIGN_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The shepherd-misreads-the-notice template — shepherd guesses, elder
    #    reads the notice carefully.
    SubplotTemplate("""{shepherd_phrase}, {emo_proud}, glanced at the notice {place} and called out
what {shepherd_he_she} thought it said without slowing. {elder_phrase} stopped
and read carefully. To {goal_text}, the notice had to be read exactly:
{elder_he_she} composed {concept_phrase} and submitted it. The REPL —
reading literally — returned the right value, while {shepherd_phrase}'s guess
fell short."""),

    # 2. The notices-stay-where-posted template — generic emphasis that bindings
    #    persist and any later code reads them.
    SubplotTemplate(""""The good thing about a notice," {elder_phrase}, {emo_patient}, said, "is that it stays where
you posted it. The next shepherd along the path reads what's there now —
whatever the latest chalk says." To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL — reading the notices as the
form directed — returned the value the notice-post had recorded."""),

    # 3. The library-of-scrolls template — generic; the library of named scrolls
    #    is a property of the watchhouse, doesn't claim a specific operation.
    SubplotTemplate("""A small wooden library stood {place}, its shelves stocked with scrolls — each
scroll holding the notices for one stretch of the village. "Names live on
scrolls," {elder_phrase}, {emo_patient}, said: "to use a notice from a scroll, you make sure the
scroll is on the shelf where the REPL can find it." To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted it, and the REPL
— finding the right notice on the right scroll — returned the value the form
had asked for."""),

    # 4. The careful-naming template — generic emphasis on names being chosen
    #    and read with care.
    SubplotTemplate(""""Naming is half the art," {elder_phrase}, {emo_patient}, said, chalking a careful notice on
slate. "A clear name at the notice-post tells every later shepherd what to
expect; a careless one trips them up." To {goal_text}, {elder_he_she}
composed {concept_phrase} with the right name in mind, submitted it, and
the REPL — reading the name exactly — returned the value the notice had
promised."""),

    # 5. The notice-post-boast template — shepherd claims he doesn't need names;
    #    elder posts the notice carefully anyway.
    SubplotTemplate("""{shepherd_phrase}, {emo_proud}, waved dismissively at the townsfolk notice-post.
"Names are pointless," {shepherd_he_she} claimed. "I can remember everything by
sight." {elder_phrase} only sighed and began chalking more notices on the post.
To {goal_text}, {elder_he_she} composed {concept_phrase}, posted the named
notice, submitted it, and the REPL — following the careful names —
returned the value only naming could have preserved."""),
]


# ─────────────────────── practice-pen (try / catch / assert) ──────────


_SAFETYNET_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The shepherd-boasts-no-safety template — shepherd claims he doesn't need
    #    the practice-pen, elder carefully prepares it anyway.
    SubplotTemplate("""{shepherd_phrase} eyed the narrow path {place}, {emo_proud}, certain {shepherd_he_she}
could run it without a practice-pen or any safety measures. {elder_phrase} shook
{elder_his_her} head and quietly prepared the pen anyway. To {goal_text} required
no daring, only the safety work: {elder_he_she} composed {concept_phrase},
submitted it, and the REPL — catching anything that fell — returned the
answer the careful design had earned."""),

    # 2. The drills-cost-nothing template — REPL safety; mistakes here are
    #    learning chances, not disasters.
    SubplotTemplate(""""This is the practice-pen," {elder_phrase}, {emo_patient}, said {place}, gesturing wide. "A slip
here costs nothing. Write a form, see what comes back, fix it, try again. The
REPL is forgiving in a way that a real run with the flock is not." To
{goal_text}, {elder_he_she} composed {concept_phrase}, submitted it,
and the REPL returned the value — even if the form had been close to a mis-step."""),

    # 3. The error-and-recovery template — generic emphasis on the runtime
    #    catching errors and the work continuing.
    SubplotTemplate(""""What matters when something goes wrong," {elder_phrase}, {emo_patient}, said, "is that the work
can continue — the runtime catches the slip, takes the recovery path, and the
answer comes back even when something inside the form went off the trail." To
{goal_text}, {elder_he_she} composed {concept_phrase}, submitted it,
and the REPL — handling the slip cleanly — returned the value the recovery path
had produced."""),

    # 4. The pen-test-beats-boast template — shepherd claims no errors will
    #    happen; elder's practice-pen catches the slip anyway.
    SubplotTemplate("""{shepherd_phrase}, {emo_proud}, strutted past the practice-pen behind the
watchhouse, insisting {shepherd_he_she} had no need for testing or safety checks.
"My code is perfect," {shepherd_he_she} claimed. {elder_phrase} said nothing,
only smiled. To {goal_text}, {elder_he_she} composed {concept_phrase}, placed
the form in the practice-pen. The REPL — pen in place —
caught the slip that {shepherd_phrase} had not foreseen."""),

    # 5. The discipline-of-checking template — generic; emphasizes care in
    #    error handling and assertions.
    SubplotTemplate(""""There's a discipline to running safely," {elder_phrase}, {emo_patient}, said, "and it starts
with checking — making sure the form does what it claims, catching what could go
wrong before it does." To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL — applying whatever check or
catch the form had asked for — returned the value the discipline had earned."""),
]


# ─────────────────────── village log-book (IO / metadata) ─────────────


_SCROLL_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The log-book-on-the-table template — reading and writing.
    SubplotTemplate("""\
{shepherd_phrase}, {emo_proud}, claimed {shepherd_he_she} could guess
what the leather-bound village log-book would say without bothering
to open it. {elder_phrase} opened the book {place}, dipping a quill
into ink at the edge. "The world
outside the REPL is scrolls," {elder_he_she} said: "you read what
they say, you write what you want to keep, and the runtime carries
the words back and forth." To {goal_text}, {elder_he_she}
composed {concept_phrase} and submitted it. The REPL handed
back what the log-book actually held."""),

    # 2. The reading-and-writing template — generic; works for
    #    slurp/spit, line-seq, edn, JSON, prn, doc, etc.
    SubplotTemplate("""\
"Reading and writing watch-roll scrolls is just like reading and
writing forms," {elder_phrase}, {emo_patient}, said. "You ask the runtime for what's
on the parchment, you write what you want recorded, and the work
goes both ways through one quill." To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted it,
and the REPL handed back what the scroll had said — or what the
writing had committed."""),

    # 3. The careful-handling template — generic; emphasizes the
    #    discipline of handling external resources.
    SubplotTemplate("""\
"The world outside the REPL is bigger than the REPL,"
{elder_phrase}, {emo_patient}, said, "and the log-book out there has its own
discipline — open it carefully, handle it with care, close it when
you're done." To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL — handling the
scroll the runtime's careful way — returned the value the work had
produced."""),

    # 4. The shepherd-tries-to-shortcut template — shepherd guesses
    #    at the log-book's contents without reading.
    SubplotTemplate("""\
{shepherd_phrase}, {emo_proud}, claimed the log-book said exactly
what {shepherd_he_she} expected and didn't bother to actually read.
{elder_phrase} unrolled it carefully. To {goal_text} required the
log-book's actual contents — {elder_he_she_cap} composed
{concept_phrase}, submitted it, and the REPL — reading the
scroll faithfully — returned the value the parchment had held."""),

    # 5. The two-worlds template — generic; the inside-the-REPL
    #    world and the outside-the-REPL world meet at the scroll.
    SubplotTemplate("""\
"There's the world inside the REPL," {elder_phrase}, {emo_patient}, said, "and the
world outside it. Watch-roll scrolls are how the two meet — a value
crosses out and becomes letters on parchment, or letters on parchment
cross in and become a value again." To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted it,
and the REPL — bridging the two worlds — handed back the value the
work had carried."""),
]


# ─────────────────────── shepherds' fellowship (protocols) ────────────


_GUILD_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The founding-the-fellowship template — defprotocol.
    SubplotTemplate("""\
{elder_phrase} carved a small wooden sign {place}: "Shepherds'
Fellowship — any species may join." "A protocol is a fellowship,"
{elder_he_she} said. "It lists what every member must be able to
do — the methods. Any animal that can sign the book may claim
membership." To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL — fellowship
founded — handed back the fellowship's record."""),

    # 2. The shepherd-claims-all-species-call template — shepherd
    #    insists the call is the same; elder checks the fellowship's
    #    ledger to see each species' different answer.
    SubplotTemplate("""\
{shepherd_phrase}, {emo_proud}, insisted that every species in the
fellowship would answer the same way — {shepherd_he_she} just knew it.
{elder_phrase} only smiled and held up the fellowship ledger. "What
makes a fellowship useful," {elder_he_she} said, "is that the call is
the same for every member, but each species answers in its own way.
The runtime looks up which species the shepherd is, then runs that
species' answer." To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL — checking the
ledger, then dispatching to the right species — returned the
species-specific value."""),

    # 3. The fellowship-ledger template — generic emphasis on the
    #    fellowship's record being how the runtime knows who's a member.
    SubplotTemplate("""\
{elder_phrase}, {emo_patient}, held up the fellowship ledger. "Membership is in
this book," {elder_he_she} said: "the species, the methods they
swear they can perform, and the actual answers each species gives.
The runtime reads from the book whenever the call goes out." To
{goal_text}, {elder_he_she} composed {concept_phrase},
submitted it, and the REPL — checking the ledger as it ran —
returned the right answer."""),

    # 4. The boundaries-of-the-fellowship template — generic emphasis
    #    that each fellowship has its own membership.
    SubplotTemplate("""\
"Each fellowship has its own boundaries," {elder_phrase}, {emo_patient}, said.
"Belonging to the Shepherds' fellowship doesn't mean belonging to
the Goatherds' fellowship — the runtime checks each separately, and
only the right fellowship's answer comes back." To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted it,
and the REPL — respecting which fellowship was being called —
returned the right value."""),

    # 5. The shepherd-claims-membership template — shepherd boasts
    #    about a fellowship he hasn't joined.
    SubplotTemplate("""\
{shepherd_phrase}, {emo_proud}, declared that {shepherd_he_she}
could of course do whatever the fellowship's call demanded — even
though the species had never signed the book. {elder_phrase} only
smiled and asked for the actual implementation. To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted it, and
the REPL — checking the book first — returned the right answer
based on who had actually signed."""),
]


# ─────────────────────── village smithy (host interop) ────────────────


_TOOLSHED_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The borrowed-tool template — .method syntax / Class/static.
    SubplotTemplate("""\
{elder_phrase} reached into the foreign toolshed {place} and pulled
out a tool {elder_he_she} hadn't carved {elder_him_her}self — a tool
from the host platform. "This isn't ours," {elder_he_she} said, "but
we can call its methods directly: dot-prefix on the instance, or
slash for static." To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL — calling into
the foreign tool — handed back what its method had returned."""),

    # 2. The shepherd-calls-the-tool-wrong template — shepherd guesses
    #    at the calling convention; elder checks the labels and calls
    #    it correctly.
    SubplotTemplate("""\
{shepherd_phrase}, {emo_proud}, reached for a foreign tool from the
toolshed and tried to call it his own way, without checking the label.
{elder_phrase} caught {shepherd_him_her}. "Each tool in the foreign
toolshed has its own label," {elder_he_she} said, "and the right way
to call it depends on which kind of tool it is — some held by a
shepherd, some standard-issue called by the toolshed's name." To
{goal_text}, {elder_he_she} composed {concept_phrase} using the
right calling convention, submitted it, and the REPL — invoking
the host tool by its correct label — returned the value the host had
computed."""),

    # 3. The careful-handling-of-foreign-tools template — generic
    #    emphasis on host interop's discipline.
    SubplotTemplate("""\
"Foreign tools work, but they need careful handling,"
{elder_phrase}, {emo_patient}, said. "Their labels are different, their calling
conventions are different, and the runtime has to bridge between
Clojure and the host every time." To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted it,
and the REPL — making the bridge cleanly — handed back the value
the foreign tool had produced."""),

    # 4. The two-worlds template — generic; the valley's own toolshed
    #    and the foreign one meet at the interop boundary.
    #    Cat-K rewrite: ground the boundary in a real shepherd image.
    #    Cat-J: {emo_patient} + the cool stone wall (cool ↔ stable
    #    boundary).
    SubplotTemplate("""\
{elder_phrase}, {emo_patient}, pointed past the cool stone wall behind
the watchhouse to the smith's shed. "Our toolshed is on this side; the
smith's is on that side. When we need a smith's tool, the runtime
carries the value over the wall, asks the foreign tool to do its work,
and carries the result back." To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL — making the
crossing cleanly — returned the value the foreign tool had produced."""),

    # 5. The shepherd-grabs-the-wrong-tool template — shepherd guesses,
    #    elder checks the toolshed labels carefully.
    SubplotTemplate("""\
{shepherd_phrase}, {emo_proud}, grabbed at the foreign toolshed
without checking which tool was which. The wrong tool, of course,
made an awful sound. {elder_phrase} sighed and walked over: to
{goal_text} required reading the toolshed's labels carefully.
{elder_he_she_cap} composed {concept_phrase}, submitted it,
and the REPL — calling the right host method by name — returned the
value cleanly while {shepherd} watched, chastened."""),
]


# ─────────────────────── dispatched runner (agent / future / promise) ─


_RUNNERAHEAD_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The runner-sent-ahead template — future / agent.
    SubplotTemplate("""\
{elder_phrase} dispatched a young child-runner down the long path
{place}, work in pouch. "The runner goes ahead while we keep on
with our own business," {elder_he_she} said, "and when we need the
result we ask the runner to hand it back." To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted it,
and the REPL — sending the runner, fetching the result later —
returned the value when it was ready."""),

    # 2. The shepherd-snatches-before-runner-ready template — shepherd
    #    tries to grab the answer before the runner has finished; elder
    #    waits patiently.
    SubplotTemplate("""\
{shepherd_phrase}, {emo_proud}, kept trying to snatch at the runner's
pouch before the child had even returned from the errand. {elder_phrase}
held {shepherd_him_her} back. "Once you've sent the runner ahead,"
{elder_he_she} said, "you keep on with your own work. The result will
be there when you ask for it — sometimes you have to wait for the
runner to be finished, sometimes you can keep arranging things until
you need it." To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL — coordinating the
runner the patient way — returned the value when the runner had
finished."""),

    # 3. The patience-of-the-elder template — generic; the elder's
    #    willingness to wait for the runner is the fable beat.
    SubplotTemplate("""\
"The hard part isn't sending the runner," {elder_phrase}, {emo_patient}, said.
"The hard part is being patient enough to wait for the answer when
it comes — not snatching too early, not giving up too soon. The
runtime makes that easier than it sounds." To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted it,
and the REPL — coordinating the wait properly — returned the
runner's answer when the runner had it ready."""),

    # 4. The elder-coordinates template — generic; the runtime keeps
    #    track of each runner.
    SubplotTemplate("""\
{elder_phrase}, {emo_patient}, arranged a small relay {place}, runners and
messengers each in their place. "The runtime keeps track of who
sent what and when each one finishes," {elder_he_she} said, "so
the values come back in the right order, no matter how long each
runner takes." To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL — coordinating
the relay — returned the right value at the right time."""),

    # 5. The shepherd-doesn't-wait template — shepherd reaches for
    #    the runner's pouch before the runner returns.
    SubplotTemplate("""\
{shepherd_phrase}, {emo_proud}, reached for the runner's pouch
before the runner had even returned. {elder_phrase} held
{shepherd_him_her} back: a runner sent ahead must be allowed to
finish. To {goal_text}, {elder_he_she} composed {concept_phrase},
submitted it, and the REPL — waiting for the runner the
patient way — returned the value when the runner had actually
delivered it."""),
]


# ─────────────────────── elder's drill-card rewrite (macros) ──────────


_REWRITERULE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The rewriting-shorthand template — `defmacro` introduction.
    SubplotTemplate("""{elder_phrase}, {emo_patient}, sat at a small writing desk {place}, slate and chalk
in hand. "A macro," {elder_he_she} said, "is a rule that rewrites
the shorthand before the runtime ever sees it. You write the rule
once, and any form that names it gets rewritten on the way in."
To {goal_text}, {elder_he_she} composed {concept_phrase},
submitted it, and the REPL — first rewriting, then evaluating —
returned the value the rewritten form had produced."""),

    # 2. The rule-shapes-the-form template — generic; emphasizes
    #    that macros operate on forms, not values.
    #    Cat-K rewrite: anchor the abstract distinction in a concrete
    #    village scene (the watchhouse wall, fresh chalk). Cat-J:
    #    {emo_patient} + cool clay slate (cool ↔ stable rewrite stage
    #    that runs before evaluation).
    SubplotTemplate("""\"Here's the difference between a recipe and a rewrite-rule,"
{elder_phrase} said, {emo_patient}, fresh chalk in hand at the cool
watchhouse slate. "A recipe takes ingredients and makes a dish. A
rewrite-rule takes one form and produces a different form — only after
that does the runtime evaluate the new form." To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted it, and the
REPL — applying the rule first, then evaluating the rewritten form —
handed back the value."""),

    # 3. The runtime-applies-the-rule template — generic.
    #    Cat-K rewrite: dialogue grounds the order in a real village
    #    routine ("first the watchhouse rewrites the drill-card, then
    #    the morning watch follows it"). Cat-J: {emo_patient} +
    #    cool watchhouse slate.
    SubplotTemplate("""\"Order matters here," {elder_phrase} said, {emo_patient},
chalking on the cool watchhouse slate. "First the watchhouse rewrites
every drill-card that names the rule. Only after that — every
appearance of the rule expanded — does the morning watch follow what
the rewritten cards say." To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL — rewriting first,
evaluating second — returned the final value."""),

    # 4. The Shepherd-claims-no-rule-needed template — generic fable
    #    beat.
    SubplotTemplate("""{shepherd_phrase}, {emo_proud}, insisted that no rule was needed —
{shepherd_he_she} could write the form directly. {elder_phrase}
allowed that sometimes that's true, but the rule shines when many
forms need the same rewriting. To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted it,
and the REPL — handling the rule the rule's way —
returned the value the form had produced."""),

    # 5. The Shepherd-tries-to-skip-the-rule template.
    SubplotTemplate("""{shepherd_phrase}, {emo_proud}, insisted that the rule was unnecessary
— {shepherd_he_she} could write the rewritten form directly.
{elder_phrase} only smiled: a hand-rewritten form is fine once, but
the rule pays off when many forms need rewriting the same way. To
{goal_text}, {elder_he_she} composed {concept_phrase}, submitted
it, and the REPL — running the rule the rule's way — returned
the value the rewritten form had yielded."""),

    # 6. The elder writes out the rule on the chalk slate; the
    #    runtime rewrite wins. Careful authoring beats guessing.
    SubplotTemplate("""{shepherd_phrase}, {emo_desperate}, was finally learning: the macro
rule was not magic, only careful. {elder_phrase} took the goal —
to {goal_text} — and chalked the rewrite-rule on the slate for any
shepherd to use. {elder_he_she_cap} composed {concept_phrase}, submitted
it, and the REPL — reading the rule as written, rewriting the
form, then evaluating — handed back the only answer that would do:
the one the rule had actually produced."""),
]


# ─────────────────────── slate-and-chalk conventions (scribe / reader) ─


_SCRIBE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The reading-conventions-of-the-form template — generic;
    #    works for comments, whitespace, parens, do, reader macros.
    #    Cat-K rewrite: dialogue grounded in a real reading
    #    moment (chalk on slate, the village's posted rules).
    #    Cat-J: {emo_patient} + cool slate (cool ↔ stable read state).
    SubplotTemplate("""\"The runtime reads our forms the way the watchhouse reads its
posted notices," {elder_phrase} said, {emo_patient}, chalk in hand at
the cool slate. "What counts as one word, what's just spacing, what
should be ignored — every reader follows the same plain rules so the
notice doesn't change between writing and reading." To
{goal_text}, {elder_he_she} composed {concept_phrase}, submitted the
form, and the REPL — reading exactly by those rules — returned the
value the form had specified."""),

    # 2. The form-is-what-the-reader-sees template — generic.
    SubplotTemplate("""\"A form is what the reader sees," {elder_phrase}, {emo_patient}, said,
"after the conventions have been applied. Some marks count, some
don't; some shapes are expanded before the runtime even gets a
look. The form you write and the form the runtime evaluates
aren't always character-for-character the same." To
{goal_text}, {elder_he_she} composed {concept_phrase},
submitted it, and the REPL — reading carefully — returned
the value of what the conventions had produced."""),

    # 3. The careful-writing-careful-reading template — generic.
    SubplotTemplate("""{elder_phrase} unrolled a small slate {place} and wrote
slowly, paying attention to every mark. "The form has to be
written so the reader can read it cleanly," {elder_he_she}
said. "If the marks are right, the runtime gets the right form;
if not, not." To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL — reading
exactly as written — returned the value cleanly."""),

    # 4. The Shepherd-misreads-the-form template — generic fable beat.
    SubplotTemplate("""{shepherd_phrase}, {emo_proud}, glanced at the form and called out
what {shepherd_he_she} thought it would do without paying attention to
the conventions of how it was written. {elder_phrase} only
shook {elder_his_her} head — the runtime reads the form
exactly. To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL — reading
literally — returned the right value, while {shepherd}'s guess fell
short."""),

    # 5. The form-as-it-is template — generic.
    SubplotTemplate("""\"A form is what's actually there on the page," {elder_phrase},
{emo_patient}, said. "After the conventions of writing and reading
have done their work, the runtime sees the cleaned-up form and gives
back what it computes." To {goal_text}, {elder_he_she} composed
{concept_phrase} and submitted it. The REPL took the form as it was
and handed back the value."""),

    # 6. The shepherd claims the written form is wrong without reading;
    #    the elder reads it carefully and the REPL proves the answer.
    SubplotTemplate("""{shepherd_phrase}, {emo_proud}, swore the written form was nonsense
and would never work, certain {shepherd_he_she} could see through it
without so much as reading. {elder_phrase} simply opened the slate
quietly. To {goal_text}, {elder_he_she} composed {concept_phrase}
with the marks precisely placed, submitted it, and the REPL —
reading exactly as written — handed back the only answer that would do:
the one the careful marks had specified."""),
]


# ─────────────────────── chalk mark vs sheep (quote / symbols) ────────


_CHALKMARK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The mark-on-the-slate template — symbols vs values.
    SubplotTemplate("""{elder_phrase}, {emo_patient}, pointed at a name chalked onto the slate {place},
then at an actual sheep standing in the fold. "The mark on the
slate is the *name*; the sheep is the *value*. They are not
the same thing — and Clojure lets you talk about either one."
To {goal_text}, {elder_he_she} composed {concept_phrase},
submitted it, and the REPL — keeping the name and the
value distinct — returned the right answer."""),

    # 2. The label-the-form template — `quote` / `'`.
    SubplotTemplate("""\"To talk about the form itself rather than evaluating it,"
{elder_phrase}, {emo_patient}, said, "you label the form with a chalk mark
in front. Quoting tells the runtime: don't evaluate this, just hand
it back as the shape it is." To {goal_text}, {elder_he_she}
composed {concept_phrase} and submitted it. The REPL —
respecting the chalk mark — returned the form unevaluated."""),

    # 3. The labeling-form-vs-evaluating-it template — generic
    #    emphasis on the distinction without claiming a specific
    #    quote/unquote arrangement.
    SubplotTemplate("""\"There's a difference between *labeling* the form and
*evaluating* it," {elder_phrase}, {emo_patient}, said. "Quote in any of its
shapes is the labeling — the runtime hands you back the form,
not its value, unless you say otherwise." To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted the
form, and the REPL — labeling exactly what the form asked for —
returned the form-as-data, exactly as the marks had directed."""),

    # 4. The Shepherd-confuses-mark-with-value template.
    SubplotTemplate("""{shepherd_phrase}, {emo_proud}, mistook the chalk mark on the slate
for the sheep it pointed to. "It says sheep, so the value must be
a sheep!" {elder_phrase} reached for chalk: the mark and the sheep
are never the same thing. To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted it,
and the REPL — keeping mark and value distinct — returned the
right answer for the goal."""),

    # 5. The shepherd tries to evaluate the chalk mark directly; elder
    #    quotes it carefully and the REPL proves the answer.
    SubplotTemplate("""{shepherd_phrase}, {emo_proud}, tried to fetch the value that the
chalk mark should carry, insisting it must be there waiting.
{elder_phrase} picked up the slate and pointed: the mark itself is
all you need when you quote it. To {goal_text}, {elder_he_she}
composed {concept_phrase} with the chalk mark in place, submitted
it, and the REPL — honoring the quote — handed back the only
answer that would do: the form-as-data, marked and unevaluated."""),

    # 6. The name and value are kept always distinct; symbols let you
    #    choose which one to work with. Generic emphasis without fable.
    # Cat-K rewrite: simpler, story-shaped — shepherd asks; elder
    # demonstrates the mark/sheep distinction with a small concrete
    # gesture. Cat-J: {emo_patient} + cool slate.
    SubplotTemplate("""{shepherd_phrase} pointed at the chalk-mark `wolf` on the slate.
"That's a wolf," {shepherd_he_she} said. {elder_phrase}, {emo_patient},
shook {elder_his_her} head and pointed at the empty meadow beyond the
pen: "That mark is the name of a wolf — not the wolf. Clojure keeps
the two apart on purpose, and the form tells the runtime which one
you want." To {goal_text}, {elder_he_she} composed {concept_phrase},
submitted it, and the REPL — choosing mark or value as the
form asked — returned the answer the form had directed."""),
]


# ─────────────────────── brand-sorting gate (multimethods) ────────────


_SORTINGTABLE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The sorting-gate template — `defmulti`.
    SubplotTemplate("""A wooden gate with three branching paths stood at the fold {place}.
"Defmulti is a sorting-gate," {elder_phrase}, {emo_patient}, said. "You decide
what brand on each sheep to look at; the gate reads the brand and
routes each sheep down the matching pen." To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted the
form, and the REPL — reading the sheep's brand, picking the
gate — returned the value the right pen had produced."""),

    # 2. The brand-handling template — `defmethod`.
    SubplotTemplate("""\"To add a pen to the sorting-gate," {elder_phrase}, {emo_patient}, said,
"you say what brand the pen handles and what the shepherds do
when a sheep with that brand arrives." To {goal_text},
{elder_he_she} composed {concept_phrase} for the right
pen, submitted it, and the REPL — adding the pen,
dispatching the sheep — returned the pen-specific value."""),

    # 3. The runtime-reads-the-brand template — generic; the
    #    sorting-gate reads whatever the dispatch function returns
    #    and routes accordingly.
    SubplotTemplate("""\"What the gate sorts by is up to you," {elder_phrase}, {emo_patient}, said.
"You decide what to look at on each sheep — a brand, a fleece color, a
mark, anything. The runtime reads it, finds the matching pen,
and routes that one." To {goal_text}, {elder_he_she}
composed {concept_phrase} and submitted it. The REPL —
reading the brand the dispatch function produced — returned the
value the right pen had given."""),

    # 4. The flexible-routing template — generic emphasis on
    #    the open-dispatch nature.
    SubplotTemplate("""\"The good thing about a sorting-gate," {elder_phrase}, {emo_patient}, said,
"is that you can keep adding new pens whenever a new brand of
sheep shows up. The original gate doesn't change; the runtime
just learns one more route." To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted the
form, and the REPL — routing through the gate cleanly —
returned the right value."""),

    # 5. The Shepherd-tries-to-skip-the-sort template.
    SubplotTemplate("""{shepherd_phrase}, {emo_proud}, tried to push a sheep through the
sorting-gate without bothering to check its brand. {elder_phrase}
pointed at the gate: every sheep must show the brand the gate
sorts by. To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL — reading the
brand first, dispatching second — returned the value from the
correct pen."""),

    # 6. The elder sets up the sorting-gate with multiple dispatch paths;
    #    each sheep goes to its proper pen. Generic emphasis on routing.
    SubplotTemplate("""{elder_phrase}, {emo_patient}, stood at the sorting-gate {place}, watching each
sheep arrive marked. "Every animal gets its own pen," {elder_he_she}
said, "not by guessing, but by reading the brand. The dispatch
function is the reader; the gate is the router." To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted it,
and the REPL — reading each brand, routing each sheep — handed back
the value from the pen the brand had earned."""),
]


# ─────────────────────── labeled tally-box (deftype / defrecord) ──────


_CARRYINGCASE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The labeled-compartments template — defrecord.
    SubplotTemplate("""\
{elder_phrase}, {emo_patient}, held up a small wooden tally-box {place}, its inside
divided into labeled pigeon-holes — one for count, one for weight,
one for breed. "A defrecord is like this box," {elder_he_she} said:
"named compartments holding specific things; a mark on the outside
saying what kind of record it is." To {goal_text}, {elder_he_she}
composed {concept_phrase} and submitted it. The REPL —
constructing the box, filling its compartments — returned the value
the tally-box held."""),

    # 2. The bare-box template — deftype.
    SubplotTemplate("""\
"A deftype is a barer tally-box," {elder_phrase}, {emo_patient}, said. "Compartments,
a mark — no map-like behavior unless you ask for it. Faster, more
focused, lighter in hand." To {goal_text}, {elder_he_she}
composed {concept_phrase} and submitted it. The REPL —
constructing the bare box as specified — returned the value
inside."""),

    # 3. The reaching-into-a-compartment template — field access.
    SubplotTemplate("""\
"To reach into a named compartment," {elder_phrase}, {emo_patient}, explained,
"you ask for it by name. The box knows where each hole is; the
runtime fetches what's inside cleanly." To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted it,
and the REPL — opening the right compartment of the tally-box —
returned exactly what was tucked there."""),

    # 4. The shepherd-guesses-the-contents template.
    SubplotTemplate("""\
{shepherd_phrase}, {emo_proud}, peered at the wooden tally-box
without opening it and insisted {shepherd_he_she} could guess what
each compartment held. {elder_phrase} shook {elder_his_her} head and
reached for the box. To {goal_text} required opening the actual
compartments — {elder_he_she_cap} composed {concept_phrase},
submitted it, and the REPL — reading the tally-box's structure
faithfully — returned the value {shepherd} had been guessing at."""),

    # 5. The construction-from-named-parts template.
    SubplotTemplate("""\
{shepherd_phrase}, {emo_desperate}, was beginning to see: the
tally-box was not magic, only careful naming. {elder_phrase} took
the goal — to {goal_text} — and composed {concept_phrase} to fill
the box's pigeon-holes with the exact values the form required.
{elder_he_she_cap} submitted it, and the REPL — constructing the
named tally-box, compartment by compartment — handed back the
complete box with all its record inside."""),
]


# ─────────────────────── tally-stick walk (reduce / count) ────────────


_TALLYWALK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The walking-the-row template — reduce.
    #    Cat-J grounding: the flock is long (long ↔ collection size),
    #    the tally-stick grows heavy with notches (heavy ↔ accumulator
    #    value), the elder's patience pays out across the walk.
    SubplotTemplate("""\
{elder_phrase}, {emo_patient}, walked the long pasture flock
{place}, one sheep at a time, notching a wooden tally-stick that
grew heavier with the crook's edge. "Reduce is this walk,"
{elder_he_she} said: "at each sheep, you combine it into the
running tally; at the end, the final count is your answer." To
{goal_text}, {elder_he_she} composed {concept_phrase}, submitted
it, and the REPL — walking the flock, notching the
tally-stick — returned the final number."""),

    # 2. The starting-tally template — reduce with init.
    #    Cat-J grounding: the stick is already partly heavy at the
    #    start (heavy ↔ initial accumulator), the walk is long
    #    (long ↔ collection size); patience carries the running
    #    total without losing a notch.
    SubplotTemplate("""\
"You don't have to start the tally-stick empty," {elder_phrase}
said, {emo_patient}, holding up a stick already heavy with notches.
"If you start with a different value, the long walk begins from
there — each new sheep adds to the starting count from that notch."
To {goal_text}, {elder_he_she} composed {concept_phrase}, submitted
it, and the REPL — starting from the given count, walking
the flock — returned the final tally."""),

    # 3. The simple-count template — count.
    SubplotTemplate("""\
"The simplest tally-stick walk is just counting," {elder_phrase}, {emo_patient}, said: "step along the flock, notch once per sheep, no other work.
The runtime does this the same way for any kind of collection."
To {goal_text}, {elder_he_she} composed {concept_phrase},
submitted it, and the REPL — walking the row, notch by notch —
returned the count."""),

    # 4. The shepherd-guesses-the-count template.
    SubplotTemplate("""\
{shepherd_phrase}, {emo_proud}, looked at the flock without bothering
to count and called out what {shepherd_he_she} thought the tally
would be. {elder_phrase} began the walk without comment. To {goal_text} required actually notching the tally-stick
— {elder_he_she_cap} composed {concept_phrase}, submitted it,
and the REPL — walking the real count — returned the only answer
that would do: the one the flock's actual size had produced."""),

    # 5. The patient walk to the answer.
    SubplotTemplate("""\
{shepherd_phrase}, {emo_desperate}, was beginning to understand: the
tally-stick walk was not magic, only patient. {elder_phrase} took the
goal — to {goal_text} — and composed {concept_phrase}, step by step
through the collection. {elder_he_she_cap} submitted it, and the
REPL — notching the tally-stick at each element, no shortcuts — handed
back the running total at the end, the only count that was true."""),
]


# ─────────────────────── knotted tally-cord (string ops) ──────────────


_BEADSTRING_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The threading-beads template — string concat / subs.
    SubplotTemplate("""\
{elder_phrase}, {emo_patient}, held up a knotted tally-cord {place}, a long string
threaded with knots at intervals. "Strings in Clojure are like this,"
{elder_he_she} said: "a cord of characters in order. Splice two cords
together, and the threads join; cut a section out, and you get a
shorter cord." To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL — splicing or
cutting as the form said — returned the new tally-cord."""),

    # 2. The counting-knots template — string length / substring.
    SubplotTemplate("""\
"To count the knots on the cord," {elder_phrase}, {emo_patient}, said, "walk your
finger along from the start. Want a section? Hold at one knot and
cut to another — you get a shorter thread, the original untouched."
To {goal_text}, {elder_he_she} composed {concept_phrase},
submitted it, and the REPL — counting or cutting the
tally-cord — returned the answer the knotted string had given up."""),

    # 3. The shepherd-yanks-at-the-thread template.
    SubplotTemplate("""\
{shepherd_phrase}, {emo_proud}, yanked at the tally-cord {place}
without bothering to count the knots. {elder_phrase} stopped
{shepherd_him_her} firmly: a cord's knots are precise — every one
in its place, every position counted. To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted it,
and the REPL — handling the cord carefully, knot by knot —
returned the right answer."""),

    # 4. The immutability of the original template.
    SubplotTemplate("""\
"Watch the tally-cord carefully," {elder_phrase}, {emo_patient}, said, holding it up.
"When I work with it, this cord stays exactly as it was — what I get
back is a fresh cord with the change made, leaving the original
untouched." To {goal_text}, {elder_he_she} composed
{concept_phrase}, submitted it, and the REPL returned a new
arrangement while the original cord waited in {elder_his_her} hand,
every knot still in its place."""),

    # 5. The shepherd-claims-knowledge template.
    SubplotTemplate("""\
{shepherd_phrase}, {emo_proud}, insisted {shepherd_he_she} knew what
answer the tally-cord would give without actually counting the knots
or cutting a section. {elder_phrase} only smiled and began the careful
work. To {goal_text}, {elder_he_she} composed {concept_phrase},
submitted it, and the REPL — tracing the cord faithfully,
knot by knot — handed back the only answer the string's structure
would allow: the one {shepherd} had not even thought to check."""),
]


# ─────────────────────── dawn fence-walk (recur / loop) ───────────────


_CIRCUIT_SUBPLOTS: list[SubplotTemplate] = [
        # 1. The circuit-without-growing-the-trail template — recur.
    SubplotTemplate("""{elder_phrase}, {emo_patient}, walked the fence-line at dawn {place}, each lap
returning to the same starting stone with fresh tallies in hand.
"Recur is this circuit," {elder_he_she} said: "back to the top with
new bindings, no extra trail laid down behind us." To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted it,
and the REPL — looping without growing the call-stack — returned
the final value."""),

    # 2. The base-case template — termination.
    SubplotTemplate("""\"Every circuit has a stopping condition," {elder_phrase}, {emo_patient}, said.
"Without one, the walker goes round and round forever. With one, the
walker knows when the circuit is done and the answer is the final
tally." To {goal_text}, {elder_he_she} composed {concept_phrase},
submitted it, and the REPL — looping until the base case —
returned the value the final lap produced."""),

    # 3. The shepherd-doesn't-trust-the-circuit template.
    SubplotTemplate("""{shepherd_phrase}, {emo_proud}, distrusted the very idea of a dawn
fence-walk: surely you'd just wander forever? {elder_phrase} smiled
patiently — the base case is the walker's compass. To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted it,
and the REPL — looping the right number of times, then stopping —
returned the value cleanly."""),

    # 4. The circuit-as-state-machine template.
    SubplotTemplate("""\"Watch the fence-walk," {elder_phrase}, {emo_patient}, said {place}. "Each lap
brings new bindings — the tally changes, the path count changes, the
walk moves forward by the logic we've composed." To {goal_text},
{elder_he_she} composed {concept_phrase}, submitted it,
and the REPL — lap by lap, from one binding set to the next — handed
back the final state when the circuit was done."""),

    # 5. The shepherd-wants-shortcuts template.
    SubplotTemplate("""{shepherd_phrase}, {emo_desperate}, wanted to take a shortcut rather
than walk the dawn fence-line carefully. {elder_phrase} shook
{elder_his_her} head: every lap must return to the fence, the base
case must be checked, the circuit must close. To {goal_text},
{elder_he_she} composed {concept_phrase}, step by step around
the fence, and submitted it. The REPL — walking the circuit
faithfully, lap by lap — handed back the only answer that would do:
the one the complete fence-walk had produced."""),

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
# of its connective prose around the {concept_phrase} action — pouch
# is "tucked into the belt-pouch", basket is "for the wool-basket",
# slate is "for the watchhouse slate", etc. The slots provide the
# specifics.


def _story(connective_prose: str) -> SubplotTemplate:
    """Build a story-scaffold template for a family.

    The template is the canonical 5-act story shape; the family
    differentiates itself only by the {connective_prose} around the
    composed/submitted action — using the family's verb (compose /
    pour / chalk / tuck / etc.) and its imagery vocabulary.
    """
    return SubplotTemplate(f"""\
{{scenario}} {{need}} {{mapping}}

{connective_prose} {{resolution}}""", fits_tags=("story",))


# Family-specific story templates. The connective prose for each uses
# the family's verb + imagery, so the metaphor's vocabulary stays
# consistent through the action act.

_POUCH_SUBPLOTS = _POUCH_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "with the binding tucked safely into the belt-pouch and submitted "
        "the form. The REPL pulled from the pouch as the form directed:"
    ),
]

_RECIPE_SUBPLOTS = _RECIPE_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} chalked {concept_phrase} onto "
        "the drill-card and submitted it. The REPL ran the routine "
        "end to end:"
    ),
]

_BASKET_SUBPLOTS = _BASKET_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "for the wool-basket and submitted it. The REPL handed back "
        "the arrangement:"
    ),
]

_SIEVE_SUBPLOTS = _SIEVE_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "as the fleece-comb's rule, poured the input through, and "
        "submitted it. The REPL caught what passed:"
    ),
]

_NOTEBOOK_SUBPLOTS = _NOTEBOOK_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "for the watchhouse slate and submitted it. The REPL "
        "applied the update on the slate:"
    ),
]

_ACORN_SUBPLOTS = _ACORN_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "and submitted it. The REPL counted out the answer:"
    ),
]

_GATE_SUBPLOTS = _GATE_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "and submitted it. The REPL let the fold-gates decide:"
    ),
]

_FORK_SUBPLOTS = _FORK_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "and submitted it. The REPL took the right path from "
        "the lookout:"
    ),
]

_ROADSIGN_SUBPLOTS = _ROADSIGN_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "and submitted it. The REPL read the notice-post and "
        "replied:"
    ),
]

_SAFETYNET_SUBPLOTS = _SAFETYNET_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "and submitted it. The REPL — practice-pen in place — "
        "handed back the value:"
    ),
]

_SCROLL_SUBPLOTS = _SCROLL_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "and submitted it. The REPL — quill in hand — completed "
        "the log-book entry:"
    ),
]

_GUILD_SUBPLOTS = _GUILD_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "and submitted it. The REPL — checking the fellowship roll "
        "— dispatched cleanly:"
    ),
]

_SORTINGTABLE_SUBPLOTS = _SORTINGTABLE_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "and submitted it. The REPL routed through the brand-gate:"
    ),
]

_CARRYINGCASE_SUBPLOTS = _CARRYINGCASE_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "and submitted it. The REPL constructed the tally-box:"
    ),
]

_TOOLSHED_SUBPLOTS = _TOOLSHED_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "and submitted it. The REPL — calling into the foreign "
        "smithy — returned:"
    ),
]

_RUNNERAHEAD_SUBPLOTS = _RUNNERAHEAD_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "and submitted it. The REPL coordinated the runner's "
        "return:"
    ),
]

_REWRITERULE_SUBPLOTS = _REWRITERULE_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "and submitted it. The REPL — applying the drill-card "
        "rewrite, then evaluating the rewritten form — returned:"
    ),
]

_SCRIBE_SUBPLOTS = _SCRIBE_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "and submitted it. The REPL read by the slate's "
        "conventions and returned:"
    ),
]

_CHALKMARK_SUBPLOTS = _CHALKMARK_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "and submitted it. The REPL — distinguishing chalk mark "
        "from the sheep it names — returned:"
    ),
]

_TALLYWALK_SUBPLOTS = _TALLYWALK_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "and submitted it. The REPL walked the row, notch by "
        "notch on the tally-stick:"
    ),
]

_BEADSTRING_SUBPLOTS = _BEADSTRING_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "and submitted it. The REPL spliced or counted along the "
        "tally-cord as the form said:"
    ),
]

_CIRCUIT_SUBPLOTS = _CIRCUIT_SUBPLOTS + [
    _story(
        "To {goal_text}, {elder_he_she} composed {concept_phrase} "
        "and submitted it. The REPL walked the fence-line without "
        "growing the trail:"
    ),
]
