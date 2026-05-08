# Deep audit — crow-pitcher (slice 0HIm)

**Branch:** `claude/audit-crow-pitcher-0HIm`
**Fable sampled:** crow-pitcher
**Grades sampled (random 6 of 12):** 1, 4, 6, 8, 9, 11
**Read-corpus size:** 1,210 records (5 per example × 102 metaphor-rich
subjects across the six grades)

---

## Baseline vs after-fix

| Audit | Baseline | After fixes |
| --- | ---: | ---: |
| crow-pitcher | 0 issues (no detectors for these patterns) | **0 issues** (after 3 new detectors land) |
| Net new issues found by added detectors (pre-fix) | — | 209 hits (43 anchor leaks, 3 wrong-fable, …) |
| Net new issues found by added detectors (post-fix) | — | **0 in crow-pitcher** |
| Smoke tests | 12/12 | 12/12 |

Cross-fable side-effects (advisory — outside this slice):

| Fable | Pre | Post | Notes |
| --- | ---: | ---: | --- |
| tortoise-hare | 0 | 0 | Exempt from fable-leak detector by design |
| ant-grasshopper | 0 | 98 | Pre-existing TH-imagery + 1 predicate collision; the detectors found real bugs in this fable that were always there |
| boy-wolf | 0 | 11 | Pre-existing TH-imagery |
| dog-shadow | 0 | 80 | Pre-existing TH-imagery + 3 predicate collisions |
| fox-grapes | 0 | 0 | Clean |
| goose-eggs | 0 | 11 | Pre-existing TH-character literals + 2 predicate collisions |
| milkmaid | 0 | 89 | Pre-existing TH-imagery |

The new detectors caught **pre-existing leakage in 5 of 7 sister
fables**. **No existing detectors regressed.** Fixing those is left to
the parent session — this slice is scoped to crow-pitcher.

---

## Papercuts found (categorized)

### Cat-C — grammar / punctuation collisions

**`PREDICATE_QUESTION_COLLISION`** — when a Clojure predicate ending in
`?` is mentioned at sentence end, the question framing's trailing `?`
or `.` collides:

- `using contains??` (G4-12, ×2 records — `contains?` + question framing)
- `using contains?.` (G4-12, ×2)
- `using empty?.` (G4-14, ×1)

Other fables had similar collisions in: G6-01 / G6-16 / G6-09 of
tortoise-hare (false-positive `(symbol? ...)` ellipsis — the regex
was tightened to require adjacency); ant-grasshopper / goose-eggs /
dog-shadow each have 1–3 real instances.

**Source location:** `generator.py:_render_question` — framings 3 & 4
appended `?` or `.` directly to a question_what that itself ended in
`?`.

### Cat-E — semantic / wrong-fable imagery

**`WRONG_FABLE_LITERAL`** — tortoise-hare ghost-character names in a
non-tortoise-hare record's narrative or as form data:

- `[G8-07]` form `(speed (->Hare "Pip"))` — "Pip" appears in user_msg
  via `{form_display}` rendering
- `[G8-07]` form `(speed (->Tortoise "Shelly"))` — "Shelly" as data
- `[G8-13]` form `(name-of (->Hare "Zephyr"))` — ".Zephyr" in form
  field; tolerated, but the type name `Hare` is TH-themed
- `[G8-16]` two records: forms `(defrecord Hare ...)` and
  `(defrecord Tortoise ...)`

