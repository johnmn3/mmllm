"""Metaphor-bearing subplot pools for crow-pitcher.

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
- the metaphor is concretely named in every template (wing-cache /
  drop-order / stone-pile / sorting-perch / water-tally / stone-count)
  so it lands as imagery, not as decoration.
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import SubplotTemplate


# ─────────────────────── wing-cache (let) ─────────────────────────


_POUCH_SUBPLOTS: list[SubplotTemplate] = [

    # 1. Clever crow tucks the value under one wing; the wing holds
    #    only for the form's stretch.
    SubplotTemplate("""\
{clever_phrase} reached up and tucked the value under one wing,
holding it for the form's reach alone. "When I want to {goal_text},"
{clever_he_she} said, "I tuck the value under a wing and carry it
just for the stretch of the form where I need it. After the drop,
the wing opens again." {clever_he_she_cap} composed {concept_phrase},
the binding held under a wing, and submitted the form to the
REPL. {hasty_phrase}, {emo_proud}, had already forgotten what was
tucked there — but the form, which still carried it, came back
with the answer."""),

    # 2. Wing-cache holds only within the form's reach; whatever's
    #    tucked is in force only while the form runs. Type-neutral
    #    framing of the same temporary-binding idea.
    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, patted the feathers of one wing.
"Whatever I tuck under a wing is in force only while the form runs,"
{clever_he_she} said, "and only for the form that names the binding.
The wing is narrow — it holds only what fits inside the form's
stretch. Step past the form's edge and the wing opens; the value
existed only inside the form's reach." To {goal_text},
{clever_he_she} composed {concept_phrase} with the binding held under
a wing for that stretch. The REPL read out the
value the wing had held."""),

    # 3. Hasty crow ignores the wing; Clever crow's form-work wins.
    SubplotTemplate("""\
{hasty_phrase} called out guesses at the pitcher {place}, {emo_proud},
without bothering to tuck a value under a wing like
{clever_phrase} did. But the wing-cache was where the answer
lived: {clever_he_she_cap} intended to {goal_text}, and the
value was tucked away under the wing for exactly that form's stretch.
{clever} composed {concept_phrase}. The REPL —
reaching under the wing as the form told it to — handed back the value
{hasty} had not even thought to cache."""),

    # 4. Substitution rule — wherever the form names the binding,
    #    the runtime reaches under the wing.
    SubplotTemplate("""\
"Wherever the form names the binding," {clever_phrase} explained,
{emo_patient}, "the REPL reaches under the wing and pulls out what
was tucked there." {clever_he_she_cap} demonstrated by intending
to {goal_text}: each mention of the bound name, {clever} said, would
be replaced by the value from under the wing the moment the form
ran — the wing's hold steady through every reference. {clever_phrase}
composed {concept_phrase}. The REPL substituted as promised — the wing-cache's value threaded into every
place the binding had been named."""),

    # 5. End-of-drop — the wing opens when the form's stretch is over.
    #    (Scope ends.)
    SubplotTemplate("""\
"Watch the wing carefully," {clever_phrase} said {place}.
"While the form's stretch runs, the wing is closed and
the binding is safe." To {goal_text}, {clever_he_she}
composed {concept_phrase} with the binding tucked safely under a wing,
then submitted the form. The REPL returned the value, and the
wing — its work done — opened again. {hasty_phrase}, {emo_tired},
finally admitted that the patient wing-cache had carried the
day."""),
]


# ─────────────────────── talon-scratched drop-order (fn) ─────────────────────────


_RECIPE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. Clever crow scratches the drop-order on the pitcher's rim;
    #    any crow can follow it. Type-neutral — works for named,
    #    anonymous, multi-arg, etc. The {goal_text}/{concept_phrase}
    #    say which kind.
    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, held up a smooth stone and scratched
a step-by-step sequence into the pitcher's clay rim. "Drop-orders in
Clojure are like this," {clever_he_she} said: "the smooth stones go
at the head, the drops in order, and the last drop is what raises
the water to beak-reach. The pitcher is narrow — every step
must fit, none can be skipped." To {goal_text}, {clever_he_she}
scratched out {concept_phrase} on the rim, submitted the form, and
the REPL followed the drop-order and handed back the value the last
drop had raised."""),

    # 2. The drop-order as a runnable sequence — emphasizes the call site.
    SubplotTemplate("""\
"A drop-order is only useful when followed," {clever_phrase}, {emo_patient}, said,
holding up the scratched rim. "You scratch the steps, you bring the
stones, the pitcher raises the water the rest." To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the
form, and the REPL — taking the drop-order and the stones —
handed back what the drops had raised."""),

    # 3. Last drop is what raises the water to beak-reach. (Body returns last form;
    #    type-neutral and pedagogically true for all fn bodies.)
    SubplotTemplate("""\
"In any drop-order," {clever_phrase}, {emo_patient}, explained, "the last drop is
what raises the water to your beak." {clever_he_she_cap} took the goal — to
{goal_text} — and scratched the drop-sequence in order, knowing
that whatever the final drop achieved was what the water's level
would carry back. {clever} composed {concept_phrase}, submitted
the form, and the REPL — discarding the earlier drops' work —
handed back only the rise from the last."""),

    # 4. Drop-orders feeding into drop-orders — emphasizes the chained
    #    nature when relevant. Type-neutral phrasing: the chain is
    #    described as something that *can* happen, not as something
    #    the form is necessarily doing.
    SubplotTemplate("""\
"Drop-orders can feed into one another," {clever_phrase}, {emo_patient}, said,
scratching several sequences on the pitcher's sides. "What one drop-order
raises, the next can take as its starting height — together they make a longer
sequence." To {goal_text}, {clever_he_she} composed
{concept_phrase}. The REPL — walking
through the drop-order in sequence — handed back the value at the
end."""),

    # 5. The Hasty-skips-the-order template — Hasty crow guesses,
    #    Clever crow scratches the order. Generic fable beat.
    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, insisted {hasty_he_she} could just
call out how much the water would rise rather than bother scratching
a drop-order. {clever_phrase} only smiled and reached for a talon.
To {goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL — running the drop-order drop
by drop — handed back the value {hasty} had been guessing
at."""),
]


# ─────────────────────── stone-pile on the rim (collections) ───────────────


_BASKET_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The stone-pile-on-the-rim template — generic; whatever the
    #    operation, the pile stays as it was, the form returns
    #    the new arrangement.
    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, pointed to a pile of smooth stones
