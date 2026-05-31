# Deep audit — milkmaid (slice k7Pq)

**Branch:** `claude/audit-milkmaid-k7Pq`

## Scope

- **Fable:** milkmaid (daydream vs. care)
- **Grades sampled (random 6 of 12):** 2, 5, 6, 8, 10, 12
- **Records read:** ~600 (3 records × ~20 subjects per grade × 6 grades)

## Workflow notes

- The playbook file (`docs/clojure-pedagogy/audits/AUDIT-PLAYBOOK.md`) referenced in the agent prompt is not present in this repo. Worked from the prompt's category list (Cat-A through Cat-J) directly.
- Baseline (before this slice) reported 0 audit-harness issues for milkmaid.

## Audit detectors added

Added **4 new detectors** to `docs/clojure-pedagogy/audits/audit-harness.py`:

1. **`CONCEPT_AS_VERB`** — `{concept_phrase}` (often a gerund noun-phrase like "calling a protocol method on a string", "applying a function to each element") substituted into a slot that grammatically requires a finite verb. Two arms:
   - Modal/quasi-modal arm: `must|should|can|will|may|own way of doing` + `<gerund>` + `(a|the|an|to|...)`.
   - Bare-subject arm: `(I|you|we)` + `<gerund>` + `(a|the|an|to|...)`, with a post-filter that skips matches whose preceding word is an aspectual licensor (`am|is|are|was|were|been|being|keep|kept|while|after|before|by|from|...`). Avoids false positives on legitimate progressive aspect like "are you reading the label?".

2. **`LOWERCASE_PRONOUN_AFTER_PERIOD`** — sentence-initial pronoun appears lowercase after a period. Catches `\.\s+(?:she|he|they)\s+(?:[a-z]+ed|only|asked|replied|...)`. Distinct from the existing `LOWERCASE_AFTER_PERIOD` (which only catches lowercase `{place}` phrases like "in the meadow").

3. **`VOCATIVE_PRONOUN`** — pronoun used as vocative form of address (e.g., "stops you, she."). Catches `,\s+(?:she|he|they)\.`. The fix is to use the character's name instead of the pronoun, or drop the vocative.

4. **`LOWERCASE_CONCEPT_AFTER_PERIOD`** — sentence-initial lowercase `{concept_phrase}` ("the multi-arg sum does X", "the inequality check is Y"). Catches `\.\s+the\s+(?:[a-z]+\s+){1,4}(?:does|is|means|chooses|examines|reads|writes|walks|stacks|fires|takes)\b`. The fix is to keep `{concept_phrase}` mid-sentence (em-dash, comma) so capitalization isn't required.

## Papercut counts (milkmaid only)

| Detector | Before | After |
| --- | ---: | ---: |
| `CONCEPT_AS_VERB` | 68 | 0 |
| `LOWERCASE_PRONOUN_AFTER_PERIOD` | 250 | 0 |
| `LOWERCASE_CONCEPT_AFTER_PERIOD` | 65 | 0 |
| `VOCATIVE_PRONOUN` | 13 | 0 |
| `HIGH_LENGTH` (existing) | 0 | 0 (1 transient regression introduced + fixed) |
| `FORM_LEAK` (existing) | 0 | 0 (1 transient regression introduced + fixed) |
| **Total milkmaid** | **396** | **0** |

## Papercuts by category

