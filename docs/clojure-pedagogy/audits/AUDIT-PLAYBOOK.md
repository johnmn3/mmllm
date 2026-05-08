# Deep-audit playbook — K-12 Clojure curriculum × 5 fables

Scope: each Phase-C-complete fable (`tortoise_hare`, `crow_pitcher`,
`milkmaid`, `boy_wolf`, `dog_shadow`) gets one or more independent
deep-read passes. Each agent picks ONE fable and a random 6 of the
12 grades — that's the working slice.

The agent's job is to **read records, find papercuts the existing
audit harness can't catch, extend the harness with new detectors, and
fix the underlying templates / pools** — then push and report.

This playbook is the agent-facing instruction manual. Read it
end-to-end before starting; you can knock out the slice solo.

---

## 0. Setup (one-time per agent)

Pick your slice:

  1. Choose ONE fable (tortoise_hare, crow_pitcher, milkmaid,
     boy_wolf, or dog_shadow).
  2. Pick a random 6 of the 12 grades.
  3. Designate a working branch:

```
claude/audit-<fable-dash>-<short-tag>     # e.g. claude/audit-milkmaid-rN0v
```

```bash
git fetch origin claude/analyze-repo-status-rN0vt
git checkout -b claude/audit-<fable-dash>-<short-tag> \
    origin/claude/analyze-repo-status-rN0vt
```

`claude/analyze-repo-status-rN0vt` is the integration branch for
the parametric system + new pools + bb verifier + this playbook.
It has not yet been merged to `main`, so you must base from this
branch directly.

If the branch already exists, rebase onto current integration:

```bash
git fetch origin claude/analyze-repo-status-rN0vt
git rebase origin/claude/analyze-repo-status-rN0vt
```

Verify the toolchain works:

```bash
python -m mmllm.aesop.curriculum.scalar_pools           # 29 pools ok
python -m mmllm.aesop.curriculum.form_parser            # 27/27 ok
python -m mmllm.aesop.curriculum.form_families          # 82 families × 5 ok
python -m mmllm.aesop.curriculum.auto_parametric        # 6 forms ok
python -m mmllm.aesop.curriculum.character_pools        # 1,824 names ok
python -m mmllm.aesop.curriculum.opener_pools           # 150 openers / 150 plans ok
python -m mmllm.aesop.curriculum.emotion_pools          # 199 band / 396 archetype ok
python scripts/test_parametric_e2e.py                   # 50/50 verified
FABLE=<your-fable> python docs/clojure-pedagogy/audits/audit-harness.py
```

If any smoke test or audit fails on `main`, DO NOT proceed. Pull
down the latest, retry, and report the breakage in your final
summary.

---

## 1. Generate a deep-read sample (Step 1 of the workflow)

For each of your 6 sampled grades, generate **5 records per
example** for every subject. Code:

```python
# scripts/deep_read_<fable>_<short-tag>.py
import sys; sys.path.insert(0, "/home/user/mmllm/src")
import importlib
from mmllm.aesop.curriculum.generator import generate_subject

FABLE  = "<your-fable>"          # e.g. "milkmaid"
GRADES = [<your six grades>]     # e.g. [1, 3, 5, 7, 10, 12]
N = 5
out = []
for g in GRADES:
    mod = importlib.import_module(
        f"mmllm.aesop.curriculum.{FABLE}.grade_{g}")
    for sid, sub in mod.SUBJECTS.items():
        seed_base = int(sid[3:].replace("-", "")) * 7
        recs = generate_subject(sub, n_per_example=N, seed=seed_base)
        for r in recs:
            out.append((sid, r))

with open(f"/tmp/deep_read_{FABLE}.txt", "w") as f:
    for sid, r in out:
        f.write(f"--- {sid} | form={r.code_str} | expected={r.expected!r}\n")
        f.write(r.user_msg.rstrip() + "\n\n")
        f.write("---\n\n")
print(f"wrote {len(out)} records")
```

Run it. Output: ~500-700 records across your 6 grades.

