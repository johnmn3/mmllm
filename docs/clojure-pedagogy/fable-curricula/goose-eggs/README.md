# Goose-and-the-Golden-Eggs — full K-12 Clojure curriculum

**216 subjects across 12 grades; 513 examples; ~113,886 training
records when generated at the standard 222 variants/example.**

This curriculum mirrors the tortoise-hare reference (the first
authored fable-curriculum) and is the second to land. The
remaining 8 fable-curricula (crow-pitcher, boy-wolf,
ant-grasshopper, milkmaid, fox-grapes, two-mice, dog-shadow,
lion-bulls) follow the same pattern via
`docs/clojure-pedagogy/SKILL-fable-curriculum-author.md`.

## How the fable maps onto the curriculum

The goose-eggs moral dynamic — **greed vs. patience** — informs
every record:

- **`{visitor}`** is the impatient guesser, the visitor or
  neighbor who wants the answer at once. "I can see it without
  evaluating." The visitor is the model's former bad habit:
  pattern-matching to a numeric answer instead of producing the
  form. Greed-as-shortcut.
- **`{owner}`** is the patient evaluator, the goose-keeper who has
  learned that the runtime tells the truth. "Submit the form to
  the REPL. Whatever comes back is the answer." Patience-as-
  correctness.
- **`{goose}`** is the value-yielding bird whose **one egg per
  morning** routine parallels the REPL's **one form, one returned
  value** rhythm. The fable's underlying caution — never kill the
  goose for all the gold at once — becomes never demand the answer
  faster than the runtime can compute it. The goose is rarely the
  speaker; she/he/they stand quietly in many subplots, the steady
  rhythm against which greed and patience play out.

Across all 216 subjects, the same characters keep playing out the
same dynamic over different Clojure concepts. The model sees the
moral lesson reinforced thousands of times in hundreds of surface
forms — and crucially in **different scenery** from tortoise-hare:
farmhouse stoops, market stalls, kitchen tables, hearth-side
ledgers, barn-door notices, village signposts. A model trained on
records from both fables sees the same Clojure concept appear in
a vastly larger surface-form space than any single fable can
provide.

## Cast pool (vs. tortoise-hare)

Where tortoise-hare uses 4 hares × 3 tortoises = 12 character
pairings, goose-eggs uses ~22 human "trader" characters as owners
and visitors (drawn from `ont.HUMANS`'s broad name pool — Bob,
Alice, Charlie, Beatrice, Sam, Jordan, Casey, Morgan, …) plus
3 named geese (Quill, Honk, Plume). Per-record draws give
roughly **22 × 21 × 3 ≈ 1,400 character configurations** before
location and subplot variation enter the cross-product.

Locations: farm, village, market, barn, cottage, kitchen, cellar,
orchard, meadow — 9 indoor/outdoor scenes that cover the fable's
domestic-and-village setting. The tortoise-hare path-locations
(road, hilltop, forest, woods) are deliberately excluded — those
belong to the racing fable.

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
src/mmllm/aesop/curriculum/goose_eggs/
    __init__.py
    grade_1.py     # 18 subjects (G1-01..G1-18) — also defines _SHARED_SUBPLOTS + _PLAN_POOL
    grade_2.py     # 22 subjects
    ...
    grade_12.py    # 18 subjects
