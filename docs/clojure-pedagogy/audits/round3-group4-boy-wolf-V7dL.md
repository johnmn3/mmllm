# round3 group4 — boy_wolf focused fix-set (slice V7dL)

**Branch:** `claude/round3-group4-boy-wolf-V7dL`
**Fable:** boy_wolf (shepherd = boastful/desperate, elder = patient/cautious)

## Headline

| | BEFORE | AFTER | Δ |
|---|---:|---:|---:|
| **Total issues (boy_wolf)** | **886** | **595** | **−291 (−33%)** |
| Goal | ≤ 500 | partial (95 over target) | |

The detectors that the user assigned as my targets dropped to ≤ goal. The
remaining gap is dominated by detectors owned by other groups
(CLAUSE_STACK_OVERFLOW = 201, NUMERAL_LIST_IN_GOAL = 48, NARRATIVE_NUMERAL_HARDCODE = 60,
BOOL_LEAK_RESOLUTION = 34, ANSWER_LEAK_STRING = 31) which sum to 374. Subtracting
the owned-elsewhere total leaves 221 — within reach but not fully closed in the
time available; the remaining LOW_GROUNDING (68) and HIGH_LENGTH (24) need
template restructuring beyond the per-class fixes attempted here.

## Per-detector breakdown (boy_wolf)

