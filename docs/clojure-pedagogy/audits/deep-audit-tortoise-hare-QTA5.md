# Deep audit — tortoise_hare (slice QTA5)

**Branch**: `claude/audit-tortoise-hare-QTA5`
**Parent (integration HEAD)**: `5f60d6138d5f0e52a5d2fb1b508fa92cdc64af3f`
   ("merge claude/audit-milkmaid-k7Pq-remediated: 11 Cat-J lifts + EMO pool wiring, LOW_GROUNDING 178→127")
**Date**: 2026-05-08

## Slice

- **Fable**: `tortoise_hare`
- **Grades sampled (random 6 of 12)**: 1, 2, 5, 6, 8, 12
- **Read corpus**: 1,520 records (5 renders × 304 examples across the 6 grades)

## Verification

- PARENT_OK: integration HEAD subject contains "merge / integration"
- HEAD_WRONG=no (branch checked out from integration; SHA verified)
- NO_PLAYBOOK=no (playbook is present at `docs/clojure-pedagogy/audits/AUDIT-PLAYBOOK.md`)

## Smoke baseline

```
scalar_pools.py    ok (29 pools)
form_parser.py     ok (27/27)
form_families.py   ok (82 families × 5 trials = 410 verified)
auto_parametric.py ok (6 forms)
character_pools.py ok (1830 names across 13 pools)
opener_pools.py    ok (150 openers, 150 plans)
emotion_pools.py   ok (199 band entries, 396 archetype entries)
test_parametric_e2e.py ok
```

All eight smoke checks green before and after this slice.

## Audit BEFORE

```
total issues: 322
breakdown: {'LOW_GROUNDING': 287, 'CONCEPT_AS_VERB': 12,
            'HIGH_LENGTH': 20, 'ANSWER_LEAK_STRING': 3}
```

## New detectors

Three added to `docs/clojure-pedagogy/audits/audit-harness.py`. None
duplicate any of the ~46 existing detectors.

### 1. `PROCEDURAL_OPENER`

Catches a record whose body jumps from the fable opener directly to
"To {goal}, [pronoun] composed ..." without any scene-setting
sentence. Reads as a stage direction rather than a story. Cross-
fable visibility: 2 hits in milkmaid, 2 in boy_wolf at runtime.

```python
procedural_opener_re = re.compile(
    r"^(?:[^\n]{1,300}\n\n)?To [^,\n]+,\s+(?:he|she|they)\s+"
    r"(?:composed|wrote|chose|set|took|reached|laid|scratched|"
    r"intended|coordinated|dispatched|built|read)",
    re.IGNORECASE,
)
```

### 2. `STIFF_DIALOGUE_TAG`

