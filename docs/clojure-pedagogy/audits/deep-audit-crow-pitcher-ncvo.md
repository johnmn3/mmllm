# Deep audit — crow_pitcher (slice ncvo, "make it make sense")

**Branch**: `claude/audit-crow-pitcher-ncvo`
**Parent (integration HEAD)**: `d8dfba0cf5ed850726d877a422c2efe11e5ad1a9`
   ("regen crow-pitcher + tortoise-hare audit reports with parametric coverage")
**Date**: 2026-05-08

## Slice

- **Fable**: `crow_pitcher`
- **Grades sampled (random 6 of 12)**: 1, 2, 6, 8, 9, 10
- **Read corpus**: 1,490 records (5 renders × 298 examples × 6 grades)
- **Storybook sample**: 30 random records pulled from the corpus

## Verification

- PARENT_OK: integration HEAD subject "regen crow-pitcher + tortoise-hare audit reports..."
- HEAD matched expected SHA after `git checkout -b`
- Playbook present at `docs/clojure-pedagogy/audits/AUDIT-PLAYBOOK.md`

## Smoke (8 modules + e2e)

All green: `scalar_pools` (29 pools), `form_parser` (27/27),
`form_families` (82 × 5 = 410), `auto_parametric` (6), `character_pools`
(1830 names × 13 pools), `opener_pools` (150/150), `emotion_pools`
(199 + 396 entries), `test_parametric_e2e.py`.

## Audit BEFORE / AFTER

| Metric                       | Before | After | Delta |
| ---------------------------- | -----: | ----: | ----: |
| total issues                 |  1,345 | 1,256 |   −89 |
| **LOW_GROUNDING**            |    149 |    97 |   −52 |
| REPL_AS_TIME_TRAVELLER       |     38 |     0 |   −38 |
| RESOLUTION_GENERIC (new)     |      − |     0 |     − |
| AI_OUTPUT_CADENCE (new)      |      − |     0 |     − |
| CONCEPT_PHRASE_COMMA_LIST (new) |   − |     0 |     − |

LOW_GROUNDING delta is **−52 (35% reduction)**. The
`STORY_RESOLUTION_NO_DRAWN` count (1,027) carries over from prior
slices — a separate concern affecting parametric story-tagged
examples whose `resolution` slot doesn't reference drawn literals;
out of scope for this slice.

## New detectors (3)

### 1. `CONCEPT_PHRASE_COMMA_LIST`

A `concept_phrase` rendered as 3+ comma-separated bare tokens — no
determiner / preposition / noun-phrase shape. Reads as a
comma-list of operation names instead of a noun phrase the template
can interpolate naturally. Cross-fable visibility: 75 hits each in
tortoise_hare, milkmaid, boy_wolf, dog_shadow.

```python
cp_tokens = [t.strip() for t in cp.split(",")]
if len(cp_tokens) >= 3 and all(
    len(t.split()) <= 3 and t and not re.match(
        r"^(?:the|a|an|of|with|...)\b", t.lower(),
    )
    for t in cp_tokens
):
    issues.append(("CONCEPT_PHRASE_COMMA_LIST", ...))
```

### 2. `AI_OUTPUT_CADENCE`

Sentences with the "with the X of one who Y" / "with the X of
someone who Y" elaborate-clause-stack cadence. Reads as model-output,
not storybook prose. Cross-fable visibility: 6 hits in boy_wolf.

```python
ai_cadence_re = re.compile(
    r"\bwith the [a-z]+ of (?:one|someone|a [a-z]+|an [a-z]+) who\b",
)
```

### 3. `RESOLUTION_GENERIC`

User_msg's resolution beat is canned boilerplate ("the count of
whatever the operation had produced", "the precise number the
operation called for") that doesn't tie back to the fable's
metaphor or drawn values. Cat-K-6 (under-earned metaphor) signal.
Caught 38 records on crow_pitcher BEFORE my Cat-K rewrites; 0
AFTER.

```python
canned_resolution_re = re.compile(
    r"\b(?:the (?:count|value|number|answer)) of (?:whatever|"
    r"the operation|...) (?:[a-z]+ )?(?:had )?(?:produced|"
    r"called for|returned|computed)|the precise (?:count|number|...) "
    r"the (?:operation|...) called for|...",
)
```

