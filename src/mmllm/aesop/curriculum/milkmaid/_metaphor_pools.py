"""Metaphor-bearing subplot pools for milkmaid.

The base `_GOAL_SUBPLOTS` (in grade_1.py) is generic Milkmaid/Farmer
banter that uses `{goal_text}` and `{concept_phrase}` but doesn't
illuminate any particular Clojure idiom. These pools below DO
illuminate specific idioms by carrying a milkmaid-fable metaphor.

Central prop: the **milk pail** — the unevaluated form balanced
in mind. Daydreaming about the answer = guessing without eval =
nodding and spilling the pail. Getting to market = evaluating
the form and reading the REPL's actual return value.

The 22 metaphor families (same names as tortoise-hare; milkmaid imagery):

  Tier 1 (high-leverage core):
  - _POUCH_SUBPLOTS         — apron-pocket (let-binding)
  - _RECIPE_SUBPLOTS        — pail-steps card (fn / defn / comp / partial)
  - _BASKET_SUBPLOTS        — market-basket (collections / immutability)
  - _SIEVE_SUBPLOTS         — milk-strainer (HOFs / transducers)
  - _NOTEBOOK_SUBPLOTS      — tally-slate by the dairy door (atom / ref)
  - _ACORN_SUBPLOTS         — coin-counting (arithmetic)
  - _GATE_SUBPLOTS          — farmyard gate (boolean logic)
  - _FORK_SUBPLOTS          — fork in the road (if / cond / case)
  - _ROADSIGN_SUBPLOTS      — market-board (def / namespace / require)
  - _SAFETYNET_SUBPLOTS     — careful steady walk (try / catch / throw)

  Tier 2-3:
  - _SCROLL_SUBPLOTS        — market order slip (IO / metadata / doc)
  - _GUILD_SUBPLOTS         — market guild (protocols / dispatch)
  - _TOOLSHED_SUBPLOTS      — neighbor's milking stool (host interop)
  - _RUNNERAHEAD_SUBPLOTS   — runner sent ahead (agent / future / promise)
  - _REWRITERULE_SUBPLOTS   — farmer rewrites the plan (macros)
  - _SCRIBE_SUBPLOTS        — chalk marks on dairy wall (comments / reader)
  - _CHALKMARK_SUBPLOTS     — chalk mark on pail vs milk (quote / symbols)
  - _SORTINGTABLE_SUBPLOTS  — dairy sorting table (multimethods)
  - _CARRYINGCASE_SUBPLOTS  — the pail itself (deftype / defrecord)
  - _TALLYWALK_SUBPLOTS     — walking to market counting coins (reduce)
  - _BEADSTRING_SUBPLOTS    — braiding the cheesecloth (string ops)
  - _CIRCUIT_SUBPLOTS       — the daily milking round (recur / loop)

All templates use {goal_text} and {concept_phrase} (never {form_display}),
keeping the form-leak design intact. Characters are {milkmaid}/{farmer}
with their standard suffix family (_phrase, _he_she, _he_she_cap, etc.).
"""
from __future__ import annotations

from mmllm.aesop.curriculum.generator import SubplotTemplate

# ─────────────────────── temporary apron-pocket (let) ─────────────────────────

_POUCH_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{milkmaid} strutted down the market road, milk pail in hand. "{goal_text}?
Why, I've already tucked the answer into my apron-pocket," {milkmaid_he_she}, {emo_proud}, boasted,
patting {milkmaid_his_her} side. But when {milkmaid_he_she} reached the village gate,
{milkmaid_he_she} fumbled for it — the pocket was empty. {farmer_he_she_cap} arrived with
a form, saying, "To {goal_text}, first tuck the value into {concept_phrase} the apron-pocket,
write the steps that use it, and submit. When the form finishes, the pocket is empty again —
the binding is gone."
"""),

    SubplotTemplate("""\
On a bright morning, {milkmaid}, {emo_proud}, announced, "I shall {goal_text} while I walk to the mill!"
She clutched her pail and pretended the answer was already sewn into her apron. But {farmer}
only shook {farmer_his_her} head. "A form must first establish {concept_phrase} inside the
apron-pocket — a temporary shelf where the value rests only for this journey. When you leave
the farm yard, the shelf vanishes." {milkmaid_he_she_cap} learned that {concept_phrase} lives
and dies with the form's scope, like the pocket's warmth on a long walk.
"""),

    SubplotTemplate("""\
{milkmaid} dreamed aloud, {emo_proud}: "To {goal_text}, I need {concept_phrase} right
here, right now." {farmer_he_she_cap} touched the milkmaid's apron — the cloth still cool from the
morning dairy — and said, "Then produce a form that tucks the value into the
apron-pocket for as long as you need; the pocket is small, the road is long, and what fits there
fits only for one stretch. The form's body can reference it — but once the form ends, the pocket is
unpicked, and the value is gone forever." {milkmaid} realized that {concept_phrase} was not hers
to carry past the gate; it lived only within the stretch of road called the form's execution.
"""),

    SubplotTemplate("""\
"I know where {goal_text} lives!" {milkmaid}, {emo_proud}, cried. But {farmer_he_she} asked, "Can you
show me the form for {concept_phrase} before you use it?" {milkmaid} had no form to show.
{farmer} explained: "The apron-pocket is a promise the form makes — 'I will tuck this value
here for you.' Only inside the pocket's scope can the value be trusted. Outside, the pocket
is loose threads and air."
"""),

    SubplotTemplate("""\
{milkmaid} arrived at the village convinced {milkmaid_he_she} could {goal_text}
wherever {milkmaid_he_she} stood. {farmer} did not argue. Instead, {farmer_he_she} wrote a
form that tucked {concept_phrase} into the apron-pocket, used it in three different steps,
and then showed {milkmaid} the result. "This is the form's scope," {farmer_he_she}, {emo_patient}, said.
"Step outside it, and the pocket is sewn shut. The binding exists only where the form breathes."
"""),
]


# ─────────────────────── pail-steps card (fn) ──────────────────────────────

_RECIPE_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
Every morning, {milkmaid} carried the same pail-steps card, a recipe pinned inside {milkmaid_his_her}
apron with a heavy pail balanced overhead. {milkmaid_he_she_cap}, {emo_proud}, always followed the
card in order, and the last step — the measured yield — was what went to market. One day,
{milkmaid} asked, "Can I skip step two?" {farmer_he_she_cap} replied: "The form
for {goal_text} is like the pail-steps card. It reads the steps in order. The last step's result
is what {concept_phrase} returns to you. Skip a step, and you skip part of {concept_phrase}."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, dreamed aloud: "I'll {goal_text} as I like, in any order
I choose." But {farmer}, only chuckled and pulled out a pail-steps card. "Look
here. This card is a recipe — a form that says: do this, then that, then the next. The
daydreamer's order shifts on a whim, but a form's steps are written. The result of
{concept_phrase} flows from step to step, like cream down the chute. You cannot reorder cream."
"""),

    SubplotTemplate("""\
{milkmaid} found {farmer}'s pail-steps card and studied it, but then said, "This recipe calls
another recipe! Is that allowed?" {farmer_he_she_cap}, {emo_patient}, nodded. "Yes — {concept_phrase} can
compose smaller steps. A pail-steps card can say: do the morning-routine, then the afternoon-routine,
then measure. Each routine is a smaller card. The form calls the other form, and the result passes
forward. This is how we build great recipes from small ones."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, claimed, "I know how to {goal_text}, and I'll tell you the answer without writing
any form!" {farmer_he_she_cap} asked calmly, "Then produce the form whose execution would {goal_text}.
Write the steps on the pail-steps card, in order, and submit it." {milkmaid} tried, stumbled,
and finally understood: a form is not a guess. It is a card with steps written, each one clear,
each one leading to the last — {concept_phrase}.
"""),

    SubplotTemplate("""\
One noon, {milkmaid}, {emo_boastful} arrived at the dairy with a wild pail-steps card that said: "Do step one.
Then, if the milk is sour, skip to step five. Otherwise, step two." {farmer_he_she_cap} read it
and said, "Good — this recipe branches. It is still a form; it still {concept_phrase} at the end.
But notice: each path through the card leads to a result. The form's logic unfolds as the steps
are read, just as the milkmaid's walk unfolds on the market road."
"""),
]


