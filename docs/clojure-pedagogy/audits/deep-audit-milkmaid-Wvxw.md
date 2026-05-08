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

## Caveats

- I read 443 generated records, not the full ~109,000 the curriculum can produce at standard `n_per_example=222`. Any pattern that appears <5x per subject in random samples is likely under-detected. The new detectors will catch many of those over time.
- I only addressed Cat-A (logical), Cat-B (syntax), Cat-C (grammar) papercuts. Cat-J (insufficient emotion-and-adjective grounding) appeared in the haiku reader's report (29 records of generic "softly|quietly|gently" emotional shorthand and 29 records of "the X operation" generic concept phrases) but I did not author a deeper richer-emotion lift in this slice — those need scenario-by-scenario authoring and would balloon the change set. Document follows.
- Cat-D (spelling) was clean. Cat-E (fable polarity) was clean — milkmaid's daydream-vs-care polarity was preserved across all 443 reviewed records. Cat-F, Cat-G, Cat-H, Cat-I were thin (1-2 records each, mostly trace-amount artifacts).

## Pedagogical lens preserved

The milkmaid moral — daydream vs. care — held up across the 443 records: in every record I reviewed, the milkmaid was the one who guesses, boasts, or tries to know without counting; the farmer (or another careful character) is the one who patiently sorts, counts, or evaluates. None of the source-edits inverted this polarity.

## Files changed

- `src/mmllm/aesop/curriculum/milkmaid/_metaphor_pools.py` — 14 source edits across 4 distinct patterns plus the wholesale 81-substitution `_he_she` → `_he_she_cap` pass.
- `docs/clojure-pedagogy/audits/audit-harness.py` — 4 new detectors appended to `check_record()`.
- `docs/clojure-pedagogy/audits/deep-audit-milkmaid-Wvxw.md` — this document.
