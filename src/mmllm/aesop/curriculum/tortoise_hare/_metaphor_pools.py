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
REPL. {hare_phrase}, {emo_proud}, had already forgotten what was
in the pouch — but the form, which still carried it, came back
with the answer."""),

    # 2. Pouch overrides the road-sign for the duration the pouch
    #    is worn. (Shadowing.)
    SubplotTemplate("""\
"There's a sign by the road that names one thing," {tortoise_phrase}
said, patting the pouch at {tortoise_his_her} hip, "but inside
this pouch I carry another. While I wear the pouch, the pouch
wins." {tortoise} described how to {goal_text} — the pouch's
binding overruling the road-sign's, but only for the pouch's
stretch of road. {tortoise_he_she_cap} composed {concept_phrase},
submitted it, and let the REPL show whose binding was in force
when the form ran."""),

    # 3. Hare ignores the pouch; Tortoise's pouch-walk wins.
    SubplotTemplate("""\
{hare_phrase} brushed past the road-sign {place}, {emo_proud},
calling out guesses without bothering to peek into
{tortoise_phrase}'s pouch. But the pouch was where the answer
lived: {tortoise_he_she_cap} intended to {goal_text}, and the
value was tucked away for exactly that stretch. {tortoise} wrote
out {concept_phrase}, submitted it, and the REPL — looking in
the pouch as the form told it to — handed back the value
{hare} had not even thought to check."""),

    # 4. Substitution rule — wherever the form names the binding,
    #    the runtime reaches into the pouch.
    SubplotTemplate("""\
"Wherever the form names the binding," {tortoise_phrase} explained,
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
the binding is yours." To {goal_text}, {tortoise_he_she_cap}
composed {concept_phrase} with the binding tucked safely inside,
then submitted the form. The REPL returned the value, and the
pouch — its work done — was empty again. {hare_phrase}, {emo_tired},
finally admitted that the patient pouch-walk had carried the
day."""),
]


# ─────────────────────── paw-step-recipe (fn) ─────────────────────────


_RECIPE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. Posted recipe-card on the road. (defn / named fn.)
    SubplotTemplate("""\
{tortoise_phrase} kept a small stack of recipe-cards by the road,
each one a paw-step routine for some animal of the meadow to
follow. "Today we add another," {tortoise_he_she} said: "to
{goal_text}, the steps go like this." {tortoise_he_she_cap}
wrote out {concept_phrase} on a fresh card, gave the recipe its
name, and submitted the form so the REPL could remember it.
{hare_phrase}, {emo_proud}, said {hare_he_she} would never bother
with cards — but the next runner along the road would pick the
card up and follow it exactly."""),

    # 2. Unnamed recipe used once. (Anonymous fn.)
    SubplotTemplate("""\
"This is a recipe we want only once," {tortoise_phrase} said,
declining to give the routine a card. To {goal_text},
{tortoise_he_she} composed the paw-steps inline — the procedure
unnamed, the ingredients listed in brackets at the head.
{tortoise} described {concept_phrase} as {tortoise_he_she} wrote
it out, then submitted the form. The REPL followed the unnamed
recipe through to its last step and handed back the value, after
which the recipe was gone — exactly as {tortoise} had
intended."""),

    # 3. Last step is what you serve. (Body returns last form.)
    SubplotTemplate("""\
"In any recipe," {tortoise_phrase} explained, "the last step is
what you serve." {tortoise_he_she_cap} took the goal — to
{goal_text} — and wrote the routine's paw-steps in order, knowing
that whatever the final line evaluated to was what the runner
would carry back. {tortoise} composed {concept_phrase}, submitted
the form, and the REPL — discarding the earlier steps' values —
handed back only the dish from the last."""),

    # 4. Two cards in a row; output of one feeds the next. (comp /
    #    threading / pipeline.)
    SubplotTemplate("""\
{tortoise_phrase} laid two recipe-cards in a row {place}, the
second following the first. "Whatever the first recipe serves,"
{tortoise_he_she} said, "the second takes as its ingredient.
Together they make a single combined recipe." To {goal_text},
{tortoise_he_she_cap} composed the chain — {concept_phrase} —
and submitted the form. The REPL walked the chain end to end,
and the value that emerged from the final card was the answer.
{hare_phrase}, {emo_tired}, conceded that even {hare_he_she}
could see the order was the lesson."""),

    # 5. Half-loaded recipe waits for the last ingredient.
    #    (partial / apply.)
    SubplotTemplate("""\
"Here's a recipe with one ingredient already added,"
{tortoise_phrase} said, holding up a card half-loaded. "When the
next animal calls it, they only have to bring the rest." To
{goal_text}, {tortoise_he_she} composed {concept_phrase} that way
— some arguments fixed in advance, the others to be supplied at
the call site. {tortoise_phrase} submitted the form, and the REPL
filled in what was missing and ran the recipe through to its
end."""),
]


# ─────────────────────── basket-and-label (collections) ───────────────


_BASKET_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The basket-on-the-path template — generic; whatever the
    #    operation, the basket stays as it was, the form returns
    #    the new arrangement.
    SubplotTemplate("""\
{tortoise_phrase} pointed to a small basket on the path {place}.
"Whatever I want to do with what's inside," {tortoise_he_she}
said, "I read from the basket, work the change, and the basket
itself stays as it was — what I get back is a fresh arrangement."
To {goal_text}, {tortoise_he_she_cap} composed {concept_phrase},
submitted the form, and let the REPL handle the basket exactly
as the operation prescribed."""),

    # 2. The labels-and-positions template — works for tagged pouches
    #    (maps), positional rows (vectors), or kind-only baskets
    #    (sets). The narrative is generic; goal_text says which.
    SubplotTemplate("""\
