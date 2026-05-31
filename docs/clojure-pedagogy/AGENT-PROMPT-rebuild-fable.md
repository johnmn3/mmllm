# Agent prompt: rebuild your fable using the Phase C framework

**Copy this entire document into each agent's session, replacing
`<FABLE>` with the assigned fable name (e.g. `goose-eggs`,
`ant-grasshopper`, `crow-pitcher`, `boy-wolf`, `milkmaid`).**

---

## Your assignment

Bring the **`<FABLE>`** Clojure curriculum up to story-scaffold parity
with the `tortoise-hare` reference. The goal: same 216-subject K-12
structure, but with this fable's characters, imagery, and grounded
stories.

You are a sonnet-class agent. **You are the architect, not the
typesetter.** Your job is planning, integration, and quality control
— not authoring 400 stories by hand. **Fan out the bulk work to
haiku sub-agents.**

If you find yourself authoring 30+ scenario/need/mapping/resolution
slots in your own context, you have failed the mission. Stop, pull
back, fan out.

## Required reading (in order)

Don't skip. Read these completely before writing any code:

1. **`docs/clojure-pedagogy/HOWTO-rebuild-fable-with-framework.md`**
   — your full playbook. Eight phases, explicit fan-out points,
   token-budget guidance, ready-to-paste sub-agent briefs. **Read
   this first.**

2. **`docs/clojure-pedagogy/SKILL-fable-curriculum-author.md`** —
   the canonical authoring skill. Pay particular attention to:
   - "Metaphor families" (the 22-family catalog)
   - "Story-scaffold framework — the metaphor must DRIVE the action"
   - "Common mistakes (anti-patterns to avoid)" — pitfalls 1-31

3. **`docs/clojure-pedagogy/audits/coverage-report-tortoise-hare.md`**
   — what "done" looks like at the metric level.

4. **`docs/clojure-pedagogy/audits/metaphor-demo-tortoise-hare.md`**
   — read 5-10 family entries to feel the difference between
   "metaphor as label" (broken) and "metaphor as story" (right).

5. **The reference codebase**: `src/mmllm/aesop/curriculum/tortoise_hare/`
   — especially `_metaphor_pools.py` and `grade_3.py` / `grade_4.py`
   for representative metaphor families.

## Working branch

Create a feature branch off `main`:

```bash
git checkout -b claude/<FABLE>-phase-c-framework main
```

Push periodically with `-u origin claude/<FABLE>-phase-c-framework`.
Do NOT push to `main` directly. Do NOT push to other agents' branches.

## The eight phases (from HOWTO)

You execute these in order. Commit + push at the end of each phase.

| Phase | What | Who | Your tokens |
| ----- | ---- | --- | ----------- |
| 1 | Map your fable's imagery to 22 metaphor families | YOU | ~5K |
| 2 | Mirror tortoise-hare directory structure | YOU (1 commit) | ~10K |
| 3 | Author 22 family pools in your fable's `_metaphor_pools.py` | **FAN OUT — 4-5 haiku** | ~5K integrating |
| 4 | Author all 216 subjects' bones | **FAN OUT — 1 haiku/grade** | ~5K integrating |
| 5 | Audit clean across all 216 subjects | YOU | ~5K |
| 6 | Author 22 canonical story-slotted examples | YOU | ~15K |
| 7 | Author the remaining ~400 metaphor-rich stories | **FAN OUT — 1 sonnet or haiku per grade** | ~5-10K integrating |
| 8 | Final audit + showcase + commit | YOU | ~5K |

**Total your-context budget: ~70-80K tokens.** If you exceed that,
you're not delegating enough.

## Three things you must NOT cheap-out on

These are the only places where your own careful authoring
matters. Every other phase, prefer to fan out:

1. **Phase 1 imagery mapping** — wrong imagery cascades into 400+
   broken stories. Take the time. Save to
   `docs/clojure-pedagogy/audits/metaphor-imagery-<FABLE>.md`.

2. **Phase 6 canonicals** — these set the pattern haiku will
   pattern-match against. Author all 22 yourself, with care.

