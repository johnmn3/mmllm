"""Metaphor-bearing subplot pools for tortoise-hare.

The base `_GOAL_SUBPLOTS` (in grade_1.py) is generic Hare/Tortoise
banter that uses `{goal_text}` and `{concept_phrase}` but doesn't
illuminate any particular Clojure idiom. These pools below DO
illuminate specific idioms by carrying a fable-natural metaphor.

The full family catalog (23 families) — see also the table in
`docs/clojure-pedagogy/SKILL-fable-curriculum-author.md` under
"Metaphor families":

  Tier 1 (high-leverage core):
  - _POUCH_SUBPLOTS         — temporary-pouch (let-binding)
  - _RECIPE_SUBPLOTS        — paw-step-recipe (fn / comp / partial)
  - _BASKET_SUBPLOTS        — basket-and-label (collections)
  - _SIEVE_SUBPLOTS         — sieve-and-pour (HOFs / transducers)
  - _NOTEBOOK_SUBPLOTS      — notebook-on-a-stump (atom / ref)
  - _ACORN_SUBPLOTS         — counting/adding acorns (numbers)
  - _GATE_SUBPLOTS          — gates on the trail (boolean logic)
  - _FORK_SUBPLOTS          — fork at a crossroads (if / cond / case)
  - _ROADSIGN_SUBPLOTS      — posted signs on the road (def / namespace)
  - _SAFETYNET_SUBPLOTS     — safety net (errors, REPL safety)

  Tier 2 (substantial):
  - _SCROLL_SUBPLOTS        — scrolls written and read (IO, metadata)
  - _GUILD_SUBPLOTS         — guild any species can join (protocols)
  - _TOOLSHED_SUBPLOTS      — borrowing a tool from another toolshed
                              (host interop)

  Tier 3 (small but worth doing):
  - _REWRITERULE_SUBPLOTS   — scribe with the power to rewrite the
                              recipe before runtime (macros)
  - _SCRIBE_SUBPLOTS        — scribe's reading conventions
                              (comments, whitespace, parens, do, reader)
  - _CHALKMARK_SUBPLOTS     — chalk mark on bark vs the acorn it names
                              (quote / symbols)
  - _RUNNERAHEAD_SUBPLOTS   — sending a runner down the road
                              (agent / future / promise / await)
  - _SORTINGTABLE_SUBPLOTS  — sorting-table that routes by tag
                              (multimethods)
  - _CARRYINGCASE_SUBPLOTS  — labeled carrying-case
                              (deftype / defrecord)
  - _TALLYWALK_SUBPLOTS     — walking the row carrying a running tally
                              (reduce / count)
  - _BEADSTRING_SUBPLOTS    — strings as strings of beads
                              (str concat / subs)
  - _CIRCUIT_SUBPLOTS       — looping back without growing the trail
                              (recur / loop)

Pool sizing: 5 templates is the standard size; small families with
1-3 subjects use 3 templates. All templates use `{goal_text}` and
`{concept_phrase}` (never `{form_display}`), keeping the form-leak
design intact.

Authoring rules followed:
- pronoun case at sentence start uses `_he_she_cap` etc.
- no "and" right after `{concept_phrase}` (avoids "the logical and
  and submit it" stutters); use ", then submit", "; submit", or
  comma + new clause.
- no "write a form to {goal_text}" (avoids verb collision when
  goal_text starts with "write"); reframe as "to {goal_text},"
  + noun-clause.
- the metaphor is concretely named in every template (pouch /
  recipe / basket / notebook / sieve) so it lands as imagery, not
  as decoration.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import SubplotTemplate


# ─────────────────────── temporary-pouch (let) ────────────────────────


_POUCH_SUBPLOTS: list[SubplotTemplate] = [

    # 1. Tortoise tucks the value into the pouch; the pouch holds
    #    only for one stretch of road.
    SubplotTemplate("""\
{tortoise_phrase} reached for the small leather pouch tied at
{tortoise_his_her} hip. "When I want to {goal_text}," {tortoise_he_she}
said, "I tuck the value into the pouch and carry it just for the
stretch of road where I need it. By the next milestone the pouch
is empty again." {tortoise_he_she_cap} composed {concept_phrase},
the binding tucked away inside, and submitted the form to the
REPL. {hare_phrase} {emo_proud} had already forgotten what was
in the pouch — but the form, which still carried it, came back
with the answer."""),

    # 2. Pouch carried for one stretch of road; whatever's tucked
    #    inside is in force only while the pouch is worn. Type-neutral
    #    framing of the same temporary-binding idea (used to also
    #    construct a road-sign-shadowing scene, but that fired for
    #    plain-let subjects too and asserted a road-sign that wasn't
    #    in the form).
    SubplotTemplate("""\
{tortoise_phrase} patted the pouch at {tortoise_his_her} hip {emo_patient}.
"Whatever I tuck in here is in force only while the pouch is
worn," {tortoise_he_she} said, "and only for the form that names
the binding. Step past the form's edge and the pouch is empty
again." To {goal_text}, {tortoise_he_she} composed
{concept_phrase} with the binding tucked in for that stretch,
submitted it, and let the REPL read out the value the pouch had
held."""),

    # 3. Hare ignores the pouch; Tortoise's pouch-walk wins.
    SubplotTemplate("""\
{hare_phrase} brushed past the road-sign {place} {emo_proud}
calling out guesses without bothering to peek into
{tortoise_phrase}'s pouch. But the pouch was where the answer
lived: {tortoise_he_she_cap} intended to {goal_text}, and the
value was tucked away for exactly that stretch. {tortoise} wrote
out {concept_phrase}. The REPL — looking in
the pouch as the form told it to — handed back the value
{hare} had not even thought to check."""),

    # 4. Substitution rule — wherever the form names the binding,
    #    the runtime reaches into the pouch.
    SubplotTemplate("""\
"Wherever the form names the binding," {tortoise_phrase} {emo_patient} explained,
"the runtime reaches into the pouch and pulls out what was tucked
there." {tortoise_he_she_cap} demonstrated by intending to
{goal_text}: each mention of the bound name, {tortoise} said,
would be replaced by the value from the pouch the moment the
form ran. {tortoise_phrase} composed {concept_phrase}, submitted
the form, and the REPL substituted as promised — the pouch's
value threaded into every place the binding had been named."""),

    # 5. End-of-stretch — the pouch is empty when the form's
    #    stretch is over. (Scope ends.)
    SubplotTemplate("""\
"Watch the pouch carefully," {tortoise_phrase} said {place}.
"While the form's stretch of road runs, the pouch is full and
the binding is yours." To {goal_text}, {tortoise_he_she}
composed {concept_phrase} with the binding tucked safely inside,
then submitted the form. The REPL returned the value, and the
pouch — its work done — was empty again. {hare_phrase} {emo_tired}
finally admitted that the patient pouch-walk had carried the
day."""),
]


# ─────────────────────── paw-step-recipe (fn) ─────────────────────────


_RECIPE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. Writing a recipe-card; the runner along the road follows it.
    #    Type-neutral — works for named, anonymous, multi-arg, etc.
    #    The {goal_text}/{concept_phrase} say which kind.
    SubplotTemplate("""\
{tortoise_phrase} {emo_patient} kept a small stack of recipe-cards by the road,
each one a paw-step routine. "Recipes in Clojure are like these
cards," {tortoise_he_she} said {emo_content}: "the ingredients go at the head,
the steps in order, and the last step is what gets served." To
{goal_text}, {tortoise_he_she} wrote out {concept_phrase} on
a fresh card, submitted the form. The REPL followed the
recipe and handed back the value the last step had produced."""),

    # 2. The recipe-as-runnable-routine — emphasizes the call site.
    SubplotTemplate("""\
