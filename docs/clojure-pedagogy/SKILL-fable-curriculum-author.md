# Skill: authoring a fable-curriculum

This document teaches another agent how to take ONE Aesop's fable
and produce the complete K-12 Clojure curriculum re-cast through
that fable's narrative lens. The work was first done end-to-end for
**tortoise-hare** at `src/mmllm/aesop/curriculum/tortoise_hare/`;
the patterns below are the codified recipe.

## Goal

For your fable F, produce ~215 `SubjectCurriculum` definitions —
one per subject in the K-12 framework
(`docs/clojure-pedagogy/framework.md`) — each generating ≥ 222
unique narrative variants per example.

Total output for one fable:
   ~215 subjects × ~5 examples avg × 222 variants
   ≈ 240,000 training records.

## Inputs you need

1. **The K-12 framework**: `docs/clojure-pedagogy/framework.md`
   — lists every subject ID and title.
2. **Your fable's character pool**: characters whose `species`
   matches your fable in `src/mmllm/aesop/ontology.py`. For example,
   crow-pitcher uses crows; goose-eggs uses geese + their human owners.
3. **Your fable's narrative dynamic**: read
   `src/mmllm/aesop/fables.py` `FABLE_OPENERS[<fable>]` to internalize
   the moral tension. For tortoise-hare it's vanity vs. steadiness;
   for crow-pitcher it's cleverness in adversity; etc.
4. **The exemplar**: `src/mmllm/aesop/curriculum/tortoise_hare/grade_1.py`
   is the canonical reference. Mirror its shape.

## Output structure

```
src/mmllm/aesop/curriculum/<your_fable>/
    __init__.py
    grade_1.py     # 18 subjects
    grade_2.py     # 22 subjects
    ...
    grade_12.py    # 18 subjects
```

Each `grade_N.py` exports a `SUBJECTS: dict[str, SubjectCurriculum]`
mapping subject id (`"G1-01"`) to its curriculum definition. Plus a
`smoke_test()` that generates one record per subject and verifies shape.

## The shape of a subject

```python
SUBJECT = SubjectCurriculum(
    grade=1,
    subject_id="G1-01",
    subject_title="Eval as substitution",
    fable="<your fable>",
    examples=[
        SubjectExample(
            form="(+ 1 2)",                        # the Clojure source
            expected=3,                            # what the form evaluates to
            concept_phrase="the form (+ 1 2)",     # noun-phrase for narrative
            question_what="the result of (+ 1 2)", # noun-phrase for question
        ),
        # ... 4-10 examples per subject ...
    ],
    subplots=[SubplotTemplate(template="""..."""), ...],   # 6+ templates
    plan_pool=("I write the form...", ...),       # 4-6 plan-only prefaces
)
```

## Writing examples

Each example pins down what Clojure form the model should write and
what value it produces.

- `form`: the Clojure source. Single-line preferred; multi-line OK
  if the form is genuinely multi-line (e.g., a `let` with several
  bindings).
- `expected`: the value evaluating the form produces. NEVER appears
  in user_msg or assistant_msg — used only by the verifier.
- `concept_phrase`: a noun-phrase the subplot weaves in:
  > "Bramble pointed to **the form `(+ 1 2)`** etched into a stone."
  Should make grammatical sense in any subplot context.
- `question_what`: a noun-phrase the closing question wraps around:
  > "Write a Clojure expression that computes **the result of (+ 1 2)**."

### Example coverage per subject

5-10 examples per subject is the sweet spot.
- Atoms-style subjects (G1-02 integers, G1-04 strings): 5-6 examples
  spanning the value-space (positive, negative, zero, boundary cases).
