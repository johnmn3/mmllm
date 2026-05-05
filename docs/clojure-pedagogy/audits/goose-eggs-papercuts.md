# Goose-eggs deep audit — paper cuts (12 grades, 1,090 records read)

12 reader agents read 5 records × 18-22 subjects per grade (totals: G1 90, G2 110, G3 90, G4 100, G5 110, G6 80, G7 90, G8 80, G9 90, G10 80, G11 70, G12 90). Each reported 11-15 distinct prose-quality patterns the structural audit harness can't detect.

Across grades, the patterns cluster into **18 distinct issue families**. The 7 cross-grade families are most impactful — they correspond to bugs in shared infrastructure (EMO pools, generator-level placeholder rendering, shared subplot templates). Per-grade families are mostly grade-specific subplot fits and concept_phrase cleanups.

## Cross-grade families (P0 / P1)

### G-1. Hardcoded gendered possessive in EMO_PATIENT — "her eyes always on the path"
**Severity:** P0 grammar bug.
**Reach:** 11 of 12 grades report this (every grade but G6 reports it directly; G6 reports the same root issue indirectly via G6-05/G6-11/G6-13 samples).
**Pattern:** `EMO_PATIENT` includes the literal string `"her eyes always on the path"`. The placeholder builder draws it uniformly, so it lands on male / `gender="n"` characters and produces "Frank, **her eyes always on the path**, said it would be simpler" (G2, G4, G5, G7, G10, G11, G12), "Henry said, **her eyes** always on the path" (G2, G12), "Oliver, **her eyes** always on the path" (G3, G4, G7, G10, G11), etc. Conservative count from samples: ≥35 mismatches per ~1000 records.
**Fix:** in `mmllm/aesop/fables.py`, replace `"her eyes always on the path"` with a gender-neutral variant `"with eyes always on the path"`. Add a harness regex `GENDERED_EMO` that flags `(David|Frank|Bob|Edward|Henry|Oliver|Charlie|George|Sam|Alex|Jordan|Robin|Casey|Morgan|Pat) [^.]*\bher (eyes|legs|hands)\b`.

### G-2. Object-case pronoun in subject position — "while {owner_him_her} submitted"
**Severity:** P0 grammar bug.
**Reach:** Grade 9 (subplot 11 of `goose_eggs/grade_9.py`).
**Pattern:** Template `agreed to wait while {owner_him_her} submitted the form` renders "while **her** submitted" / "while **him** submitted" / "while **them** submitted" — every record using subplot 11 has it. ≥6 sample hits in 90 records.
**Fix:** swap `{owner_him_her}` → `{owner}` (use the name) in `goose_eggs/grade_9.py` subplot 11. Add harness regex `OBJECT_AS_SUBJECT` flagging `\b(while|so|as) (her|him|them) (submitted|asked|wrote|said|chalked)\b`.

### G-3. Lowercase {place} after a period — sentence starts mid-prep
**Severity:** P0 grammar bug.
**Reach:** Grades 5, 7, 10, 12.
**Pattern:** Templates like `... on first glance. {place}, X typed...` and `... tests for the routines. {place}, the next entry...` — `{place}` returns lowercase prepositional phrase ("near the market", "deep inside the cellar"), so the second sentence starts in lowercase. ≥30 sample hits across the four grades.
**Fix:** restructure templates to put `{place}` in mid-sentence, OR capitalize via a helper. Targeted edits in `goose_eggs/grade_5.py` (ledger subplot), `goose_eggs/grade_7.py` (first-glance subplot), `goose_eggs/grade_10.py` (barn-wall subplot), `goose_eggs/grade_12.py` (filled-an-entire-leather-ledger subplot). Add harness regex `LOWER_PLACE_AFTER_PERIOD`.

