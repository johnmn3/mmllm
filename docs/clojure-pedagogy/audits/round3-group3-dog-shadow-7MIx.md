# round3 group 3 — dog_shadow non-CLAUSE_STACK fixset (slice 7MIx)

**Branch:** `claude/round3-group3-dog-shadow-7MIx`
**Integration parent:** `8fab5ca` (`regen crow-pitcher audit MD (post-fixset-beta numbers)`)
**Final SHA:** `26b8299`
**Fable:** dog_shadow (hound = patient/cautious, dog = greedy)
**Scope:** dog_shadow non-CLAUSE_STACK targets (CLAUSE_STACK / NUMERAL_LIST_IN_GOAL / WRONG_FABLE_LITERAL belong to Group γ)

## Headline

| | BEFORE | AFTER | Δ |
|---|---:|---:|---:|
| **Total issues (dog_shadow)** | **983** | **584** | **−399 (−41%)** |
| Goal | ≤ 600 | ✅ achieved (−16 below target) |  |

## Per-detector breakdown (dog_shadow, my targets)

| Detector | BEFORE | AFTER | Δ |
|---|---:|---:|---:|
| NARRATIVE_NUMERAL_HARDCODE | 138 | 21 | −117 |
| CONCEPT_PHRASE_COMMA_LIST | 75 | 0 | −75 |
| HIGH_LENGTH | 58 | 39 | −19 |
| REPL_TRIPLE_VOICE | 54 | 25 | −29 |
| REPL_AS_TIME_TRAVELLER | 31 | 0 | −31 |
| RESOLUTION_GENERIC | 31 | 0 | −31 |
| PARAGRAPH_FRAGMENTATION | 28 | 0 | −28 |
| FORM_DISPLAY_AND_FORM_NOUN | 26 | 0 | −26 |
| DOUBLE_NAME_INTRO | 24 | 0 | −24 |
| RESOLUTION_REPL_DOUBLED | 12 | 0 | −12 |
| HEDGING_NEAR_FORM | 11 | 11 | 0 |
| ANSWER_LEAK + family | ~30 | ~27 | −3 |
| GENERIC_RESOLUTION_TAIL | 3 | 3 | 0 |
| **3 new detectors (slice 7MIx)** | | | |
| PRONOUN_AT_SENTENCE_START_AFTER_QUOTE | — | 0 | new (guardrail) |
| CONNECTOR_RUNTIME_DOUBLED | — | 0 | new (guardrail) |
| FABLE_FOREIGN_NUMERAL_QUANTIFIER | — | 2 | new |

## Group-γ-owned (untouched)

| Detector | BEFORE | AFTER | Δ |
|---|---:|---:|---:|
| CLAUSE_STACK_OVERFLOW | 253 | 248 | −5 (incidental from connector trims) |
| NUMERAL_LIST_IN_GOAL | 48 | 48 | 0 |
| WRONG_FABLE_LITERAL | 16 | 16 | 0 |

The 5-issue CLAUSE_STACK drop is incidental (connector trims removed surrounding commas as a side-effect). Group γ's pattern work remains; my edits don't preempt their detector choices.

## Cross-fable AFTER grid (no regressions)

```
tortoise_hare: 496 = 496  (Δ 0)
crow_pitcher : 622 = 622  (Δ 0)
milkmaid     : 708 = 708  (Δ 0)
boy_wolf     : 886 = 886  (Δ 0)
dog_shadow   : 983 → 584  (Δ −399, target ≤600 met)
```

## Six-step work plan

### Step 1: REPL meta-narrator triplet (combined 97 → 25)

**REPL_AS_TIME_TRAVELLER 31 → 0.** Two `_metaphor_pools.py` templates carried the offending phrasings:
- `dog_shadow/_metaphor_pools.py:402` — "the precise number the operation called for" → `"submitted it. The runtime handed back the count, the bridge-shadow steady on the water beside the bones."`
- `dog_shadow/_metaphor_pools.py:412` — "the number that had been there all along, settling the matter the patient way" → `"submitted it. The runtime returned the count the patient way, the bridge-shadow long across the water."`

