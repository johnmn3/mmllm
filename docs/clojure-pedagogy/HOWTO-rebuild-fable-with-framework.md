# How to rebuild a fable curriculum using the Phase C framework

**Audience:** Sonnet-class agents tasked with bringing a fable's
K-12 Clojure curriculum up to story-scaffold parity with the
tortoise-hare reference.

**Your goal:** end up with the same 216-subject K-12 curriculum
structure as tortoise-hare/, but with this fable's characters,
imagery, and story slots — and clean across the audit harness.

**Most important rule:** **You are the architect, not the
typesetter.** Fan out the bulk work to haiku sub-agents. Reserve
your own context for: planning, family-pool authoring, integration,
spot-checks, and committing. If you find yourself writing 30+
scenario/need/mapping/resolution slots by hand, **stop and fan out**.

---

## 0. Read these first (in this order)

Don't skip. Each one answers a question the next assumes:

1. **`docs/clojure-pedagogy/SKILL-fable-curriculum-author.md`** —
   the canonical authoring skill. Read every section, especially:
   - "Metaphor families" (the 22-family catalog)
   - "Story-scaffold framework — the metaphor must DRIVE the action"
     (the five acts, four slots, authoring rules)
   - "Common mistakes (anti-patterns to avoid)" — the pitfall
     numbering goes up to #31. Don't relearn these.

2. **`docs/clojure-pedagogy/audits/coverage-report-tortoise-hare.md`**
   — see what "complete" looks like.

3. **`docs/clojure-pedagogy/audits/metaphor-demo-tortoise-hare.md`**
   — read 5-10 family entries. Get a feel for what a finished record
   reads like — the difference between "metaphor as label" and
   "metaphor as story."

4. **The reference codebase**: `src/mmllm/aesop/curriculum/tortoise_hare/`
   — especially `_metaphor_pools.py` and one or two grade files
   (`grade_3.py` for pouch+recipe, `grade_4.py` for basket).

You should now have the architecture in your head.

---

## 1. Architecture refresher

Each fable's curriculum lives at:
```
src/mmllm/aesop/curriculum/<fable>/
    __init__.py
    grade_1.py … grade_12.py    # 216 subjects total
    _metaphor_pools.py           # 22 family pools, fable-specific imagery
```

A subject is a `SubjectCurriculum` containing:
- `examples`: list of `SubjectExample` (each has `form`, `expected`,
  `concept_phrase`, `question_what`, `goal_text`, `tags`, and the
  four story slots: `scenario`, `need`, `mapping`, `resolution`)
- `subplots`: a list of `SubplotTemplate` — picks one per render
- `plan_pool`: tuple of plan-only prefaces

A render combines:
- aesopian opener (3 per fable, in `mmllm/aesop/fables.py`)
- one subplot template (5 generic + 1 story-scaffold per family pool)
- character/location/emotion picks
- plan-pool entry

Default `n_per_example=222` records per example.

The 23 metaphor families (22 metaphor + `_GOAL_SUBPLOTS` fallback):

```
_POUCH_SUBPLOTS         let-binding (temporary container)
_RECIPE_SUBPLOTS        fn / defn / comp / partial (named procedure)
_BASKET_SUBPLOTS        collections / immutability
_SIEVE_SUBPLOTS         map / filter / take / drop / transducers
_NOTEBOOK_SUBPLOTS      atom / ref / swap! / dosync / CAS
_ACORN_SUBPLOTS         arithmetic
_GATE_SUBPLOTS          and / or / not / falsey rules
_FORK_SUBPLOTS          if / cond / case / when
_ROADSIGN_SUBPLOTS      def / namespace / require
_SAFETYNET_SUBPLOTS     try / catch / throw / assert
_SCROLL_SUBPLOTS        IO / metadata / slurp / spit
_GUILD_SUBPLOTS         protocols
_TOOLSHED_SUBPLOTS      host interop
_RUNNERAHEAD_SUBPLOTS   agent / future / promise
_REWRITERULE_SUBPLOTS   macros
_SCRIBE_SUBPLOTS        comments / whitespace / parens / do / reader
_CHALKMARK_SUBPLOTS     quote / symbols / syntax-quote
_SORTINGTABLE_SUBPLOTS  multimethods
_CARRYINGCASE_SUBPLOTS  deftype / defrecord
_TALLYWALK_SUBPLOTS     reduce / count
_BEADSTRING_SUBPLOTS    string ops
_CIRCUIT_SUBPLOTS       recur / loop
_GOAL_SUBPLOTS          (fallback for tooling/abstract subjects only)
```

Family **names are constant across fables.** Their **imagery is
fable-specific.** That's the whole point — same family of metaphor,
different visual language. Same idiom, different storytelling
materials.

---

## 2. Phase plan (work order)