# ─────────────────────── market-basket (collections / immutability) ──────────────────────────

_BASKET_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, rummaged in the heavy market-basket, moving the cream to
the left and the curds to the right. "I'll rearrange this however I wish!" {milkmaid_he_she_cap}
cried. But {farmer} shook {farmer_his_her} head. "Look behind you — your
original basket still sits on the ground, untouched, the wicker as you wove it. To {goal_text},
{concept_phrase} is {milkmaid_his_her} rearrangement. The old basket remains. Each time you
reach in and pull out something new, you are making a fresh basket, leaving the first one
exactly as it was."
"""),

    SubplotTemplate("""\
{milkmaid} claimed, {emo_proud}, "I shall {goal_text} by changing the basket as I carry it."
{farmer_he_she_cap} weighed the basket in {farmer_his_her} hands, the wicker cool, the load
honest, and said, "No. The basket is heavy because of what is in it, and a wish
will not lighten it. To {goal_text}, produce a form that builds a new basket — a fresh one, with
compartments for cream, skim, and curds arranged according to {concept_phrase}. The old basket
never changes — the wicker remembers. The milkmaid's daydream is to imagine the basket transforms;
the farmer's method is to build a new one."
"""),

    SubplotTemplate("""\
The market-basket held cream in the first slot, skim in the second, curds in the third. {milkmaid}
peered in and guessed, "I know what's here." But {farmer_he_she}, {emo_patient}, asked, "How do you know? Look at
the form for {concept_phrase}. Each slot is labeled by the form — cream here, skim there. When we
change the order, we do not edit the old basket; we produce a form whose result is a new basket, with
new labels and new positions. The old one is a photograph — unchanged forever."
"""),

    SubplotTemplate("""\
{milkmaid} reached into the basket and stirred the cream and milk together, then declared,
"I have {concept_phrase}!" {farmer_he_she_cap}, {emo_patient}, asked quietly, "Show me the form." {milkmaid} had none.
{farmer_he_she_cap} continued, "To {goal_text}, write a form whose result is a new basket — a
collection with the compartments arranged as your steps dictate. Submit the form. The original basket
will sit beside it, still holding cream in the first slot, skim in the second."
"""),

    SubplotTemplate("""\
One afternoon, {milkmaid} arrived pulling two baskets. "This one has my guess," {milkmaid_he_she}, {emo_proud}, said,
pointing at one. "This one is the form's result," {milkmaid_he_she} said, pointing at the other. The
baskets looked different — the form's basket had the compartments in a new order. {farmer_he_she_cap}
nodded. "Exactly right. To {goal_text}, {concept_phrase} does not alter the first basket. It builds
a second one, whose arrangement is what the form computed. That is the power of the market-basket —
change is creation, not destruction."
"""),
]


# ─────────────────────── milk-strainer (map / filter / transducers) ──────────────────────────

_SIEVE_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, held a milk-strainer over a fresh pail and poured the warm milk
through. "What comes out?" {milkmaid_he_she_cap} asked. {farmer} replied:
"The strainer holds a rule — a form that decides what passes through and what falls away.
To {goal_text}, the strainer is {concept_phrase}: it says which drops belong in the fresh
pail. If the rule says yes, the drop flows in. If no, the drop spills. The original stream
is untouched — the fresh pail catches only what the rule allows."
"""),

    SubplotTemplate("""\
{milkmaid} stood with a pail of milk and cried, "I can guess which cream belongs in the market
basket!" But {farmer_he_she} set a milk-strainer between them. "No guessing," {farmer_he_she}, {emo_patient}, said. "To
{goal_text}, submit a form with a rule inside the strainer. The rule examines each drop — each item in
your collection. If the rule says 'yes, this one counts,' it drips into the fresh pail. If 'no,' it falls
away. That is {concept_phrase} — the strainer keeps what passes the test."
"""),

    SubplotTemplate("""\
{milkmaid} watched {farmer} hold a milk-strainer and pour milk while whispering a rule:
"Keep the cream, let the skim fall." The cream flowed into the fresh pail, transformed somehow — thicker,
richer. "{farmer}, what did you do?" {milkmaid_he_she_cap}, {emo_proud}, asked. {farmer_he_she_cap} replied,
"The strainer holds two rules. One filters — 'keep only the cream.' The other transforms — 'while it
falls, thicken it.' {concept_phrase} can both sieve and reshape. The fresh pail holds not just filtered
drops, but changed ones."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, claimed, "I know which drops should remain without writing down the rule." {farmer_he_she_cap}
asked, "Then produce the form with the rule written inside the strainer. The rule is {concept_phrase} —
it decides, for each drop in the stream, whether that drop belongs in the fresh pail." {milkmaid_he_she_cap}
wrote the form and submitted it. The strainer's rule flowed through, and the fresh pail caught exactly what
{milkmaid_he_she} intended. "I see," {milkmaid_he_she} said. "The rule must be written, not guessed."
"""),

    SubplotTemplate("""\
One morning, {milkmaid_he_she} poured milk through a strainer with no rule written. The strainer
did nothing — every drop fell away, the fresh pail was empty, and the milk pooled cold and useless
on the dairy floor. "The strainer is broken!" {milkmaid_he_she_cap} cried, {emo_regretful}. {farmer}
shook {farmer_his_her} head, {emo_patient}, the strainer dripping in {farmer_his_her} steady hand.
"No. The strainer requires a rule — a form for {concept_phrase}. Without the rule, the strainer
cannot decide; an empty pail is the honest result of an absent rule. Write the form that says
'pass this, reject that,' and the fresh pail will fill. But {milkmaid_he_she} must write it —
the farmer's form, not the milkmaid's guess."
"""),
]


# ─────────────────────── tally-slate by the dairy door (atom / ref / swap!) ──────────────────────────

_NOTEBOOK_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
The tally-slate hung by the dairy door with the day's count chalked across it. Any farmer
who passed could read the slate. {milkmaid_he_she_cap}, {emo_proud}, tried to erase and
rewrite it while another farmer was still reading, and the chalk smeared into nonsense.
{farmer} pointed to the slate. "To {goal_text}, we use the tally-slate.
Any reader can walk up and see the count. But to change it, {concept_phrase} happens in
one breath: read the old number, apply the change, write the new one. No other farmer
can interrupt mid-breath. That is atomic."
"""),

    SubplotTemplate("""\
{milkmaid} guessed, "I'll just change the count whenever I feel like it!" But {farmer_he_she} showed
{milkmaid} the slate: two farmers had erased at the same time, and now the count was a scribble,
unreadable. {farmer_he_she_cap} said {emo_patient}, the chalk's edge cool against {farmer_his_her}
fingers, "To {goal_text}, produce a form that changes the tally-slate atomically — the slate is a
shared ledger, and a half-written count is no count at all. The form must say: 'Read the slate,
apply {concept_phrase}, write the result — in one unbreakable motion.' If two farmers arrive together,
the atomic form is the only one that lets the slate stay honest."
"""),

    SubplotTemplate("""\
{farmer} approached the tally-slate and muttered a form: "The old count is 47. Add 3. The new
count is 50. Write it." In one motion, {farmer_he_she} read, computed, and wrote. {milkmaid_he_she_cap}
watched and asked, "How did you keep it so neat?" {farmer_he_she_cap}, {emo_patient}, replied, "The form for {concept_phrase}
is atomic — it promises that no other farmer can sneak in mid-update. The slate shows 50, and every farmer
knows it is the result of one unbroken form, not a daydream or a half-written guess."
"""),

    SubplotTemplate("""\
{milkmaid} stood at the dairy door, staring at the tally-slate. "I want to change the count,
but I do not know how," {milkmaid_he_she} admitted. {farmer}, {emo_patient}, smiled and placed a form in
{milkmaid_his_her} hand. "Here. This form reads the slate, applies {concept_phrase}, and writes the result
— all in one atomic step. Submit it to the slate. The count will {goal_text} properly, and no other farmer
can interfere."
"""),

    SubplotTemplate("""\
