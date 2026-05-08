# Deep audit — boy-wolf (slice XOE6, "make it make sense" theme)

**Branch:** `claude/audit-boy-wolf-XOE6`
**Fable:** boy-wolf
**Grades sampled (random 6 of 12):** 1, 2, 3, 8, 10, 11
**Read-corpus size:** 1,620 records (5 per example × 104 subjects)
**Storybook reading sample:** 30 records

---

## Verification gates (all passed)

- **PARENT_OK** — fetched parent SHA `d8dfba0` (subject "regen
  crow-pitcher + tortoise-hare audit reports with parametric
  coverage").
- **HEAD_OK** — branch checked out at the expected parent SHA.
- **PLAYBOOK_OK** — `AUDIT-PLAYBOOK.md` present.

## Smoke tests (8/8 green)

`scalar_pools` ✓ `form_parser` ✓ `form_families` ✓
`auto_parametric` ✓ `character_pools` ✓ `opener_pools` ✓
`emotion_pools` ✓ `scripts/test_parametric_e2e.py` ✓

---

## Storybook reading

**Before** (random 30 of 1,620): GOOD 7 / OKAY 10 / BAD 13
(23% GOOD)

**After**: GOOD 12 / OKAY 13 / BAD 5 (40% GOOD)

The `≥80% GOOD` bar is **not met**. The remaining BAD records
break for structural reasons that fall outside one slice's
budget:

- **Char/string mismatch in G1-08** (R6, R29) — the parametric
  slot draws from `STR_SHORT` but the concept_phrase is
  hard-coded to "the character \\X" (single-character idiom).
  Forms like `"harbor"` render with prose claiming "the
  character \\harbor". Fix is parametric-system territory: the
  slot type or the per-form concept_phrase needs to update
  together. Flagged for a follow-on slice.
- **Bullet-fragmented story slots in G8-14, G10-11** (R14, R9)
  — short scenario / need / mapping paragraphs each sit
  alone, reading as a manual rather than a fable. Each lift
  needs a per-grade scenario rewrite (~30 examples). Flagged.
- **Marker-form story slots in G11-12** (R17) — the "study
  basilisp" subjects use markers like `(do "pewter" :gamma)`
  with metaphorically thin scenario slots. Flagged.

The lifts I did land lift the GOOD ratio significantly (from
23% to 40%) but reaching 80% requires fixes that are scoped to
those follow-on slices.

---

## Audit-harness baseline → after

| Detector | BEFORE | AFTER | Delta |
| --- | ---: | ---: | ---: |
| **TOTAL (existing detectors only)** | 1,681 | **1,624** | **−57** |
| LOW_GROUNDING | 505 | **439** | **−66** |
| HONEST_JUDGE_REPEAT | 18 | 18 | 0 |
| VILLAGE_NOUN_OVERUSE | 22 | 21 | −1 |
| BOOL_LEAK_RESOLUTION | 34 | 34 | 0 |
| STORY_RESOLUTION_NO_DRAWN | 922 | 922 | 0 |
| REPL_AS_TIME_TRAVELLER | 38 | 38 | 0 |
| HIGH_LENGTH | 16 | 16 | 0 |
| ANSWER_LEAK_STRING | 7 | 22 | +15 (regression — see "Devs") |
| **NEW: EMPTY_GOAL_RENDERED** | — | 230 | new |
| **NEW: STRING_AS_CHAR_MISCLAIM** | — | 7 | new |
| **NEW: PARAGRAPH_FRAGMENTATION** | — | 82 | new |
| TOTAL with new detectors | 1,681 | 1,943 | (3 new categories add 319) |

LOW_GROUNDING delta is negative (**−66**, ~13% reduction) — the
Cat-J completion gate is satisfied.

---

## Cat-J grounding lifts (10+ lifts)

All in `src/mmllm/aesop/curriculum/boy_wolf/_metaphor_pools.py`.
Each adds `{emo_patient}` (rendering BW_EMO_PATIENT phrases
that the audit-harness already recognizes) + an environmental
adjective tied to the boy-wolf valley + a 1-sentence mapping to
the algorithmic situation.

1. **`_POUCH_SUBPLOTS` T2** (heavy belt-pouch + long road)
   — already wired by the prior eUtZ slice; not modified.
2. **`_GATE_SUBPLOTS` T2** "Why did the gate stay shut?" — Cat-K
   rewrite + heavy timber.
3. **`_GATE_SUBPLOTS` T3** first-closed-gate — Cat-K trim +
   heavy timber + {emo_patient}.
4. **`_GATE_SUBPLOTS` T5** "So the gate just says yes or no?"
   — Cat-K dialogue rewrite + heavy timber.
5. **`_RECIPE_SUBPLOTS` T3** last-step-is-served — Cat-K
   rewrite + worn watchhouse wall + {emo_patient}.
6. **`_NOTEBOOK_SUBPLOTS` T2** atomic-swap — Cat-K rewrite +
   heavy slate cool against forearm + {emo_patient}.
7. **`_REWRITERULE_SUBPLOTS` T2** recipe-vs-rule — Cat-K
   rewrite + cool watchhouse slate + {emo_patient}.
8. **`_REWRITERULE_SUBPLOTS` T3** order-matters — Cat-K
   rewrite + concrete village routine + {emo_patient}.
9. **`_SCRIBE_SUBPLOTS` T1** reading-conventions — Cat-K
   rewrite (replaces the abstract list with "the watchhouse
   reads its posted notices") + cool slate + {emo_patient}.
10. **`_CHALKMARK_SUBPLOTS` T_last** mark-vs-sheep — Cat-K
    rewrite (concrete shepherd-points-elder-corrects) +
    {emo_patient}.
11. **`_TOOLSHED_SUBPLOTS` T4** two-worlds — Cat-K rewrite
    (concrete cool stone wall image) + {emo_patient}.

---

## Cat-K storytelling lifts (10 prose rewrites — exceeds ≥5)

Every Cat-J lift listed above is also a Cat-K rewrite (the
template was rewritten end-to-end to scan as story prose, not
just to add an emotion injection). Specific K-classes:

- Lifts 2, 4 (gate dialogue): K-7 redundant emotion → replaced
  with K-anchored shepherd-asks-elder-answers shape.
- Lift 3 (first-closed-gate): K-2 pacing (trimmed filler).
- Lift 5 (recipe last step): K-3 AI cadence ("the runner
  would carry back" feels canned) → grounded in the chalk on
  the worn wall.
- Lift 6 (atomic-swap): K-3 cadence rewrite + K-6
  under-earned metaphor → "I don't pick it up and walk
  away" makes the atomic-swap concrete.
- Lifts 7, 8 (rewriterule): K-3 abstract distinction →
  concrete chalk-on-slate scene.
- Lift 9 (scribe conventions): K-3 list-of-rules → K-anchored
  "watchhouse reads posted notices" image.
- Lift 10 (chalkmark): K-3 declarative → K-anchored
  shepherd-points-at-mark-elder-points-at-meadow.
- Lift 11 (toolshed): K-6 under-earned boundary metaphor →
  concrete "cool stone wall behind the watchhouse" image.

In addition to the 10 metaphor-pool rewrites, the
**`_GOAL_SUBPLOTS` `_story()` helper** was rewritten:
- old: `"To {goal_text}, {elder_he_she}, {emo_patient},
  composed …"` (would render `"To , X composed"` when
  goal_text empty)
- new: `"{elder_phrase}, {emo_patient}, composed …"`

This eliminates the empty-goal stutter for the story-scaffold
template specifically; other metaphor-pool templates that still
say `"To {goal_text}, X composed …"` retain the stutter for
atom-style story examples — a follow-on slice should rewrite
them or restrict the story tag from atom subjects.

---

## New audit detectors (3)

1. **`EMPTY_GOAL_RENDERED`** — flags `"To , <pronoun>
   composed"` in user_msg. Cat-A: an empty `{goal_text}`
   placeholder rendered as visible empty space between commas.
   230 hits in current audit (atom-style story-tagged subjects
   plus a few metaphor-rich subjects whose forms aren't covered
   by the GOALS dict or the `get_goal` allow-list).

2. **`STRING_AS_CHAR_MISCLAIM`** — flags records where the form
   is a multi-character string literal (`"harbor"`) but the
   prose calls it `"the character \X"` (Cat-E semantic mismatch).
   7 hits — all from G1-08 parametric records where the slot
   draws strings but concept_phrase is still char-idiomatic.

3. **`PARAGRAPH_FRAGMENTATION`** — flags records with 4+ short
   (≤25 words) paragraphs in body. Cat-K K-2 pacing failure
   (the rendered story reads as a bulleted manual). 82 hits —
   primarily story-scaffold examples whose author-written
   scenario / need / mapping slots are each a single short
   sentence.

---

## Other source fixes

- **`opener_pools.py:265`** — pronoun-neutral fix:
  `"{primary_phrase} stood watch, and they trusted his voice"`
  → `"...trusted that voice"`. The hardcoded `his` produced a
  Cat-C grammar mismatch when the drawn primary character was
  female (sample R23 in storybook reading).
- **`_goals.py:1829`** added `get_goal()` fallback that
  synthesizes a verb-phrase from `question_what` when GOALS
  has no entry, restricted to forms containing
  `defprotocol|defmacro|deftype|defrecord|defmulti|extend-protocol|extend-type|let [^`.
- **Each grade's `_ex` helper** updated to import `get_goal`
  and use it instead of the bare `GOALS.get("goal", "")`.

## Polarity check

Spot-checked: shepherd is consistently the boastful /
false-alarmer ({emo_proud}, {emo_desperate}); elder is
consistently the patient evaluator ({emo_patient}). No
polarity flips. The Cat-J lifts attach `{emo_patient}` only to
elder-role lines.

## Sync

Branch is at integration head: `git merge-base HEAD
origin/claude/analyze-repo-status-rN0vt` returned the
integration SHA exactly. No rebase conflicts.

---

## Deviations from prompt

1. **Storybook GOOD ratio is 40% (target ≥80%)**. Closing the
   gap requires structural fixes outside this slice's source
   set: the parametric `STR_SHORT` / concept_phrase mismatch
   in G1-08, bullet-fragmented scenario slots in G8-14 /
   G10-11, and the marker-form story slots in G11-12. Each is
   ~30-50 lines of prose authoring and was not feasible inside
   one slice's budget.

2. **ANSWER_LEAK_STRING regression: 7 → 22**. Comes from
   widening `get_goal`'s allow-list to include `defprotocol /
   defmacro / deftype / defrecord` etc. The synthesized
   goal_text for some forms (e.g., the Alarm protocol form
   that returns `:string-alarm`) contains the answer string,
   which the leak detector flags. A follow-on cleanup pass
   should write per-form GOALS entries for these constructs
   so the synthesized fallback no longer fires.

3. **EMPTY_GOAL_RENDERED at 230** — atom-style subjects with
   story tags continue to render `"To , X composed"` because
   the metaphor-pool templates (113 instances of
   `"To {goal_text}, X composed"`) weren't bulk-rewritten in
   this slice. Recommend either restricting the auto-story-tag
   in `_ex` for atom forms, or rewriting the metaphor-pool
   templates to drop the `"To {goal_text}"` prefix.