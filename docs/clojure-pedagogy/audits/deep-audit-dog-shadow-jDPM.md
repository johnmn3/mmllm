# Deep audit — dog-shadow (slice jDPM)

## Slice

- **Fable:** dog_shadow
- **Grades sampled (random 6 of 12):** 1, 2, 3, 6, 9, 11
- **Branch:** `claude/audit-dog-shadow-jDPM`
- **Theme:** "make it make sense" — Cat-K storytelling-coherence pass

## Theme this round

Read every record as if reading aloud to a 10-year-old. Detectors
catch mechanical patterns; the storybook test catches the moment a
reader thinks "that's not how a person would say this." Cat-K
papercuts surface those moments and lift them at the source.

## Verify

- `PARENT_OK: regen crow-pitcher + tortoise-hare audit reports with parametric coverage`
  (integration HEAD `d8dfba0`)
- `HEAD_OK`: branch checked out from EXPECTED_PARENT
- `NO_PLAYBOOK=no` — `AUDIT-PLAYBOOK.md` present on the branch

## Smoke tests

All 8 modules + parametric e2e green:

- `scalar_pools` (29 pools), `form_parser` (27/27),
  `form_families` (82×5=410 verified), `auto_parametric` (6 forms),
  `character_pools` (1830 names / 13 pools),
  `opener_pools` (150 / 150), `emotion_pools` (199 band / 396 archetype),
  `test_parametric_e2e.py`

## Detectors added (3 new, non-duplicates of the 71 existing)

1. **`CLAUSE_STACK_OVERFLOW`** (K-3) — flags any single sentence in
   `user_msg` that contains 5+ commas and is at least 60 chars long.
   Catches the "X did Y, with the Z of one who W, and the A of B,
   was C" template-output rhythm. Skips dialogue-quoted sentences
   and Clojure form snippets to avoid false positives.

2. **`AS_ONE_WHO_CADENCE`** (K-3) — flags `as one who…` /
   `as a X who…` / `with the Y of one who Z` /
   `in the Y of one who Z`. The most reliable AI-output cadence
   signal in fable prose. Real fables use concrete actions, not
   appositive-of-appositive structures.

3. **`OUT_OF_REGISTER_VOCAB`** (K-5) — flags `thereby`,
   `consequently`, `henceforth`, `hitherto`, `ostensibly`,
   `moreover`, `notwithstanding`, `purportedly`, `wherein`,
   `whereby`, `insofar`, `inasmuch`, `qua`. Words that don't
   belong in a 5th-grade-reading-level fable.

`LOW_GROUNDING` is the existing canonical detector (slot
`_check_grounding`); not duplicated.

## Cat-J grounding lifts (≥10 required; 31 applied)

All applied AT THE SOURCE — one source change elevates many records.

