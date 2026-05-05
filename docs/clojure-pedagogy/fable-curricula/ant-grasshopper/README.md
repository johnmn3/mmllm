# Ant-and-the-Grasshopper — full K-12 Clojure curriculum

**216 subjects across 12 grades; 502 examples; ~111,444 training
records when generated at the standard 222 variants/example.**

The second complete fable-curriculum, mirroring the structure of the
[tortoise-hare reference](../tortoise-hare/README.md) through the lens
of the Ant-and-the-Grasshopper fable.

## How the fable maps onto the curriculum

The Ant-Grasshopper moral dynamic — **prudence vs. idleness** —
informs every record:

- **Grasshopper** (Chirp / Skip / Hum) is the carefree skipper. "I
  can see the answer at a glance. No need to evaluate. Why count when
  I can sing?" The Grasshopper is the model's former bad habit:
  pattern-match to a plausible answer instead of submitting the form
  to the runtime.
- **Ant** (Tic / Toc / Bit) is the patient evaluator. Every form is
  written carefully, submitted to the REPL, and the answer is read
  off the runtime's reply. The Ant's stockpile grows one grain at a
  time; the Ant's understanding grows one form at a time. "Submit
  {concept_phrase} to the REPL. Whatever comes back is the answer."

The structural lesson is the same as tortoise-hare's vanity-vs-
steadiness — patient evaluation beats hasty guessing — but the
imagery throughout is ant-grasshopper: meadows turning gold,
stockpiles measured day-by-day, the coming of winter as the moral
horizon. Across all 216 subjects, the same characters keep playing
out the same dynamic over different Clojure concepts. The model
sees the moral lesson reinforced thousands of times in hundreds of
surface forms.

The fable's accumulation/reduction theme is a natural fit for
fold/reduce-style subjects: G3 multi-binding `let`, G4 collection
counting, G5 `reduce` over a sequence — each is "the same operation
repeated, day by day, across the stockpile." G8 polymorphism leans
into the species-difference beat (different ants vs different
grasshoppers responding to the same call). G9 state/concurrency
becomes the Ant's careful day-by-day stockpile update vs the
Grasshopper's want-it-all-now mutation.

## Grade-by-grade summary

| Grade | Layer | Subjects | Examples | Variants @ 222 |
|---|---|---|---|---|
| 1 | L1+L2 intro: atoms, eval | 18 | 80 | 17,760 |
| 2 | L1+L2 mastery: operators | 22 | 77 | 17,094 |
| 3 | L3: naming, scope | 18 | 31 | 6,882 |
| 4 | L4: collections | 20 | 39 | 8,658 |
| 5 | L5 intro: control + higher-order | 22 | 39 | 8,658 |
| 6 | org: namespaces | 16 | 33 | 7,326 |
| 7 | err: errors, IO | 18 | 36 | 7,992 |
| 8 | poly: protocols, multimethods | 16 | 31 | 6,882 |
| 9 | conc: atom/ref/agent | 18 | 34 | 7,548 |
| 10 | meta: macros | 16 | 36 | 7,992 |
| 11 | interop: JVM/JS/Python | 14 | 29 | 6,438 |
| 12 | real: transducers, async, projects | 18 | 37 | 8,214 |
| **TOTAL** | | **216** | **502** | **111,444** |

## Files

```
src/mmllm/aesop/curriculum/ant_grasshopper/
    __init__.py
    grade_1.py     # 18 subjects (G1-01..G1-18) — defines _SHARED_SUBPLOTS + _PLAN_POOL
    grade_2.py     # 22 subjects
    ...
    grade_12.py    # 18 subjects
```

Each grade file:
- Imports `_SHARED_SUBPLOTS` and `_PLAN_POOL` from `grade_1`
- Extends them with 1-3 grade-flavored subplots and plan-pool entries
- Defines its grade's `SubjectCurriculum` entries
- Exposes `SUBJECTS: dict[str, SubjectCurriculum]`
- Has a `smoke_test()` that generates one record per subject

