# Deep audit — milkmaid, slice Wvxw

**Branch:** `claude/audit-milkmaid-Wvxw` (off `origin/main`)

**Slice:** grades 2, 4, 6, 8, 9, 12 (random sample of 6 of 12)

**Read corpus:** 443 generated records (~5 per subject across 110 subjects in the slice), 8100 lines, written to `/tmp/read-corpus-milkmaid.md`.

## Summary

Found 14 distinct papercut patterns affecting roughly 120-150 of the 443 read records (27-34%). All patterns trace back to ~10 specific source-template lines in `src/mmllm/aesop/curriculum/milkmaid/_metaphor_pools.py`. Fixed every pattern at the source. Added 4 new audit detectors so the harness catches the same patterns in future audits and across other fables.

| Metric | Before | After |
| --- | ---: | ---: |
| `audit-harness.py` reported issues for milkmaid | 0 | 0 |
| Sentence-start lowercase pronouns in 443-record corpus | 60 | 0 |
| `For [imperative-verb]` rendered phrasings in corpus | 7 | 0 |
| `form that <noun>` (no verb) in corpus | ~15 | 0 |
| `Now we [noun]` rendered phrasings | 2 | 0 |
| `"Pronoun, what did you do?"` vocative use | 1 | 0 |
| Pre-existing detectors reporting on milkmaid | 0 | 0 |

The harness reported 0 issues both before and after because the existing detectors did not catch any of these papercut patterns — exactly why the new detectors needed to be added.

## Papercut patterns and source fixes

### Cat-B: lowercase pronoun starting a sentence after period (60 records)

**Source:** `_metaphor_pools.py` had ~81 occurrences of `[.!?]"?\s+\{X_he_she\}` — a sentence-end punctuation followed by a lowercase pronoun placeholder where the `_cap` variant was needed. The placeholder rendered as lowercase "he" / "she" / "they", producing strings like `asked. he replied,` / `cried. she shook her head` / `said. they began sorting`.

**Fix:** programmatic find-and-replace of every `[.!?]"?\s+\{X_he_she\}` to `\1{X_he_she_cap}` across `_metaphor_pools.py`. 81 substitutions in one file.

### Cat-C: same-gender pronoun ambiguity in dialogue tags (16 records)

**Source:** `_metaphor_pools.py` had templates like `{milkmaid_he_she_cap} asked. {farmer_he_she_cap} replied,`. When both characters happen to be female (or male, or neuter), the rendering reads "She asked. She replied," — two consecutive `She`s referring to different characters. Same for `{milkmaid_he_she_cap} cried. {farmer_he_she_cap} only shook her head`.

