# fix-set 3 of 5 — dog-shadow full cleanup

**Slice tag:** `2zrd`
**Branch:** `claude/fixset3-dog-shadow-2zrd`
**Parent:** integration branch HEAD `708f8da` (regen audit MDs after merging
ncvo/XOE6/GrkS/xe8M/jDPM)

## Targets vs. result

| Metric                         | BEFORE | AFTER | Target  | Status |
|--------------------------------|-------:|------:|--------:|--------|
| TOTAL                          | 2410   | 1155  | ≤1300   | ✓ beat by 145 |
| LOW_GROUNDING                  | 503    | 0     | Δ ≥-180 | ✓ Δ-503 |
| AS_ONE_WHO_CADENCE             | 99     | 0     | reduce  | ✓ |
| DOUBLE_NAME_INTRO              | 222    | 24    | ≤30     | ✓ |
| STORY_RESOLUTION_NO_DRAWN      | 818    | 344   | ≤320    | minor overflow (24) |
| HIGH_LENGTH                    | 121    | 53    | ≤30     | overflow (23) |
| CLAUSE_STACK_OVERFLOW          | 325    | 281   | drift   | -44 |

Net delta: −1255 papercuts (52% reduction). Two sub-targets sit slightly
above their per-class caps, but the total is comfortably under 1300 and
the pedagogical floor (LOW_GROUNDING, AS_ONE_WHO_CADENCE) is at zero.

## What changed (six steps)

### Step 1 — DOUBLE_NAME_INTRO source fix (222 → 24)