"A recipe is only useful when it runs," {tortoise_phrase} {emo_patient} said,
holding up a card. "Write the steps, set the ingredients beside
them, and the kitchen does the rest." To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the
form, and the REPL — taking the recipe and its ingredients —
handed back what the steps had produced."""),

    # 3. Last step is what you serve. (Body returns last form;
    #    type-neutral and pedagogically true for all fn bodies.)
    SubplotTemplate("""\
"In any recipe," {tortoise_phrase} {emo_patient} explained, "the last step is
what you serve." {tortoise_he_she_cap} took the goal — to
{goal_text} — and wrote the routine's paw-steps in order, knowing
that whatever the final line evaluated to was what the runner
would carry back. {tortoise} composed {concept_phrase}, submitted
the form, and the REPL — discarding the earlier steps' values —
handed back only the dish from the last."""),

    # 4. Recipes feeding into recipes — emphasizes the chained
    #    nature when relevant. Type-neutral phrasing: the chain is
    #    described as something that *can* happen, not as something
    #    the form is necessarily doing.
    SubplotTemplate("""\
"Recipes can feed into one another," {tortoise_phrase} {emo_patient} said,
spreading several cards on the path. "What one recipe serves, the
next can take as its ingredient — together they make a longer
routine." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — walking
through the recipe in order — handed back the value at the
end."""),

    # 5. The Hare-skips-the-recipe template — Hare guesses,
    #    Tortoise actually writes the recipe. Generic fable beat.
    SubplotTemplate("""\
{hare_phrase} {emo_proud} insisted {hare_he_she} could just
shout the answer rather than bother writing a recipe.
{tortoise_phrase} only smiled and reached for a fresh card. To
{goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form. The REPL — running the recipe paw-step
by paw-step — handed back the value {hare} had been guessing
at."""),
]


# ─────────────────────── basket-and-label (collections) ───────────────


_BASKET_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The basket-on-the-path template — generic; whatever the
    #    operation, the basket stays as it was, the form returns
    #    the new arrangement.
    SubplotTemplate("""\
{tortoise_phrase} {emo_patient} pointed to a small basket on the path {place}.
"Whatever I want to do with what's inside," {tortoise_he_she}
said {emo_content}, "I read from the basket, work the change, and the basket
itself stays as it was — what I get back is a fresh arrangement."
To {goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form, and let the REPL handle the basket exactly
as the operation prescribed."""),

    # 2. The labels-and-positions template — works for tagged pouches
    #    (maps), positional rows (vectors), or kind-only baskets
    #    (sets). The narrative is generic; goal_text says which.
    SubplotTemplate("""\
"You can find what you want in a basket several ways,"
{tortoise_phrase} {emo_patient} said, gesturing at the woven shape:
"by the tag pinned to it, by its place in line, or by simply
asking whether it's there at all." To {goal_text},
{tortoise_he_she} wrote {concept_phrase} for the basket,
submitted the form. The REPL applied the lookup or update
exactly as the form directed."""),

    # 3. The procession template — for ordered collections
    #    (vectors, lists, seqs). Sub-template is more
    #    list/vector-leaning but doesn't claim a specific type.
    SubplotTemplate("""\
A line of animals had formed {place}, each one taking the next
animal's tail in its paw — head at the front, the rest trailing
behind. "Many of our baskets are like this procession,"
{tortoise_phrase} {emo_patient} said. "You can grab the head, you can ask for
the tail, you can put a new animal at the front of the line."
To {goal_text}, {tortoise_he_she} composed {concept_phrase} {emo_content},
submitted the form. The REPL marched the procession exactly
as the form described."""),

    # 4. The new-basket-from-old template — immutability emphasis;
    #    works for any collection type.
    SubplotTemplate("""\
"Watch carefully," {tortoise_phrase} said, holding up the
original basket. "Whatever I do to it, this one sits unchanged
on the path — what I get back is a fresh basket with the change
made, leaving the first one exactly where it was." To
{goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form. The REPL returned a new arrangement
while the original waited, untouched. {hare_phrase} {emo_tired}
was beginning to see why nothing could be lost by trying."""),

    # 5. The Hare-rummages-loudly template — Hare guesses by
    #    rummaging; Tortoise's careful basket-work wins. Generic
    #    fable beat that fits any collection operation.
    SubplotTemplate("""\
{hare_phrase} began rummaging in the basket {emo_proud} calling
out guesses about its contents without quite checking. "I know
exactly what's in there," {hare_he_she} insisted. {tortoise_phrase}
shook {tortoise_his_her} head. To {goal_text} properly,
{tortoise_he_she} wrote {concept_phrase} carefully on a slate,
submitted the form. The REPL — looking into the basket the
way the form told it to — handed back the answer
{hare} had been guessing at."""),
]


# ─────────────────────── shared-notebook-on-a-stump (atom/ref) ────────


_NOTEBOOK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. Notebook open on a stump; any animal can read or
    #    atomically update.
    SubplotTemplate("""\
A notebook lay open on a tree stump in the middle of the meadow.
Any animal could walk up, read the page, or — carefully — update
it. "Atoms are like this notebook," {tortoise_phrase} {emo_patient} said. "You
can deref to read; you can swap! to write atomically, no matter
who else is watching." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}. The REPL work the
notebook exactly as the form prescribed."""),

    # 2. Atomic swap — read, apply, write, all in one motion.
    SubplotTemplate("""\
"When I want to update the notebook," {tortoise_phrase} {emo_patient} said,
"I don't pick it up and walk away — I read the page, apply the
change, and write it back, all in a single motion. If two
animals arrive at once, the runtime makes sure only one of us
goes through at a time." To {goal_text}, {tortoise_he_she}
composed {concept_phrase} for the notebook, submitted the form,
and the REPL applied the update atomically."""),

    # 3. The notebook-and-the-quiet-stump — emphasizes the
    #    persistence of the notebook between updates.
    SubplotTemplate("""\
"The notebook stays put on the stump," {tortoise_phrase} {emo_patient} said,
"so any animal who comes by can read what's on the page right
now. The page changes only when someone writes — and only as the
runtime allows." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — reading
or writing the notebook as the form prescribed — handed back the
value the page had carried."""),

    # 4. The shared-state template — generic emphasis that this is
    #    about coordinated updates among several animals.
    SubplotTemplate("""\
"Many animals can come and go past the stump," {tortoise_phrase} {emo_patient} said, "and each one's read or write must agree with the others.
The runtime sees to that — no two writers stomp on each other's
work." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — coordinating
each access cleanly — handed back what the notebook now said."""),

    # 5. The Hare-snatches-the-notebook template — Hare tries to
    #    rip the page; Tortoise updates carefully. Generic fable
    #    beat applicable to any state operation.
    SubplotTemplate("""\
{hare_phrase} {emo_proud} swiped at the notebook on the stump,
trying to scribble an answer over the page. {tortoise_phrase}
caught {hare_him_her} firmly: notebooks shared by all the meadow
need careful updates, not snatches. To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the form,
and the REPL — applying the update the runtime's careful way —
handed back the value the page now held."""),
]


# ─────────────────────── sieve-and-pour (map/filter/transduce) ────────


_SIEVE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The general sieve — works for transform (map),
    #    select (filter), select-counted (take/drop), or dedupe
    #    (distinct). The rule attached at the sieve's mouth
    #    decides what happens to each pebble.
    SubplotTemplate("""\
{tortoise_phrase} {emo_patient} held up a sieve {place} — a paw-step rule
attached at its mouth. "Whatever rule we hang on the sieve,"
{tortoise_he_she} said {emo_content}, "the basket's pebbles pass through one
at a time: some are changed, some kept, some dropped, depending
on the rule." To {goal_text}, {tortoise_he_she} composed
{concept_phrase} as the sieve's rule, poured the basket through,
submitted the form. The REPL returned what the sieve had
let through."""),

    # 2. The pour-through-and-collect template — generic emphasis
    #    on the new-basket-out-the-other-side metaphor.
    SubplotTemplate("""\
{tortoise_phrase} {emo_patient} balanced a sieve over an empty basket. "The
pebbles go in at the top," {tortoise_he_she} said {emo_content}, "and the
sieve does its work — applying the rule, choosing or changing —
and what lands in the basket below is the result." To
{goal_text}, {tortoise_he_she} composed {concept_phrase},
poured the input through. The REPL collected what fell into the receiving basket."""),

    # 3. Stacked sieves — output of one feeds the next.
    #    (comp xform.)
    SubplotTemplate("""\
{tortoise_phrase} {emo_patient} stacked two sieves one above the other, the
output of the first feeding into the second. "What lands at the
bottom," {tortoise_he_she} said, "has been through both rules in
order — applied as a single combined sieve." To {goal_text},
{tortoise_he_she} composed {concept_phrase} as a stack of
sieves, poured the input through, submitted the form, and the
REPL caught what the stack let through."""),

    # 4. The receiver template — pour into any kind of basket.
    #    (into / into with xform.)
    SubplotTemplate("""\
"You can pour the result into any kind of basket you like,"
{tortoise_phrase} {emo_patient} said. "A row of pebbles, a unique-only
basket, a bag of any shape — the sieve doesn't care; the
receiver does." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, chose the right empty receiver, poured
through the sieve, submitted the form. The REPL packed the
result into the basket of {tortoise_his_her} choosing."""),

    # 5. The Hare-tries-to-shortcut-the-sieve template — Hare
    #    guesses, Tortoise pours through carefully. Generic
    #    fable beat applicable to any sieve operation.
    SubplotTemplate("""\
{hare_phrase} eyed the basket {emo_proud} and called out a
guess about what would come out the other side of the sieve
without bothering to actually pour. {tortoise_phrase} shook
{tortoise_his_her} head and went on with the work: to
{goal_text}, {tortoise_he_she} composed {concept_phrase} as
the sieve's rule, poured the input through carefully,
submitted the form. The REPL returned the only answer
that would do — the one the sieve had actually produced."""),
]


# ─────────────────────── acorn-arithmetic (numbers) ───────────────────


_ACORN_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The counting-acorns template — generic arithmetic frame.
    SubplotTemplate("""\
{tortoise_phrase} laid acorns out on a flat stone {place}, sorting
them {emo_patient}. "Numbers in Clojure are like acorns in heaps,"
{tortoise_he_she} said. "You can count them. You can add heaps
together. You can split a heap." To {goal_text}, {tortoise_he_she}
composed {concept_phrase}. The REPL hand back the count."""),

    # 2. The basket-grows-or-shrinks template — for inc/dec, +/-.
    SubplotTemplate("""\
"Watch the basket," {tortoise_phrase} said, gesturing {emo_patient}
at a small heap of acorns. "Every operation adds, takes away, or
combines — the heap grows or shrinks by exactly what you say." To
{goal_text}, {tortoise_he_she} composed {concept_phrase}, submitted
the form, and the REPL returned the new count."""),

    # 3. The careful-arrangement template — generic; the operation
    #    is whatever the form says, but the Tortoise's care with the
    #    acorns is what the metaphor carries.
    SubplotTemplate("""\
{tortoise_phrase} arranged a small heap of acorns {place} {emo_patient}.
"Numbers in Clojure don't fudge," {tortoise_he_she} said.
"Whatever you do, the runtime gets it right." To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the form,
and the REPL handed back the value."""),

    # 4. The Hare-counts-aloud template — Hare guesses by sight,
    #    Tortoise counts.
    SubplotTemplate("""\
{hare_phrase} eyed the heap {emo_proud} and called out a guess
without bothering to count. {tortoise_phrase} simply began counting,
{emo_patient}. To {goal_text} took no eyeballing — only the form.
{tortoise_he_she_cap} composed {concept_phrase}, submitted it to
the REPL, and the runtime returned the honest count."""),

    # 5. The exact-count template — generic; emphasizes that the
    #    REPL gives the exact number, no matter the operation.
    SubplotTemplate("""\
"The runtime gives the exact count," {tortoise_phrase} said,
{emo_patient}. "Small or large. Fraction or whole. The answer is
precise." To {goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form. The REPL handed back the value the
operation produced."""),
]


# ─────────────────────── gates-on-the-trail (boolean logic) ───────────


_GATE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The gate-on-the-trail template — generic for any boolean
    #    test, equality, or short-circuit.
    SubplotTemplate("""\
A small wooden gate stood across the trail {place}, swinging open
or closed by the value the runner brought to it. The gate was narrow
— only one verdict could pass at a time, no halfway. "Boolean forms
in Clojure are like gates," {tortoise_phrase} said, {emo_patient}.
"The runtime checks the value, swings the gate, and what comes back
is the gate's verdict." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL returned
whatever the gate had decided."""),

    # 2. The truthy/falsey-rules template — generic.
    SubplotTemplate("""\
"Only two things in Clojure close the gate," {tortoise_phrase}
{emo_patient} said: "nil and false. Everything else — zero, the
empty string, an empty list — opens it. The hinge holds tight; the rule is fixed." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL returned the
value the gate had passed, true or false."""),

    # 3. The boolean-verdict template — generic emphasis on the
    #    runtime's decision being the only authority.
    SubplotTemplate("""\
"Guessing won't tell you which way the gate opens,"
{tortoise_phrase} {emo_patient} said. "You bring the value to the gate, the
runtime checks it, and the gate hands back the only answer that
matters." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL settled the
matter — the gate held exactly as the rule said."""),

    # 4. The Hare-bumps-the-gate template — Hare guesses gate
    #    state, Tortoise tests.
    SubplotTemplate("""\
{hare_phrase} sprinted toward the gate {place} {emo_proud}
certain it would swing open for {hare_him_her}. {tortoise_phrase}
slowed and watched: the only way to know which way the gate
would swing was to actually carry the value to it. To
{goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form. The REPL settled the matter — the gate
had swung exactly as the rules said, regardless of {hare_phrase}'s
guess."""),

    # 5. The decisive-gate template — generic emphasis on the
    #    runtime returning the value the gate carries (not always
    #    a strict bool — `and` returns the last truthy, `or`
    #    returns the first truthy, etc.).
    SubplotTemplate("""\
"The gate carries the value through, not just a yes or a no,"
{tortoise_phrase} said, {emo_patient}. "Whatever the gate's verdict,
that's what the runtime hands back — sometimes a strict true or
false, sometimes the very value that passed the test. The gate is
narrow but it doesn't strip what walks through." To {goal_text},
{tortoise_phrase} composed {concept_phrase}, submitted the form,
and the REPL returned the value the gate had carried through."""),
]


# ─────────────────────── fork-in-the-path (if/cond/case/when) ─────────


_FORK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The fork-on-the-trail template — generic; the trail
    #    branches and the condition decides which arm runs. Works
    #    for if, when, cond, case alike.
    SubplotTemplate("""\
The trail forked {place}, with one or more arms branching off and
each arm marked with a condition. The arms led to different ends —
the runner could only walk one. "Branching forms in Clojure are
forks like this," {tortoise_phrase} said, {emo_patient}. "The
runtime checks the condition, takes the matching arm, and only
that arm's value comes back." To {goal_text}, {tortoise_he_she}
composed {concept_phrase}, submitted the form. The REPL —
having taken the right arm — handed back its value."""),

    # 2. The crossroads template — applies to `cond` / `case` /
    #    multi-arm branching. Type-neutral framing: "the runner
    #    walks past stones" works for if (one stone), cond/case
    #    (many stones), case (matching tokens).
    SubplotTemplate("""\
The trail {place} opened into a crossroads, each arm marked by a
small condition-stone. The day was hot and the wrong arm was a
long way back. "Branching forms work like this," {tortoise_phrase}
said, {emo_patient}: "the runner walks past the stones in order,
takes the first arm whose stone says true, and the value of that
arm is what comes back." To {goal_text}, {tortoise_he_she}
composed {concept_phrase}, submitted the form. The REPL took
the right arm and returned its value."""),

    # 3. The unrun-arm template — generic emphasis that branches
    #    not taken don't run.
    SubplotTemplate("""\
"What's important about a fork," {tortoise_phrase} said,
{emo_patient}, "is that the arm not taken doesn't run at all. The
trail is long and effort is precious — the runtime checks the
condition, walks the right arm, and the unrun arm is just left
behind." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — running only
what was needed — handed back the value of the chosen arm."""),

    # 4. The Hare-tries-to-skip-the-condition template — Hare
    #    guesses which arm; Tortoise actually checks. Generic
    #    fable beat applicable to any branching.
    SubplotTemplate("""\
{hare_phrase} {emo_proud} called out which arm of the fork
{hare_he_she} was sure the runtime would take, without bothering
to check the condition. {tortoise_phrase} only smiled: the only
way to know is to evaluate the condition. To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the form,
and the REPL — checking the condition properly — returned the
value of the arm the form actually ran."""),

    # 5. The one-form-decides template — generic; emphasizes that
    #    the condition is what decides, not the runner's hopes.
    SubplotTemplate("""\
"It isn't the runner who picks the arm," {tortoise_phrase} said,
{emo_patient}, "it's the condition. The trail is the trail; whatever
the condition evaluates to, that decides which arm runs." To
{goal_text}, {tortoise_he_she} composed {concept_phrase}, submitted
the form, and the REPL — letting the condition decide — handed
back the value of the arm the condition had pointed at."""),
]


# ─────────────────────── road-sign (def / namespace) ──────────────────


_ROADSIGN_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The posted-sign-on-the-road template — `def`.
    SubplotTemplate("""\
{tortoise_phrase} {emo_patient} drove a small wooden post {place}
and nailed a fresh sign to it. The post was set deep — once the
sign was up it would last for every later runner. "A def is a sign
by the road," {tortoise_he_she} said {emo_content}. "Anyone passing reads the
name, learns the value, and can refer to it later by name alone."
To {goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form. The REPL planted the sign — the name now
bound to its value for any later runner along the road."""),

    # 2. The signs-stay-where-posted template — generic emphasis
    #    that bindings persist on the road and any later runner
    #    reads them.
    SubplotTemplate("""\
"The good thing about a sign," {tortoise_phrase} said {emo_patient}
"is that it stays where you posted it. The road is long but the
sign holds; the next runner reads what's there now — whatever the
latest paint says." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — reading the
signs as the form directed — returned the value the road had
recorded."""),

    # 3. The roadside-library template — generic; the library of
    #    scrolls is a property of the world, doesn't claim a
    #    specific operation.
    SubplotTemplate("""\
A small wooden library stood {place}, its shelves stocked with
scrolls — each scroll holding the signs for one stretch of road.
The shelves were many but the right one was easy to find when its
name was clear. "Names live on scrolls," {tortoise_phrase} said,
{emo_patient}: "to use a sign from a scroll, you make sure the
scroll is on the shelf where the runtime can find it." To
{goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form. The REPL — finding the right sign on the
right scroll — returned the value the form had asked for."""),

    # 4. The careful-naming template — generic emphasis on names
    #    being chosen and read carefully.
    SubplotTemplate("""\
"Naming is half the art," {tortoise_phrase} said {emo_patient}
sketching a careful sign in the dust. "The road is long and the
runners who follow are many — a clear name tells every later
runner what to expect; a careless one trips them up." To
{goal_text}, {tortoise_he_she} composed {concept_phrase} with the
right name in mind, submitted the form. The REPL — reading
the name exactly — returned the value the sign had promised."""),

    # 5. The Hare-misreads-the-sign template — Hare guesses,
    #    Tortoise reads carefully.
    SubplotTemplate("""\
{hare_phrase} {emo_proud} glanced at the sign {place} and
called out what {hare_he_she} thought it said without slowing.
{tortoise_phrase} stopped and read carefully. To {goal_text}, the
sign had to be read exactly: {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — reading
literally — returned the right value, while {hare}'s guess fell
short."""),
]


# ─────────────────────── safety-net (errors / REPL safety) ────────────


_SAFETYNET_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The net-under-the-leap template — `try`/`catch`.
    SubplotTemplate("""\
{tortoise_phrase} {emo_patient} stretched a small net beneath a high jump
{place}. "If the runner falls, the net catches them; the run
doesn't end, only the path bends." To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the
form, and the REPL — net in place — caught the trouble and
returned the value the catch-arm had specified, the run continuing
the patient way."""),

    # 2. The practice-meadow template — REPL safety; nil punning.
    SubplotTemplate("""\
"This is the practice meadow," {tortoise_phrase} {emo_patient} said {place},
gesturing wide. "A stumble here costs nothing. Type a form, see
what comes back, fix it, try again. The REPL is forgiving in a
way that a real race is not." To {goal_text}, {tortoise_he_she}
composed {concept_phrase}. The REPL returned the value — even if the form had been close to a
mis-step."""),

    # 3. The slip-and-recovery template — generic emphasis on
    #    the runtime catching errors and continuing.
    SubplotTemplate("""\
"What matters when something goes wrong," {tortoise_phrase} {emo_patient} said,
"is that the run can continue — the runtime catches the slip,
takes the recovery path, and the answer comes back even when
something inside the form went off the trail." To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the
form, and the REPL — handling the slip cleanly — returned the
value the recovery path had produced."""),

    # 4. The check-and-continue template — generic.
    SubplotTemplate("""\
"There's a discipline to running safely," {tortoise_phrase} {emo_patient} said,
"and it starts with checking — making sure the form does what it
claims, catching what could go wrong before it does." To
{goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form. The REPL — applying whatever check or
catch the form had asked for — returned the value the discipline
had earned."""),

    # 5. The Hare-tries-the-jump template — Hare ignores the net,
    #    Tortoise demonstrates the safety design.
    SubplotTemplate("""\
{hare_phrase} eyed the high jump {place} {emo_proud} certain
{hare_he_she} could clear it without a net. {tortoise_phrase}
shook {tortoise_his_her} head and stretched the net carefully. To
{goal_text} required no daring, only the net: {tortoise_he_she}
composed {concept_phrase}, submitted the form. The REPL —
catching anything that fell — returned the answer the safety
design had earned."""),
]


# ─────────────────────── scroll-and-quill (IO / metadata) ─────────────


_SCROLL_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The scroll-on-the-table template — reading and writing.
    SubplotTemplate("""\
{tortoise_phrase} {emo_patient} unrolled a long scroll {place}, dipping a quill
into ink at the edge. "The world outside the REPL is scrolls,"
{tortoise_he_she} said: "you read what they say, you write what
you want to keep, and the runtime carries the words back and
forth." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL handed back
what the scroll had said, or what the writing had committed."""),

    # 2. The reading-and-writing template — generic; works for
    #    slurp/spit, line-seq, edn, JSON, prn, etc.
    SubplotTemplate("""\
"Reading and writing scrolls is just like reading and writing
forms," {tortoise_phrase} {emo_patient} said. "You ask the runtime for what's
on the parchment, you write what you want recorded, and the work
goes both ways through one quill." To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the
form, and the REPL handed back what the scroll had said — or
what the writing had committed."""),

    # 3. The careful-handling template — generic; emphasizes the
    #    discipline of handling external resources.
    SubplotTemplate("""\
"The world outside the REPL is bigger than the REPL,"
{tortoise_phrase} {emo_patient} said, "and a scroll out there has its own
discipline — open it carefully, handle it with care, close it
when you're done." To {goal_text}, {tortoise_he_she}
composed {concept_phrase}, submitted the form. The REPL —
handling the scroll the runtime's careful way — returned the
value the work had produced."""),

    # 4. The Hare-tries-to-shortcut-the-scroll template — generic
    #    fable beat.
    SubplotTemplate("""\
{hare_phrase} {emo_proud} claimed the scroll said exactly what
{hare_he_she} expected and didn't bother to actually read.
{tortoise_phrase} unrolled it carefully. To {goal_text} required
the scroll's actual contents — {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — reading the
scroll faithfully — returned the value the parchment had
held."""),

    # 5. The two-worlds template — generic; the inside-the-REPL
    #    world and the outside-the-REPL world meet at the scroll.
    SubplotTemplate("""\
"There's the world inside the REPL," {tortoise_phrase} {emo_patient} said,
"and the world outside it. Scrolls are how the two meet — a value
crosses out and becomes letters on parchment, or letters on
parchment cross in and become a value again." To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the
form, and the REPL — bridging the two worlds — handed back the
value the work had carried."""),
]


# ─────────────────────── guild-of-runners (protocols) ─────────────────


_GUILD_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The founding-the-guild template — `defprotocol`.
    SubplotTemplate("""\
{tortoise_phrase} {emo_patient} carved a small wooden sign {place}: "Runners'
Guild — any species may join." "A protocol is a guild,"
{tortoise_he_she} said. "It lists what every member must be able
to do — the methods. Any animal that can sign the book may claim
membership." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — guild
founded — handed back the guild's record."""),

    # 2. The same-call-many-species template — generic; emphasizes
    #    polymorphism's central idea without claiming a specific
    #    operation (defprotocol vs extend vs dispatch).
    SubplotTemplate("""\
"What makes a guild useful," {tortoise_phrase} {emo_patient} said, "is that
the call is the same for every member, but each species answers
in its own way. The runtime looks up which species the runner
is, then runs that species' answer." To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the
form, and the REPL — dispatching to the right species — returned
the species-specific value."""),

    # 3. The guild-ledger template — generic emphasis on the
    #    guild's record being how the runtime knows who's a member.
    SubplotTemplate("""\
{tortoise_phrase} {emo_patient} held up the guild ledger. "Membership is in
this book," {tortoise_he_she} said: "the species, the methods
they swear they can perform, and the actual answers each species
gives. The runtime reads from the book whenever the call goes
out." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — checking
the ledger as it ran — returned the right answer."""),

    # 4. The boundaries-of-the-guild template — generic emphasis
    #    that each guild has its own membership.
    SubplotTemplate("""\
"Each guild has its own boundaries," {tortoise_phrase} {emo_patient} said.
"Belonging to the Runners' guild doesn't mean belonging to the
Singers' guild — the runtime checks each separately, and only
the right guild's answer comes back." To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the
form, and the REPL — respecting which guild was being called —
returned the right value."""),

    # 5. The Hare-claims-membership template — Hare boasts about
    #    a guild he hasn't joined.
    SubplotTemplate("""\
{hare_phrase} {emo_proud} declared that {hare_he_she} could of
course do whatever the guild's call demanded — even though the
species had never signed the book. {tortoise_phrase} only smiled
and asked for the actual implementation. To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the form,
and the REPL — checking the book first — returned the right answer
based on who had actually signed."""),
]


# ─────────────────────── tool-from-another-toolshed (host interop) ────


_TOOLSHED_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The borrowed-tool template — `.method` syntax.
    SubplotTemplate("""\
{tortoise_phrase} reached into a different toolshed {place} {emo_patient} and
pulled out a tool {tortoise_he_she} hadn't carved {tortoise_him_her}self
— a tool from the host platform. "This isn't ours," {tortoise_he_she}
said, "but we can call its methods directly: dot-prefix on the
instance, or slash for static." To {goal_text}, {tortoise_he_she}
composed {concept_phrase}, submitted the form. The REPL —
calling into the foreign tool — handed back what its method had
returned."""),

    # 2. The labeled-toolshed template — generic; works for both
    #    instance methods (held by an animal) and static methods
    #    (standard-issue, called by toolshed-name). The
    #    {goal_text}/{concept_phrase} say which.
    SubplotTemplate("""\
"Each tool in the foreign toolshed has its own label,"
{tortoise_phrase} {emo_patient} said, "and the right way to call it depends on
which kind of tool it is — some held by an animal, some
standard-issue called by the toolshed's name." To {goal_text},
{tortoise_he_she} composed {concept_phrase} using the right
calling convention, submitted the form. The REPL — invoking
the host tool by its label — returned the value the host had
computed."""),

    # 3. The careful-handling-of-foreign-tools template — generic
    #    emphasis on host interop's discipline.
    SubplotTemplate("""\
"Foreign tools work, but they need careful handling,"
{tortoise_phrase} {emo_patient} said. "Their labels are different, their
calling conventions are different, and the runtime has to bridge
between Clojure and the host every time." To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the
form, and the REPL — making the bridge cleanly — handed back the
value the foreign tool had produced."""),

    # 4. The two-worlds template — generic; Clojure-side and
    #    host-side meet at the interop boundary.
    SubplotTemplate("""\
"There's the meadow's own toolshed," {tortoise_phrase} {emo_patient} said,
"and there's the foreign one. The runtime moves a value across
the boundary, calls the foreign tool, and brings the result back
into the meadow." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — bridging
the two toolsheds — returned the value cleanly."""),

    # 5. The Hare-grabs-the-wrong-tool template — Hare guesses,
    #    Tortoise checks the toolshed.
    SubplotTemplate("""\
{hare_phrase} {emo_proud} grabbed at the foreign toolshed
without checking which tool was which. The wrong tool, of course,
made an awful sound. {tortoise_phrase} sighed and walked over: to
{goal_text} required reading the toolshed's labels carefully.
{tortoise_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — calling the right host method by name —
returned the value cleanly while {hare} watched, chastened."""),
]


# ─────────────────────── rule-that-rewrites-recipes (macros) ──────────


_REWRITERULE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The rewriting-scribe template — `defmacro` introduction.
    SubplotTemplate("""\
{tortoise_phrase} sat at a small writing desk {place} {emo_patient}, quill in
paw. "A macro," {tortoise_he_she} said, "is a rule that rewrites
the recipe before the runtime ever cooks it. Write the rule
once, and any recipe that uses it gets rewritten on the way to
the kitchen." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — first
rewriting, then evaluating — returned the value the rewritten
recipe yielded."""),

    # 2. The rule-shapes-the-form template — generic; emphasizes
    #    that macros operate on forms, not values.
    SubplotTemplate("""\
"Here's the difference between a rule and a recipe,"
{tortoise_phrase} {emo_patient} said. "A recipe takes ingredients and makes a
dish. A rule takes a *form* and makes a different *form* — only
then does the runtime get to evaluate it." To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the
form, and the REPL — applying the rule to the form first, then
evaluating — handed back the value the rewritten form had
produced."""),

    # 3. The runtime-applies-the-rule template — generic.
    SubplotTemplate("""\
"The order matters," {tortoise_phrase} {emo_patient} said. "When a rule is
involved, the runtime first walks through the form and applies
the rule wherever it sees one — and only then does it evaluate
the result." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — rewriting
first, evaluating second — returned the final value."""),

    # 4. The Hare-claims-no-rule-needed template — generic fable
    #    beat.
    SubplotTemplate("""\
{hare_phrase} {emo_proud} insisted that no rule was needed —
{hare_he_she} could write the form directly. {tortoise_phrase}
allowed that sometimes that's true, but the rule shines when many
forms need the same rewriting. To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the form,
and the REPL — handling the rule's rewrite the rule's way —
returned the value the form had produced."""),

    # 5. The Hare-tries-to-skip-the-rule template.
    SubplotTemplate("""\
{hare_phrase} {emo_proud} insisted that the rule was unnecessary
— {hare_he_she} could write the rewritten recipe directly.
{tortoise_phrase} only smiled: a hand-rewritten recipe is fine
once, but the rule pays off when many recipes need rewriting the
same way. To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — running the
rule the rule's way — returned the value the rewritten recipe
yielded."""),
]


# ─────────────────────── scribe-shorthand (read-time conventions) ─────


_SCRIBE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The reading-conventions-of-the-form template — generic;
    #    works for comments, whitespace, parens, do, reader macros.
    SubplotTemplate("""\
"There are conventions for how the runtime *reads* a form,"
{tortoise_phrase} {emo_patient} said: "what counts as one token, what's just
spacing, what gets ignored, what gets grouped together. The
scribe and the reader both follow the same conventions." To
{goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form. The REPL — reading exactly by the
conventions — returned the value the form had specified."""),

    # 2. The form-is-what-the-reader-sees template — generic.
    SubplotTemplate("""\
"A form is what the reader sees," {tortoise_phrase} {emo_patient} said,
"after the conventions have been applied. Some marks count, some
don't; some shapes are expanded before the runtime even gets a
look. The form you write and the form the runtime evaluates
aren't always character-for-character the same." To
{goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form. The REPL — reading carefully — returned
the value of what the conventions had produced."""),

    # 3. The careful-writing-careful-reading template — generic.
    SubplotTemplate("""\
{tortoise_phrase} {emo_patient} unrolled a small slate {place} and wrote
slowly, paying attention to every mark. "The form has to be
written so the reader can read it cleanly," {tortoise_he_she}
said. "If the marks are right, the runtime gets the right form;
if not, not." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — reading
exactly as written — returned the value cleanly."""),

    # 4. The Hare-misreads-the-form template — generic fable beat.
    SubplotTemplate("""\
{hare_phrase} {emo_proud} glanced at the form and called out
what {hare_he_she} thought it would do without paying attention to
the conventions of how it was written. {tortoise_phrase} only
shook {tortoise_his_her} head — the runtime reads the form
exactly. To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — reading
literally — returned the right value, while {hare}'s guess fell
short."""),

    # 5. The form-as-it-is template — generic.
    SubplotTemplate("""\
"A form is what's actually there on the page," {tortoise_phrase} {emo_patient} said. "After the conventions of writing and reading have done their work, the runtime evaluates the cleaned-up form and hands back what it computed." To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the
form, and the REPL — taking the form exactly as it was — handed
back the value."""),
]


# ─────────────────────── chalk-marks-vs-acorns (quote / symbols) ──────


_CHALKMARK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The mark-on-the-bark template — symbols vs values.
    SubplotTemplate("""\
{tortoise_phrase} {emo_patient} pointed at a name scratched into the bark
{place}, then at an actual acorn lying on the path. "The mark on
the bark is the *name*; the acorn is the *value*. They are not
the same thing — and Clojure lets you talk about either one."
To {goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form. The REPL — keeping the name and the
value distinct — returned the right answer."""),

    # 2. The label-the-list template — `quote` / `'`.
    SubplotTemplate("""\
"To talk about the form itself rather than evaluating it,"
{tortoise_phrase} {emo_patient} said, "you label the form with a chalk mark
in front. Quoting tells the runtime: don't cook this, just hand
it back as the shape it is." To {goal_text}, {tortoise_he_she}
composed {concept_phrase}, submitted the form. The REPL —
respecting the chalk mark — returned the form unevaluated."""),

    # 3. The labeling-form-vs-evaluating-it template — generic
    #    emphasis on the distinction without claiming a specific
    #    quote/unquote arrangement.
    SubplotTemplate("""\
"There's a difference between *labeling* the form and
*evaluating* it," {tortoise_phrase} {emo_patient} said. "Quote in any of its
shapes is the labeling — the runtime hands you back the form,
not its value, unless you say otherwise." To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the
form, and the REPL — labeling exactly what the form asked for —
returned the form-as-data, exactly as the marks had directed."""),

    # 4. The Hare-confuses-name-with-value template.
    SubplotTemplate("""\
{hare_phrase} {emo_proud} mistook the name on the bark for the
acorn it pointed to. "It says hare, so the value must be the
hare!" {tortoise_phrase} only shook {tortoise_his_her} head: the
mark and the acorn are never the same thing. To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the form,
and the REPL — keeping mark and acorn distinct — returned the
right answer for the goal."""),
]


# ─────────────────────── runner-sent-ahead (agent / future / promise) ─


_RUNNERAHEAD_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The runner-sent-ahead template — future / agent.
    SubplotTemplate("""\
{tortoise_phrase} {emo_patient} dispatched a young messenger down the long road
{place}, work in paw. "The runner goes ahead while we keep on
with our own business," {tortoise_he_she} said, "and when we
need the result we ask the runner to hand it back." To
{goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form. The REPL — sending the runner, fetching
the result later — returned the value when it was ready."""),

    # 2. The eventually-returns template — generic; a runner sent
    #    ahead eventually returns the value, however the
    #    coordination is arranged.
    SubplotTemplate("""\
"Once you've sent the runner ahead," {tortoise_phrase} {emo_patient} said, "you
keep on with your own work. The result will be there when you ask
for it — sometimes you wait for the runner to finish; other times you keep
arranging things until you need it." To
{goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form. The REPL — coordinating the runner the
way the form prescribed — returned the value when it was
ready."""),

    # 3. The patience-of-the-Tortoise template — generic; the
    #    Tortoise's willingness to wait for the runner is the
    #    fable beat.
    SubplotTemplate("""\
"The hard part isn't sending the runner," {tortoise_phrase} {emo_patient} said.
"The hard part is being patient enough to wait for the answer
when it comes — not snatching too early, not giving up too soon.
The runtime makes that easier than it sounds." To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the
form, and the REPL — coordinating the wait properly — returned
the runner's answer when the runner had it ready."""),

    # 4. The Tortoise-coordinates template — generic.
    SubplotTemplate("""\
{tortoise_phrase} {emo_patient} arranged a small relay {place}, runners and
messengers each in their place. "The runtime keeps track of who
sent what and when each one finishes," {tortoise_he_she} said,
"so the values come back in the right order, no matter how long
each runner takes." To {goal_text}, {tortoise_he_she}
composed {concept_phrase}, submitted the form. The REPL —
coordinating the relay — returned the right value at the right
time."""),

    # 5. The Hare-doesn't-wait template — Hare reads before
    #    runner returns.
    SubplotTemplate("""\
{hare_phrase} {emo_proud} reached for the runner's pouch before
the runner had even returned. {tortoise_phrase} held {hare_him_her}
back: a runner sent ahead must be allowed to finish. To
{goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form. The REPL — waiting for the runner the
patient way — returned the value when the runner had actually
delivered it."""),
]


# ─────────────────────── sorting-table (multimethods) ─────────────────


_SORTINGTABLE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The sorting-table template — `defmulti`.
    SubplotTemplate("""\
A long wooden table stood {place}, with several arms branching off
its sides. "Defmulti is a sorting-table," {tortoise_phrase} {emo_patient} said.
"You decide what stamp on the runner to look at; the table routes
each runner down the matching arm." To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the
form, and the REPL — reading the runner's stamp, picking the
arm — returned the value the right arm had produced."""),

    # 2. The branch-of-the-table template — `defmethod`.
    SubplotTemplate("""\
"To add a branch to the sorting-table," {tortoise_phrase} {emo_patient} said,
"you say what stamp the branch handles and what behavior runs
when a runner with that stamp arrives." To {goal_text},
{tortoise_he_she} composed {concept_phrase} for the right
branch, submitted the form. The REPL — adding the branch,
dispatching the runner — returned the branch-specific value."""),

    # 3. The runtime-reads-the-stamp template — generic; the
    #    sorting-table reads whatever the dispatch function returns
    #    and routes accordingly.
    SubplotTemplate("""\
"What the table sorts by is up to you," {tortoise_phrase} {emo_patient} said.
"You decide what to look at on each runner — a tag, a kind, a
field, anything. The runtime reads it, finds the matching arm,
and runs that one." To {goal_text}, {tortoise_he_she}
composed {concept_phrase}, submitted the form. The REPL —
reading the stamp the dispatch function produced — returned the
value the right arm had given."""),

    # 4. The flexible-routing template — generic emphasis on
    #    the open-dispatch nature.
    SubplotTemplate("""\
"The good thing about a sorting-table," {tortoise_phrase} {emo_patient} said,
"is that you can keep adding new arms whenever a new kind of
runner shows up. The original table doesn't change; the runtime
just learns one more route." To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the
form, and the REPL — routing through the table cleanly —
returned the right value."""),

    # 5. The Hare-jumps-to-the-wrong-branch template.
    SubplotTemplate("""\
{hare_phrase} {emo_proud} leaped onto the sorting-table without
showing {hare_his_her} stamp. {tortoise_phrase} pointed at the
edge of the table: every runner must show the stamp the table
sorts by. To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — reading the
stamp first, dispatching second — returned the value from the
correct branch."""),
]


# ─────────────────────── carrying-case (deftype/defrecord) ────────────


_CARRYINGCASE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The labeled-compartments template — defrecord.
    SubplotTemplate("""\
{tortoise_phrase} {emo_patient} held up a small wooden case {place}, its inside
divided into labeled compartments. "Defrecord makes a case like
this," {tortoise_he_she} said: "named compartments holding
specific things; a stamp on the outside saying what kind of case
it is." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — constructing
the case, filling its compartments — returned the value the case
held or carried."""),

    # 2. The bare-case template — deftype.
    SubplotTemplate("""\
"A deftype is a barer case," {tortoise_phrase} {emo_patient} said. "Compartments,
a stamp — no map-like behavior unless you ask for it. Faster, more
focused, less convenient." To {goal_text}, {tortoise_he_she}
composed {concept_phrase}, submitted the form. The REPL —
constructing the bare case as specified — returned the value
inside."""),

    # 3. The reaching-into-the-compartment template — field
    #    access.
    SubplotTemplate("""\
"To reach into a labeled compartment," {tortoise_phrase} {emo_patient} said,
"you ask for it by name. The case knows where each compartment
is; the runtime fetches it cleanly." To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the
form, and the REPL — opening the right compartment — returned
exactly what was inside."""),
]