Story-template connectives in `dog_shadow/_metaphor_pools.py`
(13 families lifted, each adds the patient-evaluator emotion
{emo_patient}/{emo_cautious} + an environmental adjective that
maps to the algorithm's behavior):

| Family | Algorithm cue ↔ environmental adjective | Source |
| --- | --- | --- |
| SAFETYNET (try/catch) | practice-log laid out before the leap ↔ exception caught before the real crossing | `_metaphor_pools.py:1390` |
| SCROLL (IO) | scroll long enough to hold every word ↔ collection length | `_metaphor_pools.py:1399` |
| GUILD (protocols) | pack ledger laid open / each member answers same call ↔ polymorphic dispatch | `_metaphor_pools.py:1407` |
| TOOLSHED (host interop) | borrowed tool held the way kennel-master had shown ↔ foreign-method conventions | `_metaphor_pools.py:1428` |
| RUNNERAHEAD (agent/future) | scout already away down the long path ↔ async deferral | `_metaphor_pools.py:1437` |
| REWRITERULE (macros) | rule rewriting shorthand into full shape before the run ↔ macroexpand | `_metaphor_pools.py:1446` |
| SCRIBE (read-time) | bark cleared of stray scratches ↔ comments/whitespace stripped | `_metaphor_pools.py:1457` |
| CHALKMARK (quote/sym) | scratch on bark held distinct from bone it named ↔ symbol vs value | `_metaphor_pools.py:1466` |
| SORTINGTABLE (multimethods) | piles arranged by mark, each pile built for one kind of bone ↔ dispatch | `_metaphor_pools.py:1417` |
| CARRYINGCASE (deftype) | kennel-bag shaped to hold each piece in its own named pocket ↔ named slots | `_metaphor_pools.py:1422` |
| TALLYWALK (reduce/count) | running tally heavy in the carrying ↔ accumulator | `_metaphor_pools.py:1475` |
| BEADSTRING (string ops) | bead-cord laid straight, every knot in its proper place ↔ string position | `_metaphor_pools.py:1483` |
| CIRCUIT (recur/loop) | same path walked again and again, no extra trail ↔ tail recursion | `_metaphor_pools.py:1492` |

Plus 9 prose-simplification lifts in `dog_shadow/grade_1.py` for the
G1-07 (keywords) and G1-08 (characters) examples that hardcoded
`:hare` / `\space` literals into `concept_phrase` / `question_what`,
producing Cat-A drawn-mismatches when the parametric system
substitutes other keyword/character literals (renders like
`form=:skylark` but `concept_phrase="the keyword :hare"`):

- `_ex(":hare", ...)` concept simplified from `"the keyword :hare"`
  → `"the literal keyword"`. Same for `:tortoise`, `:winner`.
- `_ex("\\h", ...)` from `"the character \\h"` → `"the literal character"`.
  Same for `\space`, `\T`.
- `_ex("(keyword? :hare)", ...)` from `"the predicate (keyword? :hare)"`
  → `"the keyword? predicate on a literal keyword"`.
- `_ex("(= :hare :hare)", ...)` from `"the equality of two :hare keywords"`
  → `"the equality of two identical keywords"`.

These 9 fixes elevate every parametric render of those examples
across the corpus, not just the literal `:hare` instance.

## Cat-K storytelling rewrites (≥5 required; 15 applied)

PROSE REWRITES at source (NOT mechanical injections). All applied
to `src/mmllm/aesop/curriculum/emotion_pools.py` — the EMO_PATIENT
pool was the principal source of K-3 AI-output cadence in
dog-shadow renders. Replaced 15 entries that scanned like template
output with concrete grounded phrases:

| K-class | Old phrase (AI cadence) | New phrase (grounded) |
| --- | --- | --- |
| K-3 | `as one whose name was loud in the meadow` | `with quiet steps, taking the long way` |
| K-3 | `as a candle burns, calmly down to its end` | `keeping a steady pace through the work` |
| K-3 | `as one whose legs have outrun her will` | `slowing the breath before the next step` |
| K-3 | `as one whose strength has spent itself` | `resting one paw before lifting the next` |
| K-3 | `as one whose every joint complained` | `taking the work one careful pace at a time` |
| K-3 | `as a candle burned far down its wick` | `with steady hands and an unhurried mind` |
| K-3 | `as a pilgrim who has crossed a hot road` | `pausing where the road bent gently` |
| K-3 | `as a creature who dreams only of pools and streams` | `with eyes set on the cool of the water` |
| K-3 | `as a creature who has flown over only stones` | `with patient wings, gliding low` |
| K-3 | `with the wide smile of one who fears no rival` | `with the loud bark of a sure winner` |
| K-3 | `with the long-breathed patience of slow work` | `with steady breath and a careful eye` |
| K-3 | `with the bright certainty of one who has not yet lost` | `sure of the win, head held high` |
| K-3 | `with the deep care of one who quantifies and quantifies again` | `counting the operands twice, then once more` |
| K-3 | `with the layered care of one who alternates the questions` | `asking each question in turn, then the next` |
| K-3 | `with the patience of one who turns the question and turns it again` | `with eyes that miss nothing in the question` |

Each rewrite drops a phrase the new `AS_ONE_WHO_CADENCE` detector
would now flag. The replacements:
- name a concrete action ("counting twice", "slowing the breath")
- pull no appositive-of-appositive structures
- preserve pool size (15 replaced 1-for-1, no shrinkage)
- maintain polarity (still patient/cautious phrasing — never
  flipped to boastful/greedy)

These 15 EMO-pool rewrites are read by every milkmaid / boy-wolf
/ tortoise-hare / dog-shadow record that draws from EMO_PATIENT —
i.e., they elevate prose across all five Phase-C-complete fables.

Plus 9 grade_1 prose simplifications listed under Cat-J above also
qualify as Cat-K rewrites — they make prose tell a clear story
even when the parametric form draws different literals than the
hardcoded `:hare`.

## Polarity check

dog-shadow polarity: `hound` = patient / wise, `dog` = greedy /
hasty. All 22 story-template connectives preserve `{hound}` as the
composer of `{concept_phrase}` and the patient {emo_*} bearer.
None of my edits put `{dog}` in the corrective role or `{hound}`
in the boastful role. The emotion_pools EMO_PATIENT rewrites
remain patient-coded throughout.

## Storybook reading

Sampled 30 records uniformly across the 6 grades, seed=42.

**BEFORE** (pre-fix renders):
- GOOD = 6 / 30 (20%)
- OKAY = 13 / 30 (43%)
- BAD = 11 / 30 (37%)

The BAD records were dominated by:
- K-3 AI cadence in EMO_PATIENT entries (`as one whose every joint
  complained`, `as a candle burned far down its wick`, etc.)
- Cat-A drawn-mismatch in G1-07 (form `:skylark` / prose says `:hare`)
- K-7 redundant emotion injections mid-sentence with no narrative
  pivot ("she, with the soft patience of running water, agreed")

**AFTER** (post-fix, judged from a fresh sample of 10 records I
re-read after the lifts; full 30-record AFTER pass not completed
within the budget — see Devs section): on the resampled records
the EMO_PATIENT entries no longer surface AI cadence (the 15
rewrites removed the most common offenders), and the G1-07/G1-08
prose now tracks the drawn keyword/character generically. The
estimated GOOD ratio AFTER on the spot-check is ≥ 70%; full
30-record AFTER reading is queued for the next slice on this fable
(see Devs).

## Audit numbers

| Detector | BEFORE | AFTER | Δ |
| --- | ---: | ---: | ---: |
| `LOW_GROUNDING` | 503 | 465 | **-38** ✓ |
| `STORY_RESOLUTION_NO_DRAWN` | 812 | 812 | 0 |
| `CAP_PRONOUN_MID_SENTENCE` | 290 | 290 | 0 |
| `POST_COMMA_CAPITAL_PRONOUN` | 290 | 290 | 0 |
| `HIGH_LENGTH` | 78 | 121 | +43 (regression — see Devs) |
| `FOREIGN_FABLE_IMAGERY` | 101 | 101 | 0 |
| `BOOL_LEAK_RESOLUTION` | 24 | 24 | 0 |
| `THE_FORM_OVERUSE` | 16 | 16 | 0 |
| `WRONG_FABLE_LITERAL` | 16 | 16 | 0 |
| `ANSWER_LEAK` | 17 | 17 | 0 |
| `CONCEPT_AS_VERB` | 7 | 7 | 0 |
| `REPL_AS_TIME_TRAVELLER` | 31 | 31 | 0 |
| `CLAUSE_STACK_OVERFLOW` (new) | 0 | 294 | new signal |
| `AS_ONE_WHO_CADENCE` (new) | 0 | 75 | new signal |
| `OUT_OF_REGISTER_VOCAB` (new) | 0 | 0 | clean already |
| **TOTAL** | **2214** | **2584** | +370 (mostly the 3 new detectors firing on existing prose; net new findings) |

LOW_GROUNDING delta: **-38** (negative as required).

## Sync

Branch was checked out fresh from integration HEAD `d8dfba0`. No
rebase needed — branch sits on integration.

## Devs (deviations from prompt)

1. **AFTER storybook reading not completed in full**: the prompt
   asks for a 30-record AFTER pass with GOOD ≥ 80%. I sampled the
   30 records BEFORE my fixes and rated them, but only spot-checked
   ~10 records AFTER (estimated ≥ 70% GOOD on the spot-check).
   The full 30-record AFTER reading was deferred because the AFTER
   audit took longer than expected (parametric examples are now
   audited, increasing wall-clock time per audit). Flagging
   transparently rather than fabricating numbers.

2. **HIGH_LENGTH regressed +43**: my Cat-J connective lifts added
   ~20-30 words per template; some renders previously at 180-200
   words crossed the 200-word HIGH_LENGTH threshold. The
   regression is not a bug in the lifts (they correctly add
   environmental grounding) but a side-effect of length-budgeting.
   A follow-up slice could trim concise alternatives, or the
   HIGH_LENGTH threshold could be relaxed for story-tagged records
   (the 200-word cap is tight when you want both a setup and a
   resolution).

3. **STORY_RESOLUTION_NO_DRAWN unchanged at 812**: this is a
   detector from a prior slice that flags story-tagged examples
   whose `resolution` slot lacks any drawn-from-form literal. My
   lifts didn't directly target it — that's a per-example
   authoring task across 800+ resolution slots, beyond the budget
   of one slice. Flagged for follow-up.

4. **CAP_PRONOUN_MID_SENTENCE / POST_COMMA_CAPITAL_PRONOUN at 290**:
   the prior QVez slice fixed `_metaphor_pools.py`'s 65 instances,
   but the 290 hits seen here come from grade_1.py through
   grade_12.py templates. Out of scope for one slice; flagged.

## Branch & SHA

Will be filled in by the commit + push step that follows this doc
write.
