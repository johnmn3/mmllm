# Tortoise-and-the-Hare — full K-12 Clojure curriculum

**216 subjects across 12 grades; 513 examples; ~113,886 training
records when generated at the standard 222 variants/example.**

This curriculum is the first complete fable-curriculum to be
authored. It serves as the reference implementation; the
remaining 9 fable-curricula (crow-pitcher, goose-eggs,
boy-wolf, ant-grasshopper, milkmaid, fox-grapes, two-mice,
dog-shadow, lion-bulls) follow the same pattern via
`docs/clojure-pedagogy/SKILL-fable-curriculum-author.md`.

## How the fable maps onto the curriculum

The Tortoise-Hare moral dynamic — **vanity vs. steadiness** —
informs every record:

- **Hare** is the boastful, hasty guesser. "I can see the answer
  at a glance. No need to evaluate." The Hare is the model's
  former bad habit: skipping the form, pattern-matching to a
  numeric answer that may or may not be right.
- **Tortoise** is the patient, careful evaluator. "Let's actually
  submit the form to the REPL and read what it returns." The
  Tortoise is the model's correct behavior under eval-first
  discipline: produce the form, let the runtime compute, the
  REPL has the last word.

Across all 216 subjects, the same characters keep playing out
the same dynamic over different Clojure concepts. The model
sees the moral lesson reinforced thousands of times in
hundreds of surface forms.

## Grade-by-grade summary

| Grade | Layer | Subjects | Examples | Variants @ 222 |
|---|---|---|---|---|
| 1 | L1+L2 intro: atoms, eval | 18 | 80 | 17,760 |
| 2 | L1+L2 mastery: operators | 22 | 88 | 19,536 |
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
| **TOTAL** | | **216** | **513** | **113,886** |

## Files

```
src/mmllm/aesop/curriculum/tortoise_hare/
    __init__.py
    grade_1.py     # 18 subjects (G1-01..G1-18)
    grade_2.py     # 22 subjects
    ...
    grade_12.py    # 18 subjects
```

Each grade file:
- Imports `_SHARED_SUBPLOTS` and `_PLAN_POOL` from `grade_1`
- Extends them with 1-2 grade-flavored subplots and plan-pool entries
- Defines its grade's `SubjectCurriculum` entries
- Exposes `SUBJECTS: dict[str, SubjectCurriculum]`
- Has a `smoke_test()` that generates one record per subject

## Usage

```python
from mmllm.aesop.curriculum.tortoise_hare.grade_1 import SUBJECTS as G1
from mmllm.aesop.curriculum.generator import generate_subject

# Generate 222 narrative variants of a single subject
recs = generate_subject(G1["G1-13"], n_per_example=222, seed=0)
# → 222 × 6 examples = 1,332 records, all teaching first-arithmetic-call
```

## Variety achieved

Spot-checked at 222 variants per example across grades 1, 5, 10, 12:
- G1-13 (First arithmetic call): 1,332 records, **1,332 unique** user_msg
- G5-12 (reduce): 666 records, 665 unique (1 collision in 666)
- G10-03 (defmacro): 444 records, **444 unique**
- G12-01 (Transducers): 444 records, **444 unique**

Variety score is essentially 1.00 — the cross-product of (8-10
subplots × 7 hares × 3 tortoises × 7 path-locations × 4-5 openers
× 3+ emotion picks per template) gives a combinatorial space far
larger than any 222-record draw.

## Subjects requiring adaptation

Some grade-6/11/12 subjects don't naturally fit a single
`eval(form)` test (e.g., G11-01 "JVM/CLR/JS/Python overview",
G12-04 "core.async introduction", G6 namespace machinery). These
were adapted in two ways:
- **Surrogate forms**: instead of executing a side-effecting
  operation, an evaluable proxy form (e.g., `(name 'foo.bar)` to
  test namespace-symbol mechanics, `(:private (meta '^:private x))`
  to test metadata).
- **Placeholder forms with educational subplots**: when no
  surrogate suffices, the form is `(do "subject overview" :studied)`
  with `:studied` as the answer; the narrative subplot carries the
  educational content.

This trade-off keeps the model's tool-call shape consistent
across all 216 subjects while still teaching the underlying
concept through the surrounding text.
