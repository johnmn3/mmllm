# crow-pitcher curriculum audit

Auto-generated audit — each subject's examples checked at 3 records per example, properly matched.

---

## Grade 1

### G1-01: Eval as substitution

- examples: 4
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`"hello"` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`nil` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-02: Integer numbers

- examples: 6
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [DOUBLE_NAME_INTRO] form=`12345` — character 'Loft the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`12345` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)

### G1-03: Ratios

- examples: 5
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(- 1 1/3)` — character 'Drift the crow' introduced twice within 200 chars — drop the second 'the crow'

### G1-04: Strings

- examples: 5
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`"slow and steady"` — character 'Tempestcaw the crow' introduced twice within 200 chars — drop the second 'the crow'

### G1-05: Booleans

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'DOUBLE_NAME_INTRO': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`true` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`true` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`(> 3 5)` — character 'Brand the crow' introduced twice within 200 chars — drop the second 'the crow'

### G1-06: nil

- examples: 5
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`nil` — character 'Sable the crow' introduced twice within 200 chars — drop the second 'the crow'

### G1-07: Keywords

- examples: 5
- variety @ n=50: 1.00
- issues: {'REPEATED_OPENER_FRAGMENT': 1}
    - [REPEATED_OPENER_FRAGMENT] form=`(= :hare :hare)` — opener fragment 'at the edge of the orchard' also appears later in user_msg

### G1-08: Characters

- examples: 4
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 4, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'STRING_AS_CHAR_MISCLAIM': 6}
    - [DOUBLE_NAME_INTRO] form=`\h` — character 'Trickster the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`\h` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`\h` — character 'Realgar the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    - [STRING_AS_CHAR_MISCLAIM] form=`\space` — form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)

### G1-09: Symbols vs values

- examples: 4
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 1, 'DOUBLE_NAME_INTRO': 4, 'CLAUSE_STACK_OVERFLOW': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(symbol? 'hare)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [DOUBLE_NAME_INTRO] form=`(symbol? 42)` — character 'Cawlick the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [DOUBLE_NAME_INTRO] form=`(symbol? "tortoise")` — character 'Jet the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [DOUBLE_NAME_INTRO] form=`(= 'hare 'hare)` — character 'Cawlick the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [DOUBLE_NAME_INTRO] form=`(= 'hare 'hare)` — character 'Pipe the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(= 'hare 'hare)` — sentence with 5 commas reads as AI-output cadence: "Quoting tells the runtime: don't evaluate this, just hand\nit back as the shape i"

### G1-10: Comments

- examples: 2
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(+ 1 2) ; sum of one and two` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [CLAUSE_STACK_OVERFLOW] form=`42 ;; the answer` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    - [CLAUSE_STACK_OVERFLOW] form=`42 ;; the answer` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'

### G1-11: Whitespace doesn't matter

- examples: 2
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 1, 'EXPECTED_META_PHRASE': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`(+    1    2)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [EXPECTED_META_PHRASE] form=`(+    1    2)` — user_msg uses 'the expected X' meta-language — describes the answer in graders'-vocabulary instead of letting the runtime's return speak for itself
    - [CLAUSE_STACK_OVERFLOW] form=`(+
  1
  2)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'

### G1-12: Parens group; they don't multiply

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'ONLY_SHOOK_HEAD_TIC': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    - [ONLY_SHOOK_HEAD_TIC] form=`(* (+ 1 2) 3)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [ONLY_SHOOK_HEAD_TIC] form=`(* (+ 1 2) 3)` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G1-13: First arithmetic call

- examples: 6
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 3, 'NARRATIVE_NUMERAL_HARDCODE': 12, 'SENTENCE_START_LOWER_PRONOUN': 3, 'PARAGRAPH_FRAGMENTATION': 2}
    - [DOUBLE_NAME_INTRO] form=`(+ 1 2)` — character 'Mumble the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [DOUBLE_NAME_INTRO] form=`(+ 1 2)` — character 'Tempestcaw the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(- 5 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(- 5 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(- 5 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 4 5)` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count

### G1-14: Nested call evaluation

- examples: 4
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'DOUBLE_NAME_INTRO': 3, 'SENTENCE_START_LOWER_PRONOUN': 2}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(+ 1 (* 2 3))` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(+ 1 (* 2 3))` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(+ 1 (* 2 3))` — character 'Squall the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(+ 1 (* 2 3))` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(+ 1 (* 2 3))` — character 'Folio the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* (+ 1 2) (+ 3 4))` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count

### G1-15: Equality

- examples: 6
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 5, 'LOW_GROUNDING': 1, 'DOUBLE_NAME_INTRO': 6, 'CLAUSE_STACK_OVERFLOW': 4, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [CONCEPT_AS_VERB] form=`(= 1 1)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(= 1 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(= 1 2)` — character 'Murmur the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(= 1 2)` — sentence with 5 commas reads as AI-output cadence: "Murmur the crow, unbothered by the slow progress, paused at the pitcher's rim at"
    - [DOUBLE_NAME_INTRO] form=`(= "a" "a")` — character 'Ash the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(= "a" "a")` — sentence with 5 commas reads as AI-output cadence: "Ash the crow, calm and methodical, paused at the pitcher's rim near the garden,\n"

### G1-16: Numeric predicates

- examples: 6
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 4, 'NARRATIVE_NUMERAL_HARDCODE': 9, 'DOUBLE_NAME_INTRO': 2}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(zero? 0)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(zero? 5)` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(zero? 5)` — character 'Whistle the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(zero? 5)` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(zero? 5)` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(pos? 7)` — parametric example has hard-coded English numeral 'seven stones' in a story slot — the actual draws may differ from this fixed count

### G1-17: Printing vs returning

- examples: 2
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'DOUBLE_NAME_INTRO': 1}
    - [ONLY_SHOOK_HEAD_TIC] form=`42` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [CLAUSE_STACK_OVERFLOW] form=`42` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    - [DOUBLE_NAME_INTRO] form=`(+ 1 2)` — character 'Glyph the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 1 2)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    - [CLAUSE_STACK_OVERFLOW] form=`(+ 1 2)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'

### G1-18: Errors are safe in the REPL

- examples: 2
- variety @ n=50: 1.00
- issues: {'EXPECTED_META_PHRASE': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [EXPECTED_META_PHRASE] form=`(+ 1 2)` — user_msg uses 'the expected X' meta-language — describes the answer in graders'-vocabulary instead of letting the runtime's return speak for itself
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 7 6)` — parametric example has hard-coded English numeral 'six stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 7 6)` — parametric example has hard-coded English numeral 'six stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 7 6)` — parametric example has hard-coded English numeral 'six stones' in a story slot — the actual draws may differ from this fixed count

## Grade 2

### G2-01: Multi-arg arithmetic

- examples: 6
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2, 'SENTENCE_START_LOWER_PRONOUN': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [DOUBLE_NAME_INTRO] form=`(* 2 3 4)` — character 'Stormcaw the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [DOUBLE_NAME_INTRO] form=`(* 2 3 4)` — character 'Penumbra the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [SENTENCE_START_LOWER_PRONOUN] form=`(- 100 1 2 3)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(+ 1 2 3 4 5 6 7 8 9 10)` — parametric example has hard-coded English numeral 'ten stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(+ 1 2 3 4 5 6 7 8 9 10)` — parametric example has hard-coded English numeral 'ten stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(+ 1 2 3 4 5 6 7 8 9 10)` — parametric example has hard-coded English numeral 'ten stones' in a story slot — the actual draws may differ from this fixed count

### G2-02: Comparison chains

- examples: 5
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 15, 'SENTENCE_START_LOWER_PRONOUN': 2, 'DOUBLE_NAME_INTRO': 2}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(< 1 2 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(< 1 2 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [SENTENCE_START_LOWER_PRONOUN] form=`(< 1 2 3)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(< 1 2 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [SENTENCE_START_LOWER_PRONOUN] form=`(< 3 2 1)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(< 3 2 1)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count

### G2-03: not= and = with multiple args

- examples: 5
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'DOUBLE_NAME_INTRO': 2, 'SENTENCE_START_LOWER_PRONOUN': 4, 'NARRATIVE_NUMERAL_HARDCODE': 9}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(not= 1 2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(not= 1 2)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`(not= 1 2)` — character 'Brand the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [SENTENCE_START_LOWER_PRONOUN] form=`(not= 1 1)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(= 1 1 1)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [SENTENCE_START_LOWER_PRONOUN] form=`(= 1 1 1)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

### G2-04: min and max

- examples: 5
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 5, 'NARRATIVE_NUMERAL_HARDCODE': 12, 'CLAUSE_STACK_OVERFLOW': 4}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(min 1 2 3)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(min 1 2 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(min 1 2 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(min 1 2 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(max 1 2 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [SENTENCE_START_LOWER_PRONOUN] form=`(max 1 2 3)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

### G2-05: quot, rem, mod

- examples: 6
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'PARAGRAPH_FRAGMENTATION': 1, 'DOUBLE_NAME_INTRO': 5, 'SENTENCE_START_LOWER_PRONOUN': 2, 'REPEATED_OPENER_FRAGMENT': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(rem 17 5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [PARAGRAPH_FRAGMENTATION] form=`(rem 17 5)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [DOUBLE_NAME_INTRO] form=`(rem 17 5)` — character 'Updraft the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [SENTENCE_START_LOWER_PRONOUN] form=`(mod 17 5)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [REPEATED_OPENER_FRAGMENT] form=`(mod 17 5)` — opener fragment 'at the edge of the hilltop' also appears later in user_msg
    - [DOUBLE_NAME_INTRO] form=`(mod 17 5)` — character 'Glint the crow' introduced twice within 200 chars — drop the second 'the crow'

### G2-06: inc and dec

- examples: 5
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'SENTENCE_START_LOWER_PRONOUN': 2, 'PARAGRAPH_FRAGMENTATION': 2, 'DOUBLE_NAME_INTRO': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(inc 5)` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(inc 5)` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [SENTENCE_START_LOWER_PRONOUN] form=`(inc 5)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(inc 5)` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(dec 5)` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(dec 5)` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count

### G2-07: Absolute value

- examples: 4
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'FORM_DISPLAY_AND_FORM_NOUN': 1, 'PARAGRAPH_FRAGMENTATION': 1, 'DOUBLE_NAME_INTRO': 2}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(abs 5)` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(abs 5)` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(abs 5)` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(abs -5)` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [PARAGRAPH_FRAGMENTATION] form=`(abs -5)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [DOUBLE_NAME_INTRO] form=`(abs 0)` — character 'Mirk the crow' introduced twice within 200 chars — drop the second 'the crow'

### G2-08: Arithmetic on ratios

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 2, 'SENTENCE_START_LOWER_PRONOUN': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(+ 1/2 1/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 2/3 3/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '4'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(* 2/3 3/4)` — character 'Trickster the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(* 2/3 3/4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '4'), resolution doesn't close the loop)

### G2-09: Floats vs ints (the / operator)

- examples: 3
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'SENTENCE_START_LOWER_PRONOUN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(/ 10 2)` — parametric example has hard-coded English numeral 'ten stones' in a story slot — the actual draws may differ from this fixed count
    - [SENTENCE_START_LOWER_PRONOUN] form=`(/ 10 2)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(/ 10 2)` — parametric example has hard-coded English numeral 'ten stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(/ 10 2)` — parametric example has hard-coded English numeral 'ten stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(/ 10 3)` — parametric example has hard-coded English numeral 'ten stones' in a story slot — the actual draws may differ from this fixed count
    - [SENTENCE_START_LOWER_PRONOUN] form=`(/ 10 3)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

### G2-10: Powers via repeated multiplication

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'NARRATIVE_NUMERAL_HARDCODE': 6, 'PARAGRAPH_FRAGMENTATION': 1, 'DOUBLE_NAME_INTRO': 2}
    - [LOW_GROUNDING] form=`(* 2 2 2)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 5 5)` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 5 5)` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(* 5 5)` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [PARAGRAPH_FRAGMENTATION] form=`(* 3 3 3 3)` — user_msg has 5 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [DOUBLE_NAME_INTRO] form=`(* 3 3 3 3)` — character 'Chrysocolla the crow' introduced twice within 200 chars — drop the second 'the crow'

### G2-11: String concatenation with str

- examples: 4
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'DOUBLE_NAME_INTRO': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(str 42)` — sentence with 5 commas reads as AI-output cadence: 'Concat strings together, and the vines are spliced; cut a substring\nout, and you'
    - [DOUBLE_NAME_INTRO] form=`(str 42)` — character 'Drone the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(str 42)` — sentence with 5 commas reads as AI-output cadence: 'Concat strings together, and the vines are spliced; cut a substring\nout, and you'
    - [CLAUSE_STACK_OVERFLOW] form=`(str 1 "+" 2 "=" 3)` — sentence with 9 commas reads as AI-output cadence: 'Concat strings together, and the vines are spliced; cut a substring\nout, and you'
    - [DOUBLE_NAME_INTRO] form=`(str 1 "+" 2 "=" 3)` — character 'Cinnabar the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(str 1 "+" 2 "=" 3)` — sentence with 9 commas reads as AI-output cadence: 'Concat strings together, and the vines are spliced; cut a substring\nout, and you'

### G2-12: print and println — return values

- examples: 2
- variety @ n=50: 1.00
- issues: {'ONLY_SHOOK_HEAD_TIC': 5}
    - [ONLY_SHOOK_HEAD_TIC] form=`(println "hello")` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [ONLY_SHOOK_HEAD_TIC] form=`(println "hello")` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [ONLY_SHOOK_HEAD_TIC] form=`(print "x")` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [ONLY_SHOOK_HEAD_TIC] form=`(print "x")` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    - [ONLY_SHOOK_HEAD_TIC] form=`(print "x")` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G2-13: and / or — short circuit, return values

- examples: 6
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 6, 'CONCEPT_AS_VERB': 6, 'DOUBLE_NAME_INTRO': 3, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(and true true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(and true true)` — sentence with 5 commas reads as AI-output cadence: 'Windrider the crow, steady in the stone-by-stone approach, paused at the pitcher'
    - [CONCEPT_AS_VERB] form=`(and true false)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(or false true)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CONCEPT_AS_VERB] form=`(or false false)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G2-14: not — turning truthy to false

- examples: 5
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'CONCEPT_AS_VERB': 3, 'DOUBLE_NAME_INTRO': 3}
    - [LOW_GROUNDING] form=`(not true)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(not true)` — sentence with 5 commas reads as AI-output cadence: "Spire the crow, patient as the water rose, paused at the pitcher's rim on the hi"
    - [CONCEPT_AS_VERB] form=`(not true)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [DOUBLE_NAME_INTRO] form=`(not true)` — character 'Hush the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CONCEPT_AS_VERB] form=`(not false)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [LOW_GROUNDING] form=`(not false)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-15: Falsey values: only false and nil

- examples: 4
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 3, 'DOUBLE_NAME_INTRO': 5, 'CLAUSE_STACK_OVERFLOW': 3, 'REPEATED_OPENER_FRAGMENT': 1}
    - [CONCEPT_AS_VERB] form=`(if 0 1 0)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [DOUBLE_NAME_INTRO] form=`(if "" 1 0)` — character 'Murmur the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(if "" 1 0)` — sentence with 5 commas reads as AI-output cadence: "Murmur the crow, unbothered by the slow progress, paused at the pitcher's rim at"
    - [REPEATED_OPENER_FRAGMENT] form=`(if "" 1 0)` — opener fragment 'the pitcher near the orchard' also appears later in user_msg
    - [DOUBLE_NAME_INTRO] form=`(if nil 1 0)` — character 'Ash the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(if nil 1 0)` — sentence with 5 commas reads as AI-output cadence: "Ash the crow, dropping each stone with careful attention, paused at the pitcher'"

### G2-16: Truthy 0 and empty string

- examples: 4
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 3, 'CLAUSE_STACK_OVERFLOW': 3, 'DOUBLE_NAME_INTRO': 2, 'LOW_GROUNDING': 1}
    - [CONCEPT_AS_VERB] form=`(boolean 0)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [CLAUSE_STACK_OVERFLOW] form=`(boolean 0)` — sentence with 5 commas reads as AI-output cadence: "Hum the crow, patient as the water rose, paused at the pitcher's rim in the vill"
    - [DOUBLE_NAME_INTRO] form=`(boolean "")` — character 'Whistle the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(boolean "")` — sentence with 6 commas reads as AI-output cadence: "Whistle the crow, watching the level lift, drop by drop, paused at the pitcher's"
    - [CONCEPT_AS_VERB] form=`(boolean "")` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [DOUBLE_NAME_INTRO] form=`(boolean false)` — character 'Whistle the crow' introduced twice within 200 chars — drop the second 'the crow'

### G2-17: Keyword as function for map lookup

- examples: 3
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 3}
    - [DOUBLE_NAME_INTRO] form=`(:hare {:hare 1 :tortoise 2})` — character 'Parchment the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [DOUBLE_NAME_INTRO] form=`(:tortoise {:hare 1 :tortoise 2})` — character 'Raven the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [DOUBLE_NAME_INTRO] form=`(:missing {:hare 1})` — character 'Loop the crow' introduced twice within 200 chars — drop the second 'the crow'