gathered on the pitcher's rim {place}. The stones were heavy — one
at a time was the only way. "Whatever I want to do with the stones,"
{clever_he_she} said, "I read from the pile, work the change, and
the pile itself stays as it was — what I get back is a fresh
arrangement." To {goal_text}, {clever_he_she} composed
{concept_phrase}. The REPL handle the
stone-pile exactly as the operation prescribed."""),

    # 2. The sorted-and-tagged-stones template — works for tagged
    #    collections (maps), positional rows (vectors), or kind-only
    #    piles (sets). The narrative is generic; goal_text says which.
    SubplotTemplate("""\
"You can find what you want in a stone-pile several ways,"
{clever_phrase} said, {emo_patient}, gesturing at the gathered
stones: "by the mark scratched on it, by its place in line, or by
simply asking whether it's there at all. The pile is heavy; one
right reach saves a dozen wrong ones." To {goal_text},
{clever_he_she} wrote {concept_phrase} for the stone-pile, submitted
the form, and the REPL applied the lookup or update exactly as the
form directed."""),

    # 3. The procession-of-stones template — for ordered collections
    #    (vectors, lists, seqs). Sub-template is more
    #    vector-leaning but doesn't claim a specific type.
    SubplotTemplate("""\
A line of smooth stones had been arranged {place}, each one resting
against the next — first at the front, the rest in order behind.
"Many of our stone-piles are like this procession,"
{clever_phrase}, {emo_patient}, said. "You can grab the first, you can ask for
the rest, you can put a new stone at the front of the line."
To {goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL marched the procession exactly
as the form described."""),

    # 4. The new-pile-from-old template — immutability emphasis;
    #    works for any collection type.
    SubplotTemplate("""\
"Watch carefully," {clever_phrase} said, gesturing at the
original pile. "Whatever I do to it, this one sits unchanged
on the rim — what I get back is a fresh pile with the change
made, leaving the first one exactly where it was." To
{goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL returned a new arrangement
while the original waited, untouched. {hasty_phrase}, {emo_tired},
was beginning to see why nothing could be lost by dropping."""),

    # 5. The Hasty-scatters-the-pile template — Hasty crow guesses by
    #    scattering; Clever crow's careful stone-work wins. Generic
    #    fable beat that fits any collection operation.
    SubplotTemplate("""\
{hasty_phrase} began scattering the stone-pile, {emo_proud}, calling
out guesses about which stones were there without quite checking. "I know
exactly what's in the pile," {hasty_he_she} insisted. {clever_phrase}
shook {clever_his_her} head. To {goal_text} properly,
{clever_he_she} composed {concept_phrase} carefully on the rim,
submitted the form, and the REPL — looking at the pile the
way the form told it to — handed back the answer
{hasty} had been guessing at."""),
]


# ─────────────────────── water-tally scratch (atom/ref) ────────


_NOTEBOOK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. Water-tally scratched on the pitcher; any crow can read or
    #    atomically update.
    SubplotTemplate("""\
A tally of scratches lay etched into the pitcher's clay face in the
middle of the thirsty meadow — the water rising drop by drop with
each careful mark. Any crow could walk up, read the marks, or —
carefully — scratch a new one. "Atoms are like this water-tally,"
{clever_phrase} said, {emo_patient}: "you can read the marks to see
the level; you can scratch a new mark atomically, no matter who else
is watching." To {goal_text}, {clever_he_she} composed
{concept_phrase}. The REPL work the
tally exactly as the form prescribed."""),

    # 2. Atomic scratch — read, apply, mark, all in one motion.
    SubplotTemplate("""\
"When I want to update the tally," {clever_phrase} said,
{emo_patient}, "I don't look away and scratch elsewhere — I read the
marks, apply the change, and scratch the new count, all in a single
motion. The pitcher is narrow; two scratches at once would smear the
count. If two crows arrive at once, the runtime makes sure only one
of us completes the scratch at a time." To {goal_text},
{clever_he_she} composed {concept_phrase} for the tally, submitted
the form, and the REPL applied the update atomically."""),

    # 3. The tally-and-the-quiet-pitcher — emphasizes the
    #    persistence of the marks between updates.
    SubplotTemplate("""\
"The tally stays put on the pitcher," {clever_phrase}, {emo_patient}, said,
"so any crow who comes by can read what's marked right
now. The marks change only when someone scratches — and only as the
runtime allows." To {goal_text}, {clever_he_she} composed
{concept_phrase}. The REPL — reading
or scratching the tally as the form prescribed — handed back the
value the mark had carried."""),

    # 4. The shared-state template — generic emphasis that this is
    #    about coordinated updates among several crows.
    SubplotTemplate("""\
"Many crows can come and go past the pitcher," {clever_phrase}, {emo_patient}, said, "and each one's read or scratch must agree with the others.
The runtime sees to that — no two crows scratch over each other's
marks." To {goal_text}, {clever_he_she} composed
{concept_phrase}. The REPL — coordinating
each mark cleanly — handed back what the tally now said."""),

    # 5. The Hasty-scratches-wildly template — Hasty crow tries to
    #    claw the tally; Clever crow marks carefully. Generic fable
    #    beat applicable to any state operation.
    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, swiped at the tally on the pitcher,
trying to claw a new count over the marks. {clever_phrase}
stopped {hasty_him_her} firmly: tallies shared by all the meadow
need careful scratches, not claws. To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the form,
and the REPL — applying the update the runtime's careful way —
handed back the value the tally now held."""),
]


# ─────────────────────── sorting-perch (map/filter/HOFs) ────────


_SIEVE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The general sorting-perch — works for transform (map),
    #    select (filter), select-counted (take/drop), or dedupe
    #    (distinct). The rule held at the perch's edge
    #    decides what happens to each stone.
    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, perched at the pitcher's edge,
holding a decision-rule over the stones {place}. The pile was
heavy and the rim was high; the rule let the wrong stones fall
away before they could weigh the climb. "Whatever rule I hold here,"
{clever_he_she} said, "each stone passes under my eye one at a time:
some are changed, some kept, some set aside, depending on the rule."
To {goal_text}, {clever_he_she} composed {concept_phrase} as the
rule, sorted the pile through. The REPL returned what the rule had let drop."""),

    # 2. The sort-and-drop template — generic emphasis
    #    on the new-pile-out-the-other-side metaphor.
    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, held each stone over the pitcher's mouth. "The
stones go under my eye at the top," {clever_he_she} said, "and
the sorting-perch does its work — applying the rule, choosing or changing —
and what lands in the pitcher below is the result." To
{goal_text}, {clever_he_she} composed {concept_phrase},
sorted the input through. The REPL collected what fell into the waiting pitcher."""),

    # 3. Stacked rules — output of one feeds the next.
    #    (comp xform.)
    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, held two decision-rules at the perch, one after the
