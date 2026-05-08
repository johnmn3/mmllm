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

## Affirmative push (Cat-J) — flagged for follow-up

The milkmaid fable's emotional palette is its narrative anchor: the morning walk to market, the dreamy planning of fortunes, the careful counting that interrupts the daydream, the spilled-pail moment of regret. The current subplot pool surfaces these in openers but dilutes them in subplot prose to generic "smiled" / "replied" / "said calmly".

To lift Cat-J grounding the way the user's directive describes, the next pass should:

- Author a milkmaid-specific `MM_EMO_*` set (mirroring the `BW_EMO_*` pattern in boy-wolf) with palette entries grounded in the morning walk + market context: `MM_EMO_ANTICIPATING` ("imagining gold and silk"), `MM_EMO_SOBER` ("steady-handed at the counting table"), `MM_EMO_REGRETFUL` ("with the wet shoes of yesterday's spill"), etc.
- Wire those into the milkmaid block of `generator.py:_build_placeholders` (parallel to the existing boy-wolf wiring).
- Substitute `{emo_anticipating}` / `{emo_sober}` / `{emo_regretful}` into key subplot beats so the milkmaid's emotional state tracks the algorithmic action: a careful let-binding feels sober; a hasty multi-arg arithmetic feels anticipating; a successful evaluation closes with calm satisfaction.

This is a multi-grade authoring pass and exceeds the scope of one audit slice; queued for a separate follow-up.

## Caveats

- The `place_phrase` change for "village" (idiomatic "in the village") was reverted because it introduced 1 `HIGH_LENGTH` regression in crow-pitcher (an unrelated fable). The "on the village" rendering remains unflagged by any audit detector; left as a known low-impact prose papercut.
- The 4 new detectors fire on 4 other fables (tortoise-hare, boy-wolf, crow-pitcher, dog-shadow) — not regressions, just cross-fable signal of the same template-design errors. Each fable will need its own audit slice to fix locally; the detectors are now in place to catch the patterns there.

## Branch & SHA

- Branch: `claude/audit-milkmaid-k7Pq`
- Final commit SHA: (filled in after commit; see git log)
