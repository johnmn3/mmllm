"""Metaphor-bearing subplot pools for fox-grapes.

The 22 metaphor-family pools defined here mirror the family names in
`tortoise_hare/_metaphor_pools.py` exactly. Imagery is fox-grapes-
specific: the patient fox's leather ledger, the orchard gate's twin
latches, the tasting-card pinned to a vine-post, the catching-cloth
strung between trees. See `docs/clojure-pedagogy/audits/metaphor-
imagery-fox-grapes.md` for the full mapping.

Pool sizing: 5 templates per family. All templates use `{goal_text}`
and `{concept_phrase}` (never `{form_display}`), keeping the form-leak
design intact.

Authoring rules followed (cf. SKILL-fable-curriculum-author.md):
- pronoun case at sentence start uses `_he_she_cap` etc.
- no "and" right after `{concept_phrase}` (avoids stutter)
- no "write a form to {goal_text}" verb collisions
- the metaphor is concretely named in every template — pouch /
  tasting-card / vine-tray / sieve / ledger / etc.
- {place} never sentence-start after a period (lowercase prep clash).
- at least 2 of 5 templates carry the hasty-fox / patient-fox
  dialectic (the rationalizer vs the eval-first evaluator).
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import SubplotTemplate


# ─────────────────────── temporary-pouch (let) ────────────────────────


_POUCH_SUBPLOTS: list[SubplotTemplate] = [

    # 1. Patient fox tucks the value into the berry-pouch; held only
    #    for one stretch between trellis and basket.
    SubplotTemplate("""\
{patient_fox_phrase} reached for the small berry-pouch tied at
{patient_fox_his_her} belt. "When I want to {goal_text}," {patient_fox_he_she}
said, "I tuck the value into the pouch and carry it just for the
stretch between trellis and basket where I need it. By the time I set
it down, the pouch is empty again." {patient_fox_he_she_cap} composed
{concept_phrase}, the binding tucked away inside, and submitted the form
to the REPL. {hasty_fox_phrase}, {emo_proud}, had already forgotten what
was in the pouch — but the form, which still carried it, came back with
the answer."""),

    # 2. Pouch carried for one stretch; whatever's tucked inside is in
    #    force only while the pouch is worn. Type-neutral framing of the
    #    same temporary-binding idea.
    SubplotTemplate("""\
{patient_fox_phrase} patted the pouch at {patient_fox_his_her} belt.
"Whatever I tuck in here is in force only while the pouch is worn,"
{patient_fox_he_she} said, "and only for the form that names the binding.
Step past the form's edge and the pouch is empty again." To {goal_text},
{patient_fox_he_she_cap} composed {concept_phrase} with the binding tucked
in for that stretch, submitted it, and let the REPL read out the value
the pouch had held."""),

    # 3. Hasty fox ignores the pouch; Patient fox's pouch-walk wins.
    SubplotTemplate("""\
{hasty_fox_phrase} brushed past the vine-post {place}, {emo_proud},
calling out guesses without bothering to peek into {patient_fox_phrase}'s
pouch. But the pouch was where the answer lived: {patient_fox_he_she_cap}
intended to {goal_text}, and the value was tucked away for exactly that
stretch. {patient_fox} wrote out {concept_phrase}, submitted it, and the
REPL — looking in the pouch as the form told it to — handed back the value
{hasty_fox} had not even thought to check."""),

    # 4. Substitution rule — wherever the form names the binding,
    #    the runtime reaches into the pouch.
    SubplotTemplate("""\
"Wherever the form names the binding," {patient_fox_phrase} explained,
"the runtime reaches into the pouch and pulls out what was tucked there."
{patient_fox_he_she_cap} demonstrated by intending to {goal_text}: each
mention of the bound name, {patient_fox} said, would be replaced by the
value from the pouch the moment the form ran. {patient_fox_phrase} composed
{concept_phrase}, submitted the form, and the REPL substituted as promised
— the pouch's value threaded into every place the binding had been named."""),

    # 5. End-of-stretch — the pouch is empty when the form's stretch is
    #    over. (Scope ends.)
    SubplotTemplate("""\
"Watch the pouch carefully," {patient_fox_phrase} said {place}. "While
the form's stretch of road runs, the pouch is full and the binding is
yours." To {goal_text}, {patient_fox_he_she_cap} composed {concept_phrase}
with the binding tucked safely inside, then submitted the form. The REPL
returned the value, and the pouch — its work done — was empty again.
{hasty_fox_phrase}, {emo_tired}, finally admitted that the patient pouch-walk
had carried the day."""),
]


# ─────────────────────── tasting-card (fn) ────────────────────────────


_RECIPE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. Patient fox writes a tasting-card; the routine follows it.
    #    Type-neutral — works for named, anonymous, multi-arg, etc.
    SubplotTemplate("""\
{patient_fox_phrase} kept a small stack of tasting-cards by the orchard
post, each one a paw-step routine. "Recipes in Clojure are like these
cards," {patient_fox_he_she} said: "the ingredients go at the head,
the steps in order, and the last step is what gets served." To {goal_text},
{patient_fox_he_she_cap} wrote out {concept_phrase} on a fresh card,
submitted the form, and the REPL followed the recipe and handed back the
value the last step had produced."""),

    # 2. The tasting-card as runnable routine — emphasizes the call site.
    SubplotTemplate("""\
"A recipe is only useful when it runs," {patient_fox_phrase} said,
holding up a card. "You write the steps, you bring the ingredients,
the kitchen does the rest." To {goal_text}, {patient_fox_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL — taking
the recipe and its ingredients — handed back what the steps had produced."""),

    # 3. Last step is what you serve. (Body returns last form;
    #    type-neutral and pedagogically true for all fn bodies.)
    SubplotTemplate("""\
"In any recipe," {patient_fox_phrase} explained, "the last step is what
you serve." {patient_fox_he_she_cap} took the goal — to {goal_text} —
and wrote the routine's paw-steps in order, knowing that whatever the
final line evaluated to was what the runner would carry back. {patient_fox}
composed {concept_phrase}, submitted the form, and the REPL — discarding
the earlier steps' values — handed back only the dish from the last."""),

    # 4. Tasting-cards feeding into tasting-cards — emphasizes the chained
    #    nature when relevant. Type-neutral phrasing.
    SubplotTemplate("""\
"Recipes can feed into one another," {patient_fox_phrase} said,
spreading several cards on the path. "What one recipe serves, the next
can take as its ingredient — together they make a longer routine." To
{goal_text}, {patient_fox_he_she_cap} composed {concept_phrase}, submitted
the form, and the REPL — walking through the recipe in order — handed back
the value at the end."""),

    # 5. The Hasty-fox-skips-the-tasting-card template — Hasty fox guesses,
    #    Patient fox actually writes the tasting-card.
    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, insisted {hasty_fox_he_she} could just