**Read every record.** Don't skim. Every prose line is potentially a
papercut. Take notes as you go in `/tmp/papercuts.md`.

---

## 2. Categorize papercuts (Step 2 — the heart of the audit)

For each issue you find, capture:

```
- [<CATEGORY>] <fable>/<sid>#<example_idx> "<offending excerpt>"
  • why it's wrong: <one sentence>
  • where it lives: <file:line>  (the subplot template, the EMO pool, the
    {concept_phrase} string, etc. — pinpoint the source, not the rendered output)
  • fix sketch:    <one sentence>
```

Look for these **9 papercut categories**. The first 5 cover the
familiar surface; the last 4 are the new push the user asked for —
emotion/adjective grounding mapped to algorithmic situation.

### Cat-A — Logical errors

- Form's claimed answer is wrong (e.g. `(quot 10 3) → 4` instead of `3`).
- `expected_fn(draws)` disagrees with what the evaluator actually
  computes — the parametric verifier should already catch these, so
  any survivor here is a verifier-skip case worth flagging.
- Drawn-value collisions (e.g. `(- {a} {b})` produces a negative
  result that the prose calls "the difference of three from seven" —
  which evaluates to 4, not -4).
- `if`/`when`/`cond` branch the prose claims, but the runtime takes
  the other branch.

### Cat-B — Syntax errors (Clojure-side)

- Form has unbalanced parens (rare, but possible with template
  drift).
- Quotes inside strings unescaped (e.g. `(str "she said "hi"")`).
- Dict/vector literals with stray commas or missing closes.
- `:keyword` rendered as `":keyword"` (string with a colon prefix,
  not a true keyword).

### Cat-C — Grammatical errors (English prose)

- Pronoun mismatches (`Whisker, her eyes always on the path` for a
  male character).
- Verb-pronoun disagreement on singular-they (`they runs`, `they
  is`).
- Tense slips (`she said it would be simpler ... and decides`).
- Article errors (`a apple`, `an honor` — when "honor" begins with
  a vowel sound).
- Comma splices, run-ons, missing serial-comma where one is needed
  for clarity.
- Hyphenation: `step by step` vs. `step-by-step`, `well known` vs.
  `well-known`.

### Cat-D — Spelling errors

- Misspellings in subplot templates, EMO pools, openers, plan
  prefaces, and authored prose slots (`scenario`, `need`,
  `mapping`, `resolution`).
- Common British/American mismatches if the corpus is meant to be
  consistent (`colour` vs. `color`, `realise` vs. `realize`).
- Character names misspelled relative to the canonical pool entry.

### Cat-E — Semantic errors

- Concept-phrase doesn't actually describe the form (e.g. concept
  says "the maximum of three integers" but the form is `(min ...)`).
- Goal-text and concept-phrase contradict each other.
- Numeric prose says "five acorns" but the form drew `7`. (The
  parametric `{drawn.X}` interpolation should prevent this; any
  surviving instance is a missed substitution worth fixing.)
- Mathematical claims that are wrong even before evaluation
  ("multiplying two negatives gives a negative").

### Cat-F — Narrative errors (plot doesn't hang together)

- Setup mentions a character who never appears in the action.
- Scenario establishes a constraint (e.g. "Mira had no scroll yet")
  that the resolution silently contradicts.
- The metaphor's container/object disappears between scenario and
  resolution (e.g. "Mossback set down a basket" — basket never
  reappears).
- The character with the patient role (tortoise/crow/farmer/elder/
  hound) ends up doing the impatient thing, or vice-versa — polarity
  flip.
- The `{drawn.X}` value is mentioned in scenario but the resolution
  computes a different number's worth of consequences.

### Cat-G — Emotional inconsistencies

