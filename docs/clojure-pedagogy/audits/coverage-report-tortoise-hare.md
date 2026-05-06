# Tortoise-hare semantic coverage — gap report

**Snapshot after Phase C framework lands (commit `608df3f`).**

## Where we are

| Slice                                            | Subjects | Examples | Story slots authored |
| ------------------------------------------------ | -------: | -------: | -------------------: |
| All tortoise-hare subjects                       |      216 |      509 |                   22 |
| **Metaphor-rich (need stories)**                 |      185 |      422 |                   22 |
| Atoms (`_SHARED_SUBPLOTS`; form-display IS the lesson)            |        8 |       40 |                    — |
| Abstract (`_GOAL_SUBPLOTS`; cargo-cult to force a metaphor)        |       23 |       47 |                    — |

**Story-slot coverage of the metaphor-rich pool: 22 of 422 examples = 5.2%.**

The framework is wired in end-to-end. The long tail is **authoring slot
content for the remaining 400 metaphor-rich examples.** Each remaining
slot-set is roughly 100-150 words of grounded story (scenario + need +
mapping + resolution).

## Gap by metaphor family

| Family                | Subjects | Examples | Stories | TODO |
| --------------------- | -------: | -------: | ------: | ---: |
| `_ACORN_SUBPLOTS`     |       16 |       69 |       1 |   68 |
| `_BASKET_SUBPLOTS`    |       21 |       42 |       1 |   41 |
| `_ROADSIGN_SUBPLOTS`  |       16 |       30 |       1 |   29 |
| `_GATE_SUBPLOTS`      |        7 |       28 |       1 |   27 |
| `_NOTEBOOK_SUBPLOTS`  |       12 |       23 |       1 |   22 |
| `_REWRITERULE_SUBPLOTS` |     10 |       21 |       1 |   20 |
| `_RECIPE_SUBPLOTS`    |       12 |       20 |       1 |   19 |
| `_SIEVE_SUBPLOTS`     |       10 |       20 |       1 |   19 |
| `_SAFETYNET_SUBPLOTS` |        9 |       19 |       1 |   18 |
| `_SCROLL_SUBPLOTS`    |       10 |       19 |       1 |   18 |
| `_TOOLSHED_SUBPLOTS`  |        9 |       19 |       1 |   18 |
| `_SCRIBE_SUBPLOTS`    |        9 |       19 |       1 |   18 |
| `_GUILD_SUBPLOTS`     |        9 |       16 |       1 |   15 |
| `_POUCH_SUBPLOTS`     |        7 |       15 |       1 |   14 |
| `_CHALKMARK_SUBPLOTS` |        4 |       12 |       1 |   11 |
| `_SORTINGTABLE_SUBPLOTS` |     5 |       11 |       1 |   10 |
| `_FORK_SUBPLOTS`      |        6 |       10 |       1 |    9 |
| `_RUNNERAHEAD_SUBPLOTS` |      5 |        9 |       1 |    8 |
| `_TALLYWALK_SUBPLOTS` |        3 |        8 |       1 |    7 |
| `_BEADSTRING_SUBPLOTS`|        2 |        7 |       1 |    6 |
| `_CARRYINGCASE_SUBPLOTS` |     2 |        4 |       1 |    3 |
| `_CIRCUIT_SUBPLOTS`   |        1 |        1 |       1 |    0 ✅ |
| **TOTAL (metaphor-rich)** | **185** | **422** | **22** | **400** |

`_CIRCUIT_SUBPLOTS` is fully covered (only one subject — G5-22 recur — and
its single example is authored).

## What gaps actually look like

For each non-canonical example, the slot-set work is:

1. **Read the form + expected.** What does the operation do, concretely?
2. **Pick a fable scenario.** What's a daily-life situation in
   tortoise-hare's meadow that *needs* this exact operation?
3. **Author the four slots** (~100-150 words total):
   - **scenario** (concrete situation, names + state)
   - **need** (specific demand the operation answers)
   - **mapping** (how fable elements map 1:1 to operation parts)
   - **resolution** (closes loop with the need)
4. **Add `tags=("story",)`.**
5. **Audit clean** — no answer leaks, no `HIGH_LENGTH`, no DOUBLE_PREP.

## Prioritization

Authoring all 400 slot-sets is roughly **40-60K words of grounded
prose**. To get the highest pedagogical impact per word, work in
this order:

### Tier 1 — load-bearing concepts, ~100 examples

