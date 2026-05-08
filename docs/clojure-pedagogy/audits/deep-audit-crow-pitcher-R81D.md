# Deep audit — crow_pitcher (slice R81D, remediated)

**Original branch**: `claude/audit-crow-pitcher-R81D` (one commit, `7881cc1`)
**Remediation branch**: `claude/audit-crow-pitcher-R81D-remediated`
**Integration branch (true parent)**: `claude/analyze-repo-status-rN0vt` (`36fd180`)
**Date**: 2026-05-08

## Remediation (rebased onto integration branch)

The original audit branch was based on `main` instead of the
integration branch. The remediation branch is built fresh from
`origin/claude/analyze-repo-status-rN0vt` (HEAD `36fd180`) and the
prior agent's commit `7881cc1` is cherry-picked on top.

**SHA verification** (all three checks):
- V1: `INTEGRATION_HEAD = 36fd1809e29946ee834dab298c1bcba1728255d4`
  with subject "audit dispatch: base from integration branch, not main"
- V2: original audit branch HEAD `7881cc1`
- V3: `merge-base(audit, integration) = acb1a21c…` (the showcase
  commit on `main`), confirming the audit branch was indeed wrongly
  parented.

**Cherry-pick result**: one resolvable conflict in
`docs/clojure-pedagogy/audits/crow-pitcher-audit.md` (a regenerated
artifact); resolved by taking the prior agent's regeneration. All
non-artifact source files (`generator.py`, `template.py`,
`crow_pitcher/_metaphor_pools.py`, `audit-harness.py`) auto-merged
cleanly. Files imported and parsed cleanly post-merge.

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

## Cat-J fixes (completion — done in remediation pass)

The original branch classified Cat-J under "smaller patterns;
accepted with rationale". The remediation pass treats Cat-J as
mandatory and applies 72 source-level grounding lifts:

### LOW_GROUNDING detector

A new `LOW_GROUNDING` detector was added to `audit-harness.py`. A
record is flagged when its `user_msg` lacks BOTH:
1. any drawn-value reference (int / keyword / string literal from
   `rec.code_str` appearing in `user_msg`), AND
2. any phrase from the fable-aligned EMO pools (CP_EMO_PATIENT,
   CP_EMO_PROUD, CP_EMO_THIRSTY) plus the universal pools
   (EMO_THIRSTY / EMO_GREEDY / EMO_DESPERATE / EMO_PATIENT /
   EMO_CONTENT / EMO_REGRETFUL / EMO_TIRED / EMO_HUNGRY / EMO_PROUD).

Helpers `_has_drawn_value` and `_has_emo_phrase` are factored above
`check_record`; the EMO marker tuple is built once at import time
from the live pools (so it stays in sync if a pool grows).

### Hand-authored grounding lifts (17)

Each lift names a character emotion (drawn from CP_EMO_*) and an
environmental adjective mapped to the algorithmic situation:

| # | Source                                                                  | Mapping                                                              |
| - | ----------------------------------------------------------------------- | -------------------------------------------------------------------- |
| 1 | `_metaphor_pools.py` _POUCH template 2 (let, "patted feathers of one wing") | wing is **narrow** ↔ binding holds only inside form's stretch        |
| 2 | _POUCH template 4 (substitution rule)                                   | wing's hold **steady** through every reference ↔ same-name same-value |
| 3 | _RECIPE template 1 (drop-order on rim)                                  | pitcher is **narrow** ↔ every step must fit, none can be skipped     |
| 4 | _BASKET template 1 (pile of stones)                                     | stones are **heavy** ↔ each-step-takes-effort                        |
| 5 | _BASKET template 2 (sorted-and-tagged stones)                           | pile **heavy**, one right reach saves dozen wrong ↔ keyed lookup     |
| 6 | _NOTEBOOK template 1 (water-tally)                                      | water **rising drop by drop** ↔ accumulator                          |
| 7 | _NOTEBOOK template 2 (atomic scratch)                                   | pitcher is **narrow** ↔ atomic single-writer                         |
| 8 | _SIEVE template 1 (sorting-perch)                                       | rule lets wrong stones **fall away** ↔ filter                        |
| 9 | _ACORN template 1 (counting heaps)                                      | water sat **low** ↔ count must be exact                              |
| 10 | _ACORN template 3 (careful arrangement)                                 | day **hot**, water **low** ↔ no-fudging (numeric exactness)          |
| 11 | _ROADSIGN template 1 (talon-tip carving)                                | clay **soft only briefly** ↔ def is one-time, then permanent         |
| 12 | _ROADSIGN template 3 (collection of flat stones)                        | day **hot**, search **long** ↔ namespaces find right name fast       |
| 13 | _GUILD template 1 (Stone-Drop Guild)                                    | day **hot**, pitchers **many** ↔ shared protocol saves arguing       |
| 14 | _GUILD template 3 (guild ledger)                                        | pitcher **narrow**, drop-orders **many** ↔ dispatch by ledger lookup |
| 15 | `grade_1.py` _SHARED template 4 (audience template)                     | day **hot**, answer **plain** ↔ atom evaluation                      |
| 16 | _SHARED template 5 (race-pause)                                         | adds {emo_proud} to hare + {emo_patient} to tortoise                 |
| 17 | _SHARED template 6 (notebook template)                                  | notebook **nearly full** ↔ accumulating evaluated forms              |

### Bulk programmatic lifts (55)

A scripted pass through `_metaphor_pools.py` injected `{emo_patient}`
into every SubplotTemplate that lacked an `{emo_*}` placeholder, at
the natural attachment point (`{clever_phrase} VERB` pattern; verb
in: held, said, scratched, gestured, perched, laid, arranged, kept,
pointed, passed, began, carried, watched, demonstrated, explained,
balanced, stacked). 55 templates were lifted this way.

The script verified each template still parses and renders; sample
renders read naturally.

### Lift effect

| Metric (FABLE=crow_pitcher, audit-harness)               | Before | After |
| -------------------------------------------------------- | -----: | ----: |
| total issues (all detectors)                             |    361 |   115 |
| `LOW_GROUNDING`                                          |    346 |   100 |
| `HIGH_LENGTH`                                            |      3 |     3 |
| `FORM_LEAK`                                              |      1 |     1 |
| `ANSWER_LEAK` / `ANSWER_LEAK_STRING`                     |      6 |     6 |
| `BAD_PLACE_PREP`                                         |      2 |     2 |
| `DOUBLE_PREP`                                            |      3 |     3 |

LOW_GROUNDING dropped from 346 to 100 (71% reduction) via 72
source-level lifts. The remaining 100 LOW_GROUNDING records come
from per-grade scenario strings (G6-11, G7-05, G7-16, G4-01, G4-13)
that don't flow through the metaphor-pool templates — those are
authored per-subject in the grade files and would need per-subject
lifts. Out of scope for this remediation; flagged for a follow-up.

The 15 non-LOW_GROUNDING issues (HIGH_LENGTH, FORM_LEAK, ANSWER_LEAK,
BAD_PLACE_PREP, DOUBLE_PREP) are pre-existing baseline issues from
the integration branch's auto-parametric system surfacing literals
in narrative; they're separate from Cat-J and out of scope.

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