"You can find what you want in a basket several ways,"
{tortoise_phrase} said, gesturing at the woven shape:
"by the tag pinned to it, by its place in line, or by simply
asking whether it's there at all." To {goal_text},
{tortoise_he_she_cap} wrote {concept_phrase} for the basket,
submitted the form, and the REPL applied the lookup or update
exactly as the form directed."""),

    # 3. The procession template — for ordered collections
    #    (vectors, lists, seqs). Sub-template is more
    #    list/vector-leaning but doesn't claim a specific type.
    SubplotTemplate("""\
A line of animals had formed {place}, each one taking the next
animal's tail in its paw — head at the front, the rest trailing
behind. "Many of our baskets are like this procession,"
{tortoise_phrase} said. "You can grab the head, you can ask for
the tail, you can put a new animal at the front of the line."
To {goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form, and the REPL marched the procession exactly
as the form described."""),

    # 4. The new-basket-from-old template — immutability emphasis;
    #    works for any collection type.
    SubplotTemplate("""\
"Watch carefully," {tortoise_phrase} said, holding up the
original basket. "Whatever I do to it, this one sits unchanged
on the path — what I get back is a fresh basket with the change
made, leaving the first one exactly where it was." To
{goal_text}, {tortoise_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL returned a new arrangement
while the original waited, untouched. {hare_phrase}, {emo_tired},
was beginning to see why nothing could be lost by trying."""),

    # 5. The Hare-rummages-loudly template — Hare guesses by
    #    rummaging; Tortoise's careful basket-work wins. Generic
    #    fable beat that fits any collection operation.
    SubplotTemplate("""\
{hare_phrase} began rummaging in the basket, {emo_proud}, calling
out guesses about its contents without quite checking. "I know
exactly what's in there," {hare_he_she} insisted. {tortoise_phrase}
shook {tortoise_his_her} head. To {goal_text} properly,
{tortoise_he_she} wrote {concept_phrase} carefully on a slate,
submitted the form, and the REPL — looking into the basket the
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
it. "Atoms are like this notebook," {tortoise_phrase} said. "You
can deref to read; you can swap! to write atomically, no matter
who else is watching." To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form, and let the REPL work the
notebook exactly as the form prescribed."""),

    # 2. Atomic swap — read, apply, write, all in one motion.
    SubplotTemplate("""\
"When I want to update the notebook," {tortoise_phrase} said,
"I don't pick it up and walk away — I read the page, apply the
change, and write it back, all in a single motion. If two
animals arrive at once, the runtime makes sure only one of us
goes through at a time." To {goal_text}, {tortoise_he_she_cap}
composed {concept_phrase} for the notebook, submitted the form,
and the REPL applied the update atomically."""),

    # 3. A bell pinned to the notebook; a watcher logs each change.
    SubplotTemplate("""\
{tortoise_phrase} pinned a small bell to the corner of the
notebook. "Now," {tortoise_he_she} said, "anyone who updates the
page rings the bell, and a listener can keep a record of every
change." To {goal_text}, {tortoise_he_she_cap} composed
{concept_phrase} — listener and all — submitted the form, and
the REPL kept a record of each update, the bell ringing each
time the page turned."""),

    # 4. Only-if-still-says — CAS / compare-and-set!.
    SubplotTemplate("""\
"Sometimes I want to update the notebook only if it still says
what I last saw," {tortoise_phrase} explained. "If another animal
got there first, I'd rather not overwrite their work." To
{goal_text}, {tortoise_he_she_cap} composed {concept_phrase} that
way — the update conditional on the old value — submitted the
form, and the REPL applied the change only if the conditions
held."""),

    # 5. Several notebooks, all-or-none. (Refs / dosync / alter.)
    SubplotTemplate("""\
{tortoise_phrase} gathered several notebooks together on the
stump — one for each runner in the race. "When I update them, I
want all the changes to land together, or none at all,"
{tortoise_he_she} said. "That's a transaction." To {goal_text},
{tortoise_he_she_cap} composed {concept_phrase} inside a
coordinated block, submitted the form, and the REPL — committing
only when every notebook's change was ready — applied them as
one."""),
]


# ─────────────────────── sieve-and-pour (map/filter/transduce) ────────


_SIEVE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The general sieve — works for transform (map),
    #    select (filter), select-counted (take/drop), or dedupe
    #    (distinct). The rule attached at the sieve's mouth
    #    decides what happens to each pebble.
    SubplotTemplate("""\
{tortoise_phrase} held up a sieve {place} — a paw-step rule
attached at its mouth. "Whatever rule we hang on the sieve,"
{tortoise_he_she} said, "the basket's pebbles pass through one
at a time: some are changed, some kept, some dropped, depending
on the rule." To {goal_text}, {tortoise_he_she_cap} composed
{concept_phrase} as the sieve's rule, poured the basket through,
submitted the form, and the REPL returned what the sieve had
let through."""),

    # 2. The pour-through-and-collect template — generic emphasis
    #    on the new-basket-out-the-other-side metaphor.
    SubplotTemplate("""\
{tortoise_phrase} balanced a sieve over an empty basket. "The
pebbles go in at the top," {tortoise_he_she} said, "and the
sieve does its work — applying the rule, choosing or changing —
and what lands in the basket below is the result." To
{goal_text}, {tortoise_he_she_cap} composed {concept_phrase},
poured the input through, submitted the form, and the REPL
collected what fell into the receiving basket."""),

    # 3. Stacked sieves — output of one feeds the next.
    #    (comp xform.)
    SubplotTemplate("""\
{tortoise_phrase} stacked two sieves one above the other, the
output of the first feeding into the second. "What lands at the
bottom," {tortoise_he_she} said, "has been through both rules in
order — applied as a single combined sieve." To {goal_text},
{tortoise_he_she_cap} composed {concept_phrase} as a stack of
sieves, poured the input through, submitted the form, and the
REPL caught what the stack let through."""),

    # 4. The receiver template — pour into any kind of basket.
    #    (into / into with xform.)
    SubplotTemplate("""\
"You can pour the result into any kind of basket you like,"
{tortoise_phrase} said. "A row of pebbles, a unique-only
basket, a bag of any shape — the sieve doesn't care; the
receiver does." To {goal_text}, {tortoise_he_she_cap} composed
{concept_phrase}, chose the right empty receiver, poured
through the sieve, submitted the form, and the REPL packed the
result into the basket of {tortoise_his_her} choosing."""),

    # 5. The Hare-tries-to-shortcut-the-sieve template — Hare
    #    guesses, Tortoise pours through carefully. Generic
    #    fable beat applicable to any sieve operation.
    SubplotTemplate("""\
{hare_phrase} eyed the basket, {emo_proud}, and called out a
guess about what would come out the other side of the sieve
without bothering to actually pour. {tortoise_phrase} shook
{tortoise_his_her} head and went on with the work: to
{goal_text}, {tortoise_he_she} composed {concept_phrase} as
the sieve's rule, poured the input through carefully,
submitted the form, and the REPL returned the only answer
that would do — the one the sieve had actually produced."""),
]


# ─────────────────────── acorn-arithmetic (numbers) ───────────────────


_ACORN_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The counting-acorns template — generic arithmetic frame.
    SubplotTemplate("""\
{tortoise_phrase} laid acorns out on a flat stone {place}, sorting
them into small heaps. "Numbers in Clojure are just like acorns in
heaps," {tortoise_he_she} said: "you can count them, you can add
two heaps together, you can divide one heap among several." To
{goal_text}, {tortoise_he_she_cap} composed {concept_phrase},
submitted the form, and let the REPL hand back the count of
whatever the operation had produced."""),

    # 2. The basket-grows-or-shrinks template — for inc/dec, +/-.
    SubplotTemplate("""\
"Watch the basket," {tortoise_phrase} said, gesturing at a small
heap of acorns. "Every operation either adds, takes away, or
combines what's already there — the heap grows or shrinks by
exactly what you say." To {goal_text}, {tortoise_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL
returned the new count, the heap settled into its new
arrangement."""),

    # 3. The dividing-heaps template — quot/rem/mod, division.
    SubplotTemplate("""\
{tortoise_phrase} divided a pile of acorns into smaller equal heaps
{place}, careful to count the leftovers. "Dividing in Clojure works
the same way," {tortoise_he_she} said. "You can ask for the count
of full heaps, the leftover, or the heap-sized remainder." To
{goal_text}, {tortoise_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL handed back the right number from
the division."""),

    # 4. The Hare-counts-aloud template — Hare guesses by sight,
    #    Tortoise counts.
    SubplotTemplate("""\
{hare_phrase} eyed the heap, {emo_proud}, and called out a guess
about how many acorns were there without bothering to count.
{tortoise_phrase} simply began counting — to {goal_text} required
no eyeballing, only the form. {tortoise_he_she_cap} composed
{concept_phrase}, submitted it to the REPL, and the runtime
returned the number that had been there all along, settling the
matter the patient way."""),

    # 5. The growing-pile template — bigint promotion / large
    #    multiplications.
    SubplotTemplate("""\
{tortoise_phrase} pointed at a basket whose acorns had spilled into
a second basket — the heap had grown beyond the first basket's
edge. "When numbers grow large," {tortoise_he_she} said, "Clojure
quietly uses a bigger basket; nothing is lost." To {goal_text},
{tortoise_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL returned the value, large or small, exactly as
the heap had become."""),
]


# ─────────────────────── gates-on-the-trail (boolean logic) ───────────


_GATE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The chain-of-gates template — and / or short-circuit.
    SubplotTemplate("""\
A chain of small wooden gates stood across the trail {place}, each
swinging open or closed by the value the runner brought to it.
"Clojure's `and` is a chain of gates," {tortoise_phrase} said.
"The first closed gate stops the chain; the value at that gate is
what comes back. If they're all open, the last value passes
through." To {goal_text}, {tortoise_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL returned
whatever the gates had actually let through."""),

    # 2. The opposite-gate template — `not`.
    SubplotTemplate("""\
{tortoise_phrase} pointed at a small gate that swung the *other*
way. "This one flips: if the runner is carrying a true, the gate
returns false; if false, the gate returns true. nil and false alike
are flipped to true." To {goal_text}, {tortoise_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL
returned the flipped value, exactly as the opposite-gate
demanded."""),

    # 3. The truthy-falsey template — falsey rules, truthy 0 / "".
    SubplotTemplate("""\
"Listen carefully," {tortoise_phrase} said {place}. "Only two
things in Clojure close the gate: nil and false. Everything
else — zero, the empty string, an empty list — opens it. You
can't tell what's inside by guessing; you ask the gate." To
{goal_text}, {tortoise_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL returned the value the gate
had passed through."""),

    # 4. The Hare-bumps-the-gate template — Hare guesses gate
    #    state, Tortoise tests.
    SubplotTemplate("""\
{hare_phrase} sprinted toward the gate {place}, {emo_proud},
certain it would swing open for {hare_him_her}. {tortoise_phrase}
slowed and watched: the only way to know which way the gate
would swing was to actually carry the value to it. To
{goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form, and the REPL settled the matter — the gate
had swung exactly as the rules said, regardless of {hare_phrase}'s
guess."""),

    # 5. The chained-rules template — multi-arg comparisons /
    #    equality across many.
    SubplotTemplate("""\
A line of gates stood end to end {place}, each one checking the
runner against the next. "If every gate agrees, the runner passes
through; if any disagree, the chain stops at that gate." To
{goal_text}, {tortoise_phrase} composed {concept_phrase},
submitted the form, and the REPL returned what every gate together
had decided."""),
]


# ─────────────────────── fork-in-the-path (if/cond/case/when) ─────────


_FORK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The two-armed fork template — `if`.
    SubplotTemplate("""\
The trail forked {place}, one arm bending left, the other right.
"In Clojure, if is the simplest fork," {tortoise_phrase} said.
"The condition decides which arm the runner takes; whichever arm
runs, that arm's value is what comes back." To {goal_text},
{tortoise_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — having taken exactly one arm — handed back
its value."""),

    # 2. The crossroads template — applies to `cond` / `case` /
    #    multi-arm branching. Type-neutral framing: "the runner
    #    walks past stones" works for if (one stone), cond/case
    #    (many stones), case (matching tokens).
    SubplotTemplate("""\
The trail {place} opened into a crossroads, each arm marked by a
small condition-stone. "Branching forms work like this,"
{tortoise_phrase} said: "the runner walks past the stones in
order, takes the first arm whose stone says true, and the value
of that arm is what comes back." To {goal_text},
{tortoise_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL took the right arm and returned its
value."""),

    # 3. The catchall arm template — `:else` / default.
    SubplotTemplate("""\
"What if no condition-stone says true?" {tortoise_phrase} asked.
"There must be a catchall arm — the path the runner takes when
nothing else matched." To {goal_text}, {tortoise_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL —
following the catchall when needed — returned the right value
either way."""),

    # 4. The one-armed fork template — `when`.
    SubplotTemplate("""\
"Sometimes you only care about one arm," {tortoise_phrase} said.
"When the condition is true, take the arm; when false, the runner
just stops where the fork was — no value, only nil." To
{goal_text}, {tortoise_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL returned whatever the one-armed
fork had decided."""),

    # 5. The matching-token template — `case`.
    SubplotTemplate("""\
A flat stone with several tokens carved into it lay {place}.
"Case is a matching-stone," {tortoise_phrase} said. "The runner
shows {tortoise_his_her} token; the stone routes them to the
matching arm. No token, no match — unless a default is set."
To {goal_text}, {tortoise_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — matching by token — handed back
the right value."""),
]


# ─────────────────────── road-sign (def / namespace) ──────────────────


_ROADSIGN_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The posted-sign-on-the-road template — `def`.
    SubplotTemplate("""\
{tortoise_phrase} drove a small wooden post {place} and nailed a
fresh sign to it. "A def is a sign by the road," {tortoise_he_she}
said. "Anyone passing reads the name, learns the value, and can
refer to it later by name alone." To {goal_text},
{tortoise_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL planted the sign — the name now bound to its
value for any later runner along the road."""),

    # 2. The painted-over-sign template — redefinition.
    SubplotTemplate("""\
"You can paint over an old sign with new paint,"
{tortoise_phrase} said, holding up a brush. "The post stays where
it is; the name is the same; only the value changes. The next
runner reads the new value and never sees the old." To
{goal_text}, {tortoise_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — having painted over the sign —
returned what the new paint now said."""),

    # 3. The library-of-scrolls template — namespaces.
    SubplotTemplate("""\
A small wooden library stood {place}, its shelves stocked with
scrolls — each scroll a namespace, each scroll's signs labeled
with its name. "To borrow a scroll," {tortoise_phrase} said,
"you require it; to use a sign on it directly, you can refer or
fully qualify the name." To {goal_text}, {tortoise_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL
fetched from the library exactly as the form directed."""),

    # 4. The shop-window template — public vs private.
    SubplotTemplate("""\
{tortoise_phrase} pointed to the shop window in front of the
scroll-library. "The signs in the window are public — anyone may
read them. The signs in the back room are private; only those
inside the scroll see them." To {goal_text}, {tortoise_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL —
respecting which signs were public and which were not — handed
back what the rules permitted."""),

    # 5. The Hare-misreads-the-sign template — Hare guesses,
    #    Tortoise reads carefully.
    SubplotTemplate("""\
{hare_phrase}, {emo_proud}, glanced at the sign {place} and
called out what {hare_he_she} thought it said without slowing.
{tortoise_phrase} stopped and read carefully. To {goal_text}, the
sign had to be read exactly: {tortoise_he_she} composed
{concept_phrase}, submitted the form, and the REPL — reading
literally — returned the right value, while {hare}'s guess fell
short."""),
]


# ─────────────────────── safety-net (errors / REPL safety) ────────────


_SAFETYNET_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The net-under-the-leap template — `try`/`catch`.
    SubplotTemplate("""\
{tortoise_phrase} stretched a small net beneath a high jump
{place}. "If the runner falls, the net catches them; the run
doesn't end, only the path bends." To {goal_text},
{tortoise_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — net in place — caught the trouble and
returned the value the catch-arm had specified, the run continuing
the patient way."""),

    # 2. The practice-meadow template — REPL safety; nil punning.
    SubplotTemplate("""\
"This is the practice meadow," {tortoise_phrase} said {place},
gesturing wide. "A stumble here costs nothing. Type a form, see
what comes back, fix it, try again. The REPL is forgiving in a
way that a real race is not." To {goal_text}, {tortoise_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL
returned the value — even if the form had been close to a
mis-step."""),

    # 3. The alarm-with-detail template — `throw` / `ex-info`.
    SubplotTemplate("""\
{tortoise_phrase} pointed at a small horn hung by the trailside.
"When something goes wrong, you blow the horn — and you can attach
a slip of paper to the horn-blast saying what went wrong, with
detail enough to inspect." To {goal_text}, {tortoise_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL —
horn sounded, slip attached — handed back the value the alarm
chain had decided."""),

    # 4. The fitness-check template — pre/post conditions, assert.
    SubplotTemplate("""\
"Before a real race," {tortoise_phrase} said, "we check the
runner's fitness: are they ready to run? Are they carrying what
they should be? Pre and post conditions are exactly that — checks
that hold up the run if the runner isn't ready." To {goal_text},
{tortoise_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — fitness checked — returned the value when the
checks held, or sounded the alarm when they didn't."""),

    # 5. The Hare-tries-the-jump template — Hare ignores the net,
    #    Tortoise demonstrates the safety design.
    SubplotTemplate("""\
{hare_phrase} eyed the high jump {place}, {emo_proud}, certain
{hare_he_she} could clear it without a net. {tortoise_phrase}
shook {tortoise_his_her} head and stretched the net carefully. To
{goal_text} required no daring, only the net: {tortoise_he_she}
composed {concept_phrase}, submitted the form, and the REPL —
catching anything that fell — returned the answer the safety
design had earned."""),
]


# ─────────────────────── scroll-and-quill (IO / metadata) ─────────────


_SCROLL_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The scroll-on-the-table template — reading and writing.
    SubplotTemplate("""\
{tortoise_phrase} unrolled a long scroll {place}, dipping a quill
into ink at the edge. "The world outside the REPL is scrolls,"
{tortoise_he_she} said: "you read what they say, you write what
you want to keep, and the runtime carries the words back and
forth." To {goal_text}, {tortoise_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL handed back
what the scroll had said, or what the writing had committed."""),

    # 2. The scroll-line-by-line template — `line-seq`, reading
    #    streams.
    SubplotTemplate("""\
"You don't have to read a scroll all at once," {tortoise_phrase}
said, finger tracing the parchment. "You can take it line by line,
considering each one before moving on. The runtime gives you a
sequence of lines you can walk through." To {goal_text},
{tortoise_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL handed back the lines exactly as the scroll had
arranged them."""),

    # 3. The marginalia template — metadata, `meta`, doc.
    SubplotTemplate("""\
Down the side of the scroll, {tortoise_phrase} pointed to small
notes in the margin. "Marginalia: notes about the scroll's
contents, not the contents themselves. Clojure metadata works the
same way — a small map of facts attached to a value, readable
when you ask for it." To {goal_text}, {tortoise_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL —
peeking at the margins — handed back what the notes had said."""),

    # 4. The open-the-scroll template — `with-open`, resource
    #    cleanup.
    SubplotTemplate("""\
"When you unroll the scroll," {tortoise_phrase} said, "you must
remember to roll it up after — leaving it spread on the path
invites trouble." To {goal_text}, {tortoise_he_she_cap} composed
{concept_phrase} so the scroll would be opened, used, and rolled
up regardless of what happened inside, submitted the form, and the
REPL completed the work cleanly."""),

    # 5. The voice-of-the-meadow template — `*in*`, `*out*`,
    #    `prn`, `pprint`.
    SubplotTemplate("""\
"Some words are spoken aloud across the meadow,"
{tortoise_phrase} said, "and some are quietly noted. The runtime
keeps both — a loud voice for announcements and a quiet one for
records — and you can ask it to use either." To {goal_text},
{tortoise_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — speaking and recording as the form
specified — returned the value the work had produced."""),
]


# ─────────────────────── guild-of-runners (protocols) ─────────────────


_GUILD_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The founding-the-guild template — `defprotocol`.
    SubplotTemplate("""\
{tortoise_phrase} carved a small wooden sign {place}: "Runners'
Guild — any species may join." "A protocol is a guild,"
{tortoise_he_she} said. "It lists what every member must be able
to do — the methods. Any animal that can sign the book may claim
membership." To {goal_text}, {tortoise_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — guild
founded — handed back the guild's record."""),

    # 2. The signing-the-book template — `extend-protocol`.
    SubplotTemplate("""\
"Today another animal signs the book," {tortoise_phrase} said,
holding the guild ledger. "By signing, the species swears that any
of its members can perform the guild's methods — the same call,
species-specific behavior." To {goal_text}, {tortoise_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL —
finding the new signature in the book — dispatched correctly to
the new species' implementation."""),

    # 3. The same-call-different-paws template — protocol method
    #    dispatch.
    SubplotTemplate("""\
"Watch what happens when the call goes out," {tortoise_phrase}
said. "The guild call is the same: 'speed!' But each species
answers in its own way — the hare bounds, the tortoise plods,
the bird flits. Same call, different paws." To {goal_text},
{tortoise_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — dispatching to the right species — returned
the species-specific answer."""),

    # 4. The two-guilds-don't-merge template — protocols don't
    #    inherit.
    SubplotTemplate("""\
"Joining one guild doesn't auto-join another," {tortoise_phrase}
said firmly. "If the species belongs to the Movers' guild, that
doesn't mean they're in the Singers' guild. Each guild is signed
separately." To {goal_text}, {tortoise_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — checking
both guild books independently — returned the right answer for
each."""),

    # 5. The Hare-claims-membership template — Hare boasts about
    #    a guild he hasn't joined.
    SubplotTemplate("""\
{hare_phrase}, {emo_proud}, declared that {hare_he_she} could of
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
{tortoise_phrase} reached into a different toolshed {place} and
pulled out a tool {tortoise_he_she} hadn't carved {tortoise_him_her}self
— a tool from the host platform. "This isn't ours," {tortoise_he_she}
said, "but we can call its methods directly: dot-prefix on the
instance, or slash for static." To {goal_text}, {tortoise_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL —
calling into the foreign tool — handed back what its method had
returned."""),

    # 2. The labeled-toolshed template — generic; works for both
    #    instance methods (held by an animal) and static methods
    #    (standard-issue, called by toolshed-name). The
    #    {goal_text}/{concept_phrase} say which.
    SubplotTemplate("""\
"Each tool in the foreign toolshed has its own label,"
{tortoise_phrase} said, "and the right way to call it depends on
which kind of tool it is — some held by an animal, some
standard-issue called by the toolshed's name." To {goal_text},
{tortoise_he_she_cap} composed {concept_phrase} using the right
calling convention, submitted the form, and the REPL — invoking
the host tool by its label — returned the value the host had
computed."""),

    # 3. The constructor template — `new` / `(.Class.)`.
    SubplotTemplate("""\
"Some tools you have to build first," {tortoise_phrase} said,
holding up an empty case. "You give the toolshed the raw
materials, and it hands back a freshly built tool." To
{goal_text}, {tortoise_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — constructing the host object
from the inputs — handed back the new tool ready to use."""),

    # 4. The type-hint template — type hints, primitive arrays.
    SubplotTemplate("""\
"Sometimes the toolshed needs to know what kind of tool you mean,"
{tortoise_phrase} said, marking a small tag onto the form.
"Type-hints save the runtime from having to guess; the host can
go straight to the right method." To {goal_text},
{tortoise_he_she_cap} composed {concept_phrase} with the right
hint, submitted the form, and the REPL — taking the host's
fast path — returned the value cleanly."""),

    # 5. The Hare-grabs-the-wrong-tool template — Hare guesses,
    #    Tortoise checks the toolshed.
    SubplotTemplate("""\
{hare_phrase}, {emo_proud}, grabbed at the foreign toolshed
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
{tortoise_phrase} sat at a small writing desk {place}, quill in
paw. "A macro," {tortoise_he_she} said, "is a rule that rewrites
the recipe before the runtime ever cooks it. You write the rule
once, and any recipe that uses it gets rewritten on the way to
the kitchen." To {goal_text}, {tortoise_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — first
rewriting, then evaluating — returned the value the rewritten
recipe yielded."""),

    # 2. The before-and-after template — `macroexpand`.
    SubplotTemplate("""\
"Want to see what the rule rewrites the recipe into?"
{tortoise_phrase} asked, holding up a slate split in half.
"Macroexpand shows you the before and the after — the original
form on one side, the rewritten form on the other." To
{goal_text}, {tortoise_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL handed back the rewriting itself
or the value, depending on what was asked."""),

    # 3. The scratch-name template — gensym / hygiene.
    SubplotTemplate("""\
"When the rule introduces a name of its own," {tortoise_phrase}
said, "you don't want it to collide with names the runner is
using. So we use a one-off scratch-name — gensym — guaranteed
unique." To {goal_text}, {tortoise_he_she_cap} composed
{concept_phrase} with the scratch-name woven in, submitted the
form, and the REPL — running the hygienic rewrite — returned the
value cleanly."""),

    # 4. The function-suffices template — when not to write a macro.
    SubplotTemplate("""\
"Most of the time, you don't need a rule that rewrites,"
{tortoise_phrase} said. "A function suffices: it takes its
arguments, runs its body, returns its value. Macros are for when
you need to shape the *form* itself — not the value." To
{goal_text}, {tortoise_he_she_cap} composed {concept_phrase} —
choosing macro or function as the goal demanded — submitted the
form, and the REPL returned the value either way."""),

    # 5. The Hare-tries-to-skip-the-rule template.
    SubplotTemplate("""\
{hare_phrase}, {emo_proud}, insisted that the rule was unnecessary
— {hare_he_she} could write the rewritten recipe directly.
{tortoise_phrase} only smiled: a hand-rewritten recipe is fine
once, but the rule pays off when many recipes need rewriting the
same way. To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form, and the REPL — running the
rule the rule's way — returned the value the rewritten recipe
yielded."""),
]


# ─────────────────────── scribe-shorthand (read-time conventions) ─────


_SCRIBE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The marginalia-skipped-by-the-reader template — comments.
    SubplotTemplate("""\
{tortoise_phrase} pointed at a small note jotted along the side of
the scroll. "When the reader reaches a comment, the eye moves
past it — the runtime never sees it at all." To {goal_text},
{tortoise_he_she_cap} composed {concept_phrase} with the
side-notes ignored exactly as the runtime ignores them, submitted
the form, and the REPL returned the value the form alone
produced."""),

    # 2. The breath-doesn't-matter template — whitespace.
    SubplotTemplate("""\
"The pause between words doesn't change the meaning,"
{tortoise_phrase} said. "Two spaces, ten spaces, a line break — the
reader only cares which words are which, not how far apart you
wrote them." To {goal_text}, {tortoise_he_she_cap} composed
{concept_phrase} however the writing fell on the page, submitted
the form, and the REPL — reading by tokens, not by space —
returned the same value either way."""),

    # 3. The fence-posts template — parens group, they don't
    #    multiply.
    SubplotTemplate("""\
"Parentheses are fence-posts," {tortoise_phrase} said, drawing two
in the dust around a small group. "They mark which things go
together as a single call. They don't multiply, they don't add —
they only group." To {goal_text}, {tortoise_he_she_cap} composed
{concept_phrase} with the right groups marked, submitted the form,
and the REPL — reading the groups as the form had marked them —
returned the value cleanly."""),

    # 4. The single-breath-do template — `do` form.
    SubplotTemplate("""\
"Sometimes you want several things to happen in one breath,"
{tortoise_phrase} said, "but only the last one's value matters.
That's what do is for: a sequence in one breath, the final value
returned." To {goal_text}, {tortoise_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — running each
step in order, keeping only the last value — returned the
answer."""),

    # 5. The reader-shorthand template — reader macros, tagged
    #    literals.
    SubplotTemplate("""\
"Some shapes the reader expands automatically before the runtime
ever sees them," {tortoise_phrase} said. "The apostrophe before a
list, the at-sign before a deref, the hash-tag before a literal —
these are the scribe's shorthand for longer forms." To
{goal_text}, {tortoise_he_she_cap} composed {concept_phrase} using
whatever shorthand the goal required, submitted the form, and the
REPL — expanding shorthands, then evaluating — returned the
value."""),
]


# ─────────────────────── chalk-marks-vs-acorns (quote / symbols) ──────


_CHALKMARK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The mark-on-the-bark template — symbols vs values.
    SubplotTemplate("""\
{tortoise_phrase} pointed at a name scratched into the bark
{place}, then at an actual acorn lying on the path. "The mark on
the bark is the *name*; the acorn is the *value*. They are not
the same thing — and Clojure lets you talk about either one."
To {goal_text}, {tortoise_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — keeping the name and the
value distinct — returned the right answer."""),

    # 2. The label-the-list template — `quote` / `'`.
    SubplotTemplate("""\
"To talk about the form itself rather than evaluating it,"
{tortoise_phrase} said, "you label the form with a chalk mark
in front. Quoting tells the runtime: don't cook this, just hand
it back as the shape it is." To {goal_text}, {tortoise_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL —
respecting the chalk mark — returned the form unevaluated."""),

    # 3. The labeled-template template — syntax-quote with
    #    placeholders.
    SubplotTemplate("""\
"Sometimes you want a labeled form with blanks to fill in,"
{tortoise_phrase} said. "Syntax-quote labels everything, but
unquote drills holes where values should be filled in. Together
they let you build forms with placeholders." To {goal_text},
{tortoise_he_she_cap} composed {concept_phrase} with the
placeholders threaded in, submitted the form, and the REPL —
filling in the blanks — returned the assembled form."""),

    # 4. The Hare-confuses-name-with-value template.
    SubplotTemplate("""\
{hare_phrase}, {emo_proud}, mistook the name on the bark for the
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
{tortoise_phrase} dispatched a young messenger down the long road
{place}, work in paw. "The runner goes ahead while we keep on
with our own business," {tortoise_he_she} said, "and when we
need the result we ask the runner to hand it back." To
{goal_text}, {tortoise_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — sending the runner, fetching
the result later — returned the value when it was ready."""),

    # 2. The send-message-to-runner template — `send`,
    #    `send-off`.
    SubplotTemplate("""\
"You can send a message ahead to the runner," {tortoise_phrase}
said, "and the runner applies it to whatever they're carrying.
The message reaches them; their carry is updated." To
{goal_text}, {tortoise_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — delivering the message,
updating the runner's carry — returned what the runner now
held."""),

    # 3. The await-the-runner template — `await`.
    SubplotTemplate("""\
"Sometimes we have to wait for the runner to finish what we sent
ahead," {tortoise_phrase} said. "Await holds the call until every
message has been processed; then we can read the carry safely."
To {goal_text}, {tortoise_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — waiting until the messages
landed — returned the runner's settled carry."""),

    # 4. The sealed-scroll template — `promise` / `deliver`.
    SubplotTemplate("""\
{tortoise_phrase} held up a sealed scroll. "A promise is a scroll
sealed shut: you can hand it to the next runner, and when someone
delivers a value into it, anyone who was waiting on it can
unseal." To {goal_text}, {tortoise_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — sealing,
delivering, unsealing — returned the value the promise had
carried."""),

    # 5. The Hare-doesn't-wait template — Hare reads before
    #    runner returns.
    SubplotTemplate("""\
{hare_phrase}, {emo_proud}, reached for the runner's pouch before
the runner had even returned. {tortoise_phrase} held {hare_him_her}
back: a runner sent ahead must be allowed to finish. To
{goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form, and the REPL — waiting for the runner the
patient way — returned the value when the runner had actually
delivered it."""),
]


# ─────────────────────── sorting-table (multimethods) ─────────────────


_SORTINGTABLE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The sorting-table template — `defmulti`.
    SubplotTemplate("""\
A long wooden table stood {place}, with several arms branching off
its sides. "Defmulti is a sorting-table," {tortoise_phrase} said.
"You decide what stamp on the runner to look at; the table routes
each runner down the matching arm." To {goal_text},
{tortoise_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — reading the runner's stamp, picking the
arm — returned the value the right arm had produced."""),

    # 2. The branch-of-the-table template — `defmethod`.
    SubplotTemplate("""\
"To add a branch to the sorting-table," {tortoise_phrase} said,
"you say what stamp the branch handles and what behavior runs
when a runner with that stamp arrives." To {goal_text},
{tortoise_he_she_cap} composed {concept_phrase} for the right
branch, submitted the form, and the REPL — adding the branch,
dispatching the runner — returned the branch-specific value."""),

    # 3. The hierarchy-of-stamps template — `derive` / `isa?`.
    SubplotTemplate("""\
"Stamps can be related to one another," {tortoise_phrase} said.
"A hare-stamp is also a runner-stamp; a runner-stamp is also an
animal-stamp. The sorting-table can route by any level — the
specific stamp first, falling back to the more general." To
{goal_text}, {tortoise_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — checking the hierarchy — found
the right branch and returned its value."""),

    # 4. The two-tables-side-by-side template — multimethod vs
    #    protocol.
    SubplotTemplate("""\
"There's the sorting-table, and there's the runners' guild,"
{tortoise_phrase} said. "Both route by what the runner is, but
the sorting-table is open to any criterion you like, while the
guild is open to any species that signs the book." To
{goal_text}, {tortoise_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — using whichever was right
for the goal — returned the value cleanly."""),

    # 5. The Hare-jumps-to-the-wrong-branch template.
    SubplotTemplate("""\
{hare_phrase}, {emo_proud}, leaped onto the sorting-table without
showing {hare_his_her} stamp. {tortoise_phrase} pointed at the
edge of the table: every runner must show the stamp the table
sorts by. To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form, and the REPL — reading the
stamp first, dispatching second — returned the value from the
correct branch."""),
]


# ─────────────────────── carrying-case (deftype/defrecord) ────────────


_CARRYINGCASE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The labeled-compartments template — defrecord.
    SubplotTemplate("""\
{tortoise_phrase} held up a small wooden case {place}, its inside
divided into labeled compartments. "Defrecord makes a case like
this," {tortoise_he_she} said: "named compartments holding
specific things; a stamp on the outside saying what kind of case
it is." To {goal_text}, {tortoise_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — constructing
the case, filling its compartments — returned the value the case
held or carried."""),

    # 2. The bare-case template — deftype.
    SubplotTemplate("""\
"A deftype is a barer case," {tortoise_phrase} said. "Compartments,
a stamp — no map-like behavior unless you ask for it. Faster, more
focused, less convenient." To {goal_text}, {tortoise_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL —
constructing the bare case as specified — returned the value
inside."""),

    # 3. The reaching-into-the-compartment template — field
    #    access.
    SubplotTemplate("""\
"To reach into a labeled compartment," {tortoise_phrase} said,
"you ask for it by name. The case knows where each compartment
is; the runtime fetches it cleanly." To {goal_text},
{tortoise_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — opening the right compartment — returned
exactly what was inside."""),
]


# ─────────────────────── the-tally-walk (reduce / count) ──────────────


_TALLYWALK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The walking-the-row template — reduce.
    SubplotTemplate("""\
{tortoise_phrase} walked the row of pebbles {place}, one paw at a
time, a small slate in hand for the running tally. "Reduce is
this walk," {tortoise_he_she} said: "at each pebble, you combine
it into the tally; at the end, the tally is your answer." To
{goal_text}, {tortoise_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — walking the row, carrying the
tally — returned the final number."""),

    # 2. The starting-tally template — reduce with init.
    SubplotTemplate("""\
"You don't have to start the tally at zero," {tortoise_phrase}
said, holding up a slate already inscribed with a number. "If you
start with a different value, the walk begins from there — the
combine-step folds each pebble in from that starting point." To
{goal_text}, {tortoise_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — starting from the given tally,
walking the row — returned the final value."""),

    # 3. The simple-count template — `count`.
    SubplotTemplate("""\
"The simplest tally-walk is just counting,"
{tortoise_phrase} said: "step along the row, add one at every
pebble, no other operation. The runtime does this for any
collection — vector, list, map, string." To {goal_text},
{tortoise_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — walking the row, counting the steps —
returned the count."""),
]


# ─────────────────────── bead-string (string ops) ─────────────────────


_BEADSTRING_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The threading-beads template — `str` concat.
    SubplotTemplate("""\
{tortoise_phrase} held up a string of small wooden beads {place}.
"Strings in Clojure are like this," {tortoise_he_she} said: "a
threaded line of characters, in order. Concat strings together,
and the threads are spliced; cut a substring out, and you get a
shorter thread." To {goal_text}, {tortoise_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — splicing or
cutting as the form said — returned the new bead-string."""),

    # 2. The counting-beads template — string length / substring.
    SubplotTemplate("""\
"To count the beads, walk the thread,"
{tortoise_phrase} said. "Want a section of beads? Cut from one
position to another and you get a smaller thread, the original
untouched." To {goal_text}, {tortoise_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — counting or
cutting — returned the answer the bead-thread had given up."""),

    # 3. The Hare-yanks-at-the-thread template.
    SubplotTemplate("""\
{hare_phrase}, {emo_proud}, yanked at the bead-thread {place}
without bothering to count. {tortoise_phrase} stopped {hare_him_her}:
strings are precise — every bead in its place, every position
counted. To {goal_text}, {tortoise_he_she} composed
{concept_phrase}, submitted the form, and the REPL — handling the
thread carefully — returned the right answer."""),
]


# ─────────────────────── circuit-around-the-meadow (recur / loop) ─────


_CIRCUIT_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The circuit-without-growing-the-trail template — recur.
    SubplotTemplate("""\
{tortoise_phrase} walked a small circle around the meadow {place},
each lap returning to the same starting point with a slightly
different tally in hand. "Recur is this circuit," {tortoise_he_she}
said: "back to the top with new bindings, no extra trail laid
down behind us." To {goal_text}, {tortoise_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — looping
without growing the call-stack — returned the final value."""),

    # 2. The base-case template — termination.
    SubplotTemplate("""\
"Every circuit has a stopping condition," {tortoise_phrase}
said. "Without one, the runner walks forever. With one, the
runner knows when the laps are done and the tally is the
answer." To {goal_text}, {tortoise_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — looping
until the base case — returned the value the final lap
produced."""),

    # 3. The Hare-doesn't-trust-the-circuit template.
    SubplotTemplate("""\
{hare_phrase}, {emo_proud}, distrusted the very idea of a
circuit: surely you'd just walk forever? {tortoise_phrase} smiled
patiently — the base case is the runner's compass. To
{goal_text}, {tortoise_he_she} composed {concept_phrase},
submitted the form, and the REPL — looping the right number of
times, then stopping — returned the value cleanly."""),
]