You should execute these phases **in order** and **commit + push at
the end of each phase** so progress is visible.

| Phase | What | Who does it | Tokens you spend |
| ----- | ---- | ----------- | ---------------- |
| 0 | Read the docs above | you | ~20K |
| 1 | Map this fable's imagery to each metaphor family | you | ~5K (planning, no code) |
| 2 | Mirror the directory structure from tortoise-hare; copy + retag generic templates | you (1 commit) | ~10K |
| 3 | Author the 22 family pools in this fable's `_metaphor_pools.py` | **fan out — 1 haiku agent per ~5-7 families** | you spend ~5K integrating; haiku spend the rest |
| 4 | Author all 216 subjects' bones (form / expected / concept_phrase / question_what / goal_text / subplots-pool tag) | **fan out — 1 haiku per grade** | you spend ~5K integrating |
| 5 | Audit clean across all 216 subjects (no FORM_LEAK, no STORY_TAG_MISMATCH, no DOUBLE_PREP, etc.) | you (final integration) | ~5K |
| 6 | Author 22 canonical story-slotted examples — one per metaphor family | you (these set the tone for haiku in Phase 7) | ~15K |
| 7 | Author story slots for the remaining ~400 metaphor-rich examples | **fan out — 1 sonnet or haiku per grade** | you spend ~5K integrating |
| 8 | Final audit + showcase + commit | you | ~5K |

**Total your-context budget: ~70-80K tokens** if you delegate
properly. **3-5x more than that if you try to author everything
yourself.**

Per-phase detail follows.

---

## Phase 1: Map your fable's imagery to families

Goal: produce a small markdown table you can refer back to. **No
code yet.**

For each of the 22 metaphor families, decide what concrete imagery
in your fable carries it. The semantic structure is fixed; the
imagery is yours to set.