```

Each grade file:
- Imports `_SHARED_SUBPLOTS` and `_PLAN_POOL` from `goose_eggs.grade_1`
  (NOT from `tortoise_hare.grade_1`)
- Extends them with 1-7 grade-flavored subplots (counting eggs into
  baskets, ledger entries beside coin-tallies, market trips, the
  patience-vs-greed dynamic re-cast for that grade's topic) and
  grade-flavored plan-pool entries
- Defines its grade's `SubjectCurriculum` entries with `fable="goose-eggs"`
- Exposes `SUBJECTS: dict[str, SubjectCurriculum]`
- Has a `smoke_test()` that generates one record per subject

## Generator extension

The generator (`mmllm/aesop/curriculum/generator.py`) was extended
**additively** (per the SKILL doc's hand-off rules) to support
goose-eggs:

- New picker: `_pick_ge_chars(scene)` returns `(owner, visitor, goose)`
  drawn from `_ge_owners()` (22 human "trader" characters with
  fable-conflicting roles excluded) and `_ge_geese()` (3 named geese).
- New location picker: `_pick_ge_location(scene)` over the 9
  village + household locations.
- New placeholder builder: `_build_ge_placeholders(scene, owner,
  visitor, goose, location, example)` produces:
  - `{owner}`, `{owner_phrase}`, `{owner_he_she}`, `{owner_him_her}`,
    `{owner_his_her}`, `{owner_he_she_cap}` (and the analogous
    `{visitor_*}` / `{goose_*}` keys)
  - The tortoise-hare-style `{hare}`/`{tortoise}` aliases (mapped
    to `visitor`/`owner` respectively) so the shared 8 subplots
    keep rendering naturally
  - `{form_display}`, `{concept_phrase}`, `{place}`, `{location}`,
    `{what}`
  - Pronoun-neutral emotion picks: `{emo_proud}`, `{emo_patient}`,
    `{emo_tired}`, plus three new pools tailored to this fable —
    `{emo_greedy}`, `{emo_content}`, `{emo_regretful}` — that
    avoid the hard-coded `his/her` pronouns of the original
    `EMO_GREEDY` / `EMO_CONTENT` / `EMO_REGRETFUL` from `fables.py`.
- `generate_one_record` dispatches on `sub.fable == "goose-eggs"`
  to use the new pickers/builder; the tortoise-hare path is
  unchanged.

## Usage

```python
from mmllm.aesop.curriculum.goose_eggs.grade_1 import SUBJECTS as G1
from mmllm.aesop.curriculum.generator import generate_subject

# Generate 222 narrative variants of a single subject
recs = generate_subject(G1["G1-13"], n_per_example=222, seed=0)
# → 222 × 6 examples = 1,332 records, all teaching first-arithmetic-call
#   wrapped in the goose-eggs greed-vs-patience moral.
```

## Variety achieved

Sampled at 222 variants/example across all grades — **every
subject scores ≥ 0.95 unique user_msg / record**, with most
landing at 1.000. The cross-product (8-15 subplots × ~22
owners × ~21 visitors × 3 geese × 9 locations × 4 openers) is
combinatorially huge; n=222 hits unique on essentially every draw.

## Audit status

The curriculum-wide audit harness
(`docs/clojure-pedagogy/audits/audit-harness.py`) reports
**0 issues** across all 216 subjects on first pass and re-pass:

- Word-count compliance (35-200 words/user_msg)
- No singular-they verb agreement violations
- No un-substituted placeholders
- No answer-leak in narrative
- No nested-`computes`, no aside-parens, no em-dash commentary
- No `said-{participle}` without comma
- No double-from, no place-prep mismatches, no
  `stopped-across-X` verb-prep mismatches
- No meta-meta question_what

## Subjects requiring adaptation

Same as tortoise-hare: G6 namespace machinery, G7 IO, G11 host
overviews, G12 library briefs use surrogate forms (e.g.,
`(name 'foo.bar)` for namespace-symbol introspection,
`(do "..." :studied)` for pure-overview subjects, with-out-str
for *out* redirection). The narrative subplots in goose-eggs
re-skin these without changing the underlying eval-call shape:
the model emits the same form regardless of the surrounding
fable, and learns both the Clojure concept and the moral
flavor it is carried by.

## Connection to tortoise-hare

A model trained on **both** curricula sees the same Clojure
concept (e.g., G1-13 "First arithmetic call") rendered as:

- **Tortoise-hare**: race-pause where the hare boasts and the
  tortoise insists on evaluation, set on a forest path or
  hilltop, named characters drawn from 4 hares × 3 tortoises.
- **Goose-eggs**: market-stall wager or kitchen-ledger
  reconciliation where the visitor wants the answer at once and
  the owner counts patiently, set in a village/farm/cottage,
  named characters drawn from 22 traders × 22 traders × 3 geese.

Same Clojure form. Same expected value. Wildly different surface
text. That is the curriculum's central pedagogical bet: model
capacity that goes into recognizing "the form the user wants me
to submit" is robust to narrative dressing, and the 10 fables in
combination give it ~10× the surface-form variety any one fable
can produce.