### G2-18: Quoting symbols

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'DOUBLE_NAME_INTRO': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 2}
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(symbol? (quote hare))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(= (quote tortoise) 'tortoise)` — character 'Thermal the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [LOW_GROUNDING] form=`(= (quote tortoise) 'tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(= (quote tortoise) 'tortoise)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G2-19: Auto-promotion to bigint

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2, 'ANSWER_LEAK': 1, 'SENTENCE_START_LOWER_PRONOUN': 1}
    - [DOUBLE_NAME_INTRO] form=`(* 1000000 1000000)` — character 'Windrider the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [ANSWER_LEAK] form=`(+ 99999999999 1)` — answer 100000000000 in narrative
    - [SENTENCE_START_LOWER_PRONOUN] form=`(+ 99999999999 1)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [DOUBLE_NAME_INTRO] form=`(+ 99999999999 1)` — character 'Shout the crow' introduced twice within 200 chars — drop the second 'the crow'

### G2-20: Counting

- examples: 3
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'DOUBLE_NAME_INTRO': 4, 'CLAUSE_STACK_OVERFLOW': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(count [1 2 3])` — character 'Burble the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'Vellum the crow, deliberate, unhurried by the rising sun, walked the rim of the '
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(count "hello")` — character 'Murmur the crow' introduced twice within 200 chars — drop the second 'the crow'

### G2-21: String length and substring

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(count "tortoise")` — sentence with 5 commas reads as AI-output cadence: 'Concat strings together, and the vines are spliced; cut a substring\nout, and you'
    - [DOUBLE_NAME_INTRO] form=`(count "hare")` — character 'Trill the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(count (subs "tortoise" 0 3))` — sentence with 6 commas reads as AI-output cadence: 'Concat strings together, and the vines are spliced; cut a substring\nout, and you'

### G2-22: Compose pure arithmetic (multi-step calculation)

- examples: 3
- variety @ n=50: 1.00
- issues: {'SENTENCE_START_LOWER_PRONOUN': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'DOUBLE_NAME_INTRO': 3}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(- (* 5 4) 7)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(- (* 5 4) 7)` — parametric example has hard-coded English numeral 'four stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(- (* 5 4) 7)` — parametric example has hard-coded English numeral 'four stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(- (* 5 4) 7)` — parametric example has hard-coded English numeral 'four stones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(- (* 5 4) 7)` — character 'Pyrite the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [DOUBLE_NAME_INTRO] form=`(+ (* 3 8) (* 2 4))` — character 'Veil the crow' introduced twice within 200 chars — drop the second 'the crow'

## Grade 3

### G3-01: def — top-level binding

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(do (def x 42) x)` — character 'Galena the crow' introduced twice within 200 chars — drop the second 'the crow'

### G3-02: def — redefinition

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(do (def x 1) (def x 99) x)` — character 'Galena the crow' introduced twice within 200 chars — drop the second 'the crow'

### G3-03: let — local binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 2, 'FORM_DISPLAY_AND_FORM_NOUN': 3, 'DOUBLE_NAME_INTRO': 4, 'NARRATIVE_NUMERAL_HARDCODE': 6, 'THE_FORM_OVERUSE': 3}
    - [HIGH_LENGTH] form=`(let [x 3] (+ x 1))` — user_msg 212 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [x 3] (+ x 1))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [HIGH_LENGTH] form=`(let [x 3] (+ x 1))` — user_msg 210 words
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [x 3] (+ x 1))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [DOUBLE_NAME_INTRO] form=`(let [x 3] (+ x 1))` — character 'Brand the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [n 10] (* n n))` — parametric example has hard-coded English numeral 'ten stones' in a story slot — the actual draws may differ from this fixed count

### G3-04: let — multi-binding

- examples: 3
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'ANSWER_LEAK': 2, 'THE_FORM_OVERUSE': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [a 1 b 2] (+ a b))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [x 5 y 3] (- x y))` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [x 5 y 3] (- x y))` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(let [x 5 y 3] (- x y))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [x 5 y 3] (- x y))` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [ANSWER_LEAK] form=`(let [a 2 b 3 c 4] (+ a b c))` — answer 9 in narrative

### G3-05: let — shadowing outer def

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(do (def x 10) (let [x 99] x) x)` — character 'Malachite the crow' introduced twice within 200 chars — drop the second 'the crow'

### G3-06: let — binding can reference prior

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'DOUBLE_NAME_INTRO': 4, 'THE_FORM_OVERUSE': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 5 b (* a 2)] b)` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 5 b (* a 2)] b)` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 5 b (* a 2)] b)` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(let [a 5 b (* a 2)] b)` — character 'Climb the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(let [a 3 b (+ a 1) c (* b 2)] c)` — character 'Conundrum the crow' introduced twice within 200 chars — drop the second 'the crow'

### G3-07: fn — anonymous function

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (+ x 1)) 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [a b] (* a b)) 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [a b] (* a b)) 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [a b] (* a b)) 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)

### G3-08: fn — multi-arg

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'CONCEPT_AS_VERB': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [a b c] (+ a b c)) 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`((fn [a b c] (+ a b c)) 1 2 3)` — sentence with 6 commas reads as AI-output cadence: 'The pitcher is narrow — every step\nmust fit, none can be skipped." To create an '
    - [CONCEPT_AS_VERB] form=`((fn [a b c] (+ a b c)) 1 2 3)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [a b c] (+ a b c)) 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [a b c] (+ a b c)) 1 2 3)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G3-09: defn — shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK': 1, 'PARAMETRIC_LITERAL_NUMERALS': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'CONCEPT_AS_VERB': 1, 'EXPECTED_META_PHRASE': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [ANSWER_LEAK] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — answer 6 in narrative
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — sentence with 7 commas reads as AI-output cadence: 'The pitcher is narrow — every step\nmust fit, none can be skipped." To define a f'
    - [CONCEPT_AS_VERB] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [EXPECTED_META_PHRASE] form=`(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))` — user_msg uses 'the expected X' meta-language — describes the answer in graders'-vocabulary instead of letting the runtime's return speak for itself

### G3-10: anonymous shorthand #()

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CONCEPT_AS_VERB': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(+ % 1) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [CONCEPT_AS_VERB] form=`(#(+ % 1) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(+ % 1) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(+ % 1) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* %1 %2) 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* %1 %2) 3 4)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)

### G3-11: Substitution rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'THE_FORM_OVERUSE': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 7] (+ a a))` — parametric example has hard-coded English numeral 'seven stones' in a story slot — the actual draws may differ from this fixed count
    - [THE_FORM_OVERUSE] form=`(let [a 7] (+ a a))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 7] (+ a a))` — parametric example has hard-coded English numeral 'seven stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [a 7] (+ a a))` — parametric example has hard-coded English numeral 'seven stones' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (* x x)) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] (* x x)) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)

### G3-12: Scope vs namespace

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence with 5 commas reads as AI-output cadence: 'To define g at the top level, shadow it in a let with a different value, and com'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def g 5) (let [g 99] (+ g 1)))` — sentence with 5 commas reads as AI-output cadence: 'To define g at the top level, shadow it in a let with a different value, and com'

### G3-13: fn body returns last form

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'PARAGRAPH_FRAGMENTATION': 2}
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] x x x 99) 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`((fn [x] x x x 99) 1)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [LOW_GROUNDING] form=`((fn [x] x x x 99) 1)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] x x x 99) 1)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99',), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`((fn [x] x x x 99) 1)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G3-14: do form

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'DOUBLE_NAME_INTRO': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do 1 2 3)` — parametric example has hard-coded English numeral 'three values' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do 1 2 3)` — parametric example has hard-coded English numeral 'three values' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(do 1 2 3)` — character 'Squall the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do 1 2 3)` — parametric example has hard-coded English numeral 'three values' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(do 1 2 3)` — character 'Folio the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(do 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'

### G3-17: Naming conventions (kebab-case)

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(let [hare-speed 4 tortoise-speed 1] (- hare-speed` — character 'Parchment the crow' introduced twice within 200 chars — drop the second 'the crow'

### G3-18: When to name vs inline

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'DOUBLE_NAME_INTRO': 2, 'FORM_LEAK': 1, 'LOW_GROUNDING': 1}
    - [HIGH_LENGTH] form=`(let [n 5] (* n n n))` — user_msg 201 words
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [n 5] (* n n n))` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [n 5] (* n n n))` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [n 5] (* n n n))` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(let [n 5] (* n n n))` — character 'Sharp the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [DOUBLE_NAME_INTRO] form=`(* 5 5 5)` — character 'Symbol the crow' introduced twice within 200 chars — drop the second 'the crow'

## Grade 4

### G4-01: Vector literal

- examples: 3
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'PARAGRAPH_FRAGMENTATION': 3, 'LOW_GROUNDING': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`[1 2 3]` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`[1 2 3]` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`[1 2 3]` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [PARAGRAPH_FRAGMENTATION] form=`[]` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`[]` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    - [PARAGRAPH_FRAGMENTATION] form=`[]` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G4-02: nth — vector access

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(nth [10 20 30] 0)` — sentence with 5 commas reads as AI-output cadence: 'To get the element at index 0 of a vector containing 10, 20, and 30 properly,\nhe'
    - [CLAUSE_STACK_OVERFLOW] form=`(nth [10 20 30] 2)` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To get the element'

### G4-03: conj — append to vector

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(conj [1 2] 3)` — character 'Bicker the crow' introduced twice within 200 chars — drop the second 'the crow'

### G4-04: List literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_NAME_INTRO': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`'(1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To create a list c'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`'(1 2 3)` — character 'Mystery the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`'(1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To create a list c'

### G4-05: cons — prepend to seq

- examples: 1
- variety @ n=50: 1.00
- issues: {'PARAMETRIC_LITERAL_NUMERALS': 3, 'DOUBLE_NAME_INTRO': 1}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(cons 0 '(1 2 3))` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(cons 0 '(1 2 3))` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(cons 0 '(1 2 3))` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [DOUBLE_NAME_INTRO] form=`(cons 0 '(1 2 3))` — character 'Updraft the crow' introduced twice within 200 chars — drop the second 'the crow'

### G4-07: get — map lookup

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'LOW_GROUNDING': 1}
    - [DOUBLE_NAME_INTRO] form=`(get {:a 1} :missing :default)` — character 'Shout the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [LOW_GROUNDING] form=`(get {:a 1} :missing :default)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G4-08: assoc — map update

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(assoc {:a 1} :b 2)` — character 'Squall the crow' introduced twice within 200 chars — drop the second 'the crow'

### G4-10: keys and vals

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(count (keys {:a 1 :b 2 :c 3}))` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To count how many '
    - [CLAUSE_STACK_OVERFLOW] form=`(count (keys {:a 1 :b 2 :c 3}))` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To count how many '

### G4-11: Set literal

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAMETRIC_LITERAL_NUMERALS': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(count #{1 2 3})` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [CLAUSE_STACK_OVERFLOW] form=`(count #{1 2 3})` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To count the eleme'
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(count #{1 2 3})` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(count #{1 2 3})` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces

### G4-12: Set membership

- examples: 2
- variety @ n=50: 1.00
- issues: {'PARAMETRIC_LITERAL_NUMERALS': 3, 'CLAUSE_STACK_OVERFLOW': 3, 'BOOL_LEAK_RESOLUTION': 1, 'DOUBLE_NAME_INTRO': 1}
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(contains? #{1 2 3} 2)` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [CLAUSE_STACK_OVERFLOW] form=`(contains? #{1 2 3} 2)` — sentence with 5 commas reads as AI-output cadence: 'To check whether 2 is a member of a set containing 1, 2, and 3 properly,\nhe comp'
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(contains? #{1 2 3} 2)` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [CLAUSE_STACK_OVERFLOW] form=`(contains? #{1 2 3} 2)` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To check whether 2'
    - [PARAMETRIC_LITERAL_NUMERALS] form=`(contains? #{1 2 3} 2)` — parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    - [CLAUSE_STACK_OVERFLOW] form=`(contains? #{1 2 3} 2)` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To check whether 2'

### G4-13: count — universal

- examples: 4
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 5, 'DOUBLE_NAME_INTRO': 2}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3 4 5])` — sentence with 5 commas reads as AI-output cadence: 'To count the elements in a vector containing 1, 2, 3, 4, and 5, he composed the '
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(count [1 2 3 4 5])` — character 'Magnetite the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(count [1 2 3 4 5])` — sentence with 7 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To count the eleme'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count

### G4-14: empty?

- examples: 3
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2, 'BOOL_LEAK_RESOLUTION': 1}
    - [DOUBLE_NAME_INTRO] form=`(empty? [])` — character 'Holler the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [BOOL_LEAK_RESOLUTION] form=`(empty? [1])` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [DOUBLE_NAME_INTRO] form=`(empty? [1])` — character 'Updraft the crow' introduced twice within 200 chars — drop the second 'the crow'

### G4-15: first, rest, last

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(last [10 20 30])` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To get the last el'
    - [CLAUSE_STACK_OVERFLOW] form=`(count (rest [10 20 30]))` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To count the eleme'
    - [CLAUSE_STACK_OVERFLOW] form=`(count (rest [10 20 30]))` — sentence with 5 commas reads as AI-output cadence: 'To count the elements remaining after removing the first element from a vector w'

### G4-16: into and conj on collections

- examples: 2
- variety @ n=50: 0.99
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] '(1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'Highwing the crow, deliberate, unhurried by the rising sun, held two decision-ru'
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] '(1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'Smoulder the crow, watching the level lift, drop by drop, held two decision-rule'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} [1 2 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} [1 2 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} [1 2 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(into #{} [1 2 2 3])` — character 'Seal the crow' introduced twice within 200 chars — drop the second 'the crow'

### G4-17: Immutability — assoc returns new

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(let [m {:a 1}] (assoc m :a 99) m)` — character 'Parchment the crow' introduced twice within 200 chars — drop the second 'the crow'

### G4-18: Equality of vectors and lists

- examples: 1
- variety @ n=50: 1.00
- issues: {'BOOL_LEAK_RESOLUTION': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [BOOL_LEAK_RESOLUTION] form=`(= [1 2 3] '(1 2 3))` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [CLAUSE_STACK_OVERFLOW] form=`(= [1 2 3] '(1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To test whether a '
    - [BOOL_LEAK_RESOLUTION] form=`(= [1 2 3] '(1 2 3))` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead

### G4-19: range and seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'DOUBLE_NAME_INTRO': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (range 5))` — parametric example has hard-coded English numeral 'Five integers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (range 5))` — parametric example has hard-coded English numeral 'Five integers' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (range 5))` — parametric example has hard-coded English numeral 'Five integers' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(first (range 1 100))` — character 'Cipher the crow' introduced twice within 200 chars — drop the second 'the crow'

### G4-20: Collection vs sequence

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 2}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (seq [1 2 3]))` — parametric example has hard-coded English numeral 'three elements' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(count (seq [1 2 3]))` — sentence with 5 commas reads as AI-output cadence: 'To convert a vector containing 1, 2, and 3 to a sequence and count its elements '
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (seq [1 2 3]))` — parametric example has hard-coded English numeral 'three elements' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(count (seq [1 2 3]))` — parametric example has hard-coded English numeral 'three elements' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(count (seq [1 2 3]))` — sentence with 5 commas reads as AI-output cadence: 'The pile is heavy; one\nright reach saves a dozen wrong ones." To convert a vecto'

## Grade 5

### G5-01: if

- examples: 3
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(if false :a :b)` — sentence with 5 commas reads as AI-output cadence: 'Pirouette the crow, trusting the process, stone after stone, spread her wings in'

### G5-03: when

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 2, 'LOW_GROUNDING': 2, 'DOUBLE_NAME_INTRO': 3}
    - [ANSWER_LEAK_STRING] form=`(when true :yes)` — answer string ':yes' appears in user_msg
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [ANSWER_LEAK_STRING] form=`(when true :yes)` — answer string ':yes' appears in user_msg
    - [LOW_GROUNDING] form=`(when true :yes)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(when false :yes)` — character 'Float the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [DOUBLE_NAME_INTRO] form=`(when false :yes)` — character 'Wily the crow' introduced twice within 200 chars — drop the second 'the crow'

### G5-04: cond

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(cond (= 1 2) :a (= 1 1) :b :else :c)` — character 'Mystery the crow' introduced twice within 200 chars — drop the second 'the crow'

### G5-05: cond — :else

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(cond false :a false :b :else :c)` — sentence with 5 commas reads as AI-output cadence: 'Tailwind the crow, unhurried, form after form, spread his wings at the edge of t'
    - [CLAUSE_STACK_OVERFLOW] form=`(cond false :a false :b :else :c)` — sentence with 5 commas reads as AI-output cadence: 'Mystery the crow, deliberate, unhurried by the rising sun, perched above the pit'
    - [CLAUSE_STACK_OVERFLOW] form=`(cond false :a false :b :else :c)` — sentence with 5 commas reads as AI-output cadence: 'Trill the crow, watching the level lift, drop by drop, perched above the pitcher'

### G5-06: case

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(case 2 1 :one 2 :two 3 :three :default)` — sentence with 5 commas reads as AI-output cadence: 'Onyx the crow, trusting the process, stone after stone, perched above the pitche'

### G5-07: and / or as control flow

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'CLAUSE_STACK_OVERFLOW': 1, 'ANSWER_LEAK_STRING': 1, 'LOW_GROUNDING': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(and 1 2 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(and 1 2 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(and 1 2 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(or nil false :found)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(or nil false :found)` — sentence with 5 commas reads as AI-output cadence: 'Shadow the crow, dropping each stone with careful attention, paused at the pitch'
    - [ANSWER_LEAK_STRING] form=`(or nil false :found)` — answer string ':found' appears in user_msg