shout the answer rather than bother writing a tasting-card. {patient_fox_phrase}
only smiled and reached for a fresh card. To {goal_text}, {patient_fox_he_she}
composed {concept_phrase}, submitted the form, and the REPL — running the
recipe paw-step by paw-step — handed back the value {hasty_fox} had been
guessing at."""),
]


# ─────────────────────── vine-tray (collections) ──────────────────────


_BASKET_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The vine-tray-on-the-path template — generic; whatever the
    #    operation, the tray stays as it was, the form returns the
    #    new arrangement.
    SubplotTemplate("""\
{patient_fox_phrase} pointed to a vine-tray with named slots sitting
{place}. "Whatever I want to do with what's inside," {patient_fox_he_she}
said, "I read from the tray, work the change, and the tray itself stays
as it was — what I get back is a fresh arrangement." To {goal_text},
{patient_fox_he_she_cap} composed {concept_phrase}, submitted the form,
and let the REPL handle the tray exactly as the operation prescribed."""),

    # 2. The slots-and-positions template — works for tagged slots (maps),
    #    positional rows (vectors), or kind-only trays (sets).
    #    The narrative is generic; goal_text says which.
    SubplotTemplate("""\
"You can find what you want in a tray several ways," {patient_fox_phrase}
said, gesturing at the woven compartments: "by the label pinned to it,
by its place in line, or by simply asking whether it's there at all."
To {goal_text}, {patient_fox_he_she_cap} wrote {concept_phrase} for the
tray, submitted the form, and the REPL applied the lookup or update exactly
as the form directed."""),

    # 3. The procession template — for ordered collections
    #    (vectors, lists, seqs). Type-neutral phrasing.
    SubplotTemplate("""\
A line of clusters hung from the trellis {place}, each one hanging from
the one before — head at the top, the rest cascading down. "Many of our
trays are like this procession," {patient_fox_phrase} said. "You can grab
the head, you can ask for the tail, you can put a new cluster at the front
of the line." To {goal_text}, {patient_fox_he_she} composed {concept_phrase},
submitted the form, and the REPL marched the procession exactly as the form
described."""),

    # 4. The new-tray-from-old template — immutability emphasis;
    #    works for any collection type.
    SubplotTemplate("""\
"Watch carefully," {patient_fox_phrase} said, holding up the original tray.
"Whatever I do to it, this one sits unchanged on the trellis — what I get
back is a fresh tray with the change made, leaving the first one exactly
where it was." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL returned a new arrangement
while the original waited, untouched. {hasty_fox_phrase}, {emo_tired}, was
beginning to see why nothing could be lost by trying."""),

    # 5. The Hasty-fox-rummages-loudly template — Hasty fox guesses by
    #    rummaging; Patient fox's careful tray-work wins.
    SubplotTemplate("""\
{hasty_fox_phrase} began rummaging in the tray, {emo_proud}, calling out
guesses about its contents without quite checking. "I know exactly what's
in there," {hasty_fox_he_she} insisted. {patient_fox_phrase} shook
{patient_fox_his_her} head. To {goal_text} properly, {patient_fox_he_she}
wrote {concept_phrase} carefully on a slate, submitted the form, and the
REPL — looking into the tray the way the form told it to — handed back the
answer {hasty_fox} had been guessing at."""),
]


# ─────────────────────── grape-sieve (HOFs) ───────────────────────────


_SIEVE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The general sieve — works for transform (map), select (filter),
    #    select-counted (take/drop), or dedupe (distinct).
    SubplotTemplate("""\
{patient_fox_phrase} held up a grape-sieve {place} — a paw-step rule
attached at its mouth. "Whatever rule we hang on the sieve," {patient_fox_he_she}
said, "the basket's grapes pass through one at a time: some are changed,
some kept, some dropped, depending on the rule." To {goal_text},
{patient_fox_he_she_cap} composed {concept_phrase} as the sieve's rule,
poured the basket through, submitted the form, and the REPL returned what
the sieve had let through."""),

    # 2. The pour-through-and-collect template — generic emphasis on the
    #    new-basket-out-the-other-side metaphor.
    SubplotTemplate("""\
{patient_fox_phrase} balanced a sieve over an empty stave-bucket.
"The grapes go in at the top," {patient_fox_he_she} said, "and the sieve
does its work — applying the rule, choosing or changing — and what lands
in the bucket below is the result." To {goal_text}, {patient_fox_he_she_cap}
composed {concept_phrase}, poured the input through, submitted the form,
and the REPL collected what fell into the receiving basket."""),

    # 3. Stacked sieves — output of one feeds the next.
    #    (comp / xform.)
    SubplotTemplate("""\
{patient_fox_phrase} stacked two sieves one above the other, the output
of the first feeding into the second. "What lands at the bottom,"
{patient_fox_he_she} said, "has been through both rules in order — applied
as a single combined sieve." To {goal_text}, {patient_fox_he_she_cap}
composed {concept_phrase} as a stack of sieves, poured the input through,
submitted the form, and the REPL caught what the stack let through."""),

    # 4. The receiver template — pour into any kind of basket.
    #    (into / into with xform.)
    SubplotTemplate("""\
"You can pour the result into any kind of basket you like," {patient_fox_phrase}
said. "A row of grapes, a unique-only basket, a tray of any shape — the sieve
doesn't care; the receiver does." To {goal_text}, {patient_fox_he_she_cap}
composed {concept_phrase}, chose the right empty receiver, poured through the
sieve, submitted the form, and the REPL packed the result into the basket of
{patient_fox_his_her} choosing."""),

    # 5. The Hasty-fox-tries-to-shortcut-the-sieve template — Hasty fox
    #    guesses, Patient fox pours through carefully.
    SubplotTemplate("""\
{hasty_fox_phrase} eyed the basket, {emo_proud}, and called out a guess
about what would come out the other side of the sieve without bothering
to actually pour. {patient_fox_phrase} shook {patient_fox_his_her} head
and went on with the work: to {goal_text}, {patient_fox_he_she} composed
{concept_phrase} as the sieve's rule, poured the input through carefully,
submitted the form, and the REPL returned the only answer that would do
— the one the sieve had actually produced."""),
]

# ─────────────────────── leather-ledger (atom/ref) ────────────────────


_NOTEBOOK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. Leather ledger on the orchard wall; every fox can read or
    #    atomically update. The form is written in; swap-in a new
    #    tally means crossing out and rewriting on a new line.
    SubplotTemplate("""\
A leather ledger lay pinned to the orchard wall. Any fox could walk
by, read the page, or — carefully — update it. "{patient_fox_phrase}
tells me that atoms are like this ledger," {hasty_fox_he_she} said.
"You can deref to read; you can swap! to write atomically, no matter
who else is watching." To {goal_text}, {patient_fox_he_she_cap}
composed {concept_phrase}, submitted the form, and let the REPL work
the ledger exactly as the form prescribed."""),

    # 2. Atomic swap — read, apply, write, all in one motion.
    #    The patient fox explains the atomic-update dance.
    SubplotTemplate("""\
