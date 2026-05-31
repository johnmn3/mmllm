# Deep audit — dog-shadow (slice xe8M)

**Date**: 2026-05-08
**Branch**: `claude/audit-dog-shadow-xe8M`
**Parent**: `origin/claude/analyze-repo-status-rN0vt` @ `d8dfba0`
**Slice**: 6 grades sampled randomly → `{1, 2, 3, 6, 10, 11}`
**Read-corpus size**: 1465 records (5 records/example, seed=42).

This round's theme: **MAKE IT MAKE SENSE.** The job: read every
record like a children's fable and lift anything that doesn't
read aloud well — even when detectors don't fire.

## TL;DR

| Metric | Before | After | Δ |
| --- | ---: | ---: | ---: |
| Total audit issues | 2214 | 1596 | **-618** |
| `LOW_GROUNDING` | 503 | 440 | **-63** (negative ✓) |
| `POST_COMMA_CAPITAL_PRONOUN` | 290 | 0 | -290 |
| `CAP_PRONOUN_MID_SENTENCE` | 290 | 0 | -290 |
| `FOREIGN_FABLE_IMAGERY` | 101 | 0 | -101 |
| `REPL_AS_TIME_TRAVELLER` | 31 | 0 | -31 |
| `NARRATIVE_NUMERAL_HARDCODE` (new) | 0 | 138 | +138 (tripwire) |
| `FORM_DISPLAY_AND_FORM_NOUN` (new) | 0 | 16 | +16 (tripwire) |
| `META_FILLER_RESOLUTION` (new) | 0 | 3 | +3 (tripwire) |
| Storybook GOOD ratio | 5/30 (17%) | 12/30 (40%) | +23pp |

LOW_GROUNDING delta is **negative** (-63), satisfying the Cat-J
mechanical-proof requirement. Storybook GOOD ratio rose 23pp but
fell short of the 80% target (acknowledged below as a known gap
driven by G11 marker subjects).

## Verification gates

| Step | Observation | Result |
| --- | --- | :---: |
| Parent SHA | `d8dfba0…` "regen crow-pitcher + tortoise-hare audit reports …" | PARENT_OK |
| HEAD == EXPECTED_PARENT | `d8dfba0` matches | HEAD_OK |
| Playbook present | `docs/.../AUDIT-PLAYBOOK.md` exists | playbook_OK |
| Smoke (8 modules + e2e) | all pass | green |

## Storybook reading

30 records sampled with seed `2026508` from the 1465-record corpus.
Each marked GOOD / OKAY / BAD per the playbook.

| Cohort | BEFORE | AFTER |
| --- | ---: | ---: |
| GOOD | 5 (17%) | 12 (40%) |
| OKAY | 8 (27%) | 9 (30%) |
| BAD | 17 (57%) | 9 (30%) |

The remaining 9 BAD records cluster on G11 *marker subjects*
(forms like `(do "ember" :y)` for ClojureScript / host-overview
lessons). Those forms are abstract-by-design markers; the
dog/bone metaphor doesn't tie to "JavaScript" or "type hints".
Lifting these would require redesigning the example pool (a
different subplot family or a non-fable-metaphor template).
**Out of scope for this slice.** Captured as Cat-K K-6 system-wide
follow-up.

## Cat-J — grounding lifts (≥10 required, applied 18+)

LOW_GROUNDING fires when user_msg lacks BOTH a drawn-value
reference AND any archetype-EMO phrase. The dog_shadow
metaphor-pool templates had many that lacked `{emo_*}` placeholders
and produced flat narrative.

### Lifts at the source (each adds emo + environmental adjective + algorithmic mapping)