# ─────────────────────── the-tally-walk (reduce / count) ──────────────


_TALLYWALK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The walking-the-row template — reduce.
    SubplotTemplate("""\
{tortoise_phrase} walked the row of pebbles {place} {emo_patient}, one paw at a
time, a small slate in hand for the running tally. "Reduce is
this walk," {tortoise_he_she} said: "at each pebble, combine
it into the tally; at the end, the tally is your answer." To
{goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form. The REPL — walking the row, carrying the
tally — returned the final number."""),

    # 2. The starting-tally template — reduce with init.
    SubplotTemplate("""\
"You don't have to start the tally at zero," {tortoise_phrase} {emo_patient} said, holding up a slate already inscribed with a number. "If you
start with a different value, the walk begins from there — the
combine-step folds each pebble in from that starting point." To
{goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form. The REPL — starting from the given tally,
walking the row — returned the final value."""),

    # 3. The simple-count template — `count`.
    SubplotTemplate("""\
"The simplest tally-walk is just counting,"
{tortoise_phrase} {emo_patient} said: "step along the row, add one at every
pebble, no other operation. The runtime does this for any
collection — vector, list, map, string." To {goal_text},
{tortoise_he_she} composed {concept_phrase}, submitted the
form, and the REPL — walking the row, counting the steps —
returned the count."""),
]