other, each rule filtering the stones that the first had passed. "What lands at the
bottom," {clever_he_she} said, "has been through both rules in
order — applied as a single combined sort." To {goal_text},
{clever_he_she} composed {concept_phrase} as a stack of
rules, sorted the input through, submitted the form, and the
REPL caught what the stack let drop."""),

    # 4. The receiver template — drop into any kind of pile.
    #    (into / into with xform.)
    SubplotTemplate("""\
"You can sort the result into any kind of pile you like,"
{clever_phrase}, {emo_patient}, said. "A line of stones, a set of unique ones,
a gathered heap of any shape — the sorting-perch doesn't care;
the destination does." To {goal_text}, {clever_he_she} composed
{concept_phrase}, chose the right empty destination, sorted
through the rule. The REPL packed the
result into the pile of {clever_his_her} choosing."""),

    # 5. The Hasty-tries-to-shortcut-the-rule template — Hasty
    #    crow guesses, Clever crow sorts through carefully. Generic
    #    fable beat applicable to any sorting operation.
    SubplotTemplate("""\
{hasty_phrase} eyed the pile, {emo_proud}, and called out a
guess about what would come out after the sorting
without bothering to actually hold the rule and sort. {clever_phrase} shook
{clever_his_her} head and went on with the work: to
{goal_text}, {clever_he_she} composed {concept_phrase} as
the sorting rule, held each stone over the pitcher carefully,
submitted the form, and the REPL returned the only answer
that would do — the one the sorting had actually produced."""),
]


# ─────────────────────── stone-count (numbers) ───────────────────


_ACORN_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The counting-stones template — generic arithmetic frame.
    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, laid smooth stones out on the ground
{place}, sorting them into small heaps by how many drops each would
take. The water sat low in the pitcher; every count had to be exact
or the rise would fall short. "Numbers in Clojure are just like
stones in heaps," {clever_he_she} said: "you can count them, you
can add two heaps together, you can divide one heap among several
drops." To {goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and let the REPL hand back the running count —
exactly what the heap, dropped pebble by pebble, would have raised."""),

    # 2. The heap-grows-or-shrinks template — for inc/dec, +/-.
    SubplotTemplate("""\
"Watch the heap," {clever_phrase}, {emo_patient}, said, gesturing at a small
mound of smooth stones. "Every operation either adds more stones,
takes some away, or combines what's already there — the heap grows or shrinks by
exactly what you say." To {goal_text}, {clever_he_she}
composed {concept_phrase}. The REPL returned the new count, the heap settled into its new
arrangement."""),

    # 3. The careful-arrangement template — generic; the operation
    #    is whatever the form says, but the Clever crow's care with the
    #    stones is what the metaphor carries.
    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, arranged a small heap of smooth
stones {place}, careful with the count. The day was hot and the
water was low; the heap had to rise enough to drink, no fudging
allowed. "Numbers in Clojure don't fudge," {clever_he_she} said.
"Whatever you do — adding, subtracting, dividing stones into smaller
heaps with leftovers, comparing two piles — the runtime gets it
exactly right, every time." To {goal_text}, {clever_he_she}
composed {concept_phrase}. The REPL handed
back the precise count — the heap counted as carefully as the day's
heat would let the crow count it."""),

    # 4. The Hasty-counts-aloud template — Hasty crow guesses by sight,
    #    Clever crow counts.
    SubplotTemplate("""\
{hasty_phrase} eyed the heap, {emo_proud}, and called out a guess
about how many stones could be dropped before the water rose high
enough, without bothering to count. {clever_phrase} simply began
counting carefully — to {goal_text} required no eyeballing, only
the form. {clever_he_she_cap} composed {concept_phrase}, submitted
it to the REPL, and the runtime read off the exact tally the form
computed, settling the matter the patient way."""),

    # 5. The exact-count template — generic; emphasizes that the
    #    REPL gives the exact number, no matter the operation.
    SubplotTemplate("""\
"Whatever the heap looks like after the operation,"
{clever_phrase}, {emo_patient}, said, "the runtime gives the exact count —
small or large, fraction or whole, the answer is precise." To
{goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL handed back the value, exactly
as the operation had produced it."""),
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
# of its connective prose around the {concept_phrase} action — wing-cache
# is "tucked into the wing", drop-order is "scratched on the rim",
# stone-pile is "for the pile", sorting-perch is "as the rule",
# water-tally is "for the tally", stone-count is "counted out", etc.
# The slots provide the specifics.


def _story(connective_prose: str) -> SubplotTemplate:
    """Build a story-scaffold template for a family.

    The template is the canonical 5-act story shape; the family
    differentiates itself only by the {connective_prose} around the
    composed/submitted action — using the family's verb (compose /
    scratch / sort / scratch / count / etc.) and its imagery vocabulary.
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
        "To {goal_text}, {clever_he_she} composed {concept_phrase} "
        "with the binding tucked safely under a wing and submitted the "
        "form. The REPL reached under the wing as the form directed:"
    ),
]

_RECIPE_SUBPLOTS = _RECIPE_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} scratched out {concept_phrase} "
        "on the rim and submitted the form. The REPL followed the drop-order "
        "end to end:"
    ),
]

_BASKET_SUBPLOTS = _BASKET_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} composed {concept_phrase} "
        "for the stone-pile and submitted the form. The REPL handed back the "
        "arrangement:"
    ),
]

_NOTEBOOK_SUBPLOTS = _NOTEBOOK_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} composed {concept_phrase} "
        "for the water-tally and submitted the form. The REPL scratched the "
        "mark on the pitcher:"
    ),
]

_SIEVE_SUBPLOTS = _SIEVE_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} composed {concept_phrase} "
        "as the sorting rule, held the stones over, and submitted "
        "the form. The REPL caught what landed below:"
    ),
]

_ACORN_SUBPLOTS = _ACORN_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL counted out the answer:"
    ),
]


# ─────────────────────── dual-gate check (and/or/not/boolean) ────────────

_GATE_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, paused at the pitcher's rim {place}, talon raised. The throat was
narrow; the day was hot.
"Boolean forms in Clojure are like a dual-gate check at the pitcher's
mouth," {clever_he_she} said. "The runtime checks the value and the
gate swings open or closed — what comes back is the gate's verdict;
a narrow throat punishes any latch that lifts on a wrong guess." To
{goal_text}, {clever_he_she} composed {concept_phrase}, submitted
the form, and the REPL returned whatever the gate had decided."""),

    SubplotTemplate("""\