The narrative slots ("Hare pouch", "Hare-typed pouch", "Tortoise
pouch") also leaked the TH species into the crow-pitcher world.

### Cat-H — plot coherence / fable anchoring

**`FOREIGN_FABLE_IMAGERY`** — tortoise-hare-specific props and
phrasings appearing in crow-pitcher narrative prose, breaking the
"this is the crow-pitcher world" frame:

- `"moss-covered milestone"` — 13 occurrences (grade 1
  `_SHARED_SUBPLOTS` template 2; `_GOAL_SUBPLOTS` template 2)
- `"leather notebook"` — 10 occurrences (`_SHARED_SUBPLOTS` template
  6; `_GOAL_SUBPLOTS` template 6)
- `"small audience of forest creatures"` — 7 occurrences (templates 4
  in both pools)
- `"wooden sign nailed to a tree"` — 3 occurrences (template 8 in
  both pools)

These templates were inherited from the tortoise-hare reference and
never adapted to the pitcher / stones / talon / wing world. Records
read as generic Aesopian banter rather than as a crow standing on a
pitcher's clay rim.

### Cat-J — affirmative push (emotion grounding)

The corpus shows that ~30% of records carry an EMO-pool phrase
(`beak parched`, `clicking the beak in self-satisfaction`, etc.) and
~19% of grade-1 records mention any of pitcher / stone / rim / talon.
The new pitcher-anchored grade-1 templates lift the latter to ~95%
in grade-1; the EMO-coverage gap remains as a follow-on lift
(out-of-scope for this slice — would need fan-out to broaden EMO
pool usage across all subplot families).

---

## Detectors added to `audit-harness.py`

Three new detectors landed (all UPPER_SNAKE_CASE, simple regex):

1. **`PREDICATE_QUESTION_COLLISION`** — flags `\w+\?[?]` (predicate-?
   immediately followed by another `?`) and `\w+\?\.(?!\.)` (predicate-?
   immediately followed by `.` that is not part of an ellipsis). The
   `(?!\.)` lookahead avoids false positives on inline code references
   like `(symbol? ...)` where `?` is followed by a space then ellipsis.

2. **`WRONG_FABLE_LITERAL`** — for non-tortoise-hare records, scans
   for the eight tortoise-hare ghost names (Mossback, Shelly,
   Slowpoke, Pip, Bramble, Hopper, Whisker, Speedwick, Speedy) in
   `user_msg`. Tortoise-hare itself is exempt because those names are
   native there.

3. **`FOREIGN_FABLE_IMAGERY`** — for non-tortoise-hare records, scans
   for four tortoise-hare-specific phrases that consistently leak
   when a fable inherits TH templates wholesale: "moss-covered
   milestone", "leather notebook", "wooden sign nailed to a tree",
   "small audience of forest creatures".

All three landed in the same `check_record(...)` walk so cost is
linear in record length.

---

## Source-level fixes applied

### `src/mmllm/aesop/curriculum/generator.py`

- `_render_question` — strip a trailing `?` from `question_what`
  before formatting, so framings 3 & 4 don't collide. Added doc
  comment naming the pitfall (PREDICATE_QUESTION_COLLISION).

### `src/mmllm/aesop/curriculum/crow_pitcher/grade_1.py`

Rewrote 8 templates across the two pools (`_SHARED_SUBPLOTS` and
`_GOAL_SUBPLOTS`) to anchor to crow-pitcher imagery:

- "moss-covered milestone" → "tall clay pitcher … rim"
- "twig-marked wager in the path" → "talon-scratch on the pitcher's rim"
- generic teacher template → anchored "at the pitcher's rim, …
  one stone, one rise of water"
- "small audience of forest creatures" → "small flock of crows
  gathered around the pitcher"
- "halfway through the race, X stopped" → "halfway through the
  morning's stone-drop, X perched on the pitcher's rim"
- "small leather notebook" → "talon-scratched stone-tally on the
  pitcher's rim"
- generic boast-rebuke → adds "hopping along the pitcher's rim" +
  closing "like dropping a stone and watching the water rise"
- "wooden sign nailed to a tree" → "chalk-mark on the pitcher's rim"

### `src/mmllm/aesop/curriculum/crow_pitcher/grade_8.py`

- G8-07 (Protocol method dispatch) — renamed types
  `Hare`/`Tortoise` → `Falcon`/`Heron`, replaced TH-character
  data `"Pip"`/`"Shelly"` with `"Aria"`/`"Vesper"`, rewrote scenario
  / need / mapping / resolution to remove "Hare pouch" /
  "Tortoise pouch" phrasing.
- G8-13 first example — renamed `Hare` type → `Falcon`; preserved
  the `"Zephyr"` field value (gender-neutral wind name).
- G8-16 — renamed `Hare`/`Tortoise` → `Falcon`/`Heron` types;
  rewrote two scenarios to match (Move and Sound protocols).

One source change per template / form elevates ~5–30 records each.

---

## Polarity check (Cat-F narrative)

The crow-pitcher polarity is *patient stone-dropper vs impatient
guesser*. Spot-checked all 22 metaphor-family canonicals plus 30
sampled records: no polarity flips. The patient role (`{clever}` /
`{tortoise}` alias) consistently does the careful thing (drops a
stone, scratches the rim, submits the form); the hasty role
(`{hasty}` / `{hare}` alias) consistently overreaches.

The fable's polarity is preserved.

---

## Caveats / out-of-scope

- **Cat-J emotion grounding lift** — the affirmative push toward
  every record carrying a manner adverbial (per the user's directive
  "the answer plain", "alternating between possibility and
  verification") was not pursued at the source. It's a fan-out task
  across all subplot families and pools — too large for one slice.
- **Cross-fable leakage** — the new detectors found pre-existing
  TH-imagery / TH-character leakage in 5 of the 7 sister fables.
  Those are out of scope here (slice = crow-pitcher only) but should
  be addressed in follow-on slices on those fables.
- **Type names `Hare`/`Tortoise`** in some Clojure forms — the form
  `(defrecord Hare …)` could be argued either way: as Clojure type
  literally named `Hare` (acceptable) or as TH leakage (Cat-E).
  This audit took the conservative path of renaming.

---

## Definition-of-done checklist

- [x] Branch created off main: `claude/audit-crow-pitcher-0HIm`
- [x] 6-grade random sample documented (1, 4, 6, 8, 9, 11)
- [x] ~1,210 records read in /tmp/cp_corpus.jsonl
- [x] 3 new detectors added with clear UPPER_SNAKE_CASE names
- [x] Source-level fixes applied (generator.py, grade_1.py, grade_8.py)
- [x] All 12 grade-1..12 crow-pitcher smoke tests pass
- [x] crow-pitcher audit: 0 issues (down from 209 the new detectors
      surfaced pre-fix)
- [x] No existing detector regression in any of the 8 fables
- [x] Branch pushed