One morning, three farmers arrived at the slate to update the count. {milkmaid} panicked — "Will the count
become a mess?" But {farmer_he_she}, {emo_patient}, said no. "Each farmer submits a form for {concept_phrase} — a form
that reads the current slate, applies the change, and writes the result, atomically. The forms queue up.
One farmer's form completes, then the next, then the next. The count is always clean, always right. That is
the slate's promise: {goal_text} safely, one atom at a time."
"""),
]

# ─────────────────────── coin-counting (arithmetic) ─────────────────────────

_ACORN_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{milkmaid} arrived at the market with a handful of copper coins, jingling in
{milkmaid_his_her} pocket — the pail was heavy on {milkmaid_his_her} arm and the road had been
long. "I know how much I have without counting," {milkmaid_he_she} boasted, {emo_proud}.
But {farmer_he_she} took the coins and began stacking them in neat rows, one by one: one coin,
two coins, three coins. "To {goal_text}," {farmer_he_she} said {emo_patient}, "we count,
we stack, we tally. A heavy pail does not lighten because we wish it; the coins do not lie —
{concept_phrase} is just a name for that careful work. Submit the form and read the REPL's count."
"""),

    SubplotTemplate("""\
Every morning, {milkmaid} carried a pail of milk to the dairy, imagining what the coins would
total. {farmer_he_she_cap} only smiled and said, "Come. Let us count the coins from yesterday's
sales." Together they counted: one coin, then another, then another, stacking them into piles
that grew taller as the morning wore on. "This is {concept_phrase}," {farmer_he_she} said,
{emo_content}. "To {goal_text}, we do not guess. We count each coin — the silver heavier, the
copper warmer in the palm — and see what the stack becomes. The market is a long walk, the
sums are real, and the form is what carries the count from coin to total. Write the form and let
the REPL count for you."
"""),

    SubplotTemplate("""\
{milkmaid} watched {farmer} sort coins at the dairy table: copper in one pile, silver
in another, gold in a third — three small heaps growing patient and even under {farmer_his_her}
hands. "{farmer}, how do you know the total without guessing?" {milkmaid_he_she_cap}
asked. {farmer_he_she_cap} replied, {emo_patient}, "The coins speak for themselves. To
{goal_text}, {concept_phrase} means we examine each coin — its weight cool, its value
plain — and we combine them. The form's logic stacks them just as {farmer_his_her} hands do —
slow, certain, irrevocable. Submit it, and the REPL tallies the truth."
"""),

    SubplotTemplate("""\
At the market square, {milkmaid} declared to all the traders, "I will {goal_text}, and I need no
help!" But when she tried to tally the coins in her head, the daydream of fortune turned the
numbers slippery, and she stumbled. {farmer_he_she_cap} arrived and set out the coins in order,
the copper cool and heavy under {farmer_his_her} fingers. "Counting is not a dream,"
{farmer_he_she} said {emo_patient}, "it is a step-by-step walk through the coins,
where {concept_phrase} stacks one coin upon the next. The road is long but every step is
counted, and the form's tally is the only honest one. Submit the form and watch the stack grow."
"""),

    SubplotTemplate("""\
One afternoon, {milkmaid_he_she} found a cache of coins hidden in the dairy and tried to guess
the fortune, {emo_proud}, the dairy cool and the imagined market still far away. "Surely I can
see the total at a glance!" {milkmaid_he_she_cap} cried. {farmer} only shook {farmer_his_her}
head and began sorting the coins into neat piles — the copper warm, the silver
heavy, the gold heaviest of all. "To {goal_text}, we must count — truly count, and {concept_phrase}
is the form that ticks through each coin, one by one, and tells the REPL what the total is.
A heavy heap is heavy because of the coins it holds, not because we wish it; the form is the
honest weight. Not a dream, not a guess. A form, a count, a truth."
"""),
]


# ─────────────────────── farmyard gate (boolean logic) ─────────────────────

_GATE_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, hurried down the long farm path toward the village, the
heavy pail balanced carefully on her head. But the path was blocked by a chain of gates — one
after another. "All open, all open!" {milkmaid_he_she_cap} cried hopefully. {farmer},
{emo_patient}, shook {farmer_his_her} head. "One closed gate stops you, {milkmaid_he_she}.
To {goal_text}, the gate rule decides who passes. {concept_phrase} checks each gate in the
chain. If even one is closed — if even one says 'no' — you cannot pass. Submit the form, and
the REPL tells you: open or closed, yes or no."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, gazed at a farmyard gate blocking the path and said,
"Surely this gate will swing open!" {farmer}, only pointed at the latch.
"The gate rule is written there. To
{goal_text}, we do not guess whether the gate opens. We read the rule — {concept_phrase} — and it
tells us. If the rule says 'closed,' no amount of wishing opens it. Write the form that reads the
rule and submits it to the REPL."
"""),

    SubplotTemplate("""\
A chain of three gates stretched across the farmyard, each with a rule carved into its post. The
first said 'open for merchants,' the second said 'open for farmers,' the third said 'open for all.'
{milkmaid}, {emo_proud}, asked, "Can I pass?" {farmer_he_she_cap} replied, "Submit a form that checks the rules
— {concept_phrase} — against your name. If all three gates say 'yes,' you pass through. If any says
'no,' you stop here. That is the gate's logic: every gate in the chain must agree."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, claimed, "I know whether the gates will open without checking them!" But
{farmer_he_she} led {milkmaid} to the first gate. "Read the rule {concept_phrase}. Now write a
form that applies it. If the rule says 'open,' the gate swings. If it says 'closed,' you stop. To
{goal_text}, we do not guess. We write the form, submit it, and the REPL tells us whether we pass
or whether we are stopped by the first closed gate."
"""),

    SubplotTemplate("""\
One morning, {farmer_he_she} walked {milkmaid}, {emo_boastful} through a series of gates on the path. The first
gate was open, the second was open, but the third gate's rule said 'closed.' "Here," {farmer_he_she}
said, pointing. "The form for {concept_phrase} must check every gate. The REPL will say 'blocked' —
because one gate stopped us. To {goal_text}, every gate in the chain must say 'open.' Write the
form and let the REPL walk the chain with you."
"""),
]


# ─────────────────────── fork in the road (if / cond / case) ─────────────────────

_FORK_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, came to a fork in the long road — one path led to the
market, the other to the farm. "I'll take both paths at once!" {milkmaid_he_she_cap} cried.
{farmer} shook {farmer_his_her} head. "No, {milkmaid}. The heavy pail can
only go down one road. To {goal_text}, a condition decides which path the pail takes.
{concept_phrase} examines the choice, and the REPL walks down that one road only. Submit
the form and watch the pail roll down the right branch."
"""),

    SubplotTemplate("""\
At a crossroads {place}, {milkmaid_he_she} stood uncertain: which way to the market? "I'll guess
the quicker path," {milkmaid_he_she}, {emo_proud}, said. But {farmer_he_she} pointed to a weathered sign carved
with conditions. "To {goal_text}, we do not guess which fork to take. {concept_phrase} reads the
sign, checks the condition, and the form walks down the only path that the condition permits. The other
path is never walked — the pail stays on one road only."
"""),

    SubplotTemplate("""\
{milkmaid} found a signpost with three arrows pointing three ways: the mill, the market,
the field. "I'll {goal_text} on all three roads!" {milkmaid_he_she_cap}, {emo_proud}, announced. {farmer}
laughed gently. "No, child. To {goal_text}, {concept_phrase} chooses one branch. The form reads
the condition — 'if you are a miller, go left; if you are a merchant, go right; if you are a farmer,
go straight.' Only one path runs. The pail rolls down one road only. Submit the form."
"""),

    SubplotTemplate("""\
{milkmaid} danced between two paths at a fork, claiming she would {goal_text} on both.
But {farmer_he_she} set the pail down carefully. "The pail cannot split. To {goal_text}, the
form must be {concept_phrase} — a conditional fork that says 'if this, then that path; if not,
then the other path.' The REPL follows one branch only. Write the form and submit it. The pail will
roll down the path the condition chooses."
"""),

    SubplotTemplate("""\
On the way to market, {milkmaid}, {emo_boastful} encountered three forks in quick succession. At the first, {milkmaid_he_she}
guessed the direction. At the second, {milkmaid_he_she} stumbled. At the third, {milkmaid_he_she} was lost.
{farmer_he_she_cap} arrived and said, "To {goal_text}, write a form that is {concept_phrase} — a
series of forks, each checking a condition, each choosing a path. The form walks the right forks in the
right order. It never wavers, never guesses, never splits. Submit it, and the REPL brings you to market."
"""),
]