| Family | Why prioritize | Examples |
| ------ | -------------- | -------: |
| `_POUCH` (let-binding) | Foundational — every `let` is a scope mental model the model needs | 14 |
| `_RECIPE` (fn / defn / comp / partial) | Every named/anonymous routine | 19 |
| `_BASKET` (collections + immutability) | Vectors / lists / maps / sets / `assoc` / `get` / `conj` | 41 |
| `_NOTEBOOK` (atom / ref / state) | The state model + atomic semantics | 22 |
| **Tier 1 subtotal** |  | **96** |

### Tier 2 — high-leverage idioms, ~120 examples

| Family | Why | Examples |
| ------ | --- | -------: |
| `_SIEVE` (HOFs / transducers) | Map/filter/take/drop core pattern | 19 |
| `_FORK` (if / cond / case / when) | Control flow | 9 |
| `_GATE` (boolean) | And/or short-circuit + falsey rules | 27 |
| `_SAFETYNET` (errors) | Try/catch — defensive programming | 18 |
| `_GUILD` (protocols) | Polymorphism | 15 |
| `_SORTINGTABLE` (multimethods) | Open dispatch | 10 |
| `_REWRITERULE` (macros) | Code that writes code | 20 |
| **Tier 2 subtotal** |  | **118** |

### Tier 3 — fill out the long tail, ~110 examples

| Family | Examples |
| ------ | -------: |
| `_ACORN` (arithmetic) | 68 (small-effort-per-example; mechanical) |
| `_ROADSIGN` (def/namespace) | 29 |
| `_TOOLSHED` (host interop) | 18 |
| `_SCRIBE` (read-time conventions) | 18 |
| `_SCROLL` (IO) | 18 |
| `_CHALKMARK` (quote/symbols) | 11 |
| **Tier 3 subtotal** |  | **162** |

### Tier 4 — small but distinct, ~24 examples

| Family | Examples |
| ------ | -------: |
| `_TALLYWALK` (reduce / count) | 7 |
| `_RUNNERAHEAD` (agent / future / promise) | 8 |
| `_BEADSTRING` (strings) | 6 |
| `_CARRYINGCASE` (deftype/defrecord) | 3 |
| **Tier 4 subtotal** |  | **24** |

## Estimated effort

At ~100-150 words per slot-set and assuming the 5-act shape can be
authored in ~5-10 minutes per example by a focused writer:

- **Tier 1** (96 examples): ~12 hours of focused authoring
- **Tier 2** (118 examples): ~15 hours
- **Tier 3** (162 examples): ~20 hours (some are trivial — arithmetic
  scenarios all share the same shape, just numbers change)
- **Tier 4** (24 examples): ~3 hours

**Full tortoise-hare semantic coverage: ~50 hours of focused authoring.**

This can be accelerated by:
1. **Authoring per-family scenario bank** — for each family, write 5-10
   reusable mini-scenarios (kitchen variant, foraging variant, race-day
   variant, dawn variant, dinner variant). Each example picks one scenario
   from the bank and adapts the specifics.
2. **Per-grade fan-out to sub-agents** — one agent per grade authors
   ~15-20 stories given the family scenario banks as starting material.
3. **Audit-driven validation** — STORY_TAG_MISMATCH check (already
   shipped) + manual spot-check of 1 record per authored example.

## When goose-eggs and ant-grasshopper come online

The framework scales linearly:
- **Same 22 family pool names** in `goose_eggs/_metaphor_pools.py` and
  `ant_grasshopper/_metaphor_pools.py`
- **Parallel slot authoring** — translate each tortoise-hare scenario
  into the new fable's world (foraging-basket → egg-basket → grain-bin)
- **Same `_story()` helper** — same 5-act shape, fable-specific verbs

For a 3-fable corpus: **1,266 metaphor-rich examples × 100-150 words ≈
130-190K words of grounded scenarios**, producing **~280K story-template
records** at `n_per_example=222`. Combined with the existing
generic-template renders, the model trains on both grounded
fable-specific stories AND generic Hare/Tortoise narratives — the
metaphor-mapping reinforced from multiple narrative angles.

## Recommended next step

Author **Tier 1 (96 examples)** as a single focused commit cycle.
That covers the most load-bearing concepts (let / fn / collections /
state) and exercises the framework at the scale where the metaphor
investment pays off most clearly. After Tier 1 lands, one full
demo-doc regeneration will show every load-bearing subject as a
grounded story — and from there, the path to fan-out across all
remaining tiers and the other two fables is mechanical.
