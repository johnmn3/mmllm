# Agent prompt — deep-audit dispatch

Copy the prompt below, fill in `<FABLE>` and `<GRADE_BAND>`, dispatch
to a haiku or sonnet agent. The agent reads `AUDIT-PLAYBOOK.md` for
the detailed methodology; this prompt is the wrapper.

Each invocation is independent — the agent does not need context from
other audit slices.

---

## The prompt

```
You are running a deep-audit slice for the K-12 Clojure curriculum
in the mmllm repo. Your slice is:

  fable:       <FABLE>           # one of: tortoise_hare, crow_pitcher, milkmaid, boy_wolf, dog_shadow
  grade-band:  <GRADE_BAND>      # one of: G1-G3, G4-G6, G7-G9, G10-G12
  branch:      claude/audit-<FABLE-DASH>-<BAND-LOWER>
                                 # e.g. claude/audit-tortoise-hare-g4-g6

The full playbook lives at:
  /home/user/mmllm/docs/clojure-pedagogy/audits/AUDIT-PLAYBOOK.md

Read the playbook end-to-end before starting. It explains:
  • the 9 papercut categories (logical / syntax / grammar / spelling /
    semantic / narrative / emotional / plot-coherence / distractions)
  • the 10th category J (insufficient emotion-and-adjective grounding —
    the affirmative lift, not just bug-finding)
  • how to extend audit-harness.py with new detectors
  • where each kind of fix lives (subplot template, EMO pool, opener
    pool, per-grade prose, scalar pool, auto-parametric inference)
  • the rebase/test/push/report cycle

Workflow (also detailed in the playbook):

  1. Check out branch claude/audit-<FABLE-DASH>-<BAND-LOWER> from
     latest main. Run all smoke tests + FABLE=<FABLE> python
     docs/clojure-pedagogy/audits/audit-harness.py to confirm the
     baseline is green.

  2. Generate ~80-110 records covering every example × 5 records
     across the grades in your band. Read every record. Take notes.

  3. Categorize each papercut into Cat-A through Cat-J. Pinpoint the
     SOURCE (file:line) for each, not just the rendered output.

  4. Add ≥3 new detectors to docs/clojure-pedagogy/audits/audit-harness.py
     covering papercut patterns the existing 25 detectors don't catch.
     Use clear UPPER_SNAKE_CASE category names; use simple regex or
     small text walks (not heavy parsing).

  5. Apply fixes at the source level — one source change typically
     elevates hundreds of records. Don't tweak per-record; tweak
     the template, EMO pool, or scenario string the records are
     generated from.

  6. After fixes, re-run the audit harness. The detectors you added
     in step 4 should now report 0 hits (or close to it). If they
     don't, the fix didn't land — investigate.

  7. Rebase your branch onto latest main:

       git fetch origin main && git rebase origin/main

     Re-run all smoke tests + the audit harness. Resolve conflicts
     carefully (typically additive merges work cleanly because each
     audit slice edits different lines).

  8. Push:

       git push -u origin claude/audit-<FABLE-DASH>-<BAND-LOWER>

     Retry up to 4 times with exponential backoff on network errors.
     Do NOT force-push.

  9. Write a deliverable doc at:

       docs/clojure-pedagogy/audits/deep-audit-<FABLE-DASH>-<BAND-LOWER>.md

     using the structure from the playbook (papercuts found,
     detectors added, fixes applied, before/after numbers, branch
     SHA, caveats).

  10. Report a 6-12 line summary in your final message: branch +
      commit count, papercuts found / fixed, new detectors, audit
      before/after, blockers.

Constraints:

  - Stay focused on your slice. Don't audit grades outside your band.
  - Don't audit other fables.
  - Don't refactor unrelated infrastructure.
  - Don't create planning / scratch / decision docs. The deliverable
    doc (deep-audit-<FABLE-DASH>-<BAND-LOWER>.md) is the only doc.
  - Don't add emojis to anything.
  - Don't break existing smoke tests. If a smoke test starts failing,
    revert the offending change and reconsider.
  - Don't push to main directly. Don't push to other agents' branches.
  - Don't run /ultrareview or attempt to dispatch other agents.

Affirmative push (from the user's directive):

  Beyond bug-finding, push the prose toward characters conveying
  emotions and adjectives about their environmental situation,
  mapped onto the algorithmic situation. A grade-1 atom should feel
  "calm, the answer plain"; a grade-12 transducer should feel
  "alternating between possibility and verification, weighing the
  search against the constraint." Capture violations as Cat-J
  papercuts; lift the pattern at the source (subplot template, EMO
  pool, scenario slot) so one fix elevates many records.

Pedagogical lens (don't lose this):

  Each fable carries a distinct moral. Tortoise-hare = vanity vs.
  steadiness. Crow-pitcher = patience vs. thirst. Milkmaid =
  daydream vs. care. Boy-wolf = trust vs. false alarm. Dog-shadow =
  greed loses what was had. Your fixes should preserve the fable's
  polarity — the patient/evaluator role does the careful thing; the
  dreamer/guesser role overreaches. If you find polarity flips,
  flag them as Cat-F (narrative) papercuts.

Definition of done:

  - Branch claude/audit-<FABLE-DASH>-<BAND-LOWER> pushed.
  - All smoke tests pass on that branch.
  - audit-harness.py FABLE=<FABLE> reports fewer issues after your
    work than before (track the deltas in your deliverable doc).
  - Deliverable doc committed under
    docs/clojure-pedagogy/audits/.
  - Summary message in your final reply.

Begin by reading the playbook, then running the baseline smoke tests
to confirm main is green. After that, generate your read-corpus and
start the deep read.
```

---

## Dispatch usage

Pick a model:

- **Haiku 4.5** — fastest, cheapest. Good for small bands (G1-G3,
  G10-G12 where the macro/host-interop work blocks deep reading
  anyway).
- **Sonnet 4.6** — best balance. Recommended default.
- **Opus 4.7** — for the trickiest bands or fables with the most
  papercuts (typically dog-shadow given the higher pre-existing
  issue count).

Run agents in parallel where their branches don't conflict. Two
agents on the same fable but different bands will mostly edit
different files (per-grade prose) and merge cleanly. Two agents
both editing `emotion_pools.py` or `opener_pools.py` may conflict —
serialize those, or have the second agent rebase before adding
their entries.

## Quick-start: 5 first agents

Recommended first wave (one band per fable, the highest-impact band
for each):

| fable          | band      | rationale |
|----------------|-----------|-----------|
| tortoise_hare  | G4-G6     | most-touched by parametric migration; high-yield |
| crow_pitcher   | G4-G6     | same — these are the HOFs / collections grades |
| milkmaid       | G7-G9     | highest pre-existing issue count band per audit |
| boy_wolf       | G1-G3     | atom-heavy; quickest payoff |
| dog_shadow     | G7-G9     | dog-shadow has the highest issue count overall |

After those land, dispatch the remaining 15 slices.

## Acceptance criteria across the full sweep (post-merge)

When all 20 slices are merged:

- audit-harness.py has ≥50 detectors (currently 25).
- per-fable audit issue count ≤ 10 (currently 15-53).
- Cat-J grounding-coverage detector reports ≥85% records have
  drawn-value mentions + EMO-band phrases + environmental adjectives
  tied to the algorithmic situation.
- All smoke tests pass.
- Showcase doc regenerates cleanly with the lifted prose visible.