"Only two things close the gate," {clever_phrase}, {emo_patient}, said, perched on
the pitcher's rim. "nil and false — everything else, even an empty
string or a zero, opens it. The gate's rule is that simple." To
{goal_text}, {clever_he_she} composed {concept_phrase}, submitted
the form, and the REPL returned the value the gate had passed."""),

    SubplotTemplate("""\
"You can't tell which way the gate will swing by guessing,"
{clever_phrase}, {emo_patient}, said. "You bring the form to the gate, the runtime
checks it, and the gate gives the only answer that matters." To
{goal_text}, {clever_he_she} composed {concept_phrase}, submitted
the form, and the REPL settled the matter — the gate had swung exactly
as the rule said."""),

    SubplotTemplate("""\
{hasty_phrase} swooped toward the pitcher {place}, {emo_proud}, certain
the gate would swing open. {clever_phrase} watched: the only way to know
which way the gate swings is to bring the value to it. To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the form, and the
REPL settled the matter — the gate had swung exactly as the rules said,
regardless of {hasty}'s guess."""),

    SubplotTemplate("""\
"The gate carries the value through, not just a yes or a no,"
{clever_phrase}, {emo_patient}, said. "Whatever the gate's verdict, that's what the
runtime hands back — sometimes a strict true or false, sometimes the
very value that passed the test." To {goal_text}, {clever_he_she}
composed {concept_phrase}. The REPL returned
the value the gate had carried through."""),
]

_GATE_SUBPLOTS = _GATE_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} composed {concept_phrase} "
        "and held it at the dual-gate check. The REPL opened or closed "
        "the gates as the logic demanded:"
    ),
]


# ─────────────────────── branch-choice above the pitcher (if/cond/case) ──

_FORK_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, perched above the pitcher's mouth {place}, head tilted
one way, then the other. "Branching forms in Clojure are like this
choice above the pitcher," {clever_he_she} said. "The runtime checks
the condition, takes the matching path, and only that path's value comes
back." To {goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL — having taken the right path —
handed back its value."""),

    SubplotTemplate("""\
"The path not taken doesn't run at all," {clever_phrase}, {emo_patient}, said,
still perched above the pitcher. "The runtime checks the condition,
walks the right path, and the unrun path is just left behind." To
{goal_text}, {clever_he_she} composed {concept_phrase}, submitted
the form, and the REPL — running only what was needed — handed back
the value of the chosen path."""),

    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, spread {clever_his_her} wings {place},
one side for yes, one side for no. The day was hot and the wrong
wing meant another long flight back, so the condition had to be
read carefully. "At each branching point," {clever_he_she} said,
"the condition is what decides — not the crow's preference. Whatever
the condition evaluates to, that decides the wing to take." To
{goal_text}, {clever_he_she} composed {concept_phrase}, submitted
the form, and the REPL — letting the condition decide — handed back
the value of the branch it had taken."""),

    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, called out which path {hasty_he_she} was
sure the runtime would take, without bothering to check the condition.
{clever_phrase} only smiled: the only way to know is to evaluate the
condition. To {goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL — checking the condition properly —
returned the value of the path the form actually ran."""),

    SubplotTemplate("""\
"It isn't the crow who picks the path," {clever_phrase}, {emo_patient}, said,
"it's the condition. Whatever the condition evaluates to, that
decides." To {goal_text}, {clever_he_she} composed
{concept_phrase}. The REPL — letting the
condition decide — handed back the value of the path the condition
had pointed at."""),
]

_FORK_SUBPLOTS = _FORK_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL took the right path:"
    ),
]


# ─────────────────────── rim-carving (def/namespace/require) ────────────

_ROADSIGN_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, pressed a talon-tip into the
pitcher's clay rim {place}, carving a name with care. The clay was
soft only briefly; once dry, the carving would last for every later
crow. "A def is a carving in the rim," {clever_he_she} said.
"Anyone who perches here reads the name, learns the value, and can
call it by name alone from here on." To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the form, and
the REPL — carving the name — bound it to its value for any later
retrieval."""),

    SubplotTemplate("""\
"The good thing about a rim-carving," {clever_phrase}, {emo_patient}, said, "is that
it stays where you scratched it. The next crow who perches reads what's
there now — whatever the latest talon-stroke says." To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the form, and
the REPL — reading the carvings as the form directed — returned the
value the pitcher's rim had recorded."""),

    SubplotTemplate("""\
A collection of flat stones stood {place}, each scratched with names
and values. The day was hot and the search was long; reading the
right stone first saved a dozen useless lifts. "Names live on these
stones," {clever_phrase} said, {emo_patient}: "to use a name carved
on another stone, you make sure that stone is placed where the
runtime can find it." To {goal_text}, {clever_he_she} composed
{concept_phrase}. The REPL — finding the
right name on the right stone — returned the value the form had
asked for."""),

    SubplotTemplate("""\
"Naming is half the art," {clever_phrase}, {emo_patient}, said, scoring a careful mark
into the pitcher's clay. "A clear carving tells every later crow what to
expect; a careless one trips them up." To {goal_text},
{clever_he_she} composed {concept_phrase} with the right name in
mind. The REPL — reading the name exactly —
returned the value the carving had promised."""),

    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, glanced at the rim-carving {place} and
called out what {hasty_he_she} thought it said without stopping to
read carefully. The day was hot and the throat was narrow — a
mis-read symbol cost a wasted pebble. {clever_phrase}, {emo_patient},
stopped and read each scratch precisely. To {goal_text}, the carving
had to be read exactly: {clever_he_she} composed
{concept_phrase}. The REPL — reading literally —
returned the right value."""),
]

_ROADSIGN_SUBPLOTS = _ROADSIGN_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL read the rim-carvings and replied:"
    ),
]


# ─────────────────────── soft-moss test-drop (try/catch/throw) ──────────

_SAFETYNET_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, spread a patch of soft moss
beneath the pitcher {place} — the day was hot, the throat was narrow, and any
pebble flung wrong without a cushion would chip the rim and waste the
work. "If a stone goes wrong — if the form fails — the moss catches
it safely," {clever_he_she} said. "The pitcher's water level doesn't
drop; you try a different stone." To {goal_text}, {clever_he_she}
composed {concept_phrase}. The REPL — moss
in place — caught any trouble and returned the value the recovery
path had specified."""),

    SubplotTemplate("""\
"This patch of moss is the practice area," {clever_phrase}, {emo_patient}, said {place}.
"A stumble here costs nothing. Drop the form, see what comes back, fix
the stone, try again. The REPL is forgiving in a way the deep water
never is." To {goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL returned the value — even if the stone
had been close to a mis-drop."""),

    SubplotTemplate("""\
"What matters when a stone goes wrong," {clever_phrase}, {emo_patient}, said, "is that
the drop can continue — the runtime catches the slip, takes the recovery
path, and the water level comes back even when something inside the form
went off." To {goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL — handling the slip cleanly — returned
the value the recovery path had produced."""),

    SubplotTemplate("""\
"There's a discipline to dropping safely," {clever_phrase}, {emo_patient}, said, "and
it starts with the moss — making sure the form does what it claims,
catching what could go wrong before it does." To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the form, and
the REPL — applying whatever check or catch the form had asked for —
returned the value the discipline had earned."""),

    SubplotTemplate("""\
{hasty_phrase} eyed the pitcher {place}, {emo_proud}, certain {hasty_he_she}
could drop the stone without the moss patch. {clever_phrase} spread the
moss carefully: a failed form without a catch leaves the pitcher in an
unknown state. To {goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL — moss in place — caught anything that
fell and returned the answer the safety design had earned."""),
]