"When I want to update the ledger," {patient_fox_phrase} said,
"I don't lift it from the wall and walk away — I read the page, apply
the change, and write it back, all in a single motion. If two foxes
arrive at once, the REPL makes sure only one of us goes through at a
time." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase} for the ledger, submitted the form, and the REPL
applied the update atomically."""),

    # 3. The ledger-stays-on-the-wall template — emphasizes
    #    persistence of the ledger between updates.
    SubplotTemplate("""\
"The ledger stays put on the wall," {patient_fox_phrase} said,
"so any fox who comes by can read what's on the page right now. The
page changes only when someone writes — and only as the REPL allows."
To {goal_text}, {patient_fox_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — reading or writing the ledger as
the form prescribed — handed back the value the page had carried."""),

    # 4. The shared-state template — generic emphasis that this is
    #    about coordinated updates among several foxes.
    SubplotTemplate("""\
"Many foxes can come and go past the wall," {patient_fox_phrase}
said, "and each one's read or write must agree with the others. The
REPL sees to that — no two writers stomp on each other's work." To
{goal_text}, {patient_fox_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — coordinating each access cleanly —
handed back what the ledger now said."""),

    # 5. The hasty-fox-snatches-the-ledger template — hasty tries to
    #    rip the page; patient updates carefully. Generic fable beat.
    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, swiped at the ledger on the wall,
trying to scribble an answer over the page. {patient_fox_phrase}
caught {hasty_fox_him_her} firmly: ledgers shared by all the orchard
need careful updates, not snatches. To {goal_text},
{patient_fox_he_she} composed {concept_phrase}, submitted the form,
and the REPL — applying the update the runtime's careful way — handed
back the value the page now held."""),
]


# ─────────────────────── grape-tally (arithmetic) ─────────────────────


_ACORN_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The counting-grapes template — generic arithmetic frame.
    SubplotTemplate("""\
{patient_fox_phrase} laid grapes out on a flat slate {place}, sorting
them into small heaps. "Numbers in Clojure are just like grape-clusters
in heaps," {patient_fox_he_she} said: "you can count them, you can add
two heaps together, you can divide one heap among several." To
{goal_text}, {patient_fox_he_she_cap} composed {concept_phrase},
submitted the form, and let the REPL hand back the count of whatever
the operation had produced."""),

    # 2. The heap-grows-or-shrinks template — for inc/dec, +/-.
    SubplotTemplate("""\
"Watch the heap," {patient_fox_phrase} said, gesturing at a small
pile of grapes. "Every operation either adds, takes away, or combines
what's already there — the heap grows or shrinks by exactly what you
say." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL returned the new
count, the heap settled into its new arrangement."""),

    # 3. The careful-arrangement template — generic; the operation
    #    is whatever the form says, but the patient fox's care with
    #    the grapes is what the metaphor carries.
    SubplotTemplate("""\
{patient_fox_phrase} arranged a small heap of grapes {place}, careful
with the count. "Numbers in Clojure don't fudge," {patient_fox_he_she}
said. "Whatever you do — adding, subtracting, dividing into heaps with
leftovers, comparing two piles — the REPL gets it exactly right, every
time." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL handed back the
precise number the operation called for."""),

    # 4. The hasty-fox-counts-aloud template — hasty guesses by
    #    sight, patient counts carefully.
    SubplotTemplate("""\
{hasty_fox_phrase} eyed the heap, {emo_proud}, and called out a guess
about how many grapes were there without bothering to count.
{patient_fox_phrase} simply began counting — to {goal_text} required
no eyeballing, only the form. {patient_fox_he_she_cap} composed
{concept_phrase}, submitted it to the REPL, and the runtime returned
the number that had been there all along, settling the matter the
patient way."""),

    # 5. The exact-count template — generic; emphasizes that the
    #    REPL gives the exact number, no matter the operation.
    SubplotTemplate("""\
"Whatever the heap looks like after the operation,"
{patient_fox_phrase} said, "the REPL gives the exact count — small or
large, fraction or whole, the answer is precise." To {goal_text},
{patient_fox_he_she_cap} composed {concept_phrase}, submitted the form,
and the REPL handed back the value, exactly as the operation had
produced it."""),
]


# ─────────────────────── orchard-gate (boolean) ───────────────────────


_GATE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The gate-on-the-path template — generic for any boolean
    #    test, equality, or short-circuit. Both latches of the
    #    orchard's outer gate.
    SubplotTemplate("""\
A small wooden gate stood at the orchard's edge {place}, swinging open
or closed by the value the fox brought to it. "Boolean forms in Clojure
are like gates," {patient_fox_phrase} said. "The REPL checks the value,
swings the gate, and what comes back is the gate's verdict." To
{goal_text}, {patient_fox_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL returned whatever the gate had
decided."""),

    # 2. The truthy/falsey-rules template — both latches must lift
    #    for `and`; either lifts for `or`; the gate's verdict stands.
    SubplotTemplate("""\
"Only two things in Clojure close the gate," {patient_fox_phrase}
said: "nil and false. Everything else — zero, the empty string, an
empty cluster of grapes — opens it. The gate's verdict follows that
rule exactly." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL returned the value
the gate had passed, true or false."""),

    # 3. The gate-decides-the-verdict template — generic emphasis on
    #    the REPL's decision being the only authority.
    SubplotTemplate("""\
"You can't tell which way the gate will swing by guessing,"
{patient_fox_phrase} said. "You bring the value to the gate, the REPL
checks it, and the gate gives the only answer that matters." To
{goal_text}, {patient_fox_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL settled the matter — the gate had
swung exactly as the rule said."""),

    # 4. The hasty-fox-bumps-the-gate template — hasty guesses gate
    #    state, patient tests it. Latches both lift or either lifts.
    SubplotTemplate("""\
{hasty_fox_phrase} sprinted toward the gate {place}, {emo_proud},
certain it would swing open for {hasty_fox_him_her}. {patient_fox_phrase}
slowed and watched: the only way to know which way the gate would swing
was to actually carry the value to it. To {goal_text},
{patient_fox_he_she} composed {concept_phrase}, submitted the form,
and the REPL settled the matter — the gate had swung exactly as the
rules said, regardless of {hasty_fox_phrase}'s guess."""),

    # 5. The gate-carries-the-value template — generic emphasis on
    #    the REPL returning the value the gate carries (not always
    #    a strict true/false — `and` returns the last truthy, etc.).
    SubplotTemplate("""\
"The gate carries the value through, not just a yes or a no,"
{patient_fox_phrase} said. "Whatever the gate's verdict, that's what
the REPL hands back — sometimes a strict true or false, sometimes the
very value that passed the test." To {goal_text},
{patient_fox_he_she} composed {concept_phrase}, submitted the form,
and the REPL returned the value the gate had carried through."""),
]


# ─────────────────────── orchard-fork (control flow) ──────────────────