# ─────────────────────── market-board (def / namespace / require) ─────────────────────

_ROADSIGN_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, arrived at the village square and saw a great board nailed
to the market hall. Names and prices were chalked across it. "Who decides these names?"
{milkmaid_he_she_cap} asked. {farmer} pointed to the board. "To {goal_text},
the board {concept_phrase} — it posts a name for all buyers to read. Every buyer walks up and
reads the posted name. The name is public, stable, and true. Submit the form that writes the
name on the board."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, tried to make up a price for milk on the spot: "Let us call it 8 coins today!"
But no buyer would listen. {farmer_he_she_cap} led {milkmaid} to the market-board at the village square.
"See this board? {concept_phrase} is written here. Every buyer in the kingdom can read the posted name
and know the price. To {goal_text}, write a form that carves the name into this board — a name that
will stand for every use, in every market, every day."
"""),

    SubplotTemplate("""\
At the market, different traders had different boards. One board in the north market read differently
from one in the south. {milkmaid}, {emo_boastful} was confused: "How do I know which name to trust?" {farmer_he_she_cap}
replied, "Each market — each {concept_phrase} — posts its own board. To {goal_text}, a buyer walks
to the market-board that is posted in a particular market and reads the price written there. Different
markets, different boards, different names. The buyer reads from the right board."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, declared, "I will invent new names for the prices each time I visit the market!"
But {farmer_he_she} only shook {farmer_his_her} head. "No, {milkmaid}. To {goal_text}, you must {concept_phrase}
the name once on the market-board. Then every buyer, every day, reads that posted name. The name does not
change. The board is permanent. Write the form that posts the name where all can read it."
"""),

    SubplotTemplate("""\
One morning, {farmer_he_she} brought {milkmaid} to the market hall and showed {milkmaid_him_her} three
boards: one posted the butter price, one posted the cheese price, one posted the cream price. "See? Each
board is {concept_phrase} in a different location," {farmer_he_she}, {emo_patient}, explained. "A buyer who needs butter
walks to that board. A buyer who needs cheese walks to that board. To {goal_text}, a form {concept_phrase}
a name or a reference where all who need it can find it. The market-board is the public shelf."
"""),
]


# ─────────────────────── careful steady walk (try / catch / assert) ─────────────────────

_SAFETYNET_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, carried the pail down the long farm road in a rush,
hurrying toward the market. The fragile pail tipped, the milk spilled, and the cool grass
took the loss. {farmer} said, "To {goal_text}, you must walk carefully. In
the REPL, the practice meadow is your safety net — if the form stumbles, no milk spills.
The REPL catches the error and lets you try again.
But you must write {concept_phrase} and submit it. No rush, no stumbling. Walk carefully."
"""),

    SubplotTemplate("""\
{milkmaid} was determined to {goal_text} quickly, without pausing. But {farmer_he_she}
stopped {milkmaid_him_her} at the gate. "To {goal_text} safely, {concept_phrase} first. Check that
the form is sound. If it stumbles, the REPL will catch it — that is the safety net of the practice meadow.
But you must care enough to watch, to try carefully, to write the form correctly. Walk steady, not fast.
Then submit."
"""),

    SubplotTemplate("""\
{milkmaid} arrived at the dairy after a long walk, pail intact and milk brimming. {farmer_he_she_cap}
smiled and asked, "How did you keep the pail so steady?" {milkmaid_he_she_cap}, {emo_proud}, replied, "I walked carefully,
one step at a time, watching for stones." {farmer_he_she_cap} nodded. "To {goal_text}, {concept_phrase}
means you walk carefully in the REPL. Each form is a step. If you stumble, the REPL catches you. The safety
net is always there. But you must write the form true, and submit it with care."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, claimed, "I can {goal_text} while running and juggling!" But {farmer_he_she}
knew better. "In the real meadow, a stumble spills the pail. But in the practice meadow — the REPL — the
safety net catches every stumble. {concept_phrase} is your steady form, written carefully and submitted
once. The REPL evaluates it safely. If it catches an error, you learn, you fix it, you try again. No milk
spilled. No harm done."
"""),

    SubplotTemplate("""\
One afternoon, {milkmaid}, {emo_boastful} hurried down the path and tripped. The pail crashed, and the milk was lost.
{milkmaid_he_she_cap} wept. But {farmer_he_she} gathered the pieces of the pail and showed {milkmaid_him_her}
the REPL: "Here is the practice meadow. Here, {concept_phrase} — write the form carefully and submit it.
If it stumbles, the safety net catches it, and you know what went wrong. You try again. In the real meadow,
one stumble ends the day. In the REPL, a hundred stumbles are practice. Walk carefully. Let the REPL teach you."
"""),
]

# ─────────────────────── market order slip (IO / metadata / slurp / spit / doc) ──────────────────

_SCROLL_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
Every dawn, {milkmaid}, {emo_boastful} carried a market order slip — a written record of what the buyer wanted:
"six pails of cream, three of skim." {farmer_he_she_cap} held the slip and read aloud. "This is
{concept_phrase}. The slip holds the buyer's requirements in marks on paper. To {goal_text},
we must read this slip carefully and use what it says. The slip is a scroll — a record,
a document that comes to us from outside, written in a tongue we must understand."
"""),

    SubplotTemplate("""\
{milkmaid} arrived with a blank market order slip and asked, "{farmer}, how do
I know what to do?" {farmer_he_she_cap} took the slip and showed {milkmaid}, {emo_boastful} how to mark it: "When
the buyer sends word about {goal_text}, we write it here on the slip. The slip carries the
buyer's intention from market to farm. To read the slip, we {concept_phrase}. To write to it,
we use a different form. The slip is a bridge between the buyer's wishes and our milk."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, asked, "Can I write notes in the margins of the market order slip?"
{farmer_he_she_cap} nodded. "Yes. The slip holds not just the buyer's main request but also
metadata — notes in the margins, the date, the seal of approval. When we {concept_phrase}
to {goal_text}, those margins matter too. The slip is more than words; it is a document whose
every mark helps us understand what the buyer truly needs."
"""),

    SubplotTemplate("""\