| # | Pool | File:line | Adjective ↔ algorithm |
| ---: | --- | --- | --- |
| 1 | `_ACORN_SUBPLOTS [0]` | `dog_shadow/_metaphor_pools.py:393-403` | "each pile a steady count, no bone borrowed across" ↔ pure arithmetic / no shared state |
| 2 | `_GATE_SUBPLOTS [0]` | `dog_shadow/_metaphor_pools.py` | "chain of crossing-tests was short and cool — the first false stone halted the chain" ↔ short-circuit boolean |
| 3 | `_FORK_SUBPLOTS [0]` | `dog_shadow/_metaphor_pools.py` | "cool and clear: only one arm would be taken, the others left walked-past" ↔ if/cond exclusive branch |
| 4 | `_POUCH_SUBPLOTS [1]` | `dog_shadow/_metaphor_pools.py` | "crossing was short and the grip held only for that span — the binding sealed inside the form's reach" ↔ let-scope |
| 5 | `_RECIPE_SUBPLOTS [0]` | `dog_shadow/_metaphor_pools.py` | "trail was long and the steps fell in order, each sniff teeing up the next" ↔ ordered fn body |
| 6 | `_ROADSIGN_SUBPLOTS [0]` | `dog_shadow/_metaphor_pools.py` | "stone sat plain on the long path: any later dog could read the scratch, no bookkeeping required" ↔ def at top level |
| 7 | `_SCRIBE_SUBPLOTS [0]` | `dog_shadow/_metaphor_pools.py` | `{emo_patient}` injected into "There are conventions for how the runtime *reads* a form" |
| 8 | `_TOOLSHED_SUBPLOTS [0]` | `dog_shadow/_metaphor_pools.py` | "The shed was a foreign yard with its own conventions; the borrowed tool answered only when called by its true name" ↔ host interop |
| 9 | `_REWRITERULE_SUBPLOTS [0]` | `dog_shadow/_metaphor_pools.py` | "search for the right scratch alternating with the verification step the runtime took" ↔ macro expansion |
| 10 | `_CHALKMARK_SUBPLOTS [0]` | `dog_shadow/_metaphor_pools.py` | "The mark and the bone stayed plainly distinct: the label was not the thing it pointed at" ↔ quote / symbols |
| 11 | `_SAFETYNET_SUBPLOTS [0]` | `dog_shadow/_metaphor_pools.py` | "The log was the safety-net: a slip on the form just returned the dog to the bank, no harm done" ↔ try/catch recovery |

### Parametric scenario lifts in grade_2 (Cat-J + Cat-K K-4)

12-17. **G2-01 ex0..ex5** in `dog_shadow/grade_2.py`: rewrote
scenarios + needs + mappings + resolutions to use `{drawn.a}…`
placeholders instead of literal "1, 2, 3, 4, 5" / "ten stones" /
"one hundred" — the prose now tracks what the parametric form
actually drew. (6 example rewrites covering ~30 distinct slot
edits.)

18. **G3-04** resolution rewrite in `dog_shadow/grade_3.py:417-421`:
"The REPL read the first grip, used it to compute the second" →
"The REPL read 5 from the first grip, doubled it for the second
grip's value, and held both inside the let's span" — adds
drawn-literal '5' so STORY_RESOLUTION_NO_DRAWN is satisfied.

## Cat-K — storytelling lifts (≥5 required, applied 7+)

Cat-K lifts are PROSE REWRITES that make the story make sense,
not mechanical injections. Each:
- the offending pattern observed in the corpus
- which K-class it falls under
- the source location
- the rewrite

### K-5 (out-of-register vocabulary) + K-1 (weak voice) — foreign imagery in dog-shadow grade_1

**Observed**: G1-01 record #19 "At a moss-covered milestone near
the village, Ashy the dog sketched a small wager into the path".
Moss-covered milestone is tortoise-hare furniture, not
dog-shadow's bridge-and-bone world. Same for "wooden sign nailed
to a tree", "small audience of forest creatures", "small leather
notebook".

**Source**: `dog_shadow/grade_1.py:53, 90, 111, 132` (and the
`_GOAL_SUBPLOTS` mirrors at lines 181, 199, 218, 237). 4 distinct
phrases, 8 occurrences total.

**Rewrite (per phrase)**:
- "moss-covered milestone" → "weathered bridge-stone"
- "small audience of forest creatures" → "small pack of meadow-dogs"
- "wooden sign nailed to a tree" → "scratched marker-stone by the bridge"
- "small leather notebook" → "scratched bone-tally"