_FORK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The fork-in-the-path template — generic; the path branches
    #    and the condition decides which arm runs. Left to the
    #    vine-row, right to the market.
    SubplotTemplate("""\
The orchard path forked {place}, with one or more arms branching off
and each arm marked with a condition. "Branching forms in Clojure are
forks like this," {patient_fox_phrase} said. "The REPL checks the
condition, takes the matching arm, and only that arm's value comes
back." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — having taken the
right arm — handed back its value."""),

    # 2. The crossroads template — applies to `cond` / `case` /
    #    multi-arm branching. Type-neutral framing: "the fox walks
    #    past stones" works for if (one stone), cond/case (many).
    SubplotTemplate("""\
The orchard path {place} opened into a crossroads, each arm marked by a
small condition-stone. "Branching forms work like this,"
{patient_fox_phrase} said: "the fox walks past the stones in order,
takes the first arm whose stone says true, and the value of that arm is
what comes back." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL took the right arm
and returned its value."""),

    # 3. The unrun-arm template — generic emphasis that branches
    #    not taken don't run.
    SubplotTemplate("""\
"What's important about a fork," {patient_fox_phrase} said, "is that
the arm not taken doesn't run at all. The REPL checks the condition,
walks the right arm, and the unrun arm is just left behind." To
{goal_text}, {patient_fox_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — running only what was needed —
handed back the value of the chosen arm."""),

    # 4. The hasty-fox-tries-to-skip-the-condition template — hasty
    #    guesses which arm; patient actually checks. Generic fable beat.
    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, called out which arm of the fork
{hasty_fox_he_she} was sure the REPL would take, without bothering to
check the condition. {patient_fox_phrase} only smiled: the only way to
know is to evaluate the condition. To {goal_text},
{patient_fox_he_she} composed {concept_phrase}, submitted the form, and
the REPL — checking the condition properly — returned the value of the
arm the form actually ran."""),

    # 5. The one-form-decides template — generic; emphasizes that
    #    the condition is what decides, not the fox's hopes.
    SubplotTemplate("""\
"It isn't the fox who picks the arm," {patient_fox_phrase} said,
"it's the condition. Whatever the condition evaluates to, that decides."
To {goal_text}, {patient_fox_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — letting the condition decide —
handed back the value of the arm the condition had pointed at."""),
]

# ─────────────────────── vine-post nameplate (def/ns) ─────────────────


_ROADSIGN_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The vine-post nameplate template — `def`.
    SubplotTemplate("""\
{patient_fox_phrase} drove a wooden post into the vineyard soil
{place} and chalked a fresh nameplate on it. "A def is a nameplate
on the vine-post," {patient_fox_he_she} said. "Any fox passing reads
the name, learns what's growing here, and can refer to it later by
name alone." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL planted the
nameplate — the name now bound to its value for any later fox along
the trellis."""),

    # 2. The hasty-and-patient nameplate template — hasty assumes,
    #    patient verifies what's written.
    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, glanced at the vine-posts as {hasty_fox_he_she}
hurried past, certain {hasty_fox_he_she} remembered what each nameplate said.
{patient_fox_phrase} stopped and read the chalk carefully. "The good thing about
a nameplate," {patient_fox_he_she} said, "is that it stays where you chalked it.
The next fox along the orchard reads what's actually there — whatever the
mark says, not what you thought." To {goal_text}, {patient_fox_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL — reading the
nameplate exactly — returned the value {hasty_fox} had mis-remembered."""),

    # 3. The orchard ledger template — registry of vine-posts.
    SubplotTemplate("""\
A small leather ledger sat {place}, its pages listing the vineyard's
nameplates — each nameplate marking what grows on which post. "Names
live in the ledger," {patient_fox_phrase} said: "to use a nameplate,
you make sure the post is marked where the runtime can find it." To
{goal_text}, {patient_fox_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — finding the right nameplate on
the right post — returned the value the form had asked for."""),

    # 4. The careful-naming template — naming is half the art.
    SubplotTemplate("""\
"Naming is half the art," {patient_fox_phrase} said, sketching a
careful nameplate in chalk dust. "A clear name on the vine-post tells
every later fox what to expect; a careless one trips them up." To
{goal_text}, {patient_fox_he_she_cap} composed {concept_phrase} with
the right name in mind, submitted the form, and the REPL — reading
the nameplate exactly — returned the value the mark had promised."""),

    # 5. The hasty-fox-misreads-the-nameplate template — hasty guesses,
    #    patient fox reads carefully.
    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, glanced at the nameplate {place} and
called out what {hasty_fox_he_she} thought it said without slowing.
{patient_fox_phrase} stopped and read carefully. To {goal_text}, the
nameplate had to be read exactly: {patient_fox_he_she} composed
{concept_phrase}, submitted the form, and the REPL — reading
literally — returned the right value, while {hasty_fox}'s guess fell
short."""),
]


# ─────────────────────── catching-cloth (try/catch) ───────────────────


_SAFETYNET_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The catching-cloth template — `try`/`catch`.
    SubplotTemplate("""\
{patient_fox_phrase} strung a small catching-cloth between two
orchard trees {place}. "If a grape falls, the cloth catches it; the
harvest doesn't end, only the path bends." To {goal_text},
{patient_fox_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — cloth in place — caught the falling fruit and
returned the value the catch-arm had specified, the work continuing
the patient way."""),

    # 2. The practice orchard template — REPL safety; the cloth forgives.
    SubplotTemplate("""\
"This is the practice orchard," {patient_fox_phrase} said {place},
gesturing wide. "A slip here costs nothing — the cloth below forgives
it. Write a form, see what comes back, fix it, try again. The REPL is
forgiving in a way that a real harvest is not." To {goal_text},
{patient_fox_he_she_cap} composed {concept_phrase}, submitted the form,
and the REPL returned the value — even if the form had been close to a
mis-step."""),

    # 3. The slip-and-recovery template — catching-cloth catches the slip.
    SubplotTemplate("""\
"What matters when something goes wrong," {patient_fox_phrase} said,
"is that the harvest can continue — the cloth catches the falling
grape, and the runtime takes the recovery path. The answer comes back
even when something inside the form dropped off the vine." To
{goal_text}, {patient_fox_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — the cloth in place — returned the
value the recovery path had produced."""),

    # 4. The hasty-and-patient catching template — hasty forgets cloth,
    #    patient demonstrates safety.
    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, eyed a high trellis and sprinted toward it,
{hasty_fox_he_she} assumed the grapes would fall safely. {patient_fox_phrase}
shook {patient_fox_his_her} head and strung the catching-cloth carefully below.
"There's a discipline to gathering with the cloth," {patient_fox_he_she} said.
To {goal_text} required no recklessness, only the cloth: {patient_fox_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL — catching anything
that fell — returned the answer the safety design had earned."""),

    # 5. The hasty-fox-ignores-the-cloth template — hasty skips safety,
    #    patient demonstrates the design.
    SubplotTemplate("""\
{hasty_fox_phrase} eyed a high trellis {place}, {emo_proud}, certain
{hasty_fox_he_she} could pick without a safety cloth below.
{patient_fox_phrase} shook {patient_fox_his_her} head and strung the
cloth carefully. To {goal_text} required no recklessness, only the
cloth: {patient_fox_he_she} composed {concept_phrase}, submitted the
form, and the REPL — catching anything that fell — returned the
answer the safety design had earned."""),
]


