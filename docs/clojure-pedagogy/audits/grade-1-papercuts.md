# Grade 1 — top 12 paper cuts (second-pass review)

After fixing the 6 patterns from the first deep-dive, this second pass
reads through the post-fix records and surfaces subtler issues.

## The 12 paper cuts

1. **Surviving meta-meta question_what** — G1-01 ex1 still has
   `"the value of the form 0"` (the previous sweep caught the
   "the value of the form nil" case but missed `0`).

2. **Place-preposition mismatch — `in the hilltop`** — `place_phrase`
   picks `in / near / at the edge of / across / by` uniformly, but
   `in the hilltop` is grammatically wrong. Hilltops take "on" or "atop".

3. **Place-preposition mismatch — `in the road`** — same issue. "In
   the road" suggests being in traffic; "on the road" is correct.

4. **Verb-preposition mismatch — `stopped across the forest`** —
   `stopped` followed by `across` doesn't work. Should be "stopped at"
   or "stopped near" or restructure.

5. **Quote-break: bare unescaped quotes in narrative** — for STRING
   examples, `concept_phrase = 'the string "hello"'` produces
   `"Submit the string "hello" to the REPL."` — the inner quotes break
   the outer dialogue quotes when reading. Visible as four `"` chars
   in close proximity, parser confusion.

6. **Singular-they pronoun read** — "Pip the hare stopped... They
   called it impossible" — singular subject but `they` reads as plural.
   Cosmetic for the model (it can learn singular-they) but feels off.

7. **Abstract concept_phrase + "read aloud" mismatch** — subplot 4
   says `"Slowpoke read aloud {concept_phrase}: the form was..."`.
   When concept_phrase is "the equality (= nil nil)" / "the comparison
   (< 3 5)" / "the predicate (nil? nil)", reading aloud an abstract
   noun-phrase is grammatically OK but semantically odd. Forms are
   read aloud; abstract types are not.

8. **Subplot over-selection** — for some seed sequences, the SAME
   subplot gets picked 3+ times in 5 records (e.g., G1-02 wager
   template). Local concentration reduces variety per-subject.

9. **Plan-pool generic** — G1-03 ratio plan_pool says "I write the
   form and let the REPL evaluate it." for every ratio example,
   regardless of operation. Could be more concept-specific
   ("I express the rational arithmetic via Clojure's exact ratios").

10. **`drew a wager in the dust`** appears as a fixed cliché in
    subplot 2. Each record using subplot 2 has the exact same
    `drew a wager in the dust` substring. Cosmetic repetition.

11. **String form display visible-quote density** — for G1-04 records,
    the form `"hello"` renders 5+ times in narrative (concept,
    form_display, eval form, two question repeats), so the prose has
    `"hello"`, `"hello"`, `"hello"`, …. Marginal density.

12. **`(- 1 1/3)` concept_phrase = `"1 minus 1/3"`** — abstract
    description but loses the FORM identity. When subplot says
    "Submit 1 minus 1/3 to the REPL", the reader has to mentally
    convert "1 minus 1/3" back to `(- 1 1/3)`. The concept_phrase
    should match the form's structure.

## Remediation strategy + actions taken

| # | Issue | Status | Notes |
|---|---|---|---|
| 1 | meta-meta `the value of the form 0` | ✅ fixed | G1-01 ex1 trimmed |
| 2 | `in the hilltop` | ✅ fixed | place_phrase now uses `on / atop` |
| 3 | `in the road` | ✅ fixed | place_phrase now uses `on / along` |
| 4 | `stopped across X` | ✅ fixed | `across` removed from prep pool |
| 5 | quote-break in concept_phrase | ⚠️ accepted | nested quotes are syntactically OK; cleaner alternatives lose form identity |
| 6 | singular-they "They called it" | ✅ fixed | subplot 5 uses `{hare}` (name) |
| 7 | abstract concept + "read aloud" | ✅ fixed | subplot 4 rewritten to "pointed to ... and read out the form" |
| 8 | subplot over-selection | ⚠️ accepted | empirical distribution at n=222 is already smooth (verified) |
| 9 | generic plan_pool | ✅ fixed | added 3 more concept-tied entries |
| 10 | `drew a wager in the dust` cliché | ✅ fixed | subplot 2 split into 3 variants (sketched/chalked/marked-out) |
| 11 | string-form quote density | ⚠️ accepted | inherent to string forms; reader can disambiguate |
| 12 | concept_phrase reads as math | ✅ fixed | G1-03 ratio concepts now use "the form (X)" |

## Audit checks added

- `META_META`: question_what containing "the value of the form X"
- `BAD_PLACE_PREP`: "in the hilltop|road|beach|cliff"
- `BAD_VERB_PREP`: "stopped (across|in) the [outdoor location]"

The QUOTE_DENSITY check was considered but not implemented — the
nested quotes are syntactically valid prose and the model can learn
to disambiguate. Forcing concept_phrases to drop the inner quotes
would lose form identity.