_SAFETYNET_SUBPLOTS = _SAFETYNET_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL — moss in place — handled any "
        "slip and returned:"
    ),
]


# ─────────────────────── talon-inscribed flat stone (IO/metadata) ────────

_SCROLL_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, picked up a smooth flat stone {place}
and pressed the talon-tip in. The stone was cool against the day's
heat, and the scratch would last long after the bird had flown.
"The flat stone is how the pitcher's world and the outside world
meet," {clever_he_she} said: "you scratch what you want to keep, any
crow who alights later reads what's there." To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the form, and
the REPL handed back what the stone had said, or committed what the
scratching had written."""),

    SubplotTemplate("""\
"Scratching and reading flat stones is just like composing and evaluating
forms," {clever_phrase}, {emo_patient}, said. "You ask the runtime for what's on the stone,
you scratch what you want recorded, and the work goes both ways through
one talon-tip." To {goal_text}, {clever_he_she} composed
{concept_phrase}. The REPL handed back what the
stone had held."""),

    SubplotTemplate("""\
"The world outside the pitcher is bigger than the pitcher,"
{clever_phrase}, {emo_patient}, said, "and a flat stone out there has its own
discipline — scratch it carefully, handle it with care, close the
inscription when you're done." To {goal_text}, {clever_he_she}
composed {concept_phrase}. The REPL —
handling the stone with care — returned the value the work had
produced."""),

    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, claimed the flat stone said exactly what
{hasty_he_she} expected and didn't bother to actually read it. {clever_phrase}
pressed the talon carefully and read each scratch. To {goal_text} required the
stone's actual content — {clever_he_she} composed {concept_phrase}, submitted
the form, and the REPL — reading the stone faithfully — returned the value the
inscription had held."""),

    SubplotTemplate("""\
"There's the world inside the pitcher," {clever_phrase}, {emo_patient}, said, "and the
world outside it. Flat stones are how the two meet — a value crosses out
and becomes scratches on stone, or scratches on stone cross in and become
a value again." To {goal_text}, {clever_he_she} composed
{concept_phrase}. The REPL — bridging the two
worlds — handed back the value the work had carried."""),
]

_SCROLL_SUBPLOTS = _SCROLL_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL — talon pressed to stone — "
        "completed the inscription:"
    ),
]


# ─────────────────────── any-crow-can-drop (protocols/extend) ────────────

_GUILD_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, scratched a small sign into the
pitcher's rim {place}: "Stone-Drop Guild — any crow may join." The
day was hot and the pitchers were many; one shared call would save
every crow from arguing how. "A protocol is a guild," {clever_he_she}
said. "It lists what every member must be able to do — the methods.
Any crow who can fulfil the stone-drop call may claim membership."
To {goal_text}, {clever_he_she} composed {concept_phrase}, submitted
the form, and the REPL — guild scratched — handed back the guild's
record."""),

    SubplotTemplate("""\
"What makes a guild useful," {clever_phrase}, {emo_patient}, said, "is that the call
is the same for every member, but each crow answers in its own way. The
runtime looks up which crow is present, then runs that crow's answer."
To {goal_text}, {clever_he_she} composed {concept_phrase}, submitted
the form, and the REPL — dispatching to the right crow — returned the
crow-specific value."""),

    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, held up the guild ledger {place}.
The day's pitcher was narrow and the drop-orders many; the ledger
was what kept each crow from sounding the wrong call. "Membership
is in this scratching," {clever_he_she} said: "the crow, the drops
they swear they can perform, and the actual answer each crow gives.
The runtime reads from this ledger whenever the call goes out." To
{goal_text}, {clever_he_she} composed {concept_phrase}, submitted
the form, and the REPL — checking the ledger as it ran — returned
the right answer."""),

    SubplotTemplate("""\
"Each guild has its own boundaries," {clever_phrase}, {emo_patient}, said. "Belonging to
the stone-drop guild doesn't mean belonging to the inscription guild —
the runtime checks each separately, and only the right guild's answer
comes back." To {goal_text}, {clever_he_she} composed
{concept_phrase}. The REPL — respecting which
guild was being called — returned the right value."""),

    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, declared that {hasty_he_she} could of course
answer the guild's call — even without having scratched the ledger.
{clever_phrase} only raised a talon toward the ledger: only a member
whose name was scratched there could answer. To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the form, and the
REPL — checking the ledger first — returned the right answer based on
who had actually been recorded."""),
]

_GUILD_SUBPLOTS = _GUILD_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL — checking the guild ledger — "
        "dispatched cleanly:"
    ),
]


# ─────────────────────── shape-sorting rim (multimethods) ────────────────

_SORTINGTABLE_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
The pitcher's rim had a sorting lip carved into it {place}, with several
chutes branching off. "The shape-sorting rim is like defmulti,"
{clever_phrase}, {emo_patient}, said. "You decide what mark on the stone to look at; the
rim routes each stone down the matching chute." To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the form, and
the REPL — reading the stone's mark, picking the chute — returned the
value the right chute had produced."""),

    SubplotTemplate("""\
"To add a chute to the shape-sorting rim," {clever_phrase}, {emo_patient}, said, "you
say what mark the chute handles and what happens when a stone with that
mark arrives." To {goal_text}, {clever_he_she} composed
{concept_phrase} for the right chute. The REPL —
adding the chute, routing the stone — returned the chute-specific
value."""),

    SubplotTemplate("""\
"What the rim sorts by is up to you," {clever_phrase}, {emo_patient}, said. "You decide
what to look at on each stone — a scratch, a shape, a color, anything.
The runtime reads it, finds the matching chute, and runs that one." To
{goal_text}, {clever_he_she} composed {concept_phrase}, submitted the
form, and the REPL — reading the mark the dispatch function produced —
returned the value the right chute had given."""),

    SubplotTemplate("""\
"The good thing about a shape-sorting rim," {clever_phrase}, {emo_patient}, said, "is
that you can keep adding new chutes whenever a new kind of stone shows up.
The original rim doesn't change; the runtime just learns one more route."
To {goal_text}, {clever_he_she} composed {concept_phrase}, submitted
the form, and the REPL — routing through the rim cleanly — returned the
right value."""),

    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, dropped a stone into the shape-sorting rim