# ─────────────────────── harvest-parchment (IO) ─────────────────────────


_SCROLL_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The harvest-parchment template — reading and writing.
    SubplotTemplate("""\
{patient_fox_phrase} unrolled a harvest-parchment tied to the fence
{place}, dipping a quill into ink at the edge. "The world outside the
REPL is parchments," {patient_fox_he_she} said: "you read what they
say, you write what you want to keep, and the runtime carries the
words back and forth." To {goal_text}, {patient_fox_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL handed
back what the parchment had said, or what the writing had
committed."""),

    # 2. The hasty-assumes-parchment template — hasty guesses contents,
    #    patient reads the actual harvest-record.
    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, glanced at a harvest-parchment tied to the
fence and claimed {hasty_fox_he_she} knew exactly what it said without actually
reading. {patient_fox_phrase} unrolled it carefully. "Reading and writing
parchments is just like reading and writing forms," {patient_fox_he_she} said.
"You ask the runtime for what's actually on the harvest-record, and the work
goes both ways through one quill." To {goal_text}, {patient_fox_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL handed back what
the parchment had actually said — not what {hasty_fox} had guessed."""),

    # 3. The careful-handling template — resource discipline.
    SubplotTemplate("""\
"The world outside the REPL is bigger than the REPL,"
{patient_fox_phrase} said, "and a parchment out there has its own
discipline — open it carefully, handle it with care, close it when
you're done." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — handling the
parchment the runtime's careful way — returned the value the work had
produced."""),

    # 4. The hasty-fox-skips-the-parchment template — hasty guesses,
    #    patient reads the actual harvest-record.
    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, claimed the parchment said exactly
what {hasty_fox_he_she} expected and didn't bother to actually read.
{patient_fox_phrase} unrolled it carefully. To {goal_text} required
the parchment's actual contents — {patient_fox_he_she} composed
{concept_phrase}, submitted the form, and the REPL — reading the
harvest-record faithfully — returned the value the paper had
held."""),

    # 5. The two-worlds template — inside and outside the REPL.
    SubplotTemplate("""\
"There's the world inside the REPL," {patient_fox_phrase} said, "and
the world outside it. Parchments are how the two meet — a value
crosses out and becomes marks on paper, or marks on paper cross in and
become a value again." To {goal_text}, {patient_fox_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL —
bridging the two worlds — handed back the value the work had
carried."""),
]


# ─────────────────────── orchard-keeper guild (protocols) ─────────────


_GUILD_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The founding-the-guild template — `defprotocol`.
    SubplotTemplate("""\
{patient_fox_phrase} carved a small wooden sign {place}: "Orchard-
Keepers' Guild — any animal may join." "A protocol is a guild,"
{patient_fox_he_she} said. "It lists what every member must be able
to do — the methods. Any creature that can sign the book may claim
membership." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — guild founded —
handed back the guild's record."""),

    # 2. The same-call-many-species template — polymorphism.
    SubplotTemplate("""\
"What makes a guild useful," {patient_fox_phrase} said, "is that the
call is the same for every member, but each species answers in its own
way. The runtime looks up which species the fox is, then runs that
species' answer." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — dispatching to
the right species — returned the species-specific value."""),

    # 3. The guild-ledger template — the guild's record.
    SubplotTemplate("""\
{patient_fox_phrase} held up the guild ledger. "Membership is in this
book," {patient_fox_he_she} said: "the species, the methods they swear
they can perform, and the actual answers each species gives. The
runtime reads from the book whenever the call goes out." To
{goal_text}, {patient_fox_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — checking the ledger as it ran —
returned the right answer."""),

    # 4. The boundaries-of-the-guild template — each guild separate.
    SubplotTemplate("""\
"Each guild has its own boundaries," {patient_fox_phrase} said.
"Belonging to the Orchard-Keepers' guild doesn't mean belonging to the
Gatherers' guild — the runtime checks each separately, and only the
right guild's answer comes back." To {goal_text},
{patient_fox_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — respecting which guild was being called —
returned the right value."""),

    # 5. The hasty-and-patient-membership template — hasty boasts,
    #    patient shows the ledger.
    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, declared that {hasty_fox_he_she}
