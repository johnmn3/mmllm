# Continuation prompt: finish the Phase B + C work on your fable

**Paste this into the same agent's session (the one that just merged
main + fixed audit issues). Replace `<FABLE>` with your fable's name
(e.g. `fox-grapes`, `crow-pitcher`).**

---

## Where you are

You've completed the foundation:
- Merged `main` into your branch (the 24-commit Phase A/B/C framework
  that tortoise-hare landed)
- Fixed audit issues from the merge surface
- Pushed deep spot-check files
- Audit is clean across all 12 grades

That's roughly **Phases 0–2** of the eight-phase rebuild playbook. Now
you do **Phases 3–8** — applying the new framework that's just been
merged in. You're not done; you've just finished the prep.

## What's still missing

Run these commands and you'll see the gaps:

```bash
ls src/mmllm/aesop/curriculum/<FABLE>/_metaphor_pools.py
# → No such file. You haven't built the 22 metaphor families yet.

python3 -c "
import importlib
total_stories = 0
for g in range(1, 13):
    mod = importlib.import_module(f'mmllm.aesop.curriculum.<FABLE_MODULE>.grade_{g}')
    for sid, sub in mod.SUBJECTS.items():
        total_stories += sum(1 for ex in sub.examples if 'story' in getattr(ex, 'tags', ()))
print(f'stories: {total_stories}')
"
# → 0. You haven't authored any grounded story slots yet.
```

`tortoise-hare` has 22 metaphor pools (~110 templates) and 350+
authored story slots (~70% coverage of the 422 metaphor-rich
examples). Your fable still has 0 of each.

## Read the playbook

The full playbook lives at
**`docs/clojure-pedagogy/AGENT-PROMPT-rebuild-fable.md`** — read it
end to end. It points at:

- `docs/clojure-pedagogy/HOWTO-rebuild-fable-with-framework.md` — the
  detailed eight-phase plan
- `docs/clojure-pedagogy/SKILL-fable-curriculum-author.md` — the
  authoring rules (Metaphor families + Story-scaffold framework
  sections especially)
- `docs/clojure-pedagogy/audits/coverage-report-tortoise-hare.md` —
  what "done" looks like at the metric level
- `docs/clojure-pedagogy/audits/metaphor-demo-tortoise-hare.md` — read
  5-10 family entries to feel the difference between metaphor-as-label
  (broken) and metaphor-as-story (right)
- `src/mmllm/aesop/curriculum/tortoise_hare/_metaphor_pools.py` — the
  reference: 22 family pools with the canonical metaphor anchors and
  a `_story()` template per family

## You are the architect, not the typesetter

You are sonnet. **Fan out the bulk work to haiku sub-agents.** If you
find yourself writing 30+ scenario/need/mapping/resolution slots in
your own context, you have failed the mission. Stop, pull back, fan
out.

Total your-context budget for Phases 3–8: **~70-80K tokens.** You
should be reading, planning, integrating, auditing, committing — not
authoring template prose.

## The remaining phases

Skip Phases 0–2 (already done). Execute:

### Phase 3: Author 22 family pools in `<FABLE>/_metaphor_pools.py`

The 22 family names (`_POUCH_SUBPLOTS`, `_RECIPE_SUBPLOTS`,
`_BASKET_SUBPLOTS`, etc.) are **constant across fables**. The
templates inside each pool use **your fable's** characters and
imagery.

**Phase 1 of the original playbook (imagery mapping) was supposed to
happen first — go do it now.** Author
`docs/clojure-pedagogy/audits/metaphor-imagery-<FABLE>.md` mapping each
of the 22 metaphor anchors into your fable's world. For
fox-grapes:

| Family            | tortoise-hare            | <FABLE> equivalent             |
| ----------------- | ------------------------ | ------------------------------ |
| _POUCH_           | leather pouch at hip     | small leaf-pouch the fox carries / a knot in tail-fur for a stretch / etc. |
| _RECIPE_          | recipe-card on the road  | scratched fork-mark / a den-instruction / etc.  |
| _BASKET_          | foraging basket          | grape-cluster / fruit-basket / etc. |
| _NOTEBOOK_        | notebook on a tree stump | mark on the orchard's central tree / etc.    |
| ... (22 entries)

