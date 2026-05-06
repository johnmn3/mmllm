# Boy-wolf semantic coverage — gap report

**Snapshot after Phase C framework rebuild.**

Mirrors the tortoise-hare coverage report format.

## Where we are

| Slice | Subjects | Examples | Story slots authored |
| --- | ---: | ---: | ---: |
| All boy-wolf subjects | 216 | 542 | 465 |
| **Metaphor-rich (need stories)** | 185 | 451 | 430 |
| Atoms (`_SHARED_SUBPLOTS`; form-display IS the lesson) | 8 | 44 | — |
| Abstract (`_GOAL_SUBPLOTS`; cargo-cult to force a metaphor) | 23 | 47 | 35 |

**Story-slot coverage of the metaphor-rich pool: 430 of 451 examples = 95%.**

## Coverage by metaphor family

| Family | Subjects | Examples | Stories | Remaining |
| --- | ---: | ---: | ---: | ---: |
| `_ACORN_SUBPLOTS` | 16 | 69 | 67 | 2 |
| `_TOOLSHED_SUBPLOTS` | 9 | 48 | 33 | 15 |
| `_BASKET_SUBPLOTS` | 21 | 42 | 41 | 1 |
| `_ROADSIGN_SUBPLOTS` | 16 | 30 | 30 | 0 ✅ |
| `_GATE_SUBPLOTS` | 7 | 28 | 28 | 0 ✅ |
| `_NOTEBOOK_SUBPLOTS` | 12 | 23 | 23 | 0 ✅ |
| `_REWRITERULE_SUBPLOTS` | 10 | 21 | 21 | 0 ✅ |
| `_RECIPE_SUBPLOTS` | 12 | 20 | 20 | 0 ✅ |
| `_SIEVE_SUBPLOTS` | 10 | 20 | 20 | 0 ✅ |
| `_SCRIBE_SUBPLOTS` | 9 | 19 | 19 | 0 ✅ |
| `_SAFETYNET_SUBPLOTS` | 9 | 19 | 19 | 0 ✅ |
| `_SCROLL_SUBPLOTS` | 10 | 19 | 19 | 0 ✅ |
| `_GUILD_SUBPLOTS` | 9 | 16 | 15 | 1 |
| `_POUCH_SUBPLOTS` | 7 | 15 | 15 | 0 ✅ |
| `_CHALKMARK_SUBPLOTS` | 4 | 12 | 12 | 0 ✅ |
| `_SORTINGTABLE_SUBPLOTS` | 5 | 11 | 10 | 1 |
| `_FORK_SUBPLOTS` | 6 | 10 | 10 | 0 ✅ |
| `_RUNNERAHEAD_SUBPLOTS` | 5 | 9 | 9 | 0 ✅ |
| `_TALLYWALK_SUBPLOTS` | 3 | 8 | 8 | 0 ✅ |
| `_BEADSTRING_SUBPLOTS` | 2 | 7 | 7 | 0 ✅ |
| `_CARRYINGCASE_SUBPLOTS` | 2 | 4 | 3 | 1 |
| `_CIRCUIT_SUBPLOTS` | 1 | 1 | 1 | 0 ✅ |
| **TOTAL (metaphor-rich)** | **185** | **451** | **430** | **21** |

## Family imagery

Cross-reference to `docs/clojure-pedagogy/audits/metaphor-imagery-boy-wolf.md` for the imagery anchors. Each family's templates use one consistent prop-vocabulary (belt-pouch, watchhouse slate, fold-gates, etc.); cross-fable parity preserves the family *name* but uses fable-specific imagery.

## Authoring polarity

Boy-wolf flips the typical fable polarity:
- The **shepherd** (Tom, Will, Pat, Jess, Lou) is the cautionary character — boasts, claims he just *knows*, guesses without checking.
- The **elder/villager** (Carol, Bob, Grace, Margery, etc.) is the corrective voice — writes the form, lets the runtime decide.

Templates and story slots preserve this polarity throughout.

## When a fifth fable comes online

The framework scales linearly:
- **Same 22 family pool names** in `<fable>/_metaphor_pools.py`
- **Parallel slot authoring** — translate each tortoise-hare scenario into the new fable's world (foraging-basket → wool-basket → grain-bin → egg-basket)
- **Same `_story()` helper** — same 5-act shape, fable-specific verbs