could of course do whatever the guild's call demanded — even though
the creature had never signed the ledger. {patient_fox_phrase} only smiled
and held up the guild book: "Membership is written here," {patient_fox_he_she}
said. To {goal_text}, {patient_fox_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — checking the ledger first — returned
the right answer based on who had actually signed."""),
]


# ─────────────────────── stone tool-shed (interop) ────────────────────


_TOOLSHED_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The borrowed-tool template — host interop.
    SubplotTemplate("""\
{patient_fox_phrase} reached into a stone tool-shed at the orchard's
edge {place} and pulled out a tool {patient_fox_he_she} hadn't carved
{patient_fox_him_her}self — a tool from the stone-keepers' world. "This
isn't ours," {patient_fox_he_she} said, "but we can call its methods
directly: dot-prefix on the instance, or slash for the shed's name." To
{goal_text}, {patient_fox_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — calling into the foreign tool —
handed back what its method had returned."""),

    # 2. The labeled-toolshed template — instance and static tools.
    SubplotTemplate("""\
"Each tool in the foreign tool-shed has its own label,"
{patient_fox_phrase} said, "and the right way to call it depends on
which kind of tool it is — some held by a stone-keeper, some standard-
issue called by the shed's name." To {goal_text},
{patient_fox_he_she_cap} composed {concept_phrase} using the right
calling convention, submitted the form, and the REPL — invoking the
host tool by its label — returned the value the host had computed."""),

    # 3. The careful-handling-of-foreign-tools template — discipline
    #    of interop.
    SubplotTemplate("""\
"Foreign tools work, but they need careful handling,"
{patient_fox_phrase} said. "Their labels are different, their calling
conventions are different, and the runtime has to bridge between the
orchard and the stone-shed every time." To {goal_text},
{patient_fox_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — making the bridge cleanly — handed back the
value the foreign tool had produced."""),

    # 4. The hasty-and-patient-toolshed template — hasty grabs wrong,
    #    patient checks labels.
    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, grabbed at the stone tool-shed
without checking which tool was which. The wrong tool made an awful
sound. {patient_fox_phrase} sighed and walked over: to {goal_text}
required reading the shed's labels carefully. {patient_fox_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL — calling
the right host method by its true label — returned the value cleanly
while {hasty_fox} watched, chastened."""),

    # 5. The two-worlds template — orchard and stone-keeper tools.
    SubplotTemplate("""\
"There's the orchard's own tool-shed," {patient_fox_phrase} said,
"and there's the stone-keeper's. The runtime moves a value across the
boundary, calls the foreign tool, and brings the result back into the
orchard." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — bridging the two
tool-sheds — returned the value cleanly."""),
]

# ─────────────────────── swift-fox runner (agent/future) ──────────────


_RUNNERAHEAD_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The swift-fox-sent-ahead template — future / agent.
    SubplotTemplate("""\
{patient_fox_phrase} dispatched a swift fox down the path to the
market {place}, carrying a proposal. "The swift fox goes ahead while
we keep on with our own work," {patient_fox_he_she} said, "and when
we need to know the verdict, we ask the swift fox to bring it back."
To {goal_text}, {patient_fox_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — sending the swift fox, fetching
the verdict later — returned the value when it was ready."""),

    # 2. The eventually-returns template — generic; a swift fox sent
    #    ahead eventually returns the verdict, however the
    #    coordination is arranged.
    SubplotTemplate("""\
"Once you've sent the swift fox ahead," {patient_fox_phrase} said,
"you keep on with your own work in the orchard. The verdict will be
there when you ask for it — sometimes you have to wait for the fox
to return from the market, sometimes you can keep gathering until you
need it." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — coordinating the
swift fox the way the form prescribed — returned the value when it
was ready."""),

    # 3. The patience-of-the-patient-fox template — generic; the
    #    patient fox's willingness to wait for the swift fox is the
    #    fable beat.
    SubplotTemplate("""\
"The hard part isn't sending the swift fox," {patient_fox_phrase}
said. "The hard part is being patient enough to wait for the verdict
when it comes — not snatching the result too early, not giving up too
soon. The REPL makes that easier than it sounds." To {goal_text},
{patient_fox_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — coordinating the wait properly — returned the
swift fox's verdict when the fox had actually arrived."""),

    # 4. The patient-fox-coordinates template — generic.
    SubplotTemplate("""\
{patient_fox_phrase} arranged a small relay {place}, swift foxes and
messengers each at their post. "The runtime keeps track of which fox
was sent when and when each one finishes," {patient_fox_he_she} said,
"so the verdicts come back in the right order, no matter how long
each swift fox takes." To {goal_text}, {patient_fox_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL —
coordinating the relay — returned the right value at the right
time."""),

    # 5. The hasty-fox-doesn't-wait template — hasty fox reaches for
    #    verdict before swift fox returns.
    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, reached for the swift fox's pouch
before the fox had even returned from the market. {patient_fox_phrase}
held {hasty_fox_him_her} back: a swift fox sent ahead must be allowed
to finish the journey. To {goal_text}, {patient_fox_he_she} composed
{concept_phrase}, submitted the form, and the REPL — waiting for the
swift fox the patient way — returned the value when the swift fox had
actually delivered it."""),
]


# ─────────────────────── rewritten tasting-card (macros) ──────────────


_REWRITERULE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The rewriting-the-card template — `defmacro` introduction.
    SubplotTemplate("""\
{patient_fox_phrase} sat at a small writing desk {place}, quill in
paw. "A macro," {patient_fox_he_she} said, "is a rule that rewrites
the tasting-card before the REPL ever reads it. You write the rule
once, and any card that uses it gets rewritten on the way to the
tasting." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — first rewriting,
then evaluating — returned the value the rewritten card yielded."""),

    # 2. The rule-shapes-the-form template — generic; emphasizes that
    #    macros operate on forms, not values.
    SubplotTemplate("""\
"Here's the difference between a recipe and a rule,"
{patient_fox_phrase} said. "A recipe takes grapes and makes a tasting.
A rule takes a *card* and makes a different *card* — only then does
the REPL get to read it and taste." To {goal_text},
{patient_fox_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — applying the rule to the card first, then
tasting — handed back the value the rewritten card had
produced."""),

    # 3. The REPL-applies-the-rule template — generic.
    SubplotTemplate("""\
"The order matters," {patient_fox_phrase} said. "When a rule is
involved, the REPL first walks through the card and applies the rule
wherever it sees one — and only then does it taste the result." To
{goal_text}, {patient_fox_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — rewriting first, tasting second —
returned the final value."""),

    # 4. The hasty-fox-claims-no-rule-needed template — generic fable
    #    beat.
    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, insisted that no rule was needed —
{hasty_fox_he_she} could write the card directly. {patient_fox_phrase}
allowed that sometimes that's true, but the rule shines when many
cards need the same rewriting. To {goal_text},
{patient_fox_he_she} composed {concept_phrase}, submitted the form,
and the REPL — handling the rule's rewrite the rule's way —
returned the value the card had produced."""),

    # 5. The hasty-fox-tries-to-skip-the-rule template.
    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, insisted that the rule was
unnecessary — {hasty_fox_he_she} could write the rewritten card
directly. {patient_fox_phrase} only smiled: a hand-rewritten card is
fine once, but the rule pays off when many cards need rewriting the
same way. To {goal_text}, {patient_fox_he_she} composed
{concept_phrase}, submitted the form, and the REPL — running the rule
the rule's way — returned the value the rewritten card
yielded."""),
]


# ─────────────────────── ledger marginalia (read-time) ────────────────


_SCRIBE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The reading-conventions-of-the-form template — generic;
    #    works for comments, whitespace, parens, do, reader macros.
    SubplotTemplate("""\
"There are conventions for how the REPL *reads* a form,"
{patient_fox_phrase} said, looking at the leather ledger {place}:
"what counts as one token, what's just spacing, what gets ignored,
what gets grouped together. The scribe and the reader both follow the
same conventions." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — reading exactly
by the conventions — returned the value the form had specified."""),

    # 2. The form-is-what-the-reader-sees template — generic.
    SubplotTemplate("""\
"A form is what the reader sees," {patient_fox_phrase} said, pointing
at the ledger, "after the conventions have been applied. Some marks
count, some don't; some shapes are expanded before the REPL even gets
a look. The form you write and the form the REPL evaluates aren't
always character-for-character the same." To {goal_text},
{patient_fox_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — reading carefully — returned the value of what
the conventions had produced."""),

    # 3. The careful-writing-careful-reading template — generic.
    SubplotTemplate("""\
{patient_fox_phrase} unrolled a small slate {place} and wrote slowly,
paying attention to every mark. "The form has to be written so the
REPL can read it cleanly," {patient_fox_he_she} said. "If the marks
are right, the reader gets the right form; if not, not." To
{goal_text}, {patient_fox_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — reading exactly as written —
returned the value cleanly."""),

    # 4. The hasty-fox-misreads-the-form template — generic fable beat.
    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, glanced at the form and called out
what {hasty_fox_he_she} thought it would do without paying attention
to the conventions of how it was written. {patient_fox_phrase} only
shook {patient_fox_his_her} head — the REPL reads the form exactly.
To {goal_text}, {patient_fox_he_she} composed {concept_phrase},
submitted the form, and the REPL — reading literally — returned the
right value, while {hasty_fox} guessed wrong."""),

    # 5. The form-as-it-is template — generic.
    SubplotTemplate("""\
"A form is what's actually there on the ledger page," {patient_fox_phrase}
said, "after the conventions of writing and reading have done their
work. The REPL sees the cleaned-up form, evaluates it, and gives back
what it computes." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — taking the form
exactly as it was — handed back the value."""),
]


# ─────────────────────── chalk tag on vine-post (quote/sym) ───────────


_CHALKMARK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The mark-on-the-post template — symbols vs values.
    SubplotTemplate("""\
{patient_fox_phrase} pointed at a name scratched with chalk onto the
vine-post {place}, then at an actual grape-cluster hanging from the
vine. "The mark on the post is the *name*; the grape-cluster is the
*value*. They are not the same thing — and Clojure lets you talk
about either one." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — keeping the name
and the value distinct — returned the right answer."""),

    # 2. The label-the-list template — `quote` / `'`.
    SubplotTemplate("""\
"To talk about the form itself rather than tasting it,"
{patient_fox_phrase} said, "you label the form with a chalk mark in
front. Quoting tells the REPL: don't taste this, just hand it back as
the shape it is." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — respecting the
chalk mark — returned the form unevaluated."""),

    # 3. The labeling-form-vs-evaluating-it template — generic
    #    emphasis on the distinction without claiming a specific
    #    quote/unquote arrangement.
    SubplotTemplate("""\
"There's a difference between *labeling* the form and *tasting* it,"
{patient_fox_phrase} said. "Quote in any of its shapes is the
labeling — the REPL hands you back the form, not its value, unless you
say otherwise." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — labeling exactly
what the form asked for — returned the form-as-data, exactly as the
marks had directed."""),

    # 4. The hasty-fox-confuses-name-with-value template.
    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, mistook the chalk name on the post
for the grape-cluster it pointed to. "It says ripeness, so the value
must be ripeness itself!" {patient_fox_phrase} only shook
{patient_fox_his_her} head: the mark and the cluster are never the same
thing. To {goal_text}, {patient_fox_he_she} composed {concept_phrase},
submitted the form, and the REPL — keeping mark and cluster distinct —
returned the right answer for the goal."""),

    # 5. The tag-names-but-is-not template — generic emphasis on the
    #    distinction.
    SubplotTemplate("""\
"A chalk tag on the vine-post names what grows there," {patient_fox_phrase}
said, pointing at the post. "The tag reads 'muscat,' but the tag isn't
muscat — muscat is the cluster hanging below. The name points to the
thing; it never becomes the thing." To {goal_text},
{patient_fox_he_she_cap} composed {concept_phrase}, submitted the form,
and the REPL — keeping name and thing apart — returned the right
value."""),
]


# ─────────────────────── market sorting-tray (multimethods) ───────────


_SORTINGTABLE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The sorting-tray template — `defmulti`.
    SubplotTemplate("""\
A long wooden tray stood {place}, with several arms branching off its
sides. "Defmulti is a sorting-tray," {patient_fox_phrase} said. "You
decide what color to look at on each grape; the tray routes each
cluster down the matching arm." To {goal_text}, {patient_fox_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL — reading
the cluster's color, picking the arm — returned the value the right
arm had produced."""),

    # 2. The branch-of-the-tray template — `defmethod`.
    SubplotTemplate("""\
"To add a branch to the sorting-tray," {patient_fox_phrase} said, "you
say what color the branch handles and what behavior runs when a cluster
of that color arrives." To {goal_text}, {patient_fox_he_she_cap}
composed {concept_phrase} for the right branch, submitted the form, and
the REPL — adding the branch, dispatching the cluster — returned the
branch-specific value."""),

    # 3. The REPL-reads-the-color template — generic; the sorting-tray
    #    reads whatever the dispatch function returns and routes
    #    accordingly.
    SubplotTemplate("""\
"What the tray sorts by is up to you," {patient_fox_phrase} said. "You
decide what to look at on each cluster — a color, a kind, a field,
anything. The REPL reads it, finds the matching arm, and runs that
one." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — reading the color
the dispatch function produced — returned the value the right arm had
given."""),

    # 4. The flexible-routing template — generic emphasis on the
    #    open-dispatch nature.
    SubplotTemplate("""\
"The good thing about a sorting-tray," {patient_fox_phrase} said, "is
that you can keep adding new arms whenever a new kind of grape shows
up. The original tray doesn't change; the REPL just learns one more
route." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — routing through
the tray cleanly — returned the right value."""),

    # 5. The hasty-fox-jumps-without-sorting template.
    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, leaped onto the sorting-tray without
showing the cluster's color. {patient_fox_phrase} pointed at the edge
of the tray: every cluster must show the color the tray sorts by. To
{goal_text}, {patient_fox_he_she} composed {concept_phrase}, submitted
the form, and the REPL — reading the color first, dispatching second —
returned the value from the correct branch."""),
]

