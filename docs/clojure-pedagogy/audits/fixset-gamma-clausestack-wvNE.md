# Fixset γ — cross-fable Cat-K simplification + detector audit (wvNE)

Branch: `claude/fixset-gamma-clausestack-wvNE`

Parent: `8fab5ca` (integration HEAD: regen crow-pitcher audit MD post-fixset-beta)

## Result summary

| fable          | total before | total after | Δ        | CLAUSE_STACK before | CLAUSE_STACK after | target |
| -------------- | -----------: | ----------: | -------: | ------------------: | -----------------: | -----: |
| tortoise_hare  |          496 |         418 |   −15.7% |                 148 |              **60** |    ≤60 |
| crow_pitcher   |          622 |         496 |   −20.3% |                 265 |              **81** |   ≤100 |
| milkmaid       |          708 |         683 |   − 3.5% |                 116 |              **44** |    ≤80 |
| boy_wolf       |          886 |         770 |   −13.1% |                 201 |              **68** |    ≤90 |
| dog_shadow     |          983 |         761 |   −22.6% |                 253 |              **45** |   ≤110 |
| **TOTAL**      |    **3,695** |   **3,128** | **−15%** |             **1,083** |          **298** |        |

CLAUSE_STACK total: 1,083 → 298 (−785, −72 %).

Compared with the original user-supplied baseline (5,652 issues / 1,119
CLAUSE_STACK), this fixset lands the curriculum at **3,128 / 298**
(−45 % / −73 %) — the gap between 5,652 and 3,695 is fixset-alpha
(boy-wolf) + fixset-beta (milkmaid) which merged to integration HEAD
between this work being assigned and being checked out, leaving γ
to focus on cross-fable infra and the remaining CLAUSE_STACK / detector
audits.

The 3 new γ detectors contribute +442 detections of their own
(TRAILING_PARTICIPLE_CLOSER + ABSTRACT_RESULT_NARRATION across the 5
fables) which are included in the 3,128 total — without them the
post-fix total would be 2,686.

## Step 1 — detector audit

### NUMERAL_LIST_IN_GOAL (was 48 in every fable)

**Smell confirmed.** Every fable carried the SAME 16 source examples
(grade-4: count; grade-5: keep / fold / apply / take / drop / distinct
across 12 entries; grade-12: 3 transducer entries) where `goal_text`
hardcoded an English comma-list of vector elements: *"the vector
containing 1, 2, 3, 4, and 5"*. With ≥4 numerals + ≥3 commas the
detector fires three times per example × 16 examples = 48 hits per
fable.

**Fix.** Rewrote `goal_text` to use a Clojure vector literal — *"the
vector [1 2 3 4 5]"* — which carries no English comma-list. 51
replacements across `grade_4.py / grade_5.py / grade_12.py` in
remaining fables (some fables had already been touched on integration
HEAD) plus 16 in `boy_wolf/_goals.py` (the boy-wolf shared-goals
lookup).

Result: **48 → 0 in every fable**.

### STRING_AS_CHAR_MISCLAIM (was 6 in TH/CP/MM, 7 in BW, 0 in DS)

**Smell traced.** The detector fires when `code_str` is a multi-char
string but the prose says *"the character \X"*. Every fable's G1-08
(Characters) had four char-literal source examples: `\h`, `\space`,
`\T`, `(char? \h)`. Each got auto-parametrized via `auto_parametric`,
which routes any `str` literal through `_infer_pool → STR_SHORT` —
producing strings like `"linen"` and `"saffron"` from the slot pool
while `concept_phrase` still carried *"the character \space"* prose.

**Fix.** Added an `is_char` flag to `Lit` (`expr.py`), set it in
`form_parser.py` for every `\X` parse, threaded it through
`auto_parametric._collect_literals` into `_infer_pool`, and gave
single-char Clojure literals their own `_CharPool` subclass of
`ScalarPool` (in `scalar_pools.py`) that emits values as `\X` not
`"X"`. Now G1-08's parametric draws stay in the character type system
end-to-end.

Result: **6/7 → 0 in every fable**.

### WRONG_FABLE_LITERAL — Pip false-positive in dog_shadow

**Smell traced.** The ghost-name list had `"Pip"` flagged as a
TH-only character. But `character_pools.DOG_NAMES` *also* contains
`"Pip"`, and the dog_shadow narrative legitimately draws Pip as a dog
character — every such draw hit the wrong-fable detector.

