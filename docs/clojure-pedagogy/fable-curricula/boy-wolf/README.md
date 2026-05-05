# Boy-who-cried-Wolf — full K-12 Clojure curriculum

This curriculum re-casts the K-12 Clojure framework
(`docs/clojure-pedagogy/framework.md`) through the lens of the
Boy-who-cried-Wolf fable. Every record carries the moral —
**lying erodes trust, and trust once lost cannot be recovered when
it matters** — applied to the discipline of REPL-driven evaluation.

This is the *second* fable-curriculum in the set. The first,
[`tortoise-hare`](../tortoise-hare/README.md), is the canonical
worked example; this curriculum mirrors its structure exactly.

## How the fable maps onto the curriculum

The boy-wolf moral dynamic is a **negative** moral — the protagonist
*is* the cautionary character. That makes the polarity opposite to
tortoise-hare:

| Role in fable | Role in REPL pedagogy |
|---|---|
| The named SHEPHERD (Tom / Will / Pat / Jess / Lou) | Cautionary character. Claims to know an answer without actually evaluating the form. The model's bad-habit baseline that the curriculum is trying to correct. |
| The ELDER / VILLAGER / careful neighbouring shepherd | Corrective voice. Insists on submitting the form to the REPL — "the runtime is the only voice we trust now." The model's correct behavior under eval-first discipline. |

In tortoise-hare, the corrective voice (Tortoise) is itself a model
character — the curriculum's "good guy." In boy-wolf the corrective
voice is **the village around the boy**, not the boy himself. The
shepherd is who the model is being trained *not* to be; the elder /
villager is who the model is being trained to become.

This polarity flip is the load-bearing tonal difference. Subjects
should never have the named shepherd play the patient-evaluator role;
that line always belongs to the elder, the villagers, or a careful
neighbouring shepherd.

## Tonal care

The original boy-wolf fable involves a wolf, a flock of sheep, and a
village that no longer trusts the shepherd's calls. The
`mmllm.aesop.fables` boy-wolf chapters use **measured language** about
the wolf:

> "the wolf gave up and returned to the woods" •
> "sheep bolted in fright and could not be recovered" •
> "tracks that led off into the snow"

Never graphic predation. The dramatic stakes come from the
**waiting-for-help-that-doesn't-come** moment, not from the wolf's
actions. The curriculum subplots maintain the same tonal care: the
wolf is thematic background, not a present antagonist. The conflict
in every record is between the shepherd's careless guess and the
elder's insistence on submitting the form.

## Cast

Drawn from `mmllm.aesop.ontology`:

**Shepherds** (role `liar`+`shepherd`, the cautionary cast):
- Tom (m), Will (m), Pat (n), Jess (f), Lou (f)

**Elders / villagers** (role `everyman`, the corrective cast):
- Bob, Frank, George, Oliver, Alex, Sam, Robin, Morgan (m / n)
- Alice, Carol, Grace (f)

The shepherd-villager pair is freshly drawn per record. With
5 shepherds × 11 villagers × 8 pastoral locations × 8+ subplot
templates × 7 aesopian openers, the cross-product yields well over
30,000 distinct surface forms per subject — variety at n=50 is
essentially 1.00 across the board.

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
| 12 | real-world | 18 | 37 | 8,214 |
| **TOTAL** | | **216** | **513** | **113,886** |

(Counts are targets; final numbers are reported below once authoring
completes.)

## Files

```
src/mmllm/aesop/curriculum/boy_wolf/
    __init__.py
    grade_1.py     # 18 subjects (G1-01..G1-18)
    grade_2.py     # 22 subjects
    ...
    grade_12.py    # 18 subjects
```

Each grade file:
- Imports `_SHARED_SUBPLOTS` and `_PLAN_POOL` from `grade_1`
- Adds 1-3 grade-flavored subplot templates
- Defines its grade's `SubjectCurriculum` entries with `fable="boy-wolf"`
- Exposes `SUBJECTS: dict[str, SubjectCurriculum]`
- Has a `smoke_test()` that generates one record per subject

## Boy-wolf-flavored subplot beats

Eight base subplots in `grade_1.py`, reused across all grades, each
embodying a distinct beat from the fable applied to REPL pedagogy:

1. **The false claim** — shepherd announces an answer without checking; elder insists on the form.
2. **The trust ledger** — a slate tallying forms-submitted vs. claims-without-check; today's entry is the form.
2b/2c. **Trust-ledger variants** — slate at the village hall door; elder's pocket notebook.
3. **The careful villager** — elder gently teaches the shepherd: "the runtime is the only voice we trust now."
4. **The audience** — village crowd watches the shepherd attempt to predict; elder asks for the form proper.
5. **The waiting-for-help** — the fable's signature beat repurposed; the shepherd's claim hangs in the air until the form is actually evaluated.
6. **The end-of-week reckoning** — the reeve walks the meadow and reviews the week's submitted forms.
7. **The boast-and-rebuke** — shepherd boasts; villager insists on actual evaluation just to be sure.
8. **The puzzle on the village board** — a scrap of parchment poses the form as a riddle.

Higher grades layer additional beats on top:
- G2: chain-of-operations on the elder's slate; wager-without-typing
- G3: the village ledger of named values
- G4: collections of pebbles / sheep / marks-on-the-slate
- G5: the same operation repeated cleverly across many things
- G6: trust-as-namespace metaphor — false alarms cross village boundaries the way symbols cross namespace boundaries
- G7: the elder catches what the shepherd's careless throw produced
- G8: different villagers respond to the same call differently (polymorphic dispatch)
- G9: careful transactional ledger updates vs. uncoordinated mutations
- G10: the elder designs a small language of warnings (macros that write other forms)
- G11: trade with neighbouring villages whose REPLs speak different host runtimes
- G12: the long season ends — the village reflects on careful tools

## Variety achieved

The cross-product of (8+ subplots × 5 shepherds × 11 villagers × 8
locations × 7 openers × multiple emotion picks per template) yields a
combinatorial space far larger than any 222-record draw, so variety
score lands at essentially 1.00.

Spot-checked at n=50 records on G1-13:
- 300 records (50 × 6 examples), 300 unique user_msgs — variety 1.00.

## Subjects requiring adaptation

Same general adaptations as tortoise-hare:
- **G6 namespace machinery / G7 IO / G11 host overviews / G12 library
  briefs** — many of these don't fit a single `eval(form)` test.
  Adapted via either:
  - **Surrogate forms** (e.g., `(name 'foo.bar)` for namespace-symbol
    introspection; `(with-out-str (println …))` for IO).
  - **Placeholder forms with educational subplots** — the form is
    `(do "subject overview" :studied)` with `:studied` as the answer;
    the narrative subplot carries the educational content.
- Where tortoise-hare examples used `:hare` / `:tortoise` keywords or
  "hare" / "tortoise" strings, the boy-wolf version swaps in
  thematic analogues: `:wolf`, `:flock`, `:alarm`, `:shepherd`,
  "wolf", "flock", "shepherd". The Clojure subjects themselves are
  identical.

## Audit

Run after any change:

```bash
FABLE=boy_wolf python3 docs/clojure-pedagogy/audits/audit-harness.py
```

The harness is a per-fable router — `FABLE=boy_wolf` loads
`mmllm.aesop.curriculum.boy_wolf.grade_<N>` and writes
`boy-wolf-audit.md`. Same checks as the tortoise-hare default:
variety, singular-they verb agreement, answer leaks, place-preposition
mismatches, said-participle issues, length bounds, DOUBLE_PREP, etc.

Goal: 0 issues across all subjects.