One morning, {milkmaid} brought two slips — one the buyer wrote, one {milkmaid_he_she} had copied.
{farmer_he_she_cap} compared them, the parchment cool and the ink of the original sharper, the
copy faintly smudged. "Yours is an echo," {farmer_he_she} said, {emo_patient}, "and an echo is
softer than the voice. The true slip is the buyer's scroll, and the original carries the only
honest reading. To {goal_text} correctly, we must {concept_phrase} — read the original slip
that came from the buyer's hand. Copy errors creep in when we try to remember instead of
reading; a scroll's truth lives on the parchment, not in the daydreamer's head."
"""),

    SubplotTemplate("""\
{milkmaid} found an old market order slip in the barn, yellowed and creased. "Can this
still tell us what to do?" {milkmaid_he_she_cap}, {emo_proud}, asked. {farmer} took it and read the marks.
"Yes. This slip holds a record — even old records tell us what the buyer once wanted. To {goal_text}
with such a slip, we {concept_phrase} the document itself. The scroll is a store of information that
outlasts the moment. We read it, and the past speaks."
"""),
]


# ─────────────────────── market guild (protocols / extend-protocol / extend-type) ──────────────────

_GUILD_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
All the dairy farmers belonged to the market guild — every member must deliver milk, but each
farm's way was different. When the guild-master called out, "Deliver milk!", every farmer
answered, yet each one's delivery was {milkmaid_his_her} own. {farmer}, {emo_patient},
explained to {milkmaid}: "To {goal_text}, the guild rule says WHAT must happen — the delivery
itself. But {concept_phrase} is how each farm does it. The guild does not teach method; it
teaches promise. Each farmer promises the same call, but each farm's technique is unique."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, asked, "Does every farmer deliver milk the same way?" {farmer_he_she_cap} shook
{farmer_his_her} head. "No. The market guild sets the rule: 'All members will deliver milk.' But {concept_phrase}
for each farm. One farm uses a cart, another a bucket, another a pail carried on the head. The guild-master
never asks HOW — only that the milk arrives. To {goal_text}, you join the guild, promise to follow its rule,
and show your own way of doing {concept_phrase}."
"""),

    SubplotTemplate("""\
When a new farmer wanted to join the market guild, the guild-master asked, "Can you deliver milk?"
The farmer said yes. "Good," the master replied. "The guild has one rule for all members: deliver milk.
That is {concept_phrase}. But your farm is new — show us your way. To {goal_text}, you write the form
that {concept_phrase} for your farm only. Other farmers will write their own. The guild binds us all
to the same promise; our individual methods set us apart."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, said, "All the farmers deliver milk differently. How can the guild work?" {farmer_he_she_cap}
smiled. "The guild does not care about difference. It cares about unity of purpose. To {goal_text}, the
guild says: 'Any farmer who joins must {concept_phrase}.' Each farm does it its own way, but the guild-call
is the same. When I call 'Deliver!', a hundred farmers answer, each with {milkmaid_his_her} own {concept_phrase}."
"""),

    SubplotTemplate("""\
{farmer} brought together five new farmers at the market square. "All of you will join the guild,"
{farmer_he_she} announced. "Your first rule: {concept_phrase} when I call 'Deliver!' But each of you will
write your own form for {concept_phrase}. The guild says what you promise; your form says how you keep it.
To {goal_text}, you must join the guild by showing {concept_phrase} — your farm's unique answer to the
guild's universal call."
"""),
]


# ─────────────────────── neighbor's milking stool (host interop / .method / Class/static / new) ──────

_TOOLSHED_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, arrived at the neighbor's farm and saw a sturdy milking
stool in the toolshed. "May I borrow it?" {milkmaid_he_she_cap} asked. The neighbor nodded.
"Of course. It works the same way here or on your farm." When {milkmaid} brought the stool
home and sat on it, the wood was solid and cool, and the seat was steady — every farm
understands a milking stool. {farmer} explained: "To {goal_text}, you
{concept_phrase} — you borrow a tool from the neighbor's farm and use it as is. The stool
works
the same way regardless of whose farm it sits on."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, tried to build a milking stool but failed. The legs were uneven; it wobbled. {farmer_he_she_cap}
walked to the neighbor's place and returned with a proper stool. "Rather than reinvent, we borrow," {farmer_he_she}
said. "To {goal_text}, {concept_phrase} — use the neighbor's tool directly. It is made well; it is
tested. The neighbor's stool is sturdy — it has served the farm for years. We do not rebuild
what already works."
"""),

    SubplotTemplate("""\
{farmer} brought a basket of tools from the neighbor's farm and set them before {milkmaid}.
"Any of these will {concept_phrase}," {farmer_he_she}, {emo_patient}, said. "The hammer works the same way here. The
knife cuts the same way. To {goal_text}, you {concept_phrase} — you take the neighbor's tool and use
it in your form. The tool's behavior is not your invention; you simply call it by its true name and it
serves you."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, insisted on understanding how the neighbor's milking stool was built. {farmer_he_she_cap}
said, "You do not need to understand the stool's innards to sit on it. To {goal_text}, you {concept_phrase}
— the neighbor's tool is a sealed box. You know what it does; you call it by name; it answers. The neighbor
built the stool so well that we trust it without rebuilding it ourselves."
"""),

    SubplotTemplate("""\
When {milkmaid} borrowed the neighbor's milking stool, {farmer_he_she} asked, "Do you know how the
stool was made?" {milkmaid_he_she_cap}, {emo_proud}, said no. "Then you cannot use it?" {farmer_he_she_cap} asked. {milkmaid_he_she_cap}
laughed. "Of course I can! I sit on it." {farmer_he_she_cap} nodded. "Exactly. To {goal_text}, you {concept_phrase}
— you use the neighbor's tool by name, and it works. You do not need to understand its timber or nails.
You need only know: this tool, called this way, does that thing."
"""),
]


# ─────────────────────── runner sent ahead to the buyer (agent / future / promise) ──────────────────

_RUNNERAHEAD_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{farmer}, {emo_patient}, called a swift runner and said: "Go ahead to the market with news
of our cream. Do not wait for me — run on, and the answer will come back to you." The
runner sprinted down the long road. {milkmaid_he_she_cap} asked, "Will we
wait for the answer?" {farmer_he_she_cap} shook {farmer_his_her} head. "No. The runner is
already moving. To {goal_text}, {concept_phrase} happens now — we send the runner ahead.
The answer arrives later, but we do not stop. The heavy pail and I walk behind, and when
we reach the market, the runner's answer is waiting."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, said, "I want to know what the buyer will pay before we leave the farm!" {farmer_he_she_cap}
replied, "Then you will wait a very long time. Instead, I am {concept_phrase} — sending a runner ahead
with a message. To {goal_text}, the runner carries the news and runs toward the market. We continue our
work here. When the sun reaches its peak, the runner has returned with the buyer's answer. Checking too
early gets nothing; the runner must have time to reach and return."
"""),

    SubplotTemplate("""\
{farmer} sent a runner down the road with a message for the buyer: "We have cream. What is
your price?" Then {farmer_he_she} turned to {milkmaid}, {emo_boastful} and said, "Now we use {concept_phrase} — we continue
milking, filling pails, preparing the cart. To {goal_text}, the runner is already on the way. {milkmaid_he_she_cap},
we do not sit idle. We work while the runner moves. The answer will be waiting when we finish."
"""),

    SubplotTemplate("""\
{milkmaid} watched the runner disappear down the road and asked, "Is the answer coming?"
{farmer_he_she_cap}, {emo_patient}, said, "Not yet. The runner is {concept_phrase} — moving toward the buyer with our
question. To {goal_text}, we must wait. But waiting does not mean stopping. We do our chores. We fill
pails. We prepare. When the runner finally returns with the buyer's answer, we will have everything ready.
The answer is on its way; it just takes time."
"""),

    SubplotTemplate("""\
{farmer} sent three runners — one to the grain merchant, one to the cheese master, one to the
village council. "Each of you is {concept_phrase} with a different message," {farmer_he_she}, {emo_patient}, said.
"To {goal_text}, I will have three answers, not one. But I do not wait for all three at once. I check
each one when {milkmaid_he_she} is ready. If {milkmaid_he_she} checks too early, the runner has not
returned, and there is no answer yet. But the runners are working. Eventually, each will arrive."
"""),
]


