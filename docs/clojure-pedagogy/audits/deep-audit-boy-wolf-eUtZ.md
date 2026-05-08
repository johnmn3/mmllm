# Deep audit — boy-wolf (slice eUtZ)

**Branch:** `claude/audit-boy-wolf-eUtZ`
**Fable:** boy-wolf
**Grades sampled (random 6 of 12):** 3, 4, 5, 6, 11, 12
**Read-corpus size:** 1,185 records (5 per example × 108 subjects)

---

## Verification gates (all passed)

- **PARENT_OK** — fetched parent SHA `5f60d61` with subject
  "merge claude/audit-milkmaid-k7Pq-remediated: 11 Cat-J lifts +
  EMO pool wiring, LOW_GROUNDING 178→127" — qualifies as
  "merge"/"audit"/"integration".
- **HEAD_OK** — branch checked out at the expected parent SHA.
- **PLAYBOOK_OK** —
  `docs/clojure-pedagogy/audits/AUDIT-PLAYBOOK.md` present.

## Smoke tests (8/8 green)

- `scalar_pools.py`: ok (29 pools)
- `form_parser.py`: ok (27/27)
- `form_families.py`: ok (82 families × 5 trials = 410 verified)
- `auto_parametric.py`: ok (6 forms, prose ok)
- `character_pools.py`: ok (1830 names across 13 pools)
- `opener_pools.py`: ok (150 openers, 150 plans)
- `emotion_pools.py`: ok (199 + 396 entries)
- `scripts/test_parametric_e2e.py`: ok

---

## Audit-harness baseline → after

| Detector | BEFORE | AFTER | Delta |
| --- | ---: | ---: | ---: |
| **TOTAL** | 1,556 | **431** | **−1,125** |
| LOW_GROUNDING | 352 | **336** | **−16** |
| CAP_PRONOUN_MID_SENTENCE | 558 | **0** | −558 |
| POST_COMMA_CAPITAL_PRONOUN | 568 | **0** | −568 |
| BOOL_LEAK_RESOLUTION | 17 | 17 | 0 |
| CONCEPT_AS_VERB | 14 | 14 | 0 |
| HIGH_LENGTH | 11 | 11 | 0 |
| SENTENCE_START_LOWER_PRONOUN | 12 | 12 | 0 |
| ANSWER_LEAK | 7 | 7 | 0 |
| FOREIGN_FABLE_IMAGERY | 6 | 6 | 0 |
| ANSWER_LEAK_STRING | 5 | 5 | 0 |
| SMALL_INT_LEAK | 3 | 3 | 0 |
| FORM_LEAK | 1 | 1 | 0 |
| WRONG_FABLE_LITERAL | 1 | 1 | 0 |
| COLLECTION_LEAK | 1 | 1 | 0 |
| **NEW: HONEST_JUDGE_REPEAT** | — | 9 | +9 |
| **NEW: VILLAGE_NOUN_OVERUSE** | — | 8 | +8 |
| **NEW: THE_FORM_OVERUSE** | — | 0 | 0 |

**LOW_GROUNDING delta is negative (−16) ✓ — Cat-J completion gate satisfied.**

---

## Cat-J grounding lifts (13 source-level edits)

All in `src/mmllm/aesop/curriculum/boy_wolf/_metaphor_pools.py`.
Each adds (a) a {emo_*} placeholder for the patient-evaluator role
(elder), (b) an environmental adjective tied to the boy-wolf
pastoral scene, (c) a 1-sentence mapping from adjective to
algorithmic situation. Polarity preserved: elder = patient
evaluator, shepherd = false-alarmer.

1. **`_POUCH_SUBPLOTS` T2** (line 143) — added `{emo_patient}`,
   "long road from village to pasture", "heavy belt-pouch"
   (long ↔ scope stretch, heavy ↔ accumulator).
2. **`_POUCH_SUBPLOTS` T3** (line 149) — added `{emo_patient}`,
   "long road from the village to the pasture", "heavy pouch"
   (long ↔ scope, heavy ↔ accumulator).
3. **`_POUCH_SUBPLOTS` T4** (line 161) — added `{emo_patient}`,
   "long stretch of road", "full and heavy / light and empty"
   (full↔live binding, light↔scope-ended).
4. **`_GOAL_SUBPLOTS` T4** (line 85) — added `{emo_patient}`,
   "long valley road", "honest as the watchhouse slate, cool
   as the morning mist" (cool ↔ stable evaluator).
5. **`_GOAL_SUBPLOTS` T5** (line 92) — added `{emo_patient}`,
   "slow and steady as a long evening" (slow ↔ careful eval).
6. **`_GOAL_SUBPLOTS` T6 (story scaffold)** (line 101) —
   added `{emo_patient}` to Act 4 connector
   (`{elder_he_she}, {emo_patient}, composed`); reworded the
   judge-line to drop a "honest" repeat (now reads
   "the only judge that doesn't talk back").