without checking what mark it carried. {clever_phrase} pointed at the
lip: every stone must show the mark the rim sorts by. To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the form, and the
REPL — reading the mark first, routing second — returned the value from
the correct chute."""),
]

_SORTINGTABLE_SUBPLOTS = _SORTINGTABLE_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} composed {concept_phrase} "
        "and set it at the shape-sorting rim. The REPL read the mark "
        "and routed as directed:"
    ),
]


# ─────────────────────── custom-stitched stone-pouch (deftype/defrecord) ─

_CARRYINGCASE_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, held up a small pouch of bark and vine {place}, its inside
divided into labeled slots by careful stitching. "Defrecord makes a pouch
like this," {clever_he_she} said: "named slots holding specific stones; a
knot on the outside saying what kind of pouch it is." To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the form, and
the REPL — stitching the pouch, filling its slots — returned the value
the pouch held."""),

    SubplotTemplate("""\
"A deftype is a barer pouch," {clever_phrase}, {emo_patient}, said. "Slots, a knot — no
map-like behavior unless you ask for it. Lighter, more focused." To
{goal_text}, {clever_he_she} composed {concept_phrase}, submitted the
form, and the REPL — stitching the bare pouch as specified — returned the
value inside."""),

    SubplotTemplate("""\
"To reach into a labeled slot," {clever_phrase}, {emo_patient}, said, "you ask for it by
name. The pouch knows where each slot is; the runtime pulls from it
cleanly." To {goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL — opening the right slot — returned
exactly what was inside."""),
]

_CARRYINGCASE_SUBPLOTS = _CARRYINGCASE_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} stitched {concept_phrase} "
        "into the stone-pouch and submitted the form. The REPL pulled from "
        "the slots as the form prescribed:"
    ),
]


# ─────────────────────── borrowed earthenware pitcher (host interop) ─────

_TOOLSHED_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, found a different pitcher {place} — one
made by a human potter, not fired by any crow, its throat narrow and
its rim cool to the touch. "This isn't our clay," {clever_he_she}
said, "but we can call its methods directly: dot-prefix on the vessel,
or slash for what the potter made standard-issue. A foreign vessel is
a host bridge — pebbles drop the same way, but the rim is unfamiliar."
To {goal_text}, {clever_he_she} composed {concept_phrase}, submitted
the form, and the REPL — calling into the foreign vessel — handed back
what its method had returned."""),

    SubplotTemplate("""\
"Each vessel from the human potters has its own label," {clever_phrase}, {emo_patient}, said, "and the right way to call it depends on which kind of vessel it is
— some held by a crow, some standard-issue from the potter's hand." To
{goal_text}, {clever_he_she} composed {concept_phrase} using the
right calling convention. The REPL — invoking
the host vessel's method by its label — returned the value the human had
crafted."""),

    SubplotTemplate("""\
"Foreign pitchers work, but they need careful handling," {clever_phrase}, {emo_patient}, said. "Their labels are different, their calling conventions are different,
and the runtime has to bridge between the crow's world and the human's
every time." To {goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL — making the bridge cleanly — handed back
the value the foreign pitcher had produced."""),

    SubplotTemplate("""\
"There's the meadow's own pitcher," {clever_phrase}, {emo_patient}, said, "and there's
the human's vessel. The runtime moves a stone across the boundary, calls
the human's method, and brings the result back into the meadow." To
{goal_text}, {clever_he_she} composed {concept_phrase}, submitted the
form, and the REPL — bridging the two worlds — returned the value
cleanly."""),

    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, grabbed at the human's vessel without
checking which method was which. The wrong method rattled back an error.
{clever_phrase} shook {clever_his_her} head: to {goal_text} required
reading the vessel's labels carefully. {clever_he_she_cap} composed
{concept_phrase}. The REPL — calling the right
host method by name — returned the value cleanly."""),
]

_TOOLSHED_SUBPLOTS = _TOOLSHED_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL — calling into the earthenware "
        "vessel the human had fired — returned:"
    ),
]


# ─────────────────────── scout-crow sent ahead (agent/future/promise) ────

_RUNNERAHEAD_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, dispatched a scout-crow down the far
end of the meadow {place}, task in beak. The day was hot and the
pitcher's water still low; sending the scout meant the dropping
could continue here while the count rose elsewhere. "The scout goes
ahead while we keep dropping here," {clever_he_she} said, "and when
we need the count we signal the scout to fly back with the tally."
To {goal_text}, {clever_he_she} composed {concept_phrase}, submitted
the form, and the REPL — sending the scout, fetching the count later
— returned the value when the scout was ready."""),

    SubplotTemplate("""\
"Once you've sent the scout ahead," {clever_phrase}, {emo_patient}, said, "you keep on
dropping here. The count will be there when you signal for it —
sometimes you wait for the scout to finish; other times you keep
dropping until the scout returns." To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the form, and
the REPL — coordinating the scout the way the form prescribed — returned
the value when it was ready."""),

    SubplotTemplate("""\
"The hard part isn't sending the scout," {clever_phrase}, {emo_patient}, said. "The hard
part is being patient enough to wait for the count when it comes — not
reaching for it too early, not giving up too soon. The runtime makes that
easier than it sounds." To {goal_text}, {clever_he_she} composed
{concept_phrase}. The REPL — coordinating the
wait — returned the scout's count when the scout had it ready."""),

    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, arranged a small relay {place}, scout-crows posted at
different distances. "The runtime keeps track of who sent what and when
each finishes," {clever_he_she} said, "so the counts come back in the
right order, no matter how long each scout takes." To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the form, and
the REPL — coordinating the relay — returned the right value at the
right time."""),

    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, reached for the scout's count before the
scout had even returned. {clever_phrase} held {hasty_him_her} back: a
scout sent ahead must be allowed to finish. To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the form, and the
REPL — waiting for the scout the patient way — returned the value when
the scout had actually delivered it."""),
]

_RUNNERAHEAD_SUBPLOTS = _RUNNERAHEAD_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL sent the scout ahead and "
        "coordinated the return:"
    ),
]


# ─────────────────────── rewrite-before-drop (macros/defmacro) ───────────