Then fan out 4-5 haiku agents to author the templates — one agent
covers 4-5 families. The HOWTO has the brief template for this
fan-out.

### Phase 4: Retag subjects

Each subject's grade file currently has
`subplots=_OLD_PER_GRADE_POOL`. Update each subject's `subplots=`
field to point at the right metaphor family pool. Per-family or
per-grade haiku agents handle this mechanically.

### Phase 5: Audit clean

After Phase 3 + 4, the audit may surface new issues from the new
templates. Iterate until 0 issues.

### Phase 6: Author 22 canonical story-slotted examples (YOU)

One canonical example per metaphor family. Author these YOURSELF —
they set the pattern haiku will pattern-match against in Phase 7.
Use the canonical 5-act shape (scenario / need / mapping /
resolution + tags=("story",)). The tortoise-hare canonicals are
in the grade files (grep `tags=("story",)` to find them).

### Phase 7: Author the remaining ~400 stories

Fan out 1 haiku/grade. Each grade-agent reads the canonicals + the
SKILL doc story-scaffold section and authors slots for the rest of
their grade's metaphor-rich examples.

### Phase 8: Final audit + showcase + coverage report

- `FABLE=<FABLE_MODULE> python3 docs/clojure-pedagogy/audits/audit-harness.py`
  → 0 issues
- Generate `docs/clojure-pedagogy/audits/metaphor-demo-<FABLE>.md`
  (mirror the script that produced metaphor-demo-tortoise-hare.md)
- Generate `docs/clojure-pedagogy/audits/coverage-report-<FABLE>.md`
  (mirror the script that produced coverage-report-tortoise-hare.md)

## Things to NOT cheap-out on

- **Imagery mapping** (Phase 3 prep): wrong imagery cascades into
  ~110 broken templates. Take time, write it down.
- **Canonical stories** (Phase 6): you author all 22 yourself. Don't
  delegate.
- **Audit iteration** (Phases 5 + 8): nothing ships until 0 issues.

## What "done" looks like

Match tortoise-hare's metrics:

| Metric                              | Target            |
| ----------------------------------- | ----------------- |
| Subjects                            | 216               |
| Examples                            | ~510              |
| Audit issues                        | 0                 |
| Metaphor pools                      | 22 (in `_metaphor_pools.py`) |
| Story-slotted examples              | 350+ (target ~70% coverage of metaphor-rich) |
| Demo + coverage docs                | both present in `audits/` |

## Coordination reminders

You're sharing the codebase with 4 other sonnet agents working on
different fables. Don't touch:

- `src/mmllm/aesop/curriculum/generator.py` — shared (already merged
  cleanly; leave it)
- `src/mmllm/aesop/curriculum/tortoise_hare/` — reference; do not
  modify
- `docs/clojure-pedagogy/SKILL-*.md` — canonical skill; do not modify
- `docs/clojure-pedagogy/HOWTO-*.md` — playbook; do not modify
- `docs/clojure-pedagogy/AGENT-PROMPT-*.md` — your brief; do not
  modify
- `docs/clojure-pedagogy/audits/audit-harness.py` — shared

You CAN edit:
- `src/mmllm/aesop/curriculum/<FABLE>/**` — your fable's curriculum
- `docs/clojure-pedagogy/audits/*-<FABLE>.md` — your fable's docs

## Begin with Phase 3 prep

**Don't write code first.** Read the playbook, then draft your
imagery-mapping table for the 22 families. Save it. Only then start
Phase 3 fan-out.

## Final report (when complete)

Reply with:
- Final commit SHA on your branch
- Coverage numbers (subjects / examples / story-slot %)
- Audit-clean confirmation
- Pointers to your demo + coverage docs

Then stop. The parent session reviews and merges to main.