### G5-08: not

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(not (> 1 2))` — sentence with 6 commas reads as AI-output cadence: "Float the crow, trusting the process, stone after stone, paused at the pitcher's"
    - [DOUBLE_NAME_INTRO] form=`(not (> 1 2))` — character 'Trickster the crow' introduced twice within 200 chars — drop the second 'the crow'

### G5-09: fn as value

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [f x] (f (f x))) inc 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [f x] (f (f x))) inc 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [f x] (f (f x))) inc 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)

### G5-10: map

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(map inc [1 2 3])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(map inc [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'To pour the vector containing 1, 2, 3 through a sieve whose rule is inc, collect'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(map inc [1 2 3])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(map inc [1 2 3])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map #(* % %) [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(map #(* % %) [1 2 3 4])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)

### G5-11: filter

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(filter even? [1 2 3 4])` — sentence with 5 commas reads as AI-output cadence: 'Quibble the crow, deliberate, unhurried by the rising sun, held two decision-rul'
    - [CLAUSE_STACK_OVERFLOW] form=`(filter pos? [-2 -1 0 1 2])` — sentence with 8 commas reads as AI-output cadence: 'Riddlecaw the crow shook\nher head and went on with the work: to\nkeep the positiv'

### G5-12: reduce

- examples: 3
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 9, 'CLAUSE_STACK_OVERFLOW': 6, 'DOUBLE_NAME_INTRO': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(reduce + [1 2 3 4])` — parametric example has hard-coded English numeral 'four stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(reduce + [1 2 3 4])` — parametric example has hard-coded English numeral 'four stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + [1 2 3 4])` — sentence with 6 commas reads as AI-output cadence: 'To walk the row of pebbles 1, 2, 3, 4 carrying a tally that combines each with +'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(reduce + [1 2 3 4])` — parametric example has hard-coded English numeral 'four stones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(reduce + [1 2 3 4])` — character 'Mutter the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(reduce * [1 2 3 4 5])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count

### G5-13: reduce with init

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 3, 'DOUBLE_NAME_INTRO': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(reduce + 100 [1 2 3])` — parametric example has hard-coded English numeral 'Three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(reduce + 100 [1 2 3])` — parametric example has hard-coded English numeral 'Three stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + 100 [1 2 3])` — sentence with 9 commas reads as AI-output cadence: 'The runtime does this for any\ncollection — vector, list, map, string." To fold +'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(reduce + 100 [1 2 3])` — parametric example has hard-coded English numeral 'Three stones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(reduce + 100 [1 2 3])` — character 'Inkwell the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(reduce + 100 [1 2 3])` — sentence with 9 commas reads as AI-output cadence: 'The runtime does this for any\ncollection — vector, list, map, string." To fold +'

### G5-14: apply

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'CONCEPT_AS_VERB': 2, 'DOUBLE_NAME_INTRO': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four stones' in a story slot — the actual draws may differ from this fixed count
    - [CONCEPT_AS_VERB] form=`(apply + [1 2 3 4])` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply + [1 2 3 4])` — parametric example has hard-coded English numeral 'four stones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(apply + [1 2 3 4])` — character 'Holler the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(apply max [3 1 4 1 5])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count

### G5-15: comp

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((comp inc inc) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((comp inc inc) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((comp inc inc) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((comp str inc) 9)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((comp str inc) 9)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`((comp str inc) 9)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('9',), resolution doesn't close the loop)

### G5-16: partial

- examples: 2
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 1, 'DOUBLE_NAME_INTRO': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 2}
    - [CONCEPT_AS_VERB] form=`((partial + 10) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [DOUBLE_NAME_INTRO] form=`((partial + 10) 5)` — character 'Coal the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(map (partial * 3) [1 2 3])` — parametric example has hard-coded English numeral 'Three stones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(map (partial * 3) [1 2 3])` — character 'Whistle the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(map (partial * 3) [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'The pitcher is narrow — every step\nmust fit, none can be skipped." To apply a pa'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(map (partial * 3) [1 2 3])` — parametric example has hard-coded English numeral 'Three stones' in a story slot — the actual draws may differ from this fixed count

### G5-17: juxt

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'CONCEPT_AS_VERB': 1}
    - [DOUBLE_NAME_INTRO] form=`((juxt inc dec) 5)` — character 'Parchment the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CONCEPT_AS_VERB] form=`((juxt inc dec) 5)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')

### G5-18: some

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_NAME_INTRO': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(some even? [1 3 5 8 7])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(some even? [1 3 5 8 7])` — sentence with 7 commas reads as AI-output cadence: 'To check if any element in the vector containing 1, 3, 5, 8, and 7 is even, she '
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(some even? [1 3 5 8 7])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(some even? [1 3 5 8 7])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(some even? [1 3 5 8 7])` — sentence with 7 commas reads as AI-output cadence: 'To check if any element in the vector containing 1, 3, 5, 8, and 7 is even, she '
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(some neg? [1 2 3])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count

### G5-19: every?

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'CLAUSE_STACK_OVERFLOW': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(every? pos? [1 2 3])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(every? pos? [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'Windrider the crow shook\nher head and went on with the work: to\ncheck if all ele'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(every? pos? [1 2 3])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(every? pos? [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To check if all elements in the vector containing 1, 2, and 3 are positive, she '
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(every? pos? [1 2 3])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(every? even? [1 2 3])` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count

### G5-20: take and drop

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'CLAUSE_STACK_OVERFLOW': 2}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(take 3 [10 20 30 40 50])` — sentence with 8 commas reads as AI-output cadence: 'Burble the crow shook\nhis head and went on with the work: to\ntake the first 3 el'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(take 3 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(take 3 [10 20 30 40 50])` — sentence with 7 commas reads as AI-output cadence: 'To take the first 3 elements from the vector containing 10, 20, 30, 40, and 50, '
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(drop 2 [10 20 30 40 50])` — parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count

### G5-21: distinct and sort

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 6, 'CLAUSE_STACK_OVERFLOW': 3, 'DOUBLE_NAME_INTRO': 3}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(distinct [1 1 2 3 3 4])` — parametric example has hard-coded English numeral 'six stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 5 commas reads as AI-output cadence: 'Write a form whose evaluation gives the sequence produced by passing 1, 1, 2, 3,'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(distinct [1 1 2 3 3 4])` — parametric example has hard-coded English numeral 'six stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(distinct [1 1 2 3 3 4])` — sentence with 9 commas reads as AI-output cadence: 'Shroud the crow shook\nhis head and went on with the work: to\nremove duplicate el'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(distinct [1 1 2 3 3 4])` — parametric example has hard-coded English numeral 'six stones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(distinct [1 1 2 3 3 4])` — character 'Vellum the crow' introduced twice within 200 chars — drop the second 'the crow'

### G5-22: recur — first taste

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'ANSWER_LEAK': 2, 'BAD_PLACE_PREP': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — sentence with 6 commas reads as AI-output cadence: 'To walk a small circuit five times, multiplying a running tally by the current s'
    - [ANSWER_LEAK] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — answer 120 in narrative
    - [BAD_PLACE_PREP] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — 'in the hilltop' (wrong preposition)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [ANSWER_LEAK] form=`(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n)` — answer 120 in narrative

## Grade 6

### G6-01: Namespace as file

- examples: 3
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1, 'LOW_GROUNDING': 1, 'DOUBLE_NAME_INTRO': 3}
    - [ANSWER_LEAK_STRING] form=`(name 'foo.bar)` — answer string 'foo.bar' appears in user_msg
    - [LOW_GROUNDING] form=`(name 'foo.bar)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(name 'clojure.string)` — character 'Twilight the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [DOUBLE_NAME_INTRO] form=`(symbol? 'tortoise.race)` — character 'Smoke the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [DOUBLE_NAME_INTRO] form=`(symbol? 'tortoise.race)` — character 'Crest the crow' introduced twice within 200 chars — drop the second 'the crow'

### G6-02: ns form

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(= 'race.tortoise 'race.tortoise)` — character 'Riddle the crow' introduced twice within 200 chars — drop the second 'the crow'

### G6-03: require

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 2}
    - [DOUBLE_NAME_INTRO] form=`(clojure.string/lower-case "ZEBRA")` — character 'Float the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [DOUBLE_NAME_INTRO] form=`(clojure.string/lower-case "ZEBRA")` — character 'Wily the crow' introduced twice within 200 chars — drop the second 'the crow'

### G6-04: refer and use

- examples: 1
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(= (clojure.string/upper-case "x") (clojure.string` — character 'Char the crow' introduced twice within 200 chars — drop the second 'the crow'

### G6-05: Fully qualified names

- examples: 4
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1, 'LOW_GROUNDING': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/reverse "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(clojure.string/reverse "abc")` — character 'Puzzle the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [LOW_GROUNDING] form=`(namespace :owner/item)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(name :owner/item)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-06: Private defs

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:private (meta '^:private x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:private (meta '^:private x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:private (meta '^:private x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:private (meta 'x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:private (meta 'x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:private (meta 'x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private',), resolution doesn't close the loop)

### G6-07: Public vs private API

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'BOOL_LEAK_RESOLUTION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [BOOL_LEAK_RESOLUTION] form=`(boolean (:private (meta '^:private hidden)))` — resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta '^:private hidden)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private', ':private'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta 'public)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(boolean (:private (meta 'public)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':private',), resolution doesn't close the loop)

### G6-08: Circular dependencies

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 3}
    - [DOUBLE_NAME_INTRO] form=`(clojure.string/upper-case "a")` — character 'Trickster the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [DOUBLE_NAME_INTRO] form=`(clojure.string/upper-case "a")` — character 'Cloudshroud the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [DOUBLE_NAME_INTRO] form=`(= 'a.b 'a.b)` — character 'Trickster the crow' introduced twice within 200 chars — drop the second 'the crow'

### G6-09: Loading order

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_NAME_INTRO': 2}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def step1 1) (def step2 (+ step1 1)) step2)` — sentence with 5 commas reads as AI-output cadence: 'To define step1 as 1, then define step2 as step1 plus 1, then return step2, the '
    - [DOUBLE_NAME_INTRO] form=`(let [a 1 b (+ a 1)] (+ a b))` — character 'Gust the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a 1 b (+ a 1)] (+ a b))` — sentence with 5 commas reads as AI-output cadence: "The next crow who perches reads what's\nthere now — whatever the latest talon-str"
    - [DOUBLE_NAME_INTRO] form=`(let [a 1 b (+ a 1)] (+ a b))` — character 'Ash the crow' introduced twice within 200 chars — drop the second 'the crow'

### G6-10: Leiningen and deps.edn

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [FOREIGN_FABLE_IMAGERY] form=`(:deps {:deps {:a 1 :b 2}})` — tortoise-hare-specific imagery 'leather notebook' leaks into crow-pitcher prose
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get-in {:paths ["src"]} [:paths 0])` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':paths', ':paths', 'src'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get-in {:paths ["src"]} [:paths 0])` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':paths', ':paths', 'src'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(get-in {:paths ["src"]} [:paths 0])` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':paths', ':paths', 'src'), resolution doesn't close the loop)

### G6-11: Classpath

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "src:test" #":")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':test', 'src:test'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "src:test" #":")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':test', 'src:test'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "src:test" #":")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':test', 'src:test'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count ["src" "test" "resources"])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('src', 'test', 'resources'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count ["src" "test" "resources"])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('src', 'test', 'resources'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count ["src" "test" "resources"])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('src', 'test', 'resources'), resolution doesn't close the loop)

### G6-14: Import for host classes

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(symbol? 'java.util.List)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [DOUBLE_NAME_INTRO] form=`(symbol? 'java.util.List)` — character 'Hush the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(name 'java.util.Map)` — sentence with 5 commas reads as AI-output cadence: "The runtime moves a stone across the boundary, calls\nthe human's method, and bri"
    - [LOW_GROUNDING] form=`(name 'java.util.Map)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G6-15: Namespace meta

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '\{:doc "steady wins"\} race))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'steady wins'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '\{:doc "steady wins"\} race))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'steady wins'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(:doc (meta '\{:doc "steady wins"\} race))` — character 'Whoop the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '\{:doc "steady wins"\} race))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'steady wins'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:author (meta '\{:author "Aesop"\} race))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':author', ':author', 'Aesop'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:author (meta '\{:author "Aesop"\} race))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':author', ':author', 'Aesop'), resolution doesn't close the loop)

### G6-16: Cleaning up requires

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'BOOL_LEAK_RESOLUTION': 1, 'LOW_GROUNDING': 1}
    - [DOUBLE_NAME_INTRO] form=`(contains? #{'clojure.string} 'clojure.string)` — character 'Coal the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [BOOL_LEAK_RESOLUTION] form=`(contains? #{'clojure.string} 'clojure.set)` — resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    - [LOW_GROUNDING] form=`(contains? #{'clojure.string} 'clojure.set)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 7