## Cat-J grounding lifts (10)

All ten lifts inject `{emo_patient}` AND add an environmental
adjective sentence with a 1-sentence algorithmic mapping.

| # | Source                                            | Mapping                                                                    |
| - | ------------------------------------------------- | -------------------------------------------------------------------------- |
| 1 | `_metaphor_pools.py:650` (FORK wings template)     | "the wrong wing meant another long flight back" ↔ pick correct branch       |
| 2 | `_metaphor_pools.py:808` (SCROLL flat-stone)       | "stone cool against the day's heat, scratch will last" ↔ persistence to disk |
| 3 | `_metaphor_pools.py:1075` (RUNNERAHEAD scout-crow) | "day hot, water still low; scout means dropping continues here" ↔ async    |
| 4 | `_metaphor_pools.py:1217` (SCRIBE careful writing) | "slate rough, heat makes clay cling — each scratch clean first time" ↔ reader strictness |
| 5 | `_metaphor_pools.py:1326` (TALLYWALK reduce)       | "rim high, water far below, tally grows stone by stone — no shortcut" ↔ reduce |
| 6 | `_metaphor_pools.py:1369` (TALLYWALK rim-returns)  | `{emo_patient}` injection in instruction-quote                              |
| 7 | `_metaphor_pools.py:1411` (BEADSTRING vines)       | "vines short on their own — one wouldn't reach far enough" ↔ str concat    |
| 8 | `_metaphor_pools.py:1454` (CIRCUIT recur)          | "pitcher narrow, day long; many laps; each must leave no extra footprint" ↔ recur stack-frame |
| 9 | `crow_pitcher/grade_1.py:240` (race-pause GOAL)    | "day hot, throat dry, water still far below the rim" ↔ patience            |
| 10 | `crow_pitcher/grade_1.py:299` (race-against-REPL)  | "day hot, water lay low; wrong guess wasted breeze and pebble both" ↔ goal-pressure |

LOW_GROUNDING dropped 149 → 97 (Δ = −52) after these 10 lifts.

## Cat-K storytelling lifts (21)

Cat-K rewrites are PROSE rewrites, not mechanical injections. They
replace broken or boilerplate prose with prose that earns the
metaphor and tracks a specific story-beat.

### Cat-K-3 (AI-output cadence) — 19 concept_phrase rewrites

All 19 distinct comma-list `concept_phrase` strings in
`crow_pitcher/grade_9.py` were rewritten as proper noun phrases.
Each rewrite preserves the operational meaning while reading as a
flowing noun phrase that templates can interpolate naturally.

| Subject | BEFORE                         | AFTER                                                                             |
| ------- | ------------------------------ | --------------------------------------------------------------------------------- |
| G9-03   | `atom, swap, and deref`         | `the atom updated atomically via swap! and read by deref`                         |
| G9-03   | `atom, swap, deref`             | `the atom updated atomically and then read`                                       |
| G9-03   | `atom, reset, deref`            | `the atom reset to a new value and then read`                                     |
| G9-04   | `atom, CAS, deref`              | `the atom updated via compare-and-set and read`                                   |
| G9-04   | `atom, failed CAS, deref`       | `the atom guarded by a compare-and-set whose expected value did not match`        |
| G9-07   | `ref, dosync, alter, deref`     | `the ref altered inside a transaction and read`                                   |
| G9-07   | `ref, dosync, ref-set, deref`   | `the ref reset inside a transaction and read`                                     |
| G9-08   | `ref, dosync, alter, deref`     | (covered above; 2nd subject sharing the cp)                                       |
| G9-09   | `atom, swap, deref`             | (covered above)                                                                   |
| G9-09   | `ref, dosync, alter, deref`     | (covered above)                                                                   |
| G9-10   | `agent, send, await, deref`     | `the agent sent a function asynchronously, awaited, and read`                     |
| G9-11   | `agent, send-off, await, deref` | `the agent dispatched via send-off, awaited, and read`                            |
| G9-12   | `agent, double send, await, deref` | `the agent sent two updates in succession, awaited, and read`                  |
| G9-13   | `future, add, deref`            | `the addition wrapped in a future and dereferenced`                               |
| G9-13   | `future, multiply, deref`       | `the multiplication wrapped in a future and dereferenced`                         |
| G9-15   | `promise, deliver, deref`       | `the promise delivered a value and then dereferenced`                             |
| G9-16   | `volatile, vswap, deref`        | `the volatile updated by vswap! and read`                                         |
| G9-16   | `volatile, vreset, deref`       | `the volatile reset by vreset! and read`                                          |
| G9-17   | `dynamic var, binding, read`    | `the dynamic var rebound inside a binding form and read`                          |
| G9-17   | `dynamic var, binding, read after` | `the dynamic var rebound inside a binding form, read inside, then read again outside` |
| G9-18   | `lock, locking, arithmetic`     | `the arithmetic evaluated inside a critical section guarded by locking`           |
| G9-18   | `lock, locking, literal`        | `the literal value evaluated inside a critical section guarded by locking`        |

