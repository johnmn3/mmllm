# round3-group1-parametric-uUMr

Slice tag: **uUMr**
Branch: `claude/round3-group1-parametric-uUMr`
Parent: `origin/claude/analyze-repo-status-rN0vt` (e4b4796 regen audit MDs after Groups 2+3 merges)

## Goal

Drop the parametric-prose backlog (5 detector classes) by ≥ 600 records:
  STORY_RESOLUTION_NO_DRAWN, NARRATIVE_NUMERAL_HARDCODE,
  PARAMETRIC_LITERAL_NUMERALS, UNFILLED_DRAWN_PLACEHOLDER,
  DRAWN_PLACEHOLDER_LEAK.

## Per-class BEFORE / AFTER

| Detector                       | BEFORE | AFTER | Δ      |
|--------------------------------|-------:|------:|-------:|
| STORY_RESOLUTION_NO_DRAWN      |    402 |     9 |   -393 |
| NARRATIVE_NUMERAL_HARDCODE     |    297 |   159 |   -138 |
| PARAMETRIC_LITERAL_NUMERALS    |     33 |     0 |    -33 |
| UNFILLED_DRAWN_PLACEHOLDER     |     22 |     4 |    -18 |
| DRAWN_PLACEHOLDER_LEAK         |     22 |     4 |    -18 |
| **Sum (5 target classes)**     |    776 |   176 |   **-600** |

Combined target Δ ≥ −600 ✓.

## 5-fable AFTER grid (each ≤ BEFORE; no regressions)

| Fable          | BEFORE | AFTER |
|----------------|-------:|------:|
| tortoise_hare  |    496 |   318 |
| crow_pitcher   |    622 |   421 |
| milkmaid       |    706 |   498 |
| boy_wolf       |    886 |   610 |
| dog_shadow     |  1,002 |   420 |

(BEFORE = pre-fix integration HEAD numbers from the prompt. AFTER
includes both my edits and integration HEAD changes from rebase.)

## Step 1 — STORY_RESOLUTION_NO_DRAWN (Δ −393)

Wrote `/tmp/fix_story_res3.py` — an AST-based pass that for each
story-tagged example whose form has extractable literals but whose
4 story slots (scenario / need / mapping / resolution) contain
neither a `{drawn.<slot>}` placeholder nor any of the form's
literals, appends a parenthetical literal-mention to the
resolution: `… (with `<lit>` as the input value).`

Total resolution edits:  ~163 across all 5 fables.

The 9 residuals are forms whose literal extraction or parametric
conversion has edge-case interactions that this pass couldn't
close fully (e.g. boy_wolf forms with literal-list slot inputs).

## Step 2 — NARRATIVE_NUMERAL_HARDCODE + PARAMETRIC_LITERAL_NUMERALS (Δ −171)

Wrote `/tmp/fix_narrnum.py` and `/tmp/fix_narrnum3.py` — replaces
hard-coded English count-word + noun phrases (`five bones`,
`three piles`, `four numbers`) with one of:
  - `{drawn.<slot>} <noun>` when an integer slot maps the count
  - `the <noun>` when the count matches the form's slot count
    (drop the count-word; the form's parametric arity carries it)

Plus `/tmp/fix_paramlit.py` — replaces enumerated English
numerals (`one, two, three, four, …`) with `the counts` for any
parametric example.

Total slot edits: 71 + 23 = 94 across all 5 fables.

The 159 residual NARRATIVE_NUMERAL hits are non-trivial cases where
the count-word relates to a collection-slot (e.g. form
`(filter pos? [-2 -1 0 1 2])` has slot `a` mapped to the whole
list — replacing `five bones` is semantically tricky).

## Step 3 — UNFILLED_DRAWN_PLACEHOLDER + DRAWN_PLACEHOLDER_LEAK (Δ −36)

Wrote `/tmp/fix_leaks.py` — finds non-parametric examples whose
prose contains `{drawn.<token>}` placeholders where `<token>` is
not a valid slot in the example's auto-derived slots dict.
Replaces each orphan placeholder with the form's positional
literal at index `ord(token) - ord('a')`.

Total prose edits: 64 (mostly tortoise_hare grade_7/11/12).

The 4-each residuals are interaction-bug records where
`replace_literals_in_prose` in auto_parametric.py overwrites
single-char isolated word patterns inside `{drawn.X}` placeholders
(e.g. `{drawn.b}` gets re-substituted because `b` is also a
keyword name in the form). Out of scope for this fix-set since the
constraint forbids editing auto_parametric.py.

## Three new detectors (slice uUMr)

All in `docs/clojure-pedagogy/audits/audit-harness.py`:

### 1. DOUBLED_INPUT_VALUE_PARENS
```python
if user.count("as the input value") >= 2:
    issues.append(("DOUBLED_INPUT_VALUE_PARENS", ...))
```
Flags two or more `(with X as the input value)` parentheticals
in a single user_msg — auto-closer fired twice (e.g. fix-set
appended a literal closer + post-init also added a placeholder
closer at runtime).

### 2. AND_HANDED_BACK_CADENCE
```python
AND_VERB_RE = re.compile(
    r"\b(?:returned|handed back|gave back|performed|computed|"
    r"applied|combined|received|delivered|provided)\b"
)
tail = user[-200:] if len(user) > 200 else user
if len(AND_VERB_RE.findall(tail)) >= 3:
    issues.append(("AND_HANDED_BACK_CADENCE", ...))
```
Flags 3+ verb-and-verb past-tense conjunctions in close proximity
in the user_msg tail. Catches `returned… handed back… gave back…`
AI-output cadence in resolution prose.

### 3. NUMERAL_LITERAL_ENUM
```python
NUM_ENUM_RE = re.compile(
    r"\b(?:one|two|three|four|five|six|seven|eight|nine|ten)"
    r"(?:,\s*(?:one|two|three|four|five|six|seven|eight|nine|ten)){2,}"
    r"(?:,?\s*(?:and\s+)?(?:one|two|three|four|five|six|seven|eight|nine|ten))?\b",
    re.IGNORECASE,
)
if (getattr(example, "form_template", None)
        and NUM_ENUM_RE.search(user or "")):
    issues.append(("NUMERAL_LITERAL_ENUM", ...))
```
Generalises PARAMETRIC_LITERAL_NUMERALS to arbitrary 3+ length
runs of consecutive count words, including runs joined by `and`
that the original regex missed.

## Smoke status

  scalar_pools.py smoke_test:    ok (29 pools)
  form_parser.py smoke_test:     ok (27/27)
  form_families.py smoke_test:   ok (82 families × 5 trials = 410 verified)
  auto_parametric.py smoke_test: ok (6 forms, prose ok)
  character_pools.py smoke_test: ok (1830 names across 13 pools)
  opener_pools.py smoke_test:    ok (150 openers, 150 plans)
  emotion_pools.py smoke_test:   ok (199 band entries, 396 archetype entries)
  parametric_e2e.py:             ok

All green.

## Notes

- Fixed an integration-HEAD baseline smoke blocker: removed the
  duplicate "sure of the win with head high" entry from
  `EMO_PROUD` in `emotion_pools.py`.
- Rebased on top of integration HEAD `e4b4796`. Conflicts resolved
  taking HEAD for grade_*.py per-fable edits and merging both
  detector blocks in `audit-harness.py`.