- Operator subjects (G1-13 first-arithmetic): 6-8 examples covering
  +/-/*/, with diverse operands.
- Predicate subjects (G1-15 equality, G1-16 numeric-predicates):
  6-8 examples covering both `true` and `false` outcomes.
- Higher-grade subjects scale similarly.

## Writing subplots

A subplot is a Python format string with named placeholders. The
generator fills these from (character pool × location pool ×
emotion pool × example).

### Required placeholders
- `{form_display}` — the form, backtick-wrapped: `` `42` ``
- `{concept_phrase}` — example.concept_phrase
- `{place}` — "near the hilltop", "in the meadow"
- Two character placeholders specific to your fable. For
  tortoise-hare: `{hare}` / `{tortoise}` and their phrases /
  pronouns. For your fable: pick the two main characters and
  expose them analogously. See `_build_placeholders` in
  `generator.py` to extend.

### Optional placeholders
- `{emo_proud}`, `{emo_patient}`, `{emo_tired}`, etc. — single
  picks from `EMO_*` pools. Use to add character-flavored manner.

### Subplot pool size: 6-8 templates

Each template should embody a different narrative beat:
1. The **argument** — characters disagree about the answer; the
   form is what they should evaluate to settle it.
2. The **wager / bet** — one character bets they know what the
   form returns.
3. The **teacher** — one character explains to the other how the
   REPL works using this form.
4. The **audience** — onlookers watch the demonstration.
5. The **race-pause** / **action-interrupt** — the fable's central
   action pauses for a quick REPL question.
6. The **notebook / ledger** — a character keeps a written record
   of forms they've evaluated.
7. The **boast-and-rebuke** — one character claims to know without
   evaluating; the other insists they actually evaluate.
8. The **puzzle-on-the-path** — a sign / engraving / scrap of
   parchment poses the form as a riddle.

These 8 are the patterns that worked for tortoise-hare. Other
fables will have natural-fitting variants:
- **Crow-pitcher**: the "thirsty calculation" pattern (the crow uses
  a form to estimate how many stones it needs), the "stone-by-stone
  ledger" pattern.
- **Goose-eggs**: the "ledger" patterns (counting eggs/coins),
  "market-tally" patterns.
- **Boy-wolf**: the "village-tally" pattern (counting alarms).

You don't need to use the same 8 patterns as tortoise-hare. Pick
patterns that flow naturally from your fable's setting and props.

### Subplot constraints

- **Never reveal the answer** in the subplot. The form may appear,
  the noun-phrase may appear, but the numeric/string answer must
  not appear in narrative prose. This is the eval-first principle:
  the model produces the form; the runtime computes the answer.
- **Subplots must work for ALL examples in the subject.** Don't
  hard-code "the integer 7" in a subplot — use `{form_display}`
  and `{concept_phrase}` so the same template renders correctly
  for `42`, `"hello"`, `(+ 1 2)`, etc. If a particular template
  only fits some examples, mark it with `fits_tags=("arithmetic",)`
  and tag the relevant examples.

## Plan pool

A short list of plan-only prefaces — single sentences describing
HOW the model approaches the problem (never the answer). Example
for grade 1:

```python
PLAN_POOL = (
    "I write the form and let the REPL evaluate it.",
    "I submit the form to the REPL via the eval tool.",
    "I let the REPL do the evaluation.",
    "I express the form as Clojure source.",
)
```

For higher grades these get more specific:
- G3 (let / def): "I bind the inputs in a let, then compute."
- G5 (reduce): "I reduce + over the sequence."
- G10 (macros): "I expand the macro with macroexpand."

50% of records emit no preface; the other 50% pick from this pool
or from a chapter-specific plan. Keep entries SHORT (one sentence)
and ABSTRACT (don't reference specific values).

## Sharing infrastructure

The shared `_SHARED_SUBPLOTS` list in
`tortoise_hare/grade_1.py` is reused across all 18 grade-1 subjects.
This is the right pattern: write 6-8 subplots ONCE per grade
(or per layer), and have all subjects within that grade reference
the shared list.

For grade-specific narrative beats (e.g., grade 4 "the tortoise
sorts pebbles into a vector"), introduce a grade-specific subplot
list that supplements the shared one.

## Validating output

```python
from mmllm.aesop.curriculum.<your_fable>.grade_1 import smoke_test
smoke_test()
```

Plus a stronger check: generate 222 records of one example and
confirm at least 200 are unique:

```python
from mmllm.aesop.curriculum.generator import generate_subject
recs = generate_subject(SUBJECTS["G1-01"], n_per_example=222, seed=0)
assert len({r.user_msg for r in recs[:222]}) >= 200, "low variety"
```

If variety is low: enlarge subplot pool, vary location pool, add
emotion-pool placements.

## Grade-by-grade subject lists

Use `docs/clojure-pedagogy/framework.md` as the source of truth.
Subject IDs follow `G<grade>-<two-digit-index>` zero-padded.

### Working through a grade

For each subject:
1. Write 5-10 `SubjectExample` entries covering the concept's
   value-space.
2. Verify the subplot pool's templates work with those examples
   (re-run smoke).
3. Add subject-specific subplot variants if the shared pool reads
   awkwardly for that subject (e.g., G1-15 equality wants an
   "argument settled by checking" beat that the shared pool
   already supports — but G3 might want a "naming ceremony" beat).

### Higher-grade subjects: math vs. structural

Grades 1-2 are pure value-and-arithmetic.
Grades 3-5 introduce binding, collections, and higher-order. Subplots
need to grow in scope:
- G3 subplots can frame the form as a small recipe ("Bramble called
  for `(let [...] ...)` to settle the question").
- G4 subplots feature collections of objects ("a basket of pebbles
  Bramble had been counting").
- G5 subplots feature decisions and repetitions ("at every milestone,
  Shelly checked …").

Grades 6-12 deal with code organization, errors, polymorphism,
concurrency, macros, interop, and real-world libraries. The fable's
narrative scaffolding still applies, but the subjects are mostly
about Clojure machinery, not arithmetic. Subplots focus on the
form being submitted; the narrative becomes more about the
characters' attitudes toward the form than about the arithmetic
of the form.

## Common mistakes (anti-patterns to avoid)

These are bugs the tortoise-hare reference implementation found and
fixed during its own audit pass. Apply the lessons up front.

### 1. Pronoun case bugs (subjective vs objective)

A template like `"asked {hare_he_she} to actually..."` produces
ungrammatical text when the character has gender="n":

> "asked **they** to actually..."   ← wrong, should be "asked them to"

`{hare_he_she}` returns *subjective-case* pronouns ("he"/"she"/"they")
which only fit subject position. For object position use
`{hare_him_her}` ("him"/"her"/"them"). The placeholder set in
`generator.py`'s `_build_placeholders` exposes both:

| Position | Placeholder | Renders as |
|---|---|---|
| Subject  | `{hare_he_she}` | he / she / they |
| Object   | `{hare_him_her}` | him / her / them |
| Possess  | `{hare_his_her}` | his / her / their |

If you write a template with a character in OBJECT position, ALWAYS
use the `_him_her` form. Audit fix tier-1.

### 2. Answer-leak in question_what or concept_phrase

The eval-first design's whole point is that the answer never appears
in the user_msg or assistant_msg outside the eval form. Common
violations:

- `question_what="the value 10 returned when ..."` — leaks 10.
- `concept_phrase="the form (* 7 6) (a correct form among many possible
  attempts)"` — meta-commentary that includes the answer 42 by
  coincidence ("possible **attempts**" → "**42** possible..."): not
  caught by simple integer checks.

Rule: `concept_phrase` and `question_what` must NOT contain the
answer's literal value. Reference the operation: `"the value when 5
is doubled"` instead of `"the value 10 returned"`. Audit fix tier-1.

### 3. Concept_phrase too long / contains meta-commentary

Concept_phrases work well when they're short, factual, noun-phrase
descriptors of the form. They fail when they include instructional
asides:

> BAD: `"the form (+ 1 2) (a correct form; not all guesses are correct,
>        but mistakes in the REPL are recoverable)"`
> GOOD: `"the form (+ 1 2)"`

The instructional aside leaks into the user_msg awkwardly because the
subplot may interpolate concept_phrase mid-sentence: "...drew {concept}
on a stone" becomes a 100-char run-on with parenthetical. Keep
concept_phrase under 60 chars; put pedagogical commentary in the
subject's lesson_plan section, not in the example's concept_phrase.

### 4. Concept_phrase that duplicates the form's literal text

If `concept_phrase = "the form (assoc {:a 1} :b 2)"` AND the same
subplot also interpolates `{form_display}` (the form rendered as
`` `(assoc {:a 1} :b 2)` ``), the rendered user_msg contains the form
TWICE, once with backticks and once without:

> "...whoever guessed the result of `(assoc {:a 1} :b 2)` first..."
> "...than to argue about **the form (assoc {:a 1} :b 2)**."

Both refer to the same thing; the second feels redundant. Prefer
abstract concept_phrases (`"the assoc form"`, `"the predicate"`,
`"the multi-arity sum"`) over phrases that re-emit the literal form.

### 5. `generate_subject(sub, n_per_example=N)` returns N × len(examples) records

A common pitfall when writing audit code: the return value is
**N records per example**, not N records total. If the subject has 6
examples and you call with `n_per_example=10`, you get 60 records
covering all 6 examples — not 10 records of one example.

To run a check tied to ONE example's expected value, filter:

```python
recs = generate_subject(sub, n_per_example=N, seed=...)
target = [r for r in recs if r.code_str == example.form]
```

This bug bit the first cut of the audit harness — early reports of
"175 issues" turned out to be 169 false positives caused by checking
records of example A against example B's expected value.

### 6. Form stripping requires escape-aware regex when checking asst_msg

The assistant message contains the JSON tool call:

```json
{"tool_calls":[{"name":"eval","args":{"form":"(do (println \"hi\") 42)"}}]}
```

If you want to check whether the answer "42" appears in the asst
OUTSIDE the form arg, a naive regex like `r'"form":"[^"]*"'` won't
strip the form correctly because the form string can contain escaped
quotes (`\"hi\"`). The correct strip:

```python
re.sub(r'"form":"(?:[^"\\]|\\.)*"', '', asst)
```

Otherwise the regex stops at the first internal `\"` and leaves the
rest of the form (including any digits) in the "outside" text, causing
spurious leak reports.

### 7. Runtime-feature requirements (basilisp / Clojure compatibility)

Forms in grade 6+ may rely on runtime features:

- **Java interop** (`(.toUpperCase "abc")`, `(Math/sqrt 2.0)`) — works
  on JVM Clojure, doesn't on basilisp (Python host).
- **clojure.string** — usable on JVM Clojure with `(:require
  [clojure.string :as s])`; on basilisp, namespace must be requireable.
- **Exceptions** (`(try ... (catch Exception e ...))`) — Java
  Exception class on JVM, Python `Exception` on basilisp. The form
  works syntactically on both but the catch-class differs.
- **defprotocol / extend-type / defmulti** — all supported but
  semantics differ slightly between hosts.

When writing examples for grades 6+, prefer:
- forms that work on BOTH JVM-Clojure and basilisp (e.g. wrapping
  exceptions in a `do` so any error catches), OR
- mark the example with a `tags=("jvm-only",)` or `tags=("basilisp-only",)`
  and let the corpus prep filter accordingly.

### 8. Hard-coded literals in subplot text

A subplot that says `"...wrote the form (+ 1 2) on a stone..."`
hard-codes the form. It only works for one example. Always use
`{form_display}` and `{concept_phrase}`. Lint your subplot pool by
running every example through every subplot and inspecting outputs.

### 9. Variety drops below 0.95

Generating 222 records but only seeing ~50 unique surface forms means
the subplot pool is too small relative to the example count. The
tortoise-hare reference uses 8 base subplots + 2 grade-flavored ≈ 10
templates × ~7 hares × 3 tortoises × 7 path-locations × 5 openers ≈
~7,000 distinct combinations. With this combinatoric, n=222 yields
~221 unique user_msgs.

If your variety drops below 0.95, the probable cause is one of:
- Subplot pool < 6 templates (insufficient narrative breadth)
- Character pool < 4 characters per role (e.g., only 2 hares to pick from)
- Location pool < 5 locations
- Opener pool < 4

### 12. Participle-after-"said" needs a comma

A subplot template like:

```
"There is no need to evaluate that," {hare_phrase} said {emo_proud}.
```

reads ungrammatically when EMO_PROUD is a participle phrase:

> "...said boasting at every turn."     ← wrong
> "...said puffed up with pride."       ← wrong
> "...said swaggering through the underbrush."  ← wrong

These need a comma to parse the participle as adverbial:

> "...said, boasting at every turn,"    ← right

EMO pools mix prepositional phrases ("with a smug grin") with
participle phrases ("boasting at every turn"). The prep phrases work
without commas; the participles don't. The safe template change is to
ALWAYS comma-bracket the EMO phrase:

```
"...," {hare_phrase} said, {emo_proud}.
```

The audit harness flags `said\s+(boasting|puffed|swaggering|with a smug grin)`
in user_msg as `SAID_PARTICIPLE`. A test on 1600 records confirms 0
remaining occurrences after the comma fix.

### 13. Double-"from" in tired-hare templates

A teacher subplot like:

```
{hare}, {emo_tired} from a recent sprint, agreed to try.
```

duplicates the preposition when EMO_TIRED entries already include "from
X":

- `"her legs heavy from sprinting"` → "from sprinting from a recent sprint" ← duplicate
- `"weary from the morning's effort"` → "from the morning's effort from a recent sprint" ← duplicate
- `"drowsy from the warm sun"` → "drowsy from the warm sun from a recent sprint" ← awkward but not strictly wrong

Fix: drop the "from a recent sprint" tail in the template. The fatigue
is conveyed by EMO_TIRED itself.

The audit harness flags `from \w+ing from a recent` in user_msg as
`DOUBLE_FROM`.

### 14. Trailing parenthetical or em-dash commentary in question_what / concept_phrase

A concept_phrase or question_what like:

> `"the value of the string \"42\" (note: not the number 42)"`
> `"whether 0 is nil (it isn't)"`
> `"the form (and 1 2 3) — note: returns last truthy"`
> `"the value 42 (the REPL returns it; doesn't 'print' it)"`

carries pedagogical commentary that bloats the rendered text without
adding training signal. The instructional intent ("it isn't",
"returns last truthy") belongs in the subject's `## Common mistakes`
section of the lesson plan, not in the example's data.

The audit harness flags these as `ASIDE_PAREN` (parenthetical) and
`EMDASH_COMMENTARY` (em-dash followed by `note|first|empty|returns|integer`).
The `noise-sweep.py` script applies regex rewrites to strip them
mechanically.

### 15. Meta-meta question_what

A question_what like `"the value the form 42 evaluates to"` wraps
inside the question template `"Write a form whose evaluation gives X"`
and produces:

> "Write a form whose evaluation gives the value the form 42 evaluates to."

The "form ... evaluates to ... evaluates to" loop is meta-meta — the
question is referring to the form referring to its own evaluation.
Simplify question_whats to direct value-descriptions:

- `"the value of 42"` instead of `"the value the form 42 evaluates to"`
- `"the value of nil"` instead of `"the value of the form nil"`
- `"the result of (+ 1 2)"` instead of `"the result of (+ 1 2) (the REPL returns its result)"`

### 16. Question_what containing extra whitespace from the form

For G1-11 (whitespace-doesn't-matter) and similar, putting the literal
spaced form in question_what produces:

> "the result of (+    1    2)"  → "Write a form whose evaluation gives the result of (+    1    2)."

The extra spaces leak into prose. Use a simpler question_what like
`"the result of the form"` and let `form_display` carry the visual
spacing.

### 11. Subplot template + concept_phrase duplication (the form-form pattern)

A subplot template that says:

```
"The form {form_display} described {concept_phrase}, and ..."
```

renders awkwardly when `concept_phrase` itself starts with "the form X":

> "The form `(into [] '(1 2 3))` described **the form (into [] '(1 2 3))**, and..."

The form appears twice — once with backticks (form_display) and once
without (concept_phrase) — within five words. The duplication isn't
strictly wrong, but reads as repetitive prose.

Two ways to avoid it:

**Option A — write subplot templates that don't co-locate form_display
and concept_phrase**: structure the template so each placeholder appears
in a different sentence or with intervening prose. The G4 collection
subplots were rewritten this way — they no longer say "form X described
form Y".

**Option B — use semantic noun-phrase concept_phrases instead of
"the form X"**: for example, `"an indexed access"` (G4-02) or
`"an addition"` (G1-13) instead of `"the form (nth [10 20 30] 0)"` /
`"the form (+ 1 2)"`. This requires the noun-phrase to read naturally
in subplot prose like "wrote {concept_phrase} on a stone" — which
"an indexed access" does, awkwardly. So this option is harder to
get right. Option A is preferred.

The audit harness can't catch this issue automatically (it's prose
quality, not structural). Manual spot-check the rendered output for
each new subplot template, sampling examples with both short forms
("(+ 1 2)") and longer forms ("(let [a 1 b 2] (+ a b))") to see
whether the prose flows.

### 10. Genericizing the fable away

The whole point is that the reader feels they're inside YOUR fable.
Use the fable's characters, settings, props, and moral dynamic. Don't
write generic "a clever student approached the problem" subplots —
use the named characters constantly. The Aesopian opener at the top
+ named characters in subplots is what gives each fable its distinct
narrative voice.

## Recommended audit harness

Every fable-curriculum should ship with a smoke + variety + answer-leak
audit. Reuse the harness at:

```
/tmp/audit_curriculum.py     (in the tortoise-hare repo state)
docs/clojure-pedagogy/audits/<your-fable>-audit.md  (output)
```

The harness checks:
1. **Variety per subject**: generates 50 records, counts unique user_msgs,
   flags subjects below 0.95.
2. **Singular-they verb agreement**: regex for `\bthey\s+eats\b` etc.
3. **Un-substituted placeholders**: detects `{form_display}`, `{place}`
   leaking into rendered output (would mean a placeholder rename
   wasn't propagated).
4. **Answer leakage**: integer answers > 5 that appear in user_msg or
   asst_msg outside the eval form.
5. **Multi-line forms paired with on-stone subplots**: cosmetic flag.
6. **Long concept_phrases** (> 80 chars).
7. **Nested 'computes' in question_what**.

Run after every grade is written. Fix issues immediately while the
context is fresh.

### Form-correctness check (optional but recommended)

For grades 1-5 (atoms / arithmetic / naming / collections / control),
forms can be evaluated via basilisp to verify `expected` matches
runtime behavior. The `/tmp/form_eval_check.py` harness samples
forms-per-grade, sends them to basilisp in one batched script, and
compares results.

For grades 6+ (interop / requires / exceptions), basilisp may not
support all forms. Skip those when running the form-correctness check;
they should be tested against actual JVM Clojure if available.

## Hand-off check

You're done when:
1. All 12 `grade_N.py` files exist and pass their smoke tests.
2. Cumulative subject count is in the 200-220 range across all grades.
3. A spot-check of 5 random records per grade reads as natural
   variations of YOUR fable, not generic Aesopiana.
4. `docs/clojure-pedagogy/fable-curricula/<your-fable>/README.md`
   has a one-paragraph summary of how your fable's character pool
   and moral dynamic are mapped onto the curriculum.

## Lessons from tortoise-hare (the reference implementation)

These are findings from authoring tortoise-hare end-to-end. Apply
them when authoring your fable-curriculum.

### Subjects that don't fit eval-form testing

Several subjects in middle and high school don't naturally produce
"write a form, see a value." Examples:

- **G6 namespace machinery** (`ns`, `require`, `refer`, circular
  deps, classpath, lein/deps.edn): namespaces are loaded by side
  effect, not evaluated.
- **G7 IO** (`slurp`, `spit`, `with-open`, `*in*`, shell): touches
  the filesystem.
- **G11 host overviews** (JVM/CLR/JS/Python intro, ClojureScript
  overview, basilisp overview, .cljc reader conditionals).
- **G12 library briefs** (pedestal/ring, datomic/xtdb, reagent).
- **G12-04 core.async introduction**: channels and go-blocks
  don't fit single-form eval.

Two adaptation strategies the tortoise-hare curriculum used:

1. **Surrogate forms**: an evaluable proxy that exercises the
   *naming* aspect of the concept, even if the runtime aspect
   isn't directly testable. E.g., G6-02 `ns` form: instead of
   evaluating `(ns foo.bar)` (which has filesystem side effects),
   evaluate `(name 'foo.bar)` to teach symbol-name introspection.
   E.g., G7 IO subjects use `with-out-str` and string manipulation
   instead of touching files.

2. **Placeholder + narrative-carries-the-content**: form is
   `(do "subject-overview-string" :studied)` with `expected=":studied"`.
   The narrative subplot does the educational work; the eval call
   just confirms the shape "I read the overview and submit my
   marker."

Pick (1) over (2) where possible — surrogates train more useful
muscle. (2) is acceptable for pure-overview subjects.

### Subplot placeholders that work

The standard placeholders (`{form_display}`, `{concept_phrase}`,
`{place}`, plus `{hare}/{tortoise}` analogues for your fable) are
sufficient for ~90% of templates. For grade-flavored variation,
you can extend `_build_placeholders` in `generator.py` (e.g., add
`{emo_content}`, `{emo_thirsty}` if your fable uses those EMO_*
pools heavily).

### Variety per example

The standard cross-product (8-10 subplots × 7+ characters × 7+
locations × 4-5 openers) yields >2,000 distinct surface forms.
At n=222 records per example, expect 220-222 unique user_msg
(variety score near 1.00). If your variety drops below 0.95,
the subplot pool is too small or the character/location pool is
too narrow.

### Per-grade subplot extensions

Reusing `_G1_SHARED_SUBPLOTS` across all grades is the right base.
Each grade then adds 1-3 grade-flavored subplots:
- G3: a "naming ceremony" or "ledger of bindings" subplot
- G4: a "collection of pebbles / milestones / paw-prints" subplot
- G5: a "same operation repeated cleverly" subplot
- G6: characters working in different namespaces / cottages
- G7: tortoise tries / catches / retries
- G8: different species (creatures) responding to the same call
- G9: tortoise's careful transactional updates vs hare's racing
- G10: the tortoise designs a small language
- G11: the tortoise crosses into a foreign land
- G12: the long race finally ends — tools-at-the-finish-line

Don't try to invent NEW subplots for every grade — the shared
8 from G1 cover most subjects fine. Add 1-2 grade-specific ones
where the grade's theme genuinely calls for new framing.

### Examples per subject

3-5 examples per subject is the sweet spot. Less than 3 = the
subject under-covers its value space. More than 5 = the variant
generator is doing the diversity work anyway.

For boundary subjects (G1-02 integers spanning positive/negative/
zero/large), 5-6 examples cover the value space well. For
operator subjects (G2-05 quot/rem/mod), one example per operator
is enough. For overview-style subjects, 2-3 examples is plenty.

## Coordinating with other fable-curriculum agents

Other agents are doing the same work for the other 9 fables. To
avoid stepping on each other:
- Each fable's curriculum lives in its OWN directory:
  `src/mmllm/aesop/curriculum/<fable>/`. No file conflicts.
- Each fable's curriculum docs live in:
  `docs/clojure-pedagogy/fable-curricula/<fable>/`.
- The shared infrastructure (`generator.py`,
  `framework.md`, `subject-template.md`) is read-only; if you find
  a bug, file a note in your README and let the human author fix it
  centrally.

## Example: end-to-end

A complete grade-1 implementation lives in
`src/mmllm/aesop/curriculum/tortoise_hare/grade_1.py`. Read it.
The pattern is:

```python
_SHARED_SUBPLOTS = [SubplotTemplate("..."), ...]
_PLAN_POOL = ("I write the form...", ...)

def _ex(form, expected, concept, what):
    return SubjectExample(form=form, expected=expected,
                          concept_phrase=concept, question_what=what)

G1_01 = SubjectCurriculum(
    grade=1, subject_id="G1-01",
    subject_title="Eval as substitution",
    fable="tortoise-hare",
    examples=[
        _ex("42", 42, "the value 42", "the value the form 42 evaluates to"),
        # ...
    ],
    subplots=_SHARED_SUBPLOTS,
    plan_pool=_PLAN_POOL,
)
# ... 17 more subjects ...

SUBJECTS = {s.subject_id: s for s in (G1_01, G1_02, ..., G1_18)}
```

That's the whole pattern. Repeat 12 times (one per grade), with
appropriate-difficulty examples and subplots. Done.