# ─────────────────────── farmer rewrites the milkmaid's plan (defmacro / macroexpand) ──────────────

_REWRITERULE_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, daydreamed aloud: "I will {goal_text} by doing step one,
then step two, then step three." {farmer}, listened carefully and wrote it
all down on the dairy slate. But before anything happened, {farmer_he_she} did something
strange — {farmer_he_she} rewrote {milkmaid}'s daydream into a different set of steps. "What
are you doing?" {milkmaid_he_she_cap} asked. {farmer} replied, "The daydream is not ready to run. I
am {concept_phrase} — rewriting it into true steps before the dairy opens. What you dreamed and what
actually happens are not the same. The farmer's rewrite is what runs."
"""),

    SubplotTemplate("""\
{milkmaid} wrote a plan on a slip of paper, {emo_proud}: "First add milk, then add cream, then mix."
{farmer_he_she_cap} read it, the slip thin between {farmer_his_her} fingers, and said,
"Good plan. But now watch — the recipe is long, the day is short, and what the kitchen reads
must be exact." {farmer_he_she_cap} took the slip and rewrote it: "Add one unit of milk, add one
unit of cream, mix both together." The rewrite was simpler, clearer, the lines shorter and the
quantities precise. {milkmaid_he_she_cap} asked, "Why did you change my words?"
{farmer_he_she_cap} replied, "To {goal_text}, I {concept_phrase} — I turned
your daydream into working steps before anything runs. What you wrote is not what the dairy sees; what I rewrote
is what runs."
"""),

    SubplotTemplate("""\
{farmer}, {emo_patient}, explained to {milkmaid}, "When you {goal_text}, you write a daydream form. The form
looks like English, like a story. But {concept_phrase} happens before we run the form — we rewrite it into
machine steps. You write the story; the farmer rewrites it into true steps before the dairy opens. What you
see on the paper is not what runs inside the pail."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, asked, "Why does my form not do what I wrote?" {farmer_he_she_cap} smiled and pulled out
two slips. "This one is what you wrote — your daydream." {farmer_he_she_cap} showed the first. "This one is what
I rewrote — what actually runs." {farmer_he_she_cap} showed the second. They were very different. {milkmaid_he_she_cap}
gasped. "But I wrote..." {farmer_he_she_cap} said, "I know. To {goal_text}, {concept_phrase} happens at dawn,
before the dairy opens. The farmer rewrites dreams into reality. Your form is beautiful, but the rewrite is what
the pail understands."
"""),

    SubplotTemplate("""\
Three farmers arrived with three different ways to {goal_text}. Each wrote a daydream form on a slip. But {farmer_he_she} took all three slips and {concept_phrase} — rewrote them all into the same efficient
steps before the work began. "Why?" the farmers asked. {farmer}, {emo_patient}, replied, "Each of you dreamed differently,
but the dairy does not see dreams. It sees the rewritten form. Before anything runs, I rewrite all daydreams
into what actually happens. That is the farmer's power — the rewrite is the truth."
"""),
]

# ─────────────────────── chalk marks on dairy wall (comments / whitespace / parens / do / reader) ──────────

_SCRIBE_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, arrived at the dairy to find the wall covered in chalk
marks above the milk churns. "What are all these notes?" {milkmaid_he_she_cap} asked.
{farmer} pointed at the wall and explained: "The chalk marks explain the steps below them —
first chill the cream; second churn it; third press it. The marks do not
change the milk inside. To {goal_text} we write chalk marks with {concept_phrase} — notes that tell a reader
what the form is about. The marks sit above the form. When the reader is done reading them {farmer_he_she}
submits the form below; the milk flows unchanged."
"""),

    SubplotTemplate("""\
{milkmaid} peered at {farmer}'s dairy wall and saw lines of chalk marks above the form. Some marks were
crossed out, some added. "The form looks like a mess!" {milkmaid_he_she_cap}, {emo_proud}, cried. {farmer} smiled.
"No — the chalk marks are not the form. The form is the steps below. The marks explain them. To {goal_text},
we use {concept_phrase} to make the form clear — so anyone walking past can understand the plan without being
confused by the milk's flow. The marks are scaffolding; the form is the house."
"""),

    SubplotTemplate("""\
{farmer} handed {milkmaid} a piece of chalk. "Write a mark above the churn," {farmer_he_she}, {emo_patient}, said,
"that says what we are about to do." {milkmaid} wrote: "Cooling the cream." Then {farmer_he_she} showed the
form. "See? The mark prepares the reader. When the reader sees the form for {concept_phrase}, the mark has
already told them the purpose. The form is clear because the chalk went first. The mark changes nothing about
the milk — it only helps the reader's understanding."
"""),

    SubplotTemplate("""\
{milkmaid} studied the wall and said, "These chalk marks confuse me — there are too many!" {farmer}, {emo_patient}
nodded. "Then we remove the marks that do not help. To {goal_text}, we write chalk marks that serve the reader.
Each mark should say one thing clearly. The form {concept_phrase} the same way whether the mark says 'chilling'
or 'the cream is cold' — but one mark helps the reader understand the purpose, and the other only clouds it.
Choose {concept_phrase} wisely."
"""),

    SubplotTemplate("""\
One morning, {milkmaid} arrived to find a form with no chalk marks at all — just steps written in a jumble.
"Is this form broken?" {milkmaid_he_she_cap}, {emo_proud}, asked. {farmer} said, "The form works. It {concept_phrase}
correctly. But without chalk marks to guide the reader, no one knows why each step is there. To {goal_text},
we write {concept_phrase} to make the form's intention clear. The form itself will not change — only the reader's
understanding will. A good dairy wall has both milk and marks; a good form has both code and clarity."
"""),
]


# ─────────────────────── chalk mark on the pail vs the milk inside (quote / symbols / syntax-quote) ──────────

_CHALKMARK_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, held up a pail with a chalk mark on its side — the word
"cream" written in white. "Is this cream?" {milkmaid_he_she_cap} asked, pointing at the chalk
mark. {farmer} laughed gently. "No. The chalk mark is the name — the label
on the pail. The cream is the warm milk inside. To {goal_text}, we use {concept_phrase} to
get the chalk mark — the name itself, not the value inside. If you want the milk, you open
the pail. If you want the label, you look at what the form produced. The chalk mark and the
milk are not the same."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_boastful} peered at the pail and said, "I know what is inside — I read it on the label!" But {farmer_he_she}
replied, "The label says 'cream,' but is the label cream? No. To {goal_text}, {concept_phrase} gives you what
is written on the label — the mark, not the contents. If you want to use the cream inside, you must take off
the label and open the pail. The form you write determines whether you get the chalk mark or the milk, the
name or the value."
"""),

    SubplotTemplate("""\
{farmer} held two pails side by side. One had "butter" chalked on it; the other held actual butter.
{milkmaid_he_she_cap} touched the chalk mark and asked, "Is this butter?" {farmer_he_she_cap}, {emo_patient}, said, "That is the
chalk mark — the word. This is the butter." {farmer_he_she_cap} pointed to the pail's contents. "To {goal_text},
write a form with {concept_phrase}. The form returns the chalk mark — the symbol, the name. It does not
return what is inside the pail. The two are different. The chalk mark is the address; the milk is the treasure
at that address."
"""),

    SubplotTemplate("""\
{milkmaid} claimed, {emo_proud}, "I can {goal_text} without opening the pail — I'll
just read the label!" {farmer_he_she_cap} tapped the pail, the wood cool and heavy under the
chalk mark, and replied, "Then {concept_phrase} is your answer. The form reads
the chalk mark, not the milk inside; a label is light, the pail is heavy, and the two are not the
same. If you want to use the milk — to churn it, to drink it — you must open the pail and lift
its weight. The chalk mark is useful for knowing what is inside without lifting; {concept_phrase}
makes that distinction clear: you have the name, not the value; the label, not the contents."
"""),

    SubplotTemplate("""\