### G7-01: throw

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', 'bad'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', 'bad'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "bad")) (catch Exception e` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', 'bad'), resolution doesn't close the loop)

### G7-02: try / catch

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [DOUBLE_NAME_INTRO] form=`(try (/ 1 0) (catch Exception e -1))` — character 'Buffet the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [DOUBLE_NAME_INTRO] form=`(try 42 (catch Exception e :caught))` — character 'Vanekin the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [DOUBLE_NAME_INTRO] form=`(try 42 (catch Exception e :caught))` — character 'Eclipse the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(try 42 (catch Exception e :caught))` — sentence with 5 commas reads as AI-output cadence: 'Eclipse the crow, deliberate, unhurried by the rising sun, spread a patch of sof'

### G7-03: try / finally

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(try 7 (finally (prn :cleanup)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try 7 (finally (prn :cleanup)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', ':cleanup'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try 7 (finally (prn :cleanup)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', ':cleanup'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try 7 (finally (prn :cleanup)))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', ':cleanup'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', ':ran'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(try (try (/ 1 0) (finally (prn :ran))) (catch Exc` — character 'Buzz the crow' introduced twice within 200 chars — drop the second 'the crow'

### G7-04: ex-info

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "bad" {:a 1})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', 'bad'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "x" {:k :v})) (catch Exceptio` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':k', ':v', ':k'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(try (throw (ex-info "x" {:k :v})) (catch Exceptio` — character 'Char the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "x" {:k :v})) (catch Exceptio` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':k', ':v', ':k'), resolution doesn't close the loop)

### G7-05: nil punning

- examples: 4
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(first nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(first nil)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(count nil)` — sentence with 5 commas reads as AI-output cadence: 'Riddle the crow, watching the level lift, drop by drop, spread a patch of soft m'

### G7-06: pre and post conditions

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':pre'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — sentence with 5 commas reads as AI-output cadence: 'Galena the crow, watching the level lift, drop by drop, spread a patch of soft m'
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':pre'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — character 'Sable the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [STORY_RESOLUTION_NO_DRAWN] form=`((fn [x] {:pre [(pos? x)]} (* x 2)) 5)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':pre'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try ((fn [x] {:pre [(pos? x)]} x) -1) (catch Exce` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1', ':pre'), resolution doesn't close the loop)

### G7-07: assert

- examples: 2
- variety @ n=50: 1.00
- issues: {'REPEATED_OPENER_FRAGMENT': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'DOUBLE_NAME_INTRO': 1}
    - [REPEATED_OPENER_FRAGMENT] form=`(do (assert (= 1 1)) 1)` — opener fragment 'the pitcher near the farm' also appears later in user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(do (assert (= 1 1)) 1)` — sentence with 5 commas reads as AI-output cadence: 'Thermal the crow, watching the level lift, drop by drop, spread a patch of soft '
    - [CLAUSE_STACK_OVERFLOW] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — sentence with 5 commas reads as AI-output cadence: 'To assert that 5 equals 0, catch the failure, and return a numeric code, he comp'
    - [DOUBLE_NAME_INTRO] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — character 'Shout the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(try (assert (= 1 2)) (catch Throwable e 0))` — sentence with 5 commas reads as AI-output cadence: 'To assert that 5 equals 8, catch the failure, and return a numeric code, she com'

### G7-08: prn and pprint

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (prn 42))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (prn 42))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (prn 42))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (prn :hare))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(with-out-str (prn :hare))` — character 'Trickster the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (prn :hare))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare',), resolution doesn't close the loop)

### G7-09: tap>

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'LOW_GROUNDING': 1, 'PARAGRAPH_FRAGMENTATION': 1, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> :hello)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hello',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(tap> 42)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(tap> 42)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [PARAGRAPH_FRAGMENTATION] form=`(tap> 42)` — user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story

### G7-10: doc and source

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '^{:doc "adds two"} plus))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'adds two'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '^{:doc "adds two"} plus))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'adds two'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(:doc (meta '^{:doc "adds two"} plus))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':doc', ':doc', 'adds two'), resolution doesn't close the loop)

### G7-11: Reading stack traces

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1, 'ANSWER_LEAK_STRING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(try (throw (Exception. "oops")) (catch Exception ` — character 'Tempest the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (Exception. "oops")) (catch Exception ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('oops',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('trouble',), resolution doesn't close the loop)
    - [ANSWER_LEAK_STRING] form=`(try (throw (ex-info "trouble" {})) (catch Excepti` — answer string 'trouble' appears in user_msg

### G7-12: slurp and spit

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(count "hare
tortoise
")` — sentence with 5 commas reads as AI-output cadence: 'Flat stones are how the two meet — a value crosses out\nand becomes scratches on '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "a\nb\nc" #"\n")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc', '\\n'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "a\nb\nc" #"\n")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc', '\\n'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.string/split "a\nb\nc" #"\n")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc', '\\n'), resolution doesn't close the loop)

### G7-13: line-seq

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(count (clojure.string/split-lines "a\nb\nc"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(count (clojure.string/split-lines "a\nb\nc"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('a\\nb\\nc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(first (clojure.string/split-lines "alpha\nbeta"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('alpha\\nbeta',), resolution doesn't close the loop)

### G7-14: with-open

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(with-out-str (println "hare"))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (println "hare"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('hare',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (println "hare"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('hare',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(with-out-str (println "hare"))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('hare',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(with-out-str (println "hare"))` — character 'Hush the crow' introduced twice within 200 chars — drop the second 'the crow'

### G7-15: *in* and *out*

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'LOW_GROUNDING': 1}
    - [DOUBLE_NAME_INTRO] form=`(with-out-str (print "x"))` — character 'Whoop the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [LOW_GROUNDING] form=`(with-out-str (println))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G7-16: edn read

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'DOUBLE_NAME_INTRO': 2, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(clojure.edn/read-string "42")` — character 'Coal the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "{:a 1}")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', '{:a 1}'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "{:a 1}")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', '{:a 1}'), resolution doesn't close the loop)

### G7-17: JSON roundtrip

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str {:a 1 :b 2}))` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(clojure.edn/read-string (pr-str [1 2 3]))` — character 'Sly the crow' introduced twice within 200 chars — drop the second 'the crow'

### G7-18: Shell command

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 4}
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(:cmd {:cmd "ls" :args ["-l"]})` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(count (:args {:cmd "echo" :args ["hello" "world"]` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

## Grade 8

### G8-01: Why polymorphism

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(defn speak [k] (cond (= k :hare) "swift" (= k :to` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':tortoise', ':else'), resolution doesn't close the loop)
    - [LOW_GROUNDING] form=`(let [speak (fn [k] (cond (= k :hare) "swift" (= k` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G8-02: deftype introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Pebble [color]) (.-color (Pebble. "gr` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('grey',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Stone [weight]) (.-weight (Stone. 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (deftype Stone [weight]) (.-weight (Stone. 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (deftype Stone [weight]) (.-weight (Stone. 7))` — character 'Riddle the crow' introduced twice within 200 chars — drop the second 'the crow'

### G8-03: defrecord introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'ANSWER_LEAK_STRING': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [ANSWER_LEAK_STRING] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — answer string ':slow' appears in user_msg
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defrecord Runner [name pace]) (:pace (->Runne` — sentence with 5 commas reads as AI-output cadence: 'Lighter, more focused." To\ndefine a Runner case with two named compartments, nam'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:name (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':name', ':moderate', 'Bob'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defrecord Runner [name pace]) (:name (->Runne` — character 'Buzz the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:name (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':name', ':moderate', 'Bob'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defrecord Runner [name pace]) (:name (->Runne` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':name', ':moderate', 'Bob'), resolution doesn't close the loop)

### G8-04: Protocol definition

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(do (defprotocol Greet (hail [this])) (some? Greet` — character 'Char the crow' introduced twice within 200 chars — drop the second 'the crow'

### G8-05: Protocol extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads from this ledger whenever the call goes out." To\ndefine a prot'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', ':number'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol named Greet with one method hail, extend it to Long type wi'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', ':number'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — sentence with 6 commas reads as AI-output cadence: 'The\nruntime looks up which crow is present, then runs that crow\'s answer."\nTo de'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Greet (hail [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7', ':number'), resolution doesn't close the loop)

### G8-06: Protocol method dispatch

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 5, 'DOUBLE_NAME_INTRO': 1, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'Any crow who can fulfil the stone-drop call may claim membership."\nTo define a p'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — character 'Sable the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads from this ledger whenever the call goes out." To\ndefine a prot'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-prot` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':string-pace', ':long-pace'), resolution doesn't close the loop)

### G8-07: Record implementing protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 4, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord F` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Aria'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord F` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, define a record Falcon that impleme'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord F` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Aria'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (defrecord F` — sentence with 5 commas reads as AI-output cadence: 'Any crow who can fulfil the stone-drop call may claim membership."\nTo define a p'
    - [LOW_GROUNDING] form=`(do (defprotocol Pace (speed [this])) (defrecord F` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (defrecord F` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':swift', 'Aria'), resolution doesn't close the loop)

### G8-08: Multimethod defmulti

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads it, finds the matching chute, and runs that one." To\ndeclare a'
    - [DOUBLE_NAME_INTRO] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — character 'Trickster the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti tag :kind) (defmethod tag :stone [_]` — sentence with 6 commas reads as AI-output cadence: 'To define a multimethod tag that dispatches on the :kind key, add a method for :'

### G8-09: Multimethod defmethod

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: 'To define a multimethod pace that dispatches on :species with methods for both :'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti pace :species) (defmethod pace :hare` — sentence with 5 commas reads as AI-output cadence: 'To define a multimethod pace that dispatches on :species with methods for both :'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defmulti pace :species) (defmethod pace :hare` — character 'Wingnight the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmulti pace :species) (defmethod pace :hare` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':species', ':hare', ':swift'), resolution doesn't close the loop)

### G8-10: Multimethod vs protocol

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmulti show identity) (defmethod show :rabb` — sentence with 5 commas reads as AI-output cadence: 'To define a multimethod show that dispatches on identity with a method for one s'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Show (show [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('str-', 'hare'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Show (show [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('str-', 'hare'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Show (show [this])) (extend-proto` — sentence with 7 commas reads as AI-output cadence: 'The runtime reads it, finds the matching chute, and runs that one." To\ndefine a '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Show (show [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('str-', 'hare'), resolution doesn't close the loop)

### G8-11: Protocol vs Java interface

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol IPace (run [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':ran', 'hare'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol IPace (run [this])) (extend-proto` — sentence with 6 commas reads as AI-output cadence: 'The\nruntime looks up which crow is present, then runs that crow\'s answer."\nTo de'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol IPace (run [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':ran', 'hare'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defprotocol IPace (run [this])) (extend-proto` — character 'Tempest the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol IPace (run [this])) (extend-proto` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':ran', 'hare'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol IPace (run [this])) (extend-proto` — sentence with 5 commas reads as AI-output cadence: 'To define a protocol IPace with method run, extend it to String type, then call '

### G8-12: extend-type on built-in types

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 4}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-type` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':number-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 6 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, use extend-type to attach it to Lon'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-type` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':number-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 7 commas reads as AI-output cadence: 'The runtime reads it, finds the matching chute, and runs that one." To\ndefine a '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Pace (speed [this])) (extend-type` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', ':number-pace'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Pace (speed [this])) (extend-type` — sentence with 6 commas reads as AI-output cadence: 'To define a protocol Pace with method speed, use extend-type to attach it to Lon'

### G8-13: this-style vs fn-style

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 3, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Named (name-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':n', 'Zephyr'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Named (name-of [this])) (defrecor` — sentence with 5 commas reads as AI-output cadence: 'Any crow who can fulfil the stone-drop call may claim membership."\nTo define a p'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Tagged (tag-of [this])) (defrecor` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':t', ':grey'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Tagged (tag-of [this])) (defrecor` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads from this ledger whenever the call goes out." To\ndefine a prot'

### G8-14: Protocols don't inherit

- examples: 1
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — sentence with 6 commas reads as AI-output cadence: 'Any crow who can fulfil the stone-drop call may claim membership."\nTo define two'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a-impl', ':b-impl', ') (b-op '), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defprotocol A (a-op [this])) (defprotocol B (` — character 'Hush the crow' introduced twice within 200 chars — drop the second 'the crow'

### G8-15: derive and isa? — multimethod hierarchy

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 5, 'DOUBLE_NAME_INTRO': 1, 'LOW_GROUNDING': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':runner', ':hare'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — sentence with 6 commas reads as AI-output cadence: 'The runtime reads it, finds the matching chute, and runs that one." To\nestablish'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':runner', ':hare'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — character 'Whoop the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — sentence with 5 commas reads as AI-output cadence: 'To establish a type relationship where ::hare is a type of ::runner, then check '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (derive ::hare ::runner) (isa? ::hare ::runner` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':hare', ':runner', ':hare'), resolution doesn't close the loop)

### G8-16: Abstract design with protocols

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 4, 'DOUBLE_NAME_INTRO': 1, 'LOW_GROUNDING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Fa` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Move (step [this])) (defrecord Fa` — sentence with 5 commas reads as AI-output cadence: 'The runtime reads from this ledger whenever the call goes out." To\ndefine a prot'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Fa` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defprotocol Move (step [this])) (defrecord Fa` — character 'Coal the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defprotocol Move (step [this])) (defrecord Fa` — sentence with 6 commas reads as AI-output cadence: 'The\nruntime looks up which crow is present, then runs that crow\'s answer."\nTo de'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defprotocol Move (step [this])) (defrecord Fa` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':leap', ':plod'), resolution doesn't close the loop)

## Grade 9

### G9-01: Immutability as default — review

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4, 'NARRATIVE_NUMERAL_HARDCODE': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(let [m {:a 1}] (assoc m :b 2) m)` — sentence with 7 commas reads as AI-output cadence: 'To bind a map m, call assoc to add :b 2 to a new map, then return the unchanged '
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [v [1 2 3]] (conj v 4) v)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(let [v [1 2 3]] (conj v 4) v)` — sentence with 5 commas reads as AI-output cadence: 'To bind a vector v, call conj to add 5 to a new vector, then return the unchange'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [v [1 2 3]] (conj v 4) v)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(let [v [1 2 3]] (conj v 4) v)` — sentence with 5 commas reads as AI-output cadence: 'To bind a vector v, call conj to add 9 to a new vector, then return the unchange'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(let [v [1 2 3]] (conj v 4) v)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count

### G9-02: Why state at all

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 7 commas reads as AI-output cadence: 'To construct an atom holding 0 as counter, atomically swap it by applying inc, a'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def counter (atom 0)) (swap! counter inc) @co` — sentence with 7 commas reads as AI-output cadence: 'The marks change only when someone scratches — and only as the\nruntime allows." '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def progress (atom :idle)) (reset! progress :` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':idle', ':running'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def progress (atom :idle)) (reset! progress :` — sentence with 7 commas reads as AI-output cadence: 'The runtime sees to that — no two crows scratch over each other\'s\nmarks." To con'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def progress (atom :idle)) (reset! progress :` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':idle', ':running'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (def progress (atom :idle)) (reset! progress :` — character 'Riddle the crow' introduced twice within 200 chars — drop the second 'the crow'

### G9-03: Atom introduction

- examples: 3
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 3, 'CLAUSE_STACK_OVERFLOW': 6}
    - [LOW_GROUNDING] form=`(do (def a (atom 0)) (swap! a inc) @a)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 10)) (swap! a + 5) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (def a (atom 10)) (swap! a + 5) @a)` — character 'Buzz the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 10)) (swap! a + 5) @a)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees to that — no two crows scratch over each other\'s\nmarks." To con'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 10)) (swap! a + 5) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 10)) (swap! a + 5) @a)` — sentence with 6 commas reads as AI-output cadence: 'If two crows arrive at once, the runtime makes sure only one\nof us completes the'

### G9-04: Atom CAS semantics

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 5, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees to that — no two crows scratch over each other\'s\nmarks." To con'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 5 commas reads as AI-output cadence: 'The marks change only when someone scratches — and only as the\nruntime allows." '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (compare-and-set! a 0 1) @a)` — sentence with 5 commas reads as AI-output cadence: 'The marks change only when someone scratches — and only as the\nruntime allows." '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '99'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` — character 'Char the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 5)) (compare-and-set! a 0 99) @a)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees to that — no two crows scratch over each other\'s\nmarks." To con'

### G9-05: Watch on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 7 commas reads as AI-output cadence: 'The marks change only when someone scratches — and only as the\nruntime allows." '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 7 commas reads as AI-output cadence: 'The runtime sees to that — no two crows scratch over each other\'s\nmarks." To con'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':w',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (def log (atom [])) (add-watc` — sentence with 7 commas reads as AI-output cadence: 'The runtime sees to that — no two crows scratch over each other\'s\nmarks." To con'

### G9-06: Validator on atom

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, he composed\na'
    - [DOUBLE_NAME_INTRO] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — character 'Sable the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference, he composed\na'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (set-validator! a number?) (s` — sentence with 5 commas reads as AI-output cadence: 'validator on it, atomically swap by applying inc, and dereference,\nhe composed a'

### G9-07: Ref introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4, 'DOUBLE_PREP': 1, 'LOW_GROUNDING': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 0, perform a transactional alter by applying inc insi'
    - [DOUBLE_PREP] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — verb+preposition followed by {place} which already carries its own preposition
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('100', '7'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — sentence with 5 commas reads as AI-output cadence: 'To construct a ref holding 100, perform a transactional ref-set to 7 inside dosy'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 100)) (dosync (ref-set r 7)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('100', '7'), resolution doesn't close the loop)

### G9-08: dosync and alter

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 4, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 7 commas reads as AI-output cadence: 'If two crows arrive at once, the runtime makes sure only one\nof us completes the'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (ref 1)) (def b (ref 2)) (dosync (alter` — sentence with 6 commas reads as AI-output cadence: 'The marks change only when someone scratches — and only as the\nruntime allows." '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — character 'Trickster the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — sentence with 6 commas reads as AI-output cadence: 'If two crows arrive at once, the runtime makes sure only one\nof us completes the'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def r (ref 10)) (dosync (alter r + 5)) @r)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '5'), resolution doesn't close the loop)

### G9-09: Ref vs atom

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'LOW_GROUNDING': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding 0, atomically swap it by applying inc, and derefere'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'To construct an atom holding 0, atomically swap it by applying inc, and derefere'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def a (atom 0)) (swap! a inc) @a)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees to that — no two crows scratch over each other\'s\nmarks." To con'
    - [LOW_GROUNDING] form=`(do (def r (ref 0)) (dosync (alter r inc)) @r)` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G9-10: Agent introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 1, 'CLAUSE_STACK_OVERFLOW': 5, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [LOW_GROUNDING] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 6 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc to it, await its comple'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 9 commas reads as AI-output cadence: 'The count will be there when you signal for it —\nsometimes you have to wait for '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 8 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc to it, await its comple'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '10'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ag (agent 5)) (send ag + 10) (await ag) @` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '10'), resolution doesn't close the loop)

### G9-11: send and send-off

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 9 commas reads as AI-output cadence: 'The count will be there when you signal for it —\nsometimes you have to wait for '
    - [DOUBLE_NAME_INTRO] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — character 'Tempest the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (await ag) @a` — sentence with 8 commas reads as AI-output cadence: 'To construct an agent holding 0, use send to asynchronously apply inc, await its'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send-off ag inc) (await ag` — sentence with 8 commas reads as AI-output cadence: 'To construct an agent holding 0, use send-off to asynchronously apply inc, await'

### G9-12: await — synchronizing on agents

- examples: 1
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 8 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc twice, synchronize with'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 8 commas reads as AI-output cadence: 'The runtime makes that\neasier than it sounds." To construct an agent holding 0, '
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ag (agent 0)) (send ag inc) (send ag inc)` — sentence with 8 commas reads as AI-output cadence: 'To construct an agent holding 0, asynchronously send inc twice, synchronize with'

### G9-13: future introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`@(future (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`@(future (* 6 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '7'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`@(future (* 6 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '7'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`@(future (* 6 7))` — character 'Highwing the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [STORY_RESOLUTION_NO_DRAWN] form=`@(future (* 6 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6', '7'), resolution doesn't close the loop)

### G9-14: deref @ shorthand

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) @a)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (def a (atom 7)) @a)` — character 'Hush the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) (deref a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def a (atom 7)) (deref a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G9-15: promise — deliver and deref

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 4, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p :done) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':done',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 5 commas reads as AI-output cadence: 'The runtime makes that\neasier than it sounds." To construct a promise, deliver a'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p :done) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':done',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (def p (promise)) (deliver p :done) @p)` — character 'Whoop the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def p (promise)) (deliver p :done) @p)` — sentence with 5 commas reads as AI-output cadence: 'To construct a promise, deliver a completion keyword to it, and dereference to g'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def p (promise)) (deliver p :done) @p)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':done',), resolution doesn't close the loop)

### G9-16: volatile — when STM is too heavy

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [DOUBLE_NAME_INTRO] form=`(do (def v (volatile! 0)) (vswap! v inc) @v)` — character 'Coal the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '99'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '99'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def v (volatile! 5)) (vreset! v 99) @v)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5', '99'), resolution doesn't close the loop)

### G9-17: binding — thread-local

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 6, 'HIGH_LENGTH': 1, 'FORM_DISPLAY_AND_FORM_NOUN': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — character 'Parchment the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees to that — no two crows scratch over each other\'s\nmarks." To def'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — sentence with 5 commas reads as AI-output cadence: 'To define a dynamic var *p* as 1, use binding to rebind it to 99, and read its v'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('99', ':dynamic'), resolution doesn't close the loop)

### G9-18: locking — last resort

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 5, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_PREP': 2}
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [LOW_GROUNDING] form=`(do (def lock (Object.)) (locking lock (+ 1 2)))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (def lock (Object.)) (locking lock 42))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (def lock (Object.)) (locking lock 42))` — character 'Thermal the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(do (def lock (Object.)) (locking lock 42))` — sentence with 5 commas reads as AI-output cadence: 'The marks change only when someone scratches — and only as the\nruntime allows." '

## Grade 10

### G10-01: quote, unquote, unquote-splice

- examples: 3
- variety @ n=50: 1.00
- issues: {'FORM_DISPLAY_AND_FORM_NOUN': 1, 'LOW_GROUNDING': 1, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'DOUBLE_NAME_INTRO': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [FORM_DISPLAY_AND_FORM_NOUN] form=`(quote (+ 1 2))` — user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    - [LOW_GROUNDING] form=`(quote (+ 1 2))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three number' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`'(1 2 3)` — character 'Bicker the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three number' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`'(1 2 3)` — parametric example has hard-coded English numeral 'three number' in a story slot — the actual draws may differ from this fixed count

### G10-02: syntax-quote

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'THE_FORM_OVERUSE': 1, 'ONLY_SHOOK_HEAD_TIC': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 10] `(+ ~x ~x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 10] `(+ ~x ~x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [x 10] `(+ ~x ~x))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10',), resolution doesn't close the loop)
    - [THE_FORM_OVERUSE] form=`(let [x 10] `(+ ~x ~x))` — `the form` appears 5 times in user_msg (template tic — vary references)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [xs [1 2 3]] `(list ~@xs))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [ONLY_SHOOK_HEAD_TIC] form=`(let [xs [1 2 3]] `(list ~@xs))` — user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence

### G10-03: defmacro introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HIGH_LENGTH] form=`(do (defmacro my-when [t & body] `(if ~t (do ~@bod` — user_msg 221 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — character 'Buzz the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — sentence with 5 commas reads as AI-output cadence: 'A rule takes a\n*form* and makes a different *form* — only then does the runtime '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro twice [x] `(do ~x ~x)) (twice 7))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G10-04: Macro expansion rule

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(when true 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(or a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(or a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(macroexpand-1 '(or a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-1',), resolution doesn't close the loop)

### G10-06: when and when-not as macros

- examples: 3
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(when true 1 2 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(when true 1 2 3)` — sentence with 5 commas reads as AI-output cadence: 'You\nwrite the rule once, and any drop-order that calls it gets rewritten\non the '
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(when true 1 2 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(when true 1 2 3)` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when-not false :ok)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':ok',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(when-not false :ok)` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':ok',), resolution doesn't close the loop)

### G10-07: Threading macros revisited

- examples: 3
- variety @ n=50: 1.00
- issues: {'CONCEPT_AS_VERB': 2, 'NARRATIVE_NUMERAL_HARDCODE': 3, 'CLAUSE_STACK_OVERFLOW': 3, 'ANSWER_LEAK': 1, 'LOW_GROUNDING': 1}
    - [CONCEPT_AS_VERB] form=`(-> 5 inc inc inc)` — concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — parametric example has hard-coded English numeral 'four stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 7 commas reads as AI-output cadence: 'To thread a vector through filter, map, and reduce using thread-last, he compose'
    - [ANSWER_LEAK] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — answer 8 in narrative
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — parametric example has hard-coded English numeral 'four stones' in a story slot — the actual draws may differ from this fixed count
    - [CLAUSE_STACK_OVERFLOW] form=`(->> [1 2 3 4] (filter even?) (map inc) (reduce +)` — sentence with 5 commas reads as AI-output cadence: 'To thread a vector through filter, map, and reduce using thread-last, she scratc'

### G10-08: Macro vs fn

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 2, 'STORY_RESOLUTION_NO_DRAWN': 3}
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — sentence with 5 commas reads as AI-output cadence: 'You\nwrite the rule once, and any drop-order that calls it gets rewritten\non the '
    - [DOUBLE_NAME_INTRO] form=`(do (defn add-fn [a b] (+ a b)) (add-fn 3 4))` — character 'Trickster the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — character 'Trickster the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro add-mac [a b] `(+ ~a ~b)) (add-mac 3` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)

### G10-09: Hygiene and gensym

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'DOUBLE_NAME_INTRO': 2, 'CLAUSE_STACK_OVERFLOW': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('x_', 'x_'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('x_', 'x_'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — character 'Wingnight the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — sentence with 5 commas reads as AI-output cadence: 'You\nwrite the rule once, and any drop-order that calls it gets rewritten\non the '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('x_', 'x_'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(let [a (gensym "x_") b (gensym "x_")] (= a b))` — character 'Carbon the crow' introduced twice within 200 chars — drop the second 'the crow'

### G10-10: Anaphoric macros are confusing

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro safe-if-let [bind then else] `(if-le` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('5',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if-let [x 7] (* x x) 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(if-let [x 7] (* x x) 0)` — sentence with 5 commas reads as AI-output cadence: 'You\nwrite the rule once, and any drop-order that calls it gets rewritten\non the '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(if-let [x 7] (* x x) 0)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('7',), resolution doesn't close the loop)

### G10-11: Reader macros overview

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* % %) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* % %) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(#(* % %) 6)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('6',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(#(* % %) 6)` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 #_ 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`[1 #_ 2 3]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G10-12: Tagged literals

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 3}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inst? #inst "2024-01-01")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2024', '-01', '-01'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(inst? #inst "2024-01-01")` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inst? #inst "2024-01-01")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2024', '-01', '-01'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(inst? #inst "2024-01-01")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('2024', '-01', '-01'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(inst? #inst "2024-01-01")` — sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(uuid? #uuid "00000000-0000-0000-0000-000000000000` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('00000000', '-0000', '-0000'), resolution doesn't close the loop)

### G10-13: Data readers and EDN extension

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1, 'ONLY_SHOOK_HEAD_TIC': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "42")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', '42'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "[:a :b :c]")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b', ':c'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(clojure.edn/read-string "[:a :b :c]")` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':a', ':b', ':c'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(clojure.edn/read-string "[:a :b :c]")` — character 'Highwing the crow' introduced twice within 200 chars — drop the second 'the crow'

### G10-14: eval (the function)

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1}
    - [LOW_GROUNDING] form=`(eval '(+ 1 2 3))` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(eval '(+ 1 2 3))` — sentence with 5 commas reads as AI-output cadence: 'You\nwrite the rule once, and any drop-order that calls it gets rewritten\non the '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(eval '(+ 1 2 3))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(eval '(+ 1 2 3))` — character 'Hush the crow' introduced twice within 200 chars — drop the second 'the crow'

### G10-15: When not to write a macro

- examples: 2
- variety @ n=50: 1.00
- issues: {'NARRATIVE_NUMERAL_HARDCODE': 3, 'DOUBLE_NAME_INTRO': 2, 'CLAUSE_STACK_OVERFLOW': 1}
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do "prefer fn unless you must shape syntax" (map ` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(do "prefer fn unless you must shape syntax" (map ` — character 'Murmur the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(do "prefer fn unless you must shape syntax" (map ` — sentence with 5 commas reads as AI-output cadence: 'You\nwrite the rule once, and any drop-order that calls it gets rewritten\non the '
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do "prefer fn unless you must shape syntax" (map ` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [NARRATIVE_NUMERAL_HARDCODE] form=`(do "prefer fn unless you must shape syntax" (map ` — parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    - [DOUBLE_NAME_INTRO] form=`(do "prefer fn unless you must shape syntax" (map ` — character 'Squawk the crow' introduced twice within 200 chars — drop the second 'the crow'

### G10-16: Macro pattern library

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 2, 'LOW_GROUNDING': 1, 'PARAGRAPH_FRAGMENTATION': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — character 'Coal the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('42', ':slow-and-steady'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(do (defmacro with-tortoise-pace [& body] `(let [p` — sentence with 5 commas reads as AI-output cadence: 'You\nwrite the rule once, and any drop-order that calls it gets rewritten\non the '
    - [STORY_RESOLUTION_NO_DRAWN] form=`(do (defmacro def-pace [name v] `(def ~name ~v)) (` — story-tagged example's resolution slot has no drawn-value reference (form has literals (':slow',), resolution doesn't close the loop)

## Grade 11

### G11-01: JVM vs CLR vs JS vs Python (host overview)

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1, 'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — tortoise-hare-specific imagery 'leather notebook' leaks into crow-pitcher prose
    - [HEDGING_NEAR_FORM] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScr` — sentence with 5 commas reads as AI-output cadence: 'Featherdark the crow, patient as the water rose, walked to the slate and began t'

### G11-02: Method call syntax

- examples: 3
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 9, 'CLAUSE_STACK_OVERFLOW': 3, 'DOUBLE_NAME_INTRO': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(.toUpperCase "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(.toUpperCase "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(.toUpperCase "abc")` — sentence with 5 commas reads as AI-output cadence: 'Glint the crow, unhurried, form after form, found a different pitcher atop the h'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(.toUpperCase "abc")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(.startsWith "hare-tortoise" "hare")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('hare-tortoise', 'hare'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(.startsWith "hare-tortoise" "hare")` — sentence with 5 commas reads as AI-output cadence: "The runtime moves a stone across the boundary, calls\nthe human's method, and bri"

### G11-03: Static method call

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/abs -7)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('-7',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(Math/max 3 9)` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '9'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(Math/max 3 9)` — character 'Buzz the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(Math/max 3 9)` — sentence with 5 commas reads as AI-output cadence: "The runtime moves a stone across the boundary, calls\nthe human's method, and bri"

### G11-04: Field access

- examples: 2
- variety @ n=50: 1.00
- issues: {'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_NAME_INTRO': 1}
    - [CLAUSE_STACK_OVERFLOW] form=`(count "tortoise")` — sentence with 5 commas reads as AI-output cadence: "The runtime moves a stone across the boundary, calls\nthe human's method, and bri"
    - [DOUBLE_NAME_INTRO] form=`(count "tortoise")` — character 'Char the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(count "tortoise")` — sentence with 5 commas reads as AI-output cadence: "The runtime moves a stone across the boundary, calls\nthe human's method, and bri"

### G11-05: Import form

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "(:import (java.util Date)) imports a host cla` — tortoise-hare-specific imagery 'leather notebook' leaks into crow-pitcher prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do "import is a top-of-file ns clause" :studied)` — sentence with 5 commas reads as AI-output cadence: 'Indigo the crow, watching the level lift, drop by drop, had already written\nimpo'

### G11-06: new and dot-construct

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1, 'ANSWER_LEAK_STRING': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(String. "go")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('go',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(String. "go")` — sentence with 5 commas reads as AI-output cadence: 'Galena the crow, watching the level lift, drop by drop, found a different pitche'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(String. "go")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('go',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(String. "go")` — character 'Sable the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(String. "go")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('go',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(new String "jump")` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('jump',), resolution doesn't close the loop)

### G11-07: Arrays

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 2}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (int-array [10 20 30])] (aget a 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '20', '30'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (int-array [10 20 30])] (aget a 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '20', '30'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(let [a (int-array [10 20 30])] (aget a 1))` — sentence with 5 commas reads as AI-output cadence: 'Thermal the crow, watching the level lift, drop by drop, found a different pitch'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (int-array [10 20 30])] (aget a 1))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('10', '20', '30'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (int-array [1 2 3])] (alength a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [a (int-array [1 2 3])] (alength a))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G11-08: Type hints

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1, 'LOW_GROUNDING': 1, 'PROCEDURAL_OPENER': 1, 'METAPHOR_DISAPPEARS': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(let [^String s "abc"] (.toUpperCase s))` — sentence with 5 commas reads as AI-output cadence: 'Float the crow, trusting the process, stone after stone, found a different pitch'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(let [^String s "abc"] (.toUpperCase s))` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('abc',), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(do "type hints are metadata that guide compilatio` — character 'Mystery the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [LOW_GROUNDING] form=`(do "type hints are metadata that guide compilatio` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding

### G11-09: Checked vs unchecked math

- examples: 2
- variety @ n=50: 0.99
- issues: {'SENTENCE_START_LOWER_PRONOUN': 2}
    - [SENTENCE_START_LOWER_PRONOUN] form=`(+ 1 2)` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    - [SENTENCE_START_LOWER_PRONOUN] form=`(do "*unchecked-math* turns off overflow checking ` — pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation

### G11-11: cljs / JavaScript interop

- examples: 2
- variety @ n=50: 1.00
- issues: {'META_FILLER_RESOLUTION': 1}
    - [META_FILLER_RESOLUTION] form=`(do "(js/console.log x) calls a JS global; (.-foo ` — user_msg uses generic 'returned exactly' / 'settled with certainty' filler — describe what actually came back, not just that something did

### G11-12: Basilisp overview (Python host)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1}
    - [HEDGING_NEAR_FORM] form=`(do "basilisp is a Clojure-like Lisp implemented o` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "basilisp is a Clojure-like Lisp implemented o` — sentence with 5 commas reads as AI-output cadence: 'Trill the crow, steady in the stone-by-stone approach, walked to the slate and b'
    - [DOUBLE_NAME_INTRO] form=`(do "basilisp interops with Python via the same do` — character 'Quill the crow' introduced twice within 200 chars — drop the second 'the crow'

### G11-13: Cross-platform .cljc and reader-conditionals

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(do "#?(:clj … :cljs …) selects a form per host at` — character 'Tempestcaw the crow' introduced twice within 200 chars — drop the second 'the crow'

### G11-14: Debugging host leaks

- examples: 2
- variety @ n=50: 1.00
- issues: {'LOW_GROUNDING': 2, 'PROCEDURAL_OPENER': 2, 'METAPHOR_DISAPPEARS': 2, 'DOUBLE_NAME_INTRO': 3, 'STORY_RESOLUTION_NO_DRAWN': 3, 'CLAUSE_STACK_OVERFLOW': 1}
    - [LOW_GROUNDING] form=`(do "host stack traces leak through interop; learn` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PROCEDURAL_OPENER] form=`(do "host stack traces leak through interop; learn` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    - [METAPHOR_DISAPPEARS] form=`(do "host stack traces leak through interop; learn` — user_msg has none of the fable's primary metaphor nouns (pitcher, water, pebble, stone...)
    - [DOUBLE_NAME_INTRO] form=`(do "host stack traces leak through interop; learn` — character 'Squall the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [LOW_GROUNDING] form=`(do "host stack traces leak through interop; learn` — user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    - [PROCEDURAL_OPENER] form=`(do "host stack traces leak through interop; learn` — user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence

## Grade 12

### G12-01: Transducers introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (map inc) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To use the map-inc transducer with into to increment the vector containing 1, 2,'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (filter even?) [1 2 3 4 5])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', '5'), resolution doesn't close the loop)
    - [DOUBLE_NAME_INTRO] form=`(into [] (filter even?) [1 2 3 4 5])` — character 'Twilight the crow' introduced twice within 200 chars — drop the second 'the crow'

### G12-02: Transducer composition

- examples: 2
- variety @ n=50: 1.00
- issues: {'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 5, 'DOUBLE_NAME_INTRO': 1}
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — sentence with 8 commas reads as AI-output cadence: 'Ash the crow shook\nhis head and went on with the work: to\ncompose map-inc and fi'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4'), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(into [] (comp (map inc) (filter even?)) [1 2 3 4]` — sentence with 5 commas reads as AI-output cadence: 'Puzzle the crow, trusting the process, stone after stone, held two decision-rule'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(transduce (comp (map inc) (filter even?)) + 0 [1 ` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '4', '5'), resolution doesn't close the loop)

### G12-03: into with a transducer (xform)

- examples: 2
- variety @ n=50: 1.00
- issues: {'HIGH_LENGTH': 1, 'STORY_RESOLUTION_NO_DRAWN': 6, 'CLAUSE_STACK_OVERFLOW': 2, 'DOUBLE_NAME_INTRO': 1}
    - [HIGH_LENGTH] form=`(into #{} (map inc) [1 2 3])` — user_msg 206 words
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(into #{} (map inc) [1 2 3])` — sentence with 5 commas reads as AI-output cadence: 'To use the map-inc transducer with into to create a set from the incremented ele'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)
    - [CLAUSE_STACK_OVERFLOW] form=`(into #{} (map inc) [1 2 3])` — sentence with 6 commas reads as AI-output cadence: 'Cowl the crow shook\nhis head and went on with the work: to\nuse the map-inc trans'
    - [STORY_RESOLUTION_NO_DRAWN] form=`(into #{} (map inc) [1 2 3])` — story-tagged example's resolution slot has no drawn-value reference (form has literals ('3',), resolution doesn't close the loop)

### G12-04: core.async introduction

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "(chan), (go ...), (<! ...), (>! ...) form the` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "(chan), (go ...), (<! ...), (>! ...) form the` — sentence with 5 commas reads as AI-output cadence: 'Vane the crow, patient as the water rose, walked to the slate and began to\nwrite'

### G12-05: Channels and pipelines

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1, 'CLAUSE_STACK_OVERFLOW': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "pipe, mult, mix, pipeline-async route values ` — tortoise-hare-specific imagery 'leather notebook' leaks into crow-pitcher prose
    - [CLAUSE_STACK_OVERFLOW] form=`(do "pipe, mult, mix, pipeline-async route values ` — sentence with 6 commas reads as AI-output cadence: 'Halfway through the race, Azure the crow, preening at the thought of knowing, st'
    - [CLAUSE_STACK_OVERFLOW] form=`(do "pipelines transform streams of values channel` — sentence with 5 commas reads as AI-output cadence: 'Indigo the crow, watching the level lift, drop by drop, had already written\nthe '

### G12-06: clojure.spec

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1, 'DOUBLE_NAME_INTRO': 1, 'HEDGING_NEAR_FORM': 2}
    - [FOREIGN_FABLE_IMAGERY] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — tortoise-hare-specific imagery 'leather notebook' leaks into crow-pitcher prose
    - [DOUBLE_NAME_INTRO] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — character 'Sable the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [HEDGING_NEAR_FORM] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [HEDGING_NEAR_FORM] form=`(do (require '[clojure.spec.alpha :as s]) (s/valid` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G12-07: Spec generators

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [HEDGING_NEAR_FORM] form=`(do "s/exercise produces sample inputs for a spec"` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "s/exercise produces sample inputs for a spec"` — sentence with 6 commas reads as AI-output cadence: 'Yawp the crow, deliberate, unhurried by the rising sun, walked to the slate and '

### G12-09: Test fixtures

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1}
    - [DOUBLE_NAME_INTRO] form=`(do "fixtures provide setup/teardown around deftes` — character 'Gust the crow' introduced twice within 200 chars — drop the second 'the crow'

### G12-11: Leiningen project.clj

- examples: 2
- variety @ n=50: 1.00
- issues: {'META_FILLER_RESOLUTION': 1}
    - [META_FILLER_RESOLUTION] form=`(do "project.clj declares :dependencies, :main, :p` — user_msg uses generic 'returned exactly' / 'settled with certainty' filler — describe what actually came back, not just that something did

### G12-12: deps.edn projects

- examples: 2
- variety @ n=50: 1.00
- issues: {'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1, 'DOUBLE_NAME_INTRO': 1}
    - [HEDGING_NEAR_FORM] form=`(do "deps.edn declares :deps and :aliases for the ` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "deps.edn declares :deps and :aliases for the ` — sentence with 5 commas reads as AI-output cadence: 'Trill the crow, steady in the stone-by-stone approach, walked to the slate and b'
    - [DOUBLE_NAME_INTRO] form=`(do "deps.edn is read by the official `clj`/`cloju` — character 'Quill the crow' introduced twice within 200 chars — drop the second 'the crow'

### G12-13: Aliases and tools

- examples: 2
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [DOUBLE_NAME_INTRO] form=`(do "`clj -M:test` runs the :test alias from deps.` — character 'Tempestcaw the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [CLAUSE_STACK_OVERFLOW] form=`(do "aliases compose extra paths, deps, and main o` — sentence with 5 commas reads as AI-output cadence: 'Halfway through the race, Nightshade the crow, with a confident tilt of the head'

### G12-15: Datomic / XTDB (datalog db brief)

- examples: 2
- variety @ n=50: 1.00
- issues: {'META_FILLER_RESOLUTION': 1, 'CLAUSE_STACK_OVERFLOW': 3, 'DOUBLE_NAME_INTRO': 1, 'HEDGING_NEAR_FORM': 2}
    - [META_FILLER_RESOLUTION] form=`(do "Datomic and XTDB are immutable, time-aware da` — user_msg uses generic 'returned exactly' / 'settled with certainty' filler — describe what actually came back, not just that something did
    - [CLAUSE_STACK_OVERFLOW] form=`(do "Datomic and XTDB are immutable, time-aware da` — sentence with 5 commas reads as AI-output cadence: 'Banking the crow, letting the count rise on its own, had already written\nthe fam'
    - [DOUBLE_NAME_INTRO] form=`(do "queries are written in datalog over EDN-shape` — character 'Murmur the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [HEDGING_NEAR_FORM] form=`(do "queries are written in datalog over EDN-shape` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "queries are written in datalog over EDN-shape` — sentence with 5 commas reads as AI-output cadence: 'Cloudlark the crow, dropping each stone with careful attention, walked to the sl'
    - [HEDGING_NEAR_FORM] form=`(do "queries are written in datalog over EDN-shape` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value

### G12-17: Library design patterns

- examples: 3
- variety @ n=50: 1.00
- issues: {'DOUBLE_NAME_INTRO': 1, 'HEDGING_NEAR_FORM': 1, 'CLAUSE_STACK_OVERFLOW': 1}
    - [DOUBLE_NAME_INTRO] form=`(do "small public API surface, plain data inputs, ` — character 'Glyph the crow' introduced twice within 200 chars — drop the second 'the crow'
    - [HEDGING_NEAR_FORM] form=`(do "small public API surface, plain data inputs, ` — hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    - [CLAUSE_STACK_OVERFLOW] form=`(do "small public API surface, plain data inputs, ` — sentence with 5 commas reads as AI-output cadence: 'Gust the crow, calm and methodical, walked to the slate and began to\nwrite the m'

### G12-18: Clojure style guide

- examples: 2
- variety @ n=50: 1.00
- issues: {'FOREIGN_FABLE_IMAGERY': 1}
    - [FOREIGN_FABLE_IMAGERY] form=`(do "kebab-case names, two-space indent, threading` — tortoise-hare-specific imagery 'leather notebook' leaks into crow-pitcher prose

---

## Summary

### Issue counts (across all examples × 3 records)

- **STORY_RESOLUTION_NO_DRAWN**: 372
- **CLAUSE_STACK_OVERFLOW**: 263
- **DOUBLE_NAME_INTRO**: 221
- **NARRATIVE_NUMERAL_HARDCODE**: 213
- **LOW_GROUNDING**: 68
- **SENTENCE_START_LOWER_PRONOUN**: 34
- **CONCEPT_AS_VERB**: 29
- **FORM_DISPLAY_AND_FORM_NOUN**: 18
- **PARAGRAPH_FRAGMENTATION**: 15
- **ONLY_SHOOK_HEAD_TIC**: 14
- **PARAMETRIC_LITERAL_NUMERALS**: 12
- **HEDGING_NEAR_FORM**: 11
- **THE_FORM_OVERUSE**: 8
- **ANSWER_LEAK**: 7
- **ANSWER_LEAK_STRING**: 7
- **STRING_AS_CHAR_MISCLAIM**: 6
- **HIGH_LENGTH**: 6
- **BOOL_LEAK_RESOLUTION**: 6
- **FOREIGN_FABLE_IMAGERY**: 6
- **REPEATED_OPENER_FRAGMENT**: 4
- **EXPECTED_META_PHRASE**: 3
- **DOUBLE_PREP**: 3
- **PROCEDURAL_OPENER**: 3
- **METAPHOR_DISAPPEARS**: 3
- **META_FILLER_RESOLUTION**: 3
- **BAD_PLACE_PREP**: 2
- **FORM_LEAK**: 1

### Per-grade summary

| Grade | Subjects | Examples | Issues | Low-variety |
|---|---|---|---|---|
| 1 | 18 | 76 | 112 | — |
| 2 | 22 | 88 | 225 | — |
| 3 | 18 | 31 | 101 | — |
| 4 | 20 | 39 | 74 | — |
| 5 | 22 | 39 | 133 | — |
| 6 | 16 | 33 | 64 | — |
| 7 | 18 | 36 | 113 | — |
| 8 | 16 | 31 | 119 | — |
| 9 | 18 | 34 | 142 | — |
| 10 | 16 | 36 | 121 | — |
| 11 | 14 | 29 | 75 | — |
| 12 | 18 | 37 | 59 | — |

### Sample issues by severity

#### FORM_DISPLAY_AND_FORM_NOUN

- `G1-01` (form `"hello"`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    It had been a long, dry summer, and the rivers had pulled back from their banks in a slow and patient retreat.

A small audience of meadow birds had perched on the rim of a tall
pitcher in the garden to watch Soothe the crow attempt to outwit
Pinion the crow at reading the REPL. The day was hot, the...
    ```
- `G1-01` (form `nil`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    Drought has its own quiet way of teaching the difference between thirst and the right answer to thirst.

A small audience of meadow birds had perched on the rim of a tall
pitcher near the garden to watch Brand the crow attempt to outwit
Windrider the crow at reading the REPL. The day was hot, the wa...
    ```
- `G1-02` (form `12345`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    The farmstead had stored what it could, but the heat was honest and the water was patient with no one.

A small audience of meadow birds had perched on the rim of a tall
pitcher near the meadow to watch Pipe the crow attempt to outwit
Malachite the crow at reading the REPL. The day was hot, the wate...
    ```
- `G1-05` (form `true`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    It had been a long, dry summer, and the rivers had pulled back from their banks in a slow and patient retreat.

A small audience of meadow birds had perched on the rim of a tall
pitcher near the garden to watch Dusk the crow attempt to outwit
Emblem the crow at reading the REPL. The day was hot, the...
    ```
- `G1-05` (form `true`): user_msg places `<form>` adjacent to a 'the form ...' noun-phrase reference within 120 chars — template tic that doubles the form reference (vary the second mention)
    ```
    On the rim of a long-shadowed pitcher, a thirsty bird considered what it had and what it lacked.

A small audience of meadow birds had perched on the rim of a tall
pitcher at the market to watch Cobalt the crow attempt to outwit
Cackle the crow at reading the REPL. The day was hot, the water
inside ...
    ```

#### DOUBLE_NAME_INTRO

- `G1-02` (form `12345`): character 'Loft the crow' introduced twice within 200 chars — drop the second 'the crow'
    ```
    The drought had reached even near the farm, and Loft the crow flew in slow circles searching for water.

Sly the crow and Loft the crow stopped at the farm where someone had
scratched the integer 9007199254740992 into the dust beside a tall pitcher. The day
was hot, the throat of the pitcher was nar...
    ```
- `G1-03` (form `(- 1 1/3)`): character 'Drift the crow' introduced twice within 200 chars — drop the second 'the crow'
    ```
    by the meadow, a single pitcher held the last of the water, and Drift the crow arrived too parched to be picky.

Shadow the crow and Drift the crow stopped by the meadow where someone had
scratched the form (- 1 1/3) into the dust beside a tall pitcher. The day
was hot, the throat of the pitcher was...
    ```
- `G1-04` (form `"slow and steady"`): character 'Tempestcaw the crow' introduced twice within 200 chars — drop the second 'the crow'
    ```
    In a long-dry season, Tempestcaw the crow found the pitcher by the farm and began to consider it carefully.

Tempestcaw the crow had been trying to teach Mirk the crow how the REPL
works. The day was hot and the water in the nearby pitcher far below
the narrow rim — a fitting backdrop for a lesson a...
    ```
- `G1-05` (form `(> 3 5)`): character 'Brand the crow' introduced twice within 200 chars — drop the second 'the crow'
    ```
    Brand the crow alighted on the rim of a jar at the farm and peered down at the small dark gleam below.

Brand the crow, steady in the stone-by-stone approach, had been keeping a small leather
notebook of every form he had successfully evaluated —
each page like a pebble in the pitcher's growing pile...
    ```
- `G1-06` (form `nil`): character 'Sable the crow' introduced twice within 200 chars — drop the second 'the crow'
    ```
    at the market, a single pitcher held the last of the water, and Sable the crow arrived too parched to be picky.

Sable the crow had been trying to teach Parchment the crow how the REPL
works. The day was hot and the water in the nearby pitcher far below
the narrow rim — a fitting backdrop for a less...
    ```

#### REPEATED_OPENER_FRAGMENT

- `G1-07` (form `(= :hare :hare)`): opener fragment 'at the edge of the orchard' also appears later in user_msg
    ```
    The orchard at the edge of the orchard had grown quiet in the heat, and Plume the crow was the only sound at midday.

Whisperer the crow chalked a wager on a smooth round pebble at the edge of the orchard: whoever
predicted the result of `(= :wolf :wolf)` would drop his pebble
in the pitcher first. ...
    ```
- `G2-05` (form `(mod 17 5)`): opener fragment 'at the edge of the hilltop' also appears later in user_msg
    ```
    Glint the crow was no fool, and at the edge of the hilltop the day demanded thinking rather than complaining.

Glint the crow, letting the count rise on its own, arranged a small heap of smooth
stones at the edge of the hilltop, careful with the count. The day was hot and the
water was low; the heap...
    ```
- `G2-15` (form `(if "" 1 0)`): opener fragment 'the pitcher near the orchard' also appears later in user_msg
    ```
    Word had it that Mount had flown over three valleys before finding the pitcher near the orchard.

Mutter the crow swooped toward the pitcher near the orchard, with a confident tilt of the head, certain
the gate would swing open. Mount the crow watched: the only way to know
which way the gate swings ...
    ```
- `G7-07` (form `(do (assert (= 1 1)) 1)`): opener fragment 'the pitcher near the farm' also appears later in user_msg
    ```
    Word had it that Thermal had flown over three valleys before finding the pitcher near the farm.

Thermal the crow, watching the level lift, drop by drop, spread a patch of soft moss beneath
the pitcher near the farm — the day was hot, the throat was narrow, and any
pebble flung wrong without a cushi...
    ```

#### STRING_AS_CHAR_MISCLAIM

- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    It had been a long, dry summer, and the rivers had pulled back from their banks in a slow and patient retreat.

At the foot of a tall pitcher at the edge of the orchard, Cloudshroud the crow sketched a small
wager into the dry dust: whoever guessed the result of `"feather"`
first would claim the coo...
    ```
- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    by the meadow, where the orchard meets the well, an old clay pitcher had stood for as long as anyone could remember.

Halfway to the pitcher, Quirk the crow, preening at the thought of knowing, stopped at the edge of the meadow
and refused to take another step until someone could prove what the
form...
    ```
- `G1-08` (form `\space`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    Some problems cannot be hurried; they only respond to the slow addition of small things.

At the foot of a tall pitcher on the farm, Pitch the crow sketched a small
wager into the dry dust: whoever guessed the result of `"feather"`
first would claim the cool water lying low at the bottom. The throat...
    ```
- `G1-08` (form `\T`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    Buzz the crow arrived near the garden with no plan but a sharp eye and a willingness to take small steps.

Buzz the crow had been trying to teach Sigil the crow how the REPL
works. The day was hot and the water in the nearby pitcher far below
the narrow rim — a fitting backdrop for a lesson about pa...
    ```
- `G1-08` (form `\T`): form is a multi-character string but the prose refers to it as a single character (`the character \X` idiom)
    ```
    in the village, where the heat shimmered above the stones, Inkwell the crow began the slow business of solving thirst.

Inkwell the crow, patient as the water rose, had been keeping a small leather
notebook of every form he had successfully evaluated —
each page like a pebble in the pitcher's growin...
    ```

#### ONLY_SHOOK_HEAD_TIC

- `G1-09` (form `(symbol? 'hare)`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    On the rim of a long-shadowed pitcher, a thirsty bird considered what it had and what it lacked.

Parchment the crow, with a confident tilt of the head, mistook the chalk mark on the stone
for the stone itself. "It says crow, so the value must be the
crow!" Soar the crow only shook her head: the
mar...
    ```
- `G1-11` (form `(+    1    2)`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    There was once a Crow who had flown a great distance and found nothing in any pond worth dipping a beak.

Cloudshroud the crow, head tilted confidently to one side, glanced at the pitcher-notations and
called out what she thought they would do without paying
attention to the conventions of how they ...
    ```
- `G1-12` (form `(* (+ 1 2) 3)`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    Umbra the crow arrived on the road with no plan but a sharp eye and a willingness to take small steps.

Jet the crow, with a self-satisfied beak-click, glanced at the pitcher-notations and
called out what he thought they would do without paying
attention to the conventions of how they were scratched...
    ```
- `G1-12` (form `(* (+ 1 2) 3)`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    Cobalt the crow arrived at the edge of the hilltop with no plan but a sharp eye and a willingness to take small steps.

Cipherwing the crow, with a self-satisfied beak-click, glanced at the pitcher-notations and
called out what he thought they would do without paying
attention to the conventions of ...
    ```
- `G1-17` (form `42`): user_msg uses 'only shook his/her head' — recurring AI-fable filler cadence
    ```
    In a long-dry season, Parchment the crow found the pitcher by the garden and began to consider it carefully.

Cloudshroud the crow, ruffling up with certainty, glanced at the pitcher-notations and
called out what he thought they would do without paying
attention to the conventions of how they were s...
    ```

#### CLAUSE_STACK_OVERFLOW

- `G1-09` (form `(= 'hare 'hare)`): sentence with 5 commas reads as AI-output cadence: "Quoting tells the runtime: don't evaluate this, just hand\nit back as the shape i"
    ```
    The drought had reached even along the road, and Pipe the crow flew in slow circles searching for water.

"To talk about the form itself rather than evaluating it,"
Pipe the crow, calm and methodical, said, "you mark the form with chalk in front.
Quoting tells the runtime: don't evaluate this, just ...
    ```
- `G1-10` (form `42 ;; the answer`): sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    ```
    Stormcaw circled twice at the market before settling on the rim of the old clay jar, eyes on the water below.

"A form is what's actually there on the pitcher's clay,"
Stormcaw the crow, letting the count rise on its own, said, "after the conventions of writing and
reading have done their work. The ...
    ```
- `G1-10` (form `42 ;; the answer`): sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    ```
    There was a pitcher and there was a thirst, and between them lay a question that asked for thought rather than force.

"A form is what's actually there on the pitcher's clay,"
Circle the crow, watching the level lift, drop by drop, said, "after the conventions of writing and
reading have done their ...
    ```
- `G1-11` (form `(+
  1
  2)`): sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

"A form is what's actually there on the pitcher's clay,"
Nightshade the crow, dropping each stone with careful attention, said, "after the conventions of writing and
reading have done their work. The run...
    ```
- `G1-12` (form `(+ 2 3)`): sentence with 5 commas reads as AI-output cadence: 'The runtime sees the cleaned-up form,\nevaluates it, and gives back what it compu'
    ```
    at the edge of the meadow, where the orchard meets the well, an old clay pitcher had stood for as long as anyone could remember.

"A form is what's actually there on the pitcher's clay,"
Trill the crow, steady in the stone-by-stone approach, said, "after the conventions of writing and
reading have d...
    ```

#### EXPECTED_META_PHRASE

- `G1-11` (form `(+    1    2)`): user_msg uses 'the expected X' meta-language — describes the answer in graders'-vocabulary instead of letting the runtime's return speak for itself
    ```
    Whistle circled twice on the farm before settling on the rim of the old clay jar, eyes on the water below.

Korvus scratched a stone-drop form on the market pitcher's clay, pressing extra gaps between each token — wide spaces separating the operator from both stone-counts on the rim.

He needed to c...
    ```
- `G1-18` (form `(+ 1 2)`): user_msg uses 'the expected X' meta-language — describes the answer in graders'-vocabulary instead of letting the runtime's return speak for itself
    ```
    It was the kind of summer that turned every shaded stone into a small kindness.

Sable spread a patch of soft moss on the ground beneath the garden pitcher before dropping any stone — a safety pad in place, ready to catch any mis-drop without harm.

Sable needed to confirm that a well-formed stone-d...
    ```
- `G3-09` (form `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))`): user_msg uses 'the expected X' meta-language — describes the answer in graders'-vocabulary instead of letting the runtime's return speak for itself
    ```
    A row of pebbles lay at the foot of the wall, sun-warmed, unremarkable, and just heavy enough.

Sable pressed add3 into the village pitcher's rim alongside a three-slot recipe: accept a, b, c, then sum them — carved deep and permanent.

Sable wanted to call add3 with one, two, three and watch the wa...
    ```

#### NARRATIVE_NUMERAL_HARDCODE

- `G1-13` (form `(- 5 3)`): parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    ```
    It was by the meadow, in the long heat of late summer, that a thirsty bird met a stubborn vessel.

"Watch the heap," Chrysocolla the crow, deliberate, unhurried by the rising sun, said, gesturing at a small
mound of smooth stones. "Every operation either adds more stones,
takes some away, or combine...
    ```
- `G1-13` (form `(- 5 3)`): parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    ```
    It had been a long, dry summer, and the rivers had pulled back from their banks in a slow and patient retreat.

Caw stood at the farm pitcher's rim with five smooth stones in one talon and lifted three away, setting them aside on the ground before dropping the remainder into the water.

She needed t...
    ```
- `G1-13` (form `(- 5 3)`): parametric example has hard-coded English numeral 'three stones' in a story slot — the actual draws may differ from this fixed count
    ```
    An old pitcher of glazed clay sat by the garden wall, half-empty and entirely useless to anyone too proud to think.

Whirlwind the crow, dropping each stone with careful attention, laid smooth stones out on the ground
by the meadow, sorting them into small heaps by how many drops each would
take. Th...
    ```
- `G1-13` (form `(* 4 5)`): parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    ```
    Wheel had flown all morning in the orchard without finding so much as a damp leaf to rest a beak against.

"Whatever the heap looks like after the operation,"
Wheel the crow, watching the level lift, drop by drop, said, "the runtime gives the exact count —
small or large, fraction or whole, the answ...
    ```
- `G1-13` (form `(* 4 5)`): parametric example has hard-coded English numeral 'five stones' in a story slot — the actual draws may differ from this fixed count
    ```
    Word had it that Drone had flown over three valleys before finding the pitcher atop the hilltop.

"Whatever the heap looks like after the operation,"
Drone the crow, deliberate, unhurried by the rising sun, said, "the runtime gives the exact count —
small or large, fraction or whole, the answer is p...
    ```

#### SENTENCE_START_LOWER_PRONOUN

- `G1-13` (form `(+ 7 8)`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    It was near the hilltop, in the long heat of late summer, that a thirsty bird met a stubborn vessel.

Swoop the crow eyed the heap, preening at the thought of knowing, and called out a guess
about how many stones could be dropped before the water rose high
enough, without bothering to count. Malachi...
    ```
- `G1-13` (form `(+ 7 8)`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    In a long-dry season, Scholar the crow found the pitcher on the road and began to consider it carefully.

Riddle the crow eyed the heap, ruffling up with certainty, and called out a guess
about how many stones could be dropped before the water rose high
enough, without bothering to count. Scholar th...
    ```
- `G1-13` (form `(+ 7 8)`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    On a long afternoon when even the bees had grown slow, a thirsty bird settled on the rim of a clay vessel.

Soothe the crow eyed the heap, with a self-satisfied beak-click, and called out a guess
about how many stones could be dropped before the water rose high
enough, without bothering to count. Ri...
    ```
- `G1-14` (form `(+ (* 2 3) (* 4 5))`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    On the rim of a long-shadowed pitcher, a thirsty bird considered what it had and what it lacked.

Vane the crow eyed the heap, head tilted confidently to one side, and called out a guess
about how many stones could be dropped before the water rose high
enough, without bothering to count. Pitch the c...
    ```
- `G1-14` (form `(+ (* 2 3) (* 4 5))`): pronoun starts a sentence in lowercase — template should use the _cap variant after a sentence-ending punctuation
    ```
    It had been a long, dry summer, and the rivers had pulled back from their banks in a slow and patient retreat.

Eddy the crow eyed the heap, head tilted confidently to one side, and called out a guess
about how many stones could be dropped before the water rose high
enough, without bothering to coun...
    ```

#### PARAGRAPH_FRAGMENTATION

- `G1-13` (form `(- 20 7)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    Dimsky the crow alighted on the rim of a jar by the farm and peered down at the small dark gleam below.

Korvus counted twenty smooth stones piled on the road-side pitcher's rim, then moved seven to one side, studying the smaller heap that remained before submitting the form.

He needed the runtime ...
    ```
- `G1-13` (form `(- 20 7)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    When the cisterns ran shallow, even the cleverest creatures had to learn the patience of small additions.

Korvus counted twenty smooth stones piled on the road-side pitcher's rim, then moved seven to one side, studying the smaller heap that remained before submitting the form.

He needed the runtim...
    ```
- `G2-05` (form `(rem 17 5)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    Some problems cannot be hurried; they only respond to the slow addition of small things.

Sable had seventeen acorns at the village and pouches of five. After filling as many pouches as possible she wanted to know how many acorns spilled out as the leftover.

She needed the exact leftover count afte...
    ```
- `G2-06` (form `(inc 0)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    The orchard at the edge of the garden had grown quiet in the heat, and Stoop the crow was the only sound at midday.

Sable stood at the empty road pitcher with no stones inside. She held a single stone in her talon and wanted to know the new count after her first drop.

She needed the count after dr...
    ```
- `G2-06` (form `(inc -1)`): user_msg has 4 short (≤25-word) paragraphs in body — reads as a bullet list, not a story
    ```
    Sharp had flown all morning in the meadow without finding so much as a damp leaf to rest a beak against.

Caw had a deficit of one at the village pitcher — one below empty. She added a single stone and wanted to know whether the count climbed back to zero.

She needed to know whether adding one ston...
    ```

#### CONCEPT_AS_VERB

- `G1-15` (form `(= 1 1)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    near the road, where the orchard meets the well, an old clay pitcher had stood for as long as anyone could remember.

"You can't tell which way the gate will swing by guessing,"
Banking the crow, steady in the stone-by-stone approach, said. "You bring the form to the gate, the runtime
checks it, and...
    ```
- `G1-15` (form `(= :hare :hare)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    It was the kind of summer that turned every shaded stone into a small kindness.

"You can't tell which way the gate will swing by guessing,"
Smoke the crow, letting the count rise on its own, said. "You bring the form to the gate, the runtime
checks it, and the gate gives the only answer that matter...
    ```
- `G1-15` (form `(= :hare :hare)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    Soot the crow alighted on the rim of a jar along the road and peered down at the small dark gleam below.

"You can't tell which way the gate will swing by guessing,"
Soot the crow, unhurried, form after form, said. "You bring the form to the gate, the runtime
checks it, and the gate gives the only a...
    ```
- `G1-15` (form `(= :hare :tortoise)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    The kitchen garden had been lovingly kept, but the sun that year had been merciless and constant.

"You can't tell which way the gate will swing by guessing,"
Loft the crow, trusting the process, stone after stone, said. "You bring the form to the gate, the runtime
checks it, and the gate gives the ...
    ```
- `G1-15` (form `(= :hare :tortoise)`): concept_phrase substituted into a finite-verb slot (e.g. 'must calling X', 'I applying Y')
    ```
    The water sat at the bottom of the jar, deep enough to glimpse and far enough to tantalize.

"You can't tell which way the gate will swing by guessing,"
Currents the crow, deliberate, unhurried by the rising sun, said. "You bring the form to the gate, the runtime
checks it, and the gate gives the on...
    ```

#### LOW_GROUNDING

- `G1-15` (form `(= 1 1)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    Thermal the crow arrived near the road with no plan but a sharp eye and a willingness to take small steps.

Caw held two unmarked stones up at the pitcher's mouth in the village, one in each talon, both carrying the count 0. She set them side by side at the dual-gate check.

Only if both gate-arms c...
    ```
- `G2-10` (form `(* 2 2 2)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    The kitchen garden had been lovingly kept, but the sun that year had been merciless and constant.

Korvus scratched three tallies of two into the pitcher's rim at the farm, stacking each layer on the product of the last. He wanted the final compounded count from three doublings.

He needed the resul...
    ```
- `G2-13` (form `(and true true)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    On the rim of a long-shadowed pitcher, a thirsty bird considered what it had and what it lacked.

Korvus stood at the pitcher's mouth on the road, two gate-arms stretched across it. Both arms were raised open. He needed to know whether the path through both gates was clear.

He needed the final verd...
    ```
- `G2-13` (form `(and true true)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    In a year when the wells ran low, a single jar of water was a small kingdom unto itself.

Korvus stood at the pitcher's mouth on the road, two gate-arms stretched across it. Both arms were raised open. He needed to know whether the path through both gates was clear.

He needed the final verdict only...
    ```
- `G2-14` (form `(not true)`): user_msg lacks both a form-literal anchor and an EMO-pool phrase — no environmental grounding
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

Caw found the gate-arm above the pitcher fully raised open at the meadow. She wanted to know what the pitcher said about the opposite of that state — the gate flipped.

She needed the inverted reading: i...
    ```

#### STORY_RESOLUTION_NO_DRAWN

- `G2-08` (form `(+ 1/2 1/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    ```
    When Float landed by the garden wall, she saw the water and saw the distance, and stood very still.

Float the crow, trusting the process, stone after stone, laid smooth stones out on the ground
at the village, sorting them into small heaps by how many drops each would
take. The water sat low in the...
    ```
- `G2-08` (form `(+ 1/2 1/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    ```
    It was the kind of summer that turned every shaded stone into a small kindness.

"Watch the heap," Obsidian the crow, patient as the water rose, said, gesturing at a small
mound of smooth stones. "Every operation either adds more stones,
takes some away, or combines what's already there — the heap g...
    ```
- `G2-08` (form `(+ 1/2 1/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('4',), resolution doesn't close the loop)
    ```
    The farmstead had stored what it could, but the heat was honest and the water was patient with no one.

Buffet the crow, trusting the process, stone after stone, arranged a small heap of smooth
stones at the edge of the meadow, careful with the count. The day was hot and the
water was low; the heap ...
    ```
- `G2-08` (form `(* 2/3 3/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '4'), resolution doesn't close the loop)
    ```
    The drought had reached even atop the hilltop, and Trickster the crow flew in slow circles searching for water.

Trickster the crow, dropping each stone with careful attention, arranged a small heap of smooth
stones at the edge of the hilltop, careful with the count. The day was hot and the
water wa...
    ```
- `G2-08` (form `(* 2/3 3/4)`): story-tagged example's resolution slot has no drawn-value reference (form has literals ('3', '3', '4'), resolution doesn't close the loop)
    ```
    Yawp the crow alighted on the rim of a jar near the orchard and peered down at the small dark gleam below.

Yawp the crow, patient as the water rose, laid smooth stones out on the ground
near the orchard, sorting them into small heaps by how many drops each would
take. The water sat low in the pitch...
    ```

#### ANSWER_LEAK

- `G2-19` (form `(+ 99999999999 1)`): answer 100000000000 in narrative
    ```
    The orchard at the farm had grown quiet in the heat, and Cipher the crow was the only sound at midday.

Gale the crow eyed the heap, with a self-satisfied beak-click, and called out a guess
about how many stones could be dropped before the water rose high
enough, without bothering to count. Cipher t...
    ```
- `G3-04` (form `(let [a 2 b 3 c 4] (+ a b c))`): answer 9 in narrative
    ```
    On a long afternoon when even the bees had grown slow, a thirsty bird settled on the rim of a clay vessel.

"Watch the wing carefully," Drift the crow said near the market.
"While the form's stretch runs, the wing is closed and
the binding is safe." To bind a to 5, b to 9, c to 9, and add them, she
...
    ```
- `G3-04` (form `(let [a 2 b 3 c 4] (+ a b c))`): answer 9 in narrative
    ```
    A row of pebbles lay at the foot of the wall, sun-warmed, unremarkable, and just heavy enough.

Sage the crow, unhurried, form after form, patted the feathers of one wing.
"Whatever I tuck under a wing is in force only while the form runs,"
she said, "and only for the form that names the binding.
Th...
    ```
- `G3-09` (form `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))`): answer 6 in narrative
    ```
    It was the kind of summer that turned every shaded stone into a small kindness.

Cunning the crow, trusting the process, stone after stone, held up a smooth stone and scratched
a step-by-step sequence into the pitcher's clay rim. "Drop-orders in
Clojure are like this," she said: "the smooth stones g...
    ```
- `G5-22` (form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n)`): answer 120 in narrative
    ```
    near the village, where the heat shimmered above the stones, Buffet the crow began the slow business of solving thirst.

Caw stood at the pitcher's rim in the hilltop field, a circuit chalked beneath her feet: start with n=5 and accumulator=1. Each lap, multiply the accumulator by n, step n down by ...
    ```

#### HIGH_LENGTH

- `G3-03` (form `(let [x 3] (+ x 1))`): user_msg 212 words
    ```
    Vane circled twice at the farm before settling on the rim of the old clay jar, eyes on the water below.

Korvus arrived at the tall clay pitcher in the orchard, three smooth stones from the morning's count in mind. Before dropping any, he tucked the count of three under his left wing, close and name...
    ```
- `G3-03` (form `(let [x 3] (+ x 1))`): user_msg 210 words
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

Korvus arrived at the tall clay pitcher in the orchard, three smooth stones from the morning's count in mind. Before dropping any, he tucked the count of three under his left wing, close and named: x, ho...
    ```
- `G3-18` (form `(let [n 5] (* n n n))`): user_msg 201 words
    ```
    It was the kind of summer that turned every shaded stone into a small kindness.

Sable tucked five stones under one wing at the village pitcher, naming the count n, then used that one tucked count three times in the body — multiplying n by itself twice over without re-stating the count.

Sable neede...
    ```
- `G9-17` (form `(do (def ^:dynamic *p* 1) (binding [*p* 99] *p*) *p*)`): user_msg 203 words
    ```
    The kitchen garden had been lovingly kept, but the sun that year had been merciless and constant.

Korvus chalked `1` on the pitcher's rim at the garden. Inside an alcove he re-chalked it to `99`, but when he stepped back out of the alcove the local chalk faded and the global mark of `1` reappeared ...
    ```
- `G10-03` (form `(do (defmacro my-when [t & body] `(if ~t (do ~@body))) (my-w`): user_msg 221 words
    ```
    Vane circled twice at the farm before settling on the rim of the old clay jar, eyes on the water below.

Caw scratched a master revision rule on the pitcher's rim at the village: `my-when` — whenever this pattern appeared in a form, the talon would rewrite it before the REPL ever saw the body. The r...
    ```

#### THE_FORM_OVERUSE

- `G3-03` (form `(let [n 10] (* n n))`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    by the farm, where the orchard meets the well, an old clay pitcher had stood for as long as anyone could remember.

Crosswind the crow, calm and methodical, patted the feathers of one wing.
"Whatever I tuck under a wing is in force only while the form runs,"
she said, "and only for the form that nam...
    ```
- `G3-03` (form `(let [a 5] a)`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    On a long afternoon when even the bees had grown slow, a thirsty bird settled on the rim of a clay vessel.

Quickwit the crow, steady in the stone-by-stone approach, patted the feathers of one wing.
"Whatever I tuck under a wing is in force only while the form runs,"
she said, "and only for the form...
    ```
- `G3-03` (form `(let [a 5] a)`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    The orchard at the edge of the hilltop had grown quiet in the heat, and Shout the crow was the only sound at midday.

Shout the crow, steady in the stone-by-stone approach, patted the feathers of one wing.
"Whatever I tuck under a wing is in force only while the form runs,"
she said, "and only for t...
    ```
- `G3-04` (form `(let [a 2 b 3 c 4] (+ a b c))`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    A row of pebbles lay at the foot of the wall, sun-warmed, unremarkable, and just heavy enough.

Sage the crow, unhurried, form after form, patted the feathers of one wing.
"Whatever I tuck under a wing is in force only while the form runs,"
she said, "and only for the form that names the binding.
Th...
    ```
- `G3-06` (form `(let [a 3 b (+ a 1) c (* b 2)] c)`): `the form` appears 5 times in user_msg (template tic — vary references)
    ```
    Sigil the crow arrived near the hilltop with no plan but a sharp eye and a willingness to take small steps.

Sigil the crow, steady in the stone-by-stone approach, patted the feathers of one wing.
"Whatever I tuck under a wing is in force only while the form runs,"
she said, "and only for the form t...
    ```

#### PARAMETRIC_LITERAL_NUMERALS

- `G3-09` (form `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    It was the kind of summer that turned every shaded stone into a small kindness.

Cunning the crow, trusting the process, stone after stone, held up a smooth stone and scratched
a step-by-step sequence into the pitcher's clay rim. "Drop-orders in
Clojure are like this," she said: "the smooth stones g...
    ```
- `G3-09` (form `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

"A drop-order is only useful when followed," Folio the crow, dropping each stone with careful attention, said,
holding up the scratched rim. "You scratch the steps, you bring the
stones, the pitcher rais...
    ```
- `G3-09` (form `(do (defn add3 [a b c] (+ a b c)) (add3 1 2 3))`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    A row of pebbles lay at the foot of the wall, sun-warmed, unremarkable, and just heavy enough.

Sable pressed add3 into the village pitcher's rim alongside a three-slot recipe: accept a, b, c, then sum them — carved deep and permanent.

Sable wanted to call add3 with one, two, three and watch the wa...
    ```
- `G4-05` (form `(cons 0 '(1 2 3))`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    There was a pitcher and there was a thirst, and between them lay a question that asked for thought rather than force.

A line of smooth stones had been arranged in the orchard, each one resting
against the next — first at the front, the rest in order behind.
"Many of our stone-piles are like this pr...
    ```
- `G4-05` (form `(cons 0 '(1 2 3))`): parametric example has enumerated English numerals (one, two, three, …) hard-coded in a story slot — won't track the actual draws that {form_template} produces
    ```
    The kitchen garden had been lovingly kept, but the sun that year had been merciless and constant.

Pitch the crow, steady in the stone-by-stone approach, pointed to a pile of smooth stones
gathered on the pitcher's rim in the orchard. The stones were heavy — one
at a time was the only way. "Whatever...
    ```

#### FORM_LEAK

- `G3-18` (form `(* 5 5 5)`): form '(* 5 5 5)' appears in user_msg of a goal-style subject
    ```
    When the cisterns ran shallow, even the cleverest creatures had to learn the patience of small additions.

Korvus dropped three literal stone-counts of five into the garden pitcher all at once — no wing tucked, no name carved — just three fives fed directly to the multiplication as plain inline valu...
    ```

#### BOOL_LEAK_RESOLUTION

- `G4-12` (form `(contains? #{1 2 3} 4)`): resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    ```
    A row of pebbles lay at the foot of the wall, sun-warmed, unremarkable, and just heavy enough.

Sable held a stone marked four near the same three-stone sorting-pile at the farm pitcher. No groove was carved for four; she asked whether it belonged.

She needed a definitive answer before adding the s...
    ```
- `G4-14` (form `(empty? [1])`): resolution leaks boolean answer 'false' — describe the verdict abstractly instead
    ```
    The orchard by the garden had grown quiet in the heat, and Jet the crow was the only sound at midday.

Sable spotted a vector-pile on the meadow pitcher with a single stone inside — just one pebble, no more. She asked `empty?` whether the pile held nothing.

She needed the REPL to distinguish a trul...
    ```
- `G4-18` (form `(= [1 2 3] '(1 2 3))`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    It was the kind of summer that turned every shaded stone into a small kindness.

Caw laid a three-stone vector-pile beside a three-stone chain at the road pitcher — same stones, same order, different container shapes. She wondered if `=` would agree.

She needed `=` to compare the contents of both c...
    ```
- `G4-18` (form `(= [1 2 3] '(1 2 3))`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    It was the kind of summer that turned every shaded stone into a small kindness.

Caw laid a three-stone vector-pile beside a three-stone chain at the road pitcher — same stones, same order, different container shapes. She wondered if `=` would agree.

She needed `=` to compare the contents of both c...
    ```
- `G6-07` (form `(boolean (:private (meta '^:private hidden)))`): resolution leaks boolean answer 'true' — describe the verdict abstractly instead
    ```
    Witty circled twice near the hilltop before settling on the rim of the old clay jar, eyes on the water below.

Korvus carved a symbol onto the pitcher's rim in the orchard and pressed a small private mark into the margin beside it. He then tested whether the mark read as a firm yes when converted to...
    ```

#### ANSWER_LEAK_STRING

- `G5-03` (form `(when true :yes)`): answer string ':yes' appears in user_msg
    ```
    Vane circled twice at the farm before settling on the rim of the old clay jar, eyes on the water below.

Korvus examined the meadow pitcher's single-branch fork: one stone marked :yes sat poised above the opening. No second branch existed — only the one guarded by `when`.

He needed to know whether ...
    ```
- `G5-03` (form `(when true :yes)`): answer string ':yes' appears in user_msg
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

Korvus examined the meadow pitcher's single-branch fork: one stone marked :yes sat poised above the opening. No second branch existed — only the one guarded by `when`.

He needed to know whether the lone...
    ```
- `G5-07` (form `(or nil false :found)`): answer string ':found' appears in user_msg
    ```
    A row of pebbles lay at the foot of the wall, sun-warmed, unremarkable, and just heavy enough.

Caw examined the village pitcher's open-gate rail, three stones lined up: nil, false, then :found. The gate would release the first stone that proved truthy.

She needed to know which stone would be the f...
    ```
- `G6-01` (form `(name 'foo.bar)`): answer string 'foo.bar' appears in user_msg
    ```
    In a year when the wells ran low, a single jar of water was a small kingdom unto itself.

Korvus perched at the pitcher's clay rim in the garden and studied the name carved into the side: a dotted path, two segments pressed into the clay. He wanted to read it as a plain string, not a symbol.

He nee...
    ```
- `G7-11` (form `(try (throw (ex-info "trouble" {})) (catch Exception e (.get`): answer string 'trouble' appears in user_msg
    ```
    A row of pebbles lay at the foot of the wall, sun-warmed, unremarkable, and just heavy enough.

Onyxwing the crow, steady in the stone-by-stone approach, spread a patch of soft moss beneath
the pitcher at the market — the day was hot, the throat was narrow, and any
pebble flung wrong without a cushi...
    ```

#### BAD_PLACE_PREP

- `G5-22` (form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n)`): 'in the hilltop' (wrong preposition)
    ```
    near the village, where the heat shimmered above the stones, Buffet the crow began the slow business of solving thirst.

Caw stood at the pitcher's rim in the hilltop field, a circuit chalked beneath her feet: start with n=5 and accumulator=1. Each lap, multiply the accumulator by n, step n down by ...
    ```
- `G5-22` (form `(loop [n 5 acc 1] (if (zero? n) acc (recur (dec n) (* acc n)`): 'in the hilltop' (wrong preposition)
    ```
    On a long afternoon when even the bees had grown slow, a thirsty bird settled on the rim of a clay vessel.

Caw stood at the pitcher's rim in the hilltop field, a circuit chalked beneath her feet: start with n=5 and accumulator=1. Each lap, multiply the accumulator by n, step n down by one — loop wi...
    ```

#### FOREIGN_FABLE_IMAGERY

- `G6-10` (form `(:deps {:deps {:a 1 :b 2}})`): tortoise-hare-specific imagery 'leather notebook' leaks into crow-pitcher prose
    ```
    An old pitcher of glazed clay sat by the garden wall, half-empty and entirely useless to anyone too proud to think.

Realgar the crow, unhurried, form after form, kept a small leather notebook of
every goal she had translated into a Clojure form —
each entry a pebble's worth of progress, the ledger'...
    ```
- `G11-01` (form `(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Pytho`): tortoise-hare-specific imagery 'leather notebook' leaks into crow-pitcher prose
    ```
    Some problems cannot be hurried; they only respond to the slow addition of small things.

Pirouette the crow, trusting the process, stone after stone, kept a small leather notebook of
every goal she had translated into a Clojure form —
each entry a pebble's worth of progress, the ledger's page-count...
    ```
- `G11-05` (form `(do "(:import (java.util Date)) imports a host class" :impor`): tortoise-hare-specific imagery 'leather notebook' leaks into crow-pitcher prose
    ```
    There was a pitcher and there was a thirst, and between them lay a question that asked for thought rather than force.

Tailwind the crow, watching the level lift, drop by drop, kept a small leather notebook of
every goal he had translated into a Clojure form —
each entry a pebble's worth of progress...
    ```
- `G12-05` (form `(do "pipe, mult, mix, pipeline-async route values across cha`): tortoise-hare-specific imagery 'leather notebook' leaks into crow-pitcher prose
    ```
    There was a pitcher and there was a thirst, and between them lay a question that asked for thought rather than force.

Tailwind the crow, watching the level lift, drop by drop, kept a small leather notebook of
every goal he had translated into a Clojure form —
each entry a pebble's worth of progress...
    ```
- `G12-06` (form `(do (require '[clojure.spec.alpha :as s]) (s/valid? int? 42)`): tortoise-hare-specific imagery 'leather notebook' leaks into crow-pitcher prose
    ```
    at the market, a single pitcher held the last of the water, and Sable the crow arrived too parched to be picky.

Sable the crow, calm and methodical, kept a small leather notebook of
every goal he had translated into a Clojure form —
each entry a pebble's worth of progress, the ledger's page-count
r...
    ```

#### HEDGING_NEAR_FORM

- `G6-11` (form `(count ["src" "test" "resources"])`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    Some problems cannot be hurried; they only respond to the slow addition of small things.

The wager was set by the garden: produce the value before the breeze had
turned the next leaf. The day was hot and the pitcher's water lay
low; a wrong guess wasted the breeze and the whole pebble both.
Enigma ...
    ```
- `G11-01` (form `(do "JVM: Clojure; CLR: ClojureCLR; JS: ClojureScript; Pytho`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    The farmstead had stored what it could, but the heat was honest and the water was patient with no one.

The wager was set near the meadow: produce the value before the breeze had
turned the next leaf. The day was hot and the pitcher's water lay
low; a wrong guess wasted the breeze and the whole pebb...
    ```
- `G11-12` (form `(do "basilisp is a Clojure-like Lisp implemented on Python" `): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    at the edge of the meadow, where the orchard meets the well, an old clay pitcher had stood for as long as anyone could remember.

The wager was set at the edge of the meadow: produce the value before the breeze had
turned the next leaf. The day was hot and the pitcher's water lay
low; a wrong guess ...
    ```
- `G12-04` (form `(do "(chan), (go ...), (<! ...), (>! ...) form the core.asyn`): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    When the cisterns ran shallow, even the cleverest creatures had to learn the patience of small additions.

The wager was set at the edge of the meadow: produce the value before the breeze had
turned the next leaf. The day was hot and the pitcher's water lay
low; a wrong guess wasted the breeze and t...
    ```
- `G12-06` (form `(do (require '[clojure.spec.alpha :as s]) (s/valid? string? `): hedge 'or something close to it' in user_msg — eval-deterministic narratives shouldn't hedge about the form's value
    ```
    Gale the crow alighted on the rim of a jar near the farm and peered down at the small dark gleam below.

The wager was set on the farm: produce the value before the breeze had
turned the next leaf. The day was hot and the pitcher's water lay
low; a wrong guess wasted the breeze and the whole pebble ...
    ```

#### DOUBLE_PREP

- `G9-07` (form `(do (def r (ref 0)) (dosync (alter r inc)) @r)`): verb+preposition followed by {place} which already carries its own preposition
    ```
    Witty circled twice near the hilltop before settling on the rim of the old clay jar, eyes on the water below.

Caw placed a zero-mark in a sealed safe-box beside the pitcher at the garden. To change the mark she had to open the safe-box in one atomic transaction, nudge the tally up by one, and seal ...
    ```
- `G9-18` (form `(do (def lock (Object.)) (locking lock 42))`): verb+preposition followed by {place} which already carries its own preposition
    ```
    Cluck the crow was no fool, and at the edge of the garden the day demanded thinking rather than complaining.

Korvus planted a gate-stone at the pitcher's mouth on the road. He rolled it aside, placed a single stone tally inside the sealed section, then rolled the gate back — the tally was the body'...
    ```
- `G9-18` (form `(do (def lock (Object.)) (locking lock 42))`): verb+preposition followed by {place} which already carries its own preposition
    ```
    Coal the crow arrived at the farm with no plan but a sharp eye and a willingness to take small steps.

Korvus planted a gate-stone at the pitcher's mouth on the road. He rolled it aside, placed a single stone tally inside the sealed section, then rolled the gate back — the tally was the body's only ...
    ```

#### PROCEDURAL_OPENER

- `G11-08` (form `(do "type hints are metadata that guide compilation" :studie`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

To understand that type hints guide compilation, she composed the purpose of type hints in Clojure and submitted the form. The REPL — calling into the earthenware vessel the human had fired — returned:

...
    ```
- `G11-14` (form `(do "host stack traces leak through interop; learn to read t`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

To learn to read and debug host runtime errors, he composed debugging host-runtime errors and submitted the form. The REPL — calling into the earthenware vessel the human had fired — returned:

Question:...
    ```
- `G11-14` (form `(do "host stack traces leak through interop; learn to read t`): user_msg jumps from fable-opener directly to 'To {goal}, [pronoun] composed ...' without a scene-setting sentence
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

To learn to read and debug host runtime errors, she composed debugging host-runtime errors and submitted the form. The REPL — calling into the earthenware vessel the human had fired — returned:

What Clo...
    ```

#### METAPHOR_DISAPPEARS

- `G11-08` (form `(do "type hints are metadata that guide compilation" :studie`): user_msg has none of the fable's primary metaphor nouns (pitcher, water, pebble, stone...)
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

To understand that type hints guide compilation, she composed the purpose of type hints in Clojure and submitted the form. The REPL — calling into the earthenware vessel the human had fired — returned:

...
    ```
- `G11-14` (form `(do "host stack traces leak through interop; learn to read t`): user_msg has none of the fable's primary metaphor nouns (pitcher, water, pebble, stone...)
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

To learn to read and debug host runtime errors, he composed debugging host-runtime errors and submitted the form. The REPL — calling into the earthenware vessel the human had fired — returned:

Question:...
    ```
- `G11-14` (form `(do "host stack traces leak through interop; learn to read t`): user_msg has none of the fable's primary metaphor nouns (pitcher, water, pebble, stone...)
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

To learn to read and debug host runtime errors, she composed debugging host-runtime errors and submitted the form. The REPL — calling into the earthenware vessel the human had fired — returned:

What Clo...
    ```

#### META_FILLER_RESOLUTION

- `G11-11` (form `(do "(js/console.log x) calls a JS global; (.-foo o) reads a`): user_msg uses generic 'returned exactly' / 'settled with certainty' filler — describe what actually came back, not just that something did
    ```
    Drought has its own quiet way of teaching the difference between thirst and the right answer to thirst.

"There is no challenge here," Smoulder the crow said, ruffling up with certainty.
"Anyone could understand how ClojureScript calls JavaScript globals and reads fields without thinking." Umbra the...
    ```
- `G12-11` (form `(do "project.clj declares :dependencies, :main, :profiles fo`): user_msg uses generic 'returned exactly' / 'settled with certainty' filler — describe what actually came back, not just that something did
    ```
    Drought has its own quiet way of teaching the difference between thirst and the right answer to thirst.

"There is no challenge here," Smoulder the crow said, ruffling up with certainty.
"Anyone could study the project.clj file and how it declares dependencies, main entry points, and profiles for Le...
    ```
- `G12-15` (form `(do "Datomic and XTDB are immutable, time-aware datalog DBs"`): user_msg uses generic 'returned exactly' / 'settled with certainty' filler — describe what actually came back, not just that something did
    ```
    The orchard had not seen a real rain in weeks, and even the lavender stood with its head bowed.

"You always insist on writing it out," Foxy the crow complained,
ruffling up with certainty. "I can see the answer from here." Cawlick the crow
shook his head slowly. "To study Datomic and XTDB as immuta...
    ```