These 19 rewrites elevate ~25 examples × ~3 records each = ~75
records from "comma-list reads as keyword-soup" to "noun-phrase
flows naturally into subplots". Cat-K-3 source-level fix.

### Cat-K-6 (under-earned metaphor) — 2 ACORN template tail rewrites

`crow_pitcher/_metaphor_pools.py:424` (heap-of-stones template 1):

```
BEFORE: ... let the REPL hand back the count of whatever
        the operation had produced.
AFTER:  ... let the REPL hand back the running count —
        exactly what the heap, dropped pebble by pebble,
        would have raised.
```

`crow_pitcher/_metaphor_pools.py:449` (heap-of-stones template 3):

```
BEFORE: ... and the REPL handed back the precise number
        the operation called for.
AFTER:  ... and the REPL handed back the precise count —
        the heap counted as carefully as the day's heat
        would let the crow count it.
```

Together these two rewrites elevated 38 records (the
RESOLUTION_GENERIC + REPL_AS_TIME_TRAVELLER detectors both went 38
→ 0). Cat-K-6 — the metaphor's parts (heap, drops, day's heat) now
DRIVE the resolution rather than appearing once and disappearing.

**Total Cat-K source-level rewrites: 21** (19 concept_phrase + 2
template tails). Each is a prose rewrite, not a mechanical
{emo_*} injection.

## Storybook reading

30 records sampled (random) from the corpus. Heuristic rates each
on 4 signals (metaphor noun present, place phrase, EMO phrase, no
AI-cadence / procedural-opener / comma-list-cp / canned-resolution
penalty).

| State  | GOOD | OKAY | BAD | GOOD ratio |
| ------ | ---: | ---: | --: | ---------: |
| BEFORE |   23 |    4 |   3 |      76.7% |
| AFTER  |   25 |    3 |   1 |      86.2% |

AFTER GOOD ratio **86.2% ≥ 80%** target.

The single remaining BAD record (G1-10 sample) suffers from a
parametric drift: form is `42 ;; the answer` but goal_text says
"submit the integer 46" — caught by the existing
`PARAMETRIC_LITERAL_NUMERALS` detector. That fix belongs to a
follow-up parametric-prose slice; out of scope for this Cat-J/K
audit.

## Polarity

All 10 Cat-J lifts attached `{emo_patient}` to the `{clever_phrase}`
role (the patient stone-dropper). The hasty role kept `{emo_proud}`
in templates that already used it. No polarity flips — clever crow
remains the patient evaluator; hasty crow remains the impatient
guesser.

## Caveats

- The 1,027 STORY_RESOLUTION_NO_DRAWN hits are pre-existing — they
  flag parametric story examples whose authored `resolution` slot
  was written before the parametric drawing system was introduced.
  Fixing them requires per-example rewrites that interpolate
  `{drawn.<slot>}` placeholders into resolution prose. That's a
  Phase-D-parametric-resolution slice, distinct from this round.
- The 19 comma-list concept_phrases were unique strings; some are
  shared across multiple subjects (e.g., `atom, swap, deref` appears
  in G9-03 and G9-09). The single rewrite covers all subjects that
  used the shared string.
- 8 templates in `crow_pitcher/_metaphor_pools.py` lacked any
  `{emo_*}` placeholder before this slice; all 8 received Cat-J
  lifts in the metaphor-pool file (lifts 1-8). Lifts 9 and 10
  hit `crow_pitcher/grade_1.py` (the SHARED pool's race-pause and
  notebook templates).