One day, {milkmaid} arrived with a stack of pails, each chalked with a different name: "cream," "skim," "butter,"
"curds." {milkmaid_he_she_cap} pointed at one and guessed, "This pail contains butter." {farmer_he_she_cap} asked,
"Did you open it?" {milkmaid_he_she_cap}, {emo_proud}, said no. {farmer} said, "Then you know only the chalk mark. To
{goal_text}, {concept_phrase} lets you work with the marks — the names on the pails. The form you write
decides whether to return the chalk mark itself or to open the pail and take out the milk inside. Choose carefully:
are you reading the label or the contents?"
"""),
]


# ─────────────────────── sorting table at the dairy (multimethods / defmulti / defmethod) ──────────────

_SORTINGTABLE_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
The sorting table at the dairy had three shelves, each marked with a stamp: one shelf for cream, one for skim,
one for butter. {milkmaid_he_she_cap} poured a batch of milk onto the table, and it rolled down a chute toward
the shelves. A stamp appeared on the batch — "cream" — and the milk rolled to the cream shelf. {milkmaid_he_she_cap}
asked, "How did it know where to go?" {farmer_he_she_cap}, {emo_patient}, explained, "The table reads the stamp and routes the batch
accordingly. To {goal_text}, we use {concept_phrase} — the form that says: if the stamp is 'cream,' go to
shelf one; if 'skim,' go to shelf two. The table does not decide. The stamp on the batch decides, and the table
routes. Each stamp has its own shelf."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, tried to pour a batch onto the sorting table, but there was no stamp on it. The batch
rolled back and forth, confused, refusing to settle on any shelf. {farmer_he_she_cap} arrived and said, "Every batch
needs a stamp. To {goal_text}, the table must know what kind of milk it is. We use {concept_phrase} — the
form that asks: 'What is the stamp?' The batch must answer. Once it does, the table knows which shelf to send
it to. Without a stamp, the table cannot route, and the milk cannot flow."
"""),

    SubplotTemplate("""\
{farmer} showed {milkmaid} a new batch that had a strange stamp: "whey." {milkmaid_he_she_cap}, {emo_proud}, asked,
"Where does whey go?" {farmer_he_she_cap} smiled. "Good question. The table already has three shelves, but not
one for whey. So we add a new shelf and teach the table: if the stamp says 'whey,' send it here. {concept_phrase}
lets us extend the table — add new shelves for new stamps without rewriting the old routing rules. The table grows
as the dairy grows."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, claimed, "I can guess where each batch should go without looking at its stamp!" {farmer_he_she_cap}
asked calmly, "Then show me the sorting table you have built. Where is the code that reads the stamp and routes
the milk?" {milkmaid_he_she_cap} had no answer. {farmer_he_she_cap} continued, "{concept_phrase} is the table's
logic — the rules written in form. Each rule says: 'If you see this stamp, do this.' The table is not a guess.
It is a form with routes written out, one for each kind of milk."
"""),

    SubplotTemplate("""\
One morning, three batches arrived at the sorting table at once: cream, skim, and butter. Each had a different
stamp. {farmer_he_she_cap} showed {milkmaid} the form for {concept_phrase}. {milkmaid_he_she_cap} watched
as the form read the first batch's stamp, sent it to the cream shelf. Then it read the second batch's stamp, sent
it to the skim shelf. Then the third — to butter. "The table sorted all three, and each one went to the right
place," {milkmaid_he_she}, {emo_proud}, said in wonder. {farmer_he_she_cap} replied, "{concept_phrase} does not care how many
batches arrive. Each one is routed by its stamp. That is the power of the table — many stamps, same rules."
"""),
]


# ─────────────────────── pail itself (deftype / defrecord) ──────────────────────────────────────

_CARRYINGCASE_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{milkmaid} needed a new kind of pail — one that held not just milk but also a label and a weight.
The old pails would not work. So {farmer_he_she}, {emo_patient}, said, "To {goal_text}, we must define a pail before we
use it. {concept_phrase} is the form that says: 'A pail of this kind has these compartments — a label here,
milk there, a weight tag on the side.' Once the form is written and submitted, we can create pails of that
kind, fill them, and carry them. The pail itself is defined before it can hold anything."
"""),

    SubplotTemplate("""\
{milkmaid} reached for a pail {farmer} had never seen before. "What kind of pail is this?" {milkmaid_he_she_cap}
asked. {farmer}, {emo_patient}, said, "I defined it yesterday. {concept_phrase} — the form that says: 'This pail
holds a cow's name, the date it was milked, and the volume.' The pail is not a guess. It has structure, written
by a form. Every pail of this kind has the same compartments in the same order. To use it, you must know the
form that defined it."
"""),

    SubplotTemplate("""\
{farmer} showed {milkmaid}, {emo_boastful} a pail and explained its structure. "This pail has three slots: one for
the milk type, one for the volume, and one for the dairy's name. {concept_phrase} is the form that creates
pails with this exact structure. You cannot create a pail without the form. And you cannot add a fourth slot
unless you define a new kind of pail with a new form."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, tried to fill a pail, but it had no shape — it collapsed under the milk's weight. {farmer}
arrived and said, "You cannot use a pail that has not been defined. {concept_phrase} is the form that gives
the pail its structure — the compartments, the labels, the walls that hold the milk upright. Write the form,
submit it, and then create pails of that kind. The form comes first; the pails come after."
"""),

    SubplotTemplate("""\
One afternoon, {farmer_he_she} created two different kinds of pails. One {concept_phrase} held milk,
date, and cow-name. The other held milk, volume, and destination. {milkmaid_he_she_cap}, {emo_proud}, looked at both and
asked, "Are these the same pail?" {farmer_he_she_cap} said, "No. Each form {concept_phrase} creates pails with
a different structure. The first pail remembers the cow. The second pail tracks the destination. Both are
pails, but they are defined by different forms. The form is the blueprint; the pails are the houses built
from that blueprint."
"""),
]


# ─────────────────────── walking to market counting coins (reduce / count) ────────────────────

_TALLYWALK_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{milkmaid} walked the long road to market, and at each milestone stood a coin-bag. {milkmaid_he_she_cap}
started with zero coins in hand. At the first milestone, {milkmaid_he_she} picked up a bag and added its coins
to the running total. At the second milestone, {milkmaid_he_she} added those coins too. At each step,
{milkmaid_he_she} carried forward the tally. By the time {milkmaid_he_she} reached the market, the total was
the sum of all the bags. {farmer_he_she_cap}, {emo_patient}, explained, "{concept_phrase} is this walk — you carry the tally
with you at each step, adding each new bag's coins to what you already hold. To {goal_text}, the farmer's
form walks the same path, tallying as it goes."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, asked, "How do you know how many coins you will have when you reach the market?" {farmer_he_she_cap}
replied, "Walk the road. At each milestone, add the bag's coins to what you already have. {concept_phrase}
is that walk — it starts with an empty hand (or a starting value), and as it steps through the coin-bags,
it carries the tally forward. When the walk ends, the final tally is what {goal_text} becomes. The form
does not guess; it counts step by step."
"""),

    SubplotTemplate("""\
{farmer} showed {milkmaid} a form for {concept_phrase}. {milkmaid_he_she_cap} watched as the
form stepped through a line of coin-bags, adding each one's value to the running total. "The form carries the
tally with it the whole way," {milkmaid_he_she} observed. {farmer_he_she_cap}, {emo_patient}, nodded. "Exactly. That is how to
{goal_text} — walk the path, carry the count forward with each step, and submit the final tally when the
walk is done."
"""),

    SubplotTemplate("""\
{milkmaid} arrived at the market breathless. "How many coins do I have?" {farmer_he_she_cap}, {emo_patient}, asked.
{milkmaid_he_she_cap} counted on {milkmaid_his_her} fingers, looking back at each milestone. "I picked up bags at
five milestones. I counted them all together..." Finally, {milkmaid_he_she} arrived at a number. {farmer_he_she_cap}
smiled. "That is {goal_text} — you walked the path, tallied the coins, and produced a number. {concept_phrase}
does this form in code. The form walks the coin-bags and returns the final tally."
"""),
]