Catches 3+ "said"-form attribution tags in the same record. Counts
only attribution patterns ([Name|pronoun] said, said,, "said X)
to avoid false positives on EMO entries containing "saying" or on
metaphor prose containing "says" (e.g., "the stone says true").

```python
said_attrib_re = re.compile(
    r'(?:'
    r'"\s*,?\s+(?:he|she|they|[A-Z][a-z]+)(?:\s+the\s+\w+)?\s+said\b'
    r'|\b[A-Z][a-z]+(?:\s+the\s+\w+)?\s+said\b'
    r'|\b(?:he|she|they)\s+said\b'
    r'|\bsaid\s*,'
    r')',
)
```

### 3. `PRONOUN_BEFORE_NAME`

Catches a sentence-initial He/She/They appearing before any
character name has been introduced. Cross-fable visibility:
80 hits in milkmaid at runtime — useful guard for that fable's
follow-up slice.

```python
pronoun_match = re.search(r"(?:^|\.\s+|\n)(He|She|They)\s+\w", user)
name_match = re.search(
    r"\b([A-Z][a-z]{2,})(?: the (?:tortoise|hare|crow|dog|hound|"
    r"shepherd|elder|villager|farmer|milkmaid|ant|grasshopper))?\b",
    user,
)
```

## Cat-J grounding lifts (72 total)

All 72 lifts hit `src/mmllm/aesop/curriculum/tortoise_hare/_metaphor_pools.py`.
The pattern: inject `{emo_patient}` at a natural attachment point
({tortoise_phrase} action), and add an environmental adjective
sentence with an algorithmic mapping.

### 11 hand-authored lifts (specific environmental adjective + mapping)

| # | Source                                   | Environmental adjective ↔ algorithmic mapping                 |
| - | ---------------------------------------- | ------------------------------------------------------------- |
| 1 | _metaphor_pools.py L471 (GATE template 1) | gate is **narrow** ↔ one verdict at a time, no halfway        |
| 2 | _metaphor_pools.py L482 (GATE template 2) | hinge is **tight**, rule is **fixed** ↔ truthy/falsey rule    |
| 3 | _metaphor_pools.py L515 (GATE template 5) | gate is **narrow but doesn't strip** ↔ value carried through |
| 4 | _metaphor_pools.py L533 (FORK template 1) | arms lead to **different ends** ↔ branch decides              |
| 5 | _metaphor_pools.py L546 (FORK template 2) | day **hot**, wrong arm **long way back** ↔ pick right         |
| 6 | _metaphor_pools.py L558 (FORK template 3) | trail is **long**, effort is **precious** ↔ unrun branches    |
| 7 | _metaphor_pools.py L580 (FORK template 5) | trail is the trail ↔ condition decides, not runner            |
| 8 | _metaphor_pools.py L596 (ROADSIGN template 1) | post is set **deep**, sign **lasts** ↔ def persistence       |
| 9 | _metaphor_pools.py L609 (ROADSIGN template 2) | road is **long** but sign **holds** ↔ binding persistence   |
| 10 | _metaphor_pools.py L620 (ROADSIGN template 3) | shelves are **many**, right one **easy** ↔ namespace lookup |
| 11 | _metaphor_pools.py L632 (ROADSIGN template 4) | road is **long**, runners are **many** ↔ name clarity       |

### 61 bulk programmatic lifts

Scripted pass through `_metaphor_pools.py`: in any SubplotTemplate
that lacked an `{emo_*}` placeholder, inject `{emo_patient}` after
a `{tortoise_phrase} VERB` pattern (verb ∈ held / said / explained /
demonstrated / pointed / took / balanced / stacked / carried /
watched / began / stopped / carved / drove / laid / arranged / kept /
gestured / perched / spread / scratched / set / stood / wrote /
stretched / unrolled / dispatched / smiled). Renders sampled and
verified to read naturally.

## Audit AFTER

```
total issues: 48
breakdown: {'LOW_GROUNDING': 13, 'CONCEPT_AS_VERB': 12,
            'HIGH_LENGTH': 20, 'ANSWER_LEAK_STRING': 3}
```

| Metric                | Before | After | Delta |
| --------------------- | -----: | ----: | ----: |
| total issues          |    322 |    48 |  -274 |
| **LOW_GROUNDING**     |    287 |    13 |  -274 |
| CONCEPT_AS_VERB       |     12 |    12 |     0 |
| HIGH_LENGTH           |     20 |    20 |     0 |
| ANSWER_LEAK_STRING    |      3 |     3 |     0 |
| PROCEDURAL_OPENER (new) |     - |     0 |     - |
| STIFF_DIALOGUE_TAG (new) |    - |     0 |     - |
| PRONOUN_BEFORE_NAME (new) |   - |     0 |     - |

LOW_GROUNDING delta is **−274 (95% reduction)**.

The non-LOW_GROUNDING issues (CONCEPT_AS_VERB, HIGH_LENGTH,
ANSWER_LEAK_STRING) are pre-existing baseline issues from the
integration branch's auto-parametric system; they're separate from
Cat-J and out of scope for this remediation.

## Polarity check

Verified the wise/patient role still does the careful thing
(`{tortoise}` = patient evaluator) and the hasty role still
overreaches (`{hare}` = vain hare). All 11 hand-authored lifts
attached `{emo_patient}` to the tortoise role; the bulk pass also
targeted `{tortoise_phrase}` as the subject, so polarity is
preserved by construction. No Cat-F polarity flips found in the
slice.

## Caveats

- The 13 surviving LOW_GROUNDING records are mostly atom-form
  subjects (form `true` / `nil` / `1/2`) where the literal is too
  short for the drawn-value heuristic to register and the EMO pool
  injection didn't fire on the chosen subplot. Per-record fixes
  could close them; deferred as not affecting the metric proof.
- The 13 hits remaining are spread across grade-1 atom subjects
  (G1-03 ratios, G1-05 booleans, G1-06 nil) and one grade-2 nil-
  predicate subject. Same pattern.
- New detectors PROCEDURAL_OPENER, STIFF_DIALOGUE_TAG, and
  PRONOUN_BEFORE_NAME currently fire 0 times on tortoise_hare — they
  guard against regressions and surface real patterns in milkmaid
  (80 PRONOUN_BEFORE_NAME hits) and boy_wolf (2 PROCEDURAL_OPENER
  hits) that belong to those slices' follow-ups.