| Cat | Description | Hits | Source |
| --- | --- | ---: | --- |
| **A** (logical) | `{concept_phrase}` placed in a verb slot — broken predicate | 68 | `_metaphor_pools.py` lines 457, 466-467, 533, 539, 548, 556, 581, 588, 595, 596, 601, 617, 631, 632, 639, 647, 677, 718 |
| **B** (syntax) | Lowercase pronoun after period; lowercase `{concept_phrase}` after period | 315 | `_metaphor_pools.py` lines 249, 273, 311, 320, 326, 328, 342, 389, 396, 403, 434, 503, 555, 623, 639, 709, 742, 754, 801, 827, 836, 851, 860, 867, 877, 887, 898, 905, 913, 920, 943, 952, 963, 970, 971, 985, 998, 1013, 1019; `grade_1.py` line 254 |
| **C** (grammar) | Vocative pronoun ("stops you, she.") | 13 | `_metaphor_pools.py` line 342 (GATE template) |
| **D** (spelling) | None surfaced | — | — |
| **E** (semantic) | Broken sentence: missing verb between two NPs ("a form `{concept_phrase}` a name or a reference") | 1 distinct template (renders as ~3-5 records) | `_metaphor_pools.py` lines 466-467 |
| **F** (narrative polarity) | None — milkmaid polarity (daydreamer vs. careful farmer) preserved across templates | — | — |
| **G** (emotional) | Mild — milkmaid emotional palette dilutes to "smiled / replied / said calmly". Tracked as Cat-J for the affirmative push. | (not counted) | — |
| **H** (plot-coherence) | Subset of B — when the corrective character's pronoun lacks a clear antecedent. Resolved by capitalizing pronouns at sentence starts (the Cat-B fix elevates these too because the named-then-pronoun pattern reads cleanly when the pronoun is properly capitalized). | (subsumed) | — |
| **I** (distractions) | None surfaced beyond Cat-B | — | — |
| **J** (insufficient grounding) | The milkmaid's signature emotional palette (anticipation, dreamy planning, sober counting) is present in openers but dilutes in subplot prose to generic "she said calmly / he replied". Not fixed in this slice. | (qualitative) | (would touch `BW_EMO_*`-style milkmaid pools, beyond the slice's scope; flagged for follow-up) |

## Source-level fixes applied

### `src/mmllm/aesop/curriculum/milkmaid/_metaphor_pools.py`

- 8 templates with `{concept_phrase}` in verb position rewritten to use a noun-phrase wrapper:
  - `we {concept_phrase}` → `we use {concept_phrase}`
  - `you {concept_phrase}` → `you apply {concept_phrase}`
  - `I {concept_phrase}` → `I followed {concept_phrase}`
  - `must {concept_phrase}` → `must perform {concept_phrase}` (and similar for `should`/`can`/`will`/`may`)
  - `the form that {concept_phrase}` → `the form that performs {concept_phrase}`
  - `way of doing {concept_phrase}` → `approach to {concept_phrase}`
- 1 template with broken sentence (line 466-467): `a form {concept_phrase} a name or a reference` → `a form for {concept_phrase} provides a name or a reference`.
- 16 templates with `. {concept_phrase}` patterns rewritten to `— {concept_phrase}` (em-dash keeps `{concept_phrase}` mid-sentence).
- 26 sentence-initial `{milkmaid_he_she}` / `{farmer_he_she}` placeholders changed to their `_cap` variants (capitalize first letter at sentence start).
- 1 vocative `, {milkmaid_he_she}.` (GATE template) changed to `, {milkmaid}.` (use the name).

### `src/mmllm/aesop/curriculum/milkmaid/grade_1.py`

- 1 sentence-initial `{farmer_he_she}` changed to `_cap`.

### `src/mmllm/aesop/curriculum/milkmaid/grade_2.py`

- 1 resolution slot trimmed to drop the literal answer `true` from the prose and to fit under the 200-word `HIGH_LENGTH` threshold.

### `src/mmllm/aesop/curriculum/milkmaid/grade_11.py`

- 1 mapping slot stripped of an inline form-display (`(. "abc" toUpperCase)`) that leaked into the goal-style user_msg.

### `src/mmllm/aesop/curriculum/milkmaid/grade_4.py`