Example (tortoise-hare's mapping, for reference):

| Family | TH imagery | Goose-eggs equivalent (you'd decide) | Ant-grasshopper equivalent |
| --- | --- | --- | --- |
| pouch | small leather pouch tied at hip | apron-pocket worn while milking | grain-pouch carried while harvesting |
| recipe | recipe-card on the road | recipe-card pinned in the kitchen | seasonal-task-card in the colony |
| basket | foraging-basket with compartments | egg-basket with named tiers | grain-bin with named slots |
| sieve | sieve over an empty basket | egg-grader sorting by size | grain-sieve threshing chaff |
| notebook | notebook on a tree stump | tally-slate by the henhouse | colony-ledger in the queen's chamber |

Do this exercise for all 22. Pick imagery that has internal
coherence — props in the same fable should feel like they belong to
the same world. The Tortoise's pouch and basket and notebook all
sit on the meadow path. Your fable's props should sit in *one*
consistent setting.

Save your mapping table as `docs/clojure-pedagogy/audits/metaphor-imagery-<fable>.md`
and commit it. **This is the cheapest planning artifact you can
produce, and it saves 20-50K tokens of confusion later.**

---

## Phase 2: Mirror the directory structure

Set up the skeleton. You can copy + replace much of this from
tortoise-hare; **don't author it from scratch.**

```bash
cp -r src/mmllm/aesop/curriculum/tortoise_hare \
      src/mmllm/aesop/curriculum/<fable>
# Then edit the new files — change imports, character pickers,
# location pickers, etc.
```

What you must change in the copy:
- `from mmllm.aesop.curriculum.tortoise_hare.…` → `from
  mmllm.aesop.curriculum.<fable>.…` everywhere
- The character pool, location pool, opener pool — these come from
  `mmllm/aesop/fables.py` and pass through `Scene` to the
  generator. Verify your fable has these defined.
- `subject_title` strings should still match (they describe the
  Clojure concept, not the fable).
- `_metaphor_pools.py` is mostly placeholder at this stage — you'll
  rewrite the templates in Phase 3.

What you keep verbatim:
- Each subject's `examples` (`form`, `expected`, `concept_phrase`,
  `question_what`, `goal_text` — these describe the **Clojure idiom**,
  not the fable). You may need to swap fable-specific words like
  "tortoise" / "hare" inside these to your fable's characters.
- Each subject's `subplots=_FAMILY_SUBPLOTS` tag.
- Plan pools (mostly).

Run smoke + audit:
```
python3 -c "import mmllm.aesop.curriculum.<fable> as f; print('imports OK')"
FABLE=<fable> python3 docs/clojure-pedagogy/audits/audit-harness.py
```

Commit + push. End of phase 2.

---

## Phase 3: Author the 22 family pools (FAN OUT)

This is your first big delegation. **Don't author 22 pools × ~6
templates each yourself.** Fan out:

### How to fan out template authoring

Spawn ~4-5 haiku agents in parallel, each owning ~5 families. Brief
template (per agent):

```
You are authoring metaphor-bearing subplot templates for the
<fable> curriculum. Your families: <_FOO_, _BAR_, _BAZ_, ...>

Read first:
  - docs/clojure-pedagogy/SKILL-fable-curriculum-author.md
    (sections: Metaphor families, Story-scaffold framework, the
    8 authoring rules)
  - src/mmllm/aesop/curriculum/tortoise_hare/_metaphor_pools.py
    (the reference; mirror its structure exactly)

Imagery for this fable: see metaphor-imagery-<fable>.md
  - <_FOO_SUBPLOTS> uses <imagery>
  - <_BAR_SUBPLOTS> uses <imagery>
  ...

Write the pool definitions in
src/mmllm/aesop/curriculum/<fable>/_metaphor_pools.py.
For each pool:
  - 5 generic family templates (type-neutral within the family;
    do NOT make claims that fit only one subject in the family)
  - +1 story-scaffold template via the _story() helper

Authoring rules (do not violate):
  1. Concept named in every template (the family's noun: pouch,
     recipe, basket, etc.)
  2. Type-neutral within the family (no "Sets are X" if family
     covers vectors+lists+maps+sets)
  3. Use {goal_text}, {concept_phrase} — never {form_display}
  4. Pronoun case correct at sentence starts (use _cap variants)
  5. No "and" right after {concept_phrase} (avoids stutter)
  6. No "write a form to {goal_text}" verb collisions
  7. At least 2 of 5 templates carry a Hare/Tortoise (or
     species-equivalent) fable beat
  8. Audit clean (run audit harness; FORM_LEAK / ANSWER_LEAK_STRING
     / DOUBLE_PREP all 0 for any subjects testing your pool)

Do NOT commit. Report when done.
```

After 4-5 haiku agents finish, you (sonnet) integrate: read each
new pool, spot-check 1-2 templates per family for quality, audit
clean, commit + push.

**Token budget for you in this phase: ~5K** (briefing + integration).
Token budget for haiku: ~15-25K each, ~80-100K total. They're
cheap; spend them.

---

## Phase 4: Subject bones (FAN OUT)

Each subject's "bones" are the Clojure-side fields:
- `form`, `expected` (translate to your fable's runtime if needed —
  most are universal)
- `concept_phrase`, `question_what`, `goal_text` (should be
  fable-neutral; copy from tortoise-hare)
- `subplots=_FAMILY_SUBPLOTS` (already set if you copied properly)
- `tags` (still empty until phase 7)

If you copied the directory in phase 2, this is **mostly already
done.** Spot-check by running the audit. If clean, skip to phase 5.

If you didn't copy and you're authoring fresh: fan out one haiku per
grade with the explicit list of (form, expected, concept_phrase,
question_what, goal_text) from tortoise-hare's grade files.

**Token budget for you: ~5K.** Haiku do the rest.

---

## Phase 5: Audit clean across all 216 subjects

You run this. You verify. You don't fan out.

```
FABLE=<fable> python3 docs/clojure-pedagogy/audits/audit-harness.py
```

Must show 0 issues across:
- FORM_LEAK
- ANSWER_LEAK_STRING
- ASIDE_PAREN
- DOUBLE_PREP
- HIGH_LENGTH
- NESTED_COMPUTES
- EMDASH_COMMENTARY
- SAID_PARTICIPLE
- STORY_TAG_MISMATCH
- (and ~25 other pitfall checks)

If issues exist: fix them yourself **or** spawn one haiku to fix
the smallest cluster (1-2 grades worth) at a time.

Commit + push when clean.

---

## Phase 6: Author 22 canonical story-slotted examples

**You do this yourself.** Don't fan out. These set the *tone* for
the rest of the work; haiku will pattern-match against them in
Phase 7.

Pick one canonical example per family (use tortoise-hare's choices
as a guide — see `metaphor-demo-tortoise-hare.md` for the list).
For each, author:

```python
SubjectExample(
    form="...", expected=...,
    concept_phrase="...", question_what="...", goal_text="...",
    scenario=("..."),       # Act 1: SETUP
    need=("..."),           # Act 2: NEED
    mapping=("..."),        # Act 3: MAPPING
    resolution=("..."),     # Act 5: RESOLUTION (Act 4 is in template)
    tags=("story",),
)
```

The reference is in tortoise-hare's grade files (search for
`tags=("story",)` to find the 22 canonicals). Each lands the
metaphor + drives the operation + closes the loop in ~100-150
words across the four slots.

For your fable, pick imagery from your phase-1 mapping. Stay
under 150 words per example.

Audit must show 0 issues after each canonical lands.

**Token budget: ~15K** (22 examples × ~700 words each authoring +
edit + audit = a real chunk of work, but bounded).

Commit + push.

---