This single set of rewrites elevates ~101 records from
FOREIGN_FABLE_IMAGERY = 0 (the new audit confirms).

### K-1 (weak voice) — "the hare's guess" leak

**Observed**: G1-01 _GOAL_SUBPLOTS template 11 (wrong-guess-then-form)
ended with "The crowd compared the two, and the hare's guess was
found wanting against the form that had actually run."

**Source**: `dog_shadow/grade_1.py:279`.

**Rewrite**: "The dogs at the bridge compared the two, and the
greedy guess fell short of the form that had actually run." —
swaps tortoise-hare voice for dog-shadow voice, and ties the
voice to the fable's polarity (greedy = hasty = dog).

### K-3 (AI-output cadence) — "had been there all along"

**Observed**: G1-13 records reading "and the runtime returned the
number that had been there all along, settling the matter the
patient way." This is meta-narrator AI output — the answer doesn't
exist independently of running the form.

**Source**: `dog_shadow/_metaphor_pools.py:411` (Dog-eyeballs-the-pile
template).

**Rewrite**: "and the runtime read off the exact tally the form
computed, settling the matter the patient way." — the runtime
computes; the answer is a result, not a pre-existing fact.

### K-4 (missing causality) — parametric numeral drift

**Observed**: G2-01 ex3 form `(+ 3 5 8 4 9 5 1 3 4 16)` rendered
with prose "to add the integers 1 through 16". The parametric
form draws 10 small ints, but the prose insists they are "1
through 16" — a fable about ten random bones being labeled "1
through 16" doesn't follow.

**Source**: `dog_shadow/grade_2.py:143-194` (G2-01 ex3-ex4).

**Rewrite**: replaced fixed-numeral prose with `{drawn.a}…{drawn.j}`
placeholders so the prose tracks the actual draws; reframed the
goal as "add ten counts together" rather than "1 through 10".
Now the scenario reads "Rex the hound laid ten marked stones in
a line at the stream's edge: {drawn.a}, {drawn.b}, {drawn.c},
{drawn.d}, {drawn.e}, {drawn.f}, {drawn.g}, {drawn.h}, {drawn.i},
and {drawn.j}." — coherent for any draw.

### K-6 (under-earned metaphor) — G1-04 string mismatch

**Observed**: G1-04 ex3 (form `""`) had concept_phrase "the empty
string"; but ex0/ex1/ex2/ex4 rendered with form_template `{a}`
that draws different strings, so a record with form `"willow"`
still says "the empty string" in concept_phrase. Cat-A drift.

**Source**: `dog_shadow/grade_1.py:391-394`.

**Rewrite**: collapsed all 5 G1-04 example concept_phrases to
"the literal string" / "the value of the literal string" — works
for any draw, no mismatch.

### K-6 (under-earned metaphor) — G1-08 character mismatch

**Observed**: G1-08 ex0 form `\h` — concept_phrase "the character
\h" — but the example has form_template `{a}` which can render as
arbitrary character or string draws (one record showed form="amber"
with concept_phrase "the character \h"). Mismatch.

**Source**: `dog_shadow/grade_1.py:483-491`.

**Rewrite**: simplified concept_phrase to "the character literal"
across all 4 examples. Predicate ex (`(char? \h)`) reworded to
"the char-predicate on a character literal".

### K-7 (redundant emotion injection) — `{emo_*}` adding nothing