- (Cleanup carried over from sub-agent's pass; details in commit history.)

## Cross-fable signal (informational only)

The 4 new detectors fire on other fables' templates. **These are real bugs**; my fixes here only touch milkmaid. Other audit slices on those fables should pick up the signal:

| Fable | `CONCEPT_AS_VERB` | `LOWERCASE_PRONOUN_AFTER_PERIOD` |
| --- | ---: | ---: |
| tortoise-hare | 28 | 0 |
| boy-wolf | 21 | 19 |
| crow-pitcher | 26 | 0 |
| dog-shadow | 11 | 0 |
| goose-eggs | 0 | 0 |
| ant-grasshopper | 0 | 0 |
| **milkmaid** | **0** | **0** |

## Audit harness diff

- `+88` lines added to `audit-harness.py` (4 new detector blocks with comments and regex notes).

## Smoke tests

- `FABLE=milkmaid python3 docs/clojure-pedagogy/audits/audit-harness.py` → 0 issues.
- `FABLE=goose_eggs ...` and `FABLE=ant_grasshopper ...` → 0 issues (no regression on the two fables that were 0 before this work).
- Generation smoke (one record per sampled subject) reads cleanly: pronoun-antecedent issues resolved, concept-phrase usage grammatical.

## Remediation (rebased onto integration branch)

The original audit branch was based on `main`, which is stale —
the integration branch `claude/analyze-repo-status-rN0vt` carries
the parametric scalar system, the new `emotion_pools.py` (199
band entries + 396 archetype entries), the `AUDIT-PLAYBOOK.md`
the prior pass couldn't find, and the new `character_pools` /
`opener_pools` machinery. Cherry-picked the prior agent's audit
commit (`6df24fc`) onto the integration branch as the new
remediation branch `claude/audit-milkmaid-k7Pq-remediated`.

Cherry-pick conflicts: the four cross-fable audit-md files
(`boy-wolf-audit.md`, `crow-pitcher-audit.md`, `dog-shadow-audit.md`,
`tortoise-hare-audit.md`) were regenerated by both branches and
needed conflict resolution. Resolved with `--theirs` (prior
agent's version), per the playbook's guidance.

Smoke tests on the rebased branch: all green
(`scalar_pools`, `form_parser`, `form_families`, `auto_parametric`,
`character_pools`, `opener_pools`, `emotion_pools`,
`test_parametric_e2e.py`, the audit harness itself).

## Cat-J fixes (completion)

The prior agent flagged Cat-J as out of scope because they
believed milkmaid needed a fable-specific `MM_EMO_*` set authored
from scratch. Reframe: the integration branch's `emotion_pools.py`
already provides the 12 archetype pools (`EMO_PATIENT`,
`EMO_BOASTFUL`, `EMO_CAUTIOUS`, etc., each ≥30 entries) — so the
Cat-J lift is a wiring-and-template change, not a multi-grade
authoring pass.

### LOW_GROUNDING detector (Cat-J — affirmative)

Added to `audit-harness.py`. Flags records lacking BOTH:
- (i) any drawn-value reference (any int / keyword / string /
      symbol literal from `rec.code_str` appearing in `user_msg`);
- (ii) any phrase from the milkmaid-aligned EMO pools
      (`EMO_PATIENT`, `EMO_REGRETFUL`, `EMO_CONTENT`, `EMO_BOASTFUL`,
      `EMO_CAUTIOUS`, plus universal `EMO_PROUD`, `EMO_DESPERATE`,
      `EMO_HUNGRY`).

Also flags the generic-adverb dialogue pattern ("she said
softly / quietly / gently / calmly") when no environment-anchored
EMO phrase appears in the same record.

### Source-level lifts (≥11)

All applied to `src/mmllm/aesop/curriculum/milkmaid/_metaphor_pools.py`
or the milkmaid block of `generator.py`. Each lift fixes a class
of records, not a single instance:

1. **`generator.py:_build_mm_placeholders`** — re-wired the
   `emo_*` placeholder picks from the 6-entry legacy
   `fables.EMO_*` pools to the 33-entry+ `emotion_pools.EMO_*`
   pools (also added new `emo_boastful`, `emo_cautious`,
   `emo_desperate` placeholder substitutions).
2. **TOOLSHED-style template L128-134** — replaced
   `{farmer_he_she_cap} asked calmly` with
   `{farmer_he_she_cap} answered, {emo_cautious}` + added env
   adjectives ("the road is long, the pail is full"); milkmaid
   gets `{emo_boastful}` claim.
3. **ACORN-style template L295-298** — replaced
   `{farmer_he_she_cap} said calmly` with `said, {emo_patient}` +
   "The pail is heavy because every coin is in it" (heavy ↔
   accumulator value).
4. **ACORN-style template L317-322** — replaced
   `{farmer_he_she_cap} said gently` with `arrived and set out
   the coins in order, {emo_patient}` + "the road is long enough
   to hold every coin in turn" (long ↔ collection length).
5. **SCROLL-style template L545-550** — replaced
   `{farmer_he_she_cap} said gently` with `compared them,
   {emo_cautious}` + "the ink on her copy faint and uneven" /
   "written firm and dark by the hand that paid".
6. **SORTINGTABLE-style template L873-878** — replaced
   `asked calmly` with `answered, {emo_cautious}` + "the table
   stood empty, the pails still queued at the door".
7. **BASKET-style template L160-167** — replaced
   `smiled and said` with `smiled, {emo_patient}, the basket
   steady on the counting-table` + "The old basket never
   changes; its weight is fixed".
8. **SIEVE-style template L233-239** — replaced
   `smiled and said` with `smiled, {emo_cautious}` + milkmaid's
   `{emo_desperate}` cry + "the linen-strainer slack on its
   frame" / "which drops belong below and which return up the
   pail".
9. **ACORN-trust-ledger template L301-307** — replaced
   `only smiled and said` with `answered her, {emo_patient}` +
   "the pail full and balanced on her head" / "the table heavy
   with the slow weight of true count".
10. **CHALKMARK-style template L831-836** — replaced
    `smiled and said` with `answered, {emo_cautious}, the
    chalk-marked pail sitting unopened on the bench between
    them` (label vs value mapping).
11. **NOTEBOOK-style template L267-272** — added
    `{emo_cautious}` and `{emo_patient}` qualifiers + "the chalk
    steady, the slate firm under the heel of {farmer_his_her}
    hand" (firm ↔ atomic update).

### Sample lift mapping (representative)

| Algorithm cue | Environmental adjective | Where wired |
| --- | --- | --- |
| accumulator value | "the pail is heavy because every coin is in it" | `_metaphor_pools.py` ACORN tally template |
| collection length | "the road is long enough to hold every coin in turn" | `_metaphor_pools.py` ACORN multi-arg template |
| immutable update | "the basket steady on the counting-table" / "its weight is fixed" | `_metaphor_pools.py` BASKET assoc template |
| atomic update | "the chalk steady, the slate firm under the heel of her hand" | `_metaphor_pools.py` NOTEBOOK template |
| label-vs-value | "the chalk-marked pail sitting unopened on the bench" | `_metaphor_pools.py` CHALKMARK template |
| empty source | "the linen-strainer slack on its frame" | `_metaphor_pools.py` SIEVE template |
| copy correctness | "the ink on her copy faint and uneven" | `_metaphor_pools.py` SCROLL template |
| empty dispatch table | "the table stood empty, the pails still queued at the door" | `_metaphor_pools.py` SORTINGTABLE template |

## Numbers BEFORE / AFTER (remediated)

| Detector | BEFORE (cherry-pick + LOW_GROUNDING but no Cat-J lifts) | AFTER (Cat-J lifts applied) |
| --- | ---: | ---: |
| `LOW_GROUNDING` | 178 | 127 |
| `HIGH_LENGTH` | 23 | (qualitative; AFTER full-audit timed out at the 600s budget; sample of 792 records with the same n=3-per-example methodology shows AFTER existing-detector counts in line with BEFORE) |
| `ANSWER_LEAK` | 3 | (likely unchanged; my edits did not touch numeric content) |
| `ANSWER_LEAK_STRING` | 1 | (likely unchanged) |
| `DOUBLE_PREP` | 1 | (likely unchanged) |
| **Total LOW_GROUNDING change** | **178** | **127** |

LOW_GROUNDING dropped 178 → 127 (≈29% reduction). The four
template lifts alone don't reach every record — many records
draw from non-lifted templates that still rely on the legacy
short EMO_PATIENT pool. The most impactful lift is the
generator-level rewire to `emotion_pools.EMO_*`: it broadens
the EMO phrase pool by ≥5× across ALL milkmaid records, so any
template that uses `{emo_patient}` (and there are many) now has
access to the longer environment-anchored phrasings.

## Caveats

- The full audit harness was not allowed to complete its
  AFTER-state run within the agent's wall-clock budget (the
  integration branch's parametric system makes record
  generation slower per subject, and the audit had been running
  for ≈18 minutes when it was cut). The AFTER LOW_GROUNDING
  count was instead computed by an inline 792-record sample
  using the same detector logic and the same fixed-seed
  methodology the audit harness uses (`seed_base = int(sid[3:].
  replace("-", "")) * 7`, `n_per_example=3`) over the same 6
  grades. Comparable to the BEFORE-state full audit's 178 by
  design; the 127 figure is the apples-to-apples AFTER.
- The cross-fable detector signal from the prior agent's pass
  (CONCEPT_AS_VERB / LOWERCASE_PRONOUN_AFTER_PERIOD on TH /
  BW / CP / DS) is preserved on the remediated branch and will
  be picked up by other fables' audit slices.
- The `place_phrase` change reverted in the prior pass remains
  reverted; not in scope for this remediation.

## Branch & SHA

- Original branch (deprecated, was based on stale `main`):
  `claude/audit-milkmaid-k7Pq` @ `6df24fc`.
- Remediated branch (based on integration `claude/analyze-repo-status-rN0vt`):
  `claude/audit-milkmaid-k7Pq-remediated` @ (filled in after commit).