### G-4. "in the farm" — bad place-preposition (BAD_PLACE_PREP extension)
**Severity:** P0 grammar bug (extension of pitfall #17 family).
**Reach:** Grades 2, 4, 5, 8, 10, 12.
**Pattern:** `place_phrase()` produces "in the farm" / "in the village" — but "in the farm" reads as inside a building. Idiomatic English: "on the farm" / "at the farm".
**Fix:** Add `farm` to `place_phrase()`'s preposition map (use `on / at / by / near`). Add `\bin the farm\b` to `BAD_PLACE_PREP` regex.

### G-5. DOUBLE_PREP — verb's preposition + place_phrase's preposition
**Severity:** P0 grammar bug (claimed in 522fbe7 but check is missing from harness).
**Reach:** All grades. Specifically `Halfway to {place}` (G1, fixed) and `On the way to market {place}` (G5).
**Pattern:** A verb that needs its own preposition (`to`, `at`, `from`, `with`, `onto`, `into`) followed by `{place}` whose first word is also a preposition produces "Halfway **to in the meadow**", "On the way to market **near the market**".
**Fix:** Add the `DOUBLE_PREP` regex to the harness (claimed but currently absent). Pattern: `\b(to|at|from|with|onto|into)\s+(in the|near the|on the|atop the|by the|along the|inside the|deep inside the|at the edge of the|inside a|deep inside a)\b`.

### G-6. Hardcoded place-prefix collides with {place} — "in the kitchen {place}"
**Severity:** P0 (locational tautology / contradiction).
**Reach:** Grade 6 (`barn-and-kitchen` subplot; "kitchen table {place}" in grade 2 and 4 ledger subplots).
**Pattern:** Template embeds a literal location ("in the kitchen", "kitchen table") then appends `{place}`. The result: "kitchen table **in the cellar**", "another slate in the kitchen **deep inside the kitchen**", "stood in the farm **at the edge of the orchard**".
**Fix:** strip the hardcoded location prefix or comma-bracket the appended `{place}`. Edit `goose_eggs/grade_2.py` (ledger subplot line ~57), `goose_eggs/grade_4.py` (collection subplot), `goose_eggs/grade_6.py` (barn-and-kitchen subplot line ~44). Add harness regex `DOUBLED_PLACE` for stutter patterns.

### G-7. "but pleased" duplicates already-positive EMO_CONTENT
**Severity:** P0 (tautology / "but" reading as contrast when emo is positive).
**Reach:** Grade 12 (banquet template: "X, {emo_content} but pleased, agreed to read it").
**Pattern:** EMO_CONTENT entries are positive ("happy with the day's small gift", "pleased with the steady fortune", "grateful for every coin"). Appending "but pleased" produces "happy with the day's small gift **but pleased**" — duplicate; "but" wrongly implies contrast.
**Fix:** in `goose_eggs/grade_12.py` banquet subplot, change "but pleased" to "and pleased" or drop. Add harness regex `BUT_PLEASED_TAUTOLOGY`.

### G-8. Trailing genitive "of the lecture" attached to EMO phrase
**Severity:** P0 (grammar bug; produces ungrammatical run-on).
**Reach:** Grade 10 (ledger-notebook subplot).
**Pattern:** Template tail `of the lecture` glued onto `{emo_greedy}` produces "with hands itching to count more **of the lecture**", "tempted by the thought of plenty **of the lecture**", "imagining all that might be gained **of the lecture**".
**Fix:** in `goose_eggs/grade_10.py` ledger subplot, drop the trailing `of the lecture`. Add harness regex `OF_THE_LECTURE`.

### G-9. Concept_phrase / question_what em-dash and parenthetical commentary surviving
**Severity:** P0 (answer-leak in some cases) / P1 (noise in others).
**Reach:** Grades 2, 5, 6, 7, 10, 12 (various).
**Pattern:** Pitfall #14's existing regex covers `note|first|empty|returns|integer` but several phrases slip through:
- G6-06 ex1 `"the value of (:private (meta 'x)), which is nil"` (answer-leak)
- G2-12 `"the return value of (println \"hello\") (it is nil)"` (answer-leak)
- G7-05 ex1 `"the predicate (some? 0) — 0 is not nil"` (em-dash commentary)
- G7-10 ex0 `"the :doc metadata on a symbol — what doc would print"`
- G10-08 ex0 `"the result of calling a function (args evaluated)"`
- G10-09 ex1 `"whether two fresh gensyms are equal (they aren't)"`
- G10-11 ex2 `"what [1 #_ 2 3] reads as (the 2 is dropped)"`
- G11-04 ex0 `"the count of \"tortoise\" — host-portable length"`
**Fix:** extend the audit's `EMDASH_COMMENTARY` and `ASIDE_PAREN` regexes to catch additional clauses. Then clean the affected examples in source.

### G-10. Plan-pool entries don't fit specific subjects
**Severity:** P1 (factual mismatch in rendered assistant message).
**Reach:** Grades 2, 5, 6, 7, 8, 9, 10, 11, 12 (basically every grade).
**Pattern:** Plan pools combine general entries ("I write the form...") with specific ones ("I let the polymorphic dispatch pick", "I count each coin into the chest", "I expand the macro with macroexpand", "I write the interop form"). The specific entries fire on subjects where they don't apply, making the asst preface contradict the form.
**Fix:** tag plan-pool entries with `fits_tags` and tag examples; OR split plan_pool into per-subject sub-pools. The existing `SubjectExample.tags` field can drive both. Document as new pitfall #27.

### G-11. Subplot context misfit (grade-specific subplot extensions over-applied)
**Severity:** P1 (semantic mismatch).
**Reach:** Most grades.
**Pattern:** Grade-flavored subplots target a subset of the grade's subjects but fire on all of them. Examples:
- G5 "compounding" / "same trick repeated cleverly" subplots → don't fit `if/when/cond/case/not`
- G7 error-handling subplots ("ready to catch whatever the REPL might throw") → don't fit edn-read, JSON, line-seq
- G7 IO subplots ("Beyond the REPL the world had files...") → don't fit pure-value subjects
- G8 "different birds different yields" → doesn't fit non-dispatch subjects (defrecord field access, two-protocol independence)
- G9 "coin-counter at the chest" / "ordered update" → contradicts immutability-review, CAS-no-fire, pure deref, future, promise, locking
- G10 "ledger-DSL" macro subplots → don't fit non-macro examples
- G11 "foreign market / phrasebook" → don't fit `(+ 1 2)` checked-math example
- G12 banquet/season-finale → fires every record; should be ≤1-2 per grade
- G12 placeholder forms get treated as "puzzles to evaluate" by race-pause subplot
**Fix:** add `fits_tags` to grade-flavored subplots and tag relevant examples in each grade's source file. Document as new pitfall #26.

### G-12. "Submit {concept_phrase} to the REPL" with abstract/clausal noun-phrase
**Severity:** P1 (verb/noun mismatch — you submit a *form*, not an English description).
**Reach:** Grades 7, 8, 10, 11, 12.
**Pattern:** Race-pause subplot says "Submit {concept_phrase} to the REPL" but concept_phrase is "where Leiningen finds project.clj", "what go blocks give you", "two key cljs-js interop conventions", "a defprotocol Pace with a single method speed", etc. Reader can't submit a description.
**Fix:** change race-pause subplot template (`goose_eggs/grade_1.py:_SHARED_SUBPLOTS` subplot 5) to "Submit `{form_display}` to the REPL — it shows {concept_phrase}." Or: "Submit the form to the REPL, then read what it reports for {concept_phrase}."

### G-13. "pointed to {concept_phrase}" / "read aloud {concept_phrase}" with abstract noun
**Severity:** P1 (semantic mismatch).
**Reach:** Grades 1, 6, 8, 10, 11, 12 (subplot 6 / variants).
**Pattern:** "pointed to **the equality of two :egg keywords**" (G1), "read aloud **whether two calls to the same fully-qualified function agree**" (G6), "read out **the :deps key from a small deps-map literal**" (G6). You point at / read forms; you don't point at abstract types.
**Fix:** rewrite these subplots to "pointed to the form `{form_display}`" so the gesture targets a written form. Mirrors the G1 pitfall #7 fix that handled subplot 4 but missed subplot 6.

### G-14. Singular-they ambiguity surviving in subplots beyond #5
**Severity:** P1 (ambiguity after singular setup; pitfall #19 only fixed subplot 5).
**Reach:** Grades 3, 6, 8, 9, 10, 11, 12.
**Pattern:** Subplots 3 (teacher), 6 (ledger), 7 (boast-and-rebuke), 11 (market-trip ledger) and grade-flavored extensions still use `{X_he_she}`/`{X_he_she_cap}` for the second sentence's pronoun. With `gender="n"` characters, this renders as "Robin had been trying to teach Sam… **they said**" or "Casey had been keeping a small leather ledger… **they** had successfully evaluated".
**Fix:** systematically replace second-sentence pronouns with the character's name where the subject is singular. Apply to subplot 3, 6, 11 in `_SHARED_SUBPLOTS` and to grade-flavored subplots in grades 6, 9, 10, 11, 12.

## Single-grade families

### G-15. Form-form duplication still surviving (pitfall #11)
**Severity:** P1.
**Reach:** Grades 4, 6, 7, 10, 11.
**Pattern:** concept_phrase = "the form (X)" placed near `{form_display}` = `` `(X)` ``, producing "scratched the form (conj [] :hare) into a smooth slate" then "submit the form `(conj [] :hare)` to the REPL".
**Fix:** rewrite affected concept_phrases to semantic noun-phrases ("the appended vector", "the assoc result", "the dissoc result").

### G-16. Concept_phrase reads as math/equation (pitfall #20)
**Severity:** P1.
**Reach:** Grade 2.
**Pattern:** G2-08 ex0/1/2: `"the sum 1/2 + 1/4"`, `"the product 2/3 × 3/4"`, `"1 minus 1/3"`. G2-01 ex3/4: `"the sum 1+2+...+10"`, `"the product 1*2*3*4*5"`. Reads as math, not Clojure form.
**Fix:** in `goose_eggs/grade_2.py`, rewrite to "the form (+ 1/2 1/4)", "the form (- 1 1/3)", etc.

### G-17. Question_what with internal commas / clauses
**Severity:** P1 (parses as run-on).
**Reach:** Grades 2, 3, 6, 7.
**Pattern:** `"the result of (- x y) when x=5, y=3"` (G3-04), `"the value of (+ a b) given a=1 b=(+ a 1)"` (G6-09 — math notation), `"a fn whose body has multiple forms; only the last is returned"` (G3-13). Wrapped in question template, the trailing comma-clauses derail the sentence.
**Fix:** simplify question_whats to drop trailing clauses.

### G-18. Cliché repetitions
**Severity:** P2 (cosmetic).
**Reach:** All grades.
**Pattern:** "the way the goose laid one egg at a time" verbatim across many records; "no more, no less"; "untroubled by what others thought"; "by sky-gazing"; "kitchen kindling"; "egg-count was settled by going to the basket".
**Fix:** split each closing analogy into 3-4 variants in the relevant subplot's tail.

## ⚠️ Accepted-with-justification

### A-1. EMO_GREEDY non-fit on protocol/macro/interop subjects (G8, G10, G11)
"with hands itching to count more" / "tempted by the thought of plenty" applied to a character reading a parchment about Pace dispatch reads odd — there's no plenty to be tempted by. **Accepted** because the goose-eggs moral lens *does* attribute greed-as-haste to the impatient guesser regardless of subject; the reader should infer "greed = wanting the answer immediately". Tagging would over-narrow the corpus.

### A-2. Tortoise-hare residue in shared EMO_PROUD ("swaggering through the underbrush", "as if the race were already won")
**Reach:** All grades.
**Status:** Could replace with goose-eggs-flavored EMO_PROUD pool, but the project ships 10 fables via the same `fables.py` EMO pools. Cross-fable consistency vs. per-fable flavor is a project-level call. **Accepted as cross-fable** for now; flag for project-level discussion.

### A-3. Cross-record cliché concentration (e.g., "untroubled by what others thought" 12+ times in G4)
**Status:** EMO pool selection is uniform-random; concentration at small N (like the 5-record per subject sample) reflects sampling variance more than systematic bias. At full n=222 generation the empirical distribution smooths out. **Accepted** with note: if a downstream eval shows the model echoing one EMO line, expand the pool.

### A-4. String-form quote density ("Submit the count of \"hare\" to the REPL")
**Status:** Same accepted finding as G1 paper cut #11. Inherent to string forms; reader can disambiguate. Not changed.

### A-5. Banquet/finale subplot frequency in G12
**Status:** A real cliché-frequency issue but G12 is "real-world Clojure" / retrospective by design. Down-weighting templates is a tuning decision, not a correctness one. **Accepted** with note for a future tuning pass.
