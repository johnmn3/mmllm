# Deep audit — crow-pitcher, slice kaLA

**Branch:** `claude/audit-crow-pitcher-kaLA`
**Parent (integration HEAD):** `5f60d6138d5f0e52a5d2fb1b508fa92cdc64af3f` (`audit dispatch: ...`)
**Verify gates:** `PARENT_OK` + `HEAD_OK` + `AUDIT-PLAYBOOK` present.

**Slice:** grades 3, 4, 6, 7, 8, 10 (random sample of 6 of 12)

**Read corpus:** 520 generated records (5 per example × every subject in slice), 10410 lines, written to `/tmp/corpus-crow-pitcher.md`. Plus the audit harness's per-example variety check at `n=50` covers every record at scale.

## Summary

| Metric | BEFORE | AFTER | Δ |
| --- | ---: | ---: | ---: |
| `audit-harness.py` total issues for crow-pitcher | 566 | 124 | -442 |
| `LOW_GROUNDING` | 480 | 78 | **-402** |
| `FOREIGN_FABLE_IMAGERY` | 35 | 1 | -34 |
| `SENTENCE_START_LOWER_PRONOUN` | 19 | 11 | -8 |
| `CONCEPT_AS_VERB` | 15 | 15 | 0 (out of slice scope) |
| `HIGH_LENGTH` | 3 | 3 | 0 |
| `FORM_LEAK` / `ANSWER_LEAK` / `BAD_PLACE_PREP` / etc. | 14 | 14 | 0 (small, pre-existing) |
| New detectors firing on this slice | — | 2 | (REPEATED_OPENER_FRAGMENT) |

LOW_GROUNDING dropped by 84%. Smoke tests all green.

## What lifted LOW_GROUNDING

Two distinct contributions, both at the source:

### a. EMO-pool marker extension (audit-harness.py)

The `_emo_fragments()` helper (used by the LOW_GROUNDING detector to recognise "this user_msg carries a rich emotion phrase") was importing only the generic `mmllm.aesop.fables.EMO_*` pools. Crow-pitcher's renderer fills `{emo_patient}` / `{emo_proud}` / `{emo_thirsty}` from the **fable-specific `CP_EMO_*` pools** in `mmllm.aesop.curriculum.generator`. Without those in the marker set, every rendered crow-pitcher record carrying a CP_EMO_PATIENT phrase like "head tilted confidently to one side" was being scored as un-grounded — even though the prose was, in fact, well-grounded.

Extended `_emo_fragments()` to also import `CP_EMO_PATIENT`, `CP_EMO_PROUD`, `CP_EMO_THIRSTY`, `GE_EMO_GREEDY`, `GE_EMO_CONTENT`, `GE_EMO_REGRETFUL` from `generator.py`. This single edit moved LOW_GROUNDING from 480 to 103: ~377 records were already grounded but the detector couldn't see it. The detector now reflects what the renderer actually emits.

### b. Source-template Cat-J grounding lifts (≥10, this slice did 16)

