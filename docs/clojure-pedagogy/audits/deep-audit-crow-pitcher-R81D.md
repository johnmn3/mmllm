# Deep audit — crow_pitcher (slice R81D)

**Branch**: `claude/audit-crow-pitcher-R81D`
**Audit instructions origin**: `claude/analyze-repo-status-rN0vt`
**Date**: 2026-05-08

## Slice

- **Fable**: `crow_pitcher`
- **Grades sampled (random sample of 6 of 12)**: 1, 4, 6, 7, 8, 9
- **Read corpus**: 1,245 records (5 renders × 249 examples across 6 grades)

## Baseline

```
FABLE=crow_pitcher python docs/clojure-pedagogy/audits/audit-harness.py
total issues: 0   (clean before this slice landed)
```

## Papercut summary

Eight distinct patterns surfaced from reading the corpus. Counts are
across the 1,245-record slice unless otherwise noted.

| Cat   | Slug                          | Count | Status                                       |
| ----- | ----------------------------- | ----: | -------------------------------------------- |
| Cat-C | `cap-pronoun-mid-comma`       |   369 | **fixed at source** (template), detector added |
| Cat-C | `bird-body-articles`          |    62 | **fixed at source** (EMO pool), detector added |
| Cat-C | `bad-place-prep` (extension)  |    54 | **fixed at source** (place_phrase), detector added |
| Cat-I | `cliche-meta-phrases`         |  ~115 | partially mitigated (EMO pool diversified)   |
| Cat-J | `flat-emotion-grade7-8`       |  ~55  | accepted (intentional info-density at scale) |
| Cat-C | `pronoun-number-mismatch`     |   ~32 | subsumed by Cat-C / `cap-pronoun-mid-comma`  |
| Cat-E | `pile-metaphor-overuse`       |  ~12  | accepted (semantic ambiguity, not a bug)     |
| Cat-H | `role-polarity-flip`          |   ~8  | accepted (intentional fable-narrative beat)  |

The full per-pattern catalog (representative quotes, file:line refs,
source traces, fix guidance) lives at `/tmp/audit/papercuts-catalog.md`
and is not committed (per playbook: deliverable doc is the sole doc).

## New detectors added to `audit-harness.py`

Three new detectors plus an extension to one existing detector. All
use simple regex; none parse the AST.

### 1. `CAP_PRONOUN_MID_SENTENCE`  (Cat-C)

Catches a capitalized subject pronoun (`She` / `He` / `They`) that
appears mid-sentence after a comma. The story-template pattern
`To {goal_text}, {clever_he_she_cap} composed…` produces
`To bind X, She composed…`, which is grammatically wrong (mid-sentence
capitalization). The fix at source is to use `_he_she` (lowercase)
after a comma and reserve `_he_she_cap` for sentence-initial position.

```python
cap_mid_re = re.compile(
    r",\s+(She|He|They)\s+"
    r"(?:composed|wrote|submitted|chose|set|tested|checked|added|"
    r"swapped|paused|brought|read|laid|scratched|extracted|built|"
    r"intended|coordinated|reached|ran|dispatched|started|prepared)"
    r"\b"
)
```

Cross-fable visibility: this detector now fires
**1,015** times on `tortoise_hare`, **1,057** on `boy_wolf`, **990** on
`dog_shadow`, **217** on `milkmaid` — all surface the same template
pattern in those fables' metaphor pools, exactly as designed (the
playbook's "one detector reveals the cousin pattern" principle).
Those fixes belong to the corresponding audit slices.

### 2. `DEFINITE_BODY_PART`  (Cat-C / Cat-G)

Catches participle phrases that prefix a bird body part with a
definite article: `clicking the beak`, `cocking the head`,
`spreading the wings`, etc. Source-level the fix is to either drop
the article (`with a self-satisfied beak-click`) or use possessive-
agnostic phrasing (`with a confident tilt of the head`).

```python
body_part_re = re.compile(
    r"\b(?:clicking|cocking|tilting|preening|fluffing|ruffling|"
    r"tucking|spreading|opening|flicking|stretching|smoothing)"
    r"\s+the\s+"
    r"(?:beak|head|wings?|feathers?|tail|throat|crest)\b"
)
```

This detector covers any future regression in the EMO pool plus
catches the same pattern if other crow / bird fables (e.g. fox-grapes
when the fox eyes a vine, ant-grasshopper when the grasshopper preens)
import or copy the structure.

### 3. `BAD_PLACE_PREP` extension