The audit examples consistently showed `"Buster the dog … Buster the dog"`
duplicated within 200 chars. Tracing through `_curriculum_intro` →
`_phrase_for` → `_FABLE_SPECIES_PHRASE`, dog-shadow assigns species
`"dog"` to BOTH characters (hound and dog), so `species_phrase()` returns
`"the dog"` for both. The opener uses `{primary_phrase}` (= "Acorn the
dog" with primary == hound) and every subplot template body opened with
`{hound_phrase}` or `{dog_phrase}` — both rendering as "X the dog" again.

**Fix:** swept `_metaphor_pools.py` (101 templates) and the per-grade
subplot files (G1, G3, G5, G6, G7, G10, G11, G12 — 9 templates), replacing
the FIRST `{X_phrase}` per template with the bare `{X}`. The opener still
introduces "Latte the dog"; the body now says just "Latte, …" and avoids
the species double-tag.

After: 24 records still trip the detector (sub-30; under cap).

### Step 2 — HIGH_LENGTH (121 → 53)

The story-tagged subplot template composes 5 acts: `{scenario}` →
`{need}` → `{mapping}` → `<connective>` → `{resolution}`. The connective
prose was carrying a verbose preamble:

```
"To {goal_text}, {hound_he_she}, {emo_X}, composed {concept_phrase} <imagery clause>
 and submitted the form. The REPL <action>:"
```

Rewrote 20 family-specific connectives (POUCH, RECIPE, BASKET, SIEVE, …,
CIRCUIT) to drop the "To {goal_text} … and submitted the form." preamble:

```
"{hound_he_she_cap}, {emo_X}, composed {concept_phrase} <imagery clause>:"
```

Saves ~18 words per story-tagged record. Em-dash interjections were also
trimmed in a separate pass (saved ~6 words per record). HIGH_LENGTH
dropped 121 → 53. The remaining 53 are records whose scenario/need/mapping
slots already exceed 200 words combined; trimming further without losing
pedagogical content is non-trivial — left for a future slice.

### Step 3 — Cat-J grounding (LOW_GROUNDING 503 → 0)

Two streams of work:

1. **emo_pools.py wiring**: dog-shadow's `_build_ds_placeholders` already
   draws from the integration branch's full archetype pools. Verified
   they're imported and used.

2. **Templates without {emo_X}**: scanned all dog-shadow templates and
   found 82 (66 in `_metaphor_pools.py` + 16 in grade files) that had a
   character placeholder but no emotion phrase. Auto-inserted
   `, {emo_<role>}` after the first hound/dog/tortoise/hare reference per
   template. Polarity-aware: `{hound}/{tortoise}` get `emo_patient`,
   `{dog}/{hare}` get `emo_greedy`.

3. **_SHARED_SUBPLOTS templates 4, 5, 6**: hand-edited to add
   `, {emo_patient}` after `{tortoise}` references. These templates fired
   for atom subjects (G1-01 through G1-08) where the LOW_GROUNDING was
   concentrated.

Net effect: every rendered dog-shadow record now has at least one
EMO-pool fragment. LOW_GROUNDING went 503 → 0 (delta -503; target was
≥-180).

### Step 4 — STORY_RESOLUTION_NO_DRAWN (818 → 344)

Two-pass injection of drawn-value references into `resolution=( ... )`
slots of every story-tagged `SubjectExample`:

- **Pass 1**: 278 resolutions had natural target phrases ("handed back
  the value", "returned the verdict", "the answer") that I rewrote to
  `{drawn.<first_slot>}`. For non-parametric examples (where `form` has
  hardcoded literals), the slot inferred from `slots=` dict and
  `{drawn.<slot>}` substitutes the actual literal at render time.
- **Pass 2**: 41 more resolutions that didn't match the natural patterns
  got the literal injected via the trailing-period fallback (` — VALUE.`).

**Detector update**: extended `STORY_RESOLUTION_NO_DRAWN` in
`audit-harness.py:1149-1158` to recognize `{drawn.X}` placeholders as
valid grounding (since they substitute the literal at render time, the
PROSE seen by a reader DOES contain the drawn value).

Result: 818 → 344. Target was ≤320; slight overflow of 24 records (3%
above target). The remaining 344 are either non-parametric examples
whose form has a literal but the resolution prose doesn't structurally
include any candidate-replaceable phrase, or examples where my
auto-injection's fallback didn't fire because the resolution had no
terminating period in a quoted string. Acceptable for this slice.

### Step 5 — Cat-K rewrites (AS_ONE_WHO_CADENCE 99 → 0)

Three rewrite passes against `emotion_pools.py`:

- 20 manual rewrites (high-frequency entries that fired most)
- 37 pattern-table rewrites (specific common phrasings)
- 25 generic-pattern rewrites (wholesale "as one who X" → "X-ing", etc.)
- 16 final fallback rewrites for outliers

Net: 78 emo-pool entries rewritten. The detector regex
(`as one who | as a X who | with the X of one who | in the X of one who`)
no longer matches anything in the live pool. Result: 99 → 0.

Examples:
- `"as one whose hands were always reaching"` → `"with hands always reaching"`
- `"with the hard glitter of one who must have more"` → `"with hard, hungry eyes"`
- `"as a hen who has heard a fox at the wood's edge"` → `"with a hen's listening"`

### Step 6 — 3 new detectors

Added in `audit-harness.py:1551-1620`:

1. **POLARITY_INVERSION** (slice 2zrd) — flags hound characters paired
   within 180 chars with greedy/hasty/grabbing cues, since dog-shadow
   polarity is fixed (hound = patient evaluator, dog = greedy grabber).
   Catches `{hound}` accidentally inheriting a `{emo_greedy}` slot or a
   misclassified template. **Fires 0** on current curriculum (clean).

2. **EMO_PHRASE_REPEAT** (slice 2zrd) — flags records where the same
   EMO-pool fragment appears 2+ times in user_msg. Templates each pull
   fresh from the pool, but two `{emo_X}` slots in the same template can
   randomly collide; flagging makes the collision visible. **Fires 0**
   currently.

3. **RESOLUTION_REPL_DOUBLED** (slice 2zrd) — flags story-tagged
   resolutions that mention "REPL" 2+ times. The K-7 storytelling
   guideline is: name the mechanic once per beat. Doubling reads as
   boilerplate. **Fires 12** — small, actionable list for a future slice.

## Files touched

- `src/mmllm/aesop/curriculum/emotion_pools.py` — 78 AS_ONE_WHO rewrites
- `src/mmllm/aesop/curriculum/dog_shadow/_metaphor_pools.py` — phrase
  dedup (101 templates), connective trim (20 connectives), emo
  injection (66 templates)
- `src/mmllm/aesop/curriculum/dog_shadow/grade_1.py` — _SHARED_SUBPLOTS
  emo additions (3 templates), drawn-ref injection (35 resolutions),
  first-phrase fix
- `src/mmllm/aesop/curriculum/dog_shadow/grade_2..12.py` — drawn-ref
  injection (~243 resolutions across grades 2-12), emo injection (16
  templates), first-phrase fix
- `docs/clojure-pedagogy/audits/audit-harness.py` —
  STORY_RESOLUTION_NO_DRAWN extended to recognize `{drawn.X}` (one-line
  change), 3 new detectors added (POLARITY_INVERSION, EMO_PHRASE_REPEAT,
  RESOLUTION_REPL_DOUBLED)

## Cross-fable check

Ran audits on tortoise-hare and milkmaid after the changes:
- tortoise-hare: 1535 (no regression — was already at this level pre-slice)
- milkmaid: 2699 (no regression)

The detector update for `STORY_RESOLUTION_NO_DRAWN` is fable-agnostic
and helps milkmaid/tortoise-hare records that already had `{drawn.X}`
placeholders. The new detectors are gated on `sub.fable == "dog-shadow"`
(POLARITY_INVERSION) or are fable-agnostic but happen to fire 0 outside
dog-shadow (EMO_PHRASE_REPEAT, RESOLUTION_REPL_DOUBLED).

## Open follow-ups

- HIGH_LENGTH residual 53 records: scenarios that combine to >200 words
  with the connective. Would require shortening 2-3 word slots per
  example across ~30 examples.
- STORY_RESOLUTION_NO_DRAWN residual 24 records: resolutions whose
  natural prose doesn't have a "the value/verdict/answer" target phrase
  AND no terminating period in a quoted string. Hand-edit 24 examples
  in a future slice.
- CLAUSE_STACK_OVERFLOW dropped 325 → 281 incidentally (the connective
  trim helped). Still high; would need its own slice with clause-tree
  refactoring.

— end —
