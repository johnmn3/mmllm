# Metaphor imagery — fox-grapes curriculum

This is the Phase 1 planning artifact: for each of the 22 metaphor
families (defined in tortoise-hare's `_metaphor_pools.py`), what
concrete imagery in the fox-grapes world carries it.

The semantic structure of each family is **fixed across fables.**
Only the imagery changes. Same family of metaphor, different
storytelling materials.

## The fox-grapes world

- **Characters:** two foxes per record — the hasty fox (rationalizer)
  and the patient fox (eval-first evaluator). Names from
  Renard (m) / Vix (f) / Sly (n).
- **Locations:** orchard, garden, farm, market, meadow, woods, forest.
- **Daily props:** grape-vines on trellises, fruit-crates, baskets,
  scales, wooden posts, fences, gates, tasting-cards, the patient
  fox's leather ledger, chalk marks on posts, the stone tool-shed
  at the orchard's edge, harvest-parchments tied to the fence.
- **Moral:** *rationalizing the unattainable as undesirable.* The
  hasty fox skips the form and declares the prize sour; the patient
  fox composes the form, submits it to the REPL, and accepts
  whatever returns.

## Imagery table

| # | Family | Tortoise-hare imagery | Fox-grapes imagery |
| - | ------ | --------------------- | ------------------ |
|  1 | `_POUCH_SUBPLOTS` | small leather pouch tied at hip — holds for one stretch of road | small **berry-pouch** tied at the fox's belt — holds one cluster's worth between trellis and basket. By the time the fox sets it down, the pouch is empty again. (`let`-binding scope.) |
|  2 | `_RECIPE_SUBPLOTS` | recipe-card on the road | **tasting-card** pinned on the orchard post — names the paw-step routine to grade a cluster, press a wine, prepare a tray. Last step is what's served. (`fn` / `defn` / `comp` / `partial`.) |
|  3 | `_BASKET_SUBPLOTS` | foraging-basket with compartments | **vine-tray with named slots** — fixed-order compartments for picked clusters; the order at picking time is the order in the basket. (Vectors / lists / maps / sets.) |
|  4 | `_SIEVE_SUBPLOTS` | sieve over an empty basket | **grape-sieve** held over a stave-bucket — same operation applied to every grape that passes through. Ripe through, green retained; first-five caught; filter-by-color separates. (`map` / `filter` / `take` / `drop` / transducers.) |
|  5 | `_NOTEBOOK_SUBPLOTS` | notebook on a tree stump | **leather ledger on the orchard wall** — every successful form is written in. Swap-in a new tally means crossing out and rewriting on a new line, atomically. (Already established in fox-grapes' subplot pool.) (`atom` / `ref` / `swap!` / CAS.) |
|  6 | `_ACORN_SUBPLOTS` | counting/adding acorns | counting/adding **grapes** (or whole clusters) — arithmetic visualised as fox-tally on the slate. Same simple-tally feel as tortoise-hare's acorns. |
|  7 | `_GATE_SUBPLOTS` | gates on the trail | **orchard gate with two latches** — both must lift for `and`; either lifts for `or`; the last latch's verdict stands. The orchard's outer gate guards passage to the next plot. (`and` / `or` / `not` / falsey rules.) |
|  8 | `_FORK_SUBPLOTS` | fork at a crossroads | **fork in the orchard path** — left to the vine-row, right to the market. The fox must decide which prong by reading the test. (`if` / `cond` / `case` / `when`.) |
|  9 | `_ROADSIGN_SUBPLOTS` | posted signs on the road | **vine-post nameplates** — chalked sign on the post that says what's growing here ("ripeness", "muscat"). Declared once, persists for the season. (`def` / `namespace` / `require`.) |
| 10 | `_SAFETYNET_SUBPLOTS` | safety net | **catching-cloth** strung between two orchard trees — when a falling grape drops (an error throws), the cloth catches it and the patient fox handles it gently rather than letting it splatter. (`try` / `catch` / `throw` / `assert`.) |
| 11 | `_SCROLL_SUBPLOTS` | scrolls written and read | **harvest-parchments tied to the fence** — records of yields, weights, colors. Slurp a parchment to read; spit a new one to write. (IO / metadata / `slurp` / `spit`.) |
| 12 | `_GUILD_SUBPLOTS` | guild any species can join | **orchard-keeper guild** — any animal that gathers can join (fox, sparrow, hedgehog, badger). Each defines its own `gather` method but the guild's contract is shared. (Protocols.) |
| 13 | `_TOOLSHED_SUBPLOTS` | borrowing a tool from another toolshed | borrowing a **pruning-shear / ladder / pressing-stone** from the **stone tool-shed** at the orchard's edge — tools that belong to another household but the orchard borrows. (Host interop.) |
| 14 | `_RUNNERAHEAD_SUBPLOTS` | sending a runner down the road | **sending a swift fox ahead to the market** — fetches the verdict before the patient fox arrives at the stall. (`agent` / `future` / `promise` / `await`.) |
| 15 | `_REWRITERULE_SUBPLOTS` | scribe with the power to rewrite the recipe | the patient fox **rewriting the tasting-card** before it's followed — adds steps, conditionally inserts checks, expands shorthand into full prose. The card is rewritten before it's read. (Macros.) |
| 16 | `_SCRIBE_SUBPLOTS` | scribe's reading conventions | the patient fox's **marginalia in the ledger** — notes that don't change the harvest count but help the reader. The reader skips them; the form runs anyway. (Comments / whitespace / parens / `do` / reader.) |
| 17 | `_CHALKMARK_SUBPLOTS` | chalk mark on bark vs the acorn it names | **chalk tag on the vine-post vs the grape-cluster it names** — the tag reads "ripeness" but it isn't actually ripeness, only a name standing for it. (`quote` / symbols / syntax-quote.) |
| 18 | `_SORTINGTABLE_SUBPLOTS` | sorting-table that routes by tag | **sorting-tray at the market** that routes grapes by color or kind — green to the green box, purple to the purple box. Anyone can add a new color tag without rebuilding the tray. (Multimethods.) |
| 19 | `_CARRYINGCASE_SUBPLOTS` | labeled carrying-case | labeled **fruit-crate** — has named compartments (`:weight`, `:color`, `:vine`); each crate is its own type but all share the same shape. (`deftype` / `defrecord`.) |
| 20 | `_TALLYWALK_SUBPLOTS` | walking the row carrying a running tally | walking the **vine-row tallying clusters** — pass each vine, add its cluster-count to the running tally on the slate, end at the row's end with the total. (`reduce` / `count`.) |
| 21 | `_BEADSTRING_SUBPLOTS` | strings as strings of beads | strings as **strings of beads on the market-fox's counting-cord** — characters threaded together, slice-able by position; strung head-to-tail. (`str` concat / `subs`.) |
| 22 | `_CIRCUIT_SUBPLOTS` | looping back without growing the trail | walking **back to the start of the vine-row** each pass — `recur` means starting over at the head of the row with the new tally, not stacking new walks on top of the old. (`recur` / `loop`.) |

## Coherence check

Every prop above lives in the orchard / vineyard / farm / market
world the existing fox-grapes subplots already inhabit. The patient
fox's leather ledger is the same ledger across families (notebook,
scribe, tallywalk all touch it). The vine-post carries both the
roadsign nameplate and the chalkmark tag. The sorting-tray and
fruit-crate both belong at the market. The catching-cloth and
guild and tool-shed all sit at the orchard's edges.

This consistency is the point: the model meets the same prop
across many idioms, and the metaphor accumulates rather than
fragmenting.

## Pool-name constancy

The 22 metaphor family names are **constant across fables.** All
three of `tortoise_hare/_metaphor_pools.py`,
`ant_grasshopper/_metaphor_pools.py`,
`fox_grapes/_metaphor_pools.py` will export `_POUCH_SUBPLOTS`,
`_RECIPE_SUBPLOTS`, etc. Subjects in any grade file import the
pool from their fable's module — the family name doesn't change,
only the imagery inside.