# ─────────────────────── bead-string (string ops) ─────────────────────


_BEADSTRING_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The threading-beads template — `str` concat.
    SubplotTemplate("""\
{tortoise_phrase} {emo_patient} held up a string of small wooden beads {place}.
"Strings in Clojure are like this," {tortoise_he_she} said: "a
threaded line of characters, in order. Concat strings together,
and the threads are spliced; cut a substring out, and you get a
shorter thread." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — splicing or
cutting as the form said — returned the new bead-string."""),

    # 2. The counting-beads template — string length / substring.
    SubplotTemplate("""\
"To count the beads, walk the thread,"
{tortoise_phrase} {emo_patient} said. "Want a section of beads? Cut from one
position to another and you get a smaller thread, the original
untouched." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — counting or
cutting — returned the answer the bead-thread had given up."""),

    # 3. The Hare-yanks-at-the-thread template.
    SubplotTemplate("""\
{hare_phrase} {emo_proud} yanked at the bead-thread {place}
without bothering to count. {tortoise_phrase} stopped {hare_him_her}:
strings are precise — every bead in its place, every position
counted. To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — handling the
thread carefully — returned the right answer."""),
]


# ─────────────────────── circuit-around-the-meadow (recur / loop) ─────


_CIRCUIT_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The circuit-without-growing-the-trail template — recur.
    SubplotTemplate("""\
{tortoise_phrase} walked a small circle around the meadow {place} {emo_patient},
each lap returning to the same starting point with a slightly
different tally in hand. "Recur is this circuit," {tortoise_he_she}
said: "back to the top with new bindings, no extra trail laid
down behind us." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — looping
without growing the call-stack — returned the final value."""),

    # 2. The base-case template — termination.
    SubplotTemplate("""\
"Every circuit has a stopping condition," {tortoise_phrase} {emo_patient} said. "Without one, the runner walks forever. With one, the
runner knows when the laps are done and the tally is the
answer." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form. The REPL — looping
until the base case — returned the value the final lap
produced."""),

    # 3. The Hare-doesn't-trust-the-circuit template.
    SubplotTemplate("""\
{hare_phrase} {emo_proud} distrusted the very idea of a
circuit: surely you'd just walk forever? {tortoise_phrase} smiled
patiently — the base case is the runner's compass. To
{goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form. The REPL — looping the right number of
times, then stopping — returned the value cleanly."""),
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
# is "tucked into the pouch", basket is "for the basket", sieve is
# "as the sieve's rule", etc. The slots provide the specifics.


