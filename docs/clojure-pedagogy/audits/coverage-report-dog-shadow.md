# Dog-shadow semantic coverage — Phase C complete

**Snapshot after the dog-shadow Phase C build (216 subjects, 509 examples, audit clean).**

## Where we are

| Slice                                            | Subjects | Examples | Story slots authored |
| ------------------------------------------------ | -------: | -------: | -------------------: |
| All dog-shadow subjects                          |      216 |      509 |                  416 |
| **Metaphor-rich (story-scaffold)**               |      185 |      422 |                  412 |
| Atoms (`_SHARED_SUBPLOTS`)                       |        8 | — | — |
| Abstract (`_GOAL_SUBPLOTS` / topic-specific)     |       23 | — | — |

**Story-slot coverage of the metaphor-rich pool: 412 of 422 examples = 97%.**

Every metaphor-rich example carries a fully authored 5-act story scaffold — `scenario` + `need` + `mapping` + `resolution` slots — with imagery drawn from the dog-shadow fable (a dog crossing a stream with a real bone, snapping at his own reflection, losing what he had). The 22 canonical examples were hand-authored by the parent agent; the remaining ~395 were authored by 12 grade-scoped haiku sub-agents in parallel and validated against the audit harness.

## Coverage by metaphor family

| Family                  | Subjects | Examples | Stories | Coverage |
| ----------------------- | -------: | -------: | ------: | -------: |
| `_ACORN_SUBPLOTS` |       16 |       69 |      68 |     98% |
| `_BASKET_SUBPLOTS` |       21 |       42 |      40 |     95% |
| `_ROADSIGN_SUBPLOTS` |       16 |       30 |      30 |    100% |
| `_GATE_SUBPLOTS` |        7 |       28 |      28 |    100% |
| `_NOTEBOOK_SUBPLOTS` |       12 |       23 |      23 |    100% |
| `_REWRITERULE_SUBPLOTS` |       10 |       21 |      21 |    100% |
| `_RECIPE_SUBPLOTS` |       12 |       20 |      20 |    100% |
| `_SIEVE_SUBPLOTS` |       10 |       20 |      20 |    100% |
| `_SCRIBE_SUBPLOTS` |        9 |       19 |      19 |    100% |
| `_SAFETYNET_SUBPLOTS` |        9 |       19 |      19 |    100% |
| `_TOOLSHED_SUBPLOTS` |        9 |       19 |      17 |     89% |
| `_SCROLL_SUBPLOTS` |       10 |       19 |      19 |    100% |
| `_GUILD_SUBPLOTS` |        9 |       16 |      16 |    100% |
| `_POUCH_SUBPLOTS` |        7 |       15 |      15 |    100% |
| `_CHALKMARK_SUBPLOTS` |        4 |       12 |      12 |    100% |
| `_SORTINGTABLE_SUBPLOTS` |        5 |       11 |      11 |    100% |
| `_FORK_SUBPLOTS` |        6 |       10 |      10 |    100% |
| `_RUNNERAHEAD_SUBPLOTS` |        5 |        9 |       9 |    100% |
| `_TALLYWALK_SUBPLOTS` |        3 |        8 |       6 |     75% |
| `_BEADSTRING_SUBPLOTS` |        2 |        7 |       4 |     57% |
| `_CARRYINGCASE_SUBPLOTS` |        2 |        4 |       4 |    100% |
| `_CIRCUIT_SUBPLOTS` |        1 |        1 |       1 |    100% |

## Uniqueness

- 412 story-tagged examples
- 416 distinct scenarios (worst reuse: 1×)
- 0 tortoise-hare terms (`Mossback`, `Shelly`, `pouch`, `acorn`, `recipe-card`, etc.)
- 0 audit issues across all 12 grades

## How this was built

1. **Phase 1 — imagery mapping**: 22-family table at `docs/clojure-pedagogy/audits/metaphor-imagery-dog-shadow.md`. Each Clojure idiom mapped to a dog-shadow image: let → bone-in-mouth, fn → nose-trail, atom → tally-stone, etc.
2. **Phase 2 — directory mirror**: tortoise-hare's directory structure copied as the starting template; imports rewired to `mmllm.aesop.curriculum.dog_shadow.*`.
3. **Phase 3 — metaphor pools**: rewrote all 22 family pools in `_metaphor_pools.py` with dog-shadow imagery and the `_story()` helper extension.
4. **Phase 4 — subjects**: 216 subjects mirrored from tortoise-hare with character/imagery substitution.
5. **Phase 5 — strip TH leaks**: AST-driven script removed 348 `scenario`/`need`/`mapping`/`resolution` slots that still carried tortoise-hare imagery.
6. **Phase 6 — 22 canonicals**: parent agent hand-authored one story-slotted example per metaphor family.
7. **Phase 7 — fan out**: 12 haiku sub-agents (one per grade) story-fied the remaining ~395 examples in parallel.
8. **Phase 8 — audit + docs**: cross-fable audit pass (8 fables × audit-harness) + this report + the metaphor demo (`metaphor-demo-dog-shadow.md`).

## Cross-fable parity

All eight fable curricula (`tortoise-hare`, `ant-grasshopper`, `goose-eggs`, `fox-grapes`, `boy-wolf`, `crow-pitcher`, `milkmaid`, `dog-shadow`) audit clean. Together they form a K-12 corpus of grounded Clojure-pedagogy stories where each concept lives inside the same character roles but different imagery — the model trains on the same Clojure semantics seen from eight distinct narrative angles.