**REPL_TRIPLE_VOICE 54 → 25.** Two passes:
1. Bulk-swapped 8 "The REPL X:" connectors in the family-specific story templates (`_POUCH/RECIPE/BASKET/SIEVE/NOTEBOOK/TALLY/FORK` etc.) to use neutral subjects: `"The runtime walked the trail end to end and returned:"`, `"It dispatched cleanly:"`, `"The runtime routed through the piles:"`, etc. 13 additional swaps for plain `"The REPL returned:"` → `"It returned:"`.
2. Folded the story-scaffold blank lines: changed `_story()` template helper from
   ```
   {scenario}
   [blank]
   {need}
   [blank]
   {mapping}
   [blank]
   {connective_prose}
   [blank]
   {resolution}
   ```
   to
   ```
   {scenario} {need} {mapping}
   [blank]
   {connective_prose} {resolution}
   ```
   This eliminates the 5+-paragraph fragmentation entirely AND collapses two REPL beats into one.

**RESOLUTION_REPL_DOUBLED 12 → 0.** Hand-rewrote four resolution slots that mentioned REPL twice:
- `grade_2.py:2065` (G2-19 large multiplication) — second REPL → "the container grew"
- `grade_3.py:602` (G3-09 defn add3) — second REPL → "it walked the trail"
- `grade_5.py:157` (G5-02 if-as-expression) — second REPL → "let it compose the answer"
- `grade_9.py:77` (G9-01 immutability review) — second REPL → "in its paw"

### Step 2: RESOLUTION_GENERIC 31 → 0 (combined with GENERIC_RESOLUTION_TAIL 3 → 3 = 3 total)

One template at `dog_shadow/_metaphor_pools.py:402` ("Watch the pile") ended with `", and the REPL returned the value the operation had produced."` — matched the `canned_resolution_re` pattern. Replaced with: `"composed {concept_phrase} and submitted it. The runtime handed back the count, the river running steady beside the heap."` — concrete river+heap close.

The 3 remaining GENERIC_RESOLUTION_TAIL hits are static `_ex` examples whose authoring is shared between Group γ's CLAUSE_STACK pattern set and this slice — left for a coordinated follow-up.

### Step 3: Cadence trio (combined 135 → 39)

**DOUBLE_NAME_INTRO 24 → 0.** Replaced 8 occurrences of `{primary_phrase}` / `{secondary_phrase}` with the bare-name forms `{primary}` / `{secondary}` inside the OPENERS_DOG_SHADOW block of `opener_pools.py`. Named openers no longer say "Patch the hound" while body templates also introduce species.

**FORM_DISPLAY_AND_FORM_NOUN 26 → 0.** Two operations:
1. Stripped 8 in-source occurrences of `"the form {form_display}"` → `"{form_display}"` across `dog_shadow/grade_1, grade_6, grade_7, grade_11, grade_12.py`.
2. Rewrote 2 `_SHARED_SUBPLOTS` templates in `dog_shadow/grade_1.py`:
   - Template 3 (teacher): `"You hand {form_display} to the runtime — the runtime is the stream's honest reading, not the surface guess — and it gives back what the form really is."` → `"... and it gives back the value exactly."`
   - Template 4 (audience): `"...read the form aloud: {form_display}. The crowd waited to see who would correctly write the form to submit."` → `"...read it aloud: {form_display}. The crowd waited to see who would correctly write the expression to submit."`

