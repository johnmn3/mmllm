# Agent prompt — deep-audit dispatch

Copy the prompt below verbatim and dispatch to a haiku or sonnet
agent. No template fill-in needed — the agent picks its own fable
and grade sample.

Each invocation is independent — the agent does not need context
from other audit slices, only the playbook at
`docs/clojure-pedagogy/audits/AUDIT-PLAYBOOK.md`.

---

## The prompt

```
You are running a deep-audit slice for the K-12 Clojure curriculum
in the mmllm repo (5 Phase-C-complete fables: tortoise_hare,
crow_pitcher, milkmaid, boy_wolf, dog_shadow; 12 grades each).

Pick your slice yourself:

  1. Choose ONE fable from the five above.
  2. Pick a random 6 of the 12 grades (uniform sample; record which
     grades you picked at the top of your deliverable).
  3. Designate a working branch:

       claude/audit-<fable-dash>-<short-tag>

     where <short-tag> is a 4-character random suffix (e.g.
     "rN0v", "k7Pq"). This keeps multiple audit runs on the same
     fable from colliding.

The full playbook is at:
  /home/user/mmllm/docs/clojure-pedagogy/audits/AUDIT-PLAYBOOK.md

Read the playbook end-to-end before starting. It explains:
  • the 9 papercut categories (logical / syntax / grammar / spelling /
    semantic / narrative / emotional / plot-coherence / distractions)
  • the 10th category J (insufficient emotion-and-adjective grounding —
    the affirmative lift, not just bug-finding)
  • how to extend audit-harness.py with new detectors
  • where each kind of fix lives (subplot template, EMO pool, opener
    pool, per-grade prose, scalar pool, auto-parametric inference)
  • the rebase / test / push / report cycle

Workflow:

  1. Check out your branch from latest
     `claude/analyze-repo-status-rN0vt` (this is the integration
     branch carrying the parametric system, the new pools, the bb
     verifier, and this playbook itself; it has not yet been merged
     to main). Run all smoke tests + FABLE=<your-fable> python
     docs/clojure-pedagogy/audits/audit-harness.py to confirm the
     baseline is green.

  2. For each of the 6 grades you picked, generate ~5 records per
     example for every subject. ~80-120 records total per grade, so
     ~500-700 records across your slice. Read every record. Take
     notes in /tmp/papercuts.md as you go.

  3. Categorize each papercut into Cat-A through Cat-J. Pinpoint
     the SOURCE (file:line) for each, not just the rendered output.

  4. Add at least 3 new detectors to
     docs/clojure-pedagogy/audits/audit-harness.py covering papercut
     patterns the existing detectors don't catch. Use clear
     UPPER_SNAKE_CASE category names; use simple regex or small text
     walks (not heavy parsing).

  5. Apply fixes at the source level — one source change typically
     elevates hundreds of records. Don't tweak per-record; tweak the
     template, EMO pool, or scenario string the records are
     generated from.

  6. After fixes, re-run the audit harness. The detectors you added
     in step 4 should now report 0 hits (or close to it). Existing
     detectors should not regress. If either fails, the fix didn't
     land — investigate.

  7. Rebase your branch onto latest
     `claude/analyze-repo-status-rN0vt`:

       git fetch origin claude/analyze-repo-status-rN0vt
       git rebase origin/claude/analyze-repo-status-rN0vt

     Re-run all smoke tests + the audit harness. Resolve conflicts
     carefully (typically additive merges work cleanly because each
     audit slice edits different lines).

  8. Push:

       git push -u origin <your-branch>

     Retry up to 4 times with exponential backoff on network errors.
     Do NOT force-push.

  9. Write a deliverable doc at:

       docs/clojure-pedagogy/audits/deep-audit-<fable-dash>-<short-tag>.md

     using the structure from the playbook (grades-sampled,
     papercuts-found grouped by category, detectors added, fixes
     applied, before/after numbers, branch SHA, caveats).

  10. Report a 8-15 line summary in your final agent message
      covering:

      - which fable + which 6 grades you sampled
      - branch name + commit SHA
      - papercuts found / fixed (count by category)
      - new detectors added (count + names)
      - audit-harness issue count before / after
      - any blockers (e.g. host-interop forms beyond your scope)

Constraints:

  - Stay focused on YOUR slice. Don't audit other fables. Don't
    audit grades outside your random 6.
  - Don't refactor unrelated infrastructure.
  - Don't create planning / scratch / decision docs. The deliverable
    doc is the only doc.
  - Don't add emojis to anything.
  - Don't break existing smoke tests. If a smoke test starts
    failing, revert the offending change and reconsider.
  - Don't push to main directly. Don't push to other agents'
    branches.
  - Don't run /ultrareview or attempt to dispatch other agents.

Affirmative push (from the user's directive):

  Beyond bug-finding, push the prose toward characters conveying
  emotions and adjectives about their environmental situation,
  mapped onto the algorithmic situation. A grade-1 atom should
  feel "calm, the answer plain"; a grade-12 transducer should feel
  "alternating between possibility and verification, weighing the
  search against the constraint." Capture violations as Cat-J
  papercuts; lift the pattern at the source (subplot template, EMO
  pool, scenario slot) so one fix elevates many records.

Pedagogical lens (don't lose this):

  Each fable carries a distinct moral. Tortoise-hare = vanity vs.
  steadiness. Crow-pitcher = patience vs. thirst. Milkmaid =
  daydream vs. care. Boy-wolf = trust vs. false alarm. Dog-shadow
  = greed loses what was had. Your fixes should preserve the
  fable's polarity — the patient/evaluator role does the careful
  thing; the dreamer/guesser role overreaches. If you find
  polarity flips, flag them as Cat-F (narrative) papercuts.

Definition of done:

  - Branch pushed.
  - All smoke tests pass on that branch.
  - audit-harness.py FABLE=<your-fable> reports fewer issues after
    your work than before (track deltas in your deliverable doc).
  - Deliverable doc committed under
    docs/clojure-pedagogy/audits/deep-audit-<fable-dash>-<short-tag>.md.
  - Summary message in your final reply.

Begin by reading the playbook, picking your fable + 6 random
grades, then running the baseline smoke tests to confirm main is
green. After that, generate your read-corpus and start the deep
read.
```

---

## Dispatch usage

Pick a model:

- **Haiku 4.5** — fastest, cheapest. Workable for any slice but
  may produce shallower papercut analysis on hard grades.
- **Sonnet 4.6** — best balance. Recommended default.
- **Opus 4.7** — for fables with highest pre-existing issue count
  (typically `dog_shadow`).

Run agents in parallel where their branches don't conflict.

If two agents pick the same fable, they'll likely produce
overlapping papercut findings; that's fine — when collating, the
user dedups. If two agents both edit `emotion_pools.py` or
`opener_pools.py`, the second's rebase will need to merge — the
prompt's step 7 guidance handles this.

## Acceptance criteria across the full sweep (post-merge)

When all dispatched slices are merged:

- audit-harness.py has ≥50 detectors (currently 25).
- per-fable audit issue count ≤ 10 across all categories
  (currently 15-53).
- Cat-J grounding-coverage detector reports ≥85% of records have
  drawn-value mentions + EMO-band phrases + environmental
  adjectives mapped to the algorithmic situation.
- All smoke tests pass.
- Showcase doc regenerates cleanly with the lifted prose visible.