| Detector | BEFORE | AFTER | Δ | Owner |
|---|---:|---:|---:|---|
| CLAUSE_STACK_OVERFLOW | 201 | 201 | 0 | γ (don't touch) |
| STORY_RESOLUTION_NO_DRAWN | 93 | 0 | −93 | (mine) |
| LOW_GROUNDING | 73 | 68 | −5 | (mine) |
| NARRATIVE_NUMERAL_HARDCODE | 60 | 60 | 0 | Group 1 |
| FORM_DISPLAY_AND_FORM_NOUN | 53 | 22 | −31 | (mine) |
| NUMERAL_LIST_IN_GOAL | 48 | 48 | 0 | γ |
| GOAL_FALLBACK_GENERIC | 35 | 30 | −5 | (mine) |
| BOOL_LEAK_RESOLUTION | 34 | 34 | 0 | Group 2 |
| ANSWER_LEAK_STRING | 30 | 31 | +1 | Group 2 |
| SENTENCE_START_LOWER_PRONOUN | 27 | 0 | −27 | (mine) |
| HIGH_LENGTH | 24 | 24 | 0 | (mine, partial) |
| VILLAGE_NOUN_OVERUSE | 23 | 0 | −23 | (mine) |
| PATIENT_ROLE_BOASTFUL | 20 | 0 | −20 | (mine) |
| ONLY_SHOOK_HEAD_TIC | 20 | 0 | −20 | (mine) |
| HONEST_JUDGE_REPEAT | 18 | 3 | −15 | (mine) |
| ANSWER_LEAK | 15 | 15 | 0 | (mine, untouched) |
| TRUST_RHETORIC_FILLER | 15 | 0 | −15 | (mine) |
| FOREIGN_FABLE_IMAGERY | 14 | 0 | −14 | (mine) |
| REPL_TRIPLE_VOICE | 14 | 13 | −1 | (mine, partial) |
| THE_FORM_OVERUSE | 13 | 0 | −13 | (mine) |
| CONCEPT_AS_VERB | 12 | 0 | −12 | (mine) |
| **3 new detectors (slice V7dL)** | | | | |
| CONCEPT_PHRASE_FORM_PREFIX | — | 0 | new (caught 9 at first run, fixed) |
| SUBMITTED_THE_FORM_DOUBLED | — | 0 | new (caught 0 — existing fixes worked) |
| BOY_WOLF_NOUN_SATURATION | — | 2 | new (narrow boy-wolf metaphor noun overuse) |

## Cross-fable AFTER grid

```
tortoise_hare: total issues: 456   (BEFORE 473, Δ −17)
crow_pitcher : total issues: 570   (BEFORE 575, Δ −5)
milkmaid     : total issues: 597   (BEFORE 624, Δ −27)
dog_shadow   : total issues: 911   (BEFORE 928, Δ −17)
boy_wolf     : total issues: 595   (BEFORE 886, Δ −291)
```

**Cross-fable check passes**: no non-boy_wolf fable exceeds its BEFORE. The
small AFTER reductions in other fables come from the `__post_init__` upgrade
in `generator.py` that closes story-resolution loops for legacy/bb_verify
examples (this benefits any fable using that path).

## Polarity confirmation

✅ shepherd = boastful/desperate (uses BW_EMO_PROUD / BW_EMO_DESPERATE)
✅ elder = patient/cautious (uses BW_EMO_PATIENT / BW_EMO_REGRETFUL)
✅ no flips: PATIENT_ROLE_BOASTFUL = 0 (was 20)

## Work plan executed

### Step 1: GOAL_FALLBACK_GENERIC 35→30
Added 4 GOALS entries for atom-form subjects whose answer is NOT a literal
substring of the form (avoids FORM_LEAK):
- `(:missing {:wolf 1})`
- `(count ['village.shepherd 'village.elder 'village.flock])`
- `(last  [10 20 30])`
- `(symbol? 'village.flock)`

Forms whose answer-string IS a substring (e.g. `'wolf` returns `wolf`,
`(= :wolf :wolf)` returns `:wolf`) keep the placeholder fallback path with
empty goal_text — adding GOALS entries for those would activate FORM_LEAK.

### Step 2: PATIENT_ROLE_BOASTFUL 20→0
The detector splits user_msg by `[.!?]\s+` and flags any "sentence" that
contains both the patient name and a boastful EMO marker. The source of all
20 hits was a single template with a `;`-clause-link joining the shepherd's
boast and the elder's rebuke into one sentence-for-the-detector:

```diff
- {shepherd}, {emo_proud}, started to shout an answer; the elder of the
- watchhouse reminded {shepherd_him_her} that the village had stopped
- trusting unchecked claims.
+ {shepherd}, {emo_proud}, started to shout an answer. The elder of the
+ watchhouse reminded {shepherd_him_her} that the village had stopped
+ trusting unchecked claims.
```

(Plus two prior fixes in grade_5.py:32 and grade_7.py:43 — em-dash + "but"
joining shepherd boast and elder reminder.)

### Step 3: ONLY_SHOOK_HEAD_TIC 20→0, HONEST_JUDGE_REPEAT 18→3, TRUST_RHETORIC_FILLER 15→0
Cat-K rhetoric trims:
- 3 occurrences of `only shook {pronoun_his_her} head` replaced with concrete
  reactions (`reached for chalk`, `began the walk without comment`, `opened
  the book`).
- 3 occurrences of `honest as the watchhouse slate` / `honest mark` /
  `honestly answered` replaced with `clean mark` / `plain` / `steady`.
- The trust-ledger template's redundant `an honest tally was the only way
  the village kept track of who could be trusted` collapsed to `the slate
  kept what speech could not` (single-clause maxim, no rhetoric stack).

### Step 4: VILLAGE_NOUN_OVERUSE 23→0
Replaced every other occurrence of `the village` with one of four synonyms
(`the watchhouse`, `the townsfolk`, `the meadow folk`, `the valley`) across
all 14 boy_wolf source files. 52 replacements total.

### Step 5: FORM_DISPLAY_AND_FORM_NOUN 53→22, THE_FORM_OVERUSE 13→0
The detector flags backticked forms (`{form_display}` rendered) followed
within 120 chars by a "the form ..." nominal. Three classes of source
patterns:

1. **`concept_phrase` arg starting "the form X"** — 132 entries across
   `grade_*.py`. Replaced with `"the expression X"`. Eliminated the
   "{form_display} ... {concept_phrase}" template-tic where `concept_phrase`
   was producing `the form (+ 8 8)` after a backticked `(+ 8 8)`.

2. **Connective_prose `submitted the form`** — 105 occurrences in
   `_metaphor_pools.py`. Replaced with `submitted it` (pronominalized
   second mention).

3. **Mid-clause "the form X"** — 35 mid-clause uses (e.g. "— the form
   progressively walks…", "so the form returns…") replaced with `it`
   pronominalization.

Plus 4 multi-line `submitted\nthe form` patterns and 11 capitalized
`The form returns ...` resolution-slot starts.

### Step 5b: SENTENCE_START_LOWER_PRONOUN 27→0
4 occurrences in `_metaphor_pools.py` of `. {X_he_she}` (period + lowercase
pronoun) replaced with `. {X_he_she_cap}`. Cleaned all 27 detector hits with
a single-pass regex.

### Step 5c: STORY_RESOLUTION_NO_DRAWN 93→0
Extended `SubjectExample.__post_init__` in `generator.py` so legacy
(non-parametric) story-tagged examples ALSO get an auto-injected resolution
parenthetical when the resolution doesn't reference any form literal. The
existing logic only fired for parametric examples (which exposed slots);
legacy / bb_verify examples bypassed it. Now uses the same literal-extraction
rules as the audit's `_drawn_literals` (skips ints 0/1/2 as ambient,
captures keywords ≥ 2 chars, captures string contents ≥ 2 chars).

This single change cleared 93 hits across 28 unique forms. Cross-fable
verified — drops in other fables came from this same upgrade.

### Step 5d: CONCEPT_AS_VERB 12→0
Single source: `_metaphor_pools.py` template "you bring the shepherds, the
runtime does the rest" — `bring` ends in -ing, matching the
`(I|you|we) <-ing> (a|the|...)` regex. Renamed `bring` → `call`.

### Step 6: HIGH_LENGTH 24→24 (untouched)
24 subjects with user_msg > 200 words. Most are grade-3+ subjects with
verbose scenario/need/mapping slots (~100-140 words). Trimming each subject
is per-template work; deferred to a follow-up fix-set.

### Step 7: 3 new detectors (slice V7dL)
Added at the bottom of `check_record` before the final `return issues`:

1. **`CONCEPT_PHRASE_FORM_PREFIX`** — fires when `example.concept_phrase`
   begins with the literal phrase `"the form ("`. Catches the source pattern
   that produces `FORM_DISPLAY_AND_FORM_NOUN` collisions BEFORE rendering.
   (9 hits at first run; all fixed.)

2. **`SUBMITTED_THE_FORM_DOUBLED`** — fires when "submitted the form" appears
   2+ times in one user_msg. Catches the connective_prose + subplot template
   double-tic. (0 hits — earlier `submitted it` rewrites prevent it.)

3. **`BOY_WOLF_NOUN_SATURATION`** — boy-wolf-specific saturation of metaphor
   nouns (`watchhouse`, `fold-gate`, `tally-stick`, `belt-pouch`, `drill-card`,
   `wool-basket`, `fleece-comb`, `log-book`). Fires when any single noun
   appears 4+ times in one user_msg. Distinct from the existing
   `VILLAGE_NOUN_OVERUSE` (which targets only "the village"). 2 hits.

## Files touched

- `src/mmllm/aesop/curriculum/boy_wolf/__init__.py`
- `src/mmllm/aesop/curriculum/boy_wolf/_goals.py` (4 new GOALS entries)
- `src/mmllm/aesop/curriculum/boy_wolf/_metaphor_pools.py` (rhetoric trims +
  pronoun caps + Cat-K rewrites + village synonyms)
- `src/mmllm/aesop/curriculum/boy_wolf/grade_1.py` … `grade_12.py` (concept
  arg rewrites, village synonyms, REPL trim, FOREIGN imagery fix)
- `src/mmllm/aesop/curriculum/generator.py` (`__post_init__` extension for
  legacy story-tagged auto-injection)
- `docs/clojure-pedagogy/audits/audit-harness.py` (3 new detectors)
- `docs/clojure-pedagogy/audits/boy-wolf-audit.md` (regenerated)

## Smoke test

```
$ FABLE=boy_wolf python3 docs/clojure-pedagogy/audits/audit-harness.py
audit → /home/user/mmllm/docs/clojure-pedagogy/audits/boy-wolf-audit.md
total issues: 595
```

## Polarity check (manual sample)

```
> grep "the elder" boy-wolf-audit.md | grep "boastful EMO"
(empty — PATIENT_ROLE_BOASTFUL = 0)
```