**Fix.** Split the ghost list into UNIQUE_GHOSTS (Mossback / Shelly /
Slowpoke / Hopper / Speedwick — names not used in any other character
pool) and AMBIGUOUS_GHOSTS (Pip / Bramble / Whisker / Speedy — names
that legitimately appear in dog/hare/etc. pools). For the ambiguous
class the detector now requires a tortoise-hare species annotation
(`Pip the hare`, `Bramble the tortoise`) before flagging — a
non-TH-fable mention without that disambiguator is treated as a
legitimate same-name draw from a different pool.

Result: **DS 16 → 0; BW 1 → 0**.

### CONCEPT_PHRASE_COMMA_LIST (was 75 in MM and DS)

Both fables' `grade_9.py` (concurrency primitives) had shared
`concept_phrase` strings written as comma-listed Clojure operation
names — *"atom, swap, deref"*, *"agent, send, await, deref"*,
*"ref, dosync, alter, deref"*, etc. The detector flags 3+ comma-
separated bare tokens as a bullet-list-of-ops shape.

**Fix.** Rewrote each as a noun phrase ("the swap-then-deref pattern
on an atom", "the send-await-deref pattern on an agent", "the
dosync-alter-deref pattern on a ref"). Applied to `dog_shadow/grade_9.py`
(milkmaid's grade_9 had already been rewritten by fixset-beta).

Result: **75 → 0 in MM and DS**.

## Step 2 — CLAUSE_STACK_OVERFLOW reduction (1,083 → 298)

### Source-level rewrites

- **submit-the-form chain breakage.** The shared template cadence
  *"composed {concept_phrase}, submitted the form, and the REPL —
  XYZ — returned ..."* was burning 3 commas before any draw. Split
  the chain into two sentences: *"composed {concept_phrase}. The REPL
  — XYZ — returned ..."* in CP / BW / DS / TH `_metaphor_pools.py`
  via three regex passes (91 + 7 + 20 = 118 instances).

- **EMO entries with internal commas.** Multiple entries across 14
  `EMO_*` pools in `emotion_pools.py` were written as 2-clause comma-
  joined phrases: *"with steady, careful steps"*, *"stepping
  deliberately, one foot before the next"*. Each insertion of
  `{emo_X}` into the standard subplot frame *"{actor}, {emo_X}, did
  Y"* burned 2-3 commas before the verb fired. Rewrote the remaining
  20 entries (after fixset-beta's overlap) as comma-free phrases.

- **CP_EMO_PATIENT pool tightened** in `generator.py`: *"watching
  the level lift, drop by drop"* → *"watching the level lift"*;
  *"trusting the process, stone after stone"* → *"trusting the
  stone-by-stone process"*; etc.

- **Subplot openers tightened.**
  - TH grade_1 race-against-the-REPL template: split the 3-clause
    Hare-bolts run into a 2-sentence rhythm; broke the Tortoise-walks
    chain into shorter sentences.
  - CP `_GATE_SUBPLOTS` opener *"paused at the pitcher's rim {place},
    talon raised — the throat was narrow, the day was hot, ..."* —
    tightened to *"paused at the pitcher's rim {place}, talon raised.
    The throat was narrow; the day was hot."*
  - BW / TH / CP / DS *"Once you've sent the runner ahead"* dialogue
    coda — *"sometimes you wait for X; other times you keep arranging
    things until Y."* replaces the prior 4-comma run-on.
  - Vector literals replaced 2 hardcoded *"3, 1, 4, 1, 5, 9, 2, 6"*
    spreads in `grade_5.py` of every fable plus `boy_wolf/_goals.py`.

### Detector-level tightening

- **CLAUSE_STACK_OVERFLOW dialogue-aware.** The original detector
  only skipped sentences with `≥2 "` chars. But `re.split(r"[.!?]\s+",
  user)` splits *inside* dialogue at every `."` boundary, leaving the
  resulting fragments with 0 or 1 quote chars — and any such fragment
  with 5+ commas was flagged as AI-cadence even though the comma
  enumeration was a moralist speaking inside dialogue (*"The chalk
  marks explain the steps below them — first, chill the cream;
  second, churn it; third, press it.\""*).

  Tightened: track quote-balance up to each sentence's start. If the
  prefix `"` count is odd, the sentence began inside an open dialogue
  span and is skipped — the moralist enumeration is idiomatic, not
  AI cadence. This change was the single largest CLAUSE_STACK
  reduction, accounting for roughly half the drop in TH / CP / DS.

## Step 3 — three new detectors

Added at the tail of `check_record` (slice wvNE).

### TRAILING_PARTICIPLE_CLOSER

A sentence that closes with the LLM-signature pattern `, <verb>ing the
<noun>\.` reads as a participial coda — naming a secondary, decorative
event after the main clause has finished. ("returned the value,
settling the matter cleanly.", "waited at the perch, watching the
breeze turn.") The native fable register closes on the verb itself.
The detector REQUIRES a definite article (*the / her / his / its /
their*) after the participle, so a bare *", waiting."* or *",
boasting at every turn."* (an emotion-pool tail) is fine. Excludes
common Clojure-idiomatic verbs (*binding*, *evaluating*, *applying*,
*passing*, *calling*, *using*).

Hits per fable: TH 74 / CP 110 / MM 61 / BW 70 / DS 124 — these are
genuine LLM tails the existing 60+ detectors didn't catch.

### ABSTRACT_RESULT_NARRATION

Meta-narrative phrasings like *"the result of the operation"*, *"the
outcome of the form"*, *"the value that the form produced"*, *"the
return of the expression"* describe what the runtime does in abstract
layered-noun terms. The fable register names the concrete thing —
*"the count"*, *"the answer"*, *"the new pile"*. These layered
abstractions are an AI tic where the model hedges by stacking
nominalizations.

Regex covers `the (result|outcome|return|value) of (the|a|an)? X`
where X ∈ {operation, form, expression, evaluation, computation,
procedure, function call, application}. Hits: 3 per fable
(grade-12 transducer/protocol records that lifted abstract noun
chains from a shared template).

### REDUNDANT_VALUE_TAUTOLOGY

Circular phrasings like *"returned the value the form returned"*,
*"gave back the answer the REPL gave back"*, *"produced the result
the runtime produced"* — collapse into pure tautology, the prose
saying nothing once subject and predicate are matched. Detected by
matching the same verb stem on both sides of an *the X (that|which|
the)* clause. 0 hits in current curriculum (defensive — guards
against future template drift; the existing prose has been
hand-edited away from this shape).

## Verification

```
$ for mod in scalar_pools form_parser form_families auto_parametric \
              character_pools opener_pools emotion_pools; do
    PYTHONPATH=src python3 -m mmllm.aesop.curriculum.$mod 2>&1 | tail -1
  done
scalar_pools.py smoke_test: ok (29 pools)
form_parser.py smoke_test: ok (27/27)
form_families.py smoke_test: ok (82 families × 5 trials = 410 verified)
auto_parametric.py smoke_test: ok (6 forms, prose ok)
character_pools.py smoke_test: ok (1830 names across 13 pools)
opener_pools.py smoke_test: ok (150 openers, 150 plans)
emotion_pools.py smoke_test: ok (199 band entries, 396 archetype entries)

$ PYTHONPATH=src python3 scripts/test_parametric_e2e.py | tail -1
[OK]
```

All 8 smoke modules + e2e pass.

## Files touched

- `docs/clojure-pedagogy/audits/audit-harness.py` — 1 detector
  tightened (CLAUSE_STACK_OVERFLOW dialogue-aware), 1 detector
  refined (WRONG_FABLE_LITERAL UNIQUE/AMBIGUOUS split),
  3 new detectors added.
- `src/mmllm/aesop/expr.py` — `is_char` flag on `Lit`.
- `src/mmllm/aesop/curriculum/form_parser.py` — propagate `is_char` for
  every `\X` parse.
- `src/mmllm/aesop/curriculum/auto_parametric.py` — accept `is_char`
  in `_infer_pool`, dispatch single-char literals to CHAR_LOWER /
  CHAR_UPPER.
- `src/mmllm/aesop/curriculum/scalar_pools.py` — `_CharPool` subclass
  emits `\X` form syntax; CHAR_LOWER / CHAR_UPPER converted.
- `src/mmllm/aesop/curriculum/emotion_pools.py` — 20 EMO entries
  rewritten without internal commas (cross-fable).
- `src/mmllm/aesop/curriculum/generator.py` — CP_EMO_PATIENT comma
  cleanup.
- `src/mmllm/aesop/curriculum/{TH,CP,DS}/_metaphor_pools.py` —
  subplot-template sentence breakage.
- `src/mmllm/aesop/curriculum/{TH,CP,MM,BW,DS}/grade_*.py` — goal_text
  vector-literal rewrites; race-against-the-REPL template tightening.
- `src/mmllm/aesop/curriculum/dog_shadow/grade_9.py` — concept_phrase
  comma-list rewrites.
- `src/mmllm/aesop/curriculum/boy_wolf/_goals.py` — 16 vector-literal
  rewrites in shared goals + 2 walk-pebble rewrites.
- 5 audit MD files regenerated.