def _story(connective_prose: str) -> SubplotTemplate:
    """Build a story-scaffold template for a family.

    The template is the canonical 5-act story shape; the family
    differentiates itself only by the {connective_prose} around the
    composed/submitted action — using the family's verb (compose /
    pour / swap / tuck / etc.) and its imagery vocabulary.
    """
    return SubplotTemplate(f"""\
{{scenario}}

{{need}}

{{mapping}}

{connective_prose}

{{resolution}}""", fits_tags=("story",))


# Family-specific story templates. The connective prose for each
# uses the family's verb + imagery, so the metaphor's vocabulary
# stays consistent through the action act.

_POUCH_SUBPLOTS = _POUCH_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "with the binding tucked safely into the pouch and submitted the "
        "form. The REPL pulled from the pouch as the form directed:"
    ),
]

_RECIPE_SUBPLOTS = _RECIPE_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} wrote out {concept_phrase} "
        "on a card and submitted the form. The REPL ran the recipe end "
        "to end:"
    ),
]

_BASKET_SUBPLOTS = _BASKET_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "for the basket and submitted the form. The REPL handed back the "
        "arrangement:"
    ),
]

_SIEVE_SUBPLOTS = _SIEVE_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "as the sieve's rule, poured the input through, and submitted "
        "the form. The REPL caught what landed below:"
    ),
]