# ─────────────────────── braiding the cheesecloth (str concat / subs / string length) ──────────

_BEADSTRING_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
{milkmaid} stood at the dairy with a roll of cheesecloth and began to braid it. One strand went left,
one went right, and as {milkmaid_he_she} braided, the cloth grew longer and more intricate. "What are you doing?"
{farmer_he_she_cap} asked. {milkmaid_he_she_cap}, {emo_proud}, replied, "I am braiding the cloth — weaving the strands together so
they become one piece." {farmer_he_she_cap} said, "Good. To {goal_text}, {concept_phrase} is like braiding.
You take separate strands — separate strings — and weave them together in order. The result is a longer cloth,
made from the pieces you braided. Each strand in its place, woven tight."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, asked, "Can I take a piece of the braided cloth?" {farmer_he_she_cap} showed {milkmaid} the braid and
said, "Yes. If the braid says 'morning-walk-to-dairy,' and you want only the 'walk' part, {concept_phrase}
lets you cut it out. You say: start at position 6, take 4 characters. The result is 'walk' — a piece of the
whole braid. The original braid remains intact, and you have a sub-braid in hand."
"""),

    SubplotTemplate("""\
{farmer} held a long braided cheesecloth and measured it with {farmer_his_her} hands. "This braid
is twelve hands long," {farmer_he_she} said. {milkmaid_he_she_cap}, {emo_proud}, asked, "How do you know?" {farmer_he_she_cap}
replied, "I counted each hand-span. {concept_phrase} — the form that tells us the braid's length. The form
examines the cloth from end to end and returns the number. The braid itself does not change. We only measure it."
"""),
]


# ─────────────────────── the daily milking round (recur / loop) ──────────────────────────────

_CIRCUIT_SUBPLOTS: list[SubplotTemplate] = [

    SubplotTemplate("""\
Every morning, {milkmaid}, {emo_boastful} walked the same path: from the barn to the first cow, then to the second, then to
the third, and back to the barn. The path was a circuit — the same route each day, no new trail added. {farmer_he_she_cap}
explained, "To {goal_text}, {concept_phrase} is like the circuit. The form walks the loop, completes one
round, then walks it again from the start, without growing taller or longer. No new call added to the stack. The
form repeats the same steps in a loop, compact and efficient, just as the milkmaid's round is always the same path."
"""),

    SubplotTemplate("""\
{milkmaid}, {emo_proud}, asked, "If I walk the circuit every morning, will the path get longer and longer?" {farmer}
shook {farmer_his_her} head. "No. The circuit returns you to the barn each time. The next morning, you walk the
same path again. {concept_phrase} does this in the form — it loops back to the start without adding steps to a
growing stack. The form stays compact, memory stays light, and the work repeats until the form says 'enough.'"
"""),

    SubplotTemplate("""\
{farmer} showed {milkmaid} a form for {concept_phrase} — a loop that milked each cow in turn, then
looped back to the first cow to milk it again. "The form does not climb a hill of calls," {farmer_he_she}, {emo_patient}, said.
"It walks the circuit: milk cow one, milk cow two, milk cow three, back to cow one. Each lap is like the milkmaid's
morning round — the same steps, no height gained. To {goal_text}, use {concept_phrase} and the form will loop
without growing the call stack."
"""),
]


# ─────────────────────── Phase C: story-scaffold templates ───────────────────────────────
#
# Each SubjectExample that has all four story-scaffold slots
# (scenario / need / mapping / resolution) plus tags=("story",)
# will trigger one of these templates via fits_tags matching.
#
# The 5-act structure:
#   Act 1 (SETUP):       {scenario}
#   Act 2 (NEED):        {need}
#   Act 3 (MAPPING):     {mapping}
#   Act 4 (ACTION):      family connective prose + {concept_phrase}
#   Act 5 (RESOLUTION):  {resolution}


def _story(connective_prose: str) -> SubplotTemplate:
    """Build a story-scaffold template for a milkmaid family.

    The family differentiates itself only via the connective prose around
    the composed/submitted action — using the family's verb and imagery.
    """
    return SubplotTemplate(f"""\
{{scenario}}

{{need}}

{{mapping}}

{connective_prose}

{{resolution}}""", fits_tags=("story",))


_POUCH_SUBPLOTS = _POUCH_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "with the value tucked into the apron-pocket and submitted the "
        "form. The REPL reached into the pocket as the form directed:"
    ),
]

_RECIPE_SUBPLOTS = _RECIPE_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} wrote out {concept_phrase} "
        "on the pail-steps card and submitted the form. The REPL ran the "
        "steps end to end:"
    ),
]

_BASKET_SUBPLOTS = _BASKET_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "for the market-basket and submitted the form. The REPL handed "
        "back the arrangement:"
    ),
]

_SIEVE_SUBPLOTS = _SIEVE_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "as the strainer's rule, poured the input through, and submitted "
        "the form. The REPL caught what passed the sieve:"
    ),
]

_NOTEBOOK_SUBPLOTS = _NOTEBOOK_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "for the tally-slate and submitted the form. The REPL chalked the "
        "update on the slate:"
    ),
]

_ACORN_SUBPLOTS = _ACORN_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL counted out the coins:"
    ),
]

_GATE_SUBPLOTS = _GATE_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL let the gate decide:"
    ),
]

_FORK_SUBPLOTS = _FORK_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL took the right lane:"
    ),
]

_ROADSIGN_SUBPLOTS = _ROADSIGN_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL read the market-board and "
        "replied:"
    ),
]

_SAFETYNET_SUBPLOTS = _SAFETYNET_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL — pail balanced, walk steady "
        "— handed back the value:"
    ),
]

_SCROLL_SUBPLOTS = _SCROLL_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL — slip in hand — completed the "
        "market order:"
    ),
]

_GUILD_SUBPLOTS = _GUILD_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL — checking the guild roll — "
        "dispatched to the right member:"
    ),
]

_SORTINGTABLE_SUBPLOTS = _SORTINGTABLE_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL routed the pail through the "
        "sorting table:"
    ),
]

_CARRYINGCASE_SUBPLOTS = _CARRYINGCASE_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL stamped the pail into shape:"
    ),
]

_TOOLSHED_SUBPLOTS = _TOOLSHED_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL — borrowing the neighbor's "
        "stool — returned:"
    ),
]

_RUNNERAHEAD_SUBPLOTS = _RUNNERAHEAD_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL waited at the gate for the "
        "runner to return:"
    ),
]

_REWRITERULE_SUBPLOTS = _REWRITERULE_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL — expanding the rewrite first, "
        "then evaluating — returned:"
    ),
]

_SCRIBE_SUBPLOTS = _SCRIBE_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL read past the chalk marks and "
        "returned:"
    ),
]

_CHALKMARK_SUBPLOTS = _CHALKMARK_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL — reading the pail, not the "
        "chalk — returned:"
    ),
]

_TALLYWALK_SUBPLOTS = _TALLYWALK_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL walked the collection carrying "
        "the tally:"
    ),
]

_BEADSTRING_SUBPLOTS = _BEADSTRING_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL braided the cheesecloth as "
        "the form said:"
    ),
]

_CIRCUIT_SUBPLOTS = _CIRCUIT_SUBPLOTS + [
    _story(
        "To {goal_text}, {farmer_he_she} composed {concept_phrase} "
        "and submitted the form. The REPL looped the round without "
        "growing the trail:"
    ),
]