**Fix:** programmatic substitution of `(asked|cried|admitted|announced|said|exclaimed|wondered|said no)\.\s+\{farmer_he_she_cap\}` → `\1. {farmer}` (using the farmer's NAME for disambiguation). 16 substitutions.

### Cat-A: `For [imperative-verb]` ungrammatical (7 records)

**Source:** seven templates in `_metaphor_pools.py` started with `For {goal_text}`. `goal_text` always begins with an imperative verb ("create a vector", "find the minimum", "test whether 1 is less than 2"), producing renderings like "For create a vector containing 1, 2, and 3, a vector of three numbers is her rearrangement." The infinitive marker after "For" needed to be "To".

**Fix:** programmatic `\bFor \{goal_text\}` → `To {goal_text}` across `_metaphor_pools.py`. 7 substitutions.

### Cat-A: `the form that {concept_phrase}` — concept_phrase used as relative-clause subject without a verb (3 templates, ~15 affected records)

**Source:** four templates in `_metaphor_pools.py` used `the form that {concept_phrase}`. `concept_phrase` is a noun phrase ("the count operation", "the keyword lookup", "the conj operation"), so the rendered text became `the form that the count operation. Each slot is labeled by the form …` — a hanging relative clause with no verb.

**Fix:** replace `the form that {concept_phrase}` with `the form for {concept_phrase}` in all 4 occurrences.

### Cat-B: `{concept_phrase} is the form that ticks…` — sentence-start lowercase concept phrase (5 records)

**Source:** `_metaphor_pools.py` line 329 was `we must count — truly count. {concept_phrase} is the form that ticks through each coin, …`. After the period, `{concept_phrase}` rendered as lowercase noun phrase, putting a lowercase letter at sentence start.

**Fix:** changed period-before-concept_phrase to comma + "and": `we must count — truly count, and {concept_phrase} is the form that ticks…`. The single edit retires the entire pattern.

### Cat-B: split-quote with lowercase concept_phrase resumption (~13 records)

**Source:** `_metaphor_pools.py` line 296: `"To {goal_text}," {farmer_he_she} said calmly, "{concept_phrase} means we count …`. The second quote starts mid-attribution but `{concept_phrase}` is itself a noun-phrase fragment, producing comma-spliced output: `"To add the integers 1 through 10," she said calmly, "the sum of ten numbers means we count, we stack, we tally."`.

**Fix:** rewrote the split-dialogue so the second quote resumes with concrete prose and `{concept_phrase}` is named after a clean dash, not at sentence start: `"To {goal_text}," {farmer_he_she} said calmly, "we count, we stack, we tally. The coins do not lie — {concept_phrase} is just a name for that careful work."`.

### Cat-A: `{concept_phrase} does this step by step` — concept_phrase used as sentence subject (~11 records)

**Source:** `_metaphor_pools.py` line 321 was `step-by-step walk through the coins. {concept_phrase} does this step by step, stacking one coin upon the next.`. After the period, `{concept_phrase}` renders as `the multi-arg subtraction`, leading to a lowercase sentence start AND an awkward "the [noun] does this step by step" phrasing.

**Fix:** restructured to a single sentence with a relative-clause framing: `step-by-step walk through the coins, where {concept_phrase} stacks one coin upon the next.`. The integration handles both the capitalization and the awkward subject-of-its-own-sentence problem.

### Cat-A: `Now we {concept_phrase} — we continue milking` — concept_phrase used as a verb (2 records)

**Source:** `_metaphor_pools.py` line 678: `Then {farmer_he_she} turned to {milkmaid} and said, "Now we {concept_phrase} — we continue milking …`. Renders as `Now we future, multiply, deref — we continue milking …` when `concept_phrase` happens to be a verb-list. The template assumed `concept_phrase` was a verb phrase but it's actually a noun phrase.

**Fix:** changed `Now we {concept_phrase}` to `Now we use {concept_phrase}`. Adds the verb so the noun phrase fits.

### Cat-C: pronoun used as vocative (1 record)

**Source:** `_metaphor_pools.py` line 217 had `richer. "{farmer_he_she_cap}, what did you do?"` — the `{X_he_she_cap}` was used as a vocative-form-of-address inside dialogue. When the farmer's gender is "n", this renders as `"They, what did you do?"`. Should be the farmer's NAME, not the pronoun.

**Fix:** swapped `{farmer_he_she_cap}, what did you do?"` for `{farmer}, what did you do?"`, and elevated the second mention `{farmer} replied` to `{farmer_he_she_cap} replied` (so we don't repeat the name on consecutive lines).

### Cat-B: `But {X_he_she_cap}` after period — capitalized pronoun mid-sentence after "But" (9 records)

**Source:** my Cat-B sentence-start fix above was overly aggressive — it capitalized pronouns even when "But" preceded them. `"...as I carry it." But {X_he_she_cap}` should render `But she shook her head`, not `But She shook her head`. (English: a sentence may start with "But she...", with a lowercase pronoun.)

**Fix:** programmatic correction `\b(but|But)\s+\{X_he_she_cap\}` → `\1 {X_he_she}` for 9 occurrences in `_metaphor_pools.py`.

## New audit detectors added

Added 4 new detectors to `docs/clojure-pedagogy/audits/audit-harness.py`. Each is a regex applied to the rendered `user_msg`:

1. **`SENTENCE_START_LOWER_PRONOUN`** — flags any `[.!?]"?\s+(he|she|they)\b`. Catches sentence-start lowercase pronouns from un-capped `{X_he_she}` placeholders.

2. **`PRONOUN_AS_VOCATIVE`** — flags `"(He|She|They), `. Catches pronouns used as vocative inside dialogue (when the template should have used the character NAME).

3. **`FOR_GOAL_TEXT_VERB_INCONGRUITY`** — flags `\bFor (create|find|test|add|subtract|multiply|divide|compute|apply|append|extract|get|return|count|build|name|read|write|submit|evaluate|call|check|use|swap|deref|throw|catch|sort|filter|map|reduce|increment|decrement) `. Catches `For {goal_text}` rendered with imperative verb where `To {goal_text}` was needed.

4. **`HANGING_FORM_THAT`** — flags `\bform that\s+(the|an|a|this) [noun]` where the next ~1 word is not a verb (uses a negative lookahead for an explicit verb whitelist: says/reads/computes/etc.). Catches `the form that {concept_phrase}` patterns where concept_phrase is a noun phrase.

All four detectors fire correctly on synthetic test cases (verified manually). On the post-fix milkmaid corpus, they all return 0 hits.

**Cross-fable observation (FYI, not in scope):** The new `HANGING_FORM_THAT` detector catches 1 issue in `tortoise_hare`, 19 in `boy_wolf`, and 9 in `dog_shadow` — all pre-existing template bugs in those fables that the older detectors missed. Out-of-slice for this audit; flagged for follow-up.

## Pedagogical lens preserved

The milkmaid moral — daydream vs. care — held up across the 443 records: in every record I reviewed, the milkmaid was the one who guesses, boasts, or tries to know without counting; the farmer (or another careful character) is the one who patiently sorts, counts, or evaluates. None of the source-edits inverted this polarity.

---

## Remediation (rebased onto integration branch)

The first commit of this audit (`c50a1c3`) was based on `main`, but the integration branch carrying the parametric scalar system, the new pools, the form_families library, the auto_parametric migration tool, the bb_verifier, and the audit playbook is `claude/analyze-repo-status-rN0vt`. Re-based onto the integration branch:

- Cherry-picked `c50a1c3` cleanly onto integration (no conflicts; integration's edits and the audit's edits don't overlap).
- All seven integration-branch smoke tests pass on the rebased branch (`scalar_pools`, `form_parser`, `form_families`, `auto_parametric`, `character_pools`, `opener_pools`, `emotion_pools`, plus `scripts/test_parametric_e2e.py`).
- Resulting branch: `claude/audit-milkmaid-Wvxw-remediated`.

The integration branch's audit harness is stricter than `main`'s; baseline milkmaid issue count when the four prior detectors plus the integration's pre-existing checks run is **29** (DOUBLE_PREP=1, FORM_LEAK=1, ANSWER_LEAK=3, ANSWER_LEAK_STRING=1, HIGH_LENGTH=23). Those 29 are pre-existing on the integration branch and out-of-scope for this remediation (per "Don't touch any fable other than milkmaid" — they live in milkmaid templates but require pool-level investigation; left for a follow-up audit slice).

## Cat-J fixes (completion)

The prior commit deferred the Cat-J grounding lift. This remediation completes it.

The haiku reader had identified ~58 records with "softly|quietly|gently" generic adverbs and "the X operation" generic concept phrases. Tracing those back to source, the bare-adverb shortcut lives in 4 templates in `_metaphor_pools.py` and the flat-reaction-beat lives in another 4-5 templates. **12 distinct templates were rewritten at the source** to add: (a) named character emotion via `{emo_proud}` / `{emo_patient}` / `{emo_regretful}` / `{emo_content}` interpolation drawn from the rich EMO pools, (b) at least one concrete environmental adjective (the pail is heavy, the road is long, the silver is heavy, the copper is warm, the parchment is cool, the chalk's edge is cool, etc.), and (c) a sentence that maps that adjective to the algorithmic situation (heavy pail ↔ accumulator load, long road ↔ collection length, an empty pail ↔ the form's honest result of an absent rule, the wicker remembers ↔ persistent immutable structure).

The 12 lifts (file: `src/mmllm/aesop/curriculum/milkmaid/_metaphor_pools.py`):

1. **`said quietly` → `said {emo_patient}, the chalk's edge cool against {farmer_his_her} fingers`** (atomic-update template, line ~258). Names: chalk's edge, cool, fingers (touch). Maps: shared ledger ↔ atomic update.
2. **`said calmly` → `said {emo_patient}` plus pail-heavy / long-road framing** (counting template, line ~298). Names: pail heavy, road long. Maps: heavy pail ↔ accumulator load; coins do not lie ↔ honest tally.
3. **`said gently` → `said {emo_patient}` plus market-square / copper-cool framing** (declared-to-traders template, line ~322). Names: market square, copper cool, road long. Maps: long road / counted steps ↔ step-by-step iteration.
4. **`said` (bare) → `said, {emo_content}` plus silver-heavy / copper-warm framing** (yesterday's-sales template, line ~308). Names: silver heavy, copper warm, market a long walk. Maps: heap weight ↔ summation; carry coin to total ↔ form-as-count.
5. **`asked. {farmer_he_she} replied` → `replied, {emo_patient}` plus three-heaps-patient framing** (sort-coins template, line ~315). Names: three heaps patient and even, weight cool, value plain. Maps: stacking ↔ combine; slow-certain-irrevocable ↔ form's logic.
6. **`tried to guess the fortune` → `tried to guess the fortune, {emo_proud}, the dairy cool and the imagined market still far away`** (cache template, line ~336). Names: dairy cool, imagined market far. Maps: heavy heap ↔ honest weight; daydream of fortune ↔ slippery numbers.
7. **`said gently` → `said, {emo_patient}` plus parchment-cool / ink-sharp framing** (echo-vs-original template, line ~561). Names: parchment cool, ink sharper, copy faintly smudged. Maps: original scroll ↔ canonical source; echo ↔ stale/aliased copy.
8. **`smiled and said` → `touched the milkmaid's apron … said, {emo_patient}`** (let-binding pouch template, line ~74). Names: cloth still cool from morning dairy, pocket small, road long. Maps: small pocket ↔ scope edge; "fits there fits only for one stretch" ↔ binding lifetime.
9. **`smiled and said, "No"` → `weighed the basket … {emo_patient}`** (immutable-collection template, line ~161). Names: wicker cool, load honest, basket heavy. Maps: wicker remembers ↔ persistent immutable structure; basket heavy because of contents ↔ value-driven.
10. **`smiled and said, "No"` → `shook {his_her} head, {emo_patient}, the strainer dripping in {his_her} steady hand`** (filter-rule template, line ~237). Names: milk pooled cold and useless, strainer dripping, steady hand. Maps: empty pail ↔ honest result of absent rule.
11. **`smiled and said` → `tapped the pail … replied, {emo_patient}`** (chalk-mark vs contents template, line ~847). Names: pail wood cool and heavy, chalk mark light, label vs contents. Maps: light label ↔ symbol; heavy pail ↔ value; lifting ↔ deref.
12. **`read it and said` → `read it, the slip thin between {his_her} fingers, and said, {emo_patient}`** (recipe-rewrite-macro template, line ~737). Names: slip thin, day short, recipe long, lines shorter and quantities precise. Maps: long-recipe / short-day ↔ macro expansion budget; precise quantities ↔ deterministic rewrite.

Each lift retires the pattern across every render that fires the affected template. Each EMO interpolation also brings randomized variety across the rich pools (199 band entries, 396 archetype entries combined).

### Cat-J — LOW_GROUNDING detector

Added a fifth audit detector to `audit-harness.py`:

5. **`LOW_GROUNDING`** — fires when user_msg lacks BOTH (i) any drawn-value reference (any int>2 / keyword / quoted string from `rec.code_str` appears in user_msg) AND (ii) any phrase fragment from the rich EMO pools (EMO_PATIENT, EMO_REGRETFUL, EMO_CONTENT, EMO_BOASTFUL, EMO_PROUD, EMO_DESPERATE, EMO_HUNGRY). Also fires on the generic-adverb shortcut: `said softly|quietly|gently|calmly` without an accompanying rich EMO fragment. Both modes are LOW_GROUNDING — the affirmative directive is "name the emotion AND the environmental adjective AND map it to the algorithmic situation"; records that satisfy neither component fail Cat-J.

The detector caches the EMO pool fragments at first call (lazy import) and uses simple substring matching, so it adds negligible cost to the audit pass.

### Cat-J — before / after (LOW_GROUNDING counts on milkmaid)

| State | Total milkmaid issues | LOW_GROUNDING |
| --- | ---: | ---: |
| Before Cat-J lifts (cherry-pick state on integration) | 507 | 478 |
| After 12 source-template lifts | 427 | 398 |

LOW_GROUNDING dropped by **80 records (16.7% reduction in LOW_GROUNDING)** from 12 source-template edits. The remaining 398 LOW_GROUNDING flags identify records whose templates haven't been Cat-J-lifted yet — they are tractable per-template fixes (each remaining target template fires across many records, so subsequent slices can drive the count further down with similar leverage).

## Files changed (combined original + remediation)

- `src/mmllm/aesop/curriculum/milkmaid/_metaphor_pools.py` — 14 prose-correctness edits from the original audit (Cat-A, Cat-B, Cat-C) plus 12 Cat-J grounding lifts in the remediation.
- `docs/clojure-pedagogy/audits/audit-harness.py` — 4 detectors from the original audit (`SENTENCE_START_LOWER_PRONOUN`, `PRONOUN_AS_VOCATIVE`, `FOR_GOAL_TEXT_VERB_INCONGRUITY`, `HANGING_FORM_THAT`) plus 1 from the remediation (`LOW_GROUNDING`).
- `docs/clojure-pedagogy/audits/deep-audit-milkmaid-Wvxw.md` — this document.

## Caveats (combined)

- The original deep-read sampled 443 generated records; the remediation's Cat-J read sampled an additional 550 records (seed=42, 5 per example across grades 2/4/6/8/9/12). Patterns appearing <5x per subject in random samples are still likely under-detected.
- Cat-J lifts focus on the 12 most-fired templates that contained bare adverbs or flat-reaction beats. Other templates (the further 398 LOW_GROUNDING flags after lifts) carry less-obvious grounding deficits — those are good targets for the next audit slice.
- The 29 pre-existing milkmaid issues from the integration branch's stricter audit (DOUBLE_PREP=1, FORM_LEAK=1, ANSWER_LEAK=3, ANSWER_LEAK_STRING=1, HIGH_LENGTH=23) are not addressed here — the remediation's scope was Cat-J completion, not a fresh full-spectrum audit on the integration branch. They're pre-existing as of `36fd180` and tractable for a follow-up.
- Cat-D (spelling) was clean. Cat-E (fable polarity) preserved — milkmaid daydreams/boasts; farmer counts patiently. None of the 12 lifts inverted this. Cat-F/G/H/I were thin during the original read.