_NOTEBOOK_SUBPLOTS = _NOTEBOOK_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "for the notebook and submitted the form. The REPL applied the "
        "update on the stump:"
    ),
]

_ACORN_SUBPLOTS = _ACORN_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "and submitted the form. The REPL counted out the answer:"
    ),
]

_GATE_SUBPLOTS = _GATE_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "and submitted the form. The REPL let the gates decide:"
    ),
]

_FORK_SUBPLOTS = _FORK_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "and submitted the form. The REPL took the right arm:"
    ),
]

_ROADSIGN_SUBPLOTS = _ROADSIGN_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "and submitted the form. The REPL read the signs and replied:"
    ),
]

_SAFETYNET_SUBPLOTS = _SAFETYNET_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "and submitted the form. The REPL — net in place — handed back "
        "the value:"
    ),
]

_SCROLL_SUBPLOTS = _SCROLL_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "and submitted the form. The REPL — quill in hand — completed "
        "the scroll-work:"
    ),
]

_GUILD_SUBPLOTS = _GUILD_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "and submitted the form. The REPL — checking the guild book — "
        "dispatched cleanly:"
    ),
]

_SORTINGTABLE_SUBPLOTS = _SORTINGTABLE_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "and submitted the form. The REPL routed through the table:"
    ),
]