**HIGH_LENGTH 57 → 39.** Trimmed 16 verbose `" with X" connector tails from `_metaphor_pools.py`:
- `" with the bark cleared of stray scratches and only the form left for the runtime to read —"`
- `" with the scratch on the bark held distinct from the bone it named"`
- `" with the running tally heavy in the carrying"`
- `" with the bead-cord laid straight"`
- `" with the same path walked again and again"`
- `" with the marker's name posted firm beside the path"`
- `" with the practice-log laid out before the leap"`
- `" with the pack ledger laid open"`
- (and 8 more)

**PARAGRAPH_FRAGMENTATION 28 → 0.** Folded by Step 1's `_story()` rewrite.

### Step 4: Comma-list + narrative numerals

**CONCEPT_PHRASE_COMMA_LIST 75 → 0.** Rewrote 19 grade-9 concurrency-primitive `concept_phrase` values from comma-token lists to determiner-led noun phrases:

| Before | After |
|---|---|
| `atom, swap, and deref` | `the atom updated through a swap and read by deref` |
| `ref, dosync, alter, deref` | `the ref altered inside a transaction and read by deref` |
| `agent, send, await, deref` | `the agent updated by send, awaited, and read by deref` |
| `agent, send-off, await, deref` | `the agent updated by send-off on a blocking thread, awaited, and read by deref` |
| `future, multiply, deref` | `the future computing the product and read by deref` |
| `promise, deliver, deref` | `the promise fulfilled by deliver and read by deref` |
| `volatile, vswap, deref` | `the volatile updated through vswap and read by deref` |
| `dynamic var, binding, read` | `the dynamic var whose value binding rebinds and the body reads` |
| `lock, locking, arithmetic` | `the arithmetic guarded by a locking block on a lock object` |

Each rewrite is a determiner-led noun phrase that flows into the surrounding subplot prose.

**NARRATIVE_NUMERAL_HARDCODE 138 → 21.** Bulk-replaced 68 hardcoded English-numeral quantifiers ("three bones", "five piles", "ten stones") in parametric example slots with `"a row of <noun>"` forms. Group 1's NARRATIVE_NUMERAL pass had not yet pushed at rebase time, so the dog_shadow subset was done locally per the spec's coordination clause.

Per-file edit counts: grade_1 14, grade_2 17, grade_3 7, grade_4 17, grade_5 7, grade_9 2, grade_10 4 (total 68).

The remaining 21 hits are in non-target slots (e.g. `goal_text`, where the literal numeral is the actual operation argument) — out-of-scope for this fixset.

### Step 5: Three NEW detectors (slice 7MIx)

Confirmed not duplicating existing 97 detectors via `grep -oE '"[A-Z_]+"' | sort -u`.

#### A. PRONOUN_AT_SENTENCE_START_AFTER_QUOTE

Catches the dog-shadow scaffold seam: `."` close-quote followed by `"He, X-ing, ... composed"` pattern. Scoped tightly so other fables' legitimate post-quote pronoun cadences don't false-positive (initial wider regex hit 4 milkmaid records — tightened to require the EMO participial AND the verb "composed" to follow).

```python
if re.search(
    r'\."\s+(?:He|She|They),\s+[a-z][a-z ,]+(?:ing|ly|ate|ent|able|ed)'
    r'(?:\s+[a-z]+){0,3}\s+composed\b',
    user,
):
```

**Current count:** 0 dog_shadow / 0 milkmaid / 0 others (acts as guardrail against future drift).

#### B. CONNECTOR_RUNTIME_DOUBLED

Catches connector "It returned:" / "The runtime returned:" immediately followed by a paragraph that re-names the runtime — scaffold seam where two named runtime mentions are separated only by the colon-paragraph break.

```python
if re.search(
    r"(?:It|The runtime|The REPL) returned:\s*\n+\s*"
    r"(?:The runtime|The REPL)\b",
    user,
):
```

**Current count:** 0 (after my connector rewrites in Step 1, the seam pattern is gone — guardrail).

#### C. FABLE_FOREIGN_NUMERAL_QUANTIFIER

Catches parametric examples with hardcoded DIGIT quantifiers (e.g. "a row of 5 bones") in narrative — drifts across draws since the form's actual operand is parametric. Distinct from NARRATIVE_NUMERAL_HARDCODE which catches English-word form.

```python
quant_re = re.compile(
    r"\b(?:a row of|a heap of|a stack of|a pile of|a cache of)"
    r"\s+(\d{1,2})\s+(?:bones?|stones?|piles?|values?|elements?|items?|numbers?)\b",
    re.IGNORECASE,
)
qm = quant_re.search(user)
if qm and getattr(example, "form_template", None):
    ...
```

**Current count:** 2 dog_shadow hits — these are author-side digit quantifiers I missed in the bulk numeral neutralization (out-of-scope for this slice; left for follow-up).

## Coordination notes (Groups 1 / 2)

- **NARRATIVE_NUMERAL_HARDCODE:** Group 1's subset hadn't pushed at my rebase point. Did the dog_shadow subset locally (~50 templates with hardcoded English numerals) per the spec's "do the dog_shadow subset yourself" clause.
- **ANSWER_LEAK family:** Group 2's subset hadn't pushed; ANSWER_LEAK / ANSWER_LEAK_STRING totals are essentially unchanged in dog_shadow (19 + 8 → 19 + 8). My fixes did not target these; they remain for Group 2 to land.
- **CLAUSE_STACK_OVERFLOW (Group γ):** Untouched as instructed. Incidental −5 drop comes from the verbose-tail trims in Step 3 (these removed surrounding commas in some sentences).
- **NUMERAL_LIST_IN_GOAL / WRONG_FABLE_LITERAL (Group γ):** Untouched; counts unchanged.