# ─────────────────────── labeled fruit-crate (deftype/defrecord) ────────


_CARRYINGCASE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The labeled-compartments template — defrecord.
    SubplotTemplate("""\
{patient_fox_phrase} held up a small wooden fruit-crate {place}, its inside
divided into labeled compartments. "A defrecord is a crate like
this," {patient_fox_he_she} said: "named compartments for picked
fruit; a mark on the outside saying what kind of crate it is." To
{goal_text}, {patient_fox_he_she_cap} composed {patient_fox_his_her}
{concept_phrase}, submitted the form, and the REPL — constructing
the crate, filling its compartments — returned the value the crate
held or carried."""),

    # 2. The bare-case template — deftype.
    SubplotTemplate("""\
"A deftype is a barer crate," {patient_fox_phrase} said. "Compartments,
a mark — no map-like behavior unless you ask for it. Faster, more
focused, less convenient." To {goal_text}, {patient_fox_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL —
constructing the bare crate as specified — returned the value
inside."""),

    # 3. The reaching-into-the-compartment template — field access.
    SubplotTemplate("""\
"To reach into a labeled compartment," {patient_fox_phrase} said,
"you ask for it by name. The crate knows where each compartment
is; the runtime fetches it cleanly." To {goal_text},
{patient_fox_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — opening the right compartment — returned
exactly what was inside."""),

    # 4. The hasty-fox-guesses-the-crate template — Hare equivalent.
    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, looked at the wooden crate and
called out what {hasty_fox_he_she} thought was inside without
bothering to check the compartments. {patient_fox_phrase} only
smiled — the crate's structure was what mattered. To {goal_text},
{patient_fox_he_she} composed {concept_phrase}, submitted the form,
and the REPL — constructing the crate exactly — returned the right
answer, while {hasty_fox_phrase}'s guess fell short."""),

    # 5. The compartment-persistence template — immutability of the crate.
    SubplotTemplate("""\
"Whatever happens when you fill a compartment," {patient_fox_phrase}
said, "the crate itself remembers what was there before. Read from
one compartment, fill another, and the first stays exactly as it was
— what comes back is a fresh crate with the new arrangement." To
{goal_text}, {patient_fox_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — handling the crate the careful
way — returned the value, leaving the original crate untouched."""),
]