- A grade-1 atom subject draws a `EMO_PH` ("alternating between
  possibility and verification") complexity-band emotion — way too
  heavy.
- A grade-12 transducer subject draws `EMO_P_EASY` ("calmly, as one
  notices the colour of the sky") — way too light.
- Polarity mismatch: the patient/evaluator role gets a `BOASTFUL`
  emotion, or the dreamer/guesser gets a `CAUTIOUS` one.
- Two-sentence emotional whiplash within a single record (character
  `EMO_DESPERATE` in sentence 2, `EMO_CONTENT` in sentence 3, with
  no narrative pivot).

### Cat-H — Plot-coherence breakdown

- Three or more sentences in a row that each restate the same beat
  with different metaphors. Reader can't tell what's happening
  *next* vs. *just happened*.
- Scenario / need / mapping / resolution slots compose into prose
  whose subject, location, or item changes silently between slots
  ("the basket" → "the pail" → "the basket again").
- The closing question-what doesn't match the resolution slot's
  framing — the question asks for X, the resolution implied Y.

### Cat-I — Distractions that confuse the plot

- Aside parens for pedagogical commentary that the audit harness
  already partially flags via `ASIDE_PAREN`. Look for cases the
  existing regex misses (new aside patterns the user wouldn't
  expect from a children's story).
- Explanatory clauses ("which is to say", "or rather", "that is, the
  same thing") that fragment the metaphor.
- Footnote-like backreferences ("as we saw earlier", "from the
  previous example") — there is no "previous example" at training
  time; each record stands alone.
- Dialogue tags that announce instead of dramatize ("she said
  reluctantly, knowing the answer was already plain to anyone who
  had been paying attention").

---

## 3. Push prose toward emotion/adjective grounding (the *positive* lift)

The user's directive: prose must convey character emotions and
environmental adjectives, **mapping** those onto the algorithmic
situation. This is the affirmative half of the audit — not just
finding bugs but pushing the corpus *toward* better grounding.

For every record you read, ask:

1. **Does the character's emotion match the cognitive load of the
   form?** A 3-line `(reduce ...)` over a long collection should
   feel "methodically stepping through, one tally at a time." A
   1-line `(+ 2 3)` should feel "calm, the answer plain."

2. **Is there a physical adjective that maps the environment to the
   data?**  "The path was long enough to hold every coin she would
   carry in turn" (long ↔ collection, hold ↔ accumulator, in turn
   ↔ reduce-fold).  "The pitcher was narrow at the throat" (narrow ↔
   the bottleneck the algorithm has to work around).

3. **Does the resolution close the metaphor with a felt outcome?**
   Not "the REPL returns 25" but "Mossback's pile, weighed at last,
   counted twenty-five — exactly the sum she had set out to find."

If a record fails any of these, capture it as a Cat-J papercut:

### Cat-J — Insufficient emotion/adjective grounding

```
- [LOW_GROUNDING] <fable>/<sid>#<idx>
  • the prose names the operation but doesn't *feel* it
  • current: "<offending sentence>"
  • lift:    "<your suggested rewrite, 1-2 sentences>"
  • where to apply: SubplotTemplate at <file:line> /
                    EMO_<band> entry / scenario slot in <file>
```

Don't tweak every record by hand — capture the pattern, then **lift
the pattern at the source** (subplot template, EMO pool entry, or
scenario template). One source-level change can elevate hundreds of
records.

---

## 4. Build new detectors (Step 3 of the workflow)

For every papercut category that the existing harness can't catch,
add a new detector to `docs/clojure-pedagogy/audits/audit-harness.py`.

Existing detectors (don't duplicate):

```
LOW_LENGTH, HIGH_LENGTH, VERB_AGREEMENT, UNFILLED_PLACEHOLDER,
ANSWER_LEAK, ANSWER_LEAK_ASST, NESTED_COMPUTES, ASIDE_PAREN,
ASIDE_EXTENDED, ANSWER_LEAK_PHRASE, UNCLOSED_DIALOGUE_QUOTE,
WHO_PARTICIPLE, INSISTED_THEY, BAD_PLACE_PREP, FORM_LEAK,
ANSWER_LEAK_STRING, DOUBLE_PREP
```

A detector is a regex (or small AST/text walk) added inside
`check_record(rec, sub, example)` in `audit-harness.py`. Pattern:

```python
# <PAPERCUT_NAME> — <one-sentence explanation>
if re.search(r"<your-pattern>", user, flags=re.IGNORECASE):
    issues.append(("<NEW_CATEGORY>",
                   f"<short message — what was matched>"))
```

For category-J grounding, prefer a *coverage* detector rather than a
violation detector: count records whose `user_msg` contains at least
one EMO-pool phrase + at least one drawn-value reference, and flag
records that have NEITHER. Don't try to grade prose quality — just
verify the structural ingredients are present.

For Cat-G complexity-mismatch, you can write a new structural check:

```python
# EMO_BAND_MISMATCH — emotion-band picked doesn't match grade
from mmllm.aesop.curriculum.emotion_pools import EMO_BAND_FOR_GRADE
grade = int(sub.subject_id[1:].split("-")[0])
expected_band = EMO_BAND_FOR_GRADE[grade]
# Search user for any phrase from a *different* band that's clearly
# from a higher / lower complexity tier:
for other_band_name, other_band in (
    ("EMO_PH", EMO_PH), ("EMO_CO_NP", EMO_CO_NP), ("EMO_NP", EMO_NP),
    ("EMO_P_HARD", EMO_P_HARD), ("EMO_P_MEDIUM", EMO_P_MEDIUM),
    ("EMO_P_EASY", EMO_P_EASY),
):
    if other_band is expected_band: continue
    for phrase in other_band:
        if phrase in user:
            issues.append(("EMO_BAND_MISMATCH",
                           f"grade {grade} record uses {other_band_name}: "
                           f"{phrase[:40]!r}"))
            break
```

Add ≥3 new detectors per band you cover. More is fine. Each detector
should:

- Have a clear category name (UPPER_SNAKE_CASE).
- Match patterns you actually saw in your read-corpus (not
  speculative).
- Produce a one-line message describing what was matched.

---

## 5. Build fixes (Step 4)

For each papercut, the fix lives at one of:

1. **Subplot template** — `mmllm/aesop/curriculum/<fable>/_metaphor_pools.py`
   or per-grade `_metaphor_pools.py` extensions. Fix the template
   string in place.

2. **EMO pool entry** — `mmllm/aesop/curriculum/emotion_pools.py`.
   Replace the offending phrase with a corrected variant. If you
   delete an entry to fix a bug, add a *better* replacement so the
   pool stays ≥30 entries.

3. **Opener / plan pool** — `mmllm/aesop/curriculum/opener_pools.py`.
   Same constraint: ≥30 per pool, no duplicates.

4. **Authored scenario / need / mapping / resolution slot** —
   per-grade `<fable>/grade_<n>.py`. Edit the string literal directly.

5. **`concept_phrase` / `question_what` / `goal_text`** — per-example
   in the same per-grade file. Most of these now auto-interpolate
   `{drawn.X}` thanks to the migration; if you find a stale literal
   number that should be a slot reference, fix it manually.

6. **Pool inference / scalar pool** — `mmllm/aesop/curriculum/scalar_pools.py`
   or `auto_parametric.py`. If the pool inference is mis-typing a
   slot (e.g. a keyword list ending up as INT_SMALL), tighten the
   inference rule.

After every fix, **re-run the full audit** for your fable and confirm
your detector count drops. If it doesn't, the fix didn't land —
investigate.

```bash
FABLE=<fable> python docs/clojure-pedagogy/audits/audit-harness.py
```

---

## 6. Sync with the integration branch, retest, push (Step 5)

```bash
git fetch origin claude/analyze-repo-status-rN0vt
git rebase origin/claude/analyze-repo-status-rN0vt
```

If there are conflicts, resolve them carefully — your fixes should
NOT clobber another agent's pool/template additions. Both sets of
changes typically merge cleanly because they edit different lines.

Re-run smoke tests + the audit harness:

```bash
python -m mmllm.aesop.curriculum.scalar_pools
python -m mmllm.aesop.curriculum.form_parser
python -m mmllm.aesop.curriculum.form_families
python -m mmllm.aesop.curriculum.auto_parametric
python -m mmllm.aesop.curriculum.character_pools
python -m mmllm.aesop.curriculum.opener_pools
python -m mmllm.aesop.curriculum.emotion_pools
python scripts/test_parametric_e2e.py
FABLE=<fable> python docs/clojure-pedagogy/audits/audit-harness.py
```

All must pass. If a test now fails because of your changes, revert
the offending edit and re-think the fix.

Push:

```bash
git push -u origin claude/audit-<fable>-<grade-band>
```

If push fails on network errors, retry with backoff (2s, 4s, 8s, 16s).
Do NOT force-push.

---

## 7. Report (Step 6 — the deliverable)

Write a single markdown file at:

```
docs/clojure-pedagogy/audits/deep-audit-<fable-dash>-<short-tag>.md
```

with this structure:

```
# Deep audit — <fable> (grades: <list>)

Read <N> records (~5/example × <S> subjects × 6 grades). Total
papercuts: <T>, of which <T_fixed> fixed in this branch.

## Papercuts found (raw, before fixes)

<grouped by category, link to file:line for each>

## Detectors added to audit-harness.py

<list each new detector by category, with the regex>

## Fixes applied

<bulleted list of file:line edits, grouped by source>

## Numbers before/after

| Detector            | Before | After |
|---------------------|--------|-------|
| HIGH_LENGTH         | 12     | 8     |
| EMO_BAND_MISMATCH   | new: 23 | 0   |
| ...                 | ...    | ...   |

## Branch

claude/audit-<fable-dash>-<short-tag> at <commit-sha>

## Caveats / open work

<anything you saw but couldn't fix in scope>
```

Then in your final agent message, post a 6-12 line summary covering:

- branch name + commit count
- papercuts found / fixed
- new detectors added
- audit before/after issue count
- any blockers (e.g. "G7-09 has 14 host-interop forms that need bb
  pre-flight, not in this scope")

---

## Reference: locations the agent will most often touch

```
src/mmllm/aesop/curriculum/<fable>/grade_<N>.py                  per-example prose, story slots
src/mmllm/aesop/curriculum/<fable>/_metaphor_pools.py            subplot templates, fable-specific
src/mmllm/aesop/curriculum/emotion_pools.py                      EMO_<BAND> + EMO_<archetype>
src/mmllm/aesop/curriculum/opener_pools.py                       OPENERS_<FABLE>, PLANS_<FABLE>
src/mmllm/aesop/curriculum/character_pools.py                    HUMAN_F/M, animal pools
src/mmllm/aesop/curriculum/scalar_pools.py                       INT_*, KW_*, COLL_*, etc.
src/mmllm/aesop/curriculum/auto_parametric.py                    pool inference rules
src/mmllm/aesop/curriculum/generator.py                          render pipeline
src/mmllm/aesop/curriculum/form_families.py                      parametric form factories
docs/clojure-pedagogy/audits/audit-harness.py                    detectors live here
```

## Reference: dispatch model

Each agent picks ONE fable and a random 6 of the 12 grades. Each
agent's branch starts from `claude/analyze-repo-status-rN0vt` (the
parametric integration branch — not yet on `main`). Multiple
agents can audit the same fable on different random samples;
overlapping findings are expected and useful (the user dedups
when collating).

Branch naming: `claude/audit-<fable-dash>-<short-tag>` where
`<short-tag>` is a 4-character random suffix to keep multiple
runs on the same fable from colliding.

## Reference: detector coverage targets

After several waves of agents, the audit harness should grow from
the current ~25 detectors to ≥50. Each fable's audit issue count
should drop from 15-53 to ≤10. The prose-grounding detector
(Cat-J) should report ≥85% coverage — i.e., ≥85% of records have
at least one drawn-value mention AND at least one EMO-band phrase
AND at least one environmental adjective mapped to the algorithmic
situation.
