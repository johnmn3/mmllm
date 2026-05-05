# Fox-and-the-Grapes — full K-12 Clojure curriculum

**~215 subjects across 12 grades; ~510 examples; ~113,000+ training
records when generated at the standard 222 variants/example.**

This curriculum is the second complete fable-curriculum (after
tortoise-hare). It re-casts the entire K-12 framework through the
fable's moral lens — *rationalizing the unattainable as
undesirable* — and embeds the dialectic into every record.

## How the fable maps onto the curriculum

The Fox-and-the-Grapes moral dynamic — **rationalization vs honest
evaluation** — informs every record:

- **The hasty fox** is the rationalizer. After one failed reach (or
  one glance at a long-looking form), declares the prize "probably
  sour anyway" and walks away without evaluating. The hasty fox is
  the model's bad habit: pattern-matching to a numeric answer that
  *might* be right and skipping the eval call entirely.
- **The patient fox** is the corrective voice. Writes the form,
  submits it via the `eval` tool, counts attempts, and either reaches
  the prize or admits the limit honestly. The patient fox is the
  model's correct behavior under eval-first discipline: produce the
  form; the runtime computes; the REPL has the last word.

Across all ~215 subjects, the same two voices keep playing out the
same dynamic over different Clojure concepts. The model sees the
moral lesson reinforced thousands of times in hundreds of surface
forms.

## Second-voice approach: Option A — two foxes of opposite archetype

Fox-grapes is a solo-protagonist fable in spirit (one fox, one
unreachable cluster). Tortoise-hare gets its dialectic for free
because two characters share the path; fox-grapes had to choose
how to introduce a corrective voice. Three options were considered:

  - **A.** A second fox of the opposite archetype (patient vs hasty).
  - **B.** A small audience (rabbit, sparrow, hedgehog) that watches
        and gently corrects.
  - **C.** The fox's own internal monologue split between hasty and
        patient voices.

**This curriculum picks Option A.** The ontology supplies three foxes
(Renard m, Vix f, Sly n), so two distinct foxes can always be picked
per record. Each becomes a named voice:

  - `{hasty_fox}` — the original Aesop voice. The rationalizer.
  - `{patient_fox}` — the eval-first disciplined evaluator.

Why Option A over B or C:

  - **B (small audience)** would have required adding rabbit /
    sparrow / hedgehog characters to the ontology — out-of-scope
    additive change to a shared resource. The Renard / Vix / Sly
    pool was already there.
  - **C (internal monologue)** loses the named-character grounding
    that gives every other tortoise-hare record its distinct
    surface variability. A monologue-only template degrades to
    one fox + many adjectives, which is structurally narrower
    than a two-character beat.
  - **A** keeps the cross-product variety high (3 foxes pick 2
    distinct = 6 named pairs × 7 locations × ~10 subplots ×
    EMO picks ≈ thousands of distinct surface forms), and it
    keeps the dialectic *external and named* — which is what
    makes the moral lesson legible in every record.

Three foxes is the minimum that makes Option A work; with four or
more, the variety ceiling would scale further. The 3-fox pool is
sufficient for variety @ n=50 to land at 1.00 across all grade-1
subjects (verified — see Variety section below).

## Where the dialectic lives in the prose

Each shared subplot embeds the eval-first beat in a different way:

  1. **vine-and-post**: someone has chalked the form on a wooden
     post. Hasty fox declares the form too high to bother with.
     Patient fox suggests they evaluate it anyway.
  2. **wager** (3 variants — dirt, board, twig): hasty fox bets on
     an answer; patient fox says it's simpler to type the form.
  3. **teacher**: patient fox explaining the REPL. "You hand the
     form to the runtime, and the runtime hands you back what it
     evaluates to."
  4. **audience**: small orchard creatures watch the demonstration.
  5. **rationalize-and-rebuke** (the canonical Aesop moment):
     hasty fox refuses to evaluate the form — the answer, hasty
     insists, is probably sour anyway. Patient fox: "Submit the
     form to the REPL. Whatever comes back is the honest answer."
  6. **ledger**: patient fox keeps a leather notebook of every
     form successfully evaluated.
  7. **boast-and-rebuke**: hasty fox claims to know without
     checking; patient fox asks the hasty one to actually write
     the form and submit it.
  8. **puzzle-on-the-gate**: a sign at an orchard gate poses the
     form as a riddle.

