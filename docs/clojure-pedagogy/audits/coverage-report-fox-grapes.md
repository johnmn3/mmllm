# Fox-grapes semantic coverage — gap report

Snapshot after Phase C framework lands. Mirrors the
tortoise-hare report shape so progress is comparable.

## Where we are

| Slice                                            | Subjects | Examples | Story slots authored |
| ------------------------------------------------ | -------: | -------: | -------------------: |
| All fox-grapes subjects                          |      216 |      513 |                   393 |
| **Metaphor-rich (need stories)**                 |      185 |      422 |                   393 |
| Atoms (`_SHARED_SUBPLOTS`; form-display IS the lesson)            |        8 |       44 |                    — |
| Abstract (`_GOAL_SUBPLOTS`; goal-driven, no metaphor)             |       23 |       47 |                    — |

**Story-slot coverage of the metaphor-rich pool: 393 of 422 examples = 93.1%.**

## Gap by metaphor family

| Family                | Subjects | Examples | Stories | TODO |
| --------------------- | -------: | -------: | ------: | ---: |
| `_ACORN_SUBPLOTS` |       16 |       69 |      69 |    0 ✅ |
| `_BASKET_SUBPLOTS` |       21 |       42 |      42 |    0 ✅ |
| `_ROADSIGN_SUBPLOTS` |       16 |       30 |      23 |    7 |
| `_GATE_SUBPLOTS` |        7 |       28 |      28 |    0 ✅ |
| `_NOTEBOOK_SUBPLOTS` |       12 |       23 |      23 |    0 ✅ |
| `_REWRITERULE_SUBPLOTS` |       10 |       21 |      21 |    0 ✅ |
| `_RECIPE_SUBPLOTS` |       12 |       20 |      20 |    0 ✅ |
| `_SIEVE_SUBPLOTS` |       10 |       20 |      20 |    0 ✅ |
| `_SAFETYNET_SUBPLOTS` |        9 |       19 |      19 |    0 ✅ |
| `_SCROLL_SUBPLOTS` |       10 |       19 |      16 |    3 |
| `_TOOLSHED_SUBPLOTS` |        9 |       19 |      18 |    1 |
| `_SCRIBE_SUBPLOTS` |        9 |       19 |      19 |    0 ✅ |
| `_GUILD_SUBPLOTS` |        9 |       16 |      10 |    6 |
| `_POUCH_SUBPLOTS` |        7 |       15 |      15 |    0 ✅ |
| `_CHALKMARK_SUBPLOTS` |        4 |       12 |       9 |    3 |
| `_SORTINGTABLE_SUBPLOTS` |        5 |       11 |       6 |    5 |
| `_FORK_SUBPLOTS` |        6 |       10 |      10 |    0 ✅ |
| `_RUNNERAHEAD_SUBPLOTS` |        5 |        9 |       9 |    0 ✅ |
| `_TALLYWALK_SUBPLOTS` |        3 |        8 |       8 |    0 ✅ |
| `_BEADSTRING_SUBPLOTS` |        2 |        7 |       5 |    2 |
| `_CARRYINGCASE_SUBPLOTS` |        2 |        4 |       2 |    2 |
| `_CIRCUIT_SUBPLOTS` |        1 |        1 |       1 |    0 ✅ |
| **TOTAL (metaphor-rich)** | **185** | **422** | **393** | **29** |

## Imagery

Each family carries its own fox-grapes-specific imagery —
see `metaphor-imagery-fox-grapes.md` for the full mapping.
Family names are constant across fables; only the imagery
changes. Same idiom, different storytelling materials.

## How fox-grapes rhymes with tortoise-hare

- Same K-12 structure: 216 subjects, ~510 examples
- Same 22 metaphor families with parallel pool names
- Different imagery: orchard / vineyard / market vs path / meadow / forest
- Different second voice: hasty fox vs patient fox (vs hare vs tortoise)

Together they exercise the same Clojure idioms across two
narrative angles, reinforcing the operation's structure
in the model's training.