# ─────────────────────── vine-row tally (reduce/count) ────────────────


_TALLYWALK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The walking-the-row template — reduce.
    SubplotTemplate("""\
{patient_fox_phrase} walked the row of grape-vines {place}, one paw at
a time, a small slate in hand for the running tally. "Reduce is
this walk," {patient_fox_he_she} said: "at each vine, you count its
clusters and combine them into the tally; at the row's end, the
tally is your answer." To {goal_text}, {patient_fox_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL —
walking the vine-row, carrying the tally — returned the final
number."""),

    # 2. The starting-tally template — reduce with init.
    SubplotTemplate("""\
"You don't have to start the tally at zero," {patient_fox_phrase}
said, holding up a slate already inscribed with a number. "If you
start with a different value, the walk begins from there — at each
vine you fold its cluster-count in from that starting point." To
{goal_text}, {patient_fox_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — starting from the given tally,
walking the vine-row — returned the final value."""),

    # 3. The simple-count template — `count`.
    SubplotTemplate("""\
"The simplest tally-walk is just counting," {patient_fox_phrase}
said: "step along the row, tally one cluster at every vine, no
other operation. The runtime does this for any collection — vector,
list, map, string." To {goal_text}, {patient_fox_he_she_cap}
composed {concept_phrase}, submitted the form, and the REPL —
walking the vine-row, counting the steps — returned the count."""),

    # 4. The hasty-fox-shortcut-the-row template — Hare equivalent.
    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, eyed the vine-row and called out
a tally without bothering to actually walk it. {patient_fox_phrase}
shook {patient_fox_his_her} head — the only way to tally is to pass
each vine and add its count. To {goal_text}, {patient_fox_he_she}
composed {concept_phrase}, submitted the form, and the REPL —
walking the vine-row faithfully — returned the answer that walking
had produced."""),

    # 5. The tally-ends-the-count template — what the running total means.
    SubplotTemplate("""\
"The slate matters," {patient_fox_phrase} said. "Each time you
tally a vine's clusters, you add to the running sum on the slate.
When the row ends, the final number is the answer — the slate
doesn't lie." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — walking the
vine-row, updating the slate at each step — returned the final tally
the row had earned."""),
]


# ─────────────────────── beads on cord (strings) ──────────────────────


_BEADSTRING_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The threading-beads template — `str` concat.
    SubplotTemplate("""\
{patient_fox_phrase} held up a string of small wooden beads {place}.
"Strings in Clojure are like this," {patient_fox_he_she} said: "a
threaded line of characters, in order. Splice strings together,
and the threads are joined; cut a substring out, and you get a
shorter string." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — splicing or
cutting as the form said — returned the new bead-string."""),

    # 2. The counting-beads template — string length / substring.
    SubplotTemplate("""\
"To count the beads, walk the thread," {patient_fox_phrase} said.
"Want a section of beads? Cut from one position to another and you
get a smaller thread, the original untouched." To {goal_text},
{patient_fox_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — counting or cutting — returned the answer the
bead-string had given up."""),

    # 3. The hasty-fox-yanks-at-the-thread template — Hare equivalent.
    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, yanked at the bead-string {place}
without bothering to count. {patient_fox_phrase} stopped
{hasty_fox_him_her}: strings are precise — every bead in its place,
every position counted. To {goal_text}, {patient_fox_he_she}
composed {concept_phrase}, submitted the form, and the REPL —
handling the thread carefully — returned the right answer."""),

    # 4. The string-immutability template — the thread stays unchanged.
    SubplotTemplate("""\
"Here's what's important about a bead-string," {patient_fox_phrase}
said. "Whatever you do to it — splice threads, cut a section — the
original string sits unchanged. What you get back is a fresh string
with the work done, leaving the first one exactly as it was." To
{goal_text}, {patient_fox_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — handling the string the careful
way — returned the new bead-string, untouched."""),

    # 5. The position-matters template — each bead has a place.
    SubplotTemplate("""\
"Each bead has a place on the cord," {patient_fox_phrase} said.
"The first bead is position zero; count to any position and ask for
the bead there. Or ask for a range — from position two to position
five — and the runtime knows exactly which beads to return." To
{goal_text}, {patient_fox_he_she_cap} composed {concept_phrase},
submitted the form, and the REPL — finding the right bead by its
position — returned it cleanly."""),
]


# ─────────────────────── row-restart (recur/loop) ─────────────────────


_CIRCUIT_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The circuit-without-growing-the-trail template — recur.
    SubplotTemplate("""\
{patient_fox_phrase} walked a circuit around the orchard {place},
each lap returning to the start with a slightly different tally in
hand. "Recur is this circuit," {patient_fox_he_she} said: "back to
the head of the row with new bindings, no extra trail laid down
behind us." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — looping
without growing the call-stack — returned the final value."""),

    # 2. The base-case template — termination.
    SubplotTemplate("""\
"Every circuit has a stopping condition," {patient_fox_phrase}
said. "Without one, the runner walks forever around the row. With
one, the runner knows when the laps are done and the tally is the
answer." To {goal_text}, {patient_fox_he_she_cap} composed
{concept_phrase}, submitted the form, and the REPL — looping until
the base case — returned the value the final lap produced."""),

    # 3. The hasty-fox-distrusts-the-circuit template — Hare equivalent.
    SubplotTemplate("""\
{hasty_fox_phrase}, {emo_proud}, distrusted the very idea of a
circuit: surely {hasty_fox_he_she}'d just walk forever? {patient_fox_phrase}
smiled patiently — the base case is the runner's compass. To
{goal_text}, {patient_fox_he_she} composed {concept_phrase},
submitted the form, and the REPL — looping the right number of
times, then stopping — returned the value cleanly."""),

    # 4. The lap-with-new-tally template — each pass updates bindings.
    SubplotTemplate("""\
"Each lap around the row changes what you carry," {patient_fox_phrase}
said. "You start with one tally, walk the row, collect more — then
recur back to the start with the new tally in hand. No stack grows;
you just go back to the head with fresh bindings." To {goal_text},
{patient_fox_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — lapping the circuit with new bindings each
time — returned the final answer."""),

    # 5. The circuit-ends-at-the-goal template — when to stop looping.
    SubplotTemplate("""\
"The trick to the circuit is knowing when to stop," {patient_fox_phrase}
said. "You walk the row, update your tally. If a condition says stop,
you hand back the final tally. If not, you recur — back to the row's
head with new bindings, no extra trail." To {goal_text},
{patient_fox_he_she_cap} composed {concept_phrase}, submitted the
form, and the REPL — checking the base case each lap — returned the
answer when the row's circuit was finally done."""),
]