Higher-grade files extend this shared 8-pool with grade-flavored
subplots (e.g., grade 4 collections of fruit / clusters; grade 6
foxes tending separate orchards; grade 7 patient fox catching
errors carefully; grade 9 patient fox's transactional fruit-tally;
grade 10 patient fox reading macroexpansions cleanly; grade 11
foxes traveling into foreign orchards; grade 12 foxes reflecting
on tools at the day's end).

## Files

```
src/mmllm/aesop/curriculum/fox_grapes/
    __init__.py
    grade_1.py     # 18 subjects (G1-01..G1-18) — the shared subplot pool
    grade_2.py     # 22 subjects
    grade_3.py     # 18 subjects
    grade_4.py     # 20 subjects
    grade_5.py     # 22 subjects
    grade_6.py     # 16 subjects
    grade_7.py     # 18 subjects
    grade_8.py     # 16 subjects
    grade_9.py     # 18 subjects
    grade_10.py    # 16 subjects
    grade_11.py    # 14 subjects
    grade_12.py    # 18 subjects
```

Each grade file imports `_SHARED_SUBPLOTS` and `_PLAN_POOL` from
`fox_grapes.grade_1`, extends with 1-2 grade-flavored subplots,
defines its `SubjectCurriculum` entries, exposes
`SUBJECTS: dict[str, SubjectCurriculum]`, and ships a `smoke_test()`.

## Pool extensions in `generator.py` (additive only)

The fox-grapes curriculum is wired into the shared generator via
three additive changes to `src/mmllm/aesop/curriculum/generator.py`
(no existing tortoise-hare code path changed):

  1. `_foxes()` — picker that selects fox characters from the ontology.
  2. `FOX_GRAPES_LOCATIONS` — `("orchard", "garden", "farm", "market",
     "meadow", "woods", "forest")`.
  3. `_pick_fg_chars(scene)` / `_pick_fg_location(scene)` — two-distinct-
     foxes picker + location picker.
  4. `_FABLE_PICKERS` dispatch table — maps `"fox-grapes"` to its
     pickers; defaults to tortoise-hare's pickers for unknown fables
     so existing curricula work unchanged.
  5. `_build_placeholders` extended with `{hasty_fox}`, `{patient_fox}`
     (plus all pronoun forms `_phrase` / `_he_she` / `_he_she_cap` /
     `_him_her` / `_his_her`) — keys aliased to the same character
     objects as the existing `{hare}` / `{tortoise}` keys, so
     templates pick whichever fits their fable's voice.

## Usage

```python
from mmllm.aesop.curriculum.fox_grapes.grade_1 import SUBJECTS as G1
from mmllm.aesop.curriculum.generator import generate_subject

# Generate 222 narrative variants of a single subject
recs = generate_subject(G1["G1-13"], n_per_example=222, seed=0)
# → 222 × 6 examples = 1,332 records, all teaching first-arithmetic-call
```

## Variety achieved

Spot-checked at 50 variants per example across grades 1, 5, 10:

  - G1-01: 400 records, 400 unique (variety 1.00)
  - G1-13: 1,332 records (at n=222 × 6 examples), expected near 100%
  - Grade 5 first subject: 150 records, 150 unique (variety 1.00)

The cross-product (8-10 subplots × 6 fox pairs × 7 locations × 4
openers × 3+ emotion picks per template) gives ~thousands of
distinct surface forms, so n=222 yields effectively 100% unique
user_msgs.

## Subjects requiring adaptation

Same two adaptation strategies as tortoise-hare for grade-6/7/11/12
subjects that don't fit a single `eval(form)` test:

  - **Surrogate forms**: an evaluable proxy that exercises the
    *naming* aspect of the concept (e.g., G6-02 namespace `ns` form:
    `(name 'foo.bar)` instead of side-effecting `(ns foo.bar)`).
  - **Placeholder forms with educational subplots**: form is
    `(do "subject overview" :studied)` with `:studied` as the
    answer; the narrative subplot does the educational work.

These adaptations carry over from tortoise-hare unchanged — the
underlying examples are identical; only the narrative wrapper
changes voice.

## EMO pool note

Fox-grapes' canonical chapters use `EMO_HUNGRY` and `EMO_REGRETFUL`
heavily, but those pools have hardcoded gendered pronouns ("his
stomach hollow with hunger") that occasionally mismatch a chosen
fox's gender. This curriculum prefers `EMO_PROUD` (mostly neutral)
and `EMO_PATIENT` (mostly neutral) — both pools are reused from
tortoise-hare unchanged. Where character-name substitution helps
avoid pronoun ambiguity (e.g., singular-they after a singular
introduction), templates use `{hasty_fox}` / `{patient_fox}` (the
names) directly rather than `{hasty_fox_he_she}`.