3. **Phase 5 + Phase 8 audits** — broken state must not ship to
   `main`. Iterate until 0 issues across the audit harness.

## Fan-out discipline

When you fan out, follow these rules:

- **Spawn agents in parallel** with single-message multi-tool-use.
  Do not serialize unless an agent's output is required by the
  next.
- **Brief each agent thoroughly.** Token saved on briefs is
  generally token spent on integration. Use the ready-made
  brief templates in HOWTO sections "Phase 3" and "Phase 7".
- **Tell agents NOT to commit.** You commit. They author and
  audit-clean their own grade/family, then report back.
- **Audit your own grade-set after each agent reports.** Don't
  trust their "I audited clean" — re-run the harness yourself.
  Issues sometimes appear when changes from multiple agents land
  in the same audit run.
- **Use haiku for mechanical authoring** (template prose, story
  slots). Use sonnet only when nuanced judgment is required
  (canonical examples, integration decisions, metaphor design).

## Existing fables that may already be in `curriculum/<FABLE>/`

If your fable already has a `curriculum/<FABLE>/` directory (e.g.
`goose_eggs`, `ant_grasshopper`):

- The directory may have an OLDER curriculum without the Phase C
  framework. Check whether each grade file uses
  `_metaphor_pools.py` imports.
- **If yes**: skip Phase 2; just verify imports are correct and
  proceed to Phase 3 with the existing structure.
- **If no**: do Phase 2 — copy tortoise-hare's structure as the
  starting template, then adapt the imagery in Phase 3.

## What "done" looks like

Per HOWTO Phase 8:

- 216 subjects in `src/mmllm/aesop/curriculum/<FABLE>/grade_*.py`
- 22 family pools in `_metaphor_pools.py` with `<FABLE>`'s imagery
- 22 canonical story-slotted examples (your authoring)
- ~400 additional story-slotted examples (haiku authoring)
- Audit shows 0 issues:
  ```
  FABLE=<fable_module_name> python3 docs/clojure-pedagogy/audits/audit-harness.py
  ```
- Showcase doc at
  `docs/clojure-pedagogy/audits/metaphor-demo-<FABLE>.md`
- Coverage report at
  `docs/clojure-pedagogy/audits/coverage-report-<FABLE>.md`
- Branch pushed; ready for review and merge to `main`

## Coordination with other agents

Four other sonnet agents are working on different fables in
parallel. They share the same `main` branch and the same
codebase, but each is on its own feature branch.

Avoid editing files outside `src/mmllm/aesop/curriculum/<FABLE>/`
and `docs/clojure-pedagogy/audits/*-<FABLE>.md`. Do NOT edit:

- `src/mmllm/aesop/curriculum/generator.py` (shared)
- `src/mmllm/aesop/curriculum/tortoise_hare/` (reference; do not
  modify)
- `docs/clojure-pedagogy/SKILL-*.md` (canonical skill; do not
  modify)
- `docs/clojure-pedagogy/HOWTO-*.md` (your own playbook; do not
  modify)
- `docs/clojure-pedagogy/audits/audit-harness.py` (shared; if you
  spot a missing check, leave it for the parent session)

## When in doubt

- "Should I author this myself?" → **Probably no, fan out.**
- "Should I read this whole 1000-line file?" → **No, grep / read
  the relevant subject only.**
- "Should I think hard about the ideal scenario?" → **No, copy the
  tortoise-hare canonical structure and replace imagery.**
- "Should I audit after every single change?" → **No, batch and
  audit at phase boundaries.**

## Final report (when complete)

Reply with a short summary:
- Branch name + final commit SHA
- Coverage numbers (subjects, stories authored, audit clean
  confirmation)
- Pointers to the showcase + coverage docs
- Any subjects you couldn't author cleanly (rare; flag for
  human review)

Then stop. Don't open a PR yourself; the parent session will
review and merge.

---

**Begin with Phase 0: read the HOWTO and SKILL docs, then plan
your imagery mapping (Phase 1).** Don't write code until you've
finished reading and have your imagery table drafted.