Added `on the village` and `on the market` to the bad-place-prep
list. Both render as standing-atop a zone, which is non-idiomatic;
markets and villages are zones one is `at` / `in` / `near`. Important
nuance: the new pattern only fires when followed by a phrase
terminator (punctuation or end-of-line) so it doesn't false-positive
on compound nouns like *"on the market pitcher's clay"* (a real
crow_pitcher scenario where "market pitcher" is the compound noun).

```python
for bad in ("on the village", "on the market"):
    if re.search(re.escape(bad) + r"\b(?=[\s]*(?:[.,;:!?]|$))",
                 user, re.MULTILINE):
        issues.append(("BAD_PLACE_PREP", f"'{bad}' (wrong preposition)"))
        break
```

## Source-level fixes applied

### Fix 1: `place_phrase` — drop "on" from market/village

`src/mmllm/aesop/template.py:484`. Markets and villages are not
surfaces; one is `at / in / near / by` them, never "on". Farms keep
"on" because *"on the farm"* is idiomatic. This is a shared utility,
so the fix elevates all fables that use these locations
(`crow_pitcher`, `milkmaid`, `goose_eggs`, `boy_wolf`, `tortoise_hare`).
No fable explicitly relies on the "on the village" / "on the market"
output; smoke tests pass.

### Fix 2: `CP_EMO_PROUD` — definite-article body parts

`src/mmllm/aesop/curriculum/generator.py:305-312`. Two pool entries
were rewritten to drop the definite article:

```
"clicking the beak in self-satisfaction"  →  "with a self-satisfied beak-click"
"cocking the head with certainty"          →  "with a confident tilt of the head"
```

Verified: `0/380` post-fix records contain the body-part-with-article
pattern (vs 25/380 before).

### Fix 3: `_he_she_cap` after comma → `_he_she`

`src/mmllm/aesop/curriculum/crow_pitcher/_metaphor_pools.py`. 102
occurrences of the `, {role}_he_she_cap` pattern (80 single-line + 22
multi-line wrap) were converted to `, {role}_he_she`. Sentence-initial
`{role}_he_she_cap` left intact. The template still capitalizes
properly when the pronoun starts a sentence; only mid-sentence cases
are downcased.

### Fix 4: `CP_EMO_PATIENT` — diversify cliché phrases

`src/mmllm/aesop/curriculum/generator.py:297-304`. Added 4 new
patient-emotion entries that don't carry the *"stone after stone"* /
*"form after form"* cadence:

```
"patient as the water rose"
"letting the count rise on its own"
"watching the level lift, drop by drop"
"deliberate, unhurried by the rising sun"
```

Pool size went 6 → 10. Cliché-concentration drops mechanically.

## Before / after

| Metric                                          | Before | After |
| ----------------------------------------------- | -----: | ----: |
| `audit-harness.py FABLE=crow_pitcher` issues    |      0 |     0 |
| `CAP_PRONOUN_MID_SENTENCE` (corpus, n=1245)     |   369  |     0 |
| `DEFINITE_BODY_PART` (corpus, n=1245)           |    62  |     0 |
| `BAD_PLACE_PREP on the village/market` (corpus) |    54  |     0 |
| Curriculum imports + render smoke               |     ✓  |     ✓ |

The detector additions are net-positive across all fables because
they surface the same template patterns in `tortoise_hare`,
`milkmaid`, `boy_wolf`, `dog_shadow`. Those fixes belong to other
audit slices and are out of scope for this branch.

## Pedagogical-polarity check

Verified that the wise / patient role still does the careful thing
(`{clever}` = stone-dropper) and the hasty role still overreaches
(`{hasty}` = guesser); no Cat-F polarity flips found in the slice.
Crow-pitcher's moral (patience vs. thirst, the patient creature wins)
is preserved through every rendered record.

## Cat-J affirmative-lift status

The catalog flagged ~55 grade-7/grade-8 records with thin emotional
grounding. Reviewing a sample, the records do still carry the fable
opener and the metaphor template — the "thinness" was relative to
grade-1, where every record carries an EMO phrase, vs grade-7+ where
the template is denser with Clojure-specific vocabulary and the EMO
pool injection rate is lower by design. We left this as accepted for
the slice; a follow-up slice on grades 7-8 specifically could re-tune
the EMO injection probability if desired.

## Caveats

- The detector additions surface real patterns in the four other
  Phase-C-complete fables (1,015 + 217 + 1,057 + 990 hits across them
  combined). Those are in scope only for their respective audit slices.
- `numpy` isn't installed in this environment so the full
  `scripts/smoke_phase0.py` numpy-based corpus smoke can't run; the
  curriculum-only smoke (import + render across all 5 fables) does pass.
- The Cat-I-1 fix only diversifies the EMO pool; the metaphor-template
  cliché *"stone after stone"* still appears via templates. A deeper
  fix would parametrize that across templates; deferred.