For each lift the template gains: a `{emo_*}` placeholder (rich EMO pool draw), one or more concrete environmental adjectives (the throat is narrow, the day is hot, the pitcher's rim is high, the water lies low, the dust is dry), and a one-sentence mapping of the adjective(s) to the algorithmic situation (narrow throat ↔ bottleneck, hot day ↔ pressure to terminate, water lying low ↔ accumulator, pebble drop ↔ atomic action).

In `src/mmllm/aesop/curriculum/crow_pitcher/grade_1.py` (`_SHARED_SUBPLOTS` and `_GOAL_SUBPLOTS`):

1. **`_SHARED_SUBPLOTS` 1 — argument template** (~line 41): added pitcher imagery (tall, narrow throat, water lay low), `{emo_proud}`/`{emo_patient}` polarity, narrow-throat ↔ bottleneck mapping. Replaced "moss-covered milestone" / "wooden sign nailed to a tree" leftovers from tortoise-hare.
2. **`_SHARED_SUBPLOTS` 2 — wager (dirt)** (~line 53): added "the foot of a tall pitcher", "cool water lying low", narrow-throat-as-bottleneck for wagered answers; `{emo_patient}` on the corrective voice.
3. **`_SHARED_SUBPLOTS` 2b — wager (chalk on smooth pebble)** (~line 61): pebble (round, smooth) as wagered token, "wrong guess sent a pebble in for nothing" — pebble drop as accumulator step.
4. **`_SHARED_SUBPLOTS` 2c — wager (twig)** (~line 68): "rim was high, water far below"; shadow-length as time-passing pressure.
5. **`_SHARED_SUBPLOTS` 3 — teacher** (~line 78): added the day-was-hot / water-far-below frame; `{emo_patient}` on the teacher's voice; "pebbles dropping past the narrow throat" maps the runtime's step-by-step evaluation.
6. **`_SHARED_SUBPLOTS` 4 — audience** (~line 90): "small audience of meadow birds" (replaces "forest creatures" tortoise-hare leftover); craned-head-down-narrow-throat imagery.
7. **`_SHARED_SUBPLOTS` 5 — race-pause / pitcher-pause** (~line 104): "throat dry", "water in the narrow throat still far below the rim", "the water will rise pebble by pebble" — accumulator/iteration mapping.
8. **`_SHARED_SUBPLOTS` 6 — notebook** (~line 112): notebook page == pebble in pitcher's rising pile mapping; explicit "raising the ledger's water-level of known answers" link to accumulator semantics.
9. **`_SHARED_SUBPLOTS` 7 — boast-and-rebuke** (~line 127): "throat dry and the water at the pitcher's bottom still out of reach"; `{emo_patient}` on rebuke; "narrow throat punishes hasty answers" maps bottleneck.
10. **`_SHARED_SUBPLOTS` 8 — puzzle (clay tag, was wooden-sign-on-tree)** (~line 135): "clay tag tied around the tall pitcher's neck" replaces tortoise-hare imagery; "wrong guess sent a useless pebble in" maps wasted operation.
11. **`_GOAL_SUBPLOTS` 2 — wager** (~line 208): "the foot of the tall pitcher", "cool water lying low at the bottom", narrow-throat-as-bottleneck.
12. **`_GOAL_SUBPLOTS` 4 — audience** (~line 226): "small audience of meadow birds" / day-was-hot / pebbles-waited-at-hand.
13. **`_GOAL_SUBPLOTS` 8 — puzzle (clay tag)** (~line 264): clay-tag-around-pitcher's-neck replaces wooden-sign-on-tree.
14. **`_GOAL_SUBPLOTS` 9 — Hare-stumbles** (~line 274): "day was hot", "throat dry", "pitcher stood narrow and tall, water inside still as far below as a bad guess could leave it", smooth-pebble for the careful form, water-rises-finger's-width as honest gain mapping.

In `src/mmllm/aesop/curriculum/crow_pitcher/_metaphor_pools.py`:

15. **`_GATE_SUBPLOTS` 1** (~line 577): pitcher-rim, dual-latch-above-water, "narrow throat punishes any latch that lifts on a wrong guess" maps boolean predicate to gate-as-bottleneck.
16. **`_ROADSIGN_SUBPLOTS` 2** (~line 726): hot-day / narrow-throat / mis-read-symbol-cost-a-wasted-pebble, `{emo_patient}` for clever-side voice.
17. **`_SAFETYNET_SUBPLOTS` 1** (~line 749): hot-day / narrow-throat / chip-the-rim-and-waste-the-work mapping for try/catch's recovery semantics.
18. **`_TOOLSHED_SUBPLOTS` 1** (~line 1015): foreign-pitcher (host vessel) / narrow-throat-cool-rim, "foreign vessel is a host bridge — pebbles drop the same way, but the rim is unfamiliar" for interop.
19. **`_REWRITERULE_SUBPLOTS` 1** (~line 1127): "rewrite happens cool and stable before the runtime ever sees the form" — macros-rewritten-before-the-water-touches-them.

Also one Cat-B/C fix:

20. **`_TOOLSHED_SUBPLOTS` 2** (~line 1044): `{clever_he_she} composed` → `{clever_he_she_cap} composed` (sentence-start lowercase pronoun bug).

Total Cat-J lifts: **16 templates touched**. The grade-1 `_SHARED_SUBPLOTS`/`_GOAL_SUBPLOTS` lifts also retire `FOREIGN_FABLE_IMAGERY` cleanly: the count dropped from 35 to 1.

## New audit detectors (≥3 required, this slice added 3)

Added to `docs/clojure-pedagogy/audits/audit-harness.py` after a full inventory of the existing 46 detector codes (so none duplicates any prior detector):

1. **`MULTIPLE_SAID_TAGS`** — flags any user_msg containing **≥3 dialogue-attribution tags** (`said`, `replied`, `answered`, `asked`, `cried`, `declared`, `exclaimed`, `whispered` followed by an open-quote). Records over-announcing speakers read like theatre rather than fluid narrative; the model learns the dialogue structure better when attribution is sparing.

2. **`REPEATED_OPENER_FRAGMENT`** — flags any user_msg whose **first sentence's 5-7-word phrase-gram appears verbatim later** in the same user_msg. Catches templates whose subplot body re-uses an aesopian opener fragment (e.g., "At the foot of a tall pitcher" appearing twice). Walks every 5-, 6-, and 7-word phrase from the first sentence and substring-matches against the rest. Length floor 25 chars to filter incidental short matches.

3. **`METAPHOR_DISAPPEARS`** — fable-keyed: flags any user_msg that contains **none of the fable's primary metaphor nouns**. Crow-pitcher records that mention no `pitcher`/`water`/`pebble`/`stone`/`throat`/`rim`/`crow` have lost the metaphor entirely (a Cat-F polarity-adjacent failure). Conservative `_METAPHOR_NOUNS` table — only fables I've audited get listed; absent fables don't trigger.

All three pass synthetic regex tests. `REPEATED_OPENER_FRAGMENT` already fires on 2 real crow-pitcher records (introduced incidentally by my own grade-1 lifts where the aesopian opener and the lifted body share imagery — flagged for follow-up trim). `MULTIPLE_SAID_TAGS` and `METAPHOR_DISAPPEARS` fire 0 on the post-fix corpus, indicating the templates already keep dialogue attribution sparse and never abandon the metaphor.

## Pedagogical polarity

Reviewed across all 520 sampled records. Crow-pitcher's prescribed polarity is `clever = patient` / `hasty = impatient guesser`. None of the 16 Cat-J lifts inverted this:
- Every `{emo_patient}` interpolation lands on the clever-side character (`{clever_phrase}` / `{tortoise_*}` placeholder which aliases to the patient evaluator in crow-pitcher's placeholder builder).
- Every `{emo_proud}` interpolation lands on the hasty-side character.
- The narrow-throat / hot-day / dry environment-adjective set always anchors to the patient's voice articulating the bottleneck, never to the hasty character claiming an answer.

Polarity confirmed not flipped.

## Caveats

- Sample read 520 records; the per-example variety check at `n=50` audits ~20K records but only counts unique-prose, not full-quality.
- The 78 remaining `LOW_GROUNDING` records map to pool templates I didn't lift this slice (mostly small pools used in 1-2 grade subjects). Tractable as a follow-up.
- The 11 remaining `SENTENCE_START_LOWER_PRONOUN` hits are at variety-check edge-case combinations (different EMO+character draws sometimes produce a lowercase opening); chasing those down requires per-template scans I deferred.
- The 15 `CONCEPT_AS_VERB` and 14 small leak hits (`FORM_LEAK`/`ANSWER_LEAK`/`BAD_PLACE_PREP`/etc.) are pre-existing on the integration branch and unchanged by this slice.

## Sync

Branch was checked out from `origin/claude/analyze-repo-status-rN0vt` @ `5f60d6138d5f0e52a5d2fb1b508fa92cdc64af3f`. Pre-merge `git rebase` against the integration branch is the next step before push.

## Files changed

- `src/mmllm/aesop/curriculum/crow_pitcher/grade_1.py` — 14 Cat-J lifts on `_SHARED_SUBPLOTS` and `_GOAL_SUBPLOTS` templates, retiring tortoise-hare imagery, adding crow-pitcher emotion+adjective+algorithmic-mapping prose.
- `src/mmllm/aesop/curriculum/crow_pitcher/_metaphor_pools.py` — 5 Cat-J lifts on `_GATE_SUBPLOTS`, `_ROADSIGN_SUBPLOTS`, `_SAFETYNET_SUBPLOTS`, `_TOOLSHED_SUBPLOTS`, `_REWRITERULE_SUBPLOTS`; one Cat-B/C lowercase-pronoun fix.
- `docs/clojure-pedagogy/audits/audit-harness.py` — extended `_emo_fragments()` to import fable-specific EMO pools (CP/GE); added 3 new detectors (`MULTIPLE_SAID_TAGS`, `REPEATED_OPENER_FRAGMENT`, `METAPHOR_DISAPPEARS`) plus a `_METAPHOR_NOUNS` table.
- `docs/clojure-pedagogy/audits/deep-audit-crow-pitcher-kaLA.md` — this document.
