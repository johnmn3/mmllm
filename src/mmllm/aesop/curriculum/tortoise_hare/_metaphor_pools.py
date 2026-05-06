"""Metaphor-bearing subplot pools for tortoise-hare.

The base `_GOAL_SUBPLOTS` (in grade_1.py) is generic Hare/Tortoise
banter that uses `{goal_text}` and `{concept_phrase}` but doesn't
illuminate any particular Clojure idiom. These pools below DO
illuminate specific idioms by carrying a fable-natural metaphor.

Five high-leverage families:

- **_POUCH_SUBPLOTS**     — temporary-pouch (let-binding, scope,
                              substitution, name-collision)
- **_RECIPE_SUBPLOTS**    — paw-step-recipe (fn / defn / comp /
                              partial / apply / juxt / threading)
- **_BASKET_SUBPLOTS**    — basket-and-label (vectors / lists / maps
                              / sets / immutability)
- **_NOTEBOOK_SUBPLOTS**  — shared-notebook-on-a-stump (atom / ref
                              / CAS / watch / dosync / locking)
- **_SIEVE_SUBPLOTS**     — sieve-and-pour (map / filter / take /
                              drop / into / transducer / comp xform)

Each pool has 5 templates so subjects in a family render with
narrative variety. All templates use `{goal_text}` and
`{concept_phrase}` (never `{form_display}`), keeping the
form-leak design intact.

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
