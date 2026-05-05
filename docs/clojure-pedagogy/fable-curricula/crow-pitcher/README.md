# Crow-and-the-Pitcher — full K-12 Clojure curriculum

**216 subjects across 12 grades; 513 examples; ~113,886 training
records when generated at the standard 222 variants/example.**

The crow-pitcher curriculum is the second complete fable-curriculum
(after `tortoise-hare`). It follows the same structure and patterns
documented in
[`SKILL-fable-curriculum-author.md`](../../SKILL-fable-curriculum-author.md),
re-cast through Aesop's "thirsty crow" fable.

## How the fable maps onto the curriculum

The Crow-Pitcher moral dynamic — **cleverness in adversity** —
informs every record. The original fable: a thirsty crow finds a
pitcher whose water sits too low for her beak to reach. Rather than
give up, she patiently drops stones in one at a time until the
surface rises to where she can drink.

The pedagogy mirror is exact:

- **The hasty crow** is impatient; would give up, or guess at the
  answer rather than evaluate. The model's bad habit personified —
  pattern-matching to a numeric answer that may or may not be right.
- **The clever crow** is methodical; drops the form into the REPL
  the way a stone goes into the pitcher — one form, one rise of
  the surface, until the beak (eval) reaches the answer. The model's
  correct discipline under eval-first.

The fable has only one named protagonist in its original form, so
the curriculum stages a dialogue between two crows so the moral
dynamic — patient form-building vs. give-up impatience — can be
carried by characters rather than left implicit. Both are drawn
from the same crow pool (Korvus, Caw, Sable); roles rotate per
record, so the model sees Korvus playing the hasty side in some
records, the clever side in others, and likewise for Caw and Sable.
Same dynamic, different surface forms.

Across all 216 subjects, the same dynamic keeps playing out over
different Clojure concepts. The model sees the moral lesson
reinforced thousands of times in hundreds of surface forms.

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
src/mmllm/aesop/curriculum/crow_pitcher/
    __init__.py
    grade_1.py     # 18 subjects (G1-01..G1-18) + _SHARED_SUBPLOTS + _PLAN_POOL
    grade_2.py     # 22 subjects
    ...
    grade_12.py    # 18 subjects
```

Each grade file:
- Imports `_SHARED_SUBPLOTS` and `_PLAN_POOL` from `grade_1`
- Extends them with 1-3 grade-flavored subplots and plan-pool entries
  (collections-of-pebbles for G4, ledger-of-bindings for G3,
  meeting-of-species for G8, pitcher-as-finish-line for G12, etc)
- Defines its grade's `SubjectCurriculum` entries
- Exposes `SUBJECTS: dict[str, SubjectCurriculum]`
- Has a `smoke_test()` that generates one record per subject

## Usage

```python
from mmllm.aesop.curriculum.crow_pitcher.grade_1 import SUBJECTS as G1
from mmllm.aesop.curriculum.generator import generate_subject

# Generate 222 narrative variants of a single subject
recs = generate_subject(G1["G1-13"], n_per_example=222, seed=0)
# → 222 × 6 examples = 1,332 records, all teaching first-arithmetic-call
```

## Variety achieved

Spot-checked at 222 variants per example across every grade:
all 216 subjects pass the 0.95 variety threshold at n=50. The
combinatorial cross-product (8-10 subplots × 3 crows × 8 outdoor
locations × 4 openers × 3+ emotion picks per template) produces
~10,000+ distinct surface forms per subject, so a 222-record draw
yields 220-222 unique user_msgs per example.

## Crow-specific adaptation: roles, not species

Tortoise-hare can rely on species to distinguish the hasty character
(hare) from the patient one (tortoise) — the names and pronouns
follow naturally. Crow-pitcher has only one species (crow), so the
curriculum exposes role-aware aliases — `{hasty}` and `{clever}` —
in addition to the canonical `{hare}/{tortoise}` placeholders. The
generator's `_pick_cp_chars` returns two distinct crows per record;
`_build_placeholders` populates both placeholder sets so subplots
can use whichever names read more naturally.

The implementation is purely additive: tortoise-hare templates
continue to use `{hare}/{tortoise}` and work unchanged; crow-pitcher
templates use `{hasty}/{clever}` exclusively. See
`src/mmllm/aesop/curriculum/generator.py` (`_pick_cp_chars`,
`_pick_cp_location`, the `if fable == "crow-pitcher"` branch in
`_build_placeholders`).

## Adapted crow-pitcher tropes (reframings from tortoise-hare)

A few tortoise-hare narrative beats don't fit crow-pitcher and were
reframed:

- **race-pause** → **pitcher-pause / glide-down**: in tortoise-hare
  the hare stops mid-race; the crow-pitcher equivalent is a thirsty
  alighting at the pitcher's edge.
- **footrace finish-line** (G12) → **end-of-foraging / end-of-day**:
  the long thirsty foraging is over; the crows perch on a branch
  and look back over the tools they've gathered.
- **two cottages** (G6 cross-namespace) → **two roosts on opposite
  sides**: the crows roost in different trees, each with its own
  copybook of forms.
- **stone-by-stone ledger** (G3 naming, G6 namespaces, G9 state):
  the natural metaphor for incremental, name-bearing additions.

The fable's central props — pitcher, stones, thirsty beak, rising
water — also serve as background imagery: stones are forms; the
water surface is the answer; the beak's reach is eval; "drop the
form into the REPL" is the unifying action.

## Subjects requiring adaptation

A few grade-6/11/12 subjects don't naturally fit a single
`eval(form)` test (e.g., G11-01 "JVM/CLR/JS/Python overview",
G12-04 "core.async introduction", G6 namespace machinery). These
were adapted in two ways:

- **Surrogate forms**: instead of executing a side-effecting
  operation, an evaluable proxy form (e.g., `(name 'pitcher.crow)`
  to test namespace-symbol mechanics).
- **Placeholder forms with educational subplots**: when no
  surrogate suffices, the form is `(do "subject overview" :studied)`
  with `:studied` as the answer; the narrative subplot carries the
  educational content.

## Audit status

Final audit (via `python3 docs/clojure-pedagogy/audits/audit-harness.py
--fable crow_pitcher`): **0 issues across 215 subjects × 3 records
per example.** No META_META, BAD_PLACE_PREP, BAD_VERB_PREP,
ASIDE_PAREN, EMDASH_COMMENTARY, SAID_PARTICIPLE, DOUBLE_FROM,
ANSWER_LEAK, NESTED_COMPUTES, or low-variety findings.
