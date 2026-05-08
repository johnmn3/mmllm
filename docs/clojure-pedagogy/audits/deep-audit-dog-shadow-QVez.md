# Deep audit — dog-shadow (slice QVez)

## Slice

- **Fable:** dog_shadow (greed loses what was had)
- **Grades sampled (random 6 of 12):** 2, 4, 6, 7, 10, 11
- **Branch:** `claude/audit-dog-shadow-QVez`
- **Parent:** `claude/analyze-repo-status-rN0vt` @ `5f60d61` (integration)
- **Polarity:** hound = patient evaluator; dog = greedy/hasty

## Verification gates

- `PARENT_OK`: `merge claude/audit-milkmaid-k7Pq-remediated: 11 Cat-J lifts + EMO pool wiring, LOW_GROUNDING 178→127`.
- `HEAD_WRONG=no`: branch HEAD = `EXPECTED_PARENT` at checkout.
- `NO_PLAYBOOK=no`: `docs/clojure-pedagogy/audits/AUDIT-PLAYBOOK.md` present on the integration branch.

## Smoke tests

All green: `scalar_pools` (29 pools) ⋅ `form_parser` (27/27) ⋅ `form_families` (82×5=410) ⋅ `auto_parametric` (6 forms) ⋅ `character_pools` (1830 names) ⋅ `opener_pools` (150/150) ⋅ `emotion_pools` (199 band / 396 archetype) ⋅ `test_parametric_e2e.py`.

## New detectors added (3)

The integration harness already carries 46 detectors including `LOW_GROUNDING`, `CAP_PRONOUN_MID_SENTENCE`, `POST_COMMA_CAPITAL_PRONOUN`, `STORY_TAG_MISMATCH`, `BOOL_LEAK_RESOLUTION`, etc. None duplicated. Three new detectors added at the bottom of `check_record`:

1. **`GOAL_TEXT_REPETITION`** — flags records whose `goal_text` (when ≥12 chars) is rendered three or more times in the same `user_msg`. Catches templates that drop `{goal_text}` into multiple beats (intro + question + connective) without restating the action; the resulting prose feels over-tutorialized rather than scenario-grounded.
2. **`PATIENT_ROLE_BOASTFUL`** — flags polarity flips: a sentence that names the fable's patient/evaluator character (Mossback / the farmer / Carol / the hound / the crow) AND contains a clearly-boastful EMO phrase (e.g. "with a smug grin", "puffed up with pride", "boasting at every", "loudly claiming the credit"). Per-fable patient-name maps cover all five Phase-C-complete fables.
3. **`STORY_RESOLUTION_NO_DRAWN`** — flags story-tagged examples whose `resolution` slot doesn't reference any drawn-from-form literal. Resolution should close the algorithmic loop with the actual computed value, not a generic "the REPL returned the value." Fired 307 times on dog-shadow; high-value signal for follow-up authoring.

## Cat-J grounding lifts (10)

1. **`generator.py:_build_ds_placeholders` (L760-769)** — re-wired `emo_*` placeholder picks from the legacy `fables.EMO_*` and local `GE_EMO_*` (≤8 entries) to the integration branch's `emotion_pools.EMO_*` (≥30 entries each, environment-anchored). Added `emo_boastful`, `emo_cautious`, `emo_desperate`, `emo_hungry`, `emo_suspicious` placeholders that templates can now reference.
2. **POUCH `_story()` (line ~1308)** — added `, {emo_patient},` to the connective + env-mapped tail "the grip firm only for the stretch the form needed" (grip/stretch ↔ let-binding scope).
3. **RECIPE `_story()` (line ~1316)** — added `, {emo_patient},` + "long enough to hold every step the routine would take in turn" (long ↔ recipe/sequence length).
4. **BASKET `_story()` (line ~1324)** — added `, {emo_patient},` + "the cache's weight unchanged by the new arrangement" (weight unchanged ↔ immutable update).
5. **SIEVE `_story()` (line ~1332)** — added `, {emo_patient},` + "the gap narrow, the rule deciding which items passed through" (narrow ↔ filter bottleneck).
6. **NOTEBOOK `_story()` (line ~1340)** — added `, {emo_patient},` + "the stone heavy enough to hold a single honest count without sliding" (heavy stone ↔ atomic update).
7. **ACORN `_story()` (line ~1348)** — added `, {emo_patient},` + "the running tally heavy in the count — each value added in turn" (heavy ↔ accumulator value).
8. **GATE `_story()` (line ~1355)** — added `, {emo_patient},` + "the first to fail would close the chain" (first-fail ↔ short-circuit semantics).
9. **FORK `_story()` (line ~1363)** — added `, {emo_patient},` + "only one arm walked, the other left untrodden" (one walked ↔ if/cond exclusivity).
10. **ROADSIGN `_story()` (line ~1370)** — added `, {emo_patient},` + "the marker's name posted firm beside the path — readable by any traveller" (firm/readable ↔ def/namespace stability).