## Usage

```python
from mmllm.aesop.curriculum.ant_grasshopper.grade_1 import SUBJECTS as G1
from mmllm.aesop.curriculum.generator import generate_subject

# Generate 222 narrative variants of a single subject
recs = generate_subject(G1["G1-13"], n_per_example=222, seed=0)
# → 222 × 6 examples = 1,332 records, all teaching first-arithmetic-call
```

## Variety achieved

Spot-checked at 222 variants per example across grades 1, 5, 10, 12:
- G1-13 (First arithmetic call): 1,332 records, **1,328 unique** (0.997)
- G5-12 (reduce): 666 records, **665 unique** (0.999)
- G10-03 (defmacro): 444 records, **443 unique** (0.998)
- G12-01 (Transducers): 444 records, **444 unique** (1.000)

Variety score is essentially 1.00 — the cross-product of (8-13
subplots × 3 ants × 3 grasshoppers × 7 meadow-locations × 4-5
openers × 3+ emotion picks per template) gives a combinatorial
space far larger than any 222-record draw.

## Fable-specific extensions

Three additive changes to `mmllm.aesop.curriculum.generator`:

1. `_pick_ag_chars(scene)` — pulls a fresh `(ant, grasshopper)` pair
   from `ont.CHARACTERS` filtered by species.
2. `_pick_ag_location(scene)` — picks from the seven meadow-adjacent
   locations natural for ant-grasshopper (`meadow, forest, woods,
   garden, orchard, hilltop, farm`). Replaces tortoise-hare's `road`
   with `farm` for stockpile-narrative fit.
3. `_build_placeholders(...)` accepts a `fable=` kwarg and routes the
   two characters into either `{hare}/{tortoise}` (default) or
   `{ant}/{grasshopper}` placeholder keys with the standard suffix
   family (`_phrase`, `_he_she`, `_he_she_cap`, `_his_her`,
   `_him_her`). Three additional EMO picks (`emo_content`,
   `emo_regretful`, `emo_hungry`) round out the ant-grasshopper
   emotional palette.

All changes are additive — every tortoise-hare smoke test still
passes after the patch.

## Audit status

`docs/clojure-pedagogy/audits/ant-grasshopper-audit-harness.py` runs
every documented pitfall check (META_META, BAD_PLACE_PREP,
BAD_VERB_PREP, ASIDE_PAREN, EMDASH_COMMENTARY, SAID_PARTICIPLE,
DOUBLE_FROM, ANSWER_LEAK, UNFILLED_PLACEHOLDER, VERB_AGREEMENT,
LOW/HIGH_LENGTH, NESTED_COMPUTES) over 3 records per example for
all 502 examples. Current status: **0 issues.**

## Subjects requiring adaptation

Higher-grade tortoise-hare subjects that don't naturally fit a
single `eval(form)` test (G6 namespace machinery, G7 IO, G11 host
overviews, G12 library briefs, G12-04 core.async) use the same two
adaptation strategies as tortoise-hare:

- **Surrogate forms**: e.g., `(name 'foo.bar)` to test namespace-
  symbol introspection without filesystem side effects.
- **Marker forms with educational subplots**: form is
  `(do "subject overview" :studied)` with `:studied` as the answer;
  the narrative subplot carries the educational content.

Identical strategies as tortoise-hare; the surface narration just
shifts to ant-grasshopper voice (the Ant explains the foreign
runtime to the Grasshopper; the Ant inspects the library at the
end of the harvest season).

## Three-character touches

The ant-grasshopper fable supports three named characters per side
(Tic/Toc/Bit; Chirp/Skip/Hum) where tortoise-hare has 7 hares and
3 tortoises. The narrower per-side pool is offset by the larger
subplot pool and three additional EMO_* pools (content, regretful,
hungry). Net combinatorial space is comparable: cross-products
yield >2,000 distinct surface variants per template.