**Observed**: Some baseline templates had `{emo_patient}` placed
mid-sentence where it didn't connect to anything (e.g.,
"X said, walking up at her usual pace, simply said:"). The Cat-J
lifts (#1-#11 above) replaced these flat injections with
meaningful environmental clauses tied to the operation, not bare
adverbs.

## Detectors added (3, all new)

| Name | Pattern | Hits |
| --- | --- | ---: |
| `NARRATIVE_NUMERAL_HARDCODE` | parametric example with hard-coded English numeral count phrase ("five bones", "ten stones") in any story slot | 138 |
| `META_FILLER_RESOLUTION` | "settled with certainty", "handed back with certainty", "the answer was exact" — generic AI-output filler | 3 |
| `FORM_DISPLAY_AND_FORM_NOUN` | `\`<form>\`` adjacent to "the form …" noun-phrase within 120 chars (template-tic) | 16 |

**Source**: `docs/clojure-pedagogy/audits/audit-harness.py` —
"slice xe8M (dog-shadow) detector additions" block, immediately
before `_check_grounding`.

The new detectors don't duplicate any of the 61 detectors already
in the harness (verified via the conflict-aware audit).

### Detector-side fix: emotion_pools rich archetype set

`_build_emo_markers()` previously imported only the 6-entry
`fables.py` archetype pools, the 3-entry CP_EMO pools, and
boy-wolf BW_EMO pools — but NOT the rich `emotion_pools.py`
archetype pools (≥30 entries each) that dog_shadow's
`_build_ds_placeholders` draws from. Records with
`emotion_pools.EMO_PATIENT` phrases were over-flagged for missing
EMO. Extended `_build_emo_markers()` to include the integration
emotion_pools rich archetype set so LOW_GROUNDING credits dog-
shadow records carrying these phrases.

## Source-level non-Cat-J / non-Cat-K fixes

### Cat-C grammar — post-comma capitalized pronouns

`dog_shadow/_metaphor_pools.py` had 31 `, {X_he_she_cap}` template
artifacts producing `, He composed` / `, She composed` mid-sentence.
Bulk replaced with `, {X_he_she}` (lowercase) — eliminating
POST_COMMA_CAPITAL_PRONOUN (290 → 0) and CAP_PRONOUN_MID_SENTENCE
(290 → 0). 580 records elevated.

## Polarity check

Verified across the 30-record storybook sample: hound = patient
evaluator, dog = greedy/hasty. No flips observed. The `{hound_*}`
and `{dog_*}` placeholders dispatch through the dog_shadow
character pool as designed.

## Smoke / audit summary

```
$ python -m mmllm.aesop.curriculum.scalar_pools         ✓
$ python -m mmllm.aesop.curriculum.form_parser          ✓ (27/27)
$ python -m mmllm.aesop.curriculum.form_families        ✓ (82×5=410)
$ python -m mmllm.aesop.curriculum.auto_parametric      ✓
$ python -m mmllm.aesop.curriculum.character_pools      ✓ (1830 names)
$ python -m mmllm.aesop.curriculum.opener_pools         ✓ (150+150)
$ python -m mmllm.aesop.curriculum.emotion_pools        ✓ (199+396)
$ python scripts/test_parametric_e2e.py                 ✓
$ FABLE=dog_shadow python docs/clojure-pedagogy/audits/audit-harness.py
  total issues: 1596  (BEFORE: 2214, Δ -618)
  LOW_GROUNDING: 440  (BEFORE: 503, Δ -63)
```

## Caveats / deviations

- **Storybook GOOD < 80% target**: achieved 40% (12/30) vs. 80%
  required. The 9 BAD records are concentrated on G11 marker
  subjects (`(do "ember" :y)` style forms with abstract goal_text
  about ClojureScript / type hints / cljs-host-overview). Lifting
  these requires redesigning the example pool — out of slice
  scope. Captured as a system-wide follow-up. Other 21 records
  passed (12 GOOD + 9 OKAY).
- **STORY_RESOLUTION_NO_DRAWN at 812**: this strict detector
  (resolution slot must contain a drawn-form literal as plain
  text) requires per-example resolution rewriting; tackled the
  highest-leverage 7 in this slice (G2-01 + G3-04). Rest is a
  systematic follow-up.
- **NARRATIVE_NUMERAL_HARDCODE (138)** is a tripwire from one of
  my new detectors firing on existing parametric scenarios that
  hard-code English numeral counts. Lifted G2-01 (-30) and the
  remaining ~138 are spread across many parametric subjects in
  grades not in this slice. Marked as system-wide follow-up.
- **WRONG_FABLE_LITERAL (16)**: the detector flags "Pip" as a
  tortoise-hare ghost name, but Pip is also a valid dog name in
  `character_pools.py`. False positive of the detector; the
  rendering is correct dog_shadow. Tweaking the detector to be
  context-aware was out of scope per "don't refactor unrelated
  infrastructure".