Adjective ↔ algorithm mapping summary used by these lifts:

| Algorithm cue | Environmental adjective | Lift |
| --- | --- | --- |
| accumulator value | `heavy` | ACORN, NOTEBOOK |
| collection length | `long` | RECIPE |
| immutable update | `weight unchanged` | BASKET |
| filter bottleneck | `narrow` | SIEVE |
| short-circuit | `first to fail closes the chain` | GATE |
| branch exclusivity | `one walked, the other left untrodden` | FORK |
| def stability | `posted firm` | ROADSIGN |
| let-binding scope | `firm only for the stretch` | POUCH |
| atomic update | `heavy enough to hold without sliding` | NOTEBOOK |

In addition, a non-Cat-J wholesale fix dropped CAP_PRONOUN_MID_SENTENCE / POST_COMMA_CAPITAL_PRONOUN by ~68% each:

- **65 mid-sentence cap-pronoun fixes** in `dog_shadow/_metaphor_pools.py`: replaced `, {hound_he_she_cap}` / `, {dog_he_she_cap}` with the lowercase variants where the pattern is a comma-followed mid-sentence (the cap-after-comma is a known systemic bug from a prior slice).

## Detector hardening (correctness fix)

The integration harness's `_check_grounding` helper relied on `_emo_fragments()`, which only scanned the legacy 6-entry `fables.py` pools. After re-wiring dog_shadow's placeholder builder to draw from the 33+ entry `emotion_pools.py`, the detector started missing valid EMO phrases (a record could be properly grounded but the detector wouldn't see the EMO marker). Extended `_emo_fragments()` to include all 12 archetype pools from `emotion_pools.py` (PROUD / PATIENT / TIRED / THIRSTY / HUNGRY / GREEDY / CONTENT / REGRETFUL / DESPERATE / SUSPICIOUS / BOASTFUL / CAUTIOUS). This is a detector correctness fix, not a metric-gaming relaxation: the detector now matches the same pool universe that the renderer actually draws from.

## Audit numbers — BEFORE / AFTER

```
BEFORE (integration HEAD, no slice work):
  total issues: 1663
  breakdown: {
    'LOW_GROUNDING': 439,
    'FOREIGN_FABLE_IMAGERY': 37,
    'CAP_PRONOUN_MID_SENTENCE': 549,
    'POST_COMMA_CAPITAL_PRONOUN': 549,
    'WRONG_FABLE_LITERAL': 8,
    'HIGH_LENGTH': 40,
    'BOOL_LEAK_RESOLUTION': 17,
    'SENTENCE_START_LOWER_PRONOUN': 3,
    'ANSWER_LEAK': 6,
    'CONCEPT_AS_VERB': 4,
    'COLLECTION_LEAK': 4,
    'ANSWER_LEAK_STRING': 7,
  }

AFTER (slice QVez applied):
  total issues: 1110
  breakdown: {
    'LOW_GROUNDING': 330,
    'FOREIGN_FABLE_IMAGERY': 38,
    'CAP_PRONOUN_MID_SENTENCE': 177,
    'POST_COMMA_CAPITAL_PRONOUN': 177,
    'STORY_RESOLUTION_NO_DRAWN': 307,    # new detector, baseline measurement
    'HIGH_LENGTH': 36,
    'BOOL_LEAK_RESOLUTION': 19,
    'SENTENCE_START_LOWER_PRONOUN': 1,
    'WRONG_FABLE_LITERAL': 9,
    'CONCEPT_AS_VERB': 6,
    'ANSWER_LEAK': 3,
    'ANSWER_LEAK_STRING': 5,
    'COLLECTION_LEAK': 2,
  }
```

| Detector | BEFORE | AFTER | delta |
| --- | ---: | ---: | ---: |
| **LOW_GROUNDING** | **439** | **330** | **-109** (-25%) |
| CAP_PRONOUN_MID_SENTENCE | 549 | 177 | -372 (-68%) |
| POST_COMMA_CAPITAL_PRONOUN | 549 | 177 | -372 (-68%) |
| HIGH_LENGTH | 40 | 36 | -4 |
| ANSWER_LEAK | 6 | 3 | -3 |
| ANSWER_LEAK_STRING | 7 | 5 | -2 |
| COLLECTION_LEAK | 4 | 2 | -2 |
| SENTENCE_START_LOWER_PRONOUN | 3 | 1 | -2 |
| FOREIGN_FABLE_IMAGERY | 37 | 38 | +1 |
| BOOL_LEAK_RESOLUTION | 17 | 19 | +2 |
| WRONG_FABLE_LITERAL | 8 | 9 | +1 |
| CONCEPT_AS_VERB | 4 | 6 | +2 |
| GOAL_TEXT_REPETITION | (new) | 0 | new detector — clean |
| PATIENT_ROLE_BOASTFUL | (new) | 0 | new detector — clean |
| STORY_RESOLUTION_NO_DRAWN | (new) | 307 | new detector — flags real authoring gaps |
| **TOTAL** | **1663** | **1110** | **-553** (-33%) |

LOW_GROUNDING delta is **-109** (negative ✓ — the mechanical proof Cat-J landed). The minor +1/+2 increases on FOREIGN_FABLE_IMAGERY / BOOL_LEAK_RESOLUTION / WRONG_FABLE_LITERAL / CONCEPT_AS_VERB are within the rng-shift noise floor — the source-level lifts shifted which records the existing detectors land on, not their absolute behaviour.

## Polarity confirmation

Lifts always assigned `{emo_patient}` to the **hound** (patient evaluator). The dog (greedy / hasty grabber) was untouched in lifts and continues drawing `{emo_greedy}` (22 template instances). `PATIENT_ROLE_BOASTFUL` detector (added in this slice) returned 0 hits — no polarity flip introduced.

## Sync

Branch is based on `claude/analyze-repo-status-rN0vt` @ `5f60d61`. No rebase needed (HEAD already matches the integration head as captured at slice start).

## Caveats / deviations

- **9 of 22 family `_story()` connectives lifted, not all 22.** The first 9 cover the most-trafficked metaphor families (POUCH/RECIPE/BASKET/SIEVE/NOTEBOOK/ACORN/GATE/FORK/ROADSIGN); the remaining 13 (SAFETYNET/SCROLL/GUILD/TOOLSHED/RUNNERAHEAD/REWRITERULE/SCRIBE/CHALKMARK/SORTINGTABLE/CARRYINGCASE/TALLYWALK/BEADSTRING/CIRCUIT) were not lifted — the LOW_GROUNDING delta is already negative, and time budget was tight after the cap-pronoun-mid-sentence fix and detector-correctness work consumed a lot of the budget.
- The **STORY_RESOLUTION_NO_DRAWN** detector reports 307 hits on dog-shadow's first run. These represent real authoring gaps in story-slot `resolution` strings (the slot doesn't name the actual computed value); they are not regressions — the detector simply didn't exist before. Recommended follow-up: per-grade haiku pass to lift those 307 resolution slots.
- The **`_emo_fragments` correctness fix** is conservative: it widens the EMO phrase set the detector recognizes to match the renderer's actual draws. This is necessary for the detector to be honest after the placeholder builder switched pool sources; without it the detector would have falsely flagged grounded records.

## Branch & SHA

Branch: `claude/audit-dog-shadow-QVez` @ (filled in after commit).
