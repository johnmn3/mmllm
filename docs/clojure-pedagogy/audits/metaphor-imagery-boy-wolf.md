# Boy-wolf metaphor imagery mapping

Phase 1 artifact for the boy-wolf Phase C rebuild. Maps each of the 22
metaphor families to boy-wolf-flavored imagery. Imagery picks props
that all live in **one consistent world** — the valley, hillside
pasture, fold, watchhouse, village green, elder's slate. Same family
*structure* as tortoise-hare; different storytelling materials.

## The boy-wolf world

Setting: a hillside pasture overlooking a valley village. The shepherd
watches the flock by day from a stone lookout; the village is a short
run downhill. Props belong to either the shepherd's working life
(crook, horn, belt-pouch, tally-stick) or the village's record-keeping
(elder's slate, watchhouse log, notice-post, fold-gates).

Polarity: the **shepherd** is the cautionary character (the boy who
cried wolf — guesses, shouts, claims he just *knows*). The **elder**
is the corrective voice (writes the form, lets the runtime decide).

## Family → imagery

| Family                   | Idiom                                      | Boy-wolf imagery |
| ------------------------ | ------------------------------------------ | ---------------- |
| `_POUCH_SUBPLOTS`        | `let` — temporary container                | **shepherd's belt-pouch** at the apron-strap; tally-token tucked in for one stretch of watch, empty by the next fold |
| `_RECIPE_SUBPLOTS`       | `fn`/`defn`/`comp`/`partial`               | **drill-card on the watchhouse wall** — a named alarm/watch routine the elder posts; the village follows the steps |
| `_BASKET_SUBPLOTS`       | collections / immutability                 | **wool-basket with named pouches** — sorted by fleece, dye, or shepherd; original sits untouched, fresh basket returned |
| `_SIEVE_SUBPLOTS`        | `map`/`filter`/`take`/transducers          | **fleece-comb / wool-screen** — fleeces poured through, only those passing the rule land in the basket below |
| `_NOTEBOOK_SUBPLOTS`     | `atom`/`ref`/`swap!`/CAS                   | **watchhouse slate** — single shared running tally; shepherds erase and rewrite the count atomically |
| `_ACORN_SUBPLOTS`        | arithmetic                                 | **counting sheep / weighing fleeces** — morning flock, evening flock, the difference; coins paid for wool |
| `_GATE_SUBPLOTS`         | `and`/`or`/falsey                          | **fold-gates** — a chain of three stone gates from pasture to the fold; first closed gate stops the chain |
| `_FORK_SUBPLOTS`         | `if`/`cond`/`case`/`when`                  | **path-fork at the lookout** — three paths fan out from the stone lookout (village, fold, pasture); condition picks one |
| `_ROADSIGN_SUBPLOTS`     | `def` / namespace / `require`              | **village notice-post** — a tall pole at the crossroads where the elder pins named notices; library of pinned scrolls |
| `_SAFETYNET_SUBPLOTS`    | `try`/`catch`/`throw`/assert               | **practice-pen behind the watchhouse** — drills cost nothing here; cried-wolf gets *caught* not believed; the elder turns mistakes into lessons |
| `_SCROLL_SUBPLOTS`       | IO / metadata / `slurp`/`spit`             | **village log-book** — leather-bound, kept by the elder; watch-roll scrolls written and read; marginalia in the elder's hand |
| `_GUILD_SUBPLOTS`        | protocols                                  | **shepherds' fellowship** — sheep-shepherd, goat-shepherd, geese-keeper all join; each implements "raise alarm" its own way (horn, bell, smoke) |
| `_TOOLSHED_SUBPLOTS`     | host interop                               | **village smithy / cooper's shed** — the shepherd borrows the smith's hammer or the cooper's barrel using the foreign shed's specific calls |
| `_RUNNERAHEAD_SUBPLOTS`  | `agent`/`future`/`promise`                 | **dispatched child-runner** — a village child sent down the path with a message; come back later for the elder's reply |
| `_REWRITERULE_SUBPLOTS`  | macros                                     | **elder's drill-card rewrite** — when the shepherd writes the shorthand `alarm-three`, the elder rewrites it as the full sequence (horn, beacon, fold) before runtime sees it |
| `_SCRIBE_SUBPLOTS`       | comments / whitespace / parens / reader    | **slate-and-chalk conventions** — blank line separates entries; dashed line is a note (comment); brackets group; the elder's reading rules |
| `_CHALKMARK_SUBPLOTS`    | `quote` / symbols                          | **chalk mark on the slate** vs **the sheep it names** — the symbol `bell` is the chalk mark; the bell is the bell. Quote stops the substitution |
| `_SORTINGTABLE_SUBPLOTS` | multimethods                               | **brand-sorting gate at the fold** — each sheep wears a brand (south, north, lambing); the gate routes by brand to the right pen |
| `_CARRYINGCASE_SUBPLOTS` | `deftype`/`defrecord`                      | **labeled tally-box** — a small wooden box with named pigeon-holes (count, weight, breed) for each sheep's record |
| `_TALLYWALK_SUBPLOTS`    | `reduce` / `count`                         | **tally-stick walk** — the shepherd walks past each sheep notching the wooden tally-stick once per sheep; the running total grows knot by knot |
| `_BEADSTRING_SUBPLOTS`   | string ops                                 | **knotted tally-cord** — a cord with knots tied at intervals; can be spliced or counted bead by bead |
| `_CIRCUIT_SUBPLOTS`      | `recur` / `loop`                           | **dawn fence-walk** — the shepherd walks the same fence-line each dawn; same circuit, no growing trail behind |

## Fallback

`_GOAL_SUBPLOTS` keeps the generic shepherd-vs-elder banter for the
~36 abstract subjects (host platforms, library design, build tools)
where forcing pastoral imagery would be cargo-cult.

## Internal coherence

These props all sit in one valley:

- **Pasture & fold:** crook, horn, belt-pouch, fold-gates, fence-line,
  tally-stick, tally-cord, lambing-pen
- **Watchhouse:** slate, drill-card, log-book, watch-roll, practice-pen
- **Village:** notice-post, smithy, cooper's shed, child-runner, the
  elder's hand on the slate
- **Materials:** chalk, wax, leather, wool, fleece, stone, parchment

A render that uses pouch-imagery and slate-imagery and fold-gate-imagery
together feels like *one place* — same kind of internal coherence
tortoise-hare gets from "everything sits on the meadow path."

## Polarity reminder

Boy-wolf flips the typical fable polarity: the named protagonist
(shepherd) is the one who *gets it wrong*; the elder is the
corrective voice. Templates should preserve this — the shepherd's
"I just *know* the answer" is what the elder corrects with "write
the form, let the runtime decide." This polarity is already wired
into existing boy-wolf templates and BW_EMO pools; preserve it
across the new metaphor families.