_REWRITERULE_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, pressed a talon-tip to the pitcher's
rim {place} and traced the drop-order carefully. The day was hot, the
throat was narrow, and a hasty rewrite would lose pebbles into a wrong
sequence. "A macro," {clever_he_she} said, "is a rule that rewrites
the drop-order scratched on the rim before a single stone falls. You
write the rule once, and any drop-order that calls it gets rewritten
on the way to the pitcher; the rewrite happens cool and stable before
the runtime ever sees the form." To {goal_text}, {clever_he_she}
composed {concept_phrase}. The REPL — first
rewriting, then evaluating — returned the value the rewritten
drop-order yielded."""),

    SubplotTemplate("""\
"Here's the difference between a rule and a drop-order," {clever_phrase}, {emo_patient}, said. "A drop-order takes stones and raises the water. A rule takes a
*form* and makes a different *form* — only then does the runtime get to
evaluate it." To {goal_text}, {clever_he_she} composed
{concept_phrase}. The REPL — applying the rule to
the form first, then evaluating — handed back the value the rewritten form
had produced."""),

    SubplotTemplate("""\
"The order matters," {clever_phrase}, {emo_patient}, said. "When a rule is involved, the
runtime first walks through the form and applies the rule wherever it sees
one — and only then does it evaluate the result." To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the form, and
the REPL — rewriting first, evaluating second — returned the final
value."""),

    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, insisted that no rule was needed —
{hasty_he_she} could write the form directly. {clever_phrase} allowed
that sometimes that's true, but the rule shines when many forms need the
same rewriting. To {goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL — handling the rule's rewrite the rule's
way — returned the value the form had produced."""),

    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, insisted the rewrite-rule was unnecessary.
{clever_phrase} only smiled: a hand-scratched drop-order is fine once,
but the rule pays off when many forms need rewriting the same way. To
{goal_text}, {clever_he_she} composed {concept_phrase}, submitted the
form, and the REPL — running the rule the rule's way — returned the value
the rewritten form yielded."""),
]

_REWRITERULE_SUBPLOTS = _REWRITERULE_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} composed {concept_phrase} "
        "and scratched it on the rim for rewriting. The REPL — applying "
        "the rewrite-rule, then evaluating the rewritten form — returned:"
    ),
]


# ───────────────── families 18-22: scribe, chalkmark, tallywalk, beadstring, circuit ─────────────────
# ─────────────────────── pitcher-notations (scribe) ─────────────────────────

_SCRIBE_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The reading-conventions-of-the-form template — generic;
    #    works for comments, whitespace, parens, do, reader macros.
    SubplotTemplate("""\
"There are conventions for how the runtime *reads* a form,"
{clever_phrase}, {emo_patient}, said: "what counts as one token, what's just
spacing, what gets ignored, what gets grouped together. The
scribe and the reader both follow the same conventions." To
{goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL — reading exactly by the
conventions — returned the value the form had specified."""),

    # 2. The form-is-what-the-reader-sees template — generic.
    SubplotTemplate("""\
"A form is what the reader sees," {clever_phrase}, {emo_patient}, said,
"after the conventions have been applied. Some marks count, some
don't; some shapes are expanded before the runtime even gets a
look. The form you write and the form the runtime evaluates
aren't always character-for-character the same." To
{goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL — reading carefully — returned
the value of what the conventions had produced."""),

    # 3. The careful-writing-careful-reading template — generic.
    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, unrolled a small slate {place} and
scratched the pitcher-notations slowly, paying attention to every
talon-mark. The slate was rough and the day's heat made the clay
cling to the talon, so each scratch had to be clean the first time.
"The form has to be written so the reader can read it cleanly,"
{clever_he_she} said. "If the marks are right, the runtime gets the
right form; if not, not." To {goal_text}, {clever_he_she}
composed {concept_phrase}. The REPL —
reading exactly as written — returned the value cleanly."""),

    # 4. The Hasty-misreads-the-form template — generic fable beat.
    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, glanced at the pitcher-notations and
called out what {hasty_he_she} thought they would do without paying
attention to the conventions of how they were scratched.
{clever_phrase} only shook {clever_his_her} head — the runtime reads
the form exactly. To {goal_text}, {clever_he_she} composed
{concept_phrase}. The REPL — reading
literally — returned the right value, while {hasty}'s guess fell
short."""),

    # 5. The form-as-it-is template — generic.
    SubplotTemplate("""\
"A form is what's actually there on the pitcher's clay,"
{clever_phrase}, {emo_patient}, said, "after the conventions of writing and
reading have done their work. The runtime sees the cleaned-up form,
evaluates it, and gives back what it computes." To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the
form, and the REPL — taking the form exactly as it was — handed
back the value."""),
]

_SCRIBE_SUBPLOTS = _SCRIBE_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL read by the pitcher-notation "
        "conventions and returned:"
    ),
]


# ─────────────────────── chalk-scratch-vs-stone (quote/symbols) ────────

_CHALKMARK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The chalk-mark-on-the-stone template — symbols vs values.
    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, pointed at a chalk mark scratched on a smooth stone
{place}, then at another stone lying nearby. "The chalk mark on
the stone is the *name*; the stone is the *value*. They are not
the same thing — and Clojure lets you talk about either one."
To {goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL — keeping the name and the
value distinct — returned the right answer."""),

    # 2. The label-the-form template — `quote` / `'`.
    SubplotTemplate("""\
"To talk about the form itself rather than evaluating it,"
{clever_phrase}, {emo_patient}, said, "you mark the form with chalk in front.
Quoting tells the runtime: don't evaluate this, just hand
it back as the shape it is." To {goal_text}, {clever_he_she}
composed {concept_phrase}. The REPL —
respecting the chalk mark — returned the form unevaluated."""),

    # 3. The marking-vs-evaluating template — generic
    #    emphasis on the distinction without claiming a specific
    #    quote/unquote arrangement.
    SubplotTemplate("""\
"There's a difference between *marking* the form and
*evaluating* it," {clever_phrase}, {emo_patient}, said. "Quote in any of its
shapes is the marking — the runtime hands you back the form,
not its value, unless you say otherwise." To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the
form, and the REPL — marking exactly what the form asked for —
returned the form-as-data, exactly as the chalk had directed."""),

    # 4. The Hasty-confuses-mark-with-stone template.
    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, mistook the chalk mark on the stone
for the stone itself. "It says crow, so the value must be the
crow!" {clever_phrase} only shook {clever_his_her} head: the
mark and the stone are never the same thing. To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the form,
and the REPL — keeping mark and stone distinct — returned
the right answer for the goal."""),

    # 5. The chalk-endures-the-stone-lives template — generic.
    SubplotTemplate("""\
