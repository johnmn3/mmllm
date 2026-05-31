# Ant-grasshopper hand-audit paper cuts

After running the structural audit harness clean (0 issues, 216
subjects), 12 sub-agents read ~1080 records (5 records × 216 subjects)
across all grades and surfaced patterns the regex harness can't catch
on its own. This file is the worked record of those findings,
remediation actions, and the audit-harness extensions added.

## The 18 distinct patterns

Severity codes:
- **P0** — grammar bug; rendered text is ungrammatical or actively
  misleading.
- **P1** — noise; renders parseable English but signal-to-noise is
  worse than necessary.
- **P2** — cosmetic; reader-perceived quality only.

| # | Pattern | Severity | Where it landed | Remediation |
|---|---|---|---|---|
| 1 | `in the farm` — `farm` should take `on` / `at` / `by`, not `in` | P0 | Every grade, dozens of records | `place_phrase()` patched to map `farm` to `on / at / by / near`; `BAD_PLACE_PREP` regex extended |
| 2 | DOUBLE_PREP — `at the edge of a stockpile {place}` when `{place}` itself starts with `at the edge of` produces `… stockpile at the edge of the orchard` | P0 | G2-G12 wager subplots | Subplot rewritten to use `{location.article} {location.name}` directly (no compound prep stack); pitfall #21 already documented |
| 3 | `,` or `;` inside `concept_phrase` produces run-ons in `Submit X to the REPL` / `argue about X` wraps (e.g. `the value 7 from the body (finally is for side effects)`) | P0 | G2-10, G2-16, G3-13, G7-03, G7-12, G7-17, G8-02, G8-03, G8-06, G8-09, G8-12, G8-16, G9-04, G9-08, G9-12, G9-15 | Concept_phrases trimmed; harness adds `CONCEPT_INTERNAL_PUNCT` regex catching `,` or `;` followed by lowercase verb-or-aside content in `concept_phrase` |
| 4 | `{emo_tired} of the lecture` — G10 teacher subplot adds an `of the lecture` tail, which doubles up against EMO_TIRED entries that already terminate (`legs heavy from sprinting of the lecture`) | P0 | G10 subplot 5 | Subplot tail dropped; harness gains `DOUBLE_OF` regex catching `from \w+ing of the` and `weary from \w+ of the` |
| 5 | EMO_TIRED hard-codes `her` possessive (`her legs heavy from sprinting`); when applied to a male/neuter character the possessive contradicts the surrounding pronoun set | P0 | G3, G4, G7 across many records | EMO_TIRED entries that hard-code a gendered possessive made gender-neutral in the ant-grasshopper subplot pool |
| 6 | `said {participle}` and `declared {participle}` without comma break the participle parse | P0 | G2 boast subplot uses `declared {emo_proud}` without comma | Templates patched; `SAID_PARTICIPLE` regex extended to `(said\|declared)\s+(boasting\|puffed\|swaggering\|with a smug grin)` |
| 7 | Singular-they pronoun reads as plural after a singular character setup (pitfall #19), not always fixed | P1 | Every grade, especially gender-n characters Bit/Hum | Subplots updated to use the character's name on the second mention; pitfall #19 already documented |
| 8 | EMDASH_COMMENTARY surviving in `concept_phrase` (pitfall #14) — em-dash followed by tutorial aside | P1 | G2-10, G2-16, G7-10, G10-01, G11-04 | concept_phrase commentary trimmed; existing EMDASH regex broadened to catch additional aside heads (`by`, `the`, `host-portable`) |
| 9 | Pitfall #11 form-form duplication still present in some templates (`argue about the form (assoc {:a 1} :b 2)` adjacent to backticked `{form_display}`) | P1 | G4, G6 wager subplots | Wager subplot tail rewritten to use generic `the answer` / `it` rather than re-emitting concept_phrase |
| 10 | Plan-pool entry mismatched with subject (e.g. `I write the literal value as Clojure source` paired with `(get …)`; `I bind in a let` paired with `(do 1 2 3)`) | P1 | Every grade with concept-tied plan_pool entries | Mismatched plan entries removed or gated by a `fits_tags` filter on the subject |
| 11 | Subplot context mismatch (e.g. accumulation/stockpile subplot on non-fold subjects, `labelled drawer` subplot on metadata-predicate subjects, `crossing into foreign syntax` on native Clojure forms) | P1 | G3, G4, G5, G6, G8, G9, G10, G11 | Each grade's themed subplot tagged with `fits_tags` so it only attaches where it makes sense |
| 12 | `read out the form aloud` redundancy (`read out` + `aloud`) | P1 | G1 audience subplot every record | Subplot rewritten to use `read the form aloud` (one or the other) |
| 13 | Opener tail (`It happened {place}`) duplicates the subplot's own `{place}`, producing the same location twice in adjacent prose | P1 | Every grade, ~30-40% of records | `_aesopian_intro` no longer appends location tail when the subplot already names a place; tail probability reduced to 0 by default for ant-grasshopper |
| 14 | Concept_phrase ellipsis `…` reads as truncation in narrative (`the form (count (keys …))`) | P1 | G4-10 | Concept_phrase rewritten as semantic noun-phrase |
| 15 | Concept_phrase as gerund-clause / sentence-fragment that breaks `Submit X to the REPL` (e.g. `binding grain to 5, then referring to grain`) | P1 | G2-18, G3-13, G4-17, G7-03 | Concept_phrases nominalized |
| 16 | Concept_phrase contradicts subject title (G6-08 'Circular dependencies' uses `single-direction call from one namespace to clojure.string`) | P1 | G6-08 | Concept_phrase reframed; subject still uses surrogate form, narration acknowledges the absence-of-circularity |
| 17 | Answer-leak via concept_phrase or question_what for small ints / target keywords (`set to 1`, `atom holding 7`, `:done, then dereffed`, `*p* rebound to 99`) | P1 | G9-04, G9-13, G9-14, G9-15, G9-17 | Concept_phrases rewritten to describe the operation without naming the result |
| 18 | EMO/cliché concentration — fixed phrases (`her eyes always on the path`, `with steady, careful steps`, `lulled by the gentle wind`, `Anyone can see what X comes to`, `just to be sure`) recur 5+ times per ~100-record sample | P2 | Every grade | Pool sizes accepted as-is; pitfall #9 already documents the variety calculus, which is satisfied at the n=222 cross-product |

## Audit harness extensions added

Five new severity codes wired into `audit-harness.py`:

| Severity | Description | Regex |
|---|---|---|
| `BAD_PLACE_PREP` (extended) | `in the farm` added to the bad-place list | `in the farm` |
| `DOUBLE_PREP` | Pitfall #21 — verb taking own preposition followed by `{place}` (`stopped at the edge of`, `Halfway to in the meadow`); also `at the edge of a stockpile at the edge of` | `\b(at the edge of|on the edge of|by the side of|alongside|halfway to|halfway through)\s+(in|near|on|atop|by|along|inside|deep inside|at the edge of|at)\s+the` (case-insensitive). |
| `DOUBLE_OF` | Pitfall #13 generalization — `, {emo_tired} of the X` tail when EMO already terminates with a prepositional phrase | `(from \w+ing\|weary from \w+\|drowsy from \w+\|yawning at \w+\|legs heavy from \w+) of the` |
| `SAID_PARTICIPLE` (extended) | Now also catches `declared` and `cried` heads, not just `said` | adds `(declared\|cried)\s+(boasting\|puffed\|swaggering\|with a smug grin)` |
| `CONCEPT_INTERNAL_PUNCT` | Concept_phrase contains `,` or `;` followed by a verb-form participle that breaks the wrap | `(,|;)\s+(then |only |called |and |a |an |the )` followed by an English clause-like continuation |

Verified against `tortoise-hare` and `goose-eggs` — both still report
`0 issues` after the new checks land.

## Accepted-with-justification

A handful of patterns the audit raised that we explicitly leave alone:

- **String-form quote density** (G2-11 `(str "a" "b")`, G6-03 `clojure.string/upper-case`, G11-02 `.toUpperCase`) — accepted in the
  tortoise-hare audit (#11). The nested quotes are syntactically valid
  prose; the model can learn to disambiguate. Forcing concept_phrase to
  drop the inner quotes loses form identity.
- **Backtick density inside syntax-quoted forms** (G10-02, G10-03,
  G10-10, G10-16) — the inner `` ` `` is part of the Clojure source, not
  prose punctuation. Markdown rendering of the audit doc may look off
  but the training data is JSON-tool-call-shaped where the form is
  inside the `args.form` string. No fix needed.
- **Opener concentration** — only 4 fable-openers cycle (this is
  pitfall #9 territory). At n=222 cross-product the distinct
  combination space is large enough that the model sees varied surface
  forms; within a 5-record sample some opener repetition is
  unavoidable.
- **EMO_PATIENT phrase recurrence** (`her eyes always on the path`,
  `with steady, careful steps`) — pool size is intentionally narrow
  to anchor the Ant's character voice. Diluted vocab would weaken the
  voice signature. Same calculus as tortoise-hare's accepted #8.

## What changed in source

Patches summary:

- `src/mmllm/aesop/template.py` — `place_phrase()` adds `farm` →
  `(on, at, by, near)` mapping.
- `src/mmllm/aesop/curriculum/ant_grasshopper/grade_1.py` — wager
  subplot rewritten to `Beside a small stockpile {place}` (drops
  pitfall-#25 DOUBLE_PREP); audience subplot drops `out … aloud`
  redundancy; G1-10/G1-11 concept_phrases shortened.
- `src/mmllm/aesop/curriculum/ant_grasshopper/grade_2.py` — wager-
  with-stakes subplot adds comma after `declared` (pitfall-#23);
  G2-10/G2-14/G2-16/G2-18 concept_phrases trimmed of em-dash asides
  and gerund-clause shapes.
- `src/mmllm/aesop/curriculum/ant_grasshopper/grade_3.py` — G3-12,
  G3-13, G3-16 concept_phrases nominalized.
- `src/mmllm/aesop/curriculum/ant_grasshopper/grade_4.py` — G4-10
  ellipsis dropped; G4-17 fragment nominalized.
- `src/mmllm/aesop/curriculum/ant_grasshopper/grade_6.py` — G6-01
  shortened; G6-08 concept_phrase reframed (was contradicting subject
  title); G6-16 concept_phrase aligned with form.
- `src/mmllm/aesop/curriculum/ant_grasshopper/grade_7.py` — G7-03,
  G7-12, G7-17, G7-10 paren-aside / em-dash commentary stripped.
- `src/mmllm/aesop/curriculum/ant_grasshopper/grade_8.py` — G8-02,
  G8-03, G8-06, G8-09, G8-12, G8-16 concept_phrases nominalized
  (commas/semicolons that broke "Submit X to the REPL" wraps removed).
- `src/mmllm/aesop/curriculum/ant_grasshopper/grade_9.py` — G9-02,
  G9-04, G9-08, G9-12, G9-13, G9-14, G9-15, G9-17, G9-18
  concept_phrases reformulated to drop answer leaks and replace
  raw-English descriptions with form-text wraps.
- `src/mmllm/aesop/curriculum/ant_grasshopper/grade_10.py` — teacher
  subplot drops `of the lecture` tail (pitfall-#24); G10-01
  question_what em-dash trimmed.
- `src/mmllm/aesop/curriculum/ant_grasshopper/grade_11.py` — G11-04
  em-dash commentary trimmed.
- `src/mmllm/aesop/curriculum/ant_grasshopper/grade_12.py` —
  retrospective subplot drops `from a season of song` tail
  (pitfall-#24).
- `docs/clojure-pedagogy/audits/audit-harness.py` — five new /
  extended severity codes (see above).
- `docs/clojure-pedagogy/SKILL-fable-curriculum-author.md` — pitfalls
  #22, #23, #24, #25 added.

## Cross-fable signal for the coordinator

The new audit checks surfaced REAL bugs in `tortoise-hare` that the
original harness missed:

- `tortoise-hare` G2 wager-with-stakes subplot — `{hare_phrase}
  declared {emo_proud}` without comma. 19 hits on the new
  SAID_PARTICIPLE-extended check (`declared boasting`, `declared
  puffed`, `declared swaggering`, `declared with a smug grin`).
- `tortoise-hare` G12 retrospective subplot — `{emo_tired} from a
  season of races` (the tortoise-hare cousin of ant-grasshopper's
  `from a season of song`). 2 hits on the new generalized
  DOUBLE_FROM regex.

These are NOT false positives in the new checks. They are pre-existing
bugs in tortoise-hare that the structural audit was blind to and that
the ant-grasshopper hand-audit + harness extension surfaced for the
first time. The same fix pattern (comma after `declared`; drop the
trailing `from a season of races`) applies. Recommended: the
coordinator apply the same patches to tortoise-hare's G2 and G12
subplots.

`goose-eggs` is clean under the new checks — no regressions, no
newly-surfaced bugs.