## Phase 7: Author the remaining ~400 metaphor-rich examples (FAN OUT)

This is the longest phase. **Fan out one agent per grade.** Use
sonnet for grades with nuanced families (let, fn, protocols,
macros) and haiku for grades that are mostly mechanical (arithmetic,
arrays, host interop).

Sample grade-agent brief:

```
Author story-scaffold slots for src/mmllm/aesop/curriculum/<fable>/
grade_<N>.py.

Goal: add four story slots (scenario / need / mapping /
resolution) + tags=("story",) to every example without them. The
canonical examples already in this file are templates — read them
first, mirror shape and tone.

Read first:
  docs/clojure-pedagogy/SKILL-fable-curriculum-author.md
    (story-scaffold framework section)

Imagery anchors for this grade's families: <list>

Authoring rules:
  1. Scenario must EXIST (not be hypothetical)
  2. Need must drive the operation
  3. Mapping spells out fable elements ↔ operation parts
  4. Resolution closes the loop with the need
  5. NO answer leaks (don't write the literal expected value in
     slots — describe abstractly: "the running total", "the new
     arrangement", "the verdict")
  6. NO DOUBLE_PREP (avoid "past on the trail", "to in the orchard")
  7. Length budget ~100-150 words/example total
  8. Use this fable's character pool only

For each example without tags=("story",):
  - convert _ex(...) call to full SubjectExample(...)
  - add four story slots
  - add tags=("story",)

Audit must show 0 issues for grade <N>.
Spot-check 3-5 rendered records.
Do NOT commit; report back.
```

You wait for ~12 agents to finish. Then you:
- Audit clean across all grades
- Fix any straggling issues yourself (or spawn one haiku to mop up)
- Regenerate the showcase doc (see `metaphor-demo-tortoise-hare.md`
  for the script pattern)
- Commit + push

**Token budget for you: ~5-10K integration.** Sub-agents do the
heavy ~50K-100K of authoring.

---

## Phase 8: Final audit + showcase + commit

You run:

```bash
FABLE=<fable> python3 docs/clojure-pedagogy/audits/audit-harness.py
python3 docs/clojure-pedagogy/audits/<fable>-smoke.py   # optional
```

Audit must show 0 issues. Coverage:
- Atom subjects (8): no story slots needed
- Abstract subjects (~36): no story slots needed (kept on `_GOAL_SUBPLOTS`)
- Metaphor-rich subjects (~172, ~422 examples): all should have
  `tags=("story",)` and all four slots filled

Generate a showcase doc (the script for tortoise-hare is at
`/tmp/metaphor_demo.py` — adapt it). Commit + push.

---

## Token-budget checklist

You should finish your assignment having spent **~70-80K tokens of
your own context**. If you find yourself spending more than that:

- Are you authoring slots yourself instead of fanning out? **Stop.**
- Are you reading every grade file end-to-end instead of trusting
  the canonical pattern? **Stop.**
- Are you re-authoring family templates instead of letting haiku do
  it once and reviewing the output? **Stop.**

**The leverage is in delegation.** You produce the architecture
(phase 1, phase 6 canonicals) and integrate (phase 5, phase 8).
Haiku produces the bulk (phase 3 templates, phase 7 stories).

---

## What "done" looks like

- 216 subjects in `src/mmllm/aesop/curriculum/<fable>/grade_*.py`
- 22 family pools in `_metaphor_pools.py` with this fable's imagery
- 22 canonical story-slotted examples (your authoring)
- ~400 additional story-slotted examples (haiku authoring)
- Audit shows 0 issues
- Showcase doc exists at
  `docs/clojure-pedagogy/audits/metaphor-demo-<fable>.md`
- Coverage report exists at
  `docs/clojure-pedagogy/audits/coverage-report-<fable>.md`
  (mirror the tortoise-hare format)
- Branch pushed; PR description summarizes work

You're done when this fable's stories rhyme with tortoise-hare's
stories — same family of metaphor, different storytelling
materials. The model trains on both fables and learns the
operation's structure across narrative angles, reinforcing the
mapping every record.

---

## When in doubt, do the cheap thing

- "Should I author this myself?" → **Probably no, fan out.**
- "Should I read this whole 1000-line file?" → **No, grep / read
  the relevant subject only.**
- "Should I think hard about the ideal scenario?" → **No, copy the
  tortoise-hare canonical structure and replace imagery.**
- "Should I audit after every single change?" → **No, batch and
  audit at phase boundaries.**

Three things you must NOT cheap-out on:
1. **Phase 1 imagery mapping** — wrong imagery cascades into
   400+ broken stories.
2. **Phase 6 canonicals** — these set the pattern haiku will mimic.
3. **Phase 5 + Phase 8 audits** — broken state shouldn't ship.

Everything else: delegate, integrate, move on.