"A chalk mark can be carried from stone to stone," {clever_phrase}, {emo_patient}, explained, "passed hand to hand, written again. The mark itself is
just a shape; the value it names is separate — a thing in the world."
To {goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL — holding the mark distinct from
the value — returned exactly what the form asked for."""),
]

_CHALKMARK_SUBPLOTS = _CHALKMARK_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL — distinguishing chalk-mark "
        "from stone — returned:"
    ),
]


# ─────────────────────── stone-by-stone tally (reduce/count) ──────────────

_TALLYWALK_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The walking-the-rim-with-tally template — reduce.
    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, walked the rim of the pitcher {place},
one claw at a time, a small smooth stone held in the other talon for
the running tally. The rim was high and the water far below, so the
tally had to grow stone by stone — no shortcut, no skip.
"Reduce is this walk," {clever_he_she} said: "at each drop-point, you
combine the stone into the tally; at the end, the tally is your answer."
To {goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL — walking the rim, carrying the
tally — returned the final number."""),

    # 2. The starting-tally template — reduce with init.
    SubplotTemplate("""\
"You don't have to start the tally at zero," {clever_phrase}, {emo_patient}, said, holding up a stone already marked with a number. "If you
start with a different value, the walk begins from there — the
combine-step adds each stone in from that starting point." To
{goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL — starting from the given tally,
walking the rim — returned the final value."""),

    # 3. The simple-count template — `count`.
    SubplotTemplate("""\
"The simplest tally-walk is just counting,"
{clever_phrase}, {emo_patient}, said: "step along the rim, add one at every
drop-point, no other operation. The runtime does this for any
collection — vector, list, map, string." To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the
form, and the REPL — walking the rim, counting the steps —
returned the count."""),

    # 4. The Hasty-guesses-the-total template — fable beat.
    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, called out guesses at the pitcher
without bothering to walk the rim and carry the tally. {clever_phrase}
only smiled and reached for a stone. "The tally grows with every drop,"
{clever_he_she} said patiently. To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the
form, and the REPL — walking and counting stone by stone —
handed back the true total {hasty} had been guessing at."""),

    # 5. The rim-returns-a-number template — generic.
    SubplotTemplate("""\
"Walk the rim this way," {clever_phrase} instructed, {emo_patient},
"and what you carry back is always a single number — the one
you set out with, combined with each stone as you pass." To
{goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL — carrying the tally forward
with every step — returned the number the walk had produced."""),
]

_TALLYWALK_SUBPLOTS = _TALLYWALK_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL walked the rim carrying the "
        "tally:"
    ),
]


# ─────────────────────── pebble-string-on-a-vine (str/subs) ──────────────

_BEADSTRING_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The threading-pebbles template — `str` concat.
    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, held up a vine with small smooth pebbles threaded
on it in a row {place}. "Strings in Clojure are like this,"
{clever_he_she} said: "a threaded line of characters, in order.
Concat strings together, and the vines are spliced; cut a substring
out, and you get a shorter vine." To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the
form, and the REPL — splicing or cutting as the form said —
returned the new pebble-string."""),

    # 2. The counting-pebbles template — string length / substring.
    SubplotTemplate("""\
"To count the pebbles, walk the vine,"
{clever_phrase}, {emo_patient}, said. "Want a section of pebbles? Cut from one
position to another and you get a smaller vine, the original
untouched." To {goal_text}, {clever_he_she} composed
{concept_phrase}. The REPL — counting or
cutting — returned the answer the pebble-vine had given up."""),

    # 3. The reassembling-the-string template — generic string building.
    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, took two vines with pebbles threaded
on them {place}. The vines were short on their own — one wouldn't
reach far enough — and the day had grown hot. "Join two vines
together and you have one longer vine," {clever_he_she} said, "or
take a piece from one and attach it elsewhere." To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the form, and
the REPL — manipulating
the pebble-strings exactly — returned the new vine."""),

    # 4. The Hasty-yanks-at-the-vine template — fable beat.
    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, yanked at the pebble-vine {place}
without bothering to count the pebbles first. {clever_phrase}
stopped {hasty_him_her}: strings are precise — every pebble in
its place, every position counted. To {goal_text},
{clever_he_she} composed {concept_phrase}, submitted the form,
and the REPL — handling the vine carefully — returned the right
answer."""),

    # 5. The splice-or-slice template — generic string ops.
    SubplotTemplate("""\
"A pebble-string can be spliced with others," {clever_phrase}, {emo_patient}, said, "or sliced into pieces, characters counted and rearranged.
Whatever you ask the string to do, it does it precisely." To
{goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL — treating each pebble as the
form directed — returned the result."""),
]

_BEADSTRING_SUBPLOTS = _BEADSTRING_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL spliced or counted as the "
        "form said:"
    ),
]


# ─────────────────────── looping-drop-without-growth (recur/loop) ────────

_CIRCUIT_SUBPLOTS: list[SubplotTemplate] = [

    # 1. The circuit-without-growth template — recur.
    SubplotTemplate("""\
{clever_phrase}, {emo_patient}, walked a small circle around the
pitcher {place}, each lap returning to the same starting point with
a slightly different tally in talon. The pitcher was narrow and the
day was long; many laps would be wanted before the water rose, so
each lap had to leave no extra footprint behind. "Recur is this
circuit," {clever_he_she} said: "back to the top with new bindings,
no extra trail laid down behind us." To {goal_text}, {clever_he_she}
composed {concept_phrase}. The REPL —
looping without growing the call-stack — returned the final value."""),

    # 2. The base-case template — termination.
    SubplotTemplate("""\
"Every circuit has a stopping condition," {clever_phrase}, {emo_patient}, said. "Without one, the crow walks forever. With one, the
crow knows when the laps are done and the tally is the
answer." To {goal_text}, {clever_he_she} composed
{concept_phrase}. The REPL — looping
until the base case — returned the value the final lap
produced."""),

    # 3. The Hasty-distrusts-the-circuit template — fable beat.
    SubplotTemplate("""\
{hasty_phrase}, {emo_proud}, distrusted the very idea of a
circuit: surely you'd just walk forever? {clever_phrase}
smiled patiently — the base case is the runner's compass.
To {goal_text}, {clever_he_she} composed {concept_phrase},
submitted the form, and the REPL — looping the right number
of times, then stopping — returned the value cleanly."""),
]

_CIRCUIT_SUBPLOTS = _CIRCUIT_SUBPLOTS + [
    _story(
        "To {goal_text}, {clever_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL looped without growing the "
        "trail:"
    ),
]