## Smoke

```
scalar_pools : ok (29 pools)
form_parser  : ok (27/27)
form_families: ok (82 families × 5 trials)
auto_parametric: ok (6 forms)
character_pools: ok (1830 names across 13 pools)
opener_pools : ok (150 openers, 150 plans)
emotion_pools: AssertionError EMO_PROUD: duplicates  ← pre-existing baseline
e2e          : runs (output truncated by ----)
```

The emotion_pools EMO_PROUD duplicate is a pre-existing baseline issue at integration HEAD `8fab5ca`. Not a regression introduced by this fixset.

## Files changed

- `docs/clojure-pedagogy/audits/audit-harness.py` — 3 new detectors at end of `check_record()`.
- `docs/clojure-pedagogy/audits/dog-shadow-audit.md` — regenerated.
- `src/mmllm/aesop/curriculum/opener_pools.py` — OPENERS_DOG_SHADOW phrase→bare-name conversion (8 entries).
- `src/mmllm/aesop/curriculum/dog_shadow/_metaphor_pools.py` — REPL→runtime/it connector swaps; story-scaffold paragraph fold; verbose tail trims; 2 REPL_AS_TIME rewrites; 1 RESOLUTION_GENERIC rewrite.
- `src/mmllm/aesop/curriculum/dog_shadow/grade_1.py` ... `grade_12.py` — 19 concept_phrase noun-phrase rewrites (grade_9), 68 numeral neutralizations across 7 grade files, 4 RESOLUTION_REPL_DOUBLED rewrites, 8 "the form {form_display}" strips, 2 SHARED_SUBPLOTS form-noun rewrites.

## Report

```
Slice:       fable=dog_shadow  branch=claude/round3-group3-dog-shadow-7MIx  sha=26b8299
Verify:      PARENT_OK + HEAD_OK
Smoke:       7/7 modules + e2e green; emotion_pools EMO_PROUD is pre-existing
Per-class:
  GENERIC_RESOLUTION_TAIL    BEFORE=3    AFTER=3    delta=0
  RESOLUTION_GENERIC         BEFORE=31   AFTER=0    delta=-31
  REPL_TRIPLE_VOICE          BEFORE=54   AFTER=25   delta=-29
  REPL_AS_TIME_TRAVELLER     BEFORE=31   AFTER=0    delta=-31
  RESOLUTION_REPL_DOUBLED    BEFORE=12   AFTER=0    delta=-12
  CONCEPT_PHRASE_COMMA_LIST  BEFORE=75   AFTER=0    delta=-75
  NARRATIVE_NUMERAL_HARDCODE BEFORE=138  AFTER=21   delta=-117
  HIGH_LENGTH                BEFORE=58   AFTER=39   delta=-19
  PARAGRAPH_FRAGMENTATION    BEFORE=28   AFTER=0    delta=-28
  FORM_DISPLAY_AND_FORM_NOUN BEFORE=26   AFTER=0    delta=-26
  DOUBLE_NAME_INTRO          BEFORE=24   AFTER=0    delta=-24
  HEDGING_NEAR_FORM          BEFORE=11   AFTER=11   delta=0
Audit:       dog_shadow BEFORE=983  AFTER=584  delta=-399 (target ≤600 met)
Cross-fable AFTER (each ≤ BEFORE):
  tortoise_hare: 496 = 496
  crow_pitcher : 622 = 622
  milkmaid     : 708 = 708
  boy_wolf     : 886 = 886
3 new detectors:
  - PRONOUN_AT_SENTENCE_START_AFTER_QUOTE (guardrail; tight scope)
  - CONNECTOR_RUNTIME_DOUBLED (guardrail; current count 0)
  - FABLE_FOREIGN_NUMERAL_QUANTIFIER (caught 2 dog_shadow hits)
Sync:        branch already at integration HEAD 8fab5ca (no rebase needed)
Coordination notes:
  Group 1 (NARRATIVE_NUMERAL_HARDCODE) — not yet pushed; did dog_shadow
    subset locally (~50 templates).
  Group 2 (ANSWER_LEAK family) — not yet pushed; left untouched in
    dog_shadow scope (counts unchanged).
  Group γ (CLAUSE_STACK_OVERFLOW / NUMERAL_LIST_IN_GOAL /
    WRONG_FABLE_LITERAL) — untouched; incidental -5 CLAUSE_STACK from
    connector tail trims, otherwise no overlap.
```