_CARRYINGCASE_SUBPLOTS = _CARRYINGCASE_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "and submitted the form. The REPL constructed the case:"
    ),
]

_TOOLSHED_SUBPLOTS = _TOOLSHED_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "and submitted the form. The REPL — calling into the foreign "
        "toolshed — returned:"
    ),
]

_RUNNERAHEAD_SUBPLOTS = _RUNNERAHEAD_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "and submitted the form. The REPL coordinated the runner's "
        "return:"
    ),
]

_REWRITERULE_SUBPLOTS = _REWRITERULE_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "and submitted the form. The REPL — applying the rewrite, then "
        "evaluating the rewritten form — returned:"
    ),
]

_SCRIBE_SUBPLOTS = _SCRIBE_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "and submitted the form. The REPL read by the conventions and "
        "returned:"
    ),
]

_CHALKMARK_SUBPLOTS = _CHALKMARK_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "and submitted the form. The REPL — distinguishing label from "
        "value — returned:"
    ),
]

_TALLYWALK_SUBPLOTS = _TALLYWALK_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "and submitted the form. The REPL walked the row carrying the "
        "tally:"
    ),
]

_BEADSTRING_SUBPLOTS = _BEADSTRING_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "and submitted the form. The REPL spliced or counted as the "
        "form said:"
    ),
]

_CIRCUIT_SUBPLOTS = _CIRCUIT_SUBPLOTS + [
    _story(
        "To {goal_text}, {tortoise_he_she} {emo_patient} composed {concept_phrase} "
        "and submitted the form. The REPL looped without growing the "
        "trail:"
    ),
]
