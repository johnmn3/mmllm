# Milkmaid — Phase 1 imagery mapping

## Fable summary

The Milkmaid carries a pail of milk on her head to market, dreaming of
all the wealth it will bring. Lost in daydreams, she nods her head; the
pail falls; the milk is lost. Moral: don't count your chickens before
they hatch. Don't guess at what the REPL will return before you submit.

## Cast

| Role | Character | Analog |
|---|---|---|
| Dreamer (guesser) | **milkmaid** (Margery / Lila / Clara / Nan / Bess) | hare / grasshopper |
| Patient evaluator | **farmer** (Godfrey / Aldric / Mabel / Rowan / Edna) | tortoise / ant |
| Central prop | **the milk pail** | the unevaluated form |

The pail balanced on the milkmaid's head **is the form held in mind
without being submitted**. Daydreaming about what it might return =
guessing at the answer = nodding your head = spilling the pail.
Getting to market and exchanging the milk = evaluating the form and
reading the REPL's actual return value.

## Locations

Road, meadow, hilltop, farm, market, orchard, village.
These are the existing ontology locations that fit the milkmaid's
journey from dairy to market.

`MILKMAID_LOCATIONS = ("road", "meadow", "hilltop",
                       "farm", "market", "orchard", "village")`

## Imagery mapping — 22 metaphor families

| Family | Tortoise-hare imagery | Milkmaid imagery |
|---|---|---|
| `_POUCH_SUBPLOTS` | small leather pouch at hip | **apron-pocket** sewn to the milking apron; holds a value for one stretch of the road |
| `_RECIPE_SUBPLOTS` | recipe-card on the road | **pail-steps card**: the written routine for each dairy round (one instruction per step) |
| `_BASKET_SUBPLOTS` | foraging-basket on the path | **market-basket** on the arm; compartments for cream, skim, curds — original pail untouched |
| `_SIEVE_SUBPLOTS` | sieve over empty basket | **milk-strainer** over the pail; the rule decides what passes into the fresh pail |
| `_NOTEBOOK_SUBPLOTS` | notebook on a tree stump | **tally-slate** hung by the dairy door; records each day's count, updated carefully |
| `_ACORN_SUBPLOTS` | counting / adding acorns | **counting / stacking coins** (milk money); the farmer tallies each penny earned |
| `_GATE_SUBPLOTS` | gates on the trail | **farmyard gate**: first closed gate stops the chain; the gate rule decides which path opens |
| `_FORK_SUBPLOTS` | fork at a crossroads | **fork in the road to market**: condition decides which lane the milkmaid takes |
| `_ROADSIGN_SUBPLOTS` | posted sign on road | **market-board** at the village square; prices posted for any buyer to read |
| `_SAFETYNET_SUBPLOTS` | net under the leap | **steady, careful walk**: the pail stays full only if you don't rush — the "safety" is in patience |
| `_SCROLL_SUBPLOTS` | scrolls written and read | **market order** written on a slip of paper; the buyer's requirements recorded and read back |
| `_GUILD_SUBPLOTS` | guild any species can join | **market guild**: any dairy farmer may join; each member's call produces their own milk variety |
| `_TOOLSHED_SUBPLOTS` | borrowing tool from another toolshed | **borrowing a neighbor farmer's milking stool**; different farm, same milking technique |
| `_RUNNERAHEAD_SUBPLOTS` | sending a runner down the road | **sending a message ahead to the buyer**: the answer arrives before the pail does |
| `_REWRITERULE_SUBPLOTS` | scribe rewrites recipe before runtime | **rewriting the daydream before it solidifies**: the farmer rewrites the milkmaid's plan before she nods and spills |
| `_SCRIBE_SUBPLOTS` | scribe's reading conventions | **chalk marks on the dairy wall**: the scribe's shorthand for the day's plan |
| `_CHALKMARK_SUBPLOTS` | chalk mark on bark vs the acorn it names | **chalk mark on the pail** vs the milk inside: the name is not the value |
| `_SORTINGTABLE_SUBPLOTS` | sorting-table routing by tag | **sorting cream / skim / butter** at the dairy; each variety routed by its stamp |
| `_CARRYINGCASE_SUBPLOTS` | labeled carrying-case | **the pail itself**, labeled by its contents; the milkmaid's custom container |
| `_TALLYWALK_SUBPLOTS` | walking the row with running tally | **walking to market**, coin-counting with each step; a running total of the day's earnings |
| `_BEADSTRING_SUBPLOTS` | strings as strings of beads | **braiding the cheesecloth**: a string of dairy operations woven together in order |
| `_CIRCUIT_SUBPLOTS` | looping without growing the trail | **the daily milking round**: the same path walked again each morning, compact and repeating |
| `_GOAL_SUBPLOTS` (fallback) | generic Hare-vs-Tortoise | generic milkmaid-vs-farmer: farmer insists on evaluating the form; milkmaid would rather daydream |

## Central narrative beats

The 8 standard subplot patterns, milkmaid-adapted:

1. **Argument** — farmer and milkmaid disagree about what the form returns; farmer insists on submitting it
2. **Wager** — milkmaid bets she knows the form's value without trying; farmer says "submit first"
3. **Teacher** — farmer shows milkmaid how to translate a goal into a form and submit it
4. **Audience** — market-goers watch milkmaid try to outwit the farmer at writing the right form
5. **Pail-pause** (fable-specific) — milkmaid stops on the road to market to settle a REPL question; the pail stays balanced while she focuses
6. **Tally-slate / ledger** — farmer keeps a careful slate of goals and their forms
7. **Boast-and-rebuke** — milkmaid claims she can answer without the REPL; farmer asks for the actual form
8. **Market-board puzzle** — the market board posts a goal as a puzzle; whoever writes the right form gets the contract

## Prop inventory (for template authors)

Use these props freely — they're all canonical milkmaid-world objects:

- **pail** (milk pail balanced on head)
- **apron** (with apron-pocket)
- **market road** / **path**
- **tally-slate** (hung by the dairy door)
- **market-board** (village-square posting board)
- **cheese-cloth** / **strainer**
- **coins** / **penny**
- **dairy door** / **farmyard gate**
- **slip of paper** (market order)
- **chalk** (for marking)
- **milking stool**