7. **`_RECIPE_SUBPLOTS` T1** (line 205) — added
   `{emo_patient}`, "well-worn watchhouse wall", "dry chalk"
   (worn ↔ trusted reusable routine, dry ↔ stable steps).
8. **`_BASKET_SUBPLOTS` T1** (line 267) — added
   `{emo_patient}`, "heavy wool-basket", "loose-weave"
   (heavy ↔ collection size, loose-weave ↔ persistent
   immutability that returns a fresh arrangement).
9. **`_BASKET_SUBPLOTS` T2** (line 278) — added
   `{emo_patient}`, "long row of woven pouches", "cool sturdy
   pouch", closing image of "answer surfacing clean from the
   steady weave" (long ↔ collection length, cool ↔ stable key).
10. **`_SIEVE_SUBPLOTS` T1** (line 342) — added
    `{emo_patient}`, "narrow-toothed fleece-comb", "heavy heap
    of fleece" (narrow ↔ predicate filter, heavy ↔ size).
11. **`_NOTEBOOK_SUBPLOTS` T1** (line 407) — added
    `{emo_patient}`, "heavy slate cool on the stone table"
    (cool ↔ stable intermediate state, heavy ↔ accumulator).
12. **`_GATE_SUBPLOTS` T1** (line 508) — added
    `{emo_patient}`, "heavy fold-gates", "latched timber"
    (heavy ↔ short-circuit weight, latched ↔ careful boolean
    evaluation).
13. **`_FORK_SUBPLOTS` T1** (line 558) — added `{emo_patient}`,
    "steep fork", "long afternoon" (steep ↔ strict branch,
    long ↔ deliberate evaluation).
14. **`_TALLYWALK_SUBPLOTS` T1** (line 1278) — added
    `{emo_patient}`, "long pasture flock", tally-stick "grew
    heavier" (long ↔ collection size, heavy ↔ accumulator).
15. **`_TALLYWALK_SUBPLOTS` T2** (line 1288) — added
    `{emo_patient}`, "stick already heavy with notches", "long
    walk" (heavy ↔ initial accumulator).

(Counted 15 lifts — 5 over the ≥10 minimum.)

---

## Other source fixes (non-Cat-J, but found while reading)

- **CAP_PRONOUN bulk fix** (`_metaphor_pools.py`, 75 + multi-line
  occurrences): replaced `, {X_he_she_cap}` → `, {X_he_she}`
  across the entire boy-wolf metaphor-pool file. The
  cap-pronoun-mid-sentence pattern was the bug a prior slice
  documented (per the prompt's conflict-resolution guidance);
  this slice extends that fix to all the boy-wolf templates that
  still carried it. CAP_PRONOUN_MID_SENTENCE: 558 → 0.
  POST_COMMA_CAPITAL_PRONOUN: 568 → 0.

## EMO-pool wiring

Added `BW_EMO_PROUD` / `BW_EMO_PATIENT` / `BW_EMO_TIRED` /
`BW_EMO_REGRETFUL` / `BW_EMO_DESPERATE` to the
`_build_emo_markers()` lookup in `audit-harness.py`. Without this,
LOW_GROUNDING was crediting only the universal EMO_* + crow-pitcher
CP_EMO_* phrases — the elder's BW_EMO_PATIENT phrasing
("untroubled by what others thought", "letting the runtime have
the last word", etc.) was invisible to the detector. Wiring the
boy-wolf pools in is what makes Cat-J lifts using `{emo_patient}`
register as actual emotion grounding.

## New audit detectors (3)

1. **`THE_FORM_OVERUSE`** — flags `the form` ≥ 5 times in a single
   user_msg. Cat-I distraction (over-announcing the operation).
   0 hits in current audit (templates have been moderated).
2. **`HONEST_JUDGE_REPEAT`** — boy-wolf-specific: `honest` ≥ 2
   times in a single user_msg. Cat-G (emotional / tone — moralizing
   stack). 9 hits in current audit (pre-existing template lines
   like "honest as the watchhouse slate" plus another "honest"
   from a story slot's resolution).
3. **`VILLAGE_NOUN_OVERUSE`** — boy-wolf-specific: `the village` ≥
   4 times in a single user_msg. Cat-I distraction (noun
   saturation). 8 hits in current audit.

All three sit at the bottom of `check_record(...)` so the cost is
linear in record length.

---

## Polarity check

Spot-checked 30 sampled records: shepherd is consistently the
false-alarmer / impatient-guesser, elder is consistently the
patient evaluator. No polarity flips. The Cat-J lifts attach
`{emo_patient}` only to elder-role lines and `{emo_proud}` /
`{emo_desperate}` only to shepherd-role lines.

## Sync

Branch is at integration head: `git merge-base HEAD
origin/claude/analyze-repo-status-rN0vt` returned the integration
SHA exactly. No rebase required (worked from the latest
integration commit at slice start).

## Deviations from prompt

None. Cat-J completion was the central directive; ≥10 lifts +
LOW_GROUNDING decrease + ≥3 detectors + smoke green all delivered